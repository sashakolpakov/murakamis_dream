# Fixed residual and action evaluation for the prepared three-four cap

Unexecuted protocol, 7 November 2026. The original critical point
already exists by the completed Fourier boundary update. This protocol
makes one deterministic proposal for its five coordinates, checks one
original-gradient residual, and encloses the original action using
[the quadratic action-error theorem](research_mixed_prepared_cap_action_enclosure.md).
It performs no existence search, input change, root refinement, parameter
cover, physical-face comparison or alias comparison. No evaluation is
authorized until this protocol and its evaluator have been frozen and
fully reviewed.

## 1. Unchanged inputs and one prescribed proposal

Use the original interface record
[research-three-four-source-interface.json](../repro/results/research-three-four-source-interface.json),
its writer, its complete dependency manifest, and the successful
[boundary-update record](../repro/results/research-mixed-fourier-boundary-update.json).
The latter must have successful status, all 512 prescribed arcs
certified, and unchanged before/after input bindings. Its root-source
association must be the same original interface record.
Retain the complete certified root square, with its original radius
\(10^{-26}\), and the exact expression
\[
                    K=(1+2a-4a^2)^{-1}.
 \tag{1}
\]
The square is never replaced by its center in a rigorous evaluation.

Order coordinates as \(x=(u,s,t,p,q)\). The exact initial
Gaussian-rational proposal is
\[
 x^{(0)}=(.230+.063i,\ .407+.009i,\ .3345-.0255i,
                              \ .30-.052i,\ .30-.052i).
 \tag{2}
\]
These are fixed centers of inherited image bounds; they carry no
numerical certification claim. The containing convex domain is
\[
\begin{split}
 U&=[.21,.25]+i[.01,.10],\qquad
 E=[.33,.47]+i[-.09,.08],\\
 Q&=[.23,.45]+i[-.12,.12],\qquad
                     \mathcal D=U\times E\times Q^3.
\end{split}
 \tag{3}
\]

Use mpmath with exactly 80 decimal digits. Record its version, the
Python version and platform. The proposal uses the center of the
original algebraic square to form an untrusted \(K_0\), and
caches its principal \(\Log K_0\). Perform exactly 32 complex
Newton steps. At each step solve
\[
               H(x^{(n)};K_0)d=f(x^{(n)};K_0),
 \qquad x^{(n+1)}=x^{(n)}-\alpha_n d,
 \tag{4}
\]
with \(\alpha_n=1/2\) for \(0\le n<8\) and
\(\alpha_n=1\) for \(8\le n<32\). Use Gaussian
elimination with deterministic partial pivoting by the squared
complex modulus, with the first row winning a tie. No analytic
square root is needed for this comparison.

After each step clamp each real and imaginary coordinate separately
to its own interval in (3), inset by exactly \(10^{-8}\) at
both ends. No line search, stopping tolerance or adaptive damping
is used. Record every pre-step point, gradient, Hessian, solve,
unclamped point and clamped point. A nonfinite value, zero pivot
or other proposal error is retained and ends this single attempt;
it supplies no replacement seed or second method.

After step 32, round each real and imaginary coordinate to the
nearest multiple of \(10^{-50}\), using ties to even. The
stored finite mpmath binary value is first converted to its exact
fraction; scaling and ties-to-even rounding then use only integer
arithmetic, with no second floating rounding. The result \(x^0\)
is an exact Gaussian-rational point. The
clamping and quantization are part of the proposal only. Their
output is accepted only through the independent domain and residual
tests below.

## 2. The exact gradient, Hessian and proposal inventory

