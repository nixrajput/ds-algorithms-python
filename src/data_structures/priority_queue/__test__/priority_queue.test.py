import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.priority_queue.priority_queue import PriorityQueue


class TestCase(unittest.TestCase):
    def test_create_default_priority_queue(self):
        """
        Test to create a default PriorityQueue
        """
        priorityQueue = PriorityQueue()

        self.assertIsInstance(priorityQueue, PriorityQueue)

    def test_insert_items_to_queue(self):
        """
        Test to insert items to the queue and respect priorities
        """
        priorityQueue = PriorityQueue()

        priorityQueue.add(10, 1)
        self.assertEqual(priorityQueue.peek(), 10)

        priorityQueue.add(5, 2)
        self.assertEqual(priorityQueue.peek(), 10)

        priorityQueue.add(100, 0)
        self.assertEqual(priorityQueue.peek(), 100)

    def test_objects_in_queue(self):
        """
        Test to use objects in priority queue
        """
        priorityQueue = PriorityQueue()

        user1 = {"name": "Ram"}
        user2 = {"name": "Krishna"}
        user3 = {"name": "Shiva"}

        priorityQueue.add(user1, 1)
        self.assertEqual(priorityQueue.peek(), user1)


if __name__ == "__main__":
    unittest.main()
