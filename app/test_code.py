import app.code
import unittest

class TestCode(unittest.TestCase):
    def test_fibo_2(self):
        self.assertEqual(app.code.fibo(1), 1)
        self.assertEqual(app.code.fibo(2), 1)

    def test_fibo(self):
        self.assertEqual(app.code.fibo(3), 2)
        self.assertEqual(app.code.fibo(4), 3)
        self.assertEqual(app.code.fibo(5), 5)
        self.assertEqual(app.code.fibo(6), 8)
