from pyqpanda import *
import math
from .QFTConAdd import QFTConAdd

from .. config import *
auth = Authorization()

def ConModAdd(a, N, qvec, auxadd):
    """
    Quantum Circuit of Constant Modulo Addition Using QFT(Quantum Fourier Transform).

    Parameters:
        :math:`a`: ``int`` \n
            the integer to be added\n
        :math:`N` : ``int``\n
            the modulo \n
        qvec : ``qlist``\n
            the qubits list\n
        auxadd : ``qubit``\n
            an auxiliary qubit \n
            
    Return:
        circuit: ``pq.QCircuit``\n

    The circuit works on one quantum register :math:`|qvec \\rangle` holding the input integer :math:`x \in [0,N-1]`
    and one phase array from classical computation on a constant integer :math:`a \in [0,N-1]`.
    to compute modulo :math:`N` addition using QFT.
    The circuit is an in-place circuit, where the result :math:`x+a \mod N` of modulo addition is deposited in the register :math:`|qvec \\rangle`. The circuit needs :math:`n+1` qubits with :math:`n=\\lceil \log_{2}N \\rceil`.
    The inverse of the circuit can compute :math:`x-a \mod N`.


    Example:
        If :math:`a =7, x=9, N=11`, putting x held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|0101 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e., :math:`7+9 \mod 11=5`.
        If by the inverse of the circuit (by the operator: ConModAdd.dagger()), we can get :math:`7-9 \mod 11=9`, the result :math:`|1001 \\rangle` will be held in the :math:`|qvec \\rangle`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import ConModAdd

        if __name__ == "__main__":
            N = 11
            a = 7
            x = 9
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
            n = math.ceil(math.log(N, 2))
            qvec = qvm.qAlloc_many(n)
            auxadd = qvm.qAlloc_many(1)
            prog << bind_nonnegative_data(x, qvec) \\
                 << ConModAdd.ConModAdd(a, N, qvec, auxadd)
            result = prob_run_dict(prog, qvec, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d+%d mod %d=%d" % (x,a,N, c))

    .. parsed-literal::
        0101:1.0000000000000064
        9+7 mod 11=5

    Note that: if :math:`N` is a power of 2, we need to let :math:`n=\\lceil \log_{2}N \\rceil+1` in the Example.

    Here, we give the circuit graph of the example in the above for constant modolo addition with 5 qubits:

    .. parsed-literal::
                  ┌─┐                                                                                                    >
        q_0:  |0>─┤X├ ────────────── ────────────── ────────────────────── ───────■────────────── ───────■────────────── >
                  ├─┤                                                             │                      │               >
        q_1:  |0>─┤X├ ────────────── ────────────── ───────■────────────── ───────┼───────■────── ───────┼───────■────── >
                  ├─┤                                      │                      │       │┌─┐           │┌──────┴─────┐ >
        q_2:  |0>─┤X├ ────────────── ───────■────── ───────┼───────■────── ───────┼───────┼┤H├─── ───────┼┤CR(1.570796)├ >
                  └─┘                       │┌─┐           │┌──────┴─────┐        │┌──────┴┴─┴──┐ ┌──────┴┴────┬───────┘ >
        q_3:  |0>──── ───────■────── ───────┼┤H├─── ───────┼┤CR(1.570796)├ ───────┼┤CR(0.785398)├ ┤CR(0.392699)├──────── >
                  ┌─┐ ┌──────┴─────┐ ┌──────┴┴─┴──┐ ┌──────┴┴────┬───────┘ ┌──────┴┴────┬───────┘ └────────────┘         >
        q_4:  |0>─┤H├ ┤CR(1.570796)├ ┤CR(0.785398)├ ┤CR(0.392699)├──────── ┤CR(0.196350)├──────── ────────────────────── >
                  └─┘ └────────────┘ └────────────┘ └────────────┘         └────────────┘                                >
    """
    pass

