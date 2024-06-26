.. _ref_user_guide_operators:

=========
Operators
=========

.. include:: <isonum.txt>

运算符是用于创建、转换和流式传输数据的主要对象。在 DPF 中，您可以使用运算符加载、操作和输出数据。

每个运算符都包含 ``input`` 和 ``output`` 属性，通过它们可以建立各种输入和输出连接。

在评估过程中，运算符根据其描述来处理输入，并计算出相应的输出。

.. figure:: ../images/drawings/operator_drawing.svg

您可以将一个运算符的输出附加到另一个运算符的输入，将运算符串联起来，从而创建工作流，进行简单或复杂的数据处理。通过 "懒惰评估"，DPF 可高效处理数据，仅在评估最终运算符和请求数据时才评估每个运算符。

例如，如果您想得到结果的最大归一化位移，可以按以下顺序构造运算符：

.. figure:: ../images/drawings/max_u_norm.png

本例展示了如何计算结果的最大归一化位移：

.. code-block:: default

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    norm = ops.math.norm(displacement)
    min_max = ops.min_max.min_max(norm)
    max_displacement = min_max.outputs.field_max()
 
 
这种方法完全在 DPF 服务中高效地计算出结果的最大位移，在 DPF 得出你想要的求解数据之前，不需要从 DPF 向 Python 传输任何数据。

DPF operator 可以自动获得许可证，这意味着它需要通过许可证检查才能运行。许可证类型可以是特定的，也可以是给定列表中的，并在运算符级别定义。
有关 DPF 许可逻辑的更多信息，请参阅 :ref:`user_guide_server_context` 。

DPF 运算符库非常庞大，包括文件阅读器和数学、几何及逻辑转换。有关该运算符库的更多信息，请参见 :ref:`ref_dpf_operators_reference` 。


Create operators
~~~~~~~~~~~~~~~~
**创建运算符**

每个运算符都属于 :ref:`ref_operator` 类型。您可以使用 :ref:`ansys.dpf.core.operators package` 中的任何派生类在 Python 中创建一个实例，
也可以使用指示运算符类型的内部名称字符串直接使用 :ref:`ref_operator` 类创建一个实例。更多信息，请参阅 :ref:`ref_dpf_operators_reference` 。

本例演示如何创建位移运算符：

.. code-block:: python

   from ansys.dpf.core import operators as ops
   op = ops.result.displacement() # or op = ansys.dpf.core.Operator("U")

您可以通过打印来查看该运算符的说明、可用输入和可用输出：

.. code-block:: python

    print(op)
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPF U Operator: 
      Read/compute nodal displacements by calling the readers defined by the datasources. 
      Inputs:
             time_scoping (optional) [scoping, int32, vector<int32>, double, field, vector<double>]: time/freq (use doubles or field), time/freq set ids (use ints or scoping) or time/freq step ids (use scoping with TimeFreq_steps location) required in output 
             mesh_scoping (optional) [scopings_container, scoping]: nodes or elements scoping required in output. The scoping's location indicates whether nodes or elements are asked. Using scopings container enables to split the result fields container in domains 
             fields_container (optional) [fields_container]: Fields container already allocated modified inplace 
             streams_container (optional) [streams_container]: result file container allowed to be kept open to cache data 
             data_sources [data_sources]: result file path container, used if no streams are set 
             bool_rotate_to_global (optional) [bool]: if true the field is rotated to global coordinate system (default true) 
             mesh (optional) [abstract_meshed_region, meshes_container]: prevents from reading the mesh in the result files 
             read_cyclic (optional) [enum dataProcessing::ECyclicReading, int32]: if 0 cyclic symmetry is ignored, if 1 cyclic sector is read, if 2 cyclic expansion is done, if 3 cyclic expansion is done and stages are merged (default is 1) 
      Outputs:
             fields_container [fields_container] 


或者，也可以使用 ``Model`` 对象实例化结果提供程序。更多信息，请参阅 :ref:`user_guide_model` 。

在使用该模型的结果时，结果的文件路径直接与运算符相连，这意味着您只能为您的结果文件实例化可用的结果：


.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()


Connect operators
~~~~~~~~~~~~~~~~~
**连接运算符**

位移运算符唯一需要的输入是 ``data_sources`` 输入（见上文）。要在包含置换结果的 ``fields_container`` 对象中计算输出，必须提供结果文件的路径。

您可以通过两种方式创建数据源：

