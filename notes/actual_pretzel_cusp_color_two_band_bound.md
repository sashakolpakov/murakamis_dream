# An exact cusp-color split with a controlled original normal-source remainder

29 October 2026. For every \(j=N-r\) with
\(0\leq r\leq\lfloor(N-1)/2\rfloor\), the literal rotated pretzel
circle box has a positive half-degree core plus an ORIGINAL crossing
times a degree-\(r-1\) polynomial. The entire second band, including
every Casimir normal jet, has norm at most \(56^r\) in a faithful
source-compatible Hermite norm. Thus it costs \(\exp(O(\delta N))\)
on a fixed cusp-color corridor \(r\leq\delta N\), and subexponentially
when \(r=o(N)\). No term is deleted.

This is not yet a geometric survival theorem. The low core still
requires its selected asymptotic analysis; estimates of a remainder
do not prove that the whole original coefficient is nonzero.

## 1. The entire rotated polynomial, with its two support bands

Use the original conventions and actual rotation \(\mathscr R\) of
[the complete-base polynomial theorem](actual_pretzel_complete_base_casimir_polynomial.md).
Let \(f_v\) be the physical middle-degree continuant polynomials,
\(s_a=|(Q;Q)_a|\), \(M=\lfloor d/2\rfloor\), \(d=N-1\).
Then

\[
 \mathscr R(R^{-1}L_{N-r})=z_{N,r}(\Omega),\qquad
 z_{N,r}(z)=\kappa^{-1}\sum_{v=0}^d a_{r,v}f_v(z),
\]
\[
 \boxed{\quad a_{r,v}=s_{d-v}^2q^{r^2-v^2}
                      {2v\brack v-r}_Q.\quad}         \tag{1}
\]

The Gaussian coefficient is its finite polynomial, not an invalid
factorial ratio at a root. A negative lower index gives zero. For
the displayed cusp corridor its support and all phases are exactly

\[
 a_{r,v}=\frac{s_{d-v}^2s_{2v}}{s_{v-r}s_{v+r}}>0,
                   \quad r\leq v\leq M,              \tag{2}
\]
\[
 a_{r,N-t}=(-1)^{N-t-r}
       \frac{s_{t-1}^2s_{t+r-1}}{s_{2t-1}s_{r-t}},
                   \quad 1\leq t\leq r,              \tag{3}
\]

and it is zero elsewhere. In particular the middle band is exactly
zero. For \(r=0\), (2) is the positive complete-base coefficient
\(b_v=N^2s_{2v}/s_v^4\), and there is no upper band.

Proof by a finite resolvent, not a semiclassical approximation.
In the low block of degree \(K=d-v\), the first-to-last entry of
\((I-tJ_K+t^2I)^{-1}\) is

\[
 \frac{t^K B_K}{\prod_{k=0}^K(1-q^{2k+1}t)(1-q^{-2k-1}t)},
       \qquad B_K=(-1)^Ks_K^2.
\]

Its \(t^{j-1}\) coefficient is the first-to-last entry of
\(U_{j-1}(J_K/2)\). The full two-copy root orbit factors the inverse
denominator as

\[
 \frac{(q^{1-2v}t;Q)_{2v}}{(1+t^N)^2}.
\]

The needed remaining coefficient has degree \(v-r<N\), so the
denominator contributes exactly 1. The finite q-binomial theorem,
the original circle sign \((-1)^{j-1}\), and the literal \(R^{-1}\)
last-row coefficient give precisely (1). This derivation retains
both the actual pivotal circle normalization and its half twist.

If \(2v<N\), the Gaussian phase in (1) cancels, giving (2).
If \(2v\geq N\) and \(v-r<N\), split one whole root orbit from
the finite q-binomial product. Its factor has no coefficient in
degrees \(1,\ldots,N-1\). Thus
\({2v\brack v-r}_Q={2v-N\brack v-r}_Q\), which is zero unless
\(v+r\geq N\). Taking its explicit phase and complementing the
remaining sine factorials gives (3). This proves the exact bands
without division by a vanished factorial.

## 2. The upper band is an original crossing times a SHORT polynomial

Let \(\bar f_l\) mean coefficient conjugation at the specified
principal root. Reversing the physical Jacobi recurrence gives

\[
 f_{d-l}(\Omega)=f_d(\Omega)\bar f_l(\Omega),
       \qquad f_d(\Omega)=x^d r_N(\Omega).
\]

Indeed \(e_0^Tf_d(A)=e_d^T\) and
\(e_d^T\bar f_l(A)=e_{d-l}^T\); the cyclic first row proves the
polynomial identity modulo the FULL \(\mathcal P_N\), including
every double root. Since \(x^d=\kappa^2\), define

\[
 c_{N,r}(z)=\kappa^{-1}\sum_{v=r}^M a_{r,v}f_v(z),
\quad
 P_{N,r}(z)=\sum_{t=1}^r(-1)^{N-t-r}
       \frac{s_{t-1}^2s_{t+r-1}}{s_{2t-1}s_{r-t}}
                                           \bar f_{t-1}(z).
\]

