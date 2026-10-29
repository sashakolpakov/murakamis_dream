# What rational jet rigidity fixes about a global period

Independent function-level audit, 27 October 2026. The all-level Ward
unfolding and norm-root transfer have the stated local uniqueness.
That uniqueness does not by itself identify the selected full knot
period. The distinction is precise: an analytic function, its formal
asymptotic germ, and its period functional are different data.

This note gives sharp uniqueness statements, explicit counterexamples,
and a minimal algebraic source criterion. No literature proof is used.

## 1. Exact coefficient rigidity really is uniqueness of a function germ

Let \(Q_N=\exp(2\pi i/N)\). Suppose
\[
 F(Q,z)=\sum_{j\ge0}f_j(Q)z^j,\qquad
 G(Q,z)=\sum_{j\ge0}g_j(Q)z^j
\]
have rational \(Q\)-coefficients, and for every fixed \(j\),
\(f_j(Q_N)=g_j(Q_N)\) for every sufficiently large \(N>j\).
Then \(F=G\) coefficientwise. For each fixed \(j\), a nonzero rational
function cannot have these infinitely many distinct zeros.
The exceptional bound can depend on \(j\).

Rationality can be weakened: it suffices that each difference has a
convergent finite Puiseux--Laurent germ at \(Q=1\), on the marked branch.
Indeed a nonzero such germ is \(c\,t^m(1+O(t))\), \(c\ne0\), after
\(Q-1=t^e\), and has no zeros sufficiently near the puncture.

If the resulting power series are holomorphic in \(z\) near zero on
an open \(Q\)-domain, equality of coefficients is equality of actual
analytic germs. On any connected continuation domain, with the same
paths and logarithmic sheets marked, the functions are equal.
There is no extra holomorphic function vanishing to all orders at an
interior point. Thus the literal factorial function in
[the unfolding theorem](unfolded_ward_factorial_and_regulator.md)
has no hidden local rational-coefficient freedom.

The regularity condition matters. On a punctured neighborhood of
\(Q=1\), choose the local logarithm and put
\[
 U(Q)=\exp\!\left(\frac{4\pi^2}{\Log Q}\right).
\]
It is a nonzero holomorphic unit there and \(U(Q_N)=1\) for all large
\(N\), but \(U\ne1\). It has exponential growth of order \(1/|Q-1|\).
For example \(1+(U(Q)-1)z\) preserves the constant coefficient one
and specializes to one at every \(Q_N\), while being a different
generic formal unit. Its coefficient is not rational or Puiseux
meromorphic at \(Q=1\), so it is excluded by the actual theorem.
This example does not change a fixed exact finite root contraction;
it shows why punctured holomorphy and exponential-type growth alone
do not replace coefficient rigidity.

## 2. Growing finite jets are not a continuity theorem for a global value

Equality of a coherent local function fixes any **specified continuous
formal contraction** of it: finite sums and products, substitutions of
positive formal order, and finite-jet functionals preserve equality.
For a \(z\)-adic linear functional into a field with the discrete
topology, continuity means that it kills \((z^B)\) for some finite \(B\).
This is an elementary consequence of continuity at zero.

Without such a property, agreement of growing truncations has no
uniform evaluation implication. For fixed \(a>1\),
\[
 A_N(z)=1,\qquad B_N(z)=1+a^Nz^N
\]
agree modulo \(z^N\), but \(B_N(1)-A_N(1)=a^N\).
Each is polynomial, with algebraic coefficients; the added term is
proper hypergeometric in \(N\). This family is not a second rational
coefficient unfolding of section 1. It is a level-dependent tail
which that theorem never claims to determine.

In a nilpotent matrix algebra \(z^N=0\) the tail is literally zero
and cannot change any fixed finite matrix contraction. In a whole
normal order \(z^N\) can instead be a nonzero normal parameter; a
divided source can see it. If a selected contraction requires at
most \(B\) normal jets, knowing those jets fixes that contraction.
What must be proved is that the comparison uses the same functional,
with its boundary carries and finite jet budget. The local Ward
unfolding alone does not construct that global comparison.

This is exactly why the source and first-normal terms retained in
[the norm-root period theorem](cyclic_ward_norm_root_period.md)
and in the divided-power calculations are necessary. Their equality
as local operators does not license replacing the full contraction
by a different cycle.

## 3. All formal WKB jets do not fix an analytic period at an irregular point

