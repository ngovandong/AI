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



#manner2:
""" from graph import Node, Graph
import heapq
import pandas as pd
def update_cost(g, current_node, prev_node):
    if g.get_edge(prev_node, current_node) is not None:
        # print(g.get_edge(prev_node, current_node))
        if current_node.cost > prev_node.cost + graph.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + graph.get_edge(prev_node, current_node)[2]
def find_by_label(array_of_node, node):
    for idx, n in enumerate(array_of_node):
        if n == node:
            return idx
    return -1
def update_frontier(frontier, new_node):
    # Update trạng thái của frontier
    index = find_by_label(frontier, new_node)
    if index >= 0:
        if frontier[index] > new_node:
            frontier[index] = new_node
def a_star_search(graph, initial_state, goalTest):
    frontier = list()
    explored = list()
    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)
    df = pd.DataFrame(columns=["Frontier", "Explored"])
    pd.set_option("max_colwidth", None)
    while len(frontier) > 0:
        to_append = [
            list(map(lambda x: x.get_label(), frontier)),
            list(map(lambda x: x.get_label(), explored))
        ]
        series = pd.Series(to_append, index=df.columns)
        df = df.append(series, ignore_index=True)
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == goalTest:
            print(df)
            return True
        for neighbor in state.neighbors():
            update_cost(graph, current_node=neighbor, prev_node=state)
            # update A* cost of current node
            neighbor.compare_mode = neighbor.cost + neighbor.goal_cost
            if neighbor.get_label() not in list(set([e.get_label() for e in frontier + explored])):
                heapq.heappush(frontier, neighbor)
            elif find_by_label(array_of_node=frontier, node=neighbor) >= 0:
                update_frontier(frontier=frontier, new_node=neighbor)
    return False
if __name__ == "__main__":
    graph = Graph()
    graph.add_node_from(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])
    graph.add_edges_from(
        [
            ("A", "B", 2),
            ("A", "C", 1),
            ("A", "D", 3),
            ("B", "E", 5),
            ("B", "F", 4),
            ("C", "G", 6),
            ("C", "H", 3),
            ("D", "I", 2),
            ("D", "J", 4),
            ("F", "K", 2),
            ("F", "L", 1),
            ("F", "M", 4),
            ("H", "N", 2),
            ("H", "O", 4),
        ],
    )
    # initial setup
    graph.nodes[0].goal_cost = 6  # goal_cost của node A = 6
    graph.nodes[1].goal_cost = 3  # goal_cost của node B = 3
    graph.nodes[2].goal_cost = 4  # goal_cost của node C = 4
    graph.nodes[3].goal_cost = 5  # goal_cost của node D = 5
    graph.nodes[4].goal_cost = 3  # goal_cost của node E = 3
    graph.nodes[5].goal_cost = 1  # goal_cost của node F = 1
    graph.nodes[6].goal_cost = 6  # goal_cost của node G = 6
    graph.nodes[7].goal_cost = 2  # goal_cost của node H = 2
    graph.nodes[8].goal_cost = 5  # goal_cost của node I = 5
    graph.nodes[9].goal_cost = 4  # goal_cost của node J = 4
    graph.nodes[10].goal_cost = 2  # goal_cost của node K = 2
    graph.nodes[11].goal_cost = 0  # goal_cost của node L = 0
    graph.nodes[12].goal_cost = 4  # goal_cost của node M = 4
    graph.nodes[13].goal_cost = 0  # goal_cost của node N = 0
    graph.nodes[14].goal_cost = 4  # goal_cost của node O = 4
    graph.nodes[0].cost = 0  # cost tu A -> A = 0
    graph.set_compare_mode(Node.A_STAR)
    result = a_star_search(graph=graph, initial_state=graph.nodes[0], goalTest=graph.nodes[11])
    print(result) """
