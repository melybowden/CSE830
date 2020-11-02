import unittest

class TestSortingMethods(unittest.TestCase):

    def test_merge_sort(self):
        self.assertEqual(merge_sort(arr), sorted(arr))

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_tim_sort(self):
        self.assertEqual(tim_sort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()
