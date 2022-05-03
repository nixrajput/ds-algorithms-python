import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.heap.max_heap import MaxHeap


class TestCase(unittest.TestCase):
    def test_create_empty_max_heap(self):
        """
        Test to create an empty MaxHeap
        """
        maxHeap = MaxHeap()

        self.assertIsNone(maxHeap.peek())
        self.assertTrue(maxHeap.isEmpty())


if __name__ == "__main__":
    unittest.main()
