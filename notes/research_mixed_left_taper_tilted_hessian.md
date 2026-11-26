# A supporting-plane bound on the left taper

Research proof, 4 November 2026. This concerns an original four-crossing
block whose left angle lies in \([.15,.22]\) and whose own angle remains
in \([.24,.45]\). No variable is selected in a Fourier correction.
It is a local estimate, not an assertion about the full cyclic sum.

## 1. The joined source domain

Use
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad Q(s;a,b)=g(s+a)+g(s+b)-3g(s)+2\pi ias.
\]
The [wider conditional-source theorem](research_mixed_asymmetric_wide_conditional_packets.md)
and the [transition-source theorem](research_mixed_transition_conditional_rectangles.md)
give the original holomorphic root \(Q_s=0\) on the joined product
\[
 \begin{split}
 A_3&=[.15,.45]+i[-.03,.02],\\
 A_4&=[.15,.45]+i[-.057,0],\\
 B_4&=[.24,.45]+i[-.057,-.02].
 \end{split}                                                     \tag{1}
\]
The left type is \(3+\eta\), with \(\eta\in\{0,1\}\), and the
own type is four. Define the conditional action with its allocated
Fourier half-weights by
\[
 \phi_\eta(a,b)=Q(s(a,b);a,b)
                   -(1+\eta/2)g(a)-\tfrac32 g(b).              \tag{2}
\]
The normalized primitive and original logarithmic lifts are retained.

Here the source domain is genuinely joined, not extrapolated from the
smaller chart. The two root branches agree on \(\Re a=.22\):
the transition root lies in the wider chart's uniqueness rectangle.
They consequently agree on the overlap of their open neighborhoods.
The exact finite source is the same on both sides, so its absolute
phase and leading symbol agree there as well. The source estimates
are uniform on (1).

One can also use a common uniqueness rectangle when checking the
joined product. The wide-source curvature inequality depends on the
lower real bounds \(.15,.24\), the height bounds, and the condition
that shifted real arguments are below one. These conditions still
hold when the upper bound for \(\Re a\) is increased to \(.45\).
Thus the same proof gives \(-\Re Q_{ss}>1/8\) on
\([.08,.49]+i[-.25,.20]\) throughout (1). This identifies every
original-logarithm Newton enclosure used below with the established root.

## 2. Controlling a straight segment whose height also changes

Let \(H=-\phi_\eta''\), a symmetric complex two-by-two matrix, and put
\[
 D_\rho=\operatorname{diag}(1+i\rho,1),\qquad
 T_\rho=\Re(D_\rho^T H D_\rho).                               \tag{3}
\]
The transpose here is deliberate: (3) is the real second derivative
of a holomorphic phase along a real segment with a fixed complex
direction. It is not its Hermitian quadratic form.

**Lemma 1.** On the entire corresponding product (1),
\[
 T_\rho\succ\tfrac12 I_2
 \quad\text{for}\quad
 \begin{cases}
 -.13\le\rho\le.13,&\eta=0,\\
 -.26\le\rho\le0,&\eta=1.
 \end{cases}                                                     \tag{4}
\]

Here is a complete reduction to the accompanying interval calculation.
Writing \(A=\Re H\), \(B=\Im H\), the entries are
\[
 T_\rho=
 \begin{pmatrix}
 (1-\rho^2)A_{aa}-2\rho B_{aa}&A_{ab}-\rho B_{ab}\\
 A_{ab}-\rho B_{ab}&A_{bb}
 \end{pmatrix}.                                                  \tag{5}
\]
The certificate checks \(A_{aa}>0\) and the two strict principal-minor
tests for \(T_\rho-I_2/2\) at both endpoints of the relevant interval
in (4). Every one of the 32 products of rectangle edges in (1) is
covered by exact dyadic cells. An affine Newton inclusion verifies the
original logarithmic equation before the Hessian is evaluated.

For each endpoint \(\rho\) and each fixed real vector \(v\),
\(v^T T_\rho v\) is the real part of a holomorphic function of
\((a,b)\). Successive harmonic minimum principles extend the boundary
inequality throughout (1). The same reasoning extends \(A_{aa}>0\).
Finally
\[
 \frac{d^2}{d\rho^2}T_\rho=-2A_{aa}
                       \begin{pmatrix}1&0\\0&0\end{pmatrix}
                       \preceq0 .                              \tag{6}
\]
The matrix is concave in \(\rho\); every intermediate value dominates
the interpolation of its endpoint values. This proves (4). The argument
does not apply a maximum principle to a nonlinear eigenvalue or Schur
quotient.

