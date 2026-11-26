# Parameter-leading projected recovery for an inner endpoint product

Private written proof, 16 November 2026.

An inner turn of a product of endpoint kernels does not retain the
scalar leading operator used in the single-kernel window theorem.
After coupling to another received source, that operator is a
connection-twisted matrix operator. This note gives a different
finite-window argument: ordinary polynomial division supplies a
finite chain of exact recovery rows. The chain recovers the original
packet generically, although the auxiliary quotient packets need not
have full column rank.

The supplied data include the terminalized inner-block sources,
fixed-degree remainder sources, and both collars of every auxiliary
quotient packet. Their actual rates remain in the estimate. In
particular this is not a recovery theorem using only the original
packet's collars, or a repeated-turn filled-action bound.

## 1. Source, parameters, and retained packets

All fixed data below are independent of the level. We work at
sufficiently large \(N\ge3\); the claim is an asymptotic
conditioning statement, not an additional assertion at \(N=2\).
Use
\[
 h=N^{-1},\quad q=e^{\pi ih},\quad D=N-1,\quad
 c_0=q+q^{-1},\quad \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad C f=Zf,
\]
\[
 c_a=q^{2a+1}+q^{-2a-1},\quad
 S_j=\prod_{\ell=1}^j2\sin(\ell\pi/N),\quad S_0=1,\qquad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),
\]
\[
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\quad
 Te_j=e_{D-j},\quad J=TCT,\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n}.
 \tag{1}
\]
Multiplication and all operator identities in \(\mathcal A_N\)
retain the original double-root normals. Free endpoint parameters
are not quotiented. The original trace is
\(\phi_N(e_a e_b)=\mathbf1_{a+b=D}\).

Fix \(r\ge1\), an integer \(n\), and \(\tau\in\{1,-1\}\).
The inner block is
\[
 P=\operatorname{can}\prod_{i=1}^r k_i,\qquad
 k_i=K_N(w_i,\cdot),\qquad w_i=2\cosh(\alpha_i/N).
 \tag{2}
\]
The \(w_i\) are initially independent, and the microscopic
parameters range over fixed bounded complex sets. There is a fixed
received full-step state \(y\), independent of these parameters,
with exact rational companion
\[
                         Ey=M(v)y,\qquad E:v\mapsto q^2v.
 \tag{3}
\]
Its inverse and its fixed shifts are rational on the coefficient
chart being used. The complete source/recovery state is retained
when forming (3); an inhomogeneous channel is not discarded.
The full-step interface supplies such states for fixed products
of the already turned inputs under consideration. Extra ordinary
spectators may remain as free coefficients throughout.

The target includes
\[
                  U_\tau\operatorname{can}\bigl[(V_nP)y_\nu\bigr],
                       \qquad U_\tau=V_\tau ,
 \tag{4}
\]
and the other fixed shifted, mirrored, and descended coordinates
required below. No factor in (4) is replaced by an endpoint product.

Write \(C=v+v^{-1}\), \(W=v-v^{-1}\). The exact full-step lift is
\[
 \mathcal B_N=\mathbb C[v,v^{-1}]/((v^N+1)^2)
                =\mathcal A_N\oplus W\mathcal A_N .
 \tag{5}
\]
Even/odd descent means
\((X+\iota X)/2,(X-\iota X)/(2W)\), with
\(\iota:v\mapsto v^{-1}\), using ordinary Laurent division before
reduction. It preserves the odd ramified first jet as well.
All normal rows are derivatives of ordinary cleared residuals at
physical roots, not applications of a derivation to the quotient.

## 2. A parameter-leading row before the inner turn

For the original kernel the exact full-quotient equation is
\[
              (w_i-J)k_i=p_i g,\qquad
              p_i=P_N(w_i),\quad g=\eta h^2e_D.
 \tag{6}
\]
In the full-step chart,
\[
 J=r_*(v)-A(v)E-B(v)E^{-1},\qquad r_*=\frac8{C+c_0},
\]
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\qquad
 B(v)=A(v^{-1}).
 \tag{7}
