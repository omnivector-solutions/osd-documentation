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


OSD focuses on `loosly` coupling automation and service discovery with the operating of
Slurm itself. The reason behind `loosely` coupling the automation with Slurm operations is
because more often then not the operators and administrators of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. If the
ops code was `tightly` coupled with the application workload (in this context, slurm) it would prevent
an operator from being able to perform manual operations commonly needed in and out of cluster lifecycle.


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
     * Regeneration and redistribution of configuration based on diff from previous config


Find more on slurm lifecycle operations in the OSD operations documentation:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
