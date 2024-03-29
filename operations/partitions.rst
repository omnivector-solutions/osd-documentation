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
       charm: slurmd
       num_units: 1
     slurmd-debug:
       charm: slurmd
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

After that, re-deploy the bundle:

.. code-block:: bash

   $ juju deploy ./path/to/bundle.yaml

Alternatively, it is possible to manually add a new partition without a bundle
file:

.. code-block:: bash

   $ juju deploy slurmd slurmd-debug

This command will pull the ``slurmd`` charm from Charmhub and create a new
application named ``slurmd-debug``. It is possible to specify the operating
system to use for this application with the flag ``--series centos7`` or
``--series focal``. This approach requires issuing another command to relate
this new application to ``slurmctld``:

.. code-block:: bash

   $ juju relate slurmd-debug slurmctld

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
     charm: slurmd
     num_units: 1
     options:
       partition-name: debug

Setting the default partition
#############################

To set the default partition, you must configure ``slurmctld``:

.. code-block:: bash

   $ juju config slurmctld default-partition=debug

Alternatively, you can set the partition name in the bundle file:

::

   slurmctld:
     charm: slurmctld
     num_units: 1
     options:
       default-partition: debug

.. _changing-partition-state:

Changing partition state
########################

To change the partition state to one of ``UP``, ``DOWN``, ``DRAIN``, or
``INACTIVE``:

.. code-block:: bash

   $ juju config slurmd-debug partition-state=DRAIN

By default, the partition is in the ``UP`` state.

.. warning::

   Although it is possible to change the partition state with ``scontrol``,
   that change will be overwritten by the charms whenever OSD needs to update
   the Slurm configuration file.

Extra partition configuration options
#####################################

OSD allows the administrator to set any partition configuration, using the
*charm configuration* ``partition-config``. Please refer to the official Slurm
documentation for `configuring partitions
<https://slurm.schedmd.com/slurm.conf.html#SECTION_PARTITION-CONFIGURATION>`_
for details on all options available. The partition name and state should not
be set with this configuration, please refer to :ref:`Configuration - Slurmd
<operations-slurmd>` for details on all configuration options.

The ``partition-config`` option should be one line, with each configuration in
the format ``key=value`` separated by a space.

For example, to set the ``DefaultTime`` for a partition to 45 minutes and the
``MaxTime`` to 2 hours:

.. code-block:: bash

   $ juju config slurmd partition-config="DefaultTime=45:00 MaxTime=1:00:00"

   # running sinfo to check the partition TIMELIMIT
   $ juju run --unit slurmctld/leader sinfo
   PARTITION  AVAIL  TIMELIMIT  NODES  STATE NODELIST
   osd-slurmd    up    1:00:00      1   down juju-f48c73-262
