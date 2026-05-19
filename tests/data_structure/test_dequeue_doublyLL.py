import unittest

from src.data_structure.dequeue.dequeue_doublyLL import DeQueue

class TestNormalCases(unittest.TestCase):

    def setUp(self):
        self.dq = DeQueue()
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
        v = self.dq.getFront()
        self.assertEqual([v, self.dq.to_list()], [3, [3,6,9,0]])
    
    def test_getRear(self):
        v = self.dq.getRear()
        self.assertEqual([v, self.dq.to_list()], [0, [3,6,9,0]])
    
    def test_isNotEmpty(self):
        self.assertEqual(self.dq.isEmpty(), False)


class TestEdgeCases(unittest.TestCase):

    def test_insertFront_Empty(self):
        self.dq = DeQueue()
        self.dq.insertFront(45)
        self.assertEqual(self.dq.to_list(), [45])
    
    def test_insertRear_Empty(self):
        self.dq = DeQueue()
        self.dq.insertRear(45)
        self.assertEqual(self.dq.to_list(), [45])
    
    def test_deleteFront_1element(self):
        self.dq = DeQueue()
        self.dq.insertRear(45)
        v = self.dq.deleteFront()
        self.assertEqual([v, self.dq.to_list()], [45, [] ])
    
    def test_deleteRear_1element(self):
        self.dq = DeQueue()
        self.dq.insertRear(45)
        v = self.dq.deleteRear()
        self.assertEqual([v, self.dq.to_list()], [45, [] ])
    
    def test_isEmpty(self):
        self.dq = DeQueue()
        self.assertEqual(self.dq.isEmpty(), True)


class TestFailCases(unittest.TestCase):
    
    def test_deleteFront_empty(self):
        self.dq = DeQueue()
        with self.assertRaises(IndexError):
            self.dq.deleteFront()
    
    def test_deleteRear_empty(self):
        self.dq = DeQueue()
        with self.assertRaises(IndexError):
            self.dq.deleteRear()
    
    def test_getFront_empty(self):
        self.dq = DeQueue()
        with self.assertRaises(IndexError):
            self.dq.getFront()
    
    def test_getRear_empty(self):
        self.dq = DeQueue()
        with self.assertRaises(IndexError):
            self.dq.getRear()