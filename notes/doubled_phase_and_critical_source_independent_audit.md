# Independent audit: doubled Rivin phases and critical source traces

27 October 2026. The current proofs in
[the doubled-phase optimizer](doubled_phase_rivin_optimizer.md)
and [the irreducible critical-source theorem](irreducible_critical_source_and_whole_norm.md)
pass independently, with the corrected requirement that a density on
a reducible etale algebra be a unit on every selected component.

## 1. The phase map and the optimizer

The fixed-meridian shape Jacobian is invertible by the stated
positive Lagrangian pairing. Its peripheral slopes satisfy
\(\tau_-=\overline{\tau_+}\), \(\operatorname{Im}\tau_+>0\).
Thus the doubled logarithmic phase Jacobian
\[
 \begin{pmatrix}1&-1\\\tau_+&-\tau_-\end{pmatrix}
\]
has nonzero determinant \(\tau_+-\tau_-\). The selected
normalized shape germ is genuinely etale over the two phase ratios.
The conclusion is local at the chosen place and is not an assertion
about the raw singular plane A-polynomial fiber.

On unit phases, the conjugation involution and local uniqueness
force \(w=\bar z\). Positivity persists. Stationarity on the affine
fixed-two-phase angle slice supplies the real edge equations;
the imaginary edge equations were already imposed. Strict
concavity then makes this point the unique global maximizer of
that entire affine angle fiber and its closure. This does not
assert such a positive optimizer at arbitrary remote phase values.

Writing \(u=x+ia,v=y+ib\), the derivative is
\(d\Phi=x\,db-y\,da\). Solving the phase Jacobian gives
\[
 \operatorname{Hess}\Phi
   =\frac1{\operatorname{Im}\tau_+}
       \begin{pmatrix}|\tau_+|^2&-\operatorname{Re}\tau_+\\
                       -\operatorname{Re}\tau_+&1\end{pmatrix}.
\]
It is positive definite with determinant one. The stated complex
algebraic formula is exactly the same calculation before the real
restriction. The rational cotangent formulas also prove the
claimed algebraicity of the constrained covariance. Neither
covariance is thereby the actual quantum Gaussian density.

The centered complete meridian and longitude signs are explicitly
retained as external characters. They must accompany any later
SL2 or quantum comparison.

The added global real corollary also passes. Within ONE fixed
affine edge-angle and logarithmic marking, equal unwrapped
boundary phases place two positive edge solutions in the same
strictly concave affine fiber. They coincide; the sine rule
then identifies their shapes. The phase map is a local
diffeomorphism at every positive point, so this global injection
is a diffeomorphism onto its open image, of absolute degree one.
Fixed edge winding numbers and unwrapped phases are essential.
This proves neither image convexity or surjectivity nor any
degree statement for the periodic phase torus or quantum cycle.

## 2. The marked regulator primitive and the H5 connection

Direct differentiation yields
\[
 d\left[\frac{R_--R_+}{i}
              +\frac{\widetilde u v-u\widetilde v}{4i}\right]
 =\frac{(u+\widetilde u)d(v-\widetilde v)
              -(v+\widetilde v)d(u-\widetilde u)}{4i}.
\]
Thus the bilinear correction and all signs are correct.
Conjugate fundamental-class marks and zero centered logs at
completeness give \(\Phi=-2\operatorname{Vol}\) without fitting
an additional integration constant.

For the displayed five-dimensional Heisenberg matrix,
the central entry of \(\Pi^{-1}d\Pi\) is
\[
 dZ-A_{\log}\,dQ_{\log}+B_{\log}\,dP_{\log},
\]
which vanishes exactly by the primitive equation.
Its curvature reduces to
\(2(du\wedge dv-d\widetilde u\wedge d\widetilde v)=0\).
Every product of three connection matrices is zero, so marked
transport is exactly identity plus the single and double ordered
integrals. The central initial value \(-8i\operatorname{Vol}\)
is essential; setting the four logarithms initially to zero does
not determine it.

This is a whole algebraic flat period connection, with generally
transcendental horizontal matrix. Exponentiating its additive
center is an analytic period evaluation, not an algebraic
character of the additive group.

## 3. Irreducible trace descent and finite moments

The trace pairing proof is exact: its Gram matrix is \(V^tV\)
for the Vandermonde embedding matrix. Hence the density
\(a=\eta(\psi)\) is uniquely reconstructed from the stated
\(d\) moments by \(G^{-1}m\). In a rank-one line over a FIELD,
nonzero source and nonzero co-source imply \(a\ne0\).
Every embedding coefficient is then \(\sigma_i(a)\ne0\).
The normalization \(\lambda(\psi)=1\) is a convenient sufficient
certificate, not a necessary one.

For higher-rank lines the normalization still certifies
\(a\ne0\), but mere individual nonvanishing does not, as stated.
For a reducible etale algebra a faithful normalized matrix trace
sees every primitive idempotent with weight rank/dimension.

The density multiplying that faithful trace must be a UNIT on
every selected etale component. Mere nonzero density is insufficient:
\((1,0)\) in \(F\times F\) would kill the second component.
The current note now includes this correction.

Neither critical-field irreducibility nor normalized trace
descent has been proved for an actual global geometric quotient
of the quantum state. The explicit component, splitting-field
and already-closed-scalar qualifications are necessary.

## 4. The whole arc and height estimates

