'''
Created on Oct 11, 2016

@author: Vitoc
'''


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
    from testFunction.testMain import testMainClass
    testMainClass = testMainClass()
    testMainClass.performAllTests()
    chooseUI()

def chooseUI():
    print("Please choose between :\n1.Command line UI\n2.Interface UI\n3.Exit")
    while True:
        key = input('Input command:')
        if key == '1':
            from src.consoleUI import consoleUIClass
            consoleUIClassModule = consoleUIClass()
            consoleUIClassModule.run()
            return
        elif key == '2':
            from src.interfaceUI import interfaceUIClass
            interfaceUIClassModule = interfaceUIClass()
            interfaceUIClassModule.run()
            return
        elif key== '3':
            return
        else:
            print("You have entered a wrong key , please press 1,2 or 3 and then Enter")

main()
