.. This file is the template file to generate the configuration/slurm*.rst files
.. Please do not edit configuration/slurm*.rst files manually, they will be
.. overwritten next time the docs are rebuilt.

.. _operations-slurmrestd:

==========
slurmrestd
==========

Interface to Slurm via a REST API.



Configurations
==============

To change a configuration for this charm, use the Juju command:

.. code-block:: bash

   $ juju config slurmrestd configuration=value



``custom-slurm-repo``
---------------------

Use a custom repository for Slurm installation.

This can be set to the Organization's local mirror/cache of packages and supersedes the Omnivector repositories. Alternatively, it can be used to track a ``testing`` Slurm version, e.g. by setting to ``ppa:omnivector/osd-testing`` (on Ubuntu), or ``https://omnivector-solutions.github.io/repo/centos7/stable/$basearch`` (on CentOS).

.. note::

   The configuration ``custom-slurm-repo`` must be set *before* deploying the units. Changing this value after deploying the units will not reinstall Slurm.




* type: string
* default-value: empty




