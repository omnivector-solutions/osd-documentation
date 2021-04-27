.. architecture:

================
OSD Architecture
================

The Omnivector Slurm Distribution has the following components:

* Compute nodes (running ``slurmd``)

* Slurm database node (running ``slurmdbd``)

* Slurm control node (running ``slurmctld``)

* Slurm configurator node - an Omnivector system to configure and control the
  entire cluster

* Slurm REST service (running ``slurmrestd``) - currently only available for
  Ubuntu Focal

On the compute nodes, we also install
`Node Health Check (NHC) <https://github.com/mej/nhc>`_ with a only a few basic
checks that ensure the slurm and munge processes are active. It is possible,
and recommended, that the cluster administrator extends these checks. Check
:ref:`nhc` section for details on how to configure it.

The easiest way to install Infiniband drivers on the compute nodes is to use
the charm supplied actions related to Infiniband management. Check
:ref:`infiniband` section for more details on Infiniband driver lifecycle
operations.
