# Absolute volume calibration of the retained three-chain phase

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

For every complete-ended all-three chain covered by the
[all-length chamber theorem](research_three_chain_geometric_chamber.md),
the actual cap-plus-retained critical action has real part equal to
the original marked geometric volume divided by \(2\pi\). The
constant is fixed by the exact homogeneous calibration. This does
not identify the original integration cycle with its local Gaussian
contribution or give a lower bound for the full quantum sum.

## 1. A connected chart containing all the actual vertices

Write \(\mathcal J(z)=\int_0^z\log(2\sin\pi u)\,du\), with the
original branch on \(0<\Re z<1\), and retain the original incidence
phase
\[
 b(x,\tau)=-\mathcal J(\tfrac12-x+\tau/(2\pi))
           -\mathcal J(\tfrac12-x-\tau/(2\pi))-2\mathcal J(x).
 \tag{1}
\]
The retained critical phase is
\(\Phi(x,y)=F(s,t;x,y)-\pi i(x+y)\), with the exact index
phase and logarithms of the
[central-index theorem](research_three_vertex_central_index_chart.md).

Use \(U,V\) as coordinates on the critical surface. Put
\[
 \begin{split}
 &U=-a-ib,\quad V=-c-id,\qquad
   \frac25\le a,c\le\frac{13}{20},\quad
   \frac34\le b,d\le1,\\
 &X=(1+U-UV)^{-1},\quad Y=(1+V-UV)^{-1},\qquad
   x=\frac{\Log X}{2\pi i},\quad y=\frac{\Log Y}{2\pi i},\\
 &W=\frac{UV-U-V-1}{2},\qquad
   \tau=-i\Log\{W+\sqrt{W-1}\sqrt{W+1}\}.
 \end{split}
 \tag{2}
\]
The radicals are principal roots. Since \(\Im W>0\), their
product chooses the principal \(\arccos W\) with
\(0<\Re\tau<\pi\) and \(\Im\tau<0\).

**Lemma 1.** On the closed box (2), and on a connected open
neighborhood of it, \(X,Y\) are in the first quadrant,
\[
 |X|,|Y|,|XU|,|YV|<1,
 \qquad 0<\Re x,\Re y<\tfrac14,
 \qquad \Im x,\Im y>0.
 \tag{3}
\]
Every argument of \(\mathcal J\) in (1), for both wires,
has real part strictly between zero and one. Every actual internal
vertex of the all-length chamber theorem, and the homogeneous
vertex, lies strictly inside this box in its \((U,V)\) coordinates.

*Proof.* The assertions can be checked uniformly on a small rational
cover, without solving an additional geometric system. The
[checker](../experiments/check_three_chain_action_calibration.py)
encloses (2) on 225 rational rectangles and proves all strict
inequalities, including the six original factorial-strip conditions.
The binary addresses reconstruct an exact multiplicity-one cover
of the whole four-dimensional box. All inequalities have strict
positive margins, so they persist on a connected neighborhood.

For the actual vertices, the checker reuses the exact rational
reference centers and the proved errors of the all-length chamber
theorem: \(8/(3\cdot10^{25})\) for lengths 3 through 24,
its near-end comparison (18), and its bulk comparison (19).
It recomputes the wires and selected index branch on these entire
enclosures, and verifies 524 coordinate inclusions in (2).
Thus the inclusion uses the all-length comparison proof, not an
extrapolation from the finite reference paths. At homogeneity
\(U=V=e^{-2\pi i/3}\), which is strictly inside (2).
\(\square\)

In particular the formulas in (1)--(2) are single-valued holomorphic
functions on one connected chart. The index primitives are regular
as well: \(U,V\) lie in the lower-left quadrant, so
\(1/4<\Re s,\Re t<1/2\), and (3) keeps their denominator
primitives away from zero. No continuation through a factorial zero
or reset of an angular logarithm is used.

## 2. The exact vertex identity and its real constant

Define the original angular vertex phase on this chart by
\[
 B(x,y;\tau)=b(x,\tau)+b(y,\tau)
                      +\frac{3i\tau^2}{4\pi}-i\tau .
 \tag{4}
\]
The angle \(\tau\) in (2) is a stationary angle for (4).
Indeed the rational identities give
\[
 \begin{split}
 &U(1-V)=X^{-1}-1,\qquad V(1-U)=Y^{-1}-1,\\
 &2\cos\tau=UV-U-V-1,\\
 &U=\frac{1-X}{1+X+2X\cos\tau},\qquad
 V=\frac{1-Y}{1+Y+2Y\cos\tau}.
 \end{split}
 \tag{5}
\]
With \(z=e^{i\tau}\), they imply
\[
 z^3(1+Xz)(1+Yz)=(X+z)(Y+z).
 \tag{6}
\]
All denominators are nonzero by Lemma 1. If
\[
 r_x=\tfrac12\{\log\cos(\pi x-\tau/2)
                    -\log\cos(\pi x+\tau/2)\},
 \tag{7}
\]
and similarly for \(r_y\), equation (6) says
\(\exp(2\pi B_\tau)=1\). The cosines have positive real
parts by the factorial-strip bounds. Thus these are the original
holomorphic logarithms. At the homogeneous point
\(3\tau+2i(r_x+r_y)=2\pi\) with its original lift.
Connectedness implies \(B_\tau=0\) everywhere on the chart.

