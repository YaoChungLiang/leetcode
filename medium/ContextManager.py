## contect manager using self define class
class My_Open_File():
    def __init__(self,filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file =open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        
with My_Open_File('../Data.txt','w') as f:
    f.write('Hello Ann, this is my first time trying context manager')

print(f.closed)


## context manager using decorator
from contextlib import contextmanager

@contextmanager
def my_open_file(file, mode):
    try:
        f = open(file, mode)
        yield f   ## run in __enter__
    finally:
        f.close() ## run in __exit__
    
with my_open_file("../Data.txt",'w') as f:
    f.write('Hello Ann, this is my second time trying context manager')
print(f.closed)

import os
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
        
with change_dir('..'):
    print(os.listdir())