.. _contributing:

===================
Contributing to OSD
===================

OSD is an open-source project, and as such we welcome contributions from
developers, engineers, system administrators, and users in general.

There are many ways to contribute:

Feedback
========

Feedback is very welcome! We are interested in hearing from you how! Email us
@ `info@omnivector.solutions <mailto:info@omnivector.solutions>`_.

In the case things aren't working as expected, please
`file a bug <https://github.com/omnivector-solutions/slurm-charms/issues>`_.

Reach out if you have any questions and/or suggestions.


Documentation
=============

This documentation is built using `Sphinx <https://sphinx-doc.org/>`_ and
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
and is hosted in
`GitHub <https://github.com/omnivector-solutions/osd-documentation>`_.

General Recommendations
-----------------------

Use US English.

Wrap the lines at 80 columns when writing documentation.

Sections
--------

This projects uses the following convention for section headers, from the
`rsTructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections>`_
document::

   =================
   This is a heading
   =================

   This is a section
   =================

   This is a subsection
   --------------------

   This is a subsubsection
   ^^^^^^^^^^^^^^^^^^^^^^^

   This is a subsubsubsection
   ~~~~~~~~~~~~~~~~~~~~~~~~~~

Naming conventions
------------------

Throughout the documentation and code (specially in logs), we stick to these
naming conventions with regards to Slurm:

``SLURM``
   Schedmd Slurm project.

``slurmXXXd``
   The daemons for the Slurm component.

   For example, ``slurmd`` refers to the daemon for the compute nodes, while
   ``slurmctld`` refers to the daemon for the controller node.

``Slurm``
   Omnivector charms.


Code
====

OSD source-code is hosted in GitHub repositories. All the charms are in
`omnivector-solutions/slurm-charms <https://github.com/omnivector-solutions/slurm-charms>`_,
and a common code shared among them, called ``slurm-ops-mananger``, is hosted at
`omnivector-solutions/slurm-ops-manager <https://github.com/omnivector-solutions/slurm-ops-manager>`_.

By contributing with code development, you agree the license used.

Git usage
---------

- all commits should be atomic.
- linear history

  - always rebase with master
  - fast forward merge

- keep user related changes in the :ref:`changelog`
- annotated tags for releases, see :ref:`release-process` below for details

.. _charm-development:

Charm development
-----------------

All Python code should be compliant with Python3.6. This is a strong
requirement for the charms to run on CentOS7.

The coding style used follows closely
`PEP-008 <https://www.python.org/dev/peps/pep-0008/>`_.

Local setup
^^^^^^^^^^^

This sections describes how to setup your system for local charm development.
This section assumes the system is Linux-based and have support for `snaps`.

The tool used to build a charm is
`charmcraft <https://github.com/canonical/charmcraft/>`_, and it should be
installed as a classical snap:

.. code-block:: bash

   $ sudo snap install --edge charmcraft --classic

The charm code is available in the Git repository `slurm-charms
<https://github.com/omnivector-solutions/slurm-charms>`_, it contains all the
nuts and bolts of all Slurm Charms as well as a helper ``Makefile`` to build
the charms. To clone and build:

.. code-block:: bash

   $ git clone https://github.com/omnivector-solutions/slurm-charms
   $ cd slurm-charms
   $ make charms

You can manually deploy the charms and add the relations or use the
``slurm-core/charms/local-development.yaml`` overlay for your bundle. The
`slurm-bundles` repository contains a helper ``Makefile`` that uses this
overlay for all the targets. To deploy OSD locally in an LXD cluster running
Ubuntu 20.04, use the command ``make lxd-ubuntu``. And to deploy locally with
CentOS7: ``make lxd-centos``.

Slurm-ops-manager
^^^^^^^^^^^^^^^^^

Common code used in all charms should not be repeated. Instead, they should
live in this project.

After a new release of ``slurm-ops-manager``, all ``slurm-charms`` should have
a new commit to:

- update the version of ``slurm-ops-manager`` in the ``requirements.txt`` file.
- update the :ref:`changelog`.

Slurm-charms
^^^^^^^^^^^^

Specific code for each charm is handled in each charm.

Actions and Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~

All Juju actions, configurations, and their parameters should have a
description. This is the description that appears in the documentation pages,
after a pre-processing. Wrap the lines in the YAML files at 80 columns.

The documentation translates the ``description`` field of the actions and
configurations in the following ways:

- inline markdown code is translated to inline reStructuredText code.
- if there is a ``Note:`` text, this paragraph becomes a Sphinx ``note::``
  directive. This should be used to inform the end users of important
  information related to that action/config.
- if there is a ``Example usage:`` text, that paragraph becomes a Sphinx
  ``code-block::`` with the example given.

.. _changelog:

CHANGELOG
~~~~~~~~~

The ``CHANGELOG`` file contains notable changes for end users, not charm
developers. This means that internal changes (e.g., code related to CI,
refactoring, unit tests, etc.) should not be documented.

Changes that should be documented include:

- bug fixes
- new features
- new components
- changes in usage
- breaking changes

This file should be written in reStructuredText format and it is copied to the
documentation `Changelog page <changelog.html>`_ automatically.

There should always be one, and only one, section ``Unreleased`` in the
``CHANGELOG``. New entries should go at the top of this section.

Bats tests
~~~~~~~~~~

The Slurm Charms have an extensive suite of tests using
`Bats <https://github.com/bats-core/bats-core/>`_.

Install it with ``npm``:

.. code-block::

   $ npm install -g bats

To run the tests, enter in the directory of the ``slurm-charms`` and specify
the name of the Juju model used:

.. code-block::

   $ JUJU_MODEL=default npx bats tests/

.. note:: This will take a some minutes to run.

.. _versioning:

Versioning
----------

The Slurm-charms and ``slurm-ops-manager`` follow a semantic versioning scheme.

.. _release-process:

Release process
---------------

Slurm-charms
^^^^^^^^^^^^

To make a new release of the Slurm-charms, use the ``script/release.sh``
script. This script will update the :ref:`changelog` with the version of the
new release, create a new commit with the changes, and create a new Git tag
with a description of the new release. This script intentionally does not push
to GitHub, this way one can review the changes before ``git push``.

After the new release is made in GitHub, pack and release the charms in
Charmhub.

Slurm-ops-manager
^^^^^^^^^^^^^^^^^

The release process for ``slurm-ops-manager`` is straightforward:

- create a new annotated Git tag: ``git tag --annotate --sign x.y.z``. The tag
  name should be the new version of the library, as explained in
  :ref:`versioning`.
- the message should contain a summary of the changes for that release.
- push to GitHub.