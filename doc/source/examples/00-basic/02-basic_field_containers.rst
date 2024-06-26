
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples\00-basic\02-basic_field_containers.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_examples_00-basic_02-basic_field_containers.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_00-basic_02-basic_field_containers.py:


.. _ref_basic_field_example:

Field and field containers overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In DPF, the field is the main simulation data container. During a numerical
simulation, the result data is defined by values associated to entities
(scoping). These entities are a subset of a model (support).

Because the field data is always associated to its scoping and support,
the field is a self-describing piece of data. A field is also
defined by its parameters, such as dimensionality, unit, and location.
For example, a field can describe any of the following:

- Displacement vector
- Norm, stress, or strain tensor
- Stress or strain equivalent
- Minimum or maximum over time of any result.

A field can be defined on a complete model or on only certain entities
of the model based on its scoping. The data is stored as a vector of
double values, and each elementary entity has a number of components.
For example, a displacement has three components, and a symmetrical
stress matrix has six components.

In DPF, a fields container is simply a collection of fields that can be
indexed, just like a Python list. Operators applied to a fields
container have each individual field operated on. Fields
containers are outputs from operators.

.. GENERATED FROM PYTHON SOURCE LINES 34-41

.. code-block:: Python


    # First, import necessary modules
    import numpy as np

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples








.. GENERATED FROM PYTHON SOURCE LINES 42-44

Create a model object to establish a connection with an
example result file and then extract:

.. GENERATED FROM PYTHON SOURCE LINES 44-47

.. code-block:: Python

    model = dpf.Model(examples.find_static_rst())
    print(model)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Model
    ------------------------------
    Static analysis
    Unit system: MKS: m, kg, N, s, V, A, degC
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  reaction_force: Nodal Force   
         -  stress: ElementalNodal Stress 
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  elastic_strain: ElementalNodal Strain
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region: 
      81 nodes 
      8 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 1 
    Cumulative     Time (s)       LoadStep       Substep         
    1              1.000000       1              1               





.. GENERATED FROM PYTHON SOURCE LINES 48-50

Create the displacement operator directly from the ``results``
property and extract the displacement fields container:

.. GENERATED FROM PYTHON SOURCE LINES 50-54

.. code-block:: Python

    disp_op = model.results.displacement()
    fields = disp_op.outputs.fields_container()
    print(fields)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF displacement(s)Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  1} with Nodal location, 3 components and 81 entities.





.. GENERATED FROM PYTHON SOURCE LINES 55-57

A field can be extracted from a fields container by simply indexing
the requested field:

.. GENERATED FROM PYTHON SOURCE LINES 57-60

.. code-block:: Python

    field = fields[0]
    print(field)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF displacement_1.s Field
      Location: Nodal
      Unit: m
      81 entities 
      Data:3 components and 81 elementary data 





.. GENERATED FROM PYTHON SOURCE LINES 61-65

Extract data from a field
~~~~~~~~~~~~~~~~~~~~~~~~~
You can extract all the data from a given field using the ``data``
property. This returns a ``numpy`` array.

.. GENERATED FROM PYTHON SOURCE LINES 65-68

