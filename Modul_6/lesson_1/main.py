import unittest


def sum_numers(x, y):
    return x + y

class TestSumNumbers(unittest.TestCase):
    def test_sum_tow_numbers(self):
        result = sum_numers(2, 3)
        self.assertEqual(result, 5)
        

def diff_numers(x, y):
    return x - y

class TestDifferenceNumbers(unittest.TestCase):
    def test_difference_tow_numbers(self):
        result = diff_numers(9, 6)
        self.assertEqual(result, 3)


def abs_num(x):
    return abs(x)

class TestAbsoluteNumber(unittest.TestCase):
    def test_absolute_number(self):
        result = abs_num(10)
        self.assertEqual(result, 10)


def сomp_numbers(x, y):
    return x * y

class TestCompNumbers(unittest.TestCase):
    def test_comp_numbers(self):
        result = сomp_numbers(15, 2)
        self.assertEqual(result, 30)


def square_num(x):
    return x ** 0.5

class TestSquareNumber(unittest.TestCase):
    def test_square_number(self):
        result = square_num(9)
        self.assertEqual(result, 3)

def div_numbers(x, y):
    if y == 0:
        raise ValueError("Division by zero")
    return x / y

class TestDivNumber(unittest.TestCase):
    def test_div_number(self):
        with self.assertRaises(ValueError):
            div_numbers(10, 0)
            
    def test_div_number_success(self):
        result = div_numbers(10, 2)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()