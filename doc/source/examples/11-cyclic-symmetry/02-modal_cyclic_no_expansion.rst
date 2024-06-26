
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples\11-cyclic-symmetry\02-modal_cyclic_no_expansion.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_examples_11-cyclic-symmetry_02-modal_cyclic_no_expansion.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_11-cyclic-symmetry_02-modal_cyclic_no_expansion.py:


.. _ref_basic_cyclic:

Get base and duplicate sectors (real and imaginary) results for modal cyclic symmetry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to extract results from a modal cyclic symmetry model.

.. GENERATED FROM PYTHON SOURCE LINES 11-15

.. code-block:: Python


    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples








.. GENERATED FROM PYTHON SOURCE LINES 16-17

Create the model and display the state of the result.

.. GENERATED FROM PYTHON SOURCE LINES 17-20

.. code-block:: Python

    model = dpf.Model(examples.find_simple_cyclic())
    print(model)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF Model
    ------------------------------
    Modal analysis
    Unit system: MKS: m, kg, N, s, V, A, degC
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  stress: ElementalNodal Stress 
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region: 
      51 nodes 
      4 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 30 
    Cumulative     Frequency (Hz) LoadStep       Substep        Harmonic index  
    1              670386.325235  1              1              0.000000        
    2              872361.424038  1              2              0.000000        
    3              1142526.525324 1              3              0.000000        
    4              1252446.741551 1              4              0.000000        
    5              1257379.552140 1              5              0.000000        
    6              1347919.358013 1              6              0.000000        
    7              679667.393214  2              1              1.000000        
    8              679667.393214  2              2              -1.000000       
    9              899321.218481  2              3              -1.000000       
    10             899321.218481  2              4              1.000000        
    11             1128387.049511 2              5              1.000000        
    12             1128387.049511 2              6              -1.000000       
    13             708505.071361  3              1              -2.000000       
    14             708505.071361  3              2              2.000000        
    15             966346.820117  3              3              2.000000        
    16             966346.820117  3              4              -2.000000       
    17             1031249.070606 3              5              -2.000000       
    18             1031249.070606 3              6              2.000000        
    19             757366.624982  4              1              -3.000000       
    20             757366.624982  4              2              3.000000        
    21             926631.623058  4              3              -3.000000       
    22             926631.623058  4              4              3.000000        
    23             1035144.649248 4              5              3.000000        
    24             1035144.649248 4              6              -3.000000       
    25             807882.379030  5              1              4.000000        
    26             856868.410638  5              2              4.000000        
    27             1063247.283632 5              3              4.000000        
    28             1185511.741334 5              4              4.000000        
    29             1278969.844256 5              5              4.000000        
    30             1355579.879820 5              6              4.000000        





.. GENERATED FROM PYTHON SOURCE LINES 21-25

Get base and duplicate sectors displacement results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By default, the result providers (stress, displacement, and so on) will return results for
base and duplicate sectors for a cyclic symmetry model.

.. GENERATED FROM PYTHON SOURCE LINES 25-30

.. code-block:: Python


    # Create displacement operator
    u_cyc = model.results.displacement.on_all_time_freqs()
    fields = u_cyc.outputs.fields_container()








.. GENERATED FROM PYTHON SOURCE LINES 31-38

The output fields container print displays the organization of the different
fields in the container. The label "base_sector" gives access to base sectors
results with base_sector=1 and duplicate sector with base_sector=0 for all
modes.
The print also displays that there is no duplicate sectors for the first 6 modes.
Indeed, modes with harmonic index 0 have 0.0 displacement, stresses... on
duplicate sectors.

.. GENERATED FROM PYTHON SOURCE LINES 38-51

.. code-block:: Python


    print(fields)
    print(model.metadata.time_freq_support)

    # plot mode 7 base sector (real) result
    mode_7_base = fields.get_field({"base_sector": 1, "time": 7})
    model.metadata.meshed_region.plot(mode_7_base)

    # plot mode 7 duplicate sector (imaginary) result
    mode_7_duplicate = fields.get_field({"base_sector": 0, "time": 7})
    model.metadata.meshed_region.plot(mode_7_duplicate)





