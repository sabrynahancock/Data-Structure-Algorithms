class Node:
    """Creates a new node"""
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    """linked list constructor"""
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """prints all the node in the linked list"""
        #temp is for temporary node/pointer. Start at head
        temp = self.head
        #while the temporary node is not none/ while its not empty 
        while temp is not None:
            #print the value of the temporary node
            print(temp.value)
            #jump to the next node and do the same thing until list/node is empty/none
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        """append to the end"""
        new_node = Node(value)
        if self.head is None: #edge case if the head is none/ if list is empty
            self.head = new_node
            self.tail = new_node
            
        else:
        #
            self.tail.next = new_node 
            self.tail = new_node
            
        self.length += 1

        return True                
    def pop(self, value):

        #edg case: empty linked list and only have one node in the list
        new_node = Node(value)
        if self.length == 0:
            return None

        temp = self.head 
        prev = self.head

        while (temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre 
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp



my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""
