.. _design:

*****************************************************
Packaging, Delivery, Automation and Service Discovery
*****************************************************

OSD focuses on loosly coupling automation and service discovery with the running/operating of
slurm itself. The reason behind "loosly" coupling the automation with slurm operations is
because more often then not the operators and administrators of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. With
this said, a great deal of automation does exist in OSD, purposefully built to *aid* administrators
in the operation of slurm.

We have taken a similar approach in the delivery of the slurm process. OSD provides the bindings
that enable operators to lean on our upstream builds, or bring their own build of slurm. Whichever it is,
OSD will automate the process of distributing, installing (or upgrading) and configuring slurm. This method of
delivery enables OSD to support offline upgrades and installations in a streamline manner.


Packaging and Delivery
######################

One of the core efficiencies in OSD is the packaging and distribution of slurm as a snapped_ process.
Distributing slurm as a snap enables us to provide lightweight, idempotent and hardened slurm builds that work across operating systems.

OSD provisions slurm by means of installing the slurm snap on each slurm component node in the cluster (default).
This behavior can be changed to allow users to bring their own slurm builds by means of providing a user supplied resource_.

.. _resource: https://discourse.charmhub.io/t/using-resources-developer-guide/1127

.. _snapped: https://snapcraft.io/about


Supported user provided slurm resources are:

 * slurm snap

 * slurm tarball



Slurm Lifecycle Automation
##########################

A short list of lifecycle operations have been thoughtfully currated are as follows.

* Adding and removing nodes from a cluster partition
 
 * Powering physical or virtual machine resources on or off

 * Operating system installation

 * Network setup and configuration

 * Disk partitioning and other storage configuration

 * Installation of slurm

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


