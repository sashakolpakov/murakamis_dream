# A cap gap persists under a controlled signed stable expansion

This is a conditional transport theorem. It proves the estimate needed
after an exact signed stable expansion has been obtained; it does not
assert that the varying quantum source has such an expansion. In
particular, it makes no new full-invariant volume claim.

## 1. The finite cap functional

For an integer level N>=2 put d=N-1, M=floor(N/2)-1 and theta=pi/N.
For a homogeneous binary polynomial Q(A,C)=sum_j q_j A^j C^(d-j),
define its alternating section

\[
 \mathcal T_NQ(t)=\sum_{j=0}^M(-1)^j q_jt^j.
\]

The norm used here is the original positive sine-Cauchy norm

\[
 \|\mathcal T_NQ\|_{C_N}^2
 =\frac{N\sin\theta}{\pi}\int_0^\infty
       \frac{|\mathcal T_NQ(t)|^2}{1+t^N}\,dt,
 \qquad
 (C_N)_{ij}=\frac{\sin\theta}{\sin((i+j+1)\theta)}.
 \tag{1}
\]

Only degrees through 2M occur in this integral. At both parities they
are at most N-2. The exact protected source functional S_N(sigma;Q)
of `research_cap_uniform_spectral_gap.md`, equations (2), (9), (10),
satisfies

\[
 \sup_{-2\le\sigma\le2}|S_N(\sigma;Q)|
 \le K_N\|\mathcal T_NQ\|_{C_N},\qquad
 K_N=\frac{\pi^{5/2}}4\csc^2(\theta/2)(M+1).
 \tag{2}
\]

Thus K_N grows only polynomially. Both operations are linear in Q;
the norm itself obeys the triangle inequality.

If q_j>=0, then a useful crude bound is

\[
 \|\mathcal T_NQ\|_{C_N}\le Q(1,1).
 \tag{3}
\]

Indeed every diagonal entry (C_N)_(jj), 0<=j<=M, is at most one:
(2j+1)theta lies in [theta,pi-theta]. The triangle inequality applied
to the individual monomials gives (3). No squared moment of degree
2d is introduced.

## 2. How a bounded root-count change affects the useful estimate

Let P,Q be nonzero homogeneous real-stable binary polynomials of the
same degree d, with nonnegative coefficients. Normalize their factors by

\[
 \frac{P(A,C)}{P(1,1)}
  =\prod_{j=1}^d[(1-\lambda_j)C+\lambda_j A],
 \qquad 0\le\lambda_j\le1,
 \tag{4}
\]

and similarly use mu_j for Q. Let N_P(s) and N_Q(s) count these
parameters in [0,s], with multiplicity. Suppose

\[
 \sup_{0\le s\le1}|N_Q(s)-N_P(s)|\le r.
 \tag{5}
\]

The factor C is represented by parameter zero and A by parameter one;
they are not omitted. For every continuously differentiable real g,
integration by parts gives

\[
 \left|\sum_jg(\mu_j)-\sum_jg(\lambda_j)\right|
 \le r\int_0^1|g'(s)|\,ds.
 \tag{6}
\]

The endpoint contribution cancels because both measures have mass d.
The same statement holds for a piecewise continuously differentiable g.

Fix T>=1. For a normalized root measure define

\[
 \nu=d^{-1}\sum\lambda_j,\quad
 \kappa=d^{-1}\sum\lambda_j(1-\lambda_j),\quad
 a=1-\nu-\kappa,\quad b=\nu-\kappa,
\]
\[
 R_T(P)=\max\{a,b,1-4\kappa,a/T+bT-2\kappa\}.
 \tag{7}
\]

The four expressions are averages of
(1-s)^2, s^2, (1-2s)^2, and ((1-s)/sqrt(T)-s sqrt(T))^2.
Their total variations on [0,1] are respectively 1,1,2,T+T^(-1).
Consequently

