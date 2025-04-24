import numpy as np
from linkedlist import *
from heap import *

class DSAHashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.state = "free"


class DSAHashTable:
    def __init__(self, size):
        self.size = size
        self.num_entries = 0
        self.threshold = 0.5
        self.hashArray = np.empty(size, dtype = object)
        self.linked_list = np.empty(size, dtype = object) 

    def size_of(self):
        return self.size

    def hasKey(self, key):
        return key % self.size
    
    def loadFactor(self):
        loadfactor = self.num_entries / self.size
        return loadfactor
    
    def findCategory(self, key):
        key_index = self.hashing(key)
    
    def hashing(self, key):
            a = 63689
            b = 378551
            hashIdx = 0
            for ii in range(0, len(key)):
                hashIdx = (hashIdx * a) + ord(key[ii])
                a *= b

            return hashIdx % self.size

    
    def put(self, key, value, shop, address, rating):
        l = self.loadFactor()
        if l >= self.threshold:
            self.resize(self.size * 2)
        entry = DSAHashEntry(key, value)
        hashValue = self.hashing(key)
        
        new = 1
        for i in range(0,self.size):
            if self.hashArray[i] != None:
                if self.hashArray[i].key == key:
                    new = 0
                    key_index = i
            
        break_while = 0
        i = 0
        while i < self.size and break_while == 0:
        
            if self.hashArray[hashValue] is None or (new == 1 and self.hashArray[hashValue].state != "used"):
                self.linked_list[hashValue] = DSALinkedList()
                self.linked_list[hashValue].insertFirst(np.array([value, shop, key, address, rating]))
                self.hashArray[hashValue] = entry
                self.hashArray[hashValue].state = "used"
                self.num_entries += 1
                break_while = 1
                
            
            elif new == 0:
                self.linked_list[key_index].insertFirst(np.array([value, shop, key, address, rating]))
                break_while = 1
            
            else:
                offset = 1
                hashValue = (hashValue + offset) % self.size
                i += 1
    


    def displayshopsCategory(self, key):
        existing_category = 0
        for i in range(0,self.size):
            if self.hashArray[i] != None:
                if self.hashArray[i].key == key:
                    key_index = i
                    existing_category = 1
        
        if existing_category == 1:
            self.linked_list[key_index].displayLL()
        else:
            print("No shops are from that category")
    
    def maxHeap(self, key):
        existing_category = 0
        for i in range(0,self.size):
            if self.hashArray[i] != None:
                if self.hashArray[i].key == key:
                    key_index = i
                    
                    existing_category = 1
        
        if existing_category == 1:
            array = self.linked_list[key_index].allnodeInfo()
            arr = heapSort(array,len(array))
            print("The list of the shops in the category", key + " ranked on based on rating:\n")
            for element in arr:
                print("Shop Number:", element[4])
                print("Shop Name:", element[1])
                print("Category:", element[2])
                print("Location", element[3])
                print("Rating", element[0])
                print("")
        else:
            print("No shops are from that category")
        

    def findShop(self, shop):
        found = 0
        data = None
        for i in range(0,self.size):
            try:
                result = self.linked_list[i].findNodeInfo(shop)
                if result is not None:
                    found = 1
                    print("Found the shop", shop + "!")
                    print("Shop Number: ", result[0])
                    print("Shop Name: ", result[1])
                    print("Category: ", result[2])
                    print("Location: ", result[3])
                    print("Rating: ", result[4])
                    print("")
            except:
                None
        if found == 0:
            print("No matching shop was found with name:", shop,"\n")


    def resize(self, new_size):
        new_array = np.empty(new_size)
        old_array = self.hashArray
        self.hashArray = new_array
        self.size = new_size
        self.num_entries = 0 
        for entry in old_array:
            if entry is not None and entry.state == "used":
                self.put(entry.key, entry.value)


