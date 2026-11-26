# A positive Toeplitz Gram controls the full boundary Ward factor

Written research proof, 23 November 2026.

The entire actual boundary Ward sum is one finite Euler coefficient.
Its logarithmic factor has exactly the original lowering vacuum as
kernel. After that literal shift and an explicit factor of order \(N\)
are extracted, the remaining matrix has logarithmic norm and a bounded
inverse on the full unit activity disk, at every level \(N\ge2\).
The inverse bound follows from a positive Toeplitz Gram, obtained by
ordinary Fourier orthogonality on an auxiliary finite cycle. No
activity collar, diagonal conditioning gauge or parity restriction is
needed.

The physical occupation grading extracts the Ward coefficient by a
unitary Fourier projection. This gives an \(O(N\log N)\) normal-factor
cost before the retained Euler matrix and original factorial. The
marked co-source, all normal blocks and the final coefficient remain;
no scalar lower bound or geometric-cycle selection is asserted.

## 1. The literal Ward sum and its ordered resummation

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad m=r+1\ge2,\quad x_0=-q^{-1},\quad F_j=(Q;Q)_j.
 \tag{1}
\]
Use the original physical Euclidean occupation basis on the remaining
\(r\) heads. The operator \(E\) is their ordered lowering coproduct,
with one-head coefficient \(Q^{-a}-1\) and the original bottom zero.
Let \(L\) be the first-remaining-head unit lowering shift, tensored
with identities on other heads:
\[
 L|a\rangle=|a-1\rangle\ (a>0),\quad L|0\rangle=0,
 \qquad L^N=0,\quad \|L\|=1.
 \tag{2}
\]
Write \(b=b_{\sigma_1}\) for the actual reduced positive boundary
crossing, including its scalar. For a physical Ward order
\(1\le t<N\), input weight \(\lambda_0^2=Q^{-t}\), and
\(a=\lambda_0/x_0\), one has \(|a|=1\). The complete first-normal
arrow defect [W, (19)--(20)] is
\[
 \mathfrak D_t=2m\sum_{n=1}^{t}(-1)^{n-1}a^n
          \frac{F_t}{F_{t-n}(1-Q^n)}E^{t-n}bL^n.
 \tag{3}
\]
The actual Ward arrow restricts this matrix to its indicated input
weight. The displayed finite sum can also be formed on the full
occupation space. The factor order is part of the formula.
Equation (3) follows from W by the exact cancellation
\({t\brack n}_QF_{n-1}=F_t/[F_{t-n}(1-Q^n)]\).
No denominator has index \(N\).

Define
\[
 \mathcal E_N(z)=\sum_{j=0}^{d}\frac{z^j}{F_j},\qquad
 \ell_N(z)=\sum_{n=1}^{d}\frac{(-1)^{n-1}z^n}{1-Q^n},\qquad
 U_N(T)=\sum_{j=0}^{N-2}(-1)^j
                         \frac{1-Q}{1-Q^{j+1}}T^j.
 \tag{4}
\]
Finite coefficient multiplication proves the exact ordered identity
\[
 \boxed{\quad
 \mathfrak D_t=2mF_t[\xi^t]\,
             \mathcal E_N(\xi E)b\ell_N(a\xi L),\qquad
 \ell_N(T)=\frac{T}{1-Q}U_N(T)\quad(T^N=0).
 \quad}
 \tag{5}
\]
Left multiplication by \(E\) and right multiplication by \(aL\)
commute as operations on matrices; \(E,b,L\) need not commute.
Thus (5) never divides by either nilpotent operator.

The logarithmic sign and normalization are also finite algebra.
In \(\mathbb C[z]/(z^N)\), the Euler coefficient recurrence gives
\[
 \mathcal E_N(Qz)=(1-z)\mathcal E_N(z),\qquad
 \log\mathcal E_N(z)=\sum_{n=1}^{d}\frac{z^n}{n(1-Q^n)},\qquad
 \ell_N(z)=-z\partial_z\log\mathcal E_N(-z)
          =z\mathcal E_N'(-z)\mathcal E_N(-z)^{-1}.
 \tag{6}
\]
Indeed the logarithm has constant term zero, and its degree-\(n\)
coefficient satisfies \((Q^n-1)c_n=-1/n\). The Euler derivative
preserves the ideal \((z^N)\). Evaluation at a nilpotent matrix makes
these identities exact, with finite polynomial inverses. This finite
logarithm is prior coverage in [C].

