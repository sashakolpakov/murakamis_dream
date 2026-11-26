# A full-step tensor interface for repeated endpoint turns

Private written proof, 16 November 2026.

The full angular step preserves the original value-and-first-normal
quotient. It therefore permits exact multiplication of already turned
source channels, followed by a further original turn. This note gives
explicit polynomial conversion formulas, a finite tensor construction,
and the actual initial-data budget. It does not establish a regular
highest-order coefficient after the final turn, or a growth bound for
that final output.

## 1. Source and the quotient-safe full step

Retain the original conventions
\[
 q=e^{\pi i/N},\quad c=q+q^{-1},\quad s=q-q^{-1},\quad
 \eta=(-1)^{N-1},\quad \kappa=q^{(N-1)^2/2},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad \mathcal A_N=\mathbb C[Z]/(P_N),
 \qquad C f=Zf\pmod {P_N}.
\]
Here \(T_N\) is Chebyshev's polynomial; \(T\) is the original
turn, \(Te_j=e_{N-1-j}\), where
\[
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),\quad
 c_a=q^{2a+1}+q^{-2a-1},\quad
 S_j=\prod_{h=1}^j2\sin(h\pi/N).
\]
The original kernel, trace and signed turns are
\[
 K_N(w,Z)=\sum_{j=0}^{N-1}e_j(w)e_j(Z),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=N-1},
\]
\[
 J=TCT,\quad V_n=\kappa^nTR^{-n}T,\quad
 D_n=V_nCV_{-n},\quad U_\tau=V_\tau\quad(\tau=\pm1).
 \tag{1}
\]
All multiplications in \(\mathcal A_N\) retain its nilpotents.
The free parameters are never quotiented.

The target is
\[
 U_\tau F,\qquad
 F=\operatorname{can}\left(Q_{\rm base}\prod_{i=1}^bV_{n_i}Q_i\right),
 \quad
 Q_i=\operatorname{can}\prod_{\ell=1}^{r_i}
 K_N(2\cosh(\alpha_{i\ell}/N),Z).
 \tag{2}
\]
The integers \(b,r_i,n_i\) are fixed; all parameters range over
fixed bounded complex sets. A factor with \(n_i=0\) can be
absorbed into \(Q_{\rm base}\), which is another original endpoint
product; an empty product is \(1\).
Omit every transformed empty factor using the exact identity
\(V_n1=1\). Thus every transformed factor retained below has
\(r_i\ge1\) and \(n_i\ne0\).
No transformed factor in (2) is replaced by an endpoint product.

Introduce
\[
 \mathcal B_N=\mathbb C[v,v^{-1}]/((v^N+1)^2),
 \quad C=v+v^{-1},\quad W=v-v^{-1},\quad
 E f(v)=f(q^2v).
 \tag{3}
\]
Since
\[
 v^NP_N(v+v^{-1})=(v^N+1)^2,
\]
there is an exact presentation
\[
 \mathcal B_N=\mathcal A_N[v]/(v^2-Cv+1)
             =\mathcal A_N\oplus W\mathcal A_N.
 \tag{4}
\]
The last equality uses \(W=2v-C\), so it is a free module
decomposition, including at the ramified points. Inversion
\(\iota:v\mapsto v^{-1}\) fixes the first summand and negates
the second. Its invariants are exactly \(\mathcal A_N\).
At odd \(N\), the double angular root \(v=-1\) has only a
constant invariant local part, agreeing with the simple
spectral root \(C=-2\); its odd nilpotent belongs to the
second summand.

