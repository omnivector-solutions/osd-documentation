=====================
Install slurm on LXD
=====================


Bootstrap a localhost LXD Juju controller
##########################################
In any deployment scenario we will need to be logged into a juju controller. For this example we will bootstrap a juju controller in a LXD container
on our local machine.

.. code-block:: bash

   juju bootstrap localhost


Add a model
###########
Once you are logged into a juju controller you need to add a model. Run the following command to add the model that will house the OSD.

.. code-block:: bash

   juju add-model slurm



