# A strict relative transport for the whole weighted word and its Green currents

Research proof, 27 October 2026. The actual complete finite word,
with every intermediate head projector, has a strict Fock-relative
extension. It carries the **whole weighted generating family** and
hence every explicit least-moment Green current, rather than only
the unweighted cut coupon. Its endpoint operators are specified
exactly. Under Mellin and Rees transport those endpoints and all
irregular projectors remain present.

This constructs an actual current/source map. It does not identify
its coefficient class with the internal geometric Gaussian class.
The final section isolates why the universal relative homotopy
does not by itself prove that additional nonzero image.

## 1. Whole crossing couplings realize the actual index moments

For each crossing in a fixed arbitrary b-strand word introduce a
unit coupling `w_t`. Multiply its literal transfer-k coefficient by
`w_t^k`, with its original positive or negative crossing convention.
Equivalently use the actual factorial `P_Q(w_t Z_t)` or the
appropriate inverse factorial, in its fixed Cartan/flip order.
At `w_t=1` this is the original crossing. No braid identity away
from that specialization is needed.

Introduce `w_0^(n_cut)` at the cut. All these coupled crossings
still conserve the integer sum of positions. Thus the cut matrix
is diagonal term by term, including before its remaining finite
internal sums. Consequently the original normalized-average cut
equals normalized ordinary trace for the **entire weighted family**:

    F_N(w)=framing_line*(1/N)Tr_(H^tensor b)
       [(w_0^ncut tensor g_2 tensor ... tensor g_b)
                  R_m^H(w_m)...R_1^H(w_1)].                   (1)

The original pivot, Cartan line, zero-framing scalar and full
external modified dimension are retained. This is an exact finite
polynomial in the weights. It is not an assumption of Ward closure
of the coupled word.

The [compact coherent source period](compact_coherent_source_period.md)
therefore supplies its exact fixed compact cycle and star-trace
calculus. Every weighted array and Green-current insertion below
uses that same cycle. No identification of its coordinates with
the internal geometric framing is assumed.

Put `E_i=w_i partial_(w_i)`. Every actual moment polynomial
`p(k_0,k_1,...,k_m)` is exactly `p(E_0,E_1,...,E_m)` applied to
this family. In particular the actual Green binomials are
`product_i binom(E_i,alpha_i)`. These are whole-function coupling
identities, not guessed extensions of a Taylor jet.

Here the closure is a knot: its braid permutation has one cycle.
Following that cycle expresses every initial position as the cut
position plus an integral linear combination of the crossing
transfers. The intermediate positions are then integral affine
functions of those same variables. Thus these weights account
for every actual free-flow moment in the knot problem. For a
link with several permutation cycles, retain one additional
initial-position weight per other component before making that
claim.

## 2. The exact Green currents are weight differential operators

Use the actual Green currents of
[the full certificate formula](full_certificate_framing_boundary.md).
For any finite zero-extended array `f`, the generating transform is

    Z_w[f]=sum_k w^k f(k),
    Z_w[S_i f]=w_i^(-1)Z_w[f],
    Z_w[p(k)f]=p(E_w)Z_w[f].                    (2)

The first equality includes the shifted support and its endpoints.
For the explicit Green word `i_1,...,i_n` representing `D^beta`,
let `p_(m-1)` be its backward-difference moment polynomial. Then
the generating current is exactly

    J_i(w)=-sum_beta A_beta sum_(m:i_m=i)
       p_(m-1)(E_w-e_i)
          product_(l=m+1)^n(w_(i_l)^(-1)-1) F_N(w).            (3)

The Euler operator in (3) acts on the **whole following product**,
including its weight coefficients. Moving it to act on `F_N`
alone would drop the actual index-shift correction.

The global Green identity becomes the whole source identity

    (-1)^h A_alpha F_N(w)
                       =sum_i(w_i^(-1)-1)J_i(w).              (4)

