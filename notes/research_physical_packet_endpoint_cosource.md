# Exact endpoint and co-source transport of the physical packet

Private written proof, 17 November 2026. The actual crossing packet
has an exact endpoint reproducing row. Every clock insertion has a
finite support band, which transports an
arbitrary diagonal attachment without changing the exterior observation.
The two signed physical port orders give different matrix units and
retain their original phases. These identities do not give a lower
bound for an arbitrary completed tangle.

## 1. The packet and its endpoint row

Use the odd physical levels \(N>2\) of [P], and put
\[
 d=N-1,\quad Q=e^{2\pi i/N},\quad x=-e^{-\pi i/N},\qquad
 p_j=(Q;Q)_j=\prod_{r=1}^j(1-Q^r),\quad p_0=1.
 \tag{1}
\]
For \(0\le u\le d\), set \(m=N-u\) and
\[
 A_u(J)=\frac{p_{J+u}}{p_Jp_u},\qquad
 C_u(J,v)=p_u A_u(J)Q^{Jv}A_u(v),\quad 0\le J,v<m.
 \tag{2}
\]
This is exactly [P,(24)], with \(u\) its physical transfer index.
The matrix is symmetric and invertible: its diagonal factors are
nonzero and \((Q^{Jv})_{J,v<m}\) is a Vandermonde matrix at the
distinct points \(1,Q,\ldots,Q^{m-1}\).

The finite polynomial generating its first diagonal factor is
\[
 B_u(z):=\sum_{J=0}^{m-1}A_u(J)z^J
   =\frac{1-z^N}{\prod_{r=0}^u(1-Q^rz)}
   =\prod_{r=u+1}^{d}(1-Q^rz).
 \tag{3}
\]
Here the displayed quotient means its polynomial cancellation,
including the removable points. To prove (3), the coefficients of
\(\prod_{r=0}^u(1-Q^rz)^{-1}\) below degree \(N-u\) are
\(p_{J+u}/(p_Jp_u)\). This follows by induction on \(u\):
the factorial quotients obey
\(A_u(J)-Q^uA_u(J-1)=A_{u-1}(J)\), with \(A_u(-1)=0\);
the base \(u=0\) has all coefficients one.
Multiplication by \(1-z^N\) leaves these coefficients unchanged,
and the cyclotomic identity gives the final polynomial of degree
\(N-u-1\). This proves all its coefficients.

In particular \(B_u(1)=p_d/p_u=N/p_u\), while
\(B_u(Q^v)=0\) for \(1\le v<m\). Therefore
\[
 \boxed{\ C_u\mathbf1=N e_0,\qquad
   \mathbf1^{\mathsf T}C_u=N e_0^{\mathsf T},\qquad
   C_u^{-1}e_0=N^{-1}\mathbf1.\ }
 \tag{4}
\]
The first row of \(C_u^{-1}\) is also identically \(1/N\).
This includes \(u=0\), the full Fourier matrix, and \(u=d\),
the one-entry matrix \((N)\). The finite algebra (2)--(4) is
valid for any \(N\ge2\); the physical identifications below retain
the odd-level scope of [P].

## 2. Every clock and arbitrary diagonal attachment

For \(s\in\mathbb Z/N\mathbb Z\), define the attached row
\[
 R_{u,v}(s)=\sum_{J=0}^{m-1}Q^{sJ}C_u(J,v)
          =p_uA_u(v)B_u(Q^{v+s}).
 \tag{5}
\]
Its support is exact. With brackets denoting residues in \(0,\ldots,d\),
put \(a=[-v-s]\). Then
\[
 \boxed{\ R_{u,v}(s)=
 \begin{cases}
 N A_u(v)(-1)^aQ^{a(a+1)/2}{u\brack a}_Q,&0\le a\le u,\\
 0,&a>u,
 \end{cases}\qquad
 {u\brack a}_Q=\frac{p_u}{p_ap_{u-a}}.\ }
 \tag{6}
\]
Indeed the zeros of the product (3) are all root points except
\(Q^{-a}\), \(0\le a\le u\). At those remaining points,
\[
 B_u(Q^{-a})=\frac{p_{d-a}}{p_{u-a}}
 =\frac{N(-1)^aQ^{a(a+1)/2}}{p_ap_{u-a}}.
 \tag{7}
\]
For the last equality, reflect the final \(a\) factors in
\(p_d=N\), using \(1-Q^{-r}=-Q^{-r}(1-Q^r)\).
Thus (6) includes every cyclic seam, not just an unwrapped band.

