# Directed asymptotics and the canonical coefficient functional

This is a bounded follow-up to the earlier
[directed all-orders review](directed-all-orders.md). It records a fresh
read of Appendix M, its explanatory chapter, and the three split-monic
Lean modules. The accompanying
[snapshot](directed-monic-logic-followup-snapshot.json) fixes the versions
and the extent of each read. Earlier records are retained unchanged.

Two precision changes were made in the manuscript and matching note.
No further defect was found in the implications examined here. This is
not an exhaustive validation of the manuscript or a new proof of every
imported contour and geometric theorem. No manuscript build, Lean
compilation, or numerical source experiment was run for this follow-up.
Compilation and axiom checks reported elsewhere are separate records.

## The two changes

At Appendix M, Section 3.2, line 142, the comparison between the full
Hermite norm, the real interval norm, and the Chebyshev coefficient norm
now explicitly concerns canonical representatives of degree less than
$N$. Higher-degree products are first reduced by exact Chebyshev
folding. The matching paragraph in the standalone note was changed too.

The degree restriction is necessary. A nonzero multiple of the complete
modulus has zero values and first normals at its roots but need not
have zero interval norm. Thus the Hermite data do not define a norm on
unreduced polynomials of arbitrary degree. The actual source bounds
already make the correct distinction: (D4) is a norm on canonical
polynomials, while (D8)--(D11) control quotient reduction and fixed
products. The changed wording makes that existing argument explicit;
it does not replace a product by its values alone.

Appendix M, Section 8, and the matching note and chapter now use $r_P$
for the fixed order of an all-level operator. The source degree remains
$d=N-1$. Every occurrence of the operator order, including the translated
charts and the exponent of the meridian factor, was changed together.
In particular the retained first symbol is

$$
 (M-M^{-1})^{r_P}P_0(M,-L).
$$

The modified dimension $d_N(M)$ is unchanged. The operator, its order,
the diagram, and the signed crossing powers remain fixed before $N$
increases.

## The analytic chain checked in Appendix M

The theorem starts with a literal ordered all-circle tree, its actual
knot-producing endpoint pairing, and a directed certificate from
Appendix K. It retains the full edge sum over $0\le k<N$, the original
edge factors, the typed quotient relations, and the scalar normalization.
The source is not replaced by a product of absolute local coefficients.

The proof uses the following implications in this order.

1. **Exact source and strict first-charge margins.** Appendix M,
   Sections 1--2, imports the full-kernel, real/strip, connector, and
   first-charge estimates of Appendix K. A nonminimal charge has its
   own saddle contribution plus an absolute error already below the
   first charge. A relative error estimate at every small nonminimal
   saddle is neither assumed nor needed.
2. **Translated fixed compacts.** Section 3 works on a fixed compact
   subset of the upper half-plane and the finitely many translates
   needed by the operator. Euler subset products have uniform upper
   and inverse bounds there. The crossing interpolation is the actual
   formula (D14); its denominator stays away from zero on these
   compacts. Fixed crossing powers and their scalar carriers have
   bounded parameter dependence. The opposite-color channel is handled
   by its whole confluent trace, with its normal parameter independent
   of the moving edge parameter. Wrapped grid phases and endpoint
   currents remain in the trace.
3. **Local higher orders with global exact estimates.** Sections 4--5
   expand only the conditional first-charge saddle. The factorial
   expansions have summable differentiated remainders on a slightly
   larger complex compact. Outside that saddle the proof uses the
   exact normalized child messages and the strict exponential bounds,
   not a truncated local expansion. Division is by the exact complex
   value of the child message at zero. Its nonzero leading amplitude
   proves that this denominator is nonzero for sufficiently large $N$.
4. **Degree filtration.** Section 6 introduces $t=s/N$ only in the
   local interpolated first-charge integral. The wire Hessians and
   angular Schur complements give an invertible joint Hessian. The
   normalized local logarithm has the form
   $N[S(s/N)-S(0)]+\sum_{j\ge0}N^{-j}[C_j(s/N)-C_j(0)]$.
   Consequently its coefficient at $N^{-r}$ has degree at most $r+1$
   in $s$. This auxiliary local family is not a claim about the full
   physical source with $s$ of order $N$.
