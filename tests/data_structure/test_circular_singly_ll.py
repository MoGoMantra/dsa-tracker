import unittest

from src.data_structure.linked_list.circular_ll import CircularSinglyLL

class TestNormalCases(unittest.TestCase):
    
    def setUp(self):
        self.cll = CircularSinglyLL()
        for i in [1,2,3]:
            self.cll.insert_at_end(i)
    
    def test_insert_at_front(self):
        self.cll.insert_at_front(5)
        self.assertEqual(self.cll.to_list(),[5,1,2,3])
    
    def test_insert_at_end(self):
        self.cll.insert_at_end(5)
        self.assertEqual(self.cll.to_list(),[1,2,3,5])
    
    def test_insert_at_pos(self):
        self.cll.insert_at_pos(3,12)
        self.assertEqual(self.cll.to_list(),[1,2,12,3])
    
    def test_delete_at_start(self):
        self.cll.delete_at_start()
        self.assertEqual(self.cll.to_list(),[2,3])
    
    def test_delete_at_end(self):
        self.cll.delete_at_end()
        self.assertEqual(self.cll.to_list(),[1,2])
    
    def test_delete_at_pos(self):
        self.cll.delete_at_pos(2)
        self.assertEqual(self.cll.to_list(),[1,3])
    
    def test_delete_node(self):
        self.cll.delete_node(2)
        self.assertEqual(self.cll.to_list(),[1,3])
    
    def test_search_pos(self):
        self.assertEqual(self.cll.search_pos(2),2)
    
    def test_search_node(self):
        self.assertEqual(self.cll.search_node(2),2)
    
    def test_reverse(self):
        self.cll.reverse()
        self.assertEqual(self.cll.to_list(),[3,2,1])


class TestEdgeCases(unittest.TestCase):

    def test_insert_at_front_empty(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_front(9)
        self.assertEqual(self.cll.to_list(),[9])
    
    def test_insert_at_end_empty(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(9)
        self.assertEqual(self.cll.to_list(),[9])
    
    def test_insert_at_pos_empty_pos1(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_pos(1,5)
        self.assertEqual(self.cll.to_list(),[5])
    
    def test_insert_at_pos_start(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_pos(1,1)
        self.cll.insert_at_pos(1,2)
        self.cll.insert_at_pos(1,3)
        self.cll.insert_at_pos(1,4)
        self.assertEqual(self.cll.to_list(), [4,3,2,1])
    
    def test_insert_at_pos_end(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(1)
        self.cll.insert_at_end(2)
        self.cll.insert_at_end(3)
        self.cll.insert_at_end(4)
        self.cll.insert_at_pos(5,10)
        self.assertEqual(self.cll.to_list(),[1,2,3,4,10])
    
    def test_delete_at_start_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(5)
        self.cll.delete_at_start()
        self.assertEqual(self.cll.to_list(),[])
    
    def test_delete_at_end_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(5)
        self.cll.delete_at_end()
        self.assertEqual(self.cll.to_list(),[])
    
    def test_delete_at_pos_start(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.cll.delete_at_pos(1)
        self.assertEqual(self.cll.to_list(),[4,6,8])
    
    def test_delete_at_pos_start_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(5)
        self.cll.delete_at_pos(1)
        self.assertEqual(self.cll.to_list(),[])
    
    def test_delete_at_pos_last(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.cll.delete_at_pos(4)
        self.assertEqual(self.cll.to_list(),[2,4,6])
    
    def test_delete_node_start(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.cll.delete_node(2)
        self.assertEqual(self.cll.to_list(),[4,6,8])
    
    def test_delete_node_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(4)
        self.cll.delete_node(4)
        self.assertEqual(self.cll.to_list(),[])
    
    def test_delete_node_last(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.cll.delete_node(8)
        self.assertEqual(self.cll.to_list(),[2,4,6])
    
    def test_search_pos_start(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.assertEqual(self.cll.search_pos(1),2)
    
    def test_search_pos_last(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.assertEqual(self.cll.search_pos(4),8)
    
    def test_search_pos_start(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(4)
        self.assertEqual(self.cll.search_pos(1),4)
    
    def test_search_node_start(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.assertEqual(self.cll.search_node(2),1)
    
    def test_search_node_last(self):
        self.cll = CircularSinglyLL()
        for i in [2,4,6,8]:
            self.cll.insert_at_end(i)
        self.assertEqual(self.cll.search_node(8),4)
    
    def test_search_node_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(4)
        self.assertEqual(self.cll.search_node(4),1)
    
    def test_reverse_1element(self):
        self.cll = CircularSinglyLL()
        self.cll.insert_at_end(4)
        self.cll.reverse()
        self.assertEqual(self.cll.to_list(),[4])


class TestFailCases(unittest.TestCase):

    def setUp(self):
        self.cll = CircularSinglyLL()
        for i in [1,2,3,4]:
            self.cll.insert_at_end(i)
    
    def test_insert_at_pos_invalid(self):
        with self.assertRaises(TypeError):
            self.cll.insert_at_pos(2.0, 20)
    
    def test_insert_at_pos_less1(self):
        with self.assertRaises(IndexError):
            self.cll.insert_at_pos(0,12)
    
    def test_insert_at_pos_empty_not1(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.insert_at_pos(3,12)
    
    def test_insert_at_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.cll.insert_at_pos(6,12)
    
    def test_delete_at_start_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.delete_at_start()
    
    def test_delete_at_end_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.delete_at_end()
    
    def test_delete_at_pos_invalid(self):
        with self.assertRaises(TypeError):
            self.cll.delete_at_pos(3.0)
    
    def test_delete_at_pos_less1(self):
        with self.assertRaises(IndexError):
            self.cll.delete_at_pos(0)
    
    def test_delete_at_pos_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.delete_at_pos(1)
    
    def test_delete_at_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.cll.delete_at_pos(5)
    
    def test_delete_node_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.delete_node(1)
    
    def test_delete_node_not_found(self):
        with self.assertRaises(ValueError):
            self.cll.delete_node(5)
    
    def test_search_pos_invalid(self):
        with self.assertRaises(TypeError):
            self.cll.search_pos(3.0)
    
    def test_search_pos_less1(self):
        with self.assertRaises(IndexError):
            self.cll.search_pos(0)
    
    def test_search_pos_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.search_pos(1)
    
    def test_search_pos_out_of_bound(self):
        with self.assertRaises(IndexError):
            self.cll.search_pos(5)
    
    def test_search_node_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.search_node(2)
    
    def test_search_node_not_found(self):
        with self.assertRaises(ValueError):
            self.cll.search_node(5)
    
    def test_reverse_empty(self):
        self.cll2 = CircularSinglyLL()
        with self.assertRaises(ValueError):
            self.cll2.reverse()

