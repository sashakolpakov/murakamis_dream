# The complete ordinary three/four source between the seam and the taper

Research deduction, 7 November 2026. The complete source on every
fixed real incoming interval \([\rho,.1]\), \(\rho>0\), has a
strict geometric gap. A new real cap profile on \([.49,.5]\)
retains the upper physical tail which cannot be clipped directly
to \(.49\) near the seam. Whole-index coefficient bounds include
both cap endpoints; the old outgoing denominator-angle estimate
is not continued to this interval. No numerical evaluation is used.

## 1. Exact source and statement

Use the same ordinary \((3,4)\) reference, action \(M\),
normalization and finite polynomials as in
[the complete left-taper theorem](research_mixed_three_four_left_taper_source_completion.md).
Fix \(0<\rho<.1\), and set
\[
 a=x\in[\rho,.1],\qquad X=e^{-2\pi ix},\qquad
 Z_{34,N}=\kappa_N^3N^2\oint U_{0,N}V_{1,N}\frac{dX}{2\pi iX}.
                                                               \tag{1}
\]
The factors are the original complete ordinary functions. There
is no extra diagonal weight, outer Fourier selection or changed
observation.

**Theorem 1.** There are sufficiently small fixed ordinary-color
disks about \((-2,-2)\) such that, for every fixed pair of ordinary
derivative orders,
\[
 \left|\partial_{w_L}^{k}\partial_{w_R}^{\ell}
 \{U_{0,N}(w_L,e^{-2\pi ix})V_{1,N}(w_R,e^{-2\pi ix})\}\right|
 \le C N^B e^{N(M-1/320000)},\qquad \rho\le x\le.1.      \tag{2}
\]
Both parities and the original contour scalar are retained.
Constants and neighborhoods may depend on the fixed \(\rho\).
Taking \(\rho\) from
[the original two-vertex seam collar](research_mixed_two_vertex_first_collar.md)
joins this sector to that already paid real interval \([0,\rho]\).

## 2. A whole-index physical cap envelope, including both ends

The first cap is exactly
\[
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                   \frac{H_N(w,r^{-j})p_j(X)}{P_j}.       \tag{3}
\]
Write \(\lambda(e)=\Re S(e)\), and distinguish the endpoint
rate \(h_0(e)=\lambda(e)+J(e)\) from any contour height.
[The endpoint polynomial collar theorem](research_mixed_endpoint_polynomial_collar.md),
equation (15), proves for every prescribed \(\tau>0\)
\[
 |\partial_w^k H_N(w,e^{2\pi ie})|
 \le C N^B e^{N(h_0(e)+\tau)},\qquad 0\le e\le1,        \tag{4}
\]
on a sufficiently small fixed ordinary-color disk.
In particular \(h_0\) is continuous with zero values at both
ends. This is a whole-polynomial result, proved using degree
control and compact coherent packets, rather than an endpoint
stationary-phase extrapolation.

The uniform physical factorial and zero-safe product bounds
therefore give every row of (3) the upper rate
\[
 R_0(e,x)=\lambda(e)+I_x(e),\qquad
 I_x(e)=\int_0^e\log|1-e^{-2\pi i(x+s)}|\,ds.           \tag{5}
\]
It holds through both physical ends and every product zero,
with one arbitrarily small tolerance and a polynomial prefactor.
No outgoing denominator is divided out near a zero, and the
entire Newton sum remains in (4).

**Lemma 2.** For \(0\le x\le.1\), the physical tails obey
\[
 \begin{array}{ll}
 R_0(e,x)\le R_0(.27,x)-(27/50)(.27-e),&0\le e\le.27,\\
 R_0(e,x)\le R_0(.5,x),&.5\le e\le1.
 \end{array}                                            \tag{6}
\]
Thus the complete upper tail \(e\ge.49\) is bounded by the
additional real profile
\(\max_{.49\le e\le.5}R_0(e,x)\).

