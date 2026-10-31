# The classical boundary-pressure germ determines the cap root loss

31 October 2026. **analytical research reduction.**
Unpublished. This concerns the original ONE-cap coefficient at cap
spectrum +2 and all other CROSS spectra -2, at ODD levels. It strengthens
the effective-response criterion without assuming a global continuation
of a saddle. It does not prove the required comparison for every diagram.

## 1. Keep the same polynomial and the same classical pressure

Use the original globally extracted binary polynomial and its genuine
real-root factorization from
[the negative-axis reduction](research_global_cap_negative_axis_and_mahler_bound.md):

\[
 P_N(A,C)=P_N(1,1)\prod_{r=1}^{N-1}
       [(1-\lambda_{N,r})C+\lambda_{N,r}A],
 \qquad 0\le\lambda_{N,r}\le1. \tag{1}
\]

Assume the strict finite positive one-cap stationary exterior in
[the effective-response theorem](research_global_cap_effective_response_criterion.md).
That theorem gives a fixed complex neighborhood of zero on which

\[
 N^{-1}\log P_N(e^z,1)\longrightarrow F(z),\qquad
 F(0)=M_{\mathrm{cap}},\quad F'(0)=\nu,\quad F''(0)=\kappa_D>0.
 \tag{2}
\]

Convergence is locally uniform and the logarithm continues from real
positive weights. Here F is obtained from the original finite exterior
potential by eliminating precisely the extracted ordinary log weights.
It is not an assumed asymptotic of a modified signed coefficient.

Put

\[
 \mu_N=\frac1N\sum_{r=1}^{N-1}\delta_{\lambda_{N,r}},\qquad
 G(x)=F(\log(1+x))-F(0). \tag{3}
\]

Only a fixed small disk about x=0 is used. The logarithms log(1+px),
with p in [0,1], have a common analytic branch there.

## 2. A unique compact root measure is determined by the local germ

There is a unique probability measure mu_D on [0,1] such that
mu_N converges weakly to mu_D along the odd levels and

\[
 \begin{aligned}
 G(x)&=\int_0^1\log(1+px)\,d\mu_D(p),\\
 m_0&=1,\qquad
 m_j:=\int_0^1p^j\,d\mu_D(p)
   =\frac{(-1)^{j+1}}{(j-1)!}G^{(j)}(0),\qquad j\ge1.
 \end{aligned} \tag{4}
\]

Proof. Equation (1) gives the first integral exactly with G replaced
by its finite-N version and mu_D by mu_N. Locally uniform convergence
in (2), composed with log(1+x), permits Cauchy differentiation at zero.
Thus every moment converges to the displayed value; the total masses
(N-1)/N tend to one. Measures of bounded mass on compact [0,1] have
weakly convergent subsequences, and each limit has these moments.
Two such limits agree on polynomials. For any continuous function h,
its Bernstein polynomials converge uniformly to h: uniform continuity
controls |h(j/n)-h(p)| when |j/n-p| is small, and the remaining binomial
mass tends uniformly to zero by its variance bound 1/(4n).
Consequently the two limits agree on every continuous function and
are the same measure. Every subsequence therefore has the same limit,
which proves convergence of the full odd sequence.

This argument uses the local pressure germ only. There is no global
real or complex fugacity saddle hypothesis and no attempt to evaluate
the saddle directly across the negative real axis.

## 3. Exact limiting Mahler loss and a finite hierarchy of tests

The continuous function

\[
 h(p)=-\log\max(p,1-p),\qquad 0\le p\le1 \tag{5}
\]

is Lipschitz with constant 2, including its corner at p=1/2. Therefore

\[
 \frac{L_N}{N}=\int h\,d\mu_N\longrightarrow
 \ell_D:=\int h\,d\mu_D,\qquad
 \frac1N\log\operatorname{Mahler}(P_N)
      \longrightarrow M_{\mathrm{cap}}-\ell_D. \tag{6}
\]

All original degree demands remain inside P_N. The original cap bound,
including its strictly smaller omitted tail, now gives

\[
 \limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
       \frac1N\log|S_N|
 \le\max\{M_{\mathrm{cap}}-\ell_D,\Phi_D-\gamma_D/2\}. \tag{7}
\]

In particular ell_D > M_cap-Phi_D is sufficient for a strict absolute
cap-sector gap at these fixed spectra. This is a sufficient Mahler
criterion, not a necessary criterion for cancellation of S_N.

