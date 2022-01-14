.. _installation:

=====================
Installation overview
=====================

The OSD can be installed on a cloud of your choosing. The only common component
used across deployments is juju_ itself. You must have the Juju client
installed on your local system in order to administer the installation and
deployment of the Slurm charms.

.. _juju: https://juju.is


Install Juju
============

.. code-block:: bash

   $ sudo snap install juju --classic


Once the Juju client is installed you will be ready to proceed with deploying
Slurm to a cloud of your choosing.


Setup cloud
===========

Follow the documentation for the cloud you with to deploy Slurm on:

AWS
###


Login to a Juju controller
--------------------------

In any deployment scenario we will need to be logged into a Juju controller.
For this example we will login to the public Juju controller, JAAS.

.. code-block:: bash

   $ juju login jaas


Add a model
-----------

Once you are logged into a Juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm aws/us-west-2


LXD
###

Bootstrap a localhost LXD Juju controller
-----------------------------------------

In any deployment scenario we will need to be logged into a Juju controller.
For this example we will bootstrap a Juju controller in a LXD container on our
local machine.

Install and configure LXD, if you haven't already:

.. code-block:: bash

   $ sudo snap install lxd
   $ lxd init --auto
   $ lxc network set lxdbr0 ipv6.address none

.. note::

   Juju does not support IPv6, the last command disables it.

You can now bootstrap your local cloud:

.. code-block:: bash

   $ juju bootstrap localhost

Following a successful bootstrap, ``juju controllers`` will show your newly
provisioned LXD controller.

.. _centos7-image:

CentOS7 Deploys on LXD clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Add a model
-----------

Once you have created your Juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm


MAAS
####


Login to a Juju controller
--------------------------

If you don't already have a Juju controller, bootstrap Juju by creating a Juju
controller machine.

.. code-block:: bash

   $ juju bootstrap


Add a model
-----------

Once you are logged into a Juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   $ juju add-model slurm


Deploy Slurm
============

Now it is time to get Slurm :)

We provide a bundle and overlays to simplify deploying all the components
needed for a complete Slurm cluster in the repository `slurm-bundles
<https://github.com/omnivector-solutions/slurm-bundles>`_. First, clone the
repository and then enter it:

.. code-block:: bash

   $ git clone https://github.com/omnivector-solutions/slurm-bundles
   $ cd slurm-bundles

The ``slurm-core`` directory contains all the bundles and overlays to deploy a
basic Slurm cluster:

- ``slurm-core/bundle.yaml``: the basic definition of the Slurm components.
- ``slurm-core/clouds/``: overlays with specific settings for each supported
  cloud environment. Currently available ones are AWS and LXD.
- ``slurm-core/series/``: overlays to define the OS of the Slurm components,
  the possible options are CentOS7 and Ubuntu Focal (20.04).
- ``slurm-core/charms/``: overlays to change the source of the charms. By
  default, the bundle gets them from the ``latest/stable`` channel from
  Charmhub.  The overlays in this directory allows us to change the source to
  either ``latest/edge`` channel or from your local machine. The latter one is
  specially useful for development, see :ref:`charm-development` for details.

The ``slurm-addons`` directory contains overlays to extend Slurm with plugins:

- ``slurm-addons/influxdb.yaml``: overlay to relate ``slurmctld`` to InfluxDB,
  to collect profiling information about the jobs. See
  :ref:`influxdb-profiling` for details on usage.
- ``slurm-addons/monitoring.yaml``: overlay to deploy `prometheus2
  <https://charmhub.io/prometheus2>`_ and `prometheus-node-exporter
  <https://charmhub.io/prometheus-node-exporter>`_ for cluster monitoring. See
  :ref:`monitoring` for details on usage.

For example, to deploy Slurm to a local LXD cloud, on Ubuntu Focal, using the
``latest/stable`` charms:

.. code-block:: bash

   $ juju deploy ./slurm-core/bundle.yaml \
                 --overlay ./slurm-core/clouds/lxd.yaml \
                 --overlay ./slurm-core/series/focal.yaml

