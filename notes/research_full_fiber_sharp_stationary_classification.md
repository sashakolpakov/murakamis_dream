# Finite shared multipliers and the stationary branches after full-fiber activation

31 October 2026. **Internally reviewed analytical research addendum.**
Root and a separate reader completed full analytical reviews. This is a
calculus theorem for the original sharp full-source upper functional. It
uses the reviewed full-fiber boundary reduction and the original weighted
cofactor primitives. It makes no local weighted-maximality, strong-duality,
phase-compatibility, cap-geometry or volume-comparison assertion.

## 1. The original maximum and its remaining degrees

Use precisely the original simple-white certified diagram, protected pair,
full transport fiber and independent real spectra of
[full-fiber boundary activation theorem](research_full_fiber_sharp_boundary_activation.md). Each original
port has supply one; each ordinary face has demand one; the two protected
faces have demand zero. No LEFT/CROSS/RIGHT label inequality is imposed.
For one port write

\[
 q=(\xi,\mu,1-\nu,\nu-\mu-\xi)
       \quad\text{in the order }(x,b,c,y).
\tag{1}
\]

The theorem applies to an unrestricted global maximum. It also applies
to a competing maximum of value at least \(\Phi_D\) in the closed
non-CROSS union, provided at least one middle load is strictly greater
than \(1/2\). That strict margin persists in a neighborhood, so every
sufficiently small variation within the full transport fiber is still
admissible for this restricted problem. No seam-only NC maximum is
included.

The boundary reduction has already proved:

* all ordinary incidences have positive load and every port has positive
  interval length;
* at \(0<\delta<1/2\), neither interval endpoint is an alpha zero;
* every \(\delta=0\) port is strict CROSS;
* half-terminal monomial intervals are absent at every spectrum;
* a remaining cap \(\delta=1/2\) is a monomial interval
  \([0,\nu]\), \(0<\nu<1/2\), or its reflection, with its parent
  middle and one outer incidence both protected. There are at most two,
  adjacent to the original marked MAIN edge.

Keep these protected coordinates fixed at zero. The maximum is in the
relative interior of the resulting original transport polytope. The
relative-interior assertion is about actual incidence coordinates, not
an enlarged triangle or fractional-cover flow.

## 2. Fixed-spectrum smoothness and finite common weights

Put
\[
 \begin{aligned}
 \alpha_\delta(t)&=4\bigl[\cos^2(\pi\delta)-\sin^2(\pi t)\bigr],\\
 \beta(t)&=4\sin^2(\pi t),\qquad
 \eta_\delta(t)=\frac{\cos^2(\pi\delta)}{\sin^2(\pi t)},\\
 \Lambda_\delta(t;x,y)&=
 \frac{\beta(t)}2
 \left[x+y+\sqrt{(x-y)^2+4\eta_\delta(t)xy}\right].
 \end{aligned}
\tag{2}
\]
The original sharp functional is
\[
 h_\delta(q)=
 \int_0^\mu\log|\alpha_\delta(t)|\,dt+
 \int_\nu^1\log|\alpha_\delta(t)|\,dt+
 \inf_{\ell\in\mathbb R}
 \left\{\int_\mu^\nu\log\Lambda_\delta(t;e^\ell,1)\,dt
                   -\xi\ell\right\}.
\tag{3}
\]
Both unused integrals and their normalization remain present.

If both outer incidences are ordinary, their loads are positive. Thus
\(0<\xi<\nu-\mu\). For \(\delta<1/2\) the integrated logarithmic
root has a unique finite minimizing tilt. Indeed
\[
 \partial_\ell^2\log\Lambda_\delta(t;e^\ell,1)
 =\frac{\eta_\delta(t)\cosh(\ell/2)}
 {4\bigl(\sinh^2(\ell/2)+\eta_\delta(t)\bigr)^{3/2}}>0,
\tag{4}
\]
and its first derivative ranges from zero to one. The integrated first
derivative therefore ranges from zero to \(\nu-\mu\). At a protected
start zero or stop one, the first derivative is bounded by one and
the second derivative is integrable; on compact tilt sets it is
\(O(t)\) or \(O(1-t)\) at the corresponding endpoint. The implicit
function theorem consequently gives a smooth finite tilt in the free
degree coordinates.

