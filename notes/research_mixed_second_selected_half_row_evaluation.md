# Outward evaluation of the second-selection half-row budget

Research implementation specification, 6 November 2026. This defines
a bounded scalar calculation from already certified original references.
No sign is asserted, and no execution is supplied by this specification.

## 1. Input, source and fixed target domains

Use equation (28) of the
[half-row budget](research_mixed_second_selected_half_row_budget.md),
with first flag \(\alpha=1\), outgoing flag \(\beta\in\{0,1\}\),
and selected height \(H=1/100\). The intended missing comparison is
\(\beta=0\); the same formula also defines a valid \(\beta=1\) test.
Position 1 remains unselected. Both ordinary indices and all
retained references belong to one original canonical prefix.

The caller supplies certified complex enclosures of
\((a_*,u_*,z_*,v_*,b_*)\) and the negative-sign shapes
\[
 U=e^{-2\pi iu_*},\quad Z=e^{-2\pi iz_*},\quad
 V=e^{-2\pi iv_*},\quad B=e^{-2\pi ib_*}.
 \tag{1}
\]
For each actual external parameter under consideration, all supplied
boxes must enclose this same prefix and these exact shapes. They may
come from the original residual provider or a binding-preserving
extraction of its saved certificate. No new source root is inferred
from the boxes. Existence, the original zero logarithmic lifts and the
stationary equations remain the caller's proved hypotheses.

The module checks the containing actual-coordinate ranges used in the
budget: \(a_{*,R}\in P=[.22,.45]\),
\(u_{*,R},z_{*,R}\in[.24,.36]\), with
\(\Im a_*\in[-.078,.021]\) and
\(\Im u_*,\Im z_*\in[-.102,-.001]\).
For \(\beta=0\), the two right coordinates have real parts in
\([.267,.433]\) and heights in \([-.065,.068]\); for \(\beta=1\)
use \([.24,.36]+i[-.102,-.001]\).
Closed enclosures are sufficient because the original references
satisfy the corresponding strict hypotheses. A box not contained in
these ranges is inconclusive, not geometrically excluded.

The real target product is
\[
 P\times[.22,.5]\times P\times P
 \quad\text{in the order }(a,u,z,b).
 \tag{2}
\]
Both Fourier alternatives use the whole selected interval \(P\).
No dominance cutoff or change of the actual trial center is made.
The two original boundary tangents are already included in the
half-row budget; its trial's boundary displacements vanish.

## 2. Shared forces and the literal relative action

Set \(z_H^*=\Re z_*+iH\) and
\(\lambda=\exp(2\pi(H-\Im z_*))\). Compute six outward logarithmic
moduli
\[
 \begin{array}{lll}
 L_1=\log|1-\lambda UZ|,&L_0=\log|1-UZ|,&
 L_+=\log|1+\lambda Z|,\\
 L_-=\log|1-\lambda Z|,&L_b=\log|1+B|,&
 L_{vb}=\log|1-VB|.
 \end{array}
 \tag{3}
\]
Every modulus must be strictly separated from zero. Their real values
are the real parts of the original logarithmic differences, not a
choice of a new complex lift. The forces are exactly
\[
 A=L_1-L_0,\qquad P_\nu=L_1+L_+-(2+\nu)L_-,
 \qquad D_b=L_b-L_{vb},\qquad \nu=0,1.
 \tag{4}
\]
The original geometry gives \(A>0\). The evaluator requires its
outward enclosure to certify this sign. Neither \(P_\nu\) nor \(D_b\)
is given a sign.

The relative trial is equation (9) of the budget, evaluated before
adding any scalar gains:
\[
 \begin{split}
 T_\nu=\Re\{&
  g(u_*+z_H^*)-g(u_*+z_*)
  +g(1/2+z_H^*)-g(v_*+z_*)\\
 &+g(1/2+b_*)-g(v_*+b_*)
  -(2+\beta)[g(1/2)-g(v_*)]\\
 &+3g(z_*)-(2+\nu)g(z_H^*)
       +2\pi i[\tfrac12z_H^*-z_*v_*]\}
       -2\nu\pi H .
 \end{split}
 \tag{5}
\]
Use the original
\(g(w)=[\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6]/(2\pi i)\).
The [centered primitive enclosure](research_mixed_centered_primitive_enclosure.md)
evaluates it on its original strip \(0<\Re w<1\).
All nine arguments in (5) other than \(1/2\) are recorded and
checked on their entire supplied rectangles. The exact identity
\(g(1/2)=i\pi/8\) supplies the remaining value without a primitive
call. Its complex contribution is retained.

In particular the \(\beta g(v_*)\) reference contribution and the
asymmetric chirp in the last line of (5) survive. Only the terms
proved to cancel in the budget have been canceled.

## 3. One original conjugate and two rational quadratic bounds

