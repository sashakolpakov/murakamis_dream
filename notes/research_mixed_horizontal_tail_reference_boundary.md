# A boundary principle for horizontal tail deficits

Research deduction, 5 November 2026. A positive maximum of the
horizontal supporting-plane deficit cannot occur at an interior
original reference. This holds simultaneously for every complete
real-tail row and every horizontal target. It reduces the reference
domain to the ordinary boundary of its input bidisk, where one input
is on a circle and the other remains in its disk. It does not reduce
that boundary to the two-circle distinguished boundary, and it does
not establish a sign there.

## 1. A general reference maximum lemma

Let \(Z=U+iH\in\mathbb C^d\), and let \(f(Z)\) be a real
\(C^2\) function on an open reference domain. Fix a constant
\(\kappa_0\ge0\) and suppose
\[
                -D_U^2 f(Z)\succ2\kappa_0 I.
 \tag{1}
\]
Let \(X\) range over a fixed compact real target set, and let
\(u\) range over a fixed compact row set. Suppose the real rate
\(R_u(X,H)\) is continuous in all its variables and depends on
the reference only through its height vector \(H\). Define
\[
 \begin{split}
 B_Z(X)&=f(Z)+\nabla_U f(Z)\mathbin{\cdot}(X-U)
                         -\kappa_0\|X-U\|^2,\\
 D(Z,X,u)&=R_u(X,H)-B_Z(X).
 \end{split}
 \tag{2}
\]
Assume a matched-reference gap
\[
                         R_u(U,H)-f(Z)\le-g
 \tag{3}
\]
for some fixed \(g>0\), whenever the target \(X=U\) is
included. No differentiability of \(R\) in height or row is needed.

**Lemma 1.** An interior reference point cannot realize a joint maximum
of \(D\) whose value is greater than \(-g\).

*Proof.* At such a joint maximum hold the maximizing \(X,u\)
and the reference height \(H\) fixed. All sufficiently small real
reference changes remain allowed. The cancellation of the two first
derivatives of \(f\) in (2) gives
\[
 \nabla_U D
      =\{-D_U^2f(Z)-2\kappa_0 I\}(X-U).
 \tag{4}
\]
The gradient must vanish. The matrix in braces is positive definite
by (1), so \(X=U\). Equation (3) then bounds the attained
value by \(-g\), a contradiction. If \(X=U\) is not in
the target set, the same conclusion already rules out an interior
maximum. The argument never differentiates a maximizing row or a
maximizing target. \(\square\)

The lemma also applies to a reference domain parametrized by a local
open coordinate map. Suppose \(K\) is a compact parameter set,
\(Z(\lambda)\) is continuous on \(K\), and every interior
parameter point has a neighborhood mapped locally invertibly to an
open reference neighborhood. Suppose (1)--(3) hold there and the
same functions extend continuously to the full compact family.
Compactness gives a joint maximum, and Lemma 1 implies
\[
 \max_{\lambda\in K,\,X,\,u}D(Z(\lambda),X,u)
 \le\max\left\{-g,
        \max_{\lambda\in\partial K,\,X,\,u}D(Z(\lambda),X,u)\right\}.
 \tag{5}
\]
Global injectivity of \(Z\) is not required: the contradiction
at an interior maximizer uses only its local inverse.

## 2. The complete original conditional tail

Fix one of the six original own/external-type families in the
[reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md).
Its two external inputs range over the closed product
\(K=P_{3+\alpha}\times P_{3+\beta}\). In one orientation,
write its original two-leg solution as \((s,t)\) and its
conditional retained arguments as
\[
                 Z=(a,b)=(A,t(A,B)).
 \tag{6}
\]
The other orientation swaps the two external inputs and the two
original roots. All three conditional arguments stay in the original
rectangle \(Q=[.23,.45]+i[-.12,.12]\), on their zero lifts.
The own conditional flag is \(\epsilon\); let \(\eta\)
be the type flag of the first retained coordinate.

Use the original allocated critical phase
\[
 \phi(a,b)=Q_\epsilon(s;a,b)
                    -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \qquad f=\Re\phi.
 \tag{7}
\]
The original conditional source theorem proves
\(t_B\ne0\). Consequently the derivative of
\((A,B)\mapsto(A,t(A,B))\) is invertible. Its local
inverse gives the open reference coordinates required by Lemma 1.
The original branches glue on the conditional image as in Section 4
of that theorem; no new root or continuation is selected.

