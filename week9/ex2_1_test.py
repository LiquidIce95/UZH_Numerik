import unittest
from week9.ex2_1 import *

class TestGramSchmidt(unittest.TestCase):
    def test_compute_projection_basic(self):
        u = np.array([1, 0])
        v = np.array([5, 0])
        expected = np.array([5, 0])
        result = computeProjection(u, v)
        np.testing.assert_array_almost_equal(result, expected)

    def test_gram_schmidt_orthogonalizing_independent_vectors(self):
        A = np.array([[1, 1], [0, 1]], dtype=float)
        Q = GramSchmidtOrthogonalizing(A.copy())
        dot_product = np.dot(Q[:, 0], Q[:, 1])
        self.assertAlmostEqual(dot_product, 0)

    def test_gram_schmidt_orthogonalizing_dependent_vectors(self):
        A = np.array([[1, 2], [2, 4]], dtype=float)
        Q = GramSchmidtOrthogonalizing(A.copy())
        dot_product = np.dot(Q[:, 0], Q[:, 1])
        self.assertAlmostEqual(dot_product, 0)  # Check if second vector is zero vector

    def test_compute_qr_matrices(self):
        A = np.array([[1, 1], [0, 1]], dtype=float)
        Q, R = computeQRmatrices(A.copy())
        np.testing.assert_array_almost_equal(np.dot(Q, R), A)

    def test_compute_projection_perpendicular_vectors(self):
        u = np.array([1, 0])
        v = np.array([0, 5])
        expected = np.array([0, 0])
        result = computeProjection(u, v)
        np.testing.assert_array_almost_equal(result, expected)

    def test_compute_qr_matrices_with_singular_matrix(self):
        A = np.array([[1, 1], [1, 1]], dtype=float)
        Q, R = computeQRmatrices(A.copy())
        np.testing.assert_array_almost_equal(np.dot(Q, R), A)

if __name__ == '__main__':
    unittest.main()
