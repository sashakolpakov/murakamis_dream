# Uniform real Gaussian tails for the actual binomial-cut source

Private written proof, 18 November 2026.

The exact two-mode presentation of the binomial cut has uniformly
negligible large real radii. For a fixed finite braid, any prescribed
negative absolute exponential rate can be obtained by choosing one
fixed radius after the natural square-root rescaling. This remains
true on a meridian disk of radius proportional to \(N^{-1}\), with
every fixed meridian normal retained.

This is a bound on the original real Gaussian integral. It does not
control a deformed complex contour, the finite-radius compact part,
or the coefficient of a coherent stationary branch. The proof uses
the exact finite head, including both occupation walls and its actual
pivots. The complete directs are G, the two-mode source; B, the
literal balanced crossing; and D, the full modified-dimension
normalization. Their pins are recorded below.

## 1. Source and statement

Fix a finite braid word with one cut head and the original pivotal
closure of all other heads. The braid width and word length are
fixed independently of \(N\). Put
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\quad Q=q^2,\quad
                         x=-M/q.
 \tag{1}
\]
Use the balanced finite basis \(e_0,\ldots,e_d\), the literal
signed crossings, their prescribed scalar framing, and G's
binomial cut. Finitely many diagonal clock marks
\(e^{tJ}\), \(Je_a=ae_a\), with \(t\) in a fixed compact set,
may remain anywhere in the word. Fixed products of the actual
finite generators or fixed polynomials in \(J\) are also allowed.
The conclusion is not stated for arbitrary unspecified
level-dependent coupon matrices.
Both the reduced cut scalar and the convention retaining its
full external modified-dimension line are covered: that line
is kept as a whole function and bounded explicitly below.

Resolve this finite contraction by G's Gaussian kernels. Let
\(E\) be the number of integrated head segments in the chosen
resolution; it is fixed with the diagram. On each segment use
\[
 d\gamma(Z)=\pi^{-2}e^{-\|Z\|^2}\,d^4Z,\qquad Z\in\mathbb C^2.
\]
The cut is the latitude
\(Z_d(v)=\sqrt{d/2}(1,v)\), \(|v|=1\), with its exact outside
factor \(A_de^{-d}\), \(A_d=e^dd!/d^d\).
Write \(Z_e=\sqrt d\,z_e\) on the integrated segments.

Let \(\mathcal T_{N,R}\) denote the part of this same integral
where at least one \(\|z_e\|\ge R\). Its absolute integral means
the integral of the absolute value of the entire resolved
integrand, including every original scalar and measure. If
\(E=0\), set this tail equal to zero.

**Theorem.** Fix \(0<\rho<1/8\) and the compact clock sets.
There is \(C\), depending only on these data and the finite
diagram, such that for \(E\ge1\),
\[
 \sup_{|M-1|\le2\rho/N}
       \int_{\max_e\|z_e\|\ge R}|\text{actual integrand}|
 \le
 4E\,N^E
       \exp\!\left(CN+d\left(\log2-\frac{R^2}{2}\right)\right).
 \tag{2}
\]
For every fixed \(j\), the same absolute integral with \(j\)
meridian derivatives of the integrand, on
\(|M-1|\le\rho/N\), is bounded by the right side of (2)
times \(j!(N/\rho)^j\).

Consequently, for every \(\Lambda>0\) and fixed finite number
of these normals, one may choose \(R<\infty\), independently
of \(N\), so that all these tails are \(O(e^{-\Lambda N})\).
The estimate is absolute; it does not presume that the full
invariant is nonzero or compare the tail to its unknown value.

## 2. An elementary bound for every root factorial

