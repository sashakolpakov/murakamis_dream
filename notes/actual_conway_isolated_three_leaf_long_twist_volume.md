# Long fillings of the isolated three-leaf Conway source

31 October 2026. Internally reviewed original-source theorem.
The isolated closure $C(A_3)=C(hhh)$ has a whole-source alias gap and a
physical-color complement gap for every fixed pure or signed half-twist
pattern. Its existing finite complex packet and marked geometry therefore
give the original long-filling volume limit at both level parities.
The new input is the [uniform two-leaf block lemma](actual_conway_uniform_two_leaf_block_alias_gap.md),
including its endpoint $X=1/2$, together with the elementary three-alias
bound below. All original colors, Hermite normal directions, phases,
marks and circle factors are retained.

More precisely, let $\epsilon_l\in\{0,+1,-1\}$ at the three original leaves,
and let $Y^\epsilon$ be the actual augmented exterior. Fill any chosen
auxiliary subset $I$ by independently sufficiently long fixed signed
integral full twists $R^{-2p_i}$. The literal power at a filled leaf is
$\epsilon_i-2p_i$; an unfilled cusp is kept complete, not represented by
$p_i=0$. Then

$$
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|K_{C(A_3),N}^{\epsilon}(\mathbf p)\right|
 =\operatorname{Vol}\!\left(Y^\epsilon(\mathbf p)\right).
 \tag{1}
$$

The signs, filling subset and slopes are fixed before $N$ tends to
infinity. The threshold depends on the fixed source, sign pattern and
filling subset; all independently chosen $|p_i|$ beyond it are allowed.
The slopes need not have the same sign or comparable magnitudes. Both parity subsequences and
composite levels are included. After all auxiliary fillings, a loop-free
one-main-component parity pattern gives a knot, and the right side of (1)
is its hyperbolic **knot complement volume**. Partial fillings retain the
actual remaining cusps. The normalization is the original marked one-cut
scalar: its external enhancement has unit modulus for the reduced enhanced
Kashaev invariant, and modulus $1/N$, once, for the full modified one-cut
normalization. These are the unchanged
[original normalization conventions](actual_complete_augmented_source_normalization.md)
and [crossing comparison](kashaev_crossing_and_period_lattice.md).

## 1. Exact regrouping in the original source

Each physical changed leaf is $X_l=T(R^{\epsilon_l}L_{j_l})$, with its
original turn, pivot, Cartan phase and independent color $1\le j_l\le N$.
It belongs to the full pair-Casimir algebra
$H_N=\mathbb C[z]/(2T_N(z/2)+2)$. Its exact core/alias split
$X_l=C_l+A_l$ also consists of elements of that algebra. Consequently
$\phi(X_1X_2X_3)=\phi((X_iX_j)X_k)$ for every permutation $(i,j,k)$.
This is associativity and commutativity of the actual physical commutant,
with the original marked Frobenius functional. The complete turned coupons
are formed first; no factor is moved across a quarter-turn. It is an
algebraic identity for the original scalar, not an assertion that arbitrary
permutations of physical tangles are relative-boundary isotopies.

There is an explicit verification using the
[original positive Newton product](actual_positive_newton_multiplication.md).
Put $d=N-1$, $M=\lfloor d/2\rfloor$, and
$s_r=\prod_{t=1}^r2\sin(\pi t/N)$, with $s_0=1$. Its factorial reflection
$s_rs_{d-r}=N$, the positive product kernel, and
$\phi(\widehat B_u\widehat B_v)=\mathbf 1_{u+v=d}$ give

$$
\begin{aligned}
\mathcal T_N&=\{(i,j,k)\in\{0,\ldots,d\}^3:
 i+j,\ i+k,\ j+k\le d,\quad i+j+k\ge d\},\\
\phi(\widehat B_i\widehat B_j\widehat B_k)
 &=
 \begin{cases}
 \displaystyle
 \frac{s_{i+j}s_{i+k}s_{j+k}}
 {N\,s_i s_j s_k s_{i+j+k-d}}, &(i,j,k)\in\mathcal T_N,\\[6pt]
 0,&(i,j,k)\notin\mathcal T_N.
 \end{cases}
\end{aligned}\tag{2}
$$

Indeed, start with $\mu_{i,j,d-k}$ and apply factorial reflection to its
three complementary indices. Every factorial index in (2) lies between
$0$ and $d$. The identity is symmetric and includes all repeated-node
normal data; its zero cases follow from full polynomial divisibility,
not just nodal values. The factor $1/N$ is the derived kernel scalar,
not an additional circle or mark normalization.

