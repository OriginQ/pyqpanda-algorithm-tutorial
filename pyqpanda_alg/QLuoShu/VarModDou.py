from pyqpanda import *
import math
from .lshift import lshift
from .QFTConAdd import QFTConAdd

from .. config import *
auth = Authorization()

def VarModDou(qvec, aux, N):
    """
    Quantum Circuit for Variant Modular Doubling for Odd Modulo.

    Parameters:
        :math:`qvec` : ``qlist``\n
            holds the integer :math:`x`\n
        aux : ``qubit``\n
            an auxiliary qubit to control constant modulo addition\n
        :math:`N` : ``int``\n
            the constant modulo\n

    Return:
        circuit : ``VarModDou.QCircuit``\n

    The circuit is used to compute modular doubling that :math:`|x \\rangle |0 \\rangle \\rightarrow  |2x \mod
    N\\rangle|0\\rangle`. The modular doubling circuit for a constant odd integer modulus :math:`N`. There are two
    changes that make it more efficient than the addition circuit. First, it works in place on only one
    :math:`n`-qubit input integer :math:`|x \\rangle`, with :math:`n=\\lceil \log_{2}N \\rceil`. Therefore it uses
    only :math:`n+1` qubits.

    Example:
        If :math:`x =7, N=11`, putting :math:`x` held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|0011 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e., :math:`2*7 \mod 11=3`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import VarModDou

        if __name__ == "__main__":
            N = 11
            x = 7
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()

            qvec = qvm.qAlloc_many(n)
            aux = qvm.qAlloc_many(1)

            prog << bind_nonnegative_data(x, qvec) \\
                 << VarModDou.VarModDou(qvec, aux, N)

            result = prob_run_dict(prog, qvec, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("2*%d mod %d=%d" % (x, N, c))

    .. parsed-literal::
        0011:0.9999999999999982
        2*7 mod 11=3

    Note that: :math:`N` is an odd integer.
    """
    pass



