# A finite first-symbol test for the actual full certificate

Research note, 6 November 2026. This gives a sufficient finite
valuation test on an **original full finite-array certificate**. When
the test holds, its least-moment scalar operator has the marked
geometric factor in its first nonzero \(H=\log Q\) symbol. The test
does not require cancellation of all framing currents or a nonzero
selected geometric period.

No broad class of the existing dimension-count certificates is
proved to satisfy the test. In particular this is not a geometric
factor theorem for the primitive minimal scalar operator. Sections
4–5 identify the precise retained terms that prevent an automatic
application of the construction, the source normalization, or Weyl
reflection.

## 1. The original certificate and the transverse moments

Start with the full normalized finite array of
[the sourced-telescoping criterion, Sections 2–3](sourced_telescoping_geometric_support_criterion.md).
Remove its common central root factor **before** specializing the
whole certificate at \(q^N=-1\), exactly as there. No central factor
of an individual specialized coefficient is subsequently discarded.

Choose the two actual framing coordinates used in
[the partial theorem, Section 4](partial_geometric_support_theorem.md).
Write their logarithmic coordinates as \(\chi=(\chi_1,\chi_2)\)
and the remaining \(r\) actual logarithmic coordinates as \(u\).
Their unit index shifts translate these coordinates by \(H\).
Set \(D_\chi=S_\chi-1\), \(D_u=S_u-1\). The specialized, nonzero
certificate is
\[
 P=\sum_{\gamma\in\mathbb N^2,\ \beta\in\mathbb N^r}
       A_{\gamma\beta}(H,M,T)D_\chi^\gamma D_u^\beta,
 \qquad PI=0.                                             \tag{1}
\]
The sum is finite. The meridian operator \(T\) and all its characters
are the original ones. The coefficients contain no multiplication
by either kind of internal coordinate. Let
\[
 h=\min_{A_{\gamma\beta}\ne0}(|\gamma|+|\beta|).             \tag{2}
\]
Suppose there is a multiindex \(\alpha\in\mathbb N^r\), with
\(|\alpha|=h\), for which \(A_{0\alpha}\ne0\). This is an
additional, explicit condition: the selected least moment uses
only the transverse indices.

The exact finite weighted-sum argument then proves
\[
 A_{0\alpha}F_N=0                                          \tag{3}
\]
for the actual fully summed reduced scalar at every sufficiently
large integer level. It sums both framing indices too and retains
their finite endpoints. No formal source is used in (3).

For a nonzero operator \(A=\sum_\ell a_\ell(H,M)T^\ell\), put
\(\operatorname{ord}_H A=\min_\ell\operatorname{ord}_H a_\ell\)
on the regular generic meridian chart. Finite negative orders are
allowed. Write
\[
 v=\operatorname{ord}_H A_{0\alpha},\qquad
 w_{\gamma\beta}=\operatorname{ord}_H A_{\gamma\beta}.       \tag{4}
\]
These are coefficient valuations, not the order obtained after
applying the operator to a selected solution.

Contract only the nondegenerate \(u\) block. With formal weights
\(s=(s_1,\ldots,s_r)\), use the phase \(S(\chi,u)+s\cdot u\)
and denote its original Gaussian block by \(Z(\chi,s,H)\).
The exact ratios, critical branch, half-density and base line are
those already proved in the partial theorem. In particular
\[
 Z_0:=Z(\chi,0,H)=C(H)e^{S_0(M)/H}
                       z_0(\chi,M)(1+O(H)),\qquad z_0\ne0.
                                                               \tag{5}
\]
The critical action \(S_0\) is independent of both framing
coordinates. The leading meridian ratio of \(Z_0\) is the marked
\(L_{\rm geom}\).

For every multiindex \(\delta\),
\[
 \frac{[s^\delta]Z(s)}{Z_0}
   =H^{-|\delta|}\frac{u_*^\delta}{\delta!}
      +O(H^{-|\delta|+1}).                                \tag{6}
\]
Indeed the critical action has derivative \(u_*\) at \(s=0\);
its higher derivatives and the Gaussian amplitude are formal
regular functions of \(s\). Expanding the exponential proves (6),
including its lower-order bound even where the displayed leading
coefficient vanishes. All logarithms are the original marked
lifts. This does not integrate either framing direction.

## 2. A coefficient-only sufficient test

