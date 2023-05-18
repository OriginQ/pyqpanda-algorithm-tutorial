from pyqpanda import *
import numpy as np
import math
from .QFTConAdd import modinv, egcd

from .. config import *
auth = Authorization()

def VarModInv(qvec, N):
    """
    Quantum Circuit of Modular Inverse for Any Constant Modular.

    Parameters:
        qvec : ``qlist``\n
            the qubits list, holds the integer :math:`x`\n
        :math:`N` : ``int``\n
            the constant modulo\n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit computes a modular inverse :math:`x^{-1} \mod N`. The circuit use classical pre-processing  to get a unitary matrix and use an operation "QOracle" in the QPanda.
    The circuit is an in-place circuit that performs the operation :math:`|x \\rangle \\rightarrow |x^{-1} \mod N \\rangle`.
    It can not be extended to compute modulo inverse for integer :math:`N` of large bit length.


    Example:
        If :math:`x =7, N=11`, putting :math:`x` held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|1000 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e., :math:`7^{-1} \mod 11=8`.

    .. code-block:: python

        from pyqpanda import *
        import numpy as np
        import math
        from pyqpanda_alg.QLuoShu import VarModInv
    
        if __name__ == "__main__":
            x = 7
            N = 11
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
    
            qvec = qvm.qAlloc_many(n)
    
            prog << bind_nonnegative_data(x, qvec) \\
                 << VarModInv.VarModInv(qvec, N)
    
            result = prob_run_dict(prog, qvec, 1)
    
            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("%d**{-1} mod %d=%d" % (x, N, c))

    .. parsed-literal::
            1000:1.0
            7**{-1} mod 11=8

    """
    pass




