.. _architecture:

================
OSD Architecture
================

The Omnivector Slurm Distribution is built on a suite of automations called
"charms". Charms are the operational components that describe the lifecycle of
a Slurm cluster. A full Slurm deployment comes in the form of multiple charms,
one for each component of Slurm. A "bundle" is a YAML file where multiple
charms can be defined. We use bundles to describe the interconnectivity and
configuration of groups of charms.

OSD provisions Slurm to operate in `configless mode
<https://slurm.schedmd.com/configless_slurm.html>`_. In this mode, the
``slurmctld`` process does the work of distributing the ``slurm.conf`` file to
the nodes running ``slurmd``.

Slurm Charms
------------
The `slurm-charms <https://github.com/omnivector-solutions/slurm-charms/>`_
are the components that encapsulate the operational know-how and automation
needed to facilitate the lifecycle of a Slurm cluster.

Slurm Bundles
-------------
The `slurm-bundles <https://github.com/omnivector-solutions/slurm-bundles/>`_
define the base Slurm deployment configurations for different clouds and
operating systems.

OSD Components
--------------

The Omnivector Slurm Distribution supports the following charm components
as part of the Slurm-core offering:

* |slurmd-badge|: Compute and login nodes (running ``slurmd``)
* |slurmdbd-badge|: Slurm database node (running ``slurmdbd``)
* |slurmctld-badge|: Slurm control node (running ``slurmctld``)
* |slurmrestd-badge|: Slurm REST service (running ``slurmrestd``)

Additionally we include the `Node Health Check (NHC)
<https://github.com/mej/nhc>`_ with a minimal configuration and checks to
ensure the ``slurm`` and ``munge`` processes are active. It is possible, and
recommended, that the cluster administrator extends these checks. Check
:ref:`nhc` section for details on how to configure it.

The easiest way to install Infiniband drivers on the compute nodes is to use
the charm supplied actions related to Infiniband management. Check
:ref:`infiniband` section for more details on Infiniband driver lifecycle
operations.

.. |slurmd-badge| image:: https://charmhub.io/slurmd/badge.svg
   :target: https://charmhub.io/slurmd

.. |slurmdbd-badge| image:: https://charmhub.io/slurmdbd/badge.svg
   :target: https://charmhub.io/slurmdbd

.. |slurmctld-badge| image:: https://charmhub.io/slurmctld/badge.svg
   :target: https://charmhub.io/slurmctld

.. |slurmrestd-badge| image:: https://charmhub.io/slurmrestd/badge.svg
   :target: https://charmhub.io/slurmrestd
