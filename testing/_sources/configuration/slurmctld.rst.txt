.. This file is the template file to generate the configuration/slurm*.rst files
.. Please do not edit configuration/slurm*.rst files manually, they will be
.. overwritten next time the docs are rebuilt.

.. _operations-slurmctld:

=========
slurmctld
=========

The central management charm.



Configurations
==============

To change a configuration for this charm, use the Juju command:

.. code-block:: bash

   $ juju config slurmctld configuration=value



``custom-slurm-repo``
---------------------

Use a custom repository for Slurm installation.

This can be set to the Organization's local mirror/cache of packages and supersedes the Omnivector repositories. Alternatively, it can be used to track a ``testing`` Slurm version, e.g. by setting to ``ppa:omnivector/osd-testing`` (on Ubuntu), or ``https://omnivector-solutions.github.io/repo/centos7/stable/$basearch`` (on CentOS).

.. note::

   The configuration ``custom-slurm-repo`` must be set *before* deploying the units. Changing this value after deploying the units will not reinstall Slurm.




* type: string
* default-value: empty


``cluster-name``
----------------

Name to be recorded in database for jobs from this cluster.

This is important if a single database is used to record information from multiple Slurm-managed clusters.




* type: string
* default-value: ``osd-cluster``


``default-partition``
---------------------

Default Slurm partition. This is only used if defined, and must match an existing partition.




* type: string
* default-value: empty


``custom-config``
-----------------

User supplied Slurm configuration.

This value supplements the charm supplied ``slurm.conf`` that is used for Slurm Controller and Compute nodes.

Example Usage:

.. code-block:: bash

   $ juju config slurmcltd custom-config="FirstJobId=1234"




* type: string
* default-value: empty


``proctrack-type``
------------------

Identifies the plugin to be used for process tracking on a job step basis.




* type: string
* default-value: ``proctrack/cgroup``


``cgroup-config``
-----------------

Configuration content for ``cgroup.conf``.




* type: string
* default-value: ``CgroupAutomount=yes\nConstrainCores=yes\n``


``health-check-params``
-----------------------

Extra parameters for NHC command.

This option can be used to customize how NHC is called, e.g. to send an e-mail to an admin when NHC detects an error set this value to ``-M admin@domain.com``.




* type: string
* default-value: empty


``health-check-interval``
-------------------------

Interval in seconds between executions of the Health Check.


* type: int
* default-value: ``600``


``health-check-state``
----------------------

Only run the Health Check on nodes in this state.


* type: string
* default-value: ``ANY,CYCLE``


``acct-gather-frequency``
-------------------------

Accounting and profiling sampling intervals for the acct_gather plugins.

.. note::

   A value of ``0`` disables the periodic sampling. In this case, the accounting information is collected when the job terminates.

Example Usage:

.. code-block:: bash

   $ juju config slurmcltd acct-gather-frequency="task=30,network=30"




* type: string
* default-value: ``task=30``


``acct-gather-custom``
----------------------

User supplied ``acct_gather.conf`` configuration.

This value supplements the charm supplied ``acct_gather.conf`` file that is used for configuring the acct_gather plugins.




* type: string
* default-value: empty


``tls-key``
-----------

A TLS server private key (``.key`` file) to be used.


* type: string
* default-value: empty


``tls-cert``
------------

A TLS server certificate (``.crt`` file) to be used.


* type: string
* default-value: empty


``tls-ca-cert``
---------------

A CA certificate (``.crt`` file) to be used for verification of TLS

certificates. A CA certificate should only be issued in the case of

custom CAs and nodes not having it installed.




* type: string
* default-value: empty





Actions
=======

To run an action for this charm, use the Juju ``run-action`` command:

.. code-block:: bash

   $ juju run-action slurmctld/leader action-name [parameters=value]



``show-current-config``
-----------------------

Display the currently used ``slurm.conf``.

.. note::

   This file only exists in ``slurmctld`` charm and is automatically distributed to all compute nodes by Slurm.

Example Usage:

.. code-block:: bash

   $ juju run-action slurmctld/leader --format=json --wait | jq .[].results.slurm.conf | xargs -I % -0 python3 -c 'print(%)'







``drain``
---------

Drain specified nodes.

Example Usage:

.. code-block:: bash

   $ juju run-action slurmctld/leader drain nodename=node-[1,2] reason="Updating kernel"




Parameters:


* ``nodename``: The nodes to drain, using the Slurm format, e.g. ``node-[1,2]``.

  * type: string


* ``reason``: Reason to drain the nodes.

  * type: string






``resume``
----------

Resume specified nodes.

.. note::

   Newly added nodes will remain in the ``down`` state until configured, with the ``node-configured`` action.

Example Usage:

.. code-block:: bash

   $ juju run-action slurmctld/leader resume nodename=node-[1,2]




Parameters:


* ``nodename``: The nodes to resume, using the Slurm format, e.g. ``node-[1,2]``.



  * type: string






``influxdb-info``
-----------------

Get InfluxDB info.

This action returns the host, port, username, password, database, and retention policy regarding to InfluxDB.







``etcd-get-root-password``
--------------------------

Get the password for the etcd root account.







``etcd-get-slurmd-password``
----------------------------

Get the password for the etcd slurmd account.







``etcd-create-munge-account``
-----------------------------

Create a new etcd account to be able to query the munge key.




Parameters:


* ``user``: Desired username

  * type: string


* ``password``: Desired account password

  * type: string





