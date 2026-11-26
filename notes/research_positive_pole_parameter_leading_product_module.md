# Positive-pole parameter-leading rows for the actual endpoint product

Private written proof, 16 November 2026.

The ordinary six-channel module admits a selected-parameter leading
presentation whose spatial clearing roots are all within \(O(N^{-2})\)
of \(+2\). It does not require an inverse companion at the negative
endpoint. The construction retains every selected kernel coordinate,
the two source-alias coordinates, and all original first normals.

This is a necessary exact source system. Clearing can kill an
endpoint-supported forcing term; the original source definitions and
endpoint data therefore remain part of the presentation. No rank,
conditioning, quotient-rate, or scalar-closing conclusion is inferred
from these rows alone.

## 1. Ordinary calculus and the statement

Use the conventions of the pinned divided-difference module:
\[
 q=e^{\pi i/N},\quad s=q-q^{-1},\quad a=(q+q^{-1})/2,
 \quad c_0=2a,\quad \zeta=q^2+q^{-2},
\]
\[
 C=z(v)=v+v^{-1},\quad z_\pm=z(q^{\pm1}v),
 \quad\delta=s(v-v^{-1}),\quad
 U_1=(a^2-1)C,\quad U_2=(a^2-1)(C^2-4)=\delta^2/4.
 \tag{1}
\]
The half-step operators act on specified ordinary polynomials or
rational functions before reduction:
\[
 \mathcal Df=\frac{f(z_+)-f(z_-)}\delta,\qquad
 \mathcal Sf=\frac{f(z_+)+f(z_-)}2.
 \tag{2}
\]
Their exact product and composition rules are
\[
 \begin{split}
 \mathcal D(fg)&=(\mathcal Df)(\mathcal Sg)
                         +(\mathcal Sf)(\mathcal Dg),\\
 \mathcal S(fg)&=(\mathcal Sf)(\mathcal Sg)
                         +U_2(\mathcal Df)(\mathcal Dg),\\
 \mathcal D\mathcal S&=a\mathcal S\mathcal D+U_1\mathcal D^2,\\
 \mathcal S^2&=I+U_1\mathcal S\mathcal D+aU_2\mathcal D^2.
 \end{split}                                                   \tag{3}
\]
Matrix products below have their displayed order.

Set
\[
 p(C)=P_N(C)=2T_N(C/2)+2,\qquad
 f_i(C)=K_N(w_i,C),\quad w_i=2\cosh(\alpha_i/N),
\]
\[
 \lambda_i=(w_i-c_0)/s^2,\qquad
 \gamma_i=-P_N(w_i)/(N^4s^2),\qquad
 r_i(C)=\gamma_i/(C-c_0),
\]
\[
 \sigma=(2a^2-1)C^2-4aC+8-4a^2,
 \qquad \tau=2aC-4.
 \tag{4}
\]
The actual ordinary equation and its aliases are
\[
 (\sigma\mathcal D^2+\tau\mathcal S\mathcal D-\lambda_i)f_i
       =r_i p,\qquad
 \mathcal Dp=0,\quad\mathcal Sp=4-p.
 \tag{5}
\]
Write
\[
 Z_i=(f_i,d_i,h_i,t_i,p,1)^t,
 \quad d_i=\mathcal Df_i,\ h_i=\mathcal Sf_i,
 \ t_i=\mathcal S\mathcal Df_i.
 \tag{6}
\]
Fix a selected index \(i\) among \(r\ge1\) factors and let
\[
 g=\bigotimes_{j\ne i}Z_j,
 \qquad
 \mathcal P=(f_i g,d_i g,h_i g,t_i g)^t,
 \qquad \mathcal S_0=(p g,g)^t.
 \tag{7}
\]
The empty tensor is \(1\). Thus \(\mathcal P\), together with the
specified source columns \(\mathcal S_0\), retains the entire
ordinary \(6^r\) tensor. In particular its first product coordinate
is the original product of kernels.

**Theorem.** For fixed \(r\), at all sufficiently large levels,
there are a nonzero monic scalar polynomial \(d_N(C)\) and an
ordered polynomial matrix \(\mathcal B_i(C,J,D_1)\) such that
\[
 \boxed{\quad
 [w_i d_N(C)I-\mathcal B_i(C,J,D_1)]
                  \operatorname{can}\mathcal P
                   =\operatorname{can}\mathcal R_i .
 \quad}                                                       \tag{8}
\]
Here \(J=TCT\), \(D_1=V_1CV_{-1}\), and all operations are the
original ones. The following properties hold.