Let \(g'(z)=\Log(1-e^{-2\pi iz})\) and
\(g''(z)=2\pi i e^{-2\pi iz}/(1-e^{-2\pi iz})\),
on the original strip. Evaluate the nine arguments in this order:
\[
          1/2-u,\ u,\ s-u,\ s+t,\ t+p,\ p+q,\ t,\ p,\ q.
 \tag{5}
\]
Write \(Q_q=e^{-2\pi iq}\), reusing the last exponential.
The full original gradient is
\[
\begin{split}
 f_u={}&2g'(1/2-u)-3g'(u)+g'(s-u)+\pi i(1-6u+2s),\\
 f_s={}&g'(s+t)-g'(s-u)+2\pi iu,\\
 f_t={}&g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 f_p={}&g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 f_q={}&g'(p+q)-g'(q)-\Log(1-KQ_q)+\Log K.
\end{split}
 \tag{6}
\]
The first row equals the original cosine/sine row. Indeed
\(J'=g'-i\pi/2+i\pi z\); substituting this in
\(2J'(1/2-u)-3J'(u)+J'(s-u)+i\pi s\) gives exactly
the first line of (6), including its constant. Thus these are
the original unscaled derivatives even at a nonstationary trial.

For proposals, use the symmetric tridiagonal Hessian with
\[
\begin{split}
 H_{uu}&=-2g''(1/2-u)-3g''(u)-g''(s-u)-6\pi i,\\
 H_{us}&=g''(s-u)+2\pi i,\qquad
 H_{ss}=g''(s+t)-g''(s-u),\qquad H_{st}=g''(s+t),\\
 H_{tt}&=g''(s+t)+g''(t+p)-2g''(t),\qquad
 H_{tp}=g''(t+p)+2\pi i,\\
 H_{pp}&=g''(t+p)+g''(p+q)-3g''(p),\qquad H_{pq}=g''(p+q),\\
 H_{qq}&=g''(p+q)-g''(q)-2\pi iKQ_q/(1-KQ_q).
\end{split}
 \tag{7}
\]
This is the unreduced five-variable Hessian; no endpoint Schur
complement or re-solved endpoint root is inserted.

Each step uses nine complex exponentials and ten principal logarithms
(the nine primitive logarithms and the outgoing incidence logarithm).
The proposal ceiling is therefore 288 exponentials and 321 logarithms,
including the one cached \(\Log K_0\). No proposal dilogarithm,
trigonometric function, optimizer or phase-value search is needed.
Attempted and completed counts are saved even on failure.

## 3. One rigorous residual and action enclosure

Use Arb/Acb at exactly 256 bits. Set once and for all
\[
             r=10^{-16},\qquad \mu_- =471/1225,
             \varepsilon_F=60r^2.
 \tag{8}
\]
Check with exact fractions that every coordinate square of radius
\(r\) about \(x^0\) lies strictly inside its rectangle
in (3). This extra guard is stronger than the action theorem's
center-membership requirement and uses no new root assertion.

Construct all rational points and the whole original algebraic square
outward, saving exact input endpoints and verifying enclosure containment.
Form (1) outward and retain its whole complex enclosure. Enclose
\(\pi\), \(\Log K\) and \(\operatorname{Li}_2(K)\) once.
Check the inherited branch and nonzero denominator before each use.

At the exact rational point \(x^0\), construct all arguments
in (5), require \(0<\Re z<1\) on their containing rectangles,
and evaluate their exponentials once. Require these exponential
rectangles to avoid the principal dilogarithm cut \([1,\infty)\),
and the corresponding \(1-e^{-2\pi iz}\) rectangles to avoid
the principal logarithm cut and zero. The sufficient rectangular
guards are a strictly positive or negative imaginary interval, or
a real interval wholly on the permitted side of the relevant cut.
No clipping or branch replacement is allowed.

Likewise require the full \(KQ_q\) rectangle to be strictly in
the lower half-plane and \(\Log K\) to be on the original
branch. Neither a modulus-less-than-one assumption for \(KQ_q\)
nor a finite-product interpolation on the larger proposal domain
is used: its principal dilogarithm is regular off the cut there.
Every branch guard and its failed operands, if any, are retained.

Evaluate all nine primitive logarithms, the outgoing logarithm,
and the gradient (6) outward. If the ten real and imaginary
component intervals are \([l_j,u_j]\), save and compare
exactly
\[
 R^2=\sum_{j=1}^{10}\max(|l_j|,|u_j|)^2
                       <\mu_-^2r^2.
 \tag{9}
\]
The established existence and coercivity theorem then localize
the actual original root within Euclidean distance \(r\).
No inverse test or new existence certificate is substituted.

On the same point and input enclosure evaluate
\[
\begin{split}
 \widehat F={}&-2g(1/2-u)-3g(u)-g(s-u)
   +g(s+t)+g(t+p)+g(p+q)\\
 &-2g(t)-3g(p)-g(q)
     +\pi i(1/4+u+2su-3u^2+2tp)\\
 &+(q-1/2)\Log K-
       \frac{\operatorname{Li}_2(KQ_q)-\operatorname{Li}_2(K)}{2\pi i},\\
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
\end{split}
 \tag{10}
\]
Use the cached nine exponentials. Preserve all constants, including
\(i\pi/4\) and every \(-\pi^2/6\). If (9) is inconclusive
but the analytic domain guards pass, still retain this prescribed
value evaluation; it is not certified as a root action.

If the value interval is \([A_-,A_+]+i[B_-,B_+]\), the
certified action interval, only when (9) passes, is
\[
 [A_--\varepsilon_F,A_++\varepsilon_F]
             +i[B_--\varepsilon_F,B_++\varepsilon_F],
 \qquad M_-:=A_--\varepsilon_F.
 \tag{11}
\]
This is exact rational arithmetic on saved endpoints. The full
algebraic input uncertainty and all interval rounding remain
inside the value interval; no midpoint is used for (11).

The complete rigorous analytic ceiling is one \(\pi\), nine
exponentials, eleven logarithms and eleven dilogarithms: 32 calls.
The logarithms include cached \(\Log K\), nine primitive
logs and the outgoing log; the dilogarithms include cached
\(\operatorname{Li}_2(K)\), the nine primitive values and
the outgoing value. No cotangent, sine, square root or interval
Hessian calculation is needed. Save attempted/completed counts.

## 4. Records, provenance and failure scope

The evaluator is
[evaluate_mixed_prepared_cap_action.py](../experiments/evaluate_mixed_prepared_cap_action.py).
Its only prescribed output is
[research-mixed-prepared-cap-action.json](../repro/results/research-mixed-prepared-cap-action.json),
opened exclusively before source parsing or any proposal/analytic call.
Bind the original root source/writer/dependencies, the completed
boundary-update record/writer/protocol and every inherited binding,
the existence and action proofs, all original source/calibration/domain
inputs, this protocol, and the evaluator itself. Every pin must be
literal and current before numerical libraries are imported.
Rehash every input after the attempt; any change invalidates the result.

The consumer interface contains:

- `status`, equal to `passed` only when every prescribed domain,
  residual, value, inventory and provenance check succeeds;
- `script_sha256`, `input_sha256`, `input_sha256_after`,
  `all_inputs_unchanged`, and the complete original root association;
- the exact rational proposal, coordinate squares, all analytic
  operands, branch guards, residual components and (9);
- `certified_radius_rational`,
  `action_error_radius_rational`, and
  `original_action_at_proposal`, whose `real` and `imag` fields
  are pairs of exact rational endpoint strings;
- `action_enclosure`, with the same endpoint-pair format and
  exactly the enlargement (11), and `M_lower_rational` equal
  to its real lower endpoint, present only for a certified action.

The record also retains all proposal histories, arithmetic/interval
conversions, primitive values, every stage-specific failure and
attempted/completed inventories. A failed guard stops dependent
calculations; partial witnesses remain visible. A failed residual
is inconclusive and does not trigger a second proposal. A provenance
or arithmetic error makes the attempt failed. There are no retries,
precision changes, alternate input parameters or root-radius refinements.

A successful record supplies only the original prepared action
enclosure and a coordinate enclosure of its already existing root.
The separate physical-face and alias protocol must still compare
its bounds with \(M_-\). No new whole-source sign, full-period
estimate, propagation theorem or knot conclusion is part of this run.
