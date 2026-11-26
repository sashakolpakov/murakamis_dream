# The boundary polynomial for two adjacent power-two fillings

Research theorem, 2 November 2026. This note assembles the exact
rectangular contour and its proved bounds. The resulting asymptotic
holds for the entire original boundary polynomial. Its proof includes
a finite interval certificate for specified contour inequalities;
the exact contour identities, endpoint bounds, and Gaussian argument
are written below and in the cited research notes. The frozen
manuscripts are unchanged.

## 1. The polynomial and the statement

Let \(N\ge2\), \(q=e^{\pi i/N}\), and
\(F_k=(q^2;q^2)_k\). For \(0\le j<N\), put
\[
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\qquad
 e_j(z)=S_j^{-2}\prod_{r=0}^{j-1}
       \left(2\cos\frac{(2r+1)\pi}{N}-z\right).
\]
Empty products equal one. The original boundary polynomial is
\[
 Z_N(u)=N^2\sum_{i,j\ge0,\ i+j<N}
 q^{i^2+(i-j)^2}\frac{F_{i+j}}{F_i^3F_j^2}
                         e_j(-2\cos u).
 \tag{1}
\]
The [exact source calculation](research_adjacent_two_crossing_pair.md)
derives (1) from the original closing functional, including its
derivatives at repeated roots. Thus (1) specifies the entire source,
not only its values at distinct spectral points.

