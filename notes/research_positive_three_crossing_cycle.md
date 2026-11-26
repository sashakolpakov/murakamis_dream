# Positive spectral moments for original three-crossing chains

Research note, 3 November 2026. Frozen manuscripts are unchanged.

There is an exact positive operator behind a chain of original
three-crossing vertices. It sums the endpoint contributions before
estimating them. It gives a sharp asymptotic for the cyclic trace
network and a nonzero exponential lower bound for a specified capped
chain of arbitrary fixed length. The latter bound is not identified
with its geometric action. The general two-boundary kernel remains
a mixed spectral pairing.
The [cap-seed follow-up](research_positive_three_crossing_cap_seed.md)
identifies the third moment with a previously controlled original
source, proves its sharp rate, and improves the bounds for every
longer capped chain.

## 1. Exact source and positive conjugacy

Put \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\),
\(\kappa=q^{D^2/2}\), and \(S_j=\prod_{r=1}^j2\sin(\pi r/N)\).
The original crossing and turn matrices are
\[
 M_{jk}=\kappa(-1)^j q^{j(k+1)}
             \frac{S_j}{S_kS_{j-k}}\quad(0\le k\le j<N),
 \qquad J_{jk}=\mathbf1_{j+k=D}.
 \tag{1}
\]
The omitted crossing entries vanish. The exact original identities are
\[
 M^{-1}=\overline M,\qquad M^T=JMJ,\qquad
 MJM=\kappa JM^{-1}J.
 \tag{2}
\]
They hold in the full Newton algebra, including the normal directions
at the double roots; see the
[primitive source calculation](research_quantum_cap_primitive_source.md),
Section 2. All adjoints below are for the ordinary Euclidean Hermitian
inner product.

The traced degree-two vertex is
\[
 V_{n,N}(x,y)=h(x)^T A_n h(y),\qquad A_n=JM^n,\qquad
 h_j(x)=\frac{\sin(\pi N(x-j/N))}
                 {N\sin(\pi(x-j/N))}.
 \tag{3}
\]
The apparent singularities are removable. The exact cardinal identity
\(N\int_a^{a+1}h_j(x+ib)h_k(x+ib)\,dx=\delta_{jk}\)
composes these vertex matrices in their actual order. This is the
[full-jet circle averaging theorem](research_internal_wire_exact_circle_averaging.md),
not an approximation of the vertex kernel.

**Theorem 1.** Set \(A=JM^3\) and \(H=M^*M\). Then
\[
                  MAM^{-1}=\kappa H,\qquad
                  A^m=\kappa^m M^{-1}H^mM
                  \quad(m\ge0).
 \tag{4}
\]
In particular \(H>0\), and every eigenvalue of \(A\) is
\(\kappa\) times a strictly positive real number.

*Proof.* By (2),
\[
 MAM^{-1}=MJM^2
   =\kappa JM^{-1}JM=\kappa M^*M.
 \tag{5}
\]
The matrix \(M\) is invertible. Taking powers proves (4).
\(\square\)

For arbitrary powers the same change of basis gives the exact identity
\[
 M A_{n_1}\cdots A_{n_m}M^{-1}
    =\kappa^m H M^{n_1-3}H M^{n_2-3}\cdots H M^{n_m-3}.
 \tag{6}
\]
The extra factors in (6) cannot be treated as positive or unitary.
The positive-power theorem here concerns the homogeneous exponent
three. Coefficient conjugation gives its mirror.

For the full ordinary boundary vector
\(v(z)=(e_0(z),\ldots,e_D(z))^T\), the open chain is
\[
 v(z)^T A^m v(w)
   =\kappa^m\bigl(M^{-T}v(z)\bigr)^T
                    H^m\bigl(Mv(w)\bigr).
 \tag{7}
\]
This retains the entire boundary polynomials and all their derivatives.
It is not a positive quadratic form, even for equal real boundary
arguments: its two transformed vectors differ. No positivity of (7)
is inferred from (4).

## 2. A sharp cyclic-network asymptotic

Define the cyclic contraction of \(m\) actual vertices by
\[
 \mathcal C_{m,N}
   =N^m\int_{[0,1]^m+i\mathbf b}
       \prod_{r=1}^m V_{3,N}(x_r,x_{r+1})\,d\mathbf x,
       \qquad x_{m+1}=x_1,
 \tag{8}
\]
with arbitrary real heights \(\mathbf b\). For \(m=1\) the single
factor has the same argument in both slots. The cardinal identity
in (3), applied once to each variable, gives
\[
                  \mathcal C_{m,N}
                    =\operatorname{Tr}(A^m)
                    =\kappa^m\operatorname{Tr}(H^m).
 \tag{9}
\]
In particular its phase-normalized value is strictly positive at
every level.

