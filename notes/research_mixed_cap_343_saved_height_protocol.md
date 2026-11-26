# Two fixed harmonic height comparisons from the saved cap-343 cover

Private protocol, 8 November 2026. **Unrun.** This is one prescribed
saved-response calculation on the complete original cap-initialized
ordinary \(343\) family. It introduces neither root proposals nor a
new parameter cover. The two comparisons, all settings, and the
entire inventory are fixed before any calculation.

Only the root may execute the single frozen attempt, after independent
full source/proof and code reviews and inspection of its manifest.
Writing or reviewing these files does not authorize execution.
No pilot, changed threshold, subdivision, retry, continuation, or
automatic replay is permitted.

## 1. Exact family and the two tests

Retain the seven-variable original zero-lift root, in the order
\[
                 v=(e,a,u,p,y,s,z),
\tag{1}
\]
and the two complete reduced external disks \(P_3,P_4\) of
[the original radius protocol](research_mixed_cap_343_radius_coverage_protocol.md).
The external input is \(b=s_4\). In particular \(p=s_2\) has
zero-based index 3, and \(y=t_2\) has zero-based index 4.
No terminal third vertex or independently chosen \(p,y\) is admitted.
The original holomorphic half-chain and its actual-word identification
are those of [the coverage audit](research_mixed_next_three_deep_radius_actual_coverage.md)
and [the radius exclusion theorem](research_mixed_cap_343_radius_exclusion.md).

The only new comparisons are
\[
\begin{split}
 f_1(b)&=\frac{\log(41/50)}{2\pi}-\Im y(b),\\
 f_2(b)&=\Im p(b)-\Im y(b)-\frac{\log(4/5)}{2\pi}.
\end{split}
\tag{2}
\]
Both are harmonic on a neighborhood of each closed disk.
Writing \(R=\exp(2\pi\Im y)\) and \(r_s=\exp(2\pi\Im p)\),
strict positivity implies respectively
\[
                    R<41/50,\qquad r_s>(4/5)R.
\tag{3}
\]
In particular it implies the weak inequalities with the same
constants. The second test is not \(r_s\ge R\).
These fixed constants are the sufficient hypotheses of
[the correlated last-row transport theorem](research_mixed_next_three_correlated_last_row_transport.md),
SHA256
\(\texttt{565922d4a5594c3d603882b98fe477c676377ca6dd334cfb99130de229b02872}\).
That separate theorem retains its own finite-source and allocation
hypotheses. No finite-source or action comparison is evaluated in
this protocol.

For each comparison on each disk, an entirely positive boundary
inventory proves strict positivity on the full disk by the harmonic
minimum principle. An entirely negative inventory proves strict
negativity by the maximum principle. Mixed signs, an inconclusive
comparison, or a failed/blocked/unprocessed comparison gives no
whole-disk sign classification for that test. Regardless of sign,
a fully completed boundary inventory gives a whole-disk interval
enclosure by taking its exact outward lower minimum and upper
maximum. These aggregate bounds are withheld if any comparison in
that disk is not completed or provenance is invalidated.

## 2. Frozen saved source and inventory

Use only
[radius attempt01](../repro/results/research-mixed-cap-343-radius-coverage-attempt01.json),
SHA256
\[
\texttt{1edec732c28ac64dd11ca63026722e8062a0598aa49b15ea2f2887a7dcbdb3d5},
\]
and its authorized
[manifest](../repro/protocols/research-mixed-cap-343-radius-coverage.json),
SHA256
\[
\texttt{45091a7e3284acbcf4d8adf03267ef505f378d8a019f3a867aba7ca77255fb25}.
\]
The old protocol and checker hashes are respectively
\(\texttt{971fb50a335c9ad3588ef431e09ee0ccd204e6ef95c4b14b23695b96dbe070ae}\)
and
\(\texttt{ce4942685353371270917272a5d069e230df2597df5207ae5d52c11117c27084}\).
Their complete source/provenance records remain binding.