For any original linear co-source \(\Lambda\) on the normal insertion,
fixed in \(\xi\), the full contraction is exactly
\[
 \Lambda(\mathfrak D_t)=\frac{2mF_t}{2\pi i}
 \oint_{|\xi|=1}\Lambda\!\left(
       \mathcal E_N(\xi E)b\ell_N(a\xi L)\right)
                                      \frac{d\xi}{\xi^{t+1}}.
 \tag{7}
\]
The original weight restriction, exterior, marked closing and scalar
lines stay inside this contraction. On a reciprocal pair, its two
physical Ward arrows recover all four normal blocks of [W, (24)].
In particular the off-diagonal couplings of W's original source
formula (27) are not dropped by (5) or (7).

## 2. The exact positive Toeplitz Gram

Put \(\theta=\pi/N\). For \(0\le j\le N-2\), set
\[
 a_j=\frac{\sin\theta}{\sin((j+1)\theta)}>0,
 \qquad
 \frac{1-Q}{1-Q^{j+1}}=q^{-j}a_j.
 \tag{8}
\]
For the moment let \(N\ge3\) and put \(p=N-2\ge1\). The exact
integral representation is
\[
 a_j=\frac{N\sin\theta}{\pi}
       \int_0^1\frac{x^j+x^{p-j}}{1+x^N}\,dx,
                      \qquad 0\le j\le p.
 \tag{9}
\]
Here is a direct normalization proof. Integrate
\(z^j/(1+z^N)\) around a sector of angle \(2\pi/N\), with
positive orientation. The small and large circular arcs vanish,
respectively as \(O(\epsilon^{j+1})\) and
\(O(R^{j+1-N})\). The sole pole is \(e^{\pi i/N}\), so
\[
 (1-e^{2\pi i(j+1)/N})
       \int_0^\infty\frac{x^j}{1+x^N}\,dx
       =-\frac{2\pi i}{N}e^{\pi i(j+1)/N}.
 \tag{10}
\]
This gives the integral \(\pi/[N\sin((j+1)\theta)]\).
Substitute \(x\mapsto1/x\) in its part above one. The exponent
becomes \(N-j-2=p-j\), proving (9), including its endpoints.

For each \(0<x<1\), the matrix
\[
 C(x)_{ij}=x^{|i-j|}+x^{p-|i-j|},\qquad 0\le i,j\le p,
 \tag{11}
\]
is positive semidefinite. To verify this using finite Fourier
orthogonality, start with the \(p\)-cycle circulant whose row is
\(c_\ell=x^\ell+x^{p-\ell}\), \(0\le\ell<p\). Its Fourier
eigenvalues are the positive numbers
\[
 \sum_{\ell=0}^{p-1}c_\ell e^{-2\pi i k\ell/p}
 =\frac{(1-x^p)(1-x^2)}
          {1-2x\cos(2\pi k/p)+x^2},\qquad 0\le k<p.
 \tag{12}
\]
Summing the two finite geometric series proves the equality. It
also holds for \(p=1\), when its single value is \(1+x\).
The map taking basis vector \(e_j\), \(0\le j\le p\), to
\(e_{[j]_p}\) pulls this positive circulant back to (11): its
indices zero and \(p\) are duplicates, exactly as required by
\(c_p=c_0\). Hence (11) is a positive Gram, without an alias
assumption on a physical color.

Integrating (11) with the positive weight in (9) proves
\[
                   T_a=(a_{|i-j|})_{i,j=0}^{p}\ge0.
 \tag{13}
\]
This is an auxiliary cycle Gram. It neither changes the original
physical quantum root nor replaces any Hermite boundary variable.

## 3. A uniform inverse on the full physical unit disk