Distinct exponentials with polynomial coefficients are linearly
independent: the stated differential operators isolate one
exponential with an invertible operator on its polynomial factor.
Their order-\(m\) constant-coefficient equation bounds the zero
order at the origin by \(m-1\). Hence every fixed nonzero rational
coefficient on the physical source slice has finite vanishing
order. Applied to a polynomial relation with nonzero constant
and leading terms, Cauchy bounds and their reciprocals give
polynomial upper and lower bounds for ALL specialized conjugates.
This argument does not need bounded absolute cyclotomic degree.

The degree-independent naive-height inequality
\((1+H)^{-1}\le|\alpha|\le1+H\) is correct after removing
zero constant powers and reversing the polynomial for the lower
bound. The bounded-Weil-height counterexample is also correct:
the displayed monic polynomial is Eisenstein at two, and all
roots of modulus at least one lie in the disk centered at \(2^N\)
with radius two. The fixed-point map there is a strict contraction
for every \(N\ge2\), so only its one real root lies outside the
unit disk. Its Weil height stays bounded while its chosen
archimedean value grows exponentially.

The resulting finite-sum rate theorem correctly requires a
strict TOTAL dominance gap or a smaller-rate bound on any total
remainder. Rivin concavity alone supplies neither global period
descent nor that gap over all complex sectors.

These are substantive sufficient theorems for a proposed whole
source comparison. They do not prove its existence or the
selected volume limit.

## 5. Precise scope of the optimizer algebraicity

The current proofs already establish the claimed classical
algebraicity under their stated positive gluing/rank inputs:
[geometric rigidity](geometric_rigidity_and_cyclic_source.md) Section1,
[doubled phase optimization](doubled_phase_rivin_optimizer.md)
Sections3--5, and
[whole comparison rigidity](whole_period_cyclotomic_rigidity.md)
Section1. No algebraicity correction is needed in those statements.
It is not a new conclusion obtained from quantum jets.

Here is an independent short proof. Let F be the peripheral
coefficient field and K=F(z_1,...,z_t) the selected shape field.
Differentiate the normalized polynomial gluing equations over F.
The invertible shape Jacobian gives J(dz_j)=0, hence every dz_j=0
in Omega_(K/F). If K/F had positive transcendence degree, choose
a transcendence basis and its coordinate derivations. In
characteristic zero each extends uniquely over the remaining
finite separable field extension, producing a nonzero derivation
of K. But all dz_j=0 makes every such derivation zero, a
contradiction. Thus K/F is finite algebraic. The complete
normalized isolated point has F=Q with its recorded algebraic
lift characters, and therefore has algebraic shape coordinates.

For the ordinary one-cusped geometric branch the correct field
is the function field of its marked peripheral CURVE,
Frac(Q[M^+/-1,L^+/-1]/(A_geo)), after choosing the component
and normalized place. M and L are dependent. The result is
already finite algebraic over the meridian field Q(M) locally.
It is not a claim that arbitrary independent complex M,L give
a geometric shape solution, or that all shape coordinates are
integral over the unlocalized full polynomial ring Q[M,L].

At the complete parabolic lift, M=+1 or -1 and the selected
longitude character is retained. This gives algebraic numbers
for the UNFRAMED ideal shapes. The raw actual braid critical
scheme still has its two framing directions: its other shape/
position coordinates become algebraic numbers only after those
framing marks are fixed algebraically as well. Fixing a meridian
alone does not isolate that entire framed critical scheme.

Strict concavity identifies the unique positive real stationary
point on the stated affine angle fiber. Complex transversality
and polynomial gluing, rather than uniqueness alone, supply the
algebraicity. With two independent boundary PHASES the doubled
curve is the appropriate algebraic cover; those phase variables
are not two independent full peripheral holonomies.

Algebraic shapes do not imply algebraic logarithms or regulator
values. The regulator is a transcendental FUNCTION/period of its
algebraic connection; this wording makes no theorem that the
particular hyperbolic-volume NUMBER is transcendental. For
definition/coverage only, see
[Zagier, The Dilogarithm Function, Sections I.3--4](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf).
No proof from that source is imported here. The actual selected
wall coefficient2^-N supplies a concrete reminder that even
nonzero algebraic source values can have exponential size: all
weight-N characters must be retained before applying a bounded
whole-algebraic coefficient argument.

## 6. The whole selected-line polar criterion

The [whole selected-line theorem](whole_selected_line_polar_character.md)
also passes independently. On the EXACT marked ray
s_N=kappa N^(-1/e), kappa^e=pi i, a meromorphic rank-one
connection integrates to C s^rho exp(B(s)+H(s)), with finite
B=sum b_r s^-r and convergent H holomorphic. Its normalized
log modulus is exactly the displayed finite sum of distinct
powers N^(r/e-1), plus O(logN/N). The r=e contribution is
2Im(b_e); terms r>e can contribute zero only when each real
coefficient vanishes on that ray. A fixed meromorphic frame
changes dlog only by a logarithmic pole and preserves B.

The logarithmic quotient by exp(S_geo/h) gives the stated
volume rate and O(logN/N) error. This is a genuinely useful
sufficient GLOBAL target, not an assumption that a local
Gaussian block is the actual selected invariant. For a perturbed
physical ray the polar primitive must first be pulled back to
that exact ray; imaginary leading high poles can otherwise
produce real lower terms. The theorem uses the exact ray and
does not make that mistake.

The accumulating zeros of a sum of two different exponential
characters correctly obstruct a single meromorphic selected
line. The amplified whole-unit example has primitive
-2i pi^2/h and normalized rate -4pi^2 as printed. Existence of
the ACTUAL selected line, its original co-source and its marked
leading regulator character is still the new theorem to prove.

