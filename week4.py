#----------QUESTION1----------

class Stack():
    def __init__(self):
        self.stack = []
    
    def getsize(self):
        return len(self.stack)
    
    def push(self,element):
        self.stack.append(element)
        return
    
    def pop(self):
        if self.isempty() == False:
            self.stack.pop()
        else:
            return "No elements to pop"
        return
    
    def top(self):
        if self.isempty() == False:
            return self.stack[-1]
        else:
            return "No elements to pop"
        return
    
    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def display(self):
        if self.isempty() == False:
            return self.stack[::-1]
        else:
            return "No elements to pop"
        return
'''
santosh = Stack()
santosh.push(8)
santosh.push(2)
santosh.push(9)
santosh.pop()
santosh.push(1)
print(santosh.getsize())
print(santosh.top())
print(santosh.isempty())
print(santosh.display())
'''

#----------QUESTION2----------

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

    def getVal(self):
        return self.value

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self,data):
        dataNode = Node(data)
        if self.head is None:
            self.head = dataNode
            self.tail = dataNode
        else:
            self.tail.next = dataNode 
            self.tail = self.tail.next
        self.count += 1

    def prepend(self,data):
        data = Node(data)
        if self.head is None:
            self.head = data
        else:
            data.next = self.head
            self.head = data
        self.count += 1

    def length(self):
        return self.count

    def isempty(self):
        if self.count == 0:
            return True
        else:
            return False

    def display(self):
        pointer = self.head
        if self.isempty() == True:
            return "Empty"
        else:
            while pointer is not None:
                print(pointer.value)
                pointer = pointer.next

    def search(self, item):
        pointer = self.head
        pos = 1
        if self.isempty() == False:
            while pointer is not None:
                if pointer.value == item:
                    found = "Element found at position: " + str(pos)
                    return found
                pos += 1
                pointer = pointer.next
        return "No such element found"
    
    def delete(self, item):
        pointer = self.head
        if self.isempty() == False:
            while pointer is not None:
                if pointer.next.value == item:
                    deleted = pointer.next.value
                    pointer.next = pointer.next.next
                    return str(deleted)+" was deleted"
                pointer = pointer.next
        return "No such element found"


l = LinkedList()
l.append(1)
l.append(3)
l.append(5)
l.prepend(8)
l.display()
print(l.search(8))















































