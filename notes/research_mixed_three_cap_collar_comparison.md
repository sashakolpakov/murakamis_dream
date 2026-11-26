# A calibrated first-collar comparison for a three-three prefix

Research deduction, 5 November 2026. For every fixed open word beginning
with two type-three blocks, the literal first cap and its adjacent
conditional kernel have a strict calibrated loss on the first outgoing
collar, when the next real coordinate stays near its actual reference.
The adjacent height may undergo its entire physical attenuation. This
uses the actual open endpoint domains, not cyclic height refinements.
It is a boundary-pair estimate; the remaining boundary completion and
the full open-source contour comparison are not proved here.

## 1. Actual reference and the surviving tangent

Let the word have length at least two and start with \((3,3)\).
Write \(r_1,r_2\) for its first two retained outgoing coordinates,
\(r_1=a+ih\), \(r_2=b+ic\). The
[endpoint image extraction](research_mixed_open_word_endpoint_rectangles.md)
and [ordinary smaller-disk inclusion](research_mixed_open_local_factor_coverage.md)
give
\[
 .278<a<.391,\quad -.072<h<.021,\qquad
 .267<b<.438,\quad -.093<c<.073.                         \tag{1}
\]
For length two, the second coordinate is the private right endpoint;
its type-three rectangle is contained in the second box in (1).
For greater length it belongs to the disk of center \(.35-.01i\)
and radius \(.083\). No further restriction on the word is imposed.

