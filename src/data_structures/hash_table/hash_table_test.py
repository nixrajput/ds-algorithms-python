import os
import sys
import unittest

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
root_folder = os.path.abspath(src_dir)
sys.path.append(root_folder)
from data_structures.hash_table.hash_table import HashTable


class TestCase(unittest.TestCase):
    def test_create_hash_table(self):
        """
        Test to create an empty HashTable
        """
        defaultHashTable = HashTable()

        self.assertEqual(len(defaultHashTable.buckets), 32)

        biggerHashTable = HashTable(64)

        self.assertEqual(len(biggerHashTable.buckets), 64)

    def test_generate_hash(self):
        """
        Test to generate proper hash for specified keys
        """
        hashTable = HashTable()

        self.assertEqual(hashTable.hash("a"), 1)
        self.assertEqual(hashTable.hash("b"), 2)
        self.assertEqual(hashTable.hash("abc"), 6)

    def test_set_read_delete_data_in_hash_table(self):
        """
        Test to set, read and delete data with collisions
        """
        hashTable = HashTable(3)

        self.assertEqual(hashTable.hash("a"), 1)
        self.assertEqual(hashTable.hash("b"), 2)
        self.assertEqual(hashTable.hash("c"), 0)
        self.assertEqual(hashTable.hash("d"), 1)

        hashTable.set("a", "sky-old")
        hashTable.set("a", "sky")
        hashTable.set("b", "sea")
        hashTable.set("c", "earth")
        hashTable.set("d", "ocean")

        self.assertFalse(hashTable.has("x"))
        self.assertTrue(hashTable.has("b"))
        self.assertTrue(hashTable.has("c"))

        def nodeStringifier(value):
            return f"{value['key']}:{value['value']}"

        self.assertEqual(hashTable.buckets[0].toList(nodeStringifier), ["c:earth"])
        self.assertEqual(
            hashTable.buckets[1].toList(nodeStringifier), ["a:sky", "d:ocean"]
        )
        self.assertEqual(hashTable.buckets[2].toList(nodeStringifier), ["b:sea"])

        self.assertEqual(hashTable.get("a"), "sky")
        self.assertEqual(hashTable.get("d"), "ocean")
        self.assertEqual(hashTable.get("x"), None)

        hashTable.delete("a")

        self.assertIsNone(hashTable.delete("xyz"))

        self.assertEqual(hashTable.get("a"), None)
        self.assertEqual(hashTable.get("d"), "ocean")

        hashTable.set("d", "ocean-new")
        self.assertEqual(hashTable.get("d"), "ocean-new")

    def test_add_objects_to_hash_table(self):
        """
        Test to add objects to HashTable
        """
        hashTable = HashTable()

        hashTable.set("objectKey", {"prop1": "a", "prop2": "b"})

        obj = hashTable.get("objectKey")

        self.assertEqual(obj["prop1"], "a")
        self.assertEqual(obj["prop2"], "b")

    def test_track_actual_keys_in_hash_table(self):
        """
        Test to track actual keys in HashTable
        """
        hashTable = HashTable(3)

        hashTable.set("a", "sky-old")
        hashTable.set("a", "sky")
        hashTable.set("b", "sea")
        hashTable.set("c", "earth")
        hashTable.set("d", "ocean")

        self.assertEqual(hashTable.getKeys(), ["a", "b", "c", "d"])
        self.assertTrue(hashTable.has("a"))
        self.assertFalse(hashTable.has("x"))

        hashTable.delete("a")

        self.assertFalse(hashTable.has("a"))
        self.assertTrue(hashTable.has("b"))
        self.assertFalse(hashTable.has("x"))

    def test_get_all_values_from_hash_table(self):
        """
        Test to track values from HashTable
        """
        hashTable = HashTable(3)

        hashTable.set("a", "alpha")
        hashTable.set("b", "beta")
        hashTable.set("c", "gamma")

        self.assertEqual(hashTable.getValues(), ["gamma", "alpha", "beta"])


if __name__ == "__main__":
    unittest.main()
