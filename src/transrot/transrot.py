import numpy as np


class TransRot:
    """
    Class for computing rotation and translation transformation
    to align one set of 3D coordinates with another.

    Parameters:
    -----------
    coords1 : array-like
        First set of 3D coordinates. Each row represents a point.
    coords2 : array-like
        Second set of 3D coordinates. Each row represents a point.

    Attributes:
    -----------
    coords1 : ndarray
        First set of 3D coordinates.
    coords2 : ndarray
        Second set of 3D coordinates.
    _R : ndarray
        3x3 rotation matrix.
    _t : ndarray
        Translation vector.

    Methods:
    --------
    fit():
        Find the rotation matrix and translation vector that aligns
        the coords1 to coords2.
    transform(coords):
        Apply the transformation to a set of coordinates.

    """

    def __init__(self, coords1, coords2) -> None:
        """
        Initialize TransRot with two sets of 3D coordinates.

        Parameters:
        -----------
        coords1 : array-like
            First set of 3D coordinates. Each row represents a point.
        coords2 : array-like
            Second set of 3D coordinates. Each row represents a point.
        """
        self.coords1 = np.array(coords1)
        self.coords2 = np.array(coords2)

    def fit(self):
        """
        Find the rotation matrix and translation vector that aligns
        the coords1 to coords2.

        Adds Attributes:
        ----------------
        _R : ndarray
            3x3 rotation matrix
        _t : ndarray
            Translation vector
        """
        assert self.coords1.shape == self.coords2.shape

        # Compute centroids of coords1 and coords2
        centroid_1 = np.mean(self.coords1, axis=0)
        centroid_2 = np.mean(self.coords2, axis=0)

        # Center the points
        centered_1 = self.coords1 - centroid_1
        centered_2 = self.coords2 - centroid_2

        # Compute the covariance matrix
        H = centered_1.T @ centered_2

        # Compute SVD of the covariance matrix
        U, S, Vt = np.linalg.svd(H)

        # Compute rotation matrix
        R = Vt.T @ U.T

        # Special reflection case
        if np.linalg.det(R) < 0:
            Vt[2, :] *= -1
            R = Vt.T @ U.T

        # Compute translation vector
        t = centroid_2.T - R @ centroid_1.T

        self._R = R
        self._t = t

    def transform(self, coords):
        """
        Apply the transformation to coords.

        Parameters:
        -----------
        coords : array-like
            Nx3 matrix of points to be transformed.

        Returns:
        --------
        Transformed coords : ndarray
            Transformed coordinates.
        """
        coords = np.array(coords)
        return (self._R @ coords.T).T + self._t