.. code-block:: Python


    print(field.data)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    [[-3.31904602e-22 -6.93565975e-09 -3.28617350e-22]
     [ 2.23026491e-09 -7.14214033e-09 -2.92077883e-22]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-3.01173895e-22 -7.14214033e-09 -2.23026491e-09]
     [ 2.09077164e-09 -7.33058082e-09 -2.09077164e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 1.06212713e-09 -6.89858785e-09 -3.77906905e-22]
     [ 1.89019831e-09 -3.34398104e-09  1.43440783e-23]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.71912713e-23 -2.92690969e-09 -2.33676924e-23]
     [ 1.01364486e-09 -7.10540890e-09 -2.14726184e-09]
     [ 1.89155604e-09 -3.73823999e-09 -1.89155604e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 7.64096553e-24 -3.34398104e-09 -1.89019831e-09]
     [-3.81104389e-22 -6.89858785e-09 -1.06212713e-09]
     [ 2.14726184e-09 -7.10540890e-09 -1.01364486e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-9.53485079e-23 -7.14214033e-09  2.23026491e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 2.09077164e-09 -7.33058082e-09  2.09077164e-09]
     [ 1.18477336e-22 -3.34398104e-09  1.89019831e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 1.89155604e-09 -3.73823999e-09  1.89155604e-09]
     [ 1.01364486e-09 -7.10540890e-09  2.14726184e-09]
     [-2.61320844e-22 -6.89858785e-09  1.06212713e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [ 2.14726184e-09 -7.10540890e-09  1.01364486e-09]
     [-1.54190337e-21 -1.42766633e-08 -1.53720678e-21]
     [ 2.25103522e-09 -1.43688328e-08 -1.55960665e-21]
     [-1.55180700e-21 -1.43688328e-08 -2.25103522e-09]
     [ 2.25860708e-09 -1.44669483e-08 -2.25860708e-09]
     [-1.02704768e-21 -1.05919802e-08 -1.01743770e-21]
     [ 1.16452955e-09 -1.44002311e-08 -1.52834607e-21]
     [ 2.29356739e-09 -1.07400000e-08 -1.07537743e-21]
     [-1.08050063e-21 -1.07400000e-08 -2.29356739e-09]
     [ 1.16046741e-09 -1.44722939e-08 -2.25762828e-09]
     [ 2.26430754e-09 -1.08989140e-08 -2.26430754e-09]
     [-1.50544246e-21 -1.44002311e-08 -1.16452955e-09]
     [ 2.25762828e-09 -1.44722939e-08 -1.16046741e-09]
     [ 2.25860708e-09 -1.44669483e-08  2.25860708e-09]
     [-1.24684037e-21 -1.43688328e-08  2.25103522e-09]
     [ 2.26430754e-09 -1.08989140e-08  2.26430754e-09]
     [ 1.16046741e-09 -1.44722939e-08  2.25762828e-09]
     [-8.03413897e-22 -1.07400000e-08  2.29356739e-09]
     [ 2.25762828e-09 -1.44722939e-08  1.16046741e-09]
     [-1.35051199e-21 -1.44002311e-08  1.16452955e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.23026491e-09 -7.14214033e-09 -9.66448574e-23]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.09077164e-09 -7.33058082e-09 -2.09077164e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-1.89019831e-09 -3.34398104e-09  1.19096032e-22]
     [-1.06212713e-09 -6.89858785e-09 -2.59300974e-22]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-1.89155604e-09 -3.73823999e-09 -1.89155604e-09]
     [-1.01364486e-09 -7.10540890e-09 -2.14726184e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.14726184e-09 -7.10540890e-09 -1.01364486e-09]
     [-2.09077164e-09 -7.33058082e-09  2.09077164e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-1.01364486e-09 -7.10540890e-09  2.14726184e-09]
     [-1.89155604e-09 -3.73823999e-09  1.89155604e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.14726184e-09 -7.10540890e-09  1.01364486e-09]
     [ 0.00000000e+00  0.00000000e+00  0.00000000e+00]
     [-2.25103522e-09 -1.43688328e-08 -1.20291800e-21]
     [-2.25860708e-09 -1.44669483e-08 -2.25860708e-09]
     [-2.29356739e-09 -1.07400000e-08 -7.91446544e-22]
     [-1.16452955e-09 -1.44002311e-08 -1.32988359e-21]
     [-2.26430754e-09 -1.08989140e-08 -2.26430754e-09]
     [-1.16046741e-09 -1.44722939e-08 -2.25762828e-09]
     [-2.25762828e-09 -1.44722939e-08 -1.16046741e-09]
     [-2.25860708e-09 -1.44669483e-08  2.25860708e-09]
     [-1.16046741e-09 -1.44722939e-08  2.25762828e-09]
     [-2.26430754e-09 -1.08989140e-08  2.26430754e-09]
     [-2.25762828e-09 -1.44722939e-08  1.16046741e-09]]




.. GENERATED FROM PYTHON SOURCE LINES 69-79

While it might seem preferable to work entirely within ``numpy``,
DPF runs outside of Python and potentially even on a
remote machine. Therefore, the transfer of unnecessary data between
the DPF instance and the Python client leads to inefficient
operations on large models. Instead, you should use DPF operators to
assemble the necessary data before recalling the data from DPF.

For example, if you want the maximum displacement for a given
result, use the min/max operator:


.. GENERATED FROM PYTHON SOURCE LINES 79-88

.. code-block:: Python

    min_max_op = dpf.operators.min_max.min_max(field)
    print(min_max_op.outputs.field_max().data)

    # Out of conveience, you can simply take the max of the field with:
    print(field.max().data)

    # The above yields a result identical to:
    print(np.max(field.data, axis=0))





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    [2.29356739e-09 0.00000000e+00 2.29356739e-09]
    [2.29356739e-09 0.00000000e+00 2.29356739e-09]
    [2.29356739e-09 0.00000000e+00 2.29356739e-09]




.. GENERATED FROM PYTHON SOURCE LINES 89-92

Note that the numpy array does not retain any information about the
field it describes. Using the DPF ``max`` operator of the field does
retain this information.

.. GENERATED FROM PYTHON SOURCE LINES 92-94

.. code-block:: Python

    max_field = field.max()
    print(max_field)




.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF displacement_1.s Field
      Location: Nodal
      Unit: m
      3 entities 
      Data:1 components and 3 elementary data 






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 0.032 seconds)


.. _sphx_glr_download_examples_00-basic_02-basic_field_containers.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: 02-basic_field_containers.ipynb <02-basic_field_containers.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: 02-basic_field_containers.py <02-basic_field_containers.py>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
