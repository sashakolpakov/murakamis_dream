# Active-face curvature and the original outgoing tangent

Research deduction, 6 November 2026. The full inverse-Hessian
curvature can overestimate the response of a constrained horizontal
maximizer. This note gives the exact almost-everywhere response on
its current original face, cancellation-sensitive scalar tests, and
a unique outgoing-phase reconstruction when the two ordinary
coordinates are interior. One simultaneous-face case is bounded
strictly below six. The other tests remain conditions, not established
inequalities on the entire optimizing family.

## 1. The response on the current face

Let \(f(x,k)\) be \(C^2\) on a neighborhood of a fixed compact box
\(\mathcal Q\) and a compact height interval \(I\). Assume
\(-f_{xx}\succeq\mu I\) there for some \(\mu>0\). Write
\[
 x(k)=\mathop{\rm argmax}_{x\in\mathcal Q}f(x,k),\qquad
 G(k)=f(x(k),k),\qquad
 A=-f_{xx}/\pi,\quad q=f_{xk}/\pi,\quad a_0=f_{kk}/\pi .
 \tag{1}
\]
All derivatives on the right are evaluated at \((x(k),k)\).
Let \(J(k)\) be the coordinates strictly inside their box intervals
and \(C(k)\) their complement.

**Lemma 1.** The optimizer is Lipschitz, \(G'\) is Lipschitz, and
for almost every interior height,
\[
 x'_C=0,\qquad x'_J=A_{JJ}^{-1}q_J,\qquad
                  G''/\pi=a_0+q_J^TA_{JJ}^{-1}q_J.
 \tag{2}
\]
The formula does not require strict complementarity or a fixed
active set on an interval.

*Proof.* The variational inequalities at two maximizing points,
strong concavity, and the uniform bound on \(f_{xk}\) give
\(\mu\|x(k)-x(l)\|\le L|k-l|\) for a fixed \(L\).
Uniqueness and the maximum rule give \(G'=f_k(x(k),k)\);
this is Lipschitz because \(f_k\) and \(x\) are Lipschitz.

At every height where \(x\) is differentiable, a coordinate lying
on a fixed box endpoint has derivative zero: that coordinate
function has a local minimum or maximum there. An interior
coordinate remains interior in a neighborhood by continuity.
Its equation \(f_{x_j}=0\) can therefore be differentiated at
this height, giving
\(-A_{JJ}x'_J+q_J=0\), since \(x'_C=0\).
The principal matrix \(A_{JJ}\) is positive definite.
Differentiating \(G'=f_k(x(k),k)\) proves (2) at almost every
height. Empty free-coordinate sets have the evident zero response.
\(\square\)

There is an exact expression for the amount discarded by using
the full inverse matrix. If both index sets are nonempty, put
\[
 D_C=A_{CC}-A_{CJ}A_{JJ}^{-1}A_{JC},\qquad
 v_C=q_C-A_{CJ}A_{JJ}^{-1}q_J .
 \tag{3}
\]
Then \(D_C\succ0\), and the real block inverse identity gives
\[
 \bigl(a_0+q^TA^{-1}q\bigr)-G''/\pi
                         =v_C^TD_C^{-1}v_C\ge0
 \quad\hbox{almost everywhere}.
 \tag{4}
\]
Thus a boundary coordinate cannot simply be assigned its
unconstrained response. Nor can a coordinate be declared fixed
merely because it lies near a face.

## 2. Actual next-three factorial coordinates

Apply the lemma to the original next-type-three factorial problem
of the [height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The first selected coordinate has type four and its next vertex
is an ordinary type-three vertex of a fixed open word with
\(m\ge3\); no two-vertex endpoint substitution is made.
The real variables are \((e_R,s_R,z_R,b_R)\); the private heights
and the actual outgoing affine marginal are fixed. With that
marginal denoted \(p_*\), use
\[
 f=\Re\mathcal F(e,s,z,b)-\Re p_*(b_R-b_{*,R}),\qquad
 G(k)=\max f,\qquad z=z_R+ik,\qquad c\le k\le7/500 .
 \tag{5}
\]
Here \(c>-.07\), and \(\mathcal F\) is the original phase,
including its chirps. The factorial term \(-2\pi k\) can be
subtracted after this maximization; it has no second derivative.
The reference equations give \(G(c)=M\) and \(G'(c)=0\).

Section 12 of the height-envelope proof establishes the common
fixed concavity box. Its artificial lower side \(s_R=.2\) is
never attained, because the original marginal exclusion gives
\(s_R>.2\). The other proved coordinate bounds are likewise
consequences of maximization, not new active constraints.
Relative to the original box, the only possibilities are:

- \(e_R\) is always interior, since \(.3<e_R<.4\) inside
  the original private interval \([.27,.49]\).
- \(s_R\) is interior or on its original upper face \(s_R=.5\).
- \(z_R\) is interior or on its original lower face \(z_R=.22\);
  the whole-path upper bound is \(z_R<3/8<.45\).
- \(b_R\) is interior or on either original endpoint \(.22,.45\).

Before the further marginal exclusions, these give twelve original
face descriptions, or eight distinct patterns of free coordinates.
No artificial face such as \(z_R=1/3\) or
\(s_R+z_R=.82\) is used in Lemma 1.

The subsequent [lower first-coordinate exclusion](research_mixed_factorial_lower_face_exclusion.md)
and [upper ordinary-coordinate exclusion](research_mixed_factorial_upper_face_exclusion.md)
now show that \(e_R,s_R,z_R\) are interior throughout this
next-three factorial application. Only the status of \(b_R\)
can change. The general response formulas below remain valid, but
only their case with \(s_R,z_R\) free is attained here.

For clarity, the original first-order necessary conditions are
\[
 \begin{array}{c|c}
 \text{coordinate status}&\text{necessary real derivative}\\ \hline
 s_R\text{ interior}&\Re\mathcal F_s=0\\
 s_R=.5&\Re\mathcal F_s\ge0\\
 z_R\text{ interior}&\Re\mathcal F_z=0\\
 z_R=.22&\Re\mathcal F_z\le0\\
 b_R\text{ interior}&\Re(\mathcal F_b-p_*)=0\\
 b_R=.22&\Re(\mathcal F_b-p_*)\le0\\
 b_R=.45&\Re(\mathcal F_b-p_*)\ge0 .
 \end{array}
 \tag{6}
\]
Also \(\Re\mathcal F_e=0\). These conditions retain the
actual prescribed tangent; arbitrary points satisfying only the
coordinate bounds are not identified with maximizers.

## 3. Exact scalar responses and cancellation

Use the normalized real Hessian and its relevant imaginary column
from the [pair-curvature composition proof](research_mixed_pair_curvature_composition.md).
In the order \((e,s,z,b)\), write
\[
 A=
 \begin{pmatrix}
 E&0&b_e&0\\
 0&D_s&b_s&-j_R\\
 b_e&b_s&a_0&0\\
 0&-j_R&0&B_0
 \end{pmatrix},
 \qquad q=(q_e,q_s,q_z,0)^T .
 \tag{7}
\]
In this section \(A\) is the full matrix in (1). The scalar
\(D_s\) is its \(ss\) entry, not a phase derivative.
Explicitly, if \(d=\cot\pi(e+z)\),
\(h=\cot\pi(s+z)\), and \(j=\cot\pi(s+b)\), then
\[
 \begin{split}
 E&=\Re\sigma+\Re\cot\pi e-\Re d,\qquad
          \sigma=-S''(e)/\pi,\\
 D_s&=\Re\{2\cot\pi s-h-j\},\qquad
 B_0=\Re\{\cot\pi b-j\},\qquad j_R=\Re j,\\
 b_e&=-\Re d,\quad b_s=-\Re h,\quad
 a_0=\Re\{3\cot\pi z-d-h\},\\
 q_e&=1-\Im d,\quad q_s=-1-\Im h,\quad
 q_z=\Im\{3\cot\pi z-d-h\}-1 .
 \end{split}
 \tag{8}
\]
The private imaginary diagonal does not occur in this column.
The full real matrix is positive definite. Define
\[
 \begin{split}
 A_z&=a_0-b_e^2/E>0,\qquad
 Q_z=q_z-b_eq_e/E,\qquad R_z=a_0+q_e^2/E,\\
 T&=
 \begin{cases}
 D_s-j_R^2/B_0,& b_R\text{ interior},\\
 D_s,&b_R\text{ on an original endpoint},
 \end{cases}\\
 K_s&=R_z+Q_z^2/A_z,\qquad
 L_s=q_s-b_sQ_z/A_z,\qquad
 D=T-b_s^2/A_z>0 .
 \end{split}
 \tag{9}
\]
Here \(K_s\) denotes the response when \(s_R\) is fixed, not
a derivative with respect to \(s\). All expressions in (9) are
evaluated at the current original maximizing point.

**Proposition 2.** Almost everywhere, the exact dimensionless
curvature from Lemma 1 is given by this table:
\[
 \begin{array}{c|c|c}
 &s_R\text{ interior}&s_R=.5\\ \hline
 z_R\text{ interior}&K_s+L_s^2/D&K_s\\
 z_R=.22&R_z+q_s^2/T&R_z .
 \end{array}
 \tag{10}
\]
If \(s_R=.5\), the status of \(b_R\) has no effect on the
response, because its relevant imaginary-column entry is zero.

*Proof.* Eliminate the always-free \(e_R\) coordinate.
It contributes \(q_e^2/E\) and changes the \(zz\) entry and
the \(z\) component of the column to \(A_z,Q_z\).
If \(b_R\) is free, its zero column entry makes its elimination
change only the \(ss\) entry, from \(D_s\) to \(T\).
If it is fixed, that entry remains \(D_s\).

When \(s_R,z_R\) are both free, eliminate \(z_R\) in the
remaining real two by two matrix. Its response is exactly
\[
 \frac{Q_z^2}{A_z}
       +\frac{(q_s-b_sQ_z/A_z)^2}{T-b_s^2/A_z}.
 \tag{11}
\]
This gives the first entry of (10). Deleting the actual fixed
coordinates gives the other three entries. If \(s_R\) is fixed,
the free \(b_R\) block has zero right-hand side and no connection
to \(z_R\), so it contributes nothing. \(\square\)

The residual \(L_s\) retains the sign and cancellation of the
two contributions. Replacing it by
\(|q_s|+|b_sQ_z/A_z|\) would lose that information.
In particular, if \(K_s<6\), the interior \(s,z\) case obeys
the exact equivalence
\[
 \frac{G''}{\pi}\le6
 \quad\Longleftrightarrow\quad
 T\ge \frac{b_s^2}{A_z}+\frac{L_s^2}{6-K_s}.
 \tag{12}
\]
Without assuming \(K_s<6\), its division-free equivalent is
\[
                 \begin{pmatrix}D&L_s\\L_s&6-K_s\end{pmatrix}
                         \succeq0 .
 \tag{13}
\]
For a fixed \(z_R\) and free \(s_R\), the corresponding exact
test is \(R_z+q_s^2/T\le6\). When \(R_z<6\), it is
\(T\ge q_s^2/(6-R_z)\).

The gain from an actually fixed outgoing coordinate is also exact.
For fixed point data with \(s,z\) free, put
\(T_f=D_s-j_R^2/B_0\), \(T_a=D_s\).
Then the hypothetical full response minus the response with
the outgoing coordinate fixed is
\[
 L_s^2\,
 \frac{j_R^2/B_0}
 {(T_f-b_s^2/A_z)(T_a-b_s^2/A_z)}\ge0 .
 \tag{14}
\]
Formula (14) compares responses at the same point; it does not
assert that the optimizers for two different constrained problems
coincide.

## 4. One face case is already below six

The [whole-path direct-curvature bound](research_mixed_positive_height_factorial_bounds.md),
the [private cap bound](research_mixed_private_cap_curvature_bound.md),
and the [next-three cotangent signs](research_mixed_factorial_next_three_sum_bound.md)
give
\[
 0<a_0<299/60,\qquad E>163/90+b_e>163/90,\qquad
                         0<q_e<1,\quad -2<q_s<0 .
 \tag{15}
\]
Consequently, whenever both \(s_R=.5\) and \(z_R=.22\),
their actual response satisfies
\[
 \frac{G''}{\pi}=R_z
 <\frac{299}{60}+\frac{90}{163}
 =6-\frac{4543}{9780}<6
 \quad\hbox{almost everywhere on that face set}.
 \tag{16}
\]
This is a valid conditional bound for that face. The later
exclusions cited in Section 2 show that the face is not attained
in the present next-three factorial problem. The bound consequently
does not discharge a remaining case of that problem.

## 5. Eliminating an interior outgoing phase

The scalar threshold (12) can retain the actual outgoing tangent
without treating the phase of \(b\) as an independent box variable.
Suppose \(s_R,b_R\) are both interior. Set
\[
 S_0=e^{-2\pi is},\quad Z=e^{-2\pi iz},\quad B=e^{-2\pi ib},
 \quad r_b=|B|,\quad \tau=e^{2\Re p_*}>0,\quad
 M_s=\frac{|Z|^2|1-S_0|^4}{|1-S_0Z|^2}.
 \tag{17}
\]
The radii \(r_b,|S_0|\) and the constant \(\tau\) have their
original reference values, while \(|Z|=e^{2\pi k}\) uses the
current first height. The original regular strips
keep every displayed denominator nonzero. The real stationarity
equations, with the original chirp in \(\mathcal F_s\), are
\[
 |1-S_0B|^2=M_s,\qquad
 \frac{|1-S_0B|^2}{|1-B|^2}=\tau .
 \tag{18}
\]
Thus
\[
 C_b=\frac{1+r_b^2-M_s/\tau}{2r_b},\qquad
              B=r_b\bigl(C_b-i\sqrt{1-C_b^2}\bigr).
 \tag{19}
\]
The square root is positive: the original real interval
\(.22<b_R<.45\) has \(0<2\pi b_R<\pi\). There is at most
one candidate in this interval. It must satisfy
\[
 \cos(.9\pi)<C_b<\cos(.44\pi),\qquad
                         |1-S_0B|^2=M_s .
 \tag{20}
\]
Conversely, a candidate satisfying (19)--(20) and the prescribed
radius has exactly the two real gradient equations in (18).
This does not replace any original imaginary gradient equation,
canonical endpoint branch, or actual reference constraint.

For this candidate the entries \(B_0,j_R,T_f\) in (8)--(9)
are explicit algebraic functions of \(S_0,Z,r_b,\tau\), using
\(\cot\pi v=i(1+e^{-2\pi iv})/(1-e^{-2\pi iv})\).
The outgoing tangent has therefore removed an independent phase
from the interior stiffness test. If \(b_R\) is an original
endpoint, its exponential is already fixed, and the appropriate
inequality in (6) must instead be retained.

## 6. An integrated alternative to a pointwise bound

Let \(\mathcal K_{\rm face}(k)\) be the exact entry in (10).
The reference initialization and absolute continuity proved above
give
\[
 G(H)-M=\pi\int_c^H(H-k)\mathcal K_{\rm face}(k)\,dk .
 \tag{21}
\]
In particular, the weaker weighted condition
\[
 \int_c^H(H-k)\bigl(\mathcal K_{\rm face}(k)-6\bigr)\,dk\le0
 \tag{22}
\]
suffices for \(G(H)-M\le3\pi(H-c)^2\), the bound used in
the common-branch budget. It does not require a pointwise bound
at heights with a compensating deficit elsewhere.

Equivalently, the exact nonnegative difference in (4) can be
subtracted inside the integral of the full inverse-matrix
curvature. This requires the actual active set, not a chosen
face with a favorable response. The initialization, the fixed
reference tangent in (17), and the phase's original logarithmic
branch all remain in force.

The only numerical margin proved in this note is (16), on a face
subsequently excluded. The scalar or integrated inequality for the
actual remaining case is unproved on the full optimizing family.
Sections 5--7 of the
[stationary reconstruction](research_mixed_interior_optimizer_reconstruction.md)
now express its denominator as an exact positive multiple of a
monotone scalar residual's slope. A quantitative lower bound for
that slope is still needed. Even if it is established, the finite
Fourier alternatives, contour joins, endpoints, and other unhandled
source currents remain separate obligations.
