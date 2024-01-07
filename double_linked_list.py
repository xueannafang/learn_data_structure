#define a double-linked list node
class double_node:
    def __init__(self, value, next = None, last = None):
        self.value = value
        self.next = next
        self.last = last 


class double_linked_list:
    def __init__(self, *values):
        self.head = double_node(values[0])
        self.tail = self.head
        for value in values[1:]:
            self.add_tail(value) #inite the dll with a series of values
    
    def add_tail(self, value):
        this = double_node(value)
        this.next = None
        this.last = self.tail #the last of the new tail is the last tail
        self.tail.next = this #connect the next of old tail to the new tail
        self.tail = this # update the new tail as current node 
    
    def add_head(self, value):
        this = double_node(value)
        this.last = None
        this.next = self.head
        self.head.last = this
        self.head = this
    
    def add_middle(self, value, after_where):
        '''
        add a new node after after_where
        '''
        last = self._find_after_where(after_where)
        next = last.next
        this = double_node(value, next = next, last = last)
        last.next = this
        next.last = this

    def _find_after_where(self, after_where):
        this = self.head
        for i in range(after_where + 1):
            this = this.next
        return this