* The spatial degrees, word lengths, and matrix sizes are bounded
  in terms of \(r\), independently of \(N\). The polynomial \(d_N\)
  depends on \(q\), not on any endpoint parameter. Every root obeys
  \(|C-2|\le B_r/N^2\).
* \(\mathcal B_i\) is independent of \(w_i\), including
  \(P_N(w_i)\). Dependence on other endpoint parameters is retained.
  The actual right side is explicitly constructed below from
  \(\gamma_i\), \(g\), \(p\), and \(4-p\), before clearing.
* The two source columns in (7) are prescribed actual lower-factor
  columns, not additional unknown homogeneous directions. If a
  rectangular implementation stores all \(6^r\) coordinates in one
  column, append their definition rows; equivalently append
  \(w_i d_N\mathcal S_0=w_i d_N\mathcal S_0^{\rm actual}\).
  Scalar parameter-leading identity therefore holds on every
  non-prescribed selected coordinate; no derivative coordinate is
  omitted.
* The identity is obtained from ordinary polynomial identities by
  clearing and then canonical reduction. It preserves every
  double-root first normal and the odd simple-root value. It is
  not an inversion of \(d_N(C)\) in the finite algebra.

On bounded microscopic parameter sets the scalar coefficients have
at most polynomial growth in \(N\). This assertion does not assign
an exponential rate to any later transformed source column.

## 2. A positive-pole rational coefficient ring

For this proof call a rational spectral coefficient positive-pole
if its numerator and denominator degrees are bounded independently
of \(N\), and all its spatial poles are within \(O(N^{-2})\) of
\(+2\). Fixed scalar poles in \(q-1\) are allowed. Denominators in
the construction can be chosen independently of all endpoint
parameters. Finite sums, products, and matrix operations without
inversion preserve this class.

The class is also preserved by coefficient operations
\(\mathcal D,\mathcal S\). Indeed for a denominator \(b(C)\) use
\[
                  \mathcal N_q b(C)=b(z_+)b(z_-).
 \tag{9}
\]
It is a polynomial. Its symmetric numerator is invariant under
\(v\mapsto v^{-1}\). Its antisymmetric numerator is an ordinary
Laurent polynomial divisible by \(v-v^{-1}\); after division it
is invariant, hence a spectral polynomial. This is divisibility
of matrix coefficients entry by entry, not a statement only after
application to an actual solution. It adds no pole at \(v=-1\).
The scalar \(s^{-1}\) in (2) is harmless for spatial pole location.

If \(z(q^{\pm1}v)=2+O(N^{-2})\), its two angular solutions satisfy
\(q^{\pm1}v=1+O(N^{-1})\). Hence \(v=1+O(N^{-1})\) and
\(v+v^{-1}=2+O(N^{-2})\). This proves the quantitative pole
claim for (9), and for any fixed iteration of half shifts.

The common denominator from the original module is
\[
 d_0(C)=\sigma(C)(C-c_0)(C-2)(C-\zeta)^5.
 \tag{10}
\]
Every root is microscopic at \(+2\). For the only non-immediate
factor, put \(b=2a^2-1\); its two roots are exactly
\[
          \frac{2a\pm2\sqrt2(a^2-1)}b=2+O(N^{-2}).
 \tag{11}
\]
Here \(b\ne0\) at all sufficiently large levels. The other
roots in (10) are \(c_0,2,\zeta\). Thus all coefficient operations
on the pinned ordinary module remain in this ring.

## 3. Backward transport on the actual other-factor tensor

The pinned module supplies explicit rational matrices
\(\mathbf D_o,\mathbf S_o\), with denominators dividing a fixed
power of \(d_0\), such that
\[
                    \mathcal Dg=\mathbf D_o g,
          \qquad    \mathcal Sg=\mathbf S_o g.
 \tag{12}
\]
These equalities were derived on ordinary polynomials, with all
\(p,1\) channels present. Define
\[
 M_\pm(v)=\mathbf S_o(C)\pm\delta\mathbf D_o(C)/2,
\]
\[
 N_+(v)=M_-(qv),\qquad N_-(v)=M_+(q^{-1}v).
 \tag{13}
\]
Applying the backward half-step identity at \(qv\), and the
forward one at \(q^{-1}v\), gives exactly
\[
                 N_\pm(v)g(q^{\pm1}v)=g(v).
 \tag{14}
\]
No assertion that these matrices are inverse on arbitrary
six-channel data is needed.