The fixed inventory is \(P_3\), then \(P_4\), with indices
\(k=0,\ldots,511\) on each circle:
\[
\begin{gathered}
P_3:\ c_3=7/20-i/100,\quad \rho_3=83/1000,\\
P_4:\ c_4=3/10-13i/250,\quad \rho_4=3/50,\\
I_k=[2\pi k/512,2\pi(k+1)/512],\qquad
\theta_k=(2k+1)\pi/512,\quad \omega=\pi/512.
\end{gathered}
\tag{4}
\]
All closed endpoints, including the periodic seam, remain.
Each cell has exactly two comparison identifiers, \(f_1,f_2\),
in that order: 1,024 cells and 2,048 comparisons.

At each cell reuse its exact saved rational center \(v_k\) and
exact saved rational preconditioner \(A_k\), unchanged. The old
midpoint radius is \(r_0=2^{-30}\), and the whole-cell radius
is \(r_1=1/256\). The saved record already proves both strict
complex-disk inclusions and all original branch, chamber,
typed-disk and nonvanishing guards at those radii. It identifies
the same original holomorphic root for every parameter in the
cell. A metadata audit must verify every old cell's completed
status, all 64 stored passed checks, both seven-row inclusion
inventories, the 24-step independent proposal history, and the
original ordered labels. It does not recalculate old residuals,
inclusions, signs, or saved interval extrema.

The saved radius result must remain completed and provenance
verified, with all 1,024 positive-shallow verdicts, no failures
or unprocessed cells, and identical initial/final binding maps.
Both old review approvals, root execution authorization, settings,
and final manifest hash are checked. A missing or changed saved
input invalidates the new attempt before mathematical evaluation.

## 3. New response enclosure on the already certified boxes

Use 256-bit ball arithmetic. Reconstruct the exact circular cells,
the saved rational centers and matrices, and the Cartesian squares
containing their certified complex disks. Recheck the original
primitive-strip, chamber and typed-disk guards on the reconstructed
uniform boxes. The root inclusion itself is inherited from the
frozen certificate, not repeated.

Use the literal seven-variable Jacobian in equations (5)--(7) of
the old protocol. No old checker module is imported. For the
uniform root box and external cell, enclose
\[
 H=f_v(v_*(b);b),\qquad E=I-A_kH,\qquad
 k_i=\sum_j|E_{ij}|,\qquad k=\max_i k_i<1.
\tag{5}
\]
All scalar bounds and maxima use outward upper endpoints. Put
\[
 M_A=\max_j|(A_k)_{j6}|,\quad
 \gamma=\frac{2\pi i}{1-e^{-2\pi i(z+b)}},\quad
 k_{34}=\sum_j|E_{3j}-E_{4j}|.
\tag{6}
\]
Check the displayed denominator is nonzero on the whole box.
The row difference in (6) is formed before taking moduli; it
retains the same Jacobian and matrix correlations.

