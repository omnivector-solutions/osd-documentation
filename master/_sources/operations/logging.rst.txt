.. _logging:

=======
Logging
=======

OSD can forward internal logs to a centralized place using the built-in
integration (a *Juju relation*) to `Fluentbit <https://fluentbit.io>`_.

Fluentbit
=========

Fluentbit is a lightweight and high-performance log processor and forwarder,
and is available as a Juju charm: `charm-fluentbit
<https://charmhub.io/fluentbit>`_ 

OSD configures Fluentbit to automatically forward the following logs:

* :ref:`nhc` logs (``/var/log/nhc.log``), only on the compute nodes (running
  ``slurmd`` charm)
* internal Slurm logs:

  * ``/var/log/slurm/slurmctld.log`` on the nodes running ``slurmctld`` charm
  * ``/var/log/slurm/slurmd.log`` on the nodes running ``slurmd`` charm
  * ``/var/log/slurm/slurmdbd.log`` on the nodes running ``slurmdbd`` charm

Each log entry is enriched with:

*  ``cluster-name``
* ``hostname``
* ``service`` (one of ``nhc``, ``slurmd``, ``slurmdbd``, ``slurmctld``)
* ``partition-name`` (only for nodes running the ``slurmd`` charm)


Deploy
------

To deploy the `fluentbit charm <https://charmhub.io/fluentbit>`_ and relate it
to the other components:

.. code-block:: bash

   $ juju deploy fluentbit
   $ juju relate fluentbit:fluentbit slurmd
   $ juju relate fluentbit:fluentbit slurmdbd
   $ juju relate fluentbit:fluentbit slurmctld

This configures everything needed to read, parse, and filter the log files.

Configuration
-------------

Output
^^^^^^

The Juju relation between Fluentbit and the Slurm charms setup the *source*
logs to be forwarded, but does not define the output. This has to be done
either manually (via a Fluentbit charm configuration) or via a centralized
logging system that can be related to it.

Fluentbit support many and multiple outputs. Please consult the online
documentation for details: `Fluentbit Outputs
<https://docs.fluentbit.io/manual/pipeline/outputs>`_.

Graylog
~~~~~~~

To configure Fluentbit to forward logs to a Graylog cluster running, first
setup a Graylog GELF Input, then create a ``graylog.fluentbit`` text file with
the following::

   [{"output": [["name", "gelf"],
                ["match", "*"],
                ["host", "10.220.130.119"],
                ["port", "12201"],
                ["mode", "udp"],
                ["Gelf_Short_Message_Key", "log"]]}]

Modify the ``host``, ``port``, and ``mode`` accordingly.

Then, configure Fluentbit to use this:

.. code-block:: bash

   $ juju config fluentbit custom-config="$(cat graylog.fluentbit)"
