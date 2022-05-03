import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.heap.heap import Heap


class MinHeap(Heap):
    """
    * Checks if pair of heap elements is in correct order.
    * For MinHeap the first element must be always smaller or equal.
    * For MaxHeap the first element must be always bigger or equal.
    """

    def pairIsInCorrectOrder(self, firstElement, secondElement):
        return self.compare.lessThanOrEqual(firstElement, secondElement)
