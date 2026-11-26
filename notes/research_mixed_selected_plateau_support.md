# A local original-source gap for selected plateau variables

Research proof, 4 November 2026. The canonical outward certificate and independent written/code
review have passed.
Earlier source, taper and manuscript files are unchanged.

This bounds a whole original conditional block whenever at least one
of its plateau coordinates is a selected four-type variable. Every
branch of the true Fourier-polynomial upper bound is kept. It is not
a comparison obtained by discarding real rows or by replacing the
finite conditional sum with an unproved saddle approximation.

## 1. Literal finite source and geometric reference

Let \(r=e^{-2\pi i/N}\), and define the original functions
\[
 P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\qquad
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{\,2+\epsilon}},
                  \qquad\epsilon\in\{0,1\}.
 \tag{1}
\]
Let \(\eta\) be the left type minus three and \(\epsilon\) the own
type minus three. The original Fourier polynomial is \(d_N\).
Use the normalized primitive and zero-lift conditional phase
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi_{\eta\epsilon}(a,b)
 &=Q_\epsilon(s_*(a,b);a,b)
                -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
 \end{split}
 \tag{2}
\]
The unique original conditional root and full canonical packet on
all typed plateau products are proved in the
[transition source theorem](research_mixed_transition_conditional_rectangles.md).
All uses of \(\phi\) below refer to that branch and additive constant.

At an actual cyclic critical pair \(r=(a_*,b_*)\), the established
geometric rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{3}
\]
We prove the comparison for every independent pair
\(a_*\in R_{3+\eta},b_*\in R_{3+\epsilon}\), so the actual critical
pairs are included. The full complex tangent is
\[
 \Gamma_r(z)=\phi(r)+\phi_a(r)(z_1-a_*)
                              +\phi_b(r)(z_2-b_*).
 \tag{4}
\]
Set \(H=7/500\). Selected indicators \(\sigma_a,\sigma_b\) obey
\(\sigma_a\le\eta,\sigma_b\le\epsilon\) and
\(\sigma_a+\sigma_b>0\). For \(x,y\in[.22,.45]\), the target is
\[
 z_1=x+i\begin{cases}H,&\sigma_a=1,\\ \Im a_*,&\sigma_a=0,\end{cases}
 \qquad
 z_2=y+i\begin{cases}H,&\sigma_b=1,\\ \Im b_*,&\sigma_b=0.\end{cases}
 \tag{5}
\]
Write \(X=e^{-2\pi iz_1}\), \(Y=e^{-2\pi iz_2}\), and retain the
literal allocated modulus
\[
 B_N(z)=|C_{\epsilon,N}(X,Y)|
       |d_N(X)X^{-N\sigma_a}|^{\eta/2}
       |d_N(Y)Y^{-N\sigma_b}|^{\epsilon/2}.
 \tag{6}
\]
Its square roots are nonnegative roots of moduli, not holomorphic
choices of square roots of \(d_N\).

**Theorem 1.** Uniformly on (3)--(5), for both parities and all
sufficiently large integer levels,
\[
 B_N(z)\le \operatorname{poly}(N)
                  \exp N\left(\Re\Gamma_r(z)-\frac1{200}\right).
 \tag{7}
\]
This is an upper bound for the entire finite function (1), including
all its revived rows and contour currents.

## 2. Keeping all true Fourier branches

Put \(\nu(z)=-\Re g(z)\). The actual Fourier-polynomial estimate gives,
for any fixed \(\delta>0\), the uniform rate
\(\max\{\nu(z),2\pi(\Im z)_+\}+\delta\).
For an unselected four-type target in (5), its negative height gives
\(\nu(z)>0\); its allocated rate is \(\nu(z)/2\), up to the tolerance.
For a selected target, including its \(X^{-N}\) factor, that rate is
\[
 \tfrac12\max\{\nu(z),2\pi H\}-\pi H
 =\tfrac12\nu(z)-\tfrac12\min\{\nu(z),2\pi H\}.
 \tag{8}
\]
No relative Fourier/factorial approximation is used to make this split.

