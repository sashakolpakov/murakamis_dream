# Exact rank loss and the remaining physical normal

Private written proof, 16 November 2026.

At a simple rank loss of an actual finite-level leading coefficient,
the first-normal equation recovers a missing next value. It generally
leaves one next normal undetermined. This note identifies that channel,
gives the exact criterion for additional rows to remove it, and shows
that the original closing trace sees it. A classical exceptional color
alone does not imply such a finite-level rank loss.

## 1. The actual equations at a physical row

Use the original algebra and trace
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 \phi_N(f)=\eta N^2[Z^{N-1}]\operatorname{can}(f),
 \quad \eta=(-1)^{N-1}.
 \tag{1}
\]
The distinct double nodes are
\[
 c_j=2\cos((2j+1)\pi/N),\qquad 0\le j<\lfloor N/2\rfloor.
\]
When \(N\) is odd there is also the simple node \(-2\).
Set
\[
 h=N^{-1},\qquad C_N(u)=2\cos(2\pi u+\pi/N).
\]
The full-step source equations in the first pinned source have ordinary
residuals divisible by \(P_N\), before their physical evaluation. In
this coordinate,
\[
 P_N(C_N(u))=4\sin^2(\pi Nu).
 \tag{2}
\]
Consequently their values and first \(u\)-derivatives vanish at
\(u=j/N\). These are derivatives of ordinary residuals, not a
derivation of the physical quotient.