The allocated pair form and its complex Schur complement give
\[
                       -D_U^2 f\succ(\pi/8)I_2.
 \tag{8}
\]
This is the same full-allocation estimate proved in Section 3 of the
[horizontal completion reduction](research_mixed_first_collar_horizontal_completion.md),
using the original pair estimate on \(Q^2\). In particular it
applies throughout these conditional images, not just at a single
reference point.

Take
\[
 \begin{split}
 X=(x,z)&\in I^2,\qquad I=[11/50,9/20],\\
 u&\in[0,3/20]\cup[49/100,1],\qquad
 \kappa_0=1/2500000.
 \end{split}
 \tag{9}
\]
For \(H=(h_a,h_b)\), the entire allocated real-row rate is
\[
 \begin{split}
 R_u(X,H)={}&
  \int_0^u\log|1-e^{-2\pi i(x+ih_a+v)}|\,dv
 +\int_0^u\log|1-e^{-2\pi i(z+ih_b+v)}|\,dv\\
 &-(2+\epsilon)J(u)-2\pi u h_a
       -\frac\eta2\Re g(x+ih_a)-\frac\epsilon2\Re g(z+ih_b).
 \end{split}
 \tag{10}
\]
This retains the asymmetric chirp, both Fourier halfweight
allocations, all wrapped rows and both endpoints. Integrable zeros
are interpreted by continuity. The original zero-safe entropy bounds
give precisely the needed continuity on this compact set, including
zero heights. Most importantly, (10) depends on the reference real
coordinates \(U\) only through the separately chosen target
\(X\): when \(X,H,u\) are fixed it has no \(U\)-dependence.

At matched targets \(X=U\), the completed reduced-disk proof gives
\[
                         R_u(U,H)-f(Z)<-1/1000
                  \quad\text{for every row in (9)}.
 \tag{11}
\]
This uses the actual entropy comparison, not a deduction from
cancellation in the finite kernel. On the distinguished boundary,
the old left-tail monotonicity, both cut inequalities, all four
revived-endpoint branches and the right-tail shape estimate bound
every real row. The separately subharmonic raw-row rate minus the
selected harmonic action then transfers that matched gap to the
whole input product, as proved in Section 4 of the source theorem.
The allocated outer terms in (7) and (10) cancel from this matched
comparison. Thus it is exactly the old gap, with no tolerance spent
again.

For the present lemma the factorial allocations may be treated as
the displayed formal rate functions on the full input product.
Their eventual use as physical unselected Fourier upper rates is
restricted to the actual negative type-four reference heights, as
in the asymmetric-contour theorem. The lemma does not extend that
physical branch assignment to other heights.
Likewise \(B_Z\) is the algebraic expression (2) on this auxiliary
reference product. Its interpretation as an already proved central
zero-mode upper bound is used only on the actual-reference subfamily
covered by the asymmetric-contour theorem.

## 3. Reduction to the ordinary boundary faces

Define \(D\) by (2), using (7), (9) and (10). Equation (8)
dominates \(2\kappa_0=1/1250000\), and (11) supplies the
matched gap. Lemma 1 therefore proves
\[
 \boxed{
 \max_{K\times I^2\times([0,3/20]\cup[49/100,1])}D
 \le\max\left\{-\frac1{1000},\quad
       \max_{\partial K\times I^2\times([0,3/20]\cup[49/100,1])}D
                         \right\}.}
 \tag{12}
\]
The boundary here is
\[
 \partial K=(\partial P_{3+\alpha}\times P_{3+\beta})
             \cup(P_{3+\alpha}\times\partial P_{3+\beta}).
 \tag{13}
\]
Each face has three real reference parameters. It includes points
where the other input is strictly inside its disk. The old 4,409
cells cover the two-circle distinguished boundary; they do not by
themselves cover (13).

Consequently any nonnegative allowed deficit \(\delta\) proved
uniformly on (13), for all horizontal targets and all tail rows,
holds on the whole original reduced input product. The endpoint
\(u=1\) has the explicit scalar target optimization in the
[revived-endpoint lemma](research_mixed_horizontal_revived_endpoint.md).
The two real cuts have their separate exact scalar optimization,
and the remaining right rows retain every stationary candidate from
the asymmetric-contour theorem. None is discarded by (12).

This is a reference-domain reduction, not a new numerical bound on
the boundary faces. No positivity of a finite matrix, nonzero packet
at a new horizontal target, actual-word realization of independent
inputs, or full open-source noncancellation is asserted.