For \(f_a\in\{0,\ldots,\sigma_a\}\) and
\(f_b\in\{0,\ldots,\sigma_b\}\), define the holomorphic branch
\[
 \psi_f(z)=\phi(z)+\tfrac12[f_ag(z_1)+f_bg(z_2)]
                   -\pi H(\sigma_a-f_a+\sigma_b-f_b).
 \tag{9}
\]
The maximum of the real parts of these branches is exactly the full
rate in (8) added to the kernel rate. The five selection/type patterns
\[
 (0,1,0,1),\ (1,0,1,0),\ (1,1,1,0),\
 (1,1,0,1),\ (1,1,1,1)
 \tag{10}
\]
for \((\eta,\epsilon,\sigma_a,\sigma_b)\) have twelve branches in total.
We prove separately for every branch
\[
              \Re[\psi_f(z)-\Gamma_r(z)]<-1/100.
 \tag{11}
\]
Taking their maximum then retains the true forcing branch everywhere.
The maximum of concave branches is not itself asserted to be concave.

## 3. Strong concavity on the complete target square

**Lemma 2.** For each branch in (9), at all targets with real parts
in \([.22,.45]^2\) and the prescribed selected or unselected heights,
\[
                         -\Re\psi_f''>\tfrac32 I.
 \tag{12}
\]
The original root exists on the full complex plateau products before
this estimate is checked. The condensed matrix is
\[
 \begin{split}
 q&=Q_{\epsilon,ss},\qquad
 v_a=\pi\cot\pi(s+a)+\pi i,\quad
 v_b=\pi\cot\pi(s+b)-\pi i,\\
 W_{aa}&=\pi\cot\pi(s+a)-(1+\eta/2)\pi\cot\pi a+\eta\pi i/2,\\
 W_{bb}&=\pi\cot\pi(s+b)-(1+\epsilon/2)\pi\cot\pi b
                                                    +\epsilon\pi i/2,\\
 -\phi''&=-\operatorname{diag}(W_{aa},W_{bb})
                                  +q^{-1}(v_a,v_b)^T(v_a,v_b).
 \end{split}
 \tag{13}
\]
For \(-\psi_f''\), subtract
\(\frac12\operatorname{diag}(f_ag''(a),f_bg''(b))\).
This includes the original chirps and both allocated half-weights.

A selected target parameter runs along its full real segment at
height \(H\). An unselected target parameter runs through its
independent rectangle with the heights in (3), and real interval
\([.22,.45]\). For each fixed real test vector, the quadratic form
in (12) is harmonic in that unselected complex parameter.
Consequently its minimum reduces to the four rectangle sides.
When both parameters are selected, both real intervals are covered
directly. There are thirty-six resulting two-parameter products.

The checker encloses the original logarithmic root by rational affine
Newton self-maps on each cell. It evaluates (13) and checks positivity
of both diagonal entries and the determinant after subtracting
\(3I/2\). Complete exact binary covers retain every real target
point and every boundary side. The cover passed on 11,010 cells.
The harmonic argument extends the bound through the full unselected
height rectangles, using the already proved holomorphic branch.

## 4. A reference-cell support certificate

Fix the reference heights in (3) and a branch \(f\). As a function of
the two real target coordinates \(v=(x,y)\), put
\[
                   F_r(v)=\Re[\psi_f(z(v))-\Gamma_r(z(v))].
 \tag{14}
\]
For any rational \(c\in[.22,.45]^2\), Lemma 2 gives
\[
 \max_{v\in[.22,.45]^2}F_r(v)
       \le F_r(c)+\frac{\|\nabla_vF_r(c)\|_2^2}{3}.
 \tag{15}
\]
Indeed the concavity Taylor bound is
\(F_r(v)\le F_r(c)+\nabla F_r(c)\cdot(v-c)-3\|v-c\|^2/4\);
maximizing this quadratic over the whole real plane proves (15).
No stationary point or optimizer is presumed to lie in the target
square. Floating optimization is used only to propose \(c\); the
checker verifies that its rational coordinates lie in the square.

For a selected reference variable the target height in (5) is fixed.
At each fixed target point the defect (14) is then harmonic in that
complex reference variable. Its supremum over the compact target
square is subharmonic and locally bounded. It is therefore enough to
check the selected reference variables on their rectangle boundaries.
An unselected reference height changes the target itself and is
retained as a genuine independent real parameter. Thus one-selected
reference products are three dimensional: one selected boundary
parameter and the unselected real coordinate and height. With both
selected they are two dimensional, on both boundary curves. The
twelve branches give ninety-six such products.

