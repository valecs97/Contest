'''
Created on Oct 18, 2016

@author: Vitoc
'''

class algorithmsClass:


    def __init__(self):
        return
    
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