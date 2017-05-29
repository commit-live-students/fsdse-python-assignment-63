from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        result = solution()

        self.assertNotEqual(None, result)

        self.assertTrue(2, result[0][0])
        self.assertTrue(3, result[0][1])
        self.assertTrue(4, result[0][2])
        self.assertTrue(5, result[1][0])
        self.assertTrue(6, result[1][1])
        self.assertTrue(7, result[1][2])
        self.assertTrue(8, result[2][0])
        self.assertTrue(9, result[2][1])
        self.assertTrue(10, result[2][2])