- 使用 :ref:`ref_model` 类。
- 使用 :ref:`ref_data_sources` 类。


由于其他几个示例使用了 ``Model`` 类，因此本示例使用了 ``DataSources`` 类：

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   data_src = dpf.DataSources(examples.find_multishells_rst())
   print(data_src)
   

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
  DPF  DataSources: 
  Result files:
     result key: rst and path: path\...\ansys\dpf\core\examples\model_with_ns.rst
  Secondary files:

这段代码展示了如何将数据源连接到位移运算符：

.. code-block:: python

    op.inputs.data_sources(data_src)
    
您还可以将其他可选输入连接到位移运算符。打印运算符的输出显示，可以连接 :ref:`ref_scoping` 类型的 ``mesh_scoping`` 来处理空间子集。还可以连接一个整数列表的 ``time_scoping`` 来处理时间子集：


.. code-block:: python

    mesh_scoping = dpf.mesh_scoping_factory.nodal_scoping([1,2])
    op.inputs.mesh_scoping(mesh_scoping)
    op.inputs.time_scoping([1])
    
    
Evaluate operators
~~~~~~~~~~~~~~~~~~
**计算运算符**

分配了所有必需的输入后，您就可以从运算符输出 :class:`ansys.dpf.core.fields_container` 类：

.. code-block:: python

    fc = op.outputs.fields_container()
    print(fc)
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPF displacement(s)Fields Container
      with 1 field(s)
      defined on labels: time 
    
      with:
      - field 0 {time:  1} with Nodal location, 3 components and 2 entities.

运行时，运算符会检查是否已分配所有必需的输入。如果运算符的输入缺失，则会引发类似此例的 ``DPFServerException`` 异常：
    
.. code-block:: python

    new_oper = ops.result.displacement()
    fc = new_oper.outputs.fields_container()
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFServerException: U<-Data sources are not defined.

有关使用字段容器的更多信息，请参阅 :ref:`ref_user_guide_fields_container` 。


Chain operators
~~~~~~~~~~~~~~~
**链式运算符**

要创建更复杂的计算和可定制的结果，您可以将运算符串联起来创建工作流。使用庞大的 DPF 运算符库，您可以自定义结果以获得特定输出。

虽然在 Python 端手动定制结果的效率远低于使用运算符，但对于一个非常小的模型来说，在客户端引入所有位移数据来计算最大值是可以接受的：

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    fc = displacement.outputs.fields_container()

    # 使用 NumPy 计算第一个场的最大位移。
    # 请注意，返回的数据是一个 numpy 数组。

    disp = fc[0].data
    disp.max(axis=0)
    

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFArray([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])

但在工业模型上，您应该使用这样的代码：

.. code-block:: python

    from ansys.dpf.core import Model
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops
    model = Model(examples.find_simple_bar())
    displacement = model.results.displacement()
    min_max = ops.min_max.min_max(displacement)
    max_field = min_max.outputs.field_max()
    max_field.data
    

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
    DPFArray([8.20217171e-07, 6.26510654e-06, 0.00000000e+00])
    

在前面的示例中，只传输了 X、Y 和 Z 部分的最大位移，并以 numpy 数组的形式返回。

对于小数据集，可以在 `NumpPy <https://numpy.org/>`_ 中计算数组的最大值。
虽然有时可以为给定的结果类型获取整个数据数组，但很多时候并不需要这样做。
在这种情况下，更快的方法不是将数组传输到 Python，而是在 DPF 中计算字段容器的最大值，然后将结果返回给 Python。

此示例将运算符与其他运算符实例化：


.. code-block:: python

    min_max = ops.min_max.min_max(displacement)

这会自动连接匹配的 ``displacement`` 输出和匹配的 ``min_max`` 输入。
您也可以使用 :py:meth:`connect() <ansys.dpf.core.dpf_operator.Operator.connect>` 方法手动连接一个运算符的输出和另一个运算符的输入：

.. code-block:: python

    min_max = ops.min_max.min_max()
    min_max.inputs.connect(displacement.outputs)
    #or
    min_max.inputs.field.connect(displacement.outputs.fields_container)


尽管最后的方法比较冗长，但对于具有多个匹配输入或输出的运算符来说却很有用。


Types of operators
~~~~~~~~~~~~~~~~~~
**运算符的种类**

DPF 提供了三个主要类型的运算符：