Before sampling, the holomorphic clock insertion is exactly
\[
 R_{u,v}(z)=\sum_{J=0}^{m-1}z^J C_u(J,v)
                  =p_uA_u(v)B_u(Q^vz).             \tag{7a}
\]
Its specified source diagonal is \(\operatorname{diag}(1,z,\ldots,z^d)\).
All ordinary or logarithmic \(z\)-derivatives are derivatives of
this polynomial, also after the exterior contraction (11).
At an inactive sample \(z_0=Q^s\), put
\(r_0=[-v-s]\in\{u+1,\ldots,d\}\). Its zero is simple, and
\[
 (z\partial_zR_{u,v})(z_0)
 =-p_uA_u(v)\!
   \prod_{\substack{u+1\le r\le d\\r\ne r_0}}
                      (1-Q^{r+v+s})\ne0.           \tag{7b}
\]
Only the vanishing factor differentiates nontrivially there;
\(Q^{r_0+v+s}=1\) gives the sign. Higher jets follow from (7a).
Differentiating the sampled zero in (6) would lose these normals.
This source clock is not identified with a meridian or root deformation.

Let \(D=\operatorname{diag}(d_0,\ldots,d_d)\) be arbitrary.
It can be matrix-valued in a separate coefficient space. Define
\[
 \widehat d_s=\frac1N\sum_{J=0}^d d_JQ^{-sJ},\qquad
 R_{u,v}(D)=\sum_{J=0}^{m-1}d_J C_u(J,v).
\]
Finite Fourier inversion and (6) give
\[
 \boxed{\ R_{u,v}(D)=N A_u(v)\sum_{a=0}^u
    (-1)^aQ^{a(a+1)/2}{u\brack a}_Q
                         \widehat d_{[-v-a]}.\ }
 \tag{8}
\]
Only the actual indices \(J<m\) enter the left side. Consequently
the right side is independent of any change to the other \(d_J\),
although such a change can alter every Fourier coefficient separately.
This is a linear co-source identity; no complex conjugation is used.

For example, for the explicitly specified quadratic diagonal
\[
 d_J^{(p)}=(-1)^{pJ}Q^{pJ(J+1)/2},\qquad p\in\mathbb Z,
 \tag{9}
\]
use exactly
\(\widehat d_{p,s}=N^{-1}\sum_{J=0}^d
 (-1)^{pJ}Q^{pJ(J+1)/2-sJ}\) in (8).
Negative \(p\) is allowed because these entries are units.
When \(N,p\) are odd, the unwrapped formula (9) obeys
\(d_{J+N}^{(p)}=-d_J^{(p)}\). Its cyclic array still consists of
the prescribed \(N\) values. Dropping this half-character, or
using a cyclic Gauss formula which assumes its absence, changes
the attachment. A diagonal (9) alone is not identified with a
whole original crossing power and its other factors.

## 3. Literal signed physical matrix units

Use the same scalar-removed signed matrices as [P,(25a,b)]:
\[
 (M_+^0)_{u+v,J;\,J+u,v}=x^{-J-v}C_u(J,v),
 \qquad
 (M_-^0)_{J,d-v;\,d-u-v,J+u}=x^{d-u-J-v}C_u(J,v).
 \tag{10}
\]
Their supported indices are exactly \(J,u,v\ge0\),
\(J+u,u+v\le d\). The common crossing scalars, framing factors
and other exterior source lines remain outside \(M_\pm^0\),
as in [P]. Restoring a common scalar multiplies the respective
identities below by that same scalar.

