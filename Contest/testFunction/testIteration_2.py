'''
Created on Oct 18, 2016

@author: Vitoc
'''

from functions import algorithms
from iteration_2 import listModule
from iteration_2 import avarageModule

class testIteration_2Class:



    def __init__(self):
        return
    
    def testSortedListOp(self):
        algorithm = algorithms.algorithmsClass()
        assert(algorithm.sortTheList([[3,3,3],[2,2,2],[4,4,4],[1,1,1],[5,5,5]])==(3,1,0,2,4))
        try:
            assert(algorithm.sortTheList([[3,3,3],[2,2,2],[4,4,4],[1,1,1],[5,5,5]])==(3,1,0,4,2))
            assert(False)
        except AssertionError:
            assert(True)
        del algorithm
        
    def testSpecificListOp(self):
        test = listModule.listModuleClass()
        try:
            assert(test.createTheSpecificList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[[1,1,1],[2,2,2],[3,3,3]])
            assert(False)
        except AssertionError:
            assert(True)
        del test
        
    def testAvarageSumeOp(self):
        test = avarageModule.avarageModuleClass()
        assert(test.avarageSume(1, 3, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==3.0)
        try:
            assert(test.avarageSume(0, 4, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==2.5)
            assert(False)
        except AssertionError:
            assert(True)
            
    def testMinSumeOp(self):
        test = avarageModule.avarageModuleClass()
        assert(test.minSume(1, 3, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==3.0)
        try:
            assert(test.minSume(0, 4, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==2.5)
            assert(False)
        except AssertionError:
            assert(True)

