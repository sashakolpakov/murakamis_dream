# Full opposite-source routing and its diagonal framing factor

Private written proof, 18 November 2026.

The actual fixed routing of the opposite kernel has an explicit
classical composition in every width. Its turned tuple is an inverse
full half twist, with a specified common conjugator sending the old
opposite total eigenline to the selected axis. The quotient recut is
an explicit upper-unipotent operation. Returning the presentation
leaves the opposite-eigenflag map multiplied by a nontrivial diagonal
factor, which supplies the correct common-moment symplectic lift.

The finite turnover/degree kernel, all original scalars and the exact
source normalization are retained. This graph identity is not a
composition estimate or a map of the original relative cycles.
The five complete directs A, I, J, R, C are pinned below.

## 1. The exact routing and the complete turnover/degree kernel

Use \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(m=r+1\), and \(x=-M/q\). J defines the actual maps
\[
 q_F=p_0S_m^{-1},\qquad i_F=i_0,\qquad
 T(M)=q_F(M)E_\Sigma(M)^d\mathscr C_m(M)i_0.
 \tag{1}
\]
The right input is the reflected meridian space \(M^{-1}\).
The analytic graph calibration below fixes \(r\ge2\); the finite
routing identities also hold for \(r=1\) wherever defined.
The balanced one-head turnover is
\[
 C(M)w_a=\prod_{j=1}^a\frac{MQ^j-M^{-1}}{1-Q^j}\,w_{d-a},
 \qquad \mathscr C_r(M)=C(M)^{\otimes r}\mathsf J_r ,
\]
where \(\mathsf J_r\) reverses tensor factors. In particular
\(C(1)w_a=(-1)^a w_{d-a}\).

Let \(\tau=\sigma_1\cdots\sigma_r\), with the rightmost operator
acting first, and let \(\mathsf n\) be remaining total occupation.
Put \(i_dv=w_d\otimes v\) and \(A_N=q_FE_\Sigma^di_d\).
R's actual positive checked crossing has zero transfer when its
second input is \(w_d\): the raising endpoint forbids every positive
transfer. Its remaining coefficient is
\(\kappa x^{-a-d}Q^{ad}\). Applying this successively gives
\[
 W_\tau i_{{\rm last},d}=i_dD_{\rm top},\qquad
 D_{\rm top}=\kappa^r x^{-rd}(x^{-1}Q^{-1})^{\mathsf n}.
 \tag{2}
\]
Also \(\mathscr C_m i_0=i_{{\rm last},d}\mathscr C_r\).
The total intertwining and quotient identity \(q_FW=B_m(W)q_F\)
in J,R therefore prove, with this order,
\[
 \boxed{\quad
 T(M)=B_m(W_\tau^{-1})\,A_N(M)\,D_{\rm top}(M)\,
                                \mathscr C_r(M).
 \quad} \tag{3}
\]
No gauge or scalar has been inserted in this factorization.

Now specialize to \(M=1\), keeping the root quantum parameter.
Since \(x^{-1}Q^{-1}=x=-q^{-1}\), on an input of total degree \(k\)
the last two factors in (3) have coefficient
\[
 \kappa^r x^{-rd}x^{rd-k}(-1)^k=\kappa^r q^k.
\]
Let \(\mathsf W_r|\mathbf a\rangle
=|d-a_r,\ldots,d-a_1\rangle\), with no sign. Then exactly
\[
 \boxed{\quad D_{\rm top}(1)\mathscr C_r(1)
                  =\kappa^r\mathsf W_r q^{\mathsf n}.\quad}
 \tag{4}
\]
With the original ordinary-binomial input and monomial output,
its full finite coherent kernel is consequently
\[
 \boxed{\quad
 v(\mathbf w)D_{\rm top}\mathscr C_r c(\mathbf z)
     =\kappa^r\prod_{i=1}^r(w_{r+1-i}+qz_i)^d .
 \quad} \tag{5}
\]
This is a binomial identity with every head cap \(0\le a_i\le d\).
The physical degree passes from \(k\) to \(rd-k\).
Thus the Gauss estimate A, which acts on a degree \(T\le d\)
in its specified upper chamber, occurs in (3) at
\[
                              T=rd-k .
 \tag{6}
\]
It is not an estimate for every incoming degree of \(T(M)\).

Formula (4) is only a root identity. Away from \(M=1\) the
entire factors in (2),(3) are used before taking a meridian normal.
Neither the balanced coefficients nor \(q^{\mathsf n}\), \(\kappa\),
or an external framing line is removed from the source.

