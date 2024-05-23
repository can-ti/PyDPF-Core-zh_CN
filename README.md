# DPF - Ansys Data Processing Framework

[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![Python](https://img.shields.io/pypi/pyversions/ansys-dpf-core?logo=pypi)](https://pypi.org/project/ansys-dpf-core/)
[![pypi](https://img.shields.io/pypi/v/ansys-dpf-core.svg?logo=python&logoColor=white)](https://pypi.org/project/ansys-dpf-core)
[![freq-PyDPF-Core](https://img.shields.io/github/commit-activity/m/ansys/pydpf-core)](https://github.com/ansys/pydpf-core)
[![GH-CI](https://github.com/ansys/pydpf-core/actions/workflows/ci.yml/badge.svg)](https://github.com/ansys/pydpf-core/actions/workflows/ci.yml)
[![docs](https://img.shields.io/website?down_color=lightgrey&down_message=invalid&label=documentation&up_color=brightgreen&up_message=up&url=https%3A%2F%2Fdpfdocs.pyansys.com%2F)](https://dpfdocs.pyansys.com)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pypidl](https://img.shields.io/pypi/dm/ansys-dpf-core.svg?label=PyPI%20downloads)](https://pypi.org/project/ansys-dpf-core/)
[![cov](https://codecov.io/gh/ansys/pydpf-core/branch/master/graph/badge.svg)](https://codecov.io/gh/ansys/pydpf-core)
[![codacy](https://app.codacy.com/project/badge/Grade/61b6a519aea64715ad1726b3955fcf98)](https://www.codacy.com/gh/ansys/pydpf-core/dashboard?utm_source=github.com&utm_medium=referral&utm_content=ansys/pydpf-core&utm_campaign=Badge_Grade)

Ansys数据处理框架（DPF）为数值模拟用户和工程师提供了一个访问和转换模拟数据的工具箱。使用DPF，可以对仿真工作流中的大量仿真数据执行复杂的前处理或后处理。

DPF 是一个独立的、与物理无关的工具，您可以将其插入许多应用程序，用于数据输入和数据输出，包括可视化和结果图。它可以从求解器结果文件和其他中性格式（如 CSV、HDF5 和 VTK 文件）中获取数据。

最新版本的 DPF 支持以下的 Ansys 求解器结果文件：

- Mechanical APDL (`.rst`, `.mode`, `.rfrq`, `.rdsp`)
- LS-DYNA (`.d3plot`, `.binout`)
- Fluent (`.cas/dat.h5`, `.flprj`)
- CFX (`.cad/dat.cff`, `.flprj`)

有关文件支持的更多信息，请参阅 PyDPF-Core 文档中的 [主页](https://dpf.docs.pyansys.com/version/stable/index.html)。

使用可用的多种 DPF 运算符，您可以操作和转换这些数据。您还可以将运算符串联起来，创建简单或复杂的数据处理工作流，以便在重复或未来的评估中重复使用。

DPF 中的数据是基于与物理无关的数学量定义的，这些数学量以自给自足的实体（称为**fields**）进行描述。这使得 DPF 成为一个模块化的、易于使用的工具，具有广泛的功能。

![DPF flow](PyDPF-Core-zh_CN/doc/source/images/drawings/dpf-flow.png "DPF flow")

``ansys.dpf.core`` 包向 DPF 提供 Python 接口，从而无需离开 Python 环境即可对各种 Ansys 文件格式和物理求解进行快速后处理。

## Documentation and issues

PyDPF-Core 最新稳定版的文档托管在 [PyDPF-Core documentation](https://dpf.docs.pyansys.com/version/stable/) 上。

在文档标题栏的右上角有一个选项，可以从查看最新稳定版本的文档切换到查看开发版本或以前发布版本的文档。

您还可以 [查看](https://cheatsheets.docs.pyansys.com/pydpf-core_cheat_sheet.png) 或 [下载](https://cheatsheets.docs.pyansys.com/pydpf-core_cheat_sheet.pdf) PyDPF-Core 小抄。这一页参考资料提供了使用 PyDPF-Core 的语法规则和命令。

在 [PyDPF-Core Issues](https://github.com/ansys/pydpf-core/issues) 页面上，您可以创建问题来报告错误和申请新功能。在 Ansys Developer 门户网站上的 [PyDPF-Core Discussions](https://github.com/ansys/pydpf-core/discussions) 页面或 [Discussions](https://discuss.ansys.com/) 页面，您可以发布问题、分享想法并获得社区反馈。

如需联系项目支持团队，请发送电子邮件至 [pyansys.core@ansys.com](mailto:pyansys.core@ansys.com)。

## Installation

PyDPF-Core 需要 DPF 可用。您可以安装兼容的 Ansys 版本，或者安装独立的 ``ansys-dpf-server`` 服务器软件包。更多信息，请参阅 PyDPF-Core 文档中的 [Getting Started with DPF Server](https://dpf.docs.pyansys.com/version/stable/user_guide/getting_started_with_dpf_server.html)。

关于 PyDPF-Core 与 Ansys 之间的兼容性，请参见 PyDPF-Core 文档中的 [兼容性](https://dpf.docs.pyansys.com/version/stable/getting_started/compatibility.html)。

要将 PyDPF-Core 与 ``ansys-dpf-server`` 服务器软件包或 Ansys 2022 R2 或更高版本配合使用，请使用此命令安装最新版本：

```con
   pip install ansys-dpf-core
```

要使用 PyDPF-Core 绘图功能，您需要安装了 `PyVista <https://pyvista.org/>`_ 。要安装 PyDPF-Core 及其可选的绘图功能，请使用此命令：

```con
   pip install ansys-dpf-core[plotting]
```

有关 PyDPF-Core 绘图功能的更多信息，请参见 PyDPF-Core 文档中的 [Plot](https://dpf.docs.pyansys.com/version/stable/user_guide/plotting.html)。

若要将 PyDPF-Core 与 Ansys 2022 R1 配合使用，请使用以下命令安装最新的兼容版本：

```con
   pip install ansys-dpf-core<0.10.0
```

要在 Ansys 2021 R2 中使用 PyDPF-Core，请使用此命令安装最新的兼容版本：

```con
   pip install ansys-grpc-dpf<0.4.0; pip install ansys-dpf-core<0.10.0
```

要在 Ansys 2021 R1 中使用 PyDPF-Core，请使用此命令安装最新的兼容版本：

```con
   pip install ansys-grpc-dpf<0.3.0; pip install ansys-dpf-core<0.3.0
```

### Brief demo

只要 DPF 可用，一旦开始使用 PyDPF-Core，DPF 服务器就会自动启动。

要打开结果文件并查看其中的内容，请使用以下代码：

```pycon
>>> from ansys.dpf import core as dpf
>>> from ansys.dpf.core import examples
>>> model = dpf.Model(examples.find_simple_bar())
>>> print(model)

    DPF Model
    ------------------------------
    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  element_nodal_forces: ElementalNodal Element nodal Forces
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
      3751 nodes 
      3000 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 1 
    Cumulative     Time (s)       LoadStep       Substep       
    1              1.000000       1              1             


```

使用以下命令读取结果：

```pycon
>>> result = model.results.displacement.eval()
```

然后，开始用这些代码连接 operators ：

```pycon
>>> from ansys.dpf.core import operators as ops
>>> norm = ops.math.norm(model.results.displacement())
```

### Starting the service

``ansys.dpf.core`` 库会在后台自动启动一个 DPF 服务本地实例并连接到该实例。如果您需要连接到现有的远程或本地 DPF 实例，请使用 ``connect_to_server`` 方法：

```pycon
>>> from ansys.dpf import core as dpf
>>> dpf.connect_to_server(ip='10.0.0.22', port=50054)
```

一旦连接，该连接将在模块运行期间保持不变。退出 Python 或连接到其他服务器时，连接就会关闭。

## License and acknowledgments

PyDPF-Core 采用 MIT 许可。更多信息，请参阅 [LICENSE](https://github.com/ansys/pydpf-post/raw/master/LICENSE) 文件。

PyDPF-Core 对 Ansys 没有任何商业要求。该库通过向 DPF 添加 Python 接口扩展了 Ansys DPF 的功能，但不改变原始软件的核心行为或许可证。