\[
 R_T(Q)\le R_T(P)+(T+T^{-1})r/d.
 \tag{8}
\]

Taking g(s)=log(1+(T-1)s) in (6) also gives the exact tilt comparison

\[
 \frac{Q(T,1)}{Q(1,1)}
 \le T^r\frac{P(T,1)}{P(1,1)}.
 \tag{9}
\]

The existing finite alternating-section lemma, equation (14) of the
same cap note, implies

\[
 \|\mathcal T_NQ\|_{C_N}
 \le\sqrt{1+\log T}\,Q(1,1)R_T(Q)^{d/2}
        +(d+2)Q(T,1)T^{-M}.
 \tag{10}
\]

For this simplification use q_M T^M<=Q(T,1) in every cutoff term of
that lemma. Combining (8)--(10) retains the original cap cutoff and
the positive mass Q(1,1). In particular it does not bound each signed
coefficient separately before taking the alternating section.

## 3. An exact expansion and its total positive mass

Work along any unbounded set of integer levels I. This distinction is
essential: the presently available endpoint determinant for a general
matched exterior is stable at odd levels, not automatically at even
levels. All finite inequalities above hold at both parities when their
polynomial hypotheses are supplied.

For N in I let P_N be a nonzero homogeneous, real-stable binary
polynomial with nonnegative coefficients and degree d=N-1. It will
serve as the endpoint exterior. Fix a finite number of deformation
coordinates, independent of N. Suppose the deformed exterior has the
exact finite expansion

\[
 \widetilde P_N(\boldsymbol u;A,C)
 =\sum_{\alpha\in I_N}
      c_{N,\alpha}\boldsymbol u^{\beta_{N,\alpha}}
           Q_{N,\alpha}(A,C).
 \tag{11}
\]

Here I_N is a finite index set; c_(N,alpha) is a complex scalar;
beta_(N,alpha) is a multiindex of nonnegative integers; and each
Q_(N,alpha) is nonzero, homogeneous of degree d, real stable and has
nonnegative coefficients. All original shared face extractions and
any compensating boundary monomials are included in Q_(N,alpha).
Put k_(N,alpha)=|beta_(N,alpha)|. Require that (11) at u=0 equals
P_N, and that, for a constant J independent of N and alpha,

\[
 \sup_s|N_{Q_{N,\alpha}}(s)-N_{P_N}(s)|
        \le J k_{N,\alpha}.
 \tag{12}
\]

This formulation allows more than one rank-one insertion per spectral
power. For example, the original odd central skipping term is
u xy D_bD_c: its spectral degree is one but its two cofactors can
require two rank-one insertions. Rank and spectral degree must not be
silently identified.

Define the positive mass generating function

\[
 W_N(v)=\frac{1}{P_N(1,1)}
    \sum_{\alpha\in I_N}|c_{N,\alpha}|v^{k_{N,\alpha}}
                         Q_{N,\alpha}(1,1),\qquad v>0.
 \tag{13}
\]

This sum includes every term, regardless of rank. Assume that for some
v_0>0 there is a nonnegative function omega(v), tending to zero as
v decreases to zero, such that

\[
 \limsup_{N\to\infty,\ N\in I}N^{-1}\log W_N(v)
      \le\omega(v)\qquad(0<v\le v_0).
 \tag{14}
\]

Neither the existence of (11) nor (14) follows from a polynomial bound
for one interpolation weight. The number, magnitudes and degrees of
all terms enter (13).

## 4. Finite bound and neighborhood theorem

Let 0<epsilon<v<=v_0 and delta>0. Split (11) at k<=delta N.
For its low-degree part apply (8)--(10), with r=J k; for its remaining
part apply (3). Since epsilon^k<=v^k(epsilon/v)^(delta N) on the
remaining part, the complete bound is

