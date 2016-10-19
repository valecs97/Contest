'''
Created on Oct 11, 2016

@author: Vitoc
'''
from src.consoleUI import consoleUIClass
from testFunction.testMain import testMainClass


if __name__ == '__main__':
    pass


'''
Problem proposed by the teacher , remove any sum score than is greater than a given number
'''
'''
def removeSpecificItems(l,mx):
    for i in range (len(l)):
        if (l[i][0]+l[i][1]+l[i][2]>mx):
            remove(l,i)
'''


def main():
    consoleUI = consoleUIClass()
    testClass = testMainClass()
    testClass.performAllTests()
    consoleUI.run()
    del consoleUI,testClass

main()
