import os
import unittest
from abc import ABC
from collections.abc import Iterable

class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        s = 0
        for i in self:
            print(i)
            for j in i:
                print(j)
                s += j
        return s


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

class ManyValues(list, ValueContainer):
    pass

class Evaluate(unittest.TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

if __name__ == "__main__":
    os.system('clear') 
    unittest.main()
