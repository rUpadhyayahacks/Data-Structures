"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Linked-Lists are better for a language like C where there are no built in array methods, otherwise you would use the built in methods that come with a language like Python, JavaScript (under the hood though a JavaScript array is just an Object with the keys being consecutive ints.)

# Uses Array/Python built-in functions
# control the order that the data can be accessed in

# LIFO: think vertical, Last In Stack First Out of Stack
# I add and remove from the same spot
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []

#     def __len__(self):
#         return len(self.storage) # returns the number (int) of items in the list

#     def push(self, value):
#         self.storage.append(value) # appends object to the end of the list ("str", int, etc)
        

#     def pop(self):
#         if len(self.storage) < 1:
#             return None
#     #     return self.storage.pop(0) # specify the index or default to the last item in the list


# Linked-List Method
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_head()

    def __len__(self):
        return self.size
        



class Node: # points to the next nod
    def __init__(self, value=None, next_node=None):
     # the value at this linked list node
        self.value = value
     # reference to the next node in the list
        self.next_node = next_node

    def get_value(self): # a method that returns the value of the node
        return self.value

    def get_next(self): # a method that returns the next node in the list
        return self.next_node

    def set_next(self, new_next): # a method that sets the next_node to a different node
        # set this node's "next_node" reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list; This is the head of the list
        self.head = None 


    def add(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # value is actual value, and hasn't been wrapped in a Node yet

        # what if the list is empty?
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # we want to add it to the last node in the list
            # we can get to the last node in the list by traversing it
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list
            current.set_next(new_node)

    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            # this stores the value of the head in a variable
            value = self.head.get_value()
            # need to remove the value at the head
            # need to update the value at self.head; head needs to refer to something
            # self.head.get_next(): moves the Head pointer to the second node in the chain. 
            # The head is how we access the Node at position  0 or 1, we then cut that off. 
            # storing it in the value and then returning the value allows us 
            self.head = self.head.get_next()
            return value

    def add_to_head(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node
