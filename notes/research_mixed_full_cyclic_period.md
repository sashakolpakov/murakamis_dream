# The complete cyclic sum for words in three and four

Research assembly, 5 November 2026. This note combines the closed-half
estimate, the nonlow right-half estimate, and the near-zero comparison
with raw right edges. The statement concerns the original cyclic matrix
trace. Its use for an open tangle or a partially filled knot requires
additional boundary estimates.

## 1. The finite quantity

Fix a word \(n_1,\ldots,n_m\in\{3,4\}\), with \(m\ge1\), and put
\(\epsilon_j=n_j-3\), \(k=\sum_j\epsilon_j\). At integer level
\(N\ge2\), let \(A_n=JM^n\) be the original Newton matrices and
\(\kappa_N\) their original scalar of modulus one. Define
\[
 T_N=\operatorname{tr}(A_{n_1}\cdots A_{n_m}).                 \tag{1}
\]
All matrices depend on \(N\). We use precisely the complete finite
Laurent integrands \(f_{S,N}\) of the
[local contribution theorem](research_mixed_local_outer_contribution.md),
equations (1)--(3), where \(S\) runs over subsets of
\(E_4=\{j:\epsilon_j=1\}\). Thus
\[
 T_N=\sum_{S\subseteq E_4}\int_{[0,1]^m}f_{S,N}(t)\,dt.     \tag{2}
\]
This is an exact finite identity, including the original scalar
\(\kappa_N^{m+k}N^{m+k}\), reciprocal-factorial polynomials and
additional frequencies at the selected coordinates.

Let \(z_*=(s_*,t_*)\) be the original geometric critical point of
the full action \(\mathcal F\) in that note, and set
\[
 F_* =\mathcal F(z_*),\qquad M_* =\Re F_*,\qquad
 H_*=-\mathcal F''(z_*),\qquad
 A_* =\frac{(2\pi)^m a(z_*)}{\sqrt{\det H_*}}.              \tag{3}
\]
Here \(a\) is exactly its equation (5), and the square root is
the branch specified by the original Gaussian integral. The original
critical-point and central-source theorems give \(A_*\ne0\).
In particular neither the phase constant nor the square-root choice
is left unspecified in (3).

Choose one fixed permitted collar width \(0<\rho\le10^{-3}\).
For each selection use the
[periodic hybrid graph](research_mixed_split_cutoff_hybrid_contour.md).
The exact graph identity applies to the complete Laurent polynomial,
before any asymptotic replacement. Write \(\mathcal Z_N(D)\)
for the sum of these differential-form integrals over a real
parameter set \(D\). Their Jacobians exist almost everywhere and
are bounded independently of \(N\). Then \(T_N=\mathcal Z_N([0,1]^m)\).

## 2. Every part of the right half is exponentially smaller

Let
\[
 D_R=\{x\in[0,1]^m:\max_jx_j>1/2\},\qquad
 S_0(x)=\{j:x_j<\rho\}.                                    \tag{4}
\]
Boundary faces have measure zero. They can be assigned to either of
the corresponding closed pieces, whose estimates include their limits.

If \(S_0(x)=\varnothing\), Corollary 2 of
[the middle-interval theorem](research_mixed_nonlow_middle_transport.md)
directly bounds the complete density by
\[
                    C N^B e^{N(M_*-1/2000)}.                \tag{5}
\]
The parameters in this bound are the original coordinates and the
original selection. Coordinates originally in the right half remain
labelled as raw edges after the comparison moves them to \(1/2\).

