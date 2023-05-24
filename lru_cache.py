"""
Least Recent Used Cache is a peculiar data structure, built by combining hashing with a linked list structure.
Let's say we have to store (key, value) pairs but we can only store a maximal capacity C of these pairs.
Least Recent Used Cache storey the C most recent used key-value pairs.
All the perations are performed in constant time.
"""

"""
Node definition
"""
class Node(object):

    def __init__(self, val = 0):

        self.val = val
        self.prec = None
        self.next = None


"""
LRU Cache definition
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity #Maximal capacity of the LRU Cache
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prec = self.head
        self.map = {}
        self.cache = {}


    """
    Append node to end of linked list - O(1)
    """
    def append(self,node):

        self.tail.prec.next = node
        node.prec = self.tail.prec

        self.tail.prec = node
        node.next = self.tail


    """
    Remove node from linked list - O(1)
    """
    def remove(self,node):
        node.prec.next = node.next
        node.next.prec = node.prec



    """
    Get the corresponding value to the provided key - O(1)
    """
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:

            self.remove(self.map[key])
            new_node = Node(key)
            self.append(new_node)
            self.map[key] = new_node

            return self.cache[key]

        else: return - 1


    """
    Update the cache with a new key-value pair - O(1)
    """
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.map[key])

        elif len(self.cache) == self.cap:
            k = self.head.next.val
            self.remove(self.head.next)
            self.cache.pop(k)
            self.map.pop(k)

        new_node = Node(key)
        self.append(new_node)
        self.cache[key] = value
        self.map[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