For reference, the evaluated Hessian is explicit. With
\(p=g''(s+a)\), \(q=g''(s+b)\), \(d=p+q-3g''(s)\), and
\(u=p+2\pi i\),
\[
 H_{aa}=-p+(1+\eta/2)g''(a)+u^2/d,\quad
 H_{ab}=uq/d,\quad
 H_{bb}=-q+\tfrac32g''(b)+q^2/d .                              \tag{7}
\]

## 3. The taper supplies exactly these complex directions

Let \((a_*,b_*)\) be the two outer legs of this block at an actual
cyclic critical point. Their proved bounds are
\[
 a_*\in R_{3+\eta},\quad b_*\in R_4,
 \quad R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].                                  \tag{8}
\]
Write \(r=\Re a_*\), \(h_* =\Im a_*\). For target angles
\(x\in[.15,.22]\), \(y\in[.24,.45]\), take
\[
 a=x+i h_*(x/.22)^2,\qquad b=y+i\Im b_* .                    \tag{9}
\]
These are the left taper and the constant-height portion of the graph
with plateau \([.22,.45]\). The segment from (8) to (9) stays inside
(1). Its complex displacement is
\[
 (a-a_*,b-b_*)=D_\rho(x-r,y-\Re b_*),\qquad
 \rho=h_*\frac{1-(x/.22)^2}{r-x}.                             \tag{10}
\]

The fraction in (10) decreases with both \(r\) and \(x\) on the
stated intervals. For the second assertion its derivative has numerator
\(x^2-2rx+.22^2\), which is negative already at \(x=.15\),
\(r=.27\), and decreases as \(x\) grows to \(.22\) or \(r\)
increases. Consequently
\[
 |\rho|\le .03\frac{1-(.15/.22)^2}{.30-.15}<.13
       \quad(\eta=0),\qquad
 -.26<-.057\frac{1-(.15/.22)^2}{.27-.15}\le\rho\le0
       \quad(\eta=1).                                         \tag{11}
\]
These are exact rational comparisons. Thus Lemma 1 applies at every
point of the segment with its fixed direction \(D_\rho\).

Let
\[
 \Gamma(a,b)=\phi_\eta(a_*,b_*)+
       \phi_{\eta,a}(a_*,b_*)(a-a_*)+
       \phi_{\eta,b}(a_*,b_*)(b-b_*).
\]
Taylor's integral remainder gives
\[
 \Re\phi_\eta(a,b)-\Re\Gamma(a,b)
 \le-\tfrac14\{(x-r)^2+(y-\Re b_*)^2\}
 \le-\frac1{1600}.                                           \tag{12}
\]
Indeed \(r-x\ge.05\). No differentiation of the curved graph is used:
the segment in (10), rather than the graph itself, proves the inequality.

## 4. Returning to the complete finite source

Let \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\), and use the literal
kernel \(C_{1,N}\) and Fourier polynomial \(d_N\) of the
[right-half block theorem](research_mixed_right_half_block_bound.md).
The complete conditional-source expansions on (1) give a polynomial
times the exponential of \(Q(s)-g(a)-g(b)\). When \(\eta=1\),
the left height in (9) is negative; the own height is always negative.
On these compact left-half strips, \(\nu=-\Re g>0\), so the actual
Fourier-polynomial upper bound has rate \(\nu\), including its forcing
term. This is the sign argument in the
[plateau theorem](research_mixed_plateau_accretivity.md#4-the-true-unaliased-finite-integrand).

Allocate half of each incident Fourier weight. Each actual Fourier
factor can be bounded with rate tolerance \(1/8000\); the sum of the
allocated tolerances is at most \(1/8000\). Combining with (12) proves
the following local statement for all sufficiently large integer levels:
\[
 |C_{1,N}(X,Y)|\,|d_N(X)|^{\eta/2}|d_N(Y)|^{1/2}
 \le C N^A\exp\left\{N\left(\Re\Gamma(a,b)-\frac1{2000}\right)\right\}.
                                                                  \tag{13}
\]
All original rows and both parities are retained. There are no selected
Fourier variables in (13). The conclusion covers an own-four block
with its left angle in \([.15,.22]\) and its other angle in
\([.24,.45]\), under the actual critical height bounds (8).
It supplies no bound for a both-low pair, a reversed orientation,
an own-three block, or an entire cyclic word with untreated blocks.

## 5. Reproduction

Run
```sh
python3 experiments/certify_mixed_left_taper_tilted_hessian.py
```
The record contains every accepted boundary address and rational affine
Newton witness. The checker verifies the identities (5)--(6), the rational
taper bounds (11), complete dyadic coverage, and positivity of the two
endpoint matrices. Root holomorphy and the original finite-source
expansions are the cited source inputs; their domains and bindings are
checked before the new Hessian calculation.
