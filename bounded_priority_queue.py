#!/usr/bin/env python
#
# Based on the work of Pravin Paratey (April 15, 2011)
# Joachim Hagege (June 18, 2014)  
#
# Code released under BSD license
# 
from __future__ import print_function
DISTANCE_INDEX = 1

class BoundedPriorityQueue:
    """ This class illustrates a PriorityQueue and its associated functions """

    def __init__(self, k):
        self.heap = []
        self.k = k
    
    def items(self):
        return self.heap

    def parent(self, index):
        """
        Parent will be at math.floor(index/2). Since integer division
        simulates the floor function, we don't explicity use it
        """
        return int(index / 2)

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def max_heapify(self, index):
        """
        Responsible for maintaining the heap property of the heap.
        This function assumes that the subtree located at left and right
        child satisfies the max-heap property. But the tree at index
        (current node) does not. O(log n)
        """
        left_index = self.left_child(index)
        right_index = self.right_child(index)

        largest = index
        if left_index < len(self.heap) and self.heap[left_index][DISTANCE_INDEX] > self.heap[index][DISTANCE_INDEX]:
            largest = left_index
        if right_index < len(self.heap) and self.heap[right_index][DISTANCE_INDEX] > self.heap[largest][DISTANCE_INDEX]:
            largest = right_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        Responsible for building the heap bottom up. It starts with the lowest non-leaf nodes
        and calls heapify on them. This function is useful for initialising a heap with an
        unordered array. O(n)
        We shall note that all the elements after floor(size/2) are leaves.
        """
        for i in xrange(len(self.heap)/2, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        """ The heap-sort algorithm with a time complexity O(n*log(n))
            We run n times the max_heapify (O(log n))
        """
        self.build_max_heap()
        output = []
        for i in xrange(len(self.heap)-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            output.append(self.heap.pop())
            self.max_heapify(0)
        output.append(self.heap.pop())
        self.heap = output

    def propagate_up(self, index):
        """ Compares index with parent and swaps node if larger O(log(n)) """
        while index != 0 and self.heap[self.parent(index)][DISTANCE_INDEX] < self.heap[index][DISTANCE_INDEX]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    # Here is the whole logic of the Bounded Priority queue.
    # Add an element only if size < k and if size == k, only if the element value is less than 
    def add(self, obj):
        # If number of elements == k and new element < max_elem:
        #   extract_max and add the new element.
        # Else:
        #   Add the new element.
        size = self.size()
        
        # Size == k, The priority queue is at capacity.
        if size == self.k:
            max_elem = self.max()
            
            # The new element has a lower distance than the biggest one.
            # Then we insert, otherwise, don't insert.
            if obj[DISTANCE_INDEX] < max_elem:
                self.extract_max()
                self.heap_append(obj)
            
        # if size == 0 or 0 < Size < k
        else: 
            self.heap_append(obj)

    def heap_append(self, obj):
        """ Adds an element in the heap O(ln(n)) """
        self.heap.append(obj)
        self.propagate_up(len(self.heap) - 1) # Index value is 1 less than length
        
    def max(self):
        # The highest distance will always be at the index 0 (heap invariant)
        return self.heap[0][1]
    
    def size(self):
        return len(self.heap)
    
    def extract_max(self):
        """
        Part of the Priority Queue, extracts the element on the top of the heap and
        then re-heapifies. O(log n)
        """
        max = self.heap[0]
        data = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = data
            self.max_heapify(0)
        return max

    def increment(self, key, value):
        """ Increments key by the input value. O(log n) """
        for i in xrange(len(self.heap)):
            if self.heap[i][0] == key:
                self.heap[i] = (value + self.heap[i][1], key)
                self.propagate_up(i)
                break

if __name__ == '__main__':
    # For test purposes.
    # Create the heap object
    m = BoundedPriorityQueue(5)
    print ("Initial heap:", m.heap)

    # Add an element to the heap
    m.add((None, 0.1))
    m.add((None, 0.25))
    m.add((None, 1.33))
    m.add((None, 3.2))
    m.add((None, 4.6))
    m.add((None, 0.4))
    m.add((None, 4.0))

    print (m.heap)
    print ("Extract maximum:", m.extract_max())
    print ("Extract maximum:", m.extract_max())
    print ("Extract maximum:", m.extract_max())
    print ("Extract maximum:", m.extract_max())
    
    print (m.heap)
