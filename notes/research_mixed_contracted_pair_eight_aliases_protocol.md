# Eight fixed horizontal Fourier comparisons for the contracted pair

Research calculation protocol, 7 November 2026. This calculation
concerns the original three-four kernel with both outside parameters
equal to its alternating reference. The real domain is
\[
 C'=[1/4,1/2]\times[1/5,9/20]\times[1/5,21/50]^2
\]
in coordinates \((s,t,p,q)\). The enlargement is justified by
the separate analytic concavity and physical-tail reductions. The
failed physical calculation on the earlier smaller domain is
retained; this calculation does not revisit any of its nine points.

## 1. The eight quantities and their mathematical role

Use the original imaginary intervals
\[
 [-3/100,3/200]\quad(s,t),\qquad
 [-11/200,3/200]\quad(p,q).
\]
For each coordinate \(j\), and each of its two endpoint heights
\(h_{j,-},h_{j,+}\), define
\[
 B_{j,\pm}=\max_{u\in C'}
  \left\{\Re\mathcal F(u+ih_{j,\pm}e_j)-2\pi|h_{j,\pm}|\right\}.
 \tag{1}
\]
Only coordinate \(j\) has a nonzero imaginary part in (1).
The fixed comparison target for all eight quantities is
\[
                  B_{j,\pm}<3781/2500-1/100000.
 \tag{2}
\]
The right side is strictly below the original geometric action
\(M>3781/2500\). It is not fitted to this calculation's output.

Whole-rectangle accretivity proves strict concavity in the four
real coordinates. The original logarithmic-gradient bounds prove
that \(\Re\mathcal F(u+iv)-2\pi\sum|v_j|\) decreases as any
absolute height increases. Consequently these eight comparisons
control every purely horizontal nonzero lattice correction. Terms
on vertical sides and the zero-frequency joining integrals use
the separately established physical-face gap. Original Fourier
denominators are bounded factors; they are retained in the exact
source formula. This calculation alone does not prove that
physical-face gap or a knot-volume theorem.

At any rational real supporting point \(y\in C'\), put
\(z=y+ih_{j,\pm}e_j\). The rigorous upper bound used is
\[
 \Re\mathcal F(z)-2\pi|h_{j,\pm}|
 +\sum_{k=1}^4\max\{
   \Re\mathcal F_k(z)(L_k-y_k),
   \Re\mathcal F_k(z)(U_k-y_k)\}.
 \tag{3}
\]
There is no assertion that \(y\) is an exact stationary point.
Every derivative term in (3), with its sign, is retained.

## 2. The original primitive and phase

Use the entire saved square enclosing the original quartic root
\(a\), and \(K=(1+2a-4a^2)^{-1}\). Its first-quadrant unit-disk
branch is fixed by the existing reference proof. The original
analytic primitive on \(0<\Re z<1\) can be written
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{4}
\]
Indeed its derivative is the original
\(\operatorname{Log}(1-e^{-2\pi iz})\), and its limit at zero
along the positive real axis is zero. This fixes its additive
constant. All evaluations remain in the regular strip and use
this original lift, including where a summed logarithm has
negative real part inside its argument.

Set
\[
 I(z)=\frac{\operatorname{Li}_2(Ke^{-2\pi iz})-
                         \operatorname{Li}_2(K)}{2\pi i}.
\]
The complete phase, with its cardinal contribution unchanged, is
\[
\begin{split}
 \mathcal F={}&g(s+t)+g(t+p)+g(p+q)-2g(t)-3g(p)-g(q)\\
 &+2\pi itp+(s+q-1)\operatorname{Log}K-I(s)-I(q).
\end{split}
 \tag{5}
\]
Thus this is the same phase as the exact contracted source, not a
newly normalized vertex sum. Differentiation gives
\[
\begin{split}
 \mathcal F_s&=g'(s+t)+\operatorname{Log}K-\operatorname{Log}(1-Ke^{-2\pi is}),\\
 \mathcal F_t&=g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 \mathcal F_p&=g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 \mathcal F_q&=g'(p+q)-g'(q)+\operatorname{Log}K-\operatorname{Log}(1-Ke^{-2\pi iq}).
\end{split}
 \tag{6}
\]
For the proposal Hessian, use
\[
 g''(z)=\frac{2\pi i e^{-2\pi iz}}{1-e^{-2\pi iz}},
 \qquad -I''(z)=\frac{-2\pi iKe^{-2\pi iz}}{1-Ke^{-2\pi iz}}.
\]
Take the real part of the full four-by-four Hessian of (5).
The middle chirp contributes a purely imaginary mixed derivative
\(2\pi i\), whose real part vanishes; it is still present in
the phase and gradients.

## 3. Fixed proposals and outward verification

Process coordinates in the order \(s,t,p,q\), negative then
positive height for each. For every one of these eight cases,
start the four real coordinates at the midpoints of \(C'\).
Convert the saved rational root center to floating point and use
its rational formula for \(K\) only to propose a support point.
Perform exactly 32 Newton steps with the real analytic Hessian:
eight steps with damping \(1/2\), then 24 steps with damping one.
Use deterministic partial-pivot Gaussian elimination. After each
step, clamp every coordinate to \([L_k+10^{-8},U_k-10^{-8}]\).
No phase-value line search, adaptive precision, random input,
early termination or alternative initialization is permitted.

Round the final four real coordinates to the nearest multiples of
\(10^{-12}\), and verify their membership in \(C'\) with exact
rational arithmetic. The fixed height is retained as an exact
rational number. Newton convergence is not a proof requirement;
the supporting-plane inequality holds at any resulting interior
point. A proposal failure is recorded, without changing the method.

At each chosen rational point, evaluate (5)--(6) with Arb/Acb at
exactly 256 bits, retaining the full saved root square. The real
part of (5), the Fourier debit, and all four affine support terms
are enclosed outward. For each support term, use the larger of
the two outward product upper endpoints. Compare the final upper
endpoint with the exact rational target in (2). Record all eight
results, including failures; success requires every comparison.

## 4. Provenance, execution and scope

The checker is
`experiments/check_mixed_contracted_pair_eight_aliases.py`; its
exclusive output is
`repro/results/research-mixed-contracted-pair-eight-aliases.json`.
It binds this protocol, the final enlarged-rectangle theorem,
the exact contour identity, the source and calibration notes, and
the root record
`repro/results/research-three-four-source-interface.json`
at SHA
`9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd`.
The saved root's generating script and every recorded dependency
are verified before any analytic evaluation. The existing
three-vertex and four-vertex action records and their writers and
dependencies are also bound, without replaying their calculations.

The root and a second agent read the complete proof, protocol and
code before execution. Their final hashes are recorded then and
checked again afterward. Only the root runs the checker, once,
with the fixed parameters above. The output is opened with exclusive
creation and records exact support coordinates, rigorous phase and
gradient intervals, the original Fourier debit, all eight upper
bounds, all input hashes, and any failures.

There is no retry or change of domain, target, precision, proposal
rule, or height after this calculation's output is inspected.
A failure starts a new written mathematical diagnosis. A success
establishes the eight particular global bounds in (1). Its use
in a whole-kernel theorem additionally requires the written
physical-tail bounds, the exact contour decomposition and the
original nonzero local coefficient. It does not supply a theorem
for arbitrary incoming quantum functions or arbitrary short knots.
