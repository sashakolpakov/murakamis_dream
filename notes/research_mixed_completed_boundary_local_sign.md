# The local sign after the actual middle completion

Private research proof, 10 November 2026. The original open-word
Hessian pays the two boundary rates **after** their reserved middle
completion. The infimum here ranges over the full alphabet, not just
over a chosen local critical branch. Occupation coercivity first rules
out escape of its minimizers. The result also pays every pinned
finite-depth completion without spending its fixed approximation error
near the critical point.

The assertion is local in retained-leg boundary symbols at complete
ordinary colors \((-2,-2)\). It does not prove the remaining remote
endpoint comparison or a new full-source asymptotic.

## 1. The literal coherent boundary rates

Fix an original finite open word in three and four, its actual critical
point, and a safe middle interval \(I\) as in
[full-alphabet completion](research_mixed_actual_open_full_alphabet_completion.md).
The retained coordinates of the whole word are
\(t=(t_1,\ldots,t_\ell)\), with actual critical values
\(r=a+ic\). Write
\[
 \Phi_\ell(t)=\mathcal F_\ell(y(t),t),\qquad
 M=\Re\Phi_\ell(r),\qquad
 \mu=\frac{6\pi}{49}.
 \tag{1}
\]
This is the original stationary elimination of
\(y=(s_1,\ldots,s_\ell,u_L,u_R)\), with the full endpoint phases.
The [all-word local Gaussian theorem](research_mixed_open_local_gaussian.md)
proves the independent local packets for every literal factor and
identifies their summed phase with (1), with no additive recalibration.
The original Schur identity gives
\[
                 -\Re\Phi_\ell''(r)\succ\mu I_\ell.
 \tag{2}
\]
Both ordinary endpoint polynomials, terminal conditional factor,
actual Fourier polynomials and their original scalars are part of
that source theorem.

All actual retained real coordinates are strictly inside
\(P=[.22,.45]\). For the private and attached endpoint coordinates
this follows from
[the endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md);
the interior coordinates have the inherited typed ranges. Thus,
in a sufficiently small real neighborhood of \(a\), the unselected
hybrid graph is exactly \(t=x+ic\), with the original fixed heights.
The packet neighborhoods and (2) allow this neighborhood to be chosen
so that
\[
 \Re\Phi_\ell(x+ic)-M
                   \le-\frac{\mu}{4}\|x-a\|_2^2.
 \tag{3}
\]
For clarity, continuity preserves
\(-\Re\Phi_\ell''\succeq(\mu/2)I\) there; Taylor's integral formula
and the original critical equation prove (3).
The neighborhood may depend on the fixed word.

Let \(F\) be the middle indices other than its first and last three
physical symbols, and let \(B=\{1,\ldots,\ell\}\setminus F\).
Common entries of overlapping triples are counted once. A boundary
displacement is \(b=(x_i-a_i)_{i\in B}\). All these boundary symbols
are unselected. The indices in \(F\) will still range over their
entire original alphabet.

Near the reference choose the rates \(b_L,b_R\) in
[the open-boundary reduction](research_mixed_open_boundary_comparison_reduction.md)
to be the real phases of their literal coherent local packets.
These are valid sharp rates with polynomial prefactors; no fixed
positive exponential tolerance is necessary in a nonzero packet
neighborhood. Let \(\mathcal B_L(b),\mathcal B_R(b)\) be the resulting
calibrated rates, including the two original tangents and the six-edge
closing terms. On the full coherent local neighborhood the rate
accounting is then the exact equality
\[
 \boxed{\quad
 \mathcal B_L(b)+\mathcal B_R(b)-D(q)
                    =\Re\Phi_\ell(x+ic)-M.
 \quad}
 \tag{4}
\]
It follows by summing the original phase rates and tangent identity;
it is the equality case of the source reduction's equation (10).
It cannot be asserted for an arbitrary looser endpoint ceiling.

## 2. The full-alphabet infimum cannot escape locally

Fix \(0\le\theta<1\). Retain exactly the cost and occupation of the
full-alphabet completion:
\[
\begin{split}
 D_\theta(q)&=D(q)-\theta\kappa\sum_{i\in I}p_i(q),\\
 \kappa&=1/20000,\qquad \kappa_\theta=(1-\theta)\kappa,\\
 D_\theta(q)&\ge\kappa_\theta\sum_{i\in I}p_i(q),\\
 V_\theta(v_L,v_R)&=\inf_{\text{all middle symbols}}D_\theta(q).
\end{split}
 \tag{5}
\]
The prescribed terminal triples \(v_L,v_R\) are among the boundary
coordinates \(b\). The other boundary symbols outside \(I\) do not
enter \(D_\theta\). The infimum in (5) includes every allowed selection,
seam and right-half symbol.

