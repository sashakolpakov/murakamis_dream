# A common short filling of finitely many types of filled blocks

This note extends the repeated zero-block theorem to a fixed finite
collection of actual filled pieces. The pieces can have complex boundary
actions. In particular they may be terminal vertices with any prescribed
powers of magnitude at least two. Sufficiently many pieces meeting one
original circle allow every fixed signed power at that circle.

The collection is fixed before the number of pieces and their central
power are chosen. Its members can occur in any order and with unrelated
multiplicities. The number required depends on the collection, but not
on the central power or on which members are chosen.

## 1. A concrete finite collection

The following pieces have already been proved to have both the required
whole-boundary estimates and the original marked geometry.

1. Any fixed connected zero-filled subtree whose selected original
   degrees are at least three. Choose one of its boundary edges as the
   distinguished edge; all others remain free. Its full source and
   geometry are proved in
   [the zero-subtree boundary theorem](research_all_zero_subtree_newton_packet.md)
   and [the zero-deletion geometry](research_zero_subtree_conway_geometry.md).
2. A terminal original vertex with a fixed signed power \(p\), where
   \(|p|\ge2\). Its only boundary edge is distinguished. The unified
   statement, including the exceptional powers \(2,-2\), the complete
   source estimates and the calibrated geometric action, is in
   [the terminal filling assembly](research_verified_terminal_fillings_and_long_remainder.md),
   Sections 2--4.

Choose any finite collection \(\mathscr L\) of these pieces. Repetitions
are allowed. A member \(j\) has \(q_j\) undistinguished boundary angles
\(\mathbf u\), and full original source \(F_{j,N}(t,\mathbf u)\).
For a terminal piece \(q_j=0\); for a zero subtree \(q_j\ge2\).
The known theorems state
\[
 F_{j,N}(t,\mathbf u)
 =\epsilon_{j,N}N^{-3q_j/2}A_j(t,\mathbf u)
       e^{NW_j(t,\mathbf u)}(1+O(N^{-1})),\qquad
                         |\epsilon_{j,N}|=1,            \tag{1}
\]
on a fixed holomorphic chart, and
\[
 |F_{j,N}(x+iy,\mathbf a+i\mathbf b)|
 \le C N^p\exp N\left\{
 F_{0,j}-c(1-\cos x)-c\sum_\ell(1-\cos a_\ell)
                         +C_1y^2+C_1\sum_\ell b_\ell^2\right\}. \tag{2}
\]
Here \(F_{0,j}=\Re W_j(0,\mathbf0)\). Because the collection is
finite, the positive constants and radii in these estimates can be
chosen common to it. The separate degree is at most \(N-1\) in each
spectral boundary variable.

The action and amplitude are separately even and holomorphic, with
\(A_j(0,\mathbf0)\ne0\). Write
\[
 W_{j,tt}(0,\mathbf0)=-a_j+ib_j,\qquad a_j>0,\quad b_j\in\mathbb R.
                                                               \tag{3}
\]
The other boundary Hessian entries have strictly negative real
diagonal part, with no mixed entries at zero. The geometry of each
piece identifies \(W_j\) with its absolute marked geometric action.
In particular \(\Re W_j(0)=\operatorname{Vol}_j/(2\pi)\).
A constant phase separated into \(\epsilon_{j,N}\) in (1) is retained
as exactly that scalar. For a terminal power \(p=2\sigma\), the
normalization is \(\epsilon_{j,N}=e^{\sigma i\pi N/2}\); it is not
silently incorporated into the geometric action.

Let \(j_1,\ldots,j_m\) be any sequence of members of \(\mathscr L\).
Attach their distinguished edges to one original circle, whose
degree is exactly \(m\), with no extra incidence omitted. Their
other boundary variables are kept distinct. Set
\[
 Q_{\rm out}=\sum_{\nu=1}^m q_{j_\nu},\qquad
 F_{\rm base}=\sum_{\nu=1}^m F_{0,j_\nu},\qquad
 \epsilon_N=\prod_{\nu=1}^m\epsilon_{j_\nu,N}.
\]
The original signed central source is
\[
 P_N(\mathbf U)=
 \phi_N^{(t)}\left[R^n
        \prod_{\nu=1}^mF_{j_\nu,N}(t,\mathbf u^{(\nu)})\right].
                                                               \tag{4}
\]
The central crossing occurs once. The first normals at repeated
spectral roots are those of this full product.

