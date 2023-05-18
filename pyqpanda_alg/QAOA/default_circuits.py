import pyqpanda as pq
from itertools import combinations
from . import dstate

from .. config import *
auth = Authorization()

def parity_partition_xy_mixer(qlist, beta):
    """
    Quantum circuits to approximate a parity-partition XY mixer.

    Parameters
        qlist : ``list``\n
            Qubits list.\n

        beta : ``float``\n
            angle :math:`t` of :math:`e^{-iHt}`\n

    Return
        cir : ``pq.QCircuit``\n
            Circuit of simulation a parity-partition XY mixer :math:`e^{-iHt}`.\n

        
    Examples   
        Generate a circuit of simulation a parity-partition XY mixer :math:`e^{-iH\pi/2}`.

    
    >>> import pyqpanda as pq
    >>> import numpy as np
    >>> from pyqpanda_alg.QAOA import default_circuits
    >>> machine = pq.CPUQVM()
    >>> machine.initQVM()
    >>> qubits = machine.qAlloc_many(4)
    >>> circuit = default_circuits.parity_partition_xy_mixer(qubits, np.pi/2)
    >>> print(circuit)

    .. parsed-literal::

        q_0:  |0>─X X─
                  │ │
        q_1:  |0>─X ┼X
                    ││
        q_2:  |0>─X ┼X
                  │ │
        q_3:  |0>─X X─

    Note
        For a given XY mixer Hamiltonian\n

         
        .. math::
            H_{XY,v} = \\frac{1}{2} \sum_{c,c'\in K} (\sigma_{v,c}^x \sigma_{v',c}^x + \sigma_{v,c}^y \sigma_{v',c}^y)

    When the mixer-set :math:`K` takes a one dimensional structure: :math:`c'=c+1`, and periodic boundary condition,
    it is termed a ring mixer. In order to simulate a ring mixer in quantum circuit, a one-order approximation by
    applying local XY-Hamiltonian on even paris first and local pairs next is used, which is called parity-partition XY
    mixer. The leading error term is in order of the number of qubits in the domain. See details in [1]

    Reference
        [1] WANG Z, RUBIN N C, DOMINY J M, et. XY-mixers: analytical and numerical results for QAOA[J/OL].
        Physical Review A, 2020, 101(1): 012320. DOI:10.1103/PhysRevA.101.012320.

    """
    pass


def complete_xy_mixer(qlist, angle):
    """
    Quantum circuits to approximate a complete XY mixer.

    Parameters
        qlist : ``list``\n
            Qubits list.\n

        angle : ``float``\n
            beta :math:`t` of :math:`e^{-iHt}`\n

    Return
        cir : ``pq.QCircuit``\n
            Circuit of simulation a complete XY mixer :math:`e^{-iHt}`.\n

    Examples
        Generate a circuit of simulation a complete XY mixer :math:`e^{-iH\pi/2}`.

        
    >>> import pyqpanda as pq
    >>> import numpy as np
    >>> from pyqpanda_alg.QAOA import default_circuits
    >>> machine = pq.CPUQVM()
    >>> machine.initQVM()
    >>> qubits = machine.qAlloc_many(4)
    >>> circuit = default_circuits.complete_xy_mixer(qubits, np.pi/2)
    >>> print(circuit)

    .. parsed-literal::

        q_0:  |0>─X X─ X─
                  │ │  │
        q_1:  |0>─X ┼X ┼X
                    ││ ││
        q_2:  |0>─X X┼ ┼X
                  │  │ │
        q_3:  |0>─X ─X X─


    Note
        For a given XY mixer Hamiltonian
    
        .. math::
            H_{XY,v}=\\frac{1}{2}\sum_{c,c'\in K} (\sigma_{v,c}^x \sigma_{v',c}^x + \sigma_{v,c}^y \sigma_{v',c}^y)

    When the mixer-set :math:`K` includes all pairs, it is termed a complete mixer. In order to simulate a complete
    mixer in quantum circuit, a partition of :math:`\kappa - 1, \kappa=\lceil \log_2 n \\rceil`  is applied, where
    :math:`n` is the number of qubits. See details in [1]

    Reference
        [1] WANG Z, RUBIN N C, DOMINY J M, et. XY-mixers: analytical and numerical results for QAOA[J/OL].\n
        Physical Review A, 2020, 101(1): 012320. DOI:10.1103/PhysRevA.101.012320.

    """
    pass


