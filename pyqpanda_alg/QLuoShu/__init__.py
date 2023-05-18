"""
Fundamental Components of Quantum Arithmetic Based on **QLuoShu**.

We extract some common quantum arithmetics from QLuoShu, including QFT quantum adder,
constant modular arithmetics, variant modular arithemetics, point addition or doubling of elliptic curves,
which are the fundamental components of quantum algorithms applied to cryptography.

The QFT quantum adder **'QFTConAdd'** is an in-place circuit for computing :math:`|x\\rangle \\rightarrow
|a+x\\rangle`. Then, the four circuits including **'ConModAdd,ConModaddmul,ConModMul,ConModExp'** are constructed to
compute modular addition :math:`|x\\rangle \\rightarrow |a+x \mod N \\rangle`, modular addition-multiplication
:math:`|x\\rangle|b\\rangle \\rightarrow |x\\rangle|b+ax \mod N \\rangle`, modular multiplication
:math:`|x\\rangle|0\\rangle \\rightarrow |ax \mod N \\rangle|0\\rangle` and modular exponention
:math:`|x\\rangle|0\\rangle|0\\rangle \\rightarrow |x\\rangle|0\\rangle|a^{x} \mod N \\rangle`, which are based on
the QFT quantum adder with a constant integer :math:`a` and a constant integer modulo :math:`N`. The constant in
these circuits means that it is treated as a classical data rather than a quantum state. The circuit **'lshift'** is
a special circuit to compute :math:`|x\\rangle \\rightarrow |2x\\rangle` with only some Swap quantum gates.

Variant modular arithemetics inculding **'VarModAdd,VarModDou,VarModMul,VarModSqr'** are constructed to compute
modular addition :math:`|x\\rangle|y\\rangle \\rightarrow |x+y \mod N \\rangle|y\\rangle`, modular doubling
:math:`|x\\rangle \\rightarrow |2x \mod N \\rangle`, modular multiplication :math:`|x\\rangle|y\\rangle|0\\rangle
\\rightarrow |x\\rangle|y\\rangle|x*y \mod N \\rangle` and modular squaring :math:`|x\\rangle|0\\rangle \\rightarrow
|x\\rangle|x^{2} \mod N \\rangle`. Note that these three circuits **'VarModDou,VarModMul,VarModSqr'** are only
suitable for odd modulo :math:`N`. Here, we also give two special quantum circuits **'VarModInv,VarModNeg'** to
compute modular inverse :math:`|x\mod N\\rangle \\rightarrow |x^{-1}\mod N\\rangle` and modular negativation
:math:`|x\mod N\\rangle \\rightarrow |-x\mod N\\rangle`, which are in-place circuits using the oparation 'QOracle' in
the QPanda.

The point addition quantum operation **'q_elliptic_padd'** is used to compute two different points
:math:`|P+Q\\rangle` on elliptic curves over prime field with the character larger than 3. The point doubling quantum
operation **'q_elliptic_pdou'** is used to compute a doubling of a point :math:`|[2]P\\rangle` on elliptic curves
over prime field with the character larger than 3. These two quantum circuits are different, so we give different
algorithm introductions and solution interfaces.

"""

from . import ConModAdd
from . import ConModaddmul
from . import ConModExp
from . import ConModMul
from . import lshift
from . import q_elliptic_padd
from . import q_elliptic_pdou
from . import QFTConAdd
from . import VarModAdd
from . import VarModDou
from . import VarModInv
from . import VarModMul
from . import VarModNeg
from . import VarModSqr


__all__ = [ConModAdd, ConModaddmul, ConModExp, ConModMul, lshift, q_elliptic_padd, q_elliptic_pdou, QFTConAdd, VarModAdd, VarModDou, VarModInv, VarModMul, VarModNeg, VarModSqr]