## 2. The composition theorem

**Theorem 1.** There is an integer \(m_0(\mathscr L)\) such that for
every fixed \(m\ge m_0(\mathscr L)\), every sequence
\(j_1,\ldots,j_m\) from the collection, and every fixed signed
integer \(n\), the entire original source (4) has the asymptotic
\[
 P_N(\mathbf U)=\epsilon_N C_{N,n}
      N^{-3(Q_{\rm out}-1)/2}\mathcal A(\mathbf U)
                    e^{N\mathcal S(\mathbf U)}(1+O(N^{-1})),     \tag{5}
\]
where \(C_{N,n}=\exp(\pi i n(N-1)^2/(4N))\).
The expansion is uniform and holomorphic near zero, at both parities,
and its amplitude is nonzero. The phase is the critical value
\[
 \mathcal S(\mathbf U)=\operatorname{stat}_t
 \left[\sum_\nu W_{j_\nu}(t,\mathbf u^{(\nu)})
                          +\frac{in}{4\pi}t^2-it\right].         \tag{6}
\]
The selected critical point is the unique one in a common small
\(t\)-disk. It is below the real axis and nonzero at \(\mathbf U=0\).
The amplitude is
\[
 \mathcal A(\mathbf U)=i\sqrt{\frac2\pi}\,
 \frac{\sin t_*(\mathbf U)\prod_\nu A_{j_\nu}(t_*,\mathbf u^{(\nu)})}
 {\sqrt{-\sum_\nu W_{j_\nu,tt}(t_*,\mathbf u^{(\nu)})
                                      -in/(2\pi)}}.             \tag{7}
\]
The square root is the Gaussian branch.

If \(Q_{\rm out}>0\), this full polynomial also satisfies
\[
 |P_N(\mathbf X+i\mathbf Y)|
 \le C N^p\exp N\left\{
 M-c_*\sum_\ell(1-\cos X_\ell)+B_*\sum_\ell Y_\ell^2\right\},
 \qquad M=\Re\mathcal S(0),                                   \tag{8}
\]
on the whole real boundary torus and a sufficiently thin fixed
complex strip. Its Hessian at zero is diagonal with strictly negative
real diagonal entries. If \(Q_{\rm out}=0\), (5) is a scalar
asymptotic with a nonzero coefficient and exponent \(3/2\).

All asymptotic constants may depend on the chosen fixed pieces,
\(m,n\). Only the eligibility threshold \(m_0\) is uniform over
their choices from the fixed collection and over the central signed
integer.

## 3. Removing only the imaginary quadratic part in the analysis

Put
\[
 A=\sum_\nu a_{j_\nu},\qquad B=\sum_\nu b_{j_\nu},\qquad
 D=2\pi A,\qquad \widetilde n=n+2\pi B .
\]
The number \(\widetilde n\) is real. It need not be an integer,
and it is not a replacement of the original crossing power.
The exact trace (4) always contains \(R^n\).

For estimates define
\[
 \widetilde W_j(t,\mathbf u)=W_j(t,\mathbf u)-\frac{ib_j}{2}t^2,
 \qquad
 Q_j(t,\mathbf u)
       =-\frac{\widetilde W_{j,t}(t,\mathbf u)}{a_jt}.
\]
Then \(Q_j(0,\mathbf0)=1\), and the apparent singularity is removable.
The central phase is identically
\[
 \sum_\nu W_{j_\nu}+\frac{in}{4\pi}t^2-it
 =\sum_\nu\widetilde W_{j_\nu}
                         +\frac{i\widetilde n}{4\pi}t^2-it.     \tag{9}
\]
This is an equality of holomorphic functions, with the original phase
and all its constants preserved.

Choose common small radii \(r<1/4,\rho>0\) in the known source and
positive geometric charts. Finiteness of the collection permits
\[
\begin{gathered}
 |Q_j-1|\le1/100,\quad |\partial_tQ_j|\le L,\quad
 \Re(-W_{j,tt})\ge a_j/2,\quad
 \Re(-W_{j,\mathbf u\mathbf u})\ge\beta I,\\
 \|W_{j,t\mathbf u}\|\le B_1|t|,\qquad A_j\ne0.                 \tag{10}
\end{gathered}
\]
The external-variable conditions are empty for terminal pieces.
If the collection consists only of terminals, take \(B_1=0\)
and any \(\beta>0\).

