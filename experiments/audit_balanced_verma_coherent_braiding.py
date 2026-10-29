#!/usr/bin/env python3
"""Exact root checks of the balanced Verma resonance and coherent braiding.

The full crossing uses polynomial Gaussian coefficients, independently
of the proposed resonant exponential. Tests include nonzero central
characters, coherent kernels, changing source parameters, and inverses.
"""

import json
import math
from pathlib import Path

from audit_divided_ward_factorial_fusion import field
from audit_figure_eight_whole_source import MixedEntries


def add(out, state, value, p):
    value = (out.get(state, 0) + value) % p
    if value:
        out[state] = value
    else:
        out.pop(state, None)


class Model:
    def __init__(self, n, m1=2, m2=3):
        self.n = n
        self.p, self.q = field(n)
        self.Q = self.q**2 % self.p
        self.m1, self.m2 = m1, m2
        self.x1 = -m1 * pow(self.q, -1, self.p) % self.p
        self.x2 = -m2 * pow(self.q, -1, self.p) % self.p
        self.gamma = pow(-1, n + 1, self.p)
        self.kappa1 = (pow(m1, n, self.p)-pow(m1, -n, self.p)) % self.p
        self.central = self.gamma * self.kappa1 % self.p
        self.fac = [1]
        for j in range(1, n):
            self.fac.append(self.fac[-1]*(1-pow(self.Q,j,self.p)) % self.p)
        self.gauss = [[1]]
        for a in range(1, 8*n+4):
            prev = self.gauss[-1]
            row = [1]
            for k in range(1,a):
                row.append((prev[k]+pow(self.Q,a-k,self.p)*prev[k-1]) % self.p)
            row.append(1)
            self.gauss.append(row)

    def ecoef(self, a):
        return (self.m1*pow(self.Q,-a,self.p)-pow(self.m1,-1,self.p)) % self.p

    def eproduct(self, a, k):
        out = 1
        for j in range(a-k+1,a+1):
            out = out*self.ecoef(j) % self.p
        return out

    def cartan(self,a,b):
        return pow(self.x2,-a,self.p)*pow(self.x1,-b,self.p)*pow(self.Q,a*b,self.p) % self.p

    def full(self,a,b,short=False,cartan=False):
        out = {}
        stop = min(a,self.n-1) if short else a
        for k in range(stop+1):
            value = pow(-1,k,self.p)*pow(self.q,k*k,self.p)
            value = value*self.eproduct(a,k)*self.gauss[b+k][k] % self.p
            state = (a-k,b+k)
            if cartan:
                value = value*self.cartan(*state) % self.p
            add(out,state,value,self.p)
        return out

    def ghost(self,vector):
        out = {}
        for (a,b),value in vector.items():
            for r in range(a//self.n+1):
                coefficient = math.comb(b//self.n+r,r)*pow(self.central,r,self.p)
                add(out,(a-r*self.n,b+r*self.n),value*coefficient,self.p)
        return out

    def finite(self,a,b,s1,inverse=False,wrap=None):
        """Uncheck finite nilpotent part; E may have a genuine cyclic wrap."""
        out = {}
        evalue, fvalue, rowa = 1,1,a
        for k in range(self.n):
            if b+k >= self.n:
                break
            if k:
                cyclic = self.ecoef(0)*s1 if wrap is None else wrap
                evalue = evalue*(self.ecoef(rowa) if rowa else cyclic) % self.p
                rowa = (rowa-1) % self.n
                fvalue = fvalue*(1-pow(self.Q,b+k,self.p)) % self.p
            phase = pow(self.q,k,self.p) if inverse else pow(-1,k,self.p)*pow(self.q,k*k,self.p)
            value = phase*evalue*fvalue*pow(self.fac[k],-1,self.p) % self.p
            add(out,(rowa,b+k),value,self.p)
        return out

    def coherent_case(self,a,b,degree,s1,s2):
        left = {}
        for r in range(degree+1):
            ss = degree-r
            value = pow(s1,r,self.p)*pow(s2,ss,self.p) % self.p
            for state,c in self.full(a+r*self.n,b+ss*self.n,cartan=True).items():
                add(left,state,value*c,self.p)
        t1 = pow(self.x2,-self.n,self.p)*s1 % self.p
        t2 = pow(self.x1,-self.n,self.p)*(s2+self.central*s1) % self.p
        right = {}
        for (aa,bb),c in self.finite(a,b,s1).items():
            carry = (aa+bb-a-b)//self.n
            assert carry in (0,1)
            c = c*self.cartan(aa,bb) % self.p
            if degree < carry:
                continue
            for r in range(degree-carry+1):
                ss = degree-carry-r
                value = c*pow(t1,r,self.p)*pow(t2,ss,self.p) % self.p
                add(right,(aa+r*self.n,bb+ss*self.n),value,self.p)
        assert left == right, (self.n,a,b,degree,left,right)

    def braid(self,vector,params,pos,inverse=False,mu_chart=False):
        assert self.m1 == self.m2
        chi = pow(self.x1,self.n,self.p)
        s1,s2 = params[pos:pos+2]
        if inverse:
            target = (chi*s2 % self.p, chi*(s1-self.central*s2) % self.p)
        else:
            target = ((s2+self.central*s1)*pow(chi,-1,self.p) % self.p,
                      s1*pow(chi,-1,self.p) % self.p)
        newparams = list(params)
        newparams[pos:pos+2] = target
        out = {}
        for state,value in vector.items():
            a,b = state[pos:pos+2]
            if inverse:
                diag = pow(self.cartan(b,a),-1,self.p)
                local = self.finite(b,a,target[0],inverse=True,
                                    wrap=target[0] if mu_chart else None)
                for (aa,bb),c in local.items():
                    row = state[:pos]+(aa,bb)+state[pos+2:]
                    add(out,row,value*diag*c,self.p)
            else:
                for (aa,bb),c in self.finite(a,b,s1,wrap=s1 if mu_chart else None).items():
                    row = state[:pos]+(bb,aa)+state[pos+2:]
                    add(out,row,value*c*self.cartan(aa,bb),self.p)
        return out,tuple(newparams)

    def cut(self,word,strands,mu):
        import itertools
        chi=pow(self.x1,self.n,self.p)
        params=tuple(mu*pow(chi,-j,self.p)%self.p for j in range(strands))
        out={}
        for initial in itertools.product(range(self.n),repeat=strands):
            vector,current={initial:1},params
            for pos,inverse in word:
                vector,current=self.braid(vector,current,pos,inverse=inverse,mu_chart=True)
            assert current==params
            pivot=1
            for a in initial[1:]:
                pivot=pivot*pow(self.x1*pow(self.Q,-a,self.p)%self.p,1-self.n,self.p)%self.p
            for state,value in vector.items():
                if state[1:]==initial[1:]:
                    add(out,(state[0],initial[0]),value*pivot,self.p)
        return out


def main():
    records = []
    for n in range(2,9):
        model = Model(n)
        assert model.central
        basis = 0
        for total in range(3*n+2):
            for a in range(total+1):
                b = total-a
                assert model.full(a,b) == model.ghost(model.full(a,b,short=True))
                basis += 1
        coherent = 0
        for a in range(n):
            for b in range(n):
                for degree in range(4):
                    model.coherent_case(a,b,degree,5,7)
                    coherent += 1
        equal = Model(n,m1=2,m2=2)
        literal=MixedEntries(n,equal.p,equal.q)
        literal_checks=0
        for a in range(n):
            for b in range(n):
                for sign in (1,-1):
                    actual,_=equal.braid({(a,b):1},(0,0),0,inverse=sign<0)
                    expected={}
                    stop=min(a,n-1-b) if sign>0 else min(b,n-1-a)
                    for k in range(stop+1):
                        value=literal.direct(equal.x1,equal.x2,a,b,k,sign)
                        add(expected,(b+sign*k,a-sign*k),value,equal.p)
                    assert actual==expected
                    literal_checks+=1
        inverse_checks = 0
        for a in range(n):
            for b in range(n):
                initial = {(a,b):1}
                vector,params = equal.braid(initial,(5,7),0)
                vector,params = equal.braid(vector,params,0,inverse=True)
                assert vector == initial and params == (5,7)
                inverse_checks += 1
        braid_checks = 0
        if n <= 5:
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        initial={(a,b,c):1}
                        outcomes=[]
                        for word in ((0,1,0),(1,0,1)):
                            vector,params=initial,(5,7,11)
                            for pos in word:
                                vector,params=equal.braid(vector,params,pos)
                            outcomes.append((vector,params))
                        assert outcomes[0] == outcomes[1]
                        braid_checks += 1
        cut_checks=0
        if n<=6:
            for cutmodel in (equal,Model(n,m1=1,m2=1)):
                for strands,word in ((2,((0,False),)*3),
                                     (3,((0,False),(1,True),(0,False),(1,True)))):
                    assert cutmodel.cut(word,strands,5)==cutmodel.cut(word,strands,0)
                    cut_checks+=1
        records.append({'level':n,'full_shell_basis_checks':basis,
                        'coherent_kernel_checks':coherent,
                        'changing_center_inverse_checks':inverse_checks,
                        'three_strand_braid_basis_checks':braid_checks,
                        'literal_original_crossing_checks':literal_checks,
                        'full_cut_source_and_boundary_chart_checks':cut_checks})
    result={'cases':records,'scope':'Exact balanced-Verma/Fock/source identities; no geometric-source or volume theorem.'}
    path=Path(__file__).with_name('balanced_verma_coherent_braiding_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'levels':len(records),'shell_basis':sum(r['full_shell_basis_checks'] for r in records),
                      'coherent_kernels':sum(r['coherent_kernel_checks'] for r in records),
                      'braid_basis':sum(r['three_strand_braid_basis_checks'] for r in records),
                      'output':str(path)},indent=2))


if __name__ == '__main__':
    main()
