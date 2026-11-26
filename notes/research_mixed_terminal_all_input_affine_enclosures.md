# Canonical terminal reference enclosures on both complete input disks

Research deduction, 6 November 2026. The split Taylor inclusion
certificate closes the two previously inconclusive type-three input
families. All four canonical terminal families now have complete
input-disk affine enclosures. The failed earlier criteria and their
records remain unchanged.

## 1. The four complete families

Write \(q=(e,\xi,t,a,s)\), let \(\beta\in\{0,1\}\) be the input
flag and \(\epsilon\in\{0,1\}\) the terminal flag, and put
\[
 \begin{array}{c|c|c}
 \beta&b_\beta&r_\beta\\ \hline
 0&7/20-i/100&9/100\\
 1&3/10-13i/250&8/125
 \end{array},
 \qquad D_{3+\beta}=\{|b-b_\beta|\le r_\beta\}.
 \tag{1}
\]
Let
\[
 \rho^0=(1/500,1/1000,1/200,1/200,1/100),\qquad
 \rho^{(\beta)}=(2-\beta)\rho^0.
 \tag{2}
\]
The exact Gaussian-rational vectors \(q^0_{\beta,\epsilon}\) and
\(u_{\beta,\epsilon}\) are the original center and response vectors
in the corresponding case of the
[split Taylor record](../repro/results/research-mixed-terminal-split-taylor-inclusion.json),
fields original_center and original_response. Their association
with the unchanged earlier affine proposals is recorded and checked.

**Theorem 1.** The original canonical holomorphic families satisfy
\[
 |q_{*,i}(b)-q^0_{\beta,\epsilon,i}
             -u_{\beta,\epsilon,i}(b-b_\beta)|
       <\rho_i^{(\beta)}
       \qquad(b\in D_{3+\beta})
 \tag{3}
\]
for all four pairs \((\beta,\epsilon)\). This includes the closed
input-disk boundaries.

Apply the [split Taylor theorem](research_mixed_terminal_split_taylor_inclusion.md)
to the same sixteen candidates used by the preceding correlated
run. Both type-three input cases satisfy its strict inclusion
inequality at multiplier 2; both type-four input cases satisfy it
at multipliers 1 and 2. The minimum margins for the four candidates
chosen in (2) have the following conservative lower bounds:

| \(\beta\) | \(\epsilon\) | Multiplier | Minimum margin |
|---:|---:|---:|---:|
| 0 | 0 | 2 | \(>11/10000\) |
| 0 | 1 | 2 | \(>118/100000\) |
| 1 | 0 | 1 | \(>63/100000\) |
| 1 | 1 | 1 | \(>77/100000\) |

All full-tube contraction bounds and original-log strip guards
are the already established bounds of the corresponding unchanged
candidate. The original center root belongs to each selected
central error polydisk. Hence contraction, local implicit uniqueness,
and analytic continuation give the original canonical branches,
not merely roots of exponentiated equations.

The successful fixed saved-only record has SHA256
a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202.
It binds 42 unchanged inputs and retains all sixteen outcomes.
There were no new analytic evaluations, proposals, roots, inverse
calculations, input cells, candidate radii, or subdivisions in this
inclusion test. The improvement comes from using the smaller
affine-path curvature bound and the exact \(1/2\) Taylor remainder
factor on the error path. It does not revise the old failed tests.

## 2. A componentwise posterior bound from the quadratic error cost

For one of the four certified candidates, use the split certificate's
nonnegative residual \(R\), affine Jacobian error matrix \(A\), and
primitive error radii
\[
 d_\ell=\sum_j|v_{\ell j}|\rho_j,\qquad
 Q_i(w)=\frac12\sum_\ell h_{\ell i}m_\ell^{\rm full}
                         \left(\sum_j|v_{\ell j}|w_j\right)^2.
 \tag{4}
\]
The true error vector
\(w_i=|q_{*,i}-q_i^0-u_i(b-b_\beta)|\) already satisfies
\(0\le w<\rho\). Its exact fixed-point equation and the error-path
Taylor expansion imply
\[
 w\le R+Aw+Q(w).
 \tag{5}
\]
Because \(0\le w\le\rho\),
\[
 Q_i(w)\le(C_{\rm err}w)_i,\qquad
 (C_{\rm err})_{ij}
       =\frac12\sum_\ell h_{\ell i}m_\ell^{\rm full}
                                    d_\ell|v_{\ell j}|.
 \tag{6}
\]
Set \(C=A+C_{\rm err}\). Then \(C\ge0\) and
\[
 R+C\rho=R+A\rho+Q(\rho)<\rho,\qquad
 w\le R+Cw .
 \tag{7}
\]
In particular \(\max_i(C\rho)_i/\rho_i<1\), so
\[
 (I-C)^{-1}=\sum_{n\ge0}C^n\ge0,\qquad
 w\le z:=(I-C)^{-1}R<\rho.
 \tag{8}
\]
The proof of strict \(z<\rho\) is the same positive-inverse argument
as in the [two-family completion](research_mixed_terminal_correlated_affine_family_completion.md).
The matrix \(C\) is an error-cost bound for the already located
root; it is not asserted to bound the full derivative on the tube.
Existence, uniqueness, and continuation continue to use the old
full-tube contraction certificate. This distinction prevents a
Taylor remainder factor from being incorrectly inserted into a
Jacobian contraction estimate.

Exact rational Gaussian elimination computes \(z\), and the
identities
\[
             (I-C)z=R,\qquad 0\le z<\rho
 \tag{9}
\]
check the posterior result. If a final upward rounding enlarges
\(C\), the checker directly rechecks the strict first inequality
in (7) before making this inference.

The affine statement retains one common parameter
\(b-b_\beta\). Its independent rectangular consequence is
\[
 |\Re(q_{*,i}-q_i^0)|,\ |\Im(q_{*,i}-q_i^0)|
                    \le r_\beta|u_i|+z_i .
 \tag{10}
\]
This may supply necessary force or curvature guards, but does not
by itself prove their required signs.

## 3. Saved-only verification and scope

The standalone checker
[check_mixed_terminal_split_taylor_completion.py](../experiments/check_mixed_terminal_split_taylor_completion.py)
binds the split record, its proof and checker, the original correlated
record and completed saved audit, and the canonical center record.
It verifies all inherited hashes before and after. It reconstructs
all sixteen split-inclusion sums and exact decisions, then chooses
only the four candidates in (2) for the posterior calculation.

The center Jacobian and affine error matrix are reconstructed using
the same pinned standard-library interval helper and conservative
serialized-endpoint convention. Each error-cost matrix summand in
(6) comes from the full primitive witness of the matching candidate.
All matrix entries and solutions are rational; decimal displays
carry no certification role. The checker makes no analytic callback
or reference/source evaluation.

The fresh output is
repro/results/research-mixed-terminal-split-taylor-completion.json.
It records the four posterior vectors, their exact linear-system
checks, independent coordinate rectangles, and the full unchanged
sixteen-candidate inventory.

These are complete-disk reference-coordinate theorems for both
terminal types. They do not assert a uniform negative finite-source
budget, a nonzero observed coefficient, realization of every
canonical input by a finite word, or a whole-knot volume identity.
Original oriented and inverse-feasible finite-source restrictions
remain in force wherever a separate source theorem uses them.
