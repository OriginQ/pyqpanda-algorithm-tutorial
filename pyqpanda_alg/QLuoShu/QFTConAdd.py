from pyqpanda import *
import numpy as np
import math

from .. config import *
auth = Authorization()

def egcd(a, b):
    """
    Extended Euclid's Algorithm.

    Parameters:
        :math:`a`: ``int`` \n
            an integer \n
        :math:`b`: ``int``\n
            an integer \n

    Return:
        triples : :math:`(g,x,y)`  satisfying:  :math:`ax+by=g` \n

    Compute the g.c.d. of the integers :math:`a` and :math:`b`.
    The returning result is (g, u,v) satisfying :math:`u*a+v*b=g`.

    Example:

    .. code-block:: python

        from pyqpanda import *
        import numpy as np
        import math

        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                g, y, x = egcd(b % a, a)
                return g, x - (b // a) * y, y
        print(egcd(12,3))
    
    .. parsed-literal::
        (3, 0, 1)

    """
    pass


def modinv(a, N):
    """
    Modulo Inversr Algorithm.

    Parameters:
        :math:`a`: ``int`` \n
            an integer \n
        :math:`N`: ``int``\n
            an integer \n

    Return:
        value: :math:`a^{-1} \mod N`\n

    Compute the inverse :math:`a^{-1} \mod N`.

    Example:

    .. code-block:: python

        def modinv(a, N):
            g, x, y = egcd(a, N)
            if g != 1:
                raise Exception('Waring: Modulo inverse is not exist.')
            else:
                return x % N

        print(modinv(3,11))
    
    .. parsed-literal::
        4

    """
    pass


def getAngles(a, n):
    """
    Get the Array of Phases.

    Parameters:
        :math:`a`: ``int`` \n
            an integer expanded in QFT \n
        :math:`n`: ``int``\n
            represent :math:`n` arry with angles of :math:`a` expended in QFT \n

    Return:
        array \n

    Calculate the array of phases used in the Quantum Fourier transform.

    Example:

    .. code-block:: python

        def getAngles(a, n):
            s = bin(int(a))[2:].zfill(n)
            angles = np.zeros([n])
            for i in range(0, n):
                for j in range(i, n):
                    if s[j] == '1':
                        angles[n - i - 1] += math.pow(2, -(j - i))
                angles[n - i - 1] *= np.pi
            return angles
        print(getAngles(3,5))
    
    .. parsed-literal::
        [3.14159265 4.71238898 2.35619449 1.17809725 0.58904862]

    """
    pass


def QFTConAdd(a, qvec):
    """
    Quantum Circuit of Constant Addition using QFT.

    Parameters:
        :math:`a`: ``int`` \n
            the integer to be added \n
        qvec : ``qlist``\n
            the qubits list \n

    Return:
        circuit: ``pq.QCircuit``\n

    The circuit works on one quantum register :math:`|qvec \\rangle` holding the input integer :math:`x` and one
    phase array from classical computation on a constant integer :math:`a` to compute addition using QFT. The circuit
    is an in-place circuit, where the result of addition is deposited in the register :math:`|qvec \\rangle`. The
    circuit needs :math:`n+1` qubits with :math:`n=\max\{\\lceil \log_{2}a \\rceil, \\lceil \log_{2}x \\rceil\}`. The
    circuit is invertible, which can compute the subtraction of two integers.

    Example:
        If :math:`a =7, x=9`, putting x held in :math:`|qvec \\rangle`. By the circuit, the result :math:`|10000 \\rangle` will be held in the :math:`|qvec \\rangle`, i.e, :math:`7+9=16`.

    .. code-block:: python

        from pyqpanda import *
        import numpy as np
        import math
        from pyqpanda_alg.QLuoShu import QFTConAdd

        if __name__ == "__main__":
            qvm = init_quantum_machine(QMachineType.CPU)
            prog = QProg()

            a = 7
            x = 9
            n = max(math.ceil(math.log(x, 2)), math.ceil(math.log(a, 2)))+1
            qvec = qvm.qAlloc_many(n)

            prog << bind_nonnegative_data(x, qvec)\\
                 << QFTConAdd.QFTConAdd(a, qvec)
            result = prob_run_dict(prog, qvec, 1)

            for key in result:
                print(key + ":" + str(result[key]))
                d = int(key, 2)
            print("%d+%d=%d" % (x,a,d))

    .. parsed-literal::
            10000:1.0000000000000018
            9+7=16


    Note that: if :math:`a=x` and they are a power of 2, we need to make :math:`n=\\lceil \log_{2}a \\rceil+2` in the Example.

    Here, we give the circuit graph of the example in the above for the constant addition with 5 qubits:

     .. parsed-literal::
                                               ┌─┐                 ┌────────────┐   ┌─┐ 
        q_0:  |0>───────■────── ───────■────── ┤H├ X────────────── ┤RZ(1.374447)├ X ┤H├ ─────────■──────── ─────────■──────── >
                        │┌─┐    ┌──────┴─────┐ └─┘ │┌────────────┐ └────────────┘ │ └─┘ ┌────────┴───────┐          │┌─┐      >
        q_1:  |0>───────┼┤H├─── ┤CR(1.570796)├ X── ┼┤RZ(2.748894)├ X───────────── ┼ ─── ┤CR(1.570796).dag├ ─────────┼┤H├───── >
                 ┌──────┴┴─┴──┐ ├────────────┤ │   │└────────────┘ │              │     └────────────────┘ ┌────────┴┴─┴────┐ >
        q_2:  |0>┤CR(0.785398)├ ┤RZ(5.497787)├ ┼── ┼────────────── ┼───────────── ┼ ─── ────────────────── ┤CR(0.785398).dag├ >
                 └────────────┘ └────────────┘ │   │┌────────────┐ │              │                        └────────────────┘ >
        q_3:  |0>────────────── ────────────── X── ┼┤RZ(4.712389)├ X───────────── ┼ ─── ────────────────── ────────────────── >
                                                   │└────────────┘ ┌────────────┐ │                                           >
        q_4:  |0>────────────── ────────────── ─── X────────────── ┤RZ(3.141593)├ X ─── ────────────────── ────────────────── >
                                                                   └────────────┘



    """
    pass