\]
Choose an index \(i\). Form the finite tensor of the two kernel
coordinates for the other factors. Its homogeneous transfer is
independent of \(w_i\); all terms involving a \(p_jg\) are kept
on the right side. The determinant of each homogeneous two-by-two
transfer is \(B/A\), independent of all endpoint parameters.
Consequently its inverse can be used to derive cleared rows
without introducing parameter-dependent denominators.

For a fixed shift \(a\), multiply the shifted equation (6) by
that tensor. The homogeneous terms are exactly the connection
twist of (7). For example, if \(Ez=M_z z+S_z\), then
\[
 M_z^{-1}E\{k_i(q^{2a}v)z(v)\}
       =k_i(q^{2a+2}v)z(v)
          +k_i(q^{2a+2}v)M_z^{-1}S_z(v).
 \tag{8}
\]
The second term belongs to the retained source. It is not set to
zero when deriving the original row.

Choose common inversion-symmetric clearings for these finitely
many rows and their reflected rows, and use the exact full-step
conversion to \(C,J,D_1\). This gives a vector \(\mathcal P\) of
ordinary canonical inner-block coordinates, including \(P\), and
an exact equation
\[
            [\,w_i d(C)I-\mathcal B(C,J,D_1)\,]\mathcal P
                               =\mathcal S .
 \tag{9}
\]
Here \(d\) is a nonzero scalar polynomial, chosen monic, and
\(\mathcal B\) is independent of \(w_i\). All degrees are bounded
independently of \(N\). The source \(\mathcal S\) includes every
term produced by (8), every \(p_jg\), and every scalar carrier.
It is supplied as an actual source packet.

The polynomial \(d\) can be chosen with coefficients rational in
\(q\) alone. Its roots belong to a fixed finite set
\[
                   \varepsilon(q^a+q^{-a}),\qquad
                     \varepsilon=\pm1,\quad a\in\mathbb Z ,
 \tag{10}
\]
with multiplicities. Indeed the homogeneous kernel transfers and
their inverses have denominators made from fixed shifts of
\(qv-1,v-q,v+q\) and Laurent units. Pairing a denominator with
its inversion gives factors of (10). The full-step conversion
adds only fixed powers of \(C-c_0\), and finitely many compositions
add their fixed shifts. Scalar rational factors in \(q\) can be
removed from the entire row. No physical nonunit is canceled.

Negative endpoint factors must not be omitted. For example,
\[
 \frac BA=\frac{(v-q)^3(qv+1)}{(v+q)(qv-1)^3},\qquad
 \frac{r_*}{A}
       =-\frac{8q^2v(v^2-1)}{(v+q)(qv-1)^3}.
 \tag{11}
\]
Thus the direct companion clearing can contain \(C+c_0\).
The separate positive-endpoint ordinary module does not by itself
prove that this factor cancels from (9).

### The source in (9) is a terminalized block

Every source term before descent contains a fixed full shift of
\(e_D\). It has zero values at the physical angular grid and
first-jet support only at finitely many fixed translates of the
original endpoint. Multiplying it by the other kernel coordinates
therefore uses their values at those same colors, not their normals.
For sufficiently large \(N\) these colors are fixed-index \(c_a\),
and
\[
                         K_N(c_a,w)=F_{a,N}(w),\qquad
                              \deg_w F_{a,N}=a .
 \tag{12}
\]
The coefficients are rational in \(q\) with polynomial level cost.

After even/odd descent, each such source is a radical polynomial
supported at finitely many fixed physical colors near \(c_0\).
It is a linear combination of \(e_{D-a}\) for finitely many fixed
\(a\). To see this, order the colors from the endpoint: the first
normal of \(e_{D-a}\) is nonzero at \(c_a\), vanishes at colors
farther from the endpoint, and the resulting finite normal-value
matrix is triangular. Its nonzero diagonal entries are fixed sine
products, so its inverse is rational in \(q\) with polynomial cost.
This also verifies the full-normal statement, not merely values.

Under the inner turn,
\[
              V_ne_{D-a}
                 =\kappa^nT(R^{-n}e_a)
                 =\kappa^n e_a(J)G_n,\qquad G_n=T(R^{-n}).
 \tag{13}
\]
Thus the source in (9), after all subsequent operations, is a
whole terminal-replacement packet: fixed shifted/mirrored
coordinates and fixed \(J\)-polynomial insertions of \(G_n\),
coupled to the original external state \(y\), followed by
\(U_\tau\). Its coefficients retain the literal \(p_j\) and the
bounded-degree physical-row polynomials (12).