This is a different issue from exact rational coefficient uniqueness.
Let \(c=1-i\), and on a punctured \(h\)-neighborhood consider
\[
 P_0(h)=1,\qquad P_1(h)=1+\exp(-c/h).
\]
On a sufficiently small sector around the positive real ray,
\(\exp(-c/h)=O(h^m)\) for every \(m\). Thus both have the same
normalized formal power series, to every order. Both are holomorphic
on the punctured neighborhood and have exponential-type growth
\(\exp(O(1/|h|))\). Both even solve the same rational-coefficient
equation
\[
 (h^2\partial_h)(h^2\partial_h-c)P=0.
\]
Yet on \(h=i\epsilon\), \(\epsilon>0\),
\(\exp(-c/h)=\exp((1+i)/\epsilon)\). Therefore
\[
 \epsilon\log|P_0(i\epsilon)|=0,\qquad
 \epsilon\log|P_1(i\epsilon)|\longrightarrow1.
\]
Formal jets in one chamber do not control another marked root
direction without an analytic continuation and sectorial estimate.

Even on the same ray, adding a subdominant exponential changes the
global period while preserving all normalized dominant WKB jets.
It then leaves the leading rate unchanged, but is still an exact
global ambiguity invisible to perturbative jets.

Consequently “coefficients lie in the algebraic critical field” is
not a convergence assertion about a formal \(h\)-series. The series
\(\sum n!h^n\) already has rational coefficients and zero radius.
Nor does an algebraic optimizer rule out irregular-singular
exponentials or determine their global coefficients.

## 4. The missing source coefficient has a sharp linear-algebra criterion

Let \(V\) be a finite-dimensional global period space over a
characteristic-zero field. Suppose the retained normalizations fix a
functional \(\ell\) only on a subspace \(U\subset V\), and let
\(g\in V\) be the geometric period vector.

**Source criterion.** The value \(\ell(g)\) is forced by those data
if and only if \(g\in U\).

If \(g\in U\), this is immediate. If \(g\notin U\), extend a basis of
\(U\) by \(g\). Its dual gives a functional \(\mu\) with
\(\mu(U)=0,\ \mu(g)=1\). Then \(\ell+c\mu\) preserves every given
normalization and assigns any desired value to \(g\), including zero.
This is an exact criterion, without an asymptotic hypothesis.

Here is a function-level counterexample with a unique rigid optimizer.
Take the rigid algebra \(k\times k\), action \(S=(V,W)\), \(V>W\),
and period vector
\[
 \Pi(\epsilon)=(e^{V/\epsilon},e^{W/\epsilon}).
\]
Every normalized local amplitude is exactly \(1\), with all higher
jets zero; both points and the unique maximizing point are algebraic.
The two positive normalized functionals
\[
 \ell_+(a,b)=a,\qquad \ell_-(a,b)=b,\qquad \ell_\pm(1,1)=1
\]
give leading rates \(V\) and \(W\), respectively. All local functions,
actions, and normalized jets are identical. The differing datum is
the global source coefficient, which vanishes on the optimizer for
\(\ell_-\). A nonzero formal geometric quotient is compatible with
this example.

Strict positivity without quantitative control is also insufficient
when the source depends on the level. The normalized functional
\[
 \ell_\epsilon(a,b)=e^{-a_*/\epsilon}a+
                    (1-e^{-a_*/\epsilon})b,\quad a_*>0,
\]
is strictly positive on both points, but its period rate is
\(\max(V-a_*,W)\). What matters is nonzero **subexponential** geometric
weight, rather than positivity at each separate level.

A strictly convex/concave Rivin optimizer therefore supplies the
unique geometric critical point and its local nonzero Gaussian
block. Algebraicity supplies its critical field and local period
identities. Neither assertion by itself constrains \(\ell(g)\).
For a positive integral on a specified real domain, an ordinary
uniform density bound can supply that missing constraint; it
cannot be inferred for an unspecified complex quantum cycle.

Even strict convexity on one connected algebraic domain does not
choose that domain's integration class. For the same entire
integrand \(e^{-x^2/\epsilon}\), compare the normalized positive
functionals \(\frac12\int_{-1}^1\) and \(\int_1^2\).
Both send \(1\) to \(1\), while their period rates
\(\epsilon\log P_\epsilon\) are respectively \(0\) and \(-1\).
The action \(x^2\) is strictly convex with the unique algebraic
optimizer \(0\). The first rate follows by bounding below on
\([-\sqrt\epsilon,\sqrt\epsilon]\); the second by bounding below
on \([1,1+\epsilon]\) and above by \(e^{-1/\epsilon}\).
The changed datum is the marked relative cycle, not the function.

