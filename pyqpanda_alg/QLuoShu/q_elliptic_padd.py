
from pyqpanda import *
import math
from .VarModAdd import VarModAdd
from .VarModMul import VarModMul
from .VarModInv import VarModInv
from .VarModSqr import VarModSqr
from .ConModAdd import ConModAdd
from .VarModNeg import VarModNeg

from .. config import *
auth = Authorization()


def q_elliptic_padd(p,a,b,P,Q):
    """
    Quantum Circuit for Point Addition of Elliptic Curves over Prime Field (:math:`p>2`).

    Parameters:
        :math:`p`: ``int`` \n
            represents the character of the prime field :math:`\mathbb{F}_{p}`\n
        :math:`a,b` : ``int``\n
            represent an elliptic curve :math:`E/\mathbb{F}_{p}: y^{2}=x^{3}+ax+b`\n
        :math:`P,Q`: ``vector``\n
            represent different points on the elliptic curve :math:`E/\mathbb{F}_{p}`\n

    Return:
        The quantum states of the :math:`x-` coordinate and :math:`y-` coordinate of :math:`P+Q`. \n

     The function is used to compute point addition :math:`P+Q` with :math:`P \\neq Q` on elliptic curves :math:`y^{2}=x^{3}+ax+b` over finite field :math:`\mathbb{F}_{p}` with :math:`p>3`. 
     The circuit of point addition is constructed by some variant modulo arithmetic and based on classical addition formulas. The circuit is inverse and can be used to compute :math:`P-Q`.

    Example:
        If :math:`E/\mathbb{F}_{11}: y^{2}=x^{3}+7x+9`, :math:`P =(0,3), Q=(6，5)`, by the function, we can get the quantum state of :math:`P + Q`, which is :math:`|1010 \\rangle|0001 \\rangle`. So, :math:`P+Q=(10,1)`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import q_elliptic_padd

        if __name__ == "__main__":
            p = 11
            a = 7
            b = 9
            P = [0, 3]
            Q = [6, 5]
            q_elliptic_padd.q_elliptic_padd(p, a, b, P, Q)

    The function above would give results:
    
    .. parsed-literal::
        The elliptic curve：y^{2}=x^{3}+7x+9\n
        P=(0,3)\n
        Q=(6,5)\n
        1010 :1.0000000000000895\n
        0001 :1.0000000000000895\n       
        P+Q=(10,1)

    """
    pass









