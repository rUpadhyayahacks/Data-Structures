"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Follows FIFO also known as LILO principle
# For Queues you need to be able to add from one way and take fro another
# class Queue:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value): # saying add/push
#         self.storage.insert(0, value)
#         self.size += 1

#     def dequeue(self): # saying remove/pop
#         if self.size > 0:
#             value = self.storage.pop() # removes last thing in the queue
#             self.size = len(self.storage)
#             return value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, value):
           self.size += 1
           return self.storage.add_to_end(value)

    def dequeue(self):
           if self.size > 0:
               self.size -= 1
           return self.storage.remove_from_head()

    def __len__(self):
           return self.size


        


class Node:
    def __init__(self, value=None, next_node=None):
     # the value at this linked list node
        self.value = value
     # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's "next_node" reference to the passed in node
        self.next_node = new_next




class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        node = Node(value)
        if not self.head:
           self.head = node
        
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            
            current.set_next(node)

    def remove_from_head(self):
        if self.head:
            value = self.head.get_value()
            self.head = self.head.get_next() 
            return value # this is the removed head
            # don't need to delete because the python cleaner will remove it as it's no longer a part of the linked list