Thus the Koszul current complex of the actual zero-extended index
differences maps strictly to the weight-current complex with
differential given by the commuting factors `w_i^(-1)-1`.
Equation (1) supplies its actual finite-word/source realization.
Evaluation at `w=1` gives the original full scalar annihilation.

## 3. A relative functor for actual maps, including nonintertwining projectors

Let an actual completed source space `V` carry its fixed Fock
multiplication `T_V`. Define its relative source complex by

    delta_V f=((partial_sigma-T_V)f,f(0),f(1)).

Its coefficients are completed so that `exp(sigma T_V)` is
defined coefficientwise, as in the actual Mellin source theorem.
For a continuous actual linear map `O:V->W` define the strict
relative lift by

    O_rel(sigma)=exp(sigma T_W) O exp(-sigma T_V)

in degree one and in the bulk of degree two. Its endpoint maps
are `O` at zero and `exp(T_W)Oexp(-T_V)` at one. Direct
differentiation proves

    delta_W O_rel=O_rel delta_V.                 (5)

No commutation of `O` with the Fock operators is assumed. In
particular this applies to every actual crossing and every head
inclusion, projection and marked coupon.

For composable maps one has exactly

    (O_2 O_1)_rel=(O_2)_rel(O_1)_rel.            (6)

Take `T_(V tensor W)=T_V tensor I+I tensor T_W`. The exponential
then factors, so this transport also respects tensor products.
Finite head objects and the scalar target have `T=0`; their
actual pivotal caps and ordinary evaluation maps can be included
without introducing an infinite trace. All finite head inclusions
and projections remain explicit maps in this diagram.

The actual transgression obeys the exact naturality formula

    L_W O_rel=O L_V.                            (7)

It follows either by multiplying the integrand by `exp(-sigma T_W)`
or directly from its two endpoint terms. Thus this is a strict
relative source transport through a complete arbitrary word.

## 4. Actual moments and head projectors have explicit endpoint lifts

On a block edge the actual number is `n=j+N T B`. Since
`[n,T]=N T`, its relative lift is exactly

    n_rel=n-N sigma T.

For every degree-h polynomial the lift is

    p(n)_rel=p(n-N sigma T),

with the actual noncommutative operator order. It has sigma degree
at most `h`, and its endpoint operators are `p(n)` and `p(n-NT)`.
Multiedge polynomials and the actual transfer differences follow
by the tensor product and composition laws. Hence this construction
carries all the polynomial moments in (3), not only their constant
part or a top-degree projection.

The whole cut clock also has an exact formula. For `a=w^N`,

    (w^n)_rel=w^j exp[sigma(1-a)T] D_a,
    (D_a f)(t)=f(a t).                          (8)

This includes every coupling derivative and its finite endpoint
carry. Differentiating (8) at `w=1` recovers the displayed number
lift, including its `-N sigma T` term.

For the actual head projection `P=i pi_0`, `P T=0`. Therefore

    P_rel(sigma)=exp(sigma T)P,
    P_rel(0)=P, P_rel(1)=exp(T)P.                (9)

It is idempotent at every sigma because `P exp(sigma T)=P`.
Every intermediate projector in a word has its own factor (9).
It is not replaced by identity and is not asserted to be a
quantum-group intertwiner.

An explicit Cartan homotopy records its and every map's change:

    O_rel(sigma)-O
      =integral_0^sigma exp(t T_W)
                      (T_W O-O T_V)exp(-t T_V)dt.            (10)

This retains the inserted current rather than declaring a source
invariant. For polynomial moments its normal-ordered expression
is finite; the crossings and projector exponentials remain whole
functions in the specified completion.

## 5. Mellin, whole-R and Rees transport commute with this construction

Under the actual Fock Mellin map `T_V` becomes multiplication by
`u=Log U`; hence the endpoint in (9) is exactly `UP`. All
co-source conjugations and normal rows in the Mellin theorem
remain in (5)--(10). The exact normal-jet complex and its binomial
endpoint terms are obtained by taking jets of these whole formulas.

