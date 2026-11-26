# The complete-boundary charge characteristic and its two inner modes

Research note, 3 November 2026. This classifies every genuine root of
the frozen original one-edge charge recurrence at the complete free
boundary. The classification holds for every positive integer power
\(n\ge3\), rather than for a finite numerical list. It gives an isolated
two-dimensional spectral block on compact interior charge intervals,
and identifies why the geometric mode alone is not selected by a
modulus ordering. It does not prove a connection coefficient for the
actual source or a propagation theorem for adjacent filled vertices.

The exact recurrence, its original endpoint condition, and its physical
period identities are those of
[the current-free AW note, Sections 10--12](research_current_free_aw_crossing_transport.md).
The terminal return formula used below is proved in
[the terminal geometry note](research_terminal_powers_three_and_above.md).
No ordinary-color or first-normal channel is removed from the finite
recurrence.

## 1. A monotone curve containing all growing roots

Put \(\rho=e^{it}\). A growing root means \(|\rho|>1\), or
\(\operatorname{Im}t<0\). At the complete boundary \(w=-2\), the
characteristic equation is
\[
 \sin^2(nt/2-\pi\chi)=-\tan^2(t/2),\qquad 0<\chi<1.
 \tag{1}
\]
The points \(\rho=1,-1\), where the original trigonometric expression
has a pole or a cleared factor, will be treated separately.

For \(0<a<\pi/2\), define \(b=b_n(a)>0\) by
\[
 \sin a=\cosh b\,\tanh(nb).
 \tag{2}
\]
The right side is strictly increasing from zero to infinity as \(b\)
increases. Thus \(b_n\) exists, is smooth and strictly increasing, and
has a finite positive limit \(b_*\) at \(a=\pi/2\). Define
\[
 c_n(a)=\frac1\pi\left[
     na+\arctan\frac{\sinh b_n(a)}{\cos a}\right],
 \qquad c_*=\frac{n+1}{2}.
 \tag{3}
\]
Every term in (3) is strictly increasing. Consequently \(c_n\) maps
\((0,\pi/2)\) bijectively onto \((0,c_*)\). Write
\[
 t_n(c)=2a_n(c)-2ib_n(a_n(c)),\qquad
 H_n(c)=-\operatorname{Im}t_n(c).
 \tag{4}
\]
Both \(a_n(c)\) and \(H_n(c)\) are strictly increasing. At the endpoints
\[
 t_n(0)=0,\quad
 t_n(c_*)=\pi-2ib_*,\quad
 \cosh b_*\,\tanh(nb_*)=1.
 \tag{5}
\]
Endpoint values here mean one-sided limits.

**Theorem 1.** For \(n\ge3\) and \(0<\chi<1\), all roots of (1)
with \(|\rho|>1\) are the following:
\[
 \begin{array}{ll}
 \rho=\exp\!\bigl(it_n(\chi+j)\bigr),
     &j\ge0,\quad \chi+j<c_*;\\[2mm]
 \rho=\exp\!\bigl(-i\overline{t_n(1-\chi+j)}\bigr),
     &j\ge0,\quad 1-\chi+j<c_* .
 \end{array}
 \tag{6}
\]
For even \(n\) and \(\chi=1/2\), add the single negative-real root
\(\rho=-e^{2b_*}\). This is the common strip-boundary limit
\(c=c_*\), counted once. All roots in this list are simple.
There are exactly \(n+1\) of them. The other \(n+1\) roots are
their reciprocal complex conjugates and lie inside the unit circle.

*Proof.* On the right lower strip \(t=2a-2ib\),
\(0<a<\pi/2,\ b>0\), take the original branch
\[
 r(t)=\operatorname{asinh}\tan(t/2)
 =\operatorname{artanh}\frac{\sin a}{\cosh b}
       -i\arctan\frac{\sinh b}{\cos a}.
 \tag{7}
\]
Its real part is positive and its imaginary part lies in
\((-\pi/2,0)\). The two possibilities
\(\sin(nt/2-\pi\chi)=\pm i\tan(t/2)\) imply, by the elementary
solutions of \(\sinh v=\sinh r\), that
\[
                 r(t)=int/2-i\pi(\chi+j)
 \tag{8}
\]
for some integer \(j\). The alternative with real part \(-nb\)
cannot equal \(r(t)\). Equating real parts in (8) gives (2);
equating imaginary parts gives \(c_n(a)=\chi+j\). Positivity
forces \(j\ge0\), and the range in (3) gives the first list.
Conversely (2)--(3) imply (8), hence (1), for every listed value.

