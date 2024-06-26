.. _ref_getting_started:

===============
Getting started
===============

数据处理框架（DPF）为数值模拟用户和工程师提供了访问和转换模拟数据的工具箱。DPF 可以访问来自 Ansys 求解器结果文件以及多个中性文件（参见 :ref:`ref_main_index` ）的数据。

这个基于 **workflow-based** 框架可让您对大量仿真数据执行复杂的预处理和后处理操作。

PyDPF-Core 是一个 Python 客户端 API ，可通过网络使用 gRPC 或直接在同一进程中与 **DPF服务器** 通信。


Install DPF Server
------------------

要使用 PyDPF-Core，您需要访问 DPF 服务器。

* 在 Ansys 2021 R1 及更高版本中，DPF 服务器打包在 **Ansys 安装程序** 中。要使用它，请使用您首选的分发渠道下载标准安装程序，然后按照安装程序说明安装 Ansys。
  有关获取 Ansys 许可副本的信息，请访问 `Ansys 网站 <https://www.ansys.com/>`_ 。

* DPF 服务器预览版也可以作为 **standalone（独立）** 包（独立于 Ansys 安装程序）在 Ansys Customer Portal 的 `DPF Pre-Release page <https://download.ansys.com/Others/DPF%20Pre-Release>`_ 上提供。
  如 :ref:`ref_licensing` 中所述，单机版 DPF 服务器仍受 Ansys 许可机制的保护，需要接受 :ref:`DPF 预览版许可协议<target_to_license_terms>`。
  获得 Ansys 许可证后，请按照 :ref:`install a standalone DPF Server <target_installing_server>` 的指南进行操作。

有关安装、管理和运行 DPF 服务器的更多信息，请参阅 :ref:`ref_dpf_server` 。

Install PyDPF-Core
------------------

要在 Python 环境中安装 PyDPF-Core，请运行此命令：

.. code::

   pip install ansys-dpf-core

请务必查看 :ref:`compatibility guidelines <ref_compatibility>` ，以了解您的 DPF 服务器版本是否与最新版本的 PyDPF-Core 兼容。

有关更多安装选项，请参阅 :ref:`Installation section <installation>` 。


Use PyDPF-Core
--------------

要使用 PyDPF-Core，请在相同的 Python 环境中运行此命令：

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    model = dpf.Model(examples.download_crankshaft())
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
         -  velocity: Nodal Velocity
         -  acceleration: Nodal Acceleration
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
      69762 nodes
      39315 elements
      Unit: m
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support:
      Number of sets: 3
    Cumulative     Time (s)       LoadStep       Substep
    1              1.000000       1              1
    2              2.000000       1              2
    3              3.000000       1              3



.. code-block:: python

    over_time_disp = model.results.displacement().eval()
    over_time_disp[0].plot()


.. figure:: ../images/plotting/crankshaft_disp.png


.. toctree::
   :hidden:

   install
   dpf_server
   compatibility
   licensing
   dependencies