The exact ALL-INPUT identity is

\[
 \boxed{\quad z_{N,r}(\Omega)=c_{N,r}(\Omega)
                                     +R P_{N,r}(\Omega).\quad} \tag{4}
\]

For \(r=1\) its remainder is \((-1)^N R\). Thus the short sector
is not identically zero, and it cannot be removed by restricting
to the original cup or by retaining only the complete-circle quotient.

## 3. Uniform quantitative bound WITH every original normal jet

On \(\mathbb C[z]/(\mathcal P_N)\) use the faithful Hermite norm

\[
 \|f\|_{\mathrm H}=
 \max\left\{\max_{c\ \mathrm{double}}
                   (|f(c)|+N^{-2}|f'(c)|),\quad
              |f(-2)|\ \mathrm{if\ }N\mathrm{\ is\ odd}\right\}. \tag{5}
\]

It includes values and ALL first-normal coefficients; the simple
node has only its value. It is submultiplicative. The literal
crossing has \(\|R\|_{\mathrm H}\leq9/8\), by its original unit
nodal values and \(|r_N'/r_N|\leq N^2/8\). The original source has

\[
 |\Phi_2(f)|\leq3N^3\|f\|_{\mathrm H}.                \tag{6}
\]

This follows immediately from the exact source values and derivatives
in the complete-base theorem. In particular this norm does not
discard the nilpotent source as an ordinary semisimple quotient would.

There is a constant independent of \(N,r\), explicitly

\[
 \boxed{\quad \|R P_{N,r}\|_{\mathrm H}\leq56^r,
                   \qquad 1\leq r\leq M.\quad}        \tag{7}
\]

Here is a direct proof of the bound, including the cancellation of
small factorial denominators. Write the MONIC physical continuant
as \(p_l=(a_0\cdots a_{l-1})f_l\), so
\(|a_0\cdots a_{l-1}|=s_l^2\). On \(|z|\leq2\), its recurrence
has \(|z-D_l|\leq12\) and \(|a_{l-1}^2|\leq16\). Induction gives

\[
 |p_l(z)|\leq14^l,\qquad |p_l'(z)|\leq l14^{l-1}.
\]

The coefficient in (3) divided by \(s_{t-1}^2\) has magnitude

\[
 \frac{s_{t+r-1}}{s_{2t-1}s_{r-t}}
       =\left|{t+r-1\brack 2t-1}_Q\right|
       \leq {t+r-1\choose 2t-1}\leq4^r.
\]

The first inequality follows from the nonnegative integer
coefficients of the finite Gaussian polynomial (or its elementary
Pascal induction), since its argument has modulus one. Therefore
the \(s_{t-1}^2\) CANCELS the full denominator of \(\bar f_{t-1}\)
before estimating any normal derivative. Summing the geometric
series in \(14^{t-1}\), and multiplying by \(9/8\), proves (7)
with room to spare. No \(N^{O(r)}\) loss occurs.

There is also a full physical operator bound

\[
 \|P_{N,r}(\Omega)\|_{\rm op}\leq120^r,
 \qquad \|R P_{N,r}(\Omega)\|_{\rm op}
                                  \leq120^r\|R\|_{\rm op}. \tag{8}
\]

Indeed every physical \(\Omega\) block has norm at most18; the same
monic recurrence is bounded by \(30^l\) when evaluated at this
operator. The preceding factorial cancellation proves (8).
The factor \(\|R\|\) cannot be discarded: already \(r=1\) the
remainder is the whole original crossing. Thus (7), which is the
faithful normal-source bound needed here, is stronger than a claim
of uniform physical contraction would be and has a different scope.

## 4. Exact simultaneous original-source error accounting

For arbitrary fixed \(s\), substitute (4) at every augmented pretzel
box BEFORE applying the original source. The difference between the
complete mixed-color period and its low-core product is exactly the
sum over nonempty subsets of the retained remainder boxes. Equations
(5)--(7) give the explicit bound, with \(\epsilon_0=0\) and
\(\epsilon_r=56^r\) for \(r\geq1\),

\[
 \left|\Phi_2\left(\prod_i z_{N,r_i}
                              -\prod_i c_{N,r_i}\right)\right|
 \leq3N^3\sum_{\varnothing\ne S\subset\{1,\ldots,s\}}
      \prod_{i\in S}\epsilon_{r_i}
      \prod_{i\notin S}\|c_{N,r_i}\|_{\mathrm H}.       \tag{9}
\]

For \(r_i\leq\delta N\) the individual retained source remainders
have rate at most \(\delta\log56\); for \(r_i=o(N)\) that rate is
zero. This is an independently quantified actual source term.
It does not make the TOTAL right side negligible relative to the
geometric period without estimates of the coherent core and its
selected action gap. No open-corridor noncancellation or long-filling
survival is asserted from (9) alone.
