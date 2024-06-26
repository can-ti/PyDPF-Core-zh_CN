.. _ref_dpf_operators_reference:

=========
Operators
=========

DPF 运算符可用于操作和转换模拟数据。

从适用于 Ansys 2023 R2 及更高版本的 DPF Server 开始，
DPF 中操作符的许可逻辑取决于活动的 `ServerContext <https://dpf.docs.pyansys.com/api/ansys.dpf.core.server_context.html#servercontext>`_ 。

可用的上下文是 **Premium(高级)** 和 **Entry(入门级)**。受许可的操作符使用 ``license`` 属性在文档中标记为。
 ``license`` 属性为 **None** 的操作符不需要许可证签出。有关使用这两个上下文的详细信息，请参阅 :ref:`user_guide_server_context` 。单击下面访问操作符文档。

.. grid:: 1

   .. grid-item::
        .. card:: Operators
            :link-type: doc
            :link: operator_reference_load

            单击此处开始了解 DPF 中可用的 operator 。

            +++
            .. button-link:: OPEN
               :color: secondary
               :expand:
               :outline:
               :click-parent:              


.. note::

    对于 Ansys 2023 R1 及更早版本，上下文等同于 Premium，已加载所有 operator。
    具体到 DPF Server 2023.2.pre0，服务器上下文定义了加载和访问哪些 operator。
    使用 `PyDPF-Core 0.7 操作符文档 <https://dpf.docs.pyansys.com/version/0.7/operator_reference.html>`_ 了解更多。
    文档中的某些操作符可能不适用于特定的服务器版本。