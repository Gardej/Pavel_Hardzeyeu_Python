from unittest import TestCase
import task3


class TestPrime(TestCase):

    def test_self_dividing(self):
        self.assertFalse(task3.self_dividing(14))
        self.assertTrue(task3.self_dividing(15))

    def test_self_dividing_numbers(self):
        self.assertEqual(task3.self_dividing_numbers(20, 30), [22, 24])
