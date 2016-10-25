'''
Created on Oct 18, 2016

@author: Vitoc
'''

class testMainClass:


    def __init__(self):
        return
    
    def performAllTests(self):
        #iteration 1
        self.testRemoveOp()
        self.testAddOp()
        self.testInsertOp()
        self.testReplaceOp()
        #iteration 2
        self.testSortedListOp()
        self.testSpecificListOp()
        self.testAvarageSumeOp()
        self.testMinSumeOp()
        #iteration 3
        self.testTopContestantsOp()
        self.testTopProblemContestantsOp()
        self.testRemoveContestantsOp()
        
    def testAddOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        try:
            assert(functionsClass.add([],[1,2,3])==[[1,2,3]])
            assert(functionsClass.add([[1,2]],[9,10,11])==[[1,2],[9,10,11]])
            assert(False)
        except ValueError:
            assert(True)
    
    def testInsertOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,5],2)==[[1,1,1],[2,2,2],[5,5,5]])
        try:
            assert(functionsClass.insert([[1,1,1],[2,2,2],[3,3,3]],[5,5,11],2)==[[1,1,1],[2,2,2],[5,5,5]])
            assert(False)
        except ValueError:
            assert(True)
            
    def testRemoveOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.remove([[1,2,3],[4,5,6],[7,8,9]],2)==[[1,2,3],[4,5,6],[0,0,0]])
        try:
            functionsClass.remove([[1,2,3],[3,4,5]],7)
            assert(False) #asa sa facem la examen
        except ValueError:
            assert(True)
            
    def testReplaceOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        try:
            assert(functionsClass.replace([[1,1,1],[2,2,2],[3,3,3]],4,0,9)==[[1,1,9],[2,2,2],[3,3,3]])
            assert(False)
        except ValueError:
            assert(True)
    
    def testSortedListOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.sortTheList([[3,3,3],[2,2,2],[4,4,4],[1,1,1],[5,5,5]])==(3,1,0,2,4))
        try:
            assert(functionsClass.sortTheList([[3,3,3],[2,2,2],[4,4,4],[1,1,1],[5,5,5]])==(3,1,0,4,2))
            assert(False)
        except AssertionError:
            assert(True)
        
    def testSpecificListOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        try:
            assert(functionsClass.createTheSpecificList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[[1,1,1],[2,2,2],[3,3,3]])
            assert(False)
        except AssertionError:
            assert(True)
        
    def testAvarageSumeOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.avarageSume(1, 3, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==3.0)
        try:
            assert(functionsClass.avarageSume(0, 4, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==2.5)
            assert(False)
        except AssertionError:
            assert(True)
            
    def testMinSumeOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.minSume(1, 3, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==3.0)
        try:
            assert(functionsClass.minSume(0, 4, [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])==2.5)
            assert(False)
        except AssertionError:
            assert(True)
    
    def testTopContestantsOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert (functionsClass.topContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3)==[[4,5,5,5,5],[2,4,4,4,4],[1,3,3,3,3]])
        try:
            assert (functionsClass.topContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3)==[[4,5,5,5,5],[2,4,4,4,4],[1,2,2,2,2]])
            assert(False)
        except AssertionError:
            assert(True)
            
    def testTopProblemContestantsOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert (functionsClass.topProblemContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3,2)==[[4,5],[2,4],[1,3]])
        try:
            assert (functionsClass.topProblemContestants([[2,2,2],[3,3,3],[4,4,4],[1,1,1],[5,5,5]], 3,2)==[[4,5],[2,4],[1,2]])
            assert(False)
        except AssertionError:
            assert(True)
            
    def testRemoveContestantsOp(self):
        from src.functions import functionsClass
        functionsClass = functionsClass()
        assert(functionsClass.removeContestantsList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[0,1])
        
        try:
            assert (functionsClass.removeContestantsList([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]], 30, '<')==[0,1,2])
            assert(False)
        except AssertionError:
            assert(True)