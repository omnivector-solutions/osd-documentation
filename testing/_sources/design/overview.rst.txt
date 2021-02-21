.. _design:

**********
Automation and Service Discovery
**********

OSD focuses on loosly coupling automation and service discovery with the running/operating of
slurm itself. The reason we choose to "loosly" couple our automation with slurm operations is
due to the fact that more often then not the operator or administrator of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. With
this said, a great deal of automation does exist in OSD, purposefully built to *aid* administrators
in the operation of slurm.


Slurm Lifecycle Automation
######

* Adding and removing nodes from a cluster partition
 
 * Powering physical or virtual machine resources on or off

 * Operating system installation

 * Network setup and configuration

 * Disk partitioning and other storage configuration

 * Installation of slurm
 
* Containerized slurm process

 * We package and distribute slurm as a snapped process. This enables us to provide lightweight, idempotent and hardened slurm builds that work across operating systems

* Generating node and partition configuration

 * When a machine resource is added to a partition the ``slurm.conf`` Node and partition configuration are automatically generated for the machine and partition

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

