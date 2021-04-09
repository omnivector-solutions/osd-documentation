.. _installation:

=====================
Installation overview
=====================

The OSD can be installed on a cloud of your choosing. The only common component
used across deployments is juju_ itself.  You must have the juju client
installed on your local system in order to administer the installation and
deployment of the Slurm charms.

.. _juju: https://juju.is


Install Juju
============

.. code-block:: bash

   $ sudo snap install juju --classic


Once the juju client is installed you will be ready to proceed with deploying
Slurm to a cloud of your choosing.


Setup cloud
===========

Follow the documentation for the cloud you with to deploy Slurm on:

AWS
###


Login to a juju controller
--------------------------

In any deployment scenario we will need to be logged into a juju controller.
For this example we will login to the public juju controller, Jaas.

.. code-block:: bash

   $ juju login jaas


Add a model
-----------

Once you are logged into a juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm aws/us-west-2


LXD
###

Bootstrap a localhost LXD Juju controller
-----------------------------------------

In any deployment scenario we will need to be logged into a juju controller.
For this example we will bootstrap a juju controller in a LXD container on our
local machine.

Install and configure LXD, if you haven't already:

.. code-block:: bash

   $ sudo snap install lxd
   $ lxd init --auto
   $ lxd network set lxdbr0 ipv6.address none

.. note::

   Juju does not support IPv6, the last command disables it.

You can now bootstrap your local cloud:

.. code-block:: bash

   $ juju bootstrap localhost

Following a successful bootstrap, ``juju controllers`` will show your newly
provisioned lxd controller.


Add a model
-----------

Once you have created your juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm


MAAS
####


Login to a juju controller
--------------------------

If you don't already have a juju controller, bootstrap juju by creating a juju
controller machine.

.. code-block:: bash

   $ juju bootstrap


Add a model
-----------

Once you are logged into a juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm



Deploy Slurm
============

Now it is time to get Slurm :)

First we need to build a *charm*. That's what Juju will deploy to our cloud.
Charms are built with ``charmcraft``:

.. code-block:: bash

   $ sudo snap install --edge charmcraft

Clone the `slurm-charms <https://github.com/omnivector-solutions/slurm-charms>`_
git repository, it contains all the nuts and bolts to build the charms:

.. code-block:: bash

   $ git clone https://github.com/omnivector-solutions/slurm-charms
   $ cd slurm-charms
   $ make charms

Now it is time to deploy! The bundles and overlays are in a separate repository,
`slurm-bundles <https://github.com/omnivector-solutions/slurm-bundles>`_.
Clone the repository on the same directory you cloned ``slurm-charms/``:

.. code-block:: bash

   $ git clone https://github.com/omnivector-solutions/slurm-bundles
   $ cd slurm-bundles

The ``slurm-core`` directory contains all the bundles and overlays to deploy a
basic Slurm cluster:

- ``slurm-core/bundle.yaml``: the basic definition of the Slurm components.
- ``slurm-core/clouds/``: overlays with specific settings for each supported
  cloud environment.
- ``slurm-core/options/``: overlays with specific ``options`` for the Slurm
  components.
- ``slurm-core/series/``: overlays to define the OS of the Slurm components.

For example, to deploy Slurm to a local LXD cloud, on Ubuntu Focal:

.. code-block:: bash

   $ juju deploy ./slurm-core/bundle.yaml \
                 --overlay ./slurm-core/clouds/lxd.yaml \
                 --overlay ./slurm-core/series/focal.yaml \

Juju will then create the applications, configurations and LXD containers
described in the respective files, which will in turn define the contents of
the model.

It will take a moment get everything ready. You can check the status of your
model with juju's status:

