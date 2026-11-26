# An actual upper Euler column with a controlled complex resolvent chart

Private written proof, 18 November 2026.

A diagonal change on the donor alone turns the actual top column of
the finite Euler star into a finite resolvent of the original recipient
raising matrix. The recipients keep their binomial metric, compact
coherent kernels, and endpoint arrows. On every fixed compact recipient
chart away from incidence, sufficiently large donor coordinate gives an
actual holomorphic kernel with nonzero amplitude and relative error
\(O(N^{-1})\).

Every donor input and dual factor is explicit. In the opposite kernel,
full turnover moves the remaining inverse-factorial coupon to the last
head; it does not disappear against the first-head quotient. The result
estimates an actual source factor, not the complete opposite kernel or
a geometric relative cycle.

The sole complete direct J is pinned below. It supplies the actual
finite prefix, turnover, and compact source conventions. The column
identity, metric estimate, all-power bounds, and interfaces are proved here.

## 1. Donor-only gauges and the literal upper column

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 f_a=(Q;Q)_a,\quad x=-M/q.
 \tag{1}
\]
There are one donor and \(r\ge1\) recipient heads at common meridian
\(M\ne0\). The quantum root is fixed. With the actual ordered
recipient total \(F_{\rm r}(M)\), the original star is
\[
 S(M)=\sum_{n=0}^d\frac{x^{-n}L_1^nF_{\rm r}(M)^n}{f_n},
 \qquad F_{\rm r}(M)^N=0.
 \tag{2}
\]
The donor shift \(L_1w_a=w_{a-1}\) has its bottom zero, and every
recipient raising arrow has its physical top zero.

On the donor only define
\[
 G w_a=f_aw_a,\quad Yw_a=Q^{a(a+1)/2}w_a,\quad D=YG^{-1},
 \qquad \widetilde S=(D\otimes I)S(D^{-1}\otimes I).
 \tag{3}
\]
No recipient factorial gauge is used. All \(f_a\), \(a<N\), are
nonzero; \(Y\) is unitary in every diagonal occupation metric.
Reflecting the finite root product gives
\[
 \frac{f_d}{f_{d-n}}=(-1)^nQ^{-n(n+1)/2}f_n,\quad
 \frac{Y_{d-n}}{Y_d}=Q^{n(n+1)/2},\quad
 f_d=N,\quad Y_d=(-1)^d .
 \tag{4}
\]
For the first identity replace
\(1-Q^{N-j}=-Q^{-j}(1-Q^j)\), \(1\le j\le n\).
Consequently, with \(i_av=w_a\otimes v\),
\[
 \boxed{\quad
 \widetilde S(M)i_d=\sum_{n=0}^d i_{d-n}(-x^{-1}F_{\rm r}(M))^n .
 \quad}\tag{5}
\]
This is a whole finite-matrix identity for every \(M\ne0\).

Let \(v(\zeta)w_a=\zeta^a\), and set
\[
 \mathcal U_N(\zeta,M)=
             \sum_{n=0}^d(-x^{-1}F_{\rm r}(M)/\zeta)^n .
 \tag{6}
\]
Then
\[
 (v(\zeta)\otimes I)\widetilde S i_d=\zeta^d\mathcal U_N,
 \qquad
 \boxed{\quad\mathcal U_N=(I+x^{-1}F_{\rm r}(M)/\zeta)^{-1}\quad}
 \tag{7}
\]
for \(\zeta\ne0\). Multiplication of the finite sum leaves
\(I-(-x^{-1}F_{\rm r}/\zeta)^N=I\). The column
\(\zeta^d\mathcal U_N\) remains a polynomial at \(\zeta=0\).
No nilpotent finite matrix has been replaced by a non-nilpotent scalar.

For an arbitrary donor row \(\ell\), the exact source interface is
\[
 \boxed{\quad
 (\ell\otimes I)S i_d=\frac{(-1)^d}{N}
              (\ell GY^{-1}\otimes I)\widetilde S i_d .
 \quad}\tag{8}
\]
Thus the evaluation row of (7) corresponds to the original row
\(v(\zeta)D\), with its stated input scalar. An arbitrary exterior
row is not silently replaced by it.