- 用于导入或读取数据的运算符
- 用于转换数据的运算符
- 导出数据的运算符

***************************************
Operators for importing or reading data
***************************************
**用于导入或读取数据的运算符**

这些运算符可从求解器文件或标准文件类型读取数据，如 ``.RST`` (MAPDL)、 ``.D3Plot`` (LS DYNA)、 ``.CAS.H5/.DAT.H5`` (Fluent) 或 ``.CAS.CFF/.DAT.CFF`` (CFX)。

为了读取这些文件，不同的读取器被实现为插件。插件可以按需在任何 DPF 脚本语言中通过 “加载库” 的方法加载。由于DPF结果提供程序，文件读取器可以通用地使用，这意味着相同的运算符可以用于任何文件类型。

本例说明了如何读取任何文件的位移和应力：

.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   data_src = dpf.DataSources(examples.find_multishells_rst())
   disp = ops.result.displacement(data_sources = data_src)
   stress = ops.result.stress(data_sources = data_src)

还支持标准文件格式读取器来导入自定义数据。字段可从 CSV、VTK 和 HDF5 文件导入。

有关导入和导出 CSV 文件的示例，请参阅 :ref:`ref_basic_load_file_example` 。

*******************************
Operators for transforming data
*******************************
**用于转换数据的运算符**

字段是 DPF 中的主要数据容器。大多数转换数据的运算符都将字段或字段容器作为输入，并将转换后的字段或字段容器作为输出返回。您可以对模拟数据执行分析、平均或过滤操作。

例如，在创建完一个字段后，你可以使用缩放和筛选运算符：

.. code-block:: python

    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as ops
    
    field1 = dpf.Field(nentities=3)
    field1.data = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    field1.scoping.ids = [1,2,3]
    field1.unit = 'm'
    
    #example 1 analytic operator: scale operator
    op1 = ops.math.scale()
    op1.inputs.field.connect(field1)
    op1.inputs.ponderation.connect(2.0)
    out = op1.outputs.field()
    out.data
    
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     DPFArray([[ 2.,  4.,  6.],
          [ 8., 10., 12.],
          [14., 16., 18.]])


.. code-block:: python

    #example 2 filtering operator
    op2 = ops.filter.field_high_pass()
    op2.inputs.field.connect(field1)
    op2.inputs.threshold.connect(3.0)
    out = op2.outputs.field()
    out.data
    
.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     DPFArray([[4., 5., 6.],
          [7., 8., 9.]])
       
 
****************************
Operators for exporting data
****************************
**用于导出数据的运算符**

使用 DPF 读取或转换仿真数据后，您可能希望将结果以特定格式导出，以便在其他环境中使用或保存，供将来使用 DPF 时使用。支持导出的文件格式包括 VTK、H5、CSV 和 TXT（序列化运算符）。
导出运算符通常与导入运算符匹配，允许您重复使用数据。在 :ref:`ref_dpf_operators_reference` 中，**Entry** 和 **Premium** 部分都有一个 **Serialization** 类别，可显示可用的导入和导出运算符。


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   model = dpf.Model(examples.find_multishells_rst())
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path='c:/temp/file.vtk',
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   
本例演示了如果 Python 客户端与服务器不在同一台机器上，如何使用导入和导出运算符：


.. code-block:: python

   from ansys.dpf import core as dpf
   from ansys.dpf.core import examples
   from ansys.dpf.core import operators as ops
   server_dir = dpf.make_tmp_dir_server()
   print(server_dir)
   up_loaded_file = dpf.upload_file_in_tmp_folder(examples.find_multishells_rst())
   model = dpf.Model(up_loaded_file)
   disp = model.results.displacement()
   vtk = ops.serialization.vtk_export(file_path=server_dir+"\\file.vtk",
       mesh=model.metadata.meshed_region, fields1=disp)
   vtk.run()
   dpf.download_file(server_dir+"\\file.vtk",r"c:/temp/file_downloaded.vtk")
   

.. rst-class:: sphx-glr-script-out

 .. code-block:: none
 
     C:\Users\user_name\AppData\Local\Temp\dataProcessingTemp17168
     Downloading...: 759 KB|
 

API reference
~~~~~~~~~~~~~

有关 DPF 中所有运算符的列表，请参阅 :ref:`ref_dpf_operators_reference` 或软件包 :ref:`ansys.dpf.core.operators package` 。有关类本身的更多信息，请参阅 :ref:`ref_operator` 。
