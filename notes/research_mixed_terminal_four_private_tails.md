# The coherent private-index tails of the type-four terminal source

Research deduction, 5 November 2026. Both private-index tails reduce
to the two private faces of the broad rectangle. The Newton sum is
kept complete throughout this reduction. Its uniform whole-period
upper bound makes the reduction valid even in the private endpoint
layers, while an exact product identity retains the physical support
wall and its off-grid continuation. The resulting face comparisons
are explicit hypotheses; no calibrated gap is asserted here.

## 1. Keep the whole Newton sum before deforming the transform index

Use the original conventions and exact triple source of
[the type-four joint-source note](research_mixed_terminal_four_joint_source.md).
Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi it}\), and
\[
 a=y+iH,\quad .22\le y\le.45,\quad |H|\le.12,
 \qquad
 t=x+ih,\quad .15\le x\le.50,\quad |h|\le.12.
 \tag{1}
\]
The exact product identity
\[
 P_jp_i(r^j)=P_ip_j(r^i)
 \tag{2}
\]
holds for every \(0\le i,j<N\). Both sides are \(P_{i+j}\)
below the wall \(i+j=N\), and both vanish at and beyond the wall.
After summing the entire Newton variable in the triple source, the
whole terminal polynomial therefore has the exact representation
\[
 \mathcal V_{1,N}(w,X)
 =\sum_{i,j=0}^{N-1}
    \frac{X^{-i}p_i(X)}{P_i^2}\,
    \frac{p_j(r^i)\mathcal H_N(w,r^{-j})}{P_j^2}.
 \tag{3}
\]
The full square in (3) retains the literal zero products. In particular
it is not a replacement of the finite support by nonzero terms.

For a fixed physical private index \(e=j/N\), interpolate only
the transform index by
\[
 \mathcal A_N(a,t)=e^{2\pi iNat}
       \frac{\mathfrak P_N(a+t)}
            {\mathfrak P_N(a)\mathfrak P_N(t)^2},
 \qquad
 \mathcal B_{j,N}(a,t,w)=
    \mathcal A_N(a,t)
       \frac{p_j(Y)\mathcal H_N(w,r^{-j})}{P_j^2}.
 \tag{4}
\]
The marked factorial is exactly the prescribed one. At \(t=i/N\),
(4) is the summand of (3). The polynomial \(p_j(Y)\) remains
exact, including all of its zeros. The interpolation is holomorphic
on a fixed neighborhood of (1): its only factorial arguments are
\(a,t,a+t\), whose real parts stay in their regular strips.
In particular this statement does not require \(\Re(e+t)<1\).
No factorial interpolation across that support wall is used.

Write
\[
 \begin{split}
 G_a(t)&=g(a+t)-g(a)-2g(t)+2\pi iat,\\
 I_t(e)&=\int_0^e\log|1-e^{-2\pi i(t+s)}|\,ds,\\
 \lambda(e)&=\Re S(e),\qquad
 R(e,t)=\lambda(e)-J(e)+I_t(e).
 \end{split}
 \tag{5}
\]
The original real-index endpoint action is \(S\). Its endpoint
values in (5) mean the continuous extension
\(\lambda=h-J\), where
\(h(e)=\lambda(e)+J(e)\) is the whole-period endpoint rate.
Thus \(\lambda(0)=\lambda(1)=0\).

For every \(\eta>0\), a sufficiently small fixed ordinary-color
disk and constants \(C,A\) give
\[
 |\partial_w^k\mathcal B_{j,N}(a,t,w)|
 \le C N^A
       \exp N\{\Re G_a(t)+R(j/N,t)+\eta\}
 \quad(0\le j<N)
 \tag{6}
\]
uniformly on (1), for each fixed \(k\). Indeed the
[whole-period endpoint envelope, equation (15)](research_mixed_endpoint_polynomial_collar.md)
bounds \(\mathcal H_N(w,r^{-j})\) by the rate
\(h(e)=\lambda(e)+J(e)\), including both endpoint layers.
The two reciprocal physical factorials have rate \(-2J(e)\)
with a polynomial uniform prefactor. The zero-safe finite-product
bound gives the rate \(I_t(e)\) for \(p_j(Y)\), uniformly
through its zeros. Finally the regular factorial symbol in (4) gives
\(\Re G_a(t)\). Allocate one total tolerance between these
bounds. Ordinary derivatives are those of the entire endpoint
polynomial; no Newton value or product zero is divided out.