For small prescribed triples, take the competitor which retains them
and sets all other symbols of \(I\) to baseline. Its entire support is
an unselected plateau. The ordinary pair energy has zero value and
gradient at its reference pair and Hessian at most \(20I_2\), by
[plateau boundary forgetting](research_mixed_plateau_boundary_forgetting.md),
equation (3). Each physical retained symbol has two ordinary incidences.
Taylor's formula therefore gives
\[
 0\le V_\theta(v_L,v_R)
 \le D_\theta(q^{\rm end})
 \le D(q^{\rm end})
 \le20\sum_{i\in I\cap B}(x_i-a_i)^2
 \le20\|b\|_2^2 .
 \tag{6}
\]
The sum counts overlapping prescribed symbols once.

Suppose \(b\ne0\), and choose a near-minimizer with
\(D_\theta(q)<V_\theta+\varepsilon\), where
\(0<\varepsilon\le\|b\|_2^2\). Then (5)--(6) give
\[
 \sum_{i\in I}p_i(q)
             \le\frac{21}{\kappa_\theta}\|b\|_2^2.
 \tag{7}
\]
Choose the boundary neighborhood small enough that this is less than
one. Every middle symbol is then unselected and in \(P\), and the
occupation has its literal quadratic value. In particular
\[
 \sum_{i\in I}|x_i-a_i|^2
           \le\frac{21}{400\kappa_\theta}\|b\|_2^2 .
 \tag{8}
\]
Together with the fixed boundary coordinates, (8) puts the complete
configuration in the source neighborhood of (3)--(4) after one further
shrink. This is uniform over all the near-minimizers under discussion;
neither their support size nor an assumed minimizing branch is used.
If \(b=0\), the baseline competitor has cost zero, and coercivity
makes it the unique zero-cost configuration.

Thus there is a positive neighborhood of \(b=0\) on which the infimum
over the complete alphabet can be taken entirely inside the genuine
coherent source chart. No assertion of this kind is made for a fixed
remote boundary state.

## 3. A strict completed boundary sign

In the chart forced by (8),
\[
 \theta\kappa\sum_{i\in I}p_i
                   =\frac{\theta}{50}\sum_{i\in I}(x_i-a_i)^2.
 \tag{9}
\]
Combining (3)--(4) with (9) proves
\[
\begin{split}
 \mathcal B_L(b)+\mathcal B_R(b)-D_\theta(q)
 &\le-\frac{\mu}{4}\|x-a\|_2^2
              +\frac{\theta}{50}\|(x-a)|_I\|_2^2\\
 &\le-c_\theta\|x-a\|_2^2,\qquad
 c_\theta=\frac{3\pi}{98}-\frac{\theta}{50}>0 .
\end{split}
 \tag{10}
\]
The positivity follows already from \(\pi>3\) and \(\theta<1\).

**Theorem 1.** For each fixed original word, each safe middle and
each \(0\le\theta<1\), there is a neighborhood of the actual unselected
boundary symbols on which
\[
 \boxed{\quad
 \mathcal B_L(b)+\mathcal B_R(b)-V_\theta(v_L,v_R)
                         \le-c_\theta\|b\|_2^2.
 \quad}
 \tag{11}
\]
The same inequality holds with \(V_\theta\) replaced by any completion
obtained by pinning additional middle coordinates to their actual
reference, provided the prescribed terminal triples are retained.
In particular it holds for every \(V_\theta^{[d]}\) in the
full-alphabet completion theorem.

*Proof.* For \(b\ne0\), apply (10) to a sequence of near-minimizers
as in Section 2 and let \(\varepsilon\) decrease to zero.
Since \(x|_B-a|_B=b\), this proves (11). The baseline case follows
from (4)--(6). Pinning coordinates restricts an infimum, so its cost
is at least \(V_\theta\), which proves the remaining assertion.
\(\square\)

This pays the completed boundary expression itself near the reference.
There is no use of the positive fixed error in the finite-depth
approximation, and no false claim that \(\mathcal B_L\) or
\(\mathcal B_R\) separately is nonpositive.

## 4. The exact real Schur response of the completed rate