Let
\[
 \mathcal J(s)=\int_0^s\log(2\sin\pi t)\,dt,\qquad
 c=2\mathcal J(5/6)=-3\mathcal J(1/3)>0,\qquad
 \rho=\frac{5-\sqrt{21}}2.
 \tag{10}
\]

**Theorem 2.** For every fixed integer \(m\ge1\), along all integer
levels,
\[
 \boxed{\quad
 \mathcal C_{m,N}
   =\kappa^m e^{2mcN}
       \left\{\frac{\rho^{m/2}}{1-\rho^m}
                         +O_m(N^{-1/2})\right\}.
 \quad}
 \tag{11}
\]
Thus the limiting rate of the actual cyclic source is \(2mc\).
This statement does not identify that cyclic network with a specified
knot closure.

*Proof.* The
[one-crossing Hilbert--Schmidt theorem](research_one_crossing_gaussian_window.md),
Sections 4--5, supplies unitary diagonal gauges \(U_N,V_N\), a unit
scalar, and isometric step-function embeddings of the input and
output color spaces into \(L^2(\mathbb R)\). Under these embeddings,
the normalized matrix \(e^{-Nc}U_NMV_N\) becomes an operator \(K_N\)
such that
\[
 \|K_N-K\|_{\mathrm{HS}}=O(N^{-1/2}),\qquad
 K(X,Y)=3^{-1/4}
       e^{-\beta(X^2+Y^2)+(\beta+i\pi)XY},\qquad
 \beta=\frac{\pi}{\sqrt3}.
 \tag{12}
\]
The zero extension away from the finite embedded subspaces is part
of this statement. The nonzero spectrum of \(K_N^*K_N\) is exactly
that of \(e^{-2Nc}H\). Moreover,
\[
 \|K_N^*K_N-K^*K\|_1
 \le(\|K_N\|_{\mathrm{HS}}+\|K\|_{\mathrm{HS}})
                         \|K_N-K\|_{\mathrm{HS}}
 =O(N^{-1/2}).
 \tag{13}
\]
Here \(\|\cdot\|_1\) is trace norm. Both operators have bounded
operator norm. Telescoping their \(m\)-th powers therefore gives
trace-norm error \(O_m(N^{-1/2})\). The eigenvalues of \(K^*K\),
proved by the normalized Hermite generating function in the cited
note, are \(\rho^{r+1/2}\), \(r\ge0\). Consequently
\[
 e^{-2mcN}\operatorname{Tr}(H^m)
   =\operatorname{Tr}((K^*K)^m)+O_m(N^{-1/2})
   =\frac{\rho^{m/2}}{1-\rho^m}+O_m(N^{-1/2}).
 \tag{14}
\]
Combining (9) and (14) proves (11). \(\square\)

This calculation handles the entire cyclic contraction, rather than
subtracting only its leading local endpoint term. The local endpoint
rate \(\log2\) in the
[traced-vertex calculation](research_traced_three_vertex_endpoint.md)
therefore does not multiply by the number of vertices. The cyclic
rate is \(2c=0.6461318944\ldots\) per vertex. There is an exact
calibration to the secondary entropy saddle in that calculation.
With \(X_*=(1+i\sqrt3)/4\), its real entropy satisfies
\[
 H_{\mathrm{ent}}(1/3,1/3)
 =-\mathcal J(1/3)-\frac23\log2+
                         \frac2\pi\Im\operatorname{Li}_2(X_*),
 \qquad
 \log2+H_{\mathrm{ent}}(1/3,1/3)=2c .
 \tag{14a}
\]
Here the notation \(H_{\mathrm{ent}}\) distinguishes that scalar
entropy from the positive matrix \(H\).

For an elementary proof of the second identity, put
\(\Lambda(t)=-\int_0^t\log|2\sin u|\,du\).
The Bloch--Wigner differential in the
[original volume calculation](research_positive_edge_volume_identity.md),
equation (7), and the sine rule show that
\(D(z)=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma)\)
for the angles of the upper-half-plane triangle \((0,1,z)\).
Indeed \(|z|=\sin\beta/\sin\gamma\),
\(|1-z|=\sin\alpha/\sin\gamma\),
\(\arg z=\alpha\), and \(\arg(1-z)=-\beta\); differentiating
both sides gives the same one-form, and both sides tend to zero
at a degenerate triangle with \(0<z<1\).
For \(X_*\) these angles are \(\pi/3,\pi/6,\pi/2\).
The double-angle sine identity gives
\(\Lambda(\pi/6)=3\Lambda(\pi/3)/2\), while
\(\Lambda(\pi/2)=0\). Therefore
\[
 \Im\operatorname{Li}_2(X_*)+\frac{\pi\log2}{6}
   =D(X_*)=\frac52\Lambda(\pi/3)
   =-\frac{5\pi}{2}\mathcal J(1/3).
 \tag{14b}
\]
Substitution proves (14a). This exact entropy calibration does not
identify the cyclic network (8) with a marked three-manifold or
replace the separate logarithmic calibration of its geometric action.

