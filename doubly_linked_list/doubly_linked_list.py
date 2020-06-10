"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next 

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head:
               self.head.insert_before(value)
               self.head = self.head.prev
               self.length += 1
               return self.head.value

        else:
               self.__init__(node=ListNode(value))
               return self.head.value

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
                if self.head.next is None:
                    self.tail = None
                current_head = self.head.value
                self.head = self.head.next
                self.length -= 1
                return current_head
        else:
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
           if self.tail:
               self.tail.insert_after(value)
               self.tail = self.tail.next 
               self.length += 1
               return self.tail.value
           
           else:
                self.__init__(node=ListNode(value))
                return self.tail.value

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
            # check to see if the value being removed is the only thing in the list
            if self.tail:
                if self.tail.prev is None:
                    self.head = None     

                # store the tail value in a variable
                # set the tail to where the previous pointer is pointing to slide it over
                # the return the value you removed the tail tag from
                current_tail = self.tail.value
                self.tail = self.tail.prev
                self.length -= 1
                return current_tail
            else:
                return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
            current_node = node
            node.delete()
            self.length -= 1
            self.add_to_head(current_node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
            current_node = node
            if current_node.prev is None:
                self.head = current_node.next
        
            node.delete()
            self.length -= 1
            self.add_to_tail(current_node.value)
        
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
            if not self.head and not self.tail:
                   return None
            self.length -= 1
            if self.head is self.tail:
                   self.head = None
                   self.tail = None
            # check if the node is the head
            elif self.head is node:
                   self.head = node.next
                   node.delete()
            # check if node is the tail
            elif self.tail is node:
                   self.tail = node.prev
                   node.delete()
            
            else:
                   node.delete()
                   self.length -= 1
                   return node.value
               



            current_node = node
            # if this is the only node in the list
            # if node.prev is None and node.next is None:
            #         self.head = None
            #         self.tail = None
            #         self.length -= 1
            #         return node.value

            # checks to see if the node is the head
            # don't need to worry about deleted node's pointers
            # elif node.prev is None:
            #         self.head = node.next
            #         node.delete()
            #         self.length -= 1
            #         return node.value

            # checks to see if the node is the tail
            # elif node.next is None:
            #         self.tail = node.prev
            #         node.delete()
            #         self.length -= 1 
            #         return node.value
            
            # else:
            #        node.delete()
            #        self.length -= 1
            #        return node.value

    """Returns the highest value currently in the list"""
    def get_max(self):
            current = self.head
            max_num = current.value
            while current.next is not None:
                    if max_num < current.next.value:
                            max_num = current.next.value
                    current = current.next

            return max_num



# my_list = DoublyLinkedList()
# print('LENGTH OF LIST: ',len(my_list))
# print('add to head:', my_list.add_to_head(4))
# print('LENGTH OF LIST: ',len(my_list))
# print('add to head:', my_list.add_to_head(6))
# print('LENGTH OF LIST: ',len(my_list))
# print('removed from head:', my_list.remove_from_head())
# print('LENGTH OF LIST: ',len(my_list))
# print('removed from head:', my_list.remove_from_head())
# print('LENGTH OF LIST: ',len(my_list))
# print('removed from head:', my_list.remove_from_head())
# print('LENGTH OF LIST: ',len(my_list))