Thus, for each chosen alias subset, one may select the useful grouping
while bounding the same original signed sector. At most three free
original leaf indices remain; the internal pair output is exactly $d$
minus the third leaf index. The final gate coefficient is one.
Independent colors and either half-twist sign cause no exception. The
[full Newton transport](actual_odd_conway_newton_transport.md) and
[finite block source proof](actual_conway_two_leaf_block_source_gap.md)
supply the literal core/alias arrays, including odd alias indices above
$M$ and all Hermite directions.

For clarity, write the retained continuum profiles as

$$
\begin{aligned}
J(t)&=\int_0^t\log(2\sin(\pi u))\,du,\\
g(t)&=J(2t)-4J(t),\\
\widetilde g(t)&=g(\max\{t,1/4\}),\quad 0\le t\le1/2,\\
k(t)&=-2J(t/2),\quad 0\le t\le1,\\
m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
&\quad-J(z-x)-J(z-y)-J(x+y-z).
\end{aligned}\tag{3}
$$

These are upper rates for the actual finite core, alias and product
coefficients, respectively, with their original uniform errors. The
product domain remains $\max(x,y)\le z\le x+y\le1$.

## 2. One or two aliases: the endpoint of the uniform block lemma

The isolated complete optimum has all three leaf coordinates

$$
\begin{aligned}
a&=\frac{\arctan2}{\pi},\qquad
X=\cot(\pi a)=\frac12,\qquad b=1-a,\\
\lambda&=F_2'(b)=g'(a)=-\log4,\\
F_0&=3g(a)+m(a,a,1-a)=\frac{2v_8}{\pi},
\end{aligned}\tag{4}
$$

where $F_2(b)=2g(a)+m(a,a,b)$ is the optimized pure pair action at this
output. These are the exact
[three-leaf complete-source formulas](actual_conway_complex_window_laplace.md),
§6. The internal pair gate is strict, even though this pair is not a
proper macro-seed with $X>1/2$. The uniform block lemma includes $X=1/2$
and supplies a margin greater than $1/100$ throughout the output interval.

For one alias, group it with a core, leaving the other core. For two
aliases, group them together, leaving the unique core. Equation (2)
justifies either grouping with the original colors and signs. If $z$ is
the pair output and $u$ is the remaining core output, their upper rates
satisfy

$$
\begin{aligned}
G_{\mathrm{AC}}(z),\ G_{\mathrm{AA}}(z)
 &\le F_2(b)+\lambda(z-b)-\frac1{100},\\
\widetilde g(u)&\le g(a)+g'(a)(u-a).
\end{aligned}\tag{5}
$$

The second inequality is the complete core tangent, valid because
$a>1/4$. The exact root relation is $z+u=d/N$. Since $a+b=1$ and
$g'(a)=\lambda$, the summed per-state action is at most

$$
F_0-\frac1{100}+\lambda\left(\frac dN-1\right)
 =F_0-\frac1{100}+\frac{\log4}{N}.
\tag{6}
$$

The affine discrepancy is therefore bounded in the exponent. There are
only polynomially many states, and the original local errors are
uniformly $o(N)$. Each such signed sector has upper rate at most
$F_0-1/100$, uniformly over its physical colors. No individual alias
tangent at $a$ is required.

## 3. Three aliases: an elementary absolute margin

Let $v_3=3\Lambda(\pi/3)$ be the regular ideal tetrahedron volume, where
$\Lambda$ is the Lobachevsky function, and let $v_8=4G$, where $G$ is
Catalan's constant. The maximum of $k$ on $[0,1]$ is $v_3/\pi$. Its
normalization follows, for example, from

$$
J(2t)=2J(t)-2J(1/2-t),\qquad
3J(1/3)=2J(1/6),\qquad
k(1/3)=-3J(1/3)=\frac{v_3}{\pi}.
\tag{7}
$$

The retained product action is the sum of three ideal-tetrahedron
volumes divided by $\pi$. Explicitly, with
$p=z-x$, $q=z-y$, $r=x+y-z$ and $w=1-x-y$, the angle triples are
$(y,x,w)$, $(p,q,2r+w)$ and $(p+q,r,r+w)$. Each is nonnegative with
sum one on the true product domain, including its boundaries and an
allowed input above half. Each triangle entropy is at most $v_3/\pi$,
so $m\le3v_3/\pi$. The final gate is flat and contributes no action.
Every three-alias sector therefore has upper rate at most $6v_3/\pi$.

The strict comparison needs no decimal volume estimate. The sine series
gives

