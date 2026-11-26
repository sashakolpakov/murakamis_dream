# A full two-coordinate height-reset cost

Research proof, 4 November 2026. This permits both real coordinates
of a conditional block to readjust, while either or both heights
move toward zero. The separate single-coordinate theorem is unchanged.
The outward cover passed on all 64 boundary products, with 36,325
accepted cells. Independent review is separate.

## 1. Original phase and full source products

For ordered types \(\eta,\epsilon\in\{0,1\}\), use
\[
 \phi(a,b)=Q_\epsilon(s_*(a,b);a,b)
       -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \quad
 Q_\epsilon=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias.
 \tag{1}
\]
All roots, logarithms and symbols are the original ones. Set
\[
 \begin{array}{ll}
 R_3=[.30,.39]+i[-.03,.02],&
 R_4=[.27,.33]+i[-.057,-.02],\\
 U_3=[.22,.50]+i[-.03,.02],&
 U_4=[.22,.50]+i[-.057,0].
 \end{array}
 \tag{2}
\]
The [complete right-square packet](research_mixed_unselected_right_taper_products.md),
Theorem 1, gives the holomorphic original root and full finite source
on neighborhoods of all four products \(U_{3+\eta}\times U_{3+\epsilon}\).
For \(r\in R_{3+\eta}\times R_{3+\epsilon}\), write
\[
                 \Gamma_r(z)=\phi(r)+\phi'(r)\cdot(z-r).
 \tag{3}
\]

**Theorem 1.** Let both target real coordinates belong to
\([.22,.50]\), and let each target height lie on the segment
between zero and its own reference height. Then
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
             \le10\|\Im(z-r)\|_2^2.
 \tag{4}
\]
The inequality is strict for every nonzero displacement.
In particular resetting any subset \(S\) of the heights to zero,
while leaving the other heights at reference, costs at most
\[
                            10\sum_{j\in S}(\Im r_j)^2.
 \tag{5}
\]
Both real coordinates may change, including a coordinate whose
height is unchanged.

## 2. Completing the full real square

Write the complex symmetric outer Hessian as
\[
                    \phi''=-A+iB,\qquad A,B\ \hbox{real symmetric}.
 \tag{6}
\]
The outward certificate proves on every product of parameter sides
\[
                   A>0,\qquad K:=A+B A^{-1}B<20I.
 \tag{7}
\]
These are matrix bounds, not separate diagonal estimates.
The Hessian includes the motion of the eliminated inner root.
Explicitly, putting
\(p=g''(s_*+a)\), \(q=g''(s_*+b)\),
\(d=p+q-(2+\epsilon)g''(s_*)\), it is
\[
 \phi''=
 \begin{pmatrix}
 p-(1+\eta/2)g''(a)-(p+2\pi i)^2/d&
 -(p+2\pi i)q/d\\
 -(p+2\pi i)q/d&
 q-(1+\epsilon/2)g''(b)-q^2/d
 \end{pmatrix}.
 \tag{8}
\]
For real vectors \(u,v\), the exact completion is
\[
 \begin{split}
 \Re\{(u+iv)^T\phi''(u+iv)\}
 &=-u^TAu-2u^TBv+v^TAv\\
 &=-(u+A^{-1}Bv)^TA(u+A^{-1}Bv)+v^TKv\\
 &\le20|v|^2.
 \end{split}
 \tag{9}
\]
For each fixed \(u,v\), the first expression is harmonic in both
complex parameters. Two maximum principles therefore extend (9)
from the sixteen products of sides to the whole parameter product.
Likewise \(A>0\) extends by testing each fixed real vector.
This argument does not claim that the nonlinear matrix \(K\)
is harmonic. Strict compact boundary margins give strictness
for nonzero \(u+iv\).

The checker covers all 64 products, using rational affine Newton
self-maps for the original logarithmic root. It verifies positive
diagonals and determinants of both \(A\) and \(20I-K\).
The inverse is the literal two-by-two adjugate divided by
\(\det A>0\). All covers are exact prefix-free binary partitions.
Saved witnesses allow replay without new root proposals.

For \(w=z-r\), the straight segment \(r+tw\) remains in the
independent product (2). Integrating (9) gives
\[
 \Re\{\phi(z)-\Gamma_r(z)\}
  =\int_0^1(1-t)\Re\{w^T\phi''(r+tw)w\}\,dt
                \le10|\Im w|^2.
 \tag{10}
\]
This proves (4), including its allowance for unrestricted real
readjustment in the stated intervals.