For the left-index term use the unchanged Evaluator.conjugate
from the [original evaluator](../experiments/diagnose_mixed_second_selected_central_budget.py):
coefficient one, force \(A\), center \(\Re u_*\), height
\(\Im u_*\), target interval \([.22,.5]\), and both exact-zero
shortcuts disabled. This evaluates the original convex Bregman
conjugate \(\phi_u^*(A)\), including endpoint clipping.
The actual center is neither clipped nor replaced. Although \(A>0\)
places the maximizing displacement on the nonnegative side, the
full interval is harmless and is the original formula.

For the other terms use the proved rational lower curvatures
\[
 \mu_0=32/5,\quad\mu_1=69/10,\qquad
 \gamma_0=57/10,\quad\gamma_1=41/10.
 \tag{6}
\]
Here \(\mu_\nu\) is for the selected-coordinate potential and
\(\gamma_\beta\) includes the original outgoing halfweight.

The following exact endpoint rule encloses a clipped quadratic gain.
Suppose \(p\in[p_-,p_+]\), \(x_*\in[c_-,c_+]\subseteq[l,r]\)
and \(\eta>0\). Put
\[
 \begin{split}
 f_-&=\max(0,-p_-),&L_-&=c_+-l,&
 t_-&=\min(L_-,f_-/\eta),\\
 f_+&=\max(0,p_+),&L_+&=r-c_-,&
 t_+&=\min(L_+,f_+/\eta),\\
 G&=\max\{f_-t_--\eta t_-^2/2,\,
          f_+t_+-\eta t_+^2/2\}.
 \end{split}
 \tag{7}
\]
For each possible force and center,
\[
 \max_{l-x_*\le t\le r-x_*}\{pt-\eta t^2/2\}\le G.
 \tag{8}
\]
Indeed handle \(t\le0\) and \(t\ge0\) separately, enlarge their
lengths and increase the corresponding nonnegative force. Both
maxima in (7) are exact concave-quadratic maxima. The unrestricted
bound \(\max(p_-^2,p_+^2)/(2\eta)\) is also valid; the module
records both and takes their exact rational minimum. It never
replaces one Fourier alternative by the other.

Apply (7) with \((p,x_*,\eta)=(P_\nu,\Re z_*,\mu_\nu)\)
and \((D_b,\Re b_*,\gamma_\beta)\), always with
\([l,r]=P\). Record the two signed displacement lengths,
forces, clipped optimizers and upper bounds. Combining the budget
with (8) gives the sufficient branch upper bound
\[
 D_{0R,\nu}\le T_\nu+\phi_u^*(A)+G_{z,\nu}+G_b.
 \tag{9}
\]
The final exact rational upper endpoint is the sum of the directed
upper endpoints of \(T_\nu,\phi_u^*(A)\) and the two rational
majorants. It is an upper majorant, not a two-sided enclosure of
the original optimized phase.

## 4. API, provenance, limits and interpretation

The new [module](../experiments/evaluate_mixed_second_selected_half_row_budget.py)
exports initialize() and
evaluate_reference(e, shapes, coordinates, beta, gap).
It imports only standard-library definitions at module load, creates
no numerical constants then, and has no command-line execution path.
initialize() checks and returns its exact input hashes and its
own hash. It imports no repository provider and evaluates no function.
The caller must merge these bindings with all frozen dependencies of
the supplied old evaluator and centered primitive, and verify the
merged bindings before and after an eventual bounded calculation.

The argument e is the unchanged old Evaluator, with
old.make_primitive_class(four)() as its primitive. These class
definitions reuse the reviewed centered primitive without constructing
the unrelated fixed private cut. The caller sets outward precision
before creating either object. The module verifies their method-source
locations but does not call any old reference, transfer, inspection,
root or finite-source routine.

Each reference call has at most:

* two branch attempts, both on the full selected interval \(P\);
* six direct logarithmic-modulus calls;
* nine direct centered primitive calls and one node conjugate, which
  adds two centered primitive calls, for a total of eleven;
* three exact rational quadratic calculations, one common outgoing
  gain and one selected gain per branch.

These finite limits are checked against the provider counters, and
all counters and partial witnesses are returned. A primitive strip,
modulus, containing-domain or force-sign failure is inconclusive and
cannot exclude an actual reference. Unexpected programming errors
propagate so a future driver can stop and preserve its frontier.
There is no subdivision, retry, precision change or automatic fallback.

Both finite branch upper bounds are recorded even when one is
positive. Status accepted means both are strictly negative; the
smaller of their negatives is the proved cell margin. The optional
candidate gap, default \(1/2000\), is checked separately and does
not change the calculation. A positive majorant means this estimate
has not established suppression; it is not a lower bound or source
counterexample.

Saved reference and response data can be reused only through a
separately validated extraction retaining their full associations and
covering partitions. This scalar module makes no boundary-extension
claim. That requires the original half-row phase's Laplacian theorem
and a complete boundary gap compared with the original response cost.
No complete half-row or whole-source theorem is asserted before those
conditions are proved.
