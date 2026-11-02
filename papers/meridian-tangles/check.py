#!/usr/bin/env python3
"""Exact finite checks for the moving-meridian paper.

Independent input: physical E,F,K, their coproduct, the finite universal
crossing sum, and entrywise evaluation/coevaluation currying. Outputs are
compared with canonical polynomial, six-turn and covariant-tree formulas.
No floating point, eigenvalue fitting, or asymptotic claim is involved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

if not __debug__:
    raise SystemExit("Run without -O: assertion checks must be enabled")

import numpy as np


def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = 3
    while r*r <= n:
        if n % r == 0:
            return False
        r += 2
    return True


def factors(n):
    out = []
    k = 2
    while k*k <= n:
        if n % k == 0:
            out.append(k)
            while n % k == 0:
                n //= k
        k += 1
    if n > 1:
        out.append(n)
    return out


def field(order, skip):
    k = 1
    while True:
        p = k*order+1
        if isprime(p):
            if skip:
                skip -= 1
            else:
                break
        k += 1
    for z in range(2, p):
        t = pow(z, (p-1)//order, p)
        if all(pow(t, order//r, p) != 1 for r in factors(order)):
            return p, t
    raise AssertionError("No primitive root found")


class Model:
    def __init__(self, N, a, b, field_index=0):
        self.N, self.d, self.a, self.b = N, N-1, a, b
        self.p, self.t = field(4*b*b*N, field_index)
        p, d = self.p, self.d
        assert N*N*(p-1)**2 < np.iinfo(np.int64).max//4
        self.q, self.Q = self.tp(2*b*b), self.tp(4*b*b)
        self.rho = (self.q-self.inv(self.q)) % p
        self.I = np.eye(N*N, dtype=np.int64)
        self.s0 = ((-1)**d*N*N) % p
        self.mods = {sign: self.module(sign) for sign in (1, -1)}
        self.om = {}
        self.pol = {}
        self.eb = {}
        self.cross = {}
        for signs in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            self.om[signs] = self.omega(signs)
            shift = signs[0] if signs[0] == signs[1] else 0
            nodes = [self.node(j, shift) for j in range(N)]
            P = [1]
            for z in nodes:
                P = self.pmul(P, [-z % p, 1])
            self.pol[signs] = P
            assert not np.any(self.evalmat(P, self.om[signs]))
            self.cross[signs] = self.braid(signs)
        self.e = [[1]]
        scale = 1
        for k in range(1, N):
            scale = scale * (-(self.qpow(k)-self.qpow(-k))**2) % p
            num = [1]
            for j in range(k):
                num = self.pmul(num, [self.node(j, 0), -1 % p])
            self.e.append([z*self.inv(scale) % p for z in num])
        for signs in self.om:
            self.eb[signs] = [self.evalmat(f, self.om[signs]) for f in self.e]
        kap = self.tp(b*b*d*d)
        self.r0 = [0]*N
        for k, f in enumerate(self.e):
            c = kap*pow(-self.q % p, k, p) % p
            for j, z in enumerate(f):
                self.r0[j] = (self.r0[j]+c*z) % p
        self.G = {(1, -1): self.I,
                  (-1, 1): self.mm(self.cross[(1, -1)],
                                      self.minv(self.evalmat(self.r0, self.om[(1, -1)])))}
        self.H = 1
        self.W = [1]
        for k in range(1, N):
            base = (self.qpow(k)-self.qpow(-k)) % p
            minus = (self.qfrac(b*k-a)-self.qfrac(-b*k+a)) % p
            plus = (self.qfrac(b*k+a)-self.qfrac(-b*k-a)) % p
            self.H = self.H*minus*self.inv(base) % p
            self.W.append(self.W[-1]*minus*plus*self.inv(base*base % p) % p)
        assert self.H and all(self.W)

    def tp(self, k):
        return pow(self.t, int(k), self.p)

    def qpow(self, k):
        return self.tp(2*self.b*self.b*k)

    def qfrac(self, numerator):
        return self.tp(2*self.b*numerator)

    def inv(self, z):
        z = int(z) % self.p
        assert z
        return pow(z, self.p-2, self.p)

    def mm(self, A, B):
        return (A @ B) % self.p

    def minv(self, A):
        n, p = len(A), self.p
        B = np.concatenate([A.copy() % p, np.eye(n, dtype=np.int64)], axis=1)
        for k in range(n):
            r = next(j for j in range(k, n) if B[j, k])
            B[[r, k]] = B[[k, r]]
            B[k] = B[k]*self.inv(B[k, k]) % p
            for j in range(n):
                if j != k:
                    B[j] = (B[j]-int(B[j, k])*B[k]) % p
        return B[:, n:]

    def mpow(self, A, n):
        if n < 0:
            return self.mpow(self.minv(A), -n)
        B = np.eye(len(A), dtype=np.int64)
        while n:
            if n % 2:
                B = self.mm(B, A)
            A = self.mm(A, A)
            n //= 2
        return B

    def pmul(self, f, g):
        h = [0]*(len(f)+len(g)-1)
        for i, x in enumerate(f):
            for j, y in enumerate(g):
                h[i+j] = (h[i+j]+int(x)*int(y)) % self.p
        return h

    def rem(self, f, P):
        f = [int(x) % self.p for x in f]
        while len(f) >= len(P):
            c = f[-1]
            shift = len(f)-len(P)
            for j, x in enumerate(P):
                f[j+shift] = (f[j+shift]-c*x) % self.p
            f.pop()
        return f+[0]*(self.N-len(f))

    def phi(self, f, signs):
        return self.s0*self.rem(f, self.pol[signs])[-1] % self.p

    def evalmat(self, f, A):
        I = np.eye(len(A), dtype=np.int64)
        B = I*0
        for x in reversed(f):
            B = (self.mm(B, A)+int(x)*I) % self.p
        return B

    def evalscalar(self, f, z):
        out = 0
        for x in reversed(f):
            out = (out*z+int(x)) % self.p
        return out

    def node(self, j, sign):
        num = self.b*(2*j+1)-2*sign*self.a
        return (self.qfrac(num)+self.qfrac(-num)) % self.p

    def module(self, sign):
        N, p, b, a = self.N, self.p, self.b, self.a
        alpha = b*self.d+sign*a
        K = [self.qfrac(alpha-2*b*j) for j in range(N)]
        eps = [0]
        E, F = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        for j in range(1, N):
            v = (self.qpow(j)-self.qpow(-j))*self.inv(self.rho) % p
            w = (self.qfrac(b*j-sign*a)-self.qfrac(-b*j+sign*a))*self.inv(self.rho) % p
            eps.append(v*w % p)
            E[j-1, j] = eps[j]
            F[j, j-1] = 1
        g = [pow(z, 1-N, p) for z in K]
        return alpha, np.diag(K), E, F, eps, g

    def omega(self, signs):
        _, K, E, F, _, _ = self.mods[signs[0]]
        _, L, A, B, _, _ = self.mods[signs[1]]
        I = np.eye(self.N, dtype=np.int64)
        Et = (np.kron(E, L)+np.kron(I, A)) % self.p
        Ft = (np.kron(F, I)+np.kron(self.minv(K), B)) % self.p
        Kt = np.kron(K, L) % self.p
        return (self.rho**2 % self.p*self.mm(Ft, Et)+self.q*Kt
                +self.inv(self.q)*self.minv(Kt)) % self.p

    def braid(self, signs):
        N, p, b = self.N, self.p, self.b
        alpha, _, _, _, eps, _ = self.mods[signs[0]]
        beta = self.mods[signs[1]][0]
        R = np.zeros((N*N, N*N), dtype=np.int64)
        for i in range(N):
            for j in range(N):
                ecoef, fact = 1, 1
                for k in range(min(i, N-1-j)+1):
                    if k:
                        ecoef = ecoef*eps[i-k+1] % p
                        fact = fact*(self.qpow(k)-self.qpow(-k))*self.inv(self.rho) % p
                    v = self.tp(b*b*k*(k-1))*pow(self.rho, k, p)*ecoef*self.inv(fact) % p
                    v = v*self.tp((alpha-2*b*(i-k))*(beta-2*b*(j+k))) % p
                    R[(j+k)*N+i-k, i*N+j] = v
        return R

    def ordinary(self, length):
        p, b = self.p, self.b
        alpha = b*(length-1)
        K = [self.qfrac(alpha-2*b*j) for j in range(length)]
        E, F = np.zeros((length,length),dtype=np.int64), np.zeros((length,length),dtype=np.int64)
        eps = [0]
        for j in range(1,length):
            v = (self.qpow(j)-self.qpow(-j))*self.inv(self.rho) % p
            w = (self.qpow(length-j)-self.qpow(-length+j))*self.inv(self.rho) % p
            eps.append(v*w % p)
            E[j-1,j], F[j,j-1] = eps[j], 1
        return alpha,np.diag(K),E,F,eps,[pow(z,1-self.N,p) for z in K]

    def braid_data(self, first, second):
        alpha, _, _, _, eps, _ = first
        beta = second[0]
        n, m, p, b = len(first[1]), len(second[1]), self.p, self.b
        R = np.zeros((n*m,n*m),dtype=np.int64)
        for i in range(n):
            for j in range(m):
                ecoef,fact = 1,1
                for k in range(min(i,m-1-j)+1):
                    if k:
                        ecoef = ecoef*eps[i-k+1] % p
                        fact = fact*(self.qpow(k)-self.qpow(-k))*self.inv(self.rho) % p
                    v = self.tp(b*b*k*(k-1))*pow(self.rho,k,p)*ecoef*self.inv(fact) % p
                    v = v*self.tp((alpha-2*b*(i-k))*(beta-2*b*(j+k))) % p
                    R[(j+k)*n+i-k,i*m+j] = v
        return R

    def circles(self):
        count = 0
        for signs in ((1,1),(1,-1),(-1,1),(-1,-1)):
            # Chebyshev polynomials are generated separately from the braid word.
            Lprev, L = [1], [0,-1 % self.p]
            for j in range(1,self.N+1):
                if j == 1:
                    poly = Lprev
                elif j == 2:
                    poly = L
                else:
                    nxt = [0]+[-x % self.p for x in L]
                    for k,x in enumerate(Lprev):
                        nxt[k] = (nxt[k]-x) % self.p
                    Lprev,L = L,nxt
                    poly = L
                modules = [self.mods[signs[0]],self.mods[signs[1]],self.ordinary(j)]
                total = self.N*self.N*j
                assert total*(self.p-1)**2 < np.iinfo(np.int64).max//4
                word = np.eye(total,dtype=np.int64)
                for position in (1,0,0,1):
                    op = self.braid_data(modules[position],modules[position+1])
                    if position == 0:
                        op = np.kron(op,np.eye(len(modules[2][1]),dtype=np.int64))
                    else:
                        op = np.kron(np.eye(len(modules[0][1]),dtype=np.int64),op)
                    word = self.mm(op,word)
                    modules[position],modules[position+1] = modules[position+1],modules[position]
                reduced = np.zeros_like(self.I)
                for a in range(self.N*self.N):
                    for b in range(self.N*self.N):
                        reduced[a,b] = sum(int(word[a*j+k,b*j+k])*modules[2][-1][k] for k in range(j)) % self.p
                assert np.array_equal(reduced,self.evalmat(poly,self.om[signs])), ('circle',self.N,self.a,self.b,signs,j)
                count += 1
        return count

    def gamma(self, j, sign):
        x = self.qfrac(self.b*self.d+sign*self.a)
        return pow(-x % self.p, j, self.p)*pow(self.Q, j*(j+1)//2, self.p) % self.p

    def carrier(self, target, source):
        if target == source:
            return self.I
        return self.mm(self.G[target], self.minv(self.G[source]))

    def turn(self, A, source, target):
        N, d, p = self.N, self.d, self.p
        B = np.zeros_like(A)
        for a in range(N):
            for k in range(N):
                for j in range(N):
                    for b in range(N):
                        B[j*N+b, a*N+k] = (self.gamma(a, target[0])
                            *self.inv(self.gamma(b, source[1]))
                            *int(A[(d-a)*N+j, k*N+d-b])) % p
        return B, (-target[0], source[0]), (target[1], -source[1])

    def ptr(self, A, second_sign):
        N, p = self.N, self.p
        g = self.mods[second_sign][-1]
        B = np.zeros((N, N), dtype=np.int64)
        for i in range(N):
            for j in range(N):
                B[i, j] = sum(g[k]*int(A[i*N+k, j*N+k]) for k in range(N)) % p
        return B

    def scalar(self, A):
        c = int(A[0, 0])
        assert np.array_equal(A, c*np.eye(len(A), dtype=np.int64))
        return c

    def extract(self, A, signs):
        out = [0]*self.N
        for k in range(self.N):
            v = self.scalar(self.ptr(self.mm(A, self.eb[signs][self.d-k]), signs[1]))
            c = v*self.inv(self.H) % self.p
            for j, z in enumerate(self.e[k]):
                out[j] = (out[j]+c*z) % self.p
        assert np.array_equal(self.evalmat(out, self.om[signs]), A)
        return out

    def check(self):
        N, d, p = self.N, self.d, self.p
        counts = dict(moments=0, pairings=0, turns=0, crossing_values=0,
                      crossing_normals=0, negative_powers=0, mixed_words=0, curls=0, trees=0)
        for signs, Om in self.om.items():
            A = self.I.copy()
            for m in range(N):
                v = self.scalar(self.ptr(A, signs[1]))
                assert v == (self.s0*self.H % p if m == d else 0)
                # The left closure uses g^{-1} on the first factor.
                gl = [self.inv(z) for z in self.mods[signs[0]][-1]]
                left = np.zeros((N,N), dtype=np.int64)
                for i in range(N):
                    for j in range(N):
                        left[i,j] = sum(gl[k]*int(A[k*N+i,k*N+j]) for k in range(N)) % p
                assert self.scalar(left) == v
                counts['moments'] += 1
                A = self.mm(A, Om)
            for i in range(N):
                for j in range(N):
                    assert self.phi(self.pmul(self.e[i], self.e[j]), signs) == int(i+j == d)
                    counts['pairings'] += 1
        types = [((1,1),(1,1),-1), ((-1,1),(1,-1),1),
                 ((-1,-1),(-1,-1),1), ((1,-1),(-1,1),-1),
                 ((1,-1),(1,-1),0), ((-1,1),(-1,1),0)]
        for source, target, exponent in types:
            for k in range(N):
                A = self.mm(self.carrier(target, source), self.eb[source][k])
                B, src, dst = self.turn(A, source, target)
                scalar = self.tp(exponent*self.a*self.a)*self.W[k]*self.inv(self.H) % p
                C = scalar*self.mm(self.carrier(dst, src), self.eb[src][d-k]) % p
                assert np.array_equal(B, C), ('turn', self.N,self.a,self.b,source,target,k)
                counts['turns'] += 1
        for signs in ((1,1),(-1,-1)):
            sign = signs[0]
            R = self.cross[signs]
            alpha = self.b*d+sign*self.a
            nodes = [self.node(j, sign) for j in range(N)]
            for n in (-3,-1,1,2):
                f = self.extract(self.mpow(R,n), signs)
                df = [i*f[i] % p for i in range(1,N)]
                for j,z in enumerate(nodes):
                    v = self.tp(alpha*alpha)*pow(-1,j,p)*self.qfrac(self.b*j*(j+1)-2*sign*self.a*j) % p
                    assert self.evalscalar(f,z) == pow(v,n,p)
                    counts['crossing_values'] += 1
                    for l in range(j+1,N):
                        if nodes[l] == z:
                            u = self.qfrac(self.b*(2*j+1)-2*sign*self.a)
                            coeff = (-n*(l-j)*self.inv(2*(u-self.inv(u)) % p)) % p
                            assert self.evalscalar(df,z) == coeff*pow(v,n,p) % p
                            counts['crossing_normals'] += 1
                if n < 0:
                    counts['negative_powers'] += 1
        for signs in ((1,1),(-1,-1)):
            twist = self.tp(self.a*self.a-self.b*self.b*d*d)
            for n in (-1,1):
                assert self.scalar(self.ptr(self.mpow(self.cross[signs],n),signs[1])) == pow(twist,n,p)
                counts['curls'] += 1
        for start in ((1,-1),(-1,1)):
            for n in (-3,-2,-1,0,1,2,3):
                current, physical = start, self.I.copy()
                for _ in range(abs(n)):
                    op = self.cross[current] if n > 0 else self.minv(self.cross[current[::-1]])
                    physical = self.mm(op,physical)
                    current = current[::-1]
                rounding = n//2 if start == (1,-1) else -((-n)//2)
                scalar = self.tp(-2*rounding*self.a*self.a)
                wanted = scalar*self.mm(self.carrier(current,start),
                    self.mpow(self.evalmat(self.r0,self.om[start]),n)) % p
                assert np.array_equal(physical,wanted), ('mixed-word',N,self.a,self.b,start,n)
                counts['mixed_words'] += 1
        # One actual ordered three-vertex example; source branches have
        # different equal-color quotients, while the root is opposite.
        k1, k2 = d, max(0,d-1)
        f1, f2, f0 = self.e[k1], self.e[k2], self.pmul(self.e[1],self.r0)
        A1, _, _ = self.turn(self.evalmat(f1,self.om[(1,1)]),(1,1),(1,1))
        A2, _, _ = self.turn(self.evalmat(f2,self.om[(-1,-1)]),(-1,-1),(-1,-1))
        physical = self.scalar(self.ptr(self.mm(self.evalmat(f0,self.om[(1,-1)]),self.mm(A1,A2)),-1))
        tensor = 0
        for k in range(N):
            for l in range(N):
                root = self.phi(self.pmul(f0,self.pmul(self.e[k],self.e[l])),(1,-1))
                first = self.phi(self.pmul(f1,self.e[k]),(1,1))
                second = self.phi(self.pmul(f2,self.e[l]),(-1,-1))
                tensor += root*first*second*self.H*self.inv(self.W[k])*self.H*self.inv(self.W[l])
        tensor = tensor*self.H % p
        assert physical == tensor, ('tree',N,self.a,self.b,physical,tensor)
        counts['trees'] += 1
        return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).parent/'build'/'checks')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    summary = args.output/'summary.json'
    summary.unlink(missing_ok=True)
    own = Path(__file__).resolve()
    sources = [own, own.parent/'main.tex', own.parent/'figures'/'typed-tree.tex']
    hashes = {str(p.relative_to(own.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    cases, totals = [], {}
    for N in (2,3,4,5,6):
        for a,b in ((0,1),(1,2),(-1,2),(1,3),(-1,3)):
            for prime_index in (0,1):
                model = Model(N,a,b,prime_index)
                counts = model.check()
                if N <= 4 and (a,b) in ((0,1),(1,3)) and prime_index == 0:
                    counts['ordinary_circles'] = model.circles()
                cases.append(dict(N=N,s=[a,b],prime=model.p,root=model.t,checks=counts))
                for k,v in counts.items():
                    totals[k] = totals.get(k,0)+v
    assert hashes == {str(p.relative_to(own.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result = dict(scope='Exact finite physical-matrix and polynomial comparisons only; no all-level or analytic proof from samples.',
                  source_sha256=hashes, cases=cases, totals=totals)
    summary.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=str(summary),totals=totals),sort_keys=True))


if __name__ == '__main__':
    main()
