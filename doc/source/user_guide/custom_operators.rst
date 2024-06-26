.. _user_guide_custom_operators:

================
Custom operators
================
**自定义运算符**

在 Ansys 2023 R1 及更高版本中，您可以在 CPython 中创建自定义运算符。
创建自定义运算符包括以符合 DPF 的方式封装 Python 例程，这样就可以像访问 PyDPF-Core 中的 :class:`ansys.dpf.core.dpf_operator.Operator` 类或任何受支持的客户端 API 中的本地运算符一样访问它们。

由于支持自定义操作符，PyDPF-Core 成为了一种开发工具：

- **Accessibility:** 一个简单的脚本就能定义一个基本的运算符插件。

- **Componentization（组件化）:** 具有类似应用的操作符可归入 Python 插件包。

- **Easy distribution（易于分发）:** 标准 Python 工具可用于打包、上传和下载自定义操作符。

- **Dependency management（依赖管理）:** 可以在 Python 包中添加第三方 Python 模块。

- **Reusability（可复用性）:** 经过记录和打包的运算符可以在无数个工作流程中重复使用。

- **Remotable and parallel computing（分布式及并行计算）:** 本地 DPF 功能由自定义操作符继承。

创建自定义运算符的唯一前提是熟悉本地运算符。更多信息，请参阅 :ref:`ref_user_guide_operators` 。

Install module
--------------
**安装模块**

在完成 Ansys 统一安装后，您必须在 Ansys 安装程序的 Python 解释器中安装 ``ansys-dpf-core`` 模块。

#. 下载适用于您操作系统的安装脚本：

   - 对于 Windows，请下载 :download:`PowerShell script </user_guide/install_ansys_dpf_core_in_ansys.ps1>` 。
   - 对于 Linux，请下载  :download:`Shell script </user_guide/install_ansys_dpf_core_in_ansys.sh>` 。

