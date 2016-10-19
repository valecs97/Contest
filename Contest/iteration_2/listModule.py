'''
Created on Oct 18, 2016

@author: Vitoc
'''

from functions import algorithms

class listModuleClass:


    def __init__(self):
        return
    
    '''
    Function that prints the list
    '''
    
    def printList(self,l):
        for x in range (len(l)):
            print('Contestant ' , x , ' : ',l[x][0], ' ' ,l[x][1],' ',l[x][2])
    
    
    '''
    Function that prints the sorted list
    input data:
    l - the given list of list of integers
    output data:
    prints l sorted
    '''

    def printSortedList(self,l):
        algorithm = algorithms.algorithmsClass()
        order = algorithm.sortTheList(l)
        for i in range (len(l)):
            print('Contestant ' , order[i] , ' : ',l[order[i]][0], ' ' ,l[order[i]][1],' ',l[order[i]][2])
        del algorithm
        
    '''
    Function that prints specific items from the list (below,above or equal to a given number)
    input data:
    l - the given list of list of integers
    x - the given number
    sign - case of comparation
    output data:
    prints l sorted
    P.S if there are no such items , it will print : There are no such items
    '''    
    
    def printSpecificList(self,l,x,sign):
        toPrint = self.createTheSpecificList(l, x, sign)
        if toPrint=="There are no such contestants":
            print("There are no such contestants")
        else:
            self.printList(toPrint)
        
            
    def createTheSpecificList(self,l,x,sign):
        algorithm = algorithms.algorithmsClass()
        med = algorithm.avarageList(l)
        ok=False
        toPrint=[]
        for i in range(len(med)):
            if algorithm.compareNubmer(med[i]*10, x, sign):
                toPrint.append(l[i])
                ok=True
        if ok==False:
            return "There are no such contestants"
        else:
            return toPrint
            
    

        