The shift \(E\) preserves the ideal in (3) and permutes its
double-root jets. For \(N\ge3\), define on ordinary spectral
polynomials
\[
 \mathsf S=\frac{E+E^{-1}}2,\qquad
 \nabla=\frac{E-E^{-1}}{W},\qquad
 \mathsf D=\frac{\nabla}{q^2-q^{-2}}.
 \tag{5}
\]
The numerator defining \(\nabla\) is anti-invariant and hence
is ordinarily divisible by \(W\). This is not an inversion
of \(W\) in \(\mathcal B_N\). In particular
\[
 \nabla P_N=0,\quad \mathsf S P_N=P_N,\quad
 \nabla(P_N f)=P_N\nabla f,\quad
 \mathsf S(P_N f)=P_N\mathsf S f.
 \tag{6}
\]
Thus all three operators descend to \(\mathcal A_N\).
Their exact product rules are
\[
 \begin{split}
 \nabla(fg)&=(\nabla f)\mathsf Sg+\mathsf Sf\,\nabla g,\\
 \mathsf S(fg)&=\mathsf Sf\,\mathsf Sg
                  +\frac{C^2-4}{4}\nabla f\,\nabla g .
 \end{split}                                             \tag{7}
\]
These identities follow by multiplying the two full shifts
before taking their sum or difference.

For an ordinary Laurent lift \(X\), its two components in (4)
are
\[
 F_X=(X+\iota X)/2,\qquad G_X=(X-\iota X)/(2W).
 \tag{8}
\]
Changing the lift by \(P_N(C)H(v)\) changes each component by
a \(P_N\) multiple, because the odd part of \(H\) is divisible
by \(W\). Formula (8) is therefore well-defined in the full
quotient. At \(v=-1\), \(G_X\) retains the odd first angular
jet; dividing only values there would lose it.

An angular derivative is not a derivation of \(\mathcal B_N\):
it can lower the multiplicity of its defining ideal. All
normal equations below mean derivatives of ordinary residuals,
evaluated at the physical roots. Equality in (3) guarantees
both their values and first derivatives vanish.

## 2. Explicit polynomial conversion to the original operators

The following identities eliminate the full-step operators
without inverting a physical endpoint factor.
Write \(Z=C=v+v^{-1}\) in coefficient calculations, and set
\[
 d=(Z-c)^3,\quad a=8-cZ-c^2,\quad
 b=(4-q^{-1}Z)(Z+c)-8q,
\]
\[
 h=-\frac{s}{2}(Z^2+cZ-8),\qquad
 p=\frac{-sZ(Z^2+cZ-8)-a(Z^2-4)}4,
\]
\[
 t=8(3-q^2-q^{-1}Z),\qquad
 r=d-cp-h(4-q^{-1}Z).
 \tag{9}
\]
Then the exact polynomial operator identities are
\[
 \boxed{\begin{split}
 d(C)\nabla&=-b(C)J-q\,a(C)D_1+t(C)I,\\
 d(C)\mathsf S&=p(C)J+q\,h(C)D_1+r(C)I .
 \end{split}}                                             \tag{10}
\]
Every coefficient in (10) multiplies on the left. The
identities hold first on ordinary polynomials and then in
\(\mathcal A_N\). In particular they retain every first normal.

Here is a direct verification from the original operator.
Put
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\qquad
 B(v)=A(v^{-1}),\qquad r_*=8/(Z+c).
\]
The physical formulas for \(J,D_1\) give
\[
 \begin{split}
 J&=r_*-(A+B)\mathsf S-(A-B)W\nabla/2,\\
 D_1&=r_*+q^{-1}(A/v+Bv)\mathsf S
                  +q^{-1}(A/v-Bv)W\nabla/2 .
 \end{split}                                             \tag{11}
\]
Their removable interpretation on polynomials is the original
one. Direct common-denominator calculation gives
\[
 A+B=\frac8{Z+c}-c,\qquad
 A/v+Bv=4-q^{-1}Z-\frac{8q}{Z+c},
\]
\[
 (Z+c)W(A-B)=2h,\qquad
 (Z+c)W(A/v-Bv)/2=p .
 \tag{12}
\]
Consequently (11) becomes
\[
 -a\mathsf S-h\nabla=(Z+c)J-8I,\qquad
 b\mathsf S+p\nabla=q(Z+c)D_1-8qI.
 \tag{13}
\]
The determinant and scalar cancellation are
\[
 bh-ap=(Z-c)^3(Z+c),\qquad
 \frac{b+qa}{Z+c}=3-q^2-q^{-1}Z.
 \tag{14}
\]
Cramer's rule in the rational coefficient field proves (10).
The coefficient \(r\) can equivalently be obtained by applying
the second identity to \(1\), using
\(J1=c\) and \(D_11=4q^{-1}-q^{-2}Z\).
Both sides of (10) are polynomial operators, so the identities
extend across the coefficient poles in (11).

