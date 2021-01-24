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
graph['A']=['B',2,'C',1,'D',3]
graph['B']=['E',5,'F',4]
graph['C']=['G',6,'H',3]
graph['D']=['I',2,'J',4]
graph['F']=['K',2,'L',1,'M',4]
graph['H']=['N',2,'O',4]

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

def UCS(initialState,goalTest):
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
        while i<len(graph[state.name]):
            temp=Node(graph[state.name][i],state,state.w+graph[state.name][i+1])
            if temp not in frontier.queue and temp not in explored.queue:
                frontier.put(temp)
            i+=2
        
UCS(Node('A'),Node('O'))