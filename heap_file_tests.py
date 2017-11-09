# Mani Movva
# Section 07

import unittest
import filecmp
from heap_lab import *

class TestList(unittest.TestCase):
   
   def test_insert(self):     # testing to see if the insert() function works
      heap = MaxHeap(7)
      alist = [2, 9, 7, 6, 5, 8]
      heap.build_heap(alist)
      self.assertEqual(heap.insert(22), True)
      self.assertEqual(heap.insert(23), False)
      self.assertEqual(heap.items[1:heap.size+1],[22, 6, 9, 2, 5, 7, 8] )
      
   def test_find_max(self):   # testing to see if the find_max() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      heap.build_heap(alist)
      self.assertEqual(heap.find_max(), 9)


   def test_del_max(self):    # testing to see if the del_max() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      heap.build_heap(alist)
      heap.del_max()
      self.assertEqual(heap.find_max(), 8)

   def test_heap_contents(self): # testing to see if the heap_contents() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      heap.build_heap(alist)
      self.assertEqual(heap.heap_contents(), [9, 6, 8, 2, 5, 7])

   def test_build_heap(self): # testing to see if the build_heap() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      self.assertEqual(heap.heap_contents(), [])
      heap.build_heap(alist)
      self.assertEqual(heap.heap_contents(), [9, 6, 8, 2, 5, 7])
      
   def test_is_empty(self):      # testing to see if the is_empty() function works
      heap = MaxHeap()
      self.assertEqual(heap.is_empty(), True)
      heap.insert(6)
      self.assertEqual(heap.is_empty(), False)

   def test_is_full(self):       # testing to see if the is_full() function works
      heap = MaxHeap(2)
      self.assertEqual(heap.is_full(), False)
      heap.insert(6)
      heap.insert(7)
      self.assertEqual(heap.is_full(), True)
  
   def test_get_heap_cap(self):  # testing to see if the get_heap_cap() function works
      heap = MaxHeap(2)
      self.assertEqual(heap.get_heap_cap(), 2)
      
   def test_get_heap_size(self): # testing to see if the get_heap_size() function works
      heap = MaxHeap()
      heap.insert(6)
      self.assertEqual(heap.get_heap_size(), 1)

   def test_perc_down(self):     # testing to see if the perc_down() function works
      ding = MaxHeap()
      ding.items = [1,5,33,2,90,52,3,11,123456,23,76]
      ding.size = 11
      ding.perc_down(0)
      self.assertEqual(ding.items,[5, 33, 90, 2, 123456, 52, 3, 11, 1, 23, 76])
            
   def test_perc_up(self):       # testing to see if the perc_up() function works
      heap = MaxHeap()
      heap.items = [2, 9, 7, 6, 5, 8]
      heap.perc_up(5)
      self.assertEqual(heap.items, [2, 9, 8, 6, 5, 7])
            
   def test_max_child(self):     # testing to see if the max_child() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      heap.build_heap(alist)
      self.assertEqual(heap.max_child(1), 3)
      
   def test_heap_sort_increase(self):  # testing to see if the heap_sort_increase() function works
      heap = MaxHeap()
      alist = [2, 9, 7, 6, 5, 8]
      self.assertEqual(heap_sort_increase(alist), [2, 5, 6, 7, 8, 9])

      
if __name__ == '__main__': 
   unittest.main()
