# Reconstructing an interior maximum from one real variable

Research deduction, 6 November 2026. The stationary equations for the
first selected boundary coordinate eliminate three of its four moving
real variables. At a fixed height and a fixed actual reference, the
interior problem reduces to a scalar residual in the remaining private
coordinate, with at most two intermediate phase choices. This reduction
keeps the prescribed outgoing tangent and all original radii. It neither
proves that the maximum is interior nor proves the remaining curvature
inequality along it.

## 1. Fixed data and the four real stationary equations

Consider a fixed mixed open word of length at least three, whose first
selected coordinate has type four and whose adjoining ordinary block
has type \(3+\epsilon\), \(\epsilon\in\{0,1\}\). Fix its
original critical reference and the prescribed outgoing tangent \(p_*\).
The phase is the four-variable \(\mathcal F(e,s,z,b)\) from the
[height-envelope theorem](research_mixed_selected_boundary_height_envelope.md).
The objective is

\[
 f=\Re\mathcal F-\Re p_*\,(\Re b-\Re b_*),
 \qquad z=\Re z+ik.
 \tag{1}
\]

Subtracting \(-2\pi k\) for the factorial branch does not
change the horizontal stationary equations. The other heights remain
fixed at the actual reference values. Define

\[
 \begin{gathered}
 E=e^{-2\pi ie},\quad S_0=e^{-2\pi is},\quad
 Z=e^{-2\pi iz},\quad B=e^{-2\pi ib},\\
 r_e=|E|,\quad r_s=|S_0|,\quad r_b=|B|,
 \quad R=|Z|=e^{2\pi k},\qquad \tau=e^{2\Re p_*}>0,\\
 \nu(X)=|1-X|^2 .
 \end{gathered}
 \tag{2}
\]

Here \(r_e,r_s,r_b,\tau\) are fixed data, not independent
parameters that may be chosen anew during the optimization. They
retain their original reference relations. Only \(R\) changes
with the boundary height.

Let \(D(E)\) be the canonical square root of \(E(2-E)\)
specified by the [private-cap proof](research_mixed_private_cap_curvature_bound.md).
On the private rectangle it has positive real part and negative
imaginary part. Put

\[
                       C(E)=|1-D(E)|^4>0.
 \tag{3}
\]

**Lemma 1.** At a point where all four original real coordinates
are interior, the horizontal gradient of (1) vanishes if and only if

\[
 \begin{split}
 \nu(EZ)&=C(E),\\
 \nu(S_0Z)&=r_s^2\nu(Z)^3/C(E),\\
 \nu(S_0B)&=R^2\nu(S_0)^{2+\epsilon}/\nu(S_0Z),\\
 \nu(S_0B)&=\tau\nu(B)^{1+\epsilon/2}.
 \end{split}
 \tag{4}
\]

*Proof.* The exact real derivative formulas, with every chirp
retained, are

\[
 \begin{split}
 e^{\Re\mathcal F_e}
   &=\frac{|1-EZ|}{|1-D(E)|^2},\\
 e^{\Re\mathcal F_z}
   &=\frac{|1-EZ|\,|1-S_0Z|}{|S_0|\,|1-Z|^3},\\
 e^{\Re\mathcal F_s}
   &=\frac{|1-S_0Z|\,|1-S_0B|}
           {|Z|\,|1-S_0|^{2+\epsilon}},\\
 e^{\Re\mathcal F_b}
   &=\frac{|1-S_0B|}{|1-B|^{1+\epsilon/2}}.
 \end{split}
 \tag{5}
\]

The first uses the canonical identity
\((1-E)(W-E)=-(1-D(E))^2\), with
\(W=e^{-2\pi i u_c(e)}\). This is the same identity used
in Section 9 of the height-envelope proof. All displayed factors
are nonzero on the original strips. Setting the first three real
derivatives to zero and the last to \(\Re p_*\), then squaring
positive quantities, gives (4). Reversing these steps proves the
converse. No complex logarithmic equation is inferred from a modulus
equation; the assertion concerns the real gradient of (1). \(\square\)

