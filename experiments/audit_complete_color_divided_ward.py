#!/usr/bin/env python3
"""Sparse dual-number audits of complete-color divided Ward and fusion."""

import itertools
import json
import math
from pathlib import Path

import sympy as sy

from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


class Ring:
    def __init__(self,p):self.p=p
    def add(self,a,b):return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
    def neg(self,a):return ((-a[0])%self.p,(-a[1])%self.p)
    def mul(self,a,b):return (a[0]*b[0]%self.p,(a[0]*b[1]+a[1]*b[0])%self.p)
    def power(self,a,n):
        return (pow(a[0],n,self.p),n*pow(a[0],n-1,self.p)*a[1]%self.p)
    def scale(self,P,c):
        if isinstance(c,int):c=(c%self.p,0)
        out={}
        for col,entries in P.items():
            target={row:self.mul(v,c) for row,v in entries.items()}
            target={row:v for row,v in target.items() if v!=(0,0)}
            if target:out[col]=target
        return out
    def plus(self,P,Q):
        out={col:dict(v) for col,v in P.items()}
        for col,entries in Q.items():
            for row,v in entries.items():
                val=self.add(out.setdefault(col,{}).get(row,(0,0)),v)
                if val!=(0,0):out[col][row]=val
                else:out[col].pop(row,None)
            if not out[col]:out.pop(col)
        return out
    def compose(self,P,Q):
        out={}
        for col,entries in Q.items():
            values={}
            for middle,b in entries.items():
                for row,a in P.get(middle,{}).items():
                    values[row]=self.add(values.get(row,(0,0)),self.mul(a,b))
            values={row:v for row,v in values.items() if v!=(0,0)}
            if values:out[col]=values
        return out
    def identity(self,states):return {state:{state:(1,0)} for state in states}
    def oppower(self,P,n,states):
        out=self.identity(states)
        for _ in range(n):out=self.compose(P,out)
        return out
    def root(self,P):
        return self.scale({c:{r:(v[0],0) for r,v in rows.items()}
                           for c,rows in P.items()},1)
    def normal(self,P,denominator_derivative):
        assert all(v[0]==0 for entries in P.values() for v in entries.values())
        inv=pow(denominator_derivative%self.p,-1,self.p)
        return self.scale({c:{r:(v[1]*inv%self.p,0) for r,v in rows.items()}
                           for c,rows in P.items()},1)
    def apply(self,P,vector):
        out={}
        for col,b in vector.items():
            for row,a in P.get(col,{}).items():
                out[row]=self.add(out.get(row,(0,0)),self.mul(a,b))
        return {r:v for r,v in out.items() if v!=(0,0)}


def complete_coefficients(N,p,q0):
    R=Ring(p);m=N-1;q=(q0,q0);Q=R.power(q,2);x=R.power(q,m)
    kvals=[R.power(q,m-2*a) for a in range(N)]
    f=[R.add((1,0),R.neg(R.power(Q,a+1))) for a in range(m)]
    e=[R.mul(R.power(q,-1),R.add(R.power(x,-1),
                                  R.neg(R.mul(x,R.power(Q,-a))))) for a in range(m)]
    return R,Q,x,kvals,f,e


