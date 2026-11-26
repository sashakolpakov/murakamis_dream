# An exact source repair for correlated coherent windows

Private written proof, 19 November 2026.

The original pointed source admits an exact correlated coherent cutoff
after an exponentially small correction in one explicit coupon
direction. A polynomially bounded projection onto the actual lowering
commutant also gives a stronger Neumann repair at matrix level. Both
amplitudes are close to the original matrix in the whole-operator norm
budget. The source equalities are exact, even when that scalar is zero.

The complete directs C, F, and X are pinned below. C supplies a literal
root radical coupon and its pivotal partial trace; F supplies the
actual meridian frame; X supplies the capped Euclidean off-matching
estimate. The projection, its calibration, and the convergent source
repair are proved here. The earlier raw averaged co-source lift was
checked for coverage; it is not an input to these proofs.

## 1. Matrices, metric, and the original functional

Fix an integer width \(m\ge2\), and let
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad M=e^\mu,\quad x=-M/q,\quad x_0=-q^{-1}.
 \tag{1}
\]
The vectors \(w_0,\ldots,w_d\) are orthonormal in the physical
coefficient Euclidean metric. Put \(V=\operatorname{span}\{w_0,\ldots,w_d\}\),
\(\mathcal H_N=V^{\otimes m}\),
\(D=N^m\), and \(J_jw_a=a w_a\) on head \(j\).
All matrix norms use this metric. Write \(\|\cdot\|_2\) for the
Hilbert--Schmidt norm, \(\|\cdot\|_1\) for trace norm, and
\(\|\cdot\|_{\rm op}\) for operator norm. Superoperator norms below
are induced by \(\|\cdot\|_2\) unless indicated otherwise.

Retain the literal capped arrows
\[
 E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),\qquad E(M)w_0=0,
 \qquad K(M)w_a=xQ^{-a}w_a,
\]
\[
 E_\Sigma(M)=\sum_{j=1}^m E_j(M)K_{j+1}(M)\cdots K_m(M),
 \qquad J_\Sigma=\sum_jJ_j.
 \tag{2}
\]
Define the original highest-cut functional on every matrix by
\[
 Q_{\rm pt}(M)=|0\rangle\langle0|\otimes
                         K_2(M)^{-d}\otimes\cdots\otimes K_m(M)^{-d},
 \qquad \Phi_M(C)=\operatorname{Tr}(Q_{\rm pt}(M)C).
 \tag{3}
\]
No pivot has been inserted on the opened first head. Original crossing,
framing, or peripheral scalar factors remain in the matrix to which
this functional is applied. In particular, with \(r=m-1\),
\[
                 Q_{\rm pt}(M)=M^{-rd}Q_{\rm pt}(1).
 \tag{4}
\]
Let \(\mathcal S_M=\ker\operatorname{ad}_{E_\Sigma(M)}\).
This is a linear commutant inside \(\operatorname{End}(\mathcal H_N)\).
We require only \(E_\Sigma(M)W(M)=W(M)E_\Sigma(M)\), as in X.
Actual braid families satisfy this identity, but the construction
does not depend on their word length or filling powers.

