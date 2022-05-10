import os
import sys

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from utils.comparator import Comparator


class Heap:
    def __init__(self, comparatorFunction=None):
        self.heapContainer = []
        self.compare = Comparator(comparatorFunction)

    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex) + 1

    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex) + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasParent(self, childIndex):
        return self.getParentIndex(childIndex) >= 0

    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex(parentIndex) < len(self.heapContainer)

    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex(parentIndex) < len(self.heapContainer)

    def leftChild(self, parentIndex):
        return self.heapContainer[self.getLeftChildIndex(parentIndex)]

    def rightChild(self, parentIndex):
        return self.heapContainer[self.getRightChildIndex(parentIndex)]

    def parent(self, childIndex):
        return self.heapContainer[self.getParentIndex(childIndex)]

    def swap(self, indexOne, indexTwo):
        self.heapContainer[indexOne], self.heapContainer[indexTwo] = (
            self.heapContainer[indexTwo],
            self.heapContainer[indexOne],
        )

    def pairIsInCorrectOrder(self, firstElement, secondElement):
        # Checks if pair of heap elements is in correct order.
        # For MinHeap the first element must be always smaller or equal.
        # For MaxHeap the first element must be always bigger or equal.
        print(
            f"You have to implement heap pair comparison method for {firstElement} and {secondElement} values."
        )

    def find(self, item, comparator=None):
        comparator = self.compare

        foundItemsIndices = []

        for itemIndex in range(len(self.heapContainer)):
            if comparator.equal(item, self.heapContainer[itemIndex]):
                foundItemsIndices.append(itemIndex)

        return foundItemsIndices

    def isEmpty(self):
        return not len(self.heapContainer)

    def heapifyUp(self, customStartIndex=None):
        # Take the last element (last in array or the bottom left in a tree)
        # in the heap container and lift it up until it is in the correct
        # order with respect to its parent element.
        currentIndex = (
            customStartIndex
            if (customStartIndex is not None)
            else len(self.heapContainer) - 1
        )

        while (
            self.hasParent(currentIndex)
            and self.pairIsInCorrectOrder(
                self.parent(currentIndex), self.heapContainer[currentIndex]
            )
            == False
        ):
            self.swap(currentIndex, self.getParentIndex(currentIndex))
            currentIndex = self.getParentIndex(currentIndex)

    def heapifyDown(self, customStartIndex=0):
        # Compare the parent element to its children and swap parent with the appropriate
        # child (smallest child for MinHeap, largest child for MaxHeap).
        # Do the same for next children after swap.
        currentIndex = customStartIndex
        nextIndex = None

        while self.hasLeftChild(currentIndex):
            if self.hasRightChild(currentIndex) and self.pairIsInCorrectOrder(
                self.rightChild(currentIndex), self.leftChild(currentIndex)
            ):
                nextIndex = self.getRightChildIndex(currentIndex)
            else:
                nextIndex = self.getLeftChildIndex(currentIndex)

            if self.pairIsInCorrectOrder(
                self.heapContainer[currentIndex], self.heapContainer[nextIndex]
            ):
                break

            self.swap(currentIndex, nextIndex)
            currentIndex = nextIndex

    def peek(self):
        if len(self.heapContainer) == 0:
            return None

        return self.heapContainer[0]

    def poll(self):
        if len(self.heapContainer) == 0:
            return None

        if len(self.heapContainer) == 1:
            return self.heapContainer.pop()

        item = self.heapContainer[0]

        # Move the last element from the end to the head.
        self.heapContainer[0] = self.heapContainer.pop()
        self.heapifyDown()

        return item

    def add(self, item):
        self.heapContainer.append(item)
        self.heapifyUp()

        return self

    def remove(self, item, comparator=None):
        comparator = self.compare

        numOfItemsToRemove = len(self.find(item, comparator))

        for _ in range(numOfItemsToRemove):
            # We need to find item index to remove each time after removal since
            # indices are being changed after each heapify process.
            indexToRemove = self.find(item, comparator).pop()

            # If we need to remove last child in the heap then just remove it.
            # There is no need to heapify the heap afterwards.
            if indexToRemove == (len(self.heapContainer) - 1):
                self.heapContainer.pop()
            else:
                # Move last element in heap to the vacant (removed) position.
                self.heapContainer[indexToRemove] = self.heapContainer.pop()

                parentItem = self.parent(indexToRemove)

                # If there is a left child and left child is not
                # in correct order with the node
                # we're going to delete then heapify down.
                if self.hasLeftChild(indexToRemove):
                    self.heapifyDown(indexToRemove)

        return self

    def toList(self):
        return self.heapContainer