Here is the exact mean-value estimate used on those cells. Write
\(r=(a_*,b_*)\), \(z=z(c;r)\), \(\Delta=z-r\), and
\[
 G=\psi_f'(z)-\phi'(r),\qquad K=-\phi''(r).
 \tag{16}
\]
For a real cell parameter \(\tau\), the exact derivative is
\[
 \partial_\tau F_r(c)
 =\Re\left[
       G\cdot\partial_\tau z+
       \sum_{j,k}K_{jk}\Delta_j\,\partial_\tau r_k
       \right].
 \tag{17}
\]
A selected reference parameter has \(\partial_\tau z=0\).
For an unselected reference real coordinate it is again zero,
while its height parameter has the same imaginary increment in
\(z\) and \(r\). Formula (17) includes this height dependence;
no maximum principle is applied to it.

Each cell stores rational original-root centers, affine response
witnesses and remainder radii for both \(r\) and \(z(c;r)\).
The point Newton tests enclose the center values of \(F_r(c)\).
The full affine enclosures bound (17) throughout the cell and
\(\nabla_vF_r(c)=\Re G\). Adding the resulting mean-value cost and
the quadratic term in (15) gives an outward number strictly less
than \(-1/100\). All ninety-six complete binary covers passed,
with 4,743 accepted cells. Their target points are proposals only;
acceptance uses the strict outward inequalities and the original
zero logarithmic lift.

This proves (11) on the selected reference boundaries and all
unselected real/height values. The subharmonic maximum principle
just described proves it on every independent reference pair (3).
The actual cyclic pairs form a subset, requiring no correlation
assumption or numerical word sampling.

## 5. Whole finite source and cyclic scope

The transition theorem is a full packet for the literal finite
function (1) on every target product used here. Its proof already
keeps the full real-index tails, all revived rows, both cotangent
aliases and every connecting current. It supplies a uniform
polynomial-times-exponential upper bound with kernel rate
\(\Re[Q_\epsilon(s_*)-g(z_1)-g(z_2)]\).
Combining that actual source bound with the true Fourier estimate
(8), the two allocated half-weights cost at most a total \(\delta\).
Choose \(\delta<1/200\). Equations (9)--(11) then prove (7).

Strict margins and the uniform source neighborhoods also give
fixed derivatives of the original holomorphic contractions with
integer Fourier powers, after shrinking the gap if needed.
No derivative is asserted for the half-moduli notation itself.
Both parities and all original finite endpoint rows remain included.

A useful direct consequence is a bound for every nonempty selected
term on the mixed plateau/right-half region
\[
                       U=([.22,.45]\cup[.5,1])^m.
 \tag{18}
\]
Use the original \(\chi_1\) graph and a fixed cyclic word. A target box
with a right-half coordinate has the allocated block gap \(1/2000\)
from the [whole right-half theorem](research_mixed_right_half_block_bound.md),
for every selected indicator. Otherwise all coordinates are in the
plateau, and a nonempty selected set supplies a block with (7).
All other selected plateau blocks have the same nonpositive
support defect; unselected plateau blocks are bounded by their
own supporting planes with tolerance
\(\delta_m<1/(4000m)\).
The allocated half-weights restore exactly the original integer
Fourier powers. The full complex linear tangent terms cancel at
the original cyclic critical point, including the literal
one- and two-vertex incidences. Thus each selected density on
\(U\) is bounded by
\(\operatorname{poly}(N)e^{N(M-1/4000)}\), where \(M\) is the real
part of the original critical action.

This last assertion uses the exact original subset densities and
graph deformation already established in the cited torus and
right-half proofs. It adds no new contour or boundary current.
Selected right-taper targets, left angles below .22, and a full
mixed-word asymptotic remain separate.

## 6. Reproduction

    python3 experiments/certify_mixed_selected_plateau_support.py --precision 256

The checker first proves all thirty-six target concavity covers,
then all ninety-six reference support covers. It verifies exact
binary coverage, original logarithmic Newton witnesses, current
source provenance and start/end input immutability. Every numerical
optimizer is confined to proposing a rational support point.
