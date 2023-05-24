"""
The Trie is a data structure commonly used when dealing with strings.
If we need a database to contain all strings, it is more convenient to use a Trie rather than an array,
especially if the number of strings is big. In the trie, we see the succession of letters which build the different words.
This allows us to reuse the common prefixes. If we have N strings, searching for a word has complexity O(len(word)), rather than O(N).
"""

"""
Node Definition
"""
class Node(object):

    def __init__(self):

        self.is_end = False
        self.children = {}

"""
Trie Definition
"""
class Trie(object):

    def __init__(self):

        self.fake_node = Node()


    """
    Add word in the Trie - O(len(word))
    """
    def add_word(self, word):

        curr_node = self.fake_node

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node()

            curr_node = curr_node.children[c]

        curr_node.is_end  = True


    """
    Return True if word is stored in the Trie - O(len(word))
    """
    def search_word(self, word):
        curr_node = self.fake_node

        for c in word:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]

        return curr_node.is_end


    """
    Return True if prefix is stored in the Trie - O(len(prefix))
    """
    def search_prefix(self, prefix):
        curr_node = self.fake_node

        for c in prefix:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]

        return True
