.. _installation-operation:

============
Installation
============

Omnivector Solutions provides a repository for Slurm packages, for both CentOS7
and Ubuntu 20.04. This is used to ensure the charms install a supported Slurm
version. The currently supported Slurm version is ``20.11.8`` on CentOS 7 and
``20.11.7`` on Ubuntu Focal.

Omnivector Slurm Distribution allows one to use a custom repository URL to
install Slurm from. This is specially useful to allow using a local
mirror/cache of packages to speedup installation.

All of the Slurm charms have a configuration value ``custom-slurm-repo``
to specify a different repository URL.

To use a custom package repository, set the value of ``custom-slurm-repo`` in
your *bundle* file for each charm, *before* deploying the system. For Ubuntu
units, the URL must be a valid PPA URL. For CentOS 7 units, the URL can contain
a ``$basearch`` variable. For example:

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
       custom-slurm-repo: ppa:omnivector/osd-testing
     ...


This also allows one to specify different repositories for testing new Slurm
versions, or upgrading only specific charms.

.. note::

   The configuration ``custom-slurm-repo`` must be set *before* deploying the
   units. Changing this value after deploying the units will not reinstall
   Slurm.