**Proposition 1.** If every nonzero term in (1) with
\(\gamma\ne0\) and \(\beta\le\alpha\) componentwise satisfies
\[
 w_{\gamma\beta}+|\gamma|+|\beta|-h\ \ge\ v+1,              \tag{7}
\]
then the first nonzero \(H\)-symbol of the actual operator
\(A_{0\alpha}\) in (3) vanishes at \(L_{\rm geom}\). Its cleared
symbol therefore has the irreducible marked geometric factor.

Proof. Exact transverse translation, including the weighted phase,
transports (1) to
\[
 \sum_{\gamma,\beta}
 A_{\gamma\beta}D_\chi^\gamma
       \bigl((e^{-s}-1)^\beta Z(s)\bigr)=0.                 \tag{8}
\]
This is the same coefficientwise formal Gaussian identity as in
the partial theorem. In the coefficient of \(s^\alpha\), the only
term with \(\gamma=0\) is
\((-1)^h A_{0\alpha}Z_0\): by (2), all other such terms have
\(|\beta|>h\) or cannot contribute.

For \(\beta\le\alpha\), the remaining moment has relative order
at least \(-h+|\beta|\), by (6). Since \(S_0\) is framing
independent, each \(D_{\chi_a}=e^{H\partial_{\chi_a}}-1\)
increases that relative order by at least one. Thus the
\((\gamma,\beta)\) term has order at least the left side of (7).
Meridian shifts preserve the common WKB line and its \(H\)-order;
their leading factors are the original powers of \(L_{\rm geom}\).
Consequently
\[
 A_{0\alpha}Z_0/Z_0=O(H^{v+1}).                            \tag{9}
\]
Its \(H^v\) coefficient is exactly the initial symbol evaluated
at \(L_{\rm geom}\). This proves the assertion. The geometric
factor conclusion uses the marked irreducible branch, as in the
partial theorem. \(\square\)

A particularly simple sufficient version of (7) is:

* every \(A_{\gamma\beta}\) has valuation at least \(v\);
* each coefficient of total shift degree \(h\) involving a
  framing difference has valuation at least \(v+1\).

Terms of greater total degree then have the needed additional
order automatically. Both conditions are finite tests of the
original certificate coefficients. Multiplying the whole
certificate by a common nonzero scalar changes all valuations
equally and does not improve the test.

This conclusion concerns the constructed full scalar operator,
not every full scalar annihilator. Passing to a primitive
least-order right divisor can lose a factor carried by a
cofactor. The original full modified-dimension normalization
can be restored by the exact ordered peripheral gauge in the
partial theorem; its whole normal and root-restricted gauges
are not identified.

## 3. A weaker finite principal-current test

There is a useful explicit relaxation. Suppose the left side of
(7) is at least \(v\), and let \(\mathcal E\) be the finite set
where equality holds. Write \(a_{\gamma\beta}\) for the
coefficient symbol of \(H^{-w_{\gamma\beta}}A_{\gamma\beta}\)
at \(H=0\). Then the only possible order-\(v\) residual is
\[
 \sum_{(\gamma,\beta)\in\mathcal E}
 (-1)^{|\beta|}
 a_{\gamma\beta}(M,L_{\rm geom})\,
 \frac{1}{z_0}\,
 \partial_\chi^\gamma
 \left(z_0\frac{u_*^{\alpha-\beta}}
                  {(\alpha-\beta)!}\right).               \tag{10}
\]
Vanishing of (10) also proves (9).

To verify the formula, the leading \(s^\beta\) coefficient of
\((e^{-s}-1)^\beta\) is \((-1)^{|\beta|}\). All its higher
coefficients multiply moments with a strictly smaller pole
order in \(H\). The leading frame difference is
\(H^{|\gamma|}\partial_\chi^\gamma\). Substitution of (6)
therefore gives (10). An external meridian shift changes these
leading coefficients only by its indicated longitude factor.

Unlike (7), test (10) uses the actual geometric critical
coordinates and leading Gaussian density. It is nevertheless
a finite identity involving fixed derivatives and the marked
logarithms, rather than an all-order identification of relative
source modules. If any term has lower order than \(v\), its
higher expansions must also be retained; formula (10) alone
is not then the complete order-\(v\) test.

## 4. The existing construction does not enforce either test

