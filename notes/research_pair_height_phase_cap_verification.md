# Pair-height verification using the maximum cosine phase

Research note, 3 November 2026. The phase-restricted computation
described in Sections 1--3 is running. Section 4 distinguishes it
from the completed sector-scaled verification and the unfinished
affine comparisons.

The [maximum-principle theorem](research_geometric_phase_maximum_principle.md)
gives a smaller geometric domain for the pair-activation problem.
Its verification is separate from the earlier unrestricted-angle
and sector-domain computations. Those computations retain their
separate input files and records.

## 1. The necessary geometric domain

Use the two power-three vertices, common charge \(\chi\), and larger
height \(H\) of the
[pair-activation reduction](research_positive_path_pair_activation_gap.md).
Other powers are at least three, and the complete outside endpoint is
retained. At the vertex of height \(H\), let \(a\) be its real angle.
The already proved bounds give
\[
 0<H<23/20,\qquad
 a>\ell(H):=\arcsin(\sinh H/\sqrt3).
 \tag{1}
\]
If the scaled estimate \(H<59\chi/50\) fails, Theorem 5 of the
maximum-principle note gives \(\chi\le50H/59\) and \(a<2H\).
The small-height theorem has excluded this failure for \(H\le3/100\).
Thus it suffices to consider
\[
 H\in[3/100,23/20],\qquad
 a=(1-\xi)\ell(H)+2\xi H,\quad0\le\xi\le1.
 \tag{2}
\]

For a failure of the affine estimate
\(H<37/200+37\chi/40\), with \(\chi\ge4/5\), put
\[
 \chi_{\max}(H)=\min\{1,\ 40(H-37/200)/37\}.
 \tag{3}
\]
Then \(H\ge37/40\) and \(\chi\le\chi_{\max}(H)\).
The original return ratio satisfies
\(\sinh H/\sin a\ge\sinh H>1/\sqrt2\). The cosine-phase
bound therefore makes every return imaginary part negative.
Its period equation implies
\[
 a<2\pi\chi/3\le2\pi\chi_{\max}(H)/3.
 \tag{4}
\]
The sufficient affine domain is
\[
 H\in[37/40,23/20],\qquad
 a=(1-\xi)\ell(H)+\xi\,2\pi\chi_{\max}(H)/3,\quad0\le\xi\le1.
 \tag{5}
\]

Both parameterizations increase in \(H\) and \(\xi\). Their lower
endpoint \(\ell(H)\) increases. In (2), the upper endpoint does also,
and \(\ell(H)<2H\): use \(\arcsin x\le\pi x/2\),
\(\sinh H\le H\cosh H<7H/4\), \(\pi<22/7\), and
\(\sqrt3>5/3\) to obtain \(\ell(H)<33H/20\).
In (5), the increasing upper endpoint is at least
\(8\pi/15>\pi/2>\ell(H)\).
Thus diagonal corners of a rational parameter rectangle give a
rigorous interval enclosure of \(a\). All resulting angles lie
strictly between zero and \(\pi\).

## 2. The two support terms

Let \(A=\tan((a-iH)/2)\). The two original returns are
\(\operatorname{arsinh}(Ac_1)\) and \(\operatorname{arsinh}(Ac_2)\), with
\[
 c_1\in D_{23/20}^{\sharp},\qquad c_2\in D_H^{\sharp}.
 \tag{6}
\]
Here \(D_C^\sharp\) is the quarter ellipse of height cap \(C\)
intersected with \(0\le\Im c\le\Re c/\sqrt2\).
Complete neighbors and the zero return of an absent incidence are
included. Proposition 6 of the maximum-principle note proves that,
for a real support slope \(s\le0\), the support maximum is the larger
of zero and its maximum on the single arc
\[
 \begin{split}
 c_C(u)&=\cosh(C/2)\cos(u\vartheta_C)
             +i\sinh(C/2)\sin(u\vartheta_C),\quad0\le u\le1,\\
 \vartheta_C&=\arctan\!\left(\frac{\coth(C/2)}{\sqrt2}\right).
 \end{split}
 \tag{7}
\]
Both modes therefore require two arc bounds, one for each cap.
The old affine three-piece sector boundary is unnecessary on this
newly proved domain.

For each parameter rectangle the author proposes a rational
nonpositive slope \(s\) and two positive rational budgets \(b_1,b_2\).
It verifies the two inequalities
\[
 \Re\operatorname{arsinh}(Ac_C(u))
        -s\Im\operatorname{arsinh}(Ac_C(u))<b_i
                         \quad(0\le u\le1),
 \tag{8}
\]
and their strict separation from the required period:
\[
 b_1+b_2<
       \frac32H-s\left(\frac32a-\pi\chi_{\max}(H)\right).
 \tag{9}
\]
In scaled mode \(\chi_{\max}(H)=50H/59\). Positive budgets
also dominate the exact origin value zero.

The actual return sum is \(3H/2+i(3a/2-\pi\chi)\).
Because \(s\le0\) and \(\chi\le\chi_{\max}(H)\), its support
value is at least the right side of (9). Thus (8)--(9)
exclude the corresponding geometric failure.

