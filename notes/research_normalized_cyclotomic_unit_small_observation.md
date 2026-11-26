# A normalized quantum polynomial can have exponentially small root values

Private written deduction, 11 November 2026. Author-frozen after full
proof readback and checks of all three direct-source implications and
hashes. Independent review remains separate. This is an obstruction to
an arithmetic criterion for a comparison coefficient, not a knot
counterexample.

The existing fixed-algebraic-section theorem gives polynomial upper
and lower bounds once the actual observed coefficient has descended
to a fixed algebraic family. Integrality of finite quantum polynomials
does not supply that descent. The example below retains normalization
at one, reciprocal symmetry, quadratic degree growth, an exponential
coefficient bound, and even a root value which is a quadratic algebraic
unit. Its selected root value is nevertheless exponentially small.

## 1. Prime-power normalization gives nonvanishing, without a rate

Let \(N=p^k\), where \(p\) is prime and \(k\ge1\), and let
\(Q_N\) be a primitive \(N\)-th root of unity. If
\(F_N(q)\in\mathbb Z[q,q^{-1}]\) satisfies \(F_N(1)=1\), then
\[
                              F_N(Q_N)\ne0.                 \tag{1}
\]
Indeed multiply by a Laurent monomial to obtain an integer polynomial
with the same value one at one. If it vanished at \(Q_N\), division
by the monic minimal polynomial
\[
 \Phi_{p^k}(q)=1+q^{p^{k-1}}+\cdots+q^{(p-1)p^{k-1}}
\]
would give an integer polynomial quotient. Evaluation at one would
make \(1\) divisible by \(\Phi_{p^k}(1)=p\), a contradiction.
Irreducibility here also has a direct Eisenstein proof: substituting
\(q+1\) in \(\Phi_{p^k}\) gives an Eisenstein polynomial at
\(p\), since modulo \(p\) it is \(q^{p^{k-1}(p-1)}\) and its
constant coefficient is \(p\). In a nontrivial factorization into
monic integer polynomials, both reduced factors would be powers of
\(q\), making both constant terms divisible by \(p\) and their
product divisible by \(p^2\). Gauss's lemma then excludes a rational
factorization as well.

This argument contains no estimate for the modulus in (1).

## 2. An exponentially small quadratic unit within quadratic degree

For \(N=5m\), \(m\ge1\), define the single explicit family
\[
 F_N(q)=(q^{-m}-1+q^m)^N,
 \qquad Q_N=e^{2\pi i/N}.                              \tag{2}
\]
Its properties before root specialization are
\[
 \begin{gathered}
 F_N(q)\in\mathbb Z[q,q^{-1}],\qquad
 F_N(q^{-1})=F_N(q),\qquad F_N(1)=1,\\
 \operatorname{supp}F_N\subset[-N^2/5,N^2/5],\qquad
 \sum_j|[q^j]F_N|\le3^N .                              \tag{3}
 \end{gathered}
\]
The endpoint coefficients are one, so the Laurent width is exactly
\(2N^2/5\). The coefficient estimate follows from multiplying the
three-term polynomial \(N\) times and using the triangle inequality
for coefficient convolution. It asserts no positivity of its coefficients.

Put \(\zeta=Q_N^m=e^{2\pi i/5}\) and \(x=\zeta+\zeta^{-1}\).
Dividing \(1+\zeta+\cdots+\zeta^4=0\) by \(\zeta^2\) gives
\(x^2+x-1=0\). Since \(0<x<1\),
\[
 \alpha=x-1=\frac{\sqrt5-3}{2},\qquad
 \alpha'=\frac{-\sqrt5-3}{2},\qquad
 \alpha\alpha'=1.                                      \tag{4}
\]
Both are roots of \(X^2+3X+1\). Thus \(\alpha\) is an
algebraic integer and its inverse \(-3-\alpha\) is also integral.
It is a unit of norm one in \(\mathbb Q(\sqrt5)\).

Let \(\lambda=(3+\sqrt5)/2>1\). Equations (2)--(4) give exactly
\[
 F_N(Q_N)=\alpha^N\ne0,\qquad
 |F_N(Q_N)|=\lambda^{-N},\qquad
 \frac1N\log|F_N(Q_N)|=-\log\lambda<0.                 \tag{5}
\]
In particular (5) holds along every level \(N=5^k\), where the
normalization argument (1) also applies. There is no exceptional zero
or varying choice among conjugates in this calculation: the physical
root \(Q_N=e^{2\pi i/N}\) has been specified throughout.

