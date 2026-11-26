# Marked geometry after a large crossing power and one turn

This note supplies the geometric consequence of
[the uniform large-power turn theorem](research_uniform_large_power_turn.md).
The input is an original terminal piece \(T(R^a)\), \(|a|\ge2\).
The next original vertex has exactly one incoming child and one
outgoing bare edge. Giving it a sufficiently large signed power
\(b\) produces the original boundary piece
\[
                            T(R^bT(R^a)).
                            \tag{1}
\]
No new identification of a rational-tangle interface is needed:
this is precisely the one-child case of the previously proved
marked composition theorem.

## 1. The common geometric chart

Write \(W_a(t)\) for the calibrated geometric phase of the
terminal piece. Thus
\[
W_a(t)=\operatorname{stat}_s
 \left[\psi(s,t)+\frac{ia}{4\pi}s^2-is\right].
                                                               \tag{2}
\]
For \(a=\pm2\), any exceptional imaginary constant in a different
finite-sum formula remains in its exact unit scalar. In this note
\(W_a\) always means (2).

Section 6 of
[the common marked-block geometry theorem](research_amplified_marked_block_geometry.md)
provides one complex boundary disk \(D_{r_g}\), valid for every
fixed \(|a|\ge2\), on which the following hold:

* The terminal piece has its actual positive cell and filled-tube
  realization. Its old primitive filling period stays fixed and
  its filled core has positive length.
* Its ordered incoming and outgoing triangle ratios are
  \[
  (-Q^{-1},-Q,-Q^{-1}),\qquad
  (-Q,-Q^{-1},-Q),\qquad Q=e^{it}.
  \tag{3}
  \]
  These encode the complete labelled triangle maps.
* Its pure remaining periods are
  \[
                         U_a=-2\pi W_a'(t),\qquad V_a=2it.
                         \tag{4}
  \]
* The main cusps are complete, its phase is even, and
  \(\operatorname{Vol}(B_a,t=0)=2\pi\Re W_a(0)\).
* After one common shrinkage,
  \[
                           -\Re W_a''(t)\ge c_g>0.
                           \tag{5}
  \]

The common disk statement includes the old core lengths. It does
not assert a common positive lower bound for those lengths:
as \(|a|\) tends to infinity they tend to zero. Their positivity
on the common parameter disk is proved by the exact terminal
period equation, not by a perturbation estimate depending on
their length at the origin.

Choose \(r>0\) so small that \(D_{3r}\subset D_{r_g}\), that the
original bare edge has its positive marked realization on
\(D_{3r}^2\), and that its negative phase Hessian has positive
Hermitian real part there. Also choose it inside the common
analytic disk for the terminal sources.

Apply the large-power turn theorem using this chosen \(r\).
If that theorem was initially stated with a larger working
disk, rerun its threshold choice after this shrinkage. Enlarge
its finite threshold, if necessary, so that
\[
                              \frac{4\pi}{|b|}<r
                              \tag{6}
\]
for every permitted outer power. Denote the resulting threshold
by \(B_{\rm geom}\). It is at least the analytic threshold
chosen on the smaller disk.

The common terminal chart is essential for the uniformity here.
Using only the earlier fixed-terminal theorem would give a
threshold depending on \(a\). With the common chart and common
analytic bounds already proved, \(B_{\rm geom}\) is independent
of the signs and magnitudes of \(a\). This statement concerns
one composition. It does not assert that the same analytic
working disk survives arbitrary iteration.

## 2. The original primitive filling

Let \(t\) be the angle at the new vertex and \(u\) the remaining
outside angle. Put
\[
                              P_a(t,u)=W_a(t)+\psi(t,u).
                              \tag{7}
\]
The new vertex has exactly these two incidences. Its original
carrier is \(\eta_b\), its integer coefficient is \(p_b\), and
\[
                              b=\eta_b-2p_b.
                              \tag{8}
\]
Insert this carrier once.

Cut the two reference tori along their original disk longitudes
and glue their annular sectors in the prescribed order.
The maps (3) agree with those of the bare edge. The new
meridian traverses both sectors once, while the longitude is
one common primitive curve. This is the actual annular
composition in
[the rooted-piece geometry theorem](research_recursive_marked_block_geometry.md),
Section 2, with one child. It gives
\[
\begin{split}
U_b&=-2\pi(P_a)_t-i\eta_b t,& V_b&=2it,\\
U_b+p_bV_b
 &=-2\pi\left((P_a)_t+\frac{ib}{2\pi}t\right).
\end{split}                                                     \tag{9}
\]

For real charge \(0\le\lambda\le1\), the analytic theorem
constructs the branch through zero satisfying
\[
(P_a)_t(t_\lambda(u),u)+\frac{ib}{2\pi}t_\lambda(u)
                                  =i\lambda,
\qquad
|t_\lambda(u)|\le\frac{4\pi\lambda}{|b|}.
                                                               \tag{10}
\]
It is holomorphic on a common outside disk \(D_\rho\), with
\(\rho\le r\). By (6), it remains in the common geometric chart.

**Proposition 1.** For every fixed \(|a|\ge2\) and
\(|b|\ge B_{\rm geom}\), equation (10) is the actual marked
positive cone filling at the new vertex. At unit charge it
gives the smooth original filling of power \(b\).
The resulting piece retains its one original free boundary,
with the complete maps (3), all older primitive slopes fixed,
and all main cusps complete.

**Proof.** Apply Proposition 1 of the rooted-piece geometry
theorem with one child, phase (7), and the small branch (10).
The child is evaluated only inside its common positive chart;
the bare edge stays in its positive bidisk. Equation (9)
is the full logarithmic period
\[
                            U_b+p_bV_b=-2\pi i\lambda.
\]
It is not an equation only modulo \(2\pi i\).

