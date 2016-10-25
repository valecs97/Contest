'''
Created on Oct 23, 2016

@author: Vitoc
'''

class functionsClass():


    def __init__(self):
        return
    
    def exampleImplement(self,l):
        for i in range (1,16):
            if i<=10:
                l.append([i,i,i])
            else:
                l.append([i-10,i-10,i-10])
    
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
        
    '''
    Function that makes an avarage of some contestants scores
    input data:
    l - the main list
    start - the start position
    stop - the end position
    output data:
    avarage of scores
    raises:
    1.If the numbers arent between the boundaries
    2.If the start point is greater than the end
    '''
    
    def avarageSume(self,start,stop,l):
        if (start<0 or start>=len(l) or stop<0 or stop>=len(l)):
            return "Your numbers isnt between the list bounderies"
        if (stop<start):
            return "Your start point shoudnt be greater than the end point"
        s=0
        for i in range (start,stop+1):
            s = s + (l[i][0]+l[i][1]+l[i][2])/3
        s = s / (stop - start +1)
        return s
    
    '''
    Function that makes an avarage of the lowest grade from a set of contestants
    input data:
    l - the main list
    start - the start position
    stop - the end position
    output data:
    avarage of lowest score
    raise :
    1.If the numbers arent between the boundaries
    2.If the start point is greater than the end
    '''
    
    def minSume(self,start,stop,l):
        if (start<0 or start>=len(l) or stop<0 or stop>=len(l)):
            return "Your numbers isnt between the list bounderies"
        if (stop<start):
            return "Your start point shoudnt be greater than the end point"
        s=0
        for i in range (start,stop+1):
            mn=l[i][0]
            if l[i][1]<mn:
                mn=l[i][1]
            if l[i][2]<mn:
                mn=l[i][2]
            s = s + mn
        s = s / (stop - start +1)
        return s
    
        
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
            
    def createTheSpecificList(self,l,x,sign):
        med = self.avarageList(l)
        ok=False
        toPrint=[]
        for i in range(len(med)):
            if self.compareNubmer(med[i]*10, x, sign):
                toPrint.append(l[i])
                ok=True
        if ok==False:
            return "There are no such contestants"
        else:
            return toPrint
    
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
        order = self.sortTheList(l)
        toPrint=[]
        for i in range (1,x+1):
            toPrint.append([order[len(l)-i] ,l[order[len(l)-i]][0] ,l[order[len(l)-i]][1],l[order[len(l)-i]][2] , (l[order[len(l)-i]][0]+l[order[len(l)-i]][1]+l[order[len(l)-i]][2])/3])
        return toPrint
         
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
        med = self.avarageList(l)
        toDelete=[]
        for i in range(len(med)):
            if self.compareNubmer(med[i]*10, x, sign):
                toDelete.append(i)
        return toDelete
    
    def removeContestants(self,l,x,sign):
        toDelete=self.removeContestantsList(l, x, sign)
        for i in range (len(toDelete)):
            l[toDelete[i]]=[0,0,0]
            
    '''
    Function that undos the operations that you have made
    '''
    
    def saveTheFunction(self,l,undo):
        import copy
        undo.append(copy.deepcopy(l))
        
        
    def undoIntoPast(self,l,undo):
        try:
            import copy
            maximus = len(undo) -1
            l = copy.deepcopy(undo[maximus])
            del undo[maximus]
            return l
        except IndexError:
            print("There are no more undos , sry")
            return l
    
    '''
    Algortihms that are used by two or more functions in this class
    avarageList - it returns the avarage of a list formed by another lists formed of 3 elements
    sortTheList - it returns the order number to a sorted list
    compareNumber - it returns True or False if 2 given numbers are higher , lower or equal between them
    '''
    
    def avarageList(self,l):
        med=[]
        for i in range(len(l)):
            med.append((l[i][0]+l[i][1]+l[i][2])/3)
        return med
    
    def sortTheList(self,l):
        med=self.avarageList(l)
        order=[]
        for i in range (len(l)):
            order.append(i)
        med,order = zip(*sorted(zip(med,order)))
        return order
    
    def compareNubmer(self,first,second,case):
        if case == '<':
            if first<second:
                return True
        if case == '=':
            if first==second:
                return True
        if case == '>':
            if first>second:
                return True
        return False
        