5. **Geometric identification.** Section 7 imports the positive
   augmented-cell construction, the marked charge path, and the
   preferred longitude identity. Backward restoration places the
   selected source saddle in the same small-angle uniqueness chart.
   The auxiliary longitude is semisimple at the filling point, so a
   commuting slope with the prescribed unit eigenvalue is projectively
   the identity. These are separate geometric inputs, not consequences
   of the asymptotic expansion or the Lean algebra. Their full proofs
   were not repeated in this follow-up.
6. **A genuine operator equation.** Section 8 requires a specified,
   fixed, nonzero rational operator that annihilates the whole reduced
   function at every sufficiently large level. A sampled recurrence or
   a finite microscopic jet does not satisfy this hypothesis. The
   finite-sum annihilator note supplies a separate existence theorem;
   this follow-up checked its opening source and pointing conventions,
   not its entire existence proof anew.

In the last step the gauge is exact:

$$
 \widetilde P=
 \sum_{j=0}^{r_P}a_j(q,M)(-1)^j
       \frac{f(M)}{f(q^jM)}T^j,
 \qquad f(M)=M-M^{-1}.
$$

Clearing the displayed denominators retains $f(M)^{r_P}$. After
regrading with $h=\log q$ and $u=hs$, substitution into a bivariate
formal series is injective: if $B(h,u)=\sum B_{ab}h^au^b$, then
$B_{ab}=[h^{a+b}s^b]B(h,hs)$. The vanishing coefficient identities
therefore imply