Every movable row is strictly inside \((0,1)\). At strict spectrum it
also avoids the two alpha zeros, so differentiating the outside
integrals in that row is regular. Their possible interior logarithmic
zeros do not affect this degree smoothness. At \(\delta=0\), the
strict CROSS inequalities keep both movable endpoints away from the
central zero. A protected endpoint is fixed and is not differentiated.
Thus (3) is \(C^1\) on the relevant relative open face.

If an outer incidence is protected, specialize the exact monomer first:
its forced outer degree leaves
\(\Lambda_\delta(t;0,y)=\beta(t)y\), or its reflection. The same
row argument proves smoothness on this protected face without taking a
finite tilt of a zero weight. Both outer incidences cannot be protected,
because their MATCHING edge differs from the marked MAIN edge. Finally,
at the cap the full sharp functional is identically zero for every
degree vector. It is smooth on its protected-coordinate face as well.

Let \(A\) be the original finite row/face constraint matrix after
protected incidences are removed. The differential of the total
fixed-spectrum entropy annihilates \(\ker A\): every sufficiently small
positive and negative tangent displacement is admissible. Elementary
row-space orthogonality gives finite real row and face multipliers.
Redundant balance equations cause no difficulty. Choose the sign of the
ordinary face multiplier \(\lambda_f\) so that
\[
 L_f=e^{-\lambda_f}>0,\qquad
 \mathcal F_e(q_e)=h_{\delta_e}(q_e)
                   +\sum_{f\text{ at }e}q_{ef}\log L_f.
\tag{5}
\]
Here \(\mathcal F_e\) is stationary on the local row simplex. The row
multiplier drops out because the local supply is fixed. The same
finite \(L_f\) occurs at every original incidence of \(f\). At protected
faces use the literal value zero only after specializing their zero
coordinates; no expression \(0\log0\) or infinite multiplier is used.

This is equality stationarity in degree variables. It is not local
maximality of an individual weighted coupon. In particular no independent
optimization of local rows or interchange of a shared infimum and maximum
has been used.

## 3. The exact row equations and branch derivatives

At a port let \(x,b,c,y\) now denote its common face weights. A protected
one is zero in the literal specialized formula. If both outer weights
are positive, outer stationarity in (5) sets the minimizing tilt to
\(\ell=\log(x/y)\). Homogeneity and
\(\int_0^1\log|\alpha_\delta|=0\) then give the stationary local
Lagrangian in the exact form
\[
 F(\mu,\nu;\delta)=\mu\log b+(1-\nu)\log c+
       \int_\mu^\nu\log\mathcal L_\delta(t;x,y)\,dt,
 \qquad \mathcal L_\delta=\frac{\Lambda_\delta}{|\alpha_\delta|}.
\tag{6}
\]
Omit a protected-middle term, whose degree is fixed at zero. The same
formula follows directly from the monomer when one outer weight is zero.
Every ordinary middle row is free locally, including a row equal to
\(1/2\). Therefore
\[
 \mathcal L_\delta(\mu)=b\quad(b>0),\qquad
 \mathcal L_\delta(\nu)=c\quad(c>0).
\tag{7}
\]
A protected input has \(\mu=0\), and a protected output has \(\nu=1\),
with no corresponding derivative equation.

The spectra are independent of every row/face constraint. At a strict
spectral maximum the derivative of (3), with the degrees held fixed,
is zero. At an already stationary tilt and rows, it equals the
derivative of (6) or any of its stationary branch primitives: the
tilt and row derivatives cancel. This does not differentiate along an
assumed shared feasible family of separately optimized rows.