It has finite certificates involving only derivatives of the classical
pressure. For n>=1 let

\[
 \begin{aligned}
 H_n(p)&=\sum_{j=0}^n h(j/n)\binom nj p^j(1-p)^{n-j},\\
 b_n&=\sum_{j=0}^n h(j/n)\binom nj
           \sum_{a=0}^{n-j}(-1)^a\binom{n-j}{a}m_{j+a}.
 \end{aligned} \tag{8}
\]

The binomial variance and the Lipschitz bound imply

\[
 \|H_n-h\|_\infty\le n^{-1/2},\qquad
 b_n-n^{-1/2}\le\ell_D\le b_n+n^{-1/2}. \tag{9}
\]

Thus any single verified inequality

\[
 b_n-n^{-1/2}>M_{\mathrm{cap}}-\Phi_D. \tag{10}
\]

certifies the strict fixed-spectrum odd cap gap. Conversely, if the
strict Mahler criterion holds, some finite n satisfies (10). These
are exact mathematical certificates; floating-point evaluations without
error bounds do not certify (10). The lower bounds need not be monotone;
the running maximum of them is a monotone hierarchy with limit ell_D.
All m_j in a fixed test come from finitely many derivatives of the
finite classical gluing potential at its genuine stationary weights.

## 4. A sharper test using only the effective conductance

There is also an improvement using only the already computed response.
Define, for 0<=v<=1/4,

\[
 \psi(v)=-\log\left(\frac{1+\sqrt{1-4v}}2\right). \tag{11}
\]

Then h(p)=psi(p(1-p)). On 0<=v<1/4,

\[
 \psi'(v)=\frac{2}{\sqrt{1-4v}(1+\sqrt{1-4v})}.
 \tag{12}
\]

This derivative is increasing, so psi is convex, including its
continuous endpoint value psi(1/4)=log 2. Equations (2)-(4) give

\[
 \int p(1-p)\,d\mu_D=m_1-m_2=\kappa_D,\qquad
 \ell_D\ge\psi(\kappa_D)>\kappa_D. \tag{13}
\]

The last inequality uses kappa_D>0, psi(0)=0 and psi'(v)>1 for v>0.
Jensen's inequality proves the first bound. Hence the finite classical
condition psi(kappa_D)>M_cap-Phi_D suffices and is stronger than the
previous condition kappa_D>M_cap-Phi_D. It is still not automatic.
In particular positivity of conductance alone does not compare it
with the original geometric volume deficit.

## 5. A local response integral and a fourth-derivative improvement

The same original pressure gives stronger low-order tests. Put
v=p(1-p) and use its distribution under mu_D. The elementary series

\[
 \psi(v)=\sum_{r\ge1}\frac{\binom{2r}{r}}{2r}v^r,
 \qquad \psi''(v)\ge3 \quad(0\le v<1/4) \tag{14}
\]

follows by expanding (12). Thus psi is 3-strongly convex, with
continuous extension at 1/4. Choose t>0 inside the certified local
real gluing neighborhood and set

\[
 \begin{aligned}
 s&=4\sinh^2(t/2),\\
 D(t)&=F(t)+F(-t)-2F(0)
      =\int_{-t}^t(t-|u|)F''(u)\,du,\\
 \delta(t)&=\log(1+s\kappa_D)-D(t).
 \end{aligned} \tag{15}
\]

Multiplying the two original linear factors at exp(t) and exp(-t)
gives (1-p+pe^t)(1-p+pe^{-t})=1+s v. Hence D(t) is exactly
integral log(1+s v) dmu_D. Jensen gives delta(t)>=0. The curvature
bound for log(1+s v) gives delta(t)<=s^2 Var(v)/2; strong convexity
of psi gives ell_D>=psi(kappa_D)+3 Var(v)/2. Consequently

\[
 \ell_D\ge\psi(\kappa_D)+\frac{3\delta(t)}{s^2}. \tag{16}
\]

Every F''(u) here is the original Schur-complement response at the
nearby positive gluing weights. The cap itself need not be stationary
at nonzero u. No global real-fugacity saddle is assumed. The added
term is positive unless v is constant almost everywhere. At a mean
v equal to an endpoint, v is constant and the inequalities hold
directly without differentiating psi at its singular endpoint.