Set
\[
 S_n=\prod_{k=1}^n2\sin(\pi k/N),\qquad 0\le n<N,\quad S_0=1.
\]
Then
\[
                         e^{-N}\le S_n\le2^N.
 \tag{3}
\]
For \(n\le N/2\), concavity of sine on \([0,\pi/2]\) gives
\(2\sin(\pi k/N)\ge4k/N\). For \(n\ge1\),
\(\log(n!)\ge\int_1^n\log t\,dt\ge n\log n-n\).
Therefore
\[
 S_n\ge(4/N)^n n!
       \ge\exp\{n\log(4n/N)-n\}\ge e^{-N/4}.
 \tag{4}
\]
The last inequality follows by minimizing
\(y\log(4y)-y\) for \(y\ge0\), whose minimum is \(-1/4\).
The empty product causes no exception.

Differentiating \(z^N-1\) at \(z=1\) and taking absolute
values yields \(S_{N-1}=N\). Reflection of the sine factors
then gives
\[
                         S_n S_{N-1-n}=N.
 \tag{5}
\]
For \(n>N/2\), the elementary upper bound on the complementary
product implies \(S_n\ge N2^{-N/2}\ge e^{-N}\).
This proves (3), including both level parities and \(N=2\).
No asymptotic factorial formula is used.

In particular, every Gaussian coefficient with
\(0\le b\le a<N\) satisfies
\[
 \left|{a\brack b}_{Q}\right|
       =\frac{S_a}{S_bS_{a-b}}\le e^{(2+\log2)N}.
 \tag{6}
\]
Every denominator here is an actual nonzero root factorial.
No unreduced quotient at a length \(N\) is evaluated.

## 3. Literal balanced local matrices have exponential norm bounds

For clarity, the coefficient convention matters. B's balanced
uncheck crossing is \(D R_0\), where
\[
 D e_{a,b}=x^{-a-b}Q^{ab}e_{a,b},\qquad
 R_0=\sum_{n=0}^{d}
       \frac{(-1)^nq^{n^2}}{(Q;Q)_n}
                         \mathcal E_1^n F_2^n .
 \tag{7}
\]
The common Cartan scalar is still retained on its prescribed
external line. The actual finite generators are
\[
 \mathcal E e_a=(MQ^{-a}-M^{-1})e_{a-1}\quad(a>0),
 \qquad
 F e_b=(1-Q^{b+1})e_{b+1}\quad(b<d),
 \tag{8}
\]
with their zero extreme rows. The supported coefficient of
\(R_0\) from \((a,b)\) to \((a-n,b+n)\) is
\[
 (-1)^nq^{n^2}{b+n\brack n}_Q
             \prod_{j=a-n+1}^{a}(MQ^{-j}-M^{-1}),
 \quad 0\le n\le\min(a,d-b).
 \tag{9}
\]
This follows by canceling the finite \(F\)-product against
\((Q;Q)_n\), or directly from B. It is the balanced-head
formula; an unbalanced formula with \({a\brack n}_Q\)
must not be substituted without its basis adapter.

The inverse uncheck crossing is
\[
 R_0^{-1}D^{-1},\qquad
 R_0^{-1}=\sum_{n=0}^{d}
            \frac{q^n}{(Q;Q)_n}\mathcal E_1^nF_2^n .
 \tag{10}
\]
Thus its supported entries have the same absolute product
bound as (9). The checked signs also include the original
exchange; this does not change the entry bound or the equal
head metric. Both walls in (8) are essential for the finite
support and remain in (7)--(10).

On \(|M-1|\le2\rho/N\), both \(M\) and \(M^{-1}\) are
bounded uniformly, so the product in (9) is at most \(C_0^N\).
The factors \(x^{\pm(a+b)}\) in \(D^{\pm1}\) are uniformly
bounded since \(|\log M|\le C\rho/N\), while \(Q^{ab}\)
has modulus one. Equations (6), (9), (10) therefore bound
every signed entry by \(e^{C_1N}\).

