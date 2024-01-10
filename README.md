# Learn_data_structure

This is my learning diary for data structures. (I would also try to make some connections with chemistry when appropriate.)

## File explanation

- Linked list


Linked list consists of a "node" with a "next" feature pointed to the next node (single linked list) or with a "previous" plus "next" feature pointed to the previous and the next node (double linked list).

1) [Single linked list](https://github.com/xueannafang/learn_data_structure/blob/main/single_linked_list.py)

For single linked list (SLL), the complexity of inserting in the middle of a list is O(n), at the beginning or at the last of the list are both O(1).

The key operations are based on inserting a node and pointing to the next element.

In the case of inserting a new node at the beginning, the only thing is to create a new node and point its "next node" to the original first node of the sll.

To insert at the end, the procedure would be pointing the original last node to the new node (instead of a "None" node).

Both are irrelevant to the length of the list therefore the complexity is O(1).

In the case of inserting in the middle, an additional index of the node before the new one would be required. An additional step is to iterating through the old list until the target index has been reached, followed by 1) connecting the next node of the just-added node to the original next node of the one before, and 2) update the next node of the one before as the just-added node.

Since iteration is ineviteable now, the complexity, in the worst case, would be reading through the entire list with total number of n elements. Therefore, the compexity is O(n).


2) [Double linked list](https://github.com/xueannafang/learn_data_structure/blob/main/double_linked_list.py)

Similar to single linked list, the node in double linked list (dll) has another pointer towards the previous node (which we call it "last") apart from the "next". Inserting a node in a dll requires reconnection towards both the next node and the last node.

Some reflection from a chemist:

Linked list is the first data structure I found closely related to chemistry. How computer see molecules? Atoms and bonds. How reactions happen? Bonds formation and breaking, or inserting or removal atoms, i.e., changing the connection among atoms. That's analogous to manipulating the connection between adjacent nodes. In certain large sytems we may not want to walk through the vast region of (chemically-redundant) backbone of the molecule when only the termini/reactive site is required to be visited. That's where such type of ds could be useful.



- [Priority queue](https://github.com/xueannafang/learn_data_structure/blob/main/priority_queue.py)

This is an array of which the first element is the minimum (min priority queue) or maximum (the reverse) value. 
The array is arranged as a binary tree, or, a heap. 
Each layer has no more than two nodes. 
The lower layer (the leaves or children) must follow a given order compared to its root layer (parent). 

When adding a new number to this array, the new node will be compared to its parent layer (and its child layer) to decide whether it should go up or down. 

A heap is regarded as invariant when all the nodes in the heap follow the order given. 

For example, a branch of a min PQ can be: 1 -> (2, 3) -> ((2, 4), (5, 9)) -> ((3, 8), (4, 5), (8, 10), (9, 10)) ...
as long as the child is always larger (or equal to) its parent.

It cannot be: 2 -> (1, 3) (where the left child, 1, is smaller than 2). 

There's no strict requirement on nodes among the same layer. The key rule is along the parent-child branch.


Because it is a binary tree, we can know the left child would always be 2*idx + 1, right child: 2*idx + 2, parent in the opposite way, (idx - 1)//2, regardless it's coming from left or right child.

A few steps can be taken to check if parent node, left, right child nodes exist and whether they are valid or not. (If not, swap the reversed nodes.)

Special case is if neither child nodes is valid, we need to swap with the smaller child.

There should be many ways to implement this. My thought (may not the most efficient way..) is to continue checking the surrounding layers until the working layer has reached the top (i.e., no parent layer can be found). 


Reflection from a chemist:

Numbering functional groups according to importance(?) 