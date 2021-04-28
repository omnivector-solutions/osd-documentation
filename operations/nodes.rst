.. _nodes:

================
Nodes operations
================

This section walks through configurations and actions dealing with Slurm
compute nodes.

Adding nodes
############

New nodes are added in ``down`` state. This allows the cluster administrator to
install and configure dependencies before the node can run jobs.

To add 10 nodes to application ``slurmd``:

.. code-block:: bash

   $ juju add-unit slurmd -n10

After the node is added and properly configured, you can then enlist it:

.. code-block:: bash

   $ juju run-action slurmd/1 node-configured

Removing nodes
##############

Removing nodes are as simple as:

.. code-block:: bash

   $ juju remove-unit slurmd/4

Draining nodes
##############

We provide an action in the ``slurmctld`` charm to drain nodes. You need to
know in advance the hostname of the nodes you want to drain. You need to
specify a *reason* to drain. You can specify more than one node, by using the
Slurm convention:

.. code-block:: bash

   $ juju run-action slurmctld/leader drain nodename=juju-724cba-[1,3] reason="Maintenance - drive failure" --wait
   unit-slurmctld-0:
     UnitId: slurmctld/0
     id: "26"
     log:
     - 2021-04-28 17:13:06 -0300 -03 Draining juju-724cba-[1,3] because Maintenance -
       drive failure.
     results:
       nodes: juju-724cba-[1,3]
       status: draining
     status: completed
     timing:
       completed: 2021-04-28 20:13:07 +0000 UTC
       enqueued: 2021-04-28 20:13:04 +0000 UTC
       started: 2021-04-28 20:13:06 +0000 UTC

We recommend running this action in the *leader* of ``slurmctld`` application
instead of using the number.

Resuming nodes
##############

We provide an action to resume nodes in ``slurmctld`` charm:

.. code-block:: bash

   $ juju run-action slurmctld/leader resume nodename=juju-724cba-[1,3] --wait
   unit-slurmctld-0:
     UnitId: slurmctld/0
     id: "32"
     log:
     - 2021-04-28 17:17:23 -0300 -03 Resuming juju-724cba-[1,3].
     results:
       nodes: juju-724cba-[1,3]
       status: resuming
     status: completed
     timing:
       completed: 2021-04-28 20:17:23 +0000 UTC
       enqueued: 2021-04-28 20:17:18 +0000 UTC
       started: 2021-04-28 20:17:23 +0000 UTC


