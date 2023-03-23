.. This file is the template file to generate the configuration/slurm*.rst files
.. Please do not edit configuration/slurm*.rst files manually, they will be
.. overwritten next time the docs are rebuilt.

.. _operations-slurmd:

======
slurmd
======

The Slurm compute node.



Configurations
==============

To change a configuration for this charm, use the Juju command:

.. code-block:: bash

   $ juju config slurmd configuration=value



``custom-slurm-repo``
---------------------

Use a custom repository for Slurm installation.

This can be set to the Organization's local mirror/cache of packages and supersedes the Omnivector repositories. Alternatively, it can be used to track a ``testing`` Slurm version, e.g. by setting to ``ppa:omnivector/osd-testing`` (on Ubuntu), or ``https://omnivector-solutions.github.io/repo/centos7/stable/$basearch`` (on CentOS).

.. note::

   The configuration ``custom-slurm-repo`` must be set *before* deploying the units. Changing this value after deploying the units will not reinstall Slurm.




* type: string
* default-value: empty


``partition-name``
------------------

Name by which the partition may be referenced (e.g. ``Interactive``).

.. note::

   The partition name should only contain letters, numbers, and hyphens. Spaces are not allowed.




* type: string
* default-value: ``None``


``partition-config``
--------------------

Extra partition configuration, specified as a space separated ``key=value`` in a single line.

Example Usage:

.. code-block:: bash

   $ juju config slurmd partition-config="DefaultTime=45:00 MaxTime=1:00:00"




* type: string
* default-value: empty


``partition-state``
-------------------

State of partition or availability for use. Possible values are ``UP``, ``DOWN``, ``DRAIN`` and ``INACTIVE``. The default value is ``UP``. See also the related ``Alternate`` keyword.




* type: string
* default-value: ``UP``


``nhc-conf``
------------

Custom extra configuration to use for Node Health Check.

These lines are appended to a basic ``nhc.conf`` provided by the charm.




* type: string
* default-value: empty





Actions
=======

To run an action for this charm, use the Juju ``run-action`` command:

.. code-block:: bash

   $ juju run-action slurmd/leader action-name [parameters=value]



``version``
-----------

Return version of installed software.





``node-configured``
-------------------

Remove a node from DownNodes when the reason is ``New node``.





``get-node-inventory``
----------------------

Return node inventory.





``set-node-inventory``
----------------------

Modify node inventory.


Parameters:


* ``real-memory``: Total amount of memory of the node, in MB.

  * type: integer






``show-nhc-config``
-------------------

Display the currently used ``nhc.conf``.




