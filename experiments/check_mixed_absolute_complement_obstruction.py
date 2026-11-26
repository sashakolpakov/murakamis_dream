#!/usr/bin/env python3
"""Outward constants for an all-length absolute mixed-complement obstruction."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
I = acb(0, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-mixed-absolute-complement-obstruction.json')
    args = parser.parse_args()
    ctx.prec = args.precision
    pi = arb.pi()

    def r(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def digest(path):
        return sha256(path.read_bytes()).hexdigest()

    def jr(z):
        return -(2*pi*I*z).exp().polylog(2).imag/(2*pi)

    def jc(z):
        return -I*pi*(z*z-z)/2+I*(2*pi*I*z).exp().polylog(2)/(2*pi)-I*pi/12

    reference_path = ROOT/'repro/results/research-three-four-source-interface.json'
    rec = json.loads(reference_path.read_text())
    assert rec['status'] == 'passed'
    assert rec['script_sha256'] == digest(ROOT/'experiments/check_three_four_source_interface.py')
    for dep, want in rec['dependencies_sha256'].items():
        assert digest(ROOT/dep) == want, dep
    root = rec['root_certificate']
    center = acb(*map(r, root['center']))
    radius = r(root['complex_disk_radius'])
    alpha = acb(arb(center.real, radius), arb(center.imag, radius))
    K = 1/(1+2*alpha-4*alpha*alpha)
    x0 = K.log()/(2*pi*I)
    u3, u4 = 1-2*alpha, (1-K)/(2*K)
    z3, z4 = -u3.log()/(2*pi*I), -u4.log()/(2*pi*I)

    # Original selected actions, with the cardinal constants retained.
    phi3 = ((u3*u3).polylog(2)-pi*pi/6-2*(K*u3).polylog(2)
            +2*K.polylog(2))/(2*pi*I)+(2*z3-1)*K.log()
    integral4 = ((K*u4).polylog(2)-K.polylog(2))/(2*pi*I)
    phi4 = jc(2*z4)-2*jc(z4)-I*pi*z4*z4+(2*z4-1)*K.log()-2*integral4
    sigma = (phi3+phi4).real

    a, b, x = r(Q(343, 1000)), r(Q(7, 25)), r(Q(6, 25))
    h = jr(2*a)+jr(2*b)+2*jr(a+b)-4*jr(a)-6*jr(b)
    cost = jr(2*a)+jr(a+b)-2*jr(a)-jr(a+x)-jr(x+b)+2*jr(x)
    margins = {}

    def positive(name, value):
        assert value > 0, (name, value)
        margins[name] = str(value)

    positive('real witness pair rate', h-r('1.5369'))
    positive('single-leg entropy cost', r('.0361')-cost)
    positive('original geometric pair rate', r('1.5126')-sigma)
    positive('strict excess at two alternating pairs', 2*(h-sigma)-cost-r(Q(1, 80)))
    positive('positive excess slope for every additional pair', h-sigma-r('.0243'))
    positive('exceptional leg below central square', r(Q(1, 4))-x)
    for name, value in [('a', a), ('b', b), ('x', x), ('two a', 2*a),
                        ('two b', 2*b), ('a+b', a+b), ('a+x', a+x), ('b+x', b+x)]:
        positive(name+' positive', value)
        positive(name+' below one', 1-value)
    assert 2*Q('.0243')-Q('.0361') == Q(1, 80)
    assert Q('1.5369')-Q('1.5126') == Q('.0243')

    dependencies = ['notes/research_mixed_absolute_complement_obstruction.md',
                    'notes/research_mixed_wire_exact_contraction.md',
                    'notes/research_three_vertex_mixed_reference_packet.md',
                    'notes/research_power_four_source_packet.md',
                    'notes/research_mixed_three_four_joint_coercivity.md',
                    str(reference_path.relative_to(ROOT))]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'strict_comparison_count': len(margins), 'margins': margins,
        'real_pair_entropy': str(h), 'single_leg_cost': str(cost),
        'selected_geometric_pair_action': str(sigma),
        'rational_identities': 2,
        'scope': 'Explicit full-support configurations for every alternating cycle with at least two pairs. Constants for the absolute complement obstruction; no assertion about the signed complement or a knot invariant.',
        'script_sha256': digest(Path(__file__)),
        'dependencies_sha256': {name: digest(ROOT/name) for name in dependencies},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'strict_comparison_count',
                                                  'real_pair_entropy', 'single_leg_cost',
                                                  'selected_geometric_pair_action')}, indent=2))


if __name__ == '__main__':
    main()