For precision retain the absolutely normalized primitives from
[original LEFT spectral envelope and normalized primitives](actual_global_left_weighted_spectral_envelope.md). Write
\[
 A=x+y>0,\quad P=xy\ge0,\quad z=\sin^2(\pi\delta),\quad
 D=A^2-4Pz>0,\quad p=\tfrac12-\delta.
\tag{8}
\]
On the lower half, \(\mathcal L\) increases from zero to infinity
on \((0,p)\), then decreases from infinity to
\[
 q_{\mathrm{end}}=\frac{A+\sqrt D}{2z}
\tag{9}
\]
on \((p,1/2]\). If the row solving \(\mathcal L(r)=q\) is before
the pole, its normalized half-cofactor action is \(Q_q\). If it is
after the pole, denote the action by \(J_q\). Both use the same
definition
\[
 r\log q+\int_0^r\log|\alpha_\delta|\,dt+
                   \int_r^{1/2}\log\Lambda_\delta(t;x,y)\,dt.
\tag{10}
\]
on their respective row branch. The original derivative formulas are
\[
 \begin{aligned}
 E_q&=A+2qz+2\sqrt z\sqrt{qA+P+q^2z},&
 Q_q'&=-\log(E_q/\sqrt D),\\
 T_q&=2qz-A+2\sqrt z\sqrt{q^2z-qA+P},&
 J_q'&=-\log(T_q/\sqrt D).
 \end{aligned}
\tag{11}
\]
Primes mean differentiation in \(\delta\) at fixed face weights.
These constants are those of the original outside integrals, not an
unfixed primitive. For example the post-pole derivative is fixed by
\(r\to1/2\), where the half-alpha integral has derivative zero and
\(T_q\to\sqrt D\). At a protected input the exact limiting primitive
is \(Q_0\), with \(E_0=A+2\sqrt{zP}\).

In particular \(Q_q'<0\), except when \(q=P=0\); and \(J_q'<0\)
at every strict post-pole row. At the terminal post-pole row the latter
derivative is zero. These conclusions include the exact monomer
specialization \(P=0\).

## 4. Strict spectral CROSS and half seams cannot remain

First suppose \(\mu<1/2<\nu\). Reflect the upper half by
\(t\mapsto1-t\). The full interval (3) has exactly its original two
half-cofactor Legendre expressions with one common outer tilt. At that
tilt their actual outer allocations sum to the original \(\xi\); when
both outer weights are positive, each positive-length half has a strict
outer split. No new independent angle flow is introduced.

At (7) the weighted action is the sum of one branch from
\(\{Q_b,J_b\}\) and one from \(\{Q_c,J_c\}\), with a protected
middle interpreted as \(Q_0\). Its free spectral derivative is their
sum. Every summand is nonpositive by (11). Equality of a summand is
possible only for a monomial half with its middle and one outer weight
zero. Both halves cannot be monomial: both outer weights cannot vanish,
and otherwise it would require one outer and both distinct middles to
be protected, although there are only two protected faces. Hence the
sum is strictly negative. This contradicts interior spectral
stationarity for every strict-spectrum CROSS port, including all allowed
protected patterns.

