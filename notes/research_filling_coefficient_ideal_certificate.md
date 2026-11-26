# A finite coefficient-ideal certificate for all independently long fillings

Private research deduction, 15 November 2026.

The leading source amplitude need not itself avoid every long filling.
A finite identity among several coefficients of the **actual selected
expansion** can certify that some coefficient survives at every such
filling. This gives a stronger algebraic test than the coordinate-monomial
condition on the leading amplitude in
[the source-divisor theorem](general_long_filling_source_divisor.md).
It does not prove that an arbitrary fixed short component passes that
test, construct its selected expansion, or enlarge a proved knot class.

The certificate below is a displayed finite identity. Its proof does not
require choosing one neighborhood on which infinitely many germ-division
identities hold. No uniform quantum-level error over unbounded slopes is
asserted.

## 1. The exact source data required before forming the ideal

Fix an admissible template, a fixed short partial assignment, and the
original reduced, zero-framed Kashaev normalization. Let \(b\ge1\) be the
number of remaining crossing-circle cusps, with fixed signed integral slopes
\(\mathbf p=(p_1,\ldots,p_b)\), and put
\[
 \epsilon_i=p_i^{-1},\qquad
 U=\{\boldsymbol\epsilon:|\epsilon_i|<\rho\},\qquad
 U^\times=\{\boldsymbol\epsilon\in U:\epsilon_1\cdots\epsilon_b\ne0\}.
 \tag{1}
\]
Only tuples with the stipulated final knot and hyperbolicity properties
need be included; denote their actual knot complements by \(Y(\mathbf p)\).
Unfilled cusps and any already fixed short powers have
been specialized in the actual source before the coefficients below are
defined. Nonzero coefficients before that specialization do not suffice.

Partition all sufficiently large levels into finitely many infinite
classes \(\mathcal N_1,\ldots,\mathcal N_R\), for example the two parities.
This finite partition is fixed independently of \(\mathbf p\).
For every class assume a specified decomposition of the **whole original
scalar**, valid for every sufficiently long admissible fixed tuple:
\[
\begin{split}
 K_N(\mathbf p)
 ={}&L_{r,N}(\mathbf p)\,N^{\mu_r}
       e^{N S_r(\boldsymbol\epsilon)}
       \left[
          \sum_{j=0}^{M}c_{r,j}(\boldsymbol\epsilon)N^{-j}
          +E_{r,M,N}(\mathbf p)
       \right]
       +\mathcal R_{r,N}(\mathbf p),\\
 &N\in\mathcal N_r,\qquad
 |E_{r,M,N}(\mathbf p)|\le C_{\mathbf p,r,M}N^{-M-1}.
\end{split}
 \tag{2}
\]
Here (2) is available to every prescribed finite order \(M\); convergence
of its formal series is not assumed. The \(c_{r,j}\) are holomorphic on a
common \(U\), and \(\mu_r\) is fixed. The known factor \(L_{r,N}\) is
nonzero and satisfies
\[
 \frac1N\log|L_{r,N}(\mathbf p)|\longrightarrow0
 \quad(N\in\mathcal N_r)
 \tag{3}
\]
for each fixed \(\mathbf p\). The total complementary contribution has a
strict rate loss:
\[
 |\mathcal R_{r,N}(\mathbf p)|
 \le C_{\mathbf p,r}N^{B_{\mathbf p,r}}
      e^{N(\operatorname{Re}S_r(\boldsymbol\epsilon)-\delta_{\mathbf p,r})},
 \qquad \delta_{\mathbf p,r}>0.
 \tag{4}
\]
The actions have the same real part on these tuples:
\[
 \operatorname{Re}S_r(\boldsymbol\epsilon)=V(\boldsymbol\epsilon)
 \quad\text{for every }r.
 \tag{5}
\]
All constants and starting levels in (2)--(4) may depend on the fixed
tuple. The slopes are fixed before \(N\) tends to infinity.

The normalization in (2) must be constructed without dividing by the
unknown invariant or an unproved nonzero source coefficient. Original
framing phases, cut factors, and known nonvanishing slope prefactors
remain recorded in \(L_{r,N}\). For example, a proved filling determinant
factor with a marked branch and a factor such as
\(\prod_i\epsilon_i^{3/2}\) may be separated on the signed charts of
\(U^\times\). It is not itself required to extend holomorphically across
the coordinate faces. **Holomorphy of the remaining \(c_{r,j}\) at
\(\boldsymbol\epsilon=0\) is an additional requirement**, not a consequence
of having a pointwise expansion for every nonzero slope.

