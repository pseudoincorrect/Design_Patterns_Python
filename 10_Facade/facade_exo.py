import os
import unittest
from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self):
        self.gen = Generator() 
        self.spl = Splitter()
        self.ver = Verifier()

    def generate(self, size):
        square = self.generate_rand(size)
        while(not self.ver.verify(self.spl.split(square))):
            square = self.generate_rand(size)
        return square

    def generate_rand(self, size):
        square = []
        for _ in range(size):
            row = self.gen.generate(size)
            square.append(row)
        return square

class Evaluate(unittest.TestCase):
    def test_MagicSquareGenerator(self):
        magic = MagicSquareGenerator()
        sq = magic.generate(3)
        self.assertTrue(magic.ver.verify(sq))
        print(sq)


if __name__ == "__main__":
    os.system('clear')
    unittest.main()
