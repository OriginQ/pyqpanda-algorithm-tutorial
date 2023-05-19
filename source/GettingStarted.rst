Installation
=========================

.. _pyqpanda: https://pyqpanda-toturial.readthedocs.io/zh/latest/index.html
.. _`Microsoft Visual C++ Redistributable x64`: https://download.microsoft.com/download/0/5/6/056DCDA9-D667-4E27-8001-8A0C6971D6B1/vcredist_x64.exe
.. _`pyqpanda_algorithm`: https://originqc.com.cn/zh/quantum_soft.html?type=pyqpanda&lv2id=43&lv3id=221

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

License
==========================

Welcome to use the quantum software algorithm package pyqpanda-algorithm.
In order to ensure the complete function and the best user experience, we introduced the License certification system. On this page, we will explain to you in detail the importance of License and how to apply for a License.

**What is License?** 

License is an authorized mechanism that grants you the right to use our business software. 
It is a user-authorized software license, which aims to protect the legal use and intellectual property rights of the software.

**Why do we need livense?** 

License certification is to ensure the legitimate use of software and the protection of user equity. Through License certification, we can provide customized support, upgrades and maintenance, and ensure your software security.

**How to apply for License?** 

Before starting to use our quantum software algorithm pack Pyqpanda-Algorithm, you need to apply for an effective License. Please follow the steps below for application:
a. Visit our official website (website: `pyqpanda_algorithm`_).
b. In the quantum software column at the top, enter the quantum software algorithm package Pyqpanda-Algorithm page

    .. image:: images/origin_web.png

c. Click the application for trial, and then fill in the application form further, including your name, unit, contact information, and so on.
    .. image:: images/license.png

d. After submitting the application form, our team will approve your application as soon as possible.
e. Once your License application is approved, you will receive a confirmation email containing the License key.

**How to use License?** 

When calling any module of the Pyqpanda-Alg package, you will prompt to enter the livense, such as the following sample program:

    .. code-block:: python

        import numpy as np
        from pyqpanda_alg.QPCA.QPCA import qpca

        A = np.array([[-1, 2], [-2, -1], [-1, -2], [1, 3], [2, 1], [3, 2]])
        data_q = qpca(A, 1)
        print(data_q)

Type the license you obtained, after verification, you don't need to enter it again after the verification is passed.

    .. code-block:: python

        [root@localhost home]# python .\test_qcpa.py
        Please enter the license:

**License common question answers** 

If you encounter any problems in the process of applying or use, please visit the "Help and Support" page of our official website (https://originqc.com.cn/) to view common questions answers or contact our software development Support team.
Thank you for choosing to use our business software and abide by the License certification process. If you have any questions or need further assistance, please contact us at any time. We will provide you wholeheartedly and hope that you will enjoy the high -quality experience of our software!