Supplying this entire packet is essential. Its rate after the
outer turn is not inferred from the rate of \(G_n\) alone.
In the unknown coefficient matrix below, the selected block's
\(p_j\) occur only on the supplied right side. There is no
formal \(p_j=0\) specialization followed by an unsupported
openness claim for projected rank.

## 3. The actual leading operator after coupling

For (3), define \(M_\ell\) by \(E^\ell y=M_\ell y\).
If \(L=\sum_\ell a_\ell(v)E^\ell\) is a scalar ordinary difference
operator, then
\[
 \mathcal C_M(L)=\sum_\ell a_\ell(v)M_\ell(v)^{-1}E^\ell
                 \quad\hbox{satisfies}\quad
                 (Lf)y=\mathcal C_M(L)(fy).
 \tag{14}
\]
The identity
\[
       M_{\ell+k}(v)=M_k(q^{2\ell}v)M_\ell(v)
 \tag{15}
\]
shows directly that \(\mathcal C_M\) is an algebra homomorphism.
These rational identities are used only to derive their cleared,
quotient-safe full-step versions.

Apply \(V_n\) componentwise to (9), couple with the external state,
descend as in (5), and apply \(U_\tau\). Let \(\mathfrak F\) denote
this complete linear operation on an arbitrary vector of canonical
inner polynomials, and put \(X_0=\mathfrak F(\mathcal P)\).
Choose a common scalar clearing \(a(C)\ne0\) for the two operators
in (9) after the first three operations. It is independent of
the selected \(w_i\). After the outer turn write
\[
                       \mathcal A=a(D_\tau)I .
 \tag{16}
\]
There are fixed finite-band matrix operators \(\mathcal L,\mathcal H\),
independent of \(w_i\), such that exactly
\[
 \begin{split}
 \mathcal A\mathfrak F(d(C)F)&=\mathcal L\mathfrak F(F),\\
 \mathcal A\mathfrak F(\mathcal B F)&=\mathcal H\mathfrak F(F),\\
                 (w_i\mathcal L-\mathcal H)X_0
                                      &=\mathcal A\mathfrak F(\mathcal S).
 \end{split}                                                    \tag{17}
\]
The first two identities hold for every canonical vector \(F\).
The same clearing is used in both and on the entire source.
All shifted source/recovery coordinates needed for the external
companion are included.

In general \(\mathcal L\) is the cleared outer conjugate of
\(\mathcal C_M(d(D_n))\). It is a matrix operator. It need not have
the scalar unit extreme of \(d(D_\tau)\); reciprocal-resonant
principal support is not excluded by (17). No absence of compact
strings is asserted for \(\mathcal L\) alone.

## 4. Ordinary division supplies the recovery chain

Fix an integer \(k\ge0\). Divide each component as an ordinary
polynomial, starting with \(\mathcal P_0=\mathcal P\):
\[
          \mathcal P_j=d(C)\mathcal P_{j+1}+\mathcal R_j,
             \qquad \deg_C\mathcal R_j<\deg d,\quad 0\le j<k .
 \tag{18}
\]
For constant \(d\), take zero remainders. Canonical representatives
are chosen before division. These are ordinary exact identities,
so their classes and all first normals agree without any division
by a nonunit in \(\mathcal A_N\). Put
\[
             X_j=\mathfrak F(\mathcal P_j),\qquad
             Y_j=\mathfrak F(\mathcal R_j).
 \]
Equation (17) gives the exact rows
\[
                    \mathcal L X_{j+1}
                         =\mathcal A X_j-\mathcal A Y_j .
 \tag{19}
\]
Every \(Y_j\), with its full normals, is supplied. Since its
pre-inner polynomial degree is fixed, \(V_n\mathcal R_j\) is
still fixed-degree. After coupling to \(y\), multiplication by
its fixed polynomial coupon becomes that same polynomial in
\(D_\tau\) after the outer turn. These are lower-active-block
sources: the selected endpoint product has been replaced by a
fixed-degree coupon. A scalar coefficient of \(\mathcal R_j\)
may have degree depending on \(N\) in the endpoint parameters;
it remains part of the actual supplied source, not a coefficient
of the finite-window matrix.

