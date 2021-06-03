.. This file is the template file to generate the configuration/slurm*.rst files
.. Please do not edit configuration/slurm*.rst files manually, they will be
.. overwritten next time the docs are rebuilt.

.. _operations-slurmd:

======
slurmd
======

The SLURM compute node.



Configuration
=============

To change a configuration for this charm, use the Juju command:

.. code-block:: bash

   $ juju config slurmd configuration=value


partition-name
--------------

Name by which the partition may be referenced (e.g. "Interactive"). This name can be specified by users when submitting jobs. If the PartitionName is "DEFAULT", the values specified with that record will apply to subsequent partition specifications unless explicitly set to other values in that partition record or replaced with a different set of default values. Each line where PartitionName is "DEFAULT" will replace or add to previous default values and not a reinitialize the default values.



* type: string
* default-value: ``None``

partition-config
----------------

Extra partition configuration specified as a space separated key=value single line.



* type: string
* default-value: empty

partition-state
---------------

State of partition or availability for use. Possible values are "UP", "DOWN", "DRAIN" and "INACTIVE". The default value is "UP". See also the related "Alternate" keyword.



* type: string
* default-value: ``UP``

nhc-conf
--------

Custom extra configuration to use for Node Health Check.
These lines are appended to a basic nhc.conf provided by the charm.



* type: string
* default-value: empty





Actions
=======

To run an action for this charm, use the Juju ``run-action`` command:

.. code-block:: bash

   $ juju run-action slurmd/leader action-name [parameters]


version
-------

Return version of installed software




node-configured
---------------

Remove a nove from DownNodes when the reason is "New node".




get-node-inventory
------------------

Return node inventory.




show-nhc-config
---------------

Display the currently used nhc.conf




get-infiniband-repo
-------------------

Display the currently configured repository for Infiniband drivers.





set-infiniband-repo
-------------------

Overrides the repository file with a custom repository for Infiniband installation.
Note: this file should be base64 encoded.
On CentOS, the file is placed at /etc/yum.repos.d/infiniband.repo, while on Ubuntu it is at /etc/apt/sources.list.d/infiniband.list.



Parameters:


* ``repo``: Base64 encoded string that holds all information about the repository.


  * type: string





install-infiniband
------------------

Install Mellanox Infiniband drivers. This might take a few minutes to complete.
If no custom repository was specified before, this action will set the Mellanox repository as the default and install the latest drivers from it.





uninstall-infiniband
--------------------

Uninstall Mellanox Infiniband drivers.




start-infiniband
----------------

Start Infiniband systemd service.




enable-infiniband
-----------------

Enable Infiniband systemd service.




stop-infiniband
---------------

Stop Infiniband systemd service.




is-active-infiniband
--------------------

Check if Infiniband systemd service is active.




