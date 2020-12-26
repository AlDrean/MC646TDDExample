
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
        self.recentlist_limit = 5
        self.block = 0

    def list_files(self):
        self.file_List = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        print (self.file_List)

    def open_file(self,numFile):
        #no refactoring needed;
        self.selectFile = numFile
        f = open(self.directory+self.file_List[self.selectFile], "r")
        
        print ("[OPENNING FILE] -[{}] {}".format(self.selectFile,self.directory+self.file_List[self.selectFile]))
        self.file_content = f.read()
        f.close()

        self.recentList_add(self.selectFile,self.file_List[self.selectFile])

        return self.file_content

    def recentList_add(self,num,name):
        if self.block: return 0

        if len(self.file_recents) >= self.recentlist_limit:
            self.file_recents=self.file_recents[:-1]
            self.file_recents_num=self.file_recents_num[:-1]


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
        print ("Recent files list_num: \n {}".format(self.file_recents_num))
        print ("********************************************")
    
    def lockRecentList(self):
        print ("********************************************")
        print ("blocking recent list")
    
        print ("********************************************")
    
        self.block =1

    def unLockRecentList(self):
        
        print ("********************************************")
        print ("unblocking recent list")
    
        print ("********************************************")
    
        self.block =0


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
        self.Program.recentlist_limit = 10
        self.Program.list_files()
        self.Program.open_file(1)
        self.Program.open_file(2)
        self.Program.open_file(3)
        self.Program.open_file(4)
        self.Program.open_file(5)
        self.Program.open_file(6)
        self.Program.open_file(7)
        self.Program.open_file(8)
        self.Program.open_file(9)
        self.Program.open_file(10)
        self.Program.lockRecentList()
        self.Program.open_file(11)
        self.Program.open_file(12)
        self.Program.open_file(13)
        self.Program.open_file(14)
        self.Program.open_file(15)

        self.Program.unLockRecentList()
        self.Program.open_file(16)
        self.Program.open_file(17)
        
        self.Program.recentList_print()




        


    

        


    




directory = 'files/'
x = Program(directory)
test_class = test(x)
##print att
test_class.test_recentList_add()
