# Mani Movva
# Section 07


# MaxHeap is a class
# MaxHeap is a max heap that contains integers, it is represented using a list
class MaxHeap:
    def __init__(self, capacity = 50):
        self.capacity = capacity
        self.size = 0
        self.items = [None]*(self.capacity + 1)
        self.items[0] = 0

    # int -> Boolean
    def insert(self, item):
        """returns a boolean for if the input parameter of an integer (item) was successfully inserted"""
        if not self.is_full():
            for i in range(1,len(self.items)):
                if self.items[i] is None:
                    self.items[i] = item
                    self.size += 1
                    self.perc_up(i)
                    return True
        return False

    # None -> None, int
    def find_max(self):
        """returns either None or an int which is the maximum value stored in the MaxHeap, takes no input parameter. """
        maxVal = self.items[1]
        if maxVal is None:
            return None
        
        for i in range(1,len(self.items)):
            if self.items[i] is not None:
                if self.items[i] > maxVal:
                    maxVal = self.items[i]
        return maxVal

    # None -> None
    def del_max(self):
        """Deletes the maximum value stored in the MaxHeap. Takes no input parameters and returns nothing."""
        maxVal = self.find_max()
        if maxVal is not None:
            self.items[1] = self.items[self.size]
            self.items[self.size] = None
            self.size -= 1
            self.perc_down(1)

    # None -> list
    def heap_contents(self):
        """returns the contents of the heap, takes nothing as an input"""
        return self.items[1:self.size+1]

    # list -> Boolean
    def build_heap(self, alist):
        """builds a max heap with the correct properties, takes a list as an input and returns a boolean representing whether or not the building was successful"""
        if len(alist) > self.capacity:
            return False
        else:
            i = len(alist) // 2
            self.size = len(alist)
            self.items = [0] + alist[:] + [None]*(self.capacity+1-len(alist))
            while (i > 0):
                self.perc_down(i)
                i = i - 1
            return True

    # None -> Boolean
    def is_empty(self):
        """returns a boolean representing whether or not the MaxHeap is empty, takes no input"""
        if self.size == 0:
            return True
        return False

    # None -> Boolean
    def is_full(self):
        """returns a boolean representing whether or not the MaxHeap is full, takes no input parameters"""
        if self.size == self.capacity:
            return True
        return False 

    # None -> int
    def get_heap_cap(self):
        """returns an integer representing the capacity of the MaxHeap, takes no input parameters"""
        return self.capacity

    # None -> int
    def get_heap_size(self):
        """returns an integer representing the current size of the MaxHeap, takes no input parameters"""
        return self.size

    # int -> None
    def perc_down(self, i): #
        """percolates items down to retain order property within the max heap, takes an integer representing an index as an input parameter and returns nothing"""
        while (i * 2) <= self.size:
            mc = self.max_child(i) ## find max child
            if self.items[i] < self.items[mc]:
                tmp = self.items[i]
                self.items[i] = self.items[mc]
                self.items[mc] = tmp
            i = mc

    # int -> None
    def perc_up(self, i):
        """percolates items up to retain order property within the max heap, takes an integer representing an index as an input parameter and returns nothing"""
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                tmp = self.items[i // 2]
                self.items[i // 2] = self.items[i]
                self.items[i] = tmp
            i = i // 2

    # int -> int
    def max_child(self, i):
        """finds and returns the maximum child of any item in the max heap, takes an integer representing an index as an input parameter"""
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.items[i*2] < self.items[i*2+1]:
            return i * 2+1
        else:
            return i * 2

# list -> list
def heap_sort_increase(alist):
    """returns a list of integers sorted from least to greatest by using the heap sort algorithm, takes a list as the input"""
    heap = MaxHeap()
    heap.build_heap(alist)
    originalSize = heap.size
    for i in range(heap.size):
        maxVal = heap.items[1]
        heap.del_max()
        heap.items[originalSize-i] = maxVal
    return heap.items[1:originalSize+1]


heap = MaxHeap()
alist = [3, 6, 2, 1, 5, 8]
heap.build_heap(alist)
print(heap.heap_contents())
print(heap_sort_increase(heap.heap_contents()))