## 2. The reconstruction

Fix a height \(k\) on the original displacement interval. Allow
\(E\) to run along the fixed-radius arc corresponding to
\(.3<\Re e<.4\) at its original private height. This is
one real parameter. The following formulas either reject that
parameter or produce at most two candidates.

First set

\[
 c_e=\frac{1+r_e^2R^2-C(E)}{2r_eR},\qquad
 P_e=r_eR\bigl(c_e+i\sqrt{1-c_e^2}\bigr),
 \qquad Z=P_e/E.
 \tag{6}
\]

Require \(-1<c_e<1\), take the positive square root, and
retain only candidates with the original \(z\) height and real
coordinate in its allowed interior interval. The sign in (6) is
forced: the proved bounds give
\(1/2<\Re(e+z)<1\), so \(EZ\) is in the upper
half-plane. Thus (6) is the unique candidate satisfying the first
equation of (4) in this summed-angle interval.

Next define

\[
 N_{sz}=r_s^2\nu(Z)^3/C(E),\qquad
 c_s=\frac{1+r_s^2R^2-N_{sz}}{2r_sR},\qquad
 P_s^{\pm}=r_sR\bigl(c_s\pm i\sqrt{1-c_s^2}\bigr),
 \qquad S_0^{\pm}=P_s^{\pm}/Z.
 \tag{7}
\]

Require \(-1\le c_s\le1\). Both signs must initially be
allowed, because the original real sum \(\Re(s+z)\) may lie
on either side of one half. At \(c_s=\pm1\) they coincide;
any violation of a regular strip is still rejected. Retain only
candidates with the prescribed \(s\) height, its original interior
real coordinate, and all known coordinate bounds. Each retained
candidate satisfies the second equation of (4).

For either retained \(S_0\), set

\[
 M=\frac{R^2\nu(S_0)^{2+\epsilon}}{N_{sz}},\qquad
 N_b=(M/\tau)^{2/(2+\epsilon)},\qquad
 c_b=\frac{1+r_b^2-N_b}{2r_b},\qquad
 B=r_b\bigl(c_b-i\sqrt{1-c_b^2}\bigr).
 \tag{8}
\]

The power in \(N_b\) is its unique positive real value.
Require

\[
                  \cos(.9\pi)<c_b<\cos(.44\pi).
 \tag{9}
\]

The original real interval \(.22<\Re b<.45\) then forces
the negative sign of the imaginary part in (8), and gives a unique
outgoing candidate. In particular \(\nu(B)=N_b\).
The remaining equation is one real residual:

\[
                      \mathcal R(E;R)=\nu(S_0B)-M=0.
 \tag{10}
\]

The notation allows the two retained signs from (7); each sign has
its own residual. Neither is discarded merely because the other
has a more convenient curvature.

## 3. Equivalence with the interior maximization problem

There is no additional interior stationary point hidden in the part
of the original box removed before proving concavity. The lower-\(s\)
marginal proof in Sections 7 and 12 of the height-envelope note
shows \(\Re\mathcal F_s>0\) throughout that strip, for every
choice of the other original target coordinates. Its lower endpoint
is \(.15\) for next type three and \(.125\) for next type four;
its upper endpoint is \(.2\). Consequently any interior stationary
point has \(\Re s>.2\). Strict concavity on the remaining
fixed box makes it its unique maximum. Since every original maximum
lies in that box, it is also the original maximum and inherits all
the coordinate bounds used in the reconstruction.

**Proposition 2.** For the fixed actual data and height above,
the interior stationary points of (1) in its original box, equivalently
its interior maximizers, are exactly the candidates
of (6)--(10) that retain the original coordinate strips and canonical
cap branch. There is at most one such point. If it exists, it is
the unique horizontal maximum in the original optimization problem.

