# Payment of the complete physical middle sector

Research assembly, 7 November 2026. The saved enclosure of the original
ordinary three/four action, combined with an independent analytic upper
bound, discharges the physical middle-sector criterion. The diagnostic's
six lower-witness comparisons remain inconclusive. No computation is
repeated here, and no signed continuous arc is identified with a partial
sum over physical roots.

## 1. Saved certificate and unchanged action

The [computation record](research_mixed_three_four_half_face_witness_outcome.md)
retains the sole approved run and its four frozen artifacts:

| Artifact | SHA256 |
|---|---|
| Protocol | 628aace6ce85f5e7a8a19819255efb9fa119fb58d0ad11739bed0b8d64f40ad0 |
| Checker | eaa699d2d1e01758e923eab77f65cb2226508461e48013b5704e9a509cc935cd |
| Manifest | 6cab93f7480b7e7aad55efd3a7edabc5804a47b4f25ef8c35cb183ff94912493 |
| Result | fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70 |

The read-only audit of the saved evidence checked all 52 current input
bindings, all 14 transitive result dependencies, and all 37 successful
checks. The proposal inventory has exactly 24 iterations and one
inclusion test. All six prescribed witnesses were processed; there
are no errors, changed inputs, or unprocessed cases. The action was
evaluated once on the certified enclosure. This audit neither reran
the checker nor recomputed a root, phase, or witness.

The original six-variable action is
\[
\begin{split}
 \mathcal F={}&P_0(e_L,a,u_L)+P_1(e_R,b,u_R)\\
 &+J(a+b)-J(a)-J(b)+i\pi ab-g(b).
\end{split}                                                    \tag{1}
\]
The certified disks lie in the original open-word chamber and the
original attached reference domains. The existing uniqueness theorem
therefore identifies their zero with the prescribed ordinary three/four
reference. The matching identity in
[the original pair target](research_mixed_three_four_ordinary_pair_target.md),
equation (8), gives
\[
 M=\Re\mathcal F(z_*)=\Re\{T_0(a_*)+P_1(a_*)\}.                  \tag{2}
\]
In particular the terminal term \(-g(b)\), all chirps, and the original
primitive constants are retained. This is not a Fourier allocation or
a redefined geometric action.

The saved action lower enclosure begins with
\(2.7049005864313575583449\); its recorded outward error is less than
\(1.33\cdot10^{-76}\). It implies the coarse rational consequence
\[
                              M>\frac{27}{10}.                 \tag{3}
\]
Each of the six lower witnesses lies below the action enclosure, so the
recorded diagnostic verdict remains inconclusive. None of these lower
witnesses is used as an upper bound below.

## 2. The independent analytic upper bound pays the criterion

Keep the notation and all five private profiles of
[the physical middle reduction](research_mixed_three_four_physical_middle_reduction.md),
SHA256
0a94e52b2aaafcf50363381390ee7591038bf8058ca9ffd7213a19190ab8e40c.
The private main height \(h_e=0\) is allowed. The monotonicity proved
there, together with
[the analytic half-face ceiling](research_mixed_three_four_physical_half_face_ceiling.md),
SHA256
bf21ab20fa38760881ae9ee0e7203fb3f4c3ffe76feca5fbbadcbfb04a7b1994,
gives
\[
 \mathcal E(v;0)\le\mathcal E(1/2;0)<\frac{529}{200},
                     \qquad \frac16\le v\le\frac12.
                                                               \tag{4}
\]
All private cuts, aliases, joins, and physical private tails are part
of this envelope. The proof takes the private cap coherently before
the outer modulus; it does not replace that cap by a Newton subsum.

The exact rational comparison of (3) and (4) is
\[
 \boxed{\qquad \mathcal E(v;0)<M-\frac{11}{200},
                     \qquad \frac16\le v\le\frac12.\qquad}      \tag{5}
\]
This proves the sufficient criterion (17) of the middle reduction.
Its proof uses the independent analytic upper bound and the certified
action enclosure, rather than changing the meaning or verdict of the
six-witness diagnostic.

## 3. Complete finite-source consequence

Let \(r=e^{-2\pi i/N}\) and retain the literal functions \(U_{0,N}\),
\(V_{1,N}\), and \(\kappa_N\) of the original pair target.
For both parities of \(N\), the complete physical middle sector satisfies
\[
 \left|
  \partial_{w_L}^{k}\partial_{w_R}^{\ell}
       \{U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b)\}
 \right|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{N(M-1/25)},
 \qquad \frac12\le\frac bN\le\frac56.                            \tag{6}
\]
Here \(k,\ell\) are fixed. The estimate holds on sufficiently small
independent ordinary-color disks about \((-2,-2)\), and also uniformly
for both colors on the whole real interval \([-2,2]\), with the
corresponding fixed ordinary derivatives.

Indeed equation (14) of the middle reduction bounds the complete
product by the sum of the already paid true-transform-end contribution
of rate \(M-1/20\) and the remaining contribution of rate
\(\mathcal E(v;0)+\tau\). Choose one common \(\tau<1/200\).
Equation (5) places the latter below \(M-1/20\) as well.
Polynomial row counts and the inherited color tolerances leave the
weaker finite gap \(1/25\) in (6). The near-complete color derivatives
use fixed Cauchy disks; the all-real-color derivatives use the
whole-interval Newton bounds and Markov argument already included in
the reduction. No finite support or endpoint row is discarded in
this step.

The original root-sum normalization is
\[
       Z_{34,N}=\kappa_N^3N
             \sum_{b=0}^{N-1}U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b).
                                                               \tag{7}
\]
Since \(|\kappa_N|=1\), its prefactor and the number of physical rows
are polynomial. Consequently (6) pays the complete middle partial
sum with the same stated gap. Combining it with the independently
proved physical far-sector estimate in
[the physical far-half theorem](research_mixed_three_four_physical_far_half.md)
also gives, near complete colors and with fixed ordinary derivatives,
\[
 \left|\kappa_N^3N
       \sum_{b=\lceil N/2\rceil}^{N-1}
                U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b)\right|
       \le CN^B e^{N(M-1/200)}.                                \tag{8}
\]
If \(5N/6\) is integral, its row is counted only once.

These are physical-sample statements. An arc integral and the connector
from the stationary height require their own proof. That separate
argument is now supplied by
[the complementary-contour completion](research_mixed_three_four_complementary_contour_completion.md);
it is not inferred from (6) or (8). The present deduction itself adds
no knot-family or arbitrary-filling conclusion.
