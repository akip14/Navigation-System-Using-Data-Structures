from graphs import *
from linkedlist import *

def addAllEdges(graph):
    graph.addEdge("1","2")
    graph.addEdge("1","4")
    graph.addEdge("1","5")
    graph.addEdge("2","3")
    graph.addEdge("2","4")
    graph.addEdge("2","6")
    graph.addEdge("3","5")
    graph.addEdge("4","7")
    graph.addEdge("4","9")
    graph.addEdge("5","8")
    graph.addEdge("6","7")
    graph.addEdge("7","8")
    graph.addEdge("7","10")
    graph.addEdge("7","9")
    graph.addEdge("8","9")
    graph.addEdge("9","10")
    return graph


