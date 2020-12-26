
from os import listdir
from os.path import isfile, join

class Program:

    def __init__(self, directory):
        self.directory = directory
        self.file_List = []

    def list_files(self):
        self.file_List = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        print (self.file_List)
        

class test():
    def __init__(self,program):
        self.files_directory = 'files/'
        self.Program = program

    def test_listFiles(self):
        #Class for testing if listing all the files in the default directory;
        self.Program.list_files()

    




directory = 'files/'
x = Program(directory)
test_class = test(x)

x.list_files()
    