import ctypes
import json
import platform
#from . import EXIF
import os
from datetime import datetime

class Alpr():
    def __init__(self, country, config_file, runtime_dir):

        # Load the .dll for Windows and the .so for Unix-based
        if platform.system().lower().find("windows") != -1:
            self._openalprpy_lib = ctypes.cdll.LoadLibrary("openalprpy.dll")
        elif platform.system().lower().find("darwin") != -1:
            self._openalprpy_lib = ctypes.cdll.LoadLibrary("libopenalprpy.dylib")
        else:
            self._openalprpy_lib = ctypes.cdll.LoadLibrary("libopenalprpy.so")


        self._initialize_func = self._openalprpy_lib.initialize
        self._initialize_func.restype = ctypes.c_void_p
        self._initialize_func.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]

        self._dispose_func = self._openalprpy_lib.dispose
        self._dispose_func.argtypes = [ctypes.c_void_p]

        self._is_loaded_func = self._openalprpy_lib.isLoaded
        self._is_loaded_func.argtypes = [ctypes.c_void_p]
        self._is_loaded_func.restype = ctypes.c_bool

        self._recognize_file_func = self._openalprpy_lib.recognizeFile
        self._recognize_file_func.restype = ctypes.c_void_p
        self._recognize_file_func.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

        self._recognize_array_func = self._openalprpy_lib.recognizeArray
        self._recognize_array_func.restype = ctypes.c_void_p
        self._recognize_array_func.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint]

        self._free_json_mem_func = self._openalprpy_lib.freeJsonMem


        self._set_default_region_func = self._openalprpy_lib.setDefaultRegion
        self._set_default_region_func.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

        self._set_detect_region_func = self._openalprpy_lib.setDetectRegion
        self._set_detect_region_func.argtypes = [ctypes.c_void_p, ctypes.c_bool]


        self._set_top_n_func = self._openalprpy_lib.setTopN
        self._set_top_n_func.argtypes = [ctypes.c_void_p, ctypes.c_int]

        self._get_version_func = self._openalprpy_lib.getVersion
        self._get_version_func.argtypes = [ctypes.c_void_p]
        self._get_version_func.restype = ctypes.c_void_p

        self.alpr_pointer = self._initialize_func(country, config_file, runtime_dir)


    def unload(self):
        self._openalprpy_lib.dispose(self.alpr_pointer)

    def is_loaded(self):
        return self._is_loaded_func(self.alpr_pointer)

    def recognize_file(self, file_path):
        ptr = self._recognize_file_func(self.alpr_pointer, file_path)
        json_data = ctypes.cast(ptr, ctypes.c_char_p).value
        response_obj = json.loads(json_data)
        self._free_json_mem_func(ctypes.c_void_p(ptr))

        return response_obj

    def recognize_array(self, byte_array):

        pb = ctypes.cast(byte_array, ctypes.POINTER(ctypes.c_ubyte))
        ptr = self._recognize_array_func(self.alpr_pointer, pb, len(byte_array))
        json_data = ctypes.cast(ptr, ctypes.c_char_p).value
        response_obj = json.loads(json_data.decode())
        self._free_json_mem_func(ctypes.c_void_p(ptr))

        return response_obj

    def get_version(self):

        ptr = self._get_version_func(self.alpr_pointer)
        version_number = ctypes.cast(ptr, ctypes.c_char_p).value
        self._free_json_mem_func(ctypes.c_void_p(ptr))

        return version_number

    def set_top_n(self, topn):
        self._set_top_n_func(self.alpr_pointer, topn)

    def set_default_region(self, region):
        self._set_default_region_func(self.alpr_pointer, region)

    def set_detect_region(self, enabled):
        self._set_detect_region_func(self.alpr_pointer, enabled)

def get_plate_num(img_content):
    alpr = None
    try:
        alpr = Alpr(b"us", b"f:/openalpr.conf", b"f:/runtime_data")
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
            print("Using OpenALPR " + (alpr.get_version()).decode('utf-8'))
            alpr.set_top_n(1)
            alpr.set_default_region(b"wa")
            alpr.set_detect_region(False)
            #img_name = input("Enter the image's name: ")
            #Get the time stamp of create
            """
            print(datetime.fromtimestamp(os.path.getctime(img_name)))
            print(datetime.fromtimestamp(os.path.getmtime(img_name)))
            """
            jpeg_bytes = open(img_content, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)
            return results['results'][0]['candidates'][0]['plate']
            #print("Image size: %dx%d" %(results['img_width'], results['img_height']))
            #print("Processing Time: %f" % results['processing_time_ms'])
            """
            i = 0
            for plate in results['results']:
                i += 1
                #print("Plate #%d" % i)
                #print("   %12s %12s" % ("Plate", "Confidence"))
                for candidate in plate['candidates']:
                    prefix = "-"
                    if candidate['matches_template']:
                        prefix = "*"

                    #print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
            """
    finally:
        if alpr:
            alpr.unload()

if __name__ == "__main__":
    main()