There is no discarded scalar normalization here. On the
original marked logarithm let
\[
 H=d+\frac{\log M}{\log q},\qquad
                 \kappa=\exp((\log q)H^2/2).
 \tag{11}
\]
Then \(q^H=x\), \(H-d=O(\rho)\), and the common Cartan
scalar \(\kappa\), its inverse, and any fixed framing powers
are bounded by constants on this disk. The remaining prescribed
framing and diagonal pivot entries are root phases times
meridian monomials whose exponents are \(O(N)\); they too
have uniformly bounded modulus on this disk. Clock marks
cost at most \(e^{C_2N}\) on the stated compact sets. Fixed
generator words and polynomial index insertions cost only
an additional \(e^{C_3N}\); this bound also allows their fixed
powers of \(q-q^{-1}\) in denominators.

The external modified-dimension line mentioned in B is not
silently removed. In D's exact convention it is
\[
 d_N(M)=\eta_N\frac{M^{N-1}}{\sum_{r=0}^{N-1}M^{2r}},
                         \qquad \eta_N=i^{N+3}.
 \tag{11a}
\]
On the full disk \(|M-1|\le2\rho/N\), with \(\rho<1/8\),
the logarithm continued from one obeys
\[
 |\log M|\le\frac{2\rho}{N(1-\rho)},\qquad
 |M^{2r}-1|\le
       \exp\!\left(\frac{4\rho}{1-\rho}\right)-1
                  <e^{4/7}-1<1.
\]
Thus the whole denominator in (11a) has modulus at least
\(N(2-e^{4/7})\), and its numerator has modulus at most
\(e^{2/7}\). In particular
\[
 |d_N(M)|\le
       \frac{e^{2/7}}{N(2-e^{4/7})}.
 \tag{11b}
\]
The apparent ratio of two vanishing meridian factors has
therefore been evaluated as its holomorphic whole germ,
with \(d_N(1)=\eta_N/N\). It has no pole on this disk.
Retaining it in the integrand preserves the claimed bound
after changing \(C\). Conversely
\(|d_N(M)^{-1}|\le Ne^{6/7}\), by bounding the denominator
above and the numerator below in the same way. Thus a
prescribed conversion back to the reduced scalar also
has only polynomial cost. Neither normalization is changed
in the actual integral. These scalar derivatives are included
in the same Cauchy argument in Section 5.

Give each head the exact coherent metric
\[
                  G_{aa}=\binom da^{-1}.
 \tag{12}
\]
On \(r\) heads its diagonal condition ratio is at most
\(2^{rd}\). The orthonormal-coordinate entry of a matrix
is therefore at most \(2^{rd/2}\) times its original entry.
The elementary bound of an \(N^r\) square matrix norm by
\(N^r\) times its maximum entry proves, for every local
coupon \(A\) just specified,
\[
                             \|A\|_{G^{\otimes r}}\le e^{C_AN}.
 \tag{13}
\]
All widths and the number of coupons are fixed. Hence the
product of these local norms, including scalar lines, is
at most \(e^{CN}\). No assertion of unitarity is used.

## 4. Kernel Cauchy--Schwarz and the exact radial measure

G's kernel for a one-head map obeys
\[
 |\mathcal K_A(Z,\overline W)|
 \le \|A\|_G\,
      \frac{\|Z\|^d\|W\|^d}{d!}.
 \tag{14}
\]
Indeed the squared norm of the evaluation vector at \(Z\)
is the diagonal reproducing kernel
\(\Pi_d(Z,\overline Z)=\|Z\|^{2d}/d!\).
Cauchy--Schwarz for \(A\) gives (14). On several heads,
the bound is the product of the corresponding evaluation
norms and the actual tensor-operator norm.

In the exact resolved network, every integrated segment
has one incoming and one outgoing half-edge. Applying (14)
at every coupon therefore leaves precisely the measure
\[
                  d\mu_d(Z)=\frac{\|Z\|^{2d}}{d!}\,d\gamma(Z)
 \tag{15}
\]
on that segment. At the cut the two boundary factors cancel
the entire soft-cut normalization:
\[
                  A_de^{-d}\frac{\|Z_d(v)\|^{2d}}{d!}
                           =A_de^{-d}\frac{d^d}{d!}=1.
 \tag{16}
\]
The normalized angular measure has mass one. This cancellation
holds before any tail estimate, with no unknown scalar used.

