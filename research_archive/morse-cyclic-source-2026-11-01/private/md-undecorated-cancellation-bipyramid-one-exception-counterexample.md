# A single unprotected spectral variation already produces a remainder

The odd-level identity at the box adjoining the protected edge does not
extend to all positions. The smallest level and equator size in the
stated class already give an exact counterexample: \(N=3\), \(m=6\),
with the exceptional north box at position \(3\). In the original
raw source normalization,
\[
 \boxed{
 D_3(-2,-2,-2,\sigma,-2,-2)
       =2\cdot9^5(\sigma-1)(\sigma+2).
 }
 \tag{1}
\]
In particular the value at \(\sigma=2\) is \(472392\). This is
an exact polynomial identity, not an asymptotic observation. It
does not contradict the proved identity for exceptional position
\(0\), and gives no conclusion about a spectral exponential gap.

## The original local matrix and its full one-sided part

At \(N=3\), \(d=2\), the genuine face Casimir is
\[
 C(x,y)=
 \begin{pmatrix}
 1&-3(x+y)&-3xy\\
 0&-2&-3(x+y)\\
 0&0&1
 \end{pmatrix},\qquad
 \chi_3(z)=z^3-3z+2.
 \tag{2}
\]
Thus the full root-normal resolvent polynomial is
\[
 V_3(\sigma;C)=C^2+\sigma C+(\sigma^2-3)I.
 \tag{3}
\]
The original homogeneous source is
\(H_\sigma(x,b,c,y)=\sum_{i\le j}b^ic^{2-j}V_3(\sigma;C)_{ij}\).
Direct matrix multiplication gives
\[
 \begin{aligned}
 H_\sigma={}&(\sigma-1)(\sigma+2)(b^2+c^2)
             +(\sigma-1)^2bc\\
 &-3(\sigma-1)(x+y)(b+c)
             +9(x+y)^2-3(\sigma+2)xy.
 \end{aligned}
 \tag{4}
\]
The one-sided entries are precisely \((i,j)=(0,0)\) and \((2,2)\).
Consequently
\[
 H_\sigma-H_{\sigma,\mathrm C}
      =(\sigma-1)(\sigma+2)(b^2+c^2),
 \qquad
 H_{-2}=H_{-2,\mathrm C}=9P,
 \tag{5}
\]
where
\[
 P(x,b,c,y)=bc+(x+y)(b+c)+(x+y)^2.
 \tag{6}
\]
The central row has not been removed. In particular (3) is full
polynomial functional calculus at the repeated root \(1\), not
interpolation using only its value.

## The shared source and its two surviving monomial selections

Use the original opposite-offset factors
\(H(0,z_{j-1},z_{j+1},z_j)\) at odd \(j\), and
\(H(S,z_{j+1},z_{j-1},z_j)\) at even \(j\), with \(z_0=0\).
Every ordinary face retains target degree two. At position \(3\),
the one-sided part is proportional to \(z_2^2+z_4^2\). Since all
other boxes are at \(-2\), their full and CROSS factors agree.
Therefore their difference is exactly
\[
 9^5(\sigma-1)(\sigma+2)
 [S^2z_1^2z_2^2z_3^2z_4^2z_5^2]
       (z_2^2+z_4^2)P_0P_1P_2P_4P_5,
 \tag{7}
\]
with
\[
 \begin{aligned}
 P_0&=z_1z_5+S(z_1+z_5)+S^2,\\
 P_1&=z_1z_2+z_1^2,\\
 P_2&=z_1z_3+(S+z_2)(z_1+z_3)+(S+z_2)^2,\\
 P_4&=z_3z_5+(S+z_4)(z_3+z_5)+(S+z_4)^2,\\
 P_5&=z_4z_5+z_5^2.
 \end{aligned}
 \tag{8}
\]
All coefficients in these polynomials are nonnegative integers.
For the exceptional monomial \(z_2^2\), its two degrees force
\(P_1\) to supply \(z_1^2\). The remaining \(z_1\) and
\(z_2\) degrees are now zero. Thus \(P_0\) must supply either
\(Sz_5\) or \(S^2\), while \(P_2\) must supply either
\(Sz_3\) or \(S^2\). The shared south target is only two, so
the only choices are \(Sz_5\) and \(Sz_3\). The remaining
face targets then force \(P_5=z_4z_5\) and \(P_4=z_3z_4\).
This gives exactly one monomial selection, with coefficient one:
\[
 (Sz_5)\,(z_1^2)\,(Sz_3)\,(z_2^2)\,
                 (z_3z_4)\,(z_4z_5).
 \tag{9}
\]
Reflection gives exactly one selection for the exceptional monomial
\(z_4^2\):
\[
 (Sz_1)\,(z_1z_2)\,(z_2z_3)\,(z_4^2)\,
                 (Sz_3)\,(z_5^2).
 \tag{10}
\]
Both products have the original shared target in (7). Their sum has
coefficient two, proving (1). There is no sign cancellation hidden
in this count: the only spectral sign is the displayed common factor
\((\sigma-1)(\sigma+2)\).

## Complete position table at this smallest level

The same direct coefficient extraction at \(N=3,m=6\) gives
\[
 D_3(-2,\ldots,\sigma_j,\ldots,-2)
       =9^5 K_j(\sigma_j-1)(\sigma_j+2),
 \qquad
 (K_0,K_1,K_2,K_3,K_4,K_5)=(0,11,4,2,4,11).
 \tag{11}
\]
The contributions from the exceptional LEFT and RIGHT entries are
respectively
\[
 K^{\mathrm L}=(0,11,0,1,4,0),\qquad
 K^{\mathrm R}=(0,0,4,1,0,11).
 \tag{12}
\]
These coefficients are also checked by the accompanying standalone
integer runner, which independently constructs the matrices (2)–(3)
and compares FULL minus CROSS with the positive support count (6).

For the protected position \(0\), the zero in (11) is already a
degree obstruction: its two one-sided monomials are \(z_1^2\) and
\(z_5^2\), while \(P_1\) and \(P_5\) necessarily contribute a
further positive degree to those faces. The separate odd-level proof
extends this obstruction to every odd \(N\); it does not extend it
to the other positions.

Writing \(\eta_j=\sigma_j+2\), the one-variable restriction in
(11) is \(9^5K_j(\eta_j^2-3\eta_j)\). Thus even a single first
spectral derivative can survive at the complete endpoint:
\[
 \left.\partial_{\sigma_3}D_3\right|_{\boldsymbol\sigma=-2}
              =-6\cdot9^5=-354294.
 \tag{13}
\]
Mixed spectral variations are not required to create a remainder.
This is a finite support and polynomial statement only; the strict
global remainder estimate remains a separate question.
