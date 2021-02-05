.. _architecture:

Architecture
============
The OSD Consists of a configuration engine, slurm-configurator, and an application charm
for each component of slurm; slurmd, slurmctld, slurmdbd, slurmrestd. 


*************
Slurmctld
*************
The central management daemon of Slurm.  

*************
Slurmd
*************
The compute node daemon for Slurm.

*************
slurmdbd
*************
Slurm Database Daemon.

*************
slurmrestd
*************
Interface to Slurm via REST API.  

*************
slurm-configurator
*************
Slurm configuration engine.
