# author: Bernard Kirk Katamanso
# Date: June 6, 2024
# Description: This file contains the test cases for the singly linked list implementation in LinkedLists.py.

# How to write test cases for the singly linked list implementation in LinkedLists.py
# To write test cases for the singly linked list implementation in LinkedLists.py, we can create a new file called test.py and import the unittest module.
# We can then create a test class that inherits from unittest.TestCase and define test methods to test the add and remove methods of the SinglyLinkedList class.
# In each test method, we can create an instance of the SinglyLinkedList class, call the add or remove method with some test data, and assert the expected results using the assertEqual method.
# We can also test edge cases such as adding or removing elements from an empty list, adding or removing elements that are not present in the list, and adding or removing elements from a list with multiple elements.
# Finally, we can run the test cases by calling unittest.main() at the end of the file.


import unittest
from LinkedLists import SinglyLinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()

    def test_add(self):
        self.list.add(1)
        self.assertEqual(self.list.size(), 1)
        self.assertEqual(self.list.head.data,1 )
        self.assertEqual(self.list.tail.data, 1)
        self.list.clear()

    def test_remove(self):
        self.list.add('item1')
        self.list.add('item2')
        self.list.remove('item1')
        self.assertEqual(self.list.size(), 1)
        self.assertEqual(self.list.head.data, 'item2')
        self.assertEqual(self.list.tail.data, 'item2')
        self.list.clear()

    def test_remove_not_present(self):
        self.list.add('item1')
        self.assertFalse(self.list.remove('item2'))
        self.assertEqual(self.list.size(), 1)

if __name__ == '__main__':
    unittest.main()