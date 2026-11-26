# Fixed whole-disk test for the Fourier boundary update

Unexecuted protocol, 7 November 2026. This tests only inequality (12)
of [the boundary-update theorem](research_mixed_fourier_boundary_update.md).
There is no reference-root solve, new canonical family, trial
optimization, parameter refinement or fallback. The theorem already
proves whole-disk regularity and the original zero logarithmic lift.
No sign for the remaining disk inclusion is asserted before the test.

## 1. Immutable input and exact domain

Use the original successful
[interface record](../repro/results/research-three-four-source-interface.json)
and its [writer](../experiments/check_three_four_source_interface.py).
Its rational center and radius enclose the selected root \(a\) of
\(4a^4-6a^3+4a^2-2a+1\). Use the full Cartesian square containing
that certified disk, without replacing its radius by zero. The
original algebraic output shape is
\[
                    K=\frac1{1+2a-4a^2}.
 \tag{1}
\]
This is the same exact formula used in the completed paired-kernel
certificate. Its enclosure is propagated through every operation.
No new polynomial-root proposal or root certification is performed.

The only varying input is the original type-four disk boundary
\[
 q(t)=q_c+R_4e^{2\pi it},\qquad
 q_c=\frac3{10}-\frac{13}{250}i,\quad
 R_4=\frac8{125},\quad 0\le t\le1.
 \tag{2}
\]
Use exactly the 512 closed intervals
\[
                I_j=[j/512,(j+1)/512],\qquad0\le j<512.
 \tag{3}
\]
Their overlaps at endpoints are retained. They cover the complete
circle and introduce no interior parameter cover or target clipping.
The interval \(t\) is inserted into the exponential before any
Cartesian enclosure is formed.

Every direct proof, script and record input is SHA256-bound before
evaluation. The root record's successful status, writer association,
root-certificate schema and inherited dependencies are checked.
The analytic boundary theorem, this protocol, original interface,
calibration, typed-map and Hessian proofs are also bound. All input
hashes and the evaluator's own hash are checked again at completion.
Any provenance failure prevents a successful result.

## 2. The fixed analytic enclosure

Use Arb/Acb arithmetic at exactly 256 bits. Construct each rational
real interval outward; save and explicitly verify containment of its
specified rational endpoints. Do not silently use rounded point inputs.
Compute \(\pi\) once. Compute the single enclosure of \(K\) in
(1), retaining its full root square, and guard its denominator.

On each whole interval (3), perform exactly these operations:
\[
\begin{split}
 \omega_j&=\exp(2\pi iI_j),&
 q_j&=q_c+R_4\omega_j,&
 Q_j&=\exp(-2\pi iq_j),\\
 n_j&=1-KQ_j,&
 d_j&=K+(1-2K)Q_j,&
 B_j&=n_j/d_j,\\
 b_j&=-\operatorname{Log}(B_j)/(2\pi i).
\end{split}
 \tag{4}
\]
The first exponential encloses the complete circular arc; \(q_j\)
and all subsequent quantities are containing complex rectangles.
They are never intersected with the original disk or a favorable
image region. The theorem's analytic branch argument concerns the
actual circle; the numerical guards below ensure that its principal
branch is also valid on the containing rectangles used by Acb.

Require finite enclosures, nonzero \(n_j,d_j,B_j\), and a strictly
negative upper bound for \(\Im B_j\) before evaluating the logarithm.
Then verify \(-\pi<\Im\operatorname{Log}B_j<0\) and
\(0<\Re b_j<1/2\). Record every guard, including any failure.
For the claimed inclusion, form
\[
 d_{R,j}=\Re b_j-\frac7{20},\qquad
 d_{I,j}=\Im b_j+\frac1{100},\qquad
 U_j=\operatorname{upper}(d_{R,j}^2+d_{I,j}^2).
 \tag{5}
\]
Acceptance requires the exact rational comparison
\[
                         U_j<\frac{81}{10000}.
 \tag{6}
\]
The saved real-interval squares are outward enclosures. Their upper
endpoints and sum are also recomputed with rational endpoint arithmetic;
both bounds must satisfy (6). No square root or distance proposal is
needed.

The fixed maximum inventory is one \(\pi\) evaluation, 512 circular
complex exponentials, 512 shape exponentials, and 512 principal complex
logarithms. A guard failure may prevent a later operation on that arc;
attempted and completed counts are stored separately. All 512 original
arcs are visited once even if another arc fails. There are zero
reference-root calls, proposals, optimizers, gain evaluations,
subdivisions, precision changes, alternative branch trials or retries.

## 3. Record and failure semantics

The new evaluator is
[check_mixed_fourier_boundary_update.py](../experiments/check_mixed_fourier_boundary_update.py).
Its sole prescribed output is
[research-mixed-fourier-boundary-update.json](../repro/results/research-mixed-fourier-boundary-update.json).
The file must be absent before execution and written exclusively.
The record stores the full input bindings, root square, \(K\),
all 512 exact parameter intervals, all complex enclosures in (4),
branch and finiteness guards, coordinate differences, both squared
distance witnesses, and the exact rational margin in (6). It also
stores every exception with its arc index and stage.

Success requires the original full inventory, all guards and all
512 strict comparisons, together with unchanged final bindings.
Save the largest rational upper distance and its witnessing arc.
Any failed comparison is an inconclusive inclusion test; it is not
evidence that the actual image leaves \(D_3\). Do not discard it or
change the 512 arcs. An arithmetic or provenance error invalidates
the whole result. Save the partial record and all failure metadata.
There is no fallback or second execution in this protocol.

If the test succeeds, the maximum principle proves
\(\beta_K(D_4)\subset\operatorname{int}D_3\), and the strict
common margin persists for \(y\) in a neighborhood of \(x_0\).
The boundary-update theorem then gives the original critical
point for every ordinary-cap prefix ending in four. This test
supplies no narrower prepared-root coordinates, source-tail or
alias comparison, cap asymptotic, or whole-message entrance.