Write
\[
 W(x,y;u)=J(x+y)-3J(x)-2J(y)+b(y,u)
       +i\pi(x^2-xy+y^2/2+x+y/2),
 \tag{2}
\]
where \(J'(z)=\log(2\sin\pi z)\) continues from \((0,1)\),
\(J(0)=0\), and
\[
 b(y,u)=\int_0^y\log(2\cos2\pi t+2\cos u)\,dt-2J(y).
\]
The branches start at \(u=0\), \(0<y<1/2\), and continue
to the regular stationary point. At \(u=0\),
\(b(y,0)=J(2y)-4J(y)\).

The distinguished critical point is
\[
 x_* =\frac{\log((5+i\sqrt7)/16)}{2\pi i},\qquad
 y_* =\frac{\log(i/\sqrt7)}{2\pi i}.
 \tag{3}
\]
Both logarithms have arguments in \((0,\pi)\). Its Hessian
has negative definite real part, as proved in the source calculation.
The holomorphic implicit function theorem therefore gives a unique
nearby critical point \((x_*(u),y_*(u))\) for small complex \(u\).
Define
\[
 S(u)=W(x_*(u),y_*(u);u),\qquad M=\Re S(0).
 \tag{4}
\]
In particular \(M=0.8488512285\ldots\); the rigorous lower
bound used here is the rational interval in
[the horizontal maximum certificate](research_adjacent_two_crossing_horizontal_maximum.md).

**Boundary theorem.**
There is a fixed complex disk about zero and a nonvanishing
holomorphic function \(A\) on a smaller disk such that
\[
 Z_N(u)=A(u)e^{NS(u)}(1+O(N^{-1})),
 \tag{5}
\]
uniformly on that disk. The error is holomorphic. There are also
constants \(c,C,C_0,b_0>0\) and a fixed exponent \(a\) such that
\[
 |Z_N(t+iv)|\le C N^a
 e^{N\{M-c(1-\cos t)+C_0v^2\}},
 \qquad |t|\le\pi,\quad |v|\le b_0.
 \tag{6}
\]
These statements hold along all integer levels and retain the
original boundary variable. Their local phase is even and satisfies
\[
 S''(0)=-\frac{\sqrt7+3i}{8\pi}.
 \tag{7}
\]

## 2. The contour inputs and what each proves

The proof uses the following statements in the stated order.

1. [Extreme-index bounds](research_adjacent_two_crossing_global_tails.md)
   permit removal of \(j/N\notin[\epsilon,1/2-\epsilon]\),
   where \(\epsilon=10^{-6}\), with a strict exponential loss.
   Only this subset of the earlier tail estimate is removed; every
   first-variable index is retained.
2. [The rectangular extension](research_adjacent_pair_rectangular_extension.md)
   adds the indices \(i+j\ge N\), whose exact summands vanish.
   The first-variable interval consequently has length exactly one.
3. [The full-period residue formula](research_adjacent_pair_full_period_contour.md)
   writes this rectangular sum as sixteen integrals. It combines
   the two first-variable sides by their exact translation law
   before estimating them. The peripheral multiplier remains in
   this identity.
4. [The complete-circle bound](research_adjacent_pair_full_circle_bound.md)
   makes all four lower first-variable terms exponentially small.
   This is a cancellation statement about the integrals, not an
   absolute bound on their uncancelled integrands.
5. [The remaining surface bounds](research_adjacent_pair_grouped_contour_bounds.md)
   prove a strict loss for the
   combined first-variable sides, their second-variable endpoints,
   the upper first-variable endpoints in the second coordinate,
   and the upper-first/lower-second horizontal contour. Their common
   rate is below \(847/1000<M\), including the actual cutoff and
   half-grid displacements. The written proof gives the endpoint
   inequalities, and its standalone interval verifier covers the
   seven remaining compact rectangles.
6. [The horizontal maximum theorem](research_adjacent_two_crossing_horizontal_dominance.md)
   and its rational certificate give a unique global maximum at
   (3) on the principal upper rectangle. The part with
   \(\Re x\ge1/2\) has rate below \(1/2\), throughout the
   full rectangle, including its zero-extended portion.

The [uniform half-plane factorial expansion](research_factorial_uniform_halfplane_continuation.md)
justifies the continued asymptotic across \(\Re(x+y)=1\).
It retains the original normalization and square-root branch.
The upper correction in either variable has its additional strict
Fourier penalty. Thus these six inputs account for every term of
the exact residue identity. In particular no diagonal staircase
current, omitted endpoint, or unestimated lattice mode is left over.
The actual half-grid displacements are included in the residue
formula; its midpoint factorial bounds are uniform at the first
endpoint where an interior asymptotic alone would fail.

## 3. The local asymptotic

Near (3), the exact factorial expansion gives
\[
 f_N(x,y;u)=N^{-1}a(x,y;u)e^{NW(x,y;u)}(1+O(N^{-1})),
 \tag{8}
\]
with a nonzero holomorphic amplitude. The expansion and its error
are uniform on a fixed neighborhood. At \(u=0\),
\[
 a(x,y;0)=\frac18e^{-i\pi(x+y/2)}
   \frac{\sqrt{\sin\pi(x+y)}}
        {(\sin\pi x)^{3/2}\sin^2\pi y}.
 \tag{9}
\]
The square roots in (9) are those obtained from the canonical
factorial continuation. They are not chosen again after evaluating
the stationary point.

The principal integral has the prefactor \(N^2\) from the two
lattice kernels. Its strict exterior gap permits restricting it
to a fixed neighborhood of (3), with an exponentially small error.
For small complex \(u\), move this neighborhood through the
nearby critical point; the connecting boundary remains in the gap.
The integrand is holomorphic there. The real part of the negative
Hessian stays positive definite on the real tangent plane.

Taylor expansion and the substitution
\((x,y)=(x_*(u),y_*(u))+N^{-1/2}\mathbf z\) now give
\[
 A(u)=\frac{2\pi a(x_*(u),y_*(u);u)}
             {\sqrt{\det[-W''(x_*(u),y_*(u);u)]}}\ne0.
 \tag{10}
\]
The denominator uses the Gaussian branch on complex symmetric
matrices with positive definite real part. The Gaussian integral
has size \(N^{-1}\); together with \(N^2\) and the
\(N^{-1}\) in (8), this explains the absence of a power of
\(N\) in (5).

For clarity about the error, restrict the rescaled integral first
to a symmetric ball growing as a sufficiently small power of
\(N\). The cubic Taylor term and the first amplitude derivative
are odd, so their integrals against the centered Gaussian vanish.
The remaining Taylor terms are bounded by a polynomial times a
fixed decaying Gaussian and give relative error \(O(N^{-1})\).
Outside that ball the negative real Hessian gives a smaller error.
These bounds are uniform on a smaller complex disk in \(u\).
All discarded contour terms remain exponentially small there.
This proves (5).

The critical point, phase, and amplitude are even in \(u\),
because the exact local phase and amplitude depend on \(\cos u\)
and the nearby critical point is unique. The calculation of the
stationary boundary derivative in the exact source note gives (7).

## 4. Real angles and the complex strip

On every retained contour, the Newton estimate has a common
positive loss
\[
 \Re b(y,u)-\Re b(y,0)\le-c_1(1-\cos u),
 \qquad -\pi\le u\le\pi.
\]
The estimate is meant in its reciprocal-factorial form across
moving zeros. Its constant is positive because the real part of
\(y\) stays in a fixed compact subinterval of \((0,1/2)\)
and its imaginary part is bounded. The complete-circle estimate
is uniformly exponentially small over the same real period.
The discarded original indices have a uniform exponential gap;
reducing \(c_1\) absorbs that gap since \(1-\cos u\le2\).
The exact sixteen-term identity consequently yields
\[
 |Z_N(u)|\le C N^a e^{N\{M-c_2(1-\cos u)\}}
 \qquad(u\in\mathbb R).
 \tag{11}
\]

Here is a direct passage from (11) to (6). It uses the whole
polynomial, not a bound on an arbitrary interpolation. Its
trigonometric degree is at most \(N-1\). More generally, a
trigonometric polynomial \(P_N\) of degree at most \(dN\)
with the bound (11) satisfies
\[
 |P_N(t+iv)|\le C N^a
 \exp N\{M-c_2(1-\cos t)+(d+c_2)|v|\}.
 \tag{12}
\]
To prove this for \(v\ge0\), write
\(P_N(t)=z^{-D}p_N(z)\), \(z=e^{it}\), where
\(D\le dN\) and \(p_N\) is a polynomial. The Poisson
majorant of \(\log|p_N|\) on the unit disk, applied to
(11), is
\[
 \log(CN^a)+N\{M-c_2(1-r\cos t)\},\qquad r=e^{-v}.
\]
Multiplication by \(z^{-D}\) adds \(Dv\).
Use \(1-e^{-v}\le v\) to get (12). Reflecting the Laurent
polynomial proves the same estimate for negative \(v\).
Zeros cause no problem for the subharmonic maximum principle.

Away from a fixed neighborhood of \(t=0\), the loss in
(11) is bounded below. A sufficiently thin fixed strip
therefore absorbs the last term in (12), leaving half that
loss. Near zero, (5), evenness, and \(\Re S''(0)<0\)
give directly
\[
 \Re S(t+iv)\le M-c_3t^2+C_3v^2.
\]
Shrink the neighborhood and the strip, and bound the analytic
amplitude and error in (5). Combining the near-zero and
away-from-zero regions proves (6).

## 5. Geometric interpretation and scope

The [marked geometric calculation](research_adjacent_two_crossing_pair.md)
constructs the positive cone deformation for these two original
fillings and compares its action with (4) as a full boundary germ.
The comparison is \(S(u)=G(u)+i\pi\), with the absolute
volume constant fixed along that deformation. Thus (5) can also
be written with phase \(G\) and the unit factor \((-1)^N\).
At the complete remaining boundary,
\(2\pi M\) is the volume of that partially filled hyperbolic
exterior.

Equations (5)--(7) are exactly
the analytic hypotheses required by
[the long-filling theorem with complex boundary phase](research_long_fillings_complex_boundary_phase.md).
It treats the three-vertex path with first powers \((2,2)\)
and every sufficiently long fixed signed last power that gives
a knot, with the actual knot-complement volume. The power is fixed
before the level tends to infinity.

This is one specified adjacent short-filling component. It does
not assert stability after arbitrary adjacent short fillings,
and does not prove finitely many exceptions for all templates.
