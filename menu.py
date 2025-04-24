from graphs import *
from linkedlist import *
from graphedges import *
from ResizeHash import *
import numpy as np

graph = DSAGraph()
hashTable = DSAHashTable(10)

try:
    with open("Shop_List.csv", 'r') as csv_file:
        csv_reader = csv_file.readlines()

    for row in csv_reader:
        values = row.strip().split(",")
        graph.addVertex(values[0], values[1], values[2], values[3], values[4])
        
except:
    print("Could not open the file")

addAllEdges(graph)
shops_arr = graph.shopsList()

for element in shops_arr:
    hashTable.put(graph.getCategory(element), graph.getLabel(element), graph.getShop(element), graph.getAddress(element), graph.getRating(element))

choice = ""
while choice != "q":
    print("\nMenu:")
    print("a) Display adjacency list of graph")
    print("b) Add shop node")
    print("c) Delete a shop node")
    print("d) Update shop information")
    print("e) Add edge")
    print("f) Delete edge")
    print("g) Graph traversal from source to destination shop")
    print("h) Find information for particular shop")
    print("i) Find all shop information from a particular category")
    print("j) Rank all shops by rating from a particular category")
    print("q) Quit the program")
    


    choice = input("Enter a choice: ")

    if choice == "a":
        graph.displayAsList()

    elif choice == "b":
        number = input("What is the shop number? ")
        shop = input("What is the shop name? ")
        category = input("What is the category of the shop? ")
        address = input("What is the location of the shop? ")
        rating = input("What is the rating of the shop? ")
        graph.addVertex(number,shop,category,address,rating)
        hashTable = DSAHashTable(10)
        shops_arr = graph.shopsList()
        for element in shops_arr:
            hashTable.put(graph.getCategory(element), graph.getLabel(element), graph.getShop(element), graph.getAddress(element), graph.getRating(element))
                        
    elif choice == "c":
        number = input("What is the shop number? ")
        graph.deleteVertex(number)
        hashTable = DSAHashTable(10)
        shops_arr = graph.shopsList()
        for element in shops_arr:
            hashTable.put(graph.getCategory(element), graph.getLabel(element), graph.getShop(element), graph.getAddress(element), graph.getRating(element))

    elif choice == "d":
        number = input("What is the shop number? ")
        shop = input("What is the new shop name? ")
        category = input("What is the new category of the shop? ")
        address = input("What is the new location of the shop? ")
        rating = input("What is the new rating of the shop? ")
        graph.updateInfo(number,shop,category,address,rating)
        hashTable = DSAHashTable(10)
        shops_arr = graph.shopsList()
        for element in shops_arr:
            hashTable.put(graph.getCategory(element), graph.getLabel(element), graph.getShop(element), graph.getAddress(element), graph.getRating(element))
    
    elif choice == "e":
        label1 = input("What is the first shop number? ")
        label2 = input("What is the second shop number? ")
        graph.addEdge(label1,label2)

    elif choice == "f":
        label1 = input("What is the first shop number? ")
        label2 = input("What is the second shop number? ")
        graph.removeEdge(label1,label2)

    elif choice == "g":
        source = input("What is the starting shop number? ")
        destination = input("What is the destination shop number? ")
        graph.comparePaths(source, destination)

    elif choice == "h":
        shop = input("What is the shop name? ")
        hashTable.findShop(shop)
    
    elif choice == "i":
        category = input("What category do you want to search? ")
        hashTable.displayshopsCategory(category)
    
    elif choice == "j":
        category = input("What category do you want to be ranked? ")
        hashTable.maxHeap(category)
    else:
        None
