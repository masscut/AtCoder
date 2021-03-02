#
# abc124 a
#
import sys
from io import StringIO
import unittest


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
        input = """5 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6"""
        output = """12"""
        self.assertIO(input, output)


def resolve():
    A, B = map(int, input().split())

    print(max(A, B)+max(max(A, B)-1, min(A, B)))


if __name__ == "__main__":
    # unittest.main()
    resolve()
