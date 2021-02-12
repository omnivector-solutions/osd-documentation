.. _configuration-configuration-slurm-configurator:

******************
slurm-configurator
******************
Slurm configuration engine.

.. list-table:: slurm-configurator options
   :header-rows: 1

   * - Config
     - Description
     - Default value
   * - snapstore-channel
     - Snapstore channel to install the slurm snap from.
     - --stable
   * - cluster_name
     - Name of the slurm cluster.
     - cluster1
   * - default_partition
     - Default cluster partition.
     - 
   * - acct_gather_custom
     - User supplied acct_gather.conf confinguration.
     - 
   * - custom_config
     - User supplied slurm confinguration.
     -
   * - proctrack_type
     - Plugin to be used for process tracking on a job step basis. Defaults to 'proctrack/cgroup'.
     - proctrack/cgroup
   * - cgroup_config
     - User supplied configuration for cgroup.conf.
     - |
       CgroupAutomount=yes
       ConstrainCores=yes
   * - node_weight_criteria
     - Type of node criteria to use for setting weights on nodes.
     -




