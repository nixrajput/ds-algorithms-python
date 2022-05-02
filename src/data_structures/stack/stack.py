import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.linked_list.singly.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        return not self.linkedList.head

    def peek(self):
        if self.isEmpty():
            return None

        return self.linkedList.head.value

    def push(self, value):
        self.linkedList.prepend(value)

    def pop(self):
        removedHead = self.linkedList.deleteHead()
        return removedHead.value if removedHead else None

    def toArray(self):
        nodes = []
        for node in self.linkedList.toArray():
            nodes.append(node.value)

        return nodes

    def toList(self, callback=None):
        return self.linkedList.toList(callback)
