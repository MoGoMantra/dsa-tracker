import unittest

from src.data_structure.dequeue.dequeue_circ_arr import MyDequeu

class TestNormalCases(unittest.TestCase):

    def setUp(self):
        self.dq = MyDequeu(5)
        for i in [3,6,9,0]:
            self.dq.insertRear(i)
    
    def test_insertFront(self):
        self.dq.insertFront(12)
        self.assertEqual(self.dq.to_list(), [12,3,6,9,0])
    
    def test_insertRear(self):
        self.dq.insertRear(12)
        self.assertEqual(self.dq.to_list(), [3,6,9,0,12])
    
    def test_deleteFront(self):
        v = self.dq.deleteFront()
        self.assertEqual([self.dq.to_list(), v], [ [6,9,0], 3])
    
    def test_deleteRear(self):
        v = self.dq.deleteRear()
        self.assertEqual([self.dq.to_list(), v], [ [3,6,9], 0])
    
    def test_getFront(self):
        v = self.dq.GetFront()
        self.assertEqual([v, self.dq.to_list()], [3, [3,6,9,0]])
    
    def test_getRear(self):
        v = self.dq.GetRear()
        self.assertEqual([v, self.dq.to_list()], [0, [3,6,9,0]])
    
    def test_isNotEmpty(self):
        self.assertEqual(self.dq.isEmpty(), False)
    
    def test_isNotFull(self):
        self.assertEqual(self.dq.isFull(), False)


class TestEdgeCases(unittest.TestCase):

    def test_insertFront_Empty(self):
        self.dq = MyDequeu(5)
        self.dq.insertFront(45)
        self.assertEqual(self.dq.to_list(), [45])
    
    def test_insertRear_Empty(self):
        self.dq = MyDequeu(5)
        self.dq.insertRear(45)
        self.assertEqual(self.dq.to_list(), [45])
    
    def test_deleteFront_1element(self):
        self.dq = MyDequeu(5)
        self.dq.insertRear(45)
        v = self.dq.deleteFront()
        self.assertEqual([v, self.dq.to_list()], [45, [] ])
    
    def test_deleteRear_1element(self):
        self.dq = MyDequeu(5)
        self.dq.insertRear(45)
        v = self.dq.deleteRear()
        self.assertEqual([v, self.dq.to_list()], [45, [] ])
    
    def test_isEmpty(self):
        self.dq = MyDequeu(5)
        self.assertEqual(self.dq.isEmpty(), True)
    
    def test_isFull(self):
        self.dq = MyDequeu(1)
        self.dq.insertRear(45)
        self.assertEqual(self.dq.isFull(), True)


class TestFailCases(unittest.TestCase):

    def test_insertFront_overflow(self):
        self.dq = MyDequeu(4)
        for i in [3,6,9,0]:
            self.dq.insertRear(i)
        
        with self.assertRaises(OverflowError):
            self.dq.insertFront(23)
    
    def test_insertRear_overflow(self):
        self.dq = MyDequeu(4)
        for i in [3,6,9,0]:
            self.dq.insertRear(i)
        
        with self.assertRaises(OverflowError):
            self.dq.insertRear(23)
    
    def test_deleteFront_empty(self):
        self.dq = MyDequeu(2)
        with self.assertRaises(IndexError):
            self.dq.deleteFront()
    
    def test_deleteRear_empty(self):
        self.dq = MyDequeu(2)
        with self.assertRaises(IndexError):
            self.dq.deleteRear()
    
    def test_getFront_empty(self):
        self.dq = MyDequeu(2)
        with self.assertRaises(IndexError):
            self.dq.GetFront()
    
    def test_getRear_empty(self):
        self.dq = MyDequeu(2)
        with self.assertRaises(IndexError):
            self.dq.GetRear()