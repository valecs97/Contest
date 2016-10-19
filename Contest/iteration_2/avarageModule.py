'''
Created on Oct 18, 2016

@author: Vitoc
'''

class avarageModuleClass:

    def __init__(self):
        return
    
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
        
        