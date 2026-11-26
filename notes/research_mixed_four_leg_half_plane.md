# Lower-half-plane inverse legs at powers at least four

Research lemma, 5 November 2026. The original positive charge equations
force every inverse leg at a vertex of power at least four into the
lower half-plane. In particular the type-four inverse has a continuous
original logarithm with real leg coordinate between zero and one half.
The adjacent-sum inequalities and the remaining type-three ranges are
separate obligations.

## 1. An additional lens inequality from the actual periods

Use the positive path charge family in
[the original existence theorem](research_positive_path_fractional_charge_cube.md).
All selected powers are integers at least three; the present vertex
has power \(n\ge4\). At an active vertex write
\[
 \tau=a-iH,\qquad 0<a<\pi,\quad 0<H<23/20,
 \qquad r_j=k_j+ig_j.
                                                               \tag{1}
\]
The original branch has \(k_j>0\),
\(-\pi/2<g_j<\pi/2\), and the exact imaginary period is
\[
             \sum_jg_j=\frac{na}{2}-\pi\chi,
                         \qquad 0<\chi\le1.             \tag{2}
\]
Each actual incidence is retained. A complete neighbor has angle zero.
The [cosine phase maximum principle](research_geometric_phase_maximum_principle.md)
gives \(0\le\beta_j=\arg\cos(\tau_j/2)<\pi/4\) and
\(\cosh H<7/4\). The [wire-order theorem](research_positive_path_real_wire_order.md)
also gives \(|\cos(\tau/2)|<1\) at every active vertex.

**Lemma 1.** At every active vertex with \(n\ge4\), throughout
the whole positive charge cube,
\[
             \left|\sin\frac{\tau}{2}\right|<1.
                                                               \tag{3}
\]

*Proof.* Set \(C=\cosh H\). If (3) failed, then
\((C-\cos a)/2\ge1\), so
\(\cos a\le C-2<0\) and \(a>\pi/2\). Since \(1<C<2\),
\[
 \left(\frac{\sinh H}{\sin a}\right)^2
 \ge \frac{C^2-1}{1-(C-2)^2}
 =\frac{C+1}{3-C}>1.                                    \tag{4}
\]
But \(\arg\tan(\tau/2)=-\arctan(\sinh H/\sin a)\).
Thus every product
\(\tan(\tau/2)\cos(\tau_j/2)\) has strictly negative
imaginary part, because \(\beta_j<\pi/4\). On the original
return branch, the identity
\(\Im\sinh(k_j+ig_j)=\cosh k_j\sin g_j\) implies
\(g_j<0\). Equation (2) now gives
\(a<2\pi\chi/n\le\pi/2\), a contradiction. An absent
incidence contributes zero, while every actual incidence has the
strict sign just proved. \(\square\)

Writing \(A=\cos^2(\tau/2)\), the conclusion is the strict
lens condition
\[
                    |A|<1,\qquad |1-A|<1.               \tag{5}
\]
Only the second inequality is new here. Its proof uses the actual
period equation and the power restriction, rather than positivity
of one isolated edge.

## 2. Excluding every real crossing of an inverse leg

