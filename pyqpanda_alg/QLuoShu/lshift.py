from pyqpanda import *
import math

from .. config import *
auth = Authorization()

def lshift(qvec):
    """
    Quantum Circuit of A binary Doubling Operation :math:`*2`.

    Parameters:
        qvec: ``qlist``\n
            the qubits list\n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit is by the SWAP operation to shift the qubits in the quantum registers to the left sequentially by bits.  It works in place with an ancilla qubit
    that compute :math:`|x \\rangle \\rightarrow |2x \\rangle`. Therefore, it uses only :math:`n+1` qubits with :math:`n=\\lceil \log_{2}x \\rceil`.

    Example:
        If :math:`x=13`, putting :math:`x` held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|11010 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e., :math:`2x=26`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import lshift

        if __name__ == "__main__":
            x = 13
            n = math.ceil(math.log(x, 2)) + 1
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()
            qvec = qvm.qAlloc_many(n)

            prog << bind_nonnegative_data(x, qvec) \\
                 << lshift.lshift(qvec)
            result = prob_run_dict(prog, qvec, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                c = int(key, 2)
            print("2*%d=%d" % (x, c))
    
    .. parsed-literal::
            11010:1.0
            2*13=26


    Note that: if :math:`x` is a power of 2, we need to let :math:`\\lceil \log_{2}x \\rceil+2` qubits.

    Here, we give the circuit graph of the example in the above with 5 qubits in the following:

     .. parsed-literal::
        q_0:  |0>── ─ ─ X
                        │
        q_1:  |0>── ─ X X
                      │
        q_2:  |0>── X X ─
                    │
        q_3:  |0>─X X ─ ─
                  │
        q_4:  |0>─X ─ ─ ─

    """
    pass




