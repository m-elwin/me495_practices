#!/usr/bin/env python
""" Unit testing add_two """
import me495_practices.hardmath as hardmath

class HardCase(unittest.TestCase):
    def test_one_one(self):
       self.assertEquals(hardmath.add_two(1,1), 2)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(me495_practices, "hard_case", HardCase)
