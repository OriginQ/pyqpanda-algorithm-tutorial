from pyqpanda import *
from .ConModMul import ConModMul
import math

from .. config import *
auth = Authorization()

def ConModExp(a, N, qvec1, qvec2, qvec3, auxadd):
    """
    Quantum Circuit of Constant Modulo Exponential.

    Parameters:
        :math:`a` : ``int`` \n
            the integer to be added\n
        :math:`N` : ``int`` \n
            the modulo\n
        qvec1 & qvec2 & qvec3 : ``qlist`` \n
            the qubits list\n
        auxadd : ``qubit`` \n
            an auxiliary qubit\n

    Return:
        circuit: ``pq.QCircuit``\n

    With a constant integer :math:`a`, we can compute :math:`a^x` mod N by the formula :math:`a^{\sum_{i=0}^{len(x)-1}2^{i}x_{i}}`.
    We construct a circuit by some controlled constant multiplication circuits according to the binary expansion of :math:`a`.
    The quantum register :math:`|qvec1 \\rangle` holds the value of integer :math:`x\in [0,N-1]` and the quantum register :math:`|qvec2 \\rangle` is an auxiliary register with the same size as that of the register :math:`|qvec1 \\rangle`.
    The result of modulo exponential is deposited in the register :math:`|qvec3 \\rangle`. The circuit needs :math:`3n+1` qubits with :math:`n=\\lceil \log_{2}N \\rceil`.

    Example:
        If :math:`a =2,x=4,N=11`, putting :math:`x` held in :math:`|qvec1 \\rangle`. By the circuit, the result :math:`|00101 \\rangle` will be held in the :math:`|qvec3 \\rangle`.

    .. code-block:: python

        from pyqpanda import *
        from pyqpanda_alg.QLuoShu import ConModExp
        import math

        if __name__ == "__main__":
            N = 11
            a = 2
            x = 4
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()

            qvec1 = qvm.qAlloc_many(n)
            qvec2 = qvm.qAlloc_many(n)
            qvec3 = qvm.qAlloc_many(n)
            auxadd = qvm.qAlloc_many(1)

            prog << bind_nonnegative_data(x, qvec1) \\
                 << ConModExp.ConModExp(a, N, qvec1, qvec2, qvec3, auxadd)

            result = prob_run_dict(prog, qvec3, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d**%d mod %d=%d" % (a,x,N,c))
    
    .. parsed-literal::
            00101:1.000000000000025
            2**4 mod 11=5

    Note that: if :math:`N` is a power of 2, we need to make :math:`n=\\lceil \log_{2}N \\rceil+1` in the Example.
    """
    pass

