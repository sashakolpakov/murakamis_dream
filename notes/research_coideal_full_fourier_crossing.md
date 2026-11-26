# A full Fourier compiler for the actual coideal crossing

24 November 2026. Written research proof.

The actual coideal graph crossing has an explicit triangular matrix
between two unitary Fourier bases. Its entries are finite Gaussian
binomials and finite products. A full initialized Toeplitz adapter
then gives every pair of neighboring heights and the complete
arbitrary-width operator, with all deeper channels still coherent.
Both crossing signs and the original cup source are retained.

This is a finite source compiler. It neither replaces a coherent
input by independent column norms nor estimates the original
marked scalar below.

## 1. Original matrices and conventions

Use the complete conventions of T and B in the source table:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad c=1+q,\quad \kappa=e^{i\pi d^2/(2N)}.
\]
Every fractional phase means this specified exponential. Put
\[
 (z;Q)_a=\prod_{h=0}^{a-1}(1-zQ^h),\quad
 F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N.
\]
The physical coefficient basis \(e_0,\ldots,e_d\) is orthonormal.
The actual generators and continuants are
\[
 Ke_a=xQ^{-a}e_a,\quad Ee_a=(Q^{-a}-1)e_{a-1},\quad
 Fe_a=(1-Q^{a+1})e_{a+1},
\]
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
 =(\lambda+qQ^a\sigma)D_a-q(1-Q^a)^2D_{a-1}.
 \tag{1}
\]
Missing endpoint arrows are zero. The simple physical roots are
\[
 \mu_l=Q^l+qQ^{-l},\quad 0\le l<N,\qquad
 p_N(z)=\prod_{l=0}^{N-1}(z-\mu_l).
\]
For any such root \(\sigma\), let \(U_\sigma\) have columns
\[
 u_\lambda(\sigma)_a=q^{-a}D_a(\lambda;\sigma)/F_a,\qquad
 \Phi_{\lambda,\sigma}(z)
       =\sum_{a=0}^dD_a(\lambda;\sigma)z^a/F_a.
 \tag{2}
\]
The same ordering of \(\lambda\) is used in every \(U_\sigma\).
These are complete invertible matrices.

Write \(\mathcal D e_a=q^{-a}e_a\). T's actual graph crossing on
a scalar deeper channel is
\[
 C_{\nu|\sigma}
   =\kappa\mathcal D\,\overline{U_\nu}U_\sigma^{-1},
 \qquad
 C_{\nu|\sigma}^{-1}
   =\mathcal D\,\overline{C_{\sigma|\nu}}\,\mathcal D^{-1}.
 \tag{3}
\]
Here \(\nu,\sigma\) are arbitrary physical roots. This is the
graph action of the original crossing, not the physical two-head
matrix by itself. Its graph embedding and full-width meaning
are specified in Section 5.

## 2. The complete equal-neighbor Fourier matrix

Fix \(r\in\{0,\ldots,d\}\) and put
\[
 \nu=\mu_r,\quad t=-q^{2r-1},\quad
 \beta=t/q,\quad B=t^2/q,\quad \gamma=t^{-1},\quad v=Q^{-1}.
 \tag{4}
\]
Thus \(|t|=|\beta|=|\gamma|=|B|=1\),
\(B^N=-1\), and \(\nu=-qt-t^{-1}\).
Define the two complete Fourier bases by
\[
 V_j(a)=(\beta Q^{-j})^a,\quad
 Y_i(a)=\gamma^aQ^{ia},\quad 0\le a,i,j<N.
\]
The matrices \(\mathcal V=N^{-1/2}(V_j)_j\) and
\(\mathcal Y=N^{-1/2}(Y_i)_i\) are unitary.
For \(0\le i\le j<N\), use the finite Gaussian binomial
\[
 {j\brack i}_v=\frac{(v;v)_j}{(v;v)_i(v;v)_{j-i}},
 \qquad
 c_{ij}={j\brack i}_v B^iv^{i(i-1)}
                          (Bv^i;v)_{j-i}.
 \tag{5}
\]
Set \(c_{ij}=0\) when \(i>j\), and let \(T_B=(c_{ij})\).
Then the entire actual equal-neighbor crossing is
\[
 \boxed{\quad
 C_{\nu|\nu}V_j=\kappa\sum_{i=0}^jc_{ij}Y_i,\qquad
 C_{\nu|\nu}=\kappa\mathcal YT_B\mathcal V^\dagger .
 \quad}                                                       \tag{6}
\]
No input or output Fourier mode is omitted. Its diagonal
\(c_{jj}=B^jv^{j(j-1)}\) has modulus one, so \(T_B\) is invertible.
The inverse is its ordinary finite triangular inverse; no positivity
or unitary property of \(T_B\) is asserted.