Work first on the one physical head where the shift acts. Its range is
\(R=\operatorname{span}\{|0\rangle,\ldots,|N-2\rangle\}\).
For \(|z|=1\), let \(\eta=-q^{-1}z\) and
\(D_\eta|h\rangle=\eta^{-h}|h\rangle\). This is a physical
diagonal unitary and \(D_\eta L D_\eta^{-1}=\eta L\).
Equations (4),(8) give
\[
 U_N(zL)=D_\eta\left(\sum_{j=0}^{N-2}a_jL^j\right)D_\eta^{-1}.
 \tag{14}
\]
Restrict to the invariant space \(R\), of dimension \(p+1\).
The Hermitian part of the middle matrix in (14) is exactly
\((I+T_a)/2\): its diagonal is one and its upper diagonals are
\(a_j\). Therefore (13) proves
\[
 \operatorname{Re}(U_N(zL)|_R)\ge\tfrac12 I_R,
 \qquad \|(U_N(zL)|_R)^{-1}\|\le2,
                         \qquad |z|=1.
 \tag{15}
\]
For \(|z|<1\), apply the harmonic minimum principle to each
quadratic form \(\operatorname{Re}\langle v,U_N(zL)v\rangle\),
\(v\in R\). The same inequalities hold on the full closed disk.

In the orthogonal decomposition \(R\oplus\mathbb C|d\rangle\),
the whole one-head matrix has the form
\[
 U_N(zL)=\begin{pmatrix}U_R(z)&v(z)\\0&1\end{pmatrix},
 \qquad \|v(z)\|^2\le\sum_{j=1}^{N-2}a_j^2\le\pi^2,
                                                   \quad |z|\le1.
 \tag{16}
\]
For the last bound use
\(a_j\le\pi/[2\min(j+1,N-j-1)]\). Each positive denominator
occurs at most twice, and \(\sum_{k\ge1}k^{-2}\le2\).
Block inversion and (15) now give
\(\|U_N(zL)^{-1}\|\le2+2\pi\). Also
\(\sum_{j=0}^{N-2}a_j\le C\log N\), by the corresponding
harmonic-sum estimate. Thus, with absolute constants,
\[
 \boxed{\quad
 \|U_N(zL)\|\le C\log N,\qquad
 \|U_N(zL)^{-1}\|\le2+2\pi,\qquad |z|\le1,
 \quad N\ge2.
 \quad}
 \tag{17}
\]
For \(N=2\), the argument is completed directly by \(U_2=I\);
there is no zero-length cycle to interpret in (12). Tensoring with
identities preserves every bound. All estimates are in the stated
physical Euclidean basis, not a binomial-gauged norm.

## 4. The exact endpoint and arbitrary left contexts

Since \(U_N(zL)\) commutes with \(L\) and is invertible, (5) gives
\[
 \ker\ell_N(zL)=\ker L,\qquad
 \operatorname{im}\ell_N(zL)=\operatorname{im}L\quad(z\ne0).
 \tag{18}
\]
The shift is an isometry from \((\ker L)^\perp\) onto its range.
Using both orders \(LU_N=U_NL\), the nonzero singular values of
\(\ell_N(zL)\) lie between
\(c|z|/|1-Q|\) and \(C|z|\log N/|1-Q|\).
For any compatible rectangular left matrix \(B\), either the physical
operator norm or the Hilbert--Schmidt norm satisfies
\[
 \frac{c|z|}{|1-Q|}\|BL\|
 \le\|B\ell_N(zL)\|
 \le\frac{C|z|\log N}{|1-Q|}\|BL\|,
                     \qquad 0<|z|\le1,\quad N\ge2.
 \tag{19}
\]
The upper bound is multiplication by (17). For the lower bound,
write \(BL=(BLU_N)U_N^{-1}\); the same argument uses the least
singular value of the right factor in Hilbert--Schmidt norm.
In particular \(4/N\le|1-Q|\le2\pi/N\) proves, at \(|z|=1\),
\[
 \boxed{\quad
 cN\|BL\|\le\|B\ell_N(zL)\|
                       \le CN\log N\,\|BL\|.
 \quad}
 \tag{20}
\]
The nonzero singular values lie in the same interval
\([cN,CN\log N]\). The vacuum kernel has not been removed from
the original source. These bounds allow any matrix already on the
left, without a condition number for it. They are not a lower bound
for an arbitrary scalar co-source applied to the resulting matrix.

