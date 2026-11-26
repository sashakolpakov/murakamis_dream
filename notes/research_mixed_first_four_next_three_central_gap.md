# The first selected coordinate followed by a three-twist block

Research theorem, 6 November 2026.

For every fixed mixed open word of length at least three beginning with
types four and three, both central Fourier phase functions lie strictly
below the original geometric critical value. The comparison uses
the same critical point, the same other imaginary coordinates, and the
same outgoing affine term as the unselected source. Its gap in the real
phase is at least \(1/500\).

The proof bounds the cost of moving to one positive height. It does not
require a bound on the curvature of the moving maximum. This result
concerns the two central phase functions. To apply it to the complete
finite expression, the other finite rows and the joining and outer
parts of its contours still need estimates.

## 1. The reference, the two alternatives, and the statement

Fix a word \(n_1,\ldots,n_m\), where \(m\ge3\), each
\(n_j\) is three or four, and \(n_1=4,n_2=3\). Use the
actual open critical point constructed in the
[endpoint and ordinary equations](research_mixed_open_word_critical_localization.md).
Write \(e_*\) for the private coordinate at the first endpoint,
\(z_*\) for its attached coordinate, and \(s_*,b_*\) for
the two coordinates in the next ordinary block. Set
\[
 x_*=(\Re e_*,\Re s_*,\Re z_*,\Re b_*),\qquad
 c=\Im z_*,\qquad H=\frac7{625}.
 \tag{1}
\]
The other three imaginary coordinates are fixed at their starred
values throughout. The reference bounds include
\[
\begin{array}{c|c|c}
 &\text{real part}&\text{imaginary part}\\ \hline
 e_*&(.333,.363)&(-.051,-.019)\\
 z_*&(.246,.350)&(-.070,-.020)\\
 s_*,b_*&(.267,.433)&(-.065,.068).
\end{array}
\tag{2}
\]
These are bounds on one coupled critical point, not independent
parameters defining a new critical point.

