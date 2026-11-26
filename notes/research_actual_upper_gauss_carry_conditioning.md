# Physical conditioning of the complete upper Gauss normal

Private written proof, 18 November 2026.

The upper Fourier coefficient sector of the actual balanced Gauss
source has polynomial bounds, including its first meridian normal.
Those bounds do not survive evaluation on the original physical
Cartan--Casimir matrices. This note proves an exponential norm lower
bound for the **complete prescribed upper first-normal sum**, not
merely for one interpolation coupon or for an arbitrary nonnormal
matrix. The lower bound survives every positive diagonal physical
metric, including the binomial coherent metric.

The proof uses an actual two-tail-head block at every even level.
An exact finite harmonic cancellation computes its whole radical
multiplier. The product of its nonzero singular values then prevents
cancellation from making the full matrix polynomially bounded.
The original tail pivot on this block is one. A marked pivotal
matrix-entry test is therefore explicit, but it is not an unmarked
knot contraction or a claim about a fixed short-tangle exterior.

The only complete proof directs are C and H, pinned at the end.
No numerical tests, mathematical programs, or imported asymptotic
theorems are used.

## 1. The actual upper first-normal operator

Set
\[
 N=2p\ge2,\quad d=N-1,\quad
 q=e^{\pi i/N},\quad Q=q^2,\quad \theta=\pi/N,
 \qquad f_n=(Q;Q)_n,\quad s_n=|f_n|.
 \tag{1}
\]
The quantum root is fixed. Meridian derivatives below are
\(\partial_\mu\), where \(M=e^\mu\), at \(\mu=0\).

Use C's exact Fourier polynomials and symmetric coupons:
\[
 L_l(u)=\frac1N\sum_{a=0}^{d}(uQ^{-l})^a,\qquad
 \mathcal D_{lk}(u,v)
   =\tfrac12\{L_l(u)L_k(v)+L_k(u)L_l(v)\}.
 \tag{2}
\]
Their physical evaluation is the symmetric-polynomial substitution
\[
 u+v=\frac{\Omega}{qK},\qquad uv=\frac1{QK^2}.
 \tag{3}
\]
There is no choice of a scalar root of the Casimir in (3).
For \(l+k\ge N\), C proves
\[
 C_{lk}(1)=0,\qquad
 \dot C_{lk}=2N\frac{f_{l+k-N}}{f_lf_k}.
 \tag{4}
\]
Here \(C_{lk}(M)=g_{l+k}/(g_lg_k)\), with
\(g_n=(M^{-2}Q;Q)_n\).

Define the **whole prescribed upper normal**
\[
 U_N(K,\Omega)=
       \sum_{\substack{0\le l,k<N\\l+k\ge N}}
                \dot C_{lk}\mathcal D_{lk}(K,\Omega).
 \tag{5}
\]
It is not the derivative of a root-reflected factorial formula.
Since every upper coefficient vanishes at the root, derivatives
of the moving coupons do not occur in this particular normal:
\[
 \left.\partial_\mu
   \sum_{l+k\ge N}C_{lk}(M)
       \mathcal D_{lk}(K(M),\Omega(M))\right|_0
                 =U_N(K(1),\Omega(1)).
 \tag{6}
\]
Moving-coupon derivatives remain essential in C's complete lower
plus upper source; (6) does not remove them there.

Take two literal remaining heads and their physical integer-degree
\(d\) block
\[
 \mathcal V_d
   =\operatorname{span}\{|a,d-a\rangle:0\le a<N\}.
 \tag{7}
\]
Their actual root total Cartan is \(K=1\). Hence their original
total pivotal operator \(K^{1-N}\) is also one on this block.
We write \(U_N\) for the actual matrix \(U_N(1,\Omega)|_{\mathcal V_d}\).
The basis in (7) initially has its balanced flat Euclidean norm.
Section 4 treats every positive diagonal change of that norm.

The physical upper factor in C is
\[
 \mathcal A_{\rm up}(M)=H_d(M)K(M)^d
             \sum_{l+k\ge N}C_{lk}(M)\mathcal D_{lk}(M).
 \tag{8}
\]
Here \(H_d(M)=\prod_{a=1}^d(MQ^{-a}-M^{-1})\).
Because \(H_d(1)=(-1)^dN=-N\), (6) gives
\[
              \mathcal A_{\rm up}(1)=0,\qquad
              \mathcal A_{\rm up}'|_{\mathcal V_d}=-N U_N.
 \tag{9}
\]
Thus the estimate below concerns an actual meridian-normal part
of the literal Gauss source.

## 2. Exact evaluation of the full radical multiplier

