# Copyright (c) 2017-2022 Origin Quantum Computing. All Right Reserved.

import pyqpanda.pyQPanda as pq
import numpy as np
from numpy import pi
from . import grover
from typing import Union, List

from .. config import *
auth = Authorization()

class QAE:
    """
    This class provides a framework for original Quantum Amplitude Estimation(QAE) algorithm [1].

    Parameters
        operator_in : callable ``f(qubits)``\n
            Operator/Circuit of the estimated qubits state.
        qnumber : ``int``\n
            The number of all qubits used in circuit.
        res_index : ``int``, ``list``\n
            The index of the estimated qubit(s).
        epsilon : ``float``\n
            Estimated precision, i.e. the minimum error.
        target_state : ``str``\n
            Estimated target state.


    References
        [1] Brassard G, Hoyer P, Mosca M, et al. Quantum amplitude amplification and estimation[J].
        Contemporary Mathematics, 2002, 305: 53-74.

    """
    def __init__(self, operator_in=None,
                 qnumber: int = 0,
                 res_index: Union[int, List[int]] = -1,
                 epsilon: float = 1e-3,
                 target_state: str = '1'
                 ):
        pass

    def __del__(self):
        pass

    def run(self):
        """
        Run the quantum amplitude estimation algorithm.

        Returns
            prob : ``float``\n
                A probability value as the amplitude estimation result.

        Examples
            An example for implementing an amplitude estimation for target state '11' of the following circuit.
        
        .. parsed-literal::
                      ┌────────────┐
            q_0:  |0>─┤RY(1.047198)├ ─■─
                      └────────────┘ ┌┴┐
            q_1:  |0>─────────────── ┤X├
                                     └─┘

        >>> import pyqpanda as pq
        >>> from pyqpanda_alg.QFinance import QAE
        >>> import numpy as np
        >>> def create_cir(qlist):
        >>>     cir = pq.QCircuit()
        >>>     cir << pq.RY(qlist[0], np.pi / 3) << pq.X(qlist[1]).control(qlist[0])
        >>>     return cir
        >>> W = QAE.QAE(operator_in=create_cir, qnumber=2, epsilon=0.01, res_index=[0, 1], target_state='11').run()
        >>> print(W)
        0.24294862790338914

        """
        pass

class IQAE:
    """
    This class provides a framework for Iterative Quantum Amplitude Estimation(IQAE) algorithm [2].
    Estimated target state is  :math:`|1\\rangle`.

    Parameters
        operator_in : callable ``f(qubits)``\n
            Operator/Circuit of the estimated qubits state.\n
        qnumber : ``int``\n
            The number of all qubits used in circuit.\n
        res_index : ``int``\n
            The index of the estimated qubit.\n
        epsilon : ``float``\n
            Estimated precision, i.e. the minimum error.\n


    References
        [2] Grinko, D., Gacon, J., Zoufal, C. et al. Iterative quantum amplitude estimation.
        npj Quantum Inf 7, 52 (2021). https://doi.org/10.1038/s41534-021-00379-1

    """
    def __init__(self, operator_in=None,
                 qnumber: int = 0,
                 res_index: int = -1,
                 epsilon: float = 1e-3
                 ):
        pass

    def __del__(self):
        pass

    def run(self):
        """
        Run the iterative quantum amplitude estimation algorithm.

        Returns
            prob : ``float``\n
                A probability value as the iterative amplitude estimation result.

        Examples
            An example for implementing an iterative amplitude estimation for qubit q_1 of the following circuit.
        
        .. parsed-literal::
                      ┌────────────┐
            q_0:  |0>─┤RY(1.047198)├ ─■─
                      └────────────┘ ┌┴┐
            q_1:  |0>─────────────── ┤X├
                                     └─┘

        >>> import pyqpanda as pq
        >>> from pyqpanda_alg.QFinance import QAE
        >>> import numpy as np
        >>> def create_cir(qlist):
        >>>     cir = pq.QCircuit()
        >>>     cir << pq.RY(qlist[0], np.pi / 3) << pq.X(qlist[1]).control(qlist[0])
        >>>     return cir
        >>> W = QAE.IQAE(operator_in=create_cir, qnumber=2, epsilon=0.01, res_index=-1).run()
        >>> print(W)
        0.2447260561465428

        """
        pass
