#!/usr/bin/env python3
"""Original generic physical Casimir, forward/backward jets and divided pairs.

Four coefficients are computed exactly over cyclotomic finite fields.
The uniform analytic estimates are proved in the note; finite checks
audit the source and derivative conventions, including second pair jets.
"""
import json
import math
from pathlib import Path

from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_partner_normal_collision import original_column as old_normal


class Jet:
    p=0
    order=4

    def __init__(self,value=0):
        if isinstance(value,Jet):self.c=value.c[:]
        elif isinstance(value,(list,tuple)):self.c=[int(x)%self.p for x in value]+[0]*(self.order-len(value))
        else:self.c=[int(value)%self.p]+[0]*(self.order-1)

    def __add__(self,other):
        other=Jet(other);return Jet([(a+b)%self.p for a,b in zip(self.c,other.c)])
    __radd__=__add__
    def __neg__(self):return Jet([-a for a in self.c])
    def __sub__(self,other):return self+-Jet(other)
    def __rsub__(self,other):return Jet(other)+-self
    def __mul__(self,other):
        other=Jet(other)
        return Jet([sum(self.c[j]*other.c[k-j] for j in range(k+1))%self.p for k in range(self.order)])
    __rmul__=__mul__
    def inv(self):
        assert self.c[0]
        inv0=pow(self.c[0],-1,self.p);out=[inv0]
        for k in range(1,self.order):out.append(-sum(self.c[j]*out[k-j] for j in range(1,k+1))*inv0%self.p)
        return Jet(out)
    def __truediv__(self,other):return self*Jet(other).inv()
    def __rtruediv__(self,other):return Jet(other)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        out=Jet(1);base=self
        while n:
            if n%2:out=out*base
            base=base*base;n//=2
        return out
    def __eq__(self,other):return self.c==Jet(other).c


def original(N,q,t,m,u,F):
    Q=q*q;d=N-1;v=t-u
    def gauss(n,k):return F[n]/F[k]/F[n-k]
    return sum((-1)**a*q**(d*(u-2*a))*Q**(a*v+a*(a-1)//2)
               *F[N-m+a-1]*F[N-a-1]/F[N-m-1]/F[N-1]
               *gauss(u,a)*gauss(v,m-a)/gauss(t,m)
               for a in range(max(0,m-v),min(m,u)+1))


def matrix(N,q,t):
    Q=q*q;d=N-1;diag=[];up=[];low=[]
    for r in range(t+1):
        diag.append(q**-1*Q**(r-t)*(1-Q**(N-r))*(1-Q**r)
                    +q**(-2*d-1)*Q**r*(1-Q**(N-t+r))*(1-Q**(t-r))
                    +q**(2*d+1)*Q**(-t)+q**(-2*d-1)*Q**t)
        if r<t:
            up.append(q**(-N)*Q**(2*r+1-t)*(1-Q**(N-r-1))*(1-Q**(t-r)))
            low.append(q**(-N)*(1-Q**(N-t+r))*(1-Q**(r+1)))
    return diag,up,low


def forward(diag,up,low,lam):
    out=[Jet(1)]
    for r in range(len(up)):
        value=(lam-diag[r])*out[r]
        if r:value-=low[r-1]*out[r-1]
        out.append(value/up[r])
    return out


def divide_simple_zero(num,den):
    assert num.c[0]==0 and den.c[0]==0 and den.c[1]!=0
    out=[];inv=pow(den.c[1],-1,Jet.p)
    for k in range(Jet.order-1):
        out.append((num.c[k+1]-sum(den.c[j+1]*out[k-j] for j in range(1,k+1)))*inv%Jet.p)
    return out


def exact_checks():
    counts=dict(original_physical_column_jets=0,retained_column_coefficients=0,
                original_generic_eigenvector_equations=0,forward_backward_column_jets=0,
                generic_endpoint_jets=0,root_reversal_entries=0,
                genuine_divided_pair_jets=0,retained_pair_coefficients=0,
                prior_actual_normal_comparisons=0,nonzero_second_pair_jets=0)
    for N in range(3,11):
        p,eta=root_field(N);q0=eta*eta%p;Jet.p=p
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        qi=Jet([pow(q0,-1,p)*pow(-1,k,p)*pow(math.factorial(k),-1,p)%p for k in range(4)])
        Q=q*q;F=[Jet(1)]
        for r in range(1,N):F.append(F[-1]*(1-Q**r))
        for t in range(N):
            diag,up,low=matrix(N,q,t)
            diag_i,up_i,low_i=matrix(N,qi,t)
            for r in range(t+1):
                assert diag[r].c[0]==diag_i[t-r].c[0]
                counts['root_reversal_entries']+=1
                if r<t:
                    assert up[r].c[0]==low[r].c[0]
                    assert up[r].c[0]==up_i[t-r-1].c[0]
                    counts['root_reversal_entries']+=2
            columns={}
            for m in range(t+1):
                lam=q**(2*N-2*m-1)+q**(-2*N+2*m+1)
                actual=[original(N,q,t,m,u,F) for u in range(t+1)]
                front=forward(diag,up,low,lam)
                endpoint=(-1)**m*q**((N-1)*t-2*N*m+m*m+m)
                back=[endpoint*z for z in reversed(forward(list(reversed(diag)),list(reversed(low)),list(reversed(up)),lam))]
                assert actual[0]==1 and actual[-1]==endpoint
                counts['generic_endpoint_jets']+=2
                for u in range(t+1):
                    assert actual[u]==front[u]==back[u]
                    image=diag[u]*actual[u]
                    if u:image+=low[u-1]*actual[u-1]
                    if u<t:image+=up[u]*actual[u+1]
                    assert image==lam*actual[u]
                    counts['original_physical_column_jets']+=1
                    counts['retained_column_coefficients']+=4
                    counts['original_generic_eigenvector_equations']+=1
                    counts['forward_backward_column_jets']+=2
                columns[m]=(actual,front,lam)
            for j in range((N-1)//2+1):
                l=N-1-j
                if not(j<l<=t):continue
                s=l-j;gap=columns[j][2]-columns[l][2]
                assert gap==(q**s-q**(-s))*(q**N-q**(-N))
                Delta=(pow(q0,2*j+1,p)-pow(q0,-2*j-1,p))%p
                assert gap.c[1]==-2*N*Delta%p
                for u in range(t+1):
                    a=columns[j][0][u];b=columns[l][0][u]
                    assert a.c[0]==b.c[0]
                    pair=divide_simple_zero(a-b,gap)
                    recurrence_pair=divide_simple_zero(columns[j][1][u]-columns[l][1][u],gap)
                    assert pair==recurrence_pair
                    vj,dj=old_normal(N,t,j,u,p,q0);vl,dl=old_normal(N,t,l,u,p,q0)
                    assert vj==a.c[0] and vl==b.c[0]
                    assert dj==a.c[1] and dl==b.c[1]
                    assert pair[0]==(dj-dl)*pow(-2*N*Delta,-1,p)%p
                    counts['genuine_divided_pair_jets']+=1
                    counts['retained_pair_coefficients']+=3
                    counts['prior_actual_normal_comparisons']+=1
                    counts['nonzero_second_pair_jets']+=int(pair[2]!=0)
    assert counts['nonzero_second_pair_jets']>0
    return counts


def main():
    result=dict(status='PASS',exact=exact_checks(),
                scope='Exact original generic-q physical column jets and completed divided-pair jets, including genuine second derivatives. Uniform polynomial bounds are proved analytically. No complex magnetic continuation, completed four-port norm, or full-source asymptotic.')
    Path(__file__).with_name('actual_q_hahn_physical_generic_jet_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