$$
v_3=\frac{3\sqrt3}{4}\sum_{n\ge0}
 \left(\frac1{(3n+1)^2}-\frac1{(3n+2)^2}\right)
 <\frac{39\sqrt3}{64}<\frac{273}{256}.
\tag{8}
$$

The $n=0$ term is $3/4$. For $n\ge1$, replacing the second denominator
$3n+2$ by $3n+4$ strictly increases the differences, and the resulting
tail telescopes to $1/16$. The last inequality uses $\sqrt3<7/4$.
The first two alternating Catalan terms give $v_8>32/9$. Thus

$$
F_0-\frac{6v_3}{\pi}
 =\frac2\pi(v_8-3v_3)
 >\frac2\pi\frac{821}{2304}
 >\frac{5747}{25344}
 >\frac1{100},
\tag{9}
$$

using $\pi<22/7$. This is a coarse exact bound, not a claim that the
alias upper profiles attain it.

There are seven nonempty alias subsets. Summing their bounds and
absorbing the polynomial factors and uniform $o(N)$ errors gives,
at both parities and for all sufficiently large $N$,

$$
\sup_{1\le j_1,j_2,j_3\le N}
 \left|Z_N^\epsilon(\mathbf j)-Z_N^{\epsilon,\mathrm{core}}(\mathbf j)\right|
 \le \exp\!\left[N\left(F_0-\frac1{200}\right)\right].
\tag{10}
$$

The estimate may also be maximized over the finitely many sign patterns.
Pure-alias nilpotent vanishings can improve some sectors, but are not
assumed for arbitrary mixed patterns.

## 4. Whole physical-color complement and the finite complex packet

On the all-core support the limiting majorant is

$$
\overline F(x_1,x_2,x_3)
 =\sum_{l=1}^3\widetilde g(x_l)+m(x_1,x_2,1-x_3),
\qquad
0\le x_l\le\frac12,\quad x_1+x_2+x_3\ge1.
\tag{11}
$$

It is concave and agrees with the pure action near the strict complete
optimum $(a,a,a)$, since $a>1/4$. Its Hessian there is negative definite.
If another point also maximized it, the intervening segment would
contradict this local strictness. Thus this is its unique global maximum,
and the complement of any small fixed complete-state window has a
compact gap. Continuity carries the gap to the exact finite supports.

Inside that window, every leaf lies below a fixed $\beta<1/2$. The
existing actual core recurrence gives a strict local rate loss when its
physical color lies outside a fixed small complete corridor. The
high-index proof requires the strict quarter condition $a>1/4$, not
the proper-seed upper bound on $a$. Pure leaves satisfy the corresponding
factorial estimate; a zero core causes no difficulty. Combining the
inside and outside regions with (10) proves, for every fixed sufficiently
small $\delta>0$, some $\gamma_\delta>0$ such that

$$
\max_{\substack{1\le j_l\le N\\
             N-j_l\ge\delta N\text{ for some }l}}
 |Z_N^\epsilon(\mathbf j)|
 \le\exp[N(F_0-\gamma_\delta)]
\tag{12}
$$

for all sufficiently large $N$, at both parities.

The minimal-seed lattice and pure packet are explicitly calibrated in
[the finite complex-window theorem](actual_conway_complex_window_laplace.md),
§6. The three original leaf indices $i,j,k$ are free primitive integer
coordinates, and the retained gate output is
$t=d-k=N(1-x_3)-1$. Every factorial argument at $(a,a,1-a)$ is strict.
Rounding this three-dimensional lattice works at every sufficiently
large level without a parity constraint. Its complete negative Hessian
and pure amplitude are

$$
A=\frac{25\pi}{4}(I_3+\mathbf1\mathbf1^\mathsf T),
\qquad
\sqrt{\det A}=\frac{125\pi^{3/2}}4,\qquad
a_{\mathrm{pure}}(0)=\frac{\sqrt2}{64}.
\tag{13}
$$

The output shift by $-1$ contributes the essential factor
$\exp(-m_z)=4$ at completeness. The calibrated pure packet has power
$N^{3/2}$ and phase $F_0$. No unspecified lattice density or periodic
prefactor is introduced.

For changed leaves, each local high-index theorem in
[the actual mixed complex packet](actual_odd_conway_complex_color_packet.md),
§§1–6, applies on a fixed compact neighborhood of
$a\in(1/4,1/2)$. Its finite source formula, chirp and exponentially
accurate relative interpolation do not depend on seed width or require
two completed root children. Here $H=3$, there is one retained gate, and
the interpolated summand has power $N^{3-H}=1$. The primitive Gaussian
sum supplies $N^{3/2}$.