Replacing \(t\) by \(-\bar t\) in (1) replaces \(\chi\) by
\(1-\chi\). This gives exactly the second list in the left lower
strip. A purely negative imaginary \(t\) cannot solve (1):
\(\tan(t/2)\) is purely imaginary while
\(\sin(nt/2-\pi\chi)\) cannot be real when \(b>0\) unless
\(\chi=1/2\), in which case its modulus exceeds one whereas
\(|\tan(t/2)|<1\). Equivalently the limit \(a=0\) in the
real-part equation would force \(b=0\).
At the remaining seam \(t=\pi-2ib\), (7) has imaginary part
\(-\pi/2\). Equations (2)--(3) therefore give \(c=c_*\);
an interior charge reaches this seam exactly when \(n\) is
even and \(\chi=1/2\). The two representatives differing by
\(2\pi\) give the same \(\rho\).

Simplicity in the open right strip follows directly by differentiating
the logarithmic equation:
\[
 \frac{d}{dt}\{nt+2ir(t)\}
                       =n+i\sec(t/2)\ne0.
 \tag{9}
\]
Indeed \(\sec(a-ib)\) has positive real and negative imaginary
parts, so the real part of (9) is greater than \(n\).
At the seam its limit is \(n+\operatorname{csch}b_*>0\).
The two sine signs in (1) are distinct there and in the open
strip, since \(\tan(t/2)\ne0\). Reflection gives simplicity
on the left.

For completeness, set \(\alpha=e^{-2\pi i\chi}\). The exact polynomial
obtained from (1) is
\[
 p_{n,\chi}(\rho)=
   (\rho+1)^2(\alpha\rho^n-1)^2
                  +4\alpha\rho^n(\rho-1)^2.
 \tag{10}
\]
It has degree \(2n+2\), nonzero constant and leading coefficients,
and neither \(1\) nor \(-1\) is a root for \(0<\chi<1\).
There are no unit-circle roots: for real \(t\), the two sides
of (1) have opposite signs, and their simultaneous zero would
require \(t=0\bmod 2\pi\) and \(\chi\) integral.
For odd \(n=2r+1\), each list in (6) has \(r+1\) entries.
For even \(n=2r\), the two counts are \(r+1,r\), or \(r,r+1\);
at \(\chi=1/2\) they are \(r,r\) plus the one seam root.
Thus there are \(n+1\) distinct growing roots.
Complex conjugation in the original \(t\)-equation supplies
their \(n+1\) distinct reciprocal conjugates. This exhausts
the degree of (10). \(\square\)

The integer \(j\) in (8) records logarithmic branches which the
squared characteristic has forgotten. Only \(j=0\) on the right
is the selected positive geometric equation with charge \(\chi\).
Calling another root genuine means that it is not introduced by
pole clearing; it does not assert that its saddle occurs in the
original integration cycle.

## 2. The isolated block and its endpoint failures

Set
\[
                        R_n=e^{H_n(1)}>1.
 \tag{11}
\]
**Corollary 2.** For every \(0<\chi<1\), exactly two characteristic
roots lie in \(1<|\rho|<R_n\):
\[
 \rho_g(\chi)=e^{it_n(\chi)},\qquad
 \rho_c(\chi)=e^{-i\overline{t_n(1-\chi)}}.
 \tag{12}
\]
They are distinct, including at \(\chi=1/2\). Their moduli satisfy
\[
 \begin{cases}
 |\rho_g|<|\rho_c|,&0<\chi<1/2,\\
 |\rho_g|=|\rho_c|,&\chi=1/2,\\
 |\rho_g|>|\rho_c|,&1/2<\chi<1.
 \end{cases}
 \tag{13}
\]
Every other growing root has modulus strictly greater than \(R_n\).
All these separations are uniform on a compact subinterval of
\((0,1)\).

*Proof.* The first two charges are \(\chi,1-\chi<1\);
every other charge in (6) exceeds one. Strict monotonicity
of \(H_n\) proves the modulus claims. The two arguments in
(12) lie strictly on opposite sides of zero and strictly
between \(-\pi,\pi\), so the roots cannot coincide.
Compactness proves the uniform statements. \(\square\)

This is a separation of a two-dimensional block, not a scalar
Perron ordering for the geometric mode. In fact the geometric root
is never the largest-modulus growing root in the full characteristic,
and its ordering even within (12) changes at \(\chi=1/2\).

Neither endpoint can be silently included. As \(\chi\downarrow0\),
\(\rho_g\to1\), while \(\rho_c\) and the next positive root
reach modulus \(R_n\). As \(\chi\uparrow1\), \(\rho_c\to1\),
while \(\rho_g\) and the next negative root reach modulus \(R_n\).
At an integral charge, (10) has a double factor \((\rho-1)^2\).
After it is removed, \(1\) is not a root of the original rational
characteristic: its limiting value at \(t=0\) is
\(w=2+4n^2\), not \(-2\).
Thus the endpoint issue includes a pole-clearing collision and
a loss of the radial separation from an additional genuine mode.
It is not a degeneracy of the selected terminal saddle at charge one.

## 3. A finite-recurrence consequence retaining the cleared modes

