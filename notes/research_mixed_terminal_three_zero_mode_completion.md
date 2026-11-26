# The complete zero-mode rectangle of the terminal type-three transform

Research deduction, 5 November 2026. This note assembles the nine
constant-mode currents in the reduced two-variable terminal Newton
representation. The complete mixed-face author record and independent
320-bit saved replay establish the strict joining comparisons used
below. Together with the original source normalization and Gaussian
branch, they give a nonzero asymptotic for the entire zero-mode
rectangle. No alias or omitted real row is included in the conclusion.

## 1. The source, reference and completed face comparison

Use the exact interpolation \(\mathcal I_N(a;t,u,w)\), amplitude
\(\mathcal A(a,t,u)\), original complete-color phase
\(\mathcal T(a;t,u)\), and inward half-grid cuts of
[the joint zero-mode theorem](research_mixed_terminal_three_joint_zero_mode.md),
equations (1), (15a)--(15e). The limiting real intervals are
\[
 I_t=[3/20,1/2],\qquad I_u=[1/10,2/5],\qquad
 P=[11/50,9/20].
\tag{1}
\]
Both indices are retained with their literal finite normalization,
and every physical pair in this rectangle satisfies \(i+l<N\).
The interpolation includes the factor \(N\) from the exact
Newton identity; its uniform leading symbol is
\[
 \mathcal I_N(a;t,u,w)
   =N^{-2}\mathcal A(a,t,u)
       e^{N\mathcal T_w(a;t,u)}(1+O(N^{-1})),
\tag{2}
\]
where \(w=-2\cos\zeta\) is the ordinary endpoint color and
\[
\begin{split}
 \mathcal T_w&=\mathcal T+V(u,\zeta)-V(u,0),\\
 V(u,\zeta)&=-2J(u)-J(1/2-u+\zeta/(2\pi))
                         -J(1/2-u-\zeta/(2\pi)).
\end{split}
\tag{3}
\]
The even dependence on \(\zeta\) defines a holomorphic function
of \(w\) near \(-2\). The normalized error in (2) is
holomorphic and has uniform fixed derivatives on smaller regular
neighborhoods. This is the original factorial/Newton interpolation,
not an asymptotic substituted into the outer finite sum.

Fix an actual external reference \(a_*=A+ih_a\) of a type-three
terminal block in an open word of length at least two. Let
\(t_*=T+ih_t\), \(u_*=U+ih_u\) be its original selected
critical coordinates. The
[critical-curve identity](research_mixed_terminal_three_critical_curve.md)
fixes the complete action and its tangent:
\[
 \mathcal T_t=\mathcal T_u=0,\qquad
 \mathcal T(a_*;t_*,u_*)=\mathcal P_0(a_*),\qquad
 \mathcal T_a(a_*;t_*,u_*)=\mathcal P_0'(a_*).
\tag{4}
\]
The exact endpoint-image extraction gives
\[
 .278<T<.391,\quad -.072<h_t<.021,\qquad
 .218<U<.242,\quad .049<h_u<.077.
\tag{5}
\]
Write \(\nu\in\{0,1\}\) for the external type minus three,
\(\Pi_{0,\nu}=\mathcal P_0-\nu g/2\), and
\(\kappa=1/2500000\). Its original allocated plane is
\[
 B_\nu(a_*;y)=\Re\Pi_{0,\nu}(a_*)
       +\Re\Pi_{0,\nu}'(a_*)(y-A)-\kappa(y-A)^2.
\tag{6}
\]

**Completed face comparison.** Over both whole original input disks,
each of the eight flattened face families in
[the mixed-face certificate proof](research_mixed_terminal_three_mixed_face_certificate.md)
satisfies
\[
 \Re\mathcal T(y+ih_a;t,u)
   <B_0(a_*;y)-1/2000
\tag{7}
\]
for every free real target in its prescribed box. These are the
two real \(t\)-cuts with \(u\) at its reference height, the
two real \(u\)-cuts with \(t\) at its reference height, and
the four real-real corners. The premise includes all 3,347 retained
own-three reference cells and all eight families per cell.