Juju will then download the charms from Charmhub, create the applications,
configurations, and LXD containers described in the respective files, which
will comprise the model.

.. note::

   The Slurm-charms install Slurm from `Omnivector's OSD PPA
   <https://launchpad.net/~omnivector/+archive/ubuntu/osd>`_ on Ubuntu. It is
   possible to change the source to `Omnivector's Testing PPA
   <https://launchpad.net/~omnivector/+archive/ubuntu/osd-testing>`_ (or to a
   local cache server as well) with the configuration ``custom-slurm-repo``.
   Setting this value to repositories other than Omnivector's PPAs is not
   supported and might result in a broken system.

It will take a moment get everything ready. You can check the status of your
model with ``juju status``:

.. code-block:: bash

   $ watch -n 1 -c juju status --color

   Model    Controller  Cloud/Region         Version  SLA          Timestamp
   default  overlord    localhost/localhost  2.8.7    unsupported  17:44:29Z

   App              Version  Status  Scale  Charm            Store       Channel  Rev  OS      Message
   percona-cluster  5.7.20   active      1  percona-cluster  charmstore  stable   293  ubuntu  Unit is ready
   slurmctld        0.6.4    active      1  slurmctld        charmhub    stable     7  ubuntu  slurmctld available
   slurmd           0.6.4    active      1  slurmd           charmhub    stable    13  ubuntu  slurmd available
   slurmdbd         0.6.4    active      1  slurmdbd         charmhub    stable     5  ubuntu  slurmdbd ready
   slurmrestd       0.6.4    active      1  slurmrestd       charmhub    stable     5  ubuntu  slurmrestd available

   Unit                   Workload  Agent  Machine  Public address  Ports     Message
   percona-cluster/0*     active    idle   0        10.34.166.18    3306/tcp  Unit is ready
   slurmctld/0*           active    idle   2        10.34.166.222             slurmctld available
   slurmd/0*              active    idle   3        10.34.166.219             slurmd available
   slurmdbd/0*            active    idle   4        10.34.166.218             slurmdbd available
   slurmrestd/0*          active    idle   5        10.34.166.66              slurmrestd available

   Machine  State    DNS            Inst id        Series  AZ  Message
   0        started  10.34.166.18   juju-01ab62-0  bionic      Running
   2        started  10.34.166.222  juju-01ab62-2  focal       Running
   3        started  10.34.166.219  juju-01ab62-3  focal       Running
   4        started  10.34.166.218  juju-01ab62-4  focal       Running
   5        started  10.34.166.66   juju-01ab62-5  focal       Running


Once the workload status is *active* and the agent status is *idle*, the Slurm
cluster is ready for use.

You can see the status of your cluster by running the ``sinfo`` command:

.. code-block:: bash

   $ juju run --unit slurmctld/0 sinfo
   PARTITION         AVAIL  TIMELIMIT  NODES  STATE NODELIST
   osd-slurmd           up   infinite      1   down juju-01ab62-3

The nodes start in *down* state with a ``Reason = New node``, so when you add
more nodes to the cluster, they will not execute the jobs from queue. This way
it is possible to do some post installation before setting the nodes as *idle*.
You can double check that your nodes are down because of this and not some
other reason with ``sinfo -R``:

.. code-block:: bash

   $ juju run --unit slurmctld/0 "sinfo -R"
   REASON               USER      TIMESTAMP           NODELIST
   New node             root      2021-03-09T20:24:09 ip-172-31-83-4

After setting the node up, to bring it back you need to run a Juju *action*:

.. code-block:: bash

   $ juju run-action slurmd/1 node-configured
   $ juju run --unit slurmctld/0 sinfo
   PARTITION         AVAIL  TIMELIMIT  NODES  STATE NODELIST
   osd-slurmd           up   infinite      1   idle juju-01ab62-3

Please refer to our :ref:`operations` section for detailed instructions on how
to manage the cluster.
