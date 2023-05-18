
from .. config import *
auth = Authorization()

def vqe_solver(matrix,para):
    """
    Solving the minimum eigenvalue of a real Hermitian matrix.\n

    Parameters:
        matrix : ``2Darray`` \n
            represents input the matrix.The matrix need to be a real Hermitian matrix.\n
        para : ``list[float64]`` \n
            represent input initial parameter list.\n

    Return:
        minimum eigenvalue : ``float64``\n

    Example:

    .. code-block:: python

        from pyqpanda_alg.VQE.vqe import vqe_solver
        result = vqe_solver([[1,2],[2,1]],[2,3])
        print(result)

    The function above would give results:

    .. code-block:: python

        -0.9999051299709187

    """
    pass

def hardware_efficient_circuit(qubit_num,para_list,quantum_machine):
    """
    Building Hardware Efficient Ansatz quantum circuit.\n

    Parameters:
        qubit_num : ``int`` \n
            represents input the number of qubits, number of qubits should be larger than 1.\n

        para_list : ``list[float64]`` \n
            represent input initial parameter list.\n

        quantum_machine : ``quantum_machine`` \n
            represent quantum machine class.\n

    Return:
        circuit : ``QCircuit`` \n

    Example:

    .. code-block:: python

        from pyqpanda_alg.VQE.vqe import hardware_efficient_circuit
        import numpy as np
        import pyqpanda

        nqubit = 2
        init_para = np.zeros(4*nqubit)
        qvm = pyqpanda.CPUQVM()
        qvm.initQVM()
        circuit = hardware_efficient_circuit(nqubit,init_para,qvm)
        print(circuit)

    .. parsed-literal::
 
                  ┌────────────┐ ┌────────────┐ ┌────────────┐                ┌────────────┐
        q_0:  |0>─┤RZ(0.000000)├ ┤RX(0.000000)├ ┤RZ(0.000000)├ ───────■────── ┤RY(0.000000)├
                  ├────────────┤ ├────────────┤ ├────────────┤ ┌──────┴─────┐ └──────┬─────┘
        q_1:  |0>─┤RZ(0.000000)├ ┤RX(0.000000)├ ┤RZ(0.000000)├ ┤RY(0.000000)├ ───────■──────
                  └────────────┘ └────────────┘ └────────────┘ └────────────┘


    """
    pass