## 2. Negative Chevalley and the explicitly turned tail

All remaining equations in the graph calculation are principal
complete equations. Use A's correctly polarized physical input
symbols, dressed heads \(H_i\), and ordered totals
\[
 P=H_r\cdots H_1=
 \begin{pmatrix}K&E\\KF&K^{-1}+EF\end{pmatrix}.
 \tag{7}
\]
The principal map of (4),(5) is negative Chevalley with reversal:
\[
 (K_i,E_i,F_i)\longmapsto
       (K_{r+1-i}^{-1},-F_{r+1-i},-E_{r+1-i}),
\]
so its full totals are
\[
                 (K,E,F)\longmapsto(K^{-1},-F,-E).
 \tag{8}
\]
One can check the signs without a coherent approximation.
At the root \(\mathscr C_r E=F\mathscr C_r\),
\(\mathscr C_r F=E\mathscr C_r\); moving \(D_{\rm top}\)
past a raising or lowering arrow supplies \(x\) or \(x^{-1}\).
Both have principal value \(-1\).
The exact \(q\)-half shift remains in (4),(5).

The based labels also matter. Put
\[
 {\cal W}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 b_i^-=\begin{pmatrix}1&0\\-K_iF_i&K_i\end{pmatrix},
 \quad b_i^+=\begin{pmatrix}K_i&E_i\\0&1\end{pmatrix}.
\]
For the turned head at position \(r+1-j\), (8) is exactly
\[
 (b_{r+1-j}^+)'={\cal W}(b_j^-)^{-1}{\cal W}^{-1},
 \qquad
 (b_{r+1-j}^-)'={\cal W}(b_j^+)^{-1}{\cal W}^{-1}.
 \tag{9}
\]
Define the inverse-half-twist tuple of the tail by
\[
 {\cal I}_r(H)_{r+1-j}
   =(H_r\cdots H_{j+1})H_j(H_r\cdots H_{j+1})^{-1}.
 \tag{10}
\]
Then the actual turned based tuple is
\[
 H_i^{B}=g_B{\cal I}_r(H)_i g_B^{-1},\qquad
 g_B={\cal W}B_r^-=
          \begin{pmatrix}KF&-K\\1&0\end{pmatrix},
 \quad B_r^-=b_r^-\cdots b_1^- .
 \tag{11}
\]

Here is an explicit product proof. For \(i=r+1-j\), cancellation
of the turned minus prefixes in (9) gives
\[
 H_i^B={\cal W}L_j b_j^+(b_j^-)^{-1}L_j^{-1}{\cal W}^{-1},
 \qquad L_j=b_r^+\cdots b_{j+1}^+ .
\]
Conjugating this by \(g_B^{-1}\) leaves
\((B_r^-)^{-1}L_j b_j^+(b_j^-)^{-1}L_j^{-1}B_r^-\).
On the other hand
\(H_r\cdots H_{j+1}=(B_r^-)^{-1}L_jB_j^-\).
Inserting the definition of \(H_j\) proves exactly (10),(11).
No unchanged-label interpretation of the turnover is made.

## 3. Insert the actual Gauss graph

Work first on \(K^2\ne1,\ E F\ne0\), with the requisite prefix
pivots units, and write
\[
                             D=K-K^{-1}.
\]
A identifies the actual local Gauss graph, modulo the fixed-degree
common frame, with its specified rational representative
\[
 g_A(K,E,F)=
 \begin{pmatrix}
 0&(1-K^{-2})/F\\
 -F/(1-K^{-2})&1-EF/[K(1-K^{-2})]
 \end{pmatrix}.
 \tag{12}
\]
This representative is the one generated by A's marked factorial
Hamiltonian. Section 5 below calibrates its common moment against
I's actual marked complex-degree interpolant, at fixed physical
input. This is a phase-graph calibration, not evaluation of its
degree contour.

Apply (12) to the turned totals (8). Direct multiplication gives
\[
 \begin{split}
 g_A(K^{-1},-F,-E)&=
 \begin{pmatrix}0&KD/E\\-E/(KD)&1+EF/D\end{pmatrix},\\
 g_{AB}:=g_A(K^{-1},-F,-E)g_B
       &=\boxed{\begin{pmatrix}KD/E&0\\1&E/D\end{pmatrix}}.
 \end{split} \tag{13}
\]
Thus the tail after these three factors is
\[
 H_i^A=g_{AB}{\cal I}_r(H)_i g_{AB}^{-1},
\]
and its totals are
\[
 K_A=K^{-1},\qquad E_A=KD^2/E,\qquad
 F_A=FE^2/(KD^2).
 \tag{14}
\]
Both the order of the diagonal factor and the reversal in (11)
are used in this cancellation.

