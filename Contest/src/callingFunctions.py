'''
Created on Oct 18, 2016

@author: Vitoc
'''

from iteration_1 import addModule
from iteration_1 import modifyModule
from iteration_2 import listModule
from iteration_2 import avarageModule
from iteration_3 import podiumModule

class callingFunctionsClass:



    def __init__(self):
        return
    
    def addUI(self,l, params):
        addClass = addModule.addModuleClass()
        if len(params)!=3:
            raise ValueError('Please type 3 scores for each person')
        x = [int(params[0]),int(params[1]),int(params[2])]
        addClass.add(l,x)
        del addClass

    '''
    def removeSpecificItemsUI(self,l,params):
        if len(params)!=1:
            raise ValueError('Your syntax should be something like that removes 10 , you didnt write like so')
        x = int(params[0])
        removeSpecificItems(l,x)
    '''

    def insertUI(self,l,params):
        addClass = addModule.addModuleClass()
        if len(params)!=5:
            raise ValueError('Your syntax should be something like that insert 1 2 3 at 0 , you didnt write like so')
        x = [int(params[0]),int(params[1]),int(params[2])]
        p = int(params[4])
        addClass.insert(l,x,p)
        del addClass

    def replaceUI(self,l,params):
        modifyClass = modifyModule.modifyModuleClass()
        if len(params)!=4:
            raise ValueError('Your syntax should be something like this : replace 4 P2 with 5, you didnt write like so')
        p = int(params[0])
        s = int(params[3])
        x = int(params[1][1])
        modifyClass.replace(l, x, p, s)
        del modifyClass


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
        listClass = listModule.listModuleClass()
        listClass.printList(l)
        del listClass
        
    def printSortedListUI(self,l):
        listClass = listModule.listModuleClass()
        listClass.printSortedList(l)
        del listClass
        
    def printSpecificList(self,l,params):
        x=int(params[1])
        listClass = listModule.listModuleClass()
        listClass.printSpecificList(l,x,params[0])
        del listClass
        
    def avarageSumeUI(self,l,params):
        avg = avarageModule.avarageModuleClass()
        if len(params)!=3:
            raise ValueError("Your syntax should be something like this : avg 1 to 5, you didnt write like so")
        start = int(params[0])
        stop = int(params[2])
        print (avg.avarageSume(start,stop,l))
        del avg
        
    def minSumeUI(self,l,params):
        avg = avarageModule.avarageModuleClass()
        if len(params)!=3:
            raise ValueError("Your syntax should be something like this : avg 1 to 5, you didnt write like so")
        start = int(params[0])
        stop = int(params[2])
        print (avg.minSume(start,stop,l))
        del avg
        
    def topContestantsUI(self,l,params):
        if len(params)==2:
            self.topProblemContestants(l, params)
            return
        podiumClass = podiumModule.podiumModuleClass()
        x = int(params[0])
        podiumClass.printTopContestants(l, x)
        del podiumClass
    
    def topProblemContestants(self,l,params):
        if len(params)!=2:
            raise ValueError("Your syntax should be something like this : top 5 P2, you didnt write like so")
        podiumClass = podiumModule.podiumModuleClass()
        x = int(params[0])
        p= int (params[1][1])
        podiumClass.printTopProblemsContestants(l, x, p)
        del podiumClass
    
    def removeUI(self,l,params):
        modifyClass = modifyModule.modifyModuleClass()
        podiumClass = podiumModule.podiumModuleClass()
        if len(params)!=1:
            if len(params)==2:
                x=int(params[1])
                podiumClass.removeContestants(l, x, params[0])
            else:
                modifyClass.removeMore(l,int(params[0]),int(params[2]))
        else:
            p = int(params[0])
            modifyClass.remove(l,p)
        del modifyClass
        del podiumClass
        