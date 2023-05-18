from pyqpanda import *
import math
from .QFTConAdd import QFTConAdd

from .. config import *
auth = Authorization()

def VarModAdd(qvec1, qvec2, auxadd, aux, N):
    """
    Quantum Circuit for Variant Modular Addition.

    The circuit computes a modular addition of two integers :math:`x` and :math:`y` modulo the constant integer modulos :math:`N`, i.e., :math:`|x+y \mod N \\rangle`.

    Parameters:
        :math:`a` : ``int``\n
            the integer to be added\n
        :math:`N` : ``int``\n
            the constant modulo\n
        qvec1 & qvec2 : ``qlist``\n
            the qubits list, holds the integer :math:`x` & :math:`y`\n
        auxadd & aux : ``qubit``\n
            an auxiliary qubit for the operation of QAdder and control constant modulo addition\n

    Return:
        circuit: ``pq.QCircuit``\n

    It performs the operation in place :math:`|x \\rangle|y \\rangle \\rightarrow |(x+y) \mod N \\rangle|y \\rangle` and replaces the first input with the result.
    It uses quantum circuits for plain integer addition and constant addition and subtraction of the modulus :math:`N`. It uses two auxiliary qubits, one of which is used
    as an ancilla qubit in the constant addition and subtraction and can be in an unknown state to which it will be returned at the end of the circuit.
    The circuit needs :math:`2n+2` qubits with :math:`n=\\lceil \log_{2}N \\rceil`.
    The circuit is inverse that can be used to compute :math:`|x \\rangle|y \\rangle \\rightarrow |(x-y) \mod N \\rangle|y \\rangle`.

    Example:
        If :math:`x =7, y=9, N=11`, putting :math:`x` held in :math:`|qvec1 \\rangle` and :math:`y` held in :math:`|qvec2 \\rangle`.
        By the circuit, the result :math:`|0101 \\rangle` will be held in the :math:`|qvec1 \\rangle`, i.e., :math:`7+9 \mod 11=5`.
        If by the inverse of the circuit (by the operator: VarModAdd.dagger()), we can get :math:`7-9 \mod 11=9`, the result :math:`|1001 \\rangle` will be held in the :math:`|qvec1 \\rangle`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import VarModAdd

        if __name__ == "__main__":
            N = 11
            x = 7
            y = 9
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()

            qvec1 = qvm.qAlloc_many(n)
            qvec2 = qvm.qAlloc_many(n)
            aux = qvm.qAlloc_many(1)
            auxadd = qvm.qAlloc()

            prog << bind_nonnegative_data(x, qvec1) \\
                 << bind_nonnegative_data(y, qvec2) \\
                 << VarModAdd.VarModAdd(qvec1, qvec2, auxadd, aux, N)
            result = prob_run_dict(prog, qvec1, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d+%d mod %d=%d" % (x, y, N, c))
    
    .. parsed-literal::
        0101:1.000000000000029
        7+9 mod 11=5


    Note that: if :math:`N` is a power of 2, we need to let :math:`n=\\lceil \log_{2}N \\rceil+1` in the Example.

    """
    pass




