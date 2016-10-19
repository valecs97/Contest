'''
Created on Oct 18, 2016

@author: Vitoc
'''

from functions import algorithms

class podiumModuleClass:


    def __init__(self):
        return
    
    '''
    Tops the first x contestants with the highest avarage score
    input data:
    l - the main list
    x - the number of contestats to be show
    output data:
    a list with top contestants
    raises:
    1.x is not between the list bounderies
    '''
   
    def topContestants(self,l,x):
        algorithm = algorithms.algorithmsClass()
        order = algorithm.sortTheList(l)
        toPrint=[]
        for i in range (1,x+1):
            toPrint.append([order[len(l)-i] ,l[order[len(l)-i]][0] ,l[order[len(l)-i]][1],l[order[len(l)-i]][2] , (l[order[len(l)-i]][0]+l[order[len(l)-i]][1]+l[order[len(l)-i]][2])/3])
        return toPrint

        
    def printTopContestants(self,l,x):
        if x<0 or x>=len(l):
            raise ValueError("Your numbers isnt between the list bounderies")
        toPrint = self.topContestants(l, x)
        for i in range (len(toPrint)):
            print(i,'. Contestant ' , toPrint[i][0] , ' : ' ,toPrint[i][1], ' ' ,toPrint[i][2],' ',toPrint[i][3] , ' with avarage of ' , toPrint[i][4])
     
    '''
    Tops the first x contestants with the highest score for a problem (1 ,2 or 3
    input data:
    l - the main list
    x - the number of contestats to be show
    p - the problem number
    output data:
    a list with top contestants
    raises:
    1.x is not between the list bounderies
    2.p is not 1, 2 or 3
    '''
            
    def makeProblemList(self,l,p):
        con=[]
        for i in range (len(l)):
            con.append(l[i][p])
        return con
            
    def findTheOrder(self,con):
        order=[]
        for i in range (len(con)):
            order.append(i)
        con,order = zip(*sorted(zip(con,order)))
        return order
            
    def topProblemContestants(self,l,x,p):
        order = self.findTheOrder(self.makeProblemList(l, p))
        toPrint=[]
        for i in range (1,x+1):
            toPrint.append([order[len(l)-i] , l[order[len(l)-i]][p]])
        return toPrint
        
    def printTopProblemsContestants(self,l,x,p):
        if x<0 or x>=len(l):
            raise ValueError("Your number isnt between the list bounderies")
        if p<0 or p>3:
            raise ValueError("The problem doesnt exist")
        toPrint = self.topProblemContestants(l, x, p)
        for i in range (len(toPrint)):
            print(i,". Contestant ", toPrint[i][0], " with the grade ",toPrint[i][1])
            
    '''
    Removes (sets score to 0) to the contestants that have a score lower than or above than
    input data:
    l - the given list of list of integers
    x - the given number
    sign - case of comparation
    output data:
    nothing ... it just modifies the list which can be printed afterwards
    P.S if there are no such items , it wont do anything to the list but it will affect the undo function
    '''
    
    def removeContestantsList(self,l,x,sign):
        algorithm = algorithms.algorithmsClass()
        med = algorithm.avarageList(l)
        toDelete=[]
        for i in range(len(med)):
            if algorithm.compareNubmer(med[i]*10, x, sign):
                toDelete.append(i)
        return toDelete
    
    def removeContestants(self,l,x,sign):
        toDelete=self.removeContestantsList(l, x, sign)
        for i in range (len(toDelete)):
            l[toDelete[i]]=[0,0,0]
        
        
            
        