.. _nhc:

===
NHC
===

OSD installs `LBNL Node Health Check (NHC) <https://github.com/mej/nhc>`_ by
default in the ``slurmd`` charm. NHC is an utility to help to prevent jobs to
run on unhealthy nodes. In order to identify if a node is healthy or not, NHC
runs checks periodically. These health checks can be customized and tuned to
each particular cluster, node, and/or hardware.

The base configuration file contains only basic checks to ensure Slurm and
Munge processes are active. You can easily extend the NHC configuration to
match your setup.

When NHC identifies a node to be unhealthy, NHC drains this node to prevent
future jobs from running on it.

Installation
============

The ``slurmd`` charm installs NHC using from a tarball acquired from the official project page.

When deploying the charm directly from CharmHub, the tarball with be automatically provided. It is only necessary to acquire the file locally when the charm is deployed from a local file, or when you want to install a specific NHC version.

.. note::

   The NHC tarball must be provided _before_ deploying the charm. Attaching a different tarball after the charm is deployed will have no effect.

And example to download a tarball for NHC and deploy the ``slurmd`` charm using it:

.. code-block:: bash
    
     $ wget https://github.com/mej/nhc/releases/download/1.4.3/lbnl-nhc-1.4.3.tar.gz
     $ juju deploy slurmd --resource nhc=lbnl-nhc-1.4.3.tar.gz

Configuration
=============

Health Checks
-------------

.. note::

   OSD uses short hostnames (``hostname -s``) as node identifiers in Slurm.
   Because of this, the NHC configuration needs to use the short hostname
   also. The base NHC configuration provided in the slurmd charm takes care of
   this by setting ``* || HOSTNAME="$HOSTNAME_S"`` at the top of the NHC
   configuration file. This value will not be overridden by any custom user
   supplied NHC configuration.

   This is specially important if running checks on specific nodes on the
   cluster. For example, to only run the Nvidia monitoring on the ``gpu-*``
   nodes:

   ::

      gpu-* || NVIDIA_HEALTHMON=...

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

NHC options
-----------

The default settings used in ``slurm.conf`` for NHC are as follows:

::

   HealthCheckProgram=/usr/sbin/omni-nhc-wrapper
   HealthCheckInterval=600
   HealthCheckNodeState=ANY,CYCLE

These values implies that NHC will run at every 600 seconds (10 minutes), on
all compute nodes regardless of their state (even on allocated nodes), but it
will not run on all of them at the same time.

The ``/usr/sbin/omin-nhc-wrapper`` script allows you to supply custom arguments
to change how Slurm invokes the Health Check scripts via a ``charm-slurmctld``
configuration. For example, to configure NHC to send an e-mail to
``admin@company.com`` with the subject header ``NHC errors`` when it detects an
error, change the ``health-check-params`` configuration to:

.. code-block:: bash

   $ juju config slurmctld health-check-params='-M admin@company.com -S "NHC errors"'

Please check the `documentation for NHC <https://github.com/mej/nhc>`_ for
configuration details.

It is possible to change the interval (in seconds) that NHC runs and the node
states to perform the checks:

.. code-block:: bash

   $ juju config slurmd health-check-interval=300
   $ juju config slurmd health-check-state="CYCLE,ANY"

.. note::

   NHC does not *undrain* a node. If a node was drained and NHC runs on that
   node, the node will continue on the drained state, regardless of the checks
   passing or failing.

   This ensures that if someone drained a node for troubleshooting, it will not
   be resumed before the administrator finishes their tasks.

Please refer to the
`slurm.conf documentation <https://slurm.schedmd.com/slurm.conf.html>`_ for
configuration details.
