"""
Prepare Dicke state D(n,k) in an n-qubit system with k-Hamming-weight.
When k=1, this module is equivalent to W state generation.
A build-in W state generation supports implementation on a linear architecture.
Ref. https://doi.org/10.1109/QCE53715.2022.00027
Ref. https://doi.org/10.1002/qute.201900015

"""
from math import ceil, acos
from scipy.special import comb
import pyqpanda as pq

from .. config import *
auth = Authorization()




def prepare_dicke_state(q_list, k, compress=True):
    """Prepare Dicke state.

    The Dicke state is defined as :math:`D_{n}^{(k)} = \sum_{hmw(i)=k} |i \\rangle`,
    which is equally superposition state of all states with the same Hamming weight.
    The method prepare Dicke state with in :math:`O(k*log(n/k))` depth in
    all-to-all connectivity architecture.

    Parameters
        q_list: ``QVec``, ``List[Qubit]``, shape (n,)\n
            Qubit addresses. List size is supposed to be the :math:`n`
            of :math:`D_{n}^{(k)}`.
        k : ``int``, k>0\n
            The target Hamming weight of the Dicke state to be prepared,
            *i.e.*, the :math:`k` of :math:`D_{n}^{(k)}`.
        compress : ``bool``, ``optional``\n
            If True, compress the basic gate implementation with simulated control
            gates otherwise using basic gate implementation; default is True.

    Return
        circuit : ``pyqpanda QCircuit``\n
            A pyqpanda QCircuit which assumes the input state is all 0.

    Raises
        ValueError\n
            If the target Hamming weight is larger than the input qubit number (:math:`k<n`),
            or k is invalid (:math:`k<0`), or qubit number is 0 (:math:`n=0`).

    Reference
        [1] Bärtschi A, Eidenbenz S. Short-depth circuits for dicke state preparation[C]
        2022 IEEE International Conference on Quantum Computing and Engineering (QCE). IEEE, 2022: 87-96.
        https://doi.org/10.1109/QCE53715.2022.00027

    Examples
        .. code-block:: python

            import pyqpanda as pq
            from pyqpanda_alg.QAOA import dstate

            n = 4
            k = 2
            machine = pq.CPUQVM()
            machine.initQVM()
            qubits = machine.qAlloc_many(n)
            prog = pq.QProg()
            prog << dstate.prepare_dicke_state(qubits, k)
            print(pq.draw_qprog(prog, output='text'))
            results = machine.prob_run_list(prog, qubits)
            for key in range(2**n):
                prob = results[key]
                key_hmw = bin(key).count('1')
                if key_hmw == k:
                    print(bin(key)[2::].zfill(n), prob)


    The given example illustrates how to prepare the state :math:`D_4^{(2)}`.
    The corresponding quantum circuit is:

    .. parsed-literal::

                  ┌─┐     !                               ┌────┐         ! ┌────┐                ┌────┐
        q_0:  |0>─┤X├ ────! ────────────── ────────────── ┤CNOT├──── ────! ┤CNOT├ ───────■────── ┤CNOT├
                  ├─┤     !                               └──┬┬┴───┐     ! └──┬─┘ ┌──────┴─────┐ └──┬─┘
        q_1:  |0>─┤X├ ────! ────────────── ────────────── ───┼┤CNOT├ ────! ───■── ┤RY(1.570796)├ ───■──
                  └─┘     ! ┌────────────┐                   │└──┬─┘     ! ┌────┐ └────────────┘ ┌────┐
        q_2:  |0>──── ────! ┤RY(2.300524)├ ───────■────── ───┼───■── ────! ┤CNOT├ ───────■────── ┤CNOT├
                          ! └────────────┘ ┌──────┴─────┐    │           ! └──┬─┘ ┌──────┴─────┐ └──┬─┘
        q_3:  |0>──── ────! ────────────── ┤RY(0.927295)├ ───■────── ────! ───■── ┤RY(1.570796)├ ───■──
                          !                └────────────┘                !        └────────────┘

    And the probability of all possible state are (with possible floating errors):

    .. parsed-literal::
        0011 0.16666666666666663
        0101 0.1666666666666667
        0110 0.1666666666666667
        1001 0.1666666666666667
        1010 0.1666666666666667
        1100 0.16666666666666663

    which include all states with the same Hamming weight :math:`k=2`.

    """
    pass


def linear_w_state(q_list, compress=True):
    """Prepare W state with a divide-and-conquer algorithm on the linear architecture device.

    W state is the special Dicke state where :math:`k=1`. The special case is compatible to
    Dicke state preparation while it can be formalized on a linear connectivity device with
    exactly :math:`n-1` depth and :math:`3n-3` CNOT gates.

    Parameters
         q_list: ``QVec``, ``List[Qubit]``, shape (n,)\n
            Qubit addresses. List size is supposed to be the :math:`n` of :math:`D_{n}^{(1)}`.
         compress  : ``bool``, ``optional``\n
            If True, compress the basic gate implementation with simulated control
            gates otherwise using basic gate implementation; default is True.

    Return
        circuit : ``pyqpanda QCircuit``\n
            A pyqpanda QCircuit which assumes the input state is all 0.

    Raises
        ValueError\n
            If the input qubit number is zero.

    Reference
        Cruz D, Fournier R, Gremion F, et al.
        Efficient quantum algorithms for ghz and w states, and implementation on the IBM quantum computer[J].
        Advanced Quantum Technologies, 2019, 2(5-6): 1900015.

    Example
        .. code-block:: python

            import pyqpanda as pq

            import pyqpanda as pq
            from pyqpanda_alg.QAOA import dstate

            n = 3
            machine = pq.CPUQVM()
            machine.initQVM()
            qubits = machine.qAlloc_many(n)
            prog = pq.QProg()
            prog << dstate.linear_w_state(qubits, compress=True)
            print(pq.draw_qprog(prog, output='text'))
            results = machine.prob_run_list(prog, qubits)
            for key in range(2 ** n):
                prob = results[key]
                key_hmw = bin(key).count('1')
                if key_hmw == 1:
                    print(bin(key)[2::].zfill(n), prob)

    The example prepare W state on a 3-qubit system which is linearly connected.
    The corresponding circuit reads as:

    .. parsed-literal::
                  ┌─┐                ┌────┐
        q_0:  |0>─┤X├ ───────■────── ┤CNOT├ ────────────── ──────
                  └─┘ ┌──────┴─────┐ └──┬─┘                ┌────┐
        q_1:  |0>──── ┤RY(1.910633)├ ───■── ───────■────── ┤CNOT├
                      └────────────┘        ┌──────┴─────┐ └──┬─┘
        q_2:  |0>──── ────────────── ────── ┤RY(1.570796)├ ───■──
                                            └────────────┘

    The resulting state should be like (with possible floating errors):

    .. parsed-literal::
        001 0.3333333333333333
        010 0.3333333333333334
        100 0.3333333333333334

    Each of them is one-Hamming-weight.

    """
    pass