No inverse of \(C-c\) has been used in \(\mathcal A_N\).
It is a nonunit at the original double endpoint. In particular
(10) must not be solved by dropping this factor there.
As a normalization check, at the formal limit \(q=1\), away
from \(Z=2\), the formulas read
\[
 \nabla=\frac{ZJ+2D_1-8}{(Z-2)^2},\qquad
 \mathsf S=1+\frac{Z+2}{2(Z-2)}(J-2).
 \tag{15}
\]
This limit is only a check on coefficients, not an inverse
operator assertion at the parabolic value.

## 3. Finite actual input columns and their multiplication

We specify which input equations are tensorized. For a nonzero
\(n_i\), use the pinned endpoint-product system with
\[
 k_i=33r_i,\quad m_i=|n_i|,\quad
 M_i=k_i m_i+1,\quad \ell_i=r_i m_i.
\]
Its actual gauged channels \(W_i\), of length \(6^{r_i}\),
and its original product component \(Y_i=V_{n_i}Q_i\) satisfy
\[
 \{d_i(D_{n_i})(J-c)I-s^2E_i(D_{n_i})\}W_i=0,\qquad
 (D_{n_i}-2)^{r_i}Y_i=(W_i)_* .
 \tag{16}
\]
Here \(W_i\) already denotes the turned canonical gauged vector.
Use the value column of shifts
\[
 X_i(v)=
 \big(E^{-M_i}W_i,\ldots,E^{M_i-1}W_i;\
           E^{-\ell_i}Y_i,\ldots,E^{\ell_i-1}Y_i\big).
 \tag{17}
\]
Its rank \(2M_i6^{r_i}+2\ell_i\) is fixed independently of \(N\).
The two nonzero rational extreme coefficients proved in the
pinned source give rational forward and backward matrices
\(M_{i,+}(v),M_{i,-}(v)\). Globally their meaning is the
cleared identities
\[
 a_{i,+}(v)EX_i=B_{i,+}(v)X_i,\qquad
 a_{i,-}(v)E^{-1}X_i=B_{i,-}(v)X_i
                    \quad\hbox{in }\mathcal B_N.
 \tag{18}
\]
The scalar Laurent polynomials \(a_{i,\pm}\) and matrix
Laurent polynomials \(B_{i,\pm}\) have bounded degrees for
fixed input data; \(M_{i,\pm}=B_{i,\pm}/a_{i,\pm}\) is a
rational calculation only. The source gives their explicit
construction by solving the extreme row of (16), and the
central forcing in recovery is retained in the same column.
Ordinary residuals before solving are \(P_N\) multiples,
so multiplying back all denominators gives (18) with full jets.
Neither an endpoint inverse nor an off-grid homogeneous
identity for a canonical polynomial is asserted.

For the unturned product \(Q_{\rm base}\), the ordinary six-channel
module gives a convenient exact input column. Apply its
ordinary half shifts twice before canonical reduction.
If its ordinary half-step matrices are \(H_\pm(v)\), the
full-step matrices are
\[
 H_+(qv)H_+(v),\qquad H_-(q^{-1}v)H_-(v).
 \tag{19}
\]
These are obtained from the module's displayed half-step
mean and divided difference by
\(H_\pm=\mathbf S\pm sW\mathbf D/2\), or their tensor
versions. All ordinary source channels \(P_N,1\) stay in
this calculation: a half step sends \(P_N\) to \(4-P_N\).
Only after forming and clearing (19) is the result reduced
to (18). This includes the removable forcing
\(P_N(Z)/(Z-c)\); it is not set to zero before its
denominator has been treated. The input product is a selected
component of this unturned column.

