from collections import defaultdict
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
graph['A']=['B','C','D']
graph['B']=['E','F']
graph['C']=['G','H']
graph['D']=['I','J']
graph['F']=['K','L','M']
graph['H']=['N','O']

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
    for ele in collection:
        l.append(ele.name)
    print(l)

def BFS(initialState,goalTest):
    frontier=[]
    explored=[]
    frontier.append(initialState)
    while frontier:
        display(frontier)
        state=frontier.pop()
        explored.append(state)
        if state==goalTest:
            print('Duong di:')
            path(state)
            return
        graph[state.name].reverse()
        for neigbor in graph[state.name]:
            temp=Node(neigbor,state)
            if not checkInArray(temp,frontier) and not checkInArray(temp,explored):
                frontier.append(temp)

BFS(Node('A'),Node('O'))