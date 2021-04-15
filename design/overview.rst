.. _design:

**********
Automation and Service Discovery
**********

OSD focuses on loosely coupling automation and service discovery with the running/operating of
slurm itself. The reason we choose to "loosely" couple our automation with slurm operations is
due to the fact that more often then not the operator or administrator of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. With
this said, a great deal of automation does exist in OSD, purposefully built to *aid* administrators
in the operation of slurm.


Slurm Lifecycle Automation
######

 * Adding and removing nodes from a cluster partition

 * Installation of slurm

 * Node and partition configuration

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

