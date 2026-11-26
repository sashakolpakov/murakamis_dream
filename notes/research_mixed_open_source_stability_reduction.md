# What a complete mixed open-source theorem must supply for later fillings

Research deduction, 5 November 2026. Completing the retained-contour
comparison is not by itself a short-filling stability theorem. This
note proves a more precise analytic reduction: a complete local source
packet and a strict real outside-color gap imply the whole quadratic
complex-strip estimate required by the existing long-filling theorem.
For the mixed three/four source, its local outside Hessian is already
fixed and strictly negative by the original ordinary-color marginals.
The real outside-color gap is not supplied by the plateau theorem.
Marked geometric boundary compatibility remains a separate premise.

## 1. A local packet and one real gap suffice for the boundary estimate

Let \(r\ge1\) be fixed and let
\[
 Q_N(\boldsymbol\theta)=
 q_N(-2\cos\theta_1,\ldots,-2\cos\theta_r)
 \tag{1}
\]
be the entire original polynomial, of separate ordinary degrees at
most \(d_jN\), with fixed \(d_j\). Suppose that on a fixed
complex neighborhood of zero it has the uniform holomorphic packet
\[
 Q_N(\boldsymbol\theta)=\epsilon_N N^\alpha
 a(\boldsymbol\theta)e^{NW(\boldsymbol\theta)}(1+O(N^{-1})),
 \quad |\epsilon_N|=1,\quad a(0)\ne0,
 \tag{2}
\]
where \(W\) is separately even and
\(-\Re W''(0)\succ0\). Put \(M=\Re W(0)\).
Choose a sufficiently small fixed \(\rho>0\) so that the
local packet and strict local horizontal concavity hold on a
neighborhood of \([-2\rho,2\rho]^r\).

Assume the additional **whole-source real gap**
\[
 |Q_N(\mathbf x)|\le C N^A e^{N(M-\delta)}
 \quad\text{for }\mathbf x\in[-\pi,\pi]^r,
                  \quad\|\mathbf x\|_\infty\ge\rho,
 \qquad\delta>0.
 \tag{3}
\]
The exponent in (3) is calibrated to \(M\), not to a larger
norm or triangle-majorant ceiling.

**Lemma 1.** Under (1)--(3), there are \(c,B,h>0\) and
polynomial prefactors such that the entire finite source satisfies
\[
 |Q_N(\mathbf x+i\mathbf y)|\le C' N^{A'}
 e^{N\{M-c\sum_j(1-\cos x_j)+B\|\mathbf y\|_2^2\}}
 \quad(\mathbf x\in[-\pi,\pi]^r,\ |y_j|\le h).
 \tag{4}
\]
The local normalized error and its fixed derivatives remain those
of (2). No source decomposition or positivity of its coefficients
is required.

