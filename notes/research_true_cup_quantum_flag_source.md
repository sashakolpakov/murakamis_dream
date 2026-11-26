# A quantum flag model for the true cup source

24 November 2026. Written research proof.

The complete physical cup source has a unitary matrix-coordinate model.
In these coordinates every canonical based quantum meridian acts by an
explicit polynomial difference operator. The clock degree rises by at
most one per regular meridian entry, at every width and level.
The original last-marked closing is exactly one specified cyclic Weyl
coefficient of the actual word state, with its original phase and scale.

This identifies a full source and its observation, not a conditional
coideal eigenmode. A positive regular-boundary limit gives inverse-pair
flag circles for the cup state. The original closing still selects its
prescribed coefficient; neither that limit nor the polynomial module
gives a lower bound for the coefficient after an arbitrary braid.

## 1. Physical tensors and a unitary source map

Use the complete conventions of B and M below. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1}.
\]
The physical basis \(e_0,\ldots,e_d\) is orthonormal. Retain
\[
 Ke_a=xQ^{-a}e_a,\quad Ee_a=(Q^{-a}-1)e_{a-1},\quad
 Fe_a=(1-Q^{a+1})e_{a+1},\qquad e=qE.
 \tag{1}
\]
The missing endpoint arrows are zero. The letter \(e\) is M's actual
upper Gauss entry; its factor \(q\) is essential below.
The original tensors are
\[
 \mathbf p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\quad
 \ell_{ab}=x^a\mathbf1_{a+b=d}/N,\quad m_{ab}=x^b/N^2.
 \tag{2}
\]
At width \(2k\), write
\[
 u_0=\mathbf p^{\otimes k},\quad
 \ell_0=\ell^{\otimes(k-1)}\otimes m,\quad
 Z_N(R)=\ell_0Ru_0,\qquad K_N=\chi_N Z_N(R).
 \tag{3}
\]
Here \(R\) is an original signed unmarked braid word. It preserves
integer degree and the cup source has degree \(kd\). All its crossing
scalars and the external \(\chi_N\) remain.

Let \(J e_a=e_{d-a}\) and \(U=J\operatorname{diag}(x^{-a})\).
Thus \(U\) is unitary and \(\mathbf p=N\operatorname{vec}U\), with
the first tensor index the matrix row. Put
\(\psi=\mathbf p/N^{3/2}=\operatorname{vec}U/\sqrt N\).
For one pair define
\[
 \mathscr C(X)=(X\otimes I)\psi,\qquad
 \langle\mathscr C(X),\mathscr C(Y)\rangle
                           =N^{-1}\operatorname{Tr}(X^\dagger Y).
 \tag{4}
\]
Tensor these maps over the ordered pairs \((1,2),\ldots,(2k-1,2k)\).
Their domain is \(\operatorname{End}(V_N^{\otimes k})\), with inner
product \(\tau_k(X^\dagger Y)\), \(\tau_k=N^{-k}\operatorname{Tr}\).
The resulting \(\mathscr C_k\) is unitary onto the entire physical
\(2k\)-head space. In particular
\[
 \psi_0=u_0/N^{3k/2}=\mathscr C_k(I),\qquad
 X_R=\mathscr C_k^{-1}R\psi_0 .
 \tag{5}
\]
This defines the unique full word state \(X_R\) without its scalar value.
No physical head is swapped. The matrix indices merely label the
original odd heads and their ordered cup partners.

The exact first-to-second transpose and its inverse are
\[
 \theta(A)=(U^{-1}AU)^{\mathsf T},\qquad S=\theta^{-1},
 \qquad
 (A\otimes B)\mathscr C(X)=\mathscr C(AXS(B)).
 \tag{6}
\]
They are complex-linear antiautomorphisms, not Hermitian adjoints.
The literal cup and ordered coproduct give
\[
 \begin{array}{c|ccc}
 &K&e&F\\ \hline
 \theta&K^{-1}&-K^{-1}e&-FK\\
 S&K^{-1}&-eK^{-1}&-KF .
 \end{array}                                                   \tag{7}
\]
The orders in the two rows differ. Equations (4),(6) also follow
directly from vectorization, fixing all phases in (7).

