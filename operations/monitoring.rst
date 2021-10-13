.. _monitoring:

==========
Monitoring
==========

We provide a bundle overlay to simplify deploying
`Prometheus <https://prometheus.io/>`_ and
`Prometheus node_exporter <https://github.com/prometheus/node_exporter>`_ in
all nodes of the cluster.


Prometheus node_exporter
========================

The subordinate charm `prometheus-node-exporter <https://charmhub.io/prometheus-node-exporter>`_
can be used to to export machine metrics to a Prometheus instance. To monitor
all nodes in the cluster, first deploy the application
*prometheus-node-exporter* and then relate it to the nodes to be monitored:

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
   $ juju relate prometheus-node-exporter prometheus2

Please refer to these charm's documentation for configuration details.