## 3. A finite proof of every matrix entry

For \(0\le j<N\), set
\[
 \lambda_j=tQ^{-j}+qQ^j/t,\qquad
 w_j=u_{\lambda_j}(\nu).
\]
These \(\lambda_j\) are all the physical roots. More explicitly,
if \(N=2h\) then \(\lambda_j=\mu_{[h+1-r+j]_N}\);
if \(N=2h+1\) then \(\lambda_j=\mu_{[h+r-j]_N}\).
T's finite product therefore has lengths \(d-j,j\):
\[
 \Phi_{\lambda_j,\nu}(z)
  =(tQz;Q)_{d-j}((q/t)z;Q)_j
  =(1-(tz)^N)\frac{((q/t)z;Q)_j}
                         {(tQ^{-j}z;Q)_{j+1}}.
 \tag{7}
\]
The equality is an identity of finite polynomials after cancellation.
It is not an infinite product at a root of unity.

The \(j+1\) denominator zeros are distinct. Partial fractions at
\(z=Q^i/t\), \(0\le i\le j\), give the exact vector identity
\[
 w_j=\sum_{i=0}^ja_{ji}V_i,\qquad
 a_{ji}=
 \frac{(-1)^{j-i}Q^{(j-i)(j-i+1)/2}
                  (B^{-1}Q^i;Q)_j}{F_iF_{j-i}}.
 \tag{8}
\]
Indeed the denominator excluding its \(i\)-th zero evaluates to
\(F_i(-1)^{j-i}Q^{-(j-i)(j-i+1)/2}F_{j-i}\).
Multiplying each partial fraction by \(1-(tz)^N\) gives
\(\sum_{a=0}^d(tQ^{-i}z)^a\), whose coefficient conversion
in (2) is exactly \(V_i\). Thus no top-degree remainder occurs.

Equation (3) gives, with the original scalar,
\[
 C_{\nu|\nu}w_j
       =\kappa\mathcal D\,\overline{w_j}
       =\kappa\sum_{i=0}^j\overline{a_{ji}}Y_i.
 \tag{9}
\]
It remains to verify
\(\sum_{i=k}^ja_{ji}c_{ki}=\overline{a_{jk}}\).
We supply the finite algebra.

The elementary Gaussian Newton identity, for either base \(z\), is
\[
 \sum_{i=0}^n{n\brack i}_z
               \prod_{h=0}^{i-1}(X-z^h)=X^n.
 \tag{10}
\]
For proof write the product as \(P_i(X)\). Then
\(XP_i=P_{i+1}+z^iP_i\); induction from \(n=0\),
using Gaussian Pascal, proves (10). We use only \(n<N\),
so all its finite denominators are nonzero.

Put \(G_m=(v;v)_m\). Product reversal rewrites (8) as
\[
 a_{ji}=\frac{(-1)^{i+j}B^{-j}
 Q^{-i(i+1)/2+ij+j(j-1)/2}(Bv^i;v)_j}
                                      {G_iG_{j-i}}.
 \tag{11}
\]
In the desired sum put \(n=j-k\), \(l=i-k\), \(X=Bv^{2k+n}\).
Substitution of (5),(11), with the finite products concatenated,
factors that sum as
\[
 \frac{(-1)^nB^{-n}Q^{2kn+n(n-1)/2}(Bv^k;v)_j}
      {G_kG_n}
 \sum_{l=0}^n{n\brack l}_v
       (-1)^lv^{l(l-1)/2+(1-n)l}(X;v)_l.
 \tag{12}
\]
The last sum is \(X^n\). To see this directly, use
\[
 (X;v)_l=(-1)^lv^{l(l-1)/2}
                      \prod_{h=0}^{l-1}(X-v^{-h}),\qquad
 {n\brack l}_vv^{-l(n-l)}={n\brack l}_{v^{-1}},
 \tag{13}
\]
and apply (10) at base \(v^{-1}\).
Multiplying (12)'s prefactor by \(X^n\) leaves
\[
 \frac{(-1)^nv^{n(n+1)/2}(Bv^k;v)_j}{G_kG_n}
                         =\overline{a_{jk}}.
 \tag{14}
\]
This proves (6) on the complete eigenbasis \(w_j\).
All indices in a denominator are below \(N\).
The factors involving \(B\) are odd powers of \(q\), hence
cannot produce a hidden zero denominator or a cancellation of \(0/0\).
The argument includes \(j=0,d\), empty products and \(N=2\).

## 4. Coherent sums and the endpoint source