## 2. Actual regular meridians and cyclic Weyl coordinates

Let \(v e_a=Q^{-a}e_a\), and let \(T e_a=e_{a-1\ ({\rm mod}\ N)}\).
Then
\[
 v^N=T^N=I,\quad Tv=Q^{-1}vT,\quad K=-q^{-1}v,\quad
 e=q(Q^{-1}v-1)T,\quad F=(1-v^{-1})T^{-1}.
 \tag{8}
\]
These are exact physical matrices: the apparent cyclic wrap of \(e\)
has coefficient \(Q^{-1}v_d-1=0\), and that of \(F\) has coefficient
\(1-v_0^{-1}=0\). No endpoint arrow was restored.

Use M's canonical ordered matrices
\[
 b_-=\begin{pmatrix}1&0\\-KF&K\end{pmatrix},\quad
 b_+=\begin{pmatrix}K&e\\0&1\end{pmatrix},\quad
 G=b_-^{-1}b_+
   =\begin{pmatrix}K&e\\FK&K^{-1}+Fe\end{pmatrix}.
 \tag{9}
\]
Their inverses are bounded physical matrices. M proves
\[
 G^2-cG+QI_2=0,\qquad
 G^{-1}=Q^{-1}(cI_2-G),\qquad c=-2q.
 \tag{10}
\]
Thus an inverse entry is a linear combination of regular entries and
constants. In the Weyl coordinates, (9) is exactly
\[
 G=\begin{pmatrix}
 -q^{-1}v&q(Q^{-1}v-1)T\\
 q(1-v)T^{-1}&q(v-2)
 \end{pmatrix}.
 \tag{11}
\]
In particular its lower-right entry has no \(v^{-1}\) term.
Replacing \(e=qE\) by \(E\) would change this finite identity.

For physical head \(j\), set \(P_{j-1}=b_{-,j-1}\cdots b_{-,1}\)
and retain the actual based meridian
\[
 H_j=P_{j-1}^{-1}G_jP_{j-1}.
 \tag{12}
\]
At principal level the physical \(SL_2\) lift is \(-H_j\). M proves that these are the
actual quantum Hurwitz observables of both signed crossings, with
bounded polynomial inverses. We count each entry of \(H_j\) or
\(H_j^{-1}\) as one regular entry. A regular word is an ordered
product of such scalar operator entries, or a finite sum of them.
No localization by a head Gauss entry is included in this definition.

The \(N^{2k}\) matrices
\[
 W_{\mathbf a,\mathbf b}
       =\prod_{i=1}^k v_i^{a_i}T_i^{b_i},
              \qquad 0\le a_i,b_i<N,
\]
are an orthonormal basis for \(\tau_k(X^\dagger Y)\). Hence
\[
 X=\sum_{\mathbf a,\mathbf b}x_{\mathbf a,\mathbf b}
                       W_{\mathbf a,\mathbf b},\qquad
 \tau_k(X)=x_{\mathbf0,\mathbf0},\quad
 \tau_k(X^\dagger X)=\sum|x_{\mathbf a,\mathbf b}|^2 .
 \tag{13}
\]
Every reduction here is cyclic. Ordinary Laurent coefficients cannot
replace these coefficients when exponents cross a multiple of \(N\).

## 3. The exact two-head flag module

We give the full action on a single cup, not only its value on \(I\).
Let \(X=f(v)T^m\), \(m\in\mathbb Z\), and put
\[
 M_m=Q^m,\qquad D_Qf(v)=\frac{f(Qv)-f(v)}v .
\]
The displayed quotient is a polynomial.

The first based matrix is \(H_1=G_1\), and its entries act by left
multiplication in (11). Write \(\mathcal H_{ab}(X)\) for the exact
Choi action of the entry \((H_2)_{ab}\):
\((H_2)_{ab}\mathscr C(X)=\mathscr C(\mathcal H_{ab}(X))\).
Direct multiplication of \(H_2=b_{-,1}^{-1}G_2b_{-,1}\), followed
by (6),(7), gives
\[
 \begin{split}
 \mathcal H_{11}(X)&=XK^{-1}+KF XeK^{-1},\\
 \mathcal H_{12}(X)&=-KXeK^{-1},\\
 \mathcal H_{22}(X)&=-FKXeK^{-1}+X(K+eF),\\
 \mathcal H_{21}(X)&=FXK^{-1}-K^{-1}XF
                     +FKFXeK^{-1}-FX(K+eF).
 \end{split}                                                   \tag{14}
\]
These are linear operators on the matrix source. They are not
multiplication by four substituted scalar entries.

