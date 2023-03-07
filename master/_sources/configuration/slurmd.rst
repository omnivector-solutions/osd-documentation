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





``get-infiniband-repo``
-----------------------

Display the currently configured repository for Infiniband drivers.







``set-infiniband-repo``
-----------------------

Overrides the repository file with a custom repository for Infiniband installation.

.. note::

   This file should be base64 encoded.

On CentOS, the file is placed at ``/etc/yum.repos.d/infiniband.repo``, while on Ubuntu it is at ``/etc/apt/sources.list.d/infiniband.list``.




Parameters:


* ``repo``: Base64 encoded string that holds all information about the repository.



  * type: string






``install-infiniband``
----------------------

Install Mellanox Infiniband drivers. This might take a few minutes to complete.

If no custom repository was specified before, this action will set the Mellanox repository as the default and install the latest drivers from it.







``uninstall-infiniband``
------------------------

Uninstall Mellanox Infiniband drivers.





``start-infiniband``
--------------------

Start Infiniband systemd service.





``enable-infiniband``
---------------------

Enable Infiniband systemd service.





``stop-infiniband``
-------------------

Stop Infiniband systemd service.





``is-active-infiniband``
------------------------

Check if Infiniband systemd service is active.





``nvidia-repo``
---------------

Get or set the repository used to install Nvidia drivers.

This value must be set **before** installing the drivers. Changing it afterwards has no impact on the system.

.. note::

   The repository file must be base64 encoded when using this action.




Parameters:


* ``repo``: If specified, set the repository to the value specified.



  * type: string






``nvidia-package``
------------------

Get or set the Nvidia driver package name.

This value must be set **before** installing the drivers. Changing it afterwards has no impact on the system.




Parameters:


* ``package``: If specified, set the package name to the value specified



  * type: string






``nvidia-install``
------------------

Install Nvidia GPU drivers. This might take a few minutes to complete.

If no custom repository was specified before, this action will set the Nvidia repository as the default and install the latest drivers from it.







``singularity-install``
-----------------------

Install Singularity. This might take a few minutes to complete.

This action will install singularity using the official .deb (Ubuntu)  or .rpm (CentOS) packages retrieved from GitHub Releases.

.. note::

   The .deb or .rpm files must be supplied as Juju resources.







``mpi-install``
---------------

Install MPI (``mpich``). This might take a few minutes to complete.






