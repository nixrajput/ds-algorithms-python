import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from utils.comparator import Comparator
from data_structures.linked_list.doubly.doubly_linked_list_node import (
    DoublyLinkedListNode,
)


class DoublyLinkedList:
    def __init__(self, comparatorFunction=None):
        self.head = None
        self.tail = None
        self.compare = Comparator(comparatorFunction)

    def prepend(self, value):
        newNode = DoublyLinkedListNode(value, self.head)

        if self.head is not None:
            self.head.previous = newNode

        self.head = newNode

        if not self.tail:
            self.tail = newNode

        return self

    def append(self, value):
        newNode = DoublyLinkedListNode(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode

            return self

        self.tail.next = newNode

        newNode.previous = self.tail

        self.tail = newNode

        return self

    def delete(self, value):
        if not self.head:
            return None

        deletedNode = None
        currentNode = self.head

        while currentNode:
            if self.compare.equal(currentNode.value, value):
                deletedNode = currentNode

                if deletedNode == self.head:
                    self.head = deletedNode.next

                    if self.head:
                        self.head.previous = None

                    if deletedNode == self.tail:
                        self.tail = None
                elif deletedNode == self.tail:
                    self.tail = deletedNode.previous
                    self.tail.next = None
                else:
                    previousNode = deletedNode.previous
                    nextNode = deletedNode.next

                    previousNode.next = nextNode
                    nextNode.previous = previousNode

            currentNode = currentNode.next

        return deletedNode

    def find(self, value=None, callback=None):
        if not self.head:
            return None

        currentNode = self.head

        while currentNode:
            if callback and callback(currentNode.value):
                return currentNode

            if value is not None and self.compare.equal(currentNode.value, value):
                return currentNode

            currentNode = currentNode.next

        return None

    def deleteTail(self):
        if not self.tail:
            return None

        if self.head == self.tail:
            deletedNode = self.tail
            self.head = None
            self.tail = None

            return deletedNode

        deletedTail = self.tail

        self.tail = self.tail.previous
        self.tail.next = None

        return deletedTail

    def deleteHead(self):
        if not self.head:
            return None

        deletedHead = self.head

        if self.head.next:
            self.head = self.head.next
            self.head.previous = None
        else:
            self.head = None
            self.tail = None

        return deletedHead

    def fromArray(self, values):
        for value in values:
            self.append(value)

        return self

    def toArray(self):
        nodes = []

        currentNode = self.head

        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next

        return nodes

    def toList(self, callback=None):
        nodes = []
        for node in self.toArray():
            if callback is not None:
                nodes.append(node.toString(callback))
            else:
                nodes.append(node.toString())

        return nodes

    def reverse(self):
        currNode = self.head
        prevNode = None
        nextNode = None

        while currNode:
            nextNode = currNode.next
            prevNode = currNode.previous

            currNode.next = prevNode
            currNode.previous = nextNode

            prevNode = currNode
            currNode = nextNode

        self.tail = self.head
        self.head = prevNode

        return self
