import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from utils.comparator import Comparator
from data_structures.linked_list.singly.linked_list_node import LinkedListNode


class LinkedList:
    def __init__(self, comparatorFunction=None):
        self.head = None
        self.tail = None
        self.compare = Comparator(comparatorFunction)

    def prepend(self, value):
        # Make new node to be a head
        newNode = LinkedListNode(value, self.head)
        self.head = newNode

        # If there is no tail yet let's make new node a tail
        if not self.tail:
            self.tail = newNode

        return self

    def append(self, value):
        newNode = LinkedListNode(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

            return self

        self.tail.next = newNode
        self.tail = newNode

        return self

    def insert(self, value, rawIndex):
        index = 0 if (rawIndex < 0) else rawIndex

        if index == 0:
            self.prepend(value)
        else:
            count = 1
            currentNode = self.head
            newNode = LinkedListNode(value)

            while currentNode:
                if count == index:
                    break
                currentNode = currentNode.next
                count += 1

            if currentNode:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                if self.tail:
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    self.head = newNode
                    self.tail = newNode

        return self

    def delete(self, value):
        if not self.head:
            return None

        deleteNode = None

        # If the head must be deleted then make next node that is different
        # from the head to be a new head
        while self.head and self.compare.equal(self.head.value, value):
            deleteNode = self.head
            self.head = self.head.next

        currentNode = self.head

        if currentNode:
            while currentNode.next:
                if self.compare.equal(currentNode.next.value, value):
                    deleteNode = currentNode.next
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next

        if self.compare.equal(self.tail.value, value):
            self.tail = currentNode

        return deleteNode

    def find(self, value=None, callback=None):
        if not self.head:
            return None

        currentNode = self.head

        while currentNode:
            if callback and callback(currentNode.value):
                return currentNode

            if value != None and self.compare.equal(currentNode.value, value):
                return currentNode

            currentNode = currentNode.next

        return None

    def deleteTail(self):
        deletedTail = self.tail

        if self.head == self.tail:
            # There is only one node in linked list
            self.head = None
            self.tail = None

            return deletedTail

        # If there is many node in linked list
        # Rewind to the last node and delete "next" link for
        # the node before the last one
        currentNode = self.head

        while currentNode.next:
            if not currentNode.next.next:
                currentNode.next = None
            else:
                currentNode = currentNode.next

        self.tail = currentNode

        return deletedTail

    def deleteHead(self):
        if not self.head:
            return None

        deletedHead = self.head

        if self.head.next:
            self.head = self.head.next
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

            currNode.next = prevNode

            prevNode = currNode
            currNode = nextNode

        self.tail = self.head
        self.head = prevNode

        return self
