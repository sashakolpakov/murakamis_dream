# Central resolvent, inverse Jacobian, and compact source symmetry

Private written proof, 18 November 2026.

The original highest-cut pivotal functional is an explicit central
resolvent inside an ordinary full trace. This gives a compact coherent
period with no cut coupon to reset under Weyl turnover. The actual
turnover and half-twist return yield a specified rational exact-form
current, including every meridian pole and finite-part term. A symmetric
representative has a literal orientation-preserving involution on the
original product of compact spheres.

These are exact finite-source identities. They do not identify the two
geometric eigenline contributions of the reduced trace. The opposite
polarization and local relative boundary currents remain.

The complete directs H, P, C and G are listed at the end. H fixes the
pointed functional, P the whole-meridian turnover, C the compact kernel
calculus, and G the resolved reduced geometric chart. All new
Chebyshev, inverse-Jacobian, and compact-current calculations are below.

## 1. Exact central full-trace reconstruction

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and \(m\ge2\)
heads with common meridian \(M\) near one. The quantum parameter stays
fixed at \(q_N\). Write \(x=-M/q\), and let \(W(M)\) be an analytic
actual total intertwiner. It may be the original zero-framed braid
word, with every prescribed scalar retained. The original source is
\[
\Phi_0(W)=\operatorname{Tr}_{\rm full}
       ((P_0\otimes K_{\rm r}^{1-N})W).
\tag{1}
\]
Let \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\), with its Laurent-polynomial
continuation at \(z=\pm1\). Define two polynomial families by
\[
\begin{split}
&T_0(t)=2,\quad T_1(t)=t,\quad T_{j+1}(t)=tT_j(t)-T_{j-1}(t),\\
&U_0(t)=1,\quad U_1(t)=t,\quad U_{j+1}(t)=tU_j(t)-U_{j-1}(t).
\end{split}
\tag{2}
\]
They are monic in positive degree, and substitution proves
\[
T_N(z+z^{-1})=z^N+z^{-N},\qquad
U_{N-1}(z+z^{-1})=D_N(z).
\tag{3}
\]
Use the full ordered Casimir
\(\Omega_\Sigma=F_\Sigma E_\Sigma+qK_\Sigma+q^{-1}K_\Sigma^{-1}\),
with the scaled lowering operator of H and P. Set
\[
Z_N(M)=U_{N-1}(-\Omega_\Sigma(M))^{-1}.
\tag{4}
\]
The inverse is taken generically and then as a meromorphic matrix;
it is not evaluated separately at a singular root color. Exactly,
\[
\boxed{\displaystyle
\Phi_0(W(M))=\frac{D_N(M)}{N}
                    \operatorname{Tr}_{\rm full}(Z_N(M)W(M)).
}
\tag{5}
\]

No semisimplicity is needed. In the actual triangular coordinates,
H and P give
\[
S_m^{-1}\Omega_\Sigma S_m
 =F_1E_{\rm r}-(MK_{\rm r}+M^{-1}K_{\rm r}^{-1}),\qquad
S_m^{-1}WS_m=\sum_{n=0}^{d}F_1^n\otimes B_n .
\tag{6}
\]
Both are lower triangular in the first occupation. Every diagonal
block of the second is \(B_0\); every diagonal block of
\(U_{N-1}(-S_m^{-1}\Omega_\Sigma S_m)\) is \(D_N(MK_{\rm r})\).
The diagonal of its inverse is the inverse diagonal. Hence
\[
\operatorname{Tr}_{\rm full}(Z_NW)
 =N\operatorname{Tr}_{\rm r}(D_N(MK_{\rm r})^{-1}B_0).
\tag{7}
\]
H's exact scalar-kernel identity proves (5). Its meromorphic
continuation is prescribed by the analytic original left side.
All Jordan entries and polar coefficients remain. The coupon (4)
commutes with every total generator and actual total intertwiner.

A mark failing total intertwining retains its Ward defect and is
not covered by (5). These fixed-root meridian identities are not
off-root quantum-normal identities.

## 2. The exact inverse-Jacobian source

