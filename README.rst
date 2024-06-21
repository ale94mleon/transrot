transrot
========


Description
-----------

**transrot**  is a lightweight Python package to calculate the translation vector and rotational matrix between two sets of 3D coordinates. This transformation can be applied to another set of coordinates


Installation
------------

.. code-block:: bash

    pip install transrot


How To?
-------

.. code-block:: bash
    
    from transrot import TransRot
    import numpy as np
    
    # Get your (n, 3) array of coordinates
    coords1 = np.random.random((5, 3))
    coords2 = np.random.random((5, 3))
    coords3 = np.random.random((5, 3))
    
    # Initialize the class
    transformation = TransRot(
        coords1=coords1,
        coords2=coords2
    )
    
    # Calculate rotational matrix and translational vector that aligns coords1 to coords2
    transformation.fit()
    
    # Transform a set of coordinates with the calculated transformation
    transformed_coords = transformation.transform(coords3)

Issues
------

If you have found a bug, please open an issue on the `GitHub Issues <https://github.com/ale94mleon/hello/issues>`_.

Funding
---------

This project received funding from `Marie Skłodowska-Curie Actions <https://cordis.europa.eu/project/id/860592>`__. It was developed in the 
`Computational Biophysics Group <https://biophys.uni-saarland.de/>`__ of `Saarland University <https://www.uni-saarland.de/en/home.html>`__.