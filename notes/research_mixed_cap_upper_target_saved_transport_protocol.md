# Fixed saved-data test for the four charged cap-current transports

Protocol, 7 November 2026. This protocol performs no analytic,
root, target, primitive or gain evaluation. It reads the completed
first-cap source cover and its immutable 320-bit replay, and adds
only the prescribed rational transport costs from the
[current-transport theorem](research_mixed_cap_upper_target_current_transport.md).
All outcomes, including positive upper bounds, are retained.

## 1. Frozen inputs and coverage

The source author is
repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json,
SHA256
1e7ecb710244d417de75d794688e8786153fa82355b3d73b6811621130e1c54c.
Its completed replay is
repro/results/research-mixed-first-cap-coupled-plateau-replay.json,
SHA256
d1cc89d4ff8c249f2b4bc4b72e79842ca6151450518d99f00f28498d3edd912e.
The replay supplies one conservative maximum for each of the 21,032
original jobs, four families for each of 5,258 original endpoint cells.
The new standalone script is
[check_mixed_cap_upper_target_saved_transport.py](../experiments/check_mixed_cap_upper_target_saved_transport.py).
Its literal pins also include the new theory, original proof/driver
and completed cap theorem. Every inherited input mapping is verified
before and after processing.

The checker reconstructs the original four endpoint-reference trees,
then every descendant source-job tree, using the recorded binary
split axes and right-first stack order. It verifies full partitions,
original job/family/type ordering, all saved rational target trials,
the five immutable source tiers and replay counts. It retains every
strict geometric exclusion under the already completed original
replay, including both required length cases at coupled exclusions.
No new parameter is excluded. An all-excluded job has no maximum;
it is not converted into a source sign.

## 2. The fixed arithmetic and display convention

The original replay serializes its Arb maximum as a decimal ball.
For a displayed \([m\mathbin{+/-}r]\), the checker uses the
exact rational upper \(m+r\); an exact displayed decimal is
read as an exact rational. This is an outward display enclosure,
not an assertion that its midpoint is an original exact endpoint.
Unrecognized, nonfinite or negative-radius strings cause an error.

For every nonempty source job, decode this upper as \(u\).
Add exactly the following costs:
\[
 \begin{array}{c|cccc}
 \alpha&\text{left cut}&\text{right cut}&\text{lower alias}
                                      &\text{upper alias}\\ \hline
 0&1/25&0&1/25&1/20\\
 1&0&0&0&11/875 .
 \end{array}
 \tag{1}
\]
The last entry is the fixed outward replacement
\(\pi/250<11/875\), from \(\pi<22/7\).
No cost or family is chosen after looking at an outcome.
The four zero-cost families are also reported; their direct
analytic monotonicity and old strict margin were already proved.

For each job retain \(u\), its original displayed string,
the cost, the exact sum, and its strict-negative Boolean.
Take exact maxima by own type and family, retaining both
external input types and every original reference cell. Each
family succeeds only if all its nonempty jobs have negative
sums and coverage is complete. A positive or zero upper is
inconclusive; it is not evidence that the actual defect is positive.
No fallback, source replay, refinement or changed threshold is allowed.

## 3. Output and mathematical scope

One fresh output is planned at
repro/results/research-mixed-cap-upper-target-current-transport.json.
It records all 21,032 jobs, their complete coverage counts,
all eight family maxima, all charged failures, all input bindings,
and explicit zero analytic/root/optimizer/new-gain/refinement counts.
On an unexpected exception it preserves the completed job prefix,
the error and the unprocessed job inventory; such an output cannot
establish a family theorem.

If all fixed sums are negative, the theorem extends all eight
original calibrated cut/alias inequalities from the plateau
to outgoing real targets in \([.45,.5]\), at their original
outgoing heights and on the same actual-reference families.
If \(U_f<0\) are the eight family upper maxima, the conservative
uniform margin is \(\min_f(-U_f)=-\max_f U_f\); no stronger
margin is selected by a second run.
Any successful subfamily retains its separately stated scope.

This test does not evaluate the main cap or its true index-end
ceiling, change a retained Fourier branch, prove a height-taper
comparison, or establish a whole boundary-source sign. The
literal source and its original marginals remain those of the
bound proofs. The script must receive full root and independent
peer review before its single execution.
