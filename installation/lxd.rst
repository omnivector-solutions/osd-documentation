=====================
Install slurm on LXD
=====================


Bootstrap a localhost LXD Juju controller
#########################################

In any deployment scenario we will need to be logged into a juju controller.
For this example we will bootstrap a juju controller in a LXD container on our
local machine.

Install and configure LXD, if you haven't already:

.. code-block:: bash

   sudo snap install lxd
   lxd init --auto
   lxd network set lxdbr0 ipv6.address none

.. note::

   Juju does not support IPv6, the last command disables it.

You can now bootstrap your local cloud:

.. code-block:: bash

   juju bootstrap localhost

The command ``juju clouds`` can give you some details about the available
clouds, and the command ``juju status`` shows the status of that cloud.

Add a model
###########

Once you are logged into a juju controller you need to add a model. Run the
following command to add the model that will house the OSD.

.. code-block:: bash

   juju add-model slurm


Deploy Slurm
############

Now it is time to get Slurm :)

First we need to build a *charm*. That's what Juju will deploy to our cloud.
Chars are built with ``charmcraft``:

.. code-block:: bash

   sudo snap install --edge charmcraft

Clone the `slurm-charms <https://juju.is/docs/models>`_ git repository, it
contains all the nuts and bolts to build the charms:

.. code-block:: bash

   git clone https://github.com/omnivector-solutions/slurm-charms
   cd slurm-charms
   make charms

Now it is time to deploy!

.. code-block:: bash

   juju deploy ./bundles/slurm-core/focal-beta-lxd-bundle.yaml

Juju will then create the machines as described in that YAML and deploy the
charms. It will take a while to get everything ready. Wait some time and query
juju's status:

.. code-block:: bash

   $ juju status

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

