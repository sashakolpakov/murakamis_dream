# One positive coefficient for any fixed number of physical rows

Private written proof, 17 November 2026.

The original trace of a product of physical value rows has an exact
one-variable coefficient representation. Its generating function is
a product of linear factors and reciprocal linear factors, all with
positive coefficients. Exponential tilting therefore turns the trace
into the probability that a sum of Bernoulli and geometric random
variables equals a prescribed integer.

This representation gives a uniform nonzero leading coefficient for
any fixed number of rows, including rows at the midpoint. It also
evaluates every fixed-degree polynomial inserted into that trace.
It does not estimate a crossing power or an inserted boundary
derivative: their degrees or coefficients depend on the level.

## 1. Exact coefficient representation

Let \(N\ge3\), \(D=N-1\), \(J=\lfloor D/2\rfloor\), and put
\[
 c_a=2\cos((2a+1)\pi/N),\qquad
 P_N(C)=2T_N(C/2)+2,\qquad \eta=(-1)^D.
\]
Here \(T_N\) is the Chebyshev polynomial, so \(P_N\) is monic
of degree \(N\). The indices \(a=0,\ldots,N-1\) list its roots
with their full multiplicities. Define
\[
 d_a=c_0-c_a\ge0,\qquad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
The trace is applied to the canonical remainder even when the
ordinary degree of \(f\) is larger than \(D\).

The physical row \(F_j(C)=K_N(c_j,C)\), \(0\le j\le J\),
has ordinary degree \(j\) and \(F_j(c_0)=1\). The positive Jacobi
recurrence in the first direct source realizes it as
\[
 F_j(C)=\frac{\det(\mathcal J_j-CI)}
                    {\prod_{r=0}^{j-1}A_r},\qquad
 \mathcal J_j>c_0I.
 \tag{2}
\]
Let \(r_{j,1},\ldots,r_{j,j}>0\) be the eigenvalues of
\(\mathcal J_j-c_0I\), with multiplicity. Since \(F_j(c_0)=1\),
\[
 F_j(c_0-z)=\prod_{b=1}^{j}(1+z/r_{j,b}).
 \tag{3}
\]
An empty product is one, so (3) also covers \(j=0\).

Fix \(m\) physical indices \(j_1,\ldots,j_m\). Set
\[
 s=\sum_i j_i,\qquad k=s-D,\qquad
 a_{\mathbf j}=\prod_{i=1}^{m}\prod_{b=1}^{j_i}r_{j_i,b}^{-1},
\]
\[
 H_{\mathbf j,N}(x)=
 \frac{\displaystyle\prod_{i=1}^{m}\prod_{b=1}^{j_i}
                       (1+r_{j_i,b}x)}
      {\displaystyle\prod_{a=0}^{N-1}(1-d_ax)} .
 \tag{4}
\]
All Taylor coefficients of \(H\) are positive. For \(N\ge3\)
at least one \(d_a\) is positive, so every nonnegative coefficient
is strictly positive.

**Proposition 1.** With the convention that a negative Taylor
coefficient is zero,
\[
 \Gamma_{\mathbf j}^{(m)}
 :=\phi_N\!\left(\prod_{i=1}^{m}F_{j_i}\right)
 =N^2a_{\mathbf j}[x^k]H_{\mathbf j,N}(x).
 \tag{5}
\]
Consequently this trace is positive exactly when \(s\ge D\).
When \(s=D\), its exact value is \(N^2a_{\mathbf j}\).

**Proof.** Polynomial division gives
\[
 [C^D]\operatorname{rem}_{P_N}f=[C^{-1}]\,f(C)/P_N(C),
 \tag{6}
\]
where the right side is the Laurent coefficient at infinity.
The polynomial quotient contributes no \(C^{-1}\) term.
The substitution \(C=c_0-z\) changes that coefficient's sign.
Also
\[
 P_N(c_0-z)=(-1)^N\prod_a(z-d_a).
\]
The two signs and \(\eta=(-1)^{N-1}\) cancel. By (3),
the required coefficient is therefore \(N^2a_{\mathbf j}\)
times the coefficient of \(z^{-1}\) in
\[
 z^{s-N}
 \frac{\prod_{i,b}(1+r_{j_i,b}/z)}
      {\prod_a(1-d_a/z)}.
\]
Putting \(x=1/z\) proves (5). This calculation retains every
double root of \(P_N\); it has not replaced the trace by a
sum of values at distinct roots. \(\square\)

## 2. The exact probability distribution

Suppose \(k>0\), and write \(d_{\max}=\max_a d_a\).
For \(0<\rho<d_{\max}^{-1}\), take mutually independent random
variables as follows:

* one Bernoulli variable for each \(r=r_{j_i,b}\), with success
  probability \(v_r=\rho r/(1+\rho r)\);
* one geometric variable for each \(d=d_a\), with probabilities
  \(\mathbb P(Y_d=n)=(1-u_d)u_d^n\), \(n\ge0\), where
  \(u_d=\rho d\). A factor with \(d=0\) gives the zero variable.

Let \(S_\rho\) be their sum. Its probability generating function is
\[
 \mathbb E z^{S_\rho}=\frac{H(\rho z)}{H(\rho)}.
 \tag{7}
\]
Its mean and variance are
\[
 \mu_N(\rho)=\sum_r\frac{\rho r}{1+\rho r}
                    +\sum_a\frac{\rho d_a}{1-\rho d_a},
\]
\[
 V_N(\rho)=\sum_r\frac{\rho r}{(1+\rho r)^2}
                    +\sum_a\frac{\rho d_a}{(1-\rho d_a)^2}
              =\rho\mu_N'(\rho).
 \tag{8}
\]
The mean is strictly increasing from zero to infinity. Thus
there is exactly one \(\rho=\rho_{\mathbf j,N}\) satisfying
\[
                         \mu_N(\rho)=k.
 \tag{9}
\]
Equations (5) and (7) give the exact identity
\[
 \Gamma_{\mathbf j}^{(m)}
   =N^2a_{\mathbf j}H(\rho)\rho^{-k}
                         \mathbb P(S_\rho=k).
 \tag{10}
\]
In particular the saddle in (9) is selected by the original
finite source, without a choice of logarithmic branch.

## 3. Uniform control up to the midpoint

Fix \(m\ge3\) and \(\varepsilon>0\). Consider every physical
tuple with
\[
                       \sum_i j_i-D\ge\varepsilon N.
 \tag{11}
\]
There are constants \(0<a<b<1/4\) and \(0<c<C<\infty\),
depending only on \(m,\varepsilon\), such that, for all
sufficiently large \(N\),
\[
             a\le\rho_{\mathbf j,N}\le b,\qquad
             cN\le V_N(\rho_{\mathbf j,N})\le CN .
 \tag{12}
\]
No bound keeping \(j_i/N\) away from \(1/2\) is needed.

To prove the lower bound on \(\rho\), first control the number
of large Jacobi eigenvalues. For each fixed
\(0<\delta<1/2\), the coefficients
\[
 A_r=\frac{(2\sin((r+1)\pi/N))^4}
           {2\sin((2r+1)\pi/N)\,2\sin((2r+2)\pi/N)},\qquad
 C_r=\frac{(2\sin(r\pi/N))^4}
           {2\sin(2r\pi/N)\,2\sin((2r+1)\pi/N)}
 \tag{13}
\]
are uniformly bounded for \(r\le(1/2-\delta)N\), with
\(C_0=0\). For small arguments this follows from
\(\sin t\asymp t\); elsewhere the displayed denominators
stay away from their upper endpoint zero. The diagonal of
\(\mathcal J_j-c_0I\) is \(A_r+C_r\), and its off-diagonal
entries are \(-\sqrt{A_rC_{r+1}}\).

Delete the last at most \(\delta N+2\) rows and columns of
this matrix. The remaining principal matrix has norm at
most a constant \(R_\delta\), by the bound on its row sums.
Eigenvalue interlacing therefore implies that at most
\(\delta N+2\) of its original eigenvalues exceed
\(R_\delta\). The same statement is immediate if \(j\)
was already below the cutoff.

Since \(d_a<4\), the mean in (8), for \(0<\rho<1/4\), is at most
\[
 \mu_N(\rho)
 \le m(\delta N+2)+\frac{mN}{2}R_\delta\rho
                         +\frac{4N\rho}{1-4\rho}.
 \tag{14}
\]
Choose \(\delta\) so that \(m\delta<\varepsilon/4\), then
choose \(a>0\) small enough. For large \(N\), the right side
at \(\rho=a\) is less than \(\varepsilon N\).
Equations (9) and (11) imply \(\rho>a\).

For the upper bound, the \(N\) equally spaced angular roots
of \(P_N\), including multiplicity, imply that for each
fixed small \(\xi>0\), at least \(c_*\sqrt{\xi}\,N\) of
the numbers \(d_a\) lie in \([4-\xi,4)\), for large \(N\).
Here \(c_*>0\) is an absolute constant. The counting assertion follows from
\(2+2\cos t=4-t^2+O(t^4)\) near the maximum.
Thus, as \(b\uparrow1/4\), the geometric part alone has
\(\mu_N(b)/N\) arbitrarily large, uniformly for large \(N\):
take \(\xi\) comparable with \(1-4b\) in that count.
Choose a fixed \(b<1/4\) for which this mean exceeds \(mN/2\).
Since \(k\le mN/2\), monotonicity gives \(\rho<b\).

Finally a fixed positive fraction of the \(d_a\) lie in
\([1,2]\). For \(\rho\in[a,b]\), their geometric variances
are bounded below by a positive constant. All geometric
variances are bounded above by \(4b/(1-4b)^2\), and each
Bernoulli variance is at most \(1/4\). This proves (12).

## 4. A uniform leading coefficient

**Theorem 2.** Fix \(m,\varepsilon\) as in (11). Uniformly
over all such tuples and both parities,
\[
 \Gamma_{\mathbf j}^{(m)}
 =\frac{N^2a_{\mathbf j}H(\rho)\rho^{-k}}
         {\sqrt{2\pi V_N(\rho)}}\,(1+O(N^{-1})).
 \tag{15}
\]
The displayed leading factor is strictly positive. Moreover,
for every fixed integer \(h\),
\[
 \frac{[x^{k+h}]H}{[x^k]H}
            =\rho^{-h}(1+O_h(N^{-1})).
 \tag{16}
\]
The constants are uniform for \(h\) in any fixed finite set.

**Proof.** Fourier inversion applies to the integer-valued
variable in (7). At the saddle \(\mathbb E S_\rho=k\).
The geometric factors with \(d_a\in[1,2]\) give
\[
 \left|\mathbb E e^{i\theta(S_\rho-k)}\right|
       \le \exp(-cN\sin^2(\theta/2)),\qquad -\pi\le\theta\le\pi.
 \tag{17}
\]
Indeed each of their uncentered factors has modulus
\[
 \frac{1-u}{|1-ue^{i\theta}|}
  =\left(1+\frac{4u}{(1-u)^2}\sin^2(\theta/2)\right)^{-1/2},
\]
where \(u\) is uniformly separated from zero and one.
All remaining factors have modulus at most one.

The sum of the absolute cumulant bounds of each fixed order
is \(O(N)\). For the geometric factors this uses \(u\le4b<1\).
For Bernoulli factors it holds uniformly for all success
probabilities, regardless of the size of a Jacobi eigenvalue.
Consequently, on a fixed small interval,
\[
 \log\mathbb E e^{i\theta(S_\rho-k)}
  =-\tfrac12V_N\theta^2-\tfrac{i}{6}\kappa_3\theta^3
                                           +O(N\theta^4),
 \qquad |\kappa_3|\le CN.
 \tag{18}
\]
Outside \(|\theta|\le N^{-2/5}\), (17) makes the integral
exponentially small compared with \(N^{-1/2}\).
Inside, expand the cubic exponential and \(e^{-ih\theta}\).
Their first odd terms integrate to zero on this symmetric
interval. After Gaussian integration, the relative errors
are bounded by constant multiples of
\[
 N/V_N^2+N^2/V_N^3+(1+h^2)/V_N=O_h(N^{-1}).
\]
The discarded Gaussian tails are exponentially small.
Hence, uniformly for bounded \(h\),
\[
              \mathbb P(S_\rho=k+h)
               =(2\pi V_N)^{-1/2}(1+O_h(N^{-1})).
 \tag{19}
\]
Equation (10) proves (15). Applying (7) to \(k+h\) and \(k\)
and taking their ratio proves (16). \(\square\)

The proof is an elementary local central-limit argument for this
particular finite product. No asymptotic independence is assumed;
the independence in (7) is an exact representation.

## 5. Fixed-degree observations in the original trace

Let \(q(C)\) be any fixed polynomial. Formula (6) gives exactly
\[
 \frac{\phi_N(q(C)\prod_i F_{j_i}(C))}
      {\Gamma_{\mathbf j}^{(m)}}
 =\frac{[x^k]\{H(x)q(c_0-x^{-1})\}}{[x^k]H(x)} .
 \tag{20}
\]
The numerator uses only finitely many adjacent coefficients of
\(H\). Their ratios are given by (16). Thus
\[
 \frac{\phi_N(q(C)\prod_i F_{j_i}(C))}
      {\Gamma_{\mathbf j}^{(m)}}
       =q(c_0-\rho^{-1})+O_q(N^{-1}).
 \tag{21}
\]
This holds uniformly on (11); no derivative at a repeated root
has been dropped in taking the trace. It also holds uniformly
for polynomials of bounded degree with bounded coefficients.
If \(|q(c_0-\rho^{-1})|\ge\delta>0\), the observed trace has
a nonzero leading coefficient and the same exponential rate
as \(\Gamma_{\mathbf j}^{(m)}\).

The qualifier about bounded degree is essential. The original
crossing \(R^p\), even for fixed \(p\), is represented in the
finite algebra by a polynomial whose degree grows with \(N\).
The Fourier cancellations in that trace are not covered by
(16) or (21). Likewise replacing a physical value row by its
independent boundary derivative changes the positive
factorization used in (3).

## 6. Complete direct sources and scope

The complete direct sources used here are:

* [The physical Jacobi equation](research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  the exact physical recurrence, determinant formula, strict location
  of its eigenvalues, and normalization \(F_j(c_0)=1\).
* [The full physical product](research_physical_row_full_product_normal_support.md),
  SHA256 708d22248526c75b0d8b26cc9a07c63d8471b07d200b9e9947059ca8145b2efd:
  the original Frobenius trace, canonical remainder, physical row
  range, and repeated-root conventions.

The positivity and degree support of the unobserved product trace
were already known from the positive Newton multiplication table.
The contribution here is its single positive coefficient,
the uniform scalar saddle including midpoint rows, its explicit
probability normalization, and the bounded-degree observation
estimate. No identification with the volume of a partially filled
knot complement or lower bound for its complete crossed source is
asserted.

Only written mathematics, source reads, and metadata hashes were used.
No mathematical programs, tests, numerical evaluations, or builds were
run. Frozen manuscripts and public documents remain unchanged.