The remainder coefficients themselves cost at most a polynomial
for the microscopic inputs (2), for fixed \(k\). Here is the
needed elementary bound. All original inner coordinates have
polynomial real norm: the endpoint-product bound supplies it
before shifts; fixed full angular shifts preserve the real
circle, odd descent costs a fixed power of \(N\) by Bernstein's
inequality, and full-Hermite folding costs a fixed power as well.
Their degree is \(O(N)\).

For a polynomial of degree \(O(N)\) and real norm \(B_N\), its
Chebyshev coefficients have modulus at most \(2B_N\).
On a fixed microscopic ellipse about either endpoint, summing
the finite Chebyshev series bounds the value by \(C N B_N\);
fixed derivatives add only powers of \(N\).
The nodes in (10) lie in such ellipses. Distinct fixed nodes
are separated by at least \(cN^{-2}\) for large \(N\);
coincident nodes are combined with their multiplicities.
The fixed-size confluent interpolation matrix for the remainder
therefore has polynomial inverse. This bounds its coefficients.
The quotient in (18) has polynomial real norm too: away from
fixed \(O(N^{-2})\) neighborhoods of the roots, divide directly;
near a root, use the ordinary removable divided difference and
the same fixed derivative bounds. Iterating a fixed number of
times proves the claim.

This pre-inner estimate is not a rate bound for the outer images
\(X_j\). In particular roots of \(d\) tending to \(-2\) have not
been converted to harmless positive-endpoint recovery roots.

## 5. A finite-chain injectivity lemma

Fix an interior formal orbit
\[
                  v_j=\zeta q^{\delta+2j},\qquad
                    \zeta\ne1,-1,\quad \delta\in\mathbb Q ,
 \tag{20}
\]
over the field of rational functions in the other independent
coefficients, with transcendental \(q\). Fix a finite interval
\(I\) of row indices. The target and all \(X_1,\ldots,X_k\)
use the same component set and the same support interval \(I\).
Include every output row of (17),(19) whose shift range touches
that support. Every outside value entering such a row is
genuinely supplied. This includes both collars of every \(X_j\).

Let \(\mathcal V\) be the resulting finite-dimensional space of
compactly supported value-and-first-normal packets, and set
\[
                              d_I=\dim\mathcal V .
 \tag{21}
\]
Normal rows are included by replacing each operator \(L\) with
\[
                         L^{\rm jet}=
                  \begin{pmatrix}L&0\\L_u&L\end{pmatrix}.
 \tag{22}
\]
Here \(L_u\) differentiates its ordinary coefficients. This is
just the differentiated residual formula.

The map \(\mathcal A^{\rm jet}\) is injective on finite support.
Indeed the forward and backward extremes of \(D_\tau\) are
\[
                   q^{-\tau}v^{-\tau}A(v),\qquad
                         q^{-\tau}v^\tau B(v).
 \tag{23}
\]
They are units at every translate of (20). If \(\deg a=s\),
the forward extreme of \(a(D_\tau)\) is its leading coefficient
times \(s\) shifted factors in (23); lower powers have smaller
order. The output row immediately before the first nonzero
support entry therefore excludes a nonzero compact value
kernel. The constant-polynomial case is immediate. Applying
this first to values and then to normals proves the jet claim.
The complete collar is what makes these exterior-center rows
available.

**Finite-chain lemma.** Let \(A,L:\mathcal V\to\mathcal W\) be
linear maps into a common output-row space, with \(A\) injective.
If
\[
                  Lx_0=0,\qquad Lx_{j+1}=Ax_j
                            \quad(0\le j<d_I),
 \tag{24}
\]
then \(x_0=0\).

*Proof.* If \(x_0\ne0\), the \(d_I+1\) vectors in (24) would be
linearly independent. Otherwise choose a dependence with the
smallest possible last index \(m\ge1\). Applying \(L\) and
then injectivity of \(A\) gives a nontrivial dependence ending
at \(m-1\), a contradiction. There cannot be \(d_I+1\)
independent vectors in \(\mathcal V\). \(\square\)

