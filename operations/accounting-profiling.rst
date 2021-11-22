.. _accounting-profiling:

========================
Accounting And Profiling
========================

SLURM can collect accounting and profiling information about jobs and job
steps. Please find below instructions on how to setup accounting for the
different plugins, as well as the `official documentation about accounting
<https://slurm.schedmd.com/accounting.html>`_.


Slurmdbd
========

.. TODO

``slurmdbd`` is used for job accounting.

.. _influxdb-profiling:

InfluxDB profiling plugin
=========================

SLURM provides a profiling gathering plugin to collect metrics and send them to
`InfluxDB <https://www.influxdata.com/products/influxdb/>`_. OSD encapsulates
the configuration of this plugin in a *Juju relation* between ``slurmctld`` and
``influxdb`` charms.

A basic setup involves the following steps:

1. Deploy `InfluxDB charm <https://charmhub.io/influxdb>`_.
2. Relate ``slurmctld`` and ``influxdb``.
3. [optional] Configure the accounting frequency.

The Juju commands to accomplish these steps are:

.. code-block:: bash

   $ juju deploy influxdb
   $ juju relate slurmctld influxdb
   $ juju config slurmctld acct-gather-frequency="task=30"

In this scenario, ``slurmctld`` will setup everything needed to collect and
save the metrics, which include creating a database in InfluxDB. The name of
the database is the name of the cluster, as set in ``slurmctld``'s
configuration ``cluster-name``.

Data saved
----------

Slurm collects profiling metrics at a frequency specified in ``slurmctld``
configuration option ``acct-gather-frequency``.  The following field keys are
saved for the tasks:

``CPUFrequency``
    CPU Frequency at time of sample.

    Field type: ``float``.

``CPUTime``
    Seconds of CPU time used during the sample.

    Field type: ``float``.

``CPUUtilization``
    CPU Utilization during the interval.

    Field type: ``float``

``RSS``
    Value of RSS at time of sample.

    Field type: ``float``.

``VMSize``
    Value of VM Size at time of sample.

    Field type: ``float``.

``Pages``
    Pages used in sample.

    Field type: ``float``.

``ReadMB``
    Number of megabytes read from local disk.

    Field type: ``float``.

``WriteMB``
    Number of megabytes written to local disk. 

    Field type: ``float``.


Accessing the data
------------------

The ``slurmctld`` charm provides a convenient Juju Action to export the
InfluxDB parameters to setup a Grafana Data Source:

.. code-block:: bash

   $ juju run-action slurmctld/leader influxdb-info --wait
   unit-slurmctld-13:
     UnitId: slurmctld/13
     id: "573"
     results:
       influxdb: '{''ingress'': ''10.220.130.30'', ''port'': ''8086'', ''user'': ''slurm'',
         ''password'': ''LeCZSef2IzyOp3GAnYNC'', ''database'': ''osd-cluster'', ''retention_policy'':
         ''autogen''}'
     status: completed
     timing:
       completed: 2021-07-20 13:00:35 +0000 UTC
       enqueued: 2021-07-20 13:00:31 +0000 UTC
       started: 2021-07-20 13:00:34 +0000 UTC
