import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.heap.min_heap import MinHeap
from utils.comparator import Comparator


class TestCase(unittest.TestCase):
    def test_create_empty_max_heap(self):
        """
        Test to create an empty minHeap
        """
        minHeap = MinHeap()

        self.assertIsNone(minHeap.peek())
        self.assertTrue(minHeap.isEmpty())

    def test_add_items_to_heap(self):
        """
        Test to add items to the heap and heapify it up
        """
        minHeap = MinHeap()

        minHeap.add(5)

        self.assertFalse(minHeap.isEmpty())
        self.assertEqual(minHeap.peek(), 5)
        self.assertEqual(minHeap.toList(), [5])

        minHeap.add(3)

        self.assertEqual(minHeap.peek(), 3)
        self.assertEqual(minHeap.toList(), [3, 5])

        minHeap.add(10)

        self.assertEqual(minHeap.peek(), 3)
        self.assertEqual(minHeap.toList(), [3, 5, 10])

    def test_poll_items_from_heap(self):
        """
        Test to poll items from the heap and heapify it down
        """
        minHeap = MinHeap()

        minHeap.add(5)
        minHeap.add(3)
        minHeap.add(10)
        minHeap.add(11)
        minHeap.add(1)

        self.assertEqual(minHeap.toList(), [1, 3, 10, 11, 5])

        self.assertEqual(minHeap.poll(), 1)
        self.assertEqual(minHeap.toList(), [3, 5, 10, 11])

        self.assertEqual(minHeap.poll(), 3)
        self.assertEqual(minHeap.toList(), [5, 11, 10])

        self.assertEqual(minHeap.poll(), 5)
        self.assertEqual(minHeap.toList(), [10, 11])

        self.assertEqual(minHeap.poll(), 10)
        self.assertEqual(minHeap.toList(), [11])

        self.assertEqual(minHeap.poll(), 11)
        self.assertEqual(minHeap.toList(), [])

        self.assertEqual(minHeap.poll(), None)
        self.assertEqual(minHeap.toList(), [])

    def test_heapify_down_from_right_beanch_in_heap(self):
        """
        Test to heapify down through the right branch as well
        """
        minHeap = MinHeap()

        minHeap.add(3)
        minHeap.add(12)
        minHeap.add(10)

        self.assertEqual(minHeap.toList(), [3, 12, 10])

        minHeap.add(11)
        self.assertEqual(minHeap.toList(), [3, 11, 10, 12])

        self.assertEqual(minHeap.poll(), 3)
        self.assertEqual(minHeap.toList(), [10, 11, 12])

    def test_find_item_indices_in_heap(self):
        """
        Test to find item indices in heap
        """
        minHeap = MinHeap()

        minHeap.add(3)
        minHeap.add(12)
        minHeap.add(10)
        minHeap.add(11)
        minHeap.add(11)

        self.assertEqual(minHeap.toList(), [3, 11, 10, 12, 11])

        self.assertEqual(minHeap.find(5), [])
        self.assertEqual(minHeap.find(3), [0])
        self.assertEqual(minHeap.find(11), [1, 4])

    def test_remove_items_from_heap(self):
        """
        Test to remove items from heap
        """
        minHeap = MinHeap()

        minHeap.add(3)
        minHeap.add(10)
        minHeap.add(5)
        minHeap.add(6)
        minHeap.add(7)
        minHeap.add(4)
        minHeap.add(6)
        minHeap.add(8)
        minHeap.add(2)
        minHeap.add(1)

        self.assertEqual(minHeap.toList(), [1, 2, 4, 6, 3, 5, 6, 10, 8, 7])

        self.assertEqual(minHeap.remove(8).toList(), [1, 2, 4, 6, 3, 5, 6, 10, 7])
        self.assertEqual(minHeap.remove(7).toList(), [1, 2, 4, 6, 3, 5, 6, 10])
        self.assertEqual(minHeap.remove(1).toList(), [2, 3, 4, 6, 10, 5, 6])
        self.assertEqual(minHeap.remove(2).toList(), [3, 6, 4, 6, 10, 5])
        self.assertEqual(minHeap.remove(6).toList(), [3, 5, 4, 10])
        self.assertEqual(minHeap.remove(10).toList(), [3, 5, 4])
        self.assertEqual(minHeap.remove(5).toList(), [3, 4])
        self.assertEqual(minHeap.remove(3).toList(), [4])
        self.assertEqual(minHeap.remove(4).toList(), [])

    def test_remove_items_with_custom_comparator_from_heap(self):
        """
        Test to remove items from heap with custom finding comparator
        """
        minHeap = MinHeap()

        minHeap.add("a")
        minHeap.add("bb")
        minHeap.add("ccc")
        minHeap.add("dddd")

        self.assertEqual(minHeap.toList(), ["a", "bb", "ccc", "dddd"])

        def customFun(a, b):
            if len(a) == len(b):
                return 0

            return -1 if (len(a) < len(b)) else 1

        comparator = Comparator(customFun)

        minHeap.remove("ccc", comparator)
        self.assertEqual(minHeap.toList(), ["a", "bb", "dddd"])


if __name__ == "__main__":
    unittest.main()
