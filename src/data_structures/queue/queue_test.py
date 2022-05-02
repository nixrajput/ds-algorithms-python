import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
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


if __name__ == "__main__":
    unittest.main()