With these free leaf coordinates, all leaf offsets are zero: the sole
leading affine offset is $\exp[-m_z(x_1,x_2,1-x_3)]$, evaluated at the
changed critical point. It equals $4$ only at completeness. If different
shifted leaf coordinates are used, the general offset formula in the
packet theorem, (23), uses the changed leaf derivatives $f_{\epsilon_l}$.
No pure colored offset is reused away from completeness.

The changed complete multiplier and the retained external phase are

$$
\begin{aligned}
a_\epsilon(0)
 &=\frac{\sqrt2}{64}
 \prod_{\epsilon_l\ne0}\sqrt{\sin(\pi a)}
                       \exp(-i\epsilon_l\pi a/2)\ne0,\\
\eta_N&=\exp\!\left[\frac{i\pi d}{4}\sum_{l=1}^3\epsilon_l\right].
\end{aligned}\tag{14}
$$

The phase $\eta_N$ remains outside the normalized packet. Its separately
even color action has Hessian

$$
\partial_{\chi_l}\partial_{\chi_m}\Phi_\epsilon(0)
 =-\frac{\pi}{1-\epsilon_l i/2}\,\delta_{lm},
\tag{15}
$$

whose real part is negative definite. All original $N^2$ circle factors,
Hermite normal data and exact $N-1$ offsets remain unchanged. The finite
window contour proof therefore gives the same normalized complex packet,
with nonzero leading amplitude and relative $O(N^{-1})$ error. Equations
(10) and (12) supply the previously missing comparison with the whole
physical mixed source, including aliases and color endpoints.

## 5. Marked geometry and the filling conclusion

Use the existing [complete geometry of isolated $C(A_3)$](actual_positive_conway_hyperbolic_volume.md),
§§2, 6–7. Its proof explicitly glues the completed $hh$ child to the
last leaf with the corresponding $\pi/2$ CAP sums; it does not assume
that both root children are completed cells. The literal closed
projection cut, right-angled polyhedron and full cusp checks already
cover this case. Its doubled complete volume is $4v_8$. The
[half-twist partners](actual_conway_half_twist_partner_geometry.md)
use the same original leaf disk maps and retain this complete volume
at every fixed sign pattern.

The selected mixed action is regular at all three strict high leaf
indices, and its wire Hessian (13) is invertible. The original rational
white, prism, turn and closing maps and signed shaded words therefore
assemble its nearby representation through the
[marked peripheral deformation](actual_odd_conway_marked_peripheral_deformation.md),
§§4–6. Its primitive coordinates remain

$$
U_l=-2\pi i\chi_l,\qquad
V_l=-2\,\partial_{\chi_l}\Phi_\epsilon.
\tag{16}
$$

No pure rational-filling substitution is made. The complete geometric
anchor fixes the absolute regulator, and every main cusp remains
parabolic. The selected action, original finite packet, nonzero
amplitude and both whole-source gaps now supply every hypothesis of
the [original-source long-filling transfer](general_original_source_long_filling_transfer.md).
With the original primitive slope convention, the critical equation is
$U_i+p_iV_i=-2\pi i$. The same action and normalization identify the
limit with the actual hyperbolic exterior volume, proving (1).

After all auxiliary fillings, each leaf is the literal rational tangle
$T(R^{\epsilon_l-2p_l})$. Their original products and cylindrical closure
give a Conway algebraic link; the
[one-main-component parity criterion](actual_odd_conway_long_filling_volume.md)
selects knots. All auxiliary components have then been removed by
filling, while the knot cusp remains complete. No rational-fraction
arithmetic is being substituted for tangle isotopy. This extension makes
no assertion about isolated $C(A_2)$, arbitrary algebraic tangles, or
diagrams varying without bound as $N$ grows.

## Internal review and validation scope

The complete private source and packet proof, including the exact triple
kernel, original finite supports, endpoint tangent cancellation, elementary
three-alias margin, primitive three-dimensional lattice, gate offset,
changed amplitude and color Hessian, and marked filling interfaces, received
full analytical/source reviews from the primary agent and both independent
peer agents. The complementary alias-gap proof received an additional full
source review. These are internal reviews, not external peer review.

The proof uses the retained original coefficient, packet and marked-geometry
theorems at the strict isolated state and the exact rational certificate
for the uniform block lemma. No new numerical test or asymptotic inference
from finite samples is used here. Native equation rendering and relative
source links are checked separately. Existing theorem, checkpoint, status
and public files are unchanged.
