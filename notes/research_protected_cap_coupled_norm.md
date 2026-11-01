# A uniform bound for one cap in its moment norm

A cap is the part of the finite source at a crossing region next to the
marked strand. Two adjacent face variables there are prescribed to be zero;
the other two carry the original coefficient targets. After all other
variables have been extracted, the cap acts as a linear functional on a
finite list of coefficients. This note proves that its norm grows at most
polynomially with the level, uniformly as its real spectral parameter varies
between \(-2\) and \(2\).

The inner product uses a full moment matrix, so it retains the mixed terms
between different coefficients. The theorem holds at both level parities.
To turn it into a bound by hyperbolic volume, one would also have to bound
the norm of the remaining coefficients. That is a separate problem; the
last section explains why the present estimate alone does not solve it.

## 1. Original coefficients and the assertion

Let \(N\ge2\), and define
\[
 d=N-1,\qquad M=\lfloor N/2\rfloor-1,\qquad
 \theta=\frac{\pi}{N},\qquad
 c_j=2\cos((2j+1)\theta),\qquad
 s_j=2\sin(j\theta),\qquad S_j=\prod_{r=1}^j s_r.
 \tag{1}
\]
Empty products are one. The original protected left coefficient, including
every unused spectral row, is
\[
 v_j(\sigma)=(-1)^jS_j^2\prod_{r=j+1}^{d}(\sigma-c_r),
 \qquad 0\le j\le M.
 \tag{2}
\]
Put
\[
 U_0=\csc^2(\theta/2),\qquad
 b_k=\prod_{r=1}^k\frac{\sin(r\theta)}{\sin((r+1/2)\theta)},
 \qquad h_k=b_k^2,\qquad
 H=(h_{i+j})_{0\le i,j\le M},\qquad
 g_j(\sigma)=\frac{(-1)^jv_j(\sigma)}{U_0}.
 \tag{3}
\]
Thus \(H=H_0\circ H_0\), where \(H_0=(b_{i+j})\) and the circle denotes
entrywise multiplication. This is the coupled Gram matrix, not an unrestricted
tensor-product Gram matrix. It is positive definite by the exact positive
moment construction recalled below.

**Theorem.** For every \(N\ge2\) and every real \(\sigma\in[-2,2]\),
\[
 \boxed{\qquad
  \kappa_N(\sigma):=g(\sigma)^T H^{-1}g(\sigma)
       \le e^{210}N^5 .
 \qquad}
 \tag{4}
\]
The constants are deliberately coarse. The proof retains
\[
       2M=N-2\quad(N\ \text{even}),\qquad
       2M=N-3\quad(N\ \text{odd}).
 \tag{5}
\]
In particular it does not ask for a nonexistent moment of order \(N\).
The case \(N=2\) is immediate: \(M=0\), \(H=(1)\),
\(g_0(\sigma)=\sigma/2\), and \(\kappa_2(\sigma)\le1\).
The rest of the proof assumes \(N\ge3\).

## 2. A sine-Cauchy Gram matrix

Introduce a comparison matrix
\[
 C_{ij}=\frac{\sin\theta}{\sin((i+j+1)\theta)}
   =\frac{N\sin\theta}{\pi}
      \int_0^\infty\frac{t^{i+j}}{1+t^N}\,dt .
 \tag{6}
\]
The integral follows by substituting \(y=t^N\) in the elementary beta
integral. It is finite because \(i+j\le2M\le N-2\).
Consequently \(C\) is positive definite. Its measure is a probability
measure and has density at least \(1/\pi\) on \([0,1]\): here
\(N\sin(\pi/N)\ge2\) and \(1+t^N\le2\).

