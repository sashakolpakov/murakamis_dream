# Independent integer filling shifts and the coefficient ideal

Private written proof, 15 November 2026.

Integer filling shifts preserve the original integer lattice. In the
reciprocal variables they are holomorphic maps tangent to the identity.
This note proves that invariance under these independent shifts would
give the coordinate-monomial certificate needed in the coefficient-ideal
lemma. The invariance is a further source hypothesis; it has not been
proved for an arbitrary short partial filling.

## 1. The algebraic statement

Let
\[
 R=\mathbb C\{x_1,\ldots,x_b\},\qquad
 \mathfrak m=(x_1,\ldots,x_b),\qquad t=x_1\cdots x_b,
 \qquad b\ge1.
 \tag{1}
\]
These are convergent power-series germs at the origin. For each
coordinate define the ring automorphism
\[
 (\sigma_i f)(x)=f(x_1,\ldots,x_i/(1+x_i),\ldots,x_b).
 \tag{2}
\]
Its inverse substitutes \(x_i/(1-x_i)\). Both substitutions are
well-defined on germs. If \(x_i=1/p_i\), (2) is exactly
\(p_i\mapsto p_i+1\), leaving all other filling integers fixed.

For an ideal \(I\subset R\), write
\[
 J=I:t^\infty
   =\{f\in R:t^r f\in I\text{ for some }r\ge0\}.
 \tag{3}
\]
This is an ideal and is saturated with respect to every \(x_i\):
if \(x_i^s f\in J\), then multiplying by the other coordinate
factors shows \(t^s f\in J\), hence \(f\in J\).

**Theorem 1.** Suppose \(I\ne0\) and
\[
                         \sigma_i(J)\subseteq J
                         \quad(1\le i\le b).
 \tag{4}
\]
Then \(J=R\). Equivalently, \(t^r\in I\) for some finite \(r\).
Only the forward shifts in (4) are needed.

In particular it suffices that \(\sigma_i(I)\subseteq I\) for
every \(i\). A weaker sufficient condition is
\(\sigma_i(I)\subseteq J\): applying \(\sigma_i\) to
\(t^r f\in I\), and using
\(\sigma_i(t)=t/(1+x_i)\), proves (4) by saturation.

## 2. Recovering a derivation from integer shifts

We use the standard separation property of Noetherian local rings:
for any ideal \(J\) in \(R\),
\[
                    \bigcap_{r\ge1}(J+\mathfrak m^r)=J.
 \tag{5}
\]
Indeed apply Krull's intersection theorem to the finite module
\(R/J\). The convergent power-series ring is Noetherian by the
usual Weierstrass theory. This is the only ideal-closure input;
no convergence of an infinite operator logarithm will be asserted.

Put
\[
                   D_i=-x_i^2\partial_{x_i},
                   \Delta_i=\sigma_i-1.
 \tag{6}
\]
Both operators send \(\mathfrak m^r\) into
\(\mathfrak m^{r+1}\) for \(r\ge1\), and annihilate constants.
On every finite Taylor quotient they are nilpotent. The explicit
one-parameter substitution
\[
       f(x)\longmapsto f(x_1,\ldots,x_i/(1+s x_i),\ldots,x_b)
 \tag{7}
\]
has derivative \(D_i\) at \(s=0\), and satisfies the additive
parameter law. On a finite Taylor quotient (7) is polynomial in
\(s\) and solves the finite-dimensional equation with generator
\(D_i\). Consequently, on that quotient,
\[
 \sigma_i=\exp D_i,\qquad
 D_i=\log(1+\Delta_i)
       =\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta_i^r,
 \tag{8}
\]
where both series terminate. This also follows directly on each
monomial from the binomial series for \((1+s x_i)^{-n}\).

If (4) holds, \(\Delta_i\) and every finite polynomial in
\(\Delta_i\) with zero constant term preserve \(J\).
For \(f\in J\) and any prescribed Taylor order, truncate the
last sum in (8) beyond that order. The result lies in \(J\)
and agrees with \(D_i f\) to that order. Therefore
\[
                  D_i f\in J+\mathfrak m^r
                  \quad\text{for every }r.
\]
The derivative \(D_i f\) is a convergent germ. Equation (5)
gives \(D_i f\in J\), and coordinate saturation now gives
\[
                         \partial_{x_i}J\subseteq J.
 \tag{9}
\]

Choose a nonzero \(f\in I\subset J\). Some Taylor coefficient
\([x^\alpha]f\) is nonzero. By (9),
\(\partial^\alpha f\in J\), and its value at zero is
\(\alpha![x^\alpha]f\ne0\). It is a unit in \(R\), so
\(J=R\). This proves Theorem 1. Notice that the proof never
differentiates an identity known only at integer values of \(p_i\).
It first requires the shift identities as holomorphic germ identities.

