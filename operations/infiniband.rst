.. _infiniband:

==========
Infiniband
==========


The ``slurmd`` charm contains support for Infiniband driver lifecycle
operations.

Using the ``slurmd`` charm actions we can configure a repository and install
Infiniband drivers from it.

The general workflow for installing infiniband drivers from a custom repository
includes setting up the driver repository, installing the drivers, and
rebooting the node (in that order).

By default, OSD uses the Mellanox repository for OFED 5.3. If you want a
different version, or a different repository, you can create a text file
describing the repository and configure the charms to use it. For example, to
use Mellanox OFED 4.9, you can download the appropriate repository file to your
operating system:
- `CentOS7 - OFED 4.9 <https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/rhel7.9/mellanox_mlnx_ofed.repo>`_;
- `Ubuntu 20.04 - OFED 4.9 <https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/ubuntu20.04/mellanox_mlnx_ofed.list>`_.

For example, to download the repository file for OFED 4.9 in CentOS7 and
install the drivers in a loop to cover all 150 compute nodes:

.. code-blocK:: bash

   curl -O repository \
        https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/rhel7.9/mellanox_mlnx_ofed.repo

   for i in {{0..150}}; do
   	juju run-action compute/$i set-infiniband-repo repo="$(cat repository)" --wait
   	juju run-action compute/$i install-infiniband
   done

The charm will install a package named ``mlnx-ofed-all``. Note that this
procedure takes some time. After the drivers are installed, you need to reboot
the nodes.

