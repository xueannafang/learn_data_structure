#single linked list

#define a node
class single_node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        val_str = f"value: {self.value}"
        id_str = f"id: {id(self)}" #the id here is the address of current node
        next_str = f"next_id: {id(self.next)} "
        return ', '.join([id_str, val_str, next_str])


# Create an example sll containing numbers from 0 to 5
    
#Step 1: Inite the sll by defining the first node as head
head = single_node(0) #head is the first node of this sll with value equals to 0
temp_ptr = head #the temp_ptr is a temporary pointer representing the current node

#Step 2: Assign the value of next node as its index plus 1 (only in this case) and move the temporary pointer to the next node
for i in range(5):
    temp_ptr.next = single_node(i+1) #the next node of current node has been created, with its value equals i+1
    temp_ptr = temp_ptr.next #move the pointer to the next node

# See how it looks like
ptr = head
print(f"id of None: {id(None)}")
#while ptr is not none, i.e., not reaching the end of this linked list
while ptr:
    print(ptr)
    ptr = ptr.next



# define a generalised sll with operations including add at the beginning, at the end and insert in the middle
class sll:
    def __init__(self, head):
        self.head = head #As defined above, head is the first node of this sll
        self.tail = head #When there's just one elemnet, the tail is the head
    
    def add_first(self, value_to_add):
        '''
        Insert a number, value_to_add, at the beginning of the sll
        '''
        new_head = single_node(value_to_add, next = self.head) #the old head of the orginal sll is now the next of the new head
        self.head = new_head #the new head is moved to the new head just defined
        #the complexity of add_first is irrelevant to the total number of nodes in the sll
        #therefore, it is O(1) complexity
    
    def add_last(self, value_to_add):
        '''
        Insert a number to the end of the sll
        '''
        new_tail = single_node(value_to_add, next = None)
        self.tail.next = new_tail #point the original last node to the new last node
        self.tail = new_tail #claim the new tail as the new end of the linked list
        #also, O(1) complexity
    
    def add_middle(self, value_to_add, after_where):
        '''
        add a number after the node indexed as after_where in the original list
        '''
        #we first need another function to pick out the node indexed at after_where
        #defined function _find_after_where
        node_before_new = self._find_after_where(after_where)
        node_to_add = single_node(value_to_add, next = node_before_new.next) # point the next node to the original one after the node after which to insert
        node_before_new.next = node_to_add #then point the next of the one after which to insert to the just inserted node

    def _find_after_where(self, after_where):
        '''
        find the node indexed as after_where
        assume the input is valid, otherwise some error handling based on overflowed index is required
        '''
        i = 0
        this = self.head #initialise the position of the pointer of this node
        for i in range(after_where + 1):
            if i == after_where:
                return this
            else:
                this = this.next #before reaching the target index, move the pointer to the next node each step
                # in the worst case, we need to move n times as the length of the list
                # therefore, the complexity of inserting in the middle of a sll is O(n)