Let \(a_{\min}=\min_j a_j>0\), \(b_{\max}=\max_j|b_j|\),
\(d_{\min}=2\pi a_{\min}\), and \(q_{\max}=\max_jq_j\).
Set \(a=r/2\), \(c_0=c(1-\cos(a/2))\), \(k_0=2c/\pi^2\).
Shrink \(\rho\) so that, for every member,
\[
 |W_j(0,\mathbf u)-W_j(0,\mathbf0)|\le c_0/4,\qquad
 C_1q_{\max}\rho^2\le c_0/4.                               \tag{11}
\]
If there are no outside variables, these requirements are empty.

A sufficient threshold is obtained by taking the inequalities (12) of
[the repeated zero-block proof](research_amplified_zero_block_source.md)
with \(\kappa,\ d_0,\ B\) there replaced by
\(a_{\min},\ d_{\min},\ B_1\), and replacing its \(K_0\) by
\[
 K_{\mathscr L}
 =\frac{49}{d_{\min}^2}
                  \left(C_1+\frac{b_{\max}^2}{2k_0}\right)
                              +\frac{49}{32\pi^2k_0}.          \tag{12}
\]
Its last inequality involving \(s_0=1-\cos\rho\) is needed only
when outside variables occur. All these are finitely many explicit
inequalities in constants of the fixed collection.

For charge \(0\le\lambda\le1\), let
\[
 \overline Q=\frac1A\sum_\nu a_{j_\nu}Q_{j_\nu},\qquad
                         R=(D^2+\widetilde n^2)^{1/2}.
\]
The critical equation becomes
\[
             t=\frac{-2\pi i\lambda}{D\overline Q-i\widetilde n}.
                                                               \tag{13}
\]
The same contraction proof gives
\[
 |t_\lambda|\le\frac{7\lambda}{R},\qquad
 0<-\Im t_\lambda\le\frac{7\lambda D}{R^2},
 \qquad
 0<F_{\rm base}-M\le\frac{7D}{2R^2}
                              \le\frac7{2d_{\min}m}.           \tag{14}
\]
The first two estimates and the corresponding loss relative to
\(\sum_\nu\Re W_{j_\nu}(0,\mathbf u^{(\nu)})\) hold throughout
the small complex boundary polydisk. In particular no cancellation
between \(n\) and \(2\pi B\) makes the critical point large:
\(D\ge d_{\min}m\) remains positive.

## 4. Whole-source control with the original signed power

Apply the exact original midpoint trace to the product in (4).
The identity and all its terms are (18) in the repeated zero-block
proof. Its chirp is \(e^{inNt^2/(4\pi)}\), with the original \(n\);
its carrier is \(C_{N,n}\). Formula (9) is used only to estimate
the total analytic phase inside this exact identity.

The original outer trace points are bounded with the global estimate
(2) and Markov's inequality on the fixed spectral interval, exactly
as in Section 5 of that proof. Equations (11),(14) put them strictly
below the selected action. In the central rectangle use the full
holomorphic product (1). Its total phase has
\[
 \Re\Phi_{tt}\le-A/2<0.
\]
Thus the lower horizontal contour has one nondegenerate maximum.
The complete rational charge denominator suppresses all its higher
charges. Folding the vertical current by oddness and using convexity
in its depth gives a strict gap at both endpoints and hence throughout
the vertical current. This proves (5)--(7), including the nonzero
amplitude. The power is
\[
 N^{-3Q_{\rm out}/2}\,N^2\,N^{-1/2}
                                  =N^{-3(Q_{\rm out}-1)/2}.
\]
The scalar \(\epsilon_N\) is simply the product in (1), retained
outside the exact central trace.

It remains to check the global bound; this is where using the original
power rather than merely the effective one matters. For arbitrary real
outside angles, write \(T=\sum_\ell(1-\cos U_\ell)\) and
\(h=-\Im t_*(0)\). The full global bound (2) on the center contours
has rate at most
\[
 F_{\rm base}-cT-mk_0x^2+mC_1v^2
                           +\frac{|n|}{2\pi}|x|v-v,
                  \qquad 0\le v\le h.
\]
Completing the square and dropping the helpful last term gives
\[
 F_{\rm base}-cT+mC_1h^2+\frac{n^2h^2}{16\pi^2mk_0}.       \tag{15}
\]
Now \(|B|\le mb_{\max}\), and \(n=\widetilde n-2\pi B\), so
\[
 n^2\le2\widetilde n^2+8\pi^2m^2b_{\max}^2.
\]
Together with \(h\le7D/(D^2+\widetilde n^2)\), this proves
\[
 mC_1h^2+\frac{n^2h^2}{16\pi^2mk_0}
                                      \le\frac{K_{\mathscr L}}m. \tag{16}
\]
This bound is uniform over the original signed \(n\) and all choices
of members of the collection. It controls every central contour piece,
not just the stationary integral. At an outside angle of size at least
\(\rho\), \(T\ge1-\cos\rho\), so the threshold in Section 3
absorbs (16) and the action loss (14) into half of the global angular
loss.