.. rst-class:: sphx-glr-horizontal


    *

      .. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_001.png
          :alt: 02 modal cyclic no expansion
          :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_001.png
          :class: sphx-glr-multi-img

    *

      .. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_002.png
          :alt: 02 modal cyclic no expansion
          :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_002.png
          :class: sphx-glr-multi-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF displacement(s)Fields Container
      with 48 field(s)
      defined on labels: base_sector time 

      with:
      - field 0 {base_sector:  1, time:  1} with Nodal location, 3 components and 51 entities.
      - field 1 {base_sector:  1, time:  2} with Nodal location, 3 components and 51 entities.
      - field 2 {base_sector:  1, time:  3} with Nodal location, 3 components and 51 entities.
      - field 3 {base_sector:  1, time:  4} with Nodal location, 3 components and 51 entities.
      - field 4 {base_sector:  1, time:  5} with Nodal location, 3 components and 51 entities.
      - field 5 {base_sector:  1, time:  6} with Nodal location, 3 components and 51 entities.
      - field 6 {base_sector:  1, time:  7} with Nodal location, 3 components and 51 entities.
      - field 7 {base_sector:  1, time:  8} with Nodal location, 3 components and 51 entities.
      - field 8 {base_sector:  1, time:  9} with Nodal location, 3 components and 51 entities.
      - field 9 {base_sector:  1, time:  10} with Nodal location, 3 components and 51 entities.
      - field 10 {base_sector:  1, time:  11} with Nodal location, 3 components and 51 entities.
      - field 11 {base_sector:  1, time:  12} with Nodal location, 3 components and 51 entities.
      - field 12 {base_sector:  1, time:  13} with Nodal location, 3 components and 51 entities.
      - field 13 {base_sector:  1, time:  14} with Nodal location, 3 components and 51 entities.
      - field 14 {base_sector:  1, time:  15} with Nodal location, 3 components and 51 entities.
      - field 15 {base_sector:  1, time:  16} with Nodal location, 3 components and 51 entities.
      - field 16 {base_sector:  1, time:  17} with Nodal location, 3 components and 51 entities.
      - field 17 {base_sector:  1, time:  18} with Nodal location, 3 components and 51 entities.
      - field 18 {base_sector:  1, time:  19} with Nodal location, 3 components and 51 entities.
      - field 19 {base_sector:  1, time:  20} with Nodal location, 3 components and 51 entities.
      - field 20 {base_sector:  1, time:  21} with Nodal location, 3 components and 51 entities.
      - field 21 {base_sector:  1, time:  22} with Nodal location, 3 components and 51 entities.
      - field 22 {base_sector:  1, time:  23} with Nodal location, 3 components and 51 entities.
      - field 23 {base_sector:  1, time:  24} with Nodal location, 3 components and 51 entities.
      - field 24 {base_sector:  1, time:  25} with Nodal location, 3 components and 51 entities.
      - field 25 {base_sector:  1, time:  26} with Nodal location, 3 components and 51 entities.
      - field 26 {base_sector:  1, time:  27} with Nodal location, 3 components and 51 entities.
      - field 27 {base_sector:  1, time:  28} with Nodal location, 3 components and 51 entities.
      - field 28 {base_sector:  1, time:  29} with Nodal location, 3 components and 51 entities.
      - field 29 {base_sector:  1, time:  30} with Nodal location, 3 components and 51 entities.
      - field 30 {base_sector:  0, time:  7} with Nodal location, 3 components and 51 entities.
      - field 31 {base_sector:  0, time:  8} with Nodal location, 3 components and 51 entities.
      - field 32 {base_sector:  0, time:  9} with Nodal location, 3 components and 51 entities.
      - field 33 {base_sector:  0, time:  10} with Nodal location, 3 components and 51 entities.
      - field 34 {base_sector:  0, time:  11} with Nodal location, 3 components and 51 entities.
      - field 35 {base_sector:  0, time:  12} with Nodal location, 3 components and 51 entities.
      - field 36 {base_sector:  0, time:  13} with Nodal location, 3 components and 51 entities.
      - field 37 {base_sector:  0, time:  14} with Nodal location, 3 components and 51 entities.
      - field 38 {base_sector:  0, time:  15} with Nodal location, 3 components and 51 entities.
      - field 39 {base_sector:  0, time:  16} with Nodal location, 3 components and 51 entities.
      - field 40 {base_sector:  0, time:  17} with Nodal location, 3 components and 51 entities.
      - field 41 {base_sector:  0, time:  18} with Nodal location, 3 components and 51 entities.
      - field 42 {base_sector:  0, time:  19} with Nodal location, 3 components and 51 entities.
      - field 43 {base_sector:  0, time:  20} with Nodal location, 3 components and 51 entities.
      - field 44 {base_sector:  0, time:  21} with Nodal location, 3 components and 51 entities.
      - field 45 {base_sector:  0, time:  22} with Nodal location, 3 components and 51 entities.
      - field 46 {base_sector:  0, time:  23} with Nodal location, 3 components and 51 entities.
      - field 47 {base_sector:  0, time:  24} with Nodal location, 3 components and 51 entities.

    DPF  Time/Freq Support: 
      Number of sets: 30 
    Cumulative     Frequency (Hz) LoadStep       Substep        Harmonic index  
    1              670386.325235  1              1              0.000000        
    2              872361.424038  1              2              0.000000        
    3              1142526.525324 1              3              0.000000        
    4              1252446.741551 1              4              0.000000        
    5              1257379.552140 1              5              0.000000        
    6              1347919.358013 1              6              0.000000        
    7              679667.393214  2              1              1.000000        
    8              679667.393214  2              2              -1.000000       
    9              899321.218481  2              3              -1.000000       
    10             899321.218481  2              4              1.000000        
    11             1128387.049511 2              5              1.000000        
    12             1128387.049511 2              6              -1.000000       
    13             708505.071361  3              1              -2.000000       
    14             708505.071361  3              2              2.000000        
    15             966346.820117  3              3              2.000000        
    16             966346.820117  3              4              -2.000000       
    17             1031249.070606 3              5              -2.000000       
    18             1031249.070606 3              6              2.000000        
    19             757366.624982  4              1              -3.000000       
    20             757366.624982  4              2              3.000000        
    21             926631.623058  4              3              -3.000000       
    22             926631.623058  4              4              3.000000        
    23             1035144.649248 4              5              3.000000        
    24             1035144.649248 4              6              -3.000000       
    25             807882.379030  5              1              4.000000        
    26             856868.410638  5              2              4.000000        
    27             1063247.283632 5              3              4.000000        
    28             1185511.741334 5              4              4.000000        
    29             1278969.844256 5              5              4.000000        
    30             1355579.879820 5              6              4.000000        





