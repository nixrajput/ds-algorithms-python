import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.linked_list.singly.linked_list import LinkedList


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        return not self.linkedList.head

    def peek(self):
        if self.isEmpty():
            return None

        return self.linkedList.head.value

    def enqueue(self, value):
        self.linkedList.append(value)

    def dequeue(self):
        removedHead = self.linkedList.deleteHead()
        return removedHead.value if (removedHead is not None) else None

    def toList(self, callback=None):
        return self.linkedList.toList(callback)
