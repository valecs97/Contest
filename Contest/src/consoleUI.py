'''
Created on Oct 18, 2016

@author: Vitoc
'''
from src.functions import functionsClass
from src.printFunctions import printFunctionsClass

class consoleUIClass:


    def __init__(self):
        return
    
    
    
    '''
    Here is the console UI
    '''
   
    def readCmd(self):
        x = input()
        return x.split()
    
    def addUI(self,l, params):
        functionsClassModule=functionsClass()
        if len(params)!=3:
            raise ValueError('Please type 3 scores for each person')
        x = [int(params[0]),int(params[1]),int(params[2])]
        functionsClassModule.add(l,x)

    '''
    def removeSpecificItemsUI(self,l,params):
        if len(params)!=1:
            raise ValueError('Your syntax should be something like that removes 10 , you didnt write like so')
        x = int(params[0])
        removeSpecificItems(l,x)
    '''

    def insertUI(self,l,params):
        functionsClassModule=functionsClass()
        if len(params)!=5:
            raise ValueError('Your syntax should be something like that insert 1 2 3 at 0 , you didnt write like so')
        x = [int(params[0]),int(params[1]),int(params[2])]
        p = int(params[4])
        functionsClassModule.insert(l,x,p)

    def replaceUI(self,l,params):
        functionsClassModule=functionsClass()
        if len(params)!=4:
            raise ValueError('Your syntax should be something like this : replace 4 P2 with 5, you didnt write like so')
        p = int(params[0])
        s = int(params[3])
        x = int(params[1][1])
        functionsClassModule.replace(l, x, p, s)


    def listUI(self,l,params):
        if params==[]:
            self.printListUI(l)
            return
        if params==['sorted']:
            self.printSortedListUI(l)
            return
        if len(params)==2:
            self.printSpecificList(l,params)
            return
        else:
            print("You have written the wrong list command !!!")
            
        

    def printListUI(self,l):
        printFunctionsClassModule=printFunctionsClass()
        printFunctionsClassModule.printList(l)
        
    def printSortedListUI(self,l):
        printFunctionsClassModule=printFunctionsClass()
        printFunctionsClassModule.printSortedList(l)
        
    def printSpecificList(self,l,params):
        printFunctionsClassModule=printFunctionsClass()
        x=int(params[1])
        printFunctionsClassModule.printSpecificList(l,x,params[0])
        
    def avarageSumeUI(self,l,params):
        functionsClassModule=functionsClass()
        if len(params)!=3:
            raise ValueError("Your syntax should be something like this : avg 1 to 5, you didnt write like so")
        start = int(params[0])
        stop = int(params[2])
        print (functionsClassModule.avarageSume(start,stop,l))
        
    def minSumeUI(self,l,params):
        functionsClassModule=functionsClass()
        if len(params)!=3:
            raise ValueError("Your syntax should be something like this : avg 1 to 5, you didnt write like so")
        start = int(params[0])
        stop = int(params[2])
        print (functionsClassModule.minSume(start,stop,l))
        
    def topContestantsUI(self,l,params):
        printFunctionsClassModule=printFunctionsClass()
        if len(params)==2:
            self.topProblemContestants(l, params)
            return
        x = int(params[0])
        printFunctionsClassModule.printTopContestants(l, x)
    
    def topProblemContestants(self,l,params):
        printFunctionsClassModule=printFunctionsClass()
        if len(params)!=2:
            raise ValueError("Your syntax should be something like this : top 5 P2, you didnt write like so")
        x = int(params[0])
        p= int (params[1][1])
        printFunctionsClassModule.printTopProblemsContestants(l, x, p-1)
    
    def removeUI(self,l,params):
        functionsClassModule=functionsClass()
        if len(params)!=1:
            if len(params)==2:
                x=int(params[1])
                functionsClassModule.removeContestants(l, x, params[0])
            else:
                functionsClassModule.removeMore(l,int(params[0]),int(params[2]))
        else:
            p = int(params[0])
            functionsClassModule.remove(l,p)
    
    def undoUI(self,l,undo):
        functionsClassModule = functionsClass()
        l=functionsClassModule.undoIntoPast(l, undo)
        return l
    
    def run(self):
        l=[]
        undo=[]
        functionClassModule = functionsClass()
        functionClassModule.exampleImplement(l)
        cmdsList={"add":self.addUI,"remove":self.removeUI,"list":self.listUI,"insert":self.insertUI,"replace":self.replaceUI,"avg":self.avarageSumeUI,"min":self.minSumeUI,"top":self.topContestantsUI,"undo":"nothing"}
        while True:
            #print(l,'\n',undo)
            cmd = self.readCmd()
            if cmd[0] == 'exit':
                return
    
            if cmd[0] in cmdsList:
                if cmd[0]=="undo":
                    l=self.undoUI(l,undo)
                else:
                    try:
                        import copy
                        aux=copy.deepcopy(l)
                        cmdsList[cmd[0]](l,cmd[1:])
                        if cmd[0]!="list" and cmd[0]!="avg" and cmd[0]!="min" and cmd[0]!='top ':
                            functionsClassModule = functionsClass()
                            functionsClassModule.saveTheFunction(aux, undo)
                    except ValueError as ex:
                        print(ex)
            else:
                print("invalid command")