## 3. An actual capped chain with a positive spectral measure

Write \(\phi(f)=\mathbf e_D^T f\) for the original closure in
Newton coordinates and put
\[
 \mathcal Z_{m,N}
 =\phi\!\left(M^3J M^3J\cdots M^3J M^2\mathbf e_0\right)
 \quad(m\ge1).
 \tag{15}
\]
There are \(m\) crossing blocks: \(m-1\) threes followed by a two.
For \(m=1\) the word is just \(M^2\). All displayed turns and the
closing row are literal original operations.

**Theorem 3.** With
\(\mu_{m,N}=\mathbf e_0^*H^m\mathbf e_0\), one has exactly
\[
             \mathcal Z_{m,N}=\kappa^{m-1}\mu_{m,N},
             \qquad \mu_{m,N}>0 .
 \tag{16}
\]
The moments obey
\[
 \mu_{0,N}=1,\qquad \mu_{1,N}=N,\qquad
 \mu_{2,N}=N^2\sum_{j=0}^{D}S_j^{-2},\qquad
 \mu_{m,N}^2\le\mu_{m-1,N}\mu_{m+1,N}.
 \tag{17}
\]
In particular there is no cancellation in this specified capped
source after the explicit unit scalar.

*Proof.* The word in (15) is \(J A^mM^{-1}\). Since
\(\mathbf e_D^TJ=\mathbf e_0^T\) and the first row of \(M^{-1}\)
is \(\kappa^{-1}\mathbf e_0^T\), (4) gives
\[
 \mathcal Z_{m,N}
  =\mathbf e_0^T A^mM^{-1}\mathbf e_0
  =\kappa^{m-1}\mathbf e_0^TH^m\mathbf e_0.
 \tag{18}
\]
Strict positivity follows from \(H>0\).
The first moment equals \(\|M\mathbf e_0\|^2=N\).

For the second moment, (2) and
\(M\mathbf e_D=\kappa\mathbf e_D\) imply
\(MJM\mathbf e_0=\mathbf e_0\). Therefore
\[
 H\mathbf e_0=JM^{-1}JM\mathbf e_0=JM^{-2}\mathbf e_0,\qquad
 (H\mathbf e_0)_j
   =N\,\frac{(-i)^j q^{-j(j-1)/2}}{S_j}
   =N\,\frac{(-q)^j}{(Q;Q)_j},\qquad Q=q^2 .
 \tag{19}
\]
The last equality is the coefficient-conjugate
[exact two-crossing terminal formula](research_two_crossing_terminal_filling.md),
Section 2. Squaring its Euclidean norm proves the third identity
in (17). The last form uses
\((Q;Q)_j=(-i)^j q^{j(j+1)/2}S_j\); it is an explicit finite
\(q\)-exponential input for subsequent powers of \(H\), with no
unknown cap coefficient.

Finally, diagonalize \(H\) unitarily, with positive eigenvalues
\(\lambda_{\ell,N}\) and unit eigenvectors \(u_{\ell,N}\). Then
\[
 \mu_{m,N}=\sum_{\ell=1}^N
        |\langle u_{\ell,N},\mathbf e_0\rangle|^2
                         \lambda_{\ell,N}^m .
 \tag{20}
\]
These weights are nonnegative and sum to one. Cauchy--Schwarz
applied to this finite measure proves log-convexity. \(\square\)

The same positive measure has an exact reciprocal symmetry. Extend
\(\mu_{r,N}\) to negative integers by the invertibility of \(H\).
Then
\[
 JHJ=H^{-1},\qquad
 \mu_{-r,N}=\mu_{r-1,N}\quad(r\ge1).
 \tag{20a}
\]
Indeed \(H^{-1}=M^{-1}\overline H M\) and
\(\overline H^{-1}=MM^*\). The first row of \(M^{-1}\) is
\(\kappa^{-1}\mathbf e_0^T\), while
\(M\mathbf e_0=\kappa\overline H^{-1}\mathbf e_0\), since
\(M^*\mathbf e_0=\kappa^{-1}\mathbf e_0\). Substitution gives
\(\mu_{-r,N}=\mathbf e_0^T\overline H^{\,r-1}\mathbf e_0
=\mu_{r-1,N}\).
If \(w_N(\lambda)\) denotes the total cap weight of the eigenspace
with eigenvalue \(\lambda\), uniqueness of finite moment measures
therefore gives
\[
                    w_N(1/\lambda)=w_N(\lambda)/\lambda .
 \tag{20b}
\]
For this conclusion include the zeroth moment using
\(\mu_{-1,N}=\mu_{0,N}=1\). It concerns source weights, not merely
the reciprocal pairing of the eigenvalues.

