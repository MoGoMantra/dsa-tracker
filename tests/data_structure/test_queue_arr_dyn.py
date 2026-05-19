import unittest

from src.data_structure.queue.arr_dyn import QueueArrDyn

class TestNormalCases(unittest.TestCase):

    def setUp(self):
        self.q = QueueArrDyn()
        for i in [3,6,9,12]:
            self.q.enqueue(i)
    
    def test_getFront(self):
        self.assertEqual(self.q.getFront(), 3)
    
    def test_getRear(self):
        self.assertEqual(self.q.getRear(), 12)
    
    def test_size(self):
        self.assertEqual(self.q.size(), 4)
    
    def test_enqueue(self):
        self.q.enqueue(21)
        self.assertEqual([self.q.to_list(), self.q.size(), self.q.getFront(), self.q.getRear()], [ [3,6,9,12,21], 5, 3, 21])
    
    def test_dequeue(self):
        val_removed = self.q.dequeue()
        self.assertEqual([self.q.to_list(), self.q.size(), self.q.getFront(), self.q.getRear(), val_removed], [ [6,9,12], 3, 6, 12, 3])
    
    def test_isEmpty(self):
        self.assertEqual(self.q.isEmpty(), False)


class TestEdgeCases(unittest.TestCase):

    def test_enqueue_empty(self):
        self.q = QueueArrDyn()
        self.q.enqueue(13)
        self.assertEqual([self.q.to_list(), self.q.size(), self.q.getFront(), self.q.getRear()], [ [13], 1, 13, 13])
    
    def test_dequeue_1element(self):
        self.q = QueueArrDyn()
        self.q.enqueue(13)
        val_removed = self.q.dequeue()
        self.assertEqual([self.q.to_list(), self.q.size(), val_removed], [ [], 0, 13])
    
    def test_getFront_getRear_1element(self):
        self.que = QueueArrDyn()
        self.que.enqueue(34)
        self.assertEqual([self.que.to_list(), self.que.getFront(), self.que.getRear()],[[34], 34, 34])
    
    def test_isEmpty(self):
        self.q = QueueArrDyn()
        self.assertEqual(self.q.isEmpty(), True)


class TestFailCases(unittest.TestCase):

    def test_dequeue_empty(self):
        self.q = QueueArrDyn()
        with self.assertRaises(IndexError):
            self.q.dequeue()
    
    def test_getFront_empty(self):
        self.q = QueueArrDyn()
        with self.assertRaises(IndexError):
            self.q.getFront()
    
    def test_getRear_empty(self):
        self.q = QueueArrDyn()
        with self.assertRaises(IndexError):
            self.q.getRear()