The finite dimension-count construction uses all internal shifts,
including both framing shifts. Its boundary strata and common
denominator control the span; they impose no condition (7) on
the two filtrations \(H\)-order and shift degree.

This failure is algebraically visible within the same actual
certificate module. If \(P\) is a valid certificate, then
\(D_{\chi_1}P\) is also a nonzero valid certificate, because
the coefficient ring contains no internal multiplication.
Its least total shift degree is \(h+1\), and every least term
contains a framing difference. Thus neither validity nor the
dimension-count existence conclusion forces the required
framing-free multiindex. This observation does not prove that
a better choice is impossible.

Even when \(A_{0\alpha}\) exists, the retained term
\(\gamma=e_a,\ \beta=\alpha-e_j\) illustrates the leading
obstruction. If its coefficient has order \(v\), its contribution
to (10) is
\[
 (-1)^{h-1}a_{e_a,\alpha-e_j}(M,L_{\rm geom})
       \frac{\partial_{\chi_a}(z_0 u_{*,j})}{z_0}.          \tag{11}
\]
There is no remaining factor \(H\). The transverse first
moment contributes \(u_{*,j}/H\), while its framing translation
contributes \(H\partial_{\chi_a}\). The full Green formula
retains exactly these mixed moment currents. Flat Ward
covariance of \(z_0\) does not set the derivative of
\(u_{*,j}z_0\) to zero.

Equation (11) is a specified term that must cancel or be
excluded by a certificate construction; its coefficient is
not assumed nonzero for every knot or every chosen certificate.
The existing existence proof supplies neither its exclusion
nor the cancellation (10).

## 5. The original cut, relative endpoint, and reflection do not add an order

The normalized cut \(1/N\) is part of both the original array
and its geometric block. It is not an additional factor in a
ratio such as (9). This can be seen without an asymptotic
model: on the literal identity cut, take the actual first
moment
\[
 I_k=N^{-1}\mathbf1_{0\le k<N},\qquad J_k=k I_k .
\]
For \(D J_k=J_{k+1}-J_k\), its interior value is \(1/N\)
for \(0\le k<N-1\), and its last value is \(-(N-1)/N\).
Hence
\[
 \sum_kD J_k=0,\qquad
 \sum_{k=0}^{N-2}D J_k=(N-1)/N.                           \tag{12}
\]
The exact endpoint cancels an order-one bulk period.
Normalization alone gives no further vanishing. This is an
original cut-moment example, not a claim that this particular
current is a knot's chosen Green certificate.

The actual whole-word relative map makes the same term explicit:
for its Fock block shift \(\mathsf T\),
\[
 n_{\rm rel}=n-N\sigma\mathsf T,\qquad
 n_{\rm rel}(1)-n_{\rm rel}(0)=-N\mathsf T.                \tag{13}
\]
See [the relative-word construction, Section 4](relative_word_green_transport.md).
Under its Mellin map \(\mathsf T=\log U\). Its value may vanish
at \(U=1\), but its normal derivative retains \(-N\); the
endpoint cannot be discarded before normal transport. On the
physical root logarithmic section \(NH=2\pi i\), so the factor
\(N\) consumes rather than supplies a small \(H\)-order.

The [complete residual Ward theorem, Sections 3–5](residual_gaussian_ward_currents.md)
does prove the leading covariance of the actual density and
co-source. It also proves why its local Bernoulli adapter is
not invertible on the retained cyclotomic carries. The
[Gauss-wall source map, Sections 4–6](actual_gauss_wall_cut_current_complex.md)
keeps its degree-elevated binomial wall row, both cut endpoints,
and the second framing divergence. Its exact finite identity
is not an assertion that their separate Gaussian images have
an extra \(H\)-order.

Finally, [actual Weyl reciprocity](actual_weyl_descent.md)
relates the meridian to its inverse, with the precise original
character and shift. It is not an oddness identity for each
current in (11) on a fixed framing fiber. The Gauss-wall
complement exchanges its two cut rows while retaining the
second transfer-index current. It therefore does not prove
(7) or (10).

The remaining concrete task is now finite: construct an original
full certificate with a transverse least moment satisfying
(7), or prove its principal-current cancellation (10). The
current source identities do not yet do so. No AJ identification,
selected geometric survival, or scalar volume asymptotic is
inferred from this sufficient test.
