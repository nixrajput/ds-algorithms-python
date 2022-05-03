import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(file_path))))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.stack.stack import Stack


class TestCase(unittest.TestCase):
    def test_create_empty_stack(self):
        """
        Test to create an empty Stack
        """
        stack = Stack()

        self.assertEqual(stack.toList(), [])
        self.assertIsNotNone(stack.linkedList)

    def test_push_data_to_stack(self):
        """
        Test to push data to Stack
        """
        stack = Stack()

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.toList(), [2, 1])

    def test_push_pop_object_to_stack(self):
        """
        Test to push or pop object data to Stack
        """
        stack = Stack()

        stack.push({"value": "test1", "key": "key1"})
        stack.push({"value": "test2", "key": "key2"})

        def stringifier(value):
            return f"{value['key']}:{value['value']}"

        self.assertEqual(stack.toList(stringifier), ["key2:test2", "key1:test1"])
        self.assertEqual(stack.pop()["value"], "test2")
        self.assertEqual(stack.pop()["value"], "test1")

    def test_peek_data_from_stack(self):
        """
        Test to peek data from Stack
        """
        stack = Stack()

        self.assertIsNone(stack.peek())

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek(), 2)

    def test_check_stack_is_empty(self):
        """
        Test to check if Stack is empty
        """
        stack = Stack()

        self.assertTrue(stack.isEmpty())

        stack.push(1)

        self.assertFalse(stack.isEmpty())

    def test_pop_data_from_stack(self):
        """
        Test to pop data from Stack
        """
        stack = Stack()

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)
        self.assertTrue(stack.isEmpty())

    def test_convert_stack_to_array(self):
        """
        Test to convert Stack to Array
        """
        stack = Stack()

        self.assertIsNone(stack.peek())

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.toArray(), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
