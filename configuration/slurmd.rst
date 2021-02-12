.. _configuration-slurmd:

*************
Slurmd
*************
The compute node daemon for Slurm.


.. list-table:: slurmd options
   :header-rows: 1

   * - Config
     - Description
     - Default value
   * - snapstore-channel
     - Snap store channel to install the slurm snap from.
     - --stable
   * - partition-name
     - |
       Name by which the partition may be referenced (e.g. "Interactive"). This
       name can be specified by users when submitting jobs. If the PartitionName
       is "DEFAULT", the values specified with that record will apply to
       subsequent partition specifications unless explicitly set to other values
       in that partition record or replaced with a different set of default
       values. Each line where PartitionName is "DEFAULT" will replace or add to
       previous default values and not a reinitialize the default values.
     - 
   * - partition-config
     - |
       Extra partition configuration specified as a space separated key=value single line.
     -
   * - partition-state
     - |
       State of partition or availability for use. Possible values are "UP", "DOWN", "DRAIN" and "INACTIVE". The default value is "UP". See also the related "Alternate" keyword.
     - "UP"
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