For completeness their polynomial forms are
\[
 \mathcal H_{11}(fT^m)
 =q[(v-1-M_m)f(Qv)+M_mD_Qf(v)]T^m,
\]
\[
 \mathcal H_{12}(fT^m)=-q(v-QM_m)f(v)T^{m+1},\qquad
 \mathcal H_{22}(X)=-Q\mathcal H_{11}(X)-2qX,
 \tag{15}
\]
and
\[
 \mathcal H_{21}(fT^m)=q\,\frac{\mathcal N_{m,f}(v)}{v^2}T^{m-1},
\]
\[
 \begin{split}
 \mathcal N_{m,f}(v)={}&(v-M_m)f(v)\\
 &+(v-1)[2v-M_m(1+Q^{-1})]f(Qv)\\
 &+Q(v-1)(v-Q^{-1})(v-M_m/Q)f(Q^2v).
 \end{split}                                                   \tag{16}
\]
There is no pole in (16). Its constant coefficient is zero.
Its coefficient of \(v\) also vanishes separately for the constant
and linear coefficients of \(f\). For example those two linear
coefficient cancellations are
\[
 -2-M_m/Q-M_m+1+1+M_m+M_m/Q=0,\qquad
 M_m(1+Q)-M_m-QM_m=0.
\]
Thus \(v^2\) divides the numerator as a polynomial, at every level.
Equations (15),(16) show that each entry raises clock polynomial
degree by at most one. This holds before reducing \(v^N=1\).

One check on the order is obtained by applying (14) to \(I\).
If \(G_1=(g_{ab})\), the exact result is
\[
 H_2\psi=
 \begin{pmatrix}
 g_{22}&-Qg_{12}\\
 -Qg_{21}&Qg_{11}-(Q-1)g_{22}
 \end{pmatrix}\psi .
 \tag{17}
\]
This tends to the classical inverse, but does not authorize replacing
products by entrywise multiplication of (17). Their exact action is
composition of the operators (14).

## 4. Completed pairs and arbitrary width

For a completed pair retain the actual totals
\(K_{\rm pair}=K_1K_2\) and \(F_{\rm pair}=F_1+K_1^{-1}F_2\).
The same Choi calculation gives
\[
 K_{\rm pair}\mathscr C(fT^m)=M_m\mathscr C(fT^m),
\]
\[
 F_{\rm pair}\mathscr C(fT^m)
  =\mathscr C\!\left(
       [f(Qv)-M_m^{-1}f(v)-D_Qf(v)]T^{m-1}\right).
 \tag{18}
\]
For the second identity, (6) first gives
\(FX-K^{-1}XKF\); its two negative powers of \(v\) combine
into \(-D_Qf\). Both maps preserve clock polynomial degree.
So do \(K_{\rm pair}^{\pm1}\) and their ordered products with
\(F_{\rm pair}\).

The exact coproduct order is
\[
 b_{-,{\rm pair}}=b_{-,2}b_{-,1}
 =\begin{pmatrix}1&0\\-K_{\rm pair}F_{\rm pair}&K_{\rm pair}\end{pmatrix},
 \qquad
 b_{-,{\rm pair}}^{-1}
 =\begin{pmatrix}1&0\\F_{\rm pair}&K_{\rm pair}^{-1}\end{pmatrix}.
 \tag{19}
\]
Consequently dressing a later meridian by any preceding completed
cup pair preserves the clock degree of that preceding pair.
This statement uses the full source action (18), including when
the preceding pair has already been acted on by other entries.