## 3. Finite source relations that would suffice

Suppose the actual normalized geometric coefficient functions in one
level class are \(c_0,c_1,\ldots\in R\), with the precise whole-source
meaning and remainder assumptions of
[the coefficient-ideal lemma](research_filling_coefficient_ideal_certificate.md).
Let \(I=(c_0,c_1,\ldots)\). Noetherianity provides a finite initial
generating list \(c_0,\ldots,c_L\); it does not give its shift
invariance or prove that \(I\ne0\).

If that list is not identically zero and, for each \(i,j\), one
proves a finite identity
\[
 t^{m_{ij}}\sigma_i(c_j)
        =\sum_{\ell=0}^{L}h_{ij\ell}(x)c_\ell(x),
 \qquad m_{ij}\ge0,\quad h_{ij\ell}\in R,
 \tag{10}
\]
then \(\sigma_i(I)\subseteq J\), and Theorem 1 applies.
It gives a finite identity
\[
                  t^r=\sum_{j=0}^{L}g_j(x)c_j(x),
                  \qquad g_j\in R,
 \tag{11}
\]
which is the required certificate. The identities (10) are one
possible way to establish the hypothesis, not additional relations
already known for the knot source. No effective bound on \(L,r\),
or on a slope threshold is supplied by this argument.

For example, a proved formal scalar transport
\[
 C(h,\sigma_i x)=U_i(h,x)C(h,x),\qquad
 C=\sum_{j\ge0}c_j(x)h^j,
 \tag{12}
\]
with \(U_i\in R[[h]]\), implies \(\sigma_i(I)\subseteq I\)
by comparing coefficients. In this sufficient example no inverse
of \(U_i\) is needed. The relation must already have extracted the
correct changed action and all known source normalizations. The
existence of the finite boundary twist operator does not itself give
(12): it acts on a boundary vector and its retained exterior, while
(12) concerns the prescribed scalar geometric expansion.

Applied in every fixed level class, with a nonzero coefficient ideal
and the same action/whole-remainder requirements as the earlier lemma,
(11) proves its all-independently-long filling conclusion after the
chosen short partial assignment. The present theorem supplies an
algebraic implication, not those unproved source hypotheses.

## 4. Independence and holomorphy are essential

Simultaneously shifting all fillings is insufficient. In two variables
the proper saturated ideal
\[
                         I=(x_1-x_2)
 \tag{13}
\]
is preserved by the simultaneous shift, because
\[
 \frac{x_1}{1+x_1}-\frac{x_2}{1+x_2}
             =\frac{x_1-x_2}{(1+x_1)(1+x_2)}.
 \tag{14}
\]
It contains no power of \(x_1x_2\). Its zero set includes all
tuples \(p_1=p_2\), however long. It is not stable under the two
individual shifts. This is an algebraic illustration, not a knot
counterexample.

Holomorphy at the reciprocal origin is equally important. The exact
finite-source alias \(1-e^{-2\pi i p}\) is invariant under integer
shifts and vanishes at every integer filling. In \(x=1/p\) it has
an essential singularity, so it is not an element of \(R\).
The [continuous Ward calculation](research_continuous_filling_ward_derivative_current.md)
exhibits this alias in the actual original closing and shows that
differentiating its integer-only deletion loses a value current.
There is no contradiction with Theorem 1: the latter requires genuine
holomorphic germ transport for the already selected coefficients.

Thus the remaining source problem can be stated without importing a
filling derivative from an integer identity: prove independent integer
shift relations such as (10), with the correct geometric action,
endpoint currents and original closing retained. The rational local
Gaussian unit proves nonvanishing of a supplied local block; it does
not prove that the whole scalar coefficient ideal is nonzero or that
these shift relations hold for it.

## Sources and scope

The shift-to-derivation and saturation arguments are proved above.
Krull separation (5) is the standard Noetherian local theorem; see
[Stacks Project, Lemma 10.51.4](https://stacks.math.columbia.edu/tag/00IP).
Its hypotheses apply to \(R/J\), independently of any knot statement.

The directly used local source versions are:

* `research_filling_coefficient_ideal_certificate.md`, SHA-256
  `7a88bd1053eef0bf3309316e78a6fed6fc6408ddbd619cead85f209e0e4c28da`:
  the meaning of the coefficient ideal, coordinate certificate and
  whole-source analytic hypotheses, especially Sections 1--3.
* `research_continuous_filling_ward_derivative_current.md`, SHA-256
  `86674dc234090b220dbd5972a65077b222c9eb52774db4098c82835cdebfe25c`:
  the literal integer-alias closing identity and the essential
  singularity distinction in Sections 5--6.

No derivative-stability or shift-stability assertion for an arbitrary
knot source is assumed to have been proved. No frozen manuscript was
edited, and no mathematical code, numerical test or compilation was
used.
