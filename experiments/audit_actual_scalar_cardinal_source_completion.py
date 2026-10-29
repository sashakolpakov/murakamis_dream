#!/usr/bin/env python3
"""Supplementary checks for the source-faithful scalar cardinal completion.

Analytic checks use literal finite cardinal sums and the independent Barnes
factorial. Whole signed words are compared with the original finite R and
pivot, retaining its half-Cartan and external normalization. No output
projection or mod-N routing is introduced.
"""

import itertools
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix, partial
from audit_exact_factorial_interpolation import factorial


def cardinal(N, s, orientation=1):
    s = mp.mpc(s)
    value = mp.expm1(2j * mp.pi * s) * sum(1 / (s-j) for j in range(N)) / (2j * mp.pi)
    return value if orientation == 1 else mp.exp(-2j * mp.pi * s) * value


def mode_coefficients(N, s):
    H = mp.digamma(s+1)-mp.digamma(N-s)
    return mp.mpf('.5')-H/(2j*mp.pi), mp.mpf('.5')+H/(2j*mp.pi)


def cardinal_checks():
    values = packets = bounds = outside_residues = 0
    largest_error = mp.mpf(0)
    delta = mp.mpc('1e-16', '3e-17')
    for N in range(2, 10):
        for n in range(-2, N+2):
            for orientation in (-1, 1):
                value = cardinal(N, n+delta, orientation)
                target = 1 if 0 <= n < N else 0
                error = abs(value-target)
                assert error < mp.mpf('1e-12'), (N, n, orientation, error)
                values += 1
            if n < 0 or n >= N:
                # The derivative at the outside zero is literally S_N(n).
                target = sum(mp.mpf(1)/(n-j) for j in range(N))
                assert abs(cardinal(N, n+delta)/delta-target) < mp.mpf('1e-11')
                H = mp.digamma(n+delta+1)-mp.digamma(N-n-delta)
                assert abs(delta*H+1) < mp.mpf('1e-12')
                outside_residues += 1
        points = [mp.mpc('.3','.2'), mp.mpc(N/2,'.4'),
                  mp.mpc('-1.2','.3'), mp.mpc(N+mp.mpf('.4'), '-.5'),
                  mp.mpc('.27','-1.7'), mp.mpc(N/3,'2.1')]
        for s in points:
            A, B = mode_coefficients(N, s)
            t = mp.exp(2j*mp.pi*s)
            for orientation in (-1, 1):
                exact = cardinal(N, s, orientation)
                for power in (1, 2, 3):
                    predicted = (sum(mp.binomial(power,k)*A**(power-k)*B**k*t**k
                                     for k in range(power+1)) if orientation == 1 else
                                 sum(mp.binomial(power,k)*B**(power-k)*A**k*t**(-k)
                                     for k in range(power+1)))
                    error = abs(predicted-exact**power)/max(1,abs(exact**power))
                    largest_error = max(largest_error, error)
                    assert error < mp.mpf('1e-60'), (N, s, power, orientation, error)
                    packets += 1
                bound = mp.sqrt(N)*mp.exp(2*mp.pi*max(0,-orientation*mp.im(s)))
                assert abs(exact) <= bound*(1+mp.mpf('1e-60'))
                bounds += 1
    return dict(removable_integer_value_checks=values,
                exact_finite_mode_packet_checks=packets,
                global_halfplane_bound_checks=bounds,
                matched_outside_integer_residue_checks=outside_residues,
                max_relative_packet_error=float(largest_error))


