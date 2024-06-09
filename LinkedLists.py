# author: Bernard Kirk Katamanso
# Date: June 6, 2024
# Description: This file contains the implementation of singly and doubly linked lists in Python.

# Linked lists are a data structure that consists of a sequence of elements called nodes, where each element points to the next element in the sequence.
# The first node is called the head, and the last node is called the tail. The tail points to None, indicating the end of the list.
# Linked lists can be singly linked (each node points to the next node) or doubly linked (each node points to the next and previous nodes).
# The main advantage of linked lists is that they can grow or shrink in size dynamically, unlike arrays, which have a fixed size.
# However, linked lists have slower access times compared to arrays because elements are not stored in contiguous memory locations.
# Since linked lists do not require contiguous memory, they can be more memory-efficient than arrays for certain operations.
# Linked list have fast insertion and deletion times, especially when adding or removing elements at the beginning or end of the list.
# The following code demonstrates how to implement singly and doubly linked lists in Python.


class Pointer:
    """
    Represents a pointer object in a linked list.
    
    Attributes:
        next_item_reference: The reference to the next item in the linked list.
        previous_item_reference: The reference to the previous item in the linked list (for doubly linked list).
    """
    
    def __init__(self, next_item_reference=None, previous_item_reference=None):
        self.next_item_reference = next_item_reference
        self.previous_item_reference = previous_item_reference


class LinkedListItem:
    """
    Represents an item in a linked list.
    
    Attributes:
        data: The data stored in the item.
        pointer: The pointer to the next item in the linked list.
    """
    
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None
        self.tail = None
        self._size = 0
        
    def add(self, data):
        """
        Adds a new node with the given data to the end of the linked list.
        
        Parameters:
            data: The data to be stored in the new node.
        """
        new_node = LinkedListItem(data, Pointer(None))
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.pointer.next_item_reference = new_node
            self.tail = new_node
        self._size += 1
  
    def remove(self, data):
        """
        Removes the first occurrence of the node with the given data from the linked list.
        
        Parameters:
            data: The data to be removed from the linked list.
            
        Returns:
            True if the data was found and removed, False otherwise.
        """
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is not None:
                    previous.pointer.next_item_reference = current.pointer.next_item_reference
                else:
                    self.head = current.pointer.next_item_reference
                self._size -= 1
                return True  # data removed
            previous = current
            current = current.pointer.next_item_reference
        return False  # data not found    
    
    def size(self):
        """
        Returns the number of nodes in the linked list.
        
        Returns:
            The size of the linked list.
        """
        return self._size
    
    def print_list(self):
        """
        Prints the data of each node in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.pointer.next_item_reference
        print("None")
        
    def find(self, data):
        """
        Finds the first node with the given data.
        
        Parameters:
            data: The data to find in the linked list.
        
        Returns:
            The node containing the data, or None if not found.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.pointer.next_item_reference
        return None
    
    def is_empty(self):
        """
        Checks if the linked list is empty.
        
        Returns:
            True if the linked list is empty, False otherwise.
        """
        return self.head is None
    
    def clear(self):
        """
        Clears the linked list.
        """
        self.head = None
        self.tail = None
        self._size = 0


# Simple test
sll = SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(5)
sll.add(4)
sll.add(5)

sll.print_list()
print("Removing 5")
sll.remove(5)
sll.print_list()


class DoublyLinkedList:
    """
    A class representing a doubly linked list.
    """

    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, data):
        """
        Adds a new node with the given data to the end of the linked list.
        
        Parameters:
            data: The data to be stored in the new node.
        """
        new_node = LinkedListItem(data, Pointer(None, self.tail))
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.pointer.next_item_reference = new_node
            self.tail = new_node
        self._size += 1

    def remove(self, data):
        """
        Removes the first occurrence of the node with the given data from the linked list.
        
        Parameters:
            data: The data to be removed from the linked list.
            
        Returns:
            True if the data was found and removed, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                if current.pointer.previous_item_reference is not None:
                    current.pointer.previous_item_reference.pointer.next_item_reference = current.pointer.next_item_reference
                else:
                    self.head = current.pointer.next_item_reference
                if current.pointer.next_item_reference is not None:
                    current.pointer.next_item_reference.pointer.previous_item_reference = current.pointer.previous_item_reference
                else:
                    self.tail = current.pointer.previous_item_reference
                self._size -= 1
                return True  # data removed
            current = current.pointer.next_item_reference
        return False  # data not found

    def size(self):
        """
        Returns the number of nodes in the linked list.
        
        Returns:
            The size of the linked list.
        """
        return self._size
    
    def print_list_forward(self):
        """
        Prints the data of each node in the linked list from head to tail.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.pointer.next_item_reference
        print("None")
        
    def print_list_backward(self):
        """
        Prints the data of each node in the linked list from tail to head.
        """
        current = self.tail
        while current is not None:
            print(current.data, end=" -> ")
            current = current.pointer.previous_item_reference
        print("None")


# Simple test for DoublyLinkedList
dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)

dll.print_list_forward()
print("Removing 3")
dll.remove(3)
dll.print_list_forward()
dll.print_list_backward()