*Proof.* The exact real endpoint curvature in
[the early real-row theorem](research_mixed_cap_early_taper_real_rows.md)
gives \(\lambda''(e)<-\pi\cot\pi e\) on \((0,.5)\).
Hence \((\lambda+J)''<0\).
For \(e\le.27\), \(e+x\le.37<.5\), so
\(J'(e+x)\ge J'(e)\). Consequently
\[
 (R_0)_e\ge(\lambda+J)'(e)
 \ge(\lambda+J)'(.27)>27/50,                            \tag{7}
\]
using the original \(\lambda'(.27)>27/50\) and
\(J'(.27)>0\).

For \(e\ge.5\), the original branch identity gives
\(\lambda'(e)-J'(e)\le-\log4\). Away from an integrated
logarithmic zero,
\[
 \exp((R_0)_e)
 \le \sin\pi e\,|\sin\pi(e+x)|\le1.                  \tag{8}
\]
Integrate on the intervals complementary to any zero, then use
continuity of (5) at the zero and at \(e=1\). This proves (6).
\(\square\)

At \(x=.1\), the accepted upper-tail theorem gives
\[
 R_0(e,.1)\le R_0(.49,.1),\qquad .49\le e\le.5.         \tag{9}
\]
This is its real-height case, with its original coherent action.
It is used only at this endpoint. In particular no false
\(.49\)-clipping assertion at \(x=0\) has been introduced.

## 3. The central private cap and the additional real profile

For the central physical cap strip use the original exact private
interpolation on \(E_c=[.27,.49]+i[-.055,.04]\), with phase
\[
 \Psi_0(e,x)=S(e)+g(e+x)-g(x)-\frac{\pi i}{2}(e-e^2).
                                                               \tag{10}
\]
Every numerator and reciprocal argument is regular for
\(x\in[\rho,.1]\); only the already proved endpoint packet
on \(E_c\) is used. The exact curvature identity in
[the complex-private theorem](research_mixed_cap_early_taper_complex_profiles.md)
gives \(-\Re S''(e)>\pi C(e)\), where
\(C(e)=\Re\cot\pi e\).
At the same imaginary height, \(C(e+x)\le C(e)\): on
real parts between \(.27\) and \(.5\), the derivative of
\(C\) has the sign of
\(\cosh(2\pi\Im e)\cos(2\pi\Re e)-1<0\);
after \(.5\) the shifted \(C\) is nonpositive.
Therefore
\[
 -\Re\Psi_{0,ee}=-\Re S''(e)-\pi C(e+x)>0.             \tag{11}
\]

The original one-index residue identity consequently gives the
same five central cap profiles at its fixed actual private main
height \(k_*\), its real cuts and its two original alias heights.
Its joins are paid by (11), with linear sampling penalties on
each sign. The lower physical tail is transported to its real
cut by (6). The remaining upper physical rows are retained by
the extra real profile \(.49\le e\le.5\).
Equations (4)--(6) include both true cap endpoint layers, so no
additional old \(E_{\rm end}(h)\) assertion is needed here.

This is a complete cap upper envelope on the fixed real interval.
The extra profile uses real physical coefficient bounds only.
It neither extends the complex endpoint rectangle past \(.49\)
nor selects a new private reference.

## 4. Every terminal central profile transports to the paid endpoint

Retain the original terminal phase \(\Phi(a;t,b)\), cuts and
actual main heights, with
\(\Re t=u\in[.15,.5]\), \(|\Im t|=|\eta|\le.12\)
and \(b\in E_c\). For each regular cap profile, exact
differentiation gives
\[
 \frac d{dx}\Re\{\Psi_0(e,x)+\Phi(x;t,b)\}
 =\log\frac{
 |1-e^{-2\pi i(e+x)}|\,
 |e^{-2\pi\eta}-e^{-2\pi i(x+u)}|}
 {(2\sin\pi x)^2}>\log2.                              \tag{12}
\]
The ordinary chirp in \(\Phi\) is necessary for the reciprocal
radius in the second modulus.
Indeed \(\Re(e+x)\in[.27,.59]\), so the first modulus
exceeds one at every original private height.
The second modulus exceeds \(4/5\): while its angular cosine
is positive, minimize over its nonnegative radius and use
\(\sin(.3\pi)>4/5\); when the cosine is nonpositive its
minimum is one. Here \(x+u\in(.15,.6]\).
Finally \((2\sin\pi x)^2\le(3-\sqrt5)/2<2/5\).
Every original sampling penalty is independent of \(x\).

For the added real cap profile, the same formula holds with
\(\Re\Psi_0\) replaced by \(R_0(e,x)\),
\(.49\le e\le.5\). Its first modulus also exceeds one,
because \(e+x\in[.49,.6]\). Thus (12) transports every
cap-envelope/terminal-profile pair to \(x=.1\).
At that endpoint (9) puts the extra profile below the original
real private cap cut \(e=.49\).

The endpoint calibration here is profilewise, as established in
Sections 3--4 of the complete left-taper theorem: the main and
all eight flattened families, twelve aliases and their connecting
currents have their proved rate gaps at \(x=.1\).
An individual profile bound is not inferred from a modulus bound
for the signed complete product.
Equation (12) holds at every intermediate height as well as the
horizontal endpoints. Thus it transports the complete finite
central-current inventory to that already controlled endpoint;
there is no need to assume a new independent-target geometric
packet or a joint Hessian on the new incoming interval.

## 5. All physical terminal complements are retained

The complete extreme transform rows are paid throughout this
real interval by
[the global transform-end theorem](research_mixed_three_four_global_transform_ends.md),
with their whole private/Newton sums and the complete first factor.
Remove its initial rows \(i/N\le\delta\) first.

For each remaining real \(0<t\le.15\), the complex-private
transform force obeys
\[
 e^{\partial_t\Re\Phi}
 =\frac{2\sin\pi(x+t)\,|1-e^{-2\pi i(b+t)}|}
       {(2\sin\pi t)^3}
 >\frac1{(2\sin\pi t)^2}>625/529>9/8.                 \tag{13}
\]
Here \(t\le x+t\le.25\), \(\Re(b+t)\in(.27,.64]\)
has negative angular cosine, and
\(2\sin(.15\pi)<23/25\).
Apply the original exact private residue decomposition at each
physical \(t\ge\delta\). Transport every current point to
\(t=.15\) using (13), keeping all private penalties, then
use (12) and the original paid anchor at \(x=.1\).

On the physical lower-private complement, \(0\le b\le.27\),
the original coherent rate \(\mathcal R\) has
\[
 e^{\mathcal R_t}
 =\frac{2\sin\pi(x+t)\,2\sin\pi(b+t)}
       {(2\sin\pi t)^3}
 \ge\frac1{2\sin\pi t}>25/23>1.                       \tag{14}
\]
Transport \(t\) to \(.15\), then apply the unchanged
physical private-tail comparison to \(b=.27\).
The upper-private complement still clips first to \(b=.49\)
with its original derivative \(<-1/2\), then uses (13).
These estimates keep the whole physical \(H_N\), its endpoint
layers and every zero, exactly as in
[the left physical-complement theorem](research_mixed_three_four_left_physical_complement.md).

For central transform indices \(.15\le i/N<.5\), the two
physical-private-tail reductions are independent of the incoming
parameter. Retain their exact polynomial \(p_j(e^{-2\pi it})\)
on the deformed transform contour, including all revived off-grid
products. Transport the physical private coordinate to its
original real cut first; (12) then transports each full current
and its unchanged penalty to the already paid \(x=.1\) anchor.

Finally, the entire upper physical triangle retains the original
positive triple-row majorant
\[
 M_4(1/2)+Q_x(1/2),\qquad
 Q_x(t)=\int_0^t\log|1-e^{-2\pi i(x+s)}|\,ds.           \tag{15}
\]
The entropy derivative \(M_4'(v)>\log4\) is in the variable
\(v=1-t\) and is incoming-independent. Since
\(Q_x'(t)\le\log2\), the rate \(M_4(1-t)+Q_x(t)\)
decreases with \(t\), with derivative less than \(-\log2\).
Thus the whole upper triangle still reduces to its half-row,
with strict loss away from it,
including external zeros. Its coupled incoming derivative is
exactly (12) with \(u=.5,\eta=0\), for every central or
additional cap profile. At \(x=.1\) the calibrated
[upper-triangle theorem](research_mixed_three_four_left_upper_triangle_completion.md)
pays this complete positive majorant. No coherent terminal
value is substituted for that majorant.

## 6. Finite assembly and the real seam

Use the same disjoint physical partition as in the left-taper
theorem: initial complete transform rows, the remaining small
transform rows, central-private and physical-private-complement
sectors on \(.15\le i/N<.5\), and the entire upper triangle.
Each central source retains all nine constant-mode and seventy-two
alias currents with its original residue coefficient. The added
cap profile covers actual physical rows only; it creates no new
residue coordinate or sampling penalty.

Every endpoint calibration in this proof is one of the already
proved profilewise bounds at \(x=.1\), where the complete left
assembly has finite gap \(1/160000\) and its underlying raw
current gaps are larger. Inequalities (6), (9), and (12)--(15)
never increase a rate when transporting to those anchors.
Choose one common smaller source/color tolerance and retain the
gap \(1/320000\). All finite row counts, contour lengths,
symbols and half-grid rounding costs are polynomial.
The original upper-central parity convention keeps \(i=N/2\)
in the upper triangle at even levels. No physical row is omitted.

The fixed lower bound \(x\ge\rho>0\) keeps every new
reciprocal factorial argument in its regular strip. Ordinary
holomorphy and Cauchy's formula on smaller fixed color disks give
all mixed ordinary derivatives. This proves (2), including both
parities and the exact outside scalar in (1).

The original seam theorem handles \([0,\rho]\) as a complete
finite-source collar. Its fixed color disks can be intersected
with those above. No \(N\)-dependent continuation through the
factorial endpoint, and no identification of a partial root sum
with a real arc, is used. This closes the real interval up to the
left taper as a discarded source sector. The far incoming circle,
remaining transitions and full prescribed ordinary observation
are separate obligations; no new knot-family conclusion is made.
