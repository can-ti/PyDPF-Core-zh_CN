
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples\11-cyclic-symmetry\03-cyclic_multi_stage.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_examples_11-cyclic-symmetry_03-cyclic_multi_stage.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_11-cyclic-symmetry_03-cyclic_multi_stage.py:


.. _ref_multi_stage_cyclic:

Multi-stage cyclic symmetry example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to expand the mesh and results from a
multi-stage cyclic analysis.

.. GENERATED FROM PYTHON SOURCE LINES 12-15

.. code-block:: Python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples








.. GENERATED FROM PYTHON SOURCE LINES 16-17

Create the model and display the state of the result.

.. GENERATED FROM PYTHON SOURCE LINES 17-21

.. code-block:: Python

    cyc = examples.download_multi_stage_cyclic_result()
    model = dpf.Model(cyc)
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
         -  elastic_strain: ElementalNodal Strain
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region: 
      3595 nodes 
      1557 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 6 
    Cumulative     Frequency (Hz) LoadStep       Substep        Harmonic index  
    1              188.385357     1              1              0.000000        
    2              325.126418     1              2              0.000000        
    3              595.320548     1              3              0.000000        
    4              638.189511     1              4              0.000000        
    5              775.669703     1              5              0.000000        
    6              928.278013     1              6              0.000000        





.. GENERATED FROM PYTHON SOURCE LINES 22-29

Expand displacement results
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example expands displacement results, by default on all
nodes and the first time step. Note that the displacements are expanded using
the :func:`read_cyclic
<ansys.dpf.core.operators.mesh.mesh_provider.InputsMeshProvider.read_cyclic>`
property with 2 as an argument (1 would ignore the cyclic symmetry).

.. GENERATED FROM PYTHON SOURCE LINES 29-47

.. code-block:: Python


    # Create displacement cyclic operator
    u_cyc = model.results.displacement()
    u_cyc.inputs.read_cyclic(2)

    # expand the displacements and get a total deformation
    nrm = dpf.operators.math.norm_fc()
    nrm.inputs.connect(u_cyc.outputs)
    fields = nrm.outputs.fields_container()

    # # get the expanded mesh
    mesh_provider = model.metadata.mesh_provider
    mesh_provider.inputs.read_cyclic(2)
    mesh = mesh_provider.outputs.mesh()

    # # plot the expanded result on the expanded mesh
    mesh.plot(fields)




.. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_03-cyclic_multi_stage_001.png
   :alt: 03 cyclic multi stage
   :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_03-cyclic_multi_stage_001.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 48-50

Expand stresses at a given time step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 50-68

.. code-block:: Python


    # define stress expansion operator and request stresses at time set = 3
    s_cyc = model.results.stress()
    s_cyc.inputs.read_cyclic(2)
    s_cyc.inputs.time_scoping.connect([3])

    # request the results averaged on the nodes
    s_cyc.inputs.requested_location.connect(dpf.locations.nodal)

    # request equivalent von mises operator and connect it to stress
    # operator
    eqv = dpf.operators.invariant.von_mises_eqv_fc(s_cyc)

    # expand the results and get stress eqv
    fields = eqv.outputs.fields_container()

    # plot the expanded result on the expanded mesh
    mesh.plot(fields)



.. image-sg:: /examples/11-cyclic-symmetry/images/sphx_glr_03-cyclic_multi_stage_002.png
   :alt: 03 cyclic multi stage
   :srcset: /examples/11-cyclic-symmetry/images/sphx_glr_03-cyclic_multi_stage_002.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 0.983 seconds)


.. _sphx_glr_download_examples_11-cyclic-symmetry_03-cyclic_multi_stage.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: 03-cyclic_multi_stage.ipynb <03-cyclic_multi_stage.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: 03-cyclic_multi_stage.py <03-cyclic_multi_stage.py>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
