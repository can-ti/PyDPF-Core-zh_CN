.. _ref_dependencies:

============
Dependencies
============

Package dependencies
--------------------

**包依赖项**

安装 ``ansys-dpf-core`` 软件包时，会自动检查该软件包的依赖项。软件包依赖项包括

- `google-api-python-client <https://pypi.org/project/google-api-python-client/>`_
- `grpcio <https://pypi.org/project/grpcio/>`_
- `importlib-metadata <https://pypi.org/project/importlib-metadata/>`_
- `numpy <https://pypi.org/project/numpy/>`_
- `packaging <https://pypi.org/project/packaging/>`_
- `protobuf <https://pypi.org/project/protobuf/>`_
- `psutil <https://pypi.org/project/psutil/>`_
- `setuptools <https://pypi.org/project/setuptools/>`_
- `tqdm <https://pypi.org/project/tqdm/>`_

对于 ``ansys-dpf-core<0.10.0`` , ``ansys.dpf.gate`` , ``ansys.dpf.gatebin`` 和 ``ansys.grpc.dpf`` 模块不包括在内，它们是依赖项：

- `ansys.dpf.gate <https://pypi.org/project/ansys-dpf-gate/>`_ ，这是通往 DPF C API 或 Python gRPC API 的门户。该门户依赖于服务器配置：
- `ansys.grpc.dpf <https://pypi.org/project/ansys-grpc-dpf/>`_ 是从 protobuf 文件生成 gRPC 代码，是 ``ansys-dpf-gate`` 的依赖项。
- `ansys.dpf.gatebin <https://pypi.org/project/ansys-dpf-gatebin/>`_ 是特定于操作系统的二进制文件，包含 DPF C API，是 ``ansys-dpf-gate`` 的依赖项。


Optional dependencies
~~~~~~~~~~~~~~~~~~~~~

用于绘图，你可以安装这些可选的 Python 程序包：

- `matplotlib <https://pypi.org/project/matplotlib/>`_ package for chart plotting
- `pyvista <https://pypi.org/project/pyvista/>`_ package for 3D plotting
