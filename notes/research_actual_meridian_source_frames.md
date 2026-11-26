# Exact meridian frames for the actual opposite source

Private written proof, 18 November 2026.

The actual lowering coproduct is diagonally conjugate to its complete
root value. A different, purely Cartan frame conjugates the raising
coproduct and the entire prefix quotient. Their combination cancels
the factorial meridian dependence of the middle turnover and, apart
from its retained scalar, puts the remaining non-Cartan dependence of
the opposite kernel in one explicit diagonal insertion. The true first meridian jet follows by the product
rule. Both frames have polynomial conditioning on a fixed scaled
meridian disk.

The complete direct J supplies the literal finite matrices, quotient,
turnover, and source normalization; B supplies the ordered balanced
crossings. Every new conjugation, normal formula, and bound is proved below. These are changes of
presentation of the same finite source, not a simultaneous
trivialization of its quantum-group representation or a relative
estimate for a closed scalar.

## 1. The literal one-head lowering frame

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(m\ge2\) heads. The quantum parameter stays fixed. Write
\[
 f_a=(Q;Q)_a,\qquad x=-M/q,\qquad J_iw_a=a w_a.
 \tag{1}
\]
The actual balanced arrows on each head are
\[
 E(M)w_a=(MQ^{-a}-M^{-1})w_{a-1}\ (a>0),\quad E(M)w_0=0,
 \qquad Fw_a=(1-Q^{a+1})w_{a+1},\quad Kw_a=xQ^{-a}w_a.
 \tag{2}
\]
The upper \(F\) arrow is zero. Define the meromorphic diagonal
\[
 h_a(M)=M^{-a}\frac{f_a}{(M^{-2}Q;Q)_a},\qquad h_0=1,
 \qquad D_h(M)w_a=h_a(M)w_a.
 \tag{3}
\]
It is an invertible holomorphic matrix near \(M=1\), and
\(D_h(1)=I\). For \(a>0\),
\[
 \frac{h_{a-1}}{h_a}
   =M\frac{1-M^{-2}Q^a}{1-Q^a}.
 \]
Multiplication by \(Q^{-a}-1\) therefore proves exactly
\[
 E(M)=D_h(M)E(1)D_h(M)^{-1},\qquad K(M)=M K(1).
 \tag{4}
\]
The forced bottom arrow is zero on both sides, including when
\(M\ne1\). No cyclic bottom arrow has been added.

J's balanced turnover is
\[
 C(M)w_b=c_b(M)w_{d-b},\qquad
 c_b(M)=\prod_{j=1}^b\frac{MQ^j-M^{-1}}{1-Q^j},
 \qquad C_0w_b=(-1)^b w_{d-b}.
 \tag{5}
\]
Put \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\) with its Laurent
polynomial continuation, and \(s_N(M)=D_N(M)/N\).
Then
\[
 \boxed{\quad C(M)=s_N(M)D_h(M)C_0.\quad}
 \tag{6}
\]
Indeed \(c_b/[(-1)^b h_{d-b}]\) has consecutive ratio one:
use \(Q^{d-b}=Q^{-b-1}\) in the ratio of (3).
At \(b=0\) its value is
\[
 h_d^{-1}=M^d\frac{(M^{-2}Q;Q)_d}{N}
  =\frac{M^d}{N}\frac{1-M^{-2N}}{1-M^{-2}}
  =s_N(M).
 \]
All removable values are interpreted by continuation.
This is a whole-meridian identity at the fixed quantum root;
no root reflection has been differentiated in \(q\).

## 2. Two exact tensor frames

Let \(E_0=E_\Sigma(1)\), \(F_0=F_\Sigma(1)\), and define
\[
 A_E(M)=\bigotimes_{i=1}^m
             \bigl[D_h(M)M^{-(m-i)J_i}\bigr],\quad
 B_F(M)=M^{-\sum_{i=1}^m(i-1)J_i},\quad
 B_E(M)=M^{\sum_{i=1}^m(m-i)J_i}.
 \tag{7}
\]
All these matrices are diagonal. The ordered coproducts are
\[
 E_\Sigma(M)=\sum_{i=1}^m E_i(M)\prod_{j>i}K_j(M),\qquad
 F_\Sigma(M)=\sum_{i=1}^m\left(\prod_{j<i}K_j(M)^{-1}\right)F_i.
 \tag{8}
\]
A lowering arrow conjugated by \(M^{-aJ}\) gains \(M^a\);
a raising arrow gains \(M^{-a}\). Equations (4),(8) consequently give
\[
 \boxed{\quad
 E_\Sigma(M)=A_E(M)E_0A_E(M)^{-1},\qquad
 F_\Sigma(M)=B_F(M)F_0B_F(M)^{-1}.
 \quad}\tag{9}
\]
The first formula supplies exactly the \(M^{m-i}\) of the
right Cartan tail; the second supplies the \(M^{-(i-1)}\)
of the left inverse Cartan prefix.

