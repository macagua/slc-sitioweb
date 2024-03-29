SCRUM LATAM Comunidad Website
=============================

The `Scrum Latam Comunidad <https://www.scrumlatamcomunidad.com/>`_ Website repository.

|Built with Cookiecutter Plone Starter| |Black code style| |Backend
Tests| |Frontend Tests|

A new SCRUM LATAM Comunidad Website using Plone 6 and Volto
technologies.

Quick start
-----------

Development Setup
~~~~~~~~~~~~~~~~~

-  Python 3.9, 3.10, 3.11
-  Node 16
-  yarn
-  Docker

Install
~~~~~~~

.. code:: shell

   git clone git@github.com:ScrumLATAMComunidad/slc-sitioweb.git
   cd slc-sitioweb
   make install

Start
~~~~~

Start the Backend (http://localhost:8080/)

.. code:: shell

   make start-backend

Start the Frontend (http://localhost:3000/)

.. code:: shell

   make start-frontend

Structure
---------

This monorepo is composed by two distinct codebases: api and frontend.

-  **backend**: API (Backend) Plone installation using pip (not
   buildout). Includes a policy package named slc_sitioweb
-  **frontend**: React (Volto) package named frontend

Reasoning
~~~~~~~~~

-  Repo contains all codebase needed to run the site (excluding existing
   addons for Plone and React).
-  Github Workflows are triggered based on changes on each codebase (see
   .github/workflows)
-  Easier to create Docker images for each codebase
-  Showcase Plone installation/setup without buildout

Linters and Formatting
----------------------

There are some hooks to run lint checks on the code. If you want to
automatically format them, you can run

``make format``

in the root folder or especifically in each backend or frontend folders.

Linters commands are available in each backend and frontend folder.

Acceptance tests
----------------

There are ``Makefile`` commands in place:

``build-test-acceptance-server``: Build Acceptance Backend Server Docker
image that it’s being used afterwards. Must be run before running the
tests, if the backend code has changed.

``start-test-acceptance-server``: Start server fixture in docker
(previous build required)

``start-test-acceptance-frontend``: Start the Core Acceptance Frontend
Fixture in dev mode

``test-acceptance``: Start Core Cypress Acceptance Tests in dev mode

Credits
-------

**This was generated
by**\ `cookiecutter-plone-starter <https://github.com/collective/cookiecutter-plone-starter>`__\ **on
2023-05-11 04:07:02**

.. |Built with Cookiecutter Plone Starter| image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Plone%20Starter-0083be.svg?logo=cookiecutter
   :target: https://github.com/collective/cookiecutter-plone-starter/
.. |Black code style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
.. |Backend Tests| image:: https://github.com/ScrumLATAMComunidad/slc-sitioweb/actions/workflows/backend.yml/badge.svg
   :target: https://github.com/ScrumLATAMComunidad/slc-sitioweb/actions/workflows/backend.yml
.. |Frontend Tests| image:: https://github.com/ScrumLATAMComunidad/slc-sitioweb/actions/workflows/frontend.yml/badge.svg
   :target: https://github.com/ScrumLATAMComunidad/slc-sitioweb/actions/workflows/frontend.yml
