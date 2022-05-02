import os
import sys
from typing import List
import functools

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.linked_list.singly.linked_list import LinkedList

defaultHashTableSize = 32


class HashTable:
    def __init__(self, hashTableSize=defaultHashTableSize):
        arr = list()
        for _ in range(hashTableSize):
            arr.append(None)

        bucketList = list()
        for _ in range(len(arr)):
            bucketList.append(LinkedList())

        self.buckets = bucketList
        self.keys = {}

    def hash(self, key):
        listFromKey = list(key)

        hashedKey = 0
        for char in listFromKey:
            hashedKey += ord(char)

        return hashedKey % len(self.buckets)

    def set(self, key, value):
        keyHash = self.hash(key)
        self.keys[key] = keyHash
        bucketLinkedList = self.buckets[keyHash]

        def getNode(nodeValue):
            return nodeValue["key"] == key

        node = bucketLinkedList.find(callback=getNode)

        if not node:
            bucketLinkedList.append({"key": key, "value": value})
        else:
            node.value["value"] = value

    def delete(self, key):
        keyHash = self.hash(key)
        bucketLinkedList = self.buckets[keyHash]

        def getNode(nodeValue):
            return nodeValue["key"] == key

        node = bucketLinkedList.find(callback=getNode)

        if node:
            del self.keys[key]
            return bucketLinkedList.delete(node.value)

        return None

    def get(self, key):
        bucketLinkedList = self.buckets[self.hash(key)]

        def getNode(nodeValue):
            return nodeValue["key"] == key

        node = bucketLinkedList.find(callback=getNode)

        return node.value["value"] if node else None

    def has(self, key):
        if key in self.keys:
            return True

        return False

    def getKeys(self):
        keys = []

        for key in self.keys:
            keys.append(key)
        return keys

    def getValues(self):
        bucketValues = list()
        for bucket in self.buckets:
            for linkedListNode in bucket.toArray():
                bucketValues.append(linkedListNode.value["value"])

        return bucketValues