Their invariant and divided anti-invariant parts are the following
positive-pole spectral matrices:
\[
 \begin{split}
 N_s&=\mathcal S\mathbf S_o-U_1\mathcal S\mathbf D_o
                                  -aU_2\mathcal D\mathbf D_o,\\
 N_d&=\mathcal D\mathbf S_o-a\mathcal S\mathbf D_o
                                  -U_1\mathcal D\mathbf D_o.
 \end{split}                                                   \tag{15}
\]
In fact \(N_s=(N_++N_-)/2\), \(N_d=(N_+-N_-)/\delta\).
To verify this use
\(\delta_\pm=a\delta\pm2U_1\) and expand (13). This explicitly
performs the ordinary antisymmetric division discussed in section 2.

Define operators on arbitrary rational spectral vector functions by
\[
 \mathcal D_g=N_s\mathcal D+N_d\mathcal S,
 \qquad
 \mathcal S_g=N_s\mathcal S+U_2N_d\mathcal D.
 \tag{16}
\]
Each preserves the positive-pole rational coefficient ring, including
when applied to constant vectors. Equations (13)--(14) imply, for
every ordinary scalar function \(f\) in the relevant rational field,
\[
 \mathcal D_g(fg)=(\mathcal Df)g,
 \qquad \mathcal S_g(fg)=(\mathcal Sf)g.
 \tag{17}
\]
Iteration is legitimate: the same identities hold for every new
scalar \(\mathcal Df,\mathcal Sf,\ldots\). They do not require
inverting a matrix on redundant formal coordinates.

## 4. All four selected coordinates have parameter-leading rows

Suppress the selected index on \(f,d,h,t,r,\lambda\). Define,
with coefficient operations as in (2),
\[
 A=\mathcal S\sigma+U_1\mathcal S\tau+aU_2\mathcal D\tau,
 \quad B=\mathcal D\sigma+a\mathcal S\tau+U_1\mathcal D\tau,
 \quad c_\tau=\mathcal D\tau=2a,
\]
\[
 A_1=\mathcal SA+U_1\mathcal SB+aU_2\mathcal DB,
 \qquad B_1=\mathcal DA+a\mathcal SB+U_1\mathcal DB.
 \tag{18}
\]
The following are exact ordinary rational identities:
\[
 \begin{split}
 \lambda f={}&(\sigma\mathcal D^2+\tau\mathcal S\mathcal D)f-rp,\\
 \lambda d={}&(A\mathcal D^2+B\mathcal S\mathcal D+c_\tau)d
                                      -(\mathcal Dr)(4-p),\\
 \lambda h={}&(U_2B\mathcal D^2+A\mathcal S\mathcal D
                                    +\mathcal S\tau)d
                                      -(\mathcal Sr)(4-p),\\
 \lambda t={}&[U_2B_1\mathcal D^4+A_1\mathcal S\mathcal D^3
                            +(\mathcal SB)\mathcal D^2]f
                    +c_\tau t-(\mathcal S\mathcal Dr)p.
 \end{split}                                                   \tag{19}
\]
For the second and third rows apply \(\mathcal D\) and
\(\mathcal S\) to (5), use (3), and retain
\(\mathcal Dp=0,\mathcal Sp=4-p\). Their two highest terms are
exactly the two equations in the original module. For the fourth
row apply \(\mathcal S\) to the second. Since \(c_\tau\) is constant,
the operator terms are those displayed in (19), using
\(\mathcal D^3d=\mathcal D^4f\) and
\(\mathcal S\mathcal D^2d=\mathcal S\mathcal D^3f\).
The source transforms as
\[
        \mathcal S\{(\mathcal Dr)(4-p)\}
                              =(\mathcal S\mathcal Dr)p,
 \tag{20}
\]
because \(\mathcal S(4-p)=p\) and \(\mathcal D(4-p)=0\).
This is the second source alias, not a removable convention.

