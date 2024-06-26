要将第三方模块作为依赖项添加到插件包中，应在插件包文件夹旁边的 XML 文件中创建并引用一个文件夹或 ZIP 文件，其中包含依赖项的站点。
XML 文件的名称必须与插件包相同，并加上 ``.xml`` 的扩展名。

当调用 :py:func:`ansys.dpf.core.core.load_library` 方法时，PyDPF-Core 会使用 ``site`` Python 模块将自定义站点添加到 Python 解释器的路径中。


要创建这些自定义站点，请执行以下操作：

#. 在 Python 虚拟环境中安装插件包的 requirements。
#. 删除站点软件包中不必要的文件夹，并将其压缩为 ZIP 文件。
#. 将 ZIP 文件放入插件包。
#. 如上所述，在 XML 文件中引用 ZIP 文件的路径。

为了简化这一步骤，可以在插件包中添加一个 requirements 文件：

.. literalinclude:: /examples_user_guide/08-python-operators/plugins/gltf_plugin/requirements.txt


对于这种方法，请执行以下操作：

#. 为您的操作系统下载对应的脚本：

   - For Windows, download this :download:`PowerShell script </user_guide/create_sites_for_python_operators.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/create_sites_for_python_operators.sh>`.
  
#. 使用必选参数运行下载的脚本：

   - ``-pluginpath``: 包含插件包的文件夹路径。
   - ``-zippath``: ZIP 文件的路径和名称。
   
   可选参数包括：

   - ``-pythonexe``: 您选择的 Python 可执行文件的路径。
   - ``-tempfolder``: 临时文件夹的路径。Windows 下默认为环境变量 ``TEMP``，Linux 下默认为 ``/tmp/`` 。

#. 在你的操作系统中执行命令：

   - 在 Windows PowerShell，运行：

     .. code-block::
   
        create_sites_for_python_operators.ps1 -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/winx64.zip

   - 在 Linux Shell 中，运行：

     .. code-block::

        create_sites_for_python_operators.sh -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/linx64.zip

