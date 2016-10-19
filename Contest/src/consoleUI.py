'''
Created on Oct 18, 2016

@author: Vitoc
'''

from src import callingFunctions
from iteration_3 import undoModule
import copy

class consoleUIClass:


    def __init__(self):
        return
    
    '''
    Here is the console UI
    '''
    
    def readCmd(self):
        x = input()
        return x.split()



    def exampleImplement(self,l):
        for i in range (1,16):
            if i<=10:
                l.append([i,i,i])
            else:
                l.append([i-10,i-10,i-10])
    
    def run(self):
        l=[]
        undo=[]
        self.exampleImplement(l)
        undoClass = undoModule.undoModuleClass()
        f = callingFunctions.callingFunctionsClass()
        cmdsList={"add":f.addUI,"remove":f.removeUI,"list":f.listUI,"insert":f.insertUI,"replace":f.replaceUI,"avg":f.avarageSumeUI,"min":f.minSumeUI,"top":f.topContestantsUI,"undo":"nothing"}
        while True:
            #print(l,'\n',undo)
            cmd = self.readCmd()
            if cmd[0] == 'exit':
                return
    
            if cmd[0] in cmdsList:
                if cmd[0]=="undo":
                    l=undoClass.undoIntoPast(l, undo)
                else:
                    try:
                        aux=copy.deepcopy(l)
                        cmdsList[cmd[0]](l,cmd[1:])
                        if cmd[0]!="list" and cmd[0]!="avg" and cmd[0]!="min":
                            undoClass.saveTheFunction(aux, undo)
                    except ValueError as ex:
                        print(ex)
            else:
                print("invalid command")