#. 使用可选参数运行下载的脚本进行安装：

   - ``-awp_root`` ：Ansys 安装文件夹的根路径。例如，2023 R1 安装文件夹以 ``Ansys Inc/v231`` 结尾，默认环境变量为 ``AWP_ROOT231`` 。
   - ``-pip_args`` ：添加到 ``pip`` 命令的可选参数。例如，`-extra-index-url`` 或 ``-trusted-host`` 。

**卸载模块**

如果您想从 Ansys 安装中卸载 ``ansys-dpf-core`` 模块，可以这样做。

#. 下载适用于您操作系统的卸载脚本：

   - 对于 Windows，请下载 :download:`PowerShell script </user_guide/uninstall_ansys_dpf_core_in_ansys.ps1>` 。
   - 对于 Linux，请下载 :download:`Shell script </user_guide/uninstall_ansys_dpf_core_in_ansys.sh>` 。
  
#. 使用可选参数运行下载的脚本进行卸载：

   - ``-awp_root``：Ansys 安装文件夹的根路径。例如，2023 R1 安装文件夹以 ``Ansys Inc/v231`` 结尾，默认环境变量为 ``AWP_ROOT231`` 。


Create operators
----------------
**创建运算符**

您可以创建一个基本运算符插件，也可以创建一个包含多个运算符的插件包。

Basic operator plugin
~~~~~~~~~~~~~~~~~~~~~
**基础操作符插件**

要创建一个基本的操作符插件，您需要编写一个简单的 Python 脚本。
操作符实现源于 :class:`ansys.dpf.core.custom_operator.CustomOperatorBase` 类和对 :func:`ansys.dpf.core.custom_operator.record_operator` 方法的调用。

本示例脚本展示了如何创建基本的运算符插件：

.. literalinclude:: custom_operator_example.py


.. code-block::

        def load_operators(*args):
            record_operator(CustomOperator, *args)


在该类的各种属性中，您可以指定以下内容：

- 自定义操作符的名称
- 描述该操作符的工作
- Dictionary for each input and output pin, which includes the name, a list of supported types, a description,
  and whether it is optional and/or ellipsis (meaning that the specification is valid for pins going from pin
  number *x* to infinity)
- 操作符属性列表，包括在文档和代码生成中使用的名称以及操作符类别。可选的 ``license`` 属性允许定义运行操作符时需要检查的许可证。
  将其设置为 ``any_dpf_supported_increments`` 可允许 DPF 当前接受的任何许可证（参见 :ref:`here <target_too_ansys_license_increments_list>` ）

有关编写操作符插件的综合示例，请参阅 :ref:`python_operators` 。


Plug-in package with multiple operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**具有多个运算符的插件包**

要创建一个包含多个运算符或复杂例程的插件包，需要编写一个 Python 包。编写软件包而不是简单脚本的好处是：

- **Componentization（组件化）:** 您可以将代码分割成多个 Python 模块或文件。
- **Distribution（分发）:** 您可以使用标准 Python 工具上传和下载软件包。
- **Documentation（文档）:** 您可以在软件包中添加 README 文件、文档、测试和示例。

带有依赖项的插件包由包含必要文件的文件夹组成。假设插件包的名称是 ``custom_plugin`` 。以这个名称命名的文件夹至少需要包含四个文件：

- ``__init__.py``
- ``operators.py``
- ``operators_loader.py``
- ``common.py``

**__init__.py file**

``__init__.py`` 文件包含以下代码：

.. code-block::

    from operators_loader import load_operators


**operators.py file**

``operators.py`` 文件包含这样的代码：

.. literalinclude:: custom_operator_example.py


**operators_loader.py file**

``operators_loader.py`` 文件中包含如下代码：

.. code-block::

    from custom_plugin import operators
    from ansys.dpf.core.custom_operator import record_operator

    def load_operators(*args):
        record_operator(operators.CustomOperator, *args)


**common.py file**

``common.py`` 文件包含以类和函数形式存在的 Python 程序::

    # 在这里以类和函数的形式编写所需的 python 例程。


Third-party dependencies
^^^^^^^^^^^^^^^^^^^^^^^^
**第三方依赖项**

.. include:: custom_operators_deps.rst


我们再假设你的插件包的名字是 ``custom_plugin`` 。一个带有这个名字的文件夹将包含这些文件：

- ``__init__.py``
- ``operators.py``
- ``operators_loader.py``
- ``common.py``
- ``winx64.zip``
- ``linx64.zip``
- ``custom_plugin.xml``

**__init__.py file**

``__init__.py`` 文件包含以下代码::

    from operators_loader import load_operators


**operators.py file**

``operators.py`` 文件包含这样的代码：

.. literalinclude:: custom_operator_example.py


**operators_loader.py file**

``operators_loader.py`` 文件包含如下代码::

    from custom_plugin import operators
    from ansys.dpf.core.custom_operator import record_operator


    def load_operators(*args):
        record_operator(operators.CustomOperator, *args)


    def load_operators(*args):
                record_operator(operators.CustomOperator, *args)

**common.py file**

``common.py`` 文件包含了 Python 例程（以类和函数形式）::

    # 在这里以类和函数的形式编写所需的 python 例程。

**requirements.txt file**

``requirements.txt`` 文件中包含类似这样的代码：
    
.. literalinclude:: /examples_user_guide/08-python-operators/plugins/gltf_plugin/requirements.txt

适用于 Windows 和 Linux 的 ZIP 文件作为资产包含在内：
  
- ``winx64.zip``
- ``linx64.zip``


**custom_plugin.xml file**

``custom_plugin.xml`` 文件中包含类似以下内容的代码：
 
.. literalinclude:: custom_plugin.xml
   :language: xml


Use custom operators
--------------------
**使用自定义操作符**

创建自定义操作符后，可以使用 :func:`ansys.dpf.core.core.load_library` 方法加载它。
第一个参数是插件所在目录的路径。第二个参数是 ``py_`` 加上任何标识插件的名称。最后一个参数是记录运算符的函数名称。

对于单个脚本的插件，第二个参数应该是 ``py_`` 加上 Python 文件名：

.. code::

    dpf.load_library(
    r"path/to/plugins",
    "py_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin.py
    "load_operators")

对于插件包，第二个参数应为 ``py_`` 加上任何名称：

.. code::

    dpf.load_library(
    r"path/to/plugins/custom_plugin",
    "py_my_custom_plugin", #if the load_operators function is defined in path/to/plugins/custom_plugin/__init__.py
    "load_operators")

加载插件后，就可以实例化自定义操作符：

.. code::

    new_operator = dpf.Operator("custom_operator") # if "custom_operator" is what is returned by the ``name`` property

References
----------

更多信息，请参阅 **API reference** 中的 :ref:`ref_custom_operator` ，以及 **Examples** 中的 :ref:`python_operators` 。