def xy_mixer(domains, mixer_type='PXY'):
    """
    Generate XY mixer circuit.

    Parameters
        domains : ``integer`` or ``list[list]``\n
            Nodes of each XY mixer to be applied. If an integer n is given, the qubit list is divided into n parts. If a
            list is given, the mixer is applied to each domain.

        mixer_type: ``string``\n
            How the mixer is implemented. Should be one of

                    - ``PXY`` : Parity partition XY mixer.\n
                        See 'parity_partition_xy_mixer'
                    - ``CXY`` : Complete XY mixer\n
                        See 'complete_xy_mixer'

                If not given, default by ``PXY``.

    Return
        mixer_circuit : ``func(pq.QCircuit)``\n
            A function which use qubit list and angles as input, output a circuit of simulation a XY mixer :math:`e^{-iHt}`.

    Examples
        Generate a circuit of simulation a complete XY mixer :math:`e^{-iH\pi/2}` in qubits [0, 1] and [2, 3].

    >>> import pyqpanda as pq
    >>> import numpy as np
    >>> from pyqpanda_alg.QAOA import default_circuits
    >>> machine = pq.CPUQVM()
    >>> machine.initQVM()
    >>> qubits = machine.qAlloc_many(4)
    >>> circuit1 = pq.QCircuit()
    >>> circuit2 = pq.QCircuit()
    >>> circuit1 << default_circuits.xy_mixer(2, 'PXY')(qubits, np.pi/2)
    >>> circuit2 << default_circuits.xy_mixer([[0,1], [2,3]], 'PXY')(qubits, np.pi/2)
    >>> print(circuit1)
    >>> print(circuit2)

    .. parsed-literal::

        q_0:  |0>─X
                  │
        q_1:  |0>─X

        q_2:  |0>─X
                  │
        q_3:  |0>─X


        q_0:  |0>─X
                  │
        q_1:  |0>─X

        q_2:  |0>─X
                  │
        q_3:  |0>─X

    Note
        A XY mixer can enforce the state evolution in a feasible subspace which keep the hamming weight (total spin) of the
        state to be conserved.\n
        For example, in one-hot coding problem, a W state as initial state combine with the XY mixer
        can keep all solutions remain in one-hot form. See details in [1].

    Reference
        [1] WANG Z, RUBIN N C, DOMINY J M, et. XY-mixers: analytical and numerical results for QAOA[J/OL].
        Physical Review A, 2020, 101(1): 012320. DOI:10.1103/PhysRevA.101.012320.

    """
    pass


def init_d_state(domains, k=1, compress=True):
    """Prepare Dicke state.

    The Dicke state is defined as :math:`D_{n}^{(k)} = \sum_{hmw(i)=k} |i \\rangle`,
    which is equally superposition state of all states with the same Hamming weight.
    The method prepare an initial state, which is the product state of Dicke state in each domain,
    with in :math:`O(k*log(n/k))` depth in all-to-all connectivity architecture.

    Parameters
        domains : ``integer`` or ``list[list]``\n
            Nodes of each XY mixer to be applied. If an integer n is given, the qubit list is divided into n parts. If a
            list is given, the mixer is applied to each domain.
        k : ``integer``,  :math:`k>0` \n
            The target Hamming weight of the Dicke state to be prepared,
            *i.e.*, the :math:`k` of :math:`D_{n}^{(k)}`.
        compress : ``bool``, ``optional``\n
            If True, compress the basic gate implementation with simulated control
            gates otherwise using basic gate implementation; default is True.

    Return
        init_state_circuit : ``function``\n
            Return a function, which takes qubit list as input, and output a pyqpanda QCircuit which assumes
            the input state is all 0.

    Raises
        ValueError\n
            If the target Hamming weight is larger than the input qubit number (:math:`k<n`),
            or k is invalid (:math:`k<0`), or qubit number is 0 (:math:`n=0`).

    Reference
        Bärtschi A, Eidenbenz S. Short-depth circuits for dicke state preparation[C]\n
        2022 IEEE International Conference on Quantum Computing and Engineering (QCE). IEEE, 2022: 87-96.
        https://doi.org/10.1109/QCE53715.2022.00027

        
    Examples
        The given example illustrates how to prepare the state :math:`D_4^{(2)}`.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QAOA import default_circuits
    >>> n = 6
    >>> k = 2
    >>> machine = pq.CPUQVM()
    >>> machine.initQVM()
    >>> qubits = machine.qAlloc_many(n)
    >>> prog = pq.QProg()
    >>> domain = [[0,1,2],[3,4,5]]
    >>> init_circuit = default_circuits.init_d_state(domain, k)
    >>> prog << init_circuit(qubits)
    >>> print(pq.draw_qprog(prog, output='text'))
    >>> results = machine.prob_run_list(prog, qubits)
    >>> for key in range(2**n):
    >>>     prob = results[key]
    >>>     key_hmw = bin(key).count('1')
    >>>     if key_hmw == len(domain)*k:
    >>>         print(bin(key)[2::].zfill(n), prob)


    The corresponding quantum circuit is:

    .. parsed-literal::

                  ┌─┐                   ┌────┐                ┌────┐
        q_0:  |0>─┤X├─────────── ────── ┤CNOT├ ───────■────── ┤CNOT├
                  ├─┤            ┌────┐ └──┬─┘ ┌──────┴─────┐ └──┬─┘
        q_1:  |0>─┤X├─────────── ┤CNOT├ ───■── ┤RY(1.570796)├ ───■──
                  ├─┴──────────┐ └──┬─┘        └────────────┘
        q_2:  |0>─┤RY(1.910633)├ ───■── ────── ────────────── ──────
                  ├─┬──────────┘        ┌────┐                ┌────┐
        q_3:  |0>─┤X├─────────── ────── ┤CNOT├ ───────■────── ┤CNOT├
                  ├─┤            ┌────┐ └──┬─┘ ┌──────┴─────┐ └──┬─┘
        q_4:  |0>─┤X├─────────── ┤CNOT├ ───■── ┤RY(1.570796)├ ───■──
                  ├─┴──────────┐ └──┬─┘        └────────────┘
        q_5:  |0>─┤RY(1.910633)├ ───■── ────── ────────────── ──────
                  └────────────┘

    And the probability of all possible state are (with possible floating errors):

    .. parsed-literal::

        011011 0.1111111111111111
        011101 0.11111111111111113
        011110 0.11111111111111113
        101011 0.11111111111111113
        101101 0.11111111111111113
        101110 0.11111111111111113
        110011 0.11111111111111113
        110101 0.11111111111111113
        110110 0.11111111111111113

    which represents the state :math:`\ket{D_3^2}_{012}\otimes\ket{D_3^2}_{345}`.

    """
    pass


