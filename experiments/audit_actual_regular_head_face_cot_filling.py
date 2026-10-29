#!/usr/bin/env python3
"""Original two-neighbor head factorization and zero-side normal identities.

The finite-field checks retain literal signed R, kappa, pivots and external
line. Complex checks use the independent Barnes factorial. The all-level
normal bounds and residue-cycle assertions are proved in the note.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp

from audit_actual_scalar_cardinal_source_completion import knot_routing
from audit_actual_scalar_cardinal_source_completion import cardinal
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_exact_factorial_interpolation import factorial


def arc_metadata(strands, word):
    offsets, crossings = knot_routing(strands,word)
    count = strands+2*len(word)
    parent = list(range(count))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i,j):
        parent[find(i)] = find(j)

    active = list(range(strands))
    input_role, output_role = {}, {}
    for letter,(a,b,c,e,sign) in zip(word,crossings):
        pos = abs(letter)-1
        assert active[pos:pos+2] == [a,b]
        input_role[a],input_role[b] = ('O','U') if sign>0 else ('U','O')
        output_role[c],output_role[e] = ('U','O') if sign>0 else ('O','U')
        active[pos:pos+2] = [c,e]
    for i,node in enumerate(active):
        union(i,node)
    groups = {}
    for node in range(count):
        groups.setdefault(find(node),[]).append(node)
    arcs = []
    for nodes in groups.values():
        ins = [input_role[node] for node in nodes if node in input_role]
        outs = [output_role[node] for node in nodes if node in output_role]
        assert len(ins) == len(outs) == 1
        assert len({offsets[node] for node in nodes}) == 1
        before,after = outs[0],ins[0]
        exponent = (1 if before=='U' else -1)+(1 if after=='O' else -1)
        assert exponent == (2 if (before,after)==('U','O') else
                            -2 if (before,after)==('O','U') else 0)
        arcs.append(dict(nodes=nodes,offset=offsets[nodes[0]],
                         before=before,after=after,exponent=exponent))
    assert len(arcs) == 2*len(word)
    return offsets,crossings,arcs


def original_factorization_case(N,strands,word):
    H = HardyNetwork(N,1)
    p,d = H.p,N-1
    offsets,crossings,arcs = arc_metadata(strands,word)
    g = [pow(-1,a,p)*pow(H.Q,-a*(a+1)//2,p) % p for a in range(N)]
    checks = low = high = strict = 0
    total_literal = total_grouped = 0
    for u in itertools.product(range(N),repeat=len(word)+1):
        t,ks = u[0],u[1:]
        colors = {node:t+sum(a*b for a,b in zip(row,ks)) for node,row in offsets.items()}
        if any(not 0 <= value < N for value in colors.values()):
            continue
        literal = prefactor = 1
        for k,(a,b,c,e,sign) in zip(ks,crossings):
            a,b,c,e = (colors[v] for v in (a,b,c,e))
            R = H.plus if sign>0 else H.minus
            literal = literal*int(R[c*N+e,a*N+b]) % p
            if sign>0:
                phase = H.kappa*pow(H.x,-a-b+k,p)*pow(H.Q,b*(a-k),p)
            else:
                phase = (pow(H.kappa,-1,p)*pow(H.x,a+b-k,p)*pow(H.Q,-a*(b-k),p)
                         *g[e]*g[b]*pow(g[k]*g[a]*g[c] % p,-1,p))
            prefactor = prefactor*phase*pow(H.fac[k],-1,p) % p
        grouped = prefactor
        for arc in arcs:
            h = colors[arc['nodes'][0]]
            grouped = grouped*pow(H.fac[h],arc['exponent'],p) % p
        assert literal == grouped, (N,word,u,literal,grouped)
        pivot = 1
        for i in range(1,strands):
            pivot = pivot*int(H.pivot[colors[i]]) % p
        total_literal = (total_literal+pivot*literal) % p
        total_grouped = (total_grouped+pivot*grouped) % p
        checks += 1
        if all(k>0 for k in ks):
            strict += 1
            for arc in arcs:
                h = colors[arc['nodes'][0]]
                if h == 0:
                    assert (arc['before'],arc['after'],arc['exponent']) == ('O','U',-2)
                    low += 1
                if h == d:
                    assert (arc['before'],arc['after'],arc['exponent']) == ('U','O',2)
                    high += 1
    assert total_literal == total_grouped
    external = H.dimension*pow(H.twist,-sum(1 if a>0 else -1 for a in word),p) % p
    period = total_literal*pow(N,-1,p)*external % p
    return dict(N=N,strands=strands,word=list(word),original_valid_statewise_checks=checks,
                strict_transfer_states=strict,regular_low_head_incidence_checks=low,
                regular_high_head_incidence_checks=high,physical_arc_count=len(arcs),
                normalized_original_period_mod_p=int(period),
                original_kappa_pivots_framing_and_external_line_retained=True)


def complex_identities():
    conversion = normal = reflection = 0
    largest = mp.mpf(0)
    for N in (3,5,8):
        for z in (mp.mpc('.3','.2'),mp.mpc(N/3,'-.4'),mp.mpc('-.4','.3')):
            minus = mp.conj(factorial(N,mp.conj(z)))
            predicted = mp.exp(1j*mp.pi*z-1j*mp.pi*z*(z+1)/N)*factorial(N,z)
            error = abs(minus/predicted-1)
            largest = max(largest,error)
            assert error < mp.mpf('1e-55')
            conversion += 1
    for N in (5,8,12):
        Q = mp.exp(2j*mp.pi/N)
        for M in (1,2):
            nu = mp.mpc('-.5','.35')
            left = 1/factorial(N,nu-M)
            product = mp.fprod(1-Q**(nu-r) for r in range(M))/factorial(N,nu)
            error = abs(left/product-1)
            largest = max(largest,error)
            assert error < mp.mpf('1e-55')
            normal += 1
            nu = mp.mpc('.4','-.35')
            right = factorial(N,N-1+nu+M)
            product = factorial(N,N-1+nu)*mp.fprod(1-Q**(nu+r-1) for r in range(1,M+1))
            error = abs(right/product-1)
            largest = max(largest,error)
            assert error < mp.mpf('1e-55')
            normal += 1
            predicted = N*mp.exp(1j*mp.pi*nu*(nu+N-1)/N)/factorial(N,-nu)
            error = abs(factorial(N,N-1+nu)/predicted-1)
            largest = max(largest,error)
            assert error < mp.mpf('1e-55')
            reflection += 1
    return dict(whole_negative_root_chirp_identities=conversion,
                lower_upper_exact_normal_products=normal,
                phase_retained_upper_reflections=reflection,
                largest_relative_error=float(largest))


def complete_active_cluster_checks():
    normalized = reflections = cancellations = 0
    largest_scaled_log = mp.mpf(0)
    for N in (8,16,32):
        h = 2j*mp.pi/N
        for s in (mp.mpc('.2','.3'),mp.mpc('-1.4','.2'),mp.mpc('2.7','-.35')):
            A = factorial(N,s)/(mp.exp(s*mp.log(-h))*mp.gamma(s+1))
            scaled = abs(mp.log(A))*N/(abs(s)+1)**2
            largest_scaled_log = max(largest_scaled_log,scaled)
            assert scaled < 20
            normalized += 1
            for orientation in (-1,1):
                left = cardinal(N,N-1+s,orientation)
                right = cardinal(N,-s,-orientation)
                assert abs(left-right) < mp.mpf('1e-55')*max(1,abs(left),abs(right))
                reflections += 1
    # An aggregate with q=2*(-1)+(-1)*(-3)=1>0. Its first
    # Fhat(-z)^2 factor grows rather than going to its own zero side.
    # The FULL cardinal factors remove both sets of Gamma poles.
    N = 16
    delta = mp.mpc('1e-8','2e-9')
    for M in (1,2,3):
        def packet(z):
            return (factorial(N,-z)**2*cardinal(N,-z)**3
                    /factorial(N,-3*z)*cardinal(N,-3*z)**3)
        p1,p2 = packet(M+delta),packet(M+delta/2)
        observed = mp.log(abs(p1/p2))/mp.log(2)
        # (3-2)+(3+1)=5 is the COMPLETE pole-cancelled order.
        assert abs(observed-5) < mp.mpf('2e-5')
        cancellations += 1
    return dict(normalized_zero_free_Gamma_factor_checks=normalized,
                exact_upper_window_orientation_reflections=reflections,
                mixed_direction_complete_cluster_cancellations=cancellations,
                largest_scaled_abs_log_A=float(largest_scaled_log))


def main():
    words = [(2,[1,1,1]),(3,[1,-2,1,-2]),
             (4,[1,2,3]),(3,[1,-2,1,1,-2,-2])]
    cases = [original_factorization_case(N,b,w) for N in (2,3,4) for b,w in words]
    assert sum(r['regular_low_head_incidence_checks'] for r in cases)>0
    assert sum(r['regular_high_head_incidence_checks'] for r in cases)>0
    with mp.workdps(75):
        exact = complex_identities()
        active = complete_active_cluster_checks()
    result = dict(status='PASS',original_source_composition_cases=cases,
                  actual_complex_normal_identities=exact,
                  complete_active_cluster_checks=active,
                  scope='Exact actual signed two-neighbor composition and zero-side scalar normal formulas. Uniform contour estimates are proved in the note; no simultaneous-corner or global volume conclusion is tested.')
    target = Path(__file__).with_name('actual_regular_head_face_cot_filling_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',original_source_cases=len(cases),
                         statewise_original_compositions=sum(r['original_valid_statewise_checks'] for r in cases),
                         low_head_incidence_checks=sum(r['regular_low_head_incidence_checks'] for r in cases),
                         high_head_incidence_checks=sum(r['regular_high_head_incidence_checks'] for r in cases),
                         complex=exact,active_cluster=active),indent=2))


if __name__ == '__main__':
    main()
