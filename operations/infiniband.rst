.. _infiniband:

==========
Infiniband
==========


The ``slurmd`` charm contains support for Infiniband driver lifecycle
operations.

Using the ``slurmd`` charm actions we can configure a repository and install
Infiniband drivers from it.

The general workflow for installing Infiniband drivers from a custom repository
includes setting up the driver repository, installing the drivers, and
rebooting the node (in that order).

By default, OSD uses the Mellanox repository for OFED 5.4. If you want a
different version, or a different repository, you can create a text file
describing the repository and configure the charms to use it. If a custom
repository is not set, the charms will use the Mellanox repository. For
example, to use Mellanox OFED 4.9, you can download the appropriate repository
file to your operating system:

- `CentOS7 - OFED 4.9 <https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/rhel7.9/mellanox_mlnx_ofed.repo>`_;
- `Ubuntu 20.04 - OFED 4.9 <https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/ubuntu20.04/mellanox_mlnx_ofed.list>`_.

.. note:: The value passed to the charm action should be base64 encoded.

   It is possible to query the currently used repository, as a way to check the
   configuration:

   .. code-block:: bash

      $ juju run-action slurmd/leader get-infiniband-repo --wait

For example, to download the repository file for OFED 4.9 in CentOS7 and
install the drivers in a loop to cover all 150 compute nodes:

.. code-block:: bash

   curl -O repository \
        https://linux.mellanox.com/public/repo/mlnx_ofed/4.9-2.2.4.0/rhel7.9/mellanox_mlnx_ofed.repo

   repo=$(cat repository | base64)
   for i in {{0..150}}; do
   	juju run-action compute/$i set-infiniband-repo repo="$repo" --wait
   	juju run-action compute/$i install-infiniband
   done

The charm will install a package named ``mlnx-ofed-all``. Note that this
procedure takes some time. After the drivers are installed, you need to reboot
the nodes. An example to reboot all those 150 nodes:

.. code-block:: bash

   for i in {{0..150}}; do
   	juju ssh compute/$i sudo reboot
   done

After the node reboots, the Infiniband service should be enabled and active. To
query its state, use the ``is-active-infiband`` action for the compute node:

.. code-block:: bash

   $ juju run-action compute/42 is-active-infiniband --wait
   unit-compute-42:
     UnitId: compute/42
     id: "899"
     results:
       infiniband-is-active: "True"
     status: completed
     timing:
       completed: 2021-12-17 16:32:40 +0000 UTC
       enqueued: 2021-12-17 16:32:38 +0000 UTC
       started: 2021-12-17 16:32:39 +0000 UTC

It is also possible to run the ``ibstat`` utility over a ``juju ssh`` command
to query the Infiniband capabilities and double check the link is up:

.. code-block:: bash

   $ juju ssh compute/42 /usr/sbin/ibstat
   CA 'mlx5_0'
   	CA type: MT4115
   	Number of ports: 1
   	Firmware version: 12.25.1020
   	Hardware version: 0
   	Node GUID: 0x506b4b0fabede600
   	System image GUID: 0x
   	Port 1:
   		State: Active
   		Physical state: LinkUp
   		Rate: 100
   		Base lid: 43
   		LMC: 0
   		SM lid: 3
   		Capability mask: 0x2651e000
   		Port GUID: 0x506b4b0fabede600
   		Link layer: InfiniBand
   Connection to 10.14.192.42 closed.
