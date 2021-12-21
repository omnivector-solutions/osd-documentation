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


.. _elasticsearch-paccounting:

ElasticSearch plugin
=====================

The `Slurm Elastic Search Plugin
<https://slurm.schedmd.com/elasticsearch.html>`_ stores accounting data for
finished jobs.

This plugin can be automatically enabled by relating the ``slurmctld`` charm
with the `Elastic Search Charm <https://charmhub.io/elasticsearch/>`_:

.. code-block:: bash

   $ juju relate slurmctld elasticsearch

The ``slurmctld`` will create a new index with the name of the cluster and the
document type is named ``jobcomp``.

Data Saved
----------

An example to get all the documents saved in the ``osd-cluster`` index from the
Elastic Search server at ``10.220.130.6`` is:

.. code-block:: bash

   $ curl -XGET 'http://10.220.130.6:9200/osd-cluster/_search?pretty=true&q=*:*'
   {
     "took" : 2,
     "timed_out" : false,
     "_shards" : {
       "total" : 5,
       "successful" : 5,
       "skipped" : 0,
       "failed" : 0
     },
     "hits" : {
       "total" : 2,
       "max_score" : 1.0,
       "hits" : [
         {
           "_index" : "osd-cluster",
           "_type" : "jobcomp",
           "_id" : "bnhJ3n0BaChVi1VR3viV",
           "_score" : 1.0,
           "_source" : {
             "jobid" : 24,
             "username" : "john",
             "user_id" : 1200,
             "groupname" : "john",
             "group_id" : 1200,
             "@start" : "2021-12-21T18:37:02",
             "@end" : "2021-12-21T18:37:02",
             "elapsed" : 0,
             "partition" : "osd-slurmd",
             "alloc_node" : "juju-f48c73-285",
             "nodes" : "juju-f48c73-286",
             "total_cpus" : 16,
             "total_nodes" : 1,
             "derived_ec" : "0:0",
             "exit_code" : "0:0",
             "state" : "COMPLETED",
             "cpu_hours" : 0.0,
             "pack_job_id" : 0,
             "pack_job_offset" : 0,
             "het_job_id" : 0,
             "het_job_offset" : 0,
             "@submit" : "2021-12-21T18:37:02",
             "@eligible" : "2021-12-21T18:37:02",
             "queue_wait" : 0,
             "work_dir" : "/home/john/project/foo",
             "cluster" : "osd-cluster",
             "qos" : "normal",
             "ntasks" : 0,
             "ntasks_per_node" : 0,
             "ntasks_per_tres" : 0,
             "cpus_per_task" : 1,
             "job_name" : "hostname",
             "tres_req" : "cpu=1,mem=15921M,node=1,billing=1",
             "tres_alloc" : "cpu=16,node=1,billing=16",
             "account" : "john",
             "parent_accounts" : "/users/user"
           }
         },
         {
           "_index" : "osd-cluster",
           "_type" : "jobcomp",
           "_id" : "b3hJ3n0BaChVi1VR3vi0",
           "_score" : 1.0,
           "_source" : {
             "jobid" : 25,
             "username" : "root",
             "user_id" : 0,
             "groupname" : "root",
             "group_id" : 0,
             "@start" : "2021-12-21T18:37:25",
             "@end" : "2021-12-21T18:37:25",
             "elapsed" : 0,
             "partition" : "osd-slurmd",
             "alloc_node" : "juju-f48c73-285",
             "nodes" : "juju-f48c73-286",
             "total_cpus" : 16,
             "total_nodes" : 1,
             "derived_ec" : "0:0",
             "exit_code" : "0:0",
             "state" : "COMPLETED",
             "cpu_hours" : 0.0,
             "pack_job_id" : 0,
             "pack_job_offset" : 0,
             "het_job_id" : 0,
             "het_job_offset" : 0,
             "@submit" : "2021-12-21T18:37:25",
             "@eligible" : "2021-12-21T18:37:25",
             "queue_wait" : 0,
             "work_dir" : "/root",
             "cluster" : "osd-cluster",
             "qos" : "normal",
             "ntasks" : 0,
             "ntasks_per_node" : 0,
             "ntasks_per_tres" : 0,
             "cpus_per_task" : 1,
             "job_name" : "hostname",
             "tres_req" : "cpu=1,mem=15921M,node=1,billing=1",
             "tres_alloc" : "cpu=16,node=1,billing=16",
             "account" : "root",
             "parent_accounts" : "/root/root"
           }
         }
       ]
     }
   }




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
save the metrics. This includes creating an user and a database in InfluxDB.
The username is ``slurm`` and the password is generated at random, while name
of the database is the name of the cluster, as set in ``slurmctld``'s
configuration ``cluster-name``.

Data saved
----------

Slurm collects profiling metrics at a frequency specified in the ``slurmctld``
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