## 6. Projected recovery over the coefficient field

Take \(k=d_I\) divisions in (18). Remove the supplied terminal,
remainder, and collar columns exactly, and denote the augmented
unknown matrix by \(\mathsf M\). Its unknowns are all the
interior packets \(X_0,\ldots,X_{d_I}\). Let \(\Pi\) select \(X_0\).

**Theorem.** On the formal interior orbit (20),
\[
                              \ker\mathsf M\subseteq\ker\Pi .
 \tag{25}
\]
No claim of full column rank for \(\mathsf M\) is required.

*Proof.* In a homogeneous kernel test every supplied packet is
zero. All maps in (17),(19) are independent of the selected
\(w_i\), except the explicit \(w_i\mathcal L\).
Suppose \(X_0\ne0\). Expand its finitely many rational entries
at \(w_i=\infty\), and let \(w_i^m x_0\), \(x_0\ne0\), be
their highest common Laurent coefficient.

The coefficient of \(w_i^{m+1}\) in (17) gives
\(\mathcal L^{\rm jet}x_0=0\). Extract the coefficient of
\(w_i^m\) from every recovery row (19), and call the resulting
auxiliary coefficients \(x_1,\ldots,x_{d_I}\). They satisfy
\[
                  \mathcal L^{\rm jet}x_{j+1}
                            =\mathcal A^{\rm jet}x_j .
 \]
The auxiliary rational functions may have higher Laurent
degrees than \(X_0\); this does not change extraction of
their coefficient at this specified degree. All coefficient
vectors have support in the same space \(\mathcal V\).
The finite-chain lemma is a contradiction. \(\square\)

Working with the full jet packet in this argument is important.
Proving only that the original values vanish would not imply
that all auxiliary values vanish, so it would not justify
discarding the coefficient-derivative terms in the normal
recoveries. Formula (22) avoids that error.

The theorem does not say that (17) alone is injective, that
the original smaller window has a nonzero full-column minor,
or that the auxiliary quotients are uniquely determined.
It says exactly that its homogeneous augmented ambiguity is
invisible in the original packet.

## 7. A bounded row-span certificate and microscopic specialization

Over the coefficient field, (25) is equivalent to the rows
of \(\Pi\) belonging to the row space of \(\mathsf M\).
Choose a basis of that row space and a nonzero maximal-rank
minor. Solving the corresponding finite linear systems gives
a rational matrix \(\mathsf H\) with
\[
                              \Pi=\mathsf H\mathsf M .
 \tag{26}
\]
This is projected recovery, not inversion of all unknown columns.
Matrix size and all coefficient degrees are fixed independently
of \(N\), including the number \(d_I\) of divisions. Determinant
formulas therefore bound the rational degrees in (26).
After clearing scalar denominators on the monomial curve,
\[
                         \Delta\Pi=\mathsf H_0\mathsf M,
                                     \qquad \Delta\ne0 .
 \tag{27}
\]
The coefficients are Laurent polynomials in a fixed root of
\(q\), in \(h\), and in the independent ordinary endpoint and
endpoint-source symbols of the external companion. They also
include the ordinary \(w_i\) from (17). No actual terminal
function, quotient polynomial, or remainder coefficient of
degree depending on \(N\) has become a coefficient of (27).

For completeness, the physical specialization of (27) needs
the following adaptation of the bounded-degree argument.
Choose a rational physical phase and a residue class so
\[
 \zeta=e^{2\pi ia/b},\quad 0<a/b<1/2,\qquad
 v_{j_N}=\zeta q^\delta,\quad \delta=p'/b',\qquad
 q=t^{b'},\quad v=\zeta t^{p'} .
 \tag{28}
\]
Refine the residue if any retained source carrier requires it.
Equation (27) is already an identity on this curve, with
\(h,t\) formal and independent.