Likewise, \(c_{r,j}\) must already include the coherent sum of all
same-action contributions and exact aliases, the original closing row,
and the retained normal and endpoint terms. A transverse Gaussian block
or one unpaired contour contribution is not (2). One may instead absorb
\(\mathcal R\) into every fixed-order error if a whole-source estimate
proves that absorption; merely possessing formal coefficients does not
prove it.

These requirements are of the type used in the
[original long-filling transfer](general_original_source_long_filling_transfer.md),
with higher absolute coefficients retained. The
[directed all-order theorem](actual_all_circle_directed_all_orders.md)
proves such higher-order estimates in its already certified setting;
it does not supply them for arbitrary short partial fillings.

## 2. The finite certificate and its consequence

Assume that in every level class there are a finite \(J_r\), nonnegative
integers \(\nu_{r,i}\), and holomorphic functions \(g_{r,0},\ldots,g_{r,J_r}\)
on a common smaller polydisk such that the following is an actual identity:
\[
 \boxed{\quad
   \sum_{j=0}^{J_r}
       g_{r,j}(\boldsymbol\epsilon)c_{r,j}(\boldsymbol\epsilon)
       =\prod_{i=1}^{b}\epsilon_i^{\nu_{r,i}} .
 \quad}
 \tag{6}
\]
A germ identity suffices: only finitely many functions and identities
occur, so representatives and a single smaller polydisk can be chosen.

**Theorem.** Under (2)--(6), every independently sufficiently long
admissible fixed signed tuple has a nonzero first surviving coefficient
in every level class, at order at most \(J_r\). In particular the original
scalar is nonzero at every sufficiently large level, and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(\mathbf p)|
       =2\pi V(\boldsymbol\epsilon).
 \tag{7}
\]
If the same marked source action is separately proved to satisfy
\(2\pi V(\boldsymbol\epsilon)=\operatorname{Vol}(Y(\mathbf p))\),
then (7) is the original Kashaev volume identity for these tuples.

**Proof.** Shrink \(U\) so all the finite identities (6) hold. Choose a
slope threshold ensuring \(\boldsymbol\epsilon\in U^\times\) and the
assumed source estimates. Every right side of (6) is then nonzero.
Consequently, for each \(r\), there is a least
\[
 0\le j_r(\mathbf p)\le J_r,\qquad
 c_{r,j_r}(\boldsymbol\epsilon)\ne0.
 \tag{8}
\]
At this fixed tuple use (2) through order \(J_r\). All earlier terms
vanish, and its bracket is
\[
 N^{-j_r}
 \left[c_{r,j_r}(\boldsymbol\epsilon)+O_{\mathbf p,r}(N^{-1})\right].
 \tag{9}
\]
Dividing (4) by the magnitude of
\(L_{r,N}N^{\mu_r-j_r}e^{NS_r}c_{r,j_r}\) gives
\(\exp[-N\delta_{\mathbf p,r}+o(N)]\) times a fixed power of \(N\).
It tends to zero exponentially and is absorbed into the relative error.
Thus
\[
 K_N(\mathbf p)
  =L_{r,N}(\mathbf p)N^{\mu_r-j_r}
     e^{N S_r(\boldsymbol\epsilon)}
       c_{r,j_r}(\boldsymbol\epsilon)
       \bigl[1+O_{\mathbf p,r}(N^{-1})\bigr].
 \tag{10}
\]
Equations (3) and (5) give (7) along each class. There are finitely many
classes, so their common limit is the full-sequence limit, and their
eventual nonvanishing is full-sequence nonvanishing. The geometric last
assertion uses the additional stated action identification. \(\square\)

Only the finite expansions through \(J_r\) were used. All-order existence
makes it legitimate to seek a certificate without guessing its required
order in advance; it is not needed after (6) is exhibited.

There is also a uniform **coefficient-list** bound. On a smaller closed
polydisk, boundedness of the finite list \(g_{r,j}\) implies
\[
 \max_{0\le j\le J_r}|c_{r,j}(\boldsymbol\epsilon)|
   \ge C_r^{-1}\prod_i|\epsilon_i|^{\nu_{r,i}}
   =C_r^{-1}\prod_i|p_i|^{-\nu_{r,i}} .
 \tag{11}
\]
This is not a uniform estimate for the first nonzero coefficient or for
the scalar at a common finite quantum level. Its order may change with
the tuple, and the error constants in (2) may grow without bound.
Neither (10) nor (11) allows slopes to grow with \(N\).

