
from os import listdir
from os.path import isfile, join

class Program:

    def __init__(self, directory):
        self.directory = directory
        self.file_List = []
        self.selectFile = -1
        self.file_content = ""
        self.file_recents = []
        self.file_recents_num = []

    def list_files(self):
        self.file_List = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        print (self.file_List)

    def open_file(self,numFile):
        #no refactoring needed;
        self.selectFile = numFile
        f = open(self.directory+self.file_List[self.selectFile], "r")
        
        print ("[OPENNING FILE] - {}".format(self.directory+self.file_List[self.selectFile]))
        self.file_content = f.read()
        f.close()

        self.recentList_add(self.selectFile,self.file_List[self.selectFile])

        return self.file_content

    def recentList_add(self,num,name):
        if name in self.file_recents:
            self.file_recents.remove(name)
            self.file_recents.insert(0,name)

            self.file_recents_num.remove(num)
            self.file_recents_num.insert(0,name)
        else:
            self.file_recents.insert(0,name)
            self.file_recents_num.insert(0,num)
        


    def recentList_print(self):
        print ("********************************************")
        print ("Recent files list: \n {}".format(self.file_recents))
        print ("********************************************")
    
        
  #  def recentList_add(self)




class test():
    def __init__(self,program):
        self.files_directory = 'files/'
        self.Program = program

    def test_listFiles(self):
        #Class for testing if listing all the files in the default directory;
        self.Program.list_files()
        #assert equal listing

    def test_openFile(self,selectedfile):
        self.selectFile = selectedfile
        f = self.Program.open_file(self.selectFile)
        print ("[File] - {}".format(self.Program.file_List[self.selectFile]))
        print (f)


    def test_recetListInit(self):
        #should be empty
        self.Program.recentList_print()

    def test_recentList_add(self):
        #esperada saida dos noems dos arquivos com o primeiro primeiro sendo o 5;
        self.Program.list_files()
        self.Program.open_file(5)
        self.Program.open_file(6)
        self.Program.open_file(7)
        self.Program.open_file(8)
        self.Program.open_file(5)
        self.Program.recentList_print()


        


    

        


    




directory = 'files/'
x = Program(directory)
test_class = test(x)
##print att
test_class.test_recentList_add()