## 3. The full finite source

At every unselected four-type target in (4), its height is
nonpositive and its real coordinate belongs to \([.22,.5]\).
The true Fourier-polynomial upper rate is
\(\max\{-\Re g,0\}=-\Re g\), including the tie at .5.
The whole right-square conditional packet and the true Fourier
upper bound therefore give, for every fixed \(\delta>0\),
\[
 |\text{original allocated block}|
 \le C_\delta N^A
  \exp N\{\Re\Gamma_r(z)+10|\Im(z-r)|^2+\delta\}.
 \tag{11}
\]
All finite rows, revived rows and conditional aliases are retained
by the source input. The two half-weights recombine into the
original integer powers in an actual word. An outer selection
at a coordinate whose target height is zero has modulus one;
selections at the remaining complex coordinates are not included.

## 4. A compact low/plateau cluster consequence

Choose a periodic continuous piecewise linear cutoff that is zero
on \([0,.1]\), rises linearly to one at .22, stays one on
\(P=[.22,.45]\), falls linearly to zero at .5, and is zero on
\([.5,1]\). On the exact unselected coupled graph
\[
 H_j(x)=(\Im z_j^*)\rho(x_{j-1})\rho(x_j)\rho(x_{j+1}),
 \tag{12}
\]
the [coupled contour theorem](research_mixed_coupled_outer_graph.md)
preserves the original Laurent integral. Here
\(\|\rho'\|_\infty=20\), so its Jacobian is bounded by
\((1+(171/50)^2)^{m/2}<(18/5)^m\), independently of \(N\).
The actual critical neighborhood is unchanged.

Restrict to configurations with each real coordinate in
\(L=(0,.1]\) or \(P\), with \(L\) occurring. Formula (12) gives
every low vertex height zero and resets each plateau vertex
adjacent to a low vertex to zero. All other plateau heights
stay at reference. Count incidences before identification,
including lengths one and two.

Every block incident to a low vertex has both heights zero.
The [coherent real one-small comparison](research_mixed_real_one_small_support.md)
gives a strict allocated phase gap \(11/200\) relative to its
original complex plane. All other blocks are plateau--plateau
and obey (5). Let \(n_{LP}\) and \(n_{LL}\) count their original
edge incidences, and put \(n_G=n_{LP}+n_{LL}\ge1\).
A reset plateau vertex has \(k=1\) or \(2\) low incidences and
at most \(2-k\le k\) nongapped incidences. Hence its reset cost
can be charged to at most its low incidences, and
\[
 \begin{split}
 \text{total phase defect}
 &<- \frac{11}{200}(n_{LP}+n_{LL})
                     +10(.057)^2 n_{LP}\\
 &\le-\frac{2251}{100000}\,n_G
                    <-\frac9{400}\,n_G.
 \end{split}
 \tag{13}
\]
The linear terms in the original complex planes cancel by the
cyclic zero-lift critical equations, so (13) is a loss relative
to the original critical action. This counting also handles
all-low words and repeated incidences at lengths one and two.

On any fixed compact subregion with every low coordinate bounded
away from zero, the actual full-source bounds apply uniformly. Choosing
per-block Fourier tolerance \(\delta_m<1/(400m)\) in (11),
and using the same tolerance for the real one-small blocks,
leaves a whole-product gap greater than \(1/50\).
All original normalizing powers cost only polynomial factors.

Thus the absolute integral over each such restricted low/plateau
region on the explicit graph (12) has that same gap, with its
bounded Jacobian and finitely many boxes. This is not yet uniform
when a low target tends to zero with \(N\).

The contour itself is defined on the whole torus, but this estimate
does not cover the transitions \((.1,.22)\), the right taper or
right exterior, or selected aliases at nonzero heights. In
particular (12) also resets neighbors of right-half coordinates,
so old right-half support gaps cannot be imported unchanged.
No complete mixed-word asymptotic is asserted.

## 5. Reproduction

    python3 experiments/certify_mixed_full_height_reset.py --precision 256

    python3 experiments/certify_mixed_full_height_reset.py --precision 320 --input repro/results/research-mixed-full-height-reset.json --output /tmp/research-mixed-full-height-reset-review.json

The focused exact checks include the matrix completion and the
cluster arithmetic. The finite incidence check is bookkeeping;
the argument \(2-k\le k\) proves (13) for every cyclic length.
