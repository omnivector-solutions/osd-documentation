.. _architecture:

================
OSD Architecture
================
The Omnivector Slurm Distribution is built on a suite of automations called "charms".
Charms are the operational components that describe the lifecycle of a SLURM cluster.
A full deployment comes in the form of multiple charms, one for each component of
SLURM. A "bundle" is a yaml file where multiple charms can be defined. We use bundles
to describe the interconnectivity and configuration of groups of charms. 

Slurm Charms
------------
The `slurm-charms <https://github.com/omnivector-solutions/slurm-charms/>`_
are the components that encapsulate the operational know-how and automation
needed to facilitate the lifecycle of a SLURM cluster.

Slurm Bundles
-------------
The `slurm-bundles <https://github.com/omnivector-solutions/slurm-bundles/>`_
define the base slurm deployment configurations for different clouds and
operating systems.

OSD Components
--------------

The Omnivector Slurm Distribution supports the following charm components
as part of the slurm-core offering:

* Compute nodes (running ``slurmd``)

* Slurm database node (running ``slurmdbd``)

* Slurm control node (running ``slurmctld``)

* Slurm configurator node - an Omnivector system to configure and control the
  entire cluster

* Slurm REST service (running ``slurmrestd``) - currently only available for
  Ubuntu Focal

Additionally we include the `Node Health Check (NHC) <https://github.com/mej/nhc>`_
with a minimal configuration and checks to ensure the slurm and munge processes are active.
It is possible, and recommended, that the cluster administrator extends these checks. Check
:ref:`nhc` section for details on how to configure it.

The easiest way to install Infiniband drivers on the compute nodes is to use
the charm supplied actions related to Infiniband management. Check
:ref:`infiniband` section for more details on Infiniband driver lifecycle
operations.