**Corollary 4.** For every fixed \(m\ge2\),
\[
 \frac{\mu_{2,N}^{m-1}}{N^{m-2}}
       \le\mu_{m,N}\le\|H\|^{m-2}\mu_{2,N}.
 \tag{21}
\]
Moreover,
\[
 \mu_{2,N}
       =3^{-1/4}N^{3/2}e^{Nc}(1+O(N^{-1})),
 \tag{22}
\]
and hence
\[
 \begin{split}
 (m-1)c
   &\le\liminf_{N\to\infty}N^{-1}\log|\mathcal Z_{m,N}|\\
   &\le\limsup_{N\to\infty}N^{-1}\log|\mathcal Z_{m,N}|
      \le(2m-3)c .
 \end{split}
 \tag{23}
\]
These are lower bounds for the actual capped source, not for a
prepared Gaussian input.
For \(m\ge3\), the
[sharp third-moment seed](research_positive_three_crossing_cap_seed.md)
gives strictly stronger lower rates and improved upper rates than
(23), without assuming a top-eigenvector cap overlap.

*Proof.* Successive moment ratios increase by (17), giving the
lower bound in (21); the upper bound follows pointwise from
\(\lambda^m\le\|H\|^{m-2}\lambda^2\).
For (22), the uniform endpoint estimate
\(\log S_j=N\mathcal J(j/N)+O(\log N)\) makes all indices
outside a fixed neighborhood of \(1/6\) exponentially smaller.
On that neighborhood the regular factorial formula gives
\[
 S_j^{-2}
   =\frac{e^{-2N\mathcal J(j/N)}}{2N\sin(\pi j/N)}
                                  (1+O(N^{-1})).
 \tag{24}
\]
The phase \(-2\mathcal J\) has its unique maximum \(c\) at
\(1/6\), with second derivative \(-2\pi\sqrt3\).
Discrete Laplace summation of (24) gives
\(\sum_jS_j^{-2}=3^{-1/4}N^{-1/2}e^{Nc}(1+O(N^{-1}))\).
This proves (22). The one-crossing norm theorem also gives
\(\|H\|=e^{2Nc}(\sqrt\rho+O(N^{-1/2}))\).
Equations (21)--(22) now imply (23). \(\square\)

The normalized spectral measure in (20) is the remaining concrete
source datum for a sharp fixed-\(m\) rate. The trace-class limit in
Section 2 alone does not control it: for
\(\widehat H_N=e^{-2Nc}H\),
\[
 \mathbf e_0^*\widehat H_N\mathbf e_0=Ne^{-2Nc},\qquad
 \mathbf e_0^*\widehat H_N^2\mathbf e_0
   =3^{-1/4}N^{3/2}e^{-3Nc}(1+O(N^{-1})).
 \tag{25}
\]
The original cap thus has exponentially small weight on every
spectral interval of \(\widehat H_N\) bounded away from zero.
This is why the top Mehler eigenvalue cannot simply be substituted
for the entire fixed-length cap moment. The measure is positive
and exactly specified, so this remaining task is a quantitative
spectral-weight problem rather than a sign-cancellation problem.

## 4. Marked-word comparison and scope

In the original signed continued-fraction convention, the capped
word (15) has slope
\[
 [\underbrace{3,\ldots,3}_{m-1},2]_-
                  =\frac{F_{2m+1}}{F_{2m-1}},
 \tag{26}
\]
where \(F_0=0,F_1=1\) and \(F_{r+1}=F_r+F_{r-1}\).
Indeed, prepending a three sends numerator and denominator
\((p,q)\) to \((3p-q,p)\), giving (26) from \(2/1\).
The complementary slope has the reversed negative continued
fraction \([2,3,\ldots,3]_-\); it does not turn these fixed
threes into large powers.

The case \(m=2\) has slope \(5/2\), the reflected two-crossing
example. Already \(m=3\) has slope \(13/5\), whereas a reflected
even two-block word has absolute numerator \(4k^2+1\). Thus the
marked family does not reduce as a whole to the
[previous reflected-even family](research_reflected_even_kashaev_volume_theorem.md).
The [binary complementary reexpression](research_binary_negative_corridor_positive_reexpression.md)
also supplies no large-power condition for this all-three list.
No knot, hyperbolicity, or volume-conjecture classification is
deduced here from the slope computation.

