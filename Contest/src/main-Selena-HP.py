'''
Created on Oct 11, 2016

@author: Vitoc
'''

if __name__ == '__main__':
    pass

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

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
def add(l,el):
    for testNumber in el:
        if testNumber<0 or testNumber>10:
            raise ValueError('The score has to be between 0 and 10')
    l.append(el)
    return l

def testAddOp():
    try:
        assert(add([],[1,2,3])==[[1,2,3]])
        assert(add([[1,2]],[9,10,11])==[[1,2],[9,10,11]])
        assert(False)
    except ValueError:
        assert(True)



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

def remove(l,p):
    if p<0 or p>=len(l):
        raise ValueError('Invalid position inside the list!')
    for i in range (3):
        l[p][i]=0
    return l

def testRemoveOp():
    assert(remove([[1,2,3],[4,5,6],[7,8,9]],2)==[[1,2,3],[4,5,6],[0,0,0]])
    try:
        remove([[1,2,3],[3,4,5]],7)
        assert(False) #asa sa facem la examen
    except ValueError:
        assert(True)

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
def removeMore(l,start,end):
    if start<0 or end<0 or start>=len(l) or end>=len(l):
        raise ValueError('Invalid position inside the list!')
    if start>=end:
        raise ValueError('The start must be lower than the end!')
    for removeNumber in range(start,end+1):
        remove(l,removeNumber)
        
        
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

def insert (l,el,p):
    if p<0 or p>=len(l):
        raise ValueError('Invalid position inside the list!')
    for i in range(3):
        if el[i]<0 or el[i]>10:
            raise ValueError('The score has to be between 0 and 10')
    for i in range (3):
        l[p][i]=el[i]
    return l

def testInsertOp():
    assert(insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,5],2)==[[1,1,1],[2,2,2],[5,5,5]])
    try:
        assert(insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,11],2)==[[1,1,1],[2,2,2],[5,5,5]])
        assert(False)
    except ValueError:
        assert(True)
   
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

def checkForRaises(l,x,p,s):
    if p<0 or p>=len(l):
        raise ValueError('Invalid position inside the list!')
    if s<0 or s>10:
        raise ValueError('The score has to be between 0 and 10')
    if x<0 or x>3:
        raise ValueError('The problem has to be P1, P2 or P3')

def replace (l,x,p,s):
    checkForRaises(l, x, p, s)
    l[p][x-1]=s
    return l

def testReplaceOp():
    try:
        assert(replace([[1,1,1],[2,2,2],[3,3,3]],4,0,9)==[[1,1,9],[2,2,2],[3,3,3]])
        assert(False)
    except ValueError:
        assert(True)
    
                 
'''
Here are the UI and the main functions
'''

def performAllTests():
    testRemoveOp()
    testAddOp()
    testInsertOp()
    testReplaceOp()

def readCmd():
    x = input()
    return x.split()

def addUI(l, params):
    if len(params)!=3:
        raise ValueError('Please type 3 scores for each person')
    x = [float(params[0]),float(params[1]),float(params[2])]
    add(l,x)

def removeUI(l,params):
    if len(params)!=1:
        if params[1]!='to':
            raise ValueError('Please type 3 scores for each person')
        else:
            removeMore(l,int(params[0]),int(params[2]))
    else:
        p = int(params[0])
        remove(l,p)

def insertUI(l,params):
    if len(params)!=5:
        raise ValueError('Your syntax should be something like that insert 1 2 3 at 0 , you didnt write like so')
    x = [float(params[0]),float(params[1]),float(params[2])]
    p = int(params[4])
    insert(l,x,p)

def replaceUI(l,params):
    if len(params)!=4:
        raise ValueError('Your syntax should be something like that replace 4 P2 with 5 , you didnt write like so')
    p = int(params[0])
    s = float(params[3])
    x = int(params[1][1])
    replace(l, x, p, s)

def printList(l,params):
    for x in range (len(l)):
        print('Contestant ' , x , ' : ',l[x][0], ' ' ,l[x][1],' ',l[x][2])

def exampleImplement(l):
    for i in range (1,16):
        if i<=10:
            l.append([float(i),float(i),float(i)])
        else:
            l.append([float(i)-10,float(i)-10,float(i)-10])

def run():
    l=[]
    exampleImplement(l)
    cmdsList={"add":addUI,"remove":removeUI,"list":printList,"insert":insertUI,"replace":replaceUI}
    while True:
        cmd = readCmd()
        if cmd[0] == 'exit':
            return
        if cmd[0] in cmdsList:
            try:
                cmdsList[cmd[0]](l,cmd[1:])
            except ValueError as ex:
                print(ex)
        else:
            print("invalid command")

def main():
    performAllTests()
    run()

main()
