#!/usr/bin/env python3
"""Normalization checks for the actual local mixed outer contribution.

Finite values below test the original Laurent integrand at its critical
parameters. They are diagnostics, not a bound for an outer complement.
The universal local theorem uses the written conditional-source proofs.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dps', type=int, default=110)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-local-outer-contribution.json')
    args = ap.parse_args()
    mp.mp.dps = args.dps
    m, k = sp.symbols('m k', integer=True)
    identities = {
        'outer integrand power': m+k-(m+k)/2-k/2-m/2,
        'complete Gaussian power': m/2-m/2,
        'conditional and outer Gaussian constants': m/2+m/2-m,
    }
    for name, value in identities.items():
        assert sp.simplify(value) == 0, name

    def g(z):
        return (mp.polylog(2, mp.exp(-2j*mp.pi*z))-mp.pi**2/6)/(2j*mp.pi)

    def gp(z):
        return mp.log(1-mp.exp(-2j*mp.pi*z))

    def gpp(z):
        return mp.pi*mp.cot(mp.pi*z)-1j*mp.pi

    def gaussian_root(matrix):
        """The accretive Gaussian branch, by symmetric Schur elimination."""
        h = mp.matrix(matrix)
        answer = mp.mpc(1)
        for j in range(h.rows):
            pivot = h[j, j]
            assert pivot.real > 0
            answer *= mp.sqrt(pivot)
            for a in range(j+1, h.rows):
                for b in range(j+1, h.rows):
                    h[a, b] -= h[a, j]*h[j, b]/pivot
        return answer

    levels = (32,33,64,65,128,129,256,257)
    products = {}
    for N in levels:
        r = mp.exp(-2j*mp.pi/N)
        P = [mp.mpc(1)]
        for j in range(1,N):
            P.append(P[-1]*(1-r**j))
        d = [mp.mpc(0)]*N
        d[-1] = mp.mpf(1)/N**2
        for j in range(N-1,0,-1):
            d[j-1] = (1-r**(-j))*d[j]+mp.mpf(1)/N**2
        products[N] = r,P,d

    def kernel(N, eps, X, Y):
        r,P,_ = products[N]
        px=py=xpow=mp.mpc(1)
        terms=[mp.mpc(1)]
        for j in range(1,N):
            px *= 1-r**j*X
            py *= 1-r**j*Y
            xpow /= X
            terms.append(xpow*px*py/P[j]**(2+eps))
        return mp.fsum(terms)

    def weight(N, X):
        result=mp.mpc(0)
        for c in reversed(products[N][2]):
            result=result*X+c
        return result

    diagnostics=[]
    saddle_checks=[]
    for word in ((3,),(4,),(3,4),(3,3,4)):
        eps=[n-3 for n in word]
        size=len(word)
        initial=[]
        for n in word:
            initial.extend([mp.mpc(1)/3 if n==3 else mp.mpc('.3075','-.0552')]*2)

        def gradient(*z):
            s=z[::2];t=z[1::2]
            result=[]
            for v,e in enumerate(eps):
                left=t[(v-1)%size];right=s[(v+1)%size]
                result.extend((
                    gp(s[v]+t[v])+gp(s[v]+left)-(2+e)*gp(s[v])+2j*mp.pi*left,
                    gp(s[v]+t[v])+gp(t[v]+right)-(2+e)*gp(t[v])+2j*mp.pi*right))
            return tuple(result)

        z=list(mp.findroot(gradient,tuple(initial),tol=mp.mpf(10)**(-args.dps+15)))
        s=z[::2];t=z[1::2]
        residual=max(map(abs,gradient(*z)))
        assert residual<mp.mpf(10)**(-args.dps+12)
        F=mp.mpc(0);amp=mp.mpc(1);H=mp.matrix(2*size)
        for v,e in enumerate(eps):
            sv,tv=z[2*v:2*v+2];sn=s[(v+1)%size]
            F += g(sv+tv)+g(tv+sn)-(2+e)*(g(sv)+g(tv))+2j*mp.pi*tv*sn
            L=lambda x:mp.sqrt(2*mp.sin(mp.pi*x))
            amp *= (mp.exp(1j*mp.pi*e*(sv+tv)/2)*L(sv+tv)*L(tv+sn)
                    /(L(sv)*L(tv))**(2+e))
            for idx in (2*v,2*v+1):
                H[idx,idx]+=(2+e)*gpp(z[idx])
            for a,b,shared in ((2*v,2*v+1,False),(2*v+1,2*((v+1)%size),True)):
                term=gpp(z[a]+z[b])
                H[a,a]-=term;H[b,b]-=term
                H[a,b]-=term;H[b,a]-=term
                if shared:
                    H[a,b]-=2j*mp.pi;H[b,a]-=2j*mp.pi
        ids=list(range(0,2*size,2));idt=list(range(1,2*size,2))
        Hss=mp.matrix([[H[a,b] for b in ids] for a in ids])
        Hst=mp.matrix([[H[a,b] for b in idt] for a in ids])
        Htt=mp.matrix([[H[a,b] for b in idt] for a in idt])
        Heff=Htt-Hst.T*Hss**-1*Hst
        root=gaussian_root(H)
        branch_error=abs(gaussian_root(Hss)*gaussian_root(Heff)/root-1)
        assert branch_error<mp.mpf(10)**(-args.dps+12)
        saddle_checks.append({'word':word,'gradient_residual':str(residual),
                              'Gaussian_branch_product_error':str(branch_error)})
        for N in levels:
            X=[mp.exp(-2j*mp.pi*v) for v in t]
            actual=mp.mpc(N)**(size+sum(eps))
            for v,e in enumerate(eps):
                actual *= kernel(N,e,X[(v-1)%size],X[v])
                if e:actual *= weight(N,X[v])
            predicted=(mp.power(N,mp.mpf(size)/2)*mp.power(2*mp.pi,mp.mpf(size)/2)
                       *amp/gaussian_root(Hss)*mp.exp(N*F))
            relative=abs(actual/predicted-1)
            assert N*relative<60,(N,word,relative)
            diagnostics.append({'N':N,'word':word,'relative_error':str(relative),
                                'N_times_relative_error':str(N*relative)})
    paths=[
        'notes/research_mixed_local_outer_contribution.md',
        'notes/research_mixed_conditional_torus_composition.md',
        'notes/research_mixed_contracted_phase.md',
        'notes/research_mixed_cyclic_critical_localization.md',
        'notes/research_mixed_conditional_critical_images.md',
        'notes/research_mixed_fourier_weight_continuation.md',
        'notes/research_mixed_reoptimized_alias_action.md',
        'notes/research_mixed_shifted_conditional_packets.md',
    ]
    record={'status':'passed','decimal_digits':args.dps,
            'exact_power_identity_count':len(identities),
            'exact_power_identities':list(identities),
            'saddle_diagnostics':saddle_checks,
            'finite_density_diagnostic_count':len(diagnostics),
            'finite_density_diagnostics':diagnostics,
            'maximum_N_scaled_error':str(max(mp.mpf(x['N_times_relative_error'])
                                             for x in diagnostics)),
            'scope':'Original finite Laurent density at selected critical points and Gaussian branch/power normalization; no outer-complement bound.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({key:record[key] for key in ('status','exact_power_identity_count',
          'finite_density_diagnostic_count','maximum_N_scaled_error')}))


if __name__=='__main__':
    main()

