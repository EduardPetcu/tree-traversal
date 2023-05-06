import unittest
from tree import Tree
from node import Node

class TestTreeMethods(unittest.TestCase):
    """ Test class for Tree class """
    
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(7)
        self.tree.add(6)
        self.tree.add(8)

    def test_find(self):
        """ Test method for find data in the tree """
        self.assertEqual(self.tree.find(5).data, 5)
        self.assertEqual(self.tree.find(3).data, 3)
        self.assertEqual(self.tree.find(2).data, 2)
        self.assertEqual(self.tree.find(4).data, 4)
        self.assertEqual(self.tree.find(7).data, 7)
        self.assertEqual(self.tree.find(6).data, 6)
        self.assertEqual(self.tree.find(8).data, 8)
        self.assertEqual(self.tree.find(9), None)
    
    def test_find_node(self):
        """ Test method for find node in the tree """
        self.assertEqual(self.tree._find(5, self.tree.getRoot()).data, 5)
        self.assertEqual(self.tree._find(3, self.tree.getRoot()).data, 3)
        self.assertEqual(self.tree._find(2, self.tree.getRoot()).data, 2)
        self.assertEqual(self.tree._find(4, self.tree.getRoot()).data, 4)
        self.assertEqual(self.tree._find(7, self.tree.getRoot()).data, 7)
        self.assertEqual(self.tree._find(6, self.tree.getRoot()).data, 6)
        self.assertEqual(self.tree._find(8, self.tree.getRoot()).data, 8)
        self.assertEqual(self.tree._find(9, self.tree.getRoot()), None)
