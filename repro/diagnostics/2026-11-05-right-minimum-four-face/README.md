# A focused outward check on the difficult all-four face

This is a two-height face check, not a uniform mixed minimum-transport
theorem. It uses no parameter optimization and no raw-row root solve.
The initial outward pass used 15 accepted boxes and 29 visits, well
within the explicit 4,095-visit/30-second cover limit. The final saved
record, rather than those initial counts, is authoritative.

Consider the physical pattern

    R -> unselected A4 neighbor -> unselected A4 center -> R,

with both A real coordinates exactly .22. The two R symbols are real
.5. Their types do not enter the marginal after the two fixed raw rows
have been justified for either own-factorial indicator. Independently
allow both original height coefficients in [-.057,-.02]. At this face
the slow cutoff and right profiles of the two A symbols equal one,
so their target heights are exactly those coefficients.

Write a=.22+i h_n and b=.22+i h_c, and let phi=phi_11 be the
original coherent phase on their common edge. Define the unselected
raw target marginals, retaining the first-argument chirp,

    K_d(z,u)=g'(z+u)-(3/2)g'(z)+2 pi i d u,
    G_c=phi_b(a,b)+K_1(b,u_R),
    G_n=phi_a(a,b)+K_0(a,2/5).

For height-only motion of the negative-height neighbor, the left
raw contribution is minimized at row 2/5. For the center's
moving-real contribution, it is enough to test u_R=1/5 and 2/5.
Both deductions are the exact endpoint theorem in
[raw-row stationarity](../../../notes/research_mixed_raw_row_stationarity.md).
The four negative-height-cost switches give the eight smooth functions

    D_(chi_n,chi_c,u_R)
      = Re[(1+i chi_c h_c/.12)G_c
                     +i chi_n h_n G_n/.12],
    chi_n,chi_c in {0,1}, u_R in {1/5,2/5}.

The certificate checks that all eight exceed 1/50 over the entire
closed height square. Hence their minimum, the conservative whole
local star at this face, also exceeds 1/50. This is not a claim
that the two old gauged halves are separately nonnegative.
Repeated physical R symbols in a three-cycle still give two separate
raw edges and rows; nothing identifies or deletes those incidences.

## Outward acceptance and the saved cover

Each height box uses the original-log affine Newton disk self-map
already implemented in the frozen half-stencil arithmetic. It checks
the root in the original cotangent chamber and all regular factorial
strips. A separate point self-map encloses the root at the exact box
midpoint. Rational centers, affine responses and positive disk radii
are retained. Supplied witnesses never invoke a root proposal.

The Schur Hessian of phi gives the exact parameter derivatives.
With q_c=1+i chi_c h_c/.12 and q_n=i chi_n h_n/.12, these are

    dD/dh_n = Re[q_c i phi_ba
                  +q_n i(phi_aa+K_0,z)
                  +i chi_n G_n/.12],
    dD/dh_c = Re[q_c i(phi_bb+K_1,z)
                  +q_n i phi_ab
                  +i chi_c G_c/.12],
    K_d,z=g''(z+u)-(3/2)g''(z).

Thus the midpoint enclosure minus the full-box derivative radii is
a valid lower bound. Direct interval evaluation is an additional
bound. All comparisons between those bounds use their outward lower
endpoints, not interval partial ordering. Nonfinite values cause
subdivision rather than acceptance. One binary tree covers the entire
height square, with all eight tests on every accepted leaf.

The saved replay consumes every node, recreates every rational box,
rechecks every original-log witness and every inequality, and verifies
the complete current source bindings before and after the run.
The time/visit guard applies only to constructing a new cover; a
saved replay must finish its entire prescribed tree.

Run from the repository root:

    python3 repro/diagnostics/2026-11-05-right-minimum-four-face/check_face.py
    python3 repro/diagnostics/2026-11-05-right-minimum-four-face/check_face.py --precision 384 --input repro/diagnostics/2026-11-05-right-minimum-four-face/author.json --output repro/diagnostics/2026-11-05-right-minimum-four-face/replay.json

## What this does and does not extend

Continuity of these eight regular functions on the compact height
square gives an unquantified one-sided neighborhood of this face:
for sufficiently small common eta, the same sign holds when
t lies in [.22-eta,.22] and the neighbor real coordinate lies in
[t,.22+eta], with their literal slow-cutoff heights. This is only
an existence consequence of the strict face reserve. No numerical
width is certified.

Off the face, h_n and h_c in the fixed coefficient square continue
to mean the original reference height coefficients: the two target
heights become h_j(t-.1)/.12, while their velocity coefficients
remain h_j/.12. They are not the reduced target heights divided
by .12. The continuity assertion uses this distinction.

The rest of the real-coordinate domain, the one-R-neighbor case
with a nonright outer halo, mixed types, selected states and purely
coherent tapered halves remain separate. No complete finite source,
whole minimum-transport sign, whole-period asymptotic or knot-family
conclusion is asserted by this face check.