Theorems 1--3 are identities of the full original matrices at every
level. Theorem 2 controls one actual cyclic network, and Corollary 4
controls a specified original capped family. Neither asserts the
geometric rate for an arbitrary positive path, positivity of a
general free-boundary pairing, or stability of arbitrary short
partial fillings.

## 5. Exact finite normalization check

The focused checker
[check_positive_three_crossing_cycle.py](../experiments/check_positive_three_crossing_cycle.py)
constructs \(M\) by polynomial multiplication in the full original
Newton quotient, independently of (1). It compares (4), the original
capped words (15)--(19), reciprocal moments, shifted cardinal
contractions, and the free-boundary identity (7), including its first
ordinary derivatives. It also checks the exact two-crossing-cap
transport word (33) and its finite moment lower bound.
Both crossing signs and both level parities
are included. The saved
[record](../repro/results/research-positive-three-crossing-cycle.json)
contains the precision and hashes of the script and its project
dependencies. These finite tests check the source normalization;
the operator-limit and Laplace arguments above prove the
asymptotic statements.

## 6. Transporting independently proved source norms through positive blocks

The same positive operator admits caps other than the vector
\(\mathbf e_0\) used in Section 3. This gives a direct lower bound
when the original input and its next crossing already have proved
norm estimates. The inequality is standard moment log-convexity;
the point here is to retain its exact original source and verify
its input estimates independently of the desired output.

Let \(B,C\) be fixed words in the original matrices \(M^{\pm1},J\),
and put \(f=B\mathbf e_0\), \(g=C\mathbf e_0\). Define
\[
 \mathcal P_{m,N}(B,C)
   =\phi\!\left[J B^*M(JM^3)^mM^{-1}C\mathbf e_0\right]
   =\kappa^m f^*H^m g,\qquad m\ge1.
 \tag{27}
\]
This is an original finite word: replace every occurrence of
\(M^*\) in \(B^*\) by \(JM^{-1}J\), and use \(J^*=J\).
The equality follows from \(\phi J=\mathbf e_0^T\) and (4).
It does not replace a signed source by its absolute values.

For a nonzero actual input \(f\), write
\[
 Q_m(f)=f^*H^m f,\quad
 R(f)=\frac{\|Mf\|^2}{\|f\|^2},\quad L=\|H\|.
 \tag{28}
\]
These definitions are at the original finite level.

**Proposition 5.** For every integer \(m\ge1\),
\[
 \boxed{\qquad
 \frac{\|Mf\|^{2m}}{\|f\|^{2m-2}}
          \le Q_m(f)\le L^{m-1}\|Mf\|^2.
 \qquad}
 \tag{29}
\]
For a second actual cap \(g\) and any nonzero scalar \(a\), one
also has
\[
 |f^*H^m g|\ge |a|Q_m(f)
 \left[
 1-\left(\frac{L}{R(f)}\right)^{m/2}
                   \frac{\|g-af\|}{|a|\|f\|}
 \right].
 \tag{30}
\]
The estimate is useful when the bracket is positive; no sign
condition on \(g-af\) is assumed.

*Proof.* The spectral weights
\(|\langle u_\ell,f\rangle|^2/\|f\|^2\) form a probability
measure on the positive eigenvalues of \(H\). Their first moment
is \(R(f)\). Convexity of \(x\mapsto x^m\) proves the lower
bound in (29); the pointwise inequality
\(x^m\le L^{m-1}x\) proves the upper bound. Equivalently, these
are consequences of the moment log-convexity already used in
Section 3.

Write \(g=af+r\). Cauchy--Schwarz in the positive \(H^m\) form
gives
\[
 |f^*H^m g|
   \ge |a|Q_m(f)-Q_m(f)^{1/2}L^{m/2}\|r\|.
 \]
Substitute \(Q_m(f)\ge\|f\|^2R(f)^m\) to obtain (30).
\(\square\)

For equal caps, (27) and (29) are already a lower bound for the
actual source. They require no separate top-eigenvector overlap
or almost-invariance estimate. For different caps, (30) states
a sufficient observation condition in the original norm, with
its full amplification factor retained. Thus it does not conceal
an assumption that a small ordinary relative error survives the
remaining crossings.

### The actual two-crossing input

Take \(f=M^2\mathbf e_0\). The exact two-crossing column in
[the one-crossing calculation](research_one_crossing_gaussian_window.md),
equation (14), gives
\[
                     \|f\|^2=\sum_{j=0}^{D}S_j^2.
 \]
