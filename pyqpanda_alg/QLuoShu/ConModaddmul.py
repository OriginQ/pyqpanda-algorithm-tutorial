from pyqpanda import *
import math
from .ConModAdd import ConModAdd

from .. config import *
auth = Authorization()

def ConModaddmul(a, N, qvec1, qvec2, auxadd):
    """
    Quantum Circuit of Constant Multiplication and Modulo Addition.

    Parameters:
        :math:`a`: ``int`` \n
            the integer to be added\n
        :math:`N` : ``int`` \n
            the modulo\n
        qvec1 & qvec2 : ``qlist`` \n
            the qubits list\n
        auxadd : ``qubit`` \n
            an auxiliary qubit\n

    Return:
        circuit: ``pq.QCircuit``\n

    Based on the constant QFT modulo addition, the circuit can compute :math:`b+a*x \mod N` with a constant integer :math:`a` and a constant modulo :math:`N`,
    where the the :math:`|qvec1 \\rangle` register holds an integer :math:`x` and the :math:`|qvec2 \\rangle` register holds an integer :math:`b`.
    The result of modulo addition-multiplication is deposited in the register :math:`|qvec2 \\rangle`. The circuit needs :math:`2n+1` qubits with :math:`n=\\lceil \log_{2}N \\rceil`.
    The inverse of the circuit can compute :math:`b-a*x \mod N`.

    Example:
        If :math:`a =2, b=10, x=8, N=11`, putting x held in :math:`|qvec1 \\rangle`. By the circuit, the result :math:`|0100 \\rangle` will be held in the :math:`|qvec2 \\rangle`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import ConModaddmul

        if __name__ == "__main__":
            N = 11
            a = 2
            b = 10
            x = 8
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()

            qvec1 = qvm.qAlloc_many(n)
            qvec2 = qvm.qAlloc_many(n)
            auxadd = qvm.qAlloc_many(1)

            prog << bind_nonnegative_data(x, qvec1) \\
                 << bind_nonnegative_data(b, qvec2) \\
                 << ConModaddmul.ConModaddmul(a, N, qvec1, qvec2, auxadd)

            result = prob_run_dict(prog, qvec2, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d+%d*%d mod %d=%d" % (b,x,a, N, c))
    
    .. parsed-literal::
            0100:1.0000000000000067
            10+8*2 mod 11=4

    Note that: if :math:`N` is a power of 2, we need to let :math:`n=\\lceil \log_{2}N \\rceil+1` in the Example.

    Here, we give the circuit graph of the example in the above with 9 qubits in the following:

    .. parsed-literal::
                  ┌─┐                                                                                                   >
        q_0:  |0>─┤X├ ─■─ ───────■────── ───────■────── ───────■────── ───────■────── ─■─ ───────■────── ───────■────── >
                  ├─┤  │         │              │              │              │        │         │              │       >
        q_1:  |0>─┤X├ ─┼─ ───────┼────── ───────┼────── ───────┼────── ───────┼────── ─┼─ ───────┼────── ───────┼────── >
                  └─┘  │         │              │              │              │        │         │              │       >
        q_2:  |0>──── ─┼─ ───────┼────── ───────┼────── ───────┼────── ───────┼────── ─┼─ ───────┼────── ───────┼────── >
                  ┌─┐  │         │              │              │              │        │         │              │       >
        q_3:  |0>─┤X├ ─┼─ ───────┼────── ───────┼────── ───────┼────── ───────┼────── ─┼─ ───────┼────── ───────┼────── >
                  ├─┤  │         │              │              │              │        │         │              │       >
        q_4:  |0>─┤X├ ─┼─ ───────┼────── ───────┼────── ───────┼────── ───────■────── ─┼─ ───────┼────── ───────┼────── >
                  ├─┤  │         │              │              │              │        │         │              │       >
        q_5:  |0>─┤X├ ─┼─ ───────┼────── ───────┼────── ───────■────── ───────┼────── ─┼─ ───────┼────── ───────■────── >
                  ├─┤  │         │              │              │              │        │         │              │       >
        q_6:  |0>─┤X├ ─┼─ ───────┼────── ───────■────── ───────┼────── ───────┼────── ─┼─ ───────■────── ───────┼────── >
                  └─┘  │         │              │              │              │       ┌┴┐ ┌──────┴─────┐ ┌──────┴─────┐ >
        q_7:  |0>──── ─┼─ ───────■────── ───────┼────── ───────┼────── ───────┼────── ┤H├ ┤CR(1.570796)├ ┤CR(0.785398)├ >
                      ┌┴┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ └─┘ └────────────┘ └────────────┘ >
        q_8:  |0>──── ┤H├ ┤CR(1.570796)├ ┤CR(0.785398)├ ┤CR(0.392699)├ ┤CR(0.196350)├ ─── ────────────── ────────────── >
                      └─┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘                                   >
    """
    pass