Tensor these actual columns, including the base column if
present. Their entries are ordinary products in the same
angular color, not products transported by \(T\). Define
\[
 X=\bigotimes_iX_i,\quad
 A_\pm=\prod_i a_{i,\pm},\quad
 B_\pm=\bigotimes_iB_{i,\pm},\quad
 M_\pm=B_\pm/A_\pm .
 \tag{20}
\]
Then, exactly in the full angular quotient,
\[
                      A_\pm E^{\pm1}X=B_\pm X.
 \tag{21}
\]
This follows by multiplying (18) before taking any normal.
The product \(F\) in (2) is a specified component of \(X\):
choose the current product component at each factor.
It is inversion-invariant. This retains shared parameters
and their correlations; there is no coefficientwise absolute
majorization.

## 4. Even descent and the next original turn

Here are explicit finite matrices for descending (21).
For a rational Laurent matrix \(H\), write
\[
 H_e=(H+\iota H)/2,\qquad H_o=(H-\iota H)/(2W).
\]
They are rational in \(C\). Set
\[
 U=M_++M_-,\quad V=M_+-M_-,\quad
 W_\pm=q^{\pm2}v-q^{\mp2}v^{-1},
\]
\[
 N_\pm=M_\pm/W_\pm,\qquad
 U_N=N_++N_-,\quad V_N=N_+-N_- .
 \tag{22}
\]
For the actual descended column \(Z=(F_X,G_X)^{\mathsf T}\)
from (8), the rational matrix calculations are
\[
 \begin{split}
 \mathsf S F_X&=\tfrac12U_eF_X+\tfrac12W^2U_oG_X,&
 \nabla F_X&=V_oF_X+V_eG_X,\\
 \mathsf S G_X&=\tfrac12(U_N)_eF_X+\tfrac12W^2(U_N)_oG_X,&
 \nabla G_X&=(V_N)_oF_X+(V_N)_eG_X .
 \end{split}                                             \tag{23}
\]
For example \(E\iota X=\iota(E^{-1}X)\); inserting (21)
into the sum and difference of \(X,\iota X\) proves the
first line after clearing denominators. In the second,
\(\iota W_+=-W_-\), which gives the same calculation with
\(M_\pm\) replaced by \(N_\pm\).

Choose a common nonzero polynomial \(\mathfrak a(C)\) clearing the
four matrices in (23), with sufficient multiplicity to clear
the explicit linear combinations of (21) and its reflected
version used to derive them, before canceling any factor. One can
use products of the Laurent denominators and their inversions,
and also \(W_+W_-=C^2-(q^2+q^{-2})^2\); their invariant
products are spectral polynomials. Further finite powers
clear any rational odd parts in (22). All degrees remain
bounded independently of \(N\). Denote the resulting polynomial
matrices by \(S_0(C),N_0(C)\). Then
\[
             \mathfrak a(C)\mathsf S Z=S_0(C)Z,\qquad
             \mathfrak a(C)\nabla Z=N_0(C)Z
                       \quad\hbox{in }\mathcal A_N.       \tag{24}
\]
These are obtained by algebraic combinations of the cleared
equations (21), not by localizing \(\mathcal B_N\) and
forgetting its killed components. The actual definitions (8),
(17), the original equations (16), and their source data
are retained alongside (24). In particular (24) alone is
not asserted to characterize the source at zeros of \(\mathfrak a\).