## 2. Uniform transport to the two private cuts

**Lemma 1.** For every transform parameter in (1),
\[
 \begin{array}{ll}
 R(e,t)\le R(.27,t)-\dfrac{13}{100}(.27-e),
                                      &0\le e\le.27,\\
 R(e,t)\le R(.49,t)-\dfrac1{30}(e-.49),
                                      &.49\le e\le1.
 \end{array}
 \tag{7}
\]
Both comparisons retain the dependence between the phase of the
product and the signed transform height.

*Proof.* Away from a logarithmic zero, the exact derivative is
\[
 R_e(e,t)=\lambda'(e)-J'(e)
                 +\log|1-e^{-2\pi i(t+e)}|.
 \tag{8}
\]
The following original-branch inequalities were proved in
[the real-cap tails, equations (7), (11), and (12a)](research_mixed_outer_cap_real_tails.md):
\[
 \begin{array}{ll}
 \lambda'(e)>27/50,\quad J'(e)<41/100,
                                      &0<e\le.27,\\
 \lambda'(e)<-3/5,\quad J'(e)>3/5,
                                      &.49\le e\le.50,\\
 \lambda'(e)-J'(e)\le-\log4,
                                      &.50\le e<1.
 \end{array}
 \tag{9}
\]
The first two rows use the proved Schur concavity of \(\lambda\)
below one half and the cited endpoint scalar inequalities. These are
properties of the coherent endpoint action, not of its absolute
Newton-row maximum.

