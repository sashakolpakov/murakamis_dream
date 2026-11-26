# Exact coupled outer graphs and their conditional source domains

Research proof, 4 November 2026. This changes no completed source or
contour artifact. It is an exact contour identity and a reduction of
the conditional source domains, not an exterior support estimate.

## 1. Coupled graphs preserve the complete Laurent integral

For a fixed cyclic word and a fixed subset of its four-type aliases,
let \(F_{N,S}(X_1,\ldots,X_m)\) be its complete Laurent-polynomial
integrand from the
[exact conditional torus identity](research_mixed_conditional_torus_composition.md).
In particular the actual polynomial \(d_N\), every factor \(X_j^{-N}\),
and every conditional finite sum are retained.

**Theorem 1.** Let \(H:\mathbb T^m\longrightarrow\mathbb R^m\) be
continuous, periodic and piecewise \(C^1\), with finitely many pieces
and bounded first derivatives. Then
\[
 \operatorname{CT}F_{N,S}
 =\int_{[0,1]^m}
 F_{N,S}\!\left(e^{-2\pi i(x_1+iH_1(x))},\ldots,
               e^{-2\pi i(x_m+iH_m(x))}\right)
 \det(I+iDH(x))\,dx .
 \tag{1}
\]
The original scalar \(\kappa^{m+k}N^{m+k}\) is unchanged. Different
alias subsets may use different graphs, since (1) applies to each
original finite Laurent term separately.

To prove this, on \(\mathbb C^m/\mathbb Z^m\) use the closed holomorphic
\(m\)-form
\[
 \omega=F_{N,S}(e^{-2\pi iz_1},\ldots,e^{-2\pi iz_m})
                    \,dz_1\wedge\cdots\wedge dz_m .
 \tag{2}
\]
It is closed because a holomorphic derivative of its coefficient
wedges with a repeated \(dz_j\). Pull it back through the periodic
homotopy \(z=x+itH(x)\), \(0\le t\le1\). Stokes' theorem gives equal
integrals at the two ends. The faces of a fundamental cube cancel
periodically, and every internal interface between differentiability
pieces cancels with its opposite orientation. Equivalently one may
approximate the Lipschitz graph by periodic smooth graphs and pass
to the limit in this finite holomorphic integral.

The real-torus integral is the constant term: each Laurent monomial
has integral \(\int_{\mathbb T^m}e^{-2\pi i n\cdot x}dx=\delta_{n,0}\).
The graph pullback is exactly (1). Thus the clockwise exponential
parametrization introduces no extra sign. Neither invertibility nor
nonvanishing of the complex determinant is required. There are no
additional vertical currents, even though the heights depend on
neighboring real coordinates. The same argument applies to the
exact open-word integrands and their fixed ordinary derivatives;
it proves no new bound on the ordinary boundary polynomials.

## 2. A nearest-neighbor cutoff, including short cycles