Put \(r=m-1\), \(K_{\rm r}(M)=M^rK_0\), and
\(\varepsilon=(-1)^{(N+1)r}\), so \(K_0^N=\varepsilon I\).
Let \(\mathcal X\) be the \(N\) eigenvalues \(\chi\) of \(K_0\),
with occupation projectors \(P_\chi\). Define
\[
z_\chi=M^m\chi,\qquad
\lambda_\chi=-z_\chi-z_\chi^{-1},\qquad
t_\chi(M)=\operatorname{Tr}_{\rm r}(P_\chi B_0(M)).
\tag{8}
\]
The monic degree-\(N\) polynomial with these generic distinct roots is
\[
p_M(\lambda)=(-1)^N
 \bigl[T_N(-\lambda)
       -\varepsilon(M^{mN}+M^{-mN})\bigr].
\tag{9}
\]
Indeed \(z_\chi^N=\varepsilon M^{mN}\), and (3) proves each
root equation. Differentiating (3) gives \(T_N'=NU_{N-1}\), hence
\[
p_M'(\lambda_\chi)=(-1)^{N+1}N D_N(z_\chi).
\tag{10}
\]
Let \(t_M(\lambda)\) be the degree-\(<N\) polynomial interpolating
\(t_M(\lambda_\chi)=t_\chi(M)\). Its coefficients are meromorphic;
colliding values are not evaluated before cancellation. Then
\[
\boxed{\displaystyle
\Phi_0(W(M))
 =(-1)^{N+1}N D_N(M)
       \sum_\chi\frac{t_\chi(M)}{p_M'(\lambda_\chi)}
 =(-1)^{N+1}N D_N(M)[\lambda^{N-1}]t_M(\lambda).
}
\tag{11}
\]
The first equality is H's weightwise source formula and (10).
The second follows by taking the leading coefficient in
\[
t_M(\lambda)=\sum_\chi
t_\chi(M)\frac{p_M(\lambda)}
 {(\lambda-\lambda_\chi)p_M'(\lambda_\chi)}.
\]
Equivalently the sum is the sum of finite residues of
\(t_M(\lambda)d\lambda/p_M(\lambda)\). This fixes the inverse
Jacobian and its sign for the actual source; it is not a choice
of a scalar on a torsor. Retain the whole meromorphic expression
and the removable continuation of (5).

### Polynomial central coupon and a uniform pole-order bound

The full matrix, not only its spectrum, satisfies
\[
p_M(\Omega_\Sigma)=0.
\tag{11a}
\]
Here is a direct proof through the possible root Jordan blocks.
In (6) the off-diagonal letter \(F_1E_{\rm r}\) raises first
occupation by one and changes a remaining weight \(\chi\)
to \(Q\chi\), since \(K_{\rm r}E_{\rm r}=QE_{\rm r}K_{\rm r}\).
An entry rising by \(k<N\) therefore visits only the scalar
diagonal values
\(\lambda_\chi,\lambda_{Q\chi},\ldots,\lambda_{Q^k\chi}\).
For a polynomial \(f\), its entry on this path is
\(F_1^kE_{\rm r}^k\) times the divided difference of \(f\)
at those nodes, restricted to the starting weight space.
For \(f(t)=t^j\), expansion of all diagonal steps proves this:
their sum is the complete homogeneous polynomial of degree
\(j-k\) in the visited nodes, which is exactly that divided
difference. Linearity proves the assertion for every \(f\).
Multiplicity of a weight does not alter its scalar diagonal;
paths beyond the first-head endpoint vanish.

For generic \(M\), these \(k+1\le N\) nodes are distinct.
The polynomial \(p_M\) vanishes at every one, so its divided
difference is zero. All entries therefore vanish. Both sides
of (11a) are analytic matrix functions of \(M\); continuation
proves (11a) also at collisions, without deleting any Jordan
direction.

Substituting \(t=z+z^{-1}\) proves the polynomial identity
\((t^2-4)U_{N-1}(t)^2=T_N(t)^2-4\). With (9),(11a) it gives
\[
\boxed{\displaystyle
Z_N(M)=
\frac{(\Omega_\Sigma^2-4I)U_{N-1}(-\Omega_\Sigma)}
     {(M^{mN}-M^{-mN})^2}.
}
\tag{11b}
\]
The equality holds generically and hence meromorphically.
Thus the coupon is a polynomial in the actual Casimir with
a scalar meridian denominator; its pole order at \(M=1\)
is at most two for every \(N,m\).

For later finite parts put
\[
B_\beta(u)=
(\Omega_\Sigma(e^u)^2-4I)
 U_{N-1}(-\Omega_\Sigma(e^u))W_\beta(e^u).
\tag{11c}
\]
It is analytic. Original-source analyticity in (5) forces
\(\operatorname{Tr}B_\beta(u)=O(u^2)\). Consequently
\[
\Phi_0(W_\beta(1))
 =\frac{\operatorname{Tr}B_\beta''(0)}{8m^2N^2}.
\tag{11d}
\]
This is an exact alternative source formula, not a norm bound.
At the matrix level the finite part remains
\[
\operatorname{FP}_{u=0}
 \frac{D_N(e^u)B_\beta(u)}
 {N(e^{mNu}-e^{-mNu})^2}
 =
\frac{B_\beta''(0)}{8m^2N^2}
 +\frac{N^2-1-2m^2N^2}{24m^2N^2}B_\beta(0).
\tag{11e}
\]
Indeed expand \(\sinh(Nu)/(N\sinh u)\) and
\(4\sinh^2(mNu)\) to their quadratic terms.
The second summand has zero full trace but is not discarded
as an operator or a compact relative current.

## 3. The original compact full-trace period

Use C's head metric \(\langle e_a,e_a\rangle=\binom da^{-1}\), and
\[
X=(\mathbb P^1\times\mathbb P^1)\setminus\{1+wz=0\},\qquad
\Gamma=\{w=v,\ z=\bar v\}\simeq S^2 .
\]
For an operator \(A\) on \(m\) heads put
\[
K_A(\mathbf w,\mathbf z)=
 \sum_{\mathbf a,\mathbf b}
 \mathbf w^{\mathbf a}A_{\mathbf a\mathbf b}
 \prod_{i=1}^m\binom d{b_i}z_i^{b_i},\qquad
\omega_A=K_A\bigwedge_{i=1}^m
 \left(-\frac{dw_i\wedge dz_i}
 {2\pi i(1+w_i z_i)^{N+1}}\right).
\tag{12}
\]
All indices lie in \(0,\ldots,d\). C's exact beta pairing gives
\[
\int_{\Gamma^m}\omega_A=N^{-m}\operatorname{Tr}_{\rm full}A.
\tag{13}
\]
Define the actual source matrix and form by
\[
A_\beta(M)=\frac{D_N(M)}{N}Z_N(M)W_\beta(M),\qquad
\mathcal O_\beta(M)=N^m\omega_{A_\beta(M)}.
\tag{14}
\]
Then
\[
\Phi_0(W_\beta(M))=\int_{\Gamma^m}\mathcal O_\beta(M).
\tag{15}
\]
Composition uses C's exact kernel formula with one factor \(N\)
per integrated head. Thus (15) also has an expanded finite-word
period with the explicit resolvent coupon, every original crossing,
and every prescribed scalar. No full exponential or infinite
occupation sum replaces the finite coherent identity kernel.
There is no cut reset or additional \(N\) normalization.

Write \(u=\Log M\), with \(u=0\) at completeness. The matrix and
form (14) have finite meromorphic pole order at fixed \(N,m\).
Their coefficients are smooth on the compact cycle, which avoids
the incidence divisor. Laurent expansion and integration commute:
\[
\Phi_0(W_\beta(1))
 =\int_{\Gamma^m}\operatorname{FP}_{u=0}\mathcal O_\beta(e^u).
\tag{16}
\]
Negative coefficients have zero total integral but are retained as
forms. Higher meridian jets are obtained from the whole product
in (14) in the same way. Substituting \(D_N(1)=N\) before taking
that product's finite part can lose polar cross terms.

## 4. Literal compact Weyl turnover and its normal current

At completeness P's balanced turnover is
\[
C_0e_a=(-1)^a e_{d-a},\qquad C_0^2=(-1)^dI.
\tag{17}
\]
It is unitary for the binomial metric. Direct substitution gives
\[
K_{C_0AC_0^{-1}}(w,z)=(wz)^dK_A(-1/w,-1/z).
\tag{18}
\]
Thus conjugation pulls back \(\omega_A\) by
\(\iota(w,z)=(-1/w,-1/z)\). Its powers cancel the transformed
denominator and Jacobian exactly, including at zero and infinity.

Let \(\mathsf J\) reverse tensor factors and
\(\mathscr C_0=C_0^{\otimes m}\mathsf J\). It corresponds to
\[
\mathcal I(\mathbf w,\mathbf z)_i
       =(-1/w_{m+1-i},-1/z_{m+1-i}).
\tag{19}
\]
This preserves \(\Gamma^m\) with orientation \(+1\): each sphere
map is holomorphic of degree one, and interchanging real
two-dimensional factors adds no sign. The paired forms have
the same sign.

For the meridian germ retain the entire matrix
\[
C(M)e_a=c_a(M)e_{d-a},\qquad
c_a(M)=\prod_{j=1}^a\frac{MQ^j-M^{-1}}{1-Q^j}.
\tag{20}
\]
Set
\[
D(M)=\mathscr C_0^{-1}
                (C(M)^{\otimes m}\mathsf J).
\tag{21}
\]
This is the tensor product of diagonal \(C_0^{-1}C(M)\), whose
entries are \((-1)^a c_a(M)\). It is invertible near one and
\(D(1)=I\); it is not replaced by \(I\) in a normal derivative.

Let \(\beta^{\rm rev}\) replace \(\sigma_i^{\pm1}\) by
\(\sigma_{m-i}^{\pm1}\) without reversing word order. P's exact
conjugations of the word and Casimir, and \(D_N(M^{-1})=D_N(M)\),
give
\[
A_\beta(M)=\mathscr C_0D(M)A_{\beta^{\rm rev}}(M^{-1})
                         D(M)^{-1}\mathscr C_0^{-1}.
\tag{22}
\]
The original zero-framing line is reciprocal and included.
An additional nonreciprocal external scalar must keep its
explicit ratio in this formula. The difference from the fixed
compact pullback is the specified trace-zero matrix
\[
X_1(M)=[D(M),A_{\beta^{\rm rev}}(M^{-1})D(M)^{-1}].
\tag{23}
\]
It need not vanish in the finite part: \(D(M)-I\) can multiply
poles of the central coupon.

## 5. The rational current and half-twist return

We require a tensor version of C's explicit primitive. For every
matrix \(A\) there is a finite linear rational construction with
\[
\omega_A-\frac{\operatorname{Tr}A}{N^m}\omega_I=d\eta_A,
\tag{24}
\]
where \(\omega_I\) is the product normalized volume form.
To prove it, let \(\mathcal E_i\) replace head \(i\) by its
normalized partial trace times \(I_i\). The commuting maps give
\[
A-\mathcal E_1\cdots\mathcal E_m A
 =\sum_{i=1}^m\mathcal E_1\cdots\mathcal E_{i-1}
                                (A-\mathcal E_i A).
\tag{25}
\]
Each summand has zero \(i\)-th partial trace. Treat its other
heads as matrix coefficients. C's construction expresses it as
\([J_{0,i},B_i]+[J_{-,i},C_i]\): divide off-diagonal entries
by row-minus-column, and put the trace-zero diagonal prefix sum
divided by \(j+1\) in the raising entry. All denominators are
nonzero integers. The vector fields
\[
V_{0,i}=w_i\partial_{w_i}-z_i\partial_{z_i},\qquad
V_{-,i}=\partial_{w_i}+z_i^2\partial_{z_i}
\]
preserve \(\omega_I\) and give those commutators on symbols.
Cartan's formula proves (24), with the sum of
\(\sigma_{B_i}\iota_{V_{0,i}}\omega_I+
 \sigma_{C_i}\iota_{V_{-,i}}\omega_I\) as \(\eta_A\).
It is global and linear in matrix entries, hence preserves
every Laurent coefficient.

Apply this construction to (23). Exactly,
\[
\mathcal O_\beta(M)-
 \mathcal I^*\mathcal O_{\beta^{\rm rev}}(M^{-1})
 =N^m d\mathcal I^*\eta_{X_1(M)}.
\tag{26}
\]
For the remaining reversal let \(V(M)=W_{\Delta_m}(M)\) be
the actual half-twist operator. P proves
\(\beta^{\rm rev}=\Delta_m\beta\Delta_m^{-1}\).
Centrality of \(Z_N\) gives
\[
A_{\beta^{\rm rev}}(M)=V(M)A_\beta(M)V(M)^{-1}.
\tag{27}
\]
No cut coupon is moved and replaced here. Put
\[
X_2(M)=[V(M^{-1}),A_\beta(M^{-1})V(M^{-1})^{-1}].
\tag{28}
\]
Then (24)--(28) give the same-word identity
\[
\boxed{\displaystyle
\mathcal O_\beta(e^u)-\mathcal I^*\mathcal O_\beta(e^{-u})
 =d\mathcal T_\beta(u),\qquad
\mathcal T_\beta=N^m\mathcal I^*
       (\eta_{X_1(e^u)}+\eta_{X_2(e^u)}).
}
\tag{29}
\]
All entries of this current are specified finite original
operators. Compact Stokes proves its zero period, without
discarding its pairing on relative boundaries.

In particular
\[
\mathcal O_\beta^{\rm sym}(u)=
 \tfrac12(\mathcal O_\beta(e^u)+
                  \mathcal I^*\mathcal O_\beta(e^{-u}))
\tag{30}
\]
obeys
\(\mathcal O_\beta(e^u)-\mathcal O_\beta^{\rm sym}(u)
 =\tfrac12d\mathcal T_\beta(u)\).
It has the same original period and obeys
\(\mathcal O_\beta^{\rm sym}(u)=
\mathcal I^*\mathcal O_\beta^{\rm sym}(-u)\) exactly.
Finite parts and all coefficient identities hold before
integration. Its constant Laurent coefficient is invariant;
its coefficient of \(u\) is anti-invariant. The latter concerns
the derivative of the **whole pointed source**, not the
separate \(B_0'\) in H's closing row. All polar and current
coefficients remain specified.

## 6. Geometric scope and the scalar loxodromic character

On C's controlled physical head-symbol domain, (19) has
\[
(A,p)\longmapsto(A^{-1},-p^{-1}),\qquad
(K,E,F)\longmapsto(K^{-1},F,E)\quad(M=1).
\tag{31}
\]
Indeed \(T=wz/(1+wz)\) changes to \(1-T\), while
\(A=e^{2\pi iT}\) and \(p=1/w\). This is not a uniform
symbol theorem for an arbitrary growing full-word kernel.

The total-product slice in G requires a further distinction.
For ordered totals put
\[
b_+=\begin{pmatrix}K&E\\0&1\end{pmatrix},\quad
b_-=\begin{pmatrix}1&0\\-KF&K\end{pmatrix},\quad
P=b_-^{-1}b_+,\quad J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Total Chevalley/reversal gives directly
\[
b_+'=Jb_-^{-1}J,\qquad b_-'=Jb_+^{-1}J,\qquad
P'=Jb_-Pb_-^{-1}J.
\tag{32}
\]
Thus \(F_\Sigma=0\) is sent to \(E_\Sigma=0\); the actual
\(B_0\) quotient of G uses the former. Conjugation in (32)
transports a labeled holonomy eigenline with its eigenvalue.
It does not reselect the reciprocal eigenline on the original
\(F_\Sigma=0\) slice.

Equations (29)--(30) therefore pay a compact source symmetry
with its boundary current, but do not identify the two
geometric eigenline sectors of a reduced local decomposition.
That needs the opposite-polarization source map and its
relative chains. Where (29) can be integrated over a chain
\(\mathcal C\), its difference remains exactly
\(\int_{\partial\mathcal C}\mathcal T_\beta\).
Compact Stokes does not set these local endpoints to zero.

The central coupon is also not a unit amplitude at a
loxodromic scalar argument. On a compact set
\(|z|\ge1+\delta>1\),
\[
U_{N-1}(z+z^{-1})^{-1}
 =(z-z^{-1})z^{-N}(1-z^{-2N})^{-1}.
\tag{33}
\]
The last factor is \(1+O((1+\delta)^{-2N})\).
Its fixed \(j\)-th derivative has error
\(O_j(N^j(1+\delta)^{-2N})\), on a fixed smaller
holomorphic neighborhood. This follows by differentiating
its convergent geometric series. On a chosen branch its
scalar logarithm is
\[
-N\Log z+\Log(z-z^{-1})-\Log(1-z^{-2N}).
\tag{34}
\]
For \(|z|<1\), use the reciprocal; (3) is invariant under
that replacement. The order-\(N\) character is retained.
These scalar identities are not an operator asymptotic,
a coherent-kernel phase, or an original-cycle contribution.

No positivity, geometric thimble coefficient, cancellation
of two geometric residues, or addition of their first-jet
terms is inferred. The new exact source object is
(5),(11),(15), with the concrete involution and full
relative current (29).

## Complete proof directs

* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* P: notes/research_reduced_casimir_pair_localizer.md,
  SHA256 e5307ed7e424ba181db9b73f8473342a094ed85caf0b521b4aa965bb78e3c4ea.
* C: notes/compact_coherent_source_period.md,
  SHA256 8c6c3277367a4aa6c69269da635139d5f881f3d3d0d894e04dd97028d76537e4.
* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

All four complete sources were read nontruncated in this active
sequence. The assertions concern the actual fixed-root meridian
germ. No mathematical programs, numerical cases, or imported
modified-trace proof are used.

