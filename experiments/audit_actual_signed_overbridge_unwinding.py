#!/usr/bin/env python3
"""Exact complementary contractions and all signed original overbridge interiors."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix
from audit_whole_fermat_toric_residue_and_wire_source import frame, kron_all, sources


def inv(a, p):
    return pow(int(a) % p, -1, p)


def poch(H, a, length):
    answer = 1
    for j in range(length):
        answer = answer*(1-a*pow(H.Q, j, H.p)) % H.p
    return answer


def polynomial(H, a, length):
    answer = [1]
    for j in range(length):
        term = -a*pow(H.Q, j, H.p) % H.p
        new = [0]*(len(answer)+1)
        for k, value in enumerate(answer):
            new[k] = (new[k]+value) % H.p
            new[k+1] = (new[k+1]+term*value) % H.p
        answer = new
    return answer


def qbinom(H, a, b):
    if not 0 <= b <= a < H.N:
        return 0
    return H.fac[a]*inv(H.fac[b]*H.fac[a-b], H.p) % H.p


def over_link(H, L, s, a, b):
    if s > L:
        return 0
    return (pow(-a, s, H.p)*pow(H.Q, s*(s-1)//2, H.p)
            *qbinom(H, L, s)*poch(H, a*b*inv(H.Q, H.p) % H.p, L-s)) % H.p


def complement_identities():
    rows = []
    for N in range(2, 13):
        H = HardyNetwork(N, 1)
        p, d = H.p, N-1
        count = 0
        for a, b in ((2, 3), (5, 7)):
            for L, s in itertools.product(range(N), repeat=2):
                A, B = polynomial(H, a, L), polynomial(H, b, d-s)
                actual = sum(A[j+s]*B[j] for j in range(len(B)) if j+s < len(A)) % p
                assert actual == over_link(H, L, s, a, b)
                # Mirrored under contraction is the same identity after Z->Z^-1.
                C, D = polynomial(H, a, d-s), polynomial(H, b, L)
                mirrored = sum(C[j]*D[j+s] for j in range(len(C)) if j+s < len(D)) % p
                assert mirrored == over_link(H, L, s, b, a)
                count += 2
        rows.append({'N': N, 'arbitrary_parameter_over_under_CT_identities': count,
                     'no_norm_one_condition': True})
    return rows


def general_hypergeometric_check():
    rows = []
    for N in range(2, 9):
        H = HardyNetwork(N, 1)
        p, Q, a, b = H.p, H.Q, 2, 3
        count = 0
        for L, K in itertools.product(range(N), repeat=2):
            A, B = polynomial(H, a, L), polynomial(H, b, K)
            for h in range(L+1):
                actual = sum(A[j+h]*B[j] for j in range(K+1) if j+h <= L) % p
                prefactor = pow(-a, h, p)*pow(Q, h*(h-1)//2, p)*qbinom(H, L, h) % p
                t = a*b*pow(Q, L+K, p) % p
                series = 0
                for j in range(min(K, L-h)+1):
                    numerator = poch(H, pow(Q, h-L, p), j)*poch(H, pow(Q, -K, p), j) % p
                    denominator = poch(H, pow(Q, h+1, p), j)*H.fac[j] % p
                    series = (series+numerator*inv(denominator, p)*pow(t, j, p)) % p
                assert actual == prefactor*series % p
                count += 1
        rows.append({'N': N, 'general_terminating_two_phi_one_parameters_checked': count})
    return rows


def local_record(H, sign, roots):
    N, p = H.N, H.p
    inf = [frame(H, r) for r in roots]
    factor = H.x if sign > 0 else inv(H.x, p)
    outs = [factor*roots[1] % p, factor*roots[0] % p]
    outf = [frame(H, r) for r in outs]
    Gout = np.kron(outf[0][1], outf[1][1]) % p
    Gini = np.kron(inf[0][2], inf[1][2]) % p
    physical = H.plus if sign > 0 else H.minus
    M = (Gout@physical % p)@Gini % p
    return {'sign': sign, 'in': inf, 'out': outf,
            'M': M.reshape(N, N, N, N)}, outs


def conditional(H, record, role, input_spectator, output_spectator):
    N, p, x, Q = H.N, H.p, H.x, H.Q
    sign = record['sign']
    i, k = input_spectator, output_spectator
    if role == 'over':
        inp, out = (0, 1) if sign > 0 else (1, 0)
        if sign > 0:
            h = (i-k) % N
            b = record['in'][1][0][i]*inv(x, p) % p
            a = pow(Q, -h, p)*inv(x*record['out'][0][0][k], p) % p
        else:
            h = (k-i) % N
            b = pow(Q, h+2, p)*x*record['in'][0][0][i] % p
            a = Q*x*inv(record['out'][1][0][k], p) % p
    else:
        inp, out = (1, 0) if sign > 0 else (0, 1)
        if sign > 0:
            h = (i-k) % N
            b = pow(Q, 1-h, p)*x*record['in'][0][0][i] % p
            a = pow(Q, h+1, p)*inv(record['in'][0][0][i], p) % p
        else:
            h = (k-i) % N
            b = inv(x, p)*record['in'][1][0][i] % p
            a = Q*inv(record['in'][1][0][i], p) % p
    assert a*b % p == Q*Q*x % p
    if role == 'over':
        pin = np.array([pow(z, -h, p)*poch(H, b*inv(z, p) % p, N-1-h) % p
                        for z in record['in'][inp][0]], dtype=np.int64)
        pout = np.array([poch(H, a*z % p, h) for z in record['out'][out][0]], dtype=np.int64)
    else:
        pin = np.array([poch(H, b*inv(z, p) % p, h) for z in record['in'][inp][0]], dtype=np.int64)
        pout = np.array([pow(z, h, p)*poch(H, a*z % p, N-1-h) % p
                         for z in record['out'][out][0]], dtype=np.int64)
    D = np.empty((N, N), dtype=np.int64)
    for j, ell in itertools.product(range(N), repeat=2):
        ins = [i, i]
        outs = [k, k]
        ins[inp], outs[out] = ell, j
        D[j, ell] = record['M'][tuple(outs+ins)]
    assert int(pin[0])*int(pout[0]) % p
    reference_scalar = int(D[0, 0])*inv(int(pin[0])*int(pout[0]), p) % p
    assert reference_scalar
    exponent = h*(h+1)//2
    phase = pow(-1, h, p)*pow(Q, exponent if sign > 0 else -exponent, p) % p
    if role == 'over':
        other_output = record['out'][1-out][0][k]
        port_power = pow(other_output, h, p)
    else:
        other_input = record['in'][1-inp][0][i]
        port_power = pow(other_input, -h, p)
    scalar = (pow(H.kappa, sign, p)*inv(N, p)*phase*port_power) % p
    assert reference_scalar == scalar, (N, sign, role, i, k, reference_scalar, scalar)
    assert np.array_equal(D, scalar*np.outer(pout, pin) % p)
    return {'h': h, 'a': a, 'b': b, 'c': scalar, 'pin': pin, 'pout': pout,
            'inp': inp, 'out': out}


def all_signed_port_tables():
    rows = []
    for N in range(2, 11):
        H = HardyNetwork(N, 1)
        roots = [2, next(r for r in range(3, H.p)
                         if pow(r, N, H.p) != pow(H.x*2, N, H.p))]
        count = 0
        for sign, role in itertools.product((1, -1), ('over', 'under')):
            R, _ = local_record(H, sign, roots)
            for i, k in itertools.product(range(N), repeat=2):
                conditional(H, R, role, i, k)
                count += 1
        rows.append({'N': N, 'all_original_signed_conditional_tables': count,
                     'original_scalar_normalizers_nonzero_and_retained': True,
                     'all_four_closed_scalar_formulas_checked': True,
                     'universal_ab_equals_Q_squared_x': True})
    return rows


def mul_factors(F, G, N, p):
    av, ad = F
    bv, bd = G
    uv = tuple(av)+tuple(v for v in bv if v not in av)

    def lifted(vs, data):
        order = sorted(range(len(vs)), key=lambda i: uv.index(vs[i]))
        data = np.transpose(data, order) if order else data
        sorted_vs = [vs[i] for i in order]
        return np.reshape(data, tuple(N if v in sorted_vs else 1 for v in uv))
    return uv, lifted(av, ad)*lifted(bv, bd) % p


def contract_factors(factors, N, p):
    factors = list(factors)
    variables = set(v for vs, _ in factors for v in vs)
    while variables:
        var = min(variables, key=lambda v: len(set(w for vs, _ in factors if v in vs for w in vs)))
        group = [f for f in factors if var in f[0]]
        factors = [f for f in factors if var not in f[0]]
        merged = group[0]
        for other in group[1:]:
            merged = mul_factors(merged, other, N, p)
        vs, data = merged
        axis = vs.index(var)
        data = np.sum(data, axis=axis) % p
        factors.append((tuple(v for v in vs if v != var), data))
        variables.remove(var)
    answer = 1
    for _, value in factors:
        answer = answer*int(value) % p
    return answer


def make_network(H, width, word):
    p, N = H.p, H.N
    s = pow(H.x, N, p)
    roots, centers = [], []
    for i in range(width):
        r = next(r for r in range(1, p) if pow(s, i, p)*pow(r, N, p) % p not in centers)
        roots.append(r)
        centers.append(pow(s, i, p)*pow(r, N, p) % p)
    initial_roots = roots.copy()
    current_vars = list(range(width))
    initial_vars = tuple(current_vars)
    counter = width
    records = []
    for letter in word:
        pos, sign = abs(letter)-1, 1 if letter > 0 else -1
        R, newroots = local_record(H, sign, roots[pos:pos+2])
        ins = current_vars[pos:pos+2]
        outs = [counter, counter+1]
        counter += 2
        current_vars[pos:pos+2] = outs
        roots[pos:pos+2] = newroots
        R['invars'], R['outvars'] = ins, outs
        R['vars'] = tuple(outs+ins)
        records.append(R)
    return records, initial_vars, tuple(current_vars), initial_roots, roots


def over_paths(records):
    incoming, outgoing = {}, {}
    for j, R in enumerate(records):
        inp, out = (0, 1) if R['sign'] > 0 else (1, 0)
        R['over_in'], R['over_out'] = inp, out
        incoming[R['invars'][inp]] = j
        outgoing[R['outvars'][out]] = j
    following = {outgoing[v]: incoming[v] for v in outgoing.keys() & incoming.keys()}
    predecessors = set(following.values())
    paths = []
    for j in range(len(records)):
        if j in predecessors:
            continue
        path = [j]
        while path[-1] in following:
            path.append(following[path[-1]])
        paths.append(path)
    assert sorted(j for path in paths for j in path) == list(range(len(records)))
    return paths


def bridge_factor(H, records, path):
    N, p = H.N, H.p
    first, last = records[path[0]], records[path[-1]]
    vin = first['invars'][first['over_in']]
    vout = last['outvars'][last['over_out']]
    variables = [vin, vout]
    tables = []
    for j in path:
        R = records[j]
        si, so = R['invars'][1-R['over_in']], R['outvars'][1-R['over_out']]
        tables.append((si, so, {(i, k): conditional(H, R, 'over', i, k)
                               for i, k in itertools.product(range(N), repeat=2)}))
        for var in (si, so):
            if var not in variables:
                variables.append(var)
    data = np.zeros((N,)*len(variables), dtype=np.int64)
    survivors = 0
    for labels in np.ndindex(data.shape):
        state = dict(zip(variables, labels))
        entries = [table[state[si], state[so]] for si, so, table in tables]
        if any(entries[j+1]['h'] > entries[j]['h'] for j in range(len(entries)-1)):
            continue
        value = int(entries[0]['pin'][state[vin]])*int(entries[-1]['pout'][state[vout]]) % p
        for entry in entries:
            value = value*entry['c'] % p
        for A, B in zip(entries, entries[1:]):
            value = value*N*over_link(H, A['h'], B['h'], A['a'], B['b']) % p
        # The q-binomial product is exactly the retained q-multinomial.
        binoms = 1
        den = H.fac[entries[-1]['h']]
        for A, B in zip(entries, entries[1:]):
            binoms = binoms*qbinom(H, A['h'], B['h']) % p
            den = den*H.fac[A['h']-B['h']] % p
        assert binoms == H.fac[entries[0]['h']]*inv(den, p) % p
        assert sum(A['h']-B['h'] for A, B in zip(entries, entries[1:])) <= N-1
        data[labels] = value
        survivors += bool(value)
    # Independently contract the ORIGINAL entire conditioned crossing tensors.
    original = [(records[j]['vars'], records[j]['M']) for j in path]
    internal = set(v for vs, _ in original for v in vs)-set(variables)
    work = original.copy()
    for var in sorted(internal):
        group = [f for f in work if var in f[0]]
        work = [f for f in work if var not in f[0]]
        merged = group[0]
        for F in group[1:]:
            merged = mul_factors(merged, F, N, p)
        vs, arr = merged
        work.append((tuple(v for v in vs if v != var), np.sum(arr, axis=vs.index(var)) % p))
    merged = work[0]
    for F in work[1:]:
        merged = mul_factors(merged, F, N, p)
    vs, arr = merged
    arr = np.transpose(arr, [vs.index(v) for v in variables])
    assert np.array_equal(data, arr), (N, path)
    return (tuple(variables), data), {'crossings': len(path), 'interior_variables_removed': len(path)-1,
                                     'free_grid_variables': len(variables),
                                     'nonzero_conditional_entries': survivors}


def whole_source_case(N, word):
    H = HardyNetwork(N, 1)
    p, width = H.p, 4
    R, iv, ov, ir, outr = make_network(H, width, word)
    paths = over_paths(R)
    new_factors, reports = [], []
    for path in paths:
        factor, report = bridge_factor(H, R, path)
        new_factors.append(factor)
        reports.append(report)
    cup, cap, mark = sources(H)
    source_in = np.kron(cup, cup) % p
    source_out = np.kron(cap, mark) % p
    Gin = kron_all([frame(H, r)[1] for r in ir], p)
    Gouti = kron_all([frame(H, r)[2] for r in outr], p)
    pi = (Gin@source_in % p).reshape((N,)*width)
    mo = (source_out@Gouti % p).reshape((N,)*width)
    reduced = contract_factors(new_factors+[(iv, pi), (ov, mo)], N, p)
    literal = word_matrix(word, H.plus, H.minus, width, N, p)
    expected = int(source_out@(literal@source_in % p)) % p
    assert reduced == expected
    return {'N': N, 'word': word, 'overbridges': reports,
            'all_interiors_eliminated_simultaneously': True,
            'original_full_plat_source': expected,
            'full_original_normalizers_and_marked_row_retained': True,
            'bridge_factors_use_closed_scalar_not_reference_ratios': True}


def main():
    results = {'status': 'PASS', 'arbitrary_parameter_complement_identities': complement_identities(),
               'optional_general_hypergeometric_parameter_check': general_hypergeometric_check(),
               'all_four_original_signed_role_tables': all_signed_port_tables(),
               'whole_signed_original_overbridge_reductions': [
                   whole_source_case(N, word) for N in (2, 3)
                   for word in ([1, 2, 1, -2, -1], [1, 2, -1, 3, 2], [-3, -2, 3, -1, -2])],
               'scope': ('Exact simultaneous overbridge interiors with all original source factors. '
                         'Remaining bridge coefficients remain coupled; no second underbridge '
                         'pass or scalar volume/noncancellation assertion.')}
    Path(__file__).with_name('actual_signed_overbridge_unwinding_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS eleven all-clock complement families, nine full signed-port/closed-scalar families, '
          'six simultaneous whole original signed plat reductions')


if __name__ == '__main__':
    main()
