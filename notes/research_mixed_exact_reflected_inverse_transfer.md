# Reflection gives the inverse conditional transfer

Private written deduction, 11 November 2026. Author-frozen after a
complete proof readback and checks of all four direct-source implications
and hashes. Independent review and adoption remain separate.

The positive three-type kernel has an exact reflection identity, but
reflection produces its matrix inverse. The reflection is about
the pair of indices whose sum is \(N-1\); it is not the substitution
of \(N-a\) for \(a\). With this distinction the diagonal factorial
weight also has an exact reflected inverse. Both physical transfers
preserve the same indefinite Hermitian form after their original
powers of \(N\) are restored.

These identities retain the full finite source. They do not give a
positive norm estimate for the remaining second-coordinate interval.
The final section proves why the preserved form cannot be replaced
by a positive invariant inner product.

The existence of an indefinite conserved form is already established
in the [complete-source form theorem](actual_complete_source_krein_and_cauchy_metric.md),
and [Section 18 of the Fourier notes](research_fourier_lower_bounds_and_almost_invariance.md#18-the-canonical-positive-form-in-full-physical-coordinates)
already distinguishes that form from the positive metric obtained
by inserting the turn. The
[three/four operator obstruction](research_mixed_three_four_operator_obstruction.md)
also rules out several common positive-metric arguments. The additional
content here is the explicit inverse of the physical Newton matrix,
the resulting inverse kernel at complex arguments, and the exact
normalization of the complete \(443\) pairing in those coordinates.
No claim of external novelty is made.

## 1. Original finite matrices

Fix \(N\ge2\), and put
\[
 r=e^{-2\pi i/N},\qquad D=N-1,\qquad
 P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\qquad
 b_j(X)=p_j(X)/P_j\quad(0\le j\le D).
 \tag{1}
\]
The letter \(D\) denotes the integer \(N-1\); diagonal matrices will
use a different symbol. Retain exactly the kernels of the
[torus composition theorem](research_mixed_conditional_torus_composition.md):
\[
 C_{\epsilon,N}(X,Y)
 =\sum_{j=0}^{D}X^{-j}b_j(X)b_j(Y)P_j^{-\epsilon},
 \qquad \epsilon=0,1.
 \tag{2}
\]
Let \(B\), \(\Delta\), and \(R\) be the \(N\)-by-\(N\) matrices
\[
 B_{ja}=b_j(r^a),\qquad
 \Delta=\operatorname{diag}(P_a^{-1}),\qquad
 R_{ab}=\mathbf1_{a+b=D}.
 \tag{3}
\]
In particular \(R=R^*=R^{-1}\). The exact support zeros give
\[
 B_{ja}=\begin{cases}
 P_{j+a}/(P_jP_a),&j+a\le D,\\
 0,&j+a>D.
 \end{cases}
 \tag{4}
\]
Thus \(B\) is symmetric. A bar denotes entrywise conjugation and
an asterisk denotes conjugate transpose. Factorwise conjugation gives
\[
 \overline{P_j}=(-1)^jr^{-j(j+1)/2}P_j,\qquad
 \overline{b_j(X)}=X^{-j}b_j(X)\quad(|X|=1).
 \tag{5}
\]
Consequently the physical kernel matrices are exactly
\[
 K_0=(C_{0,N}(r^a,r^b))_{ab}=\overline B B=B^*B,
 \qquad
 K_1=(C_{1,N}(r^a,r^b))_{ab}=\overline B\Delta B.
 \tag{6}
\]
Only \(K_0\) is assigned positivity. The complex weight in \(K_1\)
has not been replaced by its modulus.

## 2. Invert the finite Newton evaluation matrix

The product over the nontrivial roots of unity is \(P_D=N\).
Pairing its complementary factors gives
\[
                         P_a\overline{P_{D-a}}=N.
 \tag{7}
\]
Indeed the conjugated factors in the second product are precisely
the factors \(1-r^k\) with \(a+1\le k\le D\).

**Lemma 1.** The matrix \(B\) is invertible, and
\[
 (B^{-1})_{ab}=
 \begin{cases}
 \displaystyle\frac{r^{a+b-D}P_aP_b}{N P_{a+b-D}},&a+b\ge D,\\[2mm]
 0,&a+b<D.
 \end{cases}
 \tag{8}
\]

*Proof.* The matrix \(BR\) is upper triangular. By (7), its
nonzero entries are
\[
                (BR)_{jk}=\frac{\overline{P_k}}
                                      {P_j\overline{P_{k-j}}}
                               \qquad(j\le k).
 \tag{9}
\]
The upper triangular Toeplitz matrix with entries
\(1/\overline{P_{k-j}}\) has inverse with entries
\(r^{k-j}/P_{k-j}\). Here is a finite proof, valid at the root
of unity without an infinite-product limit. For \(0<n<N\),
\[
 \sum_{j=0}^n\frac1{\overline{P_j}}\frac{r^{n-j}}{P_{n-j}}
 =\frac{r^n}{P_n}
    \sum_{j=0}^n(-1)^jr^{j(j-1)/2}
                    \frac{P_n}{P_jP_{n-j}}=0.
 \tag{10}
\]
The final sum is the value at \(t=1\) of
\[
 \prod_{k=0}^{n-1}(1-r^kt)
  =\sum_{j=0}^n(-1)^jr^{j(j-1)/2}
                         \frac{P_n}{P_jP_{n-j}}t^j.
\]
This polynomial identity follows by induction after multiplying
by \(1-r^nt\). All its denominators are nonzero because \(n<N\).
The product at \(t=1\) contains the factor \(1-1\). For \(n=0\)
the convolution equals one. This proves the asserted Toeplitz
inverse.

Applying it to the diagonal factors in (9) yields
\[
 ((BR)^{-1})_{jk}
       =\frac{r^{k-j}P_k}{\overline{P_j}P_{k-j}}
                       \qquad(j\le k).
\]
Multiplication by \(R\) on the left and (7) give (8).
This also proves invertibility without an assumption about a
determinant. \(\square\)

Set
\[
 S=\operatorname{diag}(r^{a/2}),\qquad
       r^{a/2}:=e^{-\pi ia/N},\qquad \widetilde B=SBS.
 \tag{11}
\]
The half powers in this formula are fixed, rather than chosen
independently at each index. Equation (8) is equivalent to
\[
 \boxed{\quad
             \widetilde B^{-1}=R\overline{\widetilde B}R.
       \quad}
 \tag{12}
\]
For verification, if \(Q=\operatorname{diag}(r^a)\), then (8)
and (7) give
\[
 B^{-1}=rQR\overline B RQ.
\]
Also \(RS^{-1}R=r^{-D/2}S\), so
\[
 R\overline{\widetilde B}R
   =r^{-D}SR\overline B RS
   =rSR\overline B RS
   =S^{-1}B^{-1}S^{-1}.
\]
The equality \(r^{-D}=r\) keeps the finite phase in (12).

## 3. One preserved indefinite form for both transfers

Since \(\widetilde B\) is symmetric,
\(\overline{\widetilde B}=\widetilde B^*\). Thus (12) says
\[
                  \widetilde B^*R\widetilde B=R.
 \tag{13}
\]
The normalized factorial matrix
\[
                         \widetilde\Delta=\sqrt N\,\Delta
\]
satisfies the same identity:
\[
                 \widetilde\Delta^*R\widetilde\Delta=R.
 \tag{14}
\]
Indeed its nonzero reflected entry is
\(N/(\overline{P_a}P_{D-a})=1\), by (7).
Because \(R\) is real, entrywise conjugation of (13) proves
the same assertion for \(\overline{\widetilde B}\).

Use the normalized physical transfer matrices
\[
                  M_0=K_0,\qquad M_1=N K_1\Delta.
 \tag{15}
\]
These are the conditional transfers in the exact composition,
including the original extra factor \(N\) for type four.
Any exterior power of the original scalar \(\kappa\), which has
modulus one, preserves the identities below.
Direct multiplication in (6) gives
\[
 \begin{split}
 S^{-1}M_0S&=\overline{\widetilde B}\,\widetilde B,\\
 S^{-1}M_1S&=\overline{\widetilde B}\,
                \widetilde\Delta\,\widetilde B\,
                \widetilde\Delta.
 \end{split}
 \tag{16}
\]
In particular neither factor of \(\sqrt N\) in the second
line has been lost.

Define the Hermitian involution
\[
 H=SRS^{-1},\qquad
 H_{ab}=r^{a-D/2}\mathbf1_{a+b=D}.
 \tag{17}
\]
It has signature
\((\lceil N/2\rceil,\lfloor N/2\rfloor)\): each reflected
pair contributes one positive and one negative eigenvalue,
and the middle index when \(N\) is odd contributes \(+1\).
Equations (13)--(16) prove
\[
 \boxed{\quad M_\epsilon^*HM_\epsilon=H,
               \qquad M_\epsilon^{-1}=HM_\epsilon^*H,
               \qquad \epsilon=0,1.\quad}
 \tag{18}
\]
Equivalently these are matrices in one explicitly given indefinite
unitary group. For any finite word \(W=M_{\epsilon_1}\cdots
M_{\epsilon_m}\),
\[
                         W^{-1}=HW^*H.
 \tag{19}
\]
The adjoint reverses the order of the factors. This is an inverse
transfer identity, not a claim that a word is equal to its reflection.

## 4. Exact inverse kernel, including complex arguments

Since \(K_0\) is Hermitian, (18) specializes to
\[
       K_0^{-1}=HK_0H,\qquad
       (K_0^{-1})_{ab}=r^{a-b}(K_0)_{D-a,D-b}.
 \tag{20}
\]
There is a canonical Laurent-polynomial extension of this inverse:
\[
 \boxed{\quad
 C_N^{-}(X,Z)=\left(\frac ZX\right)^D
          C_{0,N}(r^{-1}X^{-1},r^{-1}Z^{-1}).
       \quad}
 \tag{21}
\]
Its incoming band is \([-D,0]\), and its outgoing band is
\([0,D]\), just as for the original kernel. At physical nodes
the factor \((Z/X)^D\) equals \(r^{a-b}\); hence its physical
matrix is exactly \(K_0^{-1}\). These degree bounds and the
physical values determine (21) uniquely.

Consequently, for all nonzero complex \(X,Z\),
\[
 \boxed{\quad
 \sum_{b=0}^{D}C_{0,N}(X,r^b)C_N^{-}(r^b,Z)
             =\frac1N\sum_{k=0}^{D}(Z/X)^k.
       \quad}
 \tag{22}
\]
Both sides have the same two Fourier bands. At the \(N^2\)
physical pairs their equality is \(K_0K_0^{-1}=I\); uniqueness
of polynomial interpolation proves the global identity.
The same proof gives the opposite-order identity.
Equivalently the left side is
\(N\operatorname{CT}_Y[C_{0,N}(X,Y)C_N^{-}(Y,Z)]\),
where \(\operatorname{CT}_Y\) extracts the coefficient of \(Y^0\).
There is no weighted alias in this last composition, since its
middle band is \([-D,D]\).

The shift \(r^{-1}\) in (21) is essential. It implements the
reflection \(a\mapsto D-a\) at the physical nodes. The older
[one-variable reflection identity](research_mixed_next_lower_complement_exact_reflection.md)
uses \(Y\mapsto Y^{-1}\), which instead sends \(a\mapsto N-a\)
away from zero and requires a separate endpoint formula.
Let \(d_N\) be the unique polynomial of degree less than \(N\)
whose physical values are \(d_N(r^a)=1/P_a\).
The shifted reflection also gives the simple physical identity
\[
                   d_N(r^{D-a})=\overline{P_a}/N.
 \tag{23}
\]
It does not turn \(d_N\) into the reciprocal of a nonvanishing
function on a complex contour. No division by that polynomial is
made in this argument.

## 5. The actual complete 443 contraction

Let \(u_a=U_{1,N}(w,r^a)\), with the full original endpoint
coefficient retained inside \(U_{1,N}\). The
[complete 44 source](research_mixed_complete44_second_far_real_arc.md)
is
\[
 f_N(w,Y)=\sum_{a=0}^{D}\frac{u_a}{P_a}C_{1,N}(r^a,Y).
 \tag{24}
\]
Thus its physical row vector is \(f=u\Delta K_1\).
After the entire second sum, define
\[
 g_N(w,Z)=\sum_{b=0}^{D}\frac{f_N(w,r^b)}{P_b}
                                      C_{0,N}(r^b,Z).
 \tag{25}
\]
The torus identity retains both Fourier sectors and says exactly
\[
 g_N(w,Z)=N\operatorname{CT}_Y[
       f_N(w,Y)d_N(Y)(1+Y^{-N})C_{0,N}(Y,Z)].
 \tag{26}
\]
Its physical row vector satisfies
\[
                        g=\frac1N u\Delta M_1M_0.
 \tag{27}
\]
This is an identity for the complete first and second finite sums,
not a replacement of either by its principal contour.

Since \(\Delta H\Delta^*=H/N\), (18) also yields the exact
preserved pairing
\[
 \boxed{\quad N^3 g(u)H g(v)^*=uHv^*\quad}
 \tag{28}
\]
for arbitrary incoming rows \(u,v\). To check the normalization,
insert (27), use
\(M_1M_0H(M_1M_0)^*=H\), and then use the displayed identity
for \(\Delta\). Setting \(u=v\) gives the quadratic identity;
using two rows retains the complete sesquilinear statement.
In particular it applies to the actual ordinary-color vectors and
their separately differentiated input vectors. No positivity is
assigned to either side of (28).

## 6. What the inverse identity does not estimate

The form (17) is indefinite for every \(N\ge2\). This is not
merely an inconvenient choice of coordinates. There is no positive
definite Hermitian form for which \(M_0=K_0\) is unitary, or even
a contraction. Indeed \(b_j(1)=1\), and hence
\[
                          (K_0)_{00}=N.
\]
As \(K_0\) is positive Hermitian, it has an eigenvalue at least
\(N>1\). Every operator norm induced by a positive inner product
is at least the spectral radius. In particular it cannot be at
most one. Equation (20) pairs its eigenvalues with their
reciprocals rather than putting them on the unit circle.

The expansion is also exponential in the level in some directions.
This follows from a written factorial estimate, without computing
an eigenvalue. Put \(k_N=\lfloor N/6\rfloor\), and define
\(J(x)=\int_0^x\log(2\sin\pi t)\,dt\) for \(0\le x\le1\).
The uniform sine
factorial formula in the
[boundary-strip proof](research_mixed_boundary_strip_bounds.md),
\(\log|P_j|=NJ(j/N)+O(\log N)\), gives
\[
 \log|B_{k_N,k_N}|=N\gamma+O(\log N),\qquad
 \gamma=J(1/3)-2J(1/6)>0.
 \tag{29}
\]
Here \(J(1/6)<0\), and \(J\) strictly increases from \(1/6\)
to \(1/3\); thus
\(\gamma> -J(1/6)>0\).
The rounding changes the action by \(O(N^{-1})\) on these
regular arguments. Since \(\|B\|_2\ge|B_{k_N,k_N}|\),
\[
             \lambda_{\max}(K_0)\ge e^{2N\gamma-O(\log N)}.
 \tag{30}
\]
The reciprocal identity gives a correspondingly small eigenvalue.
This bounds the cost of an unrestricted positive operator norm;
it is not a lower bound for the prescribed signed scalar.

For the remaining real interval \(18/25<q<7/8\), (21) reflects
the incoming index into a short interval, but it simultaneously
reflects the outgoing argument and replaces the kernel by its
inverse. Equations (19), (26), and (28) likewise concern complete
transfers. They do not identify a partial second-coordinate current
with a current already bounded elsewhere. A useful next estimate
would have to control the transformed source and observation, or
exploit cancellation in their pairing before taking a positive norm.
Neither a nonzero leading coefficient nor a new knot-volume limit
follows from the identities proved here.

## Direct source versions

| Source | Implication used | SHA-256 |
|---|---|---|
| research_mixed_conditional_torus_composition.md | Exact conditional kernels, physical Gram factorization, diagonal factorial weight and the two-sector constant-term identity | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |
| research_mixed_complete44_second_far_real_arc.md | Complete \(f_{44,N}\), original coherent cap and unnormalized physical first sum | 922a114d355f134aae94065d2c8996ac26d670f6dd5439f20285c7c7b627dd2e |
| research_mixed_next_lower_complement_exact_reflection.md | Comparison with the older unshifted one-variable reflection, its changed kernel and endpoint weight | aa48a56774b278c113d7bd678de36d46bdb286c439e433e019d6a117e49ae3e3 |
| research_mixed_boundary_strip_bounds.md | Uniform sine-factorial estimate, including the endpoint-uniform formulation | e288c5d0bcf77a073dbaa8bb2f27bd46ce208a56e63c8bd0e98dfdbbc8f8c6ff |

The following versions were read for the internal coverage comparison;
none is needed to prove the new identities above.

| Earlier result | Relevant overlap | SHA-256 |
|---|---|---|
| actual_complete_source_krein_and_cauchy_metric.md | Conserved indefinite form for the complete original source; positive Cauchy metric does not remove the coherent energy problem | 83ca3c3838b6ba50ac665bc0c97ed44483040d191de3e38cf647bbdd76acbd4b |
| research_fourier_lower_bounds_and_almost_invariance.md, Section 18 | Indefinite physical trace form, positive metric supplied by the turn, and retained closing observation | 60085c532ee9db7b293d0a58c3ddf8a837c54714ff3284d53673c4e42fccd38b |
| research_mixed_three_four_operator_obstruction.md | No common positive Hermitian realization of the two transfers of the stated kind; relative insertion is neither accretive nor a unit-scalar contraction | cc1a882e10f2ec2d43e3c603cc42012c5dd6b2bcb978f6b5bd4ad72744dc7459 |

This is written mathematics. No mathematical numerical evaluation,
test, import, compilation, or frozen-source edit is used.
