.. _configuration-slurmdbd:

*************
slurmdbd
*************
Slurm Database Daemon.


.. list-table:: slurmdbd options
   :header-rows: 1

   * - Config
     - Description
     - Default value[
   * - snapstore-channel
     - Snap store channel to install the slurm snap from.
     - --stable
   * - nagios_context
     - |
       Used by the nrpe subordinate charms.
       A string that will be prepended to instance name to set the host name
       in nagios. So for instance the hostname would be something like:
           juju-myservice-0
       If you're running multiple environments with the same services in them
       this allows you to differentiate between them.
     - "juju"
   * - nagios_servicegroups
     - |
       A comma-separated list of nagios servicegroups.
       If left empty, the nagios_context will be used as the servicegroup
     -
   * - slurmdbd_debug
     - |
       The level of detail to provide slurmdbd daemon's logs. The default value
       is info. If the slurmdbd daemon is initiated with -v or --verbose
       options, that debug level will be preserve or restored upon
       reconfiguration."
     -
