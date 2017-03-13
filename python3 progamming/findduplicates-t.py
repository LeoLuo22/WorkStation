# -*- coding:utf-8 -*-

import queue
import collections
import os
import threading

def main():
    opts, path = parse_options()
    data = collections.defaultdict(list)
    for root, dirs, files in os.walk(path):
        for filename in files:
            fullname = os.path.join(root, filename)
            try:
                key = (os.path.getsize(fullname), filename)
            except EnvironmentError:
                continue
            if key[0] == 0:
                continue
            data[key].append(fullname)

    work_queue = queue.PriorityQueue()
    results_queue = queue.Queue()
    md5_from_filename = {}
    for i in range(opts.count):
        number = "{0}: ".format(i + 1) if opts.debug else ""
        worker = Worker(work_queue, md5_from_filename, results_queue, number)
        worker.daemon = True
        worker.start()

    results_thread = threading.Thread(target=lambda: print_results(results_queue))
    results_thread.daemon = True
    results_thread.start()

    for size, filename in sorted(data):
        names = data[size, filename]
        if len(names) > 1:
            work_queue.put((size, names))
    work_queue.join()
    results_queue.join()

def print_results(results_queue):
    while  True:
        try:
            results = results_queue.get()
            if results:
                print(results)
        finally:
            results_queue.task_done()

class Worker(threading.Thread):

    Md5_lock = threading.Lock()

    def __init__(self, work_queue, md5_from_filename, results_queue, number):
        super().__init__()
        self.work_queue = work_queue
        self.md5_from_filename = md5_from_filename
        self.results_queue = results_queue
        self.number = number

    def run(self):
        while  True:
            try:
                size, names = self.work_queue.get()
                self.process(size, names)
            finally:
                self.work_queue.task_done()

    def process(self, size, filenames):
        md5s = collections.defaultdict(set)
        for filename in filenames:
            with self.Md5_lock:
                md5 = self.md5_from_filename.get(filename, None)
            if md5 is not None:
                md5s[md5].add(filename)
            else:
                try:
                    md5 = hashlib.md5()
                    with open(filename, "rb") as fh:
                        md5.update(fh.read())
                    md5 = md5.digest()
                    md5s[md5].add(filename)
                    with self.Md5_lock:
                        self.md5_from_filename[filename] = md5
                except EnvironmentError:
                    continue
        for filenames in md5.values():
            if len(filenames) == 1:
                continue
            self.results_queue.put("{0}Duplicate files ({1 : n} bytes):""\n\t{2}".format(self.number, size, "\n\t".join(sorted(filenames))))

if __name__ == "__main__":
    main()
