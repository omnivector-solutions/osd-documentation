.. _operations:

==========
Operations
==========

The Omnivector Slurm Distribution can be configured to the extent that you can configure Slurm itself.
Meaning that all upstream Slurm configurations are supported by OSD.

The operational magic in OSD is encapsulated in ops code called **charms**. We have curated a suite
of automation for each Slurm component: ``slurmctld``, ``slurmd``, ``slurmdbd``, and ``slurmrestd``.

Each Slurm component charm provides a set of options that enable operators/administrators to operate the cluster.

The ``slurm.conf`` file can be customized through the ``slurmctld`` charm
configuration options. There is no need to manually update this file in all
compute nodes: OSD combines the power of Juju operations with Slurm in
configless mode (see :ref:`architecture` for details) to configure all the
nodes in the cluster with one single command. This also means that any
modification to a node's ``slurm.conf`` file will be discarded.

Alongside the capability to manage the ``slurm.conf``, the charms also provide a set of operational
tools called *actions*.

Find below a list of operations on how to manage and configure OSD. Refer to
:ref:`configuration-and-administration` for a complete list of all
configuration options and actions.

.. toctree::
   :maxdepth: 2

   installation
   nodes
   partitions
   munge
   infiniband
   gpu
   nhc
   backup-restore
   upgrading-osd
   accounting-profiling
   monitoring
   logging
