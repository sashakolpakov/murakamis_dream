#!/usr/bin/env python3
"""Signed geometric chain identities used by the hybrid-piece proof.

Checks actual tangent-circle contact coordinates and oriented tetrahedral
volumes against the signed cyclic-fan and contact-angle formulas.  The
source pairing, abstract degree-one chain, general cut-disk collapse and
representation-volume bound are analytic proofs, not conclusions inferred
from these finite fixtures.  No open Gauss re-framing invariance is used.
"""
import argparse
from collections import Counter
from itertools import islice, permutations
import json
from pathlib import Path

import mpmath as mp


def lobachevsky(angle):
    return mp.im(mp.polylog(2, mp.exp(2j * angle))) / 2


def bloch_wigner(z):
    z = mp.mpc(z)
    if z == 0 or z == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.log(abs(z)) * mp.arg(1-z)


def ideal_tetrahedron(a, b, c):
    """Oriented volume of (infinity,a,b,c), including repeated vertices."""
    a, b, c = map(mp.mpc, (a, b, c))
    if a == b or a == c or b == c:
        return mp.mpf(0)
    return bloch_wigner((c-a)/(b-a))


def run():
    counts = Counter()
    errors = {'volume': mp.mpf(0), 'contact': mp.mpf(0)}

    def check(actual, expected, category='volume'):
        error = abs(actual-expected)
        errors[category] = max(errors[category], error)
        assert error < mp.mpf('1e-65'), (category, actual, expected, error)

    # Actual polygon order is retained. Permutations include negative and
    # winding-zero signed chains, not only embedded counterclockwise fans.
    angles = [2*mp.pi*mp.mpf(k)/7 for k in range(6)]
    for size in (3, 4, 5, 6):
        for order in islice(permutations(range(size)), 120):
            phases = [angles[k] for k in order]
            vertices = [mp.exp(1j*a) for a in phases]
            fan = sum(ideal_tetrahedron(vertices[0], vertices[j], vertices[j+1])
                      for j in range(1, size-1))
            boundary = sum(lobachevsky((phases[(j+1) % size]-phases[j])/2)
                           for j in range(size))
            check(fan, boundary)
            counts['signed_cyclic_fans'] += 1

    # Repeated nonadjacent contacts are normalized chain degeneracies;
    # their edge order is not changed to a principal cyclic ordering.
    for order in ((0, 1, 2, 1, 3), (0, 1, 0, 2, 3),
                  (0, 1, 2, 0, 3), (0, 0, 1, 2)):
        phases = [angles[k] for k in order]
        vertices = [mp.exp(1j*a) for a in phases]
        size = len(order)
        fan = sum(ideal_tetrahedron(vertices[0], vertices[j], vertices[j+1])
                  for j in range(1, size-1))
        boundary = sum(lobachevsky((phases[(j+1) % size]-phases[j])/2)
                       for j in range(size))
        check(fan, boundary)
        counts['repeated_contact_fans'] += 1

    # Contact coordinates come from actual externally tangent circles.
    # An outer zero curvature is the line Y=0 with its fixed coorientation.
    for raw in ((1, 2, 3), (2, 3, 7), (0, 3, 7), (2, 3, 0)):
        x, middle, y = map(mp.mpf, raw)
        total = mp.sqrt(middle*(x+y)+x*y)
        theta = [2*mp.atan(a/total) for a in (x, middle, y)]
        check(sum(theta), mp.pi, 'contact')
        counts['center_angle_sums'] += 1
        target = sum(lobachevsky((mp.pi-a)/2) for a in theta)
        rb = 1/middle
        for sign in (1, -1):
            if x == 0:
                ry = 1/y
                cy = 1j*ry
                cb = -2*sign/mp.sqrt(middle*y)+1j*rb
                pxy = mp.mpc(0)
                pby = (ry*cb+rb*cy)/(ry+rb)
                pxb = mp.mpc(mp.re(cb))
                check(abs(cb-cy), rb+ry, 'contact')
                check(mp.im(cb), rb, 'contact')
                check(mp.im(cy), ry, 'contact')
            elif y == 0:
                rx = 1/x
                cx = 1j*rx
                cb = 2*sign/mp.sqrt(middle*x)+1j*rb
                pxy = mp.mpc(0)
                pby = mp.mpc(mp.re(cb))
                pxb = (rx*cb+rb*cx)/(rx+rb)
                check(abs(cb-cx), rb+rx, 'contact')
                check(mp.im(cb), rb, 'contact')
                check(mp.im(cx), rx, 'contact')
            else:
                rx, ry = 1/x, 1/y
                cy = rx+ry
                cb = rx+(y-x)/(middle*(x+y))+2j*sign*total/(middle*(x+y))
                pxy = rx
                pby = (ry*cb+rb*cy)/(ry+rb)
                pxb = rx*cb/(rx+rb)
                check(abs(cb), rb+rx, 'contact')
                check(abs(cb-cy), rb+ry, 'contact')
                check(abs(cy), rx+ry, 'contact')
            counts['actual_circle_or_line_tangencies'] += 3
            check(ideal_tetrahedron(pxy, pby, pxb), sign*target)
            counts['finite_and_line_contact_triangles'] += 1

    # One actual K4 strip, together with its orientation reversal. The
    # first ball's original white and shaded fans are evaluated separately;
    # a globally reflected second ball contributes the same signed volume.
    for sign in (1, -1):
        lower_left = mp.mpc(0)
        lower_right = mp.mpc(2*sign)
        upper_left = mp.mpc(0, 2)
        upper_right = mp.mpc(2*sign, 2)
        middle = mp.mpc(sign, 1)
        white = (ideal_tetrahedron(lower_left, middle, upper_left)
                 + ideal_tetrahedron(lower_right, upper_right, middle))
        shaded = (ideal_tetrahedron(lower_left, lower_right, middle)
                  + ideal_tetrahedron(upper_left, middle, upper_right))
        check(2*(white+shaded), sign*16*lobachevsky(mp.pi/4))
        counts['two_ball_strip_orientations'] += 1

    return {
        'status': 'PASS',
        'precision_digits': mp.mp.dps,
        'counts': dict(counts),
        'maximum_volume_identity_error': str(errors['volume']),
        'maximum_contact_identity_error': str(errors['contact']),
        'scope': ('Signed cyclic fans, repeated contacts, actual finite/line '
                  'contact triangles and two oriented strip chains. General '
                  'source pairing, abstract relative degree, compatible '
                  'cut-disk collapse and the volume bound remain analytic '
                  'proofs, not inferred from these fixtures.')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'actual_fejer_hybrid_piece_representation_results.json'))
    args = parser.parse_args()
    mp.mp.dps = 80
    result = run()
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
