"""
The Heap is a popular data structure which allows to retrieve min or max values of an array in efficient logarithmic time.
A MinHeap is a balanced binary tree where the value of each parent node is less than the values of both of its children.
We can add a new element in the heap, remove the top node (minimum value), or just take a look at the this value.
A MaxHeap can be built from a MinHeap by storing the inverse of the values in the MinHeap.
"""


class MinHeap(object):


    def __init__(self):

        self.heap = []

    def __get_left_child(self,idx):

        return 2*idx

    def __get_right_child(self,idx):

        return 2*idx + 1

    def __get_parent(self,idx):

        return idx // 2

    def __has_left_child(self,idx):

        return self.__get_left_child(idx) < len(self.heap)

    def __has_right_child(self,idx):

        return self.__get_right_child(idx) < len(self.heap)

    def __has_parent(self,idx):

        return idx > 0

    def __heapify_up(self,idx):

        if self.__has_parent(idx):

            parent_idx = self.__get_parent(idx)

            if (self.heap[parent_idx] > self.heap[idx]):

                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                self.__heapify_up(parent_idx)


    """
    Add a new element in the Heap - O(logN)
    """
    def push(self,val):

        self.heap.append(val)
        self.__heapify_up(len(self.heap)-1)

    def __heapify_down(self,idx):

        if (self.__has_left_child(idx)):
            min_idx = self.__get_left_child(idx)
            if (self.__has_right_child(idx)):
                right_idx = self.__get_right_child(idx)
                if (self.heap[min_idx] > self.heap[right_idx]):
                    min_idx = right_idx

            if (self.heap[idx] > self.heap[min_idx]):

                    self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
                    self.__heapify_down(min_idx)


    """
    Get and remove the top element from the Heap - O(logN)
    """
    def pull(self):

        if len(self.heap) == 0:
            print("Heap is Empty")
            return

        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.__heapify_down(0)
            return min_val

    """
    Get the top element from the Heap - O(1)
    """
    def peek(self):

        if len(self.heap) == 0:
            print("Heap is Empty")
            return

        else: return self.heap[0]