*Proof.* Separate evenness gives \(W'(0)=0\) and a diagonal
Hessian at zero. On a sufficiently small real box, (2) and the
strict negative real Hessian give
\( |Q_N(\mathbf x)|\le C_0N^{A_0}e^{N(M-c_0\|\mathbf x\|^2)}\).
Combining this with (3), and using
\(\sum_j(1-\cos x_j)\le2r\), gives some \(d>0\) with
\[
 |Q_N(\mathbf x)|\le C_1N^{A_1}
 e^{N\{M-d\sum_j(1-\cos x_j)\}}
                       \quad(\mathbf x\in[-\pi,\pi]^r).
 \tag{5}
\]
For example take \(d\le c_0\) locally, since
\(1-\cos x\le x^2/2\), and \(2rd\le\delta\) outside.

Here is a direct degree argument for the strip, as in
[the homogeneous outside-boundary proof, Section 4](research_three_chain_outside_boundary_decay.md).
In one variable put \(z=e^{i\theta}\), let \(D_N\le d_jN\)
be its angular Laurent degree, and multiply
\(z^{D_N}Q_N\) by \(e^{-Ndz}\). On the unit circle (5)
bounds this analytic disk function by its constant profile
\(C_1N^{A_1}e^{N(M-d)}\), with the other real-variable
losses retained. The maximum principle, followed by division by the
nonzero factor at \(|z|=e^{-y}\), yields for \(y\ge0\)
\[
 |Q_N(x+iy)|\le C_1N^{A_1}
 e^{N\{M-d(1-\cos x)+(d_j+d)y\}}.
 \tag{6}
\]
Indeed \(d(e^{-y}-1)\cos x\le dy\). Separate evenness
handles the negative height by replacing \(x+iy\) with
\(-x-iy\). Apply this argument successively in the \(r\)
variables; evenness remains valid when the other variables are
complex. Thus the full strip costs at most
\(\sum_j(d_j+d)|y_j|\) in addition to the rate in (5).

On \(\|\mathbf x\|_\infty\ge\rho/2\), the sum of angular
losses is at least \(s_0=1-\cos(\rho/2)>0\). Choose \(h\)
so that \(h\sum_j(d_j+d)<ds_0/2\). The linear strip cost
is then absorbed by half the real loss in (5).

On \(\|\mathbf x\|_\infty\le\rho\), use (2) instead.
Holomorphic Taylor expansion at zero and Young's inequality give
\[
 \Re W(\mathbf x+i\mathbf y)
       \le M-c_2\|\mathbf x\|^2+B_2\|\mathbf y\|^2.
 \tag{7}
\]
The mixed real-height terms from the imaginary Hessian are absorbed
into these two quadratic terms; shrinking \(\rho,h\) absorbs
the higher terms. The amplitude and relative error are bounded on
this fixed neighborhood. The local and far regions overlap, so a
common smaller \(c\), larger \(B\), and polynomial prefactor
prove (4). Only the explicit Laurent monomial was divided out,
not the source polynomial. \(\square\)

The same proof applies to every fixed number of boundary variables.
It is an abstraction of the cited homogeneous patching step, not a
new estimate for the unproved mixed outside-color gap. It means that
one need not first prove a sharp quadratic complex-strip profile on
every outside color: the real gap (3) is enough once (2) is known.

## 2. The exact missing analytic statements for a mixed path

Fix a positive word \(\mathbf n\in\{3,4\}^m\), \(m\ge2\),
and keep its literal two-boundary polynomial
\[
 Z_{\mathbf n,N}(w_L,w_R)=
             v(w_L)^T A_{n_1}\cdots A_{n_m}v(w_R).
 \tag{8}
\]
Its ordinary degree is at most \(N-1\) in each variable.
The [whole unselected plateau theorem](research_mixed_full_unselected_plateau.md)
provides a nonzero local packet for its specified sector
\(Z^P_{\mathbf n,N}\), with its original phase
\(\mathcal W_{\mathbf n}(w_L,w_R)\), power \(N^{-3/2}\)
and unit scalar. It does not replace (8) by that sector.

One sufficient **full retained-contour comparison** is a bound
\[
 |Z_{\mathbf n,N}-Z^P_{\mathbf n,N}|
 \le C N^A e^{N\{\Re\mathcal W_{\mathbf n}(w_L,w_R)-\gamma\}},
 \qquad\gamma>0,
 \tag{9}
\]
on a fixed complex ordinary-color neighborhood of \((-2,-2)\).
It must include every retained selection and nonplateau region, with
the original exact source. Together with the plateau theorem, (9)
gives (2) for the whole polynomial (8). A bound only at the complete
color, or only for its fixed derivatives there, is not (9).

There is no additional local boundary-Hessian condition to certify
for this source. Set
\(W(\theta_L,\theta_R)=
\mathcal W_{\mathbf n}(-2\cos\theta_L,-2\cos\theta_R)\).
The original endpoint marginals give exactly
\[
 W''(0,0)=\operatorname{diag}
 \left(-\frac{\tan\pi u_L}{2\pi},
       -\frac{\tan\pi u_R}{2\pi}\right).
 \tag{10}
\]
Here \(u_L,u_R\) are the actual auxiliary endpoint coordinates.
This follows by differentiating the ordinary-color germs already
proved in the plateau theorem: the first derivative of
\(-2\cos\theta\) vanishes at zero and its second derivative
is two. The mixed second derivative consequently vanishes.
Since \(0<\Re u_L,\Re u_R<1/2\),
\[
 \Re\tan\pi u=
 \frac{\sin(2\pi\Re u)}{\cos(2\pi\Re u)+\cosh(2\pi\Im u)}>0.
 \tag{11}
\]
Thus (10) has strictly negative real part, without a new numerical
cover or a positivity assumption on the matrix word.

The other analytic statement needed for the long-filling input is
(3) for **the entire** polynomial (8), with outside angles ranging
over their whole real periods and calibrated to
\(M=\Re\mathcal W_{\mathbf n}(-2,-2)\). Conditions (9)
and (3), plus the already proved (10), therefore imply exactly the
local packet and global bound (1)--(3) required by
[long fillings with a complex boundary phase](research_long_fillings_complex_boundary_phase.md).
This is a precise reduction of the analytic stability obligation.
Neither the retained-coordinate plateau loss nor a larger norm-bound
far-color deficit is a substitute for (3).

## 3. What this would imply for a selected component

Suppose (9) and (3) have been proved for every fixed positive mixed
three/four path. Such a path of \(k\) original degree-two vertices
with two distinct unfilled boundary vertices then has the exact source
(8), power \(N^{-3/2}=N^{3(k-(k+1))/2}\), nonzero amplitude,
and the required whole boundary-period/strip estimate. Uniform
sign reversal follows from the original polynomial identity
\(A_{-n}=\overline{A_n}\), with real ordinary Newton basis.
This covers a simultaneous reversal of all path signs; it is not a
claim for arbitrary mixed signs within a path.

To use the analytic component in an original knot, retain the following
**marked geometric premise** as well. Its phase must agree, throughout
a neighborhood of the free outside angles, with the stationary
original geometric component action up to a constant in \(i\mathbb R\).
The component must provide compatible original ordered face maps,
positive shapes and selected core lengths, the full continued primitive
periods for its original integer slopes, complete main cusps, and the
absolute volume at complete outside angles. Its selected filling must
remain smooth on that boundary germ. A complete-point equality of
volumes alone does not assert this derivative and marking statement.
The [mixed source/geometric identification](research_mixed_geometric_source_identification.md)
and [absolute calibration](research_mixed_geometric_action_calibration.md)
provide the complete-point identification; this deduction does not
silently enlarge their stated boundary-germ scope.

**Conditional component consequence.** With the analytic conclusions
above and this marked geometric premise, such paths may be selected
components beside the already proved components, and all remaining
original powers may be chosen independently sufficiently long.

*Proof.* Repeat the exact component assembly in
[the three-chain stability theorem](research_three_chain_short_filling_stability.md),
Sections 4--5. Every original edge is used once. On a tree an outside
vertex meets a given component at most once, and separate evenness
makes the aggregate boundary Hessian diagonal. Each free vertex has
an original incidence supplying strictly negative real curvature and
positive angular loss, from an untouched edge or a component. The
local amplitudes multiply to a nonzero amplitude. Lemma 1 supplies
the global strip bound for the complete remaining polynomial, whose
degree in a shared free color may be a fixed multiple of \(N-1\).
The long-filling theorem permits that degree.

If \(r\) vertices remain, the original edge count gives the initial
power \(-3(r-1)/2\). Their complete traces add \(3r/2\), so
the final power is \(3/2\) and its original trace coefficient is
nonzero. The fixed long-power threshold keeps the new stationary
point and charge path inside the marked geometric neighborhood.
The primitive period identities and absolute volume anchor then
identify the real action with the original knot volume, exactly as
in the cited component proof. No quotient of matrix traces or
unverified dominant-line overlap is used. \(\square\)

## 4. Why this still does not imply per-template cofiniteness

The preceding consequence treats a specified family of degree-two
components. A finite-branching deduction for an arbitrary fixed
marked template requires the partial-filling implication at every
node reached by that finite branching, with the actual fixed integer
powers there. A theorem for positive three/four paths does not
supply arbitrary short powers, arbitrary sign patterns, branching
components, or every source created by their exact marked reductions.
No threshold uniform over all such partial assignments is needed;
what is needed is an applicable theorem at each visited node.

There is also a genuine geometric obstruction to requiring every
intermediate partial filling to stay in the current positive
hyperbolic class. The strict-padding construction in
[finite exceptions under partial fillings, Section 8](research_finite_exceptions_under_partial_fillings.md)
produces a fixed template with infinitely many assignments all equal
to one prescribed hyperbolic strict core. Its short partially filled
exterior can be nonhyperbolic while all those final descendants are
hyperbolic. One must either prove the required identity for that core
and preserve its full original assignment fiber under reduction, or
supply another theorem controlling those descendants. Discarding the
intermediate exterior, or proving only finitely many reduced knot
types remain, does not close the assignment-counting argument.

Thus the new plateau theorem fixes the central nonzero source
contribution. Equations (9) and (3) specify the additional analytic
requirements for a mixed path to be usable in the existing stability
machinery. That machinery still needs its marked geometric boundary
germ. Extending those inputs or exact reduction alternatives to the
partial assignments actually required by the finite tree is what
would discharge the per-template finite-exception lemma; the present
sector theorem alone does not do so.