One can use a common \(J=\max_rJ_r\) and common exponents
\(\nu_i=\max_r\nu_{r,i}\): pad the shorter lists with zero multipliers
in the identity and multiply its multipliers by
\(\prod_i\epsilon_i^{\nu_i-\nu_{r,i}}\).
A certificate in only one level class proves only that class's rate.
If the known normalization requires different choices in different slope
orthants, apply the hypotheses and certificate separately on those
finitely many orthants and take their maximum threshold. A level
partition whose number or modulus depends on the tuple is not silently
replaced by the fixed common family above.

## 3. Coordinate saturation is exactly the algebraic certificate

Let \(\mathcal O=\mathbb C\{\epsilon_1,\ldots,\epsilon_b\}\) be the local
ring of holomorphic germs, put \(t=\epsilon_1\cdots\epsilon_b\), and in a
fixed class set
\[
 I=(c_0,c_1,\ldots)\subset\mathcal O .
 \tag{12}
\]
The following conditions are equivalent:

1. A finite identity of the form (6) exists.
2. \(t^m\in I\) for some nonnegative integer \(m\).
3. \(I:t^\infty=\mathcal O\).
4. \(I\mathcal O[t^{-1}]=\mathcal O[t^{-1}]\).

Here \(I:t^\infty=\{f:t^mf\in I\text{ for some }m\ge0\}\).
These equivalences use only the definition of an ideal and localization.
For \(1\Rightarrow2\), take \(m\ge\max_i\nu_i\) and multiply the identity
by \(\prod_i\epsilon_i^{m-\nu_i}\). Conditions 2 and 3 are equivalent by
testing whether \(1\) belongs to the saturation. Condition 2 gives 4 by
inverting \(t\). Conversely an expression of \(1\) in the localized ideal
is a finite sum. Clear its finitely many powers of \(t\) to obtain 2.
Finally ideal membership \(t^m\in I\) is, by definition, a finite sum of
the generators with holomorphic germ coefficients. It supplies (6).

Thus the test is **unit ideal after inverting only the coordinate
parameters**. It is more than nonzero ideal, and more than the absence
of a common nonunit divisor. It is sufficient for the desired real
integer slopes; it is not asserted necessary, since the complex common
zero set could avoid those discrete tuples.

Noetherian finite generation, when invoked for \(\mathcal O\), merely
replaces \(I\) by some finite initial coefficient ideal. It does not
establish any of the four conditions. The finite certificate itself
requires no Noetherian argument: its finiteness already follows from
membership of a single \(t^m\) in the ideal. In particular no shrinking
neighborhood for each of infinitely many coefficient identities is used
in the proof of the filling theorem.

There is a simple normalization invariance. With \(h=N^{-1}\), if the
normalized formal series is multiplied by
\(u(h,\boldsymbol\epsilon)=\sum_{\ell\ge0}u_\ell h^\ell\)
with holomorphic coefficients and \(u_0\) a unit, then
\[
 c'_j=\sum_{\ell=0}^{j}u_\ell c_{j-\ell},\qquad
 (c'_0,\ldots,c'_J)=(c_0,\ldots,c_J)
 \tag{13}
\]
for every \(J\). The first inclusion follows from the displayed
triangular formula; recursive division by \(u_0\) gives its inverse
and the other inclusion. Hence the certificate is unchanged by these
known formal-unit normalizations. At the full-ideal level, multiplication
by any recorded factor invertible in \(\mathcal O[t^{-1}]\) likewise
preserves condition 4. Dividing by an unknown source zero, or by a
factor with an unaccounted divisor in \(U^\times\), is not such an
invariance.

If a separate exact construction places the coefficients and all
required multipliers in an algebraic coefficient ring mapping into
\(\mathcal O\), an identity in that ring or its coordinate localization
gives the same certificate after clearing denominators that are known
units. Other denominator divisors must remain in the source domain;
they cannot be inverted silently to obtain an all-slopes conclusion.
No rationality or algebraicity of the coefficients of an arbitrary
short component is asserted here.

## 4. What later coefficients can remove

For a purely algebraic illustration in two filling coordinates, take
\[
 c_0=\epsilon_1^2-\epsilon_2^2,\qquad
 c_1=\epsilon_2^2 .
 \tag{14}
\]
The leading coefficient vanishes along both diagonals, including
infinitely many arbitrarily long signed integer tuples
\(p_1=\pm p_2\). Nevertheless
\[
                       c_0+c_1=\epsilon_1^2
 \tag{15}
\]
is a certificate. Every tuple in \(U^\times\) has a surviving order at
most one, and on either diagonal the first surviving order is one.
This illustrates the algebraic improvement; these are not claimed to
be the coefficients of a knot source.

