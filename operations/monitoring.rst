.. _monitoring:

==========
Monitoring
==========

We provide a bundle overlay to simplify deploying
`Prometheus <https://prometheus.io/>`_,
`Prometheus node_exporter <https://github.com/prometheus/node_exporter>`_ and
`slurm-exporter <https://charmhub.io/slurm-exporter>`_ to monitor the cluster
and each individual node.


Prometheus node_exporter
========================

"in all nodes of the cluster"

The subordinate charm `prometheus-node-exporter <https://charmhub.io/prometheus-node-exporter>`_
can be used to to export machine metrics to a Prometheus instance. To monitor
all nodes in the cluster, first deploy the application
``prometheus-node-exporter`` and then relate it to the nodes to be monitored:

.. code-block:: bash

   $ juju deploy prometheus-node-exporter
   $ juju relate prometheus-node-exporter slurmd
   $ juju relate prometheus-node-exporter slurmctld
   $ juju relate prometheus-node-exporter slurmdbd

This charm exposes by default all the metrics on endpoint ``/metrics`` using
the port ``9100``.

The charm ``prometheus-node-exporter`` can be related to the `prometheus2
<https://charmhub.io/prometheus2>`_ charm to automatically scrape all units.
Deploy Prometheus and relate it to node exporter to access this functionality:

.. code-block:: bash

   $ juju deploy prometheus2
   $ juju relate prometheus-node-exporter:prometheus prometheus2:scrape

Please refer to these charm's documentation for configuration details.


Prometheus Slurm exporter
=========================

The subordinate charm `slurm-exporter
<https://charmhub.io/slurm-exporter>`_ exports metrics about Slurm:
state of nodes, jobs, partitions, accounts, scheduler, CPUs, and GPUs. To
monitor the cluster, deploy the application and relate it to
``slurmrestd-charm``:

.. code-block:: bash

   $ juju deploy slurm-exporter
   $ juju relate slurm-exporter slurmrestd

.. note::

   We recommend deploying ``slurm-exporter`` in the ``slurmrestd`` node. This
   component could be deployed in other nodes.

This charm exposes by default all the metrics on endpoint ``/metrics`` using
the port ``9120``.

The charm ``slurm-exporter`` can be related to the `prometheus2
<https://charmhub.io/prometheus2>`_ charm to automatically scrape its metrics.
Deploy Prometheus and relate it to ``slurm-exporter`` to access this
functionality:

.. code-block:: bash

   $ juju deploy prometheus2
   $ juju relate prometheus-node-exporter:prometheus prometheus2:scrape

Please refer to these charm's documentation for configuration details.

You can use the `Grafana Dashboard 4323
<https://grafana.com/dashboards/4323>`_.to visualize the metrics exported via
``slurm-exporter``.