If \(S_0(x)\ne\varnothing\), apply
[the near-zero comparison with raw exterior edges](research_mixed_seam_raw_exterior_repair.md),
Theorem 2. Its upper envelope uses the established collar profile on
every edge meeting \(S_0\), including an edge that also meets the
right half. Every remaining right-incident edge uses the complete
absolute row bound. The comparison gives
\[
 \mathcal U_{S_0}(x,\sigma)
 \le \mathcal E_R(x^\#,\sigma^\#)-\frac{3|S_0|}{1000}.
                                                               \tag{6}
\]
The new coordinates lie in \([.1,.5]^m\); the original nonempty
right set is retained at \(.5\). Thus the rate conclusion of the
middle-interval theorem applies to the right side, giving
\[
 \mathcal U_{S_0}(x,\sigma)
 \le M_*-\frac1{1000}-\frac{3|S_0|}{1000}.                 \tag{7}
\]
Allocate a single total finite-source tolerance less than
\(1/2000\). The finite density then satisfies (5), with room to
spare. We use the pointwise rate conclusion in (7), not a second
application of the already rounded finite bound (5).

For a fixed word there are finitely many collar sets, right sets and
selections. Their original complete source estimates are uniform on
the relevant closed pieces. Their polynomial factors, the bounded
Jacobian, and integration over a bounded set give
\[
                    |\mathcal Z_N(D_R)|
                  \le C N^B e^{N(M_*-1/2000)}.              \tag{8}
\]
No coordinate replacement here is an integral substitution. It is a
comparison between upper rates for the original finite integrand.

## 3. The full trace and its nonzero coefficient

Put \(P=[.22,.45]\). The
[closed-half theorem](research_mixed_closed_half_period.md) supplies
\[
 \left|\mathcal Z_N([0,.5]^m)
                 -\mathcal I_{N,\varnothing}(P^m)\right|
           \le C N^B e^{N(M_*-1/8000)}.                     \tag{9}
\]
The two regions in (8)--(9) partition the full period up to null
faces. Their central terms are counted once. Therefore
\[
 \boxed{\left|T_N-\mathcal I_{N,\varnothing}(P^m)\right|
           \le C N^B e^{N(M_*-1/8000)}.}                    \tag{10}
\]

For completeness, the plateau integral has exactly the coefficient
in (3). Put \(B=[.25,.40]\); the
[central outer-integral theorem](research_mixed_central_outer_integral.md),
Section 3, evaluates \(B^m\). On \(P^m\), the unselected heights are
\(\Im t_*\), and the hybrid Jacobian equals one. The
[extracted plateau Hessian](research_mixed_extracted_plateau_curvature.md)
gives
\[
 \Re\Phi(x+i\Im t_*)\le M_*-\frac15\|x-\Re t_*\|^2.
                                                               \tag{11}
\]
Every reference real coordinate lies between \(.27\) and \(.39\).
Outside \(B^m\), at least one displacement in (11) has magnitude
greater than \(.01\). The complete plateau source bounds, with
one total tolerance below \(1/100000\), consequently give
\[
 \left|\mathcal I_{N,\varnothing}(P^m)
             -\mathcal I_{N,\varnothing}(B^m)\right|
       \le C N^B e^{N(M_*-1/100000)}.                       \tag{12}
\]
The phase loss is greater than \(1/50000\), so the
displayed finite tolerance is paid only once.

**Theorem 1.** At all sufficiently large integer levels, with both
parities included,
\[
 \boxed{T_N=\kappa_N^{m+k}A_*e^{NF_*}(1+O(N^{-1})),
                  \qquad A_*\ne0.}                        \tag{13}
\]
The constants and level threshold may depend on the fixed word.
Indeed the central theorem gives (13) on \(B^m\); (10) and (12)
add only exponentially smaller errors. In particular \(T_N\ne0\)
for all sufficiently large \(N\), and
\[
                  \lim_{N\to\infty}\frac1N\log|T_N|=M_*.
                                                               \tag{14}
\]
This lower bound uses the nonzero central coefficient and an absolute
bound for the entire remainder. It does not require nonnegative terms
in the finite sum.

The conclusion covers every fixed cyclic word in these two original
blocks, including lengths one and two. It is not yet a volume theorem
for an arbitrary knot: (1) is a specified matrix trace, and an open
tangle has additional boundary functions. Stability under arbitrary
fixed short partial fillings remains to be proved.

## 4. Reproduction

The focused checker validates the current source records and their saved
replays, the exact region partition and the loss budgets. It does not
recompute numerical covers or replace the arbitrary-length proof by
tests of finitely many words.

```sh
python3 experiments/check_mixed_full_cyclic_period.py
python3 experiments/check_mixed_full_cyclic_period.py --input repro/results/research-mixed-full-cyclic-period.json --output /tmp/research-mixed-full-cyclic-period-review.json
```