On a physical head let
\[
 S|j\rangle=|j+1\rangle\ (j<d),\quad S|d\rangle=0,
 \qquad D_x|j\rangle=x^j|j\rangle,
\]
and let \(P|a,b\rangle=|b,a\rangle\) be the literal head flip.
For \(E_{ab}=|a\rangle\langle b|\), ordinary partial traces give
\[
 \boxed{\begin{aligned}
 \operatorname{Tr}_1[((S^uD_xD)\otimes I)P M_+^0]
   &=\sum_{v=0}^{d-u}x^{-v}R_{u,v}(D)E_{u+v,v},\\
 \operatorname{Tr}_2[(I\otimes S^uD_xD)P M_-^0]
   &=\sum_{v=0}^{d-u}x^{d-u-v}R_{u,v}(D)E_{d-v,d-u-v}.
 \end{aligned}\ }
 \tag{11}
\]
For the first line, the traced input is \(J+u\), its output
before \(S^u\) is \(J\), and the insertion contributes \(x^Jd_J\).
Integer conservation fixes the remaining output to \(u+v\).
Its sum is \(x^{-v}\sum_Jd_JC_u(J,v)\) by (10).
For the second line, trace the second head with the same
\(J\mapsto J+u\); the remaining input/output are respectively
\(d-u-v,d-v\). Equation (10) gives its displayed phase.
The finite endpoint of \(S\) supplies exactly \(J\le d-u\).
This proves both lines, including \(u=0,d\).

Setting \(D=I\) in (11) yields
\[
 \boxed{\begin{aligned}
 \operatorname{Tr}_1[((S^uD_x)\otimes I)P M_+^0]
      &=N E_{u0},\\
 \operatorname{Tr}_2[(I\otimes S^uD_x)P M_-^0]
      &=N x^{d-u}E_{d,d-u}.
 \end{aligned}\ }
 \tag{12}
\]
These are different signed physical matrix units.
Coefficient symmetry in \(J,v\) does not interchange their ports.

For \(u=0\), the positive matrix in (11) with the clock \(D(z)\)
equals \(\sum_v x^{-v}B_0(Q^vz)E_{vv}\). At \(z=1\) it is
\(NE_{00}\), but its first logarithmic derivative is the full-rank matrix
\[
 \mathcal N=\frac{Nd}{2}E_{00}
       -N\sum_{v=1}^d\frac{x^{-v}}{1-Q^v}E_{vv}.     \tag{12a}
\]
This follows by differentiating \(B_0(w)=(1-w^N)/(1-w)\);
its removable value at \(w=1\) is differentiated as a polynomial.
Let \(Z|v\rangle=Q^v|v\rangle\). In the Euclidean head norm,
\[
 \mathcal N^{-1}=\frac{2}{Nd}E_{00}-\frac1N D_x(I-Z),\qquad
 \|\mathcal N\|\le\frac{N^2}{2},\quad
 \|\mathcal N^{-1}\|\le\frac2N.                     \tag{12b}
\]
These follow entrywise from \(4/N\le|1-Q^v|\le2\), \(v\ne0\).
Thus this specified clock normal has condition number at most \(N\).

## 4. The original exterior observation remains specified

For any exterior head operator \(A\), with all its original
spectator contractions retained, (12) at \(u=0\) gives
\[
 \operatorname{Tr}(A E_{00})
 =\frac1N\operatorname{Tr}_{1,2}
       [(D_x\otimes A)P M_+^0],
 \qquad
 \operatorname{Tr}(A E_{dd})
 =\frac{x^{-d}}N\operatorname{Tr}_{1,2}
       [(A\otimes D_x)P M_-^0].
 \tag{13}
\]
These are exact replacements of the specified physical cut rows,
valid for arbitrary exteriors, rather than inferred scalarity of a
partial tangle. For \(u>0\), the corresponding traces select
\(A_{0u}\) and \(A_{d-u,d}\). Arbitrary diagonal insertions are
instead given by (8),(11); their coherent sums need not be nonzero.
All identities hold coefficientwise in spectator parameters, so
parameter derivatives retain every differentiated factor.

The clock \(D_x\), finite shift and flip in (11)--(13) are part
of the replacement. They are not the unmodified pivotal cap, and
the flip is not an added physical crossing. No original pivot or
external co-source may be deleted on the strength of (12).
Likewise \(C_u\) is a fixed-transfer boundary array: its indices
range across different physical total degrees in (10). Its matrix
inverse is not asserted to be an inverse physical crossing or a
closed composition channel. Composition retains the actual sums
over transfer indices and the attached exteriors.

The endpoint recovery gives no positive-functional or noncancellation theorem.

## Complete direct source

[P] [The finite nine-cell boundary chart and its actual residue packet](research_nine_cell_pentagon_boundary_and_residue.md),
SHA256 a5722ff57bb9e228a724f863c149e05def8794ffc17c92f8afc5d1afd7e288cf.
The complete text and its physical port identities were checked.
All further identities are proved above; no mathematical programs were used.
