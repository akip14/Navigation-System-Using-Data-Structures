from graphs import *
from linkedlist import *
from graphedges import *

graph = DSAGraph()



try:
    with open("Shop_List.csv", 'r') as csv_file:
        csv_reader = csv_file.readlines()

    for row in csv_reader:
        values = row.strip().split(",")
        graph.addVertex(values[0], values[1], values[2], values[3], values[4])
        
except:
    print("Could not open the file")

addAllEdges(graph)
graph.displayAsList()
graph.addVertex("hello","df","fd","df","df")
graph.updateInfo("1", "shop", "category", "address", "rating")
graph.getInfo("1")
graph.deleteVertex("20")


graph.removeEdge("1","8")


graph.breadthFirstSearch("1")

print(graph.dfs("2", "10"))
print(graph.bfs("1", "10"))
graph.comparePaths("1","4")

print(graph.getCategory("2"))