The exhaustive author and saved replay in Section 5 prove this
input using the cited acceptance rule. The bare inequality (7)
implies its allocated version: convexity
of \(y\mapsto\Re g(y+ih_a)\) makes the external halfweight
remainder nonpositive. At \(\nu=1\), interpretation as the
original finite Fourier halfweight uses the actual negative
type-four reference height. No positive-height Fourier branch on
the auxiliary disk is inferred.

## 2. The shifted boundary has its own strict reserve

The enlarged Hessian floor alone is deliberately coarse near the
right cut. The original middle-strip floor gives a stronger
reference-based inequality throughout the enlarged horizontal box.

**Lemma 1.** For independent \(y\in P\), \(x\in I_t\),
\(z\in I_u\), at the three fixed actual heights,
\[
\begin{split}
 \Re\mathcal T_\nu(y+ih_a;x+ih_t,z+ih_u)
 \le{}&\Re\Pi_{0,\nu}(a_*)
       +\Re\Pi_{0,\nu}'(a_*)(y-A)\\
 &-\gamma\bigl((y-A)^2+(x-T)^2+(z-U)^2\bigr),
 \qquad \gamma=19\pi/800,
\end{split}
\tag{8}
\]
where \(\mathcal T_\nu=\mathcal T-\nu g/2\).
On every boundary side of \(I_t\times I_u\), (8) is
strictly less than \(B_\nu(a_*;y)-1/1250\).

*Proof.* Parameterize the real segment from the reference to the
target by \(s\in[0,1]\). During its first half the transform
coordinate stays inside \([.20,.45]\): the possible midpoint
range is \((.214,.4455)\), by (1) and (5), and the initial
coordinate also lies in that interval. Thus the middle Hessian
bound \(3\pi/50\) applies for \(0\le s\le1/2\).
For the second half the enlarged bound \(\pi/100\) applies.
Both bounds include all the needed external and Newton coordinates
and all three fixed heights. The extra allocated term has
nonnegative negative real Hessian. Twice integrating, with (4),
gives the quadratic coefficient
\[
 \int_0^{1/2}(1-s)\frac{3\pi}{50}\,ds
 +\int_{1/2}^1(1-s)\frac{\pi}{100}\,ds
 =\frac{19\pi}{800}.
\tag{9}
\]

The four possible boundary distances from the selected real
coordinates exceed \(.128,.109,.118,.158\), respectively.
Consequently at least one of \(|x-T|,|z-U|\) exceeds
\(109/1000\). Since \(\gamma>\kappa\), subtracting (6)
from (8) leaves a loss greater than
\[
 \frac{19\pi}{800}\left(\frac{109}{1000}\right)^2
 >\frac1{1250}.
\tag{10}
\]
The last inequality follows already from \(\pi>3\).
This proves the claim. \(\square\)

**Corollary 2 (all zero-mode joins).** Every
point of all four horizontal-vertical and all four vertical-vertical
zero-mode currents lies below the allocated plane by more than
\(1/2000\), at the limiting cuts and complete color.

*Proof.* The negative real Hessian is positive throughout the
enlarged product, so the real part of the holomorphic phase is
convex in each imaginary coordinate separately. A vertical join
ranges between height zero and its actual reference height; this
holds also when \(h_t\) is negative or zero. Applying convexity
in each vertical coordinate reduces its maximum to its endpoint
heights. The fully shifted combinations lie on a boundary side
of the horizontal rectangle and are covered by Lemma 1. Every
other combination belongs to one of the eight families in (7).
The smaller reserve is \(1/2000\). The external halfweight
is independent of these two vertical coordinates, so it is counted
once throughout. \(\square\)

