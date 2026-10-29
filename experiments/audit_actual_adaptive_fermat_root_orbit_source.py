#!/usr/bin/env python3
"""Adaptive resonant root source, both original signs, and first normal jets."""

import itertools
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork, whole_word
from audit_signed_green_antiunitary_transport import mirror_parameters


def terms(H):
    N, p, Q, x = H.N, H.p, H.Q, H.x
    pairs = [(i, j) for i in range(N) for j in range(N-i)]
    pp = [H.v[j]*pow(x, j, p) % p for j in range(N)]
    bb = {(i, j): H.fac[i+j]*H.inv[i]*pp[j] % p for i, j in pairs}
    rr = {(i, j): H.fac[i+j]*H.inv[i]*H.inv[j] % p for i, j in pairs}
    out = defaultdict(int)
    for (i, j), (r, k), (h, ell) in itertools.product(pairs, repeat=3):
        key = (j+r, i, r+k-h, h+ell, i+j-k-ell)
        value = H.kappa*bb[i, j]*rr[r, k]*bb[h, ell]*pow(x, -j-k-h-2*ell, p) % p
        out[key] = (out[key]+value) % p
    return {k: v for k, v in out.items() if v}


def raw_adaptive(H, A=1):
    out = defaultdict(int)
    alias_count = 0
    for (a, b, c, d, e), value in terms(H).items():
        assert -2*(H.N-1) <= e <= H.N-1
        if e == 0:
            out[a, b, c, d] = (out[a, b, c, d]+value) % H.p
        elif e == -H.N:
            alias_count += 1
            assert b >= 0 and d < H.N
            out[a, b+H.N, c, d] = (out[a, b+H.N, c, d]+value) % H.p
            out[a, b, c, d-H.N] = (out[a, b, c, d-H.N]-A*value) % H.p
    assert alias_count
    return {k: v for k, v in out.items() if v}


def finite_matrix(N, p, raw):
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for (a, b, c, d), value in raw.items():
        if min(a, b, c, d) >= 0 and max(a, b, c, d) < N:
            out[c*N+d, a*N+b] = (out[c*N+d, a*N+b]+value) % p
    return out


class AdaptiveNetwork(HardyNetwork):
    def __init__(self, N):
        super().__init__(N, 1)
        positive = raw_adaptive(self)
        mirror = raw_adaptive(mirror_parameters(self))
        negative = {(b, a, d, c): v for (a, b, c, d), v in mirror.items()}
        self.raw = {}
        for sign, data in [(1, positive), (-1, negative)]:
            by_input = defaultdict(list)
            for (a, b, c, d), value in data.items():
                by_input[a, b].append(((c, d), value))
            self.raw[sign] = by_input
        self.invalid_outputs = self.invalid_inputs = 0

    def crossing(self, states, letter):
        i = abs(letter)-1
        sign = 1 if letter > 0 else -1
        out = defaultdict(int)
        for s, value in states.items():
            if min(s[i:i+2]) < 0:
                self.invalid_inputs += 1
            for target, coefficient in self.raw[sign].get(s[i:i+2], []):
                if min(target) < 0:
                    self.invalid_outputs += 1
                assert max(target) < self.N
                key = s[:i]+target+s[i+2:]
                out[key] = (out[key]+value*coefficient) % self.p
        return {s: v for s, v in out.items() if v}

    def word(self, initial, letters):
        states = {initial: 1}
        for letter in letters:
            states = self.crossing(states, letter)
        return {s: v for s, v in states.items() if min(s) >= 0}


def scalar_polys(H, t, z0, z1, z6, z7):
    N, p, Q, x = H.N, H.p, H.Q, H.x
    pp = [H.v[j]*pow(x, j, p) % p for j in range(N)]
    def B(u, v):
        return sum(H.fac[i+j]*H.inv[i]*pp[j]*pow(u, i, p)*pow(v, j, p)
                   for i in range(N) for j in range(N-i)) % p
    def R(u, v):
        return sum(H.fac[i+j]*H.inv[i]*H.inv[j]*pow(u, i, p)*pow(v, j, p)
                   for i in range(N) for j in range(N-i)) % p
    u0, v0 = t*pow(z1, -1, p) % p, pow(x, -1, p)*t*pow(z0, -1, p) % p
    aa = pow(x, -1, p)*z7*pow(z6, -1, p) % p
    cc, ww = z6*pow(z0, -1, p) % p, pow(x, -1, p)*z6*pow(t, -1, p) % p
    db, dr = (1-pow(aa, N, p)+pow(aa*ww, N, p)) % p, (1-pow(cc, N, p)-pow(ww, N, p)) % p
    d0 = (1-pow(u0, N, p)+pow(v0, N, p)) % p
    F = B(aa, aa*ww % p)*R(cc, ww) % p
    Fprev = B(aa, Q*aa*ww % p)*R(cc, Q*ww % p) % p
    hp = (db*R(cc, ww)+aa*dr*B(aa, Q*aa*ww % p)) % p
    eta = H.kappa*(B(u0, v0)*hp+Q*aa*cc*pow(v0, -1, p)*d0*Fprev) % p
    return H.kappa*B(u0, v0)*F % p, eta


