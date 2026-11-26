# Exact endpoint tapers for the coupled internal-pair contour

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The shared-wire endpoint currents can be controlled jointly, with
both original outside kernels retained. The two trace heights must
be allowed to depend on the wire position. This freedom is exact:
it changes a representation of the retained trace, not its value.
It introduces no extra height-derivative current. The result below
removes fixed thin collars of both wire endpoints from the remaining
global estimate. It does not control the middle wire band.

## 1. The full finite source and its retained traces

Use the original Newton kernel
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),
                  \qquad M_\infty=4G/\pi .
 \tag{1}
\]
Fix integer powers \(n,p\ge3\) and an angular cut \(0<T<\pi\).
Choose the exact midpoint cuts \(T_N=T+O(N^{-1})\) from the
[combined contour reduction](research_internal_pair_combined_contour_reduction.md),
so \(e^{iNT_N}=-\eta\), \(\eta=(-1)^{N-1}\).
Write \(\phi_N^{[T]}\) for the sum of the original physical
value and first-normal residues with \(|t_a|<T_N\), including
the odd simple node. No normal is split from its physical root.

Let \(B_N(x,t)\) be the exact factorial interpolation in that note.
At \(x=j/N\) it is the canonical polynomial \(e_j(-2\cos t)\)
for arbitrary complex \(t\). Define the actual retained trace
\[
 \mathcal T_N(x;u,v)=
 \phi_N^{[T],t}\phi_N^{[T],r}
 \left[
 R^nR^p B_N(x,t)B_N(x,r)K_N(t,u)K_N(r,v)
 \right].
 \tag{2}
\]
The half-band representative of \(B_N\) agrees with its full
physical jets. Thus (2), which contains a product of two
half-band interpolants, is an entire integer-band function
of \(x\), with frequencies in \([-(N-1),N-1]\).
Its coefficients retain the literal original crossing and
outside factors. In particular it is holomorphic in \(x\).
The scalar retained in the shared index is the exact sum of
(2) at the retained lattice indices.

**Lemma 1 (pointwise trace deformation).**
In the wire Cauchy representation of this sum, the two folded
trace contours representing (2) may depend smoothly on the
wire position \(x\). They may have arbitrary positive lower
heights, provided that they enclose the same physical poles,
their endpoint verticals stay at \(T_N\), and their
factorial representatives remain regular. No additional
current involving a derivative of either height is introduced.

*Proof.* First apply the exact one-cell Cauchy identity to the
holomorphic function \(\mathcal T_N(x;u,v)\). For each fixed
point \(x\) on the resulting wire curve, the residue theorem
represents each of the two traces in (2) on any of the stated
contours, with its same folded endpoint segment. This is an
exact equality before integrating in \(x\).
Fubini on the compact curves gives the claimed representation.
Equivalently, in the three-form
\(f(x,t,r)\,dx\wedge dt\wedge dr\), terms involving \(t_x\,dx\)
or \(r_x\,dx\) vanish on pullback. The existing trace endpoint
segments are retained; they have not been replaced by a
closed horizontal integral. \(\square\)

The required regularity holds for these deformations whenever
\(0<\Re x<1/2\), \(|\Re t|,|\Re r|<T+o(1)<\pi\), and all
heights stay in a fixed bounded set: the shifted factorial
real parts lie in a compact subinterval of \((-1,1)\).
Negative arguments give reciprocal-factorial zeros, not poles.

## 2. A uniform bound for every endpoint current

The following elementary full-kernel bound is useful because
it does not require a geometric packet on the trace contour:
\[
 |K_N(t,u)|\le C N^A
       e^{N\{M_\infty+|\Im t|+|\Im u|\}},
 \quad |\Re t|,|\Re u|\le\pi,
 \quad |\Im t|,|\Im u|\le h_1 .
 \tag{3}
\]
Here \(h_1\) may be any fixed bounded height.
Indeed the positive low-index Fourier coefficients give
\(|e_j(-2\cos a)|\le e_j(-2)\) for \(2j<N\) and real \(a\).
The original radical polynomials have real interval norm
at most \(\sqrt{N-1}\), by the
[radical Fourier theorem](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials).
Therefore the real-square kernel norm is at most
\(\sum_{2j<N}e_j(-2)^2+N^2\), which is bounded by
\(CN^Ae^{NM_\infty}\) using the complete small-angle packet.
Finally \(K_N\) has angular degree at most \(D=N-1\) in each
variable. The maximum principle applied successively to
the corresponding Laurent polynomials proves the factor
\(e^{D(|\Im t|+|\Im u|)}\), and hence (3).
All fixed ordinary normals cost only additional polynomial
factors, by Cauchy on color disks of radius \(O(N^{-2})\).

Write \(\mathfrak b(x,t)\) for the continuous real factorial
upper exponent of
[the uniform interpolation bound](research_uniform_factorial_and_boundary_decay.md).
For real \(|t|\le T<\pi\), its boundary values are
\[
           \mathfrak b(0,t)=\mathfrak b(1/2,t)=0.
 \tag{4}
\]
At \(x=0\) this is \(J(1-z)=-J(z)\).
At \(x=1/2\), the two arguments are \(t/(2\pi)\) and
\(-t/(2\pi)\); the upper and lower continuations have opposite
real parts. The statement includes \(t=0\) by continuity.
The two reflected cosine terms of the exact reciprocal
factorial are part of this upper exponent.