Let \(\mathsf T_N(\chi)\) be the companion transfer matrix for the
literal charge recurrence, using a window of \(2(n+4)\) consecutive
entries and substituting \(k/N=1-\chi\) in its coefficients.
The outer coefficients have modulus \(1/16\), so this matrix is
well-defined. The limiting Laurent characteristic at \(w=-2\) is
exactly
\[
 \mathcal P_\chi(\rho)=
 \frac{(\rho-1)^2(\rho+1)^4}
                  {16\alpha\rho^{n+4}}p_{n,\chi}(\rho).
 \tag{14}
\]
For example, (14) follows by writing the original symbol as
\(4\sin^2t[\sin^2t+(1+\cos t)^2\sin^2(nt/2-\pi\chi)]\).
The six additional roots in (14) are retained at this stage.
They lie on the unit circle and do not belong to (12).

Fix \(0<\delta<1/2\). Choose the inner circle
\(r_\delta=e^{H_n(\delta/2)}\) and the outer circle \(R_n\).
On \(\delta\le\chi\le1-\delta\), the difference of the two
resolvent integrals
\[
 \mathsf P_N(\chi)=\frac1{2\pi i}
 \left(\int_{|\zeta|=R_n}-\int_{|\zeta|=r_\delta}\right)
           (\zeta I-\mathsf T_N(\chi))^{-1}\,d\zeta
 \tag{15}
\]
is defined for all sufficiently large \(N\), and has rank two.
It and its first derivative are uniformly bounded.
These statements also hold for \(w\) in a sufficiently small
complex neighborhood of \(-2\).

To justify them, the literal coefficients and their first charge
derivatives converge to their limiting coefficients at rate
\(O_n(N^{-1})\). The limiting resolvents on the two fixed circles
are uniformly bounded by Corollary 2 and compactness.
The resolvent identity then proves the same for the finite matrices,
including derivatives, and preserves the integer rank.
No finite-factor cancellation or alteration of the endpoint source
has been used.

Since \(\mathsf P_N(\chi)\) commutes with \(\mathsf T_N(\chi)\),
the actual one-step leakage has the quantitative bound
\[
 \bigl\|(I-\mathsf P_N(\chi-N^{-1}))
       \mathsf T_N(\chi)\mathsf P_N(\chi)\bigr\|
                                      \le C_{n,\delta}N^{-1}
 \tag{16}
\]
whenever both charges are in the displayed interval. This follows
by subtracting \(\mathsf P_N(\chi)\) from
\(\mathsf P_N(\chi-N^{-1})\). It is an instantaneous estimate.
Iterating it does not give a relative error bound for the actual
source: the complementary subspace contains faster growing modes,
and its source coefficient has not been estimated.
In particular (16) is not a nonzero lower bound for \(Z_{0,N}\).

## 4. The exact period constraint does not choose this block

There is a concrete distinction between the frozen growing roots
and the actual physical period. For the original one-edge source
\[
 Z_k=\phi_N[R^nK_N(z,-2)T_k(-z/2)],\qquad
 \Delta_k=Z_{k+N}-\eta Z_k,\quad \eta=(-1)^{N-1},
 \tag{17}
\]
the full Hermite identity gives
\[
 Z_{k+2N}-2\eta Z_{k+N}+Z_k=0,\qquad
                       \Delta_{k+N}=\eta\Delta_k .
 \tag{18}
\]
The recurrence coefficients themselves have period \(N\).
Consequently \(Z\) and \(\Delta\) are both solutions of that
recurrence. Moreover \(\Delta\ne0\): the exact physical Fourier
identity in
[the graph increment note](research_charge_increment_graph_norm.md)
gives
\[
 \sum_{k=0}^{N-1}|\Delta_k|^2
       =N^3\sum_{a=0}^{N-1}\sin^2\tau_a
                         |K_N(c_a,-2)|^2>0.
 \tag{19}
\]
Here crossing values have modulus one and the physical row at
\(c_0\) equals one. The two sequences are linearly independent,
since a relation \(\Delta=cZ\), combined with (18), would give
\(c^2Z=0\).

Thus the exact period transfer has, on the span generated by this
actual source and its increment, the nontrivial Jordan action
\[
                  Z\longmapsto\eta Z+\Delta,\qquad
                  \Delta\longmapsto\eta\Delta.
 \tag{20}
\]
Its eigenvalue has modulus one. This does not conflict with
Theorem 1: an instantaneous characteristic root is not a period
multiplier, and the full physical sequence combines modes.
The reflection constraint \(Z_{-k}=Z_k\) and (18), even together
with the cleared recurrence, leave the extra channel described
in the AW note. The original endpoint condition removes that
channel exactly, but a quantitative connection of the resulting
source line to (12), and a matching analysis at \(\chi=1\),
remain necessary. The already proved one-edge scalar packet is
not being reproved or extended to adjacent pairs by this argument.