The exact interpolation has a uniform exponential upper symbol on
the entire compact product, including all summed imaginary parts
up to \(.24\). Inward half-grid cuts change phase values by
\(O(N^{-1})\), uniformly, and small fixed ordinary-color
neighborhoods change the phase by a uniformly small amount. Hence
choose the color neighborhood first, then sufficiently large \(N\),
so that these changes and all polynomial prefactors use less than
\(1/4000\) of the rate. Corollary 2 then gives the finite bound
\[
 |\text{any allocated joining current}|
 \le \exp\{N(B_\nu(a_*;y)-1/4000)\}.
\tag{11}
\]
The same statement holds for each fixed ordinary-color derivative
on a smaller fixed disk, by Cauchy's formula with part of the
strict reserve. There are exactly eight joining currents, so summing
them does not introduce any word-length-dependent accumulation.
Alternatively their finite factor eight can be retained explicitly.
No halfpower is differentiated through a Fourier zero; the ordinary
color acts on the interpolated terminal source, while the allocated
external weight is independent of that color.

## 3. The complete constant-mode rectangle and its coefficient

Let \(I_{t,N}\), \(I_{u,N}\) be the inward half-grid intervals.
Define the exact double zero mode, before the external allocation,
by
\[
 Z^0_N(a,w)=N^2\int_{I_{t,N}}\int_{I_{u,N}}
                  \mathcal I_N(a;t,u,w)\,du\,dt,
\tag{12}
\]
with both real orientations increasing. In the twice-applied marked
residue identity its coefficient is \(+N^2\). The additional
frequency terms of that identity are not included in (12).
Deforming each real interval to its actual critical height expands
(12) into the horizontal-horizontal current and precisely the eight
oriented joins just bounded. Thus the joins are part of the same
exact object; no estimate for an inner error is discarded before
the other integration.

At the actual target \(a=a_*\), put
\[
 H_*=-\mathcal T''_{(t,u)}(a_*;t_*,u_*).
\tag{13}
\]
Its real part is positive definite. Define
\(\sqrt{\det H_*}\) by the Gaussian branch on the cone of
complex symmetric matrices with positive real part: it agrees with
the positive square root for real positive matrices and continues
holomorphically throughout that cone.

**Theorem 3 (zero-mode completion).** For every actual type-three
terminal reference,
\[
 Z^0_N(a_*,-2)=
 \frac{2\pi}{N}
 \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1})).
\tag{14}
\]
The leading coefficient is nonzero, its phase is the original
calibrated terminal action, and both level parities are included.

*Proof.* The unique critical point on the shifted horizontal
rectangle is \((t_*,u_*)\). Lemma 1 gives a uniform quadratic
loss away from it. Its position is uniformly separated from all
cuts by (5). The local holomorphic symbol (2) and two-dimensional
Gaussian integration therefore give
\[
 N^2\cdot N^{-2}\cdot\frac{2\pi}{N}
 \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_0(a_*)}(1+O(N^{-1}))
