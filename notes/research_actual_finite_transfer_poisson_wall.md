# The actual finite-transfer Poisson wall and its peripheral normal

Private written proof, 18 November 2026.

The original highest-cut root array has a finite Poisson identity in
its crossing-transfer coordinates. Its coupled head constraints cause
no additional upper-head current: every such tail is killed by a
literal Gaussian coefficient. The remaining upper-transfer current
has an explicit original-source formula. Its complete value vanishes,
but a specified coefficient of its first peripheral normal is nonzero.

This distinguishes a finite-support identity from the untruncated
Poisson identity used in the local formal source calculus. No map
between their relative cycles, or scalar lower bound, is inferred.

## 1. Original source and homogeneous transfer coordinates

Fix a braid on \(b\) strands with \(m\) signed crossings and one-cycle
permutation. Cut its oriented knot at the original first strand, with
both cut occupations zero. Put
\[
 N\ge2,\qquad q=e^{\pi i/N},\quad Q=q^2,\quad
 c=b-1-\operatorname{wr}(\beta)\in2\mathbb Z,\qquad Y=Qx^2.
 \tag{1}
\]
The coordinate \(x\ne0\) retains the original meridian; choose its
local square root as necessary when differentiating in \(Y\).
Use the literal canceled entries of [F]:
\[
\begin{split}
 R^+_{b'+n,a-n;\,a,b'}
 &=x^{-a-b'+n}Q^{(a-n)b'}{a\brack n}_Q
                        (x^{-2}Q^{a-n};Q)_n,\\
 R^-_{b'-n,a+n;\,a,b'}
 &=x^{a+b'-n}Q^{-ab'}{b'\brack n}_Q
                        (x^2Q^{1-b'};Q)_n .
\end{split}
 \tag{2}
\]
Here Gaussian coefficients are their polynomials before restriction
to \(Q\), including for indices at least \(N\). There is no quotient
by a vanishing root factorial.

The transfer at crossing \(i\) is \(n_i\). Following the physical knot
from its cut, an underpass adds \(n_i\) to the occupation and an
overpass subtracts \(n_i\). Consequently every occupation is the
integer linear prefix sum of these signed transfers. Each transfer
is encountered once with each sign, so the final occupation is again
zero for every \(\mathbf n\in\mathbb Z^m\).

These assignments satisfy all crossing and closing matching
equations. Conversely a matched assignment with cut zero has exactly
these occupations, by induction along that traversal. Thus the
transfers themselves give an integral basis of the entire matching
lattice, not only coordinates on its positive part.

Write \(a_i,b_i\) for the input occupations and
\[
 o_i=\begin{cases}a_i-n_i,&i\text{ positive},\\
                  b_i-n_i,&i\text{ negative}.
       \end{cases}
 \qquad
 \mathcal P=\{\mathbf n:n_i\ge0,\ o_i\ge0\text{ for every }i\}.
 \tag{3}
\]
This is exactly the untruncated physical support. Indeed the over
input is \(n_i+o_i\). Starting from cut zero, every underpass with
\(n_i\ge0\) preserves nonnegativity and every overpass exits at
\(o_i\ge0\); the one-cycle traversal visits all segments. This proves
all the required nonnegative occupations and transfer bounds.
The converse follows from (2).

Let \(\mathcal I_\infty(x;\mathbf n)\) be the product of (2) on
\(\mathcal P\), and zero off \(\mathcal P\), with the original root
pivot and framing. More explicitly put
\[
\begin{split}
 H(\mathbf n)&=\sum_{i-}(a_i+b_i-n_i)
                         -\sum_{i+}(a_i+b_i-n_i),\\
 \Omega(\mathbf n)&=-T(\mathbf n)
             +\sum_{i+}o_i b_i-\sum_{i-}a_i b_i .
\end{split}
 \tag{4}
\]
Here \(T\) is the sum of the initial occupations on the \(b-1\)
closed strands. The monomial in the entire source is
\[
                x^{-c(N-1)+H(\mathbf n)}Q^{\Omega(\mathbf n)}.
 \tag{5}
\]
Thus \(\Omega\) includes the ordinary index-dependent pivot.
The root external line \(x^{-c(N-1)}\) is the one in [M, Section 2];
the ordinarily framed source of [F] instead has \(x^c\).
Their ratio is the retained factor \(x^{-Nc}\). We use (5)
throughout and do not change it after taking a peripheral normal.

For stage marks \(w_e\), write each occupation as
\(a_e(\mathbf n)=\sum_i A_{ei}n_i\). Their exact restriction is
\(\prod_e w_e^{a_e}=\prod_i\lambda_i^{n_i}\), where
\(\lambda_i=\prod_e w_e^{A_{ei}}\). Conversely the transfers themselves
are integer differences of neighboring occupations. Retaining all
independent transfer marks therefore retains the whole original
matching-lattice clock family, with the same monomial specializations.

## 2. Protected upper heads

Let
\[
                    \mathcal Q_N=\{0,\ldots,N-1\}^m .
 \tag{6}
\]
On \(\mathcal Q_N\), the extended array \(\mathcal I_\infty\)
is exactly the original finite root array. Thus the independent
upper-head bounds may be removed while all transfer bounds in (6)
remain.

Here is the proof, with the root zero evaluated only after Gaussian
cancellation. If \(0\le n,o<N\) and \(N\le n+o<2N\), then
\[
                       {n+o\brack n}_Q=0.
 \tag{7}
\]
For generic \(Q'\) its factorial quotient has numerator
\(\prod_{r=1}^{n+o}(1-Q'^r)\) and denominators with lengths \(n,o<N\).
The latter are nonzero at \(Q\); the numerator contains \(1-Q^N\).
Evaluating that quotient, which agrees with the Gaussian polynomial,
proves (7).

Suppose a supported path with all transfers below \(N\) has a
high occupation. At an underpass an occupation cannot decrease.
For an overpass to reduce an occupation from at least \(N\) to
\(o<N\), its input is \(n+o\) and (7) kills that local entry.
Hence, on a nonzero path, a high occupation propagates around the
physical knot until it reaches the prescribed cut zero, impossible.
All occupations of a nonzero term therefore lie below \(N\).

This is an identity of the full meridian source, not only at \(Y=1\).
It survives arbitrary index marks and all peripheral derivatives:
the killing factor (7) is independent of \(x\). No infinite sum is
required. Even before the zeros are used, (6) bounds every occupation
in absolute value by \(m(N-1)\), through its prefix formula.

The ordered Hardy factorization already removes upper heads by
finite diagonal barriers. The argument here is its direct
literal-entry counterpart for the Poisson current below. Neither
argument removes the transfer cutoff.

## 3. Exact finite Poisson current with coupled support retained

Introduce independent variables \(\lambda_1,\ldots,\lambda_m\) and
define the entire finite marked source and its normalized version
\[
\begin{split}
 Z_N(x;\lambda)&=\sum_{\mathbf n\in\mathcal Q_N}
                             \lambda^{\mathbf n}\mathcal I_\infty(x;\mathbf n),\\
 \mathcal P_NF&=e^{-\sum_i\lambda_i}
       \sum_{\mathbf n\in\mathcal Q_N}
                   \frac{\lambda^{\mathbf n}}{\mathbf n!}F(\mathbf n),
 \qquad
 F(\mathbf n)=\mathbf n!\,\mathcal I_\infty(x;\mathbf n).
\end{split}
 \tag{8}
\]
In particular \(\mathcal P_NF=e^{-\sum\lambda_i}Z_N\).
The exponential is an explicitly displayed normalization of the
transfer-marked source, not a change of its closing functional.
The original unmarked root scalar is \(Z_N(x;1,\ldots,1)\).
These are finite polynomials before that exponential is inserted.

Define \((\mathsf S_iF)(\mathbf n)=F(\mathbf n+e_i)\), using the
same extended, zero-supported array in (3). Direct differentiation
of the finite sum gives
\[
 \boxed{\quad
 \partial_{\lambda_i}\mathcal P_NF
       =\mathcal P_N(\mathsf S_i-1)F-\mathcal B_{i,N},
 \qquad
 \mathcal B_{i,N}
  =N e^{-\sum\lambda_j}\lambda_i^{N-1}
       \sum_{\substack{0\le n_j<N\\j\ne i}}
          \lambda_{-i}^{\mathbf n_{-i}}
                    \mathcal I_\infty(x;N,\mathbf n_{-i}) .
 \quad}
 \tag{9}
\]
Indeed differentiating \(\lambda_i^{n_i}/n_i!\) reindexes the
result to \(0\le n_i\le N-2\). The missing \(n_i=N-1\) term
of \(\mathcal P_N\mathsf S_iF\) is the displayed boundary term:
the factor \(N!/(N-1)!\) is \(N\).
For \(\lambda_i=U_i/h\) with fixed \(h\ne0\),
\(\partial_{\lambda_i}=h\partial_{U_i}\).

No coupled face was dropped in this calculation. If a translated
point violates (3), its value in \(\mathsf S_iF\) is zero. If a
previously unsupported point enters (3), its translated value is
retained in that same term. This is why reindexing on the rectangular
transfer box is legitimate despite the coupled physical support.
One must not subsequently replace this shifted amplitude by a
generic interior ratio with its boundary zeros canceled.

The points \((N,\mathbf n_{-i})\) in (9) are outside the finite
transfer box and can have occupation \(N\) or larger. They are
explicit boundary evaluations of (2), not entries of the finite
trace. Their role is precisely to record the failed upper reindexing.

## 4. The literal color block and the first peripheral normal

For each boundary point in (9), the \(i\)-th transfer is exactly \(N\).
The root identity
\[
             \prod_{r=0}^{N-1}(1-tQ^r)=1-t^N
 \tag{10}
\]
follows by comparing its roots and constant coefficient.
In (2) it gives the factors
\[
 \mathcal I_\infty(x;N,\mathbf n_{-i})
      =\chi_i(Y)\,\mathcal J_i(x;\mathbf n_{-i}),\qquad
 \chi_i(Y)=
       \begin{cases}1-Y^{-N},&i\text{ positive},\\
                     1-Y^N,&i\text{ negative}.
       \end{cases}
 \tag{11}
\]
Define \(\mathcal J_i\) by deleting just that whole color block
from the product. It is zero on unsupported boundary points.
Every remaining factor is a Gaussian polynomial or a Laurent
polynomial, so this definition is regular also where \(\chi_i=0\).
It is not division of a specialized zero by zero.

Put
\[
 \mathcal C_{i,N}
 =N e^{-\sum\lambda_j}\lambda_i^{N-1}
       \sum_{\mathbf n_{-i}\in\{0,\ldots,N-1\}^{m-1}}
                    \lambda_{-i}^{\mathbf n_{-i}}\mathcal J_i(x;\mathbf n_{-i}).
 \tag{12}
\]
Then the full marked current, with all framing and pivot factors,
satisfies
\[
 \mathcal B_{i,N}=\chi_i\mathcal C_{i,N},\qquad
 \mathcal B_{i,N}|_{Y=1}=0,\qquad
 (Y\partial_Y\mathcal B_{i,N})|_{Y=1}
                     =\epsilon_i N\,\mathcal C_{i,N}|_{Y=1},
 \quad \epsilon_i=\begin{cases}+1,&i+,\\-1,&i-.\end{cases}
 \tag{13}
\]
The derivative acts on the entire source along fixed \(Q\).
Derivatives of its other factors are multiplied by \(\chi_i(1)=0\);
they have not been omitted from a nonzero product.

There is a source-specific nonvanishing test for (13).
Suppose the oriented cut traversal meets crossing \(i\) at its
underpass before its overpass. For \(\mathbf n=Ne_i\), the
occupation is exactly \(N\) between those two visits and zero
elsewhere. This is a supported extended boundary assignment.
At crossing \(i\), the over input is \(N\), the under input is
zero, and the Gaussian factor is \({N\brack N}_Q=1\).
Every other crossing has transfer zero and Gaussian and color
factors one. Consequently
\[
 \mathcal J_i(x;0)
           =x^{-c(N-1)+H(Ne_i)}Q^{\Omega(Ne_i)}\ne0.
 \tag{14}
\]
For any \(x_*\) with \(Qx_*^2=1\), coefficient extraction from
the unnormalized boundary current therefore gives
\[
 [\lambda_{-i}^{\,0}]
 \left.e^{\sum\lambda_j}Y\partial_Y\mathcal B_{i,N}\right|_{x=x_*}
   =\epsilon_i N^2\lambda_i^{N-1}
                 x_*^{-c(N-1)+H(Ne_i)}Q^{\Omega(Ne_i)}\ne0.
 \tag{15}
\]
Thus this first normal is a nonzero function of the full independent
transfer marks for every such crossing and every \(N\ge2\).
If the overpass is encountered first, the assignment \(Ne_i\)
has a negative interval and this particular coefficient is zero;
no conclusion about its other marked coefficients is asserted.
When \(m=0\), there are no current equations or wall claims.

## 5. Scope and complete proof directs

The exact gain is the elimination of all upper-head tails and the
explicit surviving transfer-wall formula (9)--(15).
Its nonzero normal is an original marked source datum outside the
finite box. It does not assert nonvanishing after setting every mark
to one, nor a lower bound for the prescribed unmarked scalar.

The Poissonization in (8) uses transfer marks. It is not an assertion
that its finite amplitude is already the untruncated three-mean
Poisson amplitude of a local coherent crossing. Relating these
presentations to a Borel relative chain must preserve (9), its
coupled zero extension, and the complete peripheral germs (13).
Value-only cancellation at \(Y=1\) does not supply that pushforward.
No infinite sum, Gaussian interchange, or geometric-cycle claim is used.

The direct texts were read completely and their used implications
checked. Source matching and both framing conventions come from [M];
the two polynomial signed coefficients come from [F].
The transfer coordinates, root barrier and finite current calculation
are proved above. No additional results from their cited sources
are used.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |

Only written mathematics and source-text/hash operations were used.
Frozen notes and public manuscripts are unchanged.
