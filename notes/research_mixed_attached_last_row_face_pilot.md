# Design of one bounded attached-input last-row pilot

Research pilot specification, 5 November 2026. This is one face of
the [actual-reference domain reduction](research_mixed_actual_last_row_reference_domains.md),
not a test of every face or every type. Its acceptance inequalities
are specified below before execution. No uniform last-row sign is
asserted here.

## 1. Exactly one three-parameter face

The own vertex has type three. In the original external order use
\((c,a)\), with \(c\in A_3\) and \(a\in A_4\). The
fixed face and its unit-cube parametrization are
\[
 \begin{split}
 c(t)&=\frac{391}{1000}
             +i\left(-\frac9{125}+\frac{93}{1000}t\right),\\
 a(\rho,\theta)&=\frac3{10}-\frac{13i}{250}
             +\frac3{50}\rho e^{2\pi i\theta},
        \qquad(t,\rho,\theta)\in[0,1]^3,\\
 &\frac{123}{500}\le\Re a\le\frac7{20},\qquad
       -\frac{27}{250}\le\Im a\le-\frac1{50}.
 \end{split}
 \tag{1}
\]
The last line is an exact clipping constraint. The whole segment
\(c(t)\) lies inside \(P_3\): its largest squared distance
from \(.35-.01i\) is \(.041^2+.062^2)<.083^2\).
The second parametrization stays in \(P_4\), including its center
at \(\rho=0\). Redundant angle values at the center cause no
coverage loss.

The original coupled zero-lift roots are \((r_0,r_1)\), in the
external order \((c,a)\). Both conditional orientations are tested:
\[
 (s;A,B)=(r_0;c,r_1),\quad\eta=0;
 \qquad(s;A,B)=(r_1;a,r_0),\quad\eta=1.
 \tag{2}
\]
The own flag is always \(\epsilon=0\). The external type-four
flag in the first orientation does not turn its own denominator or
its second halfweight into type four.

## 2. The exact deficit and all carrier branches

For either orientation let
\[
 \begin{split}
 \phi(A,B)&=Q_0(s;A,B)-(1+\eta/2)g(A)-g(B),\qquad
 P=(\phi_A,\phi_B),\quad H=\phi'',\\
 R_{vw}(x,z)&=-2\pi v\Im A+2\pi w\Im B
                     -\frac\eta2\Re g(x+i\Im A),
                    \qquad v,w\in\{0,1\},\\
 D_{vw}&=R_{vw}-\Re\phi-\Re P\mathbin{\cdot}d
                   +\kappa_0\|d\|^2,\qquad
 d=(x-\Re A,z-\Re B),\quad\kappa_0=1/2500000.
 \end{split}
 \tag{3}
\]
The complete last-row envelope is the maximum over all four
\((v,w)\). Each branch is tested separately, including at zero
height. The original dilogarithmic constant, first-argument chirp,
and type-four factorial halfweight remain in (3).

Put \(W=Hd\), and define the row's holomorphic marginal vector
at the target by
\[
 P^{\mathrm{row}}=
       (2\pi iv-\tfrac\eta2 g'(x+i\Im A),\ -2\pi iw).
 \tag{4}
\]
Holding \(x,z,v,w\) fixed, exact differentiation gives
\[
 D_U=-\Re W-2\kappa_0d,\qquad
 D_H=\Im(P-P^{\mathrm{row}}+W),
 \quad U=(\Re A,\Re B),\ H_{\rm ht}=(\Im A,\Im B).
 \tag{5}
\]
In (5), \(D_H\) means differentiation in the height vector
\(H_{\rm ht}\), not the Hessian matrix \(H\). The two
original root responses supply the derivatives of \((A,B)\)
with respect to the three parameters in (1). Contracting these
responses with (5) gives interval bounds on each parameter
derivative. Thus a midpoint value plus the sum of derivative
absolute bounds times the exact half-widths controls the whole
parameter box. No external or retained leg is varied independently
of the coupled map in this calculation.

For completeness the conditional Hessian is evaluated by the exact
complex Schur formula. Set
\[
 \begin{split}
 q&=g''(s+A)+g''(s+B)-2g''(s),\qquad
 \ell=(g''(s+A)+2\pi i,g''(s+B)),\\
 H_{ij}&=\operatorname{diag}
 \bigl(g''(s+A)-(1+\eta/2)g''(A),
       g''(s+B)-g''(B)\bigr)_{ij}-\ell_i\ell_j/q.
 \end{split}
 \tag{6}
\]
Uncertain interval divisions are rejected; floating roots or
responses cannot accept a box.

## 3. Exact control of every target real coordinate

The target square is \(I^2\), \(I=[11/50,9/20]\).
For \(\eta=0\), (3) is convex in each target coordinate,
so its four corners give its exact maximum. For \(\eta=1\),
the second target coordinate remains convex and its two endpoints
suffice. The first target coordinate satisfies
\[
 \frac{\partial^2D_{vw}}{\partial x^2}
       <-\frac{9\pi}{140}+2\kappa_0<-\frac15,
 \tag{7}
\]
by the whole-plateau factorial curvature bound in the
[revived-endpoint lemma](research_mixed_horizontal_revived_endpoint.md).
The inequality applies on the whole old height rectangle; it does
not require a successful clipping test at an interior midpoint.

Choose any rational trial \(x_0\in I\), and enclose the
target slope there by \(\beta\). For \(L\ge0\), define
\[
 J(\beta,L)=\max_{0\le d\le L}
                 \{\beta d-d^2/10\}.
 \tag{8}
\]
It is zero if \(\beta\le0\), equals
\(\beta L-L^2/10\) if \(\beta\ge L/5\), and equals
\(5\beta^2/2\) otherwise. The rigorous target gain is at most
\[
 \max\{0,J(\sup\beta,9/20-x_0),
                  J(\sup(-\beta),x_0-11/50)\}.
 \tag{9}
\]
The midpoint-plus-derivative bound from (5), plus (9), therefore
controls all targets. A floating clipped-cosine calculation may
propose \(x_0\); only its rational value and the outward bounds
(7)--(9) enter acceptance.

## 4. Bounded execution and what its result would mean

The proposed driver imports the original affine Newton primitive,
identifies its branch by the same original-log midpoint witness,
and uses its validated coupled root response. Every retained box
must pass that whole-box test before (3)--(9) are considered.

A parameter box is discarded only when its entire type-four input
enclosure is strictly outside one of the four clipping inequalities
in (1). A boundary-straddling box is retained. Its estimates may
cover a larger part of \(P_4\), which is conservative. Exact
dyadic splitting, explicit pending boxes and a rational volume
identity account for every part of the starting cube, including
excluded and unfinished boxes.

The limits are **511 visited boxes and 30 seconds**, including setup.
There is no option to increase them in this pilot. It may stop
earlier at an outward positive trial value whose midpoint satisfies
all clipping constraints. Such a point would concern this auxiliary
face, not an actual-word realization. An exhausted budget is reported
as incomplete, and a complete negative result would apply only to
the face (1), both orientations (2), all four carrier branches and
the full target square. It would not cover the other clipping chords,
circle pieces, types or roles in the domain reduction.

Execution is to follow the separate scope and code review. This
specification does not report a numerical result.