The same argument retains the wire derivatives. By the index
equations, \(e^{F_s}=e^{F_t}=1\); their logarithmic lifts are
zero at homogeneity and remain zero on this connected chart.
Thus the actual equations are \(F_s=F_t=0\), and the envelope
derivative is
\[
 \Phi_x=-\Log U+\log(1-XU)-\log(1-X)-\pi i,
 \qquad
 e^{\Phi_x}=\frac{XU-1}{U(1-X)}=e^{b_x(x,\tau)}.
 \tag{8}
\]
Both derivatives are holomorphic on the connected chart, and both
are zero at the homogeneous point. Their difference belongs to
\(2\pi i\mathbb Z\), so it is zero everywhere. Likewise
\(\Phi_y=b_y\). These are genuine derivative identities: the
coordinate Jacobian is
\[
 \det\frac{\partial(X,Y)}{\partial(U,V)}
                      =(1-U-V)X^2Y^2\ne0.
 \tag{9}
\]
Consequently \(\Phi-B\) is a constant on this connected chart.

At \(x=y=x_*\), the
[exact retained calculation](research_three_vertex_local_composition.md)
gives \(\Phi(x_*,x_*)=2c\). The
[continued stationary-wire identity](research_unsummed_network_phase_coercivity.md#5-what-positive-geometry-does-imply-locally)
gives
\(2b(x_*,t_*)=\psi(t_*,t_*)\). Finally the
[exact homogeneous geometric calibration](research_homogeneous_three_action_calibration.md)
gives \(\Re B(x_*,x_*;t_*)=2c\), with the original complete
constant. Thus, with a fixed real number \(\gamma\),
\[
 \boxed{\quad
 \Phi(x,y)=B(x,y;\tau(x,y))+i\gamma,
 \qquad \Re\Phi=\Re B.
 \quad}
 \tag{10}
\]
Here \(i\gamma=2c-\psi(t_*,t_*)-3it_*^2/(4\pi)+it_*\).
This retains the possible imaginary constant explicitly; it is not
discarded or reset in the original source phase. No numerical
dilogarithm comparison fixes the real constant.

## 3. Summing the original marked cells

Consider any fixed complete-ended chain of length \(m\ge3\),
with power three at every selected vertex. Let its original geometric
angles and wires be those of the all-length chamber theorem. The
inverse formulas (5), together with its Proposition 3, identify
\(\tau(x_{v-1},x_v)=t_v\) at every internal vertex: their
cosines agree, and both angles have real part in \((0,\pi)\)
and negative imaginary part. The logarithms in (10) are therefore
the same ones as at the actual geometric source.

The actual cap phase is exactly
\[
 S_{\rm cap}(x)=b(x,t_{\rm end})+\psi(t_{\rm end},0)
                    +\frac{3it_{\rm end}^2}{4\pi}-it_{\rm end}.
 \tag{11}
\]
At each internal edge the original positive stationary-wire identity
has its calibrated value
\(b(x_v,t_v)+b(x_v,t_{v+1})=\psi(t_v,t_{v+1})\).
Sum (10)--(11), counting every original incidence once. For
\(t_0=t_{m+1}=0\), this gives the full complex identity
\[
 \mathcal S_m=\sum_{v=0}^{m}\psi(t_v,t_{v+1})
        +\sum_{v=1}^{m}\left(\frac{3it_v^2}{4\pi}-it_v\right)
        +(m-2)i\gamma .
 \tag{12}
\]
Every edge in (12), including the two complete-ended edges,
retains its original constant and its eight original tetrahedra.

**Theorem 2.** The critical action of the actual cap-plus-retained
source satisfies
\[
 \boxed{\qquad
 2\pi\Re\mathcal S_m=\operatorname{Vol}(M_m),\qquad m\ge3,
 \qquad}
 \tag{13}
\]
where \(M_m\) is the original marked positive partial filling with
the two outside ends complete.

*Proof.* The original vertex periods are
\(\sum_{e\ni v}r_{v,e}=3it_v/2-\pi i\).
Apply the absolute
[positive-edge volume identity](research_positive_edge_volume_identity.md#4-a-stationary-action-on-an-arbitrary-selected-region)
to the first two terms in (12). Its outside correction vanishes
because both outside angles are zero. The last term in (12) is
purely imaginary. This proves the identity with the sum of the
original positive tetrahedron volumes. The positive geometric
solution has the original strict core signs and marking; the
[pointwise completion theorem](research_positive_point_marked_completion.md)
identifies that sum with the stated marked hyperbolic volume.
\(\square\)

Together with the chamber theorem, (13) calibrates the nonzero
restricted Gaussian at every chain length. It supplies no bound
for the complementary index, angular, or wire contours, and hence
does not by itself prove the full-source volume conjecture.

## 4. Reproduction

Run

    python3 experiments/check_three_chain_action_calibration.py

The [record](../repro/results/research-three-chain-action-volume-calibration.json)
contains 225 connected-chart rectangles with exact binary coverage,
524 actual index-coordinate enclosures, eight rational identities,
and hashes of all proof inputs. The checker certifies the branch
premises and algebra. The written connectedness argument and the
previous exact homogeneous calibration fix the action constant.