For clarity, positivity of the new core also follows directly.
The quotient
\[
                         Q_a(t,u)=\frac{(P_a)_t(t,u)}{t}
\]
is holomorphic at zero by evenness. On the chosen disk
\(\Re Q_a\le-c_0<0\), uniformly in \(a\). The exact equation gives
\[
-\Im t_\lambda(u)=
 \frac{-4\pi^2\lambda\Re Q_a(t_\lambda(u),u)}
      {b^2|1-2\pi iQ_a(t_\lambda(u),u)/b|^2}>0
\]
when \(\lambda>0\), including complex \(u\in D_\rho\).
The core length is \(-2\Im t_\lambda\). Its meridian winding
starts with the original cusp marking and remains unchanged
along the positive path; at \(\lambda=1\) the tube is smooth.

Every older slope is already held fixed in the child's
holomorphic geometry, and every older core stays positive
throughout that disk. The exact triangle identifications
preserve the main-cusp parabolic identities. No new boundary
curve or framing convention has been introduced.
\(\square\)

## 3. The outside period and the absolute volume

The selected phase is
\[
S_{a,b}(u)=\operatorname{stat}_t
 \left[W_a(t)+\psi(t,u)+\frac{ib}{4\pi}t^2-it\right].
                                                               \tag{11}
\]
This is exactly the phase of the large-power turn theorem.
The envelope identity gives
\[
S_{a,b}'(u)=\psi_u(t_*(u),u).
\]
Consequently the remaining boundary has the original pure periods
\[
                         U_{\rm out}=-2\pi S_{a,b}'(u),
\qquad                    V_{\rm out}=2iu.             \tag{12}
\]
Its carrier has not yet been inserted into the phase. When this
piece is glued at an outside original circle, that circle's
carrier is inserted once after summing all incident responses.

At \(\lambda=0,u=0\), the child and bare edge glue at a complete
cusp and their volumes add:
\[
\operatorname{Vol}_{\lambda=0}
                 =2\pi\Re\{W_a(0)+\psi(0,0)\}.         \tag{13}
\]
For the charge path set
\[
C(\lambda)=P_a(t_\lambda(0),0)
       +\frac{ib}{4\pi}t_\lambda(0)^2-i\lambda t_\lambda(0).
\]
Stationarity gives
\[
                        \frac{d}{d\lambda}\Re C
                                      =\Im t_\lambda(0).
\]
All older core angles stay fixed at \(2\pi\). Schläfli's
differential therefore has only the new term:
\[
d\operatorname{Vol}
     =-\tfrac12(-2\Im t_\lambda)\,d(2\pi\lambda)
     =2\pi\Im t_\lambda\,d\lambda.
\]
Together with (13), this proves the absolute identity
\[
\boxed{\operatorname{Vol}(B_{a,b},u=0)
                                  =2\pi\Re S_{a,b}(0).}           \tag{14}
\]
The exact finite-source unit scalars, including those at
\(a=\pm2\) and the original outer chirp scalar, remain as in
the analytic theorem. They do not alter (12) or (14).

Combining that theorem with (14) gives an actual volume identity
for the original canonical boundary polynomial:
\[
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\left|
 \operatorname{can}\!\left(T(R^bT(R^a))\right)(-2)
 \right|
                         =\operatorname{Vol}(B_{a,b},u=0).
\]
This is a boundary evaluation with its remaining auxiliary cusp
complete. It is not a claim that this evaluation is already
the invariant of a closed knot.

## 4. Attachment to a larger original tree

The corresponding selected region in a circle tree is a
two-vertex pendant path. Its first vertex is an original
terminal vertex, of degree one and power \(a\). Its next vertex
has original degree two and power \(b\). Its third vertex is
outside the selected region and remains unfilled for now.
The original order of turns and disk attachments must be
the one in (1).

The degree-two requirement is literal: formula (7) contains one
child and one outgoing bare edge. An extra untouched incidence
cannot be omitted and then recovered by calling the same
formula a source for a higher-degree vertex.

One may choose finitely many disjoint selected pendant paths
of this kind. They may meet the same outside original circle.
Their full boundary maps and pure responses compose there by
the same annular gluing: the outside longitude stays one
primitive curve and its carrier occurs once. Replace their
exact source contractions by their proved boundary packets,
and retain every other original bare edge and filling trace.

For a fixed marked template and fixed selected \(a,b\) assignments
in the stated range, all the hypotheses of
[the general complex-phase filling theorem](research_long_fillings_complex_boundary_phase.md)
hold on the remaining variables. Its phase is the sum of
the selected \(S_{a,b}\) responses and the untouched edge phases.
Each remaining diagonal real curvature is strictly negative;
at the complete boundary the mixed derivatives vanish.
The whole-angle losses and thin-strip estimates are supplied
by the large-power turn theorem and the original edge theorem.

Therefore all independently sufficiently long fixed signed
fillings of the remaining original circles satisfy the usual
original-source asymptotic, with nonzero leading coefficient.
The marked cone completion uses (12), the untouched edge
periods, and each remaining carrier once. Its Schläfli anchor
is the sum of (14) and the untouched edge volumes. Whenever
the original parity and strand tracing give a knot, the
result is the original Kashaev volume identity for that knot
complement.

The threshold in this last paragraph may be stated as depending
on the fixed template and selected powers; the older assembly
theorem already suffices with that scope. No cofinite assignment
claim follows. In particular the infinitely many pairs with
short fixed \(b\) and unbounded \(|a|\) remain outside this
large-outer-power result. Arbitrary-depth analytic closure is
a separate assertion, even though the geometric composition
proposition itself can be iterated whenever its common-disk
small-branch hypothesis is supplied.

