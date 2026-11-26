# A complete block estimate when an outer angle lies in the right half-period

Research proof, 4 November 2026. This combines estimates for the original
finite source. It does not assert a bound for the whole outer integral.

## 1. The finite function and the geometric plane

Let \(r=e^{-2\pi i/N}\), and write
\[
 P_j=\prod_{k=1}^j(1-r^k),\qquad
 p_j(X)=\prod_{k=1}^j(1-r^kX),\qquad
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},
 \quad \epsilon\in\{0,1\}.                                  \tag{1}
\]
Empty products equal one. Let \(d_N\) be the original finite Fourier
polynomial defined in the
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md).
It is kept exactly; its forced difference equation, rather than just
its values at roots of unity, underlies the bounds used here.

Fix a finite cyclic word in three- and four-crossing blocks. At one block
let \(\epsilon\) be its four-crossing indicator and \(\eta\) the
indicator of its left neighbor. Let \(a,b\) be its two outer parameters
at the actual cyclic critical point. The previous localization theorems
give
\[
 a\in R_{3+\eta},\quad b\in R_{3+\epsilon},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                                 \tag{2}
\]
Use the normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
\]
Eliminate the inner variable \(s\) by its established original
logarithmic stationary equation, and put
\[
 \Phi(a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
             -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
\]
The complex tangent at this fixed reference is
\[
 \Gamma(z,w)=\Phi(a,b)+\Phi_a(a,b)(z-a)+\Phi_b(a,b)(w-b).       \tag{3}
\]
It includes the imaginary-height terms. The real parts of both tangent
slopes lie in \((-1/5,1/4)\), by the
[correlated slope theorem](research_mixed_geometric_support_slopes.md).

## 2. The contours and the assertion

Choose either quadratic taper \(\chi\): it rises from zero to one
on \([0,l]\) as \((x/l)^2\), equals one on \([l,r_0]\), falls
to zero on \([r_0,1/2]\) as
\(((1/2-x)/(1/2-r_0))^2\), and vanishes on \([1/2,1]\).
The two choices are
\[
                 (l,r_0)=(1/4,2/5)\quad\hbox{or}\quad(11/50,9/20).
                                                                  \tag{4}
\]
For an unselected variable with critical height \(h_*\), its target
at angle \(x\) is \(x+ih_*\chi(x)\). A selected four-type variable
instead has target height \((7/500)\chi(x)\), and carries its original
factor \(X^{-N}\). There are no selected three-type variables.
Both choices in (4) fit the same support bounds; no choice of taper
may depend on \(N\).

For targets \(z,w\) of these forms let \(X=e^{-2\pi iz}\),
\(Y=e^{-2\pi iw}\). With selected indicators \(\sigma_L,\sigma_R\),
define the allocated absolute block weight
\[
 B_N(z,w)=|C_{\epsilon,N}(X,Y)|
       |d_N(X)X^{-N\sigma_L}|^{\eta/2}
       |d_N(Y)Y^{-N\sigma_R}|^{\epsilon/2}.                    \tag{5}
\]
Only nonnegative real square roots of moduli occur in this notation.
It introduces no holomorphic square root of a Fourier polynomial.

**Theorem 1.** If at least one of \(\Re z,\Re w\) belongs to
\([1/2,1]\), then, uniformly in the target angles,
\[
 B_N(z,w)\le C N^A\exp\left\{N\left(\Re\Gamma(z,w)
                                       -\frac1{2000}\right)\right\}
                                                                  \tag{6}
\]
for all sufficiently large integer levels \(N\). Both level parities
and every permitted selected indicator are included. The constants may
depend on the fixed cyclic word; no restriction on its length or on its
mixture of three- and four-crossing blocks is added.

## 3. Proof by exhaustive parameter coverage

If both angles lie in \([1/2,1]\), their heights vanish. The
[two-right-angle theorem](research_mixed_two_right_source_bound.md)
proves (6) with the larger gap \(1/100\). It remains to consider
one right angle \(x\in[1/2,1]\) and one left angle
\(y\in[0,1/2]\), at height \(h\).

Subtract the real tangent slopes from the full row envelope, retaining
the constant and imaginary parts of (3). The
[right-angle reduction](research_mixed_right_half_source_reduction.md)
reduces maximization in \(x\) to \(x=1/2\) and \(x=1\).
For upper indices \(u=j/N\ge1/2\), this is pointwise convexity
in \(x\). For lower indices the proof also adjusts \(u\), and,
when necessary, \(y\), to absorb the possible extra interior
right-angle maximum. It compares the full expression after subtracting
the tangent, rather than just its unweighted integral factors.

At \(x=1\), the
[endpoint theorem for all block types](research_mixed_all_endpoint_support.md)
applies. It bounds the absolute sum of all original rows at every other
angle and all permitted heights, with gap \(1/2000\). Its reference
rectangles include the actual reference (2). Both endpoint orientations
and the selected factors in (5) are part of that theorem.

At \(x=1/2\), the remaining coverage is as follows.

| Other angle | Lower indices \(u\le1/2\) | Upper indices \(u\ge1/2\) |
|---|---|---|
| \(.13\le y\le.5\) | The core comparison, with the established reduction of \(u<.2\). | The upper-index maximum is at \(u=.5\) or \(u=1\), both included in the core comparison. |
| \(0\le y\le.13\) | The lower-index reduction moves to \(y=.13\) at the same height. | The small-angle upper-index theorem moves to \((u,y)=(.5,.13)\) at the same height. |

Here the [core comparison](research_mixed_right_core_support.md) has
support gap \(1/500\), leaving finite-source gap \(1/1000\).
The two upper-index arguments are the
[endpoint reduction](research_mixed_high_row_endpoint_reduction.md)
and the [small-angle reduction](research_mixed_small_angle_high_rows.md).
The first allows \(|h|\le.057\). The second needs \(|h|\le.03\),
which includes every type-three height and every type-four taper height
at \(y\le.13\). The core certificate contains separate profiles at
\(y=.13\) with the entire image of these small-angle heights. Thus
moving the angle does not silently replace its original height by the
height of the graph at the new angle.

Every rectangle or endpoint in this table retains both alternatives
in the actual Fourier-weight upper bound. The right variable has
height zero, so its selected factor has modulus one. The other selected
factor is retained throughout. The finite-product estimates sum at most
\(N\) original rows and introduce only polynomial factors and the
already allocated Fourier tolerance. Taking the larger of the two
right-angle endpoint estimates proves (6). No row deletion, sign
assumption, or cancellation between rows is used. \(\square\)

## 4. What this gives in a cyclic product

Each Fourier weight is split between its two incident blocks in (5).
Multiplying therefore restores its original integer power exactly.
For the actual cyclic critical reference, stationarity gives
\[
 \sum_v\Gamma_v(z_{v-1},z_v)=\sum_v\Phi_v(a_{v-1},a_v),        \tag{7}
\]
because the two derivatives incident to each outer variable sum to zero.
The corresponding constant real part is the critical rate.

Equation (6) supplies a strict loss for every block touching a right-half
angle. To use (7) on a whole outer region, the other blocks must also
be bounded by their own planes, or any excess from them must be
controlled. Theorem 1 supplies no estimate for a block with both target
angles in the left half-period. Consequently it proves a complete
local ingredient for the exterior comparison, but does not by itself
prove that the entire exterior integral is exponentially small or that
the original knot invariant has a nonzero geometric leading term.

## 5. An unaliased integral that can now be assembled

There is a larger outer region on which the other blocks are controlled.
Put
\[
 P=[.22,.45],\qquad R=[.5,1],\qquad U=(P\cup R)^m,             \tag{8}
\]
and choose the second taper in (4). Use no selected variables. On
\(P\), each target height is its actual critical height; on \(R\)
it is zero. Let \(f_{\varnothing,N}\) be the original normalized
unaliased Laurent integrand of the
[central integral theorem](research_mixed_central_outer_integral.md).
Its exact normalization, including the original powers of \(N\), is
unchanged.

**Theorem 2.** The integral of \(f_{\varnothing,N}\) over the part
of this graph parametrized by \(U\) has the same nonzero leading
coefficient, critical exponential and all-integer-level asymptotic
as its integral over the original central cube. Every part of \(U\)
with at least one right-half coordinate has an exponentially smaller
absolute integral.

*Proof.* The [plateau concavity theorem](research_mixed_plateau_accretivity.md)
proves the central asymptotic on the entire box \(P^m\).
Partition the rest of \(U\) according to which coordinates lie in
\(R\). Fix one of these nonempty choices. Each block touching an
\(R\)-coordinate satisfies (6). Every other block has both coordinates
in \(P\), at their unchanged critical heights. Strict real concavity
of its conditional action on that product gives
\[
 \Re\phi_v(z_{v-1},z_v)\le\Re\Gamma_v(z_{v-1},z_v).           \tag{9}
\]
The line segment from the reference to the target remains in the same
fixed-height product. This is a blockwise tangent inequality; it does
not require the individual block gradient to vanish.

The full conditional-source theorem and the true Fourier-weight bound
turn (9) into a finite block upper bound with any prescribed positive
rate tolerance \(\delta\). For each unselected four-type coordinate
in \(P\), its height is negative and \(\nu=-\Re g>0\). Its actual
Fourier envelope therefore has rate \(\nu\), as proved in the plateau
theorem. Both allocated half-weights use that same bound.

There is at least one block touching an \(R\)-coordinate, including
for a length-one cycle. Multiply the block bounds and restore the
original integer Fourier weights. Equation (7) cancels every linear
term in the tangent planes. Taking \(\delta<1/(4000m)\) for the
other blocks gives
\[
 |f_{\varnothing,N}|\le C N^A\exp\{N(M-1/4000)\},             \tag{10}
\]
where \(M\) is the original critical real action. The original
normalizing powers of \(N\) are absorbed in the polynomial factor.
The graph Jacobian is bounded independently of \(N\); in the
interiors of \(P\) and \(R\) it is one. The number of pieces is
finite for the fixed word. Integrating (10) and adding the already
evaluated plateau proves the theorem. The argument counts incidences
before identifying variables, so it also applies to cycles of lengths
one and two. \(\square\)

The complement of \(U\) contains any configuration with a coordinate
in \([0,.22)\) or \((.45,.5)\). Theorem 2 does not estimate that
complement. It also makes no claim about the selected Fourier terms
on the enlarged plateau. Both issues remain before the restricted
integral can be replaced by the full cyclic sum.