Multiply every row by \(g\), and use (17) to replace each word in
\(\mathcal D,\mathcal S\) acting on a selected scalar by the same
ordered word in \(\mathcal D_g,\mathcal S_g\) acting on its product
coordinate. The resulting matrix equation is
\[
                        \lambda_i\mathcal P
                             =\mathcal A_i\mathcal P+\mathcal F_i,
 \tag{21}
\]
where \(\mathcal A_i\) is independent of \(w_i,P_N(w_i)\), and
\[
 \mathcal F_i=-\big(r_i p g,
        (\mathcal Dr_i)(4-p)g,
        (\mathcal Sr_i)(4-p)g,
        (\mathcal S\mathcal Dr_i)p g\big)^t.
 \tag{22}
\]
Every word in \(\mathcal A_i\) has even half-step parity and order
at most four. Consequently it contains only full shifts
\(v\mapsto q^{2k}v\), with \(|k|\le2\), after expansion.
All coefficient operations and source poles are positive-pole.

## 5. Positive localization of the even operator calculus

Here is a coefficient-level conversion audit. It is stronger than
removability after applying an operator to the actual \(g\).

**Lemma.** An even word in \(\mathcal D,\mathcal S\), with matrix
coefficients in the positive-pole ring, is a finite ordered polynomial
in \(J,D_1\) with left coefficients in that same ring. For bounded
word length the degrees and the number of half shifts needed in its
denominators are bounded. No negative-endpoint clearing is required.

**Proof.** The product rules move a coefficient past one half-step
without leaving the ring. The last two identities in (3) then give
the finite normal form
\[
       H(C)+\sum_{j=1}^k
          \{A_j(C)\mathcal D^{2j}
                      +B_j(C)\mathcal S\mathcal D^{2j-1}\}.
 \tag{23}
\]
One verifies this inductively by moving \(\mathcal S\)'s left with
\(\mathcal D\mathcal S=a\mathcal S\mathcal D+U_1\mathcal D^2\)
and removing adjacent \(\mathcal S^2\)'s. The coefficient product
rules handle every coefficient created during this reduction.

Let \(E f(v)=f(q^2v)\). The forward coefficient of
\(\mathcal D^{2j}\) is \(1/(\delta_0\cdots\delta_{2j-1})\),
where \(\delta_l=s(q^lv-q^{-l}v^{-1})\). For
\(\mathcal S\mathcal D^{2j-1}\) it is \(\delta_0/2\) times this.
Write the forward coefficient of \(J\) as \(-A_*(v)\), where
\[
 A_*(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)}.
\]
The ratio of the leading coefficient of \(\mathcal D^{2j}\)
to that of \(J^j\) is exactly
\[
 R_j(v)=\prod_{l=0}^{j-1}
          \frac{q^{4l+2}v^2}{s^2(q^{2l+1}v-1)^4}.
 \tag{24}
\]
In particular all shifted negative divided-difference poles cancel
in this ratio. If the top pair in (23) is nonzero, set
\[
          u(v)=\{A_k(C)+\delta B_k(C)/2\}R_k(v).
 \tag{25}
\]
The backward ratio is \(\iota u=u(v^{-1})\).
The corresponding extreme ratios of \(D_1J^{k-1}\) to \(J^k\)
are \(-q^{-1}v^{-1}\) and \(-q^{-1}v\). Therefore the spectral
matrix coefficients
\[
       b(C)=q\frac{u-\iota u}{v-v^{-1}},\qquad
       a(C)=u+q^{-1}v^{-1}b(C)
 \tag{26}
\]
match both extremes of \(aJ^k+bD_1J^{k-1}\).
They are positive-pole. To see the division explicitly, multiply
\(u\) by the product of its denominator and its inversion. The
resulting antisymmetric Laurent numerator is divisible by
\(v-v^{-1}\), so no pole at \(-1\) is introduced. Every remaining
angular pole in (24)--(26) tends to \(+1\), giving a spectral
pole \(2+O(N^{-2})\).

Both \(J\) and \(D_1\) belong to the even filtered calculus with
polynomial coefficients. For \(J\) this is
\(J=c_0+s^2(\sigma\mathcal D^2+\tau\mathcal S\mathcal D)\).
For \(D_1\), its forward coefficient is \(q^{-1}A_*(v)/v\), its
backward coefficient is its inversion, and
\(D_11=4q^{-1}-q^{-2}C\). Multiplication of its forward coefficient
by \(\delta\delta_+\) gives the Laurent polynomial
\[
       \alpha(v)=-q^{-1}v^{-1}s^2(\sigma+\delta\tau/2).
\]
The spectral polynomials
\[
        \frac{\alpha+\iota\alpha}{2},\qquad
        \frac{\alpha-\iota\alpha}{\delta}
\]
are the coefficients of \(\mathcal D^2,\mathcal S\mathcal D\),
respectively; the stated value on \(1\) supplies the order-zero
coefficient.
These checks use the original physical \(D_1\) convention.

