======================
Install slurm on MAAS
======================


Login to a juju controller
#######################################
If you don't already have a juju controller, bootstrap juju by creating a juju controller machine.

.. code-block:: bash

   juju bootstrap


Add a model
###########
Once you are logged into a juju controller you need to add a model. Run the following command to add the model that will house the OSD.

.. code-block:: bash

   juju add-model slurm



