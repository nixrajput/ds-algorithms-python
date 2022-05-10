import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from utils.comparator import Comparator
from data_structures.heap.min_heap import MinHeap


class PriorityQueue(MinHeap):
    def __init__(self, comparatorFunction=None):
        super().__init__(comparatorFunction)

        self.priorities = dict()

        self.compare = Comparator(self.comparePriority)

    def compareValue(self, a, b):
        if a == b:
            return 0

        return -1 if a < b else 1

    def comparePriority(self, a, b):
        if self.priorities.get(a) == self.priorities.get(b):
            return 0

        return -1 if self.priorities.get(a) < self.priorities.get(b) else 1

    def add(self, item, priority=0):
        self.priorities[item] = priority
        super().add(item)
        return self

    def remove(self, item, comparator=None):
        super().remove(item, comparator)
        self.priorities.__delitem__(item)
        return self

    def changePriority(self, item, priority):
        self.remove(item, Comparator(self.compareValue))
        self.add(item, priority)
        return self

    def findByValue(self, item):
        return self.find(item, Comparator(self.compareValue))

    def hasValue(self, item):
        return len(self.findByValue(item)) > 0
