import unittest
import foo

class SimpleTest(unittest.TestCase):
    """测试做除法的函数"""
    def test1(self):
        self.assertEqual(foo.divide(16, 2), 8)

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 0)

if __name__ == "__main__":
    unittest.main()