The nonzero factorial profile for the actual next column
\(Mf=M^3\mathbf e_0\) is proved in
[the three-crossing Fourier theorem](research_three_crossing_fourier_packet.md),
equations (3) and (8). Together they give, with the same
\(c=2\mathcal J(5/6)\) as in (10),
\[
 \begin{split}
 \|f\|^2&=
 3^{-1/4}N^{3/2}e^{Nc}\{1+O(N^{-1/2})\},\\
 \|Mf\|^2&=
 2^{-1/2}3^{-1/4}N^{3/2}e^{2Nc}
                                      \{1+O(N^{-1/2})\}.
 \end{split}
 \tag{31}
\]
For the first formula, \(S_j^2\) has its unique entropy maximum
at \(j/N=5/6\), with density \(N\) and quadratic exponent
\(-\pi\sqrt3(j-5N/6)^2/N\). Its lattice sum gives the displayed
constant. For the second formula, the proved column error is
relative \(O(N^{-1})\) in Euclidean norm, and its squared
leading norm is \(N^{-1}\sum_jS_j^4\). The latter Gaussian
sum has density \(N^2\) and twice the quadratic exponent,
giving the additional factor \(2^{-1/2}\).

**Corollary 6.** For this literal original input and every fixed
\(m\ge1\),
\[
 \begin{split}
 Q_m(f)&\ge
 3^{-1/4}2^{-m/2}N^{3/2}e^{(m+1)cN}
                                      \{1-O_m(N^{-1/2})\},\\
 Q_m(f)&\le
 3^{-1/4}2^{-1/2}\rho^{(m-1)/2}N^{3/2}e^{2mcN}
                                      \{1+O_m(N^{-1/2})\}.
 \end{split}
 \tag{32}
\]
Both parities and the full sequence of integer levels are included.

*Proof.* Insert (31) and
\(L=e^{2Nc}\{\sqrt\rho+O(N^{-1/2})\}\) into (29).
All seeds in this calculation were proved for the original
columns before the positive-block transport was considered.
\(\square\)

The corresponding original closing words can be written without
adjoint notation. At \(m=1\),
\[
                Q_1(f)=\phi(M^{-3}JM^3\mathbf e_0).
 \]
For \(m\ge2\), they are
\[
 Q_m(f)=\kappa^{1-m}\,
       \phi\!\left[M^{-3}JM^2(JM^3)^{m-2}JM^4\mathbf e_0\right].
 \tag{33}
\]
To check (33), use \(M^*=JM^{-1}J\), (4), and
\(JMJ=\kappa M^{-1}JM^{-1}\).
More generally \(f=M^r\mathbf e_0\) replaces the two outside
powers in (33) by \(-r-1\) and \(r+2\); for \(m=1\) the
reflected powers are \(\pm(r+1)\).

These are different caps from the moments
\(\mu_m=\mathbf e_0^*H^m\mathbf e_0\) in Section 3 and
[the improved cap-seed calculation](research_positive_three_crossing_cap_seed.md).
Their rates cannot be substituted for those moments. Nor does
(32) identify the geometric rate of (33): it is an independent,
nonzero exponential lower bound for this specified family of
original words. Classifying these closures and identifying their
hyperbolic volumes are separate steps.

Finally, the same example quantifies the limitation of the
stability estimate. Equations (31) give
\[
 R(f)=2^{-1/2}e^{Nc}\{1+O(N^{-1/2})\},\qquad
 \left(\frac{L}{R(f)}\right)^{m/2}
     =(2\rho)^{m/4}e^{mcN/2}\{1+O_m(N^{-1/2})\}.
 \tag{34}
\]
An ordinary relative cap error of order \(N^{-1}\) therefore
does not verify (30) for a fixed positive \(m\). A bound
\(\|g-af\|/(|a|\|f\|)\le e^{-\delta N+o(N)}\) with
\(\delta>mc/2\) does verify it. This is a sufficient condition,
not a necessary one. A sharper estimate in the actual
\(H^m\) form can require less accuracy.

The lower bound does not arise from almost-invariance under
\(H/\|H\|\). For the normalized input in this example its
expectation is \(R(f)/L\), which is exponentially small by (34).
The argument instead uses positivity of the exact observed
quadratic form and the independently proved norm of the next
original crossing.

## 7. The complete open boundary has a different spectral measure

The positive cap measure in (20) cannot be assigned to the open kernel
(7), even when both boundary colors are complete. This is already an
exact finite-level distinction, rather than an asymptotic issue.

