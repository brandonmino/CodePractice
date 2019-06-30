###Information and questions for data structures

#1 Linear vs Non-Linear DS
"""Linear:if elements form sequence or linear list (Ex: Array, Linked List, Stack/Queue)"""

#2 Array vs Linked List
"""Size of array is fixed, LL are dynamic. 
Insertion/Deletion in array is time consuming, unlike LL. 
Random access not allowed in LL
Extra memory for pointers in LL"""

#3 LIFO vs FILO vs FIFO
"""LIFO: Last in First out. 
FILO: First in Last out
FIFO: First in First out"""

#4 Def of Stack
"""Linear DS which uses LIFO for accesssing elements.
Basic operations of stack (all O(1)): 
Push: add item
Pop: remove item (LIFO: first element)
Peek: return top element"""

#5 Def of Queue
"""Linear DS which uses FIFO for accesssing elements.
Basic operations of queue:
Enqueue: add item (worst is O(n) average O(1))
Dequeue: remove item (O(1))"""

#6 Infix vs Prefix vs Postfix
"""Infix: X+Y: Operations are written in-between their operands.
Postfix: XY+: Operators are written after their operands.
Prefix: +XY: Operators are written before their operands."""

#7 Def of Linked List (LL)
"""Linear DS where each element is a seperate object. Each element/node of list has two items: data and reference to next node.
Singly LL: Every node stores reference to next node in list and last node has next reference or NULL if DNE.
Doubly LL: Two References associated with each node. One reference points to next node and one to previous node. NULL before and after.
Circular LL: All nodes are connected to form circle (no NULL). Can be singly or doubly circular LL."""

#8 Binary Search
"""O(n) worst, O(logn) best, Has to be sorted. Divide in half, search and redivide until item is found."""

#9 BubbleSort
"""O(n^2)
Repeatedly swaps adjacent elements if they are in wrong order."""

#10 SelectionSort
"""O(n^2)
Repeatedly finds min element (cosidering ascending order) from unsorted part and puts it at the beginning.
Has 2 arrays: subarray that's already sorted, remaining subarray is picked and moved to sorted subarray."""

#11 InsertionSort
"""O(n^2)
Repeatedly set marker for sorted section after first element until unsorted section is empty and swap elements to right to create correct position and shift the unsorted element"""

#12 HeapSort
"""O(nlogn)
Repeatedly find max element and place at end."""

#13 Quicksort
"""Average: O(nlogn), Worst: O(n^2)
Picks element as pivot and partitions the given array around pivot
Partition puts lower elements before pivot and higher elements after pivot"""

#14 MergeSort
"""O(nlogn)
Divides array into 2 halves, calls itelsef for two halves, then merges the two sorted halves.

# What DS for BFS and DFS of a graph
"""BFS: Queue
DFS: Stack"""