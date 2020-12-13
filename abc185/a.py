#
# abc185 a
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
        input = """5 3 7 11"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 100 1 100"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    A = list(map(int, input().split()))
    print(min(A))


if __name__ == "__main__":
    # unittest.main()
    resolve()