$$
 f(e^u)^{r_P}P_0(e^u,-e^{\mathcal S'(u)})=0.
$$

The formal series ring is a domain, so the displayed nonzero meridian
factor can then be cancelled. The separately identified geometric germ
gives one height-one Laurent prime. Its generator divides the first
classical symbol. This proves neither the full A-polynomial nor an
equality of ideals or multiplicities. Over the rationals the statement
uses contraction of the selected complex prime, not an assumption that
the individual complex component is defined over the rationals.

## What the split-monic modules actually establish

The definitions use ascending lists of coefficients over a commutative
ring. `CoeffEq` means equality of every coefficient, not agreement on a
sample of evaluation points. `timesLinear r` multiplies by $X-r$;
`monicMultiple roots` multiplies by the full product of those factors.
The root list includes multiplicity.

The following are concrete algebraic statements about these definitions.

| Module and declarations | Mathematical content | Necessary interpretation |
|---|---|---|
| `MonicRemainder`: `monic_division_identity`, `monic_remainder_degree_bound`, `top_coefficient_is_newton` | Successive synthetic division reconstructs the input coefficientwise as a multiple of the split monic modulus plus a remainder of smaller degree. The final Newton scalar is its top coefficient. | No division by root differences is used. Equal roots are allowed. |
| `MonicRemainder`: `double_root_remainder` | The remainder modulo $(X-r)^2$ is $f(r)+f'(r)(X-r)$. | The first normal is retained; it is not replaced by a second copy of the value. |
| `MonicLinearity`: `monicRemainder_congr`, addition/scaling lemmas, quotient invariance, padding lemmas | The constructed remainder and functional are linear and unchanged by coefficient-equivalent representatives, trailing zeros, or an actual multiple of the modulus. | Quotient invariance has an explicit coefficientwise multiple as its hypothesis. |
| `MonicUniqueness`: coefficient-degree, padded uniqueness, and idempotence lemmas | The degree condition may be stated coefficientwise, independent of the length of a padded list. A small-degree representative is unique. | The earlier list-length normalization is sufficient but is no longer the only available formulation. |
| `MonicUniqueness`: permutation lemmas | Reordering the linear factors, including repeated factors, leaves the remainder and functional unchanged. | The full multiset is preserved; deleting repeated entries would be a different modulus. |
| `MonicUniqueness`: `newtonFunctional_characterization` | A coefficient-invariant additive functional that kills every modulus multiple and has the prescribed top-coefficient value below the modulus degree equals the constructed functional on every input. | These hypotheses must be proved for the proposed functional on all polynomials. They do not follow from sampled levels or node values. |

The empty-list conventions are harmless algebraic boundary cases. The
application in Appendix N has a modulus of degree $N\ge2$. Monicity,
not a field or a distinct-root assumption, supports uniqueness. The
statements remain valid over rings with zero divisors. The characterization
does not need scalar linearity as an additional hypothesis: equality to
the already linear constructed functional proves it afterward.

No vacuous premise or replacement of coefficient equality by numerical
evaluation was found in these declarations. This was a semantic source
read; it did not rerun their compiler or axiom report.

## The normalization boundary: three different functionals

For a split monic polynomial $p$ of degree $m\ge1$, the abstract
functional identified by the Lean characterization is

$$
 \ell_p(F)=[z^{m-1}]\operatorname{rem}_p F.
$$

It has unit top-coefficient normalization. It is not the ordinary matrix
trace of multiplication, and it is not automatically the physical
quantum trace. In the fixed Newton conventions of the source-bound
note, equation (D5) explicitly sets

$$
 \phi_\sigma(F)=(-1)^{N-1}N^2
       [z^{N-1}]\operatorname{rem}_{P_\sigma}F,
 \qquad \sigma=s\text{ or }0.
$$

The factor $(-1)^{N-1}N^2$ is part of that source normalization. The
anti-diagonal Newton metric is checked in (D6); it is not built into the
split-monic definition. At the complete relation $P_0=\chi_N$,
$\phi_0=(-1)^{N-1}N^2\ell_{\chi_N}$.

The filling functional with a crossing multiplier is a further
operation. If $\widetilde f$ is the canonical polynomial with the
actual values of $f$ at all roots and the actual first derivatives at
the double roots, then

$$
 \mathcal L_N^f(H)=\ell_{\chi_N}(\widetilde f H).
$$

Appendix N, equations (8)--(15), supplies that concrete identification.
Its formula (10) contains $(fH)'$, including $f'H$ as well as $fH'$;
its odd simple root has a value term only. The actual signed crossing
power is supplied by the full-Hermite Gaussian (13), with the original
phase and lift retained. A scalar rescaling of an arbitrary functional
does not recover this multiplier or its first normals.

Accordingly the abstract characterization can identify the untwisted
$\ell_{\chi_N}$ once its hypotheses are established. To obtain the
twisted physical functional, one must separately prove the modulus,
Casimir relation, and the multiplier's value and normal data, then
apply the coefficient functional to their product. Agreement only on
spectral values is insufficient at repeated nodes. Appendix N's new
canonical-remainder proposition and the current formal README state
this boundary explicitly.

## Dependency skeleton for further formalization

The completed formal algebra supplies the first two steps below. The
later steps are mathematical application obligations, not consequences
of a successful compilation.

1. Construct the split monic modulus, quotient and remainder; prove the
   coefficientwise division identity and degree bound.
2. Prove linearity, quotient invariance, uniqueness, repeated-root
   behavior, permutation invariance, and the unit functional criterion.
3. Identify the actual Chebyshev modulus, its multiplicities, and the
   original Casimir relation. Establish the source trace normalization.
4. Identify the canonical crossing multiplier, including its first
   normals and scalar carriers, and derive the finite midpoint formula.
5. Prove the real/complex norm estimates for canonical representatives
   and the quotient reduction bounds for products.
6. Apply the exact physical tree recursion, global strict margins,
   local all-order expansion, and normalization without dropping phases.
7. Identify the actual geometric branch and apply a genuine fixed
   all-level operator equation to the filtered expansion.

This follow-up made the two stated clarifications and found no further
repair within its bounded scope. It does not certify unrelated source
classes, unpublished neighboring-spectrum transport, or the entire
manuscript.
