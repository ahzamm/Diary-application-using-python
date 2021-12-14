

class Node:
    '''This class is just for creating a Node with some data, thats why we set the refrence field to Null'''
    
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    '''This class is for performing the operations to the node which we create using class Node'''

    def __init__(self):
        self.head = None        # we are creating an empty linked list (remember we are not creating a node, we are creating linked list, for creating node we already have method above)

    def print_LL(self):
        '''This methord is for traversing Linked List'''

        if self.head == None:    # if the linked list is empty
            print('The linked list is empty')

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)     # we create new node with data=data  and  ref=Null
        new_node.ref = self.head  # we set the refrence of new node to the head
        self.head = new_node      # set the head to the new node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # if linked list is empty, then we set newely created node as head
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref         # to reach to the last node
            n.ref = new_node      # set the refrence of last node to the new node

LL1 = LinkedList()
LL1.add_begin('ahzam')
LL1.print_LL()

        # self.head is just store the refrence of first node 

