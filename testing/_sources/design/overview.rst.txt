.. _design:

******
Design
******

OSD focuses on `loosly` coupling automation and service discovery with the operating of
slurm itself. The reason behind `loosly` coupling the automation with slurm operations is
because more often then not the operators and administrators of slurm will need to
have some level of interaction with the cluster before lifecycle operations take place. If the
ops code was `tightly` coupled with the application workload (in this context, slurm) it would prevent
an operator from being able to perform manual operations commonly needed in and out of cluster lifecycle.

In codifying operations, the right balance of automation and operator interaction is often difficult to find.

With this said, a great deal of automation does exist in OSD, purposefully built to *aid* administrators
in the operation of slurm.

We have taken a similar approach in the delivery of the slurm process in that OSD will facilitate the
provisioining of either a slurm snap or tarball. In this way, OSD provides the bindings that enable operators to
lean on our upstream builds or bring their own build of slurm. Whichever it is, OSD will automate the process
of distributing, installing (or upgrading) and configuring slurm - things that are obviously automatable but not
necessarily opinionated.


Packaging and Delivery
######################

One of the core efficiencies in OSD is the packaging and distribution of slurm as a snapped_ process.
Distributing slurm as a snap enables OSD to provide lightweight, idempotent, hardened slurm builds that work across operating systems.

OSD provisions slurm by means of installing the slurm snap on each slurm component node in the cluster (default).

This behavior can be changed to allow users to bring their own slurm builds by means of providing a user supplied resource_.
A user supplied resource can be in the format of a ``.tar.gz`` or ``.snap`` file. A user can supply a tar or snap resource
and OSD will figure out how to install and configure slurm based on the type of resource that has been provided. For example, if a snap resource
is provided, OSD will know to configure slurm using snap primitives. Similarly, if a tarball resource is provided, OSD will know
the correct place to put things in order to appropriately configure and run the components of slurm at the OS level, using systemd.
OSD determines the type of resource provided and in turn uses the correct installation, configuration and lifecycle operations for that resource; snap or tarball.

.. _resource: https://discourse.charmhub.io/t/using-resources-developer-guide/1127

.. _snapped: https://snapcraft.io/about


Supported user provided slurm resources are:

 * slurm snap

 * slurm tarball



Find the slurm snap homepage on the `<snapstore_>`_.

Contribute to the slurm snap development on `<github_>`_.

.. _snapstore: https://snapcraft.io/slurm
.. _github: https://github.com/omnivector-solutions/snap-slurm



Lifecycle Automation
####################

A short list of thoughtfully curated lifecycle operations automated by OSD.

* Adding and removing nodes from a cluster partition
 
 * Powering physical or virtual machine resources on or off

 * Operating system installation

 * Network setup and configuration

 * Disk partitioning and other storage configuration

 * Installation of slurm

* Generating node and partition configuration

 * When a machine resource is added to a partition the ``slurm.conf`` `Node` and `Partition` configuration are generated for the machine and partition

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


Find more on OSD slurm operations in our ops docs:

.. toctree::
   :maxdepth: 1
   ../operations/overview