Complete certificates on these domains would directly prove the
two geometric height estimates. They would not prove the earlier
support assertions on their larger unrestricted domains.
The integration and deletion arguments of the existing
pair-activation reduction need only the geometric height estimates.

## 3. Verification and independent replay

The new author is
[certify_pair_height_phase_cap.py](../experiments/certify_pair_height_phase_cap.py).
It processes affine mode first and scaled mode second, and imports
no previous author. Numerical optimization only proposes slopes
and budgets. Outward Arb arithmetic checks every accepted rectangle
and arc segment. It evaluates the original right-half-plane inverse
hyperbolic sine, with distance and small-argument formulas available
for tighter enclosures. An incomplete run writes an explicitly
incomplete checkpoint.

The separate
[replay_pair_height_phase_cap.py](../experiments/replay_pair_height_phase_cap.py)
imports no author or optimizer. It uses the earlier independent
replayer's arithmetic and partition routines, recomputes the new
angle and arc geometry, and evaluates the return through
logarithm/square-root and real distance formulas at 160 bits.
It checks parameter coverage with multiplicity one, every exact
arc partition, both support bounds, and every budget separation.
Only a complete successful replay writes a passed report.

The output names distinguish the new domains:

~~~text
repro/results/research-pair-height-phase-cap-affine.json
repro/results/research-pair-height-phase-cap-scaled.json
~~~

Independent reports have the corresponding -replay.json suffix.
Accepted boxes from an incomplete checkpoint, or sampled positive
margins, are not a proof of full coverage.

## 4. Status of the separate computations

The unrestricted scaled run exhausted its subdivision budget without
covering its domain. The unrestricted affine run also stopped at its
300,000-visit limit, after approximately 12,516 seconds, with the
message “Coverage unfinished; no certificate saved.” Both are terminal
incomplete computations. Neither failure exhibits a counterexample to
the mathematical support inequality, and neither run was restarted.

The separate sector-scaled author has completed its smaller domain:
77,088 accepted rectangles cover the sector coordinate from zero to
one and heights from \(3/100\) to \(23/20\). Its
[complete artifact](../repro/results/research-pair-height-sector-scaled.json)
has no pending rectangles. Its
[independent 160-bit replay](../repro/results/research-pair-height-sector-scaled-replay.json)
has passed every rectangle and 26,182,200 arc intervals, with exact
multiplicity-one coverage and no additional subdivisions. The
[scaled-height theorem and its energy consequences](research_scaled_pair_activation_consequences.md)
therefore no longer depend on a pending computation.
The original sector-affine process ended with exit status 143
(`SIGTERM`), after 65,305 accepted rectangles, 130,604 visits,
and approximately 8,992 seconds, with 18 rectangles still pending.
It reported neither a mathematical failure nor a subdivision-budget
assertion. Its complete saved checkpoint and all three frozen input
hashes were verified. The accepted and pending rectangles together
still cover the original domain with exact multiplicity one.
The [resume validation](../repro/results/research-pair-height-sector-affine-resume-validation.json)
records that check; it is not an analytic replay of a finished result.

The same author resumed from that checkpoint with unchanged
precision, segment limits, input files, and the original cumulative
300,000-visit budget. Its
[controller record](../repro/results/research-pair-height-sector-affine-resume-controller.json)
records that continuation. The resumed process subsequently also
ended with exit status 143 (`SIGTERM`), after 66,369 accepted
rectangles, 132,738 cumulative visits, and approximately 10,044
cumulative seconds, with 24 rectangles still pending. It reported
no mathematical failure or subdivision-budget assertion. The
one-shot watcher ended without launching a replay because no
complete affine artifact existed. The new checkpoint passed a
[second streaming partition validation](../repro/results/research-pair-height-sector-affine-resume-2-validation.json):
all frozen hashes agree, and its 66,369 accepted and 24 pending
rectangles cover the domain with exact multiplicity one. The
[validator](../experiments/validate_pair_height_sector_checkpoint.py)
checks that partition without claiming an analytic replay.
The same author continued from this checkpoint with unchanged
inputs, precision, segment limits, and cumulative visit budget.
This second continuation also ended with exit status 143
(`SIGTERM`), at 66,491 accepted rectangles, 132,980 cumulative
visits, and approximately 10,105 cumulative seconds, with 22
rectangles pending. Its watcher ended without launching a replay.
The incomplete checkpoint is preserved; no accepted work was
discarded, and the affine inequality remains unverified.

The maximum-phase author described in this note also ended with
exit status 143 (`SIGTERM`), during affine mode. Its checkpoint
contains 65,976 accepted rectangles, 131,953 visits, approximately
8,079 seconds, and 25 pending rectangles. Its scaled mode had not
begun. Its watcher ended without a complete artifact or replay.
Neither author printed a mathematical failure or subdivision-budget
assertion, and neither has been restarted after these terminations.
The frozen input hashes still agree with both checkpoint headers.

These computations use different proved geometric restrictions from
the unrestricted runs and preserve their separate records. Their
unfinished affine comparisons must not be inferred from completion
of the scaled comparison.
