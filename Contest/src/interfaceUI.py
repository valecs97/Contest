'''
Created on Oct 18, 2016

@author: Vitoc
'''

from src.functions import functionsClass
from src.printFunctions import printFunctionsClass

class interfaceUIClass:


    def __init__(self):
        return
    
    def readCmd(self):
        x = input('Input command:')
        return x
    
    def readStartStop(self):
        start = input('Starting point :')
        end = input ('Ending point :')
        return [int(start),int(end)]
    
    def readScores(self):
        firstScore=input('First score:')
        secondScore=input('Second Score:')
        thirstScore=input('Third Score:')
        return [int(firstScore),int(secondScore),int(thirstScore)]
    
    def readContestant(self):
        contestant = input('Contestant number :')
        return int(contestant)
    
    def readProblemNumber(self):
        problem = input('Problem number :')
        return int(problem)
    
    def readSingleScore(self):
        score = input('Score :')
        return int(score)
    
    def readGivenNumber(self):
        x = input('The given number :')
        return int(x)
    
    def readTopNumber(self):
        x= input('Top :')
        return int(x)
    
    def printOptions(self):
        print("\nPlease choose one of the options:")
        print("1.Add a new contestant to the list")
        print("2.Insert a new set of scores to an existing contestant")
        print("3.Remove contestants")
        print("4.Replace a problem score to an existing contestant")
        print("5.Print the list of contestants")
        print("6.Avarage score of a number of contestants")
        print("7.The minimum score of a number of contestants")
        print("8.Top contestants")
        print("9.Undo")
        print("0.Exit")
        
    def addUI(self,l):
        functionsClassModule=functionsClass()
        x = self.readScores()
        functionsClassModule.add(l,x)
        
    
    def insertUI(self,l):
        functionsClassModule=functionsClass()
        el = self.readScores()
        p=self.readContestant()
        functionsClassModule.insert(l, el,p)
    
    def removeUI(self,l):
        cmdList={'1':self.removeUI1,'2':self.removeUI2,'3':self.removeUI3,'4':self.removeUI4,'5':self.removeUI5}
        self.removeUIPrint()
        cmd = self.readCmd()
        if cmd in cmdList:
            cmdList[cmd](l)
        else:
            print('Invalid command , you will be returned to the start menu')
        
    def removeUI1(self,l):
        functionsClassModule=functionsClass()
        p=self.readContestant()
        functionsClassModule.remove(l, p)
    
    def removeUI2(self,l):
        functionClassModule = functionsClass()
        startAndEnd = self.readStartStop()
        functionClassModule.removeMore(l, startAndEnd[0], startAndEnd[1])
    
    def removeUI3(self,l):
        functionsClassModule=functionsClass()
        x= self.readGivenNumber()
        functionsClassModule.removeContestants(l, x, '<')
    
    def removeUI4(self,l):
        functionsClassModule=functionsClass()
        x= self.readGivenNumber()
        functionsClassModule.removeContestants(l, x, '=')
    
    def removeUI5(self,l):
        functionsClassModule=functionsClass()
        x= self.readGivenNumber()
        functionsClassModule.removeContestants(l, x, '>')
        
    def removeUIPrint(self):
        print('\nPlease choose which one of the removes you want : ')
        print('1.Remove one contestant')
        print('2.Remove from a number to another')
        print('3.Remove contestants lower than a given score')
        print('4.Remove contestants equal to a given score')
        print('5.Remove contestants higher to a given score')
        
    def replaceUI(self,l):
        functionsClassModule = functionsClass()
        x=self.readProblemNumber()
        p=self.readContestant()
        s=self.readSingleScore()
        functionsClassModule.replace(l, x, p, s)
        
    def listUI(self,l):
        cmdList={'1':self.listUI1,'2':self.listUI2,'3':self.listUI3,'4':self.listUI4,'5':self.listUI5}
        self.listUIPrint()
        cmd = self.readCmd()
        if cmd in cmdList:
            cmdList[cmd](l)
        else:
            print('Invalid command , you will be returned to the start menu')
            
    def listUI1(self,l):
        printFunctionsClassModule = printFunctionsClass()
        printFunctionsClassModule.printList(l)
    
    def listUI2(self,l):
        printFunctionsClassModule = printFunctionsClass()
        printFunctionsClassModule.printSortedList(l)
    
    def listUI3(self,l):
        printFunctionsClassModule = printFunctionsClass()
        x=self.readGivenNumber()
        printFunctionsClassModule.printSpecificList(l, x, '<')
    
    def listUI4(self,l):
        printFunctionsClassModule = printFunctionsClass()
        x=self.readGivenNumber()
        printFunctionsClassModule.printSpecificList(l, x, '=')
    
    def listUI5(self,l):
        printFunctionsClassModule = printFunctionsClass()
        x=self.readGivenNumber()
        printFunctionsClassModule.printSpecificList(l, x, '>')
            
    def listUIPrint(self):
        print('\nPlease choose which print you want : ')
        print('1.Print the list')
        print('2.Print the sorted list')
        print('3.Print contestants lower than a given score')
        print('4.Print contestants equal to a given score')
        print('5.Print contestants higher to a given score')
    
    def avgUI(self,l):
        functionsClassModule=functionsClass()
        startAndStop=self.readStartStop()
        print(functionsClassModule.avarageSume(startAndStop[0], startAndStop[1], l))
        
    def minUI(self,l):
        functionsClassModule=functionsClass()
        startAndStop=self.readStartStop()
        print(functionsClassModule.minSume(startAndStop[0], startAndStop[1], l))
        
    def topUI(self,l):
        cmdList={'1':self.topUI1,'2':self.topUI2}
        self.topUIPrint()
        cmd = self.readCmd()
        if cmd in cmdList:
            cmdList[cmd](l)
        else:
            print('Invalid command , you will be returned to the start menu')
            
    def topUI1(self,l):
        printFunctionsClassModule = printFunctionsClass()
        x=self.readTopNumber()
        printFunctionsClassModule.printTopContestants(l, x)
        
        
    def topUI2(self,l):
        printFunctionsClassModule = printFunctionsClass()
        p=self.readProblemNumber()
        x=self.readTopNumber()
        printFunctionsClassModule.printTopProblemsContestants(l, x, p-1)
        
            
    def topUIPrint(self):
        print('\nPlease choose which top you want : ')
        print('1.Top x contestants')
        print('2.Top x contestants to a problem')
        
    def undoUI(self,l,undo):
        functionsClassModule = functionsClass()
        l=functionsClassModule.undoIntoPast(l, undo)
        return l
    
    def run(self):
        l=[]
        undo=[]
        functionClassModule = functionsClass()
        functionClassModule.exampleImplement(l)
        cmdsList={"1":self.addUI,"2":self.insertUI,"3":self.removeUI,'4':self.replaceUI,'5':self.listUI,'6':self.avgUI,'7':self.minUI,'8':self.topUI}
        while True:
            self.printOptions()
            cmd = self.readCmd()
            if cmd == '0':
                return
            if cmd in cmdsList or cmd == '9':
                if cmd == '9':
                    l=self.undoUI(l, undo)
                else:
                    try:
                        import copy
                        aux=copy.deepcopy(l)
                        cmdsList[cmd](l)
                        if cmd!="5" and cmd!="6" and cmd!="7" and cmd!='8':
                            functionsClassModule = functionsClass()
                            functionsClassModule.saveTheFunction(aux, undo)
                    except ValueError as ex:
                        print(ex)
            else:
                print("invalid command")