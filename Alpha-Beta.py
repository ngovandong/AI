from graph import Node, Graph
import math
def MaxValue(node,alpha,beta):
    if len(node.children)==0:
        return node
    node.value=-math.inf
    for child in node.children:
        temp=MinValue(child,alpha,beta)
        if temp.value> node.value:
            node.value=temp.value
        if child.value>= beta:
            return child
        if child.value> alpha:
            alpha=child.value
    return node

def MinValue(node,alpha,beta):
    if len(node.children)==0:
        return node
    node.value=math.inf
    for child in node.children:
        temp=MaxValue(child,alpha,beta)
        if temp.value <node.value:
            node.value=temp.value
        if child.value<= alpha:
            return child
        if child.value < beta:
            beta=child.value
    return node

def alphaBetaSearch(node):
    MaxValue(node,-math.inf,math.inf)

g=Graph()
g.add_node_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])
g.add_edges_from(
        [('A', 'B'),
         ('A', 'C'),
         ('B', 'D'),
         ('B', 'E'),
         ('C', 'F'),
         ('C', 'G'),
         ('C', 'H'),
         ('F', 'I'),
         ('F', 'J'),
         ('G', 'K'),
         ('G', 'L'),
         ('I', 'M'),
         ('I', 'N')]
    )

g.nodes[3].value = 3
g.nodes[4].value = 5
g.nodes[7].value = 4
g.nodes[9].value = 5
g.nodes[10].value = 7
g.nodes[11].value = 8
g.nodes[12].value = 0
g.nodes[13].value = 7
alphaBetaSearch(g.nodes[0])

print(g.nodes[0].value)