Subtracting the matched pair from (23) cancels its two highest
full shifts. Its normal form therefore has order at most \(2k-2\):
the two leading coefficients determine \(A_k,B_k\) uniquely over
the rational field. Continue by induction. The final order-zero
matrix is in the ring because the original operator and every
subtracted operator preserve that ring on arbitrary constant
vectors. This proves the lemma. \(\square\)

Apply the lemma to (21). Finite products and inversions of scalar
denominators already known to have microscopic positive roots give
a common clearing \(d_N(C)\), independent of the endpoint parameters.
Include the source denominators from (22). Multiply (21) by
\(s^2d_N\), use \(s^2\lambda_i=w_i-c_0\), and normalize the
scalar leading polynomial to be monic. This proves (8), with
\[
 \mathcal B_i=c_0d_NI+s^2d_N\mathcal A_i,
              \qquad \mathcal R_i=s^2d_N\mathcal F_i.
 \tag{27}
\]
The notation \(d_N\mathcal A_i\) means its cleared ordered
polynomial expression from the lemma, not evaluation of a rational
function at a nonunit operator.

## 6. Full quotient, source data, and subsequent original turns

All the preceding half-step work was performed before reduction.
Only the full-step even equations were converted and cleared.
The resulting \(C,J,D_1\) operators preserve the original full
algebra \(\mathcal A_N=\mathbb C[C]/(P_N)\). Their ordinary
residuals are \(P_N\) multiples. At the regular physical rows,
\[
 P_N(2\cos(2\pi u+\pi/N))=4\sin^2(\pi Nu),
\]
so the residual and its first angular derivative vanish. This
gives the actual first-normal equations with every coefficient
derivative. At the odd simple spectral node only its original
value is imposed. The ordinary antisymmetric descent retains
the odd angular jet where a Laurent source is stored.

The poles have been cleared, not inverted in \(\mathcal A_N\).
For example the selected source contains \(p/(C-c_0)\), which
is an actual nonzero endpoint radical after ordinary cancellation.
A clearing containing \(C-c_0\) may turn it into a \(P_N\) multiple.
This only weakens a necessary equation. It does not delete the
original forcing, its first normal, or any actual collar value
from the definition of the source. The ordinary definitions
(6)--(7), (12), (17), and (22) are retained alongside (8).

Likewise the lower-factor columns in (7) are not replaced by
arbitrary homogeneous solutions. Half-step evaluation of another
factor can reach even half-grid colors; its dependence on its
free endpoint need not have bounded polynomial degree. Such
coefficients remain actual supplied source data. They are not
identified with a fixed-degree odd physical row.

Polynomial gauges \((C-2)^b\) of any fixed order can be appended
without a negative clearing: perform the rational conjugation
by this gauge before clearing and retain its actual polynomial
definition. The new generating divisor is \(C-2\); the half-step
coefficient operations also introduce its finitely many fixed
\(q\)-shift norms. All their roots are still \(2+O(N^{-2})\) by
section 2. Recovery must retain the original homogeneous directions
and endpoint data.

Applying an original \(V_n\) to (8) gives its exact ordered
conjugate under
\[
          C\mapsto D_n,\qquad J\mapsto J,
          D_1\mapsto D_{n+1}.
 \tag{28}
\]
Shared outside coefficients and their mixed derivatives remain
inside these identities. Subsequent full-step tensor coupling and
an outer original turn may be performed by the pinned interface;
this theorem does not prove its window rank or regular extremes.
Its concrete conclusion is that the inner ordinary spatial
divisions associated to this parameter-leading clearing can be
chosen entirely in a fixed microscopic disk about \(+2\).
Their transformed norms still require a separate source theorem.

## 7. Coverage and complete direct sources

The earlier \(6^r\) module has positive-pole clearings but is not
selected-parameter leading. The Laurent two-state connection in
projected recovery produces negative-endpoint divisors. The added
construction uses backward transport on the actual augmented
half-step module, all four selected rows (19), and the coefficient
localization lemma to obtain (8) without those divisors.

The following complete direct sources were freshly read, with
their used implications and hashes checked:

* [Ordinary divided-difference product module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  exact half-step identities, both source aliases, all six channels,
  coefficient matrices and their denominator list.
* [Original full-step interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  original full-step and \(D_1\) conventions, ordinary conversion,
  odd descent, full-normal residuals and literal turn conjugation.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
