.. _configuration-configuration-slurmctld:

*************
Slurmctld
*************
The central management daemon of Slurm.  

.. list-table:: slurmctld options
   * - Config
     - Description
     - Default value
   * - snapstore-channel
     - Snapstore channel to install the slurm snap from.
     - "--stable"
   * - nagios_context
     - |
       Used by the nrpe subordinate charms.
       A string that will be prepended to instance name to set the host name
       in nagios. So for instance the hostname would be something like:
           juju-myservice-0
       If you're running multiple environments with the same services in them
       this allows you to differentiate between them.
     -
   * - nagios_servicegroups
     - |
      A comma-separated list of nagios servicegroups.
      If left empty, the nagios_context will be used as the servicegroup
     -


