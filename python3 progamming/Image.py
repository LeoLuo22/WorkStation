import os
import pickle

class ImageError(Exception): pass
class CoodinateError(ImageError): pass
class NoFilenameError(ImageError):pass
class SaveError(ImageError):pass
class LoadError(ImageError):pass

class Image:
    def __init__(self, width, height, filename="", background="#FFFFFF"):
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def background(self):
        return self._background

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def colors(self):
        return set(self._colors)

    def __getitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if(not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoodinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)

    def __setitem__(self, coordinate, color):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoodinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)

    def __delitem__(self, coordinate):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"
        if (not (0 <= coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoodinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()
        fh = None
        try:
            data = [self.width, self.height, self.__background,self.__data]
            fh = open(self.filename, 'wb')
            pickle.dump(data,fh,pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None

        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background, self.__data) = data
            self.__colors = (set(self.__data.values()) | {self.__background})
        except (EnvironmentError,pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def export(self, filename):
        if filename.lower().endswith(".xpm"):
            self.__export__xpm(filename)
        else:
            raise ExportError("unsupported export format: " + os.path.splitext(filename[1]))

    def resize(self, width=None, height=None):
        if width == None:
            width = self.width
        if height == None:
            height = self.height
        if width == None and height == None:
            return False
        if width < self.width and height < self.height:


