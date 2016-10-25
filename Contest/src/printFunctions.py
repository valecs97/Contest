'''
Created on Oct 23, 2016

@author: Vitoc
'''

class printFunctionsClass:


    def __init__(self):
        return
    
    def printTopProblemsContestants(self,l,x,p):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        if x<0 or x>=len(l):
            raise ValueError("Your number isnt between the list bounderies")
        if p<0 or p>3:
            raise ValueError("The problem doesnt exist")
        toPrint = functionsClass.topProblemContestants(l, x, p)
        for i in range (len(toPrint)):
            print(i,". Contestant ", toPrint[i][0], " with the grade ",toPrint[i][1])
            
    def printTopContestants(self,l,x):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        if x<0 or x>=len(l):
            raise ValueError("Your numbers isnt between the list bounderies")
        toPrint = functionsClass.topContestants(l, x)
        for i in range (len(toPrint)):
            print(i,'. Contestant ' , toPrint[i][0] , ' : ' ,toPrint[i][1], ' ' ,toPrint[i][2],' ',toPrint[i][3] , ' with avarage of ' , toPrint[i][4])

    '''
    Function that prints the sorted list
    input data:
    l - the given list of list of integers
    output data:
    prints l sorted
    '''

    def printSortedList(self,l):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        order = functionsClass.sortTheList(l)
        for i in range (len(l)):
            print('Contestant ' , order[i] , ' : ',l[order[i]][0], ' ' ,l[order[i]][1],' ',l[order[i]][2])
            
    '''
    Function that prints the list
    '''
    
    def printList(self,l):
        for x in range (len(l)):
            print('Contestant ' , x , ' : ',l[x][0], ' ' ,l[x][1],' ',l[x][2])
            
    def printSpecificList(self,l,x,sign):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        toPrint = functionsClass.createTheSpecificList(l, x, sign)
        if toPrint=="There are no such contestants":
            print("There are no such contestants")
        else:
            for x in range (len(toPrint)):
                print('Contestant ' , x , ' : ',toPrint[x][0], ' ' ,toPrint[x][1],' ',toPrint[x][2])