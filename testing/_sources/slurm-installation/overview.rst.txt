.. _installation:

=====================
Installation overview
=====================

The OSD can be installed on a cloud of your choosing. The only common component used across deployments is juju itself.
You must have the juju client installed on your local system in order to administer the installation and deployment of the slurm charms.

**Install Juju**

.. code-block:: bash

   sudo snap install juju --classic


Once the juju client is installed you will be ready to proceed with deploying slurm to a cloud of your choosing.


Follow the documentation for the cloud you with to deploy slurm on:

.. toctree::
   :maxdepth: 2

   lxd
   aws
   maas
   gcp
   azure