The negative star has a companion column without the chirp.
The inverse of (2) has coefficient
\((-1)^nQ^{n(n-1)/2}/f_n\) in degree \(n\) of
\(x^{-1}L_1F_{\rm r}\). Multiplication proves this: the
degree-\(n>0\) coefficient is
\(f_n^{-1}\sum_j{n\brack j}_Q(-1)^jQ^{j(j-1)/2}
=f_n^{-1}(1;Q)_n=0\), by the finite binomial product.
Using (4), its donor-only \(G^{-1}S^{-1}G\) column is therefore
\[
 (v(\zeta)\otimes I)G_1^{-1}S(M)^{-1}G_1i_d
          =\zeta^d(I-Q^{-1}x^{-1}F_{\rm r}(M)/\zeta)^{-1}.
 \tag{8a}
\]
Its original-row interface is
\(\ell S^{-1}i_d=N^{-1}(\ell G_1)
(G_1^{-1}S^{-1}G_1)i_d\).
The inverse is the exact finite nilpotent sum, with no endpoint removal. The estimates
below apply to it after replacing \(x^{-1}/\zeta\) by
\(-Q^{-1}x^{-1}/\zeta\).

## 2. Recipient norm control in the original metric

Use the original head metric
\[
                         \|w_a\|^2=\binom da^{-1}.
 \tag{9}
\]
This is the metric in which J's binomial column
\(c(z)_a=\binom daz^a\) is dual to evaluation on the real compact
coherent sphere. The literal raising matrix is
\(Fw_a=(1-Q^{a+1})w_{a+1}\), \(a<d\), and \(Fw_d=0\).
Its weighted shift norm is the maximum of
\[
 2\sin\!\left(\frac{\pi(a+1)}N\right)
                         \sqrt{\frac{a+1}{N-1-a}}.
 \tag{10}
\]
Writing \(s=(a+1)/N\) and using \(\sin(\pi s)\le\pi(1-s)\)
bounds (10) by \(2\pi\sqrt{s(1-s)}\le\pi\).
Also \(\|K^{\pm1}\|=|M|^{\pm1}\), so the actual coproduct gives
\[
 \|F_{\rm r}(M)\|\le\pi\sum_{j=0}^{r-1}|M|^{-j}.
 \tag{11}
\]
On a donor domain where
\[
 \rho:=\frac{|x|^{-1}}{|\zeta|}
                 \pi\sum_{j=0}^{r-1}|M|^{-j}<1,
 \tag{12}
\]
one therefore has
\[
 \|\mathcal U_N\|\le(1-\rho)^{-1},\qquad
 \|\mathcal U_N^{-1}\|\le1+\rho.
 \tag{13}
\]
These are estimates in the unchanged recipient metric. They hold
uniformly on a fixed meridian disk bounded away from zero, with fixed
derivatives on smaller disks. In particular they hold on
\(M=e^{u/N}\), \(|u|\le\eta\), at fixed \(r,\eta\), with a fixed
strict donor margin. They do not estimate \(G\) or \(G^{-1}\).

## 3. All finite powers on a complex coherent chart

For the recipients retain J's compact kernels
\[
 K_B(\mathbf w,\mathbf z)=v(\mathbf w)B c(\mathbf z),\quad
 B_N=\prod_{i=1}^r(1+w_i z_i)^d,\quad \sigma_N(B)=K_B/B_N.
 \tag{14}
\]
All caps are finite. The normalized kernel is defined on
\[
 X^r,\qquad
 X=(\mathbb P^1\times\mathbb P^1)\setminus\{1+wz=0\}.
 \tag{15}
\]
Put
\[
 \theta_i=\frac{w_i z_i}{1+w_i z_i},\qquad
 h=\frac{2\pi i}{N},\qquad \eta_N(\theta)=e^{dh\theta},
\]
\[
 b_{N,r}(M;\mathbf w,\mathbf z)
 =\sum_{j=1}^r x^{-(j-1)}w_j
       (1-Q\eta_N(\theta_j))\prod_{i<j}\eta_N(\theta_i).
 \tag{16}
\]
This is holomorphic on \(X^r\). In particular the apparent factor
\(w_j\) at infinity is removable because \(Q\eta_N(1)=1\) and
\(w_j(1-\theta_j)=w_j/(1+w_jz_j)\) is regular there.
Keeping \(d=N-1\) and the displayed \(Q\) prevents a false
projective pole.

