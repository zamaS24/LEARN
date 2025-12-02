'''
-> curr_dir = os.getcwd()
    returns the current working directory 

-> contents = os.listdir('/path/to/directory')
    returns a list containing the names of all the files and directories in the specified directory.

-> os.walk()
    for root, dirs, files in os.walk('/path/to/directory'):
        for file in files:
            print(os.path.join(root, file))
    # here root is always a folder, and it's recursive each time in the loop it will be a path to a folder or subfolder or subsubfolder... and go on, so we can replace dire with _ if we only want to walk over all the paths

-> os.chdir('/path/to/new/directory')
    After calling os.chdir(), any subsequent file operations (such as opening, reading, or writing  
    files) will be relative to the new current working directory.

-> path = os.path.join('folder', 'subfolder', 'file.txt')

'''







class Main(object): 

    # I think this shall just initialize data, don't do anything else, everything should 
    # be explecitly writte in a function/method

    def __init__(self) -> None:
        self.x = 'test'
        self.annotations = [1,2,3]
        

    # making an object also callable
    def __call__(self, args) -> None: 
        pass

    def __str__(self): 
        pass


    def __getitem__(self, index):
        import numpy as np 
  
    @staticmethod
    def get_state(self):    

        message = f"""
            This is just a multi line string okay, you can fucking {self.x}
        """
        pass

    # this one will prevent from making the next p-file in the spoon 
    @staticmethod
    def __execute__(self): 
        pass

    
# // Author : Omari Hamza
# // This project is a school project, for the Algorithms and data structure course final project
# // will not be maintained after the deadline
# // Mayebe I will make copy will be made and upgraded version releases will be found in my github for future works
# my passion is making beautiful websites, games, and beautiful designs

# this project mainlly consist on implementing various data structures, like queens, liksts, stacks, for a simulation fun game
# by the end of it the student will showcase a good understand and implementing various concepts for those data strcutres
    
# report for bugs: pull request on the github repo
    
# I am currently studying about software engineering in the university of science and technology, where i discover about 




