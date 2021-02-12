.. _deployment:

Deployment
============

 1 Install Juju
To deploy the OSD you must have the juju client installed. Run the following command to install Juju.

sudo snap install juju --classic


# 2 Login or Bootstrap Controller
In order to deploy OSD you must first login to a juju controller on a cloud of your choosing.

juju login jaas


# 3 Add a model
Once you are logged into a juju controller you need to add a model. Run the following command to add the model that will house the OSD.

juju add-model slurm aws/us-west-2


# 4 Deploy charms

Now that you have a model to deploy the OSD to, you can proceed with provisioning the slurm charms by deploying the slurm-core bundle which will inturn provision the OSD component charms.

juju deploy slurm-core









The Omnivector Slurm Distribution can be configured to the extent that you can configure slurm itself.
Meaning that all upstream slurm configurations are supported by OSD.

.. toctree::
   :maxdepth: 2
   :numbered: 1

The `slurm.conf` file can be customized through the slurm charm configuration options.
Each slurm component charm provides a set of options that enable operators to configure the
cluster.


.. toctree::
   :maxdepth: 2
   :numbered:

   slurm-configurator
   slurmctld
   slurmd
   slurmdbd
   slurmrestd
