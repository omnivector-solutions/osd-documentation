.. _operations:

==========
Operations
==========

The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

The operational magic in OSD is encapsulated in ops code called **charms**. We have curated a suite
of automation for each Slurm component: ``slurmctld``, ``slurmd``, ``slurmdbd``, and ``slurmrestd``.

The ``slurm.conf`` file can be customized through the slurm charm configuration options.
Each slurm component charm provides a set of options that enable operators/administrators to operate the cluster.

Alongside the capability to manage the ``slurm.conf``, the charms also provide a set of operational
tools called *actions*.

Find below a list of operations on how to manage and configure OSD:

.. toctree::
   :maxdepth: 2

   nodes
   infiniband
   nhc
   backup-restore
   upgrading-osd
