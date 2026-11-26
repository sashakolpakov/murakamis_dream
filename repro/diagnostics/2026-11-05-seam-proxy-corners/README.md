# Coarse repaired-halo seam comparison: algebra and bounded corners

This directory contains a fixed floating test and a precise description of
the remaining inequality. It supplies no interval certificate, uniform sign,
or counterexample to the actual kernel or cyclic integral.

## Exact cancellation and the remaining lower bound

Place the seam at index0. Write the last two left A coordinates as u,v and
the first two right coordinates as w,z. Their selections are retained.
Let v# and w# be their repaired complex targets after replacing the seam
halos by the unselected baseline p0. Let v,w without a hash denote their
actual physical complex targets. The complex targets u,z are unchanged
by the repair, although they depend on the additional inner halos.

The two baseline occurrences at position0 in the three-step closures have
complex coordinates

    bL = Re(r0) + i Im(r0) L_slow(Re(v)),
    bR = Re(r0) + i Im(r0) L_slow(Re(w)).

These must not be replaced by r0 when an endpoint real part is below .22.
Define e_j to be the original coherent allocated rate, including its selected
halfcorrections, and let

    C = e0(v#,bL) + e1(bL,r1)
        + e0(r_-1,bR) + e1(bR,w#),
    R = e_-1(u,v) - e_-1(u,v#)
        + e2(w,z) - e2(w#,z),
    Fref = Re(phi0(r_-1,r0) + phi1(r0,r1)),
    U = A_beta,alpha(Im(v)) + B_gamma(Im(w))
        + 2 Delta_collar + beta nu_collar.

The baseline symbols in C are unselected. With only the endpoint share of
the available A-run occupation retained, the total occupation debit is

    O = theta*(omega_v+omega_w) + (1-theta)*(omega_u+omega_v).

It includes the endpoint shares already present in the literal E3 and A3,
the additional endpoint half-shares from the run, and the outgoing Psi loss.
For the distinct-edge repair convention, the complete proxy simplifies to

    proxy = U + Fref + R - C - O.

Every target-dependent tangent term cancels. At v and w this uses the
original critical equations from the adjacent edge plus the seam edge; at
position0 it uses the middle critical equation. No Fourier halfcorrection
is discarded in this cancellation. A sufficient local inequality is therefore

    C - R >= Fref + U - O + positive reserve.

This is a coherent-connector **lower** bound. When both adjacent endpoint
reals are at least .22, bL=bR=r0, two connector rates add to Fref and cancel
it. The condition then involves just

    e0(v#,r0) + e1(r0,w#) - R >= U - O + positive reserve.

Below .22 all four connector rates remain. A singleton has no AA correction;
for a two-symbol run the two repairs belong to one edge and must be replaced
by the joint physical-minus-both-repaired expression. This independent-end
diagnostic does not test those overlap cases.

## What the existing constants do and do not give

The full-height reset certificate gives the pointwise quadratic inequality

    Re[d^T phi'' d] <= 20 |Im(d)|^2

on the unselected products with real parts in [.22,.5]. Applying this same
inequality to i*d also gives the exact lower estimate

    Re(phi(z)-Gamma_r(z)) >= -10 |Re(z-r)|^2.

This follows from the same straight-segment integral and does not require
new numerical cells. It is useful but too coarse for the general connector
comparison. Even at the already preserved alternating reference with both
neighboring endpoint reals .5, using this lower estimate on the two varying
connectors gives the scalar upper estimate approximately +.3239749121 after
the height-resolved source, full collar and all retained occupations. The
actual explicit closure there is substantially smaller. The scalar comparison
is recorded in `coarse-curvature-comparison.json`; it reuses saved reference
and source data and performs no new phase optimization.

Moreover that K<20 estimate does not cover endpoint real parts below .22 or
selected positive-height products. Positive triangle accretivity supplies
convexity in heights but no adequate quantitative lower connector value on
the entire variable-height polygon. The completed occupation theorem bounds
cyclic sums above, and the endpoint certificates bound sources above; neither
reverses into the missing lower inequality. Thus the existing results alone
have not closed this stronger proxy. A sharper connector estimate is still
needed; no high-dimensional cover has been launched.

### Sharper inherited orientation constants at the preserved half-angle point

The completed oriented reset theorem proves the quadratic upper bound with
coefficients 11 and 151/10 when only the first or second imaginary component
is nonzero. Rotate the direction by i exactly as above. If the second real
coordinate is unchanged, this gives

    Re(phi(z)-Gamma_r(z)) >= -(11/2)*(Re(z0-r0))^2;

if the first real coordinate is unchanged, the coefficient for the second
is 151/20. The other imaginary components are unrestricted within the
admitted unselected products: rotation turns them into the arbitrary real
components in the original pointwise quadratic inequality. Integrate along
the original straight segment. No rotated parameter path or new source
extension is used.

At the preserved alternating reference with both endpoint targets .5,
the two varying connector arguments have displacement
`d=.5-.2845277776565761`. The two costs become

    (11/2)*d^2 = .2553555323088765,
    (151/20)*d^2 = .3505335034421849.

Their sum .6058890357510613 is much smaller than the previous full-K
estimate .9285655720322781. With the height-only source ceiling it still
leaves a slightly positive scalar upper estimate, +.00129837581.
However the already-proved exact half-angle row source is
`c0+c1=.7350946246153732`, rather than .902272. Keeping the same full
collar and occupation changes the estimate to **−.16587899957**.
Even the certified rational ceiling `c0+c1<.291561+.443534` gives
**−.16587862419** in this floating reference substitution.

Thus this combination of already-proved inequalities is quantitatively
promising at the preserved half-angle configuration. The calculation reuses
a floating actual reference/action value; it is not a new outward reference
certificate, nor a uniform result for arbitrary endpoints or references.
The general connector lower inequality above remains unresolved.

The comparisons and source hashes are recorded in
`oriented-curvature-half-angle-comparison.json`. The small standalone script
`compare_oriented_half_angle.py --output <fresh-path>` reproduces the scalar
arithmetic without any phase evaluation or optimization.

## Bounded diagnostic

Seven original correlated references are used: homogeneous types3/4,
alternating rotations, and the three rotations of (3,4,4). At each reference,
both adjacent endpoint reals independently range over the four fixed values
{.1,.22,.45,.5}; the next two A coordinates and additional inner halos are
reference-valued. All allowed four A selection bits are included. There are
784 fixed configurations and 1,568 distinct candidate attenuation values.
No optimizer was called.

Every evaluated proxy is negative. The largest, approximately
`-.28376449751`, is homogeneous type3 with both adjacent endpoint reals .1.
It is independent of attenuation because both endpoint own cutoffs vanish.
Its decomposition is

    source + collar = .650132 + .01352605188,
    actual pair plane = 1.29226378888,
    -E3-A3 = .34509123948,
    outgoing Psi loss = .000125,
    endpoint occupation = .000125,
    exact repair corrections = 0.

This tests neither all inner coordinates nor a continuum of references.
The negative samples are evidence only. Runtime was approximately1.23s.
No further search was run.

The driver uses only repository-local helpers from the attenuation-vertex
archive and reads its frozen profile/reference data. `results.json` and
`manifest.json` record the input and helper hashes. The driver refuses to
overwrite an existing result. No upstream proof or canonical record changed.
