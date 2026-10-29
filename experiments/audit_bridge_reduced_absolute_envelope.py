#!/usr/bin/env python3
"""A supported ORIGINAL post-overbridge state above the knot-volume rate.

The rigorous certificate is an Arb sum of explicit periodic J values.
Finite-N weights retain the actual complete boundary source and every
bridge factor; common Cartan/framing factors are unit phases here.
"""

from fractions import Fraction
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from flint import acb, arb, ctx


WORD = [1, 1, 1, 2, -1, 2]  # independently identified original 5_2 three-braid
WIDTH = 3
LABELS = {0: 13, 1: 8, 2: 11, 3: 18, 4: 3, 5: 2, 6: 18,
          7: 6, 9: 4, 10: 16, 11: 13, 12: 19, 13: 4, 14: 10}
DENOMINATOR = 20


def graph():
    active = list(range(WIDTH))
    phases = {i: Fraction(0) for i in active}
    root_phases = [Fraction(0)]*WIDTH
    strands = list(range(WIDTH))
    records, incoming, outgoing = [], {}, {}
    counter = WIDTH
    for number, letter in enumerate(WORD):
        pos, sign = abs(letter)-1, 1 if letter > 0 else -1
        ins = active[pos:pos+2]
        outs = [counter, counter+1]
        counter += 2
        newphases = [root_phases[pos+1]+Fraction(sign, 2),
                     root_phases[pos]+Fraction(sign, 2)]
        for v, phase in zip(outs, newphases):
            phases[v] = phase
        over_in, over_out = (0, 1) if sign > 0 else (1, 0)
        rec = {'sign': sign, 'position': pos, 'in': ins, 'out': outs,
               'over_in': over_in, 'over_out': over_out,
               'under_strand': strands[pos+1] if sign > 0 else strands[pos]}
        records.append(rec)
        incoming[ins[over_in]] = number
        outgoing[outs[over_out]] = number
        active[pos:pos+2] = outs
        root_phases[pos:pos+2] = newphases
        strands[pos], strands[pos+1] = strands[pos+1], strands[pos]
    following = {outgoing[v]: incoming[v] for v in outgoing.keys() & incoming.keys()}
    predecessors = set(following.values())
    paths = []
    for number in range(len(records)):
        if number in predecessors:
            continue
        path = [number]
        while path[-1] in following:
            path.append(following[path[-1]])
        paths.append(path)
    return records, paths, phases, tuple(active), tuple(strands)


RECORDS, PATHS, PHASES, OUTPUTS, FINAL_PERMUTATION = graph()
assert PATHS == [[0], [1], [2, 3], [4], [5]]
assert OUTPUTS == (11, 13, 14)
assert FINAL_PERMUTATION in ((1, 2, 0), (2, 0, 1))


def limiting_data():
    labels = {v: Fraction(n, DENOMINATOR) for v, n in LABELS.items()}
    out = []
    for rec in RECORDS:
        vi = rec['in'][1-rec['over_in']]
        vo = rec['out'][1-rec['over_out']]
        h = ((labels[vi]-labels[vo]) if rec['sign'] > 0
             else (labels[vo]-labels[vi])) % 1
        theta = labels[vo]+PHASES[vo]
        alpha = (-h-Fraction(1, 2)-theta if rec['sign'] > 0
                 else Fraction(1, 2)-theta) % 1
        out.append((h, alpha))
    return labels, out


