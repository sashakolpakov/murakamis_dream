#!/usr/bin/env python3
"""Signed finite bipyramid source diagnostic, not an asymptotic proof.

The raw original Casimir resolvent is constructed by a division-free path
recurrence, before FULL/CROSS restrictions. The south variable is shared.
No private import is required. mpmath is the sole external dependency.
"""
import argparse
from collections import defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import time

import mpmath as mp


def padd(a, b):
    c = [mp.mpf(0)] * max(len(a), len(b))
    for k, v in enumerate(a): c[k] += v
    for k, v in enumerate(b): c[k] += v
    return c


def pscale(a, c): return [c*v for v in a]


def pmul(a, b):
    c = [mp.mpf(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c


def chebyshev_coefficients(N):
    # 2 T_N(z/2), calculated over the integers.
    a, b = [2], [0, 1]
    for _ in range(1, N):
        c = [0]+b
        c += [0]*max(0, len(a)-len(c))
        for j, x in enumerate(a): c[j] -= x
        a, b = b, c
    b = b[:]
    b[0] += 2
    return b


def peval(a, z):
    value = mp.mpf(0)
    for x in a[::-1]: value = value*z+x
    return value


def constants(N):
    c = [mp.mpf(0)]*N
    for j in range((N+1)//2):
        value = -mp.mpf(2) if 2*j+1 == N else 2*mp.cos((2*j+1)*mp.pi/N)
        c[j] = c[N-1-j] = value
    s = [mp.mpf(0)]*(N+1)
    for j in range(1, N//2+1):
        value = mp.mpf(2) if 2*j == N else 2*mp.sin(j*mp.pi/N)
        s[j] = s[N-j] = value
    return c, s


def numerator(N, sigma):
    c, s = constants(N)
    pre = [mp.mpf(1)]
    for a in c: pre.append(pre[-1]*(sigma-a))
    suf = [mp.mpf(1)]*(N+1)
    for j in range(N-1, -1, -1): suf[j] = suf[j+1]*(sigma-c[j])
    V = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        P = [[mp.mpf(1)]]
        V[i][i] = [pre[i]*suf[i+1]]
        for j in range(i+1, N):
            cur = pmul([-s[j]**2, -s[j]**2], P[-1])
            if j > i+1:
                cur = padd(cur, [mp.mpf(0)]+pscale(P[-2], -s[j]*s[j-1]*(sigma-c[j-1])))
            P.append(cur)
            V[i][j] = pscale(cur, pre[i]*suf[j+1])
    return V


def matrix_identity_error(N, sigma, V):
    c, s = constants(N)
    chi = peval(chebyshev_coefficients(N), sigma)
    err, scale, checked = mp.mpf(0), mp.mpf(1), 0
    # Direct left multiplication of the genuine band matrix by V(S).
    for i in range(N):
        for j in range(i, N):
            terms = [pscale(V[i][j], sigma-c[i])]
            if i+1 <= j: terms.append(pmul([s[i+1]**2]*2, V[i+1][j]))
            if i+2 <= j: terms.append([mp.mpf(0)]+pscale(V[i+2][j], s[i+2]*s[i+1]))
            lhs = [mp.mpf(0)]
            for t in terms:
                lhs = padd(lhs, t)
                scale = max(scale, *(abs(x) for x in t))
            if i == j: lhs[0] -= chi
            err = max(err, *(abs(x) for x in lhs))
            checked += len(lhs)
    return err/scale, checked


def direct_power_numerator(N, sigma):
    c, s = constants(N)
    chi = chebyshev_coefficients(N)
    power = [[[mp.mpf(i == j)] for j in range(N)] for i in range(N)]
    result = [[[mp.mpf(0)] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        coeff = sum((chi[k]*sigma**(k-1-r) for k in range(r+1, N+1)), mp.mpf(0))
        for i in range(N):
            for j in range(i, N): result[i][j] = padd(result[i][j], pscale(power[i][j], coeff))
        nxt = [[[mp.mpf(0)] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(i, N):
                val = pscale(power[i][j], c[i])
                if i+1 <= j: val = padd(val, pmul([-s[i+1]**2]*2, power[i+1][j]))
                if i+2 <= j: val = padd(val, [mp.mpf(0)]+pscale(power[i+2][j], -s[i+2]*s[i+1]))
                nxt[i][j] = val
        power = nxt
    return result


def cross_allowed(N, i, j):
    # For odd N this includes the central row and paths which jump it.
    return i <= (N-1)//2 and j >= N//2


def local_monomials(N, position, V, sector):
    """Yield (south,previous-rim,current-rim,next-rim), signed coefficient."""
    d = N-1
    for i in range(N):
        for j in range(i, N):
            if sector == 'CROSS' and not cross_allowed(N, i, j): continue
            if position % 2:
                yield (0, i, j-i, d-j), V[i][j][0]
            else:
                for p, value in enumerate(V[i][j]):
                    yield (p, d-j, j-i-p, i), value


def transitions(N, position, V, sector):
    d = N-1
    target = 0 if position == 1 else d
    rows = [[] for _ in range(N*N)]
    for (p, a, b, cc), value in local_monomials(N, position, V, sector):
        u = target-a
        if not 0 <= u <= d or not value: continue
        for v in range(N-b):
            up, vp = v+b, cc
            assert up+vp == u+v+d-target-p
            rows[u*N+v].append((up*N+vp, value))
    return rows


def contract(N, spectra, sector, cache):
    m, d = len(spectra), N-1
    # Cut immediately before the unique marked north step. Its input u=0.
    initial = [[mp.mpf(0)]*(N*N) for _ in range(N)]
    for v in range(N): initial[v][v] = mp.mpf(1)
    largest = mp.mpf(1)
    for position in list(range(1,m))+[0]:
        key = (spectra[position], position % 2, position == 1, sector)
        if key not in cache:
            V = numerator(N, mp.mpf(spectra[position]))
            cache[key] = transitions(N, position, V, sector)
        T = cache[key]
        new = [[mp.mpf(0)]*(N*N) for _ in range(N)]
        for v in range(N):
            row, out = initial[v], new[v]
            for old, value in enumerate(row):
                if value:
                    for nxt, factor in T[old]: out[nxt] += value*factor
            largest = max(largest, *(abs(x) for x in out))
        initial = new
    diagonal = [initial[v][v] for v in range(N)]
    return mp.fsum(diagonal), largest, diagonal


def brute_coefficient(N, spectra, sector):
    """Independent homogeneous matrix construction and coefficient product.

    Here C(x,y) is built with the ACTUAL global face monomials; no south
    coefficient indexing or local_monomials() map from the transfer is used.
    """
    m, d = len(spectra), N-1
    target = (d,)+(d,)*(m-1)  # variables S,z1,...,z(m-1); z0=0
    zero=(0,)*m
    one={zero:mp.mpf(1)}
    def add(a,b):
        r=dict(a)
        for k,v in b.items(): r[k]=r.get(k,mp.mpf(0))+v
        return r
    def scale(a,v): return {k:x*v for k,x in a.items() if x*v}
    def mul(a,b):
        r=defaultdict(lambda:mp.mpf(0))
        for x,aa in a.items():
            for y,bb in b.items():
                z=tuple(xi+yi for xi,yi in zip(x,y))
                if all(zi<=d for zi in z): r[z]+=aa*bb
        return dict(r)
    def variable(idx):
        if idx is None: return {}
        z=[0]*m;z[idx]=1
        return {tuple(z):mp.mpf(1)}
    def power(a,r):
        value=one
        for _ in range(r): value=mul(value,a)
        return value
    def rim(idx): return variable(idx%m) if idx%m else {}
    current = one
    diagonal,sines=constants(N)
    chi=chebyshev_coefficients(N)
    for position, sigma in enumerate(spectra):
        sig=mp.mpf(sigma)
        x={} if position%2 else variable(0)
        y=rim(position)
        b,c=(rim(position-1),rim(position+1)) if position%2 else (rim(position+1),rim(position-1))
        aa,bb=add(x,y),mul(x,y)
        P=[[one if i==j else {} for j in range(N)] for i in range(N)]
        V=[[{} for _ in range(N)] for _ in range(N)]
        for r in range(N):
            weight=sum((chi[k]*sig**(k-1-r) for k in range(r+1,N+1)),mp.mpf(0))
            for i in range(N):
                for j in range(i,N): V[i][j]=add(V[i][j],scale(P[i][j],weight))
            nxt=[[{} for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(i,N):
                    val=scale(P[i][j],diagonal[i])
                    if i+1<=j: val=add(val,scale(mul(aa,P[i+1][j]),-sines[i+1]**2))
                    if i+2<=j: val=add(val,scale(mul(bb,P[i+2][j]),-sines[i+2]*sines[i+1]))
                    nxt[i][j]=val
            P=nxt
        local={}
        for i in range(N):
            for j in range(i,N):
                # Independent complement of the two one-sided original blocks.
                if sector=='CROSS' and (j <= N//2-1 or i >= N-N//2): continue
                local=add(local,mul(mul(power(b,i),V[i][j]),power(c,d-j)))
        current=mul(current,local)
    return current.get(target, mp.mpf(0))


def lob(t): return mp.im(mp.polylog(2, mp.exp(2j*t)))/2


def triangle(x,b,y):
    vals = [x,b,y]
    positives = [v for v in vals if v > 0]
    if len(positives) == 1: return mp.log(positives[0])/2
    delta = mp.sqrt(x*b+b*y+y*x)
    angles = [2*mp.atan(v/delta) if v else mp.mpf(0) for v in vals]
    volume = 2*mp.fsum(lob(t/2)+lob((mp.pi-t)/2) for t in angles)
    logs = mp.fsum(t*mp.log(v) for t,v in zip(angles,vals) if v)
    return (volume+logs)/(2*mp.pi)


def packing_action(m):
    rim = [(mp.sin(j*mp.pi/m)/mp.sin(mp.pi/m))**2 for j in range(m)]
    rim[0] = mp.mpf(0)
    south = 1/mp.cos(mp.pi/m)**2
    terms=[]
    for j in range(m):
        x = mp.mpf(0) if j%2 else south
        y = rim[j]
        b,c = (rim[(j-1)%m],rim[(j+1)%m]) if j%2 else (rim[(j+1)%m],rim[(j-1)%m])
        terms.extend((triangle(x,b,y),triangle(x,c,y)))
    phi = mp.fsum(terms)-mp.log(south)-mp.fsum(mp.log(rim[j]) for j in range(1,m))
    return phi,dict(north='0',protected_rim='0',south=mp.nstr(south,60),rim=[mp.nstr(x,60) for x in rim],triangle_actions=[mp.nstr(x,60) for x in terms])


def cases(m):
    base=[('all_minus', ['-2']*m),('all_plus',['2']*m),
          ('north_plus_south_minus',['2' if j%2 else '-2' for j in range(m)]),
          ('north_minus_south_plus',['-2' if j%2 else '2' for j in range(m)])]
    if m == 6:
        base += [('mixed_endpoints_1',['2','2','-2','-2','2','-2']),
                 ('mixed_endpoints_2',['-2','2','2','-2','-2','2']),
                 ('interior',['-1.5','-0.5','0.3333333333333333333333333333333333333333','1.4','-1.333333333333333333333333333333333333333','0.8'])]
    return base


def value_record(value, N, phi):
    return dict(value=mp.nstr(value,80),log_abs_over_N=mp.nstr(mp.log(abs(value))/N,40) if value else None,
                log_abs_over_N_minus_Phi=mp.nstr(mp.log(abs(value))/N-phi,40) if value else None)


def exact_level_three(spectra, sector):
    """Integer polynomial check at N=3, derived from V=C^2+sigma C+(sigma^2-3)I."""
    m=len(spectra);zero=(0,)*m;one={zero:1}
    def add(a,b):
        r=dict(a)
        for k,v in b.items(): r[k]=r.get(k,0)+v
        return {k:v for k,v in r.items() if v}
    def scale(a,v): return {k:x*v for k,x in a.items() if x*v}
    def mul(a,b):
        r=defaultdict(int)
        for x,aa in a.items():
            for y,bb in b.items():
                z=tuple(xi+yi for xi,yi in zip(x,y))
                if all(zi<=2 for zi in z):r[z]+=aa*bb
        return {k:v for k,v in r.items() if v}
    def var(j):
        z=[0]*m;z[j]=1;return {tuple(z):1}
    def rim(j):return var(j%m) if j%m else {}
    total=one
    for j,sigma in enumerate(spectra):
        sig=int(sigma)
        x={} if j%2 else var(0);y=rim(j)
        b,c=(rim(j-1),rim(j+1)) if j%2 else (rim(j+1),rim(j-1))
        outer=add(x,y)
        # Directly from the raw 3x3 matrix square, all coefficients are integers.
        local=scale(mul(b,c),(sig-1)**2)
        local=add(local,scale(mul(outer,add(b,c)),-3*(sig-1)))
        local=add(local,scale(mul(outer,outer),9))
        local=add(local,scale(mul(x,y),-3*(sig+2)))
        if sector=='FULL':local=add(local,scale(add(mul(b,b),mul(c,c)),(sig-1)*(sig+2)))
        total=mul(total,local)
    return total.get((2,)*m,0)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--levels',default='3,4,5,6,7,8,9,10,11,12')
    ap.add_argument('--m',type=int,default=6)
    ap.add_argument('--precision',type=int,default=100)
    ap.add_argument('--all-endpoints',action='store_true')
    ap.add_argument('--cases',default='',help='Comma-separated named cases; empty selects the default list.')
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('md-undecorated-cancellation-bipyramid-diagnostic-results.json'))
    args=ap.parse_args()
    mp.mp.dps=args.precision
    phi,packing=packing_action(args.m)
    rows=[];local_errors=[];brute_checks=[];integer_checks=[]
    selected=cases(args.m)
    if args.all_endpoints:
        known={tuple(s) for _,s in selected}
        selected += [('endpoint_'+''.join('p' if x=='2' else 'm' for x in spec),list(spec))
                     for spec in itertools.product(('-2','2'),repeat=args.m) if spec not in known]
    if args.cases:
        wanted=set(args.cases.split(','))
        selected=[(name,s) for name,s in selected if name in wanted]
    started=time.time()
    for N in map(int,args.levels.split(',')):
        cache={}
        for sigma in ('-2','2','0.375'):
            V=numerator(N,mp.mpf(sigma))
            err,count=matrix_identity_error(N,mp.mpf(sigma),V)
            assert err < mp.power(10,-args.precision+15),(N,sigma,err)
            independent=None
            if N <= 6:
                V2=direct_power_numerator(N,mp.mpf(sigma))
                err2=mp.mpf(0);scale=mp.mpf(1)
                for i in range(N):
                    for j in range(i,N):
                        diff=padd(V[i][j],pscale(V2[i][j],-1))
                        err2=max(err2,*(abs(x) for x in diff))
                        scale=max(scale,*(abs(x) for x in V[i][j]))
                independent=err2/scale
                assert independent < mp.power(10,-args.precision+15)
            local_errors.append(dict(N=N,sigma=sigma,polynomial_coefficients=count,
                                     relative_band_identity_error=mp.nstr(err,12),
                                     direct_matrix_powers_error=mp.nstr(independent,12) if independent is not None else None))
        for name,spectra in selected:
            full,peakf,diagf=contract(N,spectra,'FULL',cache)
            cross,peakc,diagc=contract(N,spectra,'CROSS',cache)
            diff=full-cross
            peak=max(peakf,peakc)
            row=dict(N=N,m=args.m,case=name,spectra=spectra,FULL=value_record(full,N,phi),
                     CROSS=value_record(cross,N,phi),difference=value_record(diff,N,phi),
                     full_trace_diagonal=[mp.nstr(v,50) for v in diagf],
                     cross_trace_diagonal=[mp.nstr(v,50) for v in diagc],
                     max_intermediate_abs=mp.nstr(peak,25),
                     cancellation_digits_from_peak_to_difference=mp.nstr(max(0,mp.log10(peak/abs(diff))),12) if diff else 'exact_numeric_zero')
            if N==3 and all(s in ('-2','2') for s in spectra):
                for sector,value in (('FULL',full),('CROSS',cross)):
                    exact=exact_level_three(spectra,sector)
                    err=abs(value-exact)/max(1,abs(exact))
                    assert err<mp.power(10,-args.precision+20)
                    integer_checks.append(dict(case=name,sector=sector,value=str(exact),relative_error=mp.nstr(err,15)))
            if N <= 4 and name in ('north_plus_south_minus','interior'):
                for sector,actual in (('FULL',full),('CROSS',cross)):
                    brute=brute_coefficient(N,spectra,sector)
                    relative=abs(brute-actual)/max(1,abs(brute),abs(actual))
                    assert relative < mp.power(10,-args.precision+20),(N,name,sector,relative)
                    brute_checks.append(dict(N=N,case=name,sector=sector,relative_error=mp.nstr(relative,15)))
            rows.append(row)
            print(json.dumps(dict(N=N,case=name,FULL=row['FULL']['log_abs_over_N_minus_Phi'],CROSS=row['CROSS']['log_abs_over_N_minus_Phi'],D=row['difference']['log_abs_over_N_minus_Phi'])),flush=True)
        data=dict(status='finite_diagnostic_completed',precision_digits=args.precision,m=args.m,
                  Phi=mp.nstr(phi,80),actual_drilled_volume=mp.nstr(2*mp.pi*phi,80),packing=packing,
                  local_identity_checks=local_errors,independent_multivariate_coefficient_checks=brute_checks,
                  exact_integer_level_three_checks=integer_checks,
                  cases=rows,elapsed_seconds=time.time()-started,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  scope='Signed raw full/CROSS spectral numerator only. No filling applied. No asymptotic estimate or supremum theorem is inferred from finite tuples.',
                  normalizations='Original V=(chi(sigma)-chi(C))/(sigma-C); chi=2T_N(sigma/2)+2. No N-powers divided out. Protected north and z0 zero. All other face targets N-1. One common south variable.',
                  zero_caveat='Very small values must be compared between precisions; no zero is inferred merely from a small floating result.')
        args.output.write_text(json.dumps(data,indent=2)+'\n')


if __name__=='__main__': main()
