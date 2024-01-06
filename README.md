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

Some reflection from a chemist:

Linked list is the first data structure I found closely related to chemistry. How computer see molecules? Atoms and bonds. How reactions happen? Bonds formation and breaking, or inserting or removal atoms, i.e., changing the connection among atoms. That's analogous to manipulating the connection between adjacent nodes. In certain large sytems we may not want to walk through the vast region of (chemically-redundant) backbone of the molecule when only the termini/reactive site is required to be visited. That's where such type of ds could be useful.