Let \(f(x,k)\) be the real part of the joint endpoint and next-block
phase in [the static endpoint comparison](research_mixed_selected_endpoint_legendre_budget.md),
with its original outgoing affine term subtracted. Here
\(x=(e_R,s_R,z_R,b_R)\), and \(\Im z=k\). Let
\[
 G(k)=\max_x f(x,k),\qquad M=f(x_*,c),
 \tag{3}
\]
where, in the displayed coordinate order, the original horizontal
domain is
\(K=[.27,.49]\times[.15,.5]\times[.22,.45]^2\), as in
[the optimizer bounds, equation (4)](research_mixed_selected_boundary_optimizer_bounds.md).
In particular \(G(c)=M\), and the
first derivative in the height direction vanishes at \((x_*,c)\).
The two central alternatives at height \(H\) are
\[
 f_{\mathrm{fac}}(x)=f(x,H)-2\pi H,\qquad
 f_{\mathrm{force}}(x)=f(x,H)+\Re g(z_R+iH).
 \tag{4}
\]
The factorial primitive \(g\) has the original logarithmic branch,
with \(g'(z)=\log(1-e^{-2\pi iz})\). Its real restriction is
\(J(x)=\int_0^x\log(2\sin\pi t)\,dt\), so \(J(1/2)=0\).

**Theorem 1.** For every reference just described,
\[
 \max_x f_{\mathrm{fac}}(x)<M-\frac1{500},\qquad
 \max_x f_{\mathrm{force}}(x)<M-\frac1{500}.
 \tag{5}
\]
The constants are independent of the word length and its later types.
There is no change to the outgoing marginal or the logarithmic lifts.

## 2. Reduction to an explicit scalar function

Use the exponentials and the real logarithmic increments
\[
\begin{gathered}
 E=e^{-2\pi i e_*},\quad Z=e^{-2\pi i z_*},\quad
 S=e^{-2\pi i s_*},\quad
 \lambda=\frac{e^{2\pi H}}{|Z|},\quad\ell=\log\lambda,\\
 A=\log\left|\frac{1-\lambda EZ}{1-EZ}\right|,\quad
 B=\log\left|\frac{1-\lambda SZ}{1-SZ}\right|,\quad
 C=\log\left|\frac{1-\lambda Z}{1-Z}\right|,\\
 d=\ell-B>0,\qquad h=3C-\frac{B+\ell}{2}.
\end{gathered}
\tag{6}
\]
Define
\[
\begin{split}
 \mathcal B(A,B,C,\ell)={}&\frac{45}{298}h^2
 +\frac12\left(A-\frac{163}{298}h\right)^2
 +\frac{175}{768}d^2\\
 &+\frac23\sqrt{\frac{15}{14}}(d/2)^{3/2}
 +\frac23\sqrt{\frac65}(d/8)^{3/2}.
\end{split}
\tag{7}
\]
The centered scalar-cost estimate,
[equation (26)](research_mixed_centered_endpoint_scalar_costs.md), proves
\[
 \pi\{G(H)-f(x_*,H)\}\le\mathcal B(A,B,C,\ell).
 \tag{8}
\]
Its proof writes the horizontal gain as its linear gradient term minus
the sum of convex node and edge remainders. Keeping the actual center of the private edge gives
a quadratic bound for its conjugate; minimizing the resulting
quadratic in the private-edge variable produces the square in (7).
The two ordinary edges contribute the three-halves powers. Thus (8)
already includes movement of all four real coordinates, including a
maximum on a permitted boundary face.

**Lemma 2.** At every actual reference in Theorem 1,
\[
                  \mathcal B(A,B,C,\ell)<\frac{\pi^2}{128}.
 \tag{9}
\]
The computer-assisted proof of this scalar inequality is given in
Section 4. In particular it is a uniform enclosure, not a test at
sample words or approximate critical points.

## 3. The central gap follows from the endpoint bound

Equations (8)--(9) give
\[
                  G(H)-f(x_*,H)<\frac\pi{128}.
 \tag{10}
\]
On the fixed vertical segment the proved bound is
\(f_{kk}(x_*,k)<41\pi/10\). Since its first derivative vanishes
at \(k=c\), and \(H-c<203/2500\),
\[
 G(H)-M
 <\frac{41\pi}{20}\left(\frac{203}{2500}\right)^2
       +\frac\pi{128}
 =\frac{5332263\pi}{250000000}.
 \tag{11}
\]
The factorial alternative in (4) therefore satisfies
\[
 \max f_{\mathrm{fac}}-M
 <-\frac{267737\pi}{250000000}<-\frac1{500}.
 \tag{12}
\]

For the other alternative, the
[forced-coordinate bound](research_mixed_forced_optimizer_sharper_budget.md),
Proposition 2, places every maximizing point at \(z_R<2/5\).
On that set \(\Re g(z_R+iH)\le\Re g(2/5+iH)\), and the
same note proves
\[
 \Re g(2/5+iH)<-\frac{133}{2000}-\frac{\pi H}{10}.
 \tag{13}
\]
Combining (11) and (13), then using \(\pi<22/7\), gives
\[
 \max f_{\mathrm{force}}-M
 <\frac{5052263\pi}{250000000}-\frac{133}{2000}
 <-\frac{2612607}{875000000}<-\frac1{500}.
 \tag{14}
\]
Here \(G(H)\) is still the maximum over the original full horizontal
domain. The face exclusions used in deriving (8) only provide a
smaller set on which that same maximum can be computed. We do not
require the forced maximizer to belong to this smaller set: its
unselected phase is at most \(G(H)\) everywhere on the original
domain. This proves Theorem 1.

## 4. A complete interval proof of Lemma 2

The original endpoint coordinate \(u_*\) lies in
\[
 [217/1000,234/1000]+i[27/1000,45/1000].
 \tag{15}
\]
Put \(U=e^{2\pi i u_*}\). The
[rational endpoint equations](research_mixed_rational_critical_transport.md)
give the exact functions
\[
\begin{split}
 E(U)&=\frac{(U+1)^2}{5U^2-2U+1},\\
 Z(U)&=\frac{29U^4-36U^3+38U^2-20U+5}
                   {(U+1)^2(5U^2-2U+1)},\\
 S(U)&=\frac{(U-1)(U+1)^6}
 {(17U^3-21U^2+19U-7)(41U^4-34U^3+36U^2-14U+3)}.
\end{split}
\tag{16}
\]
For the next ordinary type-three block let
\[
 T=\frac{1-Z(1-S)^2/(1-ZS)}{S},\qquad
 V=\frac{1-ST}{T(1-ST)+(1-T)^2}.
 \tag{17}
\]
Here \(T=e^{-2\pi i b_*}\), and \(V\) is the exponential
of the next external coordinate. The code evaluates the expanded
rational function \(T(U)\) directly, rather than substituting three
separate enclosures into the first formula of (17).

Every actual reference satisfies the following necessary conditions.

1. The logarithmic coordinates of \(E,Z,S,T\) lie in (2).
2. The nonprivate coordinates \(s_*,b_*\) lie in the disk of radius
   \(.083\) about \(.35-.01i\), and \(z_*\) lies in the disk
   of radius \(.060\) about \(.30-.052i\).
3. The coupled sums obey
   \(.589\le\Re(z_*+s_*)\le.77\) and
   \(.635\le\Re(s_*+b_*)\le.77\).
4. The coordinate of \(V\) lies in \(K_3\cup K_4\), where
\[
\begin{split}
 K_3={}&\{|w-(.35-.01i)|\le.083,\quad
             -.072\le\Im w\le.068,\quad
             \Re w-3\Im w\le.608\},\\
 K_4={}&\{|w-(.30-.052i)|\le.060,\quad
             -.108\le\Im w\le-.001\}.
\end{split}
\tag{18}
\]

Condition 1 follows from the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
the [coupled height bound](research_mixed_first_four_attached_height_bound.md),
and the ordinary block image ranges. Condition 2 is the
[nonprivate-leg inclusion](research_mixed_open_local_factor_coverage.md).
Condition 3 uses the outward bounds in the type-three rows with a
type-four external input in the
[reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md).
For condition 4, the
[typed-domain inclusion](research_mixed_typed_last_row_envelopes.md)
includes both ordinary and attached coordinates. The next external
coordinate is attached when \(m=3\), so this case is included.
All their real parts lie between zero and one half; consequently
\(i\log X/(2\pi)\), using the principal logarithm, recovers the
actual coordinate of each exponential \(X\).

The interval program starts with (15) and bisects alternate real and
imaginary axes. It discards a rectangle only when a whole enclosure
contradicts one of these necessary conditions. An inconclusive or
nonfinite enclosure never justifies discarding a rectangle.

For a rational function \(R(U)\), the program evaluates
\[
 R(U)\in R(U_0)+R'(\mathcal U)(U-U_0),
 \tag{19}
\]
where \(\mathcal U\) is the enclosing complex rectangle and \(U_0\)
is its midpoint. Polynomial values and derivatives are evaluated by
Horner's rule with interval arithmetic. A finite quotient enclosure
ensures that its denominator does not vanish on \(\mathcal U\).
Since that rectangle is convex, integrating the derivative along
the segment from \(U_0\) proves (19). The exponential, logarithm,
modulus, and square root operations also use outward enclosures.

For every rectangle not discarded, the program evaluates (7). In
its two increasing powers of \(d\), it uses the nonnegative upper
bound \(\max(0,\sup d)\). This is valid at every actual reference,
where \(d>0\); no assertion about a fractional power of a negative
auxiliary value is used. A rectangle is accepted only if its full
upper bound is strictly below \(\pi^2/128\).

The completed calculation used 160-bit arithmetic and visited 5,583
tree nodes. Its 2,792 terminal rectangles comprise 1,169 accepted
rectangles and 1,623 exclusions, with none unresolved. The saved
addresses are prefix-free and have total dyadic weight one, so the
terminal rectangles cover (15). The largest recorded accepted upper
bound is less than \(.077094\), whereas
\(\pi^2/128>.077106\). The comparisons themselves use the
interval values, not these shortened decimals. Every actual reference
belongs to an accepted rectangle, which proves Lemma 2.

The [program](../experiments/certify_mixed_endpoint_log_budget.py) and
[completed record](../repro/results/research-mixed-endpoint-log-budget-attempt03.json)
retain the precise proof and code hashes, the splitting rule, and every
terminal address. The earlier two incomplete attempts remain in the
research archive; neither is used in this proof. The completed run
can be reproduced to a new output path with

```sh
python3 experiments/certify_mixed_endpoint_log_budget.py \
  --output /tmp/mixed-endpoint-log-budget.json \
  --max-cells 20000 --max-depth 24
```

## 5. What this result leaves to prove

Theorem 1 supplies both central real-phase comparisons for this
boundary configuration. It does not estimate the other rows of the
private finite sum, its contour joins or outer regions, or selected
coordinates elsewhere in the word. A first four-block followed by
another four-block and a word of length two also need their own
comparisons. These omissions matter because the desired conclusion
concerns the entire signed quantum expression.

The successful inequality is the centered bound (7). It does not
prove the older, larger scalar bound in equation (34) of the static
endpoint note, nor a bound on the curvature along the optimizing
path. Neither is needed for the central conclusion proved here.
