.. This file is the template file to generate the configuration/slurm*.rst files
.. Please do not edit configuration/slurm*.rst files manually, they will be
.. overwritten next time the docs are rebuilt.

.. _operations-slurmdbd:

========
slurmdbd
========

The SLURM database node.



Configuration
=============

To change a configuration for this charm, use the Juju command:

.. code-block:: bash

   $ juju config slurmdbd configuration=value


slurmdbd-debug
--------------

The level of detail to provide slurmdbd daemon's logs. The default value is info. If the slurmdbd daemon is initiated with -v or --verbose options, that debug level will be preserve or restored upon reconfiguration.



* type: string
* default-value: ``info``



