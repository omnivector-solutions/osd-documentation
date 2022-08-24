.. _singularity:

===========
Singularity
===========


The ``slurmd`` charm support installing Singularity using a Juju action.
This action will install Singularity using the supplied packages (.deb for Ubuntu or .rpm for CentOS) as Juju Resources. We recommend downloading them  from `GitHub Releases <https://github.com/sylabs/singularity/releases>`_.

For example, you can download the appropriate file to your operating system from:

- `Ubuntu 20.04 - Singularity CE 3.10.2 <https://github.com/sylabs/singularity/releases/download/v3.10.2/singularity-ce_3.10.2-focal_amd64.deb>`_
- `CentOS7 - Singularity CE 3.10.2 <https://github.com/sylabs/singularity/releases/download/v3.10.2/singularity-ce-3.10.2-1.el7.x86_64.rpm>`_

.. note:: The .deb or .rpm files must be supplied as Juju resources.

Before running the action, the packages must supplied as Juju resources, according to each operating system:

Ubuntu:

   When deploying the charm:

   .. code-block:: bash

      $ juju deploy slurmd --resource singularity-deb=singularity-ce_3.10.2-focal_amd64.deb

   Or on a deployed charm:

   .. code-block:: bash

      $ juju attach-resource slurmd singularity-deb=singularity-ce_3.10.2-focal_amd64.deb

CentOS7:

   When deploying the charm:

   .. code-block:: bash

      $ juju deploy slurmd --resource singularity-rpm=singularity-ce-3.10.2-1.el7.x86_64.rpm --series centos7

   Or on a deployed charm:

   .. code-block:: bash

      $ juju attach-resource slurmd singularity-rpm=singularity-ce-3.10.2-1.el7.x86_64.rpm

With the .deb or .rpm files supplied as Juju resources, we can run the action
that will install Singularity on the ``slurmd`` node:

.. code-block:: bash

      $ juju run-action slurmd/leader singularity-install

This might take a few minutes to complete. After that, we can check the installation using:

.. code-block:: bash

      $ juju run --unit slurmd/leader "singularity --version"