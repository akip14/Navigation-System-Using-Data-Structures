from linkedlist import *
from stackQ import *
import numpy as np

class DSAGraphNode:
    def __init__(self, label, shop, category, address, rating):
        self.label = label
        self.shop = shop
        self.category = category
        self.address = address
        self.rating = rating
        self.adjacent = DSALinkedList()

    def addAdjacent(self, label):
        self.adjacent.insertLast(label)

    def removeAdjacent(self, label):
        self.adjacent.delete(label)

    def getAdjacent(self):
        return self.adjacent

    def getLabel(self):
        return self.label

    def getShop(self):
        return self.shop
    
    def getCategory(self):
        return self.category
    
    def getAddress(self):
        return self.address
    
    def getRating(self):
        return self.rating
    



class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()

    def Adjacencylist(self, label):
        node = self.findVertex(label)
        adjacencylist = set()
        start_node = self.vertices.head
        while start_node is not None:
            if self.isAdjacent(label, start_node.getData().getLabel()):
                adjacencylist.add(start_node.getData().getLabel())
            start_node = start_node.getNext()
        return sorted(adjacencylist)

    def addVertex(self, label, shop, category, address, rating):
        list1 = self.shopsList()
        try:
            int1 = int(label)
            if label not in list1:
                node = DSAGraphNode(label, shop, category, address, rating)
                self.vertices.insertLast(node)
            else:
                print("This node already exists")
        except:
            print("The shop number must be an integer")
    
    def deleteVertex(self, label):
        node = self.findVertex(label)
        if node is not None:
            self.vertices.delete(node)
        else:
            print("Cannot delete an unknown shop node")


    def addEdge(self, label1, label2):
        node1 = self.findVertex(label1)
        node2 = self.findVertex(label2)

        if node1 is not None and node2 is not None:
            if node1.getAdjacent().contains(label2) == True:
                print("Edge already exists")
            else:
                node1.addAdjacent(label2)
                node2.addAdjacent(label1)
                print("Edge added!")
        else:
            print("At least one of the shop number inputs does does exist")
    
    def removeEdge(self, label1, label2):
        node1 = self.findVertex(label1)
        node2 = self.findVertex(label2)
        
        try: 
            if node1 is not None and node2 is not None:
                node1.removeAdjacent(label2)
                node2.removeAdjacent(label1)
                print("Edge removed!")
        except:
            print("There is no pathway between the two shops")

    def updateInfo(self, label, shop, category, address, rating):
        list1 = self.shopsList()
        if label in list1:
            node = self.findVertex(label)
            node.shop = shop
            node.category = category
            node.address = address
            node.rating = rating
            print("Shop Info Updated!")
        else:
            print("Cannot update unknown shop")

    def getInfo(self, label):
        print()
        list1 = self.shopsList()
        if label in list1:
            node = self.findVertex(label)
            print("Shop number: " + node.label)
            print("Shop Name: " + node.shop)
            print("Category: " + node.category)
            print("Location: " + node.address)
            print("Rating: " + node.rating)
        else:
            print("No such shop exists")

    def getCategory(self, label):
        list1 = self.shopsList()
        category1 = "Empty"
        if label in list1:
            node = self.findVertex(label)
            category1 = node.category
        return category1
    
    def getLabel(self, label):
        list1 = self.shopsList()
        label1 = "Empty"
        if label in list1:
            node = self.findVertex(label)
            label1 = node.label
        return label1
    
    def getShop(self, label):
        list1 = self.shopsList()
        shop1 = "Empty"
        if label in list1:
            node = self.findVertex(label)
            shop1 = node.shop
        return shop1
    
    def getAddress(self, label):
        list1 = self.shopsList()
        address1 = "Empty"
        if label in list1:
            node = self.findVertex(label)
            address1 = node.address
        return address1

    def getRating(self, label):
        list1 = self.shopsList()
        rating1 = "Empty"
        if label in list1:
            node = self.findVertex(label)
            rating1 = node.rating
        return rating1

    def hasVertex(self, label):
        return self.findVertex(label) is not None

    def findVertex(self, label):
        node = self.vertices.head
        while node is not None:
            if node.getData().getLabel() == label:
                return node.getData()
            node = node.getNext()
        return None

    def shopsList(self):
        shops_list = np.zeros([0], dtype= int)
        node = self.vertices.head
        while node is not None:
            label = node.getData().getLabel()
            node1 = self.findVertex(label)
            shops_list = np.append(shops_list, node1.label)
            node = node.getNext()
        return shops_list

    def getVertexCount(self):
        return self.vertices.getLength()

    def getEdgeCount(self):
        count = 0
        node = self.vertices.head
        while node is not None:
            count += node.getData().getAdjacent().getLength()
            node = node.getNext()
        return count // 2  # double counting each edge

    def getVertex(self, label):
        return self.findVertex(label)

    def getAdjacent(self, label):
        node = self.findVertex(label)
        if node is not None:
            return node.getAdjacent()
        return None

    def isAdjacent(self, label1, label2):
        node1 = self.findVertex(label1)
        node2 = self.findVertex(label2)

        if node1 is not None and node2 is not None:
            if node1.getAdjacent().contains(label2):
                return 1
        return 0

    def displayAsList(self):
        shops = self.shopsList()
        print("Adjacency list of graph:")
        for element in shops:
            print()
            shop = self.findVertex(element)
            print(shop.label + ":", end = " ")
            node = shop.getAdjacent().head
            while node is not None:
                print(node.getData(), end = " ")
                node = node.getNext()
        print()


    def breadthFirstSearch(self, label):
        bfs_list = np.zeros([0], dtype = int)
        self.Q = Circular_Queue()
        visited = set()
        self.Q.enqueue(label)
        visited.add(label)
        while self.Q.count != 0:
            m = self.Q.dequeue()
            #print(m, end = " ")
            bfs_list = np.append(bfs_list, m)

            for w in self.Adjacencylist(m):
                if w not in visited:    
                    visited.add(w)
                    self.Q.enqueue(w)
        print()
        return bfs_list


    def bfs(self, label1, label2):
        list1 = self.shopsList()
        try:
            if label1 in list1:
                bfs_shops = self.breadthFirstSearch(label1)
            else:
                print("The first shop number does not exist")
        except:
            print("There is no valid path between the shops")

        i = 1
        counter = 1
        if label1 in bfs_shops and label2 in bfs_shops:
            print("A breadth first search starting from " + label1 + " to " + label2 + " is:", end = ' ')
            while bfs_shops[i] != label2 and i<(len(bfs_shops)):
                counter += 1
                i += 1
            
            for j in range(0,counter+1):
                print(bfs_shops[j], end = " ")
            print()
        else:
            print("Invalid input of shop/s")


        return counter


    def depthFirstSearch(self, label, visited, dfs_list):
        if label not in visited:
            #print(label, end = " ")
            dfs_list.append(label)
            visited.add(label)
            for w in self.Adjacencylist(label):
                self.depthFirstSearch(w, visited, dfs_list)
        return dfs_list
    
    def dfs(self, label1, label2):
        visited = set()
        dfs_list = []
        list1 = self.shopsList()
        try:
            
            if label1 in list1:
                dfs_shops = self.depthFirstSearch(label1, visited, dfs_list)
            else:
                print("The first shop number does not exist")
        except:
            print("There is no valid path between the shops")

        i = 1
        counter = 1
        if label1 in dfs_shops and label2 in dfs_shops:
            print("A depth first search starting from " + label1 + " to " + label2 + " is:", end = ' ')
            while dfs_shops[i] != label2 and i<(len(dfs_shops)):
                counter += 1
                i += 1
            
            for j in range(0,counter+1):
                print(dfs_shops[j], end = " ")
            print()
        else:
            print("Invalid input of shop/s")

        return counter
    
    def comparePaths(self, label1, label2):
        list1 = self.shopsList()
        if label1 in list1 and label2 in list1:
            try:
                bfs_length = self.bfs(label1, label2)
                dfs_length = self.dfs(label1, label2)

                if bfs_length < dfs_length:
                    print("The shortest path is via breadth first search")
                elif dfs_length < bfs_length:
                    print("The shortest path is via depth first search")
                else:
                    print("Both paths have the same length")
                    
            except:
                print("Path between the two given shops does not exist")
        
        elif label1 in list1 and label2 not in list1:
            print("The second shop node input is invalid")

        elif label1 not in list1 and label2 in list1:
            print("The first shop node input is invalid")
        
        else:
            print("Both shop node inputs are invalid")



                    

