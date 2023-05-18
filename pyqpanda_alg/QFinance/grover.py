import pyqpanda as pq
import numpy as np

from .. config import *
auth = Authorization()

class Grover:
    """ This class provides a framework for Grover Search algorithm [1].

    Parameters
        in_operator : callable ``f(qubits)``\n
            Operator/Circuit of the initial search state for the algorithm, default Hadamards.
        flip_operator : callable ``f(qubits)``\n
            Operator/Circuit of marking the good states by phase-flip. Default doing a pauli-Z
            gate at the last qubit.
        zero_flip : callable ``f(qubits)``\n
            Operator/Circuit of reflects 0s by phase-flip. Default doing a zero-controled pauli-Z
            gate on qubits.
        mark_data : ``str``, ``list[str]``\n
            Marked target state. Default None.
            Only used when simply marking a known query state, as the designed flip_operator part.
        amplify_operator : callable ``f(qubits)``\n
            Constructed complete Grover amplitude amplification operator circuit. Default None.
            For users' special designed amplitude amplification operator.

    References
        [1] L. K. Grover, A fast quantum mechanical algorithm for database search. Proceedings
        28th Annual Symposium on the Theory of Computing (STOC) 1996, pp. 212-219.
        https://arxiv.org/abs/quant-ph/9605043

    """
    def __init__(self,
                 in_operator=None,
                 flip_operator=None,
                 zero_flip=None,
                 mark_data=None,
                 amplify_operator=None):
        pass

    def cir(self, q_input=None, q_flip=None, q_zero=None, iternum: int = 1):
        """
        Get full circuit of Grover search.

        Parameters
            q_input : ``QVec``\n
                Target qubit(s) for in_operator (initial preparation circuit).
                Using Hadamard gates to create the uniform superposition at the beginning most of time.
                Although in most simple cases it includes the full workspace qubits,
                auxiliary qubits can be excluded when dealing with some complex problems.
            q_flip : ``QVec``\n
                Target qubit(s) for flip_operator.
            q_zero : ``QVec``\n
                Target qubit(s) for zero_flip.
            iternum : ``int``\n
                The number of iterations. In another word number of repetition of applying the Grover operator.

        Returns
            circuit : ``QCircuit``\n
                Full quantum circuit for given Grover search.

        Examples
            An example for implementing an Grover search for state where q_0 `and` q_1 is 1.

        >>> import pyqpanda as pq
        >>> from pyqpanda_alg.QFinance import grover
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_state = m.qAlloc_many(3)

        >>> def mark(qubits):
        >>>     cir = pq.QCircuit()
        >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
        >>>     cir << pq.Z(qubits[2])
        >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
        >>>     return cir

        >>> demo_search = grover.Grover(flip_operator=mark)
        >>> prog = pq.QProg()
        >>> prog << demo_search.cir(q_input=q_state[:2], q_flip=q_state, q_zero=q_state[:2], iternum=1)
        >>> res = m.prob_run_dict(prog, q_state[:2])
        >>> print(res)
        >>> print(prog)
        {'00': 0.0, '01': 0.0, '10': 0.0, '11': 1.0000000000000004}

        .. parsed-literal::
                      ┌─┐             ┌─┐ ┌─┐     ┌─┐ ┌─┐
            q_0:  |0>─┤H├ ─■─ ─── ─■─ ┤H├ ┤X├ ─■─ ┤X├ ┤H├
                      ├─┤  │       │  ├─┤ ├─┤ ┌┴┐ ├─┤ ├─┤
            q_1:  |0>─┤H├ ─■─ ─── ─■─ ┤H├ ┤X├ ┤Z├ ┤X├ ┤H├
                      └─┘ ┌┴┐ ┌─┐ ┌┴┐ └─┘ └─┘ └─┘ └─┘ └─┘
            q_2:  |0>──── ┤X├ ┤Z├ ┤X├ ─── ─── ─── ─── ───
                          └─┘ └─┘ └─┘

        """
        pass


