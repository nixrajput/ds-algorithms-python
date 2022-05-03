import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.queue.queue import Queue


class TestCase(unittest.TestCase):
    def test_create_empty_queue(self):
        """
        Test to create an empty Queue
        """
        queue = Queue()

        self.assertEqual(queue.toList(), [])

    def test_enqueue_data_to_queue(self):
        """
        Test to enqueue data to Queue
        """
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.toList(), [1, 2])

    def test_enqueue_dequeue_object_to_queue(self):
        """
        Test to enqueue or dequeue object data to Queue
        """
        queue = Queue()

        queue.enqueue({"value": "test1", "key": "key1"})
        queue.enqueue({"value": "test2", "key": "key2"})

        def stringifier(value):
            return f"{value['key']}:{value['value']}"

        self.assertEqual(queue.toList(stringifier), ["key1:test1", "key2:test2"])
        self.assertEqual(queue.dequeue()["value"], "test1")
        self.assertEqual(queue.dequeue()["value"], "test2")

    def test_peek_data_from_queue(self):
        """
        Test to peek data from Queue
        """
        queue = Queue()

        self.assertIsNone(queue.peek())

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)

    def test_check_queue_is_empty(self):
        """
        Test to check if Queue is empty
        """
        queue = Queue()

        self.assertTrue(queue.isEmpty())

        queue.enqueue(1)

        self.assertFalse(queue.isEmpty())

    def test_dequeue_data_from_queue(self):
        """
        Test to peek data from Queue
        """
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), None)
        self.assertTrue(queue.isEmpty())


if __name__ == "__main__":
    unittest.main()
