'''
Created on Oct 18, 2016

@author: Vitoc
'''

from testFunction.testIteration_1 import testIteration_1Class
from testFunction.testIteration_2 import testIteration_2Class
from testFunction.testIteration_3 import testIteration_3Class

class testMainClass:


    def __init__(self):
        return
    
    def performAllTests(self):
        test1 = testIteration_1Class()
        test2 = testIteration_2Class()
        test3 = testIteration_3Class()
        #iteration 1
        test1.testRemoveOp()
        test1.testAddOp()
        test1.testInsertOp()
        test1.testReplaceOp()
        #iteration 2
        test2.testSortedListOp()
        test2.testSpecificListOp()
        test2.testAvarageSumeOp()
        test2.testMinSumeOp()
        #iteration 3
        test3.testTopContestantsOp()
        test3.testTopProblemContestantsOp()
        test3.testRemoveContestantsOp()
        del test1, test2
        