# Outward four-leg references and third-selection tangent bounds

Implementation proof, 6 November 2026. The two modules below implement
the value-only protocol of the
[center-comparison theorem](research_mixed_third_selected_center_comparison.md).
They perform no cover on import. The product-boundary driver owns the
exact geometry, finite visit/depth budgets, complete partitions and
final decision. No interval or source calculation is reported here.

## 1. Reference provider contract and original equations

[The provider](../experiments/mixed_third_selected_external_reference.py)
exposes `initialize()` and `evaluate(alpha,beta,abox,cbox)`.
Each external rectangle is the exact tuple
`(real_lower,real_upper,imag_lower,imag_upper)`.
Its result is JSON-safe, with status `enclosed`, `inconclusive` or
`error`, coordinates `(a,u,z,v,b)`, counters and partial diagnostics.
The conclusion is conditional on actual external parameters in
\(a\in K_{3+\alpha}\), \(c\in K_3\cup K_4\) and the supplied
rectangles. The caller retains the external type and chart association.
The provider never excludes a chart cell geometrically.

Use \(q=(u,z,v,b)\) and exactly the four original residuals in
[the fixed diagnostic](research_mixed_third_selected_two_vertex_diagnostic.md),
equation (8). Write \(G(q,a,c)\) for this vector, and
\(k(w)=g''(w)=\pi\cot\pi w-i\pi\). Its symmetric tridiagonal
Jacobian has diagonal
\[
\begin{split}
 k(u+z)+k(a+u)-3k(u),&\quad k(u+z)+k(z+v)-3k(z),\\
 k(z+v)+k(v+b)-(2+\beta)k(v),&\quad
 k(v+b)+k(b+c)-(2+\beta)k(b),
\end{split}
\tag{1}
\]
and off-diagonal entries
\[
 k(u+z),\qquad k(z+v)+2\pi i,\qquad k(v+b).
\tag{2}
\]
The external derivative vectors have only
\((G_a)_u=k(a+u)+2\pi i\) and
\((G_c)_b=k(b+c)+2\pi i\) nonzero.
These differentiate original logarithms; no exponentiated equation
or independent logarithmic lift is introduced.

One proposal starts from the own typed centers, takes at most twenty
Newton steps at fifty decimal digits, and rounds its center \(q_0\)
and two predictor columns \(T_a,T_c\) to forty decimal places.
The two external centers are the exact rectangle midpoints.
A numerical solve of (1)--(2) proposes the predictor columns. Its
inverse and its convergence flag are not certificates. There is no
alternate seed or retry.

## 2. Full-box residual bounds before any clipping

Put \(\delta_a=a-a_0\), \(\delta_c=c-c_0\) and
\[
 q_{\rm aff}=q_0+T_a\delta_a+T_c\delta_c.
\tag{3}
\]
All arithmetic uses the full supplied external rectangles, before
intersection with any necessary reference image. The full affine
image must lie in \(Q^4\), where
\(Q=[.23,.45]+i[-.12,.12]\); the supplied rectangles must lie in
\(Q\), too. Failure is inconclusive. Every own and summed logarithmic
argument must have real part strictly between zero and one throughout
the connecting set. These conditions also justify the common original
branch and the residual Taylor formula.

There are two independent residual estimates. The direct one evaluates
\(G(q_{\rm aff},a,c)\) by outward original logarithms. For the
centered one, let
\[
 L_a=G_q(q_0,a_0,c_0)T_a+G_a(q_0,a_0,c_0),\qquad
 L_c=G_q(q_0,a_0,c_0)T_c+G_c(q_0,a_0,c_0).
\tag{4}
\]
Every logarithm in residual row \(i\) has an affine argument
\(w_j=w_j^0+h_j\), where
\(h_j=d_{ja}\delta_a+d_{jc}\delta_c\). Its coefficient is an
integer \(n_{ij}\), including the own coefficient \(-3\) or
\(-(2+\beta)\). Since
\[
                  g'''(w)=-\pi^2\csc^2\pi w,
\tag{5}
\]
a valid row remainder is
\[
 R_i=\tfrac12\sum_j |n_{ij}|
       \sup_{\rm full\ affine\ image}|g'''(w_j)|
       \sup_{\rm full\ external\ box}|h_j|^2.
\tag{6}
\]
The chirps are affine in these parameters and have no remainder.
The midpoint, linear-defect and quadratic terms are all retained.
Sine denominators are tested by Cartesian separation from zero;
the reciprocal is formed before squaring to avoid a needless product
rectangle obstruction. A failed Taylor refinement may fall back to
the independently finite direct residual estimate.

