.. _partitions:

==========
Partitions
==========

We recommend to use one ``slurmd`` application for each partition in your
cluster. So, to add a new partition you need to deploy a new ``slurmd`` charm,
with a new *Juju application name*.

Adding partitions
#################

The easiest way to add a new partition is to modify the
``slurm-bundles/slurm-core/bundle.yaml`` file with your new application.

To add a ``slurmd-debug`` application for the ``debug`` partition, we need to:

- add the application;
- add a relation to the slurmctld charm;
- add extra options depending on the cloud provider.

So, edit the bundle file to add a new entry in the ``applications`` section:

::

   applications:
     slurmd:
       charm: ./../../slurm-charms/slurmd.charm
       num_units: 1
     slurmd-debug:
       charm: ./../../slurm-charms/slurmd.charm
       num_units: 1
     ...

And similarly, the relations:

::

   relations:
     - - slurmctld:slurmd
       - slurmd-debug:slurmd

If you need any custom configurations for your cloud provider, you could add
them in this file or in the used overlay file. For example, we provide
constraints and bindings for AWS clouds as an overlay in
``slurm-bundles/slurm-core/clouds/aws.yaml``. If deploying to AWS, you should
also copy those bindings to the new application.

Changing partition name
#######################

By default, the charms create a unique name for each partition, based on the
name of the Juju Application. You can change the partition name with a Juju
configuration command:

.. code-block:: bash

   $ juju config slurmd-debug partition-name=debug

Alternatively, you can set the partition name in the bundle file:

::

   slurmd-debug:
     charm: ./../../slurm-charms/slurmd.charm
     num_units: 1
     options:
       partition-name: debug

Setting the default partition
#############################

To set the default partition, you must configure ``slurmctld``:

.. code-block:: bash

   $ juju config slurmdctld default-partition=debug

Alternatively, you can set the partition name in the bundle file:

::

   slurmdctld:
     charm: ./../../slurm-charms/slurmctld.charm
     num_units: 1
     options:
       default-partition: debug

.. _changing-partition-state:

Changing partition state
########################

To change the partition state to one of ``UP``, ``DOWN``, ``DRAIN``, or
``INACTIVE``:

.. code-blocK:: bash

   $ juju config slurmd-debug partition-state=DRAIN

By default, the partition is in the ``UP`` state.