At \(N=3\), put \(v=v(-2)=(1,1,0)^T\), \(B=\kappa^{-1}JM^3\), and
\(p_m=v^TB^mv\). The original matrices in (1) give
\[
 \det(\lambda I-B)=(\lambda-1)(\lambda^2-5\lambda+1),\qquad
 \lambda_\pm=\frac{5\pm\sqrt{21}}2,
 \tag{35}
\]
and, for every integer \(m\ge0\),
\[
 e^{-i\pi/6}p_m
 =\left(\frac{\sqrt3}{2}+\frac{5\sqrt7}{14}\right)\lambda_+^m
  +\left(\frac{\sqrt3}{2}-\frac{5\sqrt7}{14}\right)\lambda_-^m-i.
 \tag{36}
\]
For an elementary verification, compute the characteristic polynomial
and the first three moments directly from (1). Both sides of (36) then
satisfy the same third-order recurrence, proving the formula for all
\(m\). The two displayed real coefficients have opposite signs: their
product is \(-1/7\). The weight at the remaining eigenvalue \(1\)
is \(-i\). Uniqueness of the three spectral weights follows from the
Vandermonde determinant, since these eigenvalues are distinct.

Consequently no scalar phase makes all weights of this actual open
source nonnegative. In particular its sequence cannot be substituted
for \(\mu_m\) in the positive cap inequalities. This does not refute
an exponential lower bound or the volume conjecture: the finite source
in (36) is nonzero, and coherent estimates can retain complex weights.
For general levels and boundary colors the missing input remains
control of the actual mixed spectral pairing in (7), including its
boundary normalization; positivity of \(H\) alone does not supply it.

The [focused exact algebra checker](../experiments/check_positive_three_boundary_spectrum.py)
constructs the \(N=3\) original matrix and verifies (35), the initial
moments in (36), and the opposite-sign product. At this same level it
also checks the reciprocal identities and full physical inverse-crossing
jets used in Section 8. Its
[record](../repro/results/research-positive-three-boundary-spectrum.json)
contains no numerical asymptotic inference.

## 8. Reciprocal weights and an upper bound for the whole open source

There is more structure at an odd-level complete endpoint than for
arbitrary vectors in (7), but its weights remain complex. Put
\(B=\kappa^{-1}A\), and let \(P_\lambda\) be its spectral projector
at the positive eigenvalue \(\lambda\). Repeated eigenvalues are
allowed: the projectors are defined by similarity with the orthogonal
spectral projectors \(\Pi_\lambda\) of \(H\). For any boundary colors,
define the actual weights
\[
 c_\lambda(z,w)
 =v(z)^TP_\lambda v(w)
 =v(z)^TM^{-1}\Pi_\lambda Mv(w),\qquad
 p_m(z,w)=\kappa^{-m}v(z)^TA^mv(w)
                   =\sum_\lambda\lambda^m c_\lambda(z,w).
 \tag{37}
\]
They include every coefficient of the original boundary polynomial.

**Proposition 7.** At odd \(N\), set \(v=v(-2)\),
\(\varrho=R(-2)\), and \(d_\lambda=\varrho c_\lambda(-2,-2)\).
Then
\[
 \begin{gathered}
 \varrho^2=\kappa,\qquad
 d_{1/\lambda}=\lambda^{-2}\overline{d_\lambda},\qquad
 \sum_\lambda\lambda^{-1}d_\lambda=1,\\
 \varrho p_m(-2,-2)
 =d_1+\sum_{\lambda>1}
       \left(\lambda^m d_\lambda+
                         \lambda^{-m-2}\overline{d_\lambda}\right),
                \qquad d_1\in\mathbb R.
 \end{gathered}
 \tag{38}
\]
An absent eigenvalue contributes zero. The formula holds for all
integer \(m\), including negative \(m\).

*Proof.* The complete color is the simple physical root at odd levels.
Actual multiplication therefore gives \(v^TM=\varrho v^T\), not an
off-grid eigenvector assertion. At \(N=2j+1\), its original value is
\(\varrho=\kappa(-1)^jq^{j(j+1)}\), whose square is \(\kappa\).
Also
\[
 B^T=B,\qquad J\overline B J=B^{-1},\qquad
 P_{1/\lambda}=J\overline{P_\lambda}J,\qquad
 v^TJP_\lambda=\frac{\varrho^3}{\kappa\lambda}v^TP_\lambda.
 \tag{39}
\]
The last identity uses \(M^3=\kappa JB\). Transpose it and use
\(P_\lambda^T=P_\lambda\), then conjugate the resulting identity for
\(v^TJP_\lambda Jv\). This gives
\(c_{1/\lambda}=\varrho^{-2}\lambda^{-2}\overline{c_\lambda}\),
which is the first weight relation in (38).
Finally the exact identity-kernel normalization is \(v^TJv=1\).
Since \(B^{-1}=\kappa M^{-3}J\),
\(p_{-1}=\kappa\varrho^{-3}=\varrho^{-1}\). This proves the sum
rule. Pair the reciprocal eigenvalues to obtain (38). No spectral
simplicity or sign of the \(\lambda>1\) weights was used. \(\square\)

