.. _operations:

=============
Operations
=============

The operational magic in OSD is encapsulated in ops code called **charms**. We have curated a suite 
of automation for each component of slurm; slurmctld, slurmd, slurmdbd, slurmrestd, and additionally our
custom configuration engine charm called "slurm-configurator".

Configuration
*************
The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

Each slurm component charm provides a set of options that enable operators to customize the cluster.

slurm.conf
-----------
User supplied ``slurm.conf`` values can be added to OSD configuration via the slurm-configurator charm configuration option, ``custom-config``.

Alongside the capability to manage the ``slurm.conf``, the slurm operator charms also provide a set of tools called *actions* that enable administrators
to perform cluster wide operations and configurations from a simplified, unified interface.


.. toctree::
   :maxdepth: 1

   configuration/slurmd
   configuration/slurmdbd
   configuration/slurmctld
   configuration/slurmrestd
   configuration/slurm-configurator


Upgrade
*******

.. toctree::
   :maxdepth: 2

   upgrading-osd



Backup/Restore
**************

.. toctree::
   :maxdepth: 2

   backup-restore