## 5. Unitary extraction of every physical Ward order

Let \(\mathsf n\) be total remaining integer occupation and put
\(D_\phi=e^{-i\phi\mathsf n}\). Both \(E\) and \(L\) lower degree
by one. The actual \(b\) preserves degree, because every original
crossing, each prefix term, and first-head zero extraction have that
property. Thus
\[
 D_\phi ED_\phi^{-1}=e^{i\phi}E,\quad
 D_\phi LD_\phi^{-1}=e^{i\phi}L,\quad
 D_\phi bD_\phi^{-1}=b.
 \tag{21}
\]
The matrices \(D_\phi\) are unitary in the physical basis. For
\(F(\xi)=\mathcal E_N(\xi E)b\ell_N(a\xi L)\), one consequently has
\[
 F(e^{i\phi})=D_\phi F(1)D_\phi^{-1},\qquad
 [\xi^t]F=\mathsf P_tF(1),\quad
 \mathsf P_tB=\frac1{2\pi}\int_0^{2\pi}
                   e^{-it\phi}D_\phi BD_\phi^{-1}\,d\phi.
 \tag{22}
\]
This is the exact projection onto entries of degree difference
\(-t\). It is contractive in operator norm, by unitary averaging,
and an orthogonal projection in Hilbert--Schmidt norm, where different
degree differences have disjoint matrix-entry supports. In particular
the full family satisfies Parseval; it is not a geometric-window
projection.

Combining (5),(20),(22) proves the all-transfer estimate
\[
 \boxed{\quad
 \|\mathfrak D_t\|\le C m|F_t|N\log N\,
                         \|\mathcal E_N(E)bL\|,
       \qquad 1\le t<N,\quad N\ge2,
 \quad}
 \tag{23}
\]
in both of the stated physical norms. All constants in the factor
estimates are independent of the number of heads; the displayed
\(m\), factorial and remaining Euler-crossing product are retained.
Terms of \(F\) of degree at least \(N\) can occur; exact projection
selects the specified order without replacing \(F(1)\) by a truncated
matrix. An arbitrary exterior is not commuted through \(\mathsf P_t\).
It can always remain in (7), while (19)--(20) apply when it is already
on the left of the logarithmic factor.

There is no lower bound after \(\mathsf P_t\) or the original marked
closing: both can annihilate nonzero matrices. The full-activity
Euler matrix and its geometric period remain to be controlled. The
small-activity results of [C] are not extended to unit activity by
(23). The exact negative-generator and word cocycle laws in [W]
retain their actual inverse matrices and normal insertions when
applied to (5). No bound for those remaining factors is inferred.
All quantum parameters remain at the original root. No physical
Cartan weight is replaced by an off-circle geometric eigenvalue,
and no fixed-root meridian normal or complementary current is erased.

## Complete sources and prior coverage

* W, complete proof direct: notes/research_actual_word_normal_cocycle_and_source.md,
  458 lines, SHA256
  db453e02bc349e7740b2718b25819e9aa8ad1a71b86044fb7128524bea292106.
* C, complete proof direct: notes/research_root_capped_euler_coproduct_factorization.md,
  360 lines, SHA256
  e11f5f827f226ee93505e00aed3885a33abdbfc15ee71e023a67c048c9c17720.
* Earlier collar proof, complete coverage only:
  notes/research_boundary_ward_logarithmic_collar.md, 434 lines, SHA256
  43e71e44044d14895cacc02eeed99bd742f47964bbd2317bd22663e93bca08bd.

The complete matching source and coverage texts were read untruncated
in the author sequence. The earlier collar proof is not used as a
premise for the positive Toeplitz argument. The exact integral, cycle
Gram, inverse estimate, endpoint comparison and physical extraction
are proved above. This text is submitted for independent whole-text
and whole-source review. Only written mathematics and text/hash
operations were used; earlier frozen files were unchanged.