In particular, for every polynomial \(p\) with meridian-independent
coefficients,
\[
 p(E_\Sigma(M))=A_E(M)p(E_0)A_E(M)^{-1}.
 \tag{10}
\]
This includes the actual finite Euler polynomial
\(\sum_{n<N}\lambda^nE_\Sigma(M)^n/f_n\) at fixed \(\lambda\).
It does not replace a polynomial with shifted denominators
\((M^{-2}Q;Q)_n\). Any meridian dependence in \(\lambda\) or
the coefficients retains its own derivative.

Let \(L_1w_a=w_{a-1}\), with bottom zero, and let \(F_{\rm r}(M)\)
be the ordered raising coproduct on heads \(2,\ldots,m\).
J's prefix and quotient are
\[
 S(M)=\sum_{n=0}^d\frac{(x^{-1}L_1F_{\rm r}(M))^n}{f_n},
 \qquad q_F(M)=p_0S(M)^{-1},\qquad i_F(M)=i_0.
 \tag{11}
\]
Write \(S_0=S(1)\), \(q_0=p_0S_0^{-1}\), and
\[
 B_{\rm t}(M)=M^{-\sum_{i=2}^m(i-1)J_i}
 \]
on the remaining-head space \(U\).
The first exponent in \(B_F\) is zero, so \(L_1\) is unchanged.
The term on head \(i\ge2\) in \(x^{-1}F_{\rm r}(M)\) has
meridian power \(M^{-(i-1)}\). Hence, exactly,
\[
 S(M)=B_F(M)S_0B_F(M)^{-1},\qquad
 \boxed{\ q_F(M)=B_{\rm t}(M)q_0B_F(M)^{-1}.\ }
 \tag{12}
\]
Here \(p_0B_F=B_{\rm t}p_0\) and
\(B_Fi_0=i_0B_{\rm t}\). The entire finite prefix sum and
its inverse are retained, including every endpoint.

The two frames are different. In particular \(K_\Sigma(M)\)
still has its scalar factor \(M^m\); (9) does not assert a
single simultaneous conjugation of \(E,F,K\) to their root values.

## 3. One diagonal insertion in the actual opposite kernel

Let \(\mathsf J\) reverse the tensor factors, and put
\(\mathscr C_0=C_0^{\otimes m}\mathsf J\).
The actual turnover is \(\mathscr C(M)=C(M)^{\otimes m}\mathsf J\).
From (6),(7),
\[
 A_E(M)^{-1}\mathscr C(M)
                  =s_N(M)^m B_E(M)\mathscr C_0.
 \tag{13}
\]
Define the relative diagonal
\[
 D_{\rm rel}(M)=B_F(M)^{-1}A_E(M)
       =\bigotimes_{i=1}^m
                    \bigl[D_h(M)M^{(2i-m-1)J_i}\bigr].
 \tag{14}
\]
J's actual analytic opposite map, with its original normalization, is
\[
 T(M)=q_F(M)E_\Sigma(M)^d\mathscr C(M)i_0.
 \]
Equations (9),(12),(13) give the exact presentation
\[
 \boxed{\quad
 T(M)=s_N(M)^m B_{\rm t}(M)q_0D_{\rm rel}(M)
                       E_0^dB_E(M)\mathscr C_0i_0.
 \quad}\tag{15}
\]
Apart from the displayed scalar \(s_N(M)^m\), only the diagonal
insertion has non-Cartan meridian dependence. No new prefix or
Euler kernel has been substituted.

There is a useful equivalent symmetric Cartan placement. Set
\(\xi=d\,m(m-1)/2\). Complementing and reversing each occupation
in \(\mathscr C_0\) gives
\[
 B_E(M)\mathscr C_0=M^\xi\mathscr C_0B_F(M).
 \]
Thus
\[
 \boxed{\quad
 T(M)=s_N(M)^m M^\xi B_{\rm t}(M)
           [q_0D_{\rm rel}(M)E_0^d\mathscr C_0i_0]
                                    B_{\rm t}(M).
 \quad}\tag{16}
\]
The two tail factors in (16) have the same sign. The scalar
\(M^\xi\) and the tensor reversal are part of the identity.

## 4. The true first normal and the source finite part

