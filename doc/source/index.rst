.. _ref_main_index:

==========
PyDPF-Core
==========

Ansys 数据处理框架 (DPF) 为数值模拟用户和工程师提供一个访问和转换模拟数据的工具箱。借助 DPF，您可以在模拟工作流程内对大量模拟数据执行复杂的前处理或后处理。

DPF 是一个独立的、与物理无关的工具，您可以将其插入许多应用程序中，用于数据输入和数据输出，包括可视化和结果绘图。下表显示了 DPF 支持的应用程序的详尽列表及其相关格式：

.. table:: Truth table for "not"
   :widths: auto
   :align: center

+--------------------+------------------------+----------------------------------+----------------------------------+
|     **Solver**     |    **File format**     |       **Server version**         |       **DPF examples**           |
+====================+========================+==================================+==================================+
|                    || .rst, .mode           || **1.0** and later               | :ref:`ref_basic_example`         |
|        MAPDL       || .rfrq, .rdsp          || (*Ansys 2021 R1*)               |                                  |
+--------------------+------------------------+----------------------------------+----------------------------------+
|       LS DYNA      |   .d3plot, .binout     || **4.0** and later               | :ref:`lsdyna_operators`          |
|                    |                        || (*Ansys 2022 R2*)               |                                  |
+--------------------+------------------------+----------------------------------+----------------------------------+
|                    || *CFF restart files*   ||                                 | :ref:`ref_fluids_model`          |
|                    || .cas/dat.h5           ||                                 +----------------------------------+
|                    |                        || **7.0** and later               | :ref:`ref_fluids_mesh`           |
|        Fluent      +------------------------+| (*Ansys 2024 R1 pre0*)          +----------------------------------+
|                    || *Project files*       |                                  | :ref:`ref_fluids_results`        |
|                    || .flprj                |                                  |                                  |
+--------------------+------------------------+----------------------------------+----------------------------------+
|                    || *CFF files*           ||                                 | :ref:`ref_fluids_model`          |
|                    || .cas/dat.cff          ||                                 +----------------------------------+
|                    |                        || **7.0** and later               | :ref:`ref_fluids_mesh`           |
|          CFX       +------------------------+| (*Ansys 2024 R1 pre0*)          +----------------------------------+
|                    || *Project files*       |                                  | :ref:`ref_fluids_results`        |
|                    || .flprj                |                                  |                                  |
+--------------------+------------------------+----------------------------------+----------------------------------+

可视化由 VTK 确保，并利用 `PyVista 工具 <https://docs.pyvista.org>`_ 。

您可以利用众多现成的 DPF 运算符来处理和转换此数据。您还可以将运算符串联在一起，以便创建简单或复杂的数据处理工作流，可用于重复评估或后续评估。

DPF 中的数据是基于与物理无关的数学量定义的，这些数学量以自给自足的实体（称为 **字段** ）进行描述。这使得 DPF 成为一个模块化的、易于使用的工具，具有广泛的功能。

.. image:: images/drawings/dpf-flow.png
  :width: 670
  :alt: DPF flow

``ansys.dpf.core`` 软件包为 DPF 提供了一个 Python 接口，该接口可在不离开 Python 环境的情况下，快速对各种 Ansys 文件格式和物理求解进行后处理。

Brief demo
~~~~~~~~~~
下面是如何打开由 MAPDL（或其他 ANSYS 求解器）产生的结果文件并提取结果：

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    model = Model(examples.find_simple_bar())
    print(model)


以下是绘制位移结果的方法：

.. code-block:: python

    disp = model.results.displacement().X()
    model.metadata.meshed_region.plot(disp.outputs.fields_container())

有关如何使用 PyDPF-Core 的综合示例，请参见 :ref:`gallery` 。


Key features
~~~~~~~~~~~~

**计算效率**

DPF 是基于新型硬件架构的现代化框架。得益于持续发展，新功能会频繁增加。

**通用接口**

DPF 与物理无关，这意味着它的使用不局限于特定领域、物理求解或文件格式。

**可扩展性和定制性**

