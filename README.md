BoundedPriorityQueue
====================

A bounded priority queue, used for Kd-Tree implementation.
This is a priority queue that can accept up to k elements.
If size = k: insert iff the value is less than the max element now.
If size < k: insert anyway.

It is based on a max-heap, and has efficient standard algorithms to:
- Build the tree (O(n))
- Sort the tree (O(n log n))
- Extract the max element (priority queue): O(log n)

A requirement for this data structure was that it could enable custom objects to be passed, and not only integers, so it's 
important to pass a tuple of the type (Object, value to add)

Example:
    
    # When creating, give it a k value.
    m = BoundedPriorityQueue(5)
    print "Initial heap:", m.heap

    # Add an element to the heap
    m.add((None, 0.1))
    m.add((None, 0.25))
    m.add((None, 1.33))
    m.add((None, 3.2))
    m.add((None, 4.6))
    m.add((None, 0.4))
    m.add((None, 4.0))

Based on the work of Pravin Paratey, and on the excellent document of Stanford: 
http://www.stanford.edu/class/cs106l/handouts/assignment-3-kdtree.pdf
This is a very good helper class to implement a kNN search with a k-d tree.
Read the pdf for more details.