The fourth derivative of the Bernoulli logarithm in (1) gives
F''''(0)=integral v(1-6v) dmu_D. Thus the limit t tending to zero
of (16) is the explicit finite-germ bound

\[
 \ell_D\ge\psi(\kappa_D)
     +\frac{\kappa_D-F^{(4)}(0)-6\kappa_D^2}{4}. \tag{17}
\]

The numerator is 6 Var(v), hence is nonnegative. The full moment
hierarchy can improve these low-order tests further.

## 6. The exact negative-axis supremum rates also come from the germ

The Mahler bound can lose information by maximizing each root factor
separately. Keep the common real variable instead. Define

\[
 \begin{aligned}
 U^-(t)&=\int\log|1-(1+t)p|\,d\mu_D(p),\\
 U^+(t)&=\int\log|t-(1+t)p|\,d\mu_D(p),\\
 m^\pm&=\max_{0\le t\le1}U^\pm(t),\qquad
 \chi_D=-\max(m^-,m^+).
 \end{aligned} \tag{18}
\]

The maxima are finite and attained, although individual values may
be minus infinity. The exact original suprema satisfy

\[
 \begin{aligned}
 \lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}
       \frac1N\log B_N^\pm&=M_{\mathrm{cap}}+m^\pm,\\
 \chi_D&\ge\ell_D\ge\psi(\kappa_D)>\kappa_D.
 \end{aligned} \tag{19}
\]

Here B_N^- is sup |P_N(-t,1)| and B_N^+ is sup |P_N(-1,t)| on
0<=t<=1, exactly as in the original cap reduction. We prove the
continuity of these supremum rates, rather than assuming pointwise
logarithmic-potential convergence at polynomial zeros.

For a finite positive measure mu on [0,1], put
U_mu(t)=integral log|1-(1+t)p| dmu(p). For a nondegenerate interval
I=[a,b] in [0,1], the averaged kernel is

\[
 A_I(p)=\frac{H(1-(1+a)p)-H(1-(1+b)p)}{p(b-a)},\qquad
 H(x)=x\log|x|-x,\quad H(0)=0. \tag{20}
\]

It is continuous for p>0, including a zero at an integration endpoint.
At p=0 it extends continuously by A_I(0)=0, since the original kernel
tends uniformly to zero. Thus A_I is bounded and continuous on the
whole root interval. Tonelli applied to the nonnegative negative
kernel justifies averaging; the finite integral of A_I then proves
finiteness of every such interval average.

The truncated kernels max(log|1-(1+t)p|,-R) are continuous and
decrease to the logarithmic kernel. Their integrals show U_mu is
upper semicontinuous. Its full-interval average is finite, so it is
finite somewhere and has a finite attained maximum on [0,1].

For a shrinking-interval estimate, take a point t0 with U_mu(t0)
finite. Use I_epsilon=[t0,t0+epsilon] if t0<1 and the left interval
if t0=1. For p>0, put r=p^{-1}-1. Apart from the single singular
root value, cancel log p and rescale. The difference between the
averaged and point kernels is

\[
 \begin{aligned}
 \omega(v)&=\int_0^1\log|u-v|\,du-\log|v|\\
 &=(1-v)\log\left|\frac{1-v}{v}\right|-1,\qquad
 v=(r-t_0)/\varepsilon.
 \end{aligned} \tag{21}
\]

At v=1 the continuous value is -1. The left interval uses omega(-v).
For nonzero real v, omega(v)>=-2 and omega(v) tends to zero as
|v| tends to infinity. For 0<v<=1/2 the logarithm in (21) is
nonnegative; for 1/2<v<1 use (1-v)log(1-v)>=-1/e. For v>=1,
rewrite it as (v-1)log(1+1/(v-1))-1>=-1. For v<0 use
log(1+x)>=x/(1+x), giving omega(v)>=0. At p=0 the difference
is exactly zero.

Finiteness of U_mu(t0) excludes an atom at its singular root and
makes the point kernel integrable. The differences tend to zero
almost everywhere and are bounded below by -2. Fatou gives that
the lower limit of shrinking averages is at least U_mu(t0).
Upper semicontinuity gives the opposite upper limit. Thus these
averages converge to every finite point value, including endpoints.

Now let mu_j converge weakly to mu, with bounded finite masses.
Choose maximizing t_j and a subsequence converging to t. Each
continuous truncated kernel gives
limsup U_mu_j(t_j)<=integral max(log|1-(1+t)p|,-R) dmu(p).
Let R tend to infinity to obtain the upper bound by max U_mu.
For the lower bound, average on a fixed short interval adjacent
to a finite maximizing point of U_mu. Equation (20) permits
passage through weak convergence; then shrink the interval using
(21). Therefore max U_mu_j converges to max U_mu.

Apply this lemma to the actual mu_N of mass (N-1)/N. Factorization
(1) proves the first line of (19). The plus kernel is the minus
kernel with p replaced by 1-p, so the same proof applies. Both
affine factors have absolute value at most max(p,1-p); integrating
and maximizing proves chi_D>=ell_D.

The original finite cap identity and its strict omitted-tail estimate
therefore give the stronger bound

\[
 \limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
       \frac1N\log|S_N|
 \le\max\{M_{\mathrm{cap}}-\chi_D,\Phi_D-\gamma_D/2\}. \tag{22}
\]

The condition chi_D>M_cap-Phi_D suffices for strict absolute cap
suppression at these fixed spectra. There is no signed-S lower bound:
the expectation defining S_N can have additional cancellation.

## 7. Finite certificates for the stronger common-variable criterion

Even the criterion using chi_D can be detected by finite gluing
derivatives. This needs an approximation argument because the
logarithmic kernel is unbounded below. For R>0 set

\[
 \begin{aligned}
 K_R^-(t,p)&=\log\max\{|1-(1+t)p|,e^{-R}\},\\
 K_R^+(t,p)&=K_R^-(t,1-p).
 \end{aligned} \tag{23}
\]

These kernels are Lipschitz with constants e^R in t and 2e^R in p.
Let B_n be the Bernstein polynomial operator of degree n in p, as
in (8), and let m>=1 be an integer grid size. Define

\[
 C_{R,n,m}^{\pm}
 =\max_{0\le j\le m}\int
       B_n[K_R^\pm(j/m,\cdot)](p)\,d\mu_D(p)
       +e^R\bigl(n^{-1/2}+m^{-1}\bigr). \tag{24}
\]

The Bernstein error is at most e^R/sqrt(n), and the grid error is
at most e^R/m. Thus m^pm<=C^pm. Each integral in (24) is the finite
moment expression in (8), with h(a/n) replaced by
K_R^pm(j/m,a/n). It uses only m_0 through m_n, hence finitely many
derivatives of the original pressure.

For fixed R, letting n,m tend to infinity makes (24) converge to
the maximum of integral K_R^pm(t,p) dmu_D(p). These maxima decrease
to m^pm as R tends to infinity. Indeed choose maximizers along a
diverging R sequence, pass to a convergent t subsequence, and bound
by each fixed smaller truncation level before letting that level
tend to infinity. The reverse inequality holds because every
truncated kernel dominates the original one.

Consequently any verified finite test

\[
 M_{\mathrm{cap}}+\max(C_{R,n,m}^-,C_{R,n,m}^+)<\Phi_D. \tag{25}
\]

proves the strict fixed-spectrum odd cap gap. Conversely every strict
instance of chi_D>M_cap-Phi_D is detected by some finite R,n,m.
Finite enclosures must include all approximation and evaluation errors;
no sample of growing quantum polynomials is part of the test.

## 8. What this closes and what remains

The normalized Mahler loss and both exact negative-axis supremum rates
are now determined by the SAME local classical gluing germ that computes
the boundary response. A growing collection
of quantum roots need not be computed separately. Finite derivative
certificates can detect every strict instance of the stronger common-variable
criterion.
This does not claim that the germ or the measure is encoded by the
ordinary knot A-polynomial alone; the original exterior, degree demands,
and selected pressure branch are part of the data.

No argument here proves that all eligible fixed plat diagrams pass the
criterion. The two-cap case also needs its actual joint extraction: a
projection onto a selected total degree is not in general stability
preserving. For example, the stable polynomial (A+B)(C+D), projected
to total degree one in A,C, becomes AD+BC. This vanishes at
A=D=exp(i*pi/4), B=C=exp(3*i*pi/4), all in the upper half-plane.
This is a closure counterexample, not an actual two-cap source counterexample.
Even levels, spectral neighborhoods, the original Green
truncations and the full filled-knot assembly retain their stated
requirements. The general prescribed long-twist conjecture remains open.
