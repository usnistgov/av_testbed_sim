

.. _installation:


Installation
=============

Carla
------

Follow the instructions on the `Carla website <https://carla.readthedocs.io/en/latest/start_quickstart/>`_.

- Official `Carla documentation <https://carla.readthedocs.io/en/latest/>`_

Mayavi
------

Mayavi is a 3D visualization tool for Python. It is used to visualize the simulation environment. 

Ubuntu
^^^^^^

- Follow the instructions on the `Mayavi website <https://docs.enthought.com/mayavi/mayavi/installation.html#installing-ready-made-distributions>`_.
- Update to the latest version:

   .. code-block:: bash
      
      pip install mayavi -U

Running the simulation
======================

- Start the Carla server:

   .. code-block:: bash
      
      ./CarlaUE4.sh

- Start the simulation:
   
      .. code-block:: bash
         
         python3 carla_visualization.py
         # or ./carla_visualization.py