Since \(Hv'=-\gamma e_6\),
\[
 v'=-\gamma A_ke_6+Ev',\qquad
 \|v'\|_\infty\le \frac{|\gamma|M_A}{1-k}.
\tag{7}
\]
Therefore
\[
\begin{split}
 -y'&=\gamma(A_k)_{46}+\epsilon_1,
 &|\epsilon_1|&\le \frac{|\gamma|k_4M_A}{1-k}=:\epsilon_1^+,\\
 p'-y'&=-\gamma\{(A_k)_{36}-(A_k)_{46}\}+\epsilon_2,
 &|\epsilon_2|&\le \frac{|\gamma|k_{34}M_A}{1-k}=:\epsilon_2^+.
\end{split}
\tag{8}
\]
This is a Neumann estimate, with no inverse of a wide interval
Jacobian. No point inverse is computed either.

On the circle \(b_\theta=i(b-c_\nu)\), with exact modulus
\(\rho_\nu\). Taking the imaginary parts of the centers in
(8), multiplied by \(b_\theta\), and adding respectively
\([-\rho_\nu\epsilon_j^+,\rho_\nu\epsilon_j^+]\), gives interval
bounds for \(df_j/d\theta\). The sign in the first line of (8)
is positive; the second uses row 3 minus row 4.

At the midpoint use only the already certified radius-\(r_0\)
root box and the two constants in (2). In particular the
difference \(\Im p-\Im y\) retains both coordinate radii.
If \(L_j\) bounds the absolute angular derivative on the whole
cell, then
\[
             f_j(b)\in f_{j,\mathrm{mid}}
                             +[-\omega L_j,\omega L_j].
\tag{9}
\]
Also record the direct radius-\(r_1\) enclosure of (2) as an
audit bound. The asserted cell sign comes only from (9);
neither the direct enclosure nor an intersection supplies an
adaptive alternative. Positive means its lower endpoint is
strictly positive, negative means its upper endpoint is
strictly negative, and otherwise the verdict is inconclusive.

No new root, gradient, residual, Newton proposal, matrix inverse,
action, dilogarithm, or finite-source rate is evaluated. The new
mathematical work is exactly the reconstructed uniform Jacobian,
the two fixed logarithmic constants, the two response bounds,
and the two transported harmonic comparisons.

## 4. Failures, provenance and the one output

Checker:
[check_mixed_cap_343_saved_height_comparisons.py](../experiments/check_mixed_cap_343_saved_height_comparisons.py).
Manifest:
repro/protocols/research-mixed-cap-343-saved-height-comparisons.json.
Exclusive output:
repro/results/research-mixed-cap-343-saved-height-comparisons-attempt01.json.

The new manifest binds this protocol and checker, the exact old
result and authorized manifest, every inherited old file binding,
the original branch/action/domain sources used here, and their
JSON dependency edges transitively. It records all fixed settings
and separate root and peer static approvals. The mutable progress
record is not a permitted binding. Manifest preparation reads
hashes and provenance metadata only, without importing either
checker or evaluating saved mathematical values.

The checker validates the frozen old inventory and provenance
before setting arithmetic precision or constructing either new
threshold. It retains the claimed binding map even on a
provenance failure. Initial and final hashes of all dependencies
and the new manifest must agree.

All prescribed cells are attempted. A shared reconstruction or
response failure leaves both comparison records explicitly
blocked, with the exact failing check and traceback. A failure
in one comparison does not skip the other. Every inconclusive
comparison is completed and retained. Cell and comparison
failure, blocked and unprocessed identifiers remain explicit.
There are no retries or altered settings.

The output includes the unchanged rational source centers and
preconditioners, both reconstructed boxes, complete guard and
response records, each comparison's midpoint/direct/transported
intervals and sign, exact outward endpoints, both per-disk
comparison summaries, full operation counts, and all failures.
The output is opened exclusively. Zero counts explicitly cover
Newton/proposal/root solves, gradients, new root-inclusion tests,
matrix inversions, actions, dilogarithms, subdivisions and retries.
Reading the old certified inclusions is a provenance operation;
it is not an additional root solve.

Only a valid, complete, single-sign boundary inventory licenses
the corresponding whole-disk sign classification. No conclusion
survives changed provenance. An inconclusive outcome does not
authorize a second execution.

For manifest preparation, copy the literal values returned by the
written \(\texttt{settings}\) function without importing or executing
the checker. Include its \(\texttt{REQUIRED}\) files and every
\(\texttt{PINNED}\) binding, all old manifest bindings unchanged,
then close the listed JSON dependency fields starting from the old
result and old manifest. Record each edge with its record, field,
dependency path and digest; duplicate edges from distinct fields
remain distinct. Hash only those file bytes. The manifest initially
has execution authorization false; record the exact final protocol
and checker hashes in the root and independent review entries.
Root inspection and explicit authorization are the final separate
steps before the sole attempt.