Let \(\mathcal T_0\) be the original complete cap phase and
\(\phi_{00}\) the allocated conditional phase. Put
\[
 M_{12}=\Re\{\mathcal T_0(r_1,-2)+\phi_{00}(r_1,r_2)\},
 \qquad P=\partial_b\phi_{00}(r_1,r_2).                  \tag{2}
\]
There are no type-four diagonal weights or selected alternatives at
these two positions. Original stationarity gives
\(\mathcal T_0'(r_1,-2)+\partial_a\phi_{00}(r_1,r_2)=0\).
Thus the two-block supporting plane is exactly
\[
                      M_{12}+\Re\{P(z_2-r_2)\}.         \tag{3}
\]
The first-coordinate tangent cancels; the second does not. For a
longer boundary block its second tangent cancels against the next
incidence in the usual allocation. Equation (3) is not an assertion
that this pair alone is the entire endpoint boundary function.

Take \(0<\rho\le1/1000\), \(x\in[0,\rho]\), and initially
\[
 X=e^{-2\pi ix},\qquad z_2=b+ik,
 \qquad k\in[\min(0,c),\max(0,c)].                     \tag{4}
\]
This includes the physical hybrid attenuation beside the collar.
At its exact seam \(x=0\), the neighboring cutoff is one, so
\(k=c\) if its other cutoffs are one. At the face \(x=\rho\)
the cutoff is zero. We do not replace the neighbor by a real target
at the exact seam.

## 2. A real floor and its vertical transfer

Let \(f=\Re\phi_{00}\) on real arguments. The
[real supporting-plane theorem](research_mixed_real_outer_support.md)
proves joint concavity. Six original-log scalar witnesses already
saved in [the seam-run lower bound](research_mixed_seam_run_connector_lower.md)
give
\[
 f(v)>11/25\quad\text{for }v\in\mathcal V,
 \quad\mathcal V=\{(.1,.3),(.1,.39),(.39,.5),
                         (.5,.39),(.39,.1),(.3,.1)\}.    \tag{5}
\]
Their smallest value exceeds \(.4464521948\). The rectangle
\([.278,.391]\times[.267,.438]\) is contained in the convex
hexagon with these vertices. Concavity therefore gives
\[
                               f(a,b)>11/25.             \tag{6}
\]
The focused checker reuses those six saved root disks and evaluates
their original phases; it introduces no root proposal or new domain.

The larger common box
\([.267,.438]+i[-.093,.093]\) has
\(\Re\cot\pi z>0\), \(|\Im\cot\pi z|<1/2\).
Indeed the maximum imaginary modulus is at \(x=.267,|y|=.093\),
and
\[
 2\sinh(.186\pi)<\cosh(.186\pi)-\cos(.534\pi).          \tag{7}
\]
Monotonicity in \(|y|\) and in \(x\in[.267,.438]\)
follows from the explicit cotangent formula. Thus the whole vertical
segment from \((a,b)\) to \((r_1,r_2)\) lies in the
[closed cotangent phase domain](research_mixed_closed_cotangent_roots.md).
Its unique root agrees with the actual original conditional root.
The positive triangle forms and their complex Schur complement give
vertical convexity of \(\Re\phi_{00}\). The
[acute real gradient bounds](research_mixed_acute_gradient_height_transfer.md)
then yield
\[
 \Re\phi_{00}(r_1,r_2)
       \ge f(a,b)-\frac\pi2\{h_++(-c)_+\}.              \tag{8}
\]
This is a phase lower bound only; no finite kernel lower estimate on
the larger vertical box is imported. The actual reference source
packet is already proved separately.

One further sign is needed at the actual complex reference. Write
\(S=u+iv=\cot\pi s_*\), \(Q=q+i\beta=\cot\pi r_2\).
The original lifted gradient is
\[
 P=\log_{\rm R}(S+Q)-\log_{\rm R}(S+i),\qquad
                         -\pi<\Im P<0.                  \tag{9}
\]
Both logarithms have positive-real-part arguments. The imaginary
numerator of their ratio is
\(u(\beta-1)-q(v+1)<0\), because
\(u,q>0\), \(|v|<1\), \(|\beta|<1/2\).
The difference of their right-half-plane arguments lies in
\((-\pi,\pi)\), proving (9) on the original lift.

## 3. Full finite source, including both collar allowances

Use the original full-row function
\[
 L(u)=-2J((1-u)/2),\qquad
 M_0(C)=\max_{0\le u\le1}\{L(u)-J(u)+Cu\}.              \tag{10}
\]
The [full seam kernel bound](research_mixed_boundary_strip_bounds.md)
and [real collar product estimate](research_mixed_real_zero_collar.md)
give, with every row retained,
\[
 |C_{0,N}(X,e^{-2\pi iz_2})|
       \le C_\eta N^A
        e^{N\{M_0(2\pi k_+)+\Delta_\rho+\eta\}},
 \qquad \Delta_\rho=\rho\log2-J(\rho).                 \tag{11}
\]
The factor \(X^{-j}\) has modulus one. The first numerator product
costs one \(\Delta_\rho\); the full second product is bounded
by its complete-period arc maximum, at its actual complex height.
In particular this is not an extension of the cancellation identity
\(C_{0,N}(1,Y)=Nd_N(Y)\) to a neighborhood.

The [refined cap theorem](research_mixed_cap_seam_source_bounds.md)
contributes \(101/125+\Delta_\rho\), with arbitrarily small
ordinary-color tolerance. Its reference action satisfies
\(\Re\mathcal T_0(r_1,-2)>1\), by the existing
[complete cap theorem](research_mixed_complete_first_cap_packet.md).

The function \(M_0\) is increasing and convex in \(C\).
For \(0\le C<\log2\), its unique maximum is at
\(u=2\arcsin(e^C/2)/\pi\), since its row derivative is
\(C-\log(2\sin(\pi u/2))\). Fixed outward evaluations give
\[
                  M_0(0)<.326,
                  M_0(.146\pi)<.526.                    \tag{12}
\]
For \(c\le0\), (9) and \(k-c\ge0\) show that
\((k-c)\Im P\le0\). For \(c\ge0\), use
\((k-c)\Im P\le\pi(c-k)\), and convexity reduces
\(M_0(2\pi k)+\pi(c-k)\) on \([0,c]\) to its two endpoints.
Together with (1) and (12), these give the single bound
\[
 M_0(2\pi k_+)+\frac\pi2(-c)_++(k-c)\Im P
                      <.326+.073\pi.                   \tag{13}
\]
For the negative case, \(.326+.0465\pi\) is already enough;
for the positive case the other endpoint \(.526\) is smaller
than the right side of (13).

## 4. The calibrated loss and its scope

Subtract (3) from the rate of the complete product
\(U_{0,N}(w_L,X)C_{0,N}(X,e^{-2\pi iz_2})\).
Equations (6), (8), and (13), together with \(h_+<.021\),
give the strict rate bound
\[
 \begin{split}
 &\frac{101}{125}+.326+.0835\pi+2\Delta_{1/1000}
                                      -1-\frac{11}{25}\\
 &\hspace{35mm}=-.306+.0835\pi+2\Delta_{1/1000}<-3/100.
 \end{split}                                                   \tag{14}
\]
The last inequality is a fixed scalar check. Only one total finite
source and ordinary-color tolerance is spent after this comparison.

**Theorem 1.** For each fixed open word beginning \((3,3)\),
there is an ordinary-color neighborhood of \(-2\) on which,
uniformly over (4) and both level parities,
\[
 |U_{0,N}(w_L,X)C_{0,N}(X,e^{-2\pi iz_2})|
 \le C N^A
   \exp N\left\{M_{12}+\Re[P(z_2-r_2)]-\frac1{40}\right\}.
                                                               \tag{15}
\]
It also holds with each fixed ordinary derivative of the cap on a
smaller color neighborhood. These are upper estimates for the
literal finite factors, with no division by a possibly vanishing
Fourier polynomial or cap.

The rate reserve before the final tolerance is strictly larger than
\(3/100\). Consequently a sufficiently small fixed change in the
second real coordinate from \(b\) preserves a positive reserve,
with the same original tangent retained. The source ceiling (11)
is angle-uniform; the extra tangent change is bounded on the compact
actual-reference families. If a smaller finite reserve such as
\(1/50\) is used, this gives a genuine collar times neighbor
neighborhood. The two reference height boxes in (1) also have strict
room. This continuity statement does not remove the neighboring
coordinate from the rest of the source or discard its next edge.

In the finite-boundary reduction, (15) can replace the first two
literal factors by their actual supporting plane with a strict debit.
The middle completion and the remaining boundary factors still need
their stated comparisons. No result for prefixes containing type
four, no global boundary-function sign, and no whole open-word
asymptotic follows from this restricted estimate.
