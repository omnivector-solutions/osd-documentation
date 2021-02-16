.. _operations:

=============
Operations
=============

The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

The operational magic in OSD is encapsulated in ops code called **charms**. We have curated a suite 
of automation for each component of slurm; slurmctld, slurmd, slurmdbd, slurmrestd. As well as our
custom configuration engine charm called "slurm-configurator".

The ``slurm.conf`` file can be customized through the slurm charm configuration options.
Each slurm component charm provides a set of options that enable operators/administrators to operate the cluster.

Alongside the capability to manage the ``slurm.conf``, the charms also provide a set of operational
tools called *actions*.

Find the charm action information and configuration information for each charm:

**Configuration and Administration**

.. toctree::
   :maxdepth: 2

   configuration/configuration

**Upgrade Procedure**

.. toctree::
   :maxdepth: 2

   upgrading-osd

**Backup/Restore Procedure**

.. toctree::
   :maxdepth: 2

   backup-restore