For any complex packet \(z\), put \(\eta=\mathcal V^\dagger z\).
The full counting norm and Gram are exactly
\[
 \|C_{\nu|\nu}z\|_2^2
    =\sum_{i=0}^d\left|\sum_{j=i}^dc_{ij}\eta_j\right|^2,
 \qquad
 C_{\nu|\nu}^\dagger C_{\nu|\nu}
    =\mathcal VT_B^\dagger T_B\mathcal V^\dagger .
 \tag{15}
\]
Every cross-input term is inside the square. Unit Fourier bases
do not make the triangular crossing matrix unitary.

For \(h=(t^a)_a\), B's literal matched graph row is \(h/N\).
Since \(hY_i=N\mathbf1_{i=0}\), the normalized observed row is
\[
 \mathscr L(V_j):=\frac{hC_{\nu|\nu}V_j}{N\kappa}
                    =P_j,\qquad P_j=(B;Q^{-1})_j.
 \tag{16}
\]
Thus for arbitrary \(z\), with
\(\widehat z_j=N^{-1}\sum_{a=0}^d\beta^{-a}Q^{ja}z_a\),
one has \(\mathscr L(z)=\sum_j\widehat z_jP_j\).
This retains every high-degree Fourier channel of the input.

In particular \(e_d\) has coefficients
\(\widehat z_j=\beta^{-d}Q^{-j}/N\). The finite products obey
\[
 P_{j+1}=(1-BQ^{-j})P_j,\quad P_0=1,\quad
 P_N=1-B^N=2,
\]
\[
 \sum_{j=0}^{N-1}Q^{-j}P_j=-B^{-1}=B^d,\qquad
 \mathscr L(e_d)=t^d/N.
 \tag{17}
\]
The sum telescopes after multiplying by \(B\).
This is a coherent cancellation, not an estimate by moduli.
The product value \(P_N=2\) must not be confused with the
periodicity \(V_N=V_0\), whose observed value is \(P_0=1\).
When Fourier indices are reduced modulo \(N\), it is the latter
periodicity that applies. Both facts are required by (17).

## 5. Arbitrary neighbors and every deeper channel

For any two physical roots define \(R_{\nu,\sigma}(z)\), modulo \(z^N\),
by constant coefficient one and
\[
 R_{\nu,\sigma}(z)N_\sigma(z)
       =N_\nu(z)R_{\nu,\sigma}(Qz),\qquad
 N_\sigma(z)=1+q\sigma z+q^3z^2.
\]
Writing \(R=\sum_{m=0}^dr_mz^m\), \(r_0=1\), \(r_{-1}=0\),
its complete initialized recursion is
\[
 (1-Q^m)r_m
  =q(\nu Q^{m-1}-\sigma)r_{m-1}
     +q^3(Q^{m-2}-1)r_{m-2},\quad 1\le m<N.
 \tag{18}
\]
Equivalently, the coefficients \(\alpha_m=q^{-m}r_m\) of
\(A_{\nu,\sigma}=\sum_m\alpha_mZ^m\) obey
\[
 (1-Q^m)\alpha_m
   =(\nu Q^{m-1}-\sigma)\alpha_{m-1}
       +q(Q^{m-2}-1)\alpha_{m-2}.
\]
These are the coefficient-shift version of the same initialized recursion.
Let \(Ze_a=e_{a+1}\), \(Ze_d=0\). P's already proved full
Toeplitz comparison, also obtained from T's finite functional equation,
is
\[
 A_{\nu,\sigma}=R_{\nu,\sigma}(q^{-1}Z)
       =U_\nu U_\sigma^{-1},\qquad
 A_{\nu,\sigma}^{-1}=A_{\sigma,\nu}.
\]
Consequently the general scalar-channel compiler is
\[
 \boxed{\quad
 C_{\nu|\sigma}=C_{\nu|\nu}A_{\nu,\sigma}
      =\kappa\mathcal YT_B\mathcal V^\dagger A_{\nu,\sigma}.
 \quad}                                                       \tag{19}
\]
It is the actual two-parameter matrix, with both signs given by
(3) or by finite inversion of (19).