.. code-block:: bash

   $ watch -n 1 -c juju status --color

   Model    Controller  Cloud/Region         Version  SLA          Timestamp
   default  overlord    localhost/localhost  2.8.7    unsupported  17:44:29Z

   App                 Version  Status  Scale  Charm               Store       Rev  OS      Notes
   percona-cluster     5.7.20   active      1  percona-cluster     jujucharms  293  ubuntu
   slurm-configurator  20.11.3  active      1  slurm-configurator  local         1  ubuntu
   slurmctld           20.11.3  active      1  slurmctld           local         0  ubuntu
   slurmd              20.11.3  active      1  slurmd              local         0  ubuntu
   slurmdbd            20.11.3  active      1  slurmdbd            local         0  ubuntu
   slurmrestd          20.11.3  active      1  slurmrestd          local         0  ubuntu

   Unit                   Workload  Agent  Machine  Public address  Ports     Message
   percona-cluster/0*     active    idle   0        10.34.166.18    3306/tcp  Unit is ready
   slurm-configurator/0*  active    idle   1        10.34.166.187             slurm-configurator available
   slurmctld/0*           active    idle   2        10.34.166.222             slurmctld available
   slurmd/0*              active    idle   3        10.34.166.219             slurmd available
   slurmdbd/0*            active    idle   4        10.34.166.218             slurmdbd available
   slurmrestd/0*          active    idle   5        10.34.166.66              slurm installed

   Machine  State    DNS            Inst id        Series  AZ  Message
   0        started  10.34.166.18   juju-01ab62-0  bionic      Running
   1        started  10.34.166.187  juju-01ab62-1  focal       Running
   2        started  10.34.166.222  juju-01ab62-2  focal       Running
   3        started  10.34.166.219  juju-01ab62-3  focal       Running
   4        started  10.34.166.218  juju-01ab62-4  focal       Running
   5        started  10.34.166.66   juju-01ab62-5  focal       Running


Once the workload status is *active* and the agent status is *idle*, the Slurm
cluster is ready for use.

You can see the status of your cluster by running the ``sinfo`` command:

.. code-block:: bash

   $ juju run --unit slurm-configurator/0 sinfo
   PARTITION         AVAIL  TIMELIMIT  NODES  STATE NODELIST
   juju-compute-GsLk    up   infinite      1   down juju-01ab62-3
   configurator*     inact   infinite      1   idle juju-01ab62-1

The nodes start in *down* state with a ``Reason = New node``, so when you add
more nodes to the cluster, they will not execute the jobs from que queue. This
way it is possible to do some post installation before setting the nodes as
*idle*. You can double check that your nodes are down because of this and not
some other reason with ``sinfo -R``:

.. code-block:: bash

   $ juju run --unit slurm-configurator/0 "sinfo -R"
   REASON               USER      TIMESTAMP           NODELIST
   New node             root      2021-03-09T20:24:09 ip-172-31-83-4

After setting the node up, to bring it back you need to run a Juju *action*:

.. code-block:: bash

   $ juju run-action slurmd/1 node-configured
   $ juju run --unit slurm-configurator/0 sinfo
   PARTITION         AVAIL  TIMELIMIT  NODES  STATE NODELIST
   juju-compute-GsLk    up   infinite      1   idle juju-01ab62-3
   configurator*     inact   infinite      1   idle juju-01ab62-1


CentOS7 Deploys on LXD clouds
-----------------------------

You need to manually create an LXD image for CentOS7 in order to deploy it with
Juju.

First step is to download a configuration file describing the image:

.. code-block:: bash

    $ wget https://raw.githubusercontent.com/lxc/lxc-ci/master/images/centos.yaml

Juju needs two extra packages (`sudo` and `openssh-server`) that are not in the
base image. You need to manually add them in the `packages` section of the yaml
file. The first `set` of packages in the file should then be:

.. code-block:: bash

    packages:
      manager: yum
      update: true
      cleanup: true
      sets:
      - packages:
        - cronie
        - cronie-noanacron
        - curl
        - dhclient
        - initscripts
        - openssh-clients
        - passwd
        - policycoreutils
        - rootfiles
        - rsyslog
        - vim-minimal
        - sudo
        - openssh-server
        action: install

Now we need to install `distrobuilder` and generate the image:

.. code-block:: bash

    $ sudo snap install distrobuilder --classic
    $ sudo distrobuilder build-lxd centos.yaml -o image.architecture=x86_64 -o image.release=7 -o image.variant=cloud

To make this new image available to Juju, we need to import it with an alias:

.. code-block:: bash

    $ lxc image import lxd.tar.xz rootfs.squashfs --alias juju/centos7/amd64

You can check that the image was correctly imported to LXD with
``lxc image list``. To test it works with Juju, you can
``juju add-machine --series centos7``.