On an edge from the present vertex to a neighbor put
\[
 A=\cos^2(\tau/2),\qquad B=\cos^2(\tau_j/2),\qquad
 q^2=A^{-1}+B^{-1}-1,
 \qquad U=\frac{-i}{2A(q+i)-i}.                          \tag{6}
\]
The square root is the original positive branch, continued from
\(q=1\) at completeness. Formula (6) is the same inverse as
\(U=(1-X)/(1+X+2X\cos\tau)\), where
\(X=(q+i)/(q-i)=e^{2\pi ix}\), by
[the inverse-leg calculation](research_mixed_positive_geometry_action_route.md#2-the-inverse-from-the-already-existing-positive-geometry).
It has no zero or pole on the positive family. At an active vertex
\(A=a_0+ib_0\) has \(a_0,b_0>0\); the neighbor has
\(\Im B\ge0\), including \(B=1\) at completeness.

**Theorem 2.** Every inverse leg (6) at a power \(n\ge4\)
vertex satisfies
\[
                       \Im U<0.                         \tag{7}
\]
Consequently its principal logarithm, continued without a reset
from completeness, defines
\(s=i\Log U/(2\pi)\) with \(0<\Re s<1/2\).

*Proof.* Suppose first that an active configuration has \(U=t\)
real. Since \(U\ne0\), put \(k=1-1/t\). Equation (6) gives
\[
 q=\frac{i(k-2A)}{2A},\qquad
 B=\frac{-4A^2}{4A(1-k)+k^2},
 \qquad
 \Im B=
 \frac{-4b_0\{4(1-k)|A|^2+2a_0k^2\}}
 {|4A(1-k)+k^2|^2}.                                    \tag{8}
\]
The denominator is nonzero: the same rearrangement before division
has left side equal to that denominator times the finite nonzero
\(B\), and right side \(-4A^2\ne0\).

If \(t>0\), then \(1-k=1/t>0\), so (8) gives
\(\Im B<0\), impossible. If \(t<0\), then \(k>1\), and
\[
\begin{split}
 4(1-k)|A|^2+2a_0k^2
 &=2a_0(k-2)^2+4(k-1)(2a_0-|A|^2)>0,\\
 2a_0-|A|^2&=1-|1-A|^2>0.
\end{split}                                                   \tag{9}
\]
Again (8) contradicts \(\Im B\ge0\). Notice that only the
present vertex needs the lens inequality; its neighbor may have
power three.

Scale the entire charge vector continuously from zero to the
specified vector. At completeness \(A=B=q=1\) and
\(U=-1/5-2i/5\). At every positive scaling parameter the
present vertex is active, Lemma 1 applies, and (8)--(9) forbid
a real crossing. The inverse stays finite and nonzero, so it
remains in the lower half-plane. This also fixes the stated
logarithm continuously. If the present vertex has zero charge,
then \(A=1\), \(q^2=B^{-1}\), and the original square root
has \(\Re q>0\). The denominator \(2q+i\) in (6) has
strictly positive real part, so \(\Im U<0\) directly in
this case as well. \(\square\)

## 3. Conditional original zero lifts with weaker angle hypotheses

The following observation separates the remaining logarithmic issue
from the already proved algebraic unit-period elimination. It does
not assert its additional wire-before-leg hypotheses for every
positive inverse.

Use a unit vertex of type three or four and the notation of
[the unit-period elimination lemma](research_mixed_unit_period_leg_elimination.md).
Suppose its inverse legs \(U,V\) lie in the lower half-plane,
and their corresponding original wires obey
\[
 0<\Re x<\min\{\Re s,1/4\},\qquad
 0<\Re y<\min\{\Re t,1/4\},
 \quad s=\frac{i\Log U}{2\pi},\quad
 t=\frac{i\Log V}{2\pi}.                               \tag{10}
\]
Assume the original continued source logarithms are the principal
ones on this regular chart. The original gradients are
\[
 f_s=\Log(1-UV)-\epsilon\Log(1-U)
                          +2\pi ix-\Log(1-XU),          \tag{11}
\]
and its transpose, with \(\epsilon=0,1\). Their exponentials
are one by the unit-period elimination lemma.

For type three, \(\arg(1-UV)\in(-\pi,\pi)\),
\(\arg(1-XU)\in(0,\pi)\), and
\(0<2\pi\Re x<\pi/2\). Hence
\(-2\pi<\Im f_s<3\pi/2\), and the same holds for \(f_t\).
Both integer lifts therefore vanish.

For type four it suffices in addition that
\(\Re U,\Re V\le0\). Indeed, writing
\(U=a-ib\), \(V=c-id\), with \(b,d>0\), one has
\[
 \Im\frac{1-UV}{1-U}
 =\frac{d(a-a^2-b^2)+b(c-1)}{|1-U|^2}<0.                \tag{12}
\]
The principal argument difference
\(\arg(1-UV)-\arg(1-U)\) lies in \((-2\pi,\pi)\).
Its strictly negative sine forces it into \((-\pi,0)\).
Thus \(-2\pi<\Im f_s<\pi/2\), and similarly for \(f_t\),
so these lifts also vanish. Under this extra left-half-plane
condition, (10) follows already from \(\Re s,\Re t\ge1/4\)
and the proved strict upper-quarter wire range.

Theorem 2 supplies only the lower-half-plane part for type four.
It does not supply this extra left-half-plane condition, all
adjacent-sum inequalities, or the analogous unconditional type-three
range. No action-to-volume identification or finite-source estimate
is inferred from the present lemma.
