import numpy as np
class DSAListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next


class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertFirst(self, data):
        newNode = DSAListNode(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def insertLast(self, data):
        newNode = DSAListNode(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.length += 1

    def deleteFirst(self):
        if self.head is None:
            raise ValueError("Linked list is empty")
        data = self.head.getData()
        self.head = self.head.getNext()
        if self.head is None:
            self.tail = None
        self.length -= 1
        return data

    def deleteLast(self):
        if self.tail is None:
            raise ValueError("Linked list is empty")
        data = self.tail.getData()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            node = self.head
            while node.getNext() != self.tail:
                node = node.getNext()
            node.setNext(None)
            self.tail = node
        self.length -= 1
        return data

    def delete(self, data):
        if self.head is None:
            raise ValueError("Linked list is empty")
        if self.head.getData() == data:
            return self.deleteFirst()
        if self.tail.getData() == data:
            return self.deleteLast()
        node = self.head
        while node.getNext() is not None:
            if node.getNext().getData() == data:
                data = node.getNext().getData()
                node.setNext(node.getNext().getNext())
                self.length -= 1
                return data
            node = node.getNext()
        raise ValueError("Data not found in linked list")

    def contains(self, data):
        node = self.head
        while node is not None:
            if node.getData() == data:
                return True
            node = node.getNext()
        return False
    
    def findNodeInfo(self, shop):
        node = self.head
        while node is not None:
            if node.getData()[1] == shop:
                data = node.getData()
                return data
            node = node.getNext()
    
    def allnodeInfo(self):
        node = self.head
        info = np.zeros(self.length, dtype = object)
        i = 0
        while node is not None:
            info[i] = (float(node.getData()[4]), node.getData()[1], node.getData()[2], node.getData()[3], node.getData()[0])
            node = node.getNext()
            i = i+1

        return info


    def displayLL(self):
        node = self.head
        print("\nAll shops in the category:", node.getData()[2])
        print("")
        while node is not None:
            print("Shop Number: ", node.getData()[0])
            print("Shop Name: ", node.getData()[1])
            print("Category: ", node.getData()[2])
            print("Location: ", node.getData()[3])
            print("Rating: ", node.getData()[4])
            print("")
            node = node.getNext()

    def getLength(self):
        return self.length

    def isEmpty(self):
        return self.length == 0
    
    def iterator(self):
        return DSALinkedListIterator(self.head)


class DSALinkedListIterator:
    def __init__(self, head):
        self.current = head

    def hasNext(self):
        return self.current is not None

    def next(self):
        if self.current is None:
            raise StopIteration
        data = self.current.getData()
        self.current = self.current.getNext()
        return data
    

    