Consequently there is a modulus \(\omega_T(\epsilon)\to0\)
as \(\epsilon\downarrow0\) such that
\[
 \mathfrak b(x,t)\le\omega_T(\epsilon)
 \tag{5}
\]
whenever \(\Re x\) is within \(\epsilon\) of \(0\) or \(1/2\),
\(0\le\Re x\le1/2\), \(|\Im x|\le\epsilon\),
\(|\Re t|\le T+\epsilon\), and \(|\Im t|\le\epsilon\).
Take \(\epsilon\) small enough that \(T+\epsilon<\pi\).
This is uniform continuity of the original real upper exponent
on a compact set; it is not a continuation of an asymptotic
known only at an endpoint.
More quantitatively, one may take
\(\omega_T(\epsilon)\le C_T\epsilon(1+|\log\epsilon|)\)
for small \(\epsilon\). The shifted arguments stay a fixed
distance from the nonzero integer singularities. Near zero,
\(J(z)=z\Log z+O(z)\) on either side, whose real primitive
has this modulus of continuity; away from zero its gradient
is bounded. The reflected boundary values agree in real part,
so the same estimate holds across the negative real cut.

**Theorem 2 (joint collar currents).**
For every \(\delta>0\), there is \(\epsilon>0\) such that
all the following original contour pieces have absolute value
at most
\[
                         C N^A e^{N(2M_\infty+\delta)}.
 \tag{6}
\]
The shared-wire piece lies in either of the collars in (5);
its heights have modulus at most \(\epsilon\).
Both folded trace contours, including their vertical endpoint
segments, have heights of modulus at most \(\epsilon\).
The outside angles \(u,v\) may have arbitrary real parts
in their real periods and imaginary parts at most \(\epsilon\).
The statement includes all fixed outside ordinary normals.

Wire endpoint sides are chosen on the exact half-index lines.
Wire upper and lower arcs and trace lower arcs have positive
heights bounded away from zero for each fixed chosen
deformation. Heights may vary smoothly with \(x\); no bound
independent of this fixed deformation is asserted.

*Proof.* The exact factorial bound, with its reflected terms,
gives \(|B_N(x,t)B_N(x,r)|
\le CN^A e^{2N\omega_T(2\epsilon)}\) on these collars.
The slight enlargement covers the \(O(N^{-1})\) midpoint
adjustments and derivative neighborhoods.
The two full outside kernels in (3) cost at most
\(2M_\infty+4\epsilon\) in rate.
The two crossing Gaussian factors cost at most
\((n+p)(T+\epsilon)\epsilon/(2\pi)\).

The exact folded lower trace weights have the form
\(e^{-iNt}/(1-\eta e^{-iNt})^2\).
On a fixed positive lower height they are bounded by a
constant, with their favorable exponential decrease
discarded here. On the vertical midpoint segment the weight
is \(1/(4\cosh^2(Ns/2))\), also bounded.
The one-cell wire weight \(1/(1-e^{2\pi iNx})\) is bounded
on the upper arc, is even smaller on the lower arc, and has
modulus at most one on a half-index vertical side.
Thus every original alias and every vertical term is
included, at only polynomial scalar cost.

The complete rate is bounded by
\[
 2M_\infty+
 2\omega_T(2\epsilon)+4\epsilon+
               \frac{(n+p)(T+\epsilon)\epsilon}{2\pi}.
 \tag{7}
\]
Choose \(\epsilon\) so its last three terms are below
\(\delta\). The fixed curve lengths and parametrization
derivatives are absorbed in \(C\); Lemma 1 shows that no
height-derivative term is missing.
Cauchy on slightly larger collars proves the same bound
for fixed outside normals, with a polynomial additional cost.
The estimate holds through both level parities. \(\square\)

For a positive internal pair take \(\delta=1/200\).
The original pair energy gap is
\(M_{n,p}>2M_\infty+1/100\), so (6) is below its selected
rate by more than \(1/200\).
The real-tail cuts of the combined reduction may be moved
closer to \(0\) and \(1/2\) to lie in these collars; this
only reduces the omitted real tails.
Choose the wire and both trace heights small on the collars,
and equal to their desired geometric heights near the
critical point. Smooth positive interpolation is legal by
Lemma 1. The theorem controls the collar portions and their
endpoint currents, but does not estimate the interpolation
in the middle band.

## 3. Geometric interpretation of the two endpoint phases

On a positive lower angular branch, the exact continued
phase identities are
\[
 b(0,t)=0,\qquad b(1/2,t)=it/2.
 \tag{8}
\]
Thus the endpoint shared-wire phase decouples the two vertices.
At \(x=0\) its one-vertex terms are the complete-edge filling
phases of charge one; at \(x=1/2\) they have charge one half:
\[
 S_n(\lambda)=\operatorname{crit}_t
       \left[\psi(t,0)+\frac{int^2}{4\pi}-i\lambda t\right].
 \tag{9}
\]
The leaf case of the
[positive charge-cube theorem](research_positive_path_fractional_charge_cube.md)
supplies the branch satisfying
\[
       nt+2i\operatorname{asinh}(\tan(t/2))=2\pi\lambda,
 \qquad
 \frac{d}{d\lambda}\Re S_n(\lambda)=-H_n(\lambda)\le0,
 \qquad S_n(0)=M_\infty .
 \tag{10}
\]
Hence both decoupled selected endpoint rates are at most
\(2M_\infty\). This identifies the half-charge endpoint
without claiming its quantum coefficient.
Theorem 2 is stronger for the present purpose: its upper
bound keeps the full original finite trace and does not
require a half-charge packet or an endpoint stationary
phase theorem.

The remaining global problem is the middle wire band and
its coupled angular connecting surfaces. Neither a separate
worst-case estimate for a one-vertex Fourier source nor
strict concavity only near the selected point supplies
that missing estimate.