At even levels \(-2\) is not a physical root. Proposition 7 is
therefore not an all-parity identity obtained by evaluating the
canonical polynomial there. The next source bound instead uses all
physical values and first normals and applies at both parities.

**Proposition 8.** For every fixed \(m\ge1\) and nonnegative integers
\(a,b\), the full original open source
\(S_{m,N}(z,w)=v(z)^TA^mv(w)\) satisfies
\[
 \sup_{z,w\in[-2,2]}
       |\partial_z^a\partial_w^b S_{m,N}(z,w)|
 \le C_{m,a,b}N^{A_{m,a,b}}
          \exp N\{(2m+1)c+M_\infty\},
                   \qquad M_\infty=4G/\pi .
 \tag{40}
\]
For real angles \(u,v\) and arbitrary fixed real heights \(h,k\),
the corresponding complex-color upper bound has exponent
\[
              (2m+1)c+M_\infty+|h|+|k|,
       \qquad z=-2\cos(u+ih),\quad w=-2\cos(v+ik).
 \tag{41}
\]
Both statements hold for the mirrored homogeneous chain as well.

*Proof.* The complete Hermite bounds give
\[
 \|v^{(\epsilon)}(c_a)\|_2
       \le CN^A e^{NM_\infty/2},\qquad
 |(R^{-1})^{(\epsilon)}(c_a)|\le CN^2,
 \tag{42}
\]
where \(\epsilon=0,1\) at a double physical root and only
\(\epsilon=0\) at the odd simple root. For the first estimate, each
low Newton mode has rate at most
\(\max_{0\le x\le1/2}\{J(2x)-4J(x)\}=M_\infty/2\), and the
high modes have polynomial full Hermite norm. These estimates,
including their first normals, are recalled explicitly in
[the terminal factorial bound](research_terminal_powers_qbinomial.md),
equations (18)--(20). Summing the squared component bounds changes
only a power of \(N\).

At these same jets, actual multiplication by the inverse crossing
gives exactly
\[
 (v^TM^{-1})^{(\epsilon)}(c_a)
   =\sum_{j=0}^{\epsilon}{\epsilon\choose j}
       (R^{-1})^{(\epsilon-j)}(c_a)v^{(j)}(c_a)^T.
 \tag{43}
\]
This identity retains the normal forcing at a repeated root. It
does not replace that normal by the value eigenvector equation.
For any physical mixed jet \((\epsilon,\epsilon')\), orthogonality
of the \(H\)-projectors and Cauchy--Schwarz now imply
\[
 \begin{split}
 \sum_\lambda
   |\partial_z^\epsilon\partial_w^{\epsilon'}
                                      c_\lambda(c_a,c_b)|
 &\le\|(v^TM^{-1})^{(\epsilon)}(c_a)\|_2
                          \|Mv^{(\epsilon')}(c_b)\|_2\\
 &\le CN^A\exp N\{c+M_\infty\}.
 \end{split}
 \tag{44}
\]
Here \(\|M\|=O(e^{Nc})\), by the proved one-crossing norm theorem.
Also \(\|H\|=O(e^{2Nc})\). Multiplication of (44) by
\(\|H\|^m\) bounds every required physical mixed jet of the
literal source by the exponent in (40).

Each free boundary variable in \(S_{m,N}\) has degree at most
\(N-1\), independently of the number of selected vertices. Full
Hermite interpolation on the original complete Chebyshev nodes has
polynomial interval norm. One direct construction first interpolates
the distinct-node values, subtracts that interpolant, divides by the
distinct-node polynomial, and interpolates the remaining first-normal
data. Its node derivatives have a polynomial lower bound; at odd
levels the second interpolation omits the simple root \(-2\).
The exact construction and bounds are recalled in
[the finite-wire estimate](research_degree_three_zero_wire_tails.md),
Section 3. Apply this in each boundary variable. It proves (40) for
\(a=b=0\) without discarding any normal or changing the polynomial.
Markov's inequality gives every fixed ordinary derivative at polynomial
cost. Finally Bernstein--Walsh on \([-2,2]\), whose angular ellipse
parameter is \(e^{|h|}\), gives (41) in each variable. Coefficient
conjugation proves the mirror statement. \(\square\)

Equations (37), (38), and (44) provide a controlled oscillatory spectral
sum for the actual open boundary source. Proposition 8 improves the
direct similarity norm estimate by one factor \(e^{Nc}\), using the
physical eigenfunctional and its full normals. It supplies neither
the sharp geometric rate nor a lower coefficient for a general
homogeneous-three chain. In particular no whole-period angular loss
at that geometric rate, or admissibility under further composition,
is inferred from this upper bound.