Throughout the analytic statements choose buffered disks
\(0<\eta<\eta'<\pi\), and suppose the families in question are
holomorphic on a neighborhood of \(|N\mu|\le\eta'\).
All true meridian derivatives keep \(q\) fixed.

## 2. A literal source-calibrating coupon

C gives the following two-head root intertwiner, in the original
coefficient basis:
\[
 R_N=N|\psi\rangle\langle\varphi|,\qquad
 |\psi\rangle=\sum_{a=0}^d x_0^{a-d}|a,d-a\rangle,
 \quad \langle\varphi|=\sum_{a=0}^d x_0^{-a}Q^{-a}
                                               \langle a,d-a|.
 \tag{5}
\]
The covector here is algebraic, not the Hermitian adjoint of
\(|\psi\rangle\). Its Euclidean functional norm, and the norm of
\(\psi\), are both \(\sqrt N\). Consequently
\[
 R_N^2=0,\qquad \|R_N\|_{\rm op}=N^2,\qquad
 \operatorname{Tr}_2((I\otimes K_2(1)^{-d})R_N)=N I.
 \tag{6}
\]
For the first identity use
\(\langle\varphi|\psi\rangle=x_0^{-d}\sum_aQ^{-a}=0\).
For the partial trace, the support in (5) makes it diagonal.
The \(a\)-th entry is
\(N x_0^{-d}Q^{-a}x_0^{-d}Q^{d(d-a)}=N\), using
\(x_0^2=Q^{-1}\). Thus the calibration includes its actual pivot.

Each adjacent embedding \(R_{j,j+1}\) commutes with the root total
lowering arrow and preserves total integer degree. Indeed C proves
local total \(E,K\) intertwining; the local \(E\) block in (2)
commutes, as do the terms before it through the product of its two
Cartans and the terms after it by disjoint support. Define, in the
displayed order,
\[
       T_0=N^{-r}R_{12}R_{23}\cdots R_{m-1,m}.
 \tag{7}
\]
Take the pivotal trace of the final head first. All preceding factors
are independent of that head, and the last factor is precisely the
one in (6). This removes it with multiplier \(N\). Repeat from
right to left; the final first-head trace is
\(\operatorname{Tr}|0\rangle\langle0|=1\). Hence
\[
 T_0\in\mathcal S_1,\quad [J_\Sigma,T_0]=0,\qquad \Phi_1(T_0)=1.
 \tag{8}
\]
The chain has better norms than the product estimate. Since
\(x_0^2=Q^{-1}\), the nonzero pair entry of \(R_N/N\) is
\(x_0^{u+v-d}\), with output \((u,d-u)\) and input \((v,d-v)\).
Successive contractions in (7) therefore give exactly
\[
 T_0|a_1,\ldots,a_{m-2},v,d-v\rangle
   =\sum_{u=0}^d x_0^{u+v-d}
                  |u,d-u,a_1,\ldots,a_{m-2}\rangle,
 \tag{8a}
\]
and zero if the last input pair does not sum to \(d\).
At each intermediate pair the required occupation is forced, and
its exponent cancels the preceding intermediate exponent. This
proves (8a) for every width, including the empty list when \(m=2\).
It is one rank-one pair matrix, tensored with an identity and followed
by a tensor permutation. Thus
\[
 \|T_0\|_{\rm op}=N,\qquad
 \operatorname{rank}T_0=N^{m-2},\qquad \|T_0\|_2=N^{m/2}.
 \tag{8b}
\]
This fixed coupon is known explicitly; it does not require dividing
by the unknown source of a braid. It is not asserted to be a braid
word or a positive matrix.

Let \(P_E\) be the coefficient-Hilbert--Schmidt orthogonal projection
onto \(\mathcal S_1\). Define
\[
 \mathcal P_1 C=P_EC+
                    [\Phi_1(C)-\Phi_1(P_EC)]T_0.
 \tag{9}
\]
Its image is \(\mathcal S_1\), it is the identity there, and
\(\Phi_1\mathcal P_1=\Phi_1\). It is therefore an exact
source-preserving projection. Since
\(\|\Phi_1\|_{2^*}=\|Q_{\rm pt}(1)\|_2=N^{r/2}\) and
\(\|I-P_E\|_{2\to2}=1\),
\[
              \|\mathcal P_1\|_{2\to2}
                            \le 1+N^{m-1/2}.
 \tag{10}
\]
The same calibration gives the root functional bounds
\[
 N^{-m/2}\le\|\Phi_1|_{\mathcal S_1}\|_{2^*}
                                      \le N^{(m-1)/2}.
 \tag{10a}
\]
The lower bound is obtained by evaluating on \(T_0/\|T_0\|_2\).
It controls the functional on the whole commutant, not its value
on a specified matrix or a selected geometric state.
No spectral gap or inverse of \(\operatorname{ad}_E\) is used.
The finite orthogonal projection exists independently of such a gap.
Unitary degree conjugation preserves \(\mathcal S_1\), hence commutes
with \(P_E\). The functional \(\Phi_1\) kills every nonzero integer
degree and \(T_0\) has degree zero. Thus \(\mathcal P_1\) also commutes
with degree conjugation and degree averaging.

## 3. The whole-meridian projection and its true jets

Put \(f_a=\prod_{j=1}^a(1-Q^j)\), with \(f_0=1\), and set
\[
 h_a(M)=M^{-a}\frac{f_a}{\prod_{j=1}^a(1-M^{-2}Q^j)},
 \qquad D_h(M)w_a=h_a(M)w_a,
\]
\[
 A(M)=\bigotimes_{j=1}^m[D_h(M)M^{-(m-j)J_j}],
 \qquad \mathcal G_M C=A(M)CA(M)^{-1}.
 \tag{11}
\]
F proves, including the forced bottom zeros,
\[
 E_\Sigma(M)=A(M)E_\Sigma(1)A(M)^{-1}.
 \tag{12}
\]
The same direct proves polynomial bounds for \(A^{\pm1}\) on the
whole buffered scaled disk. Those estimates apply in the present
metric: these matrices are diagonal, so their operator norms are
the maxima of their entries in either diagonal head metric.

Since \(A\) is diagonal it commutes with \(Q_{\rm pt}(1)\).
Equations (3)--(4) give for every matrix \(C\),
\[
          \Phi_M(\mathcal G_MC)=M^{-rd}\Phi_1(C).
 \tag{13}
\]
Define
\[
 \boxed{\quad \mathcal P_M=\mathcal G_M\mathcal P_1\mathcal G_M^{-1}.
                  \quad}
 \tag{14}
\]
It is a holomorphic projection onto \(\mathcal S_M\), is the identity
on that space, and preserves \(\Phi_M\) on every matrix.
Equivalently, put
\[
 P_{E,M}=\mathcal G_MP_E\mathcal G_M^{-1},\qquad
 T_M=M^{rd}\mathcal G_MT_0.
\]
Then \(\Phi_M(T_M)=1\), and
\[
 \mathcal P_MC=P_{E,M}C+
                     [\Phi_M(C)-\Phi_M(P_{E,M}C)]T_M.
 \tag{15}
\]
Off the root \(P_{E,M}\) need not be orthogonal. We assert only
\(E_\Sigma(M)\)-commutation for \(T_M\); the frame (11) is not a
simultaneous \(E,F\) trivialization.

There exist constants \(C_\eta,b\), depending on the fixed width and
larger collar, such that
\[
 \sup_{|N\mu|\le\eta'}\|\mathcal P_M\|_{2\to2}
       \le C_\eta N^b=:p_N.
 \tag{16}
\]
Indeed (14) costs at most
\((\|A\|_{\rm op}\|A^{-1}\|_{\rm op})^2\) times (10).
For each fixed \(k\), Cauchy's formula on a further arbitrarily
small collar buffer gives polynomial bounds with the factor \(N^k\)
for \(\partial_\mu^k\mathcal P_M\) and \(\partial_\mu^kT_M\).
All matrices remain at the fixed quantum root. For example, if
\(\mathfrak a=\partial_\mu A|_0\), then
\[
 \partial_\mu\mathcal P_M|_0
       =[\operatorname{ad}_{\mathfrak a},\mathcal P_1],\qquad
 \partial_\mu T_M|_0=rd\,T_0+[\mathfrak a,T_0].
 \tag{17}
\]
Thus neither the moving projection nor the pivot normal has been
reset to its root value. Finite-dimensional Schatten norm comparison
changes (16) only by the polynomial factor
\(D^{|1/p-1/2|}\) for the induced \(S_p\)-norm.

## 4. The coherent cutoff is a positive superoperator

Use the coefficient-Euclidean coherent vectors and probability measure
\[
 \psi_z=(1+|z|^2)^{-d/2}\sum_{a=0}^d\sqrt{\binom da}\,z^a w_a,
 \qquad d\nu(z)=\frac{d\Re z\,d\Im z}{\pi(1+|z|^2)^2}.
 \tag{18}
\]
Tensor products are denoted by \(\psi_{\mathbf z}\), and
\(d\nu^{[m]}\) is the product measure. The exact resolution is
\(N\int|\psi_z\rangle\langle\psi_z|d\nu=I\).
Consequently the map
\[
 (\mathscr SC)(\mathbf y,\mathbf z)
                 =N^m\langle\psi_{\mathbf y},C\psi_{\mathbf z}\rangle
 \tag{19}
\]
is an isometry from Hilbert--Schmidt matrices into the indicated
\(L^2\) space: apply the resolution to both variables in its squared
norm to obtain \(\operatorname{Tr}(C^*C)\).

For completeness, choose precisely a window of X. On strict charts put
\[
 p(z)=\frac{|z|^2}{1+|z|^2},\quad
 e(z)=\frac z{|z|}(e^{-2\pi i p(z)}-1),\quad
 k(z)=-e^{-2\pi i p(z)},\quad
 \epsilon(\mathbf z)=\sum_j e(z_j)\prod_{\ell>j}k(z_\ell).
\]
Choose \(0\le\kappa\le1\) smoothly supported in a compact strict
chart for both variables, \(\gamma>0\), and a smooth
\(0\le\vartheta\le1\) which vanishes below \(\gamma^2\) and equals
one above \(4\gamma^2\). Set
\[
 b=\kappa\vartheta(|\epsilon(\mathbf y)-\epsilon(\mathbf z)|^2),
                    \qquad \chi=1-b.
 \tag{20}
\]
The fixed cutoff keeps the entire real observable-matching locus and
all occupation endpoints. It is independent of \(N,\mu,W\).
Define multiplication operators \(M_\chi,M_b\) in the \(L^2\) space
of (19), and the finite matrix superoperators
\[
 \mathcal L=\mathscr S^*M_\chi\mathscr S,\qquad
 \mathcal R=I-\mathcal L=\mathscr S^*M_b\mathscr S.
 \tag{21}
\]
They are self-adjoint positive contractions on Hilbert--Schmidt
space, because their quadratic forms lie between zero and
\(\|C\|_2^2\). In particular
\(\|\mathcal L\|_{2\to2},\|\mathcal R\|_{2\to2}\le1\).
This is positivity of superoperators; it does not assert that
\(\mathcal L(C)\) is a positive matrix or that \(\mathcal L^2=\mathcal L\).
Their exact synthesis formula is
\[
 \mathcal L(C)=N^{2m}\iint\chi(\mathbf y,\mathbf z)
 |\psi_{\mathbf y}\rangle
 \langle\psi_{\mathbf y},C\psi_{\mathbf z}\rangle
 \langle\psi_{\mathbf z}|\,d\nu^{[m]}(\mathbf y)d\nu^{[m]}(\mathbf z).
 \tag{22}
\]

X proves, for every \(C\in\mathcal S_M\), uniformly on the larger
scaled disk,
\[
 \|\mathcal R(C)\|_1\le C_0N^{2m}e^{-cN}\|C\|_{\rm op}.
\]
Its proof uses the literal finite matrices and capped propagation;
it applies pointwise to every member of this commutant. Therefore
\[
 \|\mathcal R|_{\mathcal S_M}\|_{2\to2}
                  \le \varepsilon_N:=C_0N^{2m}e^{-cN}.
 \tag{23}
\]
The constants depend on width, window, and collar, not on the word
length or integer filling powers of an eventual \(W\).

## 5. A single-coupon exact source repair

The simplest repair uses only the known coupon \(T_M\). Set
\[
 z_N(M)=\Phi_M(\mathcal L(T_M))
                =1-\Phi_M(\mathcal R(T_M)).
 \tag{23a}
\]
Both \(\|T_M\|_2\) and \(\|Q_{\rm pt}(M)\|_2\) are polynomially
bounded on the larger collar. Since \(T_M\in\mathcal S_M\), (23)
gives \(|z_N-1|\le C N^B e^{-cN}\), uniformly there. In particular
\(z_N\) is a holomorphic unit, bounded away from zero, for all
\(N\ge N_0\), with \(N_0\) independent of \(W\).

For any holomorphic \(W_N(M)\in\mathcal S_M\), define
\[
 W_N^\sharp=W_N+
         \frac{\Phi_M(\mathcal R(W_N))}{z_N(M)}T_M,
 \qquad C_N^\sharp=\mathcal L(W_N^\sharp).
 \tag{23b}
\]
Then \(W_N^\sharp\) is still an exact lowering intertwiner, and
\[
 \Phi_M(C_N^\sharp)=\Phi_M(W_N),\qquad
 \|W_N^\sharp-W_N\|_2+\|C_N^\sharp-W_N\|_2
                         \le C N^B e^{-cN}\|W_N\|_2.
 \tag{23c}
\]
Indeed \(\Phi_M(\mathcal L W_N)=\Phi_M(W_N)-\Phi_M(\mathcal R W_N)\),
and the added term contributes precisely
\(\Phi_M(\mathcal R W_N)\). Cauchy--Schwarz, (23), and the
polynomial coupon bounds prove the first norm estimate; the
contraction of \(\mathcal L\) and (23) prove the second.
Thus the original source has the exact formula
\[
 \boxed{\quad
 \Phi_M(W_N)=N^{2m}\iint\chi(\mathbf y,\mathbf z)
 \langle\psi_{\mathbf y},W_N^\sharp(M)\psi_{\mathbf z}\rangle
 \langle\psi_{\mathbf z},Q_{\rm pt}(M)\psi_{\mathbf y}\rangle
                    d\nu^{[m]}(\mathbf y)d\nu^{[m]}(\mathbf z).
 \quad}\tag{23d}
\]
This uses a known linear functional of the discarded matrix, not
division by the source of \(W_N\). The correction has one fixed
explicit matrix direction. Cauchy's formula gives all fixed true
meridian jets of (23c) on the smaller collar, with \(N^k\) per
derivative and the supremum of \(\|W_N\|_2\) on the larger collar.
All derivatives of (23d), including its pivot, are exact identities.

## 6. A stronger matrix repair by a convergent series

Put \(\mathcal K_M=\mathcal P_M\mathcal R\) and
\(q_N=p_N\varepsilon_N\). Its range lies in \(\mathcal S_M\), and
\[
            \|\mathcal K_M|_{\mathcal S_M}\|_{2\to2}\le q_N.
 \tag{24}
\]
There is an \(N_0\), independent of \(W\), such that \(q_N<1/2\)
for \(N\ge N_0\). For such levels and every holomorphic actual
\(W_N(M)\in\mathcal S_M\), define
\[
 V_N(M)=\sum_{j=0}^{\infty}\mathcal K_M^jW_N(M),\qquad
                         C_N^{\rm ex}(M)=\mathcal L(V_N(M)).
 \tag{25}
\]
The inverse in (25) is holomorphic without choosing bases in moving
commutants. Indeed \(\|\mathcal K_M\|\le p_N\) on all matrices,
and its range property gives
\(\|\mathcal K_M^j\|\le q_N^{j-1}p_N\) for \(j\ge1\).
Thus the full-space Neumann series converges uniformly on the collar
to \((I-\mathcal K_M)^{-1}\). Its restriction preserves
\(\mathcal S_M\), so \(V_N\) remains an exact lowering intertwiner.

Equations (23)--(25) yield the quantitative bounds
\[
 \|V_N\|_2\le\frac{\|W_N\|_2}{1-q_N},\qquad
 \|V_N-W_N\|_2\le\frac{q_N}{1-q_N}\|W_N\|_2,
\]
\[
 \|C_N^{\rm ex}-\mathcal L(W_N)\|_2
                       \le\frac{q_N}{1-q_N}\|W_N\|_2,
 \qquad
 \|C_N^{\rm ex}-W_N\|_2
             \le\frac{q_N+\varepsilon_N}{1-q_N}\|W_N\|_2.
 \tag{26}
\]
The contraction of \(\mathcal L\) proves the first estimate on its
second line; the last follows from
\(C_N^{\rm ex}-W_N=V_N-W_N-\mathcal R(V_N)\).

More strongly, the actual matrix and source identities are
\[
 \boxed{\qquad W_N=\mathcal P_M C_N^{\rm ex},\qquad
                  \Phi_M(W_N)=\Phi_M(C_N^{\rm ex}).\qquad}
 \tag{27}
\]
Indeed \(V_N-\mathcal P_M\mathcal R(V_N)=W_N\) and
\(\mathcal P_MV_N=V_N\), proving the first identity; source
preservation proves the second. Combining it with (22) gives the
promised exact formula, with the original coupon in its actual order:
\[
 \boxed{\quad
 \Phi_M(W_N)=N^{2m}\iint\chi(\mathbf y,\mathbf z)
 \langle\psi_{\mathbf y},V_N(M)\psi_{\mathbf z}\rangle
 \langle\psi_{\mathbf z},Q_{\rm pt}(M)\psi_{\mathbf y}\rangle
                    d\nu^{[m]}(\mathbf y)d\nu^{[m]}(\mathbf z).
 \quad}\tag{28}
\]
There is no division by \(\Phi_M(W_N)\), a coherent entry, or a
selected coefficient. This equality includes zero sources.

For every fixed \(k\), Cauchy's formula on the collar buffer gives
\[
 N^{-k}\sup_{|N\mu|\le\eta}
  \bigl(\|\partial_\mu^k(V_N-W_N)\|_2+
        \|\partial_\mu^k(C_N^{\rm ex}-W_N)\|_2\bigr)
 \le C_k N^B e^{-cN}
                 \sup_{|N\mu|\le\eta'}\|W_N(e^\mu)\|_2.
 \tag{29}
\]
The constants and \(B\) are independent of the word or its filling
powers. Dimension comparison gives corresponding Schatten estimates
with polynomial costs. Since \(E_\Sigma\) is uniformly bounded,
\([E_\Sigma,C_N^{\rm ex}]=[E_\Sigma,C_N^{\rm ex}-W_N]\)
has the same kind of exponentially small norm and true-jet bounds.
The same reasoning applies to \(C_N^\sharp\) by (23c).
These currents need not vanish identically.

Every derivative of (27)--(28) is an exact source equality. In
particular \(\partial_\mu^kQ_{\rm pt}=(-rd)^kQ_{\rm pt}\), and
the first derivative of (28) contains both \(\partial_\mu V_N\)
and \(-rd\,V_N\). Any separately retained scalar line must multiply
every term before differentiation. No root-only formula is being
differentiated in place of the actual family.

## 7. Degree preservation and what the repair does not select

One may choose \(\kappa\) in (20) invariant under the simultaneous
rotation of all \(\mathbf y,\mathbf z\). Since
\(\epsilon(e^{i\theta}\mathbf z)=e^{i\theta}\epsilon(\mathbf z)\),
the resulting \(\chi\) is invariant too. The identity
\(\psi_{e^{i\theta}\mathbf z}=e^{i\theta J_\Sigma}\psi_{\mathbf z}\)
and a change of variables in (22) then show that \(\mathcal L\)
and \(\mathcal R\) commute with degree conjugation. Equations
(9)--(14) show the same for \(\mathcal P_M\). Hence a degree-zero
\(W_N\) has degree-zero \(W_N^\sharp,C_N^\sharp,V_N,C_N^{\rm ex}\),
without changing the source or any meridian jet. The construction for
a general fixed cutoff is valid without this additional degree conclusion.

The cutoffs in (23d) and (28) are integral cutoffs. The coherent kernel
of either repaired marked matrix is obtained by another overlap integral;
it need not vanish where \(\chi=0\). Neither \(P_E\), the radical
calibrator, nor \(\mathcal P_M\) is asserted to preserve a complex
phase, a local canonical graph, or a relative integration cycle.
They are not algebra maps or positive matrix projections.

The scalar correction is substantive. At any fixed level,
\(\Phi_M(I)=x^{-rd}(\sum_{a=0}^dQ^{-a})^r=0\), although
\(I\in\mathcal S_M\). But
\[
 \Phi_M(\mathcal R(I))=N^{2m}\iint b(\mathbf y,\mathbf z)
 \langle\psi_{\mathbf y},\psi_{\mathbf z}\rangle
 \langle\psi_{\mathbf z},Q_{\rm pt}(M)\psi_{\mathbf y}\rangle\,d\nu d\nu
 \tag{30}
\]
need not vanish. On a protected nonempty open set where the strict
matching gap exceeds \(2\gamma\), the displayed integrand is a
nonzero real-analytic function:
its numerator is a product of nonzero coherent-overlap polynomials,
including the vacuum factor on head one. Choose a point where it is
nonzero and a sufficiently small nonnegative smooth bump there;
after a fixed scalar rotation the integrand has positive real part
on that bump. It is an allowed \(b\) of (20), and (30) is nonzero.
The whole-meridian factor is exactly \(M^{-rd}\); degree averaging
does not change this scalar. This fixed-level test shows that an
uncorrected window need not preserve the source kernel. It is not
a knot or geometric-cycle counterexample.

Only the original functional \(\Phi_M\) is exactly repaired.
Writing \(\Phi_{{\rm top},M}(C)=\operatorname{Tr}(Q_{\rm top}(M)C)\)
for X's top coupon, one has equality with \(\Phi_M\) on
\(\mathcal S_M\), but cannot replace \(Q_{\rm pt}\) by \(Q_{\rm top}\)
in either exact integral merely because its amplitude intertwines:
the marked matrix is its image under \(\mathcal L\). Its two source
values may differ.
Their difference still has an exponentially small whole-norm budget
by (23c), (26), and the bounded coupons; it has not been set to zero.

The amplitude in (28) is close to the original matrix only on the
scale \(\|W_N\|_2\). This scale may be exponentially larger than
an individual geometric contribution or the original closed scalar.
The window retains the full real matching locus and all endpoints,
including competing contributions. Exact source repair therefore
does not establish geometric component selection, a nonzero relative
cycle coefficient, or an asymptotic lower bound. Its gain is an exact
source-preserving cutoff representation with a quantitatively small
matrix repair and no assumed commutator spectral gap.

## Complete directs and author verification

* C: [research_prefix_commutant_and_pointed_normal_functional.md](research_prefix_commutant_and_pointed_normal_functional.md),
  549 lines, SHA256
  \(\texttt{b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0}\).
* F: [research_actual_meridian_source_frames.md](research_actual_meridian_source_frames.md),
  506 lines, SHA256
  \(\texttt{6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976}\).
* X: [research_euclidean_correlated_intertwiner_localization.md](research_euclidean_correlated_intertwiner_localization.md),
  417 lines, SHA256
  \(\texttt{12296ab7a60c3e424dcce9faf030c0f3299c14af64dd548d38dc254df3bbfdb2}\).

All three complete directs were freshly read nontruncated in this
uninterrupted author sequence, and every used implication was checked.
Only written mathematics and text/hash operations were used. No
mathematical programs, numerical tests, builds, git writes, or frozen
file edits were performed. The entire matching final was freshly
reread nontruncated and all four pins renewed before author freeze.
Independent matching final/direct review and parent adoption are
separate gates.
