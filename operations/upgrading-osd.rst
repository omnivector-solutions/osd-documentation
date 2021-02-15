.. _operations-upgrading-osd:

=============
Upgrading OSD
=============
OSD upgrades can happen at two different levels; 1) the upgrading of the charm code itself, 2) the
upgrading of the underlying slurm snap resource (the slurm process itself).

If the desired affect is to upgrade the ops code, upgrade the charms. In the case that you want
to update the running slurm process itself, you will want to upgrade the snap.


**Charm Upgrades**
To upgrade the operations code, the slurm charms, you can follow the example
 (the order in which charms are upgraded does not matter here):
```bash
for application in slurmctld slurmd slurmdbd slurmrestd slurm-configurator; do
    juju upgrade-charm $application
done
```

Juju will reach out to the charmhub and pull down the latest charm code (if a more recent revisions exists
then what is running on the machine) and run the ``upgrade-charm`` hook event.


**Snap Upgrades**
The slurm snap can be upgraded via the slurm charms in a number of ways:

1) Attach a new resource to the charms.
The slurm charms will always use a supplied resource if available. To upgrade the running slurm snap
to a later version, attach the snap resource to the charm as follows.
```bash
for application in slurmctld slurmd slurmdbd slurmrestd slurm-configurator; do
    juju attach $application slurm-resource=slurm-snap.resource
done
```



In the case you want to upgrade the snap and the charm simultaneously, you can run:
```bash
for application in slurmctld slurmd slurmdbd slurmrestd slurm-configurator; do
    juju upgrade-charm $application --resource slurm-resource=slurm-snap.resource
done
```
