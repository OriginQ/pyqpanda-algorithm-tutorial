from pyqpanda import *
import math
from .VarModDou import VarModDou
from .VarModAdd import VarModAdd

from .. config import *
auth = Authorization()

def VarModSqr(qvec1, qvec2, auxadd, aux, auxsqr, N):
    """
    Quantum Circuit of Variant Modular Square for Odd Modulo.

    Parameters:
        qvec1 & qvec2 : ``qlist``\n
            the qubits list, holds the integer :math:`x`\n
        auxadd & aux & auxsqr : ``qubit``\n
            auxiliary qubit for the operation of QAdder and control constant modulo addition\n
        :math:`N` : ``int``\n
            the constant modulo\n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit performs the operation that :math:`|x \\rangle|0 \\rangle \\rightarrow |x \\rangle|x^{2} \mod N
    \\rangle`.  It uses :math:`2n + 3` qubits with :math:`n=\\lceil \log_{2}N \\rceil` by removing the :math:`n`
    qubits for the second input multiplicand, and adding one ancilla qubit, which is used in round :math:`i` to copy
    out the current bit :math:`x_{i}` of the input in order to add :math:`x` to the accumulator conditioned on the
    value of :math:`x_{i}`.

    Example:
        If :math:`x =7, N=11`, putting :math:`x` held in :math:`|qvec1 \\rangle`. By the circuit, the result :math:`|00101 \\rangle` will be held in the :math:`|qvec2 \\rangle`, i.e., :math:`7^{2} \mod 11=5`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import VarModSqr

        if __name__ == "__main__":
            x = 7
            N = 11
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
    
            qvec1 = qvm.qAlloc_many(n)
            qvec2 = qvm.qAlloc_many(n)
            auxadd = qvm.qAlloc()
            aux = qvm.qAlloc_many(1)
            auxsqr = qvm.qAlloc()
    
            prog << bind_nonnegative_data(x, qvec1) \\
                 << VarModSqr.VarModSqr(qvec1, qvec2, auxadd, aux, auxsqr, N)

    
            result = prob_run_dict(prog, qvec2, 1)
    
            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d**2 mod %d=%d" % (x, N, c))

    .. parsed-literal:: 
            0101:1.0000000000000013
            7**2 mod 11=5

    Note that: :math:`N` is an odd integer.
    """
    pass