Now suppose \(\nu=1/2\) and \(\mu<1/2\). The row \(\nu\) is
ordinary and is a free coordinate in the full local simplex. Its row
equation is \(c=q_{\mathrm{end}}\). The local action is
\[
 U_b(\delta)+\tfrac12\log c,
 \qquad U_b\in\{Q_b,J_b\}.
\tag{12}
\]
Taking the spectral derivative at the stationary rows gives \(U_b'\).
It is strictly negative unless \(b=P=0\), in which case the input
start is zero and this is exactly the double-protected half-terminal
monomial. That case has already been excluded by the cost-free
\(\delta=0\) retuning in the boundary theorem. Thus no strict-spectrum
half seam remains. Exact original row reflection proves the same for
\(\mu=1/2<\nu\).

This uses an equality row equation, not a one-sided terminal KKT test:
the problem is the full original fiber, and \(1/2\) is not one of its
local row boundaries. The only fixed row boundaries are those forced
by protected zero middles.

## 5. The remaining noncap Green branches

The boundary theorem already makes every \(\delta=0\) port strict
CROSS. Sections 3--4 leave, at a strict spectrum, a strict lower-half
interval \(0\le\mu<\nu<1/2\) or its reflected upper-half interval.
For the lower interval (6) has the following exact stationary actions:

\[
 \begin{array}{c|c|c}
 \text{row positions}&F&\partial_\delta F\\ \hline
 \text{before/before}&Q_b-Q_c+\log c&\log(E_c/E_b)\\
 \text{after/after}&J_b-J_c+\log c&\log(T_c/T_b)\\
 \text{before/after}&Q_b-J_c+\log c&\log(T_c/E_b).
 \end{array}
\tag{13}
\]

Before/before forces \(b<c\), so its derivative is positive.
After/after forces \(b>c>q_{\mathrm{end}}\), so its derivative is
negative. A protected input uses \(Q_0\) and has only the first or
third possibility. Consequently a spectral critical point must
straddle the lower pole and satisfy \(T_c=E_b\).

The two numbers have the common product parameter \(D\):
\[
 E_b=C_b+\sqrt{C_b^2-D},\quad C_b=A+2bz,
 \qquad
 T_c=C_c+\sqrt{C_c^2-D},\quad C_c=2cz-A.
\tag{14}
\]
The larger-root function is strictly increasing, so the equality is
equivalent to
\[
 \mu<p<\nu<\tfrac12,\qquad
 (c-b)\sin^2(\pi\delta)=x+y.
\tag{15}
\]
The established real primitive ratio is \(-E_b/T_c=-1\). Here this is
only a local stationary identity, not a face-sign solution or a
developing representation.

If one outer is protected, \(P=0\), (13)--(15) follow from the exact
monomer. If the input middle is protected and both outers are positive,
the fixed start is \(\mu=0\), and the same argument gives
\(c=(x+y)/z\) with a strict post-pole stop. If both that middle and
one outer are protected, \(E_0=A=\sqrt D\); every strict post-pole
\(T_c\) is greater than \(A\). Therefore no strict nonterminal
Green critical point has that double-protected pattern. Its equality
case would be the half-terminal monomial already excluded.

Original row reflection gives the corresponding RIGHT branch, with
\((b-c)\sin^2(\pi\delta)=x+y\) and the reflected strict endpoint
inequalities. A protected overloaded middle cannot occur because its
degree exceeds \(1/2\), while its target is zero.

For free ordinary endpoints, the row second derivatives of (6) are
\(-\partial_t\log\mathcal L(\mu)<0\) and
\(\partial_t\log\mathcal L(\nu)<0\) on the straddling branch.
Thus the regular-window endpoint maxima follow on compact subcharts.
A protected start remains the literal fixed start; no false interior
start saddle is introduced. This does not assert local weighted
maximality in the spectral variable or eliminate a constrained shared
maximum by following separately stationary rows.

## 6. The residual cap equation and the remaining scope

For a surviving cap corner, orient it as \(x=b=0\),
\(q=(0,0,1-\nu,\nu)\), \(0<\nu<1/2\). Both remaining faces are
ordinary. The fixed-cap entropy is identically zero, and its local
stationarity equation in the genuinely free degree \(\nu\) is
\[
 0=\partial_\nu\bigl[(1-\nu)\log c+\nu\log y\bigr]
   =\log(y/c),\qquad c=y>0.
\tag{16}
\]
Use outer exchange or exact row reflection for the other orientation.
There are still at most two such ports, at the original marked pair.
Equation (16) is not a spectral boundary derivative equality and
constructs no finite cap collar or geometric pairing.

Thus every maximum in section 1 has finite common positive ordinary
face weights. Every noncap port is either complete strict CROSS at
\(\delta=0\), or a strict positive-spectral straddling LEFT/RIGHT
branch, including its allowed protected single-line specialization.
No other positive-length half seam survives. The only cap configurations
not removed by this addendum are the already classified double-protected
monomial corners, now with equal remaining weights.

These conclusions concern the proved original-source upper functional;
the global closed-domain coefficient-limsup theorem is a separate input.
No lower coefficient asymptotic, finite-level relabeling, loss of an
unused scalar, shared sign compatibility, geometric cap continuation,
absolute bound by \(\Phi_D\), or filling-period conclusion is inferred.

## Inputs and review scope

The source functional and both-parity closed-domain upper scope are in
the [global closed-domain coefficient majorant](research_global_sharp_coefficient_limsup_majorant.md).
The reduction to ordinary positivity and the global/NC hypotheses is
[full-fiber boundary activation theorem](research_full_fiber_sharp_boundary_activation.md).
The weighted roots, original normalization and derivatives in (9)--(15)
are those proved in the
[original LEFT spectral envelope and normalized primitives](actual_global_left_weighted_spectral_envelope.md);
their use in the present full-fiber setting is shown in sections3--5.
The present new points are applying smoothness to the entire reduced
protected face, obtaining finite multipliers without an extra hypothesis,
using the full-fiber row equation at a half seam, and recording (16).
Both internal readers checked all these points, the strict-spectrum
CROSS and half-seam exclusions, every allowed protected specialization,
the original normalization of the row primitives, and the strict-margin
qualification in the non-CROSS variant. These are internal proof reviews,
not external peer review. No numerical asymptotic test is claimed or
needed for this calculus addendum.