Equation (13) is a graph composition. A's actual amplitude estimate
applies only where its transformed coherent arguments lie in its
proved chart. No estimate for the full integral (3) follows from
this matrix multiplication.

## 4. The inverse routing on the full tuple

C's actual quotient section lifts a remaining tuple to
\[
 X_0=\begin{pmatrix}-1&0\\-F&-1\end{pmatrix},\qquad
 X_j=h_0H_jh_0^{-1}\ (1\le j\le r),\qquad
 h_0=\begin{pmatrix}1&0\\F&-1\end{pmatrix}=h_0^{-1}.
 \tag{15}
\]
Its full product is
\[
 P_{\rm full}=X_r\cdots X_0
                =\begin{pmatrix}-K&E\\0&-K^{-1}\end{pmatrix}.
\]
Lift the tuple in (14) by the same rule, with \(F\) replaced by
\(F_A\), and denote its heads by \(Y_0,Y_1,\ldots,Y_r\).
Let \(h_A=\left(\begin{smallmatrix}1&0\\F_A&-1\end{smallmatrix}\right)\).
The combined full-frame matrix is
\[
 g_{\rm full}=h_Ag_{AB}h_0^{-1}
                 =\boxed{\begin{pmatrix}KD/E&0\\-1&E/D\end{pmatrix}}.
 \tag{16}
\]
In obtaining its lower-left entry, use \(F_AKD/E=FE/D\).

For \(i\ge1\), (11),(13),(15) already identify \(Y_i\) with
the corresponding turned tail head conjugated by \(g_{\rm full}\).
The exposed head also agrees:
\[
                         Y_0=g_{\rm full}X_0g_{\rm full}^{-1}.
 \tag{17}
\]
Indeed a lower triangular conjugator with diagonal entries \(a,b\)
scales \(e_{21}\) by \(b/a\); here \(b/a=E^2/(KD^2)\),
giving exactly \(F_A\). This proves the missing exposed-head
incidence, not merely equality of tail characters.

R's positive Hurwitz convention is
\((X,Y)\mapsto(X^{-1}YX,X)\). Its inverse is
\((X,Y)\mapsto(Y,YXY^{-1})\).
Because \(\tau^{-1}=\sigma_r^{-1}\cdots\sigma_1^{-1}\)
acts at positions \(1,2,\ldots,r\) in that order, it sends
\[
 (Y_0,Y_1,\ldots,Y_r)\longmapsto
 (Y_1,\ldots,Y_r,\ (Y_r\cdots Y_1)Y_0(Y_r\cdots Y_1)^{-1}).
 \tag{18}
\]
Using (17) and the product preservation of the tail half twist
in (10), this is exactly
\[
 \boxed{\quad
       g_{\rm full}\,{\cal I}_m(X)\,g_{\rm full}^{-1},
 \quad
 {\cal I}_m(X)_{r-j}
   =(X_r\cdots X_{j+1})X_j(X_r\cdots X_{j+1})^{-1}.
 \quad} \tag{19}
\]
This is the full tuple statement in its original order.
It proves the routing identity before the quotient recut.

For clarity the corresponding positive half twist is
\[
 \Delta_m=(\sigma_1\cdots\sigma_r)
          (\sigma_1\cdots\sigma_{r-1})\cdots\sigma_1.
\]
Its inverse has action (19): induction using (18) moves the first
head last and applies the same operation to the remaining heads.
The positive \(\Delta_m\) returns (19) to its input presentation.

## 5. Quotient recut, eigenflag, and the common-moment lift

The full source flag must be recut after (18). Let \([v_1:v_2]\)
be the selected flag of \(X_r\). Its image under (16) has affine
coordinate
\[
 p_*=\frac{(KD/E)v_1}{-v_1+(E/D)v_2}.
 \tag{20}
\]
On the chart where this denominator is nonzero, C's quotient
section applies the actual upper-unipotent conjugation
\(U(-p_*)=\left(\begin{smallmatrix}1&-p_*\\0&1\end{smallmatrix}\right)\).
Thus the lifted section of the final reduced output of (3) is
\[
 U(-p_*)g_{\rm full}\,{\cal I}_m(X)\,
                     g_{\rm full}^{-1}U(p_*).
 \tag{21}
\]
The lower-left entry of its first meridian, and hence its required
new \(h_0\), is retained. This is not resetting the source cut
without a transformation. Its total tail Cartan is \(K^{-1}\);
the upper full-product entry in this section is \(E_A+p_*D\).

