'''
Created on Oct 18, 2016

@author: Vitoc
'''

from iteration_3 import podiumModule

class testIteration_3Class:

    def __init__(self):
        return
        
    def testTopContestantsOp(self):
        podiumClass = podiumModule.podiumModuleClass()
        assert (podiumClass.topContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3)==[[4,5,5,5,5],[2,4,4,4,4],[1,3,3,3,3]])
        try:
            assert (podiumClass.topContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3)==[[4,5,5,5,5],[2,4,4,4,4],[1,2,2,2,2]])
            assert(False)
        except AssertionError:
            assert(True)
            
    def testTopProblemContestantsOp(self):
        podiumClass = podiumModule.podiumModuleClass()
        assert (podiumClass.topProblemContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3,2)==[[4,5],[2,4],[1,3]])
        try:
            assert (podiumClass.topProblemContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3,2)==[[4,5],[2,4],[1,2]])
            assert(False)
        except AssertionError:
            assert(True)
            
    def testRemoveContestantsOp(self):
        podiumClass = podiumModule.podiumModuleClass()
        assert(podiumClass.removeContestantsList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[0,1])
        try:
            assert (podiumClass.removeContestantsList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[0,1,2])
            assert(False)
        except AssertionError:
            assert(True)
        