For a single remaining coordinate, every nonzero holomorphic
coefficient germ gives a certificate: write
\[
 c_j(\epsilon)=\epsilon^\nu v(\epsilon),\qquad v(0)\ne0,
 \tag{16}
\]
using its first nonzero Taylor coefficient, and multiply by \(v^{-1}\).
Thus, under the actual source estimates, a nonzero coefficient germ at
some finite order in every level class is enough for every sufficiently
long one-cusp filling. In several variables (14)--(15) show why a list of
coefficients can be stronger than checking only the leading amplitude.

The list in (6) is not a proposal to alter the invariant by a linear
combination of asymptotic coefficients. Its sole use is to prove that
the original expansion already has a nonzero first term.

## 5. Why the exact source does not automatically give the certificate

The [two-pole source calculation](actual_two_pole_source_contour.md),
§4, already distinguishes a zero leading source symbol from a zero
derived series. Its next coefficient can survive, but a whole selected
expansion and its first nonzero derived coefficient are additional
requirements. Formula (6) is a finite way to certify that survival
simultaneously for filling parameters once such coefficients exist.

The exact original period law gives a source-specific reason not to
infer the certificate merely from nonzero exact inputs or a nonzero
unpaired formal block. In the notation of
[the twist-period insertion theorem](research_twist_period_insertion_growth.md),
for every fixed degree \(d\ge1\) and signed power \(n\),
\[
\begin{split}
 P_{d,n+2Nk,N}
     &=\eta^k(P_{d,n,N}+kB_{d,n,N}),\\
 P_{d,n,N}
     &=2\eta^{-k}P_{d,n+2Nk,N}
                -\eta^{-2k}P_{d,n+4Nk,N},
 \qquad \eta=(-1)^{N-1},\quad k\ne0 .
\end{split}
 \tag{17}
\]
The complete original nilpotent insertion \(B\) has a nonzero local
asymptotic with augmented action \(W_0\) and all finite inverse-power
orders. The exact uninserted \(P\) has a strict loss below that action.
Consequently **every coefficient of the larger augmented sector
cancels** in the second line of (17), with the original normal data
retained. Finite-order algebra cannot recover the smaller sector by
declaring some coefficient of that larger sector nonzero.

The powers shifted by \(2Nk\) depend on \(N\), so (17) is not an
application of a fixed-slope filling theorem. Its role here is solely
the exact demonstration of coherent all-order cancellation in the
original source. The augmented sector in this demonstration is not
being identified with the desired filled geometric sector. It neither
disproves geometric survival nor proves that survival.

For an arbitrary fixed short partial filling, the missing assertions
therefore remain: construct the actual selected coefficient functions
with their closing/current data and a total remainder estimate, and
prove the coordinate-saturated ideal is the unit ideal in **every**
level class. Geometric existence or a transverse formal unit does not
prove those assertions. The separate geometric calibration must also
refer to this same selected action. The present result sharpens the
finite algebraic certificate to seek; it does not supply it for new
short components or settle the finite-exception conjecture.

## 6. Direct sources and proof scope

The proof of (6)--(16) is contained above. The five direct sources have
the following roles; none is used to infer the unproved hypotheses for
arbitrary short components.

- [Source divisor](general_long_filling_source_divisor.md), §§1--4, 7:
  absolute holomorphic leading amplitudes, partial-coordinate
  restrictions, coordinate-monomial survival, and level-class scope.
  SHA-256: dd2d27d482e1301683a15c026c08880fa99f1afecff291e49b9721e74508f7a6.
- [Original long-filling transfer](general_original_source_long_filling_transfer.md),
  §§1--5: original normalization, whole color/current gap, nonvanishing
  filling factors and the independent geometric calibration.
  SHA-256: b51fa1d6280e2c1027641d27561722ba0e9753c0a26f49c7d4c8e40ac8b47997.
- [Directed all orders](actual_all_circle_directed_all_orders.md), §§1--6, 9:
  actual all-order expansions with finite-order remainders and the
  restriction to the already certified source class.
  SHA-256: fa3ce585427f037b36f5ef4f201a7b1a521995434985f5ac95c37826305a46c6.
- [Twist-period insertion](research_twist_period_insertion_growth.md),
  §§1--5: the exact two-point reconstruction and cancellation at every
  algebraic order of the larger augmented sector.
  SHA-256: 45a5183609ddea6b8d69915efc7c86798157f3c16cedb17a94b4adff61531308.
- [Two-pole source](actual_two_pole_source_contour.md), §§1--4:
  the retained closing functional and the conditional first surviving
  derived coefficient.
  SHA-256: 792e0398e0b334a60fd159d1a728973544334692b128f02531dce2c864e48c9e.

Only written proofs and source-text reads were used. No numerical
calculation, mathematical execution, test, or compilation was performed.