The old opposite total eigenline in (15) is \([E/D:1]\).
Equation (16) sends it to \(e_1\):
\[
                     g_{\rm full}[E/D,1]^t=[K,0]^t .
 \tag{22}
\]
It keeps the old first-meridian flag \(e_2\). For complete
discrete faithful regular-total data, C proves that a parabolic
meridian flag cannot equal either loxodromic total eigenline.
Thus \(E,F,D\) and the denominator in (20) are units at these
geometric frames. This is algebraic regularity, not membership
in the estimated coherent sector.

Apply the actual positive half-twist presentation return to (21).
Hurwitz transformations commute with common conjugation, so its
full tuple is \(U(-p_*)g_{\rm full}Xg_{\rm full}^{-1}U(p_*)\).
Its first selected flag is now \([-p_*:1]\).
The quotient recut is \(U(p_*)\), exactly cancelling the first
one. The returned full tuple is therefore
\(g_{\rm full}Xg_{\rm full}^{-1}\). Returning to its remaining
section gives
\[
                         H_i^{\rm ret}=g_{AB}H_i g_{AB}^{-1}.
 \tag{23}
\]

A's opposite-eigenflag map, with the old first-meridian flag fixed,
has representative
\[
 \ell=\begin{pmatrix}1&0\\D/E&1\end{pmatrix},\qquad
 (K,E,F)\mapsto(K^{-1},E,F).
\]
Equations (13),(23) prove the precise comparison
\[
 \boxed{\quad
 g_{AB}\ \sim\ \operatorname{diag}(\zeta,1)\ell,\qquad
 \zeta=\frac{KD^2}{E^2},\qquad
 (K,E,F)_{\rm ret}=
       \left(K^{-1},\,\frac{KD^2}{E},\,\frac{FE^2}{KD^2}\right).
 \quad} \tag{24}
\]
Here \(\sim\) means a scalar multiple of a matrix, which leaves
conjugation unchanged. No diagonal factor has been discarded.

