from transrot import TransRot
import numpy as np


def test_main_class():
    coords1 = np.random.random((5, 3))
    coords2 = np.random.random((5, 3))

    transformation = TransRot(
        coords1=coords1,
        coords2=coords2
    )

    transformation.fit()
    print(transformation.transform(coords1))


if __name__ == "__main__":
    pass