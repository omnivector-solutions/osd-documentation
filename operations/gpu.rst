.. _gpu:

===========
GPU Support
===========

OSD supports the installation of GPU drivers for the compute nodes via a set of
Juju Actions.

We currently only support Nvidia GPUs.

Nvidia
======

The ``slurmd`` charm provides an ``install-nvidia`` action to install the
Nvidia drivers easily:

.. code-block:: bash

   $ juju run-action slurmd/leader install-nvidia

This action, by default, pulls the latest drivers from official Nvidia
repositories. If you need to install older drivers, you should specify them
with the action ``nvidia-package`` *before* installing the drivers. For
example, to install the version ``470`` for the Kepler GPUs:

.. code-block:: bash

   $ juju run-action slurmd/leader nvidia-package package="nvidia-driver-branch-470" # for CentOS7
   $ juju run-action slurmd/leader nvidia-package package="cuda-drivers-470" # for Ubuntu 20.04
   $ juju run-action slurmd/leader install-nvidia

Please check the official `Nvidia documentation about compatibility
<https://docs.nvidia.com/deploy/cuda-compatibility/#faq>`_ before installing
the drivers.

.. note::

   By default, OSD will install the latest drivers from Nvidia. This might not
   be the drivers your graphics card need. Please double check the versions
   before installing the drivers. Nvidia website has a `compatibility page
   <https://docs.nvidia.com/deploy/cuda-compatibility/#faq>`_ to guide you on
   installing the correct version.

After installing GPU Drivers, your need to reboot the node. Check
:ref:`rebooting-nodes` section for details on rebooting them.
