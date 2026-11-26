# Finite occupation cutoffs in the literal Poisson kernels

Private written proof, 18 November 2026.

The finite head restrictions at a crossing are coupled restrictions on
its three Poisson indices. They are not three independent cutoffs.
This note writes the exact multiplier for those restrictions and gives
a quantitative complex domain where it differs exponentially little
from one. The original coefficient function remains inside the pairing;
no sum of absolute matrix entries replaces it.

The scalar partial-exponential identity is classical; it is also the
integer incomplete-gamma identity
[DLMF 8.4.8](https://dlmf.nist.gov/8.4.E8). Its proof and the estimates
used here are elementary and are included. No novelty is claimed for
that scalar function.

## 1. The finite projector as a multiplier

For a positive integer \(N\), define
\[
 E_{N-1}(t)=\sum_{j=0}^{N-1}\frac{t^j}{j!},
 \qquad Q_N(t)=e^{-t}E_{N-1}(t).
 \tag{1}
\]
These are entire functions. For three variables put
\[
 S_N=\{(n,c,d)\in\mathbb Z_{\ge0}^3:
                         n+c<N,\ n+d<N\}
 \tag{2}
\]
and
\[
 Q_{S_N}(t)=e^{-t_1-t_2-t_3}
       \sum_{(n,c,d)\in S_N}
              \frac{t_1^nt_2^ct_3^d}{n!c!d!}.
 \tag{3}
\]
All sums in (1) and (3) are finite.

The scalar wall has the exact entire formulas
\[
 Q_N'(t)=-\frac{e^{-t}t^{N-1}}{(N-1)!},\qquad
 Q_N(t)=1-\frac1{(N-1)!}\int_0^t e^{-s}s^{N-1}\,ds .
 \tag{3a}
\]
Differentiate (1) to telescope its two sums, then use \(Q_N(0)=1\).
The integrand is entire, so the displayed finite integral is
path-independent. Together with the elementary gamma moment
\(\int_0^\infty e^{-s}s^{N-1}ds=(N-1)!\), proved by integration
by parts, this also proves the stated incomplete-gamma connection.

More generally, for the coupled mask define its outgoing facets by
\[
 \partial_iS_N=\{k\in S_N:k+e_i\notin S_N\}.
\]
Direct differentiation of (3) gives
\[
 \partial_{t_i}Q_{S_N}(t)
       =-e^{-\sum_jt_j}\sum_{k\in\partial_iS_N}\frac{t^k}{k!}.
 \tag{3b}
\]
Indeed reindexing the differentiated polynomial leaves
\(S_N-e_i=\{k\ge0:k+e_i\in S_N\}\), a subset of \(S_N\);
their difference is exactly the displayed facet. For \(i=1\)
the facet is the union \(n+c=N-1\) or \(n+d=N-1\), with the
intersection counted once. For \(i=2\) only the first face occurs,
and for \(i=3\) only the second. Thus the multiplier retains the
coupled boundary currents before any estimate.

Let \(h\ne0\), \(\lambda_i=U_i/h\), and
\(t_i=\lambda_i e^{\Xi_i}\). Then
\[
 e^{-\sum_i\lambda_i}
     \sum_{k\in S_N}\prod_i\frac{(\lambda_i e^{\Xi_i})^{k_i}}{k_i!}
 =
 e^{\sum_i\lambda_i(e^{\Xi_i}-1)}Q_{S_N}(t).
 \tag{4}
\]
This is an identity of entire functions of \(\lambda,\Xi\). In
particular it has no apparent singularity at a zero mean.

Here is its exact functional interpretation. For every polynomial
\(f(X_1,X_2,X_3)\), the cross-Wick rule with
\[
 K_\times=\begin{pmatrix}0&I_3\\I_3&0\end{pmatrix}
\]
gives
\[
\begin{split}
 &\mathbb E_{hK_\times}
  \left[
    f(X)e^{\sum_i\lambda_i(e^{\Xi_i}-1)}Q_{S_N}(t)
  \right]\\
 &\hspace{12mm}=
 e^{-\sum_i\lambda_i}
        \sum_{k\in S_N}\frac{\lambda^k}{k!}\,f(hk).
\end{split}
\tag{5}
\]
Indeed \(\mathbb E_{hK_\times}[f(X)e^{k\cdot\Xi}]=f(hk)\),
by differentiating the exponential generator. Equation (4) reduces
the left side to a finite sum of precisely those generators.

The function \(f\) in (5) may couple all three variables. If it
also depends polynomially on other source variables, the equality
is an identity in those variables. An analytic interpretation for
a nonpolynomial \(f\) requires its values on the indicated shifted
domain: the finite-translation right side then defines the pairing.
It is not permission to exchange an arbitrary Taylor series with an
infinite Gaussian integral.

For independent coordinate cutoffs \(0\le k_i<N\), the multiplier
instead factors as \(\prod_i Q_N(t_i)\). For the coupled support
(2), that product is incorrect. An exact useful expression is
\[
 Q_{S_N}(t)=e^{-\sum_i t_i}
  \sum_{n=0}^{N-1}\frac{t_1^n}{n!}
                  E_{N-n-1}(t_2)E_{N-n-1}(t_3).
 \tag{6}
\]

## 2. Why this is the actual local head mask

Keep the literal signed entries of [F], with all their Gaussian
polynomials, color products, and monomials. At a positive crossing
write the original indices as
\[
       a=n+c,\quad b=d,\qquad
       (a_{\rm out},b_{\rm out})=(d+n,c).
 \tag{7}
\]
All four occupations belong to \(\{0,\ldots,N-1\}\) exactly when
\((n,c,d)\in S_N\). At a negative crossing use
\[
       a=d,\quad b=n+c,\qquad
       (a_{\rm out},b_{\rm out})=(c,d+n).
 \tag{8}
\]
The same support (2) results. Thus (3), before any division by a
classical kernel or change of fields, is the local mask for both
input and output head projectors.

The exact Poisson presentations of [P] use the means
\[
\begin{array}{lll}
 U_+=(1-Y^{-1})Z_1P_1,&
 V_+=Y^{-1/2}Z_2P_1,&
 W_+=Y^{-1/2}Z_1P_2,\\
 U_-=(1-Y)Z_2P_2,&
 V_-=Y^{1/2}Z_1P_2,&
 W_-=Y^{1/2}Z_2P_1 .
\end{array}
\tag{9}
\]
Their index order is \(n,c,d\), as in (7)--(8). The remaining
literal entry factor is the same function of these indices before
and after projection. At each polynomial coefficient of its
original quantum expansion, (5) inserts the mask exactly. At a
fixed level, the finite-translation interpretation retains its
literal values at every supported integer index.

Consequently the finite matrices can be assembled using these
projected kernels and the original matching equations. The highest
cut, pivot, scalar framing and occupation marks have not been
changed. This describes the exact finite local projector. It does
not identify a chosen analytic resummation of the untruncated
coefficient function with its finite-level values, or turn the
finite-translation functional into an unrestricted analytic Gaussian
integral. Those are distinct source comparisons.

## 3. A complex domain with exponentially small projector error

First, the elementary scalar tail estimate is
\[
 |1-Q_N(N\zeta)|
 \le \frac{\bigl(|\zeta|e^{1-\Re\zeta}\bigr)^N}
                 {1-|\zeta|},\qquad |\zeta|<1.
 \tag{10}
\]
To prove it, use
\[
 1-Q_N(N\zeta)
       =e^{-N\zeta}\sum_{j=N}^\infty\frac{(N\zeta)^j}{j!}.
\]
The ratio of successive absolute terms after the first is at most
\(|\zeta|\). Also
\(\log N!\ge\int_1^N\log t\,dt=N\log N-N+1\),
so \(N!\ge(N/e)^N\). Summing the geometric bound gives (10).
In particular a compact subset of
\[
 |\zeta|<1,\qquad |\zeta|e^{1-\Re\zeta}<1
 \tag{11}
\]
has a uniform exponential error. Every real \(0\le\zeta<1\)
belongs to this domain.

For the actual coupled mask let
\[
\begin{split}
 r_{12}&=|\zeta_1|+|\zeta_2|,
 &\theta_{12}&=r_{12}
   e^{\,1-\sum_i\Re\zeta_i+|\zeta_3|},\\
 r_{13}&=|\zeta_1|+|\zeta_3|,
 &\theta_{13}&=r_{13}
   e^{\,1-\sum_i\Re\zeta_i+|\zeta_2|}.
\end{split}
\tag{12}
\]
If \(r_{12},r_{13}<1\), then
\[
 |1-Q_{S_N}(N\zeta)|
 \le\frac{\theta_{12}^{\,N}}{1-r_{12}}
       +\frac{\theta_{13}^{\,N}}{1-r_{13}} .
 \tag{13}
\]
Indeed the omitted triples lie in the union \(n+c\ge N\) or
\(n+d\ge N\). After taking absolute values, the first part is at
most
\[
 e^{-N\sum_i\Re\zeta_i}e^{N|\zeta_3|}
      \sum_{m=N}^\infty\frac{(Nr_{12})^m}{m!}.
 \tag{14}
\]
The binomial identity groups the \(n,c\) sum into \(m=n+c\).
Apply the same factorial and ratio bounds as above. This gives
the first term of (13), and the other part gives the second.
Possible overlap only improves this upper bound.

It follows that every compact subset of
\[
 r_{12},r_{13}<1,\qquad
                    \theta_{12},\theta_{13}<1
 \tag{15}
\]
has constants \(C,\delta>0\), independent of \(N\), for which
\[
                  Q_{S_N}(N\zeta)=1+O(Ce^{-\delta N}).
 \tag{16}
\]
This is an open complex domain containing the strict real
occupation polytope
\[
 \zeta_i\ge0,\qquad
               \zeta_1+\zeta_2<1,\quad \zeta_1+\zeta_3<1.
 \tag{17}
\]
For example, on the real polytope,
\(\theta_{12}=r_{12}e^{1-r_{12}}<1\); at \(r_{12}=0\)
the continuous value is zero. The other row is identical.

On smaller compact subsets, every fixed order of holomorphic
derivatives satisfies the same type of exponential estimate.
Choose a buffered complex polydisk still inside (15), apply
(13) there, and use the Cauchy integral formula. The derivative
order is fixed; this statement gives no bound uniform for orders
growing with \(N\).

For any fixed finite number of crossings the product of their
mask multipliers is likewise \(1+O(e^{-\delta N})\), provided all
their arguments stay in common compact subsets of (15). This
follows by expanding the product and using the finite number of
factors. Every source coupling remains present.

## 4. The contour estimate that would actually use this bound

At a physical scaling \(h=a/N\), \(a\ne0\), the arguments in (3)
are \(N\zeta_i\), with
\[
                        \zeta_i=U_i e^{\Xi_i}/a.
 \tag{18}
\]
At the stationary point of the original Poisson phase,
\(X_i=U_i e^{\Xi_i}\); hence \(\zeta_i=X_i/a\).
These are the original lifted logarithmic occupations. They are
not automatically tetrahedral angles. In particular shape
positivity alone does not choose their logarithmic lifts.

Here is the precise conditional analytic consequence. Suppose a
proved common cycle representation has two integrals
\[
 I_N=\int_{\Gamma_N}F_N,\qquad
 I_N^{\rm cut}=\int_{\Gamma_N}F_N\prod_\nu Q_{S_N}(N\zeta_\nu).
 \tag{19}
\]
Suppose the arguments obey (15) uniformly on the entire cycle,
the preceding product error is \(Ce^{-\delta N}\), and
\[
 I_N=cN^{-\beta}e^{NS}(1+o(1)),\quad c\ne0,\qquad
 \int_{\Gamma_N}|F_N|\le C_1N^A e^{NE}.
 \tag{20}
\]
If
\[
                            \delta>E-\Re S,
 \tag{21}
\]
then \(I_N^{\rm cut}/I_N\to1\). Indeed the absolute difference
is bounded by \(CC_1N^A e^{N(E-\delta)}\); division by (20)
proves the assertion. On a descent cycle whose absolute integral
has the same exponential rate as its nonzero saddle contribution,
every positive \(\delta\) suffices.

The common cycle in (19) is a hypothesis. Neither a formal Wick
identity nor a pointwise check at the stationary point supplies
it. Nor does (16) control the omitted parts of a larger cycle
outside (15). This estimate therefore preserves a supplied
contribution; it does not prove that the original knot closing
contains that contribution.

## 5. Complete direct sources and scope

| Label | Complete proof source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |

F supplies the literal matrices and original cut normalization;
P supplies the exact three-mean presentation and its principal
stationary equations. Both complete unchanged texts were read
in the current research sequence and their used implications were
checked; their matching pins were renewed. The finite support,
multiplier, estimates and conditional integral comparison are
proved above. The DLMF link is coverage only.

No mathematical program, numerical test, or build was used.
Public files and frozen manuscripts are unchanged. No finite-exception
or new volume-identity case is claimed.