## 5. A useful sufficient global regularity hypothesis

Suppose a **constructed global comparison** gives a nonzero
geometric coefficient \(c(Q)\) which is meromorphic Puiseux at
\(Q=1\). Then
\[
 c(Q_N)=C\,N^{-\alpha}(1+o(1))
\]
on its marked branch, with \(C\ne0\); in particular
\[
 \frac1N\log|c(Q_N)|\longrightarrow0.                          \tag{5.1}
\]
Proof: substitute \(Q_N-1=2\pi i/N+O(N^{-2})\) in the first
nonzero Puiseux--Laurent term. Thus a nonzero rational or
algebraic-meromorphic global comparison coefficient cannot
hide an exponential suppression or infinitely many zero levels.

This is a practical target for torsor descent: construct the
global geometric projection and prove its coefficient belongs
to this field and is nonzero. Proving uniqueness of such a
comparison **if it exists** does not prove existence or
nonvanishing.

For clarity, the elementary rate-transfer statement is as follows.
If
\[
 P_N=c_NG_N+R_N,\quad
 \frac{2\pi}{N}\log|G_N|\to V,\quad
 \log|c_N|=o(N),\quad
 |R_N|\le \exp\!\left(\frac N{2\pi}(V-\delta)\right)
\]
for some \(\delta>0\), then
\((2\pi/N)\log|P_N|\to V\).
Indeed \(R_N/(c_NG_N)\to0\); upper and lower triangle bounds
then give the conclusion. This needs a bound for the **total**
remainder, not only for individual local critical points.

An algebraic alternative to Puiseux meromorphy suffices for (5.1).
If \(c_N\ne0\) satisfies an integer polynomial of degree \(d_N\)
and coefficient maximum \(H_N\), with
\(\log(d_NH_N)=o(N)\), then \(\log|c_N|=o(N)\).
After removing powers of \(X\), its constant and leading
coefficients are nonzero integers. For \(|c_N|\le1\),
\(1\le d_NH_N|c_N|\); for \(|c_N|\ge1\), the elementary
Cauchy bound gives \(|c_N|\le1+H_N\).
This condition is not automatic from algebraicity at each level:
\(c_N=a^N\) already has exponentially large height.

The later [critical-source theorem](irreducible_critical_source_and_whole_norm.md)
strengthens this criterion: \(\log H_N=o(N)\) alone suffices, with no
degree bound, by applying the geometric-series Cauchy bound to an
integer polynomial and its reciprocal. More substantively, a fixed
whole algebraic source on the actual exponential root arc has
polynomial upper and lower bounds without an absolute height
estimate. Irreducible field descent and a retained nonzero source
pairing then force the geometric coefficient to be nonzero; neither
source descent nor a total remainder bound is inferred from the
classical optimizer.

## 6. Consequences for the current repository claims

- [The unfolded Ward theorem](unfolded_ward_factorial_and_regulator.md)
  has exact rational-coefficient uniqueness, a marked local cyclic
  gauge, and a controlled norm on its stated compact chart. Its
  derivations and scope do not assert a global source coefficient.
- [The norm-root theorem](cyclic_ward_norm_root_period.md) transports
  the actual missing-edge class to the marked peripheral period.
  Its norm-one kernel and the selected internal knot contraction
  remain additional data; the full peripheral period does not
  determine a knot Bloch-period coefficient.
- [The partial support theorem](partial_geometric_support_theorem.md)
  constructs a nonzero formal geometric quotient before the final
  two-index contraction. The source criterion above explains
  exactly why this need not survive that contraction.
- The divided-power drafts make operator/source statements. Their
  positive ghosts lower total index by \(N\), so ordinary full
  weight-zero closure kills them. Their present stated scope
  does not claim a selected global relative pairing.

There is no free ambiguity in the **already specified actual**
period: [the all-level pointing theorem](all_level_a_period.md)
determines it from its actual operator and finite initial colors.
Changing its global functional, or adding a flat solution without
preserving that pointing, gives a different period and is not a
counterexample to that theorem.

The remaining logical step is consequently concrete. One must map
the actual selected source, including its divided normal row, into
the geometric quotient and prove a nonzero coefficient with
subexponential control, or construct an exact global period
comparison preserving that source and metric. Local jet uniqueness
then removes local freedom. It cannot substitute for this source
map or prove its value by itself.