For each \(\mathcal K\Subset X^r\) and fixed compact meridian disk
\(\mathcal M\) bounded away from zero, there is \(C>1\), independent
of \(N\), such that, for every \(1\le n<N\),
\[
 \boxed{\begin{split}
 |\sigma_N(F_{\rm r}(M)^n)|&\le C^n,\\
 |\sigma_N(F_{\rm r}(M)^n)-b_{N,r}(M)^n|
                                  &\le C^n n^2/N .
 \end{split}}\tag{17}
\]
Each fixed coordinate or meridian derivative has the same form on
smaller charts, after increasing the constants.

Here is a proof including the finite endpoints. On output polynomials
let \(T_i p(\mathbf w)=p(w_1,\ldots,Qw_i,\ldots,w_r)\).
The literal matrices act as
\[
 F_i=w_i(1-QT_i),\qquad K_i^{-1}=x^{-1}T_i,
\]
and hence
\[
 F_{\rm r}=\sum_{j=1}^r
         x^{-(j-1)}w_j(1-QT_j)\prod_{i<j}T_i.
 \tag{18}
\]
In particular \(F_iw_i^d=0\). An \(n\)-fold expansion has at most
\((2r)^n\) words. Moving coordinate multiplications to the left
turns each into
\[
 c(M)Q^\ell\mathbf w^{\mathbf s}T^{\mathbf k},\qquad
 |\mathbf s|=n,\quad 0\le k_i\le n,\quad |\ell|\le C_r n^2.
 \tag{19}
\]
The coefficient mass is at most \(C^n\) uniformly on \(\mathcal M\).
Retain the basic factors \(Q\) from \(1-QT_j\). Replacing only the
extra ordering phase by one changes its coefficient by at most
\(C^n n^2/N\), since \(|Q^\ell-1|\le2\pi|\ell|/N\).

The exact normalized kernel of the remaining monomial is
\[
 \mathbf w^{\mathbf s}
       \prod_i\left(\frac{1+Q^{k_i}w_i z_i}{1+w_i z_i}\right)^d.
 \tag{20}
\]
Individual terms may have apparent upper-degree parts, but their
complete finite sum has exactly the endpoint cancellations in (18).
No expanded term is interpreted as an unrestricted physical shift.

On an affine compact set away from incidence,
\[
 \left|\left(\frac{1+Q^k v}{1+v}\right)^d\right|\le e^{Ck},
 \qquad 0\le k<N.
 \tag{21}
\]
This follows from \(|Q^k-1|\le2\pi k/N\) and
\(|1+(Q^k-1)v/(1+v)|^d\le e^{Ck}\).
For \(k\le\sqrt N\), expansion of the logarithm at one gives
\[
 \left(\frac{1+Q^k v}{1+v}\right)^d
     =e^{dhk\,v/(1+v)}
                     +O(k^2e^{Ck}/N).
 \tag{22}
\]
The finitely many small levels are absorbed by the constant.
For \(k>\sqrt N\), (21) and the corresponding exponential
bound prove (22) with a larger constant, since \(k^2/N>1\).
Multiplying over the fixed number of heads gives an error
\(C^n n^2/N\) when the shifts in (20) are replaced by
\(\eta_N(\theta_i)^{k_i}\).

After that replacement and removal of the extra ordering phases,
the word expansion is precisely the commutative \(n\)-th power
of (16). Summing proves (17) on affine compacts.
Both sides of the difference are holomorphic on \(X^r\).
Around an infinite coordinate choose a small projective polydisk
avoiding incidence, with distinguished boundary in finite old
coordinates. The affine estimates on that boundary and the maximum
principle extend them through the polydisk. A finite cover proves
(17) on arbitrary \(\mathcal K\Subset X^r\).
Doing this on slightly larger charts and a larger meridian disk
and applying Cauchy estimates proves the fixed-derivative statement.
Only the original finite caps and exact shift words were used.

## 4. A genuine complex local unit

