.. _operations:

=============
Operations
=============

**Slurm Charm Operations**
The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

The ``slurm.conf`` file can be customized through the slurm charm configuration options.
Each slurm component charm provides a set of options that enable operators to configure the
cluster.

Alongside the capability to manage the ``slurm.conf``, the charms also provide a set of operational
tools called *actions*.

Find the charm action information and configuration information for each charm:

**Configuration and Actions**

.. toctree::
   :maxdepth: 2

   slurm-configurator
   slurmctld
   slurmd
   slurmdbd
   slurmrestd


**Upgrade Procedure**

.. toctree::
   :maxdepth: 2

   upgrading-osd

**Backup Procedure**

.. toctree::
   :maxdepth: 2

   backups
