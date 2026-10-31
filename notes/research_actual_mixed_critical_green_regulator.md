# Correct mixed-color symbols at a critical signed Green collar

Unpublished workspace research theorem, 31 October 2026. Internally
reviewed local source identity, with exact author verification and a
fresh independent portable replay for both reciprocal auxiliary flags,
both central lifts and every retained half sign. This
repairs the color error in the quarantined20/25-symbol notes.
The universal Gauss maps in those notes were correct, but their
symbols had put color-1 on an auxiliary strand whose color is not-1.

The result below concerns the ACTUAL mixed crossing Bloch sum on the
stated regular critical collar. It does not identify that sum with
the original globally sewn relative fundamental class. The latter
has a nonunipotent peripheral-decoration correction still to check.

## 1. Literal mixed source and its monomial terms

Use actual_mixed_crossing_circle_preferred_longitude.md, sections1--3.
For input colors chi1,chi2, physical A=chi1/K1,B=chi2/K2 and
C=1/(1-E1 F2), the literal positive mixed coefficient gives

    beta_mix=[B]+[C]+[chi1²/A]-[BC]-[chi1² C/A].              (1)

Thus, in the universal Gauss coordinates, the five shapes are

    chi2/K2, 1/d, chi1 K1, chi2/(K2 d), chi1 K1/d,
    with coefficients +,+,+,-,- and d=1-E1 F2.              (2)

The colors exchange places under the actual crossing. The same
universal Gauss update applies to arbitrary Casimirs; this is why
the previously verified matrix maps survive the correction.

There is also an explicit non-dilog part. Let l1=Log chi1,
l2=Log chi2, a=Log A,b=Log B,t=Log C, with the ORIGINAL unwrapped
Cartan and parity branches. Writing the leading coefficient as
exp[N W/(2pi i)], the literal mixed formula gives

    W=sum beta_mix Li2 - Li2(1) + W_mono,
    W_mono=l1 l2 +t²/2-l1(b+2t)-l2 a+l2 t
                         +(a-t)(b+t)+pi i t.               (3)

Indeed these terms come respectively from q^(alpha beta/2),
q^(k²-k), chi1^(-b_index-2k), chi2^(-a_index+k),
Q^((a_index-k)(b_index+k)), and (-1)^k. The -k in q^(k²-k)
is a finite prefactor, not an order-N action term.
The coefficient Li2(1) is real. Equation (3) is not permission
to remove the closing pivot, source cups/caps or integer marks.

All non-dilog terms in (3) have the real-quadratic/imaginary-linear
form of the recorded wall-regulator identity. Therefore the exact
matched-sheet relation is

    Im W-D(beta_mix)=rho dot Im(gradient W),                (4)

including ALL logarithmic variables and monomial terms.
At an open crossing the right side need not vanish. A unit-modulus
color makes its own rho_color zero, not every boundary contribution.
The original auxiliary pivot and source closure phases must still
be sewn before invoking any global full-stationarity cancellation.

## 2. Actual auxiliary colors from the selected raw flag

Keep the critical physical chart of the quarantined algebraic lemma:

    s=sin(pi delta), k=cos(pi delta), 0<delta<1/2,
    c=b+(x+y)/s², R0=-1, sigma=tr P=-2+4s².

The main colors are exactly-1. In the source flag convention a raw
head G has selected eigenvalue chi^-1, while the physical meridian
is -G. This fixes the auxiliary color, rather than inferring it
from the symmetric trace alone.

For the displayed untwisted raw auxiliary

    M0=(2P-sigma I)/(4sk),

its selected J-line eigenvalue is +i, so chi_aux=-i. Reversing
its central lift reverses chi_aux. For the displayed retained-half
matrices

    M_+=((sigma+1)I-P)/(2s), M_-=-(P+I)/(2s),