In the radial variable \(t=\|Z\|^2\), the Gaussian measure
has density \(e^{-t}t\,dt\) after normalized sphere integration.
Thus
\[
 \mu_d(\mathbb C^2)=\frac{(d+1)!}{d!}=N,\qquad
 \frac{d\mu_d}{N}
       =\frac{e^{-t}t^{d+1}}{(d+1)!}\,dt\,d\sigma .
 \tag{17}
\]
Every factorial integral in (17) follows by repeated
integration by parts. Scaling that integral shows that
the normalized measure has
\(\mathbb E e^{t/2}=2^{d+2}\). On \(t\ge dR^2\),
exponential Markov inequality consequently gives
\[
 \mu_d\{\|Z\|\ge R\sqrt d\}
 \le N\,2^{d+2}e^{-dR^2/2}
       =4N\exp\!\left(d\left(\log2-\frac{R^2}{2}\right)\right).
 \tag{18}
\]
Combining (13)--(18), integrating the other \(E-1\) segments
with mass \(N\), and taking the union over the \(E\) possible
large segments proves (2). The shared physical restrictions
are still in the local matrices; no independent transfer
cutoff has replaced them.

## 5. Normals, radius choice and scope

For each fixed field configuration the full finite integrand
is holomorphic in \(M\) on the larger disk used above. A
Cauchy circle of radius \(\rho/N\), centered anywhere in
\(|M-1|\le\rho/N\), stays in that larger disk. Cauchy's
formula bounds its \(j\)-th derivative by
\(j!(N/\rho)^j\) times the same pointwise majorant. The
positive majorant is integrable on the whole real contour,
so integration proves the asserted derivative-tail bound.
This retains derivatives of all scalar, pivot and wall
factors. Fixed clock derivatives may similarly be taken
on a slightly larger compact marking domain.

Since \(d\ge N/2\), the negative term in (2) can dominate
any fixed \(CN\), every \(E\log N\), and the fixed derivative
powers by increasing one \(R\). This proves the stated
arbitrary absolute exponential rate, with constants adjusted
for the finitely many small levels if necessary.

The compact region \(\max\|z_e\|\le R\) is still the full
coupled finite source. Its local kernels can have exponential
growth, oscillation and cancellation. This theorem gives
no coherent phase or amplitude estimate on that region,
and no lower bound for its integral. In particular the
regular five-shape midpoint chart does not by itself select
a stationary branch of a coherent crossing sum.

The proof also gives no tail bound for a complexly deformed
Gaussian cycle: its positivity and radial estimate refer
to the original real Gaussian measures. No stratum or
occupation endpoint inside the compact region is deleted.
The finite Borel cutoff/coarea currents belong to a different
presentation until an actual comparison map is proved.

## Complete proof-source pins

* G: notes/research_soft_cut_two_mode_gaussian_source.md,
  SHA256 1f95717e33e0fdcfe6b1cd453a02b4e5e63d83ed578df761a5c8bdd07e990c19.
* B: notes/balanced_verma_coherent_braiding.md,
  SHA256 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4.
* D: notes/factorial_source_torsor.md,
  SHA256 2a46e6454aa3a08911c8266fcfdcc7159714369df3518950265fe76ef3acfccf.

G supplies the exact finite Gaussian network, its head metric,
projector and source-preserving binomial closing. B supplies
the literal balanced signed coefficients, common Cartan line
and finite generator/wall conventions. D supplies only the
exact full modified-dimension normalization (11a). The factorial bounds,
local norm estimate and complete real-tail argument are proved
above. Only written mathematics and text/hash operations were
used; frozen sources and public files are unchanged.