def finite_resonance(H):
    N, p, Q = H.N, H.p, H.Q
    roots = {pow(z, N, p): z for z in range(1, p)}
    z1 = 1
    for t0 in range(2, p):
        zz = (1-pow(t0, -N, p)) % p
        if zz and pow(zz, -1, p) in roots:
            z7 = roots[pow(zz, -1, p)]
            break
    else:
        raise AssertionError('missing regular finite Fermat point')
    z0, z6 = 2, 5
    kernel = terms(H)
    Y, Ydot, eta, aa, adot = [], [], [], [], []
    ratio = z7*pow(z1, -1, p) % p
    Bcentral = pow(ratio, N, p)
    velocity = pow(N*(Bcentral-1), -1, p)
    for j in range(N):
        t = t0*pow(Q, j, p) % p
        value = derivative = 0
        for (a, b, c, d, e), coef in kernel.items():
            mono = coef*pow(z0, -a, p)*pow(z1, -b, p)*pow(z6, c, p)*pow(z7, d, p)*pow(t, e, p) % p
            value = (value+mono) % p
            derivative = (derivative+velocity*e*mono) % p
        bcoef = ratio*(1-Q*z1*pow(t, -1, p)) % p
        bdot = ratio*Q*z1*pow(t, -1, p)*velocity % p
        independent, source = scalar_polys(H, t, z0, z1, z6, z7)
        assert value == independent
        Y.append(value);Ydot.append(derivative);eta.append(source);aa.append(bcoef);adot.append(bdot)
    assert np.prod(np.array(aa, dtype=object)) % p == 1
    T = np.zeros((N, N), dtype=np.int64);Td = np.zeros_like(T)
    for j in range(N):T[j, (j-1) % N], Td[j, (j-1) % N] = aa[j], adot[j]
    Y, Ydot, eta = (np.array(v, dtype=np.int64) for v in (Y, Ydot, eta))
    assert np.array_equal((Y-T@Y) % p, eta)
    etadot = (Ydot-Td@Y-T@Ydot) % p
    G=np.eye(N,dtype=np.int64);Gd=np.zeros_like(G)
    power=G.copy();pdot=np.zeros_like(G)
    for k in range(1,N):
        pdot=(pdot@T+power@Td)%p;power=power@T%p
        G=(G+power)%p;Gd=(Gd+pdot)%p
    assert not np.any(G@eta % p)
    assert np.array_equal(-(Gd@eta+G@etadot) % p, Y)
    gg=[1];gd=[0]
    for j in range(1,N):
        value=aa[j]*gg[-1]%p
        derivative=(adot[j]*gg[-1]+aa[j]*gd[-1]-value*pow(N,-1,p))%p
        gg.append(value);gd.append(derivative)
    meanY=sum(int(Y[j])*pow(gg[j],-1,p) for j in range(N))*pow(N,-1,p)%p
    moment=sum((int(etadot[j])*pow(gg[j],-1,p)-int(eta[j])*gd[j]*pow(gg[j],-2,p))
               for j in range(N))*pow(N,-1,p)%p
    assert meanY == -N*moment % p
    return {'N':N,'regular_Fermat_point':{'z0':z0,'z1':z1,'z6':z6,'z7':z7,'t0':t0},
            'full_unsplit_source_recurrence':True,'resonant_solvability':True,
            'whole_state_first_normal_reconstruction':True,
            'actual_homogeneous_source_moment':int(meanY)}


def main():
    families=[];words=[];resonances=[]
    for N in range(2,8):
        H=AdaptiveNetwork(N)
        for A in [0,1,3]:
            positive=raw_adaptive(H,A)
            negative={(b,a,d,c):v for (a,b,c,d),v in raw_adaptive(mirror_parameters(H),A).items()}
            assert np.array_equal(finite_matrix(N,H.p,positive),H.plus)
            assert np.array_equal(finite_matrix(N,H.p,negative),H.minus)
        families.append({'N':N,'all_source_parameters':[0,1,3],
                         'both_original_finite_crossings_entrywise_equal':True,
                         'input_output_alias_walls_retained':True})
        resonances.append(finite_resonance(H))
        if N<=4:
            for heads,word in [(3,[1,-2,1,-2]),(4,[2,-1,3,2]),(3,[-1,2,-1,2])]:
                row=whole_word(H,heads,word)
                row.update(raw_invalid_outputs_retained=H.invalid_outputs,
                           raw_invalid_inputs_killed_by_support=H.invalid_inputs)
                words.append(row)
    result={'status':'PASS','adaptive_source_operator_families':families,
            'original_whole_signed_sources':words,'resonant_normal_sources':resonances,
            'scope':'Complete kernels only; no sectorwise alias deletion or global geometric noncancellation.'}
    Path(__file__).with_name('actual_adaptive_fermat_root_orbit_source_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS six all-parameter signed adaptive operator families, nine original signed '
          'word sources and six full resonant first-normal-source reconstructions')


if __name__=='__main__':main()