Substitute (10) into \(d(C)\) times (24). This yields the
explicit polynomial, ordered system
\[
 \boxed{\begin{split}
 \{\mathfrak a(C)[p(C)J+qh(C)D_1+r(C)]-d(C)S_0(C)\}Z&=0,\\
 \{\mathfrak a(C)[-b(C)J-qa(C)D_1+t(C)]-d(C)N_0(C)\}Z&=0.
 \end{split}}                                             \tag{25}
\]
Applying the actual \(U_\tau\) to every component gives
these same ordered polynomial relations under
\[
              C\mapsto D_\tau,\quad J\mapsto J,\quad
              D_1\mapsto D_{\tau+1},\quad Z\mapsto U_\tau Z.
 \tag{26}
\]
This is exact conjugation by (1). The resulting physical
difference orders and matrix sizes are bounded in terms of
the fixed input data. The desired output in (2) is the
specified \(F_X\) component of \(U_\tau Z\).
No rational coefficient is evaluated at a nonunit operator.

Every ordinary residual in (24)--(26) is a \(P_N\) multiple.
In the physical coordinate \(c_N(u)=2\cos(2\pi u+\pi/N)\),
\[
                         P_N(c_N(u))=4\sin^2(\pi Nu).
 \tag{27}
\]
Thus values and first \(u\)-derivatives of the residual vanish
at the grid. Differentiating includes all coefficient
derivatives. This supplies the original full normal equations,
including all product-rule normals and the odd simple node.
No half step is applied to an already reduced source.

## 5. Actual data retained at the interfaces

Clearing a nonunit can create additional solutions. Equations
(18), (24), or (25) are therefore necessary source equations,
not license to choose new homogeneous endpoint data. The actual
column definitions and forced recovery in (16) remain part of
the construction. Endpoint values and first normals are the
original source traces described below. They are not set to
zero when a clearing coefficient vanishes.

There is a useful uniform bound for the data before the final
turn. Write \(\mathcal I_n\) for the finite terminal maximal
characteristic integral in the pinned sources, and set
\[
                         A_{\rm in}=\sum_{i=1}^b\mathcal I_{n_i}.
 \tag{28}
\]
The first-turn initialization theorem proves, simultaneously
for \(Y_i\) and every gauged \(W_i\), real canonical norm
at most \(\exp[N\mathcal I_{n_i}+o(N)]\), uniformly on the
fixed complex parameter sets. The unturned base channels
have polynomial real norm. Full shifts on \(|v|=1\) keep
the spectral argument in \([-2,2]\), so the tensor column
has unit-circle norm at most \(\exp[NA_{\rm in}+o(N)]\).
Its ordinary Laurent degree is \(O(N)\).

The descent (8) costs only a polynomial: every Laurent
coefficient is bounded by the unit-circle norm, and
\(|\sin(kt)/\sin t|\le k\) bounds the odd quotient, including
its endpoint limits. Summing the \(O(N)\) coefficients
costs \(O(N^2)\). Canonical reduction of these ordinary
spectral polynomials also costs polynomially, by Markov
and full-Hermite reconstruction of their unchanged jets.
Consequently
\[
       \max_\nu\|Z_\nu\|_{\mathbb R}
                    \le \exp[NA_{\rm in}+o(N)].          \tag{29}
\]
Uniformity on larger parameter disks gives all fixed parameter
derivatives; Markov gives fixed spectral normals. Every channel
is even in each microscopic \(\alpha_{i\ell}\). Descending to
\(\alpha_{i\ell}^2\), the map
\(\alpha_{i\ell}^2\mapsto N^2(w_{i\ell}-2)\) has a uniformly
regular analytic inverse on bounded sets for large \(N\).
Thus fixed derivatives in the original exterior \(w_{i\ell}\)
cost only \(N^2\) per derivative and obey the same rate.

For every fixed physical row \(j\), let
\[
 F_j(Z)=K_N(c_j,Z),\quad Q_j(Z)=\partial_wK_N(c_j,Z),
 \quad Q_*=\partial_wK_N(c_0,Z),\quad
 G_n=TR^{-n},\quad H_n=T(R^{-n}Q_*).
 \]