Tensor the polynomial modules in their original pair order.
For an odd head of a pair, its own \(G\) acts by left multiplication;
for an even head, its own based action is (14). Earlier completed
pairs act through (19). An entry of a finite auxiliary matrix product
is a sum of compositions of these stated maps. This proves
\[
 \boxed{\quad
 \mathscr C_k^{-1}W\psi_0
   =\sum_{\mathbf m}f_{\mathbf m}(v_1,\ldots,v_k)
                       T_1^{m_1}\cdots T_k^{m_k},\qquad
 \deg f_{\mathbf m}\le L
 \quad}                                                       \tag{20}
\]
for every regular word \(W\) of length at most \(L\).
The degree is total clock polynomial degree. Inverse meridian
entries obey the same bound by (10). The proof is induction:
a prefix action preserves total degree and each own entry adds
at most one. Linearity covers nonseparable coefficient polynomials.

All calculations hold modulo the actual cyclic relations and include
\(N=2\), composite levels, arbitrary shifts and empty prefixes.
Polynomial division in (15),(16) was done before that reduction.
No physical pair-Casimir nilpotent direction or complementary source
coordinate is deleted.

## 5. The original marked scalar is one Frobenius coefficient

Put \(p=k-1\) and let
\(\mathcal P=\prod_{i=1}^p\mathcal Q_{2i}\), where
\(\mathcal Qe_a=Q^ae_a\). On the total integer degree \(kd\) subspace,
the literal row is exactly
\[
 \ell_0=(x^d/N^2)^p N^{-3}u_0^\dagger\mathcal P.
 \tag{21}
\]
Indeed an ordinary cap is
\((x^d/N^2)\mathbf p^\dagger(I\otimes\mathcal Q)\).
On pair degree \(d\), the last marked row is
\(N^{-3}\mathbf p^\dagger\). The ordinary caps first fix the degrees
of their own pairs; total degree then forces degree \(d\) on the
last pair. This proves (21), including its phase and its necessary
domain. It is not an equality of ambient rows.

For any actual degree-preserving word \(R\), (5),(21) give
\[
 Z_N(R)=x^{dp}N^p\langle\psi_0,\mathcal P R\psi_0\rangle.
\]
The Choi clock identity is
\(U\mathcal Q U^\dagger=Q^{-1}v\). Therefore the exact full-source
period is
\[
 \boxed{\quad
 Z_N(R)=x^{dp}N^pQ^{-p}\,
             \tau_k(v_1\cdots v_p X_R)
        =x^{dp}N^pQ^{-p}\,x_{\boldsymbol\eta,\mathbf0}(R),
 \quad \boldsymbol\eta=(d,\ldots,d,0).
 \quad}                                                       \tag{22}
\]
Here \(x_{\mathbf a,\mathbf b}(R)\) are the canonical cyclic Weyl
coefficients (13) of the full \(X_R\). For \(k=1\) the product is
empty and \(\boldsymbol\eta=0\). Equivalently the prefactor is
\(N^px^{-dp}\), since \(x^{2d}=Q\).
No coefficient in (22) has been normalized using its unknown value.

The full coefficient chart and boundary budget satisfy
\[
 \sum_{\mathbf a,\mathbf b}|x_{\mathbf a,\mathbf b}(R)|^2
       =\|R\psi_0\|_{\rm phys}^2,\qquad
 |Z_N(R)|\le N^p\left(\sum|x_{\mathbf a,\mathbf b}(R)|^2\right)^{1/2}.
 \tag{23}
\]
The initial state is \(X_I=I\). The normalized cup has norm one
and the extension (22)'s row has dual norm \(N^p\).
Any true-source constraints are carried by the same unitary map;
the whole matrix space is not asserted to be the saturated source.

There is a precise selection cutoff for regular observations.
If a degree-preserving \(W\) is a sum of regular words of length
at most \(L\), (20),(22) imply
\[
 Z_N(W)\ne0\quad\Longrightarrow\quad L\ge(k-1)(N-1).
 \tag{24}
\]
Indeed every surviving term must supply exponent at least \(N-1\)
in each of the first \(p\) clock variables before cyclic reduction.
Their sum is at least \(p(N-1)\). Shift aliases cannot change this
clock degree requirement. At \(k=1\) the assertion is vacuous.
An actual crossing has level-dependent degree; (24) makes no
claim that a fixed braid word is a bounded regular word.

## 6. A regular holomorphic flag-circle limit

