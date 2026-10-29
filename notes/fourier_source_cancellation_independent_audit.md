# Independent audit: actual Fourier currents can lose geometric support

Proof audit, 27 October 2026, of
[the actual Fourier cancellation theorem](actual_fourier_source_cancellation.md).
The actual current/source equations, cyclic contraction and nonzero
geometric formal block pass with the qualifications below. This does
not refute the volume conjecture or show that the original uninserted
knot period loses its geometric contribution.

## 1. The current and whole source are literal actual operations

For the original four-port tensor and B=diag(Q^b) on its second wire,

    W(T)=((I tensor B)T(I tensor B^-1)-T)/(Q-1)

has coefficient [q]_Q T on output offset q=d-b. For every integer
q, [q]_Q=(Q^q-1)/(Q-1) is a Laurent polynomial. Thus this is an
actual finite port current with unchanged support and source tensors.
It is not an assumed total Hopf action on a diagonal reshaping.

The identity-wire closure sets d=b, where the multiplier is exactly
zero. Therefore ptr_second W(T)=0 entrywise as a WHOLE rational
finite-matrix identity, including all its specified normal derivatives.
All original first-port bands, pivots, scalar phases and d_N(M) factors
remain. No root scalarity, source invariance on charged matrices or
positivity hypothesis is needed for this cancellation.

At the primitive root the raw Fourier kernel is Q_N^(jq)/N, so its
effect is exactly (J_(j+1)-J_j)/(Q_N-1), with cyclic j. There is
no further original-cut 1/N after fixing the first input. The printed
centered prefix inverse satisfies Dh=hD=I-P, and its nonconstant
Fourier eigenvalues are (Q_N-1)/(Q_N^k-1), all of modulus at most
one. The distance identity follows from orthogonal projection onto
the constant line. These statements concern the declared finite
root source complex, not a bound for the full word or its normal
germs.

Off root the actual whole Vandermonde inverse has its last-row
carry. Its transformed current is not the uncorrected cyclic
difference. The note explicitly uses the whole partial-trace
identity for normal sources, which is the correct scope.

## 2. The formal shift uses the specified proper root lift

The geometric construction uses the ORIGINAL open coefficient
model and its specified proper lift Q^(jq)/N. Multiplication by
[q]_Q is consequently exactly the external shift difference

    Z_W(v,H)=(Z(v+H,H)-Z(v,H))/(exp(H)-1).

This is a coefficient identity before Gaussian contraction. Formal
contraction at the shifted critical point commutes with that base
shift, by the same translated-critical-point argument used for the
partial certificate theorem. It is stronger than summing bounded
q asymptotics; every original finite-band term is retained first.

This identity is NOT asserted for the actual whole Vandermonde
inverse away from the root. Those two partial families agree on
the original roots but have different normal source germs. The
note preserves this distinction. Likewise the local critical
branch need not be periodic under v->v+2pi*i even though the
original finite root family is cyclic. Its global continuation/
selected source is precisely the issue being tested.

The critical action is frame-independent: on the open Fourier
critical family t=0, so the envelope derivative with respect to v
is t=0. The added vt term also vanishes there. Thus no derivative
of a moving leading phase has been omitted. With all common
base/peripheral lines retained,

    Z=C exp(S_geo/H)(A_0(v)+H A_1(v)+...),

the shift yields

    Z_W=C exp(S_geo/H)(partial_v A_0+O(H)).

The common line C can retain M-dependent peripheral data; the
v derivative does not replace or reset it.

## 3. Why the leading derivative is genuinely nonzero

The uniform actual principal-density theorem gives, on its marked
half-density cover,

    Omega_beta^2=-(T_beta/2) Omega_cut^2.

Here T_beta is independent of the representation's simultaneous
framing conjugation. This follows directly from its determinant
definition, not an imported torsion theorem. If S is the derivative
of simultaneous conjugation and G its adjoint action on sl_2,
the complex maps transform as

    A'=S A G^-1, D'=S D S^-1, M'=G M S^-1.

Use V_c'=S V_c and W'=S W G^-1 in its determinant ratio. The
same det(S) occurs in numerator and denominator, while det(G)=1;
they cancel. The last equality follows, for example, because
conjugation on all 2x2 matrices has determinant one and fixes the
scalar line, hence also has determinant one on sl_2.

The square-root ratio is a nonzero function whose square is
frame-independent. In characteristic zero its framing derivatives
are therefore zero. The fixed ordered phase/sign remains in its
marked line and cannot become an arbitrary v-dependent factor.

At completeness and fixed good A, s=A^-1-1 is fixed and

    Omega_cut=-dr wedge ds/[s(1+s)]
             =-(partial_v r/s) dlog A wedge dv.

The Fourier Gaussian normalization supplies the actual Jacobian
to the same exterior coordinate volume. Consequently

    A_0(v)=c(M,A) partial_v r,

with c nonzero and independent of v, up to the recorded fixed
Fourier phase. On the proved complete birational (A,p_e) chart,
r is a nonconstant rational function of eta=exp(v)=p_e^-1.
If partial_v A_0 vanished, then eta partial_eta r would be a
constant d. The rational derivative dr has zero residue at eta=0,
whereas d deta/eta has residue d. Thus d=0 and r is constant,
a contradiction. This proves nonzero leading current amplitude
on a dense regular open; its marked meridian germ remains nonzero.

The nonzero statement is at a GOOD first-position phase. The
highest-input a=0 specialization has the exact one-sided support,
but no nonzero geometric block is thereby proved at its A=1
boundary. These are two properties of the same actual family at
different first-input phases. They must not be presented as a
simultaneous one-sided highest-boundary counterexample. The
weaker, needed obstruction already follows: a genuine zero-source
actual family has nonzero regular geometric partial support.

## 4. A clean certificate proof avoids a unit-amplitude shortcut

The current multiplier is (exp(t)-1)/(exp(H)-1) in the enlarged
open phase. It vanishes at t=0 and carries H^-1. Thus the original
unit-principal-amplitude premise cannot simply be invoked for its
UNCONTRACTED current integrand. The exact shift constructs the
formal contraction, including those finite negative powers, and
the preceding proof makes its final leading coefficient nonzero.

There is a simple independent way to obtain its certified meridian
operator. Let D(eta) be an already constructed nonzero operator
annihilating the proper partial family J(eta) and its formal block.
The coefficient substitution eta->Q eta commutes with the meridian
Ore step, so D(Q eta) annihilates J(Q eta) and its corresponding
shifted block. A nonzero common LEFT multiple L of these two
operators annihilates their difference divided by Q-1, and hence
both the actual root current family and the SAME formal current.

Such a multiple needs only finite coefficient linear algebra.
If the two orders are r,s, seek X of order at most s and Y of
order at most r with X D=Y D_shift. There are r+s+2 unknown
coefficients and at most r+s+1 equations over the coefficient
field. A nonzero solution gives a nonzero common multiple,
since the Ore polynomial ring over a field is a domain: leading
coefficients multiply with an automorphism and cannot vanish.
Clear denominators in this exact combination before root/source
specialization, using the existing finite-array specialization guard.

Its nonzero formal current has the same leading action and a
nonzero coefficient on a dense open, so the original classical
symbol argument forces the same geometric A-factor. No independent
A-polynomial is inserted into an annihilator. The final actual
scalar current is nonetheless identically zero, and its scalar
annihilator is the unit operator. This establishes the claimed
loss of partial support in the source pushforward.

The exact audit script
[checks the coefficient/source complex](../experiments/audit_zero_source_fourier_current.py)
and its whole two-color carry guard. The analytic growth, selected
cycle and uninserted knot period are not determined by this example.
