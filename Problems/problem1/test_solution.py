from unittest import TestCase
from solution import solution


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 233168)