.. GENERATED FROM PYTHON SOURCE LINES 52-57

Get displacement results on the first sector with a cyclic phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:class:`ansys.dpf.result.cyclic_expanded_displacement` gives access
to all cyclic expansion configuration. By default all sectors will be expanded.
The cyclic phase (in degree) can be changed with the phi argument.

.. GENERATED FROM PYTHON SOURCE LINES 57-85

.. code-block:: Python

    u_cyc = dpf.operators.result.cyclic_expanded_displacement(
        streams_container=model.metadata.streams_provider,
        sectors_to_expand=[0],
        time_scoping=[7],
        phi=0.0,
    )
    # # get the mesh expanded on the first sector for consistency between results and mesh
    mesh_provider = model.metadata.mesh_provider
    mesh_provider.inputs.read_cyclic(2)  # read_cyclic=2 allows to expand cyclic result
    mesh_provider.connect(18, [0])  # connect the sectors_to_expand
    mesh = mesh_provider.outputs.mesh()

    mode_7_base = u_cyc.outputs.fields_container()
    print(mode_7_base)
    mesh.plot(mode_7_base[0])

    # a phase phi=90° is equivalent to returning the duplicate sector results:
    u_cyc.inputs.phi(90.0)
    mode_7_duplicate = u_cyc.outputs.fields_container()
    print(mode_7_duplicate)
    mesh.plot(mode_7_duplicate[0])

    # with phi=45°
    u_cyc.inputs.phi(45.0)
    mode_7_45 = u_cyc.outputs.fields_container()
    print(mode_7_45)
    mesh.plot(mode_7_45[0])