def iter_num(q_num, sol_num):
    """
    Calculate the optimal number of iterations in Grover search.

    Parameters
        q_num : ``int``\n
            The number of qubits in the search space. Search space size:  :math:`N = 2 ^ {\\text {q_num}}`.
        sol_num : ``int``\n
            Number of target solution states.

    Returns
        num : The optimal number of iterations in Grover search.

    Examples
        An example for the case we show in the Grover search circuit. And we know there
        is only one solution to be found. And total 2 qubits for the search space.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QFinance import grover
    >>> m = pq.CPUQVM()
    >>> m.initQVM()
    >>> q_state = m.qAlloc_many(3)
    >>> def mark(qubits):
    >>>     cir = pq.QCircuit()
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     cir << pq.Z(qubits[2])
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     return cir
    >>> demo_search = grover.Grover(flip_operator=mark)
    >>> iter_num = grover.iter_num(q_num=len(q_state), sol_num=2)
    >>> print('best iter num: ', iter_num)
    best iter num:  1

    """
    pass


def iter_analysis(q_num, sol_num, iternum=1):
    """
    Calculate the amplification probability and rotation angle for given amplitude
    amplification iteration number.

    Parameters
        q_num : ``int``\n
            The number of qubits in the search space. Search space size:  :math:`N = 2 ^ {\\text {q_num}}`.
        sol_num : ``int``\n
            Number of target solution states.
        iternum : ``int``\n
            Given number of iteration.

    Returns
        prob, theta : (``float``, ``float``)\n
            The amplification probability and rotation angle for given iteration.

    Examples
        An example for the case we show in the Grover search circuit. And we know there
        is only one solution to be found. And total 2 qubits for the search space.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QFinance import grover
    >>> m = pq.CPUQVM()
    >>> m.initQVM()
    >>> q_state = m.qAlloc_many(3)
    >>> def mark(qubits):
    >>>     cir = pq.QCircuit()
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     cir << pq.Z(qubits[2])
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     return cir
    >>> demo_search = grover.Grover(flip_operator=mark)
    >>> prob, angle = grover.iter_analysis(q_num=len(q_state), sol_num=2, iternum=1)
    >>> print('prob for getting one of the solution with given iter num 1:', prob)
    >>> prob, angle = grover.iter_analysis(q_num=len(q_state), sol_num=2, iternum=2)
    >>> print('prob for getting one of the solution with given iter num 2:', prob)
    prob for getting one of the solution with given iter num 1: 1.0
    prob for getting one of the solution with given iter num 2: 0.24999999999999956

    """
    pass

# def iter_analysis(q_num, sol_num, iternum=1, prob_input=None):
#     # 因为反三角函数的性质，输入概率看角度时iternum应为1
#     # 输入prob_input可以反推出原有解个数
#     if prob_input:
#         theta = np.arcsin(np.sqrt(prob_input)) / ((2 * iternum + 1) / 2)
#         sol_num_real = (2 ** q_num) * (np.sin(theta / 2) ** 2)
#         print('circuit_sol_num:', sol_num_real, 'circuit_theta:', theta)
#     sol_prob = sol_num / (2 ** q_num)
#     theta = np.arcsin(np.sqrt(sol_prob)) * 2
#     print("theta:", theta)
#     prob = np.sin(((2 * iternum + 1) / 2) * theta) ** 2
#     return prob