*Proof.* An interior maximizer satisfies (4). The known
sign of the imaginary part of \(EZ\) forces (6), and the two
possibilities for the imaginary part of \(S_0Z\) give (7).
The last two equations of (4) force (8), with the sign fixed by
the original \(b\) interval. They also give (10). Thus no
interior maximizer is lost.

Conversely, (6) and (7) give the first two equations of (4).
Equation (10) gives the third. The definition of \(N_b\),
which is positive, then gives
\(\nu(S_0B)=M=\tau\nu(B)^{1+\epsilon/2}\), the fourth
equation. Lemma 1 proves stationarity.

The whole-reset theorem supplies a fixed box, with
\(\Re s\in[.2,.5]\), on which the objective is strictly
concave. All original maximizers lie in that box, and every retained
candidate lies in its interior in the relevant coordinates. A zero
gradient there is its unique global maximum. It is consequently
also the original maximum, and two retained candidates cannot
be distinct. This uniqueness does not apply to algebraic roots
discarded by the strip or branch conditions. \(\square\)

No existence assertion for an interior maximum is included.
If a maximum lies on an original face, the corresponding stationary
equation must be replaced by its one-sided condition and that real
coordinate fixed. The [active-face theorem](research_mixed_active_face_curvature_budget.md)
describes those cases and their exact almost-everywhere curvature.

## 4. Algebraic structure and remaining sign problem

The reconstruction uses only field operations, complex conjugation,
positive real square roots, and, when \(\epsilon=1\), one
positive real cube root. With the reference exponentials and their
moduli retained as fixed data, it is therefore real algebraic in
\(E,R\). For example, the last power can be recorded without
fractional exponents as

\[
              \tau^2 N_b^{2+\epsilon}=M^2,
                         \qquad N_b>0.
 \tag{11}
\]

The equations for every square root must retain their stated signs.
Clearing denominators requires their nonvanishing conditions; in
particular it must not introduce points with \(C(E)=0\),
\(N_{sz}=0\), or \(\nu(S_0)=0\). The reference radii and
\(\tau\) remain linked to the same actual reference, which can
be represented by the original rational endpoint parameter.

Thus the interior curvature test can be attempted on one scalar
residual with at most two intermediate phase choices, instead of
on independent boxes for four angles. The nonstationary example
in Section 8 of the [composition note](research_mixed_pair_curvature_composition.md)
is excluded by the retained stationary equations, rather than
requiring a new arbitrary cutoff.
This is a reduction of the constrained sign problem, not a proof
of that sign. It gives no new contribution to the finite sum and
does not remove the other boundary, face, or short-filling obligations.

## 5. A monotone residual on the next-three branch

There is now a sharper statement when the ordinary neighbor has type
three. The [summed-angle exclusions](research_mixed_factorial_positive_sum.md)
prove, at every factorial maximum in that case,
\[
 \frac12<\Re(s+z)<\frac{41}{50},\qquad
                         \frac12<\Re(s+b)<1.
 \tag{12}
\]
The [lower-face exclusion](research_mixed_factorial_lower_face_exclusion.md)
also makes \(z\) interior throughout the height displacement.
The [upper ordinary-face exclusion](research_mixed_factorial_upper_face_exclusion.md)
makes \(s\) interior as well. Thus \(e,s,z\) are interior
at every next-three factorial maximum; only \(b\) may be on
an original face.
Consequently only the positive-imaginary choice of \(P_s\) in
(7) can represent a maximum. Its remaining alternatives are an
interior outgoing coordinate or one of its two original endpoints.