All derivatives in this section are with respect to
\(\mu=\log M\) at \(\mu=0\), with \(q\) fixed.
Let
\[
 \Sigma_{a,N}=\sum_{j=1}^a\frac{Q^j}{1-Q^j},\quad \Sigma_{0,N}=0.
 \]
Direct differentiation of (3) gives
\[
 (\log h_a)'=-a-2\Sigma_{a,N}.
 \tag{17}
\]
Consequently the lowering-frame generator and relative generator are
\[
 \mathcal H=A_E'(1)=
       \sum_i[-(m-i+1)J_i-2\Sigma_{J_i,N}],\qquad
 \mathcal L=D_{\rm rel}'(1)=
       \sum_i[(2i-m-2)J_i-2\Sigma_{J_i,N}].
 \tag{18}
\]
The notation \(A_E'(1)\) means the stated \(\mu\)-derivative.
Since \(A_E(1)=I\), (10) gives the exact commutator
\[
 \left.\partial_\mu p(E_\Sigma(e^\mu))\right|_0
                                    =[\mathcal H,p(E_0)].
 \tag{19}
\]
This formula retains the actual bottom-zero normal. It is not
obtained by differentiating a meridian-independent root symbol.

Put \(\mathcal B=-\sum_{i=2}^m(i-1)J_i\) on \(U\).
The Laurent polynomial \(D_N(e^\mu)\) is even in \(\mu\), so
\(s_N(1)=1\) and \(s_N'(1)=0\). With
\[
 T_0=q_0E_0^d\mathscr C_0i_0,\qquad
 \mathcal V=q_0\mathcal L E_0^d\mathscr C_0i_0,
 \]
differentiation of (16) therefore yields the true ordered row
\[
 \boxed{\quad
 T_1:=\left.\partial_\mu T(e^\mu)\right|_0
     =\xi T_0+\mathcal B T_0+T_0\mathcal B+\mathcal V.
 \quad}\tag{20}
\]
No derivative of \(q_F\) or turnover has been discarded:
(12)--(16) have evaluated them before this product rule.

To retain the original normalized source, let \(r=m-1\),
\(K_{\rm r}(M)=M^rK_0\), and
\(\varepsilon=K_0^N=(-1)^{(N+1)r}\).
J's normalization is
\[
 J_{\rm op}(M)=H(M)^{-1}T(M),\qquad H(M)=D_N(M^mK_0).
 \tag{21}
\]
Its exact diagonal inverse has expansion
\[
 H(e^\mu)^{-1}=\frac{U_{-1}}{\mu}+U_0+O(\mu),\qquad
 U_{-1}=\frac{K_0-K_0^{-1}}{2\varepsilon mN},\quad
 U_0=\frac{K_0+K_0^{-1}}{2\varepsilon N}.
 \tag{22}
\]
This follows by expanding
\((M^mK_0-M^{-m}K_0^{-1})/
[\varepsilon(M^{mN}-M^{-mN})]\); it includes the removable
self weights. Therefore the actual residue and finite part are
\[
 \operatorname{Res}_{\mu=0}J_{\rm op}=U_{-1}T_0,\qquad
 \operatorname{FP}_{\mu=0}J_{\rm op}=U_0T_0+U_{-1}T_1,
 \tag{23}
\]
with \(T_1\) given by (20). The diagonal factors are on the left,
as in the actual source. Individual windows and insertions still
retain the normal rows in J; (23) does not remove their defects.

## 5. Polynomial conditioning on the whole scaled collar

Use the original binomial head metric
\(\|w_a\|^2=\binom da^{-1}\) and its tensor products.
Fix \(0<\eta<\pi\) and put \(M=e^{u/N}\), \(|u|\le\eta\).
There are no zeros of any factor in (3) on this disk. More
quantitatively, for \(1\le j<N\),
\[
 1-e^{-2u/N}Q^j
   =-2i e^{\pi i j/N-u/N}
                       \sin((\pi j+i u)/N).
 \]
The real part of the sine argument lies strictly between zero
and \(\pi\). Since
\(|\sin z|\ge|\sin\operatorname{Re}z|\), the elementary sine
bound on this interval gives
\[
 |1-e^{-2u/N}Q^j|
 \ge \frac{4(\pi-\eta)}{\pi}e^{-\eta/2}
                              \frac{\min(j,N-j)}N.
 \tag{24}
\]
Here \(\pi\min(j,N-j)-\eta\ge(\pi-\eta)\min(j,N-j)\),
and \(N\ge2\) was used in the exponential factor.

The analytic logarithm of each \(h_a(e^{u/N})\) is normalized
to zero at \(u=0\). Differentiating it gives
\[
 \partial_u\log h_a(e^{u/N})
 =-\frac aN-\frac2N\sum_{j=1}^a
               \frac{e^{-2u/N}Q^j}{1-e^{-2u/N}Q^j}.
 \]
By (24) its absolute value is at most
\(C_\eta\log(N+1)\), uniformly in every \(0\le a<N\).
Integrating along the straight segment from zero proves
\[
 (N+1)^{-C_\eta}\le |h_a(e^{u/N})|
                         \le(N+1)^{C_\eta}.
 \tag{25}
\]
The same bound holds for the inverse. All Cartan factors in
(7),(14),(16) have uniformly bounded modulus and inverse on
this collar, for fixed \(m\). Also
\[
 s_N(e^{u/N})=\frac{\sinh u}{N\sinh(u/N)}
 \tag{26}
\]
is a uniformly bounded holomorphic unit with bounded inverse
on \(|u|\le\eta\); the values at zero are removable, and the
nearest nonzero zeros of \(\sinh u\) are at \(\pm\pi i\).
For example write (26) as the quotient of
\(\sinh u/u\) and \(\sinh(u/N)/(u/N)\) on their indicated compact
zero-free disks.

Diagonal operator norms in the binomial metric are the maxima
of their entries. Equations (25)--(26) thus give polynomial
bounds, uniform over all head occupations, for \(A_E^{\pm1}\),
\(D_{\rm rel}^{\pm1}\), and the bounded Cartan frames.
Choose \(\eta<\eta'<\pi\) and apply Cauchy's estimates on the
larger disk: every fixed \(u\)-derivative has polynomial cost
as well. A fixed \(\mu\)-derivative costs a further \(N\) per
derivative, since \(\partial_\mu=N\partial_u\).
At the root, (17)--(18),(24) give directly
\[
 \|\mathcal H\|+\|\mathcal L\|
                         \le C_m N\log(N+1).
 \tag{27}
\]
These are bounds for the specified frames and insertions.
They are not relative bounds on \(T(M)/T_0\), on individual
matrix entries, or on a closing scalar that may cancel.

## 6. Original marks, cut, and pivot

The F frame has an exact adapter for an arbitrary actual matrix
\(A(M)\), without an intertwining assumption:
\[
 q_F(M)A(M)i_0
  =B_{\rm t}(M)
     [q_0\widetilde A(M)i_0]B_{\rm t}(M)^{-1},
 \qquad \widetilde A(M)=B_F(M)^{-1}A(M)B_F(M).
 \tag{28}
\]
Every crossing or mark in a product is transported in that
order; adjacent frame factors cancel exactly. At the first
normal,
\[
 \widetilde A_1=A_1+[A_0,\mathcal B_F],\qquad
 \mathcal B_F=-\sum_i(i-1)J_i.
 \tag{29}
\]
Thus transported marks do not have unchanged normal matrices.

The original pointed pivot is
\(P_0\otimes K_{\rm r}(M)^{1-N}\). It commutes with \(B_F\).
Writing \(g_0=K_0^{1-N}\), cyclicity gives the exact source
identity for every \(A\),
\[
 \operatorname{Tr}[(P_0\otimes K_{\rm r}(M)^{1-N})A(M)]
   =M^{-rd}\operatorname{Tr}[(P_0\otimes g_0)\widetilde A(M)].
 \tag{30}
\]
All original external scalars and framing factors remain in
\(A\); the explicit pivot power in (30) is not suppressed.
The source-normalized trace formula of J can additionally be
used for its actual total intertwiners. It is not imposed on
arbitrary marks merely because (28) exists.

In coherent resolutions these diagonal transformations act
on both sides of the finite kernels and on the retained
source coupons. A partial resolution or relative window is
transported as a matrix too. No claim that its original
real chain is fixed, or that its boundary current vanishes,
follows from (9),(12), or the polynomial conditioning.
The exact finite frame and isolated insertion (14),(20),(23)
therefore preserve the original source. The following local
crossing calculation makes the same normal adapter explicit
for every fixed original braid word.

## 7. Literal crossing and whole-braid first jets

Use two adjacent heads \(i,i+1\) at the same meridian, and set
\(\mathcal J_i=J_i+J_{i+1}\). Retain the original common Cartan
scalar \(\kappa(M)\). B gives the actual positive checked crossing
and its finite nilpotent factor in the order
\[
 R_i^+(M)=\kappa(M)P_iD_i(M)\Theta_i(M),\qquad
 \Theta_i(M)=\sum_{n=0}^d
       \frac{(-1)^nq^{n^2}E_i(M)^nF_{i+1}^n}{f_n},
 \tag{31}
\]
where
\[
 D_i(M)w_{a,b}=x^{-a-b}Q^{ab}w_{a,b}
                    =M^{-a-b}D_i(1)w_{a,b}.
 \]
These are the original finite heads, with no semicyclic wrap.
The actual negative crossing is its inverse:
the order is \(\kappa^{-1}\Theta_i^{-1}D_i^{-1}P_i\),
and B gives \(\Theta_i^{-1}=\sum_{n<N}q^nE_i^nF_{i+1}^n/f_n\).

Since \(F_{i+1}\) is meridian independent, (4) gives
\(\Theta_i(M)=D_{h,i}(M)\Theta_i(1)D_{h,i}(M)^{-1}\).
The diagonal factors commute, while
\(P_iD_{h,i}=D_{h,i+1}P_i\). Therefore, including the scalar,
\[
 \boxed{\begin{split}
 R_i^+(M)
  &=\frac{\kappa(M)}{\kappa(1)}M^{-\mathcal J_i}
                  D_{h,i+1}(M)R_i^+(1)D_{h,i}(M)^{-1},\\
 R_i^-(M)
  &=\frac{\kappa(1)}{\kappa(M)}M^{\mathcal J_i}
                  D_{h,i}(M)R_i^-(1)D_{h,i+1}(M)^{-1}.
 \end{split}}\tag{32}
\]
The second formula follows by taking the actual inverse of the
first. In moving \(M^{\mathcal J_i}\) to the left one uses exact
conservation of the sum of the two occupations. In particular
the checked flip has changed the location of the left \(D_h\);
it cannot be omitted from this calculation.

Put
\[
 \ell_i=-J_i-2\Sigma_{J_i,N},\qquad
 \gamma_\kappa=\left.\partial_\mu\log\kappa(e^\mu)\right|_0,
 \qquad R_{i,0}^\pm=R_i^\pm(1).
 \]
Differentiating (32) in the actual fixed-\(q\) family yields
\[
 \boxed{\begin{split}
 R_{i,1}^+
  &=(\gamma_\kappa I-\mathcal J_i+\ell_{i+1})R_{i,0}^+
                                          -R_{i,0}^+\ell_i,\\
 R_{i,1}^-
  &=(-\gamma_\kappa I+\mathcal J_i+\ell_i)R_{i,0}^-
                                          -R_{i,0}^-\ell_{i+1}.
 \end{split}}\tag{33}
\]
All new matrix insertions here are diagonal and have norm
\(O(N\log(N+1))\) in the original binomial metric.
The original scalar derivative \(\gamma_\kappa\) is displayed,
not absorbed into that bound.

More explicitly, let an actual fixed marked word be
\[
 W(M)=\zeta(M)A_L(M)\cdots A_1(M),
 \]
where the \(A_j\) are literal signed crossings or prescribed
marks, and \(\zeta\) retains any original external and
zero-framing line. Its true first normal is exactly
\[
 W_1=\zeta_1 A_{L,0}\cdots A_{1,0}
    +\zeta_0\sum_{j=1}^L
       A_{L,0}\cdots A_{j+1,0}A_{j,1}A_{j-1,0}\cdots A_{1,0}.
 \tag{34}
\]
For crossing factors substitute (33); for a mark retain its
prescribed derivative. Thus a fixed unmarked braid has a finite
root-word expression for its first normal with the explicit
diagonal insertions (33) and the original scalar derivatives.
No cancellation of adjacent \(D_h\)'s is assumed. Bounds for
additional marks are not supplied by their mere insertion.
Higher fixed meridian derivatives can likewise use the exact
factorization (32) and the polynomial collar bounds, with
all scalar derivatives retained.

In the original highest-cut pivotal functional this gives
\[
 \left.\partial_\mu\operatorname{Tr}
   [(P_0\otimes K_{\rm r}(e^\mu)^{1-N})W(e^\mu)]\right|_0
   =\operatorname{Tr}[(P_0\otimes g_0)(W_1-rd\,W_0)].
 \tag{35}
\]
The pivot derivative, \(\kappa\), zero-framing line, and every
marked normal are therefore explicit. Equations (32)--(35)
concern fixed-root meridian derivatives, not quantum-parameter
derivatives or an ordinary-color path without its full adapter.
They do not bound a relative closing scalar or establish
noncancellation after contraction. Analytic composition and
geometric source contributions remain separate.

## Complete proof direct

* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* B: notes/balanced_verma_coherent_braiding.md,
  SHA256 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.

Both complete directs were freshly read nontruncated in this active
author sequence. Only written mathematics and text/hash operations
were used. Frozen and public files were not edited.
