from collections import defaultdict
from queue import PriorityQueue
class Node:
    def __init__(self,name,par=None,w=0):
        self.name=name
        self.w=w
        self.par=par
    def display(self):
        print(self.name,self.par)
    def __lt__(self, value):
        if value==None : return False
        return self.w<value.w
    def __eq__(self, value):
        if value==None : return False
        return self.name==value.name

graph=defaultdict(list)
graph['A']=['B','C','D',6]
graph['B']=['E','F',3]
graph['C']=['G','H',4]
graph['D']=['I','J',5]
graph['E']=[3]
graph['F']=['K','L','M',1]
graph['G']=[6]
graph['H']=['N','O',2]
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
        l.append(ele.name+'('+str(ele.w)+')')
    print(l)

def GBFS(initialState,goalTest):
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
            temp=Node(name,state,graph[name][-1])
            if temp not in frontier.queue and temp not in explored.queue:
                frontier.put(temp)
            i+=1
        
GBFS(Node('A',None,graph['A'][-1]),Node('M'))