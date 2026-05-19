import unittest

from src.data_structure.queue.circular_queue_LL import MyQueue

class TestNormalCases(unittest.TestCase):
    
    def test_enqueue_circular(self):
        self.q = MyQueue()
        for i in [2,4,6,8]:
            self.q.enqueue(i)
        self.assertEqual(self.q.to_list(), [2,4,6,8])
    
    def test_dequeue_circular(self):
        self.q = MyQueue()
        for i in [2,4,6,8]:
            self.q.enqueue(i)
        x = self.q.dequeue()
        self.assertEqual(self.q.to_list(), [4,6,8])

class TestEdgeCases(unittest.TestCase):

    def test_enq_empty(self):
        self.q = MyQueue()
        self.q.enqueue(4)
        self.assertEqual(self.q.to_list(), [4])
    
    def test_deq_1element(self):
        self.q = MyQueue()
        self.q.enqueue(4)
        x = self.q.dequeue()
        self.assertEqual(self.q.to_list(), [])


class TestFailCases(unittest.TestCase):

    def test_deq_empty(self):
        self.q = MyQueue()
        with self.assertRaises(IndexError):
            self.q.dequeue()
