#
# abc185 c
#
import sys
from io import StringIO
import unittest
import math


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """17"""
        output = """4368"""
        self.assertIO(input, output)


def resolve():
    L = int(input())

    print(math.factorial(L-1) // (math.factorial(L-12) * math.factorial(11)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
