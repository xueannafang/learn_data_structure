#PQ is an indexed based binary tree structure

class binary_tree:

    '''
    min PQ: an array that the higher layer always smaller than its child layer
    '''

    def __init__(self):
        self.pq_bt = []
    
    def insert_btn(self, value):
        #insert a binary tree node

        self.pq_bt.append(value)
        crt_idx = len(self.pq_bt) - 1 #the index of the just-added node
        #update the oder of nodes to make this heap invariant

        #evaluate if this node has parent node and child nodes or not
        has_prt, has_l_ch, has_r_ch = self.check_surrounding(self, crt_idx)

        old_heap = self.pq_bt

        while has_prt:

            #condition to bubble up: has parent and the parent is larger than this node
            #if parent is larger: prt_vld check will return False
            if has_prt:
                prt_vld = self.is_prt_vld(crt_idx) #return False if parent is larger than this
                if not prt_vld:
                    self.bubble_up(crt_idx)
            
            if has_l_ch and not has_r_ch:
                #when children is smaller than the current node
                #either, if this node is larger than only one child, then simply swap the two nodes
                #or, if both children are smaller than this node, only swap the node with the smaller child
                #if r_ch exists, l_ch must exists already
                #first consider the situation when only has left child
                l_ch_vld = self.is_l_ch_vld(crt_idx)
                if not l_ch_vld:
                    self.sink_left(crt_idx)
            
            elif has_l_ch and has_r_ch:
                #now, this node has two children
                #we need to compare the value between the two children
                #then decide to swap with which

                l_ch_vld = self.is_l_ch_vld(crt_idx)
                r_ch_vld = self.is_r_ch_vld(crt_idx)
                if not l_ch_vld and not r_ch_vld:
                    l_ch_value = self.pq_bt[self.get_l_ch_idx(crt_idx)]
                    r_ch_value = self.pq_bt[self.get_r_ch_idx(crt_idx)]
                    if l_ch_value <= r_ch_value:
                        self.sink_left(crt_idx)
                    else:
                        self.sink_right(crt_idx)
                elif not l_ch_vld:
                    self.sink_left(crt_idx)
                elif not r_ch_vld:
                    self.sink_right(crt_idx)
            
            new_heap = self.pq_bt
            #compare if the heap has changed or not
            #if not, the heap is invariant and we can break the current loop
            if new_heap == old_heap:
                break


    
    def check_surrounding(self, this_idx):
        #check if this node has parent node and children nodes
        has_prt = self.has_parent(this_idx)
        has_l_ch = self.has_l_ch(this_idx)
        has_r_ch = self.has_r_ch(this_idx)
        return has_prt, has_l_ch, has_r_ch

    
    def bubble_up(self, this_idx):
        #swap this node with its parent
        parent_idx = self.get_parent_idx(this_idx)
        self.swap(parent_idx, this_idx)
    
    def sink_left(self, this_idx):
        #swap this node with its left child
        l_ch_idx = self.get_l_ch_idx(this_idx)
        self.swap(this_idx, l_ch_idx)
    
    def sink_right(self, this_idx):
        #swap this node with its right child
        r_ch_idx = self.get_r_ch_idx(this_idx)
        self.swap(this_idx, r_ch_idx)

    def swap(self, idx_1, idx_2):
        #swap the value of two idx, idx_1 is at the higher level at the beginning of this function
        mid_var = self.pq_bt[idx_1]
        self.pq_bt[idx_1] = self.pq_bt[idx_2]
        self.pq_bt[idx_2] = self.pq_bt[mid_var]

    def get_parent_idx(self, idx):
        parent_idx = (idx-1)//2
        return parent_idx
    
    def has_parent(self, this_idx):
        par_idx = self.get_parent_idx(this_idx)
        if par_idx >= 0:
            return True

    def get_l_ch_idx(self, idx):
        l_ch_idx = 2*idx + 1
        return l_ch_idx
    
    def has_l_ch(self, this_idx):
        l_ch_idx = self.get_l_ch_idx(this_idx)
        if l_ch_idx < len(self.pq_bt):
            return True
    
    def get_r_ch_idx(self, idx):
        r_ch_idx = 2*idx + 2
        return r_ch_idx
    
    def has_r_ch(self, this_idx):
        r_ch_idx = self.get_r_ch_idx(this_idx)
        if r_ch_idx < len(self.pq_bt):
            return True
    
    def is_prt_vld(self, this_idx):
        #note that here the parent layer has been confirmed to exist
        #parent valid means parent is smaller or equal to the current node
        is_prt_vld = True
        prt_idx = self.get_parent_idx(this_idx)
        prt_value = self.pq_bt[prt_idx]
        this_value = self.pq_bt[this_idx]
        if prt_value > this_value:
            is_prt_vld = False
        return is_prt_vld
    
    def is_l_ch_vld(self, this_idx):
        #l_ch has been confirmed to exist
        #left child valid means the child is larger or equal to the current node
        is_l_ch_vld = True
        l_ch_idx = self.get_l_ch_idx(this_idx)
        l_ch_value = self.pq_bt[l_ch_idx]
        this_value = self.pq_bt[this_idx]
        if this_value > l_ch_value:
            is_l_ch_vld = False
        return is_l_ch_vld

    def is_r_ch_vld(self, this_idx):
        #r_ch has been confirmed to exist
        #right child valid means the child is larger or equal to the current node
        is_r_ch_vld = True
        r_ch_idx = self.get_r_ch_idx(this_idx)
        r_ch_value = self.pq_bt[r_ch_idx]
        this_value = self.pq_bt[this_idx]
        if this_value > r_ch_value:
            is_r_ch_vld = False
        return is_r_ch_vld




    
