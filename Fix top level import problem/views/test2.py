import sys
import os

# Multi Directory Python Project ... 

def LoadSearchPaths():
    for i,j,y in os.walk(os.getcwd()):
        sys.path.append(i)
        print('i = ', i,'\n')
        print('j = ', j,'\n')
        print('y = ', y,'\n')
            


# This LoadSearchPaths() method can be written as given bellow ... 

''' 

import sys
import os

def LoadSearchPaths():
    for i,j,y in os.walk(os.getcwd()):
        if(str(i).find('__pycache__') == -1 and str(i).find('.vscode') == -1):
            sys.path.append(i)

'''

'''

Note:- __pycache__ is a directories where interpreters stores the cache information

        and .vscode also same here, but this time the cache is vs code editor.

'''

LoadSearchPaths()

from controller import main_controller




'''

references:- 

    http://python.robasworld.com/python-multi-directory-project/
    
'''
