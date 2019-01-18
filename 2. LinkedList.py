class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def  getSize(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size = size + 1
            actualNode = actualNode.nextNode

        print('Length of Linked List is', size)

    def insertEnd(self, data):
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverse(self):
        if self.head is None:
            print('Linked List is empty')
            return

        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        data = int(input('Enter the number : '))
        
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


linkedlist = LinkedList()

while True:
    print('*'*25)
    print('1 for insertion at start')
    print('2 for insertion at end')
    print('3 for deletion')
    print('4 for traversal')
    print('5 to get size')
    print('0 to exit')
    print('*'*25)
    
    choice = int(input('Enter your choice : '))

    if choice == 1:
        linkedlist.insertStart(int(input('Enter the number : ')))
    if choice == 2:
        linkedlist.insertEnd(int(input('Enter the number : ')))
    if choice == 3:
        linkedlist.remove()
    if choice == 4:
        linkedlist.traverse()
    if choice == 5:
        linkedlist.getSize()
    if choice == 0:
        exit()
    
    