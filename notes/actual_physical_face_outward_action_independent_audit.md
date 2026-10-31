# Independent audit of the physical-face outward action theorem

28 October 2026. This note checks the local hypotheses and formulas of [the physical-face theorem](actual_physical_face_outward_action.md), including its quantum Gamma packet. The remaining global cycle, gluing and knot-volume estimate are not established here.

The theorem concerns a NONEMPTY one-component braid word. The empty
one-head unknot has a constant factorial density and zero radial q;
it is an irrelevant but literal exception to an unrestricted phrase
"every braid word."

## Algebra and face geometry

I independently re-derived the signed head gathering from the actual
negative-root chirp. The head exponents are even, and each independent
total transfer has exponent minus one. The transfer coordinates are
integrally free for a one-component closure, with one additional base
color; this also follows from the separate source lattice proof in
[the transfer-face note](actual_transfer_only_face_downhill_patch.md).

The interval-column proof of total unimodularity is valid. After
restricting to selected arc rows, successive row differences produce
at most one positive and one negative entry per column. Expansion
or zero column sums give determinants in {0,+1,-1}. Unit transfer
rows and upper inequality signs preserve the assertion. Consequently
the physical vertices are binary and independent active rows give
honest affine unimodular source coordinates.

The parity argument proves q_F!=0 whenever a transfer endpoint is
active. With no active transfer, physical support forces a zero head
to be an over-to-under minimum and a unit head to be an under-to-over
maximum; hence q_F=-2 times the sum of active inward normals, which
cannot vanish by strict interior feasibility. The k=1 constraints
cannot be facets because they force independent head endpoint
equalities. The remaining facet cases and the codimension-at-least-two
halfspace construction are correct. A primitive normal direction
with selected inward slope -1 exists, so its positive integer source
normal is invalid for all tangent values, including complex ones.

## Action, marks and the exact quantum packet

Both endpoints of I(s)=integral_0^s log|2sin(pi t)|dt have the SAME
coefficient delta*v*log(delta). No upper-end sign is missing.
Integer cardinal and full-Psi norm characters have exactly constant
modulus along the prescribed real displacements. Thus their leading
marks do not reverse the strict far-normal height drop. The statement
is correctly a face-to-far-edge estimate; it does not assert monotonicity
at every point of a general interpolating sweep.

I checked the whole factorial factorization

    Fhat(s)=(-h)^s Gamma(s+1) A_N(s).

Its branch is the original Gaussian branch. The 1/t coefficient in
LogGamma(t+s+1)-LogGamma(t-s)-(2s+1)log t cancels exactly, leaving a
summable O((|s|+1)^3/t^2) error. This proves the stated zero-free
A_N and inverse bound on a fixed sufficiently small O(N) disk.
The exact upper reflection retains both N=F_d and its chirp; the
cardinal orientations exchange correctly under reflection.

For negative normal arguments, Gamma reflection and the COMPLETE
window leave nonnegative powers of sin(pi*s). This cancels the
negative-integer Gamma poles before estimating. Positive arguments
use ordinary Stirling. Summing the signed slopes r_i beta_i gives
exactly q_F(v_F), and hence the displayed leading term
-q M log(N/(M+1)). Bounded offsets cost O(log N); smaller growing
offsets cost the stated O((L+1)log N). Upper endpoint powers N^c
are retained explicitly. No estimate of separated polar cardinal
modes has been substituted for the complete packet.

## Scope required for a global use

The exact inactive-bulk allowance (18) is a substantive hypothesis.
It is not supplied merely by bounds on B and 1-B in a continued
chart near an outside-band integer divisor. The note states this
correctly. Retained inactive mode exponentials belong in that bulk
reference; their wrong-side growth cannot be omitted.

The zero-residue normal extension is exact after re-presenting the
COMPLETE finite residue source in the chosen unimodular chart. It
is not a pointwise replacement of the old cotangent product. Partial
chart transitions, valid physical residues swept in a larger move,
side curtains, repeated visits and escaping tangential regions still
need the separate global control identified in the original note.

The [exact audit](../experiments/audit_actual_physical_face_outward_action.py) checks seven signed braid words, 790 proper physical faces, 4,877 maximal minors and 28 logarithmic phase diagnostics. These finite tests supplement the uniform witness and face-enumeration proof.