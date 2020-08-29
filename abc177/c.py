#
# abc177 c
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
        input = """3
1 2 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
141421356 17320508 22360679 244949"""
        output = """437235829"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    S = sum(A)
    ans = 0
    for a in A:
        S -= a
        ans += a * S

    print(ans % (10**9+7))


if __name__ == "__main__":
    # unittest.main()
    resolve()
