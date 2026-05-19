import unittest

from src.data_structure.queue.arr_fix import QueueArrFix

class TestNormalCases(unittest.TestCase):

    def setUp(self):
        self.queue = QueueArrFix(5)
        for i in [2,4,6,8]:
            self.queue.enqueue(i)
    
    def test_enqueue(self):
        self.queue.enqueue(12)
        self.assertEqual([self.queue.to_list(),self.queue.getRear(), self.queue.size],[[2,4,6,8,12], 12, 5])
    
    def test_dequeue(self):
        x = self.queue.dequeue()
        self.assertEqual([self.queue.to_list(), self.queue.getFront(), x, self.queue.size], [ [4,6,8], 4, 2, 3])
    
    def test_getFront(self):
        self.assertEqual([self.queue.getFront(), self.queue.to_list()], [ 2, [2,4,6,8]])
    
    def test_getRear(self):
        self.assertEqual([self.queue.getRear(), self.queue.to_list()], [ 8, [2,4,6,8]])
    
    def test_isEmpty(self):
        self.assertEqual(self.queue.isEmpty(), False)
    
    def test_isFull(self):
        self.assertEqual(self.queue.isFull(), False)
    

class TestEdgeCases(unittest.TestCase):

    def test_enqueue_empty(self):
        self.que = QueueArrFix(5)
        self.que.enqueue(34)
        self.assertEqual([self.que.to_list(),self.que.getRear(),self.que.getFront(), self.que.size],[[34], 34, 34, 1])
    
    def test_dequeue_1element(self):
        self.que = QueueArrFix(5)
        self.que.enqueue(34)
        ele_removed = self.que.dequeue()
        self.assertEqual([self.que.to_list(), self.que.size, ele_removed], [ [], 0, 34])
    
    def test_getFront_getRear_1element(self):
        self.que = QueueArrFix(5)
        self.que.enqueue(34)
        self.assertEqual([self.que.to_list(), self.que.getFront(), self.que.getRear()],[[34], 34, 34])
    
    def test_isEmpty_T(self):
        self.que = QueueArrFix(2)
        self.assertEqual(self.que.isEmpty(), True)
    
    def test_isFull_T(self):
        self.que = QueueArrFix(1)
        self.que.enqueue(34)
        self.assertEqual(self.que.isFull(), True)


class TestFailCases(unittest.TestCase):

    def test_enueue_overflow(self):
        self.que = QueueArrFix(1)
        self.que.enqueue(34)
        with self.assertRaises(OverflowError):
            self.que.enqueue(36)
    
    def test_dequeue_underflow(self):
        self.que = QueueArrFix(10)
        with self.assertRaises(IndexError):
            self.que.dequeue()
    
    def test_getFront_empty(self):
        self.que = QueueArrFix(10)
        with self.assertRaises(IndexError):
            self.que.getFront()
    
    def test_getRear_empty(self):
        self.que = QueueArrFix(10)
        with self.assertRaises(IndexError):
            self.que.getRear()