Consider one such finite-order row, possibly with several components.
Move all already specified values and normals to the right. Suppose
the only unknown value packet is
\(x=F(u_0+mh)\in\mathbb C^d\), and its unknown first-normal packet is
\(y=F'(u_0+mh)\). The two equations are exactly
\[
                  A x=b,\qquad A y+\dot A x=\dot b .
 \tag{3}
\]
Here \(A\) is the full finite-\(N\) coefficient at \(u_0\),
\(\dot A\) is its ordinary \(u\)-derivative, and \(\dot b\) includes
every derivative of the coefficients and known shifted values on the
right. A dot in (3) never means that the unknown packet is held
constant when the ordinary source equation is differentiated.
The level and all exterior parameters are fixed in this calculation.

Equation (3) also applies to a larger future packet, with rectangular
\(A\), after all its unknown shifted values are included. A row involving
another unknown future value cannot be stacked as an equation for
\(x\) alone by treating that extra value as known.

## 2. A simple square rank loss

**Theorem 1.** Let \(A(u)\) be a holomorphic \(d\)-by-\(d\) matrix
near \(u_0\). Suppose
\[
 \operatorname{rank}A(u_0)=d-1,\qquad
 \ker A(u_0)=\mathbb C r,\qquad
 \ker A(u_0)^{\mathsf T}=\mathbb C\ell^{\mathsf T},
 \qquad \ell\dot A r\ne0.
 \tag{4}
\]
The vectors \(\ell,r\) are nonzero, and no conjugation is used in
\(\ell\dot A r\). The system (3) is solvable if and only if
\(\ell b=0\). When it is solvable, its value \(x\) is unique and its
normal \(y\) has precisely one undetermined scalar:
\[
 \begin{split}
 Ax_p&=b,\\
 x&=x_p+
       \frac{\ell(\dot b-\dot A x_p)}{\ell\dot A r}\,r,\\
 Ay_p&=\dot b-\dot A x,\qquad
 y=y_p+\zeta r,\quad \zeta\in\mathbb C.
 \end{split}
 \tag{5}
\]
The condition in (4) is equivalent to a simple zero of
\(\det A(u)\) at \(u_0\).

*Proof.* The range of \(A\) is \(\ker\ell\), so the value equation
is solvable precisely when \(\ell b=0\). Its solutions are
\(x_p+zr\). The normal equation is solvable precisely when
\(\ell(\dot b-\dot A x_p-z\dot A r)=0\). This uniquely gives
the displayed \(z\); the solutions for \(y\) then differ by
\(\ker A\). Changing \(x_p\) changes \(z\) by the opposite
multiple, so \(x\) is independent of that choice.

At a rank-\((d-1)\) matrix, its adjugate is a nonzero scalar
multiple of \(r\ell\). Thus
\((\det A)'=\operatorname{tr}(\operatorname{adj}(A)\dot A)\)
is a nonzero scalar multiple of \(\ell\dot A r\). This proves
the last assertion. \(\square\)

In the scalar case, \(A(u_0)=0\), \(\dot A(u_0)\ne0\).
The exact equations reduce to
\[
                     b=0,\qquad x=\dot b/\dot A,
 \tag{6}
\]
and leave \(y\) arbitrary. Thus first normals supply the missing
value row; they do not themselves supply a full next-state transfer.

The same fact has a local-algebra description. At a double spectral
node \(c\), put \(\epsilon=Z-c\). In
\(\mathbb C[\epsilon]/(\epsilon^2)\), multiplication by a
coefficient with a simple zero is
\[
 (a_1\epsilon)(f_0+f_1\epsilon)=a_1f_0\epsilon .
 \tag{7}
\]
It detects the value and kills the remaining normal component.
This is an exact statement about the retained nilpotent, not about a
reduced value-only quotient.

## 3. All aligned rows and their precise recovery criterion

**Theorem 2.** Stack any collection of actual rows aligned on the
same unknown value packet, obtaining
\[
                     Bx=b,\qquad By+\dot Bx=\dot b ,
 \tag{8}
\]
where \(B:\mathbb C^d\to\mathbb C^p\). Assume that at least one
solution exists, as it does for the original source with its actual
previous data. Define
\[
 K=\ker B,\qquad
 \pi:\mathbb C^p\longrightarrow\operatorname{coker}B,\qquad
 H=\left.\pi\dot B\right|_K .
 \tag{9}
\]
Then the possible differences of value packets are precisely
\(\ker H\subseteq K\). For each fixed admissible value packet,
the possible normals form a translate of \(K\). In particular:

* the value is unique if and only if \(H\) is injective;
* the full value-and-normal packet is unique if and only if
  \(B\) has full column rank.

*Proof.* Subtract two solutions. The resulting equations are
\[
 B\,\delta x=0,\qquad B\,\delta y=-\dot B\,\delta x .
 \tag{10}
\]
The second is solvable precisely when
\(\pi\dot B\,\delta x=0\). Every \(\delta x\in\ker H\)
therefore occurs, and its corresponding \(\delta y\)'s differ
by \(K\). For \(\delta x=0\), every element of \(K\) is an
allowed \(\delta y\), irrespective of \(H\). This proves both
criteria. \(\square\)

In Theorem 1, suppose further actual rows have coefficient matrix
\(C\) on the same future value packet. Once its value has been
fixed by (5), the additional normal equations determine \(\zeta\)
if and only if
\[
                              Cr\ne0.
 \tag{11}
\]
Indeed the stacked coefficient is \((A^{\mathsf T},C^{\mathsf T})^{\mathsf T}\),
whose kernel is \(\mathbb Cr\cap\ker C\). More generally, independent
normal constraints applied after the value is known remove the
remaining normal exactly when their restriction to \(K\) is
injective. All right sides must still be the original compatible
source data.

These are statements about the equations at this row. Later rows,
other recovery equations, or the original global closing conditions
may determine the remaining scalar even when (11) fails locally.
Theorem 2 neither discards those equations nor asserts a free
parameter in the globally defined source.

## 4. The original trace sees the remaining normal

For every double node \(c\), including the sole node at \(N=2\),
\[
                 P_N''(c)=\frac{2N^2}{4-c^2}.
 \tag{12}
\]
Define the ordinary polynomial of degree \(N-1\)
\[
 R_c(Z)=\frac{2P_N(Z)}{P_N''(c)(Z-c)}
       =\frac{(4-c^2)P_N(Z)}{N^2(Z-c)}.
 \tag{13}
\]
Division in this formula is exact ordinary polynomial division.
The value of \(R_c\) at every physical node is zero.
Its derivative is one at \(c\) and zero at every other double
node. At odd \(N\) its value at the simple node \(-2\) is also
zero. These facts follow directly from the root multiplicities
of \(P_N\).

**Proposition 3.** For every original spectator \(g\in\mathcal A_N\),
\[
                    \phi_N(R_c g)=\eta(4-c^2)g(c).
 \tag{14}
\]
The identity holds coefficientwise with arbitrary ordinary exterior
variables and their fixed derivatives retained.

*Proof.* At the double node \(c\), the only nonzero jet of
\(R_c g\) is its derivative \(g(c)\). All other physical jets
vanish. Hence \(R_c g=g(c)R_c\) in the full algebra.
The polynomial \(P_N\) is monic, so the leading coefficient in
(13) is \((4-c^2)/N^2\). Apply (1). Formula (12), used above,
also follows from the Chebyshev differential equation at a
root with \(T_N(c/2)=-1\) and \(T_N'(c/2)=0\). \(\square\)

Thus a spectral normal difference \(\zeta r\) in a vector channel
can be represented by \(\zeta rR_c\). For a vector spectator
\(g=(g_1,\ldots,g_d)\), its local contribution to the original
closing is
\[
 \sum_{\nu=1}^d\phi_N(\zeta r_\nu R_cg_\nu)
             =\eta(4-c^2)\zeta\sum_{\nu=1}^dr_\nu g_\nu(c).
 \tag{15}
\]
This need not vanish. For the scalar channel, \(g=1\) already
detects it. Original crossing phases can remain inside \(g\);
their physical values are not dropped.

Formula (15) concerns vector components at one common physical
color. For a future packet spanning several shifted colors,
use the corresponding cardinal \(R_{c_a}\) at each distinct
color and sum its separate contribution (14), with the
appropriate component spectator. Repeated occurrences of the
same physical color must satisfy their original identification;
they are not independent normal coordinates.

If the packet in (3) uses the \(u\)-normal instead, then
\(C_N'(u_0+mh)\ne0\) at a double node. The spectral normal in
(15) is \(\zeta r/C_N'(u_0+mh)\). The conclusion is unchanged.
There is no independent spectral normal in the quotient at the
odd simple node. An angular first derivative there vanishes for
an invariant spectral polynomial; it is not an additional free
channel to which Theorem 1 should be applied.

The cardinal in (13) proves visibility in the original algebra.
It does not say that adding this cardinal to an actual source
continues to solve every shifted row. That is the distinction
between a local missing transfer datum and a global homogeneous
solution.

## 5. Why a second differentiated equation is not available for free

Let an ordinary residual of a cleared full-step row be
\[
 \mathscr R(u)=P_N(C_N(u))\,H_N(u),
 \tag{16}
\]
with \(H_N\) holomorphic near the physical point. Formula (2)
gives the exact next derivative
\[
                \mathscr R''(j/N)=8\pi^2N^2 H_N(j/N).
 \tag{17}
\]
Thus only the value and first differentiated equations (3)
are homogeneous at the grid. Passing to a second differentiated
row would introduce the actual quotient residual
\(H_N\). Setting the right side of (17) to zero would delete
source data. Equivalently, the original double-root relation
does not become a triple-root relation.

Fixed exterior-parameter derivatives are different: they
differentiate a \(P_N\) multiple without changing its physical
root multiplicities. They may be retained in (3)--(17), with
the usual product rules, wherever the coefficient/rank chart
is defined.

## 6. Application and boundary of the conclusion

The leading matrix in these statements is the actual
finite-level coefficient after retaining every quantum shift
and every source channel. A limiting characteristic phase
color, even when it equals an exact physical node, does not
by itself establish that this matrix is singular. Terms of
smaller asymptotic size can repair the coefficient, or can
have greater shift order and change the appropriate unknown
packet. No such terms are omitted in (3).

If an actual simple rank loss does occur, (5) gives its exact
value repair and (11) gives the test for removing the residual
normal with further aligned rows. Quantitative transfer also
needs bounds for the inverse on the range of \(A\), for
\((\ell\dot A r)^{-1}\), and, when used, for the extra restriction
in (11). If these are polynomially conditioned, the determined
data cost polynomially. No bound for the undetermined normal
follows from that fact alone.

In particular this note supplies neither propagation across
every classical exceptional color nor a growth rate for a
general composed source. The original traces and global source
constraints remain available to control the identified datum.
Local physical jets do not give an off-grid polynomial bound
for a canonical polynomial of growing degree.

## 7. Direct sources and coverage

The following complete source texts were read at matching pins:

* [Full-step repeated-turn interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  exact cleared source equations, derivatives of ordinary
  residuals, retained recovery data, and the identity (2).
* [Original physical radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  the original trace normalization, double-node residue,
  odd simple node, and joint-spectator scope.

The elementary first-jet obstruction map (9) is proved here.
The coverage search found earlier first-order kernel/cokernel
lifting arguments, but no statement identifying this remaining
physical-row normal together with its original-trace visibility
and the complete stacked-row recovery criterion.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts are unchanged.