\]
for the horizontal-horizontal current. This calculation retains both
the literal source normalization inside \(\mathcal I_N\) and
the exact \(+N^2\) residue coefficient. The sine factors in
\(\mathcal A\) are regular and nonzero, and the determinant
cannot vanish by the positive real Hessian. The Gaussian branch
fixes the orientation and square root. Odd first corrections
integrate to zero; the uniform source expansion gives the stated
relative error, as in the original
[ordinary boundary Gaussian proof](research_complete_boundary_coefficient_asymptotic.md#4-exact-summation-aliases-and-the-nonzero-coefficient).

At \(y=A\), (11) bounds each of the eight remaining currents
strictly below \(\Re\mathcal P_0(a_*)\), before allocation.
Their sum is exponentially smaller than the nonzero Gaussian term.
This proves (14). \(\square\)

For independent \(y\in P\), the same proof of the upper bound,
without claiming a new critical point, gives
\[
 |\text{allocated }Z^0_N(y+ih_a,w)|
 \le\exp\{N(B_\nu(a_*;y)+\eta)\}
\tag{15}
\]
for every prescribed \(\eta>0\), on a sufficiently small fixed
ordinary-color disk and for sufficiently large \(N\). The nonzero
asymptotic (14) is asserted at the actual reference, not throughout
that independent target interval.

## 4. Ordinary colors and all fixed jets

For fixed \(a_*\), the nondegenerate critical point has a
holomorphic continuation \((t_*(w),u_*(w))\) for \(w\) near
\(-2\). Set
\[
 \mathcal P_0(a_*,w)=\mathcal T_w(a_*;t_*(w),u_*(w)).
\tag{16}
\]
There is a fixed color disk on which the root remains interior,
the Gaussian Hessian remains accretive, and every strict joining
and exterior-horizontal gap above persists. This follows from
the original holomorphic interpolation and compact contour bounds,
not from pointwise continuity of an \(N\)-dependent finite sum.
Deform the central contour locally to the moving saddle within
that regular neighborhood. Its normalized stationary-phase expansion
is holomorphic and uniform on the color disk; the discarded joins
and horizontal exterior remain exponentially smaller there.

Consequently (14) has the uniform holomorphic form
\[
 Z^0_N(a_*,w)=\frac{2\pi}{N}
 \frac{\mathcal A(a_*,t_*(w),u_*(w))}
 {\sqrt{\det[-\mathcal T''_{w,(t,u)}(a_*;t_*(w),u_*(w))]}}
 e^{N\mathcal P_0(a_*,w)}(1+O(N^{-1})).
\tag{17}
\]
Fixed derivatives of the normalized relative error obey the same
\(O(N^{-1})\) bound on smaller disks. The original Newton
formula gives
\[
 \partial_w\mathcal P_0(a_*,w)\big|_{w=-2}
   =-\frac{\tan\pi u_*}{4\pi}=:\beta_*\ne0.
\tag{18}
\]
The equality uses stationarity to cancel the moving-critical-point
derivatives. It is the ordinary-color derivative, with its original
sign; it is not a derivative in either finite index.

For every fixed integer \(j\ge0\), differentiating (17) gives
\[
 \partial_w^j Z^0_N(a_*,w)\big|_{w=-2}
  =2\pi N^{j-1}
    \frac{\mathcal A(a_*,t_*,u_*)}{\sqrt{\det H_*}}
    \left(-\frac{\tan\pi u_*}{4\pi}\right)^j
    e^{N\mathcal P_0(a_*)}(1+O(N^{-1})).
\tag{19}
\]
In particular every fixed ordinary jet has a nonzero local leading
coefficient. Any signed-jet convention contributes its original
external sign. These statements concern this one terminal source
and do not assert a word-length-uniform asymptotic error.

## 5. Evidence and the remaining source terms

The [first complete author record](../repro/results/research-mixed-terminal-three-mixed-faces-attempt01.json)
has 26,776 accepted jobs, one leaf per job and no reference refinement.
It retains all 3,347 old own-three root witnesses and the complete
original tree coverage. Its SHA-256 is
`2ab91d18d9f89ca76d1af6e617ea0460b3b87627d845ffc4fda4d1598a626032`.
The [independent saved 320-bit replay](../repro/results/research-mixed-terminal-three-mixed-faces-replay.json)
has SHA-256
`8fdb997394efeb5fc87b224cbd848e3706521d25a55adc6599fb3820e2ba75aa`.
It revalidates all 26,776 saved leaves and all 3,347 original root
contexts, with zero target or root proposals and zero refinements.
The exact completed trees and rational targets agree with the author;
its input hash and all 54 current dependencies, proof and driver
bindings agree. Every outward upper bound is strictly below
\(-1/2000\). The displayed floating approximations of those
bounds are not used in the deduction.

The conclusion is a complete zero-mode rectangular contribution
only. The one-index and two-index
aliases of the exact residue formula, and the surviving real
triangular support outside (1), remain outside the theorem. The
already proved end-index and low/high-Newton sectors stay separate.
Thus a nonzero coefficient for (12) does not yet establish that the
full terminal transform, the ordinary open boundary coefficient,
or the full projected invariant is nonzero with this leading rate.
