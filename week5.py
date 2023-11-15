#----------QUESTION1----------
from week4 import Stack
from week4 import LinkedList
from week4 import Node


def PostFix(exp):
    stack = Stack()
    operations = ['+', '-', '*', '/']
    op1 = None
    op2 = None
    #operation = None
    for i in range(len(exp)):
        if exp[i] not in operations:
            stack.push(exp[i])
        else:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if exp[i] == '+':
                stack.push(op1 + op2)
            elif exp[i] =='*':
                stack.push(op1 * op2)
            elif exp[i] == '-':
                stack.push(op1 - op2)
            elif exp[i] == '/':
                stack.push(op1 / op2)
    return stack.top()
#print(PostFix('28+41+*'))


#----------QUESTION2----------


class BinarySearchTree():
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
    def addchild(self, child):
        child = BinarySearchTree(child, self)
        if self.value >= child.value:
            if self.left == None:
                self.left = child
            elif self.right == None and child.value >= self.left.value:
                self.right = child
            else:
                print("Left child greater than right; and only two children allowed")
        else:
            print("Child cannot be greater than parent")
        return
    #def height(self):


    def printree(self):
        print(self.value, self.left.value, self.right.value)
        return
#tree = BinarySearchTree(10)
#tree.addchild(4)
#tree.addchild(9)
#tree.printree()


class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, val):
        if self.value:
            if self.left == None:
                self.left = BinaryTree(val)
            else:
                print("value already there")
        return

    def addRight(self, val):
        if self.value:
            if self.right == None:
                self.right = BinaryTree(val)
            else:
                print("value already there")
        return

    def InorderDisplay(self):
        out = []
        if self.left:
            self.left.InorderDisplay()
        out.append(self.value)
        if self.right:
            self.right.InorderDisplay()
        return out

    def Height(self):
        if self.left == None and self.right == None:
            return 0
        else:
            return (max(self.left.Height(), self.right.Height())+1)

    def isBST(self):
        inorder = self.InorderDisplay()
        if sorted(inorder) == inorder:
            return True
        else:
            return False



root = BinaryTree(100)
root.addLeft(20)
root.addRight(50)
root.left.addLeft(10)
root.right.addRight(6)
root.InorderDisplay()
print(root.Height())
print(root.isBST())


#----------QUESTION3----------

class Song():
    def __init__(self, title, year, duration: float):
        self.title = title
        self.year = year
        self.duration = duration
        self.next = None

class Playlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def appendSong(self, title, year, duration):
        songNode = Song(title, year, duration)
        if self.head is None:
            self.head = songNode
            self.tail = songNode
        else:
            self.tail.next = songNode 
            self.tail = self.tail.next
        self.count += 1

    def prependSong(self, title, year, duration):
        songNode = Song(title, year, duration)
        if self.head is None:
            self.head = songNode
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

    def printSongs(self):
        pointer = self.head
        if self.isempty() == True:
            return "Empty"
        else:
            while pointer is not None:
                print(pointer.title)
                pointer = pointer.next

    def search(self, name):
        pointer = self.head
        pos = 1
        if self.isempty() == False:
            while pointer is not None:
                if pointer.title == name:
                    found = "Element found at position: " + str(pos)
                    return found
                pointer = pointer.next    
                pos += 1
        return "No such element found"
#chill = Playlist()
#chill.appendSong("Winds", 2022, 3)
#chill.appendSong("Dance of the Corpses", 2023, 2)
#chill.appendSong("Pills on my mind", 2022, 3)
#chill.printSongs()






