the selected raw eigenvalue is -i exp(pi i epsilon delta);
therefore

    chi_aux=i exp(-pi i epsilon delta)=epsilon s+i k.       (5)

Again a central lift multiplies both the raw eigenvalue and chi
by the same sign. Independently, choosing the RECIPROCAL raw
P eigenflag replaces the displayed eigenvalue and chi by their
inverses. This is a separate choice, especially for retained halves.
All twelve sign/lift/flag combinations have been checked. The
verifier proves chi times its chosen raw eigenvalue is1,
chi+chi^-1 is the actual raw trace, and chi conjugate(chi)=1.
This covers either actual scalar mode once its original flag has
been selected; it does not identify the modes by trace alone or
conflate the raw chi^-1 flag with the physical positive-M flag.

The true preferred SL2 longitude remains lambda=P. Its centered
version ell=-P carries the explicit mixed-pivot character.
For epsilon=+/-1, M_epsilon² lambda^epsilon=I, whereas
M_epsilon² ell^epsilon=-I. For epsilon0, M0²=-I. These give
the same killed peripheral word in PSL but different recorded
central characters; they are not conflated here.

The flag conversion can be stated without a reciprocal ambiguity. Let
f=+1 denote the raw chi^-1 flag on the P=J line and f=-1 the
reciprocal line. The literal positive physical eigenvalue is M=-chi,
so its preferred longitude eigenvalue is lambda=J^(-f), whereas
its centered eigenvalue is ell=-J^(-f)=exp(2pi i f delta). Thus
V=4pi i f delta; the earlier V=-4pi i delta convention is f=-1.
For a half-twisted displayed raw matrix,

    chi=lift*f*i*exp(-pi i f epsilon delta),
    U=2Log(-lift*f*i)-2pi i f epsilon delta=U0-epsilon V/2.

For the untwisted displayed matrix chi=-lift*f*i. The difference
of the displayed central origins is retained: H/(2k) tends to-I,
so matching one external-color lift across the half-twist convention
may flip the auxiliary central sign. No unrecorded logarithm reset
is made. Covering both f and both lifts avoids assigning the original
scalar mode from trace alone.

## 3. Propagate colors in the ORIGINAL four-crossing word

Start with colors(-1,-1,chi_aux) and apply positions[2,1,1,2].
They propagate as

    (-1,-1,chi) -> (-1,chi,-1) -> (chi,-1,-1)
               -> (-1,chi,-1) -> (-1,-1,chi).

Relative to the FORMAL complete-color expression used before,
equation(2) multiplies precisely the shapes with zero-based indices

    0,3,5,8,12,14,17,19

by -chi_aux. It leaves all other shapes unchanged. The fifth
crossing, when present, is on two MAIN colors-1 and already used
the correct symbol of its actual sign. This is an explicit
source correction, not a change of frame or a new choice of trace.

The corrected exact verifier constructs these factors from the
color list at each crossing, not only from the displayed index list.
It checks that the list and final colors agree and factors every
corrected shape and complement with all Gaussian rational norms
retained.

## 4. Exact differential, domain, and absolute constant

Let h be the previously calibrated critical interval Legendre
value and retain its original head forces. The exact factor
certificate proves, for epsilon0,+1,-1, BOTH central lifts and BOTH reciprocal flags,

    d D(sum beta_mix)=
        log b dArg p_in-log c dArg p_out
                     -log x dArg(Ex_in/Ex_out)=2pi dh       (y=1). (6)

All twelve identities have passed exactly over Q(i)(b,T,v), with
v=tan(pi delta/2). Their expanded tensor sizes are85 for each
untwisted case,125 for each positive-half case and112 for each
negative-half case. No omitted color monomial is being inferred
to have zero value from this tensor: equations(1)--(4) keep its
separate action-boundary role explicit.

The earlier formal-shape domain checks now have a valid limited use.
Each corrected shape is the corresponding formal shape multiplied
either by1 or by -chi_aux. In the untwisted case this is a constant
unit. In the half cases

    chi_+=-i(v+i)/(v-i),  chi_-=-i(v-i)/(v+i),