For each row choose the smaller of its valid direct and Taylor modulus
upper bounds, denoted \(E_i\). The existing canonical existence and
\(-\Re\mathcal W''\succ\pi I/4\) give, at every actual parameter,
\[
 \|q_*-q_{\rm aff}\|_2\le\rho,
 \qquad \rho=\frac4\pi\sqrt{\sum_iE_i^2}.
\tag{7}
\]
An outward rational upper value is used for \(\rho\): the code uses
\(\pi>157/50\) and saves a rational radius whose square is at least
\((200/157)^2\sum_iE_i^2\). Thus expanding
every real and imaginary affine coordinate interval by this radius
is valid. This uses a segment between the known canonical root and
the affine trial in \(Q^4\), not a contraction or an inverse theorem.

Only after (7), the resulting root images may be intersected with
the proved ordinary rectangles: \(u,z\in O_4\), and
\(v,b\in O_{3+\beta}\). The direct external coordinate \(a\)
may likewise be intersected with the rectangular bounds of its
\(K\) domain. These are necessary actual-reference restrictions,
not differentiated maps. Raw affine, residual, radius and root records
are preserved separately. Empty intersections remain inconclusive,
so they never substitute for the caller's exact geometric exclusions.

The interval precision is fixed at 256 bits and checked explicitly.
Expected domain/arithmetic failures have status `inconclusive`;
unexpected exceptions have status `error`. Both preserve their
partial witnesses and counters for the caller to archive.

## 3. Target evaluator and signed compensation

[The evaluator](../experiments/evaluate_mixed_third_selected_tangent.py)
exposes `initialize()`,
`propose_trial(reference,alpha,beta,left,right,nu)`, and
`evaluate(reference,anchor,alpha,beta,left,right,nu,trial)`.
The proposal returns `(exact_trial, metadata)` and makes at most one
bounded numerical target optimization. The evaluation uses only the
supplied exact trial and the original phase; optimizer success is not
an acceptance condition.

The reference is a provider result with `coordinates`. The anchor is
its matching certified center row from the frozen eight-center record,
whose coordinates are in `reference_certificate.coordinates`.
Both must carry the same \(\alpha,\beta\); the caller binds the
anchor's right external type to its chart case. Neither a midpoint
reference nor an independently normalized action is substituted.

Keep \(F,p_L,p_R\) from the center-comparison theorem. On each
full original target box the evaluator computes the literal defect,
its five real derivatives and
\[
 U=f(y)^+ +\sum_i\max\{d_i^-(l_i-y_i),d_i^+(r_i-y_i)\}.
\tag{8}
\]
The original cuts are real, the selected height is \(.01\), and
both Fourier alternatives retain all of \(P\). No target domain
is optimized independently of the original reference.

The returned `compensation_record` contains the same current and anchor
\(p_L,p_R,a,b\), both product contributions, and the exact rational
interval for
\[
 C_0=\tfrac12\Re\{(p_L-p_L^0)\overline{a-a_0}
                         +(p_R-p_R^0)\overline{b-b_0}\}.
\tag{9}
\]
The real parts of these products are recombined from their saved
Cartesian rational endpoint intervals, so a stdlib-only checker can
reproduce the compensation interval exactly. Its lower endpoint is
retained, including if its upper endpoint overlaps zero. The final
quantity is precisely
\[
                         U-C_0^-.
\tag{10}
\]
All support products, original trial bounds, marginals and primitive
call counts are saved. The separate signed-energy theorem supplies
\(C_0\le0\) and separate subharmonicity; this evaluator supplies
only the outward values needed by that theorem. A positive or
inconclusive bound is not a geometric exclusion.