This factor is necessary in the full common-moment variables.
The brackets in A give \(\{\log K,\log E\}=1\).
For (24),
\[
 \log K'=-\log K,\qquad
 \log E'=\log K+2\Log D-\log E ,
 \qquad \{\log K',\log E'\}=1.
 \tag{25}
\]
In contrast the bare map \(K'=K^{-1},E'=E\) would give \(-1\).
It is the opposite flag map on the fixed-moment quotient, not
the unqualified symplectic lift of that map. Under common diagonal
scaling \(E\mapsto aE,\ F\mapsto a^{-1}F\), the returned \(E'\)
scales by \(a^{-1}\), as required by the reversed moment.
This is the explicit common-frame character of the chosen lift.

### Actual common-moment calibration

A proves its graph on the fixed-degree quotient. To fix the remaining
common diagonal lift we now use the actual marked phase in I, rather
than adding an arbitrary function of the total moment. This calculation
takes place on the nonzero small-input sector where I proves a genuine
unit; no asymptotic estimate is taken to its puncture.

Use \(c_0=2\pi i\), \(\sigma=(T+1)/N\), \(C=e^{-c_0\sigma}\),
and, for this calculation, the variables of the input to \(A_N\).
In particular \(K=(-1)^r C\). I retains exactly
\[
 \begin{split}
 \mathfrak a_{00,N}^{(r)}
  &=(-1)^d(x^rQC)^d\widehat F_N(N\sigma-1)^2\nu_r(\sigma),\\
 \mathfrak b_N
  &=\frac{\Gamma(N)}
     {\Gamma(N\sigma)\Gamma(N(1-\sigma)+1)},\\
 \mathfrak P_N
  &=\mathfrak a_{00,N}^{(r)}
       e^{(N\sigma-1)\mathfrak l}\mathfrak b_N\mathfrak U_N,
       \qquad \mathfrak l=\Log(w_rz_r).
 \end{split} \tag{25a}
\]
Here \(\nu_r=N^{r-2}\) times a holomorphic unit with fixed
derivatives bounded independently of \(N\), as specified in I.
The marked factorial has phase
\[
 I(\sigma)=\frac{\operatorname{Li}_2(1)
                    -\operatorname{Li}_2(e^{c_0\sigma})}{c_0},
 \qquad I'(\sigma)=\Log(1-C^{-1}).
\]
Its marks are those of the exact \(\widehat F_N\), not a newly
chosen branch. Consequently the extensive phase of (25a), up to
a constant independent of \(\sigma\), is
\[
 \chi=\Log K+2I(\sigma)+h(\sigma)+\sigma\mathfrak l
                           +S(\rho,\xi;\sigma),\qquad
 h=-\sigma\Log\sigma-(1-\sigma)\Log(1-\sigma).
 \tag{25b}
\]
All \(d=N-1\), \(Q,q\), \(\tau=\sigma-1/N\), and width factors
remain in the exact formula (25a). They give the specified
subprincipal factors; none is changed to calibrate (25b).

Differentiation here fixes the physical input \(\xi\), not I's
bundle coordinate \(a_*\). In I's bundle
\(\xi_i=\vartheta_i a_*^2/[(2/c_0)b_\sigma]\), where
\(b_\sigma=\sigma/(1-\sigma)\). Therefore the required derivative is
\[
 \left.\partial_\sigma\right|_\xi
 =\left.\partial_\sigma\right|_{a_*,\vartheta}
       +\frac{a_*}{2\sigma(1-\sigma)}\partial_{a_*}.
 \tag{25c}
\]
This correction is part of the actual fixed-input degree contour.

At the output axis, A and I give the actual boundary phase
\[
 S(0,\xi;\sigma)=\phi(t;C)+S_B(\xi/t;\sigma),
 \quad
 \frac{U}{1+U}+\sum_{i<r}\frac{U\xi_i}{t+U\xi_i}=\sigma ,
\]
at its selected \(t\)-saddle. The function \(Y(0)=1\) satisfies
\[
 CY^2-(1+C-t)Y+1-Ct=0,\qquad
 c_0t\phi_t=\Log Y-\Log(1-t),\qquad \phi(0;C)=0.
 \tag{25d}
\]
The second equation also follows directly from A's
\(e^{-c_0p_r}=CY/(1-t)\) and \(p_r=\sigma-t\phi_t\).
The binomial envelope at fixed \(\xi,t\) has derivative
\(\partial_\sigma S_B=-\Log U+\Log b_\sigma\).
Its \(+\Log b_\sigma\) cancels \(h'=-\Log b_\sigma\).
The \(t\)-derivative cancels by the actual saddle equation.
Thus the full logarithmic normal is
\[
 \boxed{\quad
 \chi_\sigma=-c_0+2\Log(1-C^{-1})+\mathfrak l
                        +\phi_\sigma-\Log U .
 \quad} \tag{25e}
\]
The displayed \(-c_0\) is retained; exponentiating it does not
authorize changing the marked action.

There is an elementary closed form for the remaining derivative:
\[
 \boxed{\quad
 \exp\phi_\sigma
   =\frac{(1-CY)^2}{(C-1)(CY+Ct-1)} .
 \quad} \tag{25f}
\]
To prove it, put \(\Delta=2CY-(1+C-t)\). Differentiation of
(25d) gives
\[
 Y_t=(C-Y)/\Delta,\qquad
 Y_C=-(Y^2-Y-t)/\Delta,\qquad
 \partial_t\phi_\sigma=-CY_C/(tY).
\]
The \(t\)-derivative of the logarithm on the right of (25f) is
the last expression: multiply by
\(tY\Delta(1-CY)(CY+Ct-1)\) and use the quadratic in (25d).
Both logarithms have value zero at \(t=0\). This last evaluation
uses the analytic phase germ only, whose existence and normalization
are proved in A,I. It is not a limit of the punctured-sector amplitude.
Continue the resulting identity to the nonzero selected saddle.

It follows that the exponentiated common-moment stationarity is
precisely
\[
 \boxed{\quad
 e^{\chi_\sigma}=1
 \quad\Longleftrightarrow\quad
 w_rz_r=\frac{U C^2(CY+Ct-1)}
                    {(C-1)(1-CY)^2}.
 \quad} \tag{25g}
\]
This is the missing full covector of the representative (12).
Indeed A's boundary input totals, with \(a=z_r/U\), are
\[
 E=a(CY+Ct-1),\qquad
 F=-\frac{(-1)^r}{aCt}(C-t-CY).
\]
Its output has
\(F'=(-1)^{r-1}w_r(1-C^{-1})\), while (12) gives
\(F'=-EF^2/[K(1-K^{-2})^2]\). Substituting and using
\[
             (1-CY)(C-t-CY)=(C^2-1)t
\]
gives exactly (25g), including its sign and the ordinary-binomial
input factor \(U\).

At fixed \(\sigma\), A already matches all reduced covectors and
proves analytic uniqueness of the mixed generating function.
Two symplectic lifts of that same reduced graph can differ only by
a common diagonal displacement depending on \(\sigma\): in Darboux
coordinates its difference is \(f(\sigma)\,d\sigma\), since equality
of all reduced derivatives removes dependence on the other variables.
The actual boundary calculation (25e)--(25g) fixes this displacement.
Compatibility and the analytic uniqueness in A,I propagate it over
the connected estimated chart. Equations (16),(24),(25) therefore
give the full exponentiated canonical lift selected by the actual
marked complex-degree phase, wherever that phase and the routing
charts apply. No unknown moment function has been discarded.

The logarithmic equations \(\chi_\sigma=c_0j\), \(j\in\mathbb Z\),
still distinguish degree Fourier aliases of the same exponentiated
seam. I's finite degree contour, its connectors, excluded degree
blocks and homogeneous logarithmic character retain those aliases.
Likewise the exact \(q^k\) in (4) is an order-one phase when \(k=O(N)\);
it remains a subprincipal source factor. This calibration does not
select a radial stationary cycle or estimate its coefficient.

## 6. Original source and remaining analytic burden

The root routing proves a universal algebraic component, not an
identity of asymptotic contributions. Its physical total-degree
complement is exact:
\[
 T(1)U_k\subset U_{rd-k},\qquad
 x^rQ^{-(rd-k)}=(x^rQ^{-k})^{-1}.
\]
The half-twist return is an actual degree-preserving reduced braid.
R,J supply its unmarked source conjugation and retain the differentiated
commutator for the first meridian source row. For inserted marks or
relative windows their transformations must be performed in the same
order; no separate cut-reset invariance is asserted.

In particular the original normalized kernel is still
\[
 J(M)=D_N(MK_{\rm r}(M))^{-1}T(M),
\]
and J's exact sewing expression remains
\[
 \Phi_0(W_\beta(M))=
 \frac{D_N(M)}{a_N(M)}
 \operatorname{Tr}\!\left[
 J(M)B_{\beta^{\rm rev}}(M^{-1})J(M^{-1})\right],
 \quad
 a_N=(-1)^dN\left((-1)^dD_N(M)/N\right)^m.
 \tag{26}
\]
All meromorphic factors have the continuation prescribed by this
actual source. The Cartan factor in (26) is not replaced by a unit
amplitude, and the root graph calculation is not differentiated
as a whole-meridian identity.

Likewise a choice of local coherent windows retains the finite
defect \(P_{\mathcal C}T-TP_{\mathcal D}\) and the complementary
resolutions in J. Equations (19),(22),(24) do not set that defect
to zero. They neither remove root-zero Gauss primary channels
nor their nonzero first normals. At a nonreal geometric moment,
a physical upper/lower primary label cannot be assigned without
the same retained marked continuation.

A concrete composition estimate still has to put the transformed
arguments of (5),(12), the actual reduced braid factors in (3),
and the final half-twist return into compatible analytic charts,
or transport their original capped contours with estimates of all
complements. The graph has no extra algebraic flag obstruction at
the complete regular geometric frame, but its coefficient has
not been continued there by this proof. No volume or original
relative-cycle noncancellation conclusion is inferred.

## Complete proof-source pins

* A: notes/research_actual_gauss_collective_canonical_graph.md,
  532 lines, SHA256 8ca0a51e9c2f3c11854e33809a349772d373b3da555286109acdbbc122e6b9bb.
* I: notes/research_fixed_width_coherent_complex_degree_interpolation.md,
  623 lines, SHA256 abd8009aa0e0e729efe82450a4f838fe1bdf250574cedf82a7c84a51e2e1de8e.
* J: notes/research_opposite_polarization_source_kernel.md,
  639 lines, SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* C: notes/research_actual_reduced_braid_critical_scheme.md,
  564 lines, SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

The complete I, J and R were freshly wholly read in this author
sequence. The complete matching A and C reads from the immediately
preceding collective-graph author/formal sequence are retained
fresh and unchanged. Every used implication was checked. The entire
matching final was reread nontruncated and all six hashes renewed.
Independent peer review and root adoption remain separate.
All additional finite-kernel,
matrix routing and recut identities above are written proofs.
No mathematical programs were used. Frozen and public files
were not edited.