Choose the following continuous periodic piecewise linear cutoff:
\[
 \rho(x)=
 \begin{cases}
 0,&0\le x\le11/50,\\
 \dfrac{100}{3}(x-11/50),&11/50\le x\le1/4,\\
 1,&1/4\le x\le9/20,\\
 20(1/2-x),&9/20\le x\le1/2,\\
 0,&1/2\le x\le1.
 \end{cases}
 \tag{3}
\]
It satisfies \(0\le\rho\le1\) and \(|\rho'|\le100/3\).
For each outer variable take \(c_j\) to be its original critical
height if unselected, and \(c_j=7/500\) if it is a selected four-type
variable. The established geometric ranges give
\[
 c_j\in[-.03,.02]\quad\hbox{for type three},\qquad
 c_j\in[-.057,-.02]\ \hbox{or}\ \{.014\}
                                      \quad\hbox{for type four}.
 \tag{4}
\]
Set, with cyclic subscripts and with every occurrence retained,
\[
             H_j(x)=c_j\,\rho(x_{j-1})\rho(x_j)\rho(x_{j+1}).
 \tag{5}
\]
Repeated subscripts mean repeated factors. In particular
\[
 \begin{array}{ll}
 m=1:&H_1=c_1\rho(x_1)^3,\\
 m=2:&H_1=c_1\rho(x_2)^2\rho(x_1),\quad
       H_2=c_2\rho(x_1)^2\rho(x_2).
 \end{array}
 \tag{6}
\]
No separate self-loop or parallel-incidence convention is needed.

At every differentiability point, the sum of absolute values in
each row of \(DH\) is at most
\[
 3\max_j|c_j|\,\|\rho'\|_\infty
 \le3\frac{57}{1000}\frac{100}{3}=\frac{57}{10}.
 \tag{7}
\]
This bound also counts coinciding derivative columns in (6).
Since \(DH\) is real, the squared Euclidean norm of row \(j\) of
\(I+iDH\) is \(1+\sum_k(\partial_kH_j)^2\). Hadamard's inequality gives
\[
 |\det(I+iDH)|
 \le\left(1+(57/10)^2\right)^{m/2}
 <(29/5)^m .
 \tag{8}
\]
Thus for each fixed word the Jacobian has no exponential cost in \(N\).

Every actual critical real coordinate is strictly inside
\((1/4,9/20)\): type-three coordinates lie in \((.30,.39)\) and
type-four coordinates in \((.27,.33)\). On the whole open box
\((1/4,9/20)^m\), \(H_j=c_j\) and \(DH=0\).
Consequently the original local unselected critical integral and
its coefficient are unchanged. The previously proved local selected
contours are also unchanged there. This statement identifies a local
contribution only; it does not estimate its new complement.

## 3. Exact reduction of the block source domains

Write \(z_j=x_j+iH_j(x)\). A local conditional factor has arguments
\((z_j,z_{j+1})\), with their original ordered types.
If \(\rho(x_j)=0\), then
\[
                    H_{j-1}=H_j=H_{j+1}=0 .
 \tag{9}
\]
Hence every block incident to a coordinate in
\([0,.22]\cup[.5,1]\) has both heights exactly zero.
This includes both incident blocks and remains literal for \(m=1,2\).

For blocks whose two real coordinates lie in \((0,.5]\), there
are only the following source cases.

* If both coordinates are at least .22, their arguments lie in the
  full independent boxes
  \[
    B_3=[.22,.50]+i[-.03,.02],\qquad
    B_4=[.22,.50]+i[-.057,.0141].
    \tag{10}
  \]
  Thus the [whole right-square conditional packet](research_mixed_unselected_right_taper_products.md),
  Theorem 1, applies. Every height in (5) is between zero and its
  original or selected value; dependence on the other coordinates
  is irrelevant because that theorem covers independent products.
* If either coordinate is at most .22, both arguments are real by
  (9). The [closed-half-endpoint conditional packet](research_mixed_half_endpoint_conditional_packet.md),
  Theorem 2, applies uniformly whenever this real pair stays in a
  fixed compact subset of \((0,.5]^2\). It is the same canonical finite sum,
  not another interpolation agreeing only at physical nodes.

For the literal Laurent kernel, divide the canonical packet by its
two actual marked factorials, as in the torus identity. On the compact
real pair in the second case, these factorials have their original
regular-strip nonzero symbols. Thus the kernel phase is
\(Q_\epsilon(s_*)-g(a)-g(b)\), its power is
\(N^{-(1+\epsilon)/2}\), and its coefficient is the original nonzero
one. This is a uniform source statement on that compact real pair;
it asserts no complex-neighbor neighborhood near arbitrarily small
outer angles.

The half-period endpoint is covered by that separate theorem, not
by treating a measure-zero edge as harmless. Its direct closed-quadrant
root count, strict phase gaps and original finite-current proof
include \((a,.5)\) for \(a>0\), uniformly on each compact
\([\delta,.5]^2\), \(\delta>0\). It also distinguishes all canonical
levels from the even levels at which .5 is an exactly physical
index. The right-square packet independently covers the endpoint
when both coordinates are at least .22.
No uniform packet as a real coordinate tends to zero is claimed.
Exact finite values on the zero seams remain in (1).

Consequently, for each fixed \(\delta>0\), every left-left block
on the coupled graph with both real coordinates in \([\delta,.5]\)
has a uniform original conditional packet supplied by these two
proved source theorems. This covers reset configurations, all
selection choices, and both orientations. It does not compare
their critical actions with the geometric tangent.

If a block has a coordinate in \([.5,1]\), both its heights are
zero by (9). Whole finite-product and true Fourier-polynomial
absolute upper bounds remain available at those real arguments.
However the previously proved right-half *support gap* is stated
for specified independent quadratic taper heights. It cannot be
imported unchanged when (5) resets an adjacent plateau height to
zero. A new comparison with the original complex supporting plane
is required, even though no new definition of the finite source
is required.

## 4. The remaining estimate is not a contour identity

Equations (1) and (9)--(10) eliminate the need to continue a
conditional packet to complex low neighbors on this graph.
They do not prove that a reset block is below its geometric
tangent. In particular setting a neighboring height to zero
can increase its real action even when its real coordinate stays
near the critical one.

The graph tangent is genuinely coupled. Along a real direction
\(v\), for a holomorphic total phase \(\Phi\),
\[
 \frac{d^2}{dt^2}\Re\Phi(x+tv+iH(x+tv))\big|_{t=0}
 =\Re\!\left[
 ((I+iDH)v)^T\Phi''((I+iDH)v)
             +i\sum_j\Phi_j\,D^2H_j[v,v]\right].
 \tag{11}
\]
Even away from the cutoff corners, (5) has mixed second derivatives.
Ambient real Hessian positivity alone therefore proves neither
graph concavity nor cancellation of these new action changes.
The actual \(d_N\) forcing alternatives and every selected
\(X_j^{-N}\) must also be retained in any such comparison.

No exterior loss, complete cyclic asymptotic, new ordinary-boundary
estimate or knot-volume theorem follows from this note.

## 5. Reproduction

    python3 experiments/check_mixed_coupled_outer_graph.py

The checker validates the exact cutoff, derivative and Jacobian
arithmetic, the graph chain rule, original normalization, and the
zero-height incidence assertion for every zero/nonzero pattern at
cyclic lengths one through eight. The general incidence proof,
closed-form homotopy and domain deductions above are analytic;
finite checks are not a substitute for them.
