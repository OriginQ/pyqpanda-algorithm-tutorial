from pyqpanda import *
import math
from .VarModDou import VarModDou
from .VarModAdd import VarModAdd

from .. config import *
auth = Authorization()

def VarModMul(qvec1, qvec2, qvec3, auxadd, aux, N):
    """
    Quantum Circuit of Variant Modular Multiplication for Odd Modulo.

    Parameters:
        qvec1 & qvec2 : ``qlist``\n
            the qubits list, holds the integer :math:`x` & :math:`y`\n
        qvec3 : ``qlist``\n
            store the result :math:`x*y \mod N`\n
        auxadd & aux : ``qubit``\n
            an auxiliary qubit for the operation of QAdder and control constant modulo addition\n
        :math:`N` : ``int``\n
            the constant modulo\n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit is used to compute modular multiplication that :math:`|x \\rangle|y \\rangle|0 \\rangle \\rightarrow
    |x \\rangle|y \\rangle|x*y \mod N \\rangle` and replaces the third input with the result. Modular multiplication
    can be computed by repeated modular doublings and conditional modular additions. The circuit computes the product
    :math:`z=x \cdot y \mod N` for constant odd integer :math:`N` by using a simple expansion of the product along a
    binary decomposition of the first multiplicand, i.e.,

    :math:`x * y=\sum_{i=0}^{n-1} x_{i} 2^i * y=x_0 y+2(x_1 y+2(x_2 y+...+2(x_{n-2} y+2(x_{n-1} y)) ...))`.

    It uses :math:`3n + 2` qubits with :math:`n=\\lceil \log_{2}N \\rceil`.

    Example:
        If :math:`x =7,y=5, N=11`, putting :math:`x` held in :math:`|qvec1\\rangle` and putting :math:`y` held in :math:`|qvec2 \\rangle`.
        By the circuit, the result :math:`|0010 \\rangle` will be held in the :math:`|qvec3 \\rangle`, i.e., :math:`7*5 \mod 11=2`.


    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import VarModMul

        if __name__ == "__main__":
            N = 11
            x = 7
            y = 5
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
    
            qvec1 = qvm.qAlloc_many(n)
            qvec2 = qvm.qAlloc_many(n)
            qvec3 = qvm.qAlloc_many(n)
            auxadd = qvm.qAlloc()
            aux = qvm.qAlloc_many(1)
    
            prog << bind_nonnegative_data(x, qvec1) \\
                 << bind_nonnegative_data(y, qvec2) \\
                 << VarModMul.VarModMul(qvec1, qvec2, qvec3, auxadd, aux, N)
            result = prob_run_dict(prog, qvec3, 1)
    
            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d*%d mod %d=%d" % (x, y, N, c))
    
    .. parsed-literal::
            0010:1.0000000000000047
            7*5 mod 11=2

    Note that: `N` is an odd integer.

    """
    pass
