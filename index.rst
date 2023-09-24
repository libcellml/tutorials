.. _tutorials_index:

===================
libCellML Tutorials
===================

Please follow the :libcellml_doc_page:`Installation instructions <installation>` first to get yourself a copy of libCellML.

Introductory tutorials
----------------------

The first set of tutorials provides a simple starting point for users who are unfamiliar with CellML and/or modelling in general.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:
       
    tutorial*/index

For information on solving a CellML model with a simple numerical solver, please see the :libcellml_doc_page:`solving a generated model page <solver>`.   

Hodgkin-Huxley modelling tutorials
----------------------------------

The second set of tutorials take the user progressively through different aspects of the libCellML functionality while building towards a model of Hodgkin and Huxley's squid axon activation.
It is aimed at users who are already familiar with the concept of CellML and modelling.

For more information on their theoretical background, please see the `Hodgkin-Huxley theory pages <https://libcellml.org/documentation/theory>`_.  

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    hh_tutorial*/index

Common use case tutorials
-------------------------

The third set of tutorials take the user through some common use case scenarios.
For this set of tutorials it's presumed that you're already familiar with the structure and usage of CellML models, if this is not you then perhaps start from :ref:`Tutorial 1<tutorial1>` instead.

.. toctree::
    :maxdepth: 2
    :titlesonly:

    common_use_cases/annotation_tool_dev
    common_use_cases/import_debugger
    common_use_cases/model_debugger
    common_use_cases/package_dev
    common_use_cases/simulation_tool_dev
    common_use_cases/solver

.. toctree::
   :hidden:

   common_use_cases/index