def factorial_divisor_checks():
    rows = []
    power = 6
    delta = mp.mpc('1e-8', '2e-9')
    for N in (2, 3, 5):
        integers = sorted(set((-2*N, -N-1, -N, -1, 0, N-1, N, N+1, 2*N)))
        for n in integers:
            F1, F2 = factorial(N, n+delta), factorial(N, n+delta/2)
            for exponent in (-1, 1):
                for orientation in (-1, 1):
                    g1 = F1**exponent*cardinal(N,n+delta,orientation)**power
                    g2 = F2**exponent*cardinal(N,n+delta/2,orientation)**power
                    order = 0 if 0 <= n < N else power+exponent*(n//N)
                    slope = mp.log(abs(g1/g2))/mp.log(2)
                    assert abs(slope-order) < mp.mpf('2e-5'), (N,n,exponent,orientation,slope,order)
                    if not 0 <= n < N:
                        assert order >= 1
                    rows.append(dict(N=N, integer=n, exponent=exponent,
                                     orientation=orientation, predicted_order=order,
                                     observed_order=float(slope)))
    return rows


def favorable_microlocal_checks():
    rows = []
    points = [mp.mpc('.3','.2'),mp.mpc('-.4','.3'),
              mp.mpc('1.4','-.2'),mp.mpc('.7','-.6')]
    for z in points:
        orientation = 1 if mp.im(z)>0 else -1
        h = mp.log(z)-mp.log(1-z)
        limit = mp.mpf('.5')-orientation*h/(2j*mp.pi)
        assert abs(limit)>mp.mpf('.02')
        for N in (8,16,32,64):
            value = cardinal(N,N*z,orientation)
            error = abs(value-limit)
            assert N*error < 2
            rows.append(dict(N=N,z=[float(mp.re(z)),float(mp.im(z))],
                             favorable_orientation=orientation,
                             limit_modulus=float(abs(limit)),
                             scaled_N_error=float(N*error)))
    return rows


def knot_routing(strands, word):
    """Integral physical routing: exactly one t and m independent transfers."""
    m = len(word)
    active = list(range(strands))
    next_node = strands
    successor, crossings = {}, []
    for j, letter in enumerate(word):
        pos, sign = abs(letter)-1, 1 if letter > 0 else -1
        a, b = active[pos:pos+2]
        c, e = next_node, next_node+1
        next_node += 2
        change_plus, change_minus = [0]*m, [0]*m
        change_plus[j], change_minus[j] = sign, -sign
        successor[a] = (e, change_minus)
        successor[b] = (c, change_plus)
        crossings.append((a,b,c,e,sign))
        active[pos:pos+2] = [c,e]
    for i, node in enumerate(active):
        successor[node] = (i, [0]*m)
    offsets, node, current = {}, 0, [0]*m
    while node not in offsets:
        offsets[node] = tuple(current)
        node, delta = successor[node]
        current = [a+b for a,b in zip(current,delta)]
    assert node == 0 and current == [0]*m
    assert len(offsets) == next_node, 'closure is not one component'
    assert all(entry in (-1,0,1) for row in offsets.values() for entry in row)
    return offsets, crossings


def original_coefficient_checks():
    checks = 0
    for N in range(2,8):
        H = HardyNetwork(N,1)
        p = H.p
        Fminus = [1]
        for j in range(1,N):
            Fminus.append(Fminus[-1]*(1-pow(H.Q,-j,p)) % p)
        for a,b in itertools.product(range(N),repeat=2):
            for k in range(min(a,N-1-b)+1):
                value = (H.kappa*pow(H.x,-a-b+k,p)*pow(H.Q,b*(a-k),p)
                         *H.fac[b+k]*H.fac[a]
                         *pow(H.fac[k]*H.fac[b]*H.fac[a-k] % p,-1,p)) % p
                assert value == H.plus[(b+k)*N+a-k,a*N+b]
                checks += 1
            for k in range(min(b,N-1-a)+1):
                value = (pow(H.kappa,-1,p)*pow(H.x,a+b-k,p)*pow(H.Q,-a*(b-k),p)
                         *Fminus[a+k]*Fminus[b]
                         *pow(Fminus[k]*Fminus[a]*Fminus[b-k] % p,-1,p)) % p
                assert value == H.minus[(b-k)*N+a+k,a*N+b]
                checks += 1
    return checks


def closed_source_case(N, strands, word):
    H = HardyNetwork(N, 1)
    offsets, crossings = knot_routing(strands, word)
    m, d, p = len(word), N-1, H.p
    # A strict REAL physical source point, with every transfer nonzero.
    t, transfer = Fraction(d,2), Fraction(d,8*(m+1))
    interior = [t+sum(row)*transfer for row in offsets.values()]
    assert all(Fraction(d,4) < value < Fraction(3*d,4) for value in interior)
    assert 0 < transfer < d
    literal = word_matrix(word, H.plus, H.minus, strands, N, p)
    cut = partial(literal, H.pivot, strands, N, p)
    expected = sum(int(cut[j,j]) for j in range(N))*pow(N,-1,p) % p
    routed, valid, nonzero, invalid = 0, 0, 0, 0
    for u in itertools.product(range(N), repeat=m+1):
        t, ks = u[0], u[1:]
        colors = {node:t+sum(a*b for a,b in zip(row,ks))
                  for node,row in offsets.items()}
        if any(not 0 <= value < N for value in colors.values()):
            invalid += 1
            continue
        valid += 1
        weight = 1
        for a,b,c,e,sign in crossings:
            matrix = H.plus if sign == 1 else H.minus
            weight = weight*int(matrix[colors[c]*N+colors[e],colors[a]*N+colors[b]]) % p
        for head in range(1,strands):
            weight = weight*int(H.pivot[colors[head]]) % p
        routed = (routed+weight) % p
        nonzero += int(bool(weight))
    routed = routed*pow(N,-1,p) % p
    assert routed == expected, (N,strands,word,routed,expected)
    external = H.dimension*pow(H.twist,-sum(1 if k>0 else -1 for k in word),p) % p
    assert routed*external % p == expected*external % p
    # Enlarged scalar contour box has only original physical integer residues.
    enlarged_valid = 0
    enlarged_invalid = 0
    for u in itertools.product(range(-1,N+1), repeat=m+1):
        if any(not 0 <= value < N for value in u):
            enlarged_invalid += 1
            continue
        t, ks = u[0], u[1:]
        colors = [t+sum(a*b for a,b in zip(row,ks)) for row in offsets.values()]
        if all(0 <= value < N for value in colors):
            enlarged_valid += 1
        else:
            enlarged_invalid += 1
    assert enlarged_valid == valid
    return dict(N=N,strands=strands,word=list(word),source_lattice_dimension=m+1,
                physical_arc_count=len(offsets),valid_integer_states=valid,
                nonzero_original_state_weights=nonzero,
                invalid_intermediate_states_in_original_cube=invalid,
                killed_enlarged_box_integer_states=enlarged_invalid,
                original_normalized_period_mod_p=int(routed*external % p),
                retained_original_kappa_pivot_and_external_line=True,
                exact_unwrapped_source_bijection_and_strict_real_interior=True)


def main():
    with mp.workdps(80):
        windows = cardinal_checks()
        divisors = factorial_divisor_checks()
        favorable = favorable_microlocal_checks()
    words = [(2,[1,1,1]),(3,[1,-2,1,-2]),
             (4,[1,-2,1,-2,3]),(4,[1,2,3])]
    sources = [closed_source_case(N,b,word) for N in (2,3) for b,word in words]
    result = dict(status='PASS',cardinal_windows=windows,
                  actual_factorial_divisor_packages=divisors,
                  favorable_nonzero_microlocal_symbols=favorable,
                  exact_original_both_signed_coefficient_checks=original_coefficient_checks(),
                  original_signed_whole_source_lattice_cases=sources,
                  scope='Exact scalar cardinal completion, finite marks, factorial pole cancellation and original integer source routing. No global transport-mass estimate, boundary critical-value theorem or volume bound is inferred.')
    target = Path(__file__).with_name('actual_scalar_cardinal_source_completion_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',windows=windows,
                         factorial_divisor_packages=len(divisors),
                         exact_original_both_signed_coefficients=result['exact_original_both_signed_coefficient_checks'],
                         original_signed_whole_sources=len(sources),
                         result=str(target)),indent=2))


if __name__ == '__main__':
    main()
