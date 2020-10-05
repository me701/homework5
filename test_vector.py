from vector import Vector
import unittest

class TestVector(unittest.TestCase):

    def test_add(self):
        """ Ensures a pair is found.
        """

        V = Vector(5, 1)
        Y = Vector(5, 1)
        Z = V + Y
        self.assertEqual(Z.norm, 4.472135955)

    def test_cant_add(self):


        V = Vector(5, 1)
        Y = Vector(6, 1) # too big
        self.assertRaises(AssertionError, V + Y)

    def test_dot(self):
        V = Vector(5, 1)
        Y = Vector(5, 1)
        d = V.dot(Y)
        self.assertAlmostEqual(d, 20, 12)

if __name__ == '__main__':

    unittest.main()