Suppose the microscopic germ of its nonzero denominator
\(\Delta\) vanished identically. At every sufficiently large
level in the residue class, the independent maps
\(w_\ell=2\cosh(\alpha_\ell/N)\) have open image. Hence the
polynomial obtained after substituting
\(p_\ell=P_N(w_\ell)\) would vanish identically in the \(w_\ell\).
For large \(N\), every bounded coefficient degree in \(w_\ell\)
is less than \(N\). The monic degree-\(N\) substitution is then
injective: the largest power of \(p_\ell\) gives a strictly
larger \(w_\ell\)-degree than all lower powers. Applying this
argument successively to the independent pairs proves the
multivariate assertion.

Every formal coefficient of \(\Delta\) would consequently
vanish at infinitely many \(h=1/N\), \(t=e^{\pi ih/b'}\).
After a fixed power of \(h\), it is a finite sum of polynomials
in \(h\) times exponentials with distinct rational frequencies.
The analytic identity theorem, followed by the elementary
independence of exponential polynomials, forces each coefficient
to vanish formally. For that independence one can apply the
product of powers of \(\partial_h-\lambda\) for all other
frequencies; the remaining shifted derivative is invertible
on finite-degree polynomials. This contradicts \(\Delta\ne0\).

Thus the microscopic denominator has a nonzero meromorphic germ
in \(h,\boldsymbol\alpha\). Remove its finite pole and take the
first nonzero \(h\)-coefficient. On each compact parameter chart
where that coefficient is uniformly a unit, (27) gives
\[
 \|X_{0,N}\|\le C N^K\left(
       \|\text{terminal-replacement packets}\|
       +\sum_{j<d_I}\|Y_{j,N}\|
       +\|\text{both collars of every }X_{j,N}\|
       +\|\text{other retained forcing}\|\right).
 \tag{29}
\]
All scalar coefficient clearings add at most fixed polynomial
cost on the same chart.

This proof transfers the row-span certificate itself. It does
not infer projected rank at generic parameters merely from a
specialized \(p=0\) matrix, and it does not invoke a full-column
minor theorem for a matrix known only to recover a projection.
Identified endpoint parameters require their relations to be
retained, or a separate holomorphic-source extension argument;
generic rank on an ambient polarized family does not by itself
give rank on every diagonal.

## 8. Source and rate scope

Every equality above is in the original full quotient before
the original trace is applied. Therefore the equalities retain
all shared factors, all signed crossings and their scalar
carriers, and all outside normals. Ordinary free boundary
variables are untouched. Fixed derivatives in endpoint
parameters commute with the source identities; uniform
estimates for those derivatives use a larger parameter unit
chart and Cauchy's formula, not an unstated enlargement of the
coefficient ring.

There are two distinct lower source classes in (29).
The terminal-replacement class keeps \(G_n\) and fixed insertions
inside the received product before the outer turn. The remainder
class deletes the selected active block and leaves fixed-degree
coupons. Both classes retain the complete external state and
its shared coordinates. Neither is replaced by the product of
individual scalar norms.

The additional quotient collars are a further, separate input.
Polynomial real norms of \(\mathcal P_j\) before turning do not
prove that their outer collar packets have the original smaller
incoming rate. Negative-endpoint factors in (11) have not been
removed. Even for a hypothetical positive-endpoint improvement,
its source-specific propagation proof would be additional work.

Consequently the exponential budget in (29) is the maximum of
the actual supplied budgets, including every right collar.
The theorem supplies a finite exact algebraic extension of
parameter-leading recovery to a multikernel inner block, with
explicit extra data. It supplies neither a global composed
action bound nor a nonzero geometric coefficient, and it does
not dispose of the undecorated branching-star source.

## 9. Direct sources

Complete direct texts were read at these unchanged pins; their
used implications and hashes were checked.

* [Single-kernel parameter-leading windows](research_single_kernel_parameter_leading_window_rank.md),
  SHA256 64e6e1d9fc7987a3e7a79d958e0705467514c922f37c9d316eb1381b6aa6c73c.
* [Full-step tensor interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398.
* [Original finite-band operators and mixed forcing](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
* [Full endpoint products and exact Hermite folding](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Bounded-degree quantum-binomial specialization](research_repeated_turn_quantum_binomial_rank_criterion.md),
  SHA256 5910f76a9e70e589d07476cae663b31bc949266e187f4f2902ce33cc8cd669cf.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Frozen notes and public manuscripts are unchanged.
