.. _user_guide_plotting:

====
Plot
====

DPF-Core 有多种绘图方法，可直接从 Python 生成 Ansys 模型的 3D 图。
这些方法使用 VTK 并利用 `PyVista <https://github.com/pyvista/pyvista>`_ 库来简化绘图。
更多信息，请参阅 `PyVista 文档 <https://docs.pyvista.org>`_ 。


Plot the mesh from the ``Model`` object
---------------------------------------
**绘制 ``Model`` 对象中的网格**

:meth:`Model.plot() <ansys.dpf.core.model.Model.plot>` 方法会在加载模型后立即绘制模型的网格。

本例下载了一个简单的浮桥网格模型，并使用 :class:`ansys.dpf.core.model` 类加载它：

.. code-block:: python

    import ansys.dpf.core as dpf
    from ansys.dpf.core import examples
    filename = examples.download_pontoon()
    model = dpf.Model(filename)
    model.plot()

.. image:: ../images/plotting/pontoon.png

默认的绘图设置会显示网格边线。所有关键字参数的列表，请参阅 `plot <https://docs.pyvista.org/plotting/plotting.html?highlight=plot#pyvista.plot>`_ 。


Plot the meshed region
-----------------------
**绘制网格区域图**

:meth:`MeshedRegion.plot() <ansys.dpf.core.meshed_region.MeshedRegion.plot>` 方法会绘制网格区域。
如果网格区域是从模型的元数据生成的，生成的绘图与 :meth:`Model.plot() <ansys.dpf.core.model.Model.plot>` 方法生成的绘图相同。

.. code-block:: python

    mesh = model.metadata.meshed_region
    mesh.plot()

.. image:: ../images/plotting/pontoon.png

当字段作为第一个参数提供时，将使用这些值绘制 网格。

此示例提取了 X 方向的节点应变：

首先，提取 X 应变分量

.. code-block:: python

    strain = model.results.elastic_strain()
    fields = strain.outputs.fields_container()
    field = fields.select_component(0)[0]
    print(field)

.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    DPF elastic_strain_1.s0 Field
      Location: ElementalNodal
      Unit:
      8640 entities
      Data:1 components and 69120 elementary data


必须将该“单元节点应变”转换为“节点应变”才能绘制。

.. code-block::

    nodal_field = field.to_nodal()
    mesh.plot(nodal_field)

.. image:: ../images/plotting/pontoon_strain.png

.. note::

   仅支持具有 ``Nodal`` 和 ``Elemental`` 位置的字段。使用 :meth:`too_nodal <ansys.dpf.core.field.Field.to_nodal>` 运算符转换到 ``Nodal`` 位置，或使用 :class:`ansys.dpf.core.operators.averaging.nodal_too_elemental` 类转换到 ``Elemental`` 位置。