The pinned fixed-row source identities give polynomials
\(\alpha_{j,N},\beta_{j,N}\), of fixed degree and polynomial
coefficient size, with
\[
 Q_j=\alpha_{j,N}(C)Q_*+\beta_{j,N}(C)1.
 \]
For every component \(z=Z_\nu\), the actual outer data are
\[
 \begin{split}
 (U_\tau z)(c_j)
   &=\kappa^\tau\phi_N(F_j(J)G_\tau\,z),\\
 (U_\tau z)'(c_j)
   &=\kappa^\tau\phi_N(
       [\alpha_{j,N}(J)H_\tau+\beta_{j,N}(J)G_\tau]z).
 \end{split}                                             \tag{30}
\]
Here \(H_\tau\) is the true normal channel, not \(V_\tau Q_*\).
Since \(\mathcal I_{\pm1}=0\), the coherent trace bound,
\(\|J\|\le34N^3\), and (29) prove
\[
 \max_{\nu,\ 0\le j\le j_0}
  \big(|(U_\tau Z_\nu)(c_j)|+
                  |(U_\tau Z_\nu)'(c_j)|\big)
             \le \exp[NA_{\rm in}+o(N)]
 \tag{31}
\]
for every fixed \(j_0\). Every product and shared parameter
stays inside the original traces. Formula (31) controls
actual fixed windows; it does not prescribe data at other
possible singular rows or prove global propagation.

The construction concerns sufficiently large \(N\), as do
the input companions. No shortest-level limit is inferred
from (10). At \(N=2\), \(C^2=0\) and directly
\[
 V_n(a+bC)=(a-4inb)+bC .
 \tag{32}
\]
Canonical multiplication followed by this formula retains
the complete double-root data. It handles the finite
exception without dividing \(q^2-q^{-2}\) or \(C-c\).

## 6. What the interface does not yet estimate

On a regular compact chart the principal full-step matrices
of the inputs can be tensorized: their eigenvalues multiply,
with the source and recovery branches retained. Formula
(23) converts the step symbols to their sum and difference,
and (26) performs the actual turn automorphism. It does not
replace the ordinary product by a transported product, or
identify this correspondence with a positive angle sector.

After (26), a coefficient such as \(\mathfrak a(D_\tau)\)
is an operator. The preceding clearing and descent do not
prove that the highest physical shift coefficient of the
combined system is invertible, uniformly or otherwise.
Eliminating components can also expose terms of smaller
asymptotic coefficient size but greater shift order. Such
terms cannot be discarded from a transfer proof. The
regular leading-order argument for one original endpoint
product does not automatically persist under (20)--(26).

The new result is therefore an exact finite interface with
full normals and a proved source initialization budget,
not a new general annihilator existence statement or an
integrated growth theorem. A regular physical companion
and its endpoint control are still needed before a maximal
characteristic-growth upper bound can be asserted for (2).
No selected coefficient, filled-action inequality, or
general forest closure follows here.

## 7. Direct sources

The following complete sources were read at the stated pins;
the directly used identities and hashes were checked:

* [Original finite-band operators](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  original ordinary operator, signed conjugation and carriers,
  finite physical order, ideal preservation and actual trace anchors.
* [Ordinary divided-difference product module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  base input channels, ordinary half-step source aliases and their
  explicit matrices, polynomial gauge and forced recovery.
* [Actual product companions and fixed-row data](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a:
  exact forward/backward extremes, unequal companion windows,
  canonical input bounds and full-normal fixed-row trace formulas.
* [First-turn initialization and the improved input budget](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_first_turn_endpoint_product_initialization.md),
  SHA256 7d0871a7dcde94c1cc73f98495b9521a61478729ddd52c51570ffa95f1901105:
  simultaneous gauged-channel estimate and the upper budget
  \(\mathcal I_n\), with uniform complex parameters and normals.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.