The true cup is a positive vector state. For its fixed holomorphic
regular observations it has the following boundary representative,
before its original closing is applied.
For \(w\) on the unit circle put
\[
 G_0(w)=\begin{pmatrix}0&-w^{-1}\\w&-2\end{pmatrix}.
\]
It has determinant one, trace \(-2\), and a noncentral parabolic flag
\([w^{-1}:1]\). For any fixed regular word \(W\),
\[
 \begin{split}
 \langle\psi_0,W(H_1,\ldots,H_{2k})\psi_0\rangle
   =\int_{\mathbb T^k}
    W(&G_0(w_1),G_0(w_1)^{-1},\ldots,\\
      &G_0(w_k),G_0(w_k)^{-1})
                   \prod_{i=1}^k\frac{dw_i}{2\pi i w_i}
       +O_W(N^{-1}).
 \end{split}                                                   \tag{25}
\]
This includes inverse words by (10).

Here is a direct proof from the actual module. For fixed word degree,
all shifts and clock degrees are bounded independently of \(N\).
For sufficiently large \(N\), normalized cyclic trace in (13)
therefore becomes ordinary constant term in \(v_i,T_i\).
The coefficient formulas (15),(16),(18) are regular Laurent
polynomials in \(q\) after their proved divisions. Replacing \(q\)
by one costs \(O_W(N^{-1})\). At \(q=1\) and \(v=0\), the first
matrix in (11) is \(G_0(w)\), with \(T=w^{-1}\).
The second-pair maps become multiplication by \(G_0(w)^{-1}\).
A completed-pair \(K_{\rm pair}\) becomes one and
\(F_{\rm pair}\) becomes zero, so preceding prefixes become identity.
Finally constant term in \(T_i\) is the stated flag Haar integral.
This proves (25) with all original based orders retained.

Formula (25) concerns the holomorphic regular algebra, not its full
closure under Hermitian adjoints. The flag curve is not asserted to
represent that larger positive moment problem. Formula (22) also has
its separate unitary clock insertion and growing selected exponent;
neither may be removed to replace the original scalar by (25).
The flag variables are relative boundary data, not independently
declared global framing gauges or knot meridians chosen after sewing.

## 7. What this changes and what remains

The coordinate map is unitary on the complete physical source.
It retains the entire cup, every coherent input term, actual signed
crossings, the original last mark, and the separate \(\chi_N\).
It does not project to a selected coideal height or a value-only
pair-Casimir quotient.
The statements are at the fixed quantum root. Parameter normals require
their original families; the cyclic Weyl identities are not differentiated
as off-root identities.

The exact maps (14)--(20) supply a canonical polynomial module for
regular quantum holonomy observations. Equation (22) identifies the
original scalar's precise coefficient in that same full source.
A change to these fixed linear coordinates preserves the degree of
a polynomial variational formulation; no convexity theorem for an
anchored quartic is inferred.

Degree four in auxiliary variational variables is not bounded degree
in the regular physical meridian entries. The level-dependent
crossing, its original Frobenius coefficient and all remaining
coherent sewing must still be estimated. No volume lower bound,
nonzero original scalar, or finite-exception theorem is proved here.

## Complete inputs and coverage

Generic vectorization, maximally entangled cap marginals and their
source-projection guard already occur in
[the earlier cap-projection note](research_main_color_cap_projection_energy.md).
No novelty for those facts or Weyl orthogonality is claimed.
B supplies the physical cup, ordinary and marked caps, their integer
degree conventions and original scalar. M supplies the actual ordered
quantum meridians, polynomial inverse and signed Hurwitz transport.
The additions are the typed polynomial module at every width and
the exact original co-source coefficient in that full module.

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| B | [Balanced original marked observations](research_coideal_balanced_marked_height_observations.md) | 467 | 214c462d38a4e1c8bbe64e998d21f259859909a89e8767fde5b234f6dbdde4a6 |
| M | [Bounded actual quantum meridians](actual_bounded_quantum_meridian_transport.md) | 215 | dac1e5656b4b1e6923b8be5efc0e0543428fc3a2829d1183053cc899aa1fe5c8 |

Only written mathematics and text/hash operations were used. Earlier
final notes, public manuscripts and the progress ledger remain unchanged.