For a polynomial \(p\) of degree at most \(M\), expansion in the shifted
Legendre polynomials gives
\[
 \max_{0\le t\le1}|p(t)|^2
       \le (M+1)^2\int_0^1|p(t)|^2\,dt.
 \tag{7}
\]
Indeed the shifted polynomial of degree \(r\) has squared norm
\(1/(2r+1)\) and absolute value at most one on this interval;
Cauchy--Schwarz sums \(\sum_{r=0}^M(2r+1)=(M+1)^2\).
This proof applies to complex coefficients. In particular evaluation at zero,
as a functional on the \(C\) norm, satisfies
\[
                   (C^{-1})_{00}\le\pi(M+1)^2 .
 \tag{8}
\]

Let \(A\) be the real lower bidiagonal matrix
\[
 A_{jj}=c_j,\qquad A_{j,j-1}=s_j^2\quad(1\le j\le M).
 \tag{9}
\]
It satisfies the exact matrix identity
\[
                         AC=CA^T.
 \tag{10}
\]
To check this, put \(k=i+j\). For \(k\ge1\) the difference of the two
entries is
\[
 (c_i-c_j)\frac{\sin\theta}{\sin((k+1)\theta)}
 +(s_i^2-s_j^2)\frac{\sin\theta}{\sin(k\theta)}=0.
 \tag{11}
\]
The equality uses
\(c_i-c_j=-4\sin((k+1)\theta)\sin((i-j)\theta)\) and
\(s_i^2-s_j^2=4\sin(k\theta)\sin((i-j)\theta)\).
At \(i=j=0\) both sides agree directly; no division by \(\sin0\) is used.
Thus \(A\) is self-adjoint for the inner product with matrix \(C^{-1}\).
Equivalently \(C^{-1/2}AC^{1/2}\) is a real symmetric matrix.
Its eigenvalues are the distinct numbers \(c_0,\ldots,c_M\).