Fix the height and reference data. Write
\(x=(e_R,s_R,z_R,b_R)\) and \(g=\nabla_x f\), with \(f\)
as in (1). On the common strict-concavity box, write
\[
 -\frac1\pi f_{xx}=A=
 \begin{pmatrix}
 E_0&0&b_e&0\\
 0&D_s&b_s&-j_R\\
 b_e&b_s&a_0&0\\
 0&-j_R&0&B_0
 \end{pmatrix}.
 \tag{13}
\]
Here \(D_s\) is a Hessian entry, not the marginal derivative
\(\Re\mathcal F_s\). Put
\[
 \begin{gathered}
 a_s=\Re\cot\pi s,\quad a_b=\Re\cot\pi b,\quad
 a_z=\Re\cot\pi z,\quad j_R=\Re\cot\pi(s+b),\\
 b_e=-\Re\cot\pi(e+z),\quad b_s=-\Re\cot\pi(s+z),\\
 D_s=2a_s+b_s-j_R,\quad B_0=a_b-j_R,\quad
 a_0=3a_z+b_e+b_s,\quad A_z=a_0-b_e^2/E_0,\\
 T_f=D_s-j_R^2/B_0,\qquad D_f=T_f-b_s^2/A_z.
 \tag{14}
\]
All these definitions agree with the
[active-face curvature calculation](research_mixed_active_face_curvature_budget.md).
On an interior neighborhood of an actual next-three maximum,
\(A\) is positive definite, \(a_s,a_b,a_z>0\),
\(b_e,b_s>0\), and \(E_0>b_e\). In particular
\[
          A_z=3a_z+b_s+b_e(1-b_e/E_0)>b_s,
                  \qquad D_f>0.
 \tag{15}
\]

Consider the three equations imposed by the reconstruction before
its final residual is set to zero:
\[
                       g_e=0,\qquad g_z=0,\qquad g_s=g_b.
 \tag{16}
\]
The last equality includes the original outgoing tangent in \(g_b\).
It is exactly the equation \(\nu(B)=N_b\) in (8): by (5),
\[
 g_s-g_b=\frac12\log\frac{\tau\nu(B)}{M}
 \qquad(\epsilon=0).
 \tag{17}
\]
Thus along (16) the natural residual is
\[
              h=g_s=g_b=\frac12\log\frac{\nu(S_0B)}{M}.
 \tag{18}
\]
Its zero is the required stationary point. The logarithm is real
because both numerator and denominator are positive.

**Proposition 3.** Near every interior next-three maximum,
(16) defines a unique smooth curve parametrized by \(e_R\).
Along this curve, wherever the above strict inequalities continue
to hold,
\[
 \begin{split}
 \frac{dz_R}{de_R}&=-\frac{E_0}{b_e}<0,\\
 \frac{ds_R}{de_R}&=\frac{E_0A_z}{b_e b_s}>0,\\
 \frac{db_R}{de_R}&=
 \frac{ds_R}{de_R}\,
       \frac{2a_s+b_s-b_s^2/A_z}{a_b}>0,\\
 -\frac1\pi\frac{dh}{de_R}
   &=\frac{E_0A_z}{b_e b_s}\frac{B_0}{a_b}D_f>0.
 \end{split}
 \tag{19}
\]
In particular the logarithmic residual is strictly decreasing on
each connected admissible branch. No stationary root on such a
branch is multiple.

*Proof.* The Jacobian of \((g_e,g_z,g_s-g_b)\) with respect
to \((s_R,z_R,b_R)\) is \(-\pi\) times
\[
 \begin{pmatrix}
 0&b_e&0\\
 b_s&a_0&0\\
 D_s+j_R&b_s&-(B_0+j_R)
 \end{pmatrix}.
 \tag{20}
\]
Its determinant is \(-\pi^3b_e b_s a_b\ne0\), since
\(B_0+j_R=a_b\). The implicit function theorem applies.
Differentiate (16), taking \(de_R/de_R=1\). The first two
rows give the first two identities in (19). Subtracting the
\(b\) row from the \(s\) row gives the third, using
\(D_s+j_R=2a_s+b_s\). Its sign follows from (15).

