'''
Created on Oct 18, 2016

@author: Vitoc
'''

class modifyModuleClass:


    def __init__(self):
        return
    
    '''
    function that sets the score of a person to 0:
    l - the given list of list of integers
    p - position of the element that will be set to 0
    0<=p<len(l)
    output data:
    l[p] = [0,0,0]
    raises:
    ValueError - when p is not a valid position inside the list l
    '''

    def remove(self,l,p):
        if p<0 or p>=len(l):
            raise ValueError('Invalid position inside the list!')
        for i in range (3):
            l[p][i]=0
        return l

    '''
    Function that sets the score to 0 to the persons that are between start and end
    l - the given list of list of integers
    start - the position from which to start removing
    end - the position from which to stop removing
    0<=start<end<len(l)
    output data:
    from l[start] to l[end] = [0,0,0]
    raises:
    ValueError - when p is not a valid position inside the list l
    ValueError(second one) - when the start is higher or equal to the end
    '''        
    def removeMore(self,l,start,end):
        if start<0 or end<0 or start>=len(l) or end>=len(l):
            raise ValueError('Invalid position inside the list!')
        if start>=end:
            raise ValueError('The start must be lower than the end!')
        for removeNumber in range(start,end+1):
            self.remove(l,removeNumber)
        return l


   
    '''
    Function that replaces the score from the problem x at the position p to the new score s
    l - the given list of list of integers
    x - the problem that will be replaced (1 , 2 or 3)
    p - position of the element in the list to be modified
    s - the new score (integer)
    0<=p<len(l)
    1<=x<3
    0<=s<10
    output data:
    l[p][x]=s
    raises:
    ValueError - when x is not between 1 and 3
    ValueError (the second one) - when p is not a valid position inside the list l
    ValueError (the third one) - when s is not a valid grade
    '''     
    def replace (self,l,x,p,s):
        self.checkForRaises(l, x, p, s)
        l[p][x-1]=s
        return l
    
    def checkForRaises(self,l,x,p,s):
        if p<0 or p>=len(l):
            raise ValueError('Invalid position inside the list!')
        if s<0 or s>10:
            raise ValueError('The score has to be between 0 and 10')
        if x<0 or x>3:
            raise ValueError('The problem has to be P1, P2 or P3')

    

    

        