For clarity, this also gives the complete higher-width graph operator,
without restricting to one deeper height. Let the remaining tail be
\(\mathcal U=V_N^{\otimes(b-2)}\), and let \(S=B_c^{(b-2)}\)
be T's entire deeper coideal on it. At \(b=2\), put \(\mathcal U=\mathbb C\)
and \(S=c\). Here, in the original physical head order,
\[
 \mathsf K=\prod_iK_i,\quad
 \mathsf E=\sum_iE_i\prod_{j>i}K_j,\quad
 \mathsf F=\sum_i\left(\prod_{j<i}K_j^{-1}\right)F_i,\quad
 B_c^{(m)}=\mathsf F-(\mathsf E-cI)\mathsf K^{-1},\quad B_c^{(0)}=c.
\]
On \(V_N\otimes\mathcal U\), the actual first graph
crossing is \(C_\nu=\pi_0R_1^+L_\nu\), where
\[
 L_\nu=\sum_{a=0}^d|a\rangle\otimes
          \frac{q^{-a}D_a(\nu;T)}{F_a},\quad
 T=F_2-E_2K_2^{-1}+K_2^{-1}S,\quad \pi_0L_\nu=I.
\]
Use recursion (18) with \(\sigma=S\) and let
\[
 A_{\nu,S}=\sum_{m=0}^dq^{-m}Z^m\otimes r_m(S).
\]
These coefficients commute, and \(p_N(S)=0\) with simple roots.
The complete decomposition into all deeper eigenspaces therefore proves
\[
 C_\nu=(C_{\nu|\nu}\otimes I_{\mathcal U})A_{\nu,S},
 \qquad
 C_\nu^{-1}=A_{\nu,S}^{-1}
                    (C_{\nu|\nu}^{-1}\otimes I_{\mathcal U}).
 \tag{20}
\]
The adapter is unit lower triangular in the first occupation,
with full tail-operator entries. No deeper eigenspace is projected out.
In particular \(A_{\nu,S}(e_d\otimes w)=e_d\otimes w\).

For any full coherent input \(z\), put
\(\eta=(\mathcal V^\dagger\otimes I)A_{\nu,S}z\), whose components
\(\eta_j\) are vectors in the full physical tail. Then
\[
 \|C_\nu z\|_2^2
       =\sum_{i=0}^d\left\|\sum_{j=i}^dc_{ij}\eta_j\right\|_{\mathcal U}^2.
 \tag{21}
\]
Thus the transform is not confined to the equal-neighbor sector.
It preserves coherence both among Fourier inputs and within all
deeper channels. The adapter itself has not been declared unitary
or polynomially conditioned in a physical height metric.

T's actual graph triangular formula also gives
\(C_{\nu|\sigma}e_d=\kappa e_d\), including all endpoints.
The original tensors are
\[
 \mathbf p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\quad
 \ell_{ab}=x^a\mathbf1_{a+b=d}/N,\quad m_{ab}=x^b/N^2.
\]
For the original even-width cup source it yields, exactly,
\[
 z_0=Nx^{-d}e_d\otimes\mathbf p^{\otimes(k-1)},\quad
 u_0=L_cz_0,\quad
 C_cz_0=\kappa z_0,\quad
 K_N=\chi_N\,\ell_0L_c\,R_cz_0.
 \tag{22}
\]
Here \(R_c=\pi_0RL_c\) is the actual complete reduced word, and
\(\ell_0=\ell^{\otimes(k-1)}\otimes m\) is the original last-marked
closing. Formula (17) verifies this endpoint behavior from the
full Fourier sum in the matched block. It does not replace \(z_0\)
by the single geometric packet \(V_0\).

## 6. Sewing, coverage and remaining scope

In a composition the full adapter, Fourier interfaces, source column
and literal closing row are all transported. If \(F\) is an invertible
coordinate frame, they become \(F^{-1}u\) and \(\ell F\), with the
full pulled-back Gram retained. Different faces share their actual
tail variables; no independent resummation or probability is inserted.
The original external \(\chi_N\) and every marked or framing scalar
remain in their prescribed positions.

T already gives the full two-parameter crossing and both signs.
P already gives initialized Toeplitz neighbor adapters, and the
bidiagonal-height note refines those adapters on the physical grid.
B already identifies the matched geometric packet and its legal
charged observation. None of these general comparisons is claimed new.
The addition is the explicit entire Fourier matrix (5)--(6), its finite
Newton proof, and its coherent full-tail use (19)--(22).

The equations are linear maps on full packets, so retaining them as
auxiliary source equations does not increase a quartic variational
objective's degree. They compare representations of the same packet;
they impose no equation between independently summed physical heights.
They do not identify this simple coideal module with the confluent
pair-Casimir compiler or remove its bilinear Conway gluing gates.

This note makes no assertion about canonical quantum holonomy
observations, geometric contour coefficients, or the propagation of a
positive packet through an arbitrary word. In particular (15),(21)
are complete coherent Gram identities, not lower bounds for the
original marked observation in (22). No global scalar lower bound or
arbitrary-short-filling finite-exception theorem follows.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| T | [Actual crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| B | [Balanced marked observations](research_coideal_balanced_marked_height_observations.md) | 467 | 214c462d38a4e1c8bbe64e998d21f259859909a89e8767fde5b234f6dbdde4a6 |
| P | [Initialized Toeplitz comparison](research_coideal_normalized_marked_period.md) | 410 | e5e7ab88016f682411258ccab299f4b7bc2ab6e7052366729d59d993abf84d4b |

Only written mathematics and text/hash operations were used. Earlier
final notes, public manuscripts and the progress ledger remain unchanged.
