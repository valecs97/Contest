'''
Created on Oct 18, 2016

@author: Vitoc
'''

class addModuleClass:


    def __init__(self):
        return
    
    '''
    funtion that adds a set of integer values as a list to the given list of integers l
    imput data:
    l - the given list of list of integers
    el - the list of integers to be added
    output:
    l'=l+[p1,p2,p3]
    raises:
    ValueError - if one of the scores are not integer between 0 and 10

    '''
    def add(self,l,el):
        for testNumber in el:
            if testNumber<0 or testNumber>10:
                raise ValueError('The score has to be between 0 and 10')
        l.append(el)
        return l
    
    '''
    Function that inserts a given score to a position:
    l - the given list of list of integers
    el - the given list of scores to be modified
    p - position of the element in the list to be modified
    0<=p<len(l)
    output data:
    l[p] = el
    raises:
    ValueError - when p is not a valid position inside the list l
    ValueError (the second one) - if one of the scores are not integer between 0 and 10
    '''  

    def insert (self,l,el,p):
        if p<0 or p>=len(l):
            raise ValueError('Invalid position inside the list!')
        for i in range(3):
            if el[i]<0 or el[i]>10:
                raise ValueError('The score has to be between 0 and 10')
        for i in range (3):
            l[p][i]=el[i]
        return l




        