.. _configuration:

=============
Configuration
=============

The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

The `slurm.conf` file can be customized through the slurm charm configuration options.
Each slurm component charm provides a set of options that enable operators to configure the
cluster.


.. toctree::
   :maxdepth: 2

   slurm-configurator
   slurmctld
   slurmd
   slurmdbd
   slurmrestd
