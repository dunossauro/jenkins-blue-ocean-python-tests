from unittest import TestCase
from app.example import add


class Test(TestCase):
    def test_soma(self):
        self.assertEqual(add(1, 1), 2)

    def test_sub(self):
        self.assertEqual(add(1, 1), 0)
