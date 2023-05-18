from pyqpanda import *
import math
from .VarModMul import VarModMul
from .VarModInv import VarModInv
from .ConModAdd import ConModAdd
from .VarModNeg import VarModNeg
from .VarModSqr import VarModSqr
from .ConModMul import ConModMul

from .. config import *
auth = Authorization()

def q_elliptic_pdou(p,a,b,P):
    """
    Quantum Circuit for Point Addition of Elliptic Curves over Prime Field (:math:`p>2`).

    Parameters:
        :math:`p`: ``int`` \n
            represents the character of prime field :math:`\mathbb{F}_{p}`\n
        :math:`a,b` : ``int``\n
            represent an elliptic curve :math:`E/\mathbb{F}_{p}: y^{2}=x^{3}+ax+b`\n
        :math:`P`: ``vector``\n
            represents a point on the elliptic curve :math:`E/\mathbb{F}_{p}`\n

    Return:
        The quantum states of the :math:`x-` coordinate and :math:`y-` coordinate of :math:`[2]P`.\n


     The function is used to compute point addition :math:`P+Q` with :math:`P \\neq Q` on elliptic curves :math:`y^{2}=x^{3}+ax+b` over finite field :math:`\mathbb{F}_{p}` (:math:`p>2`).
     The circuit of point doubling is constructed by some variant modulo arithmetic and based on classical addition formulas.

    Example:
       If :math:`E/\mathbb{F}_{11}: y^{2}=x^{3}+7x+9`, :math:`P =(5,2)`, by the function, we can get the quantum state of :math:`[2]P`, which is :math:`|0110 \\rangle|0101 \\rangle`.
       So, :math:`[2]P=(6,5)`.

    .. code-block:: python

        from pyqpanda import *
        import math
        from pyqpanda_alg.QLuoShu import q_elliptic_pdou

        if __name__ == "__main__":
            p = 11
            a = 7
            b = 9
            P = [5, 2]
            q_elliptic_pdou.q_elliptic_pdou(p, a, b, P)

    The function above would give results:
    
    .. parsed-literal::
        The elliptic curve：y^{2}=x^{3}+7x+9\n
        P=(5,2)\n
        0110 :1.0000000000000255\n
        0101 :1.0000000000000255\n
        2P=(6,5)

    """
    pass


