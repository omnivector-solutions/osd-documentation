.. _operations-upgrading-osd:

===========
Upgrade OSD
===========

Charm Upgrades
**************
To upgrade the operations code, the Slurm charms, you can follow the example
(the order in which charms are upgraded does not matter here):

.. code-block:: bash

    for application in slurmctld \
                       slurmd \
                       slurmdbd \
                       slurmrestd; do

        juju upgrade-charm $application

    done

Juju will reach out to the Charmhub and pull down the latest charm code (if a
more recent revisions exists then what is running on the machine) and run the
``upgrade-charm`` hook event.