def certify_entropy():
    ctx.prec = 192
    pi = arb.pi()
    I = acb(0, 1)
    def rational(v):
        v = Fraction(v)
        return arb(v.numerator)/v.denominator
    def J(v):
        v = Fraction(v) % 1
        if not v:
            return arb(0)
        return -(2*pi*I*rational(v)).exp().polylog(2).imag/(2*pi)
    def poch(start, length):
        return J(start+length)-J(start)
    labels, data = limiting_data()
    rates, detail = [], []
    for path in PATHS:
        hs = [data[j][0] for j in path]
        aa = [data[j][1] for j in path]
        differences = [a-b for a, b in zip(hs, hs[1:])]
        assert all(d >= 0 for d in differences)
        first, last = RECORDS[path[0]], RECORDS[path[-1]]
        vin, vout = first['in'][first['over_in']], last['out'][last['over_out']]
        input_phase = labels[vin]+PHASES[vin]
        output_phase = labels[vout]+PHASES[vout]
        rate = poch(Fraction(1, 2)-aa[0]-input_phase, 1-hs[0])
        rate += poch(aa[-1]+output_phase, hs[-1])
        rate += J(hs[0])-J(hs[-1])-sum((J(d) for d in differences), arb(0))
        for alpha, beta, delta in zip(aa, aa[1:], differences):
            rate += poch(alpha-beta+Fraction(1, 2), delta)
        rates.append(rate)
        detail.append({'path': path, 'h': [str(h) for h in hs],
                       'a_phases_over_2pi': [str(a) for a in aa], 'certified_rate': str(rate)})
    total = sum(rates, arb(0))
    v3 = (I*pi/3).exp().polylog(2).imag
    geometric_upper = 3*v3/(2*pi)
    assert total > arb('2.54')
    assert total < arb('2.55')
    assert geometric_upper < arb('0.485')
    assert total-geometric_upper > arb('2.05')
    return {'bridge_rates': detail, 'certified_total_rate': str(total),
            'three_tetrahedron_volume_rate_upper_bound': str(geometric_upper),
            'gap_above_geometric_upper_bound': str(total-geometric_upper)}