Let \(C_n(z)\) be the monic polynomial defined by
\[
 C_n(w+w^{-1})=w^n+w^{-n}.
 \tag{10}
\]
On (7), H proves that the actual Casimir \(\mathcal J=\Omega\)
is complex symmetric tridiagonal. Its offdiagonals are
\[
 \mathcal J_{a+1,a}=\mathcal J_{a,a+1}
                   =-(1-Q^{a+1})^2,\qquad 0\le a<d.
 \tag{11}
\]
Its characteristic polynomial is
\[
 C_N(z)+2=C_p(z)^2.
 \tag{12}
\]
The distinct nodes, all double, are
\[
 \lambda_j=qQ^j+q^{-1}Q^{-j}
       =2\cos((2j+1)\theta),\qquad 0\le j<p.
 \tag{13}
\]
Write \(k=d-j\),
\(\Delta_j=qQ^j-q^{-1}Q^{-j}=2i\sin((2j+1)\theta)\), and
\(\nu_j=(-1)^jq^{j(j+1)}\).

The symmetric polynomial (5), at \(K=1\), has degree at most
\(d\) in \(z=\Omega\). At \(z=\lambda_j\) one can evaluate it
using \(u=Q^j,v=Q^k\). The interpolation polynomials in (2)
then select only the pair \((j,k)\), whose sum is \(d<N\).
Consequently
\[
                        U_N(\lambda_j)=0.
 \tag{14}
\]
To compute its derivative, vary \(u=Q^je^t,v=Q^ke^{-t}\).
The product \(uv=Q^{-1}\) is fixed and
\(\Omega_t|_0=\Delta_j\). For \(l\ne j\), the exact finite
fraction for \(L_l\) gives
\[
 Q^jL_l'(Q^j)=-\frac1{1-Q^{j-l}}.
 \tag{15}
\]
The coefficient array is symmetric, so its sum against
\(\mathcal D_{lk}\) equals its sum against \(L_l(u)L_k(v)\).
Only \(l>j\) or \(k'>k\) survives in its \(t\)-derivative.
Put
\[
 T_r(l)=\frac{f_{r-1}f_l}
                {f_{l+r}(1-Q^{-r})},\qquad l+r<N.
 \tag{16}
\]
Using \(f_d/(f_jf_k)=\nu_j^{-1}\), equations (4),(15)
give the exact finite sum
\[
 (U_N)_t(\lambda_j)
 =2\nu_j^{-1}\left\{
        \sum_{s=1}^{j}T_s(k)-\sum_{r=1}^{k}T_r(j)\right\}.
 \tag{17}
\]
No phases in this sum have been discarded.

Here is its finite harmonic cancellation. Direct subtraction yields
\[
 T_r(l)-T_r(l-1)
       =\frac{Q^{l+r}f_{l-1}f_{r-1}}{f_{l+r}}
       =:G(l,r)=G(r,l).
 \tag{18}
\]
Indeed the quotient of the two \(T\)'s is
\((1-Q^l)/(1-Q^{l+r})\), and
\((Q^r-1)/(1-Q^{-r})=Q^r\).
Expanding \(T_r(j)\) from \(j=0\) makes the two double sums
in (17) equal rectangular sums of \(G\). They cancel.
Finally
\[
 T_r(0)=\frac1{(1-Q^r)(1-Q^{-r})}
                         =\frac1{4\sin^2(r\theta)}.
 \tag{19}
\]
Since \(j<k\), we obtain
\[
 \boxed{\quad
 U_N'(\lambda_j)=
   -\frac{\nu_j^{-1}}{2\Delta_j}
        \sum_{r=j+1}^{d-j}\csc^2(r\theta).
 \quad}
 \tag{20}
\]
This is the derivative with respect to the Casimir argument, of
the already specified meridian normal (5).
Every coefficient in (20) is nonzero.

## 3. The original Hermite frame and its determinant

For clarity we recall exactly the part of H used here.
Let \(\phi_a(z)\) be the normalized continuant column of
the tridiagonal matrix (11):
\[
 \phi_0(z)=1,\qquad
 \phi_a(z)=
 \frac{\det(zI-\mathcal J_{[0,a-1]})}
      {\mathcal J_{1,0}\mathcal J_{2,1}\cdots
                              \mathcal J_{a,a-1}}.
 \tag{21}
\]
It has degree \(a\) and the displayed reciprocal leading
coefficient. Write
\[
 v_j=(\phi_0(\lambda_j),\ldots,\phi_d(\lambda_j))^{\mathsf t},
 \qquad
 v'_j=(\phi_0'(\lambda_j),\ldots,\phi_d'(\lambda_j))^{\mathsf t}.
 \tag{22}
\]
These are the actual value and Jordan-partner columns,
\((\mathcal J-\lambda_j)v'_j=v_j\).
The bilinear pairings of distinct nodes vanish, and the
pairing on each two-column block is
\[
 \begin{pmatrix}0&\sigma_j\\
                 \sigma_j&\sigma_j\eta_j\end{pmatrix},
       \qquad
              |\sigma_j|=\frac1{4\sin^2((2j+1)\theta)}.
 \tag{23}
\]
No estimate or value of \(\eta_j\) is needed.
The inverse of this two-by-two block shows that a polynomial
whose values vanish at all nodes acts by
\(\sum_j P'(\lambda_j)v_jv_j^{\mathsf t}/\sigma_j\).
Applying (14),(20), and setting
\[
 F=(v_0,\ldots,v_{p-1}),\qquad
 b_j=U_N'(\lambda_j)/\sigma_j,
 \tag{24}
\]
therefore proves the actual matrix identity
\[
                 U_N=F\operatorname{diag}(b_j)F^{\mathsf t}.
 \tag{25}
\]
It has rank \(p\). In particular, this expression retains
all Jordan directions and is not a diagonal spectral evaluation.
Equations (20),(23) give
\[
 |b_j|=\sin((2j+1)\theta)
            \sum_{r=j+1}^{d-j}\csc^2(r\theta)
             \ \ge\ \sin((2j+1)\theta).
 \tag{26}
\]

The first \(p\) physical rows of \(F\), denoted \(F_0\),
have a Vandermonde determinant. By (11),(21),
\[
 |\det F_0|^2
   =\frac{\prod_{j<k}|\lambda_k-\lambda_j|^2}
          {\prod_{a=0}^{p-1}s_a^4}.
 \tag{27}
\]
The roots in (13) are precisely those of monic \(C_p\).
Differentiating \(C_p(2\cos t)=2\cos(pt)\) gives
\[
 |C_p'(\lambda_j)|=\frac p{\sin((2j+1)\theta)}.
 \tag{28}
\]
The elementary root product
\(\prod_{j=0}^{p-1}\sin((2j+1)\theta)=2^{1-p}\)
follows by taking absolute values in \(z^p+1\) at \(z=1\).
Hence
\[
 \prod_{j<k}|\lambda_k-\lambda_j|^2
                  =2^{p-1}p^p,\qquad
 \det(F^*F)\ge|\det F_0|^2
      =\frac{2^{p-1}p^p}{\prod_{a=0}^{p-1}s_a^4}.
 \tag{29}
\]
The Gram inequality is Cauchy--Binet and uses an actual
physical-row minor, not a chosen eigenframe norm.

## 4. An exact lower bound in every diagonal physical metric

For any positive diagonal \(D\) in the basis (7), let
\(\|\cdot\|_D\) mean \(\|D(\cdot)D^{-1}\|_{\rm op}\).
This includes the balanced flat norm and the tensor binomial
coherent metric restricted to this block.

For a full-column-rank matrix \(X\), thin QR shows that the
product of the \(p\) nonzero singular values of
\(X B X^{\mathsf t}\) is
\(\det(X^*X)|\det B|\).
More generally, for (25) after diagonal conjugation, that product is
\[
 \left(\prod_j|b_j|\right)
 \sqrt{\det(F^*D^2F)\det(F^*D^{-2}F)}.
 \tag{30}
\]
To verify it, write
\(DU_ND^{-1}=(DF)\operatorname{diag}(b_j)
 (D^{-1}\overline F)^*\) and take thin QR on both
rectangular factors. Their determinant moduli are the square roots
of their Gram determinants. Complex conjugation on the second
Gram does not change its positive real determinant.

Determinant Cauchy--Schwarz applied to \(DF,D^{-1}F\) gives
\[
 \det(F^*D^2F)\det(F^*D^{-2}F)
                         \ge\det(F^*F)^2.
 \tag{31}
\]
One proof takes their exterior products of degree \(p\)
and applies ordinary Cauchy--Schwarz; their mutual determinant is
\(\det(F^*F)\).
Combining (26),(29)--(31), the product of the nonzero singular
values is at least
\[
 \frac{2^{p-1}p^p}{\prod_{a=0}^{p-1}s_a^4}
       \prod_{j=0}^{p-1}\sin((2j+1)\theta)
                =\frac{p^p}{\prod_{a=0}^{p-1}s_a^4}.
 \tag{32}
\]
At least one singular value is at least their geometric mean.
We have proved the finite, uniform statement
\[
 \boxed{\qquad
 \|U_N\|_D\ \ge\
       p\left(\prod_{a=0}^{p-1}s_a\right)^{-4/p}
       \quad\text{for every positive diagonal }D.
 \qquad}
 \tag{33}
\]
This argument concerns the **entire** upper normal.
Its scalar phases cannot invalidate (33), since they cancel
from the product of singular values.

## 5. The positive exponential rate

Define
\[
 J(t)=\int_0^t\log(2\sin(\pi x))\,dx,\qquad
 \gamma=-8\int_0^{1/2}J(t)\,dt.
 \tag{34}
\]
Here \(\gamma>0\). Indeed the logarithm is negative up to
\(t=1/6\) and positive thereafter up to \(1/2\), and
\(J(1/2)=0\). The latter identity follows by putting
\(I=\int_0^{\pi/2}\log\sin x\,dx
 =\int_0^{\pi/2}\log\cos x\,dx\), adding, and using
\(\sin x\cos x=\tfrac12\sin2x\); it gives
\(I=-(\pi/2)\log2\).
Thus \(J(t)<0\) for every \(0<t<1/2\).

For completeness a monotone integral comparison on
\([1/N,1/2]\) gives, uniformly for \(0\le a\le p\),
\[
                    \log s_a=NJ(a/N)+O(\log N).
 \tag{35}
\]
The function \(\log(2\sin\pi x)\) is increasing on this
interval. Comparing its left and right rectangle sums costs
at most its endpoint difference \(O(\log N)\);
the omitted interval \([0,1/N]\) has integral
\(O((\log N)/N)\). This proves (35), including \(a=0\).
Since \(J\) has bounded variation on \([0,1/2]\), a second
rectangle comparison gives
\[
 \sum_{a=0}^{p-1}\log s_a
          =N^2\int_0^{1/2}J(t)\,dt+O(N\log N).
 \tag{36}
\]
Equations (33),(36), with \(p=N/2\), imply
\[
 \boxed{\quad
       \log\|U_N\|_D\ge\gamma N-O(\log N),
                     \qquad N\ \text{even}.
 \quad}
 \tag{37}
\]
The constants are independent of \(D\).
By (9), the same exponential rate holds for the actual upper
normal \(\mathcal A_{\rm up}'\), with its extra factor \(N\).
Consequently a polynomial estimate on a whole scaled meridian
collar for this evaluated upper sector is impossible:
Cauchy's estimate would give a polynomial first \(\mu\)-normal,
contradicting (37).

## 6. Source meaning and limits

C bounds the complete upper coefficient array, its fixed scalar
Fourier jets on thin annuli, and its fixed meridian jets by
polynomials. Equations (33),(37) show that evaluation on the
specified original physical representation can nevertheless cost
an exponential. This holds after every positive diagonal
factorial or coherent change of metric.

There is an exact marked pivotal test. In any such orthonormal
physical coordinates, one entry of \(U_N\) has modulus at least
\(\|U_N\|_D/N\). The corresponding reversed matrix-unit mark has
norm one. Since the actual total tail pivot is one on (7), its
pivotal trace with \(U_N\) is exactly that entry. Applying (9)
retains the actual \(H_dK^d\) first-normal factor as well.
The mark can depend on the level and the entry attaining this
bound. It is not asserted to be the image of a fixed braid or
a fixed short filling.

The complete opposite source remains C's identity
\[
 T=\mathcal B_m(W_\tau^{-1})\,\mathcal A_N\,
              D_{\rm top}\mathscr C_r(M),\qquad
 J=D_N(MK)^{-1}T.
 \tag{38}
\]
None of these factors, the original cut, its framing scalar,
or an exterior contraction is removed. Even though the upper
factor vanishes at the root, its normal (9) must be transported
through all factors in (38). The present lower bound for that
factor does not give a lower bound after those compositions.
Their coherent cancellations remain possible.

Thus the proposed general polynomial-cost evaluation of the
upper Fourier carry is false already on this actual fixed-width
physical block. A proof that its contribution is small in a
particular original closed source would require additional
source-specific cancellation or a weighted non-diagonal estimate
with its boundary costs retained. No knot noncancellation,
geometric occurrence, or volume conclusion is inferred.

## Complete proof directs

* C: notes/research_balanced_gauss_cyclic_divisor_source.md,
  SHA256 c15668d7dff95346d72801b721bf95970b661e5b17d125aaadd7e0dc38905b00.
* H: notes/actual_complete_casimir_hermite_packet.md,
  SHA256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.

Both complete directs were read nontruncated in this active author
sequence. Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.
