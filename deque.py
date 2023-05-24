"""
Here we build a personal implementation of the common deque, which can also be found on the collection library in Python
Deque is built here as a double linked list, allowing insertion and removal of elements at the ends to be performed in O(1)
"""

"""
Node definition
"""
class Node():

    def __init__(self,val = 0):

        self.val = val
        self.prec = None
        self.next = None


"""
Deque definition
"""
class Deque():

    def __init__(self,array):

        self.length = 0

        self.fake_head = Node()
        self.fake_tail = Node()
        self.fake_head.next = self.fake_tail
        self.fake_tail.prec = self.fake_head

        for val in array:
            self.append_right(val)


    """
    Return length of the list - O(1)
    """
    def get_length(self):

        return self.length


    """
    Add an element at the end of the Deque - O(1)
    """
    def append_right(self, val):

        new_node = Node(val)
        new_node.prec = self.fake_tail.prec
        self.fake_tail.prec.next = new_node

        self.fake_tail.prec = new_node
        new_node.next = self.fake_tail

        self.length += 1

    """
    Add an element at the start of the Deque - O(1)
    """
    def append_left(self,val):

        new_node = Node(val)
        new_node.next = self.fake_head.next
        self.fake_head.next.prec = new_node

        self.fake_head.next = new_node
        new_node.prec = self.fake_head

        self.length += 1


    """
    Remove an element at the end of the Deque - O(1)
    """
    def pop_right(self):

        if(self.length == 0): print("No element in the queue")

        else:

            self.fake_tail.prec.prec.next = self.fake_tail
            self.fake_tail.prec = self.fake_tail.prec.prec
            self.length -= 1


    """
    Remove an element at the start of the Deque - O(1)
    """
    def pop_left(self):

        if(self.length == 0): print("No element in the queue")

        else:

            self.fake_head.next.next.prec = self.fake_head
            self.fake_head.next = self.fake_head.next.next
            self.length -= 1


    """
    Display the Deque - O(N)
    """
    def display(self):

        curr = self.fake_head
        print("START--->>",end = "")
        for l in range(self.length):
            curr = curr.next
            print(curr.val, "--->>", end = "")

        print("END")