def amp_operator(q_input=None, q_flip=None, q_zero=None, in_operator=None, flip_operator=None, zero_flip=None):
    """
    Construct complete Grover amplitude amplification operator.
    Can be part of Grover/Quantum Count/QAE and other amplitude amplification related algorithm.

    Parameters
        q_input : ``QVec``\n
            Target qubit(s) for in_operator (initial preparation circuit).
            Using Hadamard gates to create the uniform superposition at the beginning most of time.
            Although in most simple cases it includes the full workspace qubits,
            auxiliary qubits can be excluded when dealing with some complex problems.
        q_flip : ``QVec``\n
            Target qubit(s) for flip_operator.
        q_zero : ``QVec``\n
            Target qubit(s) for zero_flip.
        in_operator : callable ``f(qubits)``\n
            Operator/Circuit of the initial search state for the algorithm, default Hadamards.
        flip_operator : callable ``f(qubits)``\n
            Operator/Circuit of marking the good states by phase-flip. Default doing a pauli-Z
            gate at the last qubit.
        zero_flip : callable ``f(qubits)``\n
            Operator/Circuit of reflects 0s by phase-flip. Default doing a zero-controled pauli-Z
            gate on qubits.

    Returns
        circuit : QCircuit\n
            Amplitude amplification operator.

    Examples
        An example for constucting a amplitude amplification operator used in the case we show
        in the Grover search circuit.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QFinance import grover
    >>> m = pq.CPUQVM()
    >>> m.initQVM()
    >>> q_state = m.qAlloc_many(3)
    >>> def mark(qubits):
    >>>     cir = pq.QCircuit()
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     cir << pq.Z(qubits[2])
    >>>     cir << pq.Toffoli(qubits[0], qubits[1], qubits[2])
    >>>     return cir
    >>> print(grover.amp_operator(q_input=q_state[:2], q_flip=q_state, q_zero=q_state[:2], flip_operator=mark))

    .. parsed-literal::
                              ┌─┐ ┌─┐     ┌─┐ ┌─┐
        q_0:  |0>──■─ ─── ─■─ ┤H├ ┤X├ ─■─ ┤X├ ┤H├
                   │       │  ├─┤ ├─┤ ┌┴┐ ├─┤ ├─┤
        q_1:  |0>──■─ ─── ─■─ ┤H├ ┤X├ ┤Z├ ┤X├ ┤H├
                  ┌┴┐ ┌─┐ ┌┴┐ └─┘ └─┘ └─┘ └─┘ └─┘
        q_2:  |0>─┤X├ ┤Z├ ┤X├ ─── ─── ─── ─── ───
                  └─┘ └─┘ └─┘

    """
    pass


def mark_data_reflection(qubits: list = None, mark_data=None):
    """
    Can be used to construct a phase flip operator for given target states.

    Parameters
        qubits : ``QVec``\n
            Target qubit(s) for flip_operator.
        mark_data : ``str``, ``list[str]``\n
            Marked target state(s).

    Returns
        flip_operator : ``QCircuit``\n
            A phase flip operator for given target states

    Examples
        An example for searching '101' and '001' using the flip operator given by this function.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QFinance import grover
    >>> m = pq.CPUQVM()
    >>> m.initQVM()
    >>> q_state = m.qAlloc_many(3)
    >>> def mark(qubits):
    >>>     return grover.mark_data_reflection(qubits=qubits, mark_data=['101', '001'])
    >>> demo_search = grover.Grover(flip_operator=mark)
    >>> prog = pq.QProg()
    >>> prog << demo_search.cir(q_input=q_state)
    >>> res = m.prob_run_dict(prog, q_state)
    >>> print(res)
    {'000': 0.0, '001': 0.5000000000000002, '010': 0.0, '011': 0.0, '100': 0.0, '101': 0.5000000000000002, '110': 0.0, '111': 0.0}

    """
    pass


