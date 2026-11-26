# Original-gradient enclosures over an external-coordinate cell

Research specification, 6 November 2026. This defines the import-safe
[reference provider](../experiments/mixed_second_selected_external_reference.py)
for flags \((1,1,\beta)\), \(\beta=0,1\). It makes no numerical
call on import and supplies no scalar sign or parameter-cover result.

## 1. Interface and scope

`initialize()` checks the pinned inputs, including the 29 bindings of
the [canonical record](../repro/results/research-mixed-second-selected-canonical-reference.json),
and returns the bindings and its two fixed exact seed centers.
`evaluate(cbox, cmid, beta, seed_centers=None)` accepts an exact
rectangle and a prescribed exact expansion point inside it, normally
the image of a boundary chart's parameter midpoint. Only the prescribed canonical seed
for that beta is allowed. Precision is fixed at 256 bits for outward
arithmetic. The return contains a status, live coordinate and
negative-shape dictionaries, the seven reference derivatives, the
original Hessian and its inverse enclosure, JSON-safe details, and
operation counts. No file is written. The caller binds these inputs
before and after its separately authorized traversal.

The conclusion concerns every actual canonical reference with
\(c\in\texttt{cbox}\cap(K_3\cup K_4)\). It does not assert that
this intersection is nonempty or realized by a finite suffix.
The full enclosing rectangle may extend outside the typed disks;
it must lie in the common external rectangle
\(Q=[.23,.45]+i[-.12,.12]\). Existence is needed only at its
actual typed points, where the
[original reference theorem](research_mixed_second_selected_reference_curve.md)
already provides it.

## 2. Fixed proposal and original derivatives

Order \(q=(e,\xi,a,u,z,v,b)\). Reuse exactly the original seven
gradient equations from the pinned canonical helper and
[residual theorem](research_mixed_prefix_residual_localization.md).
Use the analytic symmetric Jacobian of these equations. Its only
external derivative is
\[
                  f_c=e_b\{\pi\cot\pi(b+c)+i\pi\}.
 \tag{1}
\]

Starting from the saved \(c=1/3\) seed, perform at most twenty
undamped Newton steps at 50 decimal digits at the prescribed midpoint.
The stopping tolerance \(10^{-42}\) is only a proposal rule.
Round the final proposed coordinates to forty decimal places, giving
exact rational complex \(q_0\). At that rounded point form a floating
inverse of the analytic Jacobian and the response \(-H^{-1}f_c\),
then round each component to forty decimal places, giving exact
rational \(P,T\). There is one proposal and no alternative seed,
midpoint, precision or retry. Neither floating convergence nor the
floating inverse has a proof role.

## 3. Whole-box residual certification

For \(\delta=c-c_0\), form the full-box affine predictor
\(q_{\mathrm{aff}}=q_0+T\delta\). Its entire image must stay
inside the common convex product \(E\times U\times Q^5\) of
the residual theorem. Check every original \(j=J'\) argument
has real part strictly between zero and one before using its sine,
cotangent or third derivative. These checks include
\(1/2-\xi,\xi,e-\xi\) in the auxiliary row.

At the rational midpoint data compute outward
\[
 r_0=f(q_0;c_0),\quad H_0=f_q(q_0;c_0),\quad s_0=f_c(q_0;c_0),
 \quad L_0=H_0T+s_0.
 \tag{2}
\]
For every gradient term \(a_{ik}j(L_{ik})\), enclose
\(-\pi^2\csc^2(\pi L_{ik})\) over the full affine image and
charge
\[
 \rho_i=\sum_k|a_{ik}|\,\overline{|J'''(L_{ik})|}
                          |L_{ik}(T,1)|^2.
 \tag{3}
\]
The chirps are affine and contribute no second derivative. Exact
rational squared-modulus bounds and outward square roots give
\(R_0\ge\|r_0\|_2\), \(L\ge\|L_0\|_2\),
\(R_2\ge\|\rho\|_2\), and \(d\ge\sup|\delta|\).
Equations (16)--(17) of the
[boundary-extension proof](research_mixed_stationary_reference_boundary_extension.md)
and \(\mu_-=6\pi_-/49\) then give
\[
 \|q_*(c)-q_{\mathrm{aff}}(c)\|_2
 \le \varepsilon
 :=(R_0+Ld+R_2d^2/2)/\mu_-.
 \tag{4}
\]
This proof applies separately at every actual typed point in the
cell, even if other points of the enclosing rectangle have no
canonical-existence premise. Save all raw affine boxes, residual
vectors, termwise remainder bounds and rational norm factors.

Expand every real and imaginary affine coordinate interval by
\(\varepsilon\). Only after (4), intersect these localized boxes
with the common product and the proved necessary endpoint/ordinary
reference rectangles. These are the mandatory filters in Sections 2
and 4 of the original reference theorem: every canonical solution
at an actual \(c\in K_3\cup K_4\) satisfies them. For the external
coordinate, exclude an alternative only by its own necessary disk,
height or oblique inequality, and retain the rectangle hull of all
surviving typed alternatives. This hull contains every actual external
point of the cell, even when the full chart box also contains points
outside the typed domains. Save every
unclipped and clipped box and every intersection. An empty necessary
intersection excludes actual references; it does not request a new
proposal. No clipped value enters (2)--(4).

## 4. Verified response and output

On the resulting actual-point enclosures, evaluate the original
Jacobian \(H=f_q\) and rank-one forcing \(s=f_c\). Keep the
whole interval matrices. For the exact rational preconditioner
\(P\), compute \(E=I-PH\) and an outward row-sum bound
\(\eta\ge\|E\|_\infty\). Require \(\eta<1\).
Then
\[
 \|H^{-1}-P\|_\infty
 \le\frac{\eta\|P\|_\infty}{1-\eta},\qquad
 \|q_*'-T\|_\infty
 \le\frac{\|P(HT+s)\|_\infty}{1-\eta}.
 \tag{5}
\]
The first formula follows from \(H^{-1}=(I-E)^{-1}P\);
the second uses the exact identity \(Hq_*'+s=0\).
Expanding each complex entry by the corresponding bound gives
rigorous inverse and derivative rectangles. This evaluates the
Jacobian at enclosed actual points; it does not differentiate a
clipping operation. Save \(H,P,E\), inverse rectangles, the
response residual and all seven derivative rectangles.

Finally form the seven negative shapes \(\exp(-2\pi iw)\) from
the actual-point enclosures, excluding the auxiliary \(\xi\).
Return `enclosed` only when the residual, original domains and
response verification all succeed. A failed finite arithmetic or
Neumann check is `inconclusive`, with partial witnesses preserved.
Unexpected code/API errors have status `error` and a saved
`unexpected_error` field; the caller must stop and archive them,
rather than subdividing on a programming failure.
The provider neither changes the caller's cell nor retries it.
The live coordinate dictionary includes \(c\), while the derivative
dictionary has the seven names of \(q\). Quantitative phase-height
and response-cost checks remain the caller's responsibility.
