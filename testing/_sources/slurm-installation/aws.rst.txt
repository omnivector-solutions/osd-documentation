=====================
Install slurm on AWS
=====================


Login to a juju controller
#######################################
In any deployment scenario we will need to be logged into a juju controller. For this example we will login to the public juju controller, jaas.

.. code-block:: bash

   juju login jaas


Add a model
###########
Once you are logged into a juju controller you need to add a model. Run the following command to add the model that will house the OSD.

.. code-block:: bash

   juju add-model slurm aws/us-west-2



