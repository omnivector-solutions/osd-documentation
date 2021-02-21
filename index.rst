.. OSD Documentation documentation master file, created by
   sphinx-quickstart on Thu Feb  4 07:44:03 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation for the Omnivector Slurm Distribution!
===================================================================

The Omnivector Slurm Distribution (OSD) provides a no-nonsense way to operate and maintain
a slurm cluster. Deploy one of our slurm bundles to a cloud of your choosing and begin
processing your workload in a matter of minutes.

Slurm Automation
****************

OSD focuses on loosly coupling automation and service discovery with the running/operating of
slurm itself. The reason we choose to "loosly" couple our automation with slurm operations is
due to the fact that more often then not the operator or administrator of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. With
this said, a great deal of automation does exist in OSD, purposefully built to aid administrators
in the operation of slurm, not automate the operation of slurm itself.

Slurm lifecycle tasks that have been automated in OSD include:
 * Adding and removing nodes from a cluster partition.
   * Powering physical or virtual machine resources on or off
     * OSD will communicate with a cloud backend to facilitate providing the requested machine resource
   * Instalation of the operating system
     * OSD was built with public, private and on-prem clouds in mind, interfacing to your cloud backend to provision
       machine images with the backing store and image type used by the cloud.
   * Network setup and configuration
     * OSD allows users to define custom network configurations that enable operators to select where infrastructure lives
   * Disk partitioning and other storage configuration
     * Add storage pools to automatically provision disks to a filesyste and partition scheme of your choosing.
   * Installation of slurm
     * Containerized slurm process.
       * We package and distribute slurm as a snapped process.
         * This enables us to provide lightweight, idempotent, hardened slurm builds that work across operating systems.
           * This means you can run the exact same slurm bits on centos, ubuntu, rhel, or whatever operating system you choose.
   * Generating node and partition configuration
     * When a machine resource is added to a partition the ``slurm.conf`` Node and partition configuration are automatically generated for the machine and partition.
 * Composition and distribution of ``slurm.conf``
   * Discover and aggregate node level inventory information
     * node name
     * node addr
     * node state
     * real memory
     * num cpus
     * threads per core
     * cores per socket
     * sockets per board
   * Partition configuration
     * node inventory
     * partition name
     * partition state
     * partition config
   * User defined configuration
     * Seed your own configuration into the ``slurm.conf``
     * Regeneration and redistribution of configuration based on diff from previous config

.. toctree::
   :maxdepth: 3

   Slurm Installation Overview <slurm-installation/overview>
   Operations Overview <operations/overview>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