up to the central sign. These functions have no zero or pole
on the positive physical domain. Thus multiplication creates
no new0/0 or ambiguous limit, and the existing explicit
physical-factor classification applies to the CORRECTED shapes.

For epsilon0 the eight changed shapes are exactly the four
zeros and four poles of the endpoint calibration table. Their
limits remain0 or infinity; the twelve finite limits stay real.
For epsilon=+/-1, the color tends to +1 or-1 as delta->1/2,
up to the central sign. Every corrected25-shape limit at the
fixed anchor b=1,x=2,T->sqrt6 remains real. The new verifier
independently recomputes every corrected endpoint valuation.

The connected-domain continuity argument and the explicit
scaled-integral h->0 proof therefore apply without a source
reference reset. They fix the constant in (6), giving

    D(sum ACTUAL beta_mix)=2pi h                              (7)

on the stated positive critical chart, for all three half-twist
choices, both central lifts and both reciprocal auxiliary flags.

The previously derived final MAIN half-crossing term

    beta=-D(r)+D(xr/c)+D(yr/c),
    r=1-(T-i c k)²/(xy),

is unaffected by this correction, because both final strands
have color-1. Equation(7) consequently gives the CORRECTLY
COLORED four-word compensation

    D(B4_mix(M_epsilon))-D(B4_mix(M0))=-beta.                 (8)

## 5. Exact artifacts and remaining global obstruction

The author-passed exact verifier and complete corrected shape lists are

    experiments/research_audit_actual_mixed_critical_green_regulator.py
    experiments/research_actual_mixed_critical_green_regulator_results.json

The [portable direct verifier](../experiments/research_audit_actual_mixed_critical_green_regulator.py)
accepts --output and reconstructs EVERY universal head and actual
mixed symbol from its input heads and transported colors. It reads
no private result file. Its helper supplies only the already checked
universal Gauss maps, factor arithmetic and formal-shape domain
certificate. The symbols themselves are generated directly from(1).
No formal-symbol result is relabeled as an actual-source result.
The expanded portable direct replay passed all twelve cases: three
preferred-word identities,54 returned head coordinates,36 color/flag
identities,12 actual mixed differential tensors and280 endpoint
valuations. A separate focused check then proved all560 uncancelled
leading numerator/denominator anchor values nonzero before ratio
cancellation. Coherent subsequently completed a fresh independent
replay of the strengthened PORTABLE twelve-case verifier, reproducing
all those counts including all560 uncancelled checks. The saved main
result beside the verifier is that complete independent replay; the
earlier focused supplemental record is
[retained separately](../experiments/research_mixed_critical_green_uncancelled_anchor_results.json).

Internal review: root completed the corrected source/proof and direct
code review and a fresh selected-flag six-case replay. Coherent
completed the full corrected proof/code review, the selected-flag
six-case replay, and the strengthened direct twelve-case replay.
These are internal analytical and exact-algebra checks, not external
peer review. The theorem remains unpublished and local.

The actual global chain question remains open. In
crossing_fundamental_cycle.md, the determinant/five-term comparison
for a nonunipotent component uses its positive eigenflag when it
passes over and its inverse eigenflag when it passes under.
The two auxiliary flags here are distinct. The explicit generic
correction F_kappa(z0)-F_kappa(zP), kappa=M_aux², is retained.
One must sew its actual cusp bridge chains, original cups/caps,
unrestricted mark and preferred peripheral decoration. Neither
unit eigenvalue modulus nor a fixed point on the peripheral axis
alone proves that this correction has zero regulator.

Thus(7) repairs a LOCAL actual mixed-symbol identity; it is not yet
an actual global representation-volume identity or a source-period
estimate. Protected-line extensions and free boundary strata also
remain outside the present theorem.
