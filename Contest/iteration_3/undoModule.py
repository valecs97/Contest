'''
Created on Oct 18, 2016

@author: Vitoc
'''

import copy

class undoModuleClass:

    def __init__(self):
        return
    
    '''
    Function that undos the operations that you have made
    '''
    
    def saveTheFunction(self,l,undo):
        undo.append(copy.deepcopy(l))
        
        
    def undoIntoPast(self,l,undo):
        try:
            maximus = len(undo) -1
            l = copy.deepcopy(undo[maximus])
            del undo[maximus]
        except IndexError:
            print("There are no more undos , sry")
        return l
        