The Rees maps have the form
`C=D_eta exp(-p u/d)`, so they commute with multiplication by `u`.
They are therefore coefficientwise maps of these relative complexes.
For an actual transformed internal projector, the lift is

    (C P C^(-1))_rel(sigma)=exp[(sigma-p/d)u]P,                (11)

with the head eta flags retained in non-diagonal coupons. Its
endpoint is `exp[(1-p/d)u]P`, not a regular vacuum.

The whole coupled crossings are exactly those of
[the whole-R source factorization](rees_whole_crossing_source_factorization.md),
with its parameter `t` now the actual transfer weight. Both its
regular cyclic factor and its specified resonant/Cartan period
are kept; no separate root value of an infinite factor is taken.

Because the chosen source operators do not depend on the coupling
weights, (5)--(7) commute with all Euler weight derivatives and
Laurent weight factors in (3). Thus equations (1)--(4) transport
to this actual relative/Fock/Mellin/Rees source diagram as exact
cochain identities for a complete word, including every projector.

This does not discard the actual two-wall word curvature. It is
carried as an ordinary coefficient map in the same functor. The
[constrained-word source construction](constrained_verma_word_source_extension.md)
supplies a finite algebraic realization of those coefficients;
this relative lift adds their endpoint/current coherence rather
than replacing them. Its differentials, inclusions and retractions
can all be lifted by (5), degree by degree. Their exact chain
identities remain exact by (6); no commutation with the original
Fock multiplication is presumed.

## 6. An exact whole-source resummation shows what remains

Before taking any root limit, let the fully head-projected word be
`O_beta(w)=i_b B_beta^H(w) p_b`. Under a common Rees conjugation
its **whole** operator is exactly

    C_b O_beta(w) C_b^(-1)
      =exp[-sum_i p_i u_i/d]
           D_eta B_beta^H(w) D_eta^(-1) P_b.     (12)

Its relative version has `sigma` added to every displayed source
exponent. This resums the complete product of cyclic factors,
canonical periods and all internal projectors. It does not leave
an independently adjustable regular cyclic vacuum.

Applying the actual final source and co-source recovers the original
weighted finite period, and hence every Green moment, exactly.
But the coefficient in (12) is the original finite head word.
The source exponent is irregular and the head flags remain. This
identity does not evaluate the coefficient of its geometric
stationary block.

There is a precise homological limitation. The relative complex
is equivalent by its explicit transgression to its original
coefficient space in degree two. Therefore the functor (5)--(7)
preserves coefficient classes; it does not turn an unknown map
from the geometric Gaussian module into a nonzero one. To preserve
the geometric horizontal generator, that coefficient map still
has to be constructed through the irregular projectors (11)--(12).

At the geometric end the exact two framing currents already
computed in the full Green formula still have their marked
endpoint/carry defect. The actual source diagram above specifies
its own corresponding co-sources completely. What is not proved
is that the Gaussian pushforward sends one set to the other with
nonzero horizontal image. This is now a comparison of specified
whole current/source objects, rather than an unspecified boundary
normalization. No full scalar geometric factor or selected
volume growth is concluded from this relative transport alone.

The compact source construction supplies the actual global cycle
for the weighted family (1) and currents (3). The next geometric
pushforward must commute with its exact star product and current
maps while controlling degeneration or escape of the critical
family at the compactified polar divisor. That statement has not
been proved here.

[Exact relative-operator audit](../experiments/audit_relative_word_green_transport.py)
and [results](../experiments/relative_word_green_transport_results.json)
check the actual number and whole-clock lifts, Green binomial
moments, internal projector and ordered word composition. The
universal full Green formula is independently checked by
[the free-shift audit](../experiments/audit_full_certificate_green.py).
