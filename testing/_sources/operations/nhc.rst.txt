.. _nhc:

===
NHC
===

OSD installs `LBNL Node Health Check (NHC) <https://github.com/mej/nhc>`_ by
default in the ``slurmd`` charm. The base configuration file contains only
basic checks to ensure slurm and munge processes are active. You
can easily extend the NHC configuration to match your setup.

For example, suppose you want to also check for: 100 Gb/sec Infiniband, and the
``/scratch`` partition to be mounted as ``r/w``. The easiest way to do so is to
create a ``custom-conf.nhc`` file with those checks:

::

   * || check_fs_mount_rw -f /scratch
   * || check_hw_ib 100

And then configure your ``slurmd`` application to use it:

.. code-block:: bash

        $ juju config slurmd nhc-conf="$(cat custom-conf.nhc)"

Note that this *appends* your custom configurations to the charm defined
``nhc.conf``, without overwriting the pre-existing checks defined by the charm.

We also provide an action to see the currently used ``nhc.conf``, which
contains our base checks in addition to your custom ones:

.. code-block:: bash

        $ juju run-action slurmd/leader show-nhc-config --wait

The default settings used in ``slurm.conf`` for NHC are as follows:

::

   HealthCheckProgram=/sbin/nhc
   HealthCheckInterval=600
   HealthCheckNodeState=ANY,CYCLE

It is possible to change the interval (in seconds) and the node states:

.. code-block:: bash

   $ juju config slurmd health-check-interval=300
   $ juju config slurmd health-check-state="CYCLE,ANY"

Please refer to the
`slurm.conf documentation <https://slurm.schedmd.com/slurm.conf.html>`_ for
configuration details.