Near zero the Schur complement is the block diagonal external Hessian
minus \(vv^T/\Phi_{tt}\), where
\(\|v\|^2\le mB_1^2|t_*|^2\). Consequently
\[
 \left\|\frac{vv^T}{\Phi_{tt}}\right\|
 \le\frac{2B_1^2|t_*|^2}{a_{\min}}
 \le\frac{98B_1^2}{a_{\min}D^2}.
\]
The selected threshold makes this at most \(\beta/2\). The local
strict real Hessian and the far-angle bound therefore combine exactly
as before. Polynomial Bernstein--Walsh continuation away from zero,
and the local holomorphic quadratic estimate near zero, yield (8).
At zero every mixed \(t,u_\ell\) derivative vanishes by separate
evenness, giving the stated diagonal Hessian without a Schur correction.

This proves Theorem 1 for the actual finite collection in Section 1.
No norm estimate for a crossing operator, and no suppression of the
forced polynomial evaluation defect, was assumed.

## 5. Geometric scope and the scalar terminal case

Every chosen piece has its original positive deformed cell description
and primitive boundary curves. Fill its selected vertices first, leaving
its distinguished circle complete. Glue the resulting annular sectors
at the center in their original cyclic order. Their meridian periods
add, their common primitive longitude remains \(V=2it\), and the
central carrier is inserted once. Thus
\[
 U+p_vV=-2\pi\left(\sum_\nu W_{j_\nu,t}
                                      +\frac{in}{2\pi}t\right).
                                                               \tag{17}
\]
The complete volume is \(2\pi F_{\rm base}\).
The fixed common positive chart in (10), the charge bound (14),
and the positive length \(-2\Im t_\lambda\) identify the full path
with the original primitive filling. Schläfli's formula gives absolute
filled volume \(2\pi M\). When outside angles remain, the same
marked positive charts continue in them and provide the geometry for
the complex-phase long-filling theorem.

The marked geometric assembly is detailed in
[the finite-collection filling geometry](research_amplified_marked_block_geometry.md).
It treats the previously calibrated terminal actions and their
unit scalars separately, including the powers \(2,-2\).

**Corollary 2.** Choose a finite set
\(\mathscr P\subset\{p\in\mathbb Z:|p|\ge2\}\).
There is \(m_0(\mathscr P)\) such that every original star template
with \(m\ge m_0(\mathscr P)\) terminal powers chosen arbitrarily
from \(\mathscr P\), and with any fixed signed central power \(n\),
has a nonzero original full source asymptotic of the form
\[
               \Omega_N N^{3/2}D_0e^{NS},
                  \qquad |\Omega_N|=1,\quad D_0\ne0,     \tag{18}
\]
with relative error \(O(N^{-1})\), through all large integer levels.
When its original component and carrier pattern gives a knot,
that knot is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                         =\operatorname{Vol}(S^3\setminus K).   \tag{19}
\]
Here all crossing powers, including the center, are fixed before
\(N\to\infty\). No circle remains to receive a long filling.

More generally, mixing terminal pieces with the zero-subtree pieces
in Section 1 gives the same volume identity after independently
sufficiently long fixed fillings at the remaining original circles.
The pre-filling exponent is \(-3(r-1)/2\): if the selected region
has \(Q_{\rm out}\) boundary edges and there are \(r\) remaining
vertices, then \(e_0+Q_{\rm out}=r\), where \(e_0\) counts untouched
edges. The remaining traces again yield a final \(N^{3/2}\).

The finite-set qualification matters. This note does not give a
threshold uniform over all possible terminal powers, over an unbounded
collection of zero blocks, or over arbitrary connected short fillings.
It proves closure for arbitrarily many pieces from any fixed finite
collection, with every original scalar, boundary variable, and normal
retained.

