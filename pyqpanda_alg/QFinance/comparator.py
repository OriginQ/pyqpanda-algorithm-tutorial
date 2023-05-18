import pyqpanda as pq
import numpy as np

from .. config import *
auth = Authorization()


def int_comparator(value, q_state, q_anc_cmp, function='geq', reuse=False):
    """
    This function provides comparators to compare basis states(can be superposition states)
    against a given classical integer.

    Parameters
        value : ``int``\n
            The given classical integer.
        q_state : ``Qubit``, ``QVec``\n
            State qubits.
        q_anc_cmp : ``QVec``\n
            Ancilla and comparison result qubits. The comparison result qubit should be the last element.
            The qubit number of this register should be equal to q_state.
        function : ``str{'geq', 'g', 'seq', 's'}``, optional\n
            Evaluate conditions:\n
            - ``geq`` : evaluate a ``>=`` condition. (Default)
            - ``g``   : evaluate a ``>`` condition.
            - ``seq`` : evaluate a ``<=`` condition.
            - ``s``   : evaluate a ``<`` condition.

        reuse : ``bool``\n
            Set to True to add a reverse circuit part to reuse ancilla qubits.

    Returns
        circuit : ``QCircuit``\n
            The result this function return is a quangtum circuit.
            The comparison result qubit would be in state  :math:`|1\\rangle` when the quantum state
            satisfies the comparison condition, otherwise  :math:`|0\\rangle`. Therefore we can get a
            probability outcome of the comparison.

    Examples
        An example of implementing a two-qubit uniform superposition state compared with 2.

        >>> from pyqpanda_alg.QFinance import comparator
        >>> import pyqpanda as pq
        >>> value = 2
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state = m.qAlloc_many(2)
        >>> q_anc_cmp = m.qAlloc_many(2)
        >>> prog = pq.QProg()
        >>> prog << pq.H(q_state)
        >>> cir = comparator.int_comparator(value, q_state, q_anc_cmp, function='g', reuse=True)
        >>> prog << cir
        >>> res = m.prob_run_dict(prog, [q_anc_cmp[-1]])
        >>> print(res)
        {'0': 0.7500000000000003, '1': 0.2500000000000001}

    """
    pass


def interpolation_comparator(value, q_state, q_anc_cmp, function='g', reuse=False):
    """
    This function provides comparators to compare basis states(generate from a smooth distribution)
    against a given classical number(can be float).
    This function introduces an interpolation method to make qubits "look" like a float number when compared,
    so that comparisons can be made in the real number domain. In detail, when sampling, we regard the
    quantum state ``a`` as the interval from ``inf:=a-0.5`` to ``sup:=a+1.5``. When comparing the quantum
    state with ``inf+delta``, the probability of smaller is delta.

    Parameters
        value : ``float``\n
            The given classical number.
        q_state : ``Qubit``, ``QVec``\n
            State qubits.
        q_anc_cmp : ``QVec``\n
            Ancilla and comparison result qubits. The comparison result qubit should be the last element.
            The qubit number of this register should be equal to q_state.
        function : ``str{'g', 's'}``, optional\n
            Evaluate conditions:\n
            - ``g`` : evaluate a ``>`` condition.(Default)
            - ``s`` : evaluate a ``<`` condition.

        reuse : ``bool``\n
            Set to True to add a reverse circuit part to reuse ancilla qubits.

    Returns
        circuit : ``QCircuit``\n
            The result this function return is a quangtum circuit.
            The comparison result qubit would be in state :math:`|1\\rangle` when the quantum state
            satisfies the comparison condition, otherwise :math:`|0\\rangle`. Therefore we can get a
            probability outcome of the comparison.

    Examples
        An example of implementing qubit state '110' compared with 3.3.

        >>> from pyqpanda_alg.QFinance import comparator
        >>> import pyqpanda as pq
        >>> value = 3.3
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state = m.qAlloc_many(3)
        >>> q_anc_cmp = m.qAlloc_many(3)
        >>> prog = pq.QProg()
        >>> prog << pq.X(q_state[:2])
        >>> cir = comparator.interpolation_comparator(value, q_state, q_anc_cmp, function='g', reuse=True)
        >>> prog << cir
        >>> res = m.prob_run_dict(prog, [q_anc_cmp[-1]])
        >>> print(res)
        {'0': 0.7999999999999997, '1': 0.20000000000000023}

    """
    pass


