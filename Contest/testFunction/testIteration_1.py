'''
Created on Oct 18, 2016

@author: Vitoc
'''

from iteration_1.addModule import addModuleClass
from iteration_1.modifyModule import modifyModuleClass

class testIteration_1Class:


    def __init__(self):
        return
        
    def testAddOp(self):
        addClass = addModuleClass()
        try:
            assert(addClass.add([],[1,2,3])==[[1,2,3]])
            assert(addClass.add([[1,2]],[9,10,11])==[[1,2],[9,10,11]])
            assert(False)
        except ValueError:
            assert(True)
    
    def testInsertOp(self):
        addClass = addModuleClass()
        assert(addClass.insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,5],2)==[[1,1,1],[2,2,2],[5,5,5]])
        try:
            assert(addClass.insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,11],2)==[[1,1,1],[2,2,2],[5,5,5]])
            assert(False)
        except ValueError:
            assert(True)
        del addClass
            
    def testRemoveOp(self):
        modifyClass = modifyModuleClass()
        assert(modifyClass.remove([[1,2,3],[4,5,6],[7,8,9]],2)==[[1,2,3],[4,5,6],[0,0,0]])
        try:
            modifyClass.remove([[1,2,3],[3,4,5]],7)
            assert(False) #asa sa facem la examen
        except ValueError:
            assert(True)
        del modifyClass
            
    def testReplaceOp(self):
        modifyClass = modifyModuleClass()
        try:
            assert(modifyClass.replace([[1,1,1],[2,2,2],[3,3,3]],4,0,9)==[[1,1,9],[2,2,2],[3,3,3]])
            assert(False)
        except ValueError:
            assert(True)
        del modifyClass