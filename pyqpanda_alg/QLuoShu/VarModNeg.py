from pyqpanda import *
import numpy as np
import math

from .. config import *
auth = Authorization()

def VarModNeg(qvec, N):
    """
    Quantum Circuit of Modular Negation for Any Constant Modular.

    Parameters:
        qvec : ``qlist``\n
            holds the integer :math:`x`\n
        :math:`N` : ``int``\n
            the constant modulo\n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit computes a modular inverse :math:`-x \mod N`. The circuit use classical pre-processing  to get a unitary matrix and use an operation "QOracle" in the QPanda.
    The circuit is an in-place circuit that performs the operation :math:`|x \\rangle \\rightarrow |-x \mod N \\rangle`.
    It can not be extended to compute modulo negation for integer :math:`N` of large bit length.


    Example:
        If :math:`x =7, N=11`, putting :math:`x` held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|00100 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e., :math:`-7 \mod 11=4`.

    .. code-block:: python

        from pyqpanda import *
        import numpy as np
        import math
        from pyqpanda_alg.QLuoShu import VarModNeg
    
        if __name__ == "__main__":
            x = 7
            N = 11
            n = math.ceil(math.log(N, 2))
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
            qvec = qvm.qAlloc_many(n)
    
            prog << bind_nonnegative_data(x, qvec) \\
                 << VarModNeg.VarModNeg(qvec, N)
    
            result = prob_run_dict(prog, qvec, 1)
    
            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("-%d mod %d=%d" % (x, N, c))
    
    .. parsed-literal::
            0100:1.0
            -7 mod 11=4
    """
    pass