For the last identity, let a prime denote \(d/de_R\).
The \(b\) row of \(A x'\) is
\[
 \begin{split}
 -j_Rs_R'+B_0b_R'
 &=\frac{s_R'}{a_b}
       \{B_0D_s-j_R^2-B_0b_s^2/A_z\}\\
 &=s_R'\frac{B_0}{a_b}D_f.
 \end{split}
 \tag{21}
\]
Because \(g'=-\pi A x'\), this equals \(-h'/\pi\).
Every factor on the final right side is positive. \(\square\)

The unnormalized residual \(\mathcal R=\nu(S_0B)-M\) in
(10) obeys \(\mathcal R=M(e^{2h}-1)\). At a zero,
\(\mathcal R'=2Mh'<0\). Away from a zero its derivative
also contains \(M'(e^{2h}-1)\); no global monotonicity claim
for \(\mathcal R\) follows. Nor does Proposition 3 prove
that the admissible reconstruction domain is connected or that
it contains a zero.

## 6. The same residual with an outgoing coordinate fixed

If the maximum lies on an original outgoing face, fix
\(b_R=b_0\in\{.22,.45\}\), with its original height.
Do not impose \(g_b=0\). Near a point with \(s_R\) interior,
the two equations \(g_e=g_z=0\) still determine
\(s_R,z_R\) smoothly from \(e_R\), with the first two
derivatives in (19). Set \(h_a=g_s\) on this curve and
\[
                         D_a=D_s-b_s^2/A_z>0.
 \tag{22}
\]
The free-coordinate Hessian is positive definite, so
differentiating the \(s\) marginal gives
\[
             -\frac1\pi\frac{dh_a}{de_R}
                   =\frac{E_0A_z}{b_e b_s}D_a>0.
 \tag{23}
\]
The outgoing one-sided condition remains necessary:
\(g_b\le0\) at the lower face, and \(g_b\ge0\) at the
upper face. A zero of \(h_a\) satisfying this condition is the
unique constrained maximum, by strict concavity. No face is
selected merely to obtain a smaller response.

## 7. What a quantitative slope bound would prove

At an actual maximum with \(s_R\) interior, use the quantities
\(K_s,L_s\) of the active-face calculation. Since \(z_R\)
is now known to be interior, its exact height response is
\[
                       \frac{G''}{\pi}=K_s+\frac{L_s^2}{D},
 \tag{24}
\]
almost everywhere. Here \(D=D_f\) for free \(b_R\) and
\(D=D_a\) for an outgoing face. Put
\[
 \mu_b=\begin{cases} B_0/a_b,&b_R\text{ interior},\\
                      1,&b_R\text{ on an original face},
       \end{cases}
 \qquad \mathfrak h=\begin{cases}h,&b_R\text{ interior},\\
                         h_a,&b_R\text{ on an original face}.
          \end{cases}
 \tag{25}
\]
Equations (19) and (23) yield
\[
 \frac{G''}{\pi}
   =K_s+\frac{\pi\mu_b E_0A_z L_s^2}
                  {b_e b_s(-\partial_{e_R}\mathfrak h)}.
 \tag{26}
\]
Consequently, whenever \(K_s<6\), the desired bound
\(G''\le6\pi\) is equivalent to
\[
 -\partial_{e_R}\mathfrak h\ \ge
       \frac{\pi\mu_b E_0A_z}{b_e b_s}
                   \frac{L_s^2}{6-K_s}.
 \tag{27}
\]
The derivatives in (26)--(27) are at fixed height along the
specified reconstruction curve, not derivatives along the
height-varying maximizing path. This distinction is essential.

The sign \(-\partial_{e_R}\mathfrak h>0\) is proved above. Its
required quantitative size in (27), and a bound \(K_s<6\),
remain unproved on the full optimizing family. The face exclusions
show that (26), with the actual outgoing status, now applies
almost everywhere along the whole next-three factorial optimizing
path. Thus the result expresses the unresolved response in terms
of the original stationary equations and their slope; it does not
itself settle the selected-source estimate.

## 8. One scalar equation including the outgoing endpoints

The three outgoing cases can be combined without guessing which
one contains the maximum. Fix the height and use the positive
square roots in (6)--(7) to form a connected admissible curve
\((e_R,s_R(e_R),z_R(e_R))\) satisfying \(g_e=g_z=0\).
Retain the original strips, \(b_e,b_s>0\), and the strict
concavity assumptions used above. This is a statement on each
such curve, not a claim that the full parameter domain is connected.

For an outgoing real coordinate \(v\in[b_-,b_+]\), where
\(b_-=.22\) and \(b_+=.45\), put
\[
 Q_b(v)=1+r_b^2-2r_b\cos(2\pi v),\qquad m(e_R)=M(e_R)/\tau.
 \tag{28}
\]
The fixed height of \(b\) is encoded in \(r_b\).
Since \(0<v<1/2\), \(Q_b\) is strictly increasing.
Define the continuous clipped reconstruction
\[
 \widehat b_R(e_R)=
 \begin{cases}
 b_-,&m(e_R)\le Q_b(b_-),\\
 Q_b^{-1}(m(e_R)),&Q_b(b_-)<m(e_R)<Q_b(b_+),\\
 b_+,&m(e_R)\ge Q_b(b_+).
 \end{cases}
 \tag{29}
\]
Use its original imaginary part to define \(\widehat b\),
and let \(\widehat h(e_R)=g_s(e_R,s_R,z_R,\widehat b_R)\).

**Proposition 4.** Zeros of \(\widehat h\) on this admissible
curve are exactly the constrained maxima of the original problem
lying on the curve, including its outgoing faces. The function
\(\widehat h\) is continuous and strictly decreasing. As
\(e_R\) increases, \(\widehat b_R\) is nondecreasing and
can change status only from the lower face to the interior and
then to the upper face; either transition may be absent.

*Proof.* Along the curve the first two derivatives in (19) hold,
independently of the outgoing coordinate. Differentiating (17)
with that coordinate temporarily fixed gives
\[
 \frac{d\log M}{de_R}
   =2\pi\frac{ds_R}{de_R}
               \left(2a_s+b_s-\frac{b_s^2}{A_z}\right)>0.
 \tag{30}
\]
Thus \(m\) is strictly increasing. The lower and upper
thresholds in (29) are fixed, proving the assertion about
\(\widehat b_R\) and its possible transitions. The interior
inverse in (29) has nonzero derivative throughout the closed
outgoing interval, so the clipped function is locally Lipschitz.

At a zero of \(\widehat h\), the three internal derivatives
vanish. If \(\widehat b_R\) is interior, (17) gives
\(g_s-g_b=0\), hence \(g_b=0\). At the lower endpoint,
(17) and (29) give \(g_s-g_b\ge0\), so \(g_b\le0\).
At the upper endpoint they give \(g_b\ge0\). These are
exactly the original one-sided conditions. Strict concavity
therefore makes the point the constrained maximum. Conversely,
the internal stationarity and outgoing one-sided conditions of
any maximum force (29) and \(\widehat h=0\).

On the open part where (29) is interior, \(\widehat h=h\)
and (19) gives its strictly negative derivative. On each part
where it is on a face, \(\widehat h=h_a\) and (23) gives
the same sign. There are at most two transition points and the
function is continuous across them. It is consequently strictly
decreasing on the whole connected admissible curve. \(\square\)

This gives a single stationary equation for all remaining outgoing
statuses. It supplies neither the endpoint signs needed to prove
a zero exists on a particular reconstruction component, nor a
quantitative lower bound for its slope. The status-order statement
is for variation of \(e_R\) at fixed height. It is not a claim
that the maximizing outgoing coordinate is monotone as the height
changes.
