Installation
=========================

.. _pyqpanda: https://pyqpanda-toturial.readthedocs.io/zh/latest/index.html
.. _`Microsoft Visual C++ Redistributable x64`: https://download.microsoft.com/download/0/5/6/056DCDA9-D667-4E27-8001-8A0C6971D6B1/vcredist_x64.exe
.. _`Origin Quantum``  http://10.10.10.57/zh/quantum_soft.html?type=pyqpanda&lv2id=43&lv3id=221

pyqpanda_alg is an algorithm expansion module based on ``pyqpanda`` . 
It contains many practical quantum application algorithms. Installation and use need to rely on ``pyqpanda`` . For the interface usage of ``pyqpanda`` , please refer to pyqpanda_

Configuration
>>>>>>>>>>>>>>>>>>>

pyqpanda_alg uses C++ as the host language, and its environmental requirements for the system are as follows:

Windows
---------------------
.. list-table::

    * - software
      - version
    * - `Microsoft Visual C++ Redistributable x64`_ 
      - 2013 
    * - Python
      - >= 3.7 && <= 3.9

Linux
---------------------

.. list-table::

    * - software
      - version
    * - GCC
      - >= 5.4.0 
    * - Python
      - >= 3.7 && <= 3.9


Install
>>>>>>>>>>>>>>>>>

If you have already installed the python environment and the pip tool, enter the following command in the terminal or console:

    .. code-block:: python

        pip install pyqpanda_alg

.. note:: If you encounter permission problems under linux, you need to add ``sudo``




