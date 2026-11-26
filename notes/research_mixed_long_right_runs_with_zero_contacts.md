# Long right runs with arbitrary zero-collar contacts

Research deduction, 5 November 2026. The completed closed-half envelope
can be used as the replacement benchmark even when a right run touches
zero. This removes the zero-contact limitation of the separate direct
coherent replacement proof. It does not posit a coherent packet at zero.
Short right runs remain outside the theorem.

## 1. The original allocation and three kinds of coordinates

Fix a typed cyclic word of length \(m\ge1\), its actual reference \(r\),
an allowed original selection \(\sigma\), and
\(0<\rho\le1/1000\). Use the unchanged periodic
[hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
Partition the coordinates into
\[
 T=\{j:x_j\in[1/2,1]\},\qquad
 S=\{j\notin T:x_j<\rho\},\qquad
 A=\{1,\ldots,m\}\setminus(S\cup T).
 \tag{1}
\]
The half-angle boundary can be assigned consistently to either adjacent
set; the estimates include the closed endpoints. Every S target is real,
including physical angle zero. Every original allocated modulus is
\[
 \mathcal B_{j,N}=
 |C_{\epsilon_j,N}(X_{j-1},X_j)|
 |d_N(X_{j-1})X_{j-1}^{-N\sigma_{j-1}}|^{\epsilon_{j-1}/2}
 |d_N(X_j)X_j^{-N\sigma_j}|^{\epsilon_j/2}.
 \tag{2}
\]
These are nonnegative modulus powers. The two halves at each cyclic
vertex recombine exactly once.

We use a mixed upper envelope for (2). On every T-incident edge use the
complete raw row rate \(\mathscr F_j\), including the first-argument
chirp and both true Fourier alternatives. On every remaining S-incident
edge use precisely the fixed SS or SA ceiling of the
[closed-half proof](research_mixed_closed_half_period.md), Section 4.
On every other edge use its proved coherent rate, including both selected
branches. Denote the sum of these rates by \(\mathcal E_{\rm old}\).
For every fixed positive total tolerance, this bounds the entire original
finite product up to its fixed polynomial prefactor, uniformly through
zeros and at both level parities.

For explicitness put
\[
 \nu=-J(.001),\qquad\Delta=.001\log2-J(.001).
 \tag{3}
\]
On an ordered SS edge of types \((\eta,\epsilon)\) its fixed ceiling is
\[
 U_{SS}=\epsilon/6+2\Delta+(\eta+\epsilon)\nu/2.
 \tag{4}
\]
When only the second endpoint is in S, the ceiling is
\[
 U_{AS}=A_{\epsilon,\eta}(h_{\rm other})
                          +\Delta+\epsilon\nu/2.
 \tag{5}
\]
When only the first endpoint is in S, it is
\[
 U_{SA}=B_\epsilon(h_{\rm other})+\Delta+\eta\nu/2.
 \tag{6}
\]
The profiles are the original
[height-resolved full-source ceilings](research_mixed_height_resolved_seam_sources.md),
on the band chosen by the other endpoint's selection.
Equations (5)--(6) are whole allocated-edge rates, not additional
halfweights. The remaining seam halfweight occurs on its other incident
edge. Its selected monomial has unit modulus.

## 2. The repaired benchmark is a proved closed-half envelope

Replace every T coordinate by its reference real part and remove only
its selection. Recompute the hybrid targets and call them \(z^\#\).
Both old right real coordinates and their new reference reals have
every row's left cutoff equal to one. Therefore every non-T target,
selection and original edge not incident to T is unchanged exactly.
This remains true on the actual periodic collar
\(L_b(x)=1-x/\rho\).

The S set is unchanged, while every new right coordinate lies in A.
Use the same ceilings (4)--(6) on all repaired S-incident edges and the
complete coherent rate on every other repaired edge. The resulting
sum \(\mathcal E_\#\) is exactly a benchmark covered by the pointwise
closed-half argument:
\[
                        \mathcal E_\#\le M-3|S|/1000.
 \tag{7}
\]
If S is empty, this means the established half-period coherent inequality
\(\mathcal E_\#\le M\). No saddle phase is evaluated at an S endpoint.
In particular (7) is the proved mixed rate inequality, not an inference
from the final integrated closed-half theorem.

Let \(\Gamma_j\) be the original complex geometric tangent.
For any target vector, including one containing zeros,
\[
 \sum_j\Re\Gamma_j(z)=\sum_j\Re\Gamma_j(z^\#)=M.
 \tag{8}
\]
This is the original critical stationarity identity. The tangent is
affine and is well defined at zero without any conditional root there.
Since all non-T targets are unchanged, tangent differences also cancel
after restricting their sum to T-incident edges.

## 3. Three kinds of changed edge

On an internal TT edge the old rate is raw and the new rate is coherent.
The [direct-run deduction](research_mixed_direct_right_run_replacement.md)
gives tangent-subtracted difference at most \(-1/50\). Indeed the old
raw margin is \(1/50\), while the new coordinates have their reference
real parts and arbitrary admitted unselected height fractions; vertical
convexity gives their nonnegative residual above the original tangent.

On a TA or AT boundary edge, the new rate is also coherent. The
[quantitative boundary theorem](research_mixed_quantitative_right_run_boundary.md)
gives the tangent-subtracted costs
\[
                  B_{TA}<11/4,\qquad
                  B_{TA}<7/4\ \hbox{if }x_A\ge.1.
 \tag{9}
\]

On a TS or ST boundary edge, the new rate is instead (5) or (6).
The new right vertex is unselected. Every saved source-profile knot is
strictly greater than \(29/100\); interpolation on the appropriate band
preserves this strict lower bound for the chosen ceiling. The collar
costs in (3) are nonnegative. Hence
\[
                         U_{TS}>29/100.
 \tag{10}
\]
This is a lower bound for the fixed numerical ceiling used in (7),
not a lower bound for the modulus of the actual finite kernel.

The old TS raw source has rate less than \(13/8\), by the quantitative
theorem's whole-row and original-polynomial bounds. Those bounds hold
at S angle zero as well. Only the right argument changes in the
tangent difference, whose adverse contribution is at most
\(439/1250\). Consequently
\[
 B_{TS}<\frac{13}{8}-\frac{29}{100}+\frac{439}{1250}
       =\frac{8431}{5000}<\frac74.
 \tag{11}
\]
Thus a zero contact is no more expensive than the nonlow boundary
allowance. Both original Fourier halves and their selections remain
accounted for in (2), (5)--(6) and the old raw ceiling. No coherent
zero-endpoint packet or division by a possibly vanishing factor is used.

All other envelope terms cancel because their two targets, selections
and chosen source rules are unchanged. Adding the tangent-subtracted
differences and using (8) proves
\[
 \mathcal E_{\rm old}
 \le M-\frac{3|S|}{1000}
          +\sum_{\partial T}B_j-\frac{n_{TT}}{50}.
 \tag{12}
\]
There are no omitted neighboring-edge reset fees: every non-T height
is literally unchanged.

## 4. Uniform run bounds and the original finite integrals

**Theorem 1.** Allow arbitrary original coordinates on the full period.
If T is nonempty and every proper T run has length at least 552, then
\[
                \mathcal E_{\rm old}
                  \le M-|T|/100-3|S|/1000.
 \tag{13}
\]
If every non-T coordinate belongs to \([0,\rho)\cup[.1,.5]\),
length 352 suffices. All-T cycles satisfy the stronger loss \(m/50\)
without a length restriction.

A proper run of length k has two boundary edges and \(k-1\) internal
TT edges. In the first case use \(B_j<11/4\); in the second use
\(B_j<7/4\) on both TA and TS edges. The exact inequalities are
\[
 \begin{split}
 2(11/4)-(k-1)/50&\le-k/100&& (k\ge552),\\
 2(7/4)-(k-1)/50&\le-k/100&& (k\ge352).
 \end{split}
 \tag{14}
\]
Summing (14) proves (13). If all vertices are in T, every edge is
internal and its repaired targets are exactly their references.
If T is empty, (7) is simply the already completed closed-half
comparison; no artificial boundary is inserted.

All counts use physical edges. A shared S or A neighbor has its original
two halfweights, one on each of its incident edges. A one-cycle is either
all-T or has T empty. A mixed two-cycle has two distinct boundary edges,
so its algebra is still (12), although its singleton T run does not
meet (14). The argument does not require disjoint boundary stars.
All-S cycles use (4) and the closed-half benchmark, without a new
coherent interpretation at zero.

For each fixed word and collar width, spend one total finite-source
tolerance smaller than \(1/1000\) over all physical edges. Since
\(|T|\ge1\), (13) implies the complete finite-product upper rate
\[
                       M-|T|/200-|S|/500.
 \tag{15}
\]
Restoring the original polynomial powers, carriers, selected Laurent
factors and bounded hybrid Jacobian gives the same exponential upper
bound for the corresponding original selected integrals. Summing the
finitely many type-allowed selections and coordinate-set pieces changes
only the fixed-word prefactor. Both integer level parities are included.

Thus the full-period region with sufficiently long right runs is
exponentially suppressed even with arbitrary zero contacts. The theorem
does not cover the general short-run region. Other already established
subsets, such as the low/plateau/right assembly, remain valid and unchanged.
No complete whole-period asymptotic or enlarged knot-family theorem is
inferred.

## Reproduction

    python3 experiments/check_mixed_long_right_runs_with_zero_contacts.py

The focused checker validates the complete inherited profile table,
the exact boundary/run/tolerance arithmetic and current proof/source
bindings. No new roots, source cells, parameter covers or word-length
enumerations are performed.
