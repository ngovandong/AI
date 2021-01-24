from collections import defaultdict
from queue import PriorityQueue
class Node:
    def __init__(self,name,par=None,w=0,h=0):
        self.name=name
        self.w=w
        self.par=par
        self.h=h
    def display(self):
        print(self.name,self.par)
    def __lt__(self, value):
        if value==None : return False
        return self.w+self.h<value.w+value.h
    def __eq__(self, value):
        if value==None : return False
        return self.name==value.name

graph=defaultdict(list)
graph['A']=['B',2,'C',1,'D',3,6]
graph['B']=['E',5,'F',4,3]
graph['C']=['G',6,'H',3,4]
graph['D']=['I',2,'J',4,5]
graph['E']=[3]
graph['F']=['K',2,'L',1,'M',4,1]
graph['G']=[6]
graph['H']=['N',2,'O',4,2]
graph['I']=[5]
graph['J']=[4]
graph['K']=[2]
graph['L']=[0]
graph['M']=[4]
graph['N']=[0]
graph['O']=[4]


def checkInArray(ele, collection):
    for i in collection:
        if ele==i:
            return True
    return False

def path(state):
    print(state.name)
    if state.par!=None:
        path(state.par)
    else:
        return
         
def display(collection):
    l=[]
    newlist=collection.queue[:]
    for ele in newlist:
        l.append(ele.name+'('+str(ele.w)+'+'+str(ele.h) +')')
    print(l)

def Astar(initialState,goalTest):
    frontier=PriorityQueue()
    explored=PriorityQueue()
    frontier.put(initialState)
    while not frontier.empty():
        display(frontier)
        state=frontier.get()
        explored.put(state)
        if state==goalTest:
            print('Duong di:')
            path(state)
            return
        i=0
        while i<len(graph[state.name])-1:
            name=graph[state.name][i]
            temp=Node(name,state,state.w+graph[state.name][i+1],graph[name][-1])
            if temp not in frontier.queue and temp not in explored.queue:
                frontier.put(temp)
            i+=2
        
Astar(Node('A',None,0,graph['A'][-1]),Node('N'))