The root value has degree exactly two over \(\mathbb Q\), despite
the growing degree of the ambient cyclotomic field. Its other conjugate
is \((\alpha')^N\), which has modulus \(\lambda^N\). More explicitly,
\[
 F_N(Q_N)\text{ has minimal polynomial }
 X^2-s_NX+1,
 \qquad s_N=\alpha^N+(\alpha')^N\in\mathbb Z.            \tag{6}
\]
Integrality follows either from the trace or from
\(s_0=2,s_1=-3,s_{n+2}=-3s_{n+1}-s_n\).
The two conjugates are distinct, which proves the degree assertion.
The naive coefficient height of (6) is
\[
                         |s_N|=\lambda^N+\lambda^{-N}. \tag{7}
\]
Thus this example does not meet a subexponential annihilating-height
hypothesis, even if one allows an annihilating polynomial of larger
degree: the reciprocal Cauchy root bound forces its height to be at
least \(\lambda^N-1\). It demonstrates precisely why the weaker bounds (3)
do not imply that hypothesis for the selected value.

## 3. Why a cyclotomic norm bound does not close the gap

For any nonzero algebraic integer \(a_N\in\mathbb Q(Q_N)\), its
field norm is a nonzero integer. If \(\sigma_0\) is the prescribed
embedding, then
\[
 |\sigma_0(a_N)|\ge
    \prod_{\sigma\ne\sigma_0}|\sigma(a_N)|^{-1}.       \tag{8}
\]
There are \(\varphi(N)\) embeddings. A common upper bound
\(|\sigma(a_N)|\le C N^A e^{BN}\) therefore gives only
\[
 \log|\sigma_0(a_N)|\ge
 -\bigl(\varphi(N)-1\bigr)
             \bigl(BN+A\log N+\log C\bigr).           \tag{9}
\]
When the cyclotomic degree is comparable to \(N\), this is a
quadratic exponential loss if \(B>0\). Even a polynomial bound at
each other embedding gives a potential \(N\log N\) loss, rather
than the required \(o(N)\). An estimate for the sum of the other
positive logarithms would be needed to improve this use of (8).

Even fixed degree and norm one do not solve the issue: in (5), the
single other conjugate supplies exactly the exponential loss. The
norm relation is satisfied without making the prescribed value large.

## 4. Relation to the existing algebraic and source criteria

The [critical-source theorem](irreducible_critical_source_and_whole_norm.md),
Sections 4--5, already proves two sufficient conditions: a nonzero
coefficient in a fixed finite algebraic extension of
\(k(t,Q)\), evaluated at \((t,Q)=(1/N,e^{2\pi i/N})\); or
an absolute integer annihilating polynomial of subexponential naive
height. The first yields polynomial bounds, and the second yields
subexponential bounds independently of its degree.
The family (2) satisfies neither condition. Both its internal power
\(m=N/5\) and its outer character \(N\) vary with the level.
The distinction between a fixed torsor and a controlled section is
also already established by the
[whole-unit weight theorem](whole_torsor_unit_weights_and_irregular_type.md).

The additional obstruction here is that the simultaneous finite
polynomial properties (3), even together with reciprocal symmetry,
prime-power nonvanishing and fixed-degree unit values, still permit
the exact decay (5). No claim is made that (2) is a knot invariant,
an actual tangle output, or a coefficient of its geometric period.
Nor does this calculation preserve an actual knot recurrence or its
pointing; those are further constraints which could exclude it.

For arbitrary fixed partial fillings, the actual prescribed observation
must therefore supply information beyond these polynomial bounds.
The source-adapted composition criterion already identifies a sufficient
analytic condition: controlled complementary feedback and a quantitative
overlap with the original closing row. The algebraic alternative still
requires a source-preserving descent to the critical-period coefficient.
Dividing an invariant by its proposed geometric exponential does not
make the quotient algebraic or construct that descent.

No finite-exception theorem follows here. The precise missing hypothesis
is not mere nonvanishing at each level; it is a lower bound at the correct
geometric normalization, uniform in the level and on the retained
boundary domain of each fixed partial filling.

## Direct source versions

The elementary proofs in Sections 1--3 are self-contained. The three
following sources are used for the comparison in Section 4.

| Source | Implication used | SHA-256 |
|---|---|---|
| irreducible_critical_source_and_whole_norm.md | Fixed algebraic section and subexponential annihilating-height criteria; descent is required for the actual coefficient | d1b10fb2bb1ef5c5621639b3bf6f045d4841fe7804d68826f12926008c35f7a5 |
| whole_torsor_unit_weights_and_irregular_type.md | Fixed whole torsors do not bound growing characters of their sections | 1bce81517db9617b788d2fc42b7ab4b7d5e25dbdb7fb606a5fc6c4ba51b18376 |
| research_source_adapted_observation_composition.md | Complementary feedback and prescribed closing overlap in the sufficient composition criterion | e4a1781624d76edad35f6cc6ff3639e22b315f8314b049edaea25bc8623c0d27 |

No numerical mathematical evaluation, test, import, compilation or
frozen-source edit is used.