class GroverAdaptiveSearch:
    """This class provides a framework for Grover Adaptive Search [2].

    Parameters
        init_value : ``float``\n
            The given initial value of the optimization function.
        n_index : ``int``\n
            The number of qubits in the search space. Search space size: N = 2 ** q_num.
        init_circuit : callable ``f(qubits)``\n
            Operator/Circuit of the initial search state for the algorithm, default Hadamards.
        oracle_circuit : callable ``f(qubits, value)``\n
            Operator/Circuit of marking the `better` states by phase-flip. Default doing a pauli-Z
            gate at the last qubit.

    References
        [2] A. Gilliam, S. Woerner, C. Gonciulea, Grover Adaptive Search for Constrained
        Polynomial Binary Optimization. https://arxiv.org/abs/1912.04088

    """
    def __init__(self, init_value, n_index, init_circuit=None, oracle_circuit=None):
        pass

    def run(self, continue_times: int = 3, n_value_function=None, value_function=None,
            rotation_change='random', process_show=False):
        """
        Run the Grover Adaptive Search algorithm to find the minimum.

        Parameters
            continue_times : ``int``\n
                The maximum number of repeated searches at the current optimal point.
            n_value_function : callable ``f(value)``\n
                Function for computing the number of qubits for marking the `better` states at current
                best value, variable qubits not included.
            value_function : callable ``f(var_array)``\n
                Function for computing the problem value of given varriables array(str given as qpanda state).
            rotation_change : ``str{'random', 'increase'}``, optional\n
                The method to get the number of Grover iterations for each search of a search cycle.

               - ``random`` : The number of Grover iterations for each search is randomly obtained from a
                increasing interval. (Default)
               - ``increase`` : The number of Grover iterations for each search is increasing.
            process_show : ``bool``\n
                Set to True to print the detail during search.

        Returns
            minimum_indexes, minimum_res : ( ``list[list[int]]``, ``float``)\n
                The optimization result including the solution array and the optimal value.

        Examples
            An example for minimization of quadratic binary function: x0 * x1 + x0 - x1.

        >>> from pyqpanda_alg.QFinance import grover
        >>> import numpy as np
        >>> import pyqpanda as pq

        >>> # flip if x0 * x1 + x0 - x1 - current_min < 0
        >>> def flip_oracle_function(q_index_value, current_min):
        >>>     q_index = q_index_value[:2]
        >>>     q_value = q_index_value[2:]
        >>>     n_value = len(q_value)
        >>>     factor = np.pi * 2 ** (1 - n_value)
        >>>     cal_cir = pq.QCircuit()
        >>>     cal_cir << pq.H(q_value)
        >>>     for i, q_i in enumerate(q_value):
        >>>         cal_cir << pq.U1(q_i, factor * 2 ** i).control(q_index)
        >>>         cal_cir << pq.U1(q_i, factor * 2 ** i).control(q_index[0])
        >>>         cal_cir << pq.U1(q_i, -factor * 2 ** i).control(q_index[1])
        >>>         cal_cir << pq.U1(q_i, factor * 2 ** i * (-current_min))
        >>>     cal_cir << pq.QFT(q_value).dagger()
        >>>     return cal_cir

        >>> demo_search = grover.GroverAdaptiveSearch(init_value=0, n_index=2, oracle_circuit=flip_oracle_function)

        >>> def n_value_function(current_min):
        >>>     n_value = 2 if current_min == 0 else 3
        >>>     return n_value

        >>> def value_function(var_array):
        >>>     var_array = list(map(int, var_array))[::-1]
        >>>     value = var_array[0] * var_array[1] + var_array[0] - var_array[1]
        >>>     return value

        >>> res = demo_search.run(continue_times=3,
        >>>                       n_value_function=n_value_function,
        >>>                       value_function=value_function,
        >>>                       process_show=True)
        >>> print(res)
        ======searching 1 ,rotation = 1 ======
        minimum Key Again:  00
        minimum Value No Change:  0
        ======searching 2 ,rotation = 1 ======
        Current minimum Key:  10
        Current minimum Value:  -1
        ======searching 1 ,rotation = 1 ======
        minimum Key Again:  10
        minimum Value No Change:  -1
        ======searching 2 ,rotation = 1 ======
        ======searching 3 ,rotation = 1 ======
        rotations:  5
        ([[0, 1]], -1)

        """
        pass

    @staticmethod
    def _bin_to_int(bin_value):
        pass
