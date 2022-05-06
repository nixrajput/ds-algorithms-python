import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.heap.max_heap import MaxHeap
from utils.comparator import Comparator


class TestCase(unittest.TestCase):
    def test_create_empty_max_heap(self):
        """
        Test to create an empty MaxHeap
        """
        maxHeap = MaxHeap()

        self.assertIsNone(maxHeap.peek())
        self.assertTrue(maxHeap.isEmpty())

    def test_add_items_to_heap(self):
        """
        Test to add items to the heap and heapify it up
        """
        maxHeap = MaxHeap()

        maxHeap.add(5)

        self.assertFalse(maxHeap.isEmpty())
        self.assertEqual(maxHeap.peek(), 5)
        self.assertEqual(maxHeap.toList(), [5])

        maxHeap.add(3)

        self.assertEqual(maxHeap.peek(), 5)
        self.assertEqual(maxHeap.toList(), [5, 3])

        maxHeap.add(10)

        self.assertEqual(maxHeap.peek(), 10)
        self.assertEqual(maxHeap.toList(), [10, 3, 5])

    def test_poll_items_from_heap(self):
        """
        Test to poll items from the heap and heapify it down
        """
        maxHeap = MaxHeap()

        maxHeap.add(5)
        maxHeap.add(3)
        maxHeap.add(10)
        maxHeap.add(11)
        maxHeap.add(1)

        self.assertEqual(maxHeap.toList(), [11, 10, 5, 3, 1])

        self.assertEqual(maxHeap.poll(), 11)
        self.assertEqual(maxHeap.toList(), [10, 3, 5, 1])

        self.assertEqual(maxHeap.poll(), 10)
        self.assertEqual(maxHeap.toList(), [5, 3, 1])

        self.assertEqual(maxHeap.poll(), 5)
        self.assertEqual(maxHeap.toList(), [3, 1])

        self.assertEqual(maxHeap.poll(), 3)
        self.assertEqual(maxHeap.toList(), [1])

        self.assertEqual(maxHeap.poll(), 1)
        self.assertEqual(maxHeap.toList(), [])

        self.assertEqual(maxHeap.poll(), None)
        self.assertEqual(maxHeap.toList(), [])

    def test_heapify_down_from_right_beanch_in_heap(self):
        """
        Test to heapify down through the right branch as well
        """
        maxHeap = MaxHeap()

        maxHeap.add(3)
        maxHeap.add(12)
        maxHeap.add(10)

        self.assertEqual(maxHeap.toList(), [12, 3, 10])

        maxHeap.add(11)
        self.assertEqual(maxHeap.toList(), [12, 11, 10, 3])

        self.assertEqual(maxHeap.poll(), 12)
        self.assertEqual(maxHeap.toList(), [11, 3, 10])

    def test_find_item_indices_in_heap(self):
        """
        Test to find item indices in heap
        """
        maxHeap = MaxHeap()

        maxHeap.add(3)
        maxHeap.add(12)
        maxHeap.add(10)
        maxHeap.add(11)
        maxHeap.add(11)

        self.assertEqual(maxHeap.toList(), [12, 11, 10, 3, 11])

        self.assertEqual(maxHeap.find(5), [])
        self.assertEqual(maxHeap.find(12), [0])
        self.assertEqual(maxHeap.find(11), [1, 4])

    def test_remove_items_with_heapify_down_from_heap(self):
        """
        Test to remove items from heap with heapify down
        """
        maxHeap = MaxHeap()

        maxHeap.add(3)
        maxHeap.add(12)
        maxHeap.add(10)
        maxHeap.add(11)
        maxHeap.add(11)

        self.assertEqual(maxHeap.toList(), [12, 11, 10, 3, 11])

        self.assertEqual(maxHeap.remove(12).toList(), [11, 11, 10, 3])
        self.assertEqual(maxHeap.remove(12).peek(), 11)
        self.assertEqual(maxHeap.remove(11).toList(), [10, 3])
        self.assertEqual(maxHeap.remove(10).peek(), 3)

    def test_remove_items_with_heapify_up_from_heap(self):
        """
        Test to remove items from heap with heapify up
        """
        maxHeap = MaxHeap()

        maxHeap.add(3)
        maxHeap.add(10)
        maxHeap.add(5)
        maxHeap.add(6)
        maxHeap.add(7)
        maxHeap.add(4)
        maxHeap.add(6)
        maxHeap.add(8)
        maxHeap.add(2)
        maxHeap.add(1)

        self.assertEqual(maxHeap.toList(), [10, 8, 6, 7, 6, 4, 5, 3, 2, 1])

        self.assertEqual(maxHeap.remove(4).toList(), [10, 8, 6, 7, 6, 1, 5, 3, 2])
        self.assertEqual(maxHeap.remove(3).toList(), [10, 8, 6, 7, 6, 1, 5, 2])
        self.assertEqual(maxHeap.remove(5).toList(), [10, 8, 6, 7, 6, 1, 2])
        self.assertEqual(maxHeap.remove(10).toList(), [2, 8, 6, 7, 6, 1])
        self.assertEqual(maxHeap.remove(6).toList(), [2, 8, 1, 7])
        self.assertEqual(maxHeap.remove(2).toList(), [7, 8, 1])
        self.assertEqual(maxHeap.remove(1).toList(), [7, 8])
        self.assertEqual(maxHeap.remove(7).toList(), [8])
        self.assertEqual(maxHeap.remove(8).toList(), [])

    def test_remove_items_with_custom_comparator_from_heap(self):
        """
        Test to remove items from heap with custom finding comparator
        """
        maxHeap = MaxHeap()

        maxHeap.add("a")
        maxHeap.add("bb")
        maxHeap.add("ccc")
        maxHeap.add("dddd")

        self.assertEqual(maxHeap.toList(), ["dddd", "ccc", "bb", "a"])

        def customFun(a, b):
            if len(a) == len(b):
                return 0

            return -1 if (len(a) < len(b)) else 1

        comparator = Comparator(customFun)

        maxHeap.remove("ccc", comparator)
        self.assertEqual(maxHeap.toList(), ["dddd", "a", "bb"])


if __name__ == "__main__":
    unittest.main()