Enlarge \(C\) in (17) to bound \(|b_{N,r}|\) too. Choose a donor
domain with fixed \(\varrho<1\) satisfying
\[
           \sup_{M\in\mathcal M}|x|^{-1}C/|\zeta|\le\varrho.
 \tag{23}
\]
Summing the exact finite resolvent gives
\[
 \boxed{\quad
 \sigma_N(\mathcal U_N(\zeta,M))
    =\frac{1}{1+x^{-1}b_{N,r}(M;\mathbf w,\mathbf z)/\zeta}
                                  +O(N^{-1}).
 \quad}\tag{24}
\]
Indeed the error in (17) sums to
\(N^{-1}\sum_{n\ge1}n^2\varrho^n\); the missing commutative
geometric tail is bounded by \(\varrho^N/(1-\varrho)\).
The same conclusion holds with every fixed derivative on smaller
domains by Cauchy estimates.

The leading factor has modulus at least \((1+\varrho)^{-1}\).
Thus the actual normalized kernel is nonzero for sufficiently
large \(N\), uniformly on smaller compact domains. In local
branches the actual transformed upper-column kernel is
\[
 \boxed{\quad
 \zeta^d\prod_i(1+w_i z_i)^d
   \left[\frac{1}{1+x^{-1}b_{N,r}/\zeta}+O(N^{-1})\right].
 \quad}\tag{25}
\]
This phase and unit amplitude belong to an actual finite kernel,
not to an interpolation of a discrete spectral label.

The estimate is uniform on a fixed complex \(M\)-disk. Fixed
meridian derivatives retain every \(x(M)\) factor and obey the same
error on smaller disks; restricting to \(M=e^{u/N}\) is legitimate.
Ordinary quantum-parameter normals are not obtained by differentiating
the root identity \(F_{\rm r}^N=0\).

## 5. The retained interface in the opposite source

For J's actual opposite kernel on \(m=r+1\) heads, use
\(E_\Sigma^d\mathscr C_m=\mathscr C_mF_\Sigma(M^{-1})^d\)
and \(F_\Sigma(M^{-1})^di_0=NS_m(M^{-1})i_d\).
These give the exact form
\[
             T(M)=Nq_F(M)\mathscr C_m(M)S_m(M^{-1})i_d.
 \tag{26}
\]
The upper star is therefore at the reflected meridian. Equation (8)
gives the exact pairing
\[
 T(M)=(-1)^d q_F(M)\mathscr C_m(M)
                 (GY^{-1})_1\widetilde S_m(M^{-1})i_d.
 \tag{27}
\]
Full turnover reverses the heads. Moving the donor diagonal through
it puts the reflected diagonal on the last head, not the first.
The finite reflection identity in (4) gives
\[
 f_{d-b}Q^{-(d-b)(d-b+1)/2}
                          =N(-1)^{d+b}/f_b.
 \tag{28}
\]
The balanced turnover coefficient cancels in this diagonal
conjugation, so the identity is valid in the whole meridian family.
Writing \(Z_m w_b=(-1)^bw_b\) on the last head,
\[
 \mathscr C_m(GY^{-1})_1
                  =N(-1)^dZ_mG_m^{-1}\mathscr C_m,
\]
and hence
\[
 \boxed{\quad
 T(M)=Nq_F(M)Z_mG_m^{-1}\mathscr C_m(M)
                             \widetilde S_m(M^{-1})i_d.
 \quad}\tag{29}
\]
This is the original-source interface. The recipients in (24) have
no hidden factorial gauge, but the complete paired source retains
the specified last-head inverse-\(G\) coupon. It does not commute
freely through \(q_F=p_0S_m^{-1}\). Neither its size nor its
coherent generating function is estimated by (24).

Every factor in (26)--(29), including \(N\), full balanced turnover
and the first-head quotient, remains in J's compact source
convolution. Its normalization \(D_N(MK_{\rm r})^{-1}\), Laurent
rows, and first-meridian-jet assembly remain unchanged.
An arbitrary exterior is paired through (8), (27), or (29); it is
not replaced by the special evaluation row in (7).

The theorem supplies a controlled upper-column factor with exact
source interfaces. It does not bound the residual inverse-\(G\)
coupon or prove that the resolved loxodromic frame satisfies (23)
in the full pairing. No geometric occurrence, relative-window
transport, or lower bound for the closed source is inferred.

## Complete proof direct

* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.

The complete direct was freshly read nontruncated in the preceding
active author sequence and retained unchanged here. Every used
implication was checked. Only written mathematics and text/hash
operations were used. Frozen and public files were not changed.

