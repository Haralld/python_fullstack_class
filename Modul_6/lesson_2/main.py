import unittest

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]


def get_unique_numbers(numbers):
    seen = set()
    unique_numbers = []
    for number in numbers:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)
    return unique_numbers

unique_numbers = get_unique_numbers(numbers)
print(unique_numbers)


class TestGetUniqueNumbers(unittest.TestCase):

    def test_with_duplicates(self):
        self.assertEqual(get_unique_numbers([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_same(self):
        self.assertEqual(get_unique_numbers([1, 1, 1, 1, 1]), [1])

    def test_empty_list(self):
        self.assertEqual(get_unique_numbers([]), [])

    def test_no_duplicates(self):
        self.assertEqual(get_unique_numbers([10, 20, 30, 40]), [10, 20, 30, 40])

    def test_with_negative_numbers(self):
        self.assertEqual(get_unique_numbers([0, -1, -1, 0, 1]), [0, -1, 1])

if __name__ == '__main__':
    unittest.main()