For \(0<e\le.10\), the real part of \(t+e\) lies in
\([.15,.60]\). Minimizing \(|1-\rho e^{-i\theta}|\)
over \(\rho\ge0\) shows that the product modulus in (8)
is greater than \(4/5\): when the cosine is positive the
minimum is its sine modulus, bounded below by
\(\sin(.3\pi)>4/5\), and otherwise the minimum is one.
Also \(J'(e)<0\). Hence
\[
 R_e>27/50+\log(4/5)>27/50-1/4=29/100.
 \tag{10}
\]
For \(.10\le e\le.27\), the real part of \(t+e\)
belongs to \([.25,.77]\), so
\(\cos(2\pi\Re(t+e))\le\sin(.04\pi)<13/100\).
Put \(\rho=e^{2\pi h}\). The already established
\(e^{.24\pi}<43/20<9/4\) gives \(\rho>4/9\).
Consequently
\[
 |1-\rho e^{-2\pi i(x+e)}|^2
  =1+\rho\{\rho-2\cos(2\pi(x+e))\}>1.
 \tag{11}
\]
Equation (9) then gives \(R_e>13/100\) on this interval.

On the whole upper tail the elementary bound is
\[
 \log|1-e^{-2\pi i(t+e)}|
 \le\log(1+e^{.24\pi})<\log(63/20)<7/6.
 \tag{12}
\]
For the last inequality the exponential series through degree four
at \(7/6\) is already greater than \(63/20\).
On \([.49,.50]\), (9) and (12) give
\(R_e<-6/5+7/6=-1/30\). On \([.50,1)\), they give
\[
 R_e<-\log(80/63)<-1/30.
 \tag{13}
\]
For example \(\log(80/63)>17/80>1/30\).
Integrate on the complementary intervals of any logarithmic zero.
The potential \(I_t\) is absolutely continuous, and all terms
of (5) are continuous at \(e=0,1\). Passing to these endpoint
limits proves (7), uniformly also when a zero is present. \(\square\)

## 3. The anchor rates are the original coherent private faces

At either cut \(c=.27,.49\), every \(c+t\) is in its
original regular strip. The prescribed branch gives
\(I_t(c)=\Re\{g(c+t)-g(t)\}\). Define the exact reduced
action
\[
 \Phi_1(a;e,t)=
 g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
       -i\pi(e-e^2)/2+S(e)+2\pi iat.
 \tag{14}
\]
It is obtained from the original triple phase by inserting the
original complete endpoint saddle \(u_c(e)\). The endpoint
packet on [the full cap rectangle](research_mixed_endpoint_cap_rectangle.md)
fixes its phase and logarithmic lift. Since the private cuts are real,
\[
       \Re G_a(t)+R(c,t)=\Re\Phi_1(a;c,t).
 \tag{15}
\]
All marks in (14) are retained; (15) is only an equality of real
rates at the two stated real cuts.

For fixed \(a,c\),
\(-\Re\Phi_{1,tt}>0\) throughout the transform rectangle.
Indeed this second derivative is independent of \(u_c(c)\)
and equals the \(t,t\) entry of the broad joint Hessian in
the source note. The entry can be evaluated at any permitted
\(u\), and is greater than \(\pi/100\). Thus
\(h\mapsto\Re\Phi_1(a;c,x+ih)\) is strictly convex.
No root at a moving independent horizontal target is required.

## 4. An explicit finite face criterion for both complete private tails

Fix an actual type-four terminal reference \(a_*\), its original
transform height \(h_*\in(-.108,-.020)\), and a real ceiling
\(B(a_*;y)\), such as the original bare supporting plane.
Suppose a uniform \(\delta>0\) gives the following comparisons,
for \(a=y+i\Im a_*\), all \(y\in[.22,.45]\), and
both \(c\in\{.27,.49\}\):
\[
 \begin{array}{ll}
 \Re\Phi_1(a;c,x+ih_*)\le B(a_*;y)-\delta,
                                              &.15\le x\le.50,\\
 \Re\Phi_1(a;c,b)\le B(a_*;y)-\delta,
                                              &b=.15,.50,\\
 \Re\Phi_1(a;c,x\pm.12i)-.24\pi
                \le B(a_*;y)-\delta,
                                              &.15\le x\le.50.
 \end{array}
 \tag{16}
\]
These are respectively flattened private faces, real corners, and
the two transform-alias faces. None of their gaps is proved here.

**Proposition 2.** Under (16), the two exact sectors of (3) with
the transform index in the inward half-grid version of \([.15,.50]\)
and private index respectively \(j/N\le.27\) or \(j/N\ge.49\)
have upper rate at most \(B(a_*;y)-\delta'\), for every fixed
\(0<\delta'<\delta\) and all sufficiently large \(N\).
The assertion includes a fixed small ordinary-color disk, all its
fixed derivatives on smaller disks, and both level parities.

*Proof.* For each physical \(j\), retain the exact function (4)
and apply the original one-variable residue identity in \(t\).
Its constant-mode coefficient is \(+N\); there is no additional
literal \(N\) in the source (3). Deform this mode to height
\(h_*\). The resulting pieces are one shifted horizontal
segment, two joins, two horizontal aliases at \(\pm.12\),
and four vertical alias half-sides. The finite upper bound (6) applies
to every piece, including revived products beyond the physical wall.

First transport \(e=j/N\) to its cut using (7) and (15).
Any transform-alias penalty is unchanged by this step. The shifted
horizontal piece is then bounded by the first row of (16). The
horizontal aliases use its third row. At either transform cut,
vertical convexity from Section 3 bounds each zero-mode join by its
shifted endpoint or its real corner. On each alias sign half, the
phase minus \(2\pi|h|\) is still convex, so its maximum is
at its real endpoint or its horizontal-alias endpoint. These are
exactly the other comparisons in (16).

The half-grid residue kernels are uniformly bounded at height zero
and have their usual exponential penalties off the real axis.
The lengths, residue factor \(N\), and at most \(N\)
private rows cost polynomial factors. Choose the one tolerance in
(6) smaller than the unused part of \(\delta-\delta'\).
Rounding a limiting cut by \(O(N^{-1})\) is harmless after
transport to its regular anchor, whose derivatives are uniformly
bounded. This also covers the strips needed to match the central
private half-grid cuts. Cauchy's formula supplies the stated fixed
ordinary derivatives. \(\square\)

All comparisons (16) are contained in the eight flattened-face and
twelve alias conditions of
[the reduced-current criterion](research_mixed_terminal_four_reduced_currents.md#3-the-sufficient-outer-current-comparisons).
They are its two flattened private faces, four real-real corners,
and transform-single aliases with private height zero. Thus this
exterior reduction adds no new tested family to that central criterion.

The whole Newton sum must be retained in these sectors before applying
Proposition 2. It does not bound arbitrary partial Newton sums near
the private endpoints. The physical wall \(i+j=N\), including
the rows that revive on a complex transform contour, is handled
explicitly by (2)--(6); the wall \(l=j\) is already inside the
complete \(\mathcal H_N\). Thus separate Newton-tail or support-wall
estimates are unnecessary for these two sectors. The central private
strip, the transform exterior, and the unproved calibrated face gaps
remain distinct obligations.