The optimized cost has a unique real-analytic minimizing branch in a
possibly smaller boundary neighborhood. To justify this for the full
alphabet, the coercive bound above first confines every minimizing
sequence to a compact subset of the coherent chart. There the cost
is continuous and its free-middle Hessian is strictly positive.
Indeed, each free coordinate has two ordinary pair incidences,
whose Hessian lower bound is \(I_2/5\), while (9) subtracts only
\((\theta/25)I\) from that Hessian. Hence the lower bound
\[
                         \frac25-\frac{\theta}{25}>0
 \tag{12}
\]
holds on a small real convex neighborhood. A minimizer exists there,
is interior, and is unique; the real-analytic implicit-function
theorem applies at the baseline. This branch realizes the original
full-alphabet infimum by Section 2.

Let
\[
 H=\Re[-\Phi_\ell''(r)],\qquad
 H_\theta=H-\frac{\theta}{25}P_I ,
 \tag{13}
\]
where \(P_I\) is the coordinate projection on the original middle
indices, including its prescribed triples. Then
\(H_\theta\succ(\mu-\theta/25)I\). Split its indices into \(B,F\)
and set
\[
 S_\theta=(H_\theta)_{BB}
    -(H_\theta)_{BF}(H_\theta)_{FF}^{-1}(H_\theta)_{FB}.
 \tag{14}
\]
If \(F\) is empty, (14) means its first term. The exact optimized
rate has Taylor expansion
\[
 \mathcal B_L(b)+\mathcal B_R(b)-V_\theta(v_L,v_R)
        =-\frac12 b^TS_\theta b+O(\|b\|_2^3),\qquad
 S_\theta\succ(\mu-\theta/25)I_B .
 \tag{15}
\]
For the matrix lower bound, apply \(H_\theta\) to
\((b,-(H_\theta)_{FF}^{-1}(H_\theta)_{FB}b)\).
Its quadratic form equals \(b^TS_\theta b\), while its Euclidean
norm is at least \(\|b\|_2\).

Equation (15) follows from stationary elimination in the real
function (4) plus (9). This is a real horizontal Schur complement
after the original holomorphic elimination of \(y\). It does not
replace the complex Schur complement used to construct \(\Phi_\ell\).
If some middle coordinates are pinned, use the principal submatrix
on the boundary and remaining free indices in (14). The resulting
Schur matrix is at least \(S_\theta\) as a real quadratic form,
since a quadratic minimum is being taken over fewer variables.
This agrees with the exact inequality of Theorem 1.

## 5. What remains for the endpoint sign

The sign at the selected reference and throughout a sufficiently
small boundary neighborhood is therefore already forced by the
original source normalization, occupation bound and Hessian. The
known positive quadratic contribution to a *separate* raw boundary
rate is the relaxation term which (14) correctly retains.

This does not pay a remote boundary configuration. For such a state
(6) need not be small enough to force the full-alphabet minimizer
into the coherent chart. Even inside a geometric phase domain, a
literal endpoint factor may require an additional finite row or alias
profile. Extending (11) there requires a genuine comparison of those
original source rates with the optimized completion; a local Schur
matrix alone supplies none.

The ordinary-color response theorem concerns different variables:
its boundary angles deform \(\mathcal F_\ell\), whereas \(b\) here
varies retained integration coordinates at fixed ordinary colors.
No ordinary boundary strip, marked composition, knot identification
or finite-assignment conclusion is inferred from (11)--(15).
No radius uniform over all word lengths is asserted. The result is
compatible with the fixed-depth reduction: its remote approximation
error need only be used away from the now-paid local neighborhood.

## Source bindings

All direct inputs were read at the following unchanged hashes:

| File | SHA-256 |
|---|---|
| research_mixed_actual_open_full_alphabet_completion.md | d41f2c57b0ee397a24f299f5ffbfb132a1fb78ed1c47423543c56c975da0b782 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_open_word_hessian.md | 21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23 |
| research_mixed_open_local_gaussian.md | f3717d752fea9ea640c66b80ae805becde75bbd3dc3811493622bd124e01de89 |
| research_mixed_open_local_factor_coverage.md | b0fdc0b9b968c29469b86f5d29f9bc86b1dd535f762ac1386f96bd3514e3659a |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_plateau_boundary_forgetting.md | 6f3294e9beaaa20c1048dff534cca91d0036150ead2f6609df56a31a22f495c9 |
| research_mixed_open_word_boundary_response.md | 3dbf213d665eb74a84592bd497880ede215f45e9d9da710e7f9a6cd2c796057c |

No mathematical numerical evaluation, optimization run, source replay,
or edit to a frozen manuscript is used.