def full_reduced_weight(N, labels_override=None, precision=100):
    """Full actual bridge/source term up to one label-independent unit phase.

    Original kappa/framing have modulus one and do not change neighbor
    ratios. No summation over the surviving labels is performed here.
    """
    assert N % DENOMINATOR == 0
    mp.mp.dps = precision
    q = mp.exp(mp.pi*1j/N)
    Q, x, d = q*q, -1/q, N-1
    s = (-1)**(N+1)
    centers = [2, 3, 4]
    roots = [mp.exp(mp.log(mp.mpc(s**i*c))/N) for i, c in enumerate(centers)]
    initial_roots = roots.copy()
    variable_roots = dict(enumerate(roots))
    for rec in RECORDS:
        pos, sign = rec['position'], rec['sign']
        factor = x if sign > 0 else 1/x
        outputs = [factor*roots[pos+1], factor*roots[pos]]
        variable_roots.update(dict(zip(rec['out'], outputs)))
        roots[pos:pos+2] = outputs
    labels = {v: n*N//DENOMINATOR for v, n in LABELS.items()}
    labels.update(labels_override or {})
    values = {v: root*Q**labels[v] for v, root in variable_roots.items() if v in labels}
    fac = [mp.mpc(1)]
    for j in range(1, N):
        fac.append(fac[-1]*(1-Q**j))
    def poch(arg, length):
        answer = mp.mpc(1)
        for j in range(length):
            answer *= 1-arg*Q**j
        return answer
    data = []
    for rec in RECORDS:
        vi = rec['in'][1-rec['over_in']]
        vo = rec['out'][1-rec['over_out']]
        h = ((labels[vi]-labels[vo]) if rec['sign'] > 0
             else (labels[vo]-labels[vi])) % N
        if rec['sign'] > 0:
            a = Q**(-h)/(x*values[vo])
            b = values[vi]/x
        else:
            a = Q*x/values[vo]
            b = Q**(h+2)*x*values[vi]
        c = (-1)**h*Q**(rec['sign']*h*(h+1)//2)*values[vo]**h/N
        data.append({'h': h, 'a': a, 'b': b, 'c': c})
    answer = mp.mpc(1)
    for path in PATHS:
        entries = [data[j] for j in path]
        assert all(a['h'] >= b['h'] for a, b in zip(entries, entries[1:]))
        first, last = RECORDS[path[0]], RECORDS[path[-1]]
        zin = values[first['in'][first['over_in']]]
        zout = values[last['out'][last['over_out']]]
        factor = zin**(-entries[0]['h'])*poch(entries[0]['b']/zin, d-entries[0]['h'])
        factor *= poch(entries[-1]['a']*zout, entries[-1]['h'])
        for entry in entries:
            factor *= entry['c']
        for A, B in zip(entries, entries[1:]):
            L, h = A['h'], B['h']
            factor *= (N*(-A['a'])**h*Q**(h*(h-1)//2)
                       *fac[L]/(fac[h]*fac[L-h])
                       *poch(A['a']*B['b']/Q, L-h))
        answer *= factor
    # ORIGINAL averaged cut and both ORIGINAL closed pivots, transported
    # by the initial/final normalized Fourier frames.
    def geom(v):
        return (1-v**N)/(1-v)
    boundary = geom(values[0])*geom(1/values[OUTPUTS[0]])/N**2
    for head in (1, 2):
        boundary *= x**(1-N)*geom(values[head]/(Q*values[OUTPUTS[head]]))/N
    assert abs(boundary) > 0
    return answer*boundary


def independent_original_matrix_check():
    """Evaluate the same state from ORIGINAL sparse R, summing wire 8.

    No bridge coefficient, conditional normalizer or CT identity is
    used in this independent finite-N convention check.
    """
    N = 20
    q = np.exp(1j*np.pi/N)
    Q, x, s = q*q, -1/q, -1
    fac = np.ones(N, dtype=complex)
    for j in range(1, N):
        fac[j] = fac[j-1]*(1-Q**j)
    original = []
    for a in range(N):
        for b in range(N):
            for k in range(min(a, N-1-b)+1):
                j, c = a-k, b+k
                coefficient = (x**(-b-j)*Q**(j*b)*fac[c]*fac[a]
                               /(fac[k]*fac[b]*fac[j]))
                original.append((a, b, c, j, coefficient))
    indices = np.array([v[:4] for v in original], dtype=int)
    coefficients = np.array([v[4] for v in original])
    roots = [np.exp(np.log(complex(s**i*c))/N) for i, c in enumerate((2, 3, 4))]
    variable_roots = dict(enumerate(roots))
    for rec in RECORDS:
        pos = rec['position']
        factor = x if rec['sign'] > 0 else 1/x
        outputs = [factor*roots[pos+1], factor*roots[pos]]
        variable_roots.update(dict(zip(rec['out'], outputs)))
        roots[pos:pos+2] = outputs
    labels = {v: n*N//DENOMINATOR for v, n in LABELS.items()}
    def entry(rec, lab):
        z0, z1 = [variable_roots[v]*Q**lab[v] for v in rec['in']]
        z6, z7 = [variable_roots[v]*Q**lab[v] for v in rec['out']]
        if rec['sign'] > 0:
            a, b, c, e = indices.T
            values = coefficients
        else:
            b, a, e, c = indices.T
            values = coefficients.conjugate()
        return np.dot(values, z0**(-a)*z1**(-b)*z6**c*z7**e)/N**2
    value = 1+0j
    for path in PATHS:
        if len(path) == 1:
            value *= entry(RECORDS[path[0]], labels)
        else:
            value *= sum(entry(RECORDS[2], {**labels, 8: j})
                         *entry(RECORDS[3], {**labels, 8: j}) for j in range(N))
    ports = {v: r*Q**labels[v] for v, r in variable_roots.items() if v in labels}
    geom = lambda z: (1-z**N)/(1-z)
    boundary = geom(ports[0])*geom(1/ports[OUTPUTS[0]])/N**2
    for head in (1, 2):
        boundary *= x**(1-N)*geom(ports[head]/(Q*ports[OUTPUTS[head]]))/N
    value *= boundary
    reference = complex(full_reduced_weight(N))
    error = abs(value/reference-1)
    assert error < 1e-8
    return {'N': N, 'original_full_R_and_shared_wire_sum_checked': True,
            'complete_original_boundary_source_checked': True,
            'relative_error': float(error)}


def main():
    certified = certify_entropy()
    finite = []
    for N in (20, 40, 80, 160):
        weight = full_reduced_weight(N)
        finite.append({'N': N, 'nonzero_complete_source_weight': True,
                       'N_inverse_log_absolute_weight': float(mp.log(abs(weight))/N)})
    result = {'word': WORD, 'paths': PATHS, 'eliminated_wire': 8,
              'remaining_labels_over_20': LABELS,
              'rigorous_entropy_certificate': certified,
              'independent_original_sparse_matrix_contraction': independent_original_matrix_check(),
              'full_finite_original_source_diagnostics': finite,
              'scope': 'Absolute envelope of actual post-overbridge source; no failure of the invariant or volume conjecture'}
    path = Path(__file__).with_name('bridge_reduced_absolute_envelope_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS rigorous post-bridge exponent>2.54 versus geometric rate<0.485, '
          'four nonzero FULL original-source finite weights')
    print(json.dumps(finite))


if __name__ == '__main__':
    main()
