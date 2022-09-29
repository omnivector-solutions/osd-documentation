.. _mpi:

===
MPI
===


The ``slurmd`` charm support installing MPI (mpich implementation) using a Juju action.
This action will install mpich using the system package manager.

To do that we just need to run the ``mpi-install`` action in the target ``slurmd`` unit:

.. code-block:: bash

      $ juju run-action slurmd/leader mpi-install

This might take a few minutes to complete. After that, we can check the installation using:

.. code-block:: bash

      $ juju run --unit slurmd/leader "mpirun --version"

.. note::

   In CentOS 7, the mpich is installed and configured as a module of the ``environment modules``.
   Thus, It must be loaded in the system using ``module load mpi/mpich-3.2-x86_64``. This is done
   automatically when the users log in to the operating system, because the action configures the 
   ``/etc/bashrc`` file. However, to check the installation with ``juju run --unit`` as described 
   above, we need to do the following:
   
   .. code-block:: bash

      $ juju run --unit slurmd/leader "PATH=/usr/lib64/mpich-3.2/bin:$PATH && --version"