.. rst-class:: sphx-glr-horizontal


    *

      .. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_003.png
          :alt: 02 modal cyclic no expansion
          :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_003.png
          :class: sphx-glr-multi-img

    *

      .. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_004.png
          :alt: 02 modal cyclic no expansion
          :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_004.png
          :class: sphx-glr-multi-img

    *

      .. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_005.png
          :alt: 02 modal cyclic no expansion
          :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_005.png
          :class: sphx-glr-multi-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with Nodal location, 3 components and 51 entities.

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with Nodal location, 3 components and 51 entities.

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with Nodal location, 3 components and 51 entities.





.. GENERATED FROM PYTHON SOURCE LINES 86-88

Get nodal stress results on the first sector with a cyclic phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 88-100

.. code-block:: Python

    s_cyc = dpf.operators.result.cyclic_expanded_stress(
        streams_container=model.metadata.streams_provider,
        sectors_to_expand=[0],
        time_scoping=[7],
        phi=45.0,
        requested_location=dpf.locations.nodal,
    )

    s_7_45 = s_cyc.outputs.fields_container()
    print(s_7_45)
    mesh.plot(s_7_45[0])




.. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_006.png
   :alt: 02 modal cyclic no expansion
   :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_006.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with Nodal location, 6 components and 51 entities.





.. GENERATED FROM PYTHON SOURCE LINES 101-104

Get elemental_nodal stress results on the first sector with a cyclic phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Elemental nodal is the default result location for stress and strain.

.. GENERATED FROM PYTHON SOURCE LINES 104-120

.. code-block:: Python

    s_cyc = dpf.operators.result.cyclic_expanded_stress(
        streams_container=model.metadata.streams_provider,
        sectors_to_expand=[0],
        time_scoping=[7],
        phi=45.0,
    )

    s_7_45 = s_cyc.outputs.fields_container()
    print(s_7_45)

    # To average the result for each element
    to_elemental = dpf.operators.averaging.to_elemental_fc(s_cyc)
    s_7_45 = to_elemental.outputs.fields_container()
    print(s_7_45)
    mesh.plot(s_7_45[0])




.. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_007.png
   :alt: 02 modal cyclic no expansion
   :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_007.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with ElementalNodal location, 6 components and 4 entities.

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  7} with Elemental location, 6 components and 4 entities.





.. GENERATED FROM PYTHON SOURCE LINES 121-123

Get nodal stress results expanded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 123-136

.. code-block:: Python


    s_cyc = dpf.operators.result.cyclic_expanded_stress(
        streams_container=model.metadata.streams_provider,
        time_scoping=[7],
        requested_location=dpf.locations.nodal,
    )

    mesh_provider = model.metadata.mesh_provider
    mesh_provider.inputs.read_cyclic(2)  # read_cyclic=2 allows to expand cyclic result
    mesh = mesh_provider.outputs.mesh()
    s = s_cyc.outputs.fields_container()

    mesh.plot(s[0])



.. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_008.png
   :alt: 02 modal cyclic no expansion
   :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_02-modal_cyclic_no_expansion_008.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 2.881 seconds)


.. _sphx_glr_download_examples_11-cyclic-symmetry_02-modal_cyclic_no_expansion.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: 02-modal_cyclic_no_expansion.ipynb <02-modal_cyclic_no_expansion.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: 02-modal_cyclic_no_expansion.py <02-modal_cyclic_no_expansion.py>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