def qubit_comparator(q_state_1, q_state_2, q_anc_cmp, function='geq'):
    """
    This function provides comparators to compare between two basis states(can be superposition states).

    Parameters
        q_state_1 : ``Qubit``, ``QVec``\n
            The first state qubits.
        q_state_2 : ``Qubit``, ``QVec``\n
            The second state qubits.
        q_anc_cmp : ``QVec``\n
            Ancilla and comparison result qubits. The comparison result qubit should be the last element.
            The qubit number of this register should be equal to q_state.
        function : ``str{'geq', 'g', 'seq', 's', 'eq', 'neq'}``, optional\n
            Evaluate conditions:\n
            - ``geq`` : evaluate a ``>=`` condition. (Default)
            - ``g``   : evaluate a ``>`` condition.
            - ``seq`` : evaluate a ``<=`` condition.
            - ``s``   : evaluate a ``<`` condition.
            - ``eq``  : evaluate a ``==`` condition.
            - ``neq`` : evaluate a ``!=`` condition.
        reuse : bool\n
            Set to True to add a reverse circuit part to reuse ancilla qubits.

    Returns
        circuit : ``QCircuit``\n
            The result this function return is a quangtum circuit.
            The comparison result qubit would be in state :math:`|1\\rangle` when the quantum state
            satisfies the comparison condition, otherwise :math:`|0\\rangle`. Therefore we can get a
            probability outcome of the comparison.

    Examples
        An example of implementing a two-qubit uniform superposition state compared with qubit state '01'.

        >>> from pyqpanda_alg.QFinance import comparator
        >>> import pyqpanda as pq
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state_1 = m.qAlloc_many(2)
        >>> q_state_2 = m.qAlloc_many(2)
        >>> q_anc_cmp = m.qAlloc_many(2)
        >>> prog = pq.QProg()
        >>> prog << pq.H(q_state_1)
        >>> prog << pq.X(q_state_2[0])
        >>> cir = comparator.qubit_comparator(q_state_1, q_state_2, q_anc_cmp, function='g')
        >>> prog << cir
        >>> res = m.prob_run_dict(prog, [q_anc_cmp[-1]])
        >>> print(res)
        {'0': 0.5000000000000002, '1': 0.5000000000000002}

    """
    pass

def qft_comparator(value, q_state, q_cmp, function='geq'):
    """
    This function provides qft_based comparators to compare basis states(can be superposition states)
    against a given classical integer.

    Parameters
        value : ``int``\n
            The given classical integer in range [0,N).
        q_state : ``Qubit``, ``QVec``\n
            State qubits.
        q_cmp : ``QVec``\n
            The comparison result qubit.
        function : ``str{'geq', 'g', 'seq', 's'}``, optional\n
            Evaluate conditions:\n
            - ``geq`` : evaluate a ``>=`` condition. (Default)
            - ``g``   : evaluate a ``>`` condition.
            - ``seq`` : evaluate a ``<=`` condition.
            - ``s``   : evaluate a ``<`` condition.

    Returns
        circuit : ``QCircuit``\n
            The result this function return is a quangtum circuit.
            The comparison result qubit would be in state  :math:`|1\\rangle` when the quantum state
            satisfies the comparison condition, otherwise  :math:`|0\\rangle`. Therefore we can get a
            probability outcome of the comparison.

    Examples
        An example of implementing a two-qubit uniform superposition state compared with 2.

        >>> from pyqpanda_alg.QFinance import comparator
        >>> import pyqpanda as pq
        >>> value = 2
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state = m.qAlloc_many(2)
        >>> q_cmp = m.qAlloc()
        >>> prog = pq.QProg()
        >>> prog << pq.H(q_state)
        >>> cir = comparator.qft_comparator(value, q_state, q_cmp, function='g')
        >>> prog << cir
        >>> res = m.prob_run_dict(prog, [q_cmp])
        >>> print(res)
        {'0': 0.7500000000000003, '1': 0.2500000000000001}

    """
    pass


def qft_qubit_comparator(q_state_1, q_state_2, q_cmp, function='geq'):
    """
    This function provides qft_based comparators to compare between two basis states(can be superposition states).

    Parameters
        q_state_1 : ``Qubit``, ``QVec``\n
            The first state qubits.
        q_state_2 : ``Qubit``, ``QVec``\n
            The second state qubits.
        q_cmp : ``QVec``\n
            Comparison result qubit.
        function : ``str{'geq', 'g', 'seq', 's'}``, optional\n
            Evaluate conditions:\n
            - ``geq`` : evaluate a ``>=`` condition. (Default)
            - ``g``   : evaluate a ``>`` condition.
            - ``seq`` : evaluate a ``<=`` condition.
            - ``s``   : evaluate a ``<`` condition.

    Returns
        circuit : ``QCircuit``\n
            The result this function return is a quangtum circuit.
            The comparison result qubit would be in state :math:`|1\\rangle` when the quantum state
            satisfies the comparison condition, otherwise :math:`|0\\rangle`. Therefore we can get a
            probability outcome of the comparison.

    Examples
        An example of implementing a two-qubit uniform superposition state compared with qubit state '01'.

        >>> from pyqpanda_alg.QFinance import comparator
        >>> import pyqpanda as pq
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state_1 = m.qAlloc_many(2)
        >>> q_state_2 = m.qAlloc_many(2)
        >>> q_anc_cmp = m.qAlloc()
        >>> prog = pq.QProg()
        >>> prog << pq.H(q_state_1)
        >>> prog << pq.X(q_state_2[0])
        >>> cir = comparator.qft_qubit_comparator(q_state_1, q_state_2, q_cmp, function='g')
        >>> prog << cir
        >>> res = m.prob_run_dict(prog, [q_cmp])
        >>> print(res)
        {'0': 0.5000000000000002, '1': 0.5000000000000002}

    """
    pass