The full spectral polynomial, with its original repeated roots, is
\[
 \chi_N(z)=\prod_{r=0}^{d}(z-c_r)
              =2\bigl(T_N(z/2)+1\bigr).
 \tag{12}
\]
Here \(T_N(\cos a)=\cos(Na)\). For real \(z\in[-2,2]\),
\[
                  |\chi_N'(z)|\le N^2.
 \tag{13}
\]
For example, differentiating gives
\(\chi_N'(z)=N U_{N-1}(z/2)\); the geometric-sum formula for
\(\sin(Na)/\sin a\) gives \(|U_{N-1}|\le N\), including its endpoint limits.

The original coefficient recurrence is
\[
  (\sigma-c_j)g_j=s_j^2g_{j-1}\quad(j\ge1),\qquad
  (\sigma-c_0)g_0=\chi_N(\sigma)/U_0.
 \tag{14}
\]
For a fixed \(\sigma\), let
\[
 q_\sigma(z)=\frac{\chi_N(\sigma)-\chi_N(z)}{\sigma-z},
 \tag{15}
\]
interpreted as a polynomial divided difference. Since \(\chi_N(A)=0\),
equation (14), first away from its finitely many nodes and then by polynomial
continuation, gives
\[
                  g(\sigma)=U_0^{-1}q_\sigma(A)e_0.
 \tag{16}
\]
For every eigenvalue \(c_j\) of \(A\), the mean-value bound (13) implies
\[
             |q_\sigma(c_j)|\le N^2
                \qquad(-2\le\sigma\le2).
 \tag{17}
\]
This includes \(\sigma=c_j\); there is no resolvent singularity in (15).
The finite-dimensional spectral theorem in the \(C^{-1}\) inner product
therefore yields
\[
 \begin{aligned}
  g(\sigma)^T C^{-1}g(\sigma)
   &\le \frac{N^4}{U_0^2}(C^{-1})_{00}\\
   &\le\frac{\pi^5}{16}(M+1)^2.
 \end{aligned}
 \tag{18}
\]
The last step uses \(U_0\ge4N^2/\pi^2\).
This estimate is for the complete source vector \(g\), not for its two
separated spectral factors.

## 3. A quantitative lower density for the original coupled measure

The exact beta-product construction of the protected moments has the
following form. Let \(T_1,T_2\) be independent
\(\operatorname{Beta}(1,1/2)\) variables. Independently, for \(k\ge1\) and
\(\ell=1,2\), take
\[
 A_{k,\ell}\sim\operatorname{Beta}(kN-1/2,1/2),\qquad
 B_{k,\ell}\sim\operatorname{Beta}(kN+1,1/2),\qquad
 G=\prod_{k\ge1}\prod_{\ell=1}^2\frac{B_{k,\ell}}{A_{k,\ell}},
 \qquad X=T_1T_2G.
 \tag{19}
\]
All factors are independent. The product is defined by the convergent
series of logarithms. The beta integral and Euler's sine product give
\[
                \mathbb E X^j=h_j\qquad(0\le j\le d).
 \tag{20}
\]
These are precisely the original cap moments. To recall why the infinite
product is legitimate, a beta ratio pair has logarithmic mean and variance
of order \((kN)^{-2}\). Its real moments on compact subsets of
\(-1<s<N-1/2\) have logarithms of the same summable order.
The log series converges in \(L^2\), and a slightly larger positive moment
gives uniform integrability at each integer \(j\le d\).
Thus (20) follows from finite products, not from an unproved interchange
of an infinite product and an integral. This is the original
positive-moment theorem; the estimates below quantify its density.

Here are explicit bounds sufficient for that purpose. If
\(Y_a\sim\operatorname{Beta}(a,1/2)\) and \(f(a)=\mathbb E\log Y_a\), then
\[
 f(a)=-\int_0^\infty\frac{e^{-at}}{1+e^{-t/2}}\,dt,\qquad
 0<f'(a)=\operatorname{Var}(\log Y_a)\le a^{-2},
 \qquad |f(a)|\le a^{-1}.
 \tag{21}
\]
These formulas follow by differentiating the beta integral, or by
expanding the usual difference of the two logarithmic gamma derivatives
as a convergent integral. The displayed estimates follow immediately
from the integral and its derivative.
Since \(kN-1/2\ge5kN/6\), (21) gives for each ratio in (19)
\[
 0\le\mathbb E\log(B_{k,\ell}/A_{k,\ell})
                   \le\frac{3}{(kN)^2},\qquad
 \operatorname{Var}\log(B_{k,\ell}/A_{k,\ell})
                   \le\frac{3}{(kN)^2}.
 \tag{22}
\]
Summing and using \(\sum_{k\ge1}k^{-2}<2\) gives
\[
 0\le\mathbb E\log G\le12N^{-2},\qquad
 \operatorname{Var}\log G\le12N^{-2}.
 \tag{23}
\]

Remove just one inverse-beta factor and put \(G_*=A_{1,1}G\).
The variable \(G_*\) is independent of \(A_{1,1},T_1,T_2\).
Its logarithmic variance is at most that of \(G\), and its logarithmic
mean lies between \(-1/(N-1/2)\) and \(12/N^2\).
Chebyshev's inequality, with displacement \(8/N\) from the respective
means, proves
\[
 \mathbb P(|\log G|\le24/N)\ge3/4,\qquad
 \mathbb P(|\log G_*|\le24/N)\ge3/4.
 \tag{24}
\]
For example the failure probability is at most \(12/64<1/4\), and the
absolute mean is at most \(4/N\).

We now prove the density bound
\[
 \boxed{\quad
   \frac{d\mu_N}{dt}(t)\ge
       \frac{e^{-200}}{N^2}
       \begin{cases}
         1,&0<t\le1,\\
         t^{-N-1/2},&t\ge1,
       \end{cases}
 \quad}
 \tag{25}
\]
where \(\mu_N\) is the law of \(X\). Densities and their inequalities may
be read almost everywhere, which suffices for all ensuing integrals.

First, the product \(Y=T_1T_2\) has density
\[
 f_Y(y)=\frac14\int_y^1
      \frac{dx}{\sqrt{x}\sqrt{1-x}\sqrt{x-y}}
             \ge\frac{\pi}{4}\qquad(0<y<1).
 \tag{26}
\]
The last integral without \(1/\sqrt x\) is \(\pi\), and
\(1/\sqrt x\ge1\). For \(0<t\le e^{-24/N}\), condition on the first event
in (24). Then \(t/G\le1\), \(G^{-1}\ge e^{-24/N}\ge e^{-8}\), and
\[
                   f_X(t)\ge (3\pi/16)e^{-8}.
 \tag{27}
\]

For the remaining \(t\), write
\(X=R/A_{1,1}\), where \(R=T_1T_2G_*\).
Since the \(\operatorname{Beta}(1,1/2)\) density is at least \(1/2\), each event
\[
                 e^{-60/N}\le T_\ell\le e^{-50/N}
 \tag{28}
\]
has probability at least \(5e^{-20}/N\). Together with the second event
in (24), these independent events have probability at least
\((75/4)e^{-40}N^{-2}\) and imply
\[
                     e^{-144/N}\le R\le e^{-76/N}.
 \tag{29}
\]
Set \(a=N-1/2\). The conditional density of \(R/A_{1,1}\) at \(t>R\) is
\[
 \frac{R^a}{B(a,1/2)}\,t^{-a-1}(1-R/t)^{-1/2}.
 \tag{30}
\]
Here \(B(a,1/2)\le B(1,1/2)=2\). If \(t\ge e^{-24/N}\), all values
of \(R\) in (29) satisfy \(R<t\) and \(R^a\ge e^{-144}\).
Equations (29)--(30) therefore give
\[
            f_X(t)\ge\frac{75}{8}\,
                     e^{-184}N^{-2}t^{-N-1/2}.
 \tag{31}
\]
For \(t\le1\) the last power is at least one. The bounds (27),(31)
imply (25), with ample room in the numerical constant.

The different tail powers in (6) and (25) are essential.
There is no assertion that \(\mu_N\) pointwise dominates a constant
multiple of the sine-Cauchy measure on the whole half-line.

## 4. The finite-degree tail comparison

We first record an elementary weighted inequality. If \(q\) has degree at
most \(M\) and \(\alpha\in\{0,1\}\), then
\[
 \int_0^1 |q(t)|^2t^\alpha\,dt
       \le2\sqrt2(M+1)
          \int_0^1 |q(t)|^2t^{\alpha+1/2}\,dt.
 \tag{32}
\]
For \(\alpha=0\), put
\(\delta=1/[2(M+1)^2]\). Inequality (7) shows that the interval
\([0,\delta]\) contains at most half the unweighted squared norm.
The remaining half lies where \(t^{1/2}\ge\sqrt\delta\), proving (32).

For \(\alpha=1\), write \(A_r=\int_0^1|q(t)|^2t^r\,dt\).
The same argument first gives
\(A_1\ge A_0/[4(M+1)^2]\); hence (7) implies
\(\|q\|_\infty^2\le4(M+1)^4A_1\).
It follows that
\[
 \int_0^\delta t|q(t)|^2\,dt
       \le \frac{\delta^2}{2}\|q\|_\infty^2
       \le \frac12 A_1 .
 \tag{33}
\]
Again the remaining half has the extra weight at least \(\sqrt\delta\).
This proves (32) also for complex coefficients.

For a polynomial \(p\) of degree at most \(M\), define its reversal
\(q(t)=t^M p(t^{-1})\). Substitution \(t=1/x\) shows
\[
 \begin{aligned}
  \int_1^\infty |p(x)|^2x^{-N}\,dx
       &=\int_0^1|q(t)|^2t^{N-2M-2}\,dt,\\
  \int_1^\infty |p(x)|^2x^{-N-1/2}\,dx
       &=\int_0^1|q(t)|^2t^{N-2M-3/2}\,dt .
 \end{aligned}
 \tag{34}
\]
The first exponent is exactly \(0\) at even levels and \(1\) at odd
levels. Therefore (32) compares precisely these two tails. Since
\(N\sin\theta/\pi\le1\), equations (6),(25),(32)--(34) yield, for every
coefficient vector \(p\),
\[
 \begin{aligned}
 p^*Cp
  &\le \int_0^1|p(t)|^2\,dt
                 +\int_1^\infty|p(t)|^2t^{-N}\,dt\\
  &\le 2\sqrt2(M+1)e^{200}N^2\,p^*Hp .
 \end{aligned}
 \tag{35}
\]
Thus the required finite-dimensional matrix comparison is
\[
        H\succeq
           \frac{e^{-200}}{2\sqrt2(M+1)N^2}\,C .
 \tag{36}
\]
This is a comparison of quadratic forms on the original finite cutoff.
The proof explicitly uses that cutoff to compensate for the tail
discrepancy; entrywise moment comparisons would not prove (36).

## 5. The coupled bound and its precise source implication

Inverting the positive matrices in (36) and applying (18) gives
\[
 \begin{aligned}
 \kappa_N(\sigma)
  &\le 2\sqrt2(M+1)e^{200}N^2
          \frac{\pi^5}{16}(M+1)^2\\
  &\le \frac{\sqrt2\,\pi^5}{64}\,e^{200}N^5
   <e^{210}N^5 .
 \end{aligned}
 \tag{37}
\]
This proves (4) for both parities and every real spectral value,
including repeated nodes and the odd simple endpoint.
No separation into the two one-factor spectral functionals is used.

To state the actual coefficient consequence, retain the original
spectator targets and write the resulting homogeneous polynomial as
\[
 B(x,c)=\sum_{k=0}^d B_kx^kc^{d-k},\qquad
 a_j=(-1)^jB_{d-j}\quad(0\le j\le M).
 \tag{38}
\]
The original protected contraction and its exact coupled energy are
\[
 [x^dc^d]H_L(x,0,c,0;\sigma)B(x,c)
     =U_0\sum_{j=0}^M g_j(\sigma)a_j,\qquad
 \mathcal E_N(B)=a^*Ha.
 \tag{39}
\]
Finite-dimensional Cauchy--Schwarz with (4) now proves
\[
 \sup_{\sigma\in[-2,2]}
 \left|[x^dc^d]H_L(x,0,c,0;\sigma)B(x,c)\right|^2
     \le e^{210}N^5U_0^2\,\mathcal E_N(B).
 \tag{40}
\]
This is a polynomial comparison with the same interference-retaining
energy that occurs at \(\sigma=2\). All exterior coefficients are retained;
they are not replaced by independent absolute local bounds.

The energy can itself exceed a positive endpoint comparison
exponentially, as the existing cap-moment obstruction proves.
Consequently (40) is not a bound by the drilled action, a strict
full-minus-central estimate, or a filling-volume theorem.
It does remove a specific spectral obstruction: controlling the actual
coupled energy would suffice uniformly over the entire real cap spectrum
at polynomial cost. Derivative or first-normal estimates are not asserted
here; any passage through the finite Hermite functional must retain its
separate hypotheses and factors.

## 6. Dependencies and finite checks

The original coefficient (2) and its normalization are recorded in
the protected sharp-scalar derivation and in the frozen
spectral-moment projection note. The positive law (19)--(20) is the
existing theorem in
[An exact positive moment form for the original flat-cap coefficients](research_flat_cap_positive_moment_form.md), not a new assertion of
positivity. Its single-factor metric and the noninvariance of the
monomial-diagonal subspace are also explained in
[Actual continuant recurrences and an explicit positive cap tensor metric](research_cap_demand_continuant_jacobi_interface.md).
The present proof instead uses the sine-Cauchy matrix (6), the
self-adjoint recurrence (10), and the finite-degree comparison (36).

The accompanying exact finite checker compares the original
unused-row products, the direct matrix polynomial (16), and the
symmetry identity (10), at representative levels of both parities.
Those checks are checks of finite identities. The density and
weighted-integral arguments above, rather than a numerical spectrum
scan, prove the uniform theorem.