def prepare_dicke_state(q_list, k, compress=True):
    """Prepare Dicke state.

    The Dicke state is defined as :math:`D_{n}^{(k)} = \sum_{hmw(i)=k} |i\\rangle` ,
    which is equally superposition state of all states with the same Hamming weight.
    The method prepare Dicke state with in :math:`O(k*log(n/k))` depth in
    all-to-all connectivity architecture.

    Parameters
        q_list : ``QVec``, ``List[Qubit]``, shape (n,)\n
            Qubit addresses. List size is supposed to be the :math:`n`
            of :math:`D_{n}^{(k)}`.\n
        k : ``integer``, k>0 \n
            The target Hamming weight of the Dicke state to be prepared,
            *i.e.*, the :math:`k` of :math:`D_{n}^{(k)}`.
        compress : ``bool``, ``optional`` \n
            If True, compress the basic gate implementation with simulated control
            gates otherwise using basic gate implementation; default is True.

    Return
        circuit : ``pyqpanda QCircuit`` \n
            A pyqpanda QCircuit which assumes the input state is all 0.\n

    Raises
        ValueError\n
            If the target Hamming weight is larger than the input qubit number (:math:`k<n`),
            or k is invalid (:math:`k<0`), or qubit number is 0 (:math:`n=0`).

    Reference
        Bärtschi A, Eidenbenz S. Short-depth circuits for dicke state preparation[C]
        2022 IEEE International Conference on Quantum Computing and Engineering (QCE). IEEE, 2022: 87-96.
        https://doi.org/10.1109/QCE53715.2022.00027

    Examples
        The given example illustrates how to prepare the state :math:`D_4^{(2)}`.

    >>> import pyqpanda as pq
    >>> from pyqpanda_alg.QAOA import default_circuits
    >>> n = 4
    >>> k = 2
    >>> machine = pq.CPUQVM()
    >>> machine.initQVM()
    >>> qubits = machine.qAlloc_many(n)
    >>> prog = pq.QProg()
    >>> prog << default_circuits.prepare_dicke_state(qubits, k)
    >>> print(pq.draw_qprog(prog, output='text'))
    >>> results = machine.prob_run_list(prog, qubits)
    >>> for key in range(2**n):
    >>>     prob = results[key]
    >>>     key_hmw = bin(key).count('1')
    >>>     if key_hmw == k:
    >>>         print(bin(key)[2::].zfill(n), prob)


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
        q_list : ``QVec``, ``List[Qubit]``, shape (n,)\n
            Qubit addresses. List size is supposed to be the :math:`n` of :math:`D_{n}^{(1)}`.\n

        compress : ``bool``, ``optional``\n
            If True, compress the basic gate implementation with simulated control
            gates otherwise using basic gate implementation; default is True.\n

    Return
        circuit : ``pyqpanda QCircuit`` \n
            A pyqpanda QCircuit which assumes the input state is all 0.\n

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
            from pyqpanda_alg.QAOA import default_circuits

            n = 3
            machine = pq.CPUQVM()
            machine.initQVM()
            qubits = machine.qAlloc_many(n)
            prog = pq.QProg()
            prog << default_circuits.linear_w_state(qubits, compress=True)
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
