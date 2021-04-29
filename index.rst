.. OSD Documentation documentation master file, created by
   sphinx-quickstart on Thu Feb  4 07:44:03 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation for the Omnivector Slurm Distribution!
===================================================================

.. toctree::
   :maxdepth: 3

   Slurm Installation Overview <slurm-installation/overview>
   Operations Overview <operations/overview>


Lifecycle Automation
####################

A short list of thoughtfully curated lifecycle operations automated by OSD.

 * Adding and removing nodes from a cluster partition
 * Installation of slurm
 * Generating node and partition configuration
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
     * Regeneration and redistribution of configuration based on ``diff`` from previous configuration
