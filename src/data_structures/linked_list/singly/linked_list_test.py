import unittest
from linked_list import LinkedList


class TestCase(unittest.TestCase):
    def test_empty_linked_list(self):
        """
        Test to create an empty LinkedList
        """
        linkedList = LinkedList()
        self.assertEqual(linkedList.toList(), [])

    def test_append_to_linked_list(self):
        """
        Test to append nodes to the LinkedList
        """
        linkedList = LinkedList()

        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

        linkedList.append(1)
        linkedList.append(2)

        self.assertListEqual(linkedList.toList(), [1, 2])
        self.assertIsNone(linkedList.tail.next)

    def test_prepend_to_linked_list(self):
        """
        Test to prepend node to the LinkedList
        """
        linkedList = LinkedList()

        linkedList.prepend(2)

        self.assertEqual(linkedList.head.toString(), 2)
        self.assertEqual(linkedList.tail.toString(), 2)

        linkedList.append(1)
        linkedList.prepend(3)

        self.assertListEqual(linkedList.toList(), [3, 2, 1])

    def test_insert_to_linked_list(self):
        """
        Test to insert node to the LinkedList
        """
        linkedList = LinkedList()

        linkedList.insert(4, 3)

        self.assertEqual(linkedList.head.toString(), 4)
        self.assertEqual(linkedList.tail.toString(), 4)

        linkedList.insert(3, 2)
        linkedList.insert(2, 1)
        linkedList.insert(1, -7)
        linkedList.insert(10, 9)

        self.assertListEqual(linkedList.toList(), [1, 4, 2, 3, 10])

    def test_delete_node_from_linked_list(self):
        """
        Test to delete node by value from the LinkedList
        """
        linkedList = LinkedList()

        self.assertIsNone(linkedList.delete(7))

        linkedList.append(1)
        linkedList.append(1)
        linkedList.append(2)
        linkedList.append(3)
        linkedList.append(3)
        linkedList.append(3)
        linkedList.append(4)
        linkedList.append(5)

        self.assertEqual(linkedList.head.toString(), 1)
        self.assertEqual(linkedList.tail.toString(), 5)

        deletedNode = linkedList.delete(3)
        self.assertEqual(deletedNode.value, 3)
        self.assertListEqual(linkedList.toList(), [1, 1, 2, 4, 5])

        linkedList.delete(3)
        self.assertListEqual(linkedList.toList(), [1, 1, 2, 4, 5])

        linkedList.delete(1)
        self.assertListEqual(linkedList.toList(), [2, 4, 5])

        linkedList.delete(5)
        self.assertListEqual(linkedList.toList(), [2, 4])

        self.assertEqual(linkedList.head.toString(), 2)
        self.assertEqual(linkedList.tail.toString(), 4)

        linkedList.delete(4)
        self.assertListEqual(linkedList.toList(), [2])

        self.assertEqual(linkedList.head.toString(), 2)
        self.assertEqual(linkedList.tail.toString(), 2)

        linkedList.delete(2)
        self.assertListEqual(linkedList.toList(), [])

    def test_delete_tail_node_from_linked_list(self):
        """
        Test to delete tail node from the LinkedList
        """
        linkedList = LinkedList()

        linkedList.append(1)
        linkedList.append(2)
        linkedList.append(3)

        self.assertEqual(linkedList.head.toString(), 1)
        self.assertEqual(linkedList.tail.toString(), 3)

        deletedNode1 = linkedList.deleteTail()

        self.assertEqual(deletedNode1.value, 3)
        self.assertListEqual(linkedList.toList(), [1, 2])
        self.assertEqual(linkedList.head.toString(), 1)
        self.assertEqual(linkedList.tail.toString(), 2)

        deletedNode2 = linkedList.deleteTail()

        self.assertEqual(deletedNode2.value, 2)
        self.assertListEqual(linkedList.toList(), [1])
        self.assertEqual(linkedList.head.toString(), 1)
        self.assertEqual(linkedList.tail.toString(), 1)

        deletedNode3 = linkedList.deleteTail()

        self.assertEqual(deletedNode3.value, 1)
        self.assertListEqual(linkedList.toList(), [])
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

    def test_delete_head_node_from_linked_list(self):
        """
        Test to delete head node from the LinkedList
        """
        linkedList = LinkedList()

        linkedList.append(1)
        linkedList.append(2)

        self.assertEqual(linkedList.head.toString(), 1)
        self.assertEqual(linkedList.tail.toString(), 2)

        deletedNode1 = linkedList.deleteHead()

        self.assertEqual(deletedNode1.value, 1)
        self.assertListEqual(linkedList.toList(), [2])
        self.assertEqual(linkedList.head.toString(), 2)
        self.assertEqual(linkedList.tail.toString(), 2)

        deletedNode2 = linkedList.deleteHead()

        self.assertEqual(deletedNode2.value, 2)
        self.assertListEqual(linkedList.toList(), [])
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

    def test_store_objects_in_linked_list(self):
        """
        Test to store objects in the LinkedList and print them out
        """
        linkedList = LinkedList()

        nodeValue1 = {"value": 1, "key": "key1"}
        nodeValue2 = {"value": 2, "key": "key2"}

        linkedList.append(nodeValue1)
        linkedList.prepend(nodeValue2)

        def nodeStringifier(value):
            return f"{value['key']}:{value['value']}"

        self.assertEqual(linkedList.toList(nodeStringifier), ["key2:2", "key1:1"])

    def test_find_node_by_value_in_linked_list(self):
        """
        Test to find node by value in the LinkedList
        """
        linkedList = LinkedList()

        self.assertIsNone(linkedList.find(value=5))

        linkedList.append(1).append(2).append(3)
        self.assertListEqual(linkedList.toList(), [1, 2, 3])

        node = linkedList.find(value=2)

        self.assertEqual(node.value, 2)
        self.assertIsNone(linkedList.find(value=5))

    def test_find_node_by_callback_in_linked_list(self):
        """
        Test to find node by callback in the LinkedList
        """
        linkedList = LinkedList()

        linkedList.append({"value": 1, "key": "test1"})
        linkedList.append({"value": 2, "key": "test2"})
        linkedList.append({"value": 3, "key": "test3"})
        self.assertListEqual(
            linkedList.toList(),
            [
                {"key": "test1", "value": 1},
                {"key": "test2", "value": 2},
                {"key": "test3", "value": 3},
            ],
        )

        def dictCallback(value):
            return value["key"] == "test2"

        node = linkedList.find(callback=dictCallback)

        self.assertEqual(node.value["value"], 2)
        self.assertEqual(node.value["key"], "test2")

        def dictCallback2(value):
            return value["key"] == "test5"

        self.assertIsNone(linkedList.find(callback=dictCallback2))

    def test_create_linked_list_from_array(self):
        """
        Test to create a LinkedList from an array
        """
        linkedList = LinkedList()

        linkedList.fromArray([1, 1, 2, 3, 3, 3, 4, 7, 8])

        self.assertListEqual(linkedList.toList(), [1, 1, 2, 3, 3, 3, 4, 7, 8])

    def test_find_node_by_custom_compare_function(self):
        """
        Test to find node by means of custom compare function in LinkedList
        """

        def comparatorFunction(a, b):
            if a["customValue"] == b["customValue"]:
                return 0

            return -1 if (a["customValue"] < b["customValue"]) else 1

        linkedList = LinkedList(comparatorFunction)

        linkedList.append({"value": 1, "customValue": "test1"})
        linkedList.append({"value": 2, "customValue": "test2"})
        linkedList.append({"value": 3, "customValue": "test3"})

        node = linkedList.find(value={"value": 2, "customValue": "test2"})

        self.assertEqual(node.value["value"], 2)
        self.assertEqual(node.value["customValue"], "test2")
        self.assertIsNone(linkedList.find(value={"value": 2, "customValue": "test5"}))

    def test_find_preferring_callback_over_compare_function(self):
        """
        Test to find preferring callback over compare function in LinkedList
        """

        def greaterThan(value, compareTo):
            return 0 if (value > compareTo) else 1

        linkedList = LinkedList(greaterThan)

        linkedList.fromArray([1, 2, 3, 4, 5])

        node = linkedList.find(value=3)
        self.assertEqual(node.value, 4)

        node = linkedList.find(callback=lambda value: value < 3)
        self.assertEqual(node.value, 1)

    def test_reverse_linked_list(self):
        """
        Test to reverse the nodes in LinkedList
        """
        linkedList = LinkedList()

        linkedList.append(1)
        linkedList.append(2)
        linkedList.append(3)

        self.assertListEqual(linkedList.toList(), [1, 2, 3])
        self.assertEqual(linkedList.head.value, 1)
        self.assertEqual(linkedList.tail.value, 3)

        linkedList.reverse()
        self.assertListEqual(linkedList.toList(), [3, 2, 1])
        self.assertEqual(linkedList.head.value, 3)
        self.assertEqual(linkedList.tail.value, 1)


if __name__ == "__main__":
    unittest.main()