def tensor_case(N,b):
    p,g,q0=field(N);R,Q,x,k,f,e=complete_coefficients(N,p,q0)
    states=list(itertools.product(range(N),repeat=b));I=R.identity(states)
    atoms=[]
    for i in range(b):
        op={}
        for col in states:
            if col[i]==0:continue
            row=list(col);row[i]-=1;coefficient=e[col[i]-1]
            for j in range(i+1,b):coefficient=R.mul(coefficient,k[col[j]])
            op[col]={tuple(row):coefficient}
        atoms.append(op)
    C={}
    for op in atoms:C=R.plus(C,op)
    power=R.oppower(C,N,states)
    J=R.normal(power,-2*N)
    C0=R.root(C);atoms0=[R.root(op) for op in atoms]
    assert R.oppower(C0,N,states)=={}
    assert J and R.oppower(J,b,states)=={}
    def factorial(op,arg):
        result=I;power=I;den=1
        for r in range(1,N):
            power=R.compose(op,power);den=den*(1-pow(Q[0],r,p))%p
            result=R.plus(result,R.scale(power,pow(arg,r,p)*pow(den,-1,p)%p))
        return result
    def partial_trace(op):
        out={}
        for col,entries in op.items():
            for row,value in entries.items():
                if row[1:]!=col[1:]:continue
                coefficient=value[0]
                for a in col[1:]:coefficient=coefficient*pow(k[a][0],1-N,p)%p
                key=(row[0],col[0]);out[key]=(out.get(key,0)+coefficient)%p
        return {key:v for key,v in out.items() if v}
    for arg in (1,-2):
        product=I
        for atom in atoms0:product=R.compose(factorial(atom,arg),product)
        ghost=I;power=I;coefficient=1
        for r in range(1,(b*(N-1))//N+1):
            power=R.compose(J,power)
            coefficient=coefficient*pow(arg,N,p)*pow(N*r,-1,p)%p
            ghost=R.plus(ghost,R.scale(power,coefficient))
        assert product==R.compose(ghost,factorial(C0,arg))
        defect=R.plus(ghost,R.scale(I,-1))
        assert R.oppower(defect,b,states)=={}
        for col,entries in defect.items():
            for row in entries:
                degree=sum(col)-sum(row)
                assert degree>=N and degree%N==0
        assert partial_trace(defect)=={}
    # Actual checked R commutes with the divided operator, all adjacent positions.
    entries=MixedEntries(N,p,q0);x0=x[0]
    for i in range(b-1):
        for sign in (-1,1):
            braid={}
            for col in states:
                a,bb=col[i:i+2]
                maximum=min(a,N-1-bb) if sign>0 else min(bb,N-1-a)
                values={}
                for transfer in range(maximum+1):
                    row=list(col);row[i]=bb+sign*transfer;row[i+1]=a-sign*transfer
                    coeff=entries.direct(x0,x0,a,bb,transfer,sign)
                    if coeff:values[tuple(row)]=(coeff,0)
                if values:braid[col]=values
            assert R.compose(braid,J)==R.compose(J,braid)
            assert partial_trace(R.compose(J,braid))=={}
    pairing=None
    if b==2:
        Wtot={}
        for col in states:
            values={}
            if col[0]==0:values[(N-1,col[1])]=k[col[1]]
            if col[1]==0:values[(col[0],N-1)]=R.add(values.get((col[0],N-1),(0,0)),(1,0))
            if values:Wtot[col]=values
        test=partial_trace(R.compose(J,Wtot))
        expected=pow(-1,N-1,p)*N*pow(x0,2-N,p)%p
        assert test.get((0,1),0)==expected and expected
        entry=J.get((N-1,1),{}).get((0,0),(0,0))[0]
        assert entry==(-N*q0)%p
        pairing=True
    return {'level':N,'strands':b,'moving_complete_color_normal':True,
            'whole_fusion_exponential_both_argument_signs':True,
            'both_crossing_signs_commute_with_divided_action':True,
            'nilpotence_bound':b,'ordinary_one_cut_closure_zero':True,
            'one_wrap_cut_current_nonzero':pairing}


def adjoint_case(N):
    p,g,q0=field(N);R,Q,x,k,f,e=complete_coefficients(N,p,q0)
    states=list(itertools.product(range(N),repeat=2));AE={};AF={}
    for a,b in states:
        erows={};frows={}
        if a>0:erows[(a-1,b)]=R.mul(e[a-1],R.power(k[b],-1))
        if b<N-1:erows[(a,b+1)]=R.neg(R.mul(e[b],R.power(k[b+1],-1)))
        if a<N-1:frows[(a+1,b)]=f[a]
        if b>0:frows[(a,b-1)]=R.neg(R.mul(R.mul(R.power(k[a],-1),k[b]),f[b-1]))
        if erows:AE[(a,b)]=erows
        if frows:AF[(a,b)]=frows
    JE=R.normal(R.oppower(AE,N,states),-2*N)
    JF=R.normal(R.oppower(AF,N,states),-2*N)
    W={(N-1,0):(1,0)};U={(a,a+1):(1,0) for a in range(N-1)}
    assert R.apply(JE,W)=={key:((-N)%p,0) for key in U}
    assert R.apply(JE,U)=={}
    assert R.apply(JF,U)=={(N-1,0):(N%p,0)}
    assert R.apply(JF,W)=={}
    assert R.compose(JE,JE)=={} and R.compose(JF,JF)=={}
    for a in range(N-1):
        assert R.apply(JF,{(a,a+1):(1,0)})=={
            (N-1,0):((-N*pow(Q[0],-a-1,p))%p,0)}
    pairing=(-N*pow(e[0][0],-1,p))%p
    assert pairing
    delta=pow(-1,N-1,p)
    for a in range(N):
        adapter=R.power(k[a],-N)
        assert adapter==(delta%p,delta*N*(2*a-(N-1))%p)
    return {'level':N,'true_divided_Hopf_adjoint_regular':True,
            'explicit_two_dimensional_SL2_block':True,
            'relative_cut_current_pairing_nonzero':True,
            'ordinary_ADO_pivot_first_normal_adapter':True}


def generic_two_wall_checks():
    q,M=sy.symbols('q M',nonzero=True);Q=q*q;x=-M/q;rho=q-1/q
    records=[]
    for N in range(2,8):
        m=N-1
        e=[sy.cancel((1/x-x*Q**(-a))/q) for a in range(m)]
        f=[1-Q**(a+1) for a in range(m)]
        kvals=[x*Q**(-a) for a in range(N)]
        missing=M*Q**(-N)-1/M
        for a in range(N):
            comm=(e[a]*f[a] if a<m else 0)-(f[a-1]*e[a-1] if a else 0)
            expected=rho*(kvals[a]-1/kvals[a])-(1-Q**N)*missing*int(a==m)
            assert sy.cancel(comm-expected)==0
        assert sy.cancel(missing.subs(M,-q**N))==0
        records.append({'level':N,'exact_auxiliary_boundary_product':True,
                        'missing_edge_zero_on_complete_integral_path':True})
    return records


def main():
    choices=[(N,2) for N in range(2,7)]+[(N,3) for N in range(2,5)]+[(2,4),(3,4)]
    tensors=[tensor_case(N,b) for N,b in choices]
    adjoints=[adjoint_case(N) for N in range(2,9)]
    walls=generic_two_wall_checks()
    result={'tensor_fusion_cases':tensors,'true_Hopf_adjoint_cases':adjoints,
            'generic_two_wall_cases':walls,
            'scope':'Complete integral-color exact divided operators and relative tests only; no global period selection.'}
    path=Path(__file__).with_name('complete_color_divided_ward_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'tensor_fusion_cases':len(tensors),'true_divided_adjoint_cases':len(adjoints),
                      'generic_two_wall_cases':len(walls),'output':str(path)},indent=2))


if __name__=='__main__':main()