DPF 是围绕两个核心实体而开发的：

- 以 **field** 表示的数据
- 针对该数据执行操作的 **operator**

每一个 DPF 功能都是通过允许框架组件化的 operators 来开发的。由于 DPF 是基于插件的，因此可以轻松添加新功能或新格式。

Accessing and enriching DPF capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

绝大多数 DPF 功能都可以使用 operator 访问。有关更多信息，请参见 :ref:`ref_dpf_operators_reference` 。

DPF 还遵循 :ref:`ref_licensing` 中详述的许可策略。

以下各节为摘要。更多信息，请参阅 :ref:`user_guide_waysofusing` 。

**访问 DPF 服务器文件**

当 DPF 服务器文件可用时，可访问 DPF 功能。可使用 **Ansys installer** 和 **DPF Server** 访问这些文件。

- 要使用  **Ansys installer**，请使用首选分发渠道下载标准  **Ansys installer**，并按照安装程序说明安装 Ansys。有关获取 Ansys 授权副本的信息，请访问 `Ansys 网站 <https://www.ansys.com/>`_ 。

- DPF 服务器软件包独立于 Ansys 安装程序。有关详细信息，请参阅 :ref:`ref_dpf_server` 。

**使用脚本访问功能**

- C++ 文档:

  - 在 Ansys Developer 门户网站的 `开发人员文档 <https://developer.ansys.com/docs>`_ 页面上，请参阅 **数据处理框架 (DPF)** 。

- PyDPF 文档:

  - `PyDPF-Core documentation <https://dpf.docs.pyansys.com/version/stable/>`_

  - `PyDPF-Post documentation <https://post.docs.pyansys.com/version/stable/>`_

- Mechanical scripting (IronPython):

  - `Data Processing Framework <https://ansyshelp.ansys.com/account/secured?returnurl=/Views/Secured/corp/v232/en/act_script/mech_apis_data_process_frame.html>`_
    in the *Scripting in Mechanical Guide*.
  
  - `Python Result <https://ansyshelp.ansys.com/account/secured?returnurl=/Views/Secured/corp/v231/en/wb_sim/ds_python_result.html>`_
    in the *Mechanical User's Guide*.

**增强 DPF 功能**

- `User guide <https://developer.ansys.com/product/DPF-C-Client-Library-2023-R2/modules.xhtml>`_ in the *DPF C++ Client Library*

- :ref:`user_guide_custom_operators` in the PyDPF-Core documentation 

- `How to write a new solver reader as a DPF plugin <https://astonishing-hyacinth-e64.notion.site/How-to-write-a-new-solver-reader-as-a-DPF-s-plugin-bd2d2a3cf51f47ef9e70df45d64f89cb>`_


Documentation and issues
------------------------
最新稳定发行版的 PyDPF-Core 文档托管在 `PyDPF-Core 文档 <https://dpf.docs.pyansys.com/version/stable/>`_ 中。

在文档标题栏的右上角，可以选择从查看最新稳定版文档切换到查看开发版本或以前发布版本的文档。

你也可以 `查看 <https://cheatsheets.docs.pyansys.com/pydpf-core_cheat_sheet.png>`_ 或 `下载 <https://cheatsheets.docs.pyansys.com/pydpf-core_cheat_sheet.pdf>`_ PyDPF-Core cheatsheets。
这一页参考资料提供了使用 PyDPF-Core 的语法规则和命令。

在 `PyDPF-Core Issues <https://github.com/ansys/pydpf-core/issues>`_ 页面，您可以创建问题来报告错误和申请新功能。
在 `PyDPF-Core Discussions <https://github.com/ansys/pydpf-core/discussions>`_ 页面或 Ansys Developer 门户网站上的 `Discussions <https://discuss.ansys.com/>`_ 页面，您可以发布问题、分享想法并获得社区反馈。

如需联系项目支持团队，请发送电子邮件至 `pyansys.core@ansys.com <pyansys.core@ansys.com>`_ 。


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting_started/index
   user_guide/index
   examples/index
   api/index
   operator_reference
   concepts/index
   contributing