\[
\begin{split}
 \sup_{\|\boldsymbol u\|_\infty\le\varepsilon}
 \|\mathcal T_N\widetilde P_N(\boldsymbol u)\|_{C_N}
 \le{}&\sqrt{1+\log T}\,P_N(1,1)W_N(\varepsilon)
       [R_T(P_N)+(T+T^{-1})J\delta N/d]^{d/2}\\
 &+(d+2)T^{J\delta N}P_N(T,1)T^{-M}W_N(\varepsilon)\\
 &+P_N(1,1)(\varepsilon/v)^{\delta N}W_N(v).
\end{split}
 \tag{15}
\]

The same estimate multiplied by K_N bounds the original protected
functional uniformly in sigma in [-2,2]. It is uniform on a complex
polydisk in the remaining parameters. No noncancellation of the
deformed source is assumed or needed for this upper bound.

For the fixed T>=1, suppose the original endpoint quantities have limits,
with F_0 and F_T finite real numbers:

\[
 N^{-1}\log P_N(1,1)\to F_0,\quad
 N^{-1}\log P_N(T,1)\to F_T,\quad R_T(P_N)\to R_T.
 \tag{16}
\]

The notation F_T here is the unnormalized tilted pressure; the term
-(log T)/2 has not been included in its definition. Since R_T>=1/4,
equations (14)--(16) give the following theorem:

\[
\begin{split}
 \lim_{\varepsilon\downarrow0}\limsup_{N\to\infty,\ N\in I}
 \frac1N\log\sup_{\substack{\|\boldsymbol u\|_\infty\le\varepsilon\\
                         -2\le\sigma\le2}}
       |S_N(\sigma;\widetilde P_N(\boldsymbol u))|
 \le\max\{F_0+\tfrac12\log R_T,\ F_T-\tfrac12\log T\}.
\end{split}
 \tag{17}
\]

To check the order of limits, first keep delta>0 and 0<v<=v_0 fixed.
The three rates in (15) are bounded by

\[
\begin{gathered}
 F_0+\tfrac12\log[R_T+(T+T^{-1})J\delta]+\omega(\varepsilon),\\
 F_T-\tfrac12\log T+J\delta\log T+\omega(\varepsilon),\\
 F_0-\delta\log(v/\varepsilon)+\omega(v).
\end{gathered}
\]

As epsilon decreases to zero the third rate tends to minus infinity.
The first two then tend to their displayed delta-dependent bounds.
Finally let delta decrease to zero. The finite sum of the three terms
does not change their maximum exponential rate. This proves (17).

If the right side of (17) is strictly less than the actual complete
action Phi, a fixed positive polydisk and a fixed strict margin below
Phi therefore exist. This is the desired persistence implication.
It is not yet its application to the actual varying exterior.

## 5. Exact status of the source application

The coefficient-swap and colored-basis argument can provide (12) for
stable compressions of an actual positive determinant product. It
keeps the common face targets; deleting local variables independently
would be a different problem. The quantitative positive-endpoint
eigenvalue bound is a possible way to obtain (14) from a controlled
matrix perturbation. An exact, uniformly controlled connection from
the varying original Casimir source to (11) remains necessary.

Even after that connection is proved, (17) concerns one selected cap
with a neighborhood of the remaining spectral parameters. A complete
volume theorem needs the applicable level parities, all complementary
sectors and the full spectral domain required by its filling norm.
Those additional steps are not consequences of this conditional lemma.

For coverage, stable supports and matroids are established subjects:
see Branden, *Polynomials with the half-plane property and matroid
theory*, https://arxiv.org/abs/math/0605678; and Borcea--Branden--Liggett,
*Negative dependence and the geometry of polynomials*,
https://arxiv.org/abs/0707.2340. The related stochastic-covering theory
appears in Pemantle--Peres, https://arxiv.org/abs/1108.0687.
These references locate the general background; none is asserted to
provide the original quantum-source expansion or the cap-specific
estimate (15). The coefficient-swap and tail proofs here are checked
directly, rather than inferred from a literature attribution.
