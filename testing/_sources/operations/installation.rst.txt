.. _installation-operation:

==================
Slurm Installation
==================

Omnivector Solutions provides a repository for Slurm packages, for both CentOS
7 and Ubuntu 20.04. This is used to ensure the charms install a supported and
stable Slurm version. The currently supported Slurm version is ``20.11.8`` on
CentOS 7 and ``20.11.7`` on Ubuntu Focal.

Omnivector Slurm Distribution allows one to use a custom repository URL to
install Slurm from. This is specially useful to allow using a local
mirror/cache of packages to speedup installation. This also allows one to
specify different repositories for testing new Slurm versions, or upgrading
only specific charms.

All of the Slurm charms have a configuration option ``custom-slurm-repo``
to specify a different repository URL.

.. note::

   The configuration ``custom-slurm-repo`` must be set *before* deploying the
   units. Changing this value after deploying the units will not have any
   effects on the Slurm version.


Changing the repository
=======================

To use a custom package repository, set the value of ``custom-slurm-repo`` in
your *bundle* file for all ``slurm-charms``, *before* deploying the system. For
Ubuntu units, the URL must be a valid PPA URL. For CentOS 7 units, the URL can
contain a ``$basearch`` variable. For example:

::

   applications:
     slurmd-centos:
       charm: slurmd
       num_units: 1
       series: centos7
       custom-slurm-repo: https://omnivector-solutions.github.io/repo/centos7/stable/$basearch
     slurmd-ubuntu:
       charm: slurmd
       num_units: 1
       series: focal
       custom-slurm-repo: ppa:omnivector/osd
     ...

Another possibility is to supply the repository URL in the command line when
deploying the units:

.. code-block:: bash

   $ juju deploy slurmd --series centos7 --config custom-slurm-repo='https://omnivector-solutions.github.io/repo/centos7/stable/$basearch'

.. note::

   It is the responsibility of the system administrator to ensure that all
   Slurm components are running a compatible Slurm version, when using a custom
   repository. Omnivector Solutions' repository hosts packages that guarantee
   the compatibility of all components.
