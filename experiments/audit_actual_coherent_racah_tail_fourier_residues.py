#!/usr/bin/env python3
"""Exact modular audit of the own finite Fourier tail identity.

The proof is in the accompanying note. Root images are exact finite-field
checks, not a replacement for the uniform algebraic argument.
"""
import itertools
import json
from pathlib import Path


def prime(n):
    if n < 2:
        return False
    return all(n % k for k in range(2, int(n**0.5) + 1))


def field(N):
    p = 4*N+1
    while not prime(p):
        p += 4*N
    factors = []
    rest = p-1
    d = 2
    while d*d <= rest:
        if rest % d == 0:
            factors.append(d)
            while rest % d == 0:
                rest //= d
        d += 1
    if rest > 1:
        factors.append(rest)
    g = next(g for g in range(2,p)
             if all(pow(g,(p-1)//r,p) != 1 for r in factors))
    q = pow(g,(p-1)//(2*N),p)
    ii = pow(g,(p-1)//4,p)
    assert pow(q,N,p)==p-1 and ii*ii % p==p-1
    inv = lambda a: pow(a % p,-1,p)
    s = [1]
    H = [0]
    for u in range(1,N):
        qp = pow(q,u,p); qm=inv(qp)
        sine = (qp-qm)*inv(ii) % p
        s.append(s[-1]*sine % p)
        H.append((H[-1]+ii*(qp+qm)*inv(qp-qm)) % p)
    assert s[-1] == N % p
    sine = (q-inv(q))*inv(ii)*inv(2) % p
    return p,q,ii,s,H,sine


def prod(values,p):
    result=1
    for value in values:
        result=result*value % p
    return result


def one(N,aa,cc,data):
    p,q,ii,s,H,sintheta=data
    D=N-1; A,B=aa[:2]; inv=lambda x:pow(x % p,-1,p)
    assert len(aa)==4 and len(cc)==3 and min(cc)>=max(aa)
    assert max(cc)<D and sum(cc)-sum(aa)==D
    cores=[prod((s[c-v] for c in cc),p)*inv(N*s[v]*prod((s[a-v] for a in aa),p)) % p
           for v in range(A+1)]
    J=[(H[v]+sum(H[c-v] for c in cc)-sum(H[a-v] for a in aa)) % p
       for v in range(A+1)]
    harmonic=-sintheta*sum(c*j for c,j in zip(cores,J)) % p
    residual=2*sintheta*inv(N)*sum(
        (-1)**(A+v)*s[v-A-1]*prod((s[c-v] for c in cc),p)*
        inv(s[v]*prod((s[a-v] for a in aa[1:]),p))
        for v in range(A+1,B+1)) % p
    tail=-2*sintheta*N*N*sum(
        (-1)**k*s[k]*inv(prod((s[a+1+k] for a in aa),p)*
                         prod((s[D-c-1-k] for c in cc),p))
        for k in range(D-max(cc))) % p
    assert tail==(harmonic+residual) % p, (N,aa,cc,tail,harmonic,residual)
    Q=q*q % p
    K=sum(c*(c+1)//2 for c in cc)-sum(a*(a+1)//2 for a in aa)
    beta=2*sintheta*inv(N)*pow(ii,N-2,p)*pow(q,-K,p) % p
    def rational(j):
        x=pow(Q,j,p)
        answer=x*inv(1-x) % p
        for u in range(1,max(cc)+1):
            exponent=sum(c>=u for c in cc)-sum(a>=u for a in aa)
            if exponent:
                answer=answer*pow((1-pow(Q,u,p)*x) % p,exponent,p) % p
        return answer
    actual=beta*sum(rational(j) for j in range(1,D-max(cc)+1)) % p
    assert actual==tail
    full=beta*sum(rational(j) for j in range(1,N) if N-j>A) % p
    assert full==harmonic
    if A==B:
        assert residual==0 and tail==harmonic
    else:
        astar=tuple(sorted([A]+[D-c+A for c in cc]))
        cstar=tuple(sorted(D-a+A for a in aa[1:]))
        assert astar[0]==A<astar[1] and max(astar)<=min(cstar)
        assert max(cstar)<D and sum(cstar)-sum(astar)==D
        astarstar=tuple(sorted([A]+[D-c+A for c in cstar]))
        cstarstar=tuple(sorted(D-a+A for a in astar[1:]))
        assert astarstar==tuple(aa) and cstarstar==tuple(sorted(cc))
        dualtail=-2*sintheta*N*N*sum(
            (-1)**k*s[k]*inv(prod((s[a+1+k] for a in astar),p)*
                             prod((s[D-c-1-k] for c in cstar),p))
            for k in range(D-max(cstar))) % p
        dualcores=[prod((s[c-v] for c in cstar),p)*inv(N*s[v]*prod((s[a-v] for a in astar),p)) % p
                   for v in range(A+1)]
        dualJ=[(H[v]+sum(H[c-v] for c in cstar)-sum(H[a-v] for a in astar)) % p
               for v in range(A+1)]
        assert dualtail==residual
        assert dualcores==cores[::-1]
        assert dualJ==[(-j) % p for j in J[::-1]]
    return tail, sum(cores) % p, residual


def main():
    level_records=[]
    repeated=0; unique=0; nonzero_residual=0
    for N in range(3,16):
        data=field(N);D=N-1;count=0
        for aa in itertools.combinations_with_replacement(range(D),4):
            desired=D+sum(aa)
            for c1 in range(aa[-1],D):
                for c2 in range(c1,D):
                    c3=desired-c1-c2
                    if not c2<=c3<D:
                        continue
                    tail,core,res=one(N,aa,(c1,c2,c3),data)
                    count+=1
                    if aa[0]==aa[1]:repeated+=1
                    else:unique+=1
                    nonzero_residual+=bool(res)
        level_records.append({'N':N,'prime':data[0],'balanced_arrays':count})
    all_high=[]
    for m in range(1,33):
        N=3*m+1;data=field(N);p,q,ii,s,H,sintheta=data
        tail,core,res=one(N,(0,0,0,0),(m,m,m),data)
        target=-3*sintheta*H[m]*core % p
        assert tail==target and res==0
        all_high.append({'m':m,'N':N,'prime':p})
    # Actual label realization: flip precisely the three edges outside
    # the unique largest face, without changing the generic formula.
    physical_duals=0
    face_edges=((0,1,4),(2,3,4),(0,3,5),(1,2,5))
    def incidence(L):
        a,b,c,d,e,f=L
        return [a+b+e,c+d+e,a+d+f,b+c+f], [a+b+c+d,a+c+e+f,b+d+e+f]
    for N in range(3,11):
        D=N-1;M=D//2
        for low in itertools.product(range(M+1),repeat=6):
            F,_=incidence(low)
            if min(F)<D:continue
            seen=set()
            for bits in range(64):
                labels=tuple(D-x if bits>>i&1 else x for i,x in enumerate(low))
                if labels in seen:continue
                seen.add(labels)
                F,Q=incidence(labels)
                if min(Q)<=2*D or F.count(max(F))!=1:continue
                ix=F.index(max(F));A=2*D-max(F)
                dual=tuple(x if i in face_edges[ix] else D-x for i,x in enumerate(labels))
                FF,QQ=incidence(dual)
                aa=sorted(2*D-u for u in F);cc=sorted(3*D-u for u in Q)
                assert sorted(2*D-u for u in FF)==sorted([A]+[D-c+A for c in cc])
                assert sorted(3*D-u for u in QQ)==sorted(D-a+A for a in aa[1:])
                assert FF[ix]==F[ix]==max(FF) and FF.count(max(FF))==1
                physical_duals+=1
    # A live physical branch where omitting the residual is false.
    p,*_=field(5)
    tail,core,res=one(5,(0,1,1,2),(2,3,3),field(5))
    assert tail==res==p-1
    result={
        'status':'PASS',
        'scope':'Exact modular checks of uniform own finite Fourier identity, including residual nodes; no general residual bound inferred.',
        'abstract_hypotheses':'0<=a_i<=c_k<=N-2 for every i,k; sum c-sum a=N-1',
        'balanced_array_checks':sum(x['balanced_arrays']for x in level_records),
        'repeated_minimum_checks':repeated,
        'unique_minimum_checks':unique,
        'exact_dual_involution_and_core_reversal_checks':unique,
        'actual_unique_max_face_star_flip_checks':physical_duals,
        'nonzero_residual_images':nonzero_residual,
        'levels':level_records,
        'all_high_closed_identity_checks':all_high,
        'physical_nonzero_residual_regression':{
            'N':5,'partner_labels':[2,2,3,3,2,2],
            'a':[0,1,1,2],'c':[2,3,3],
            'exact_current':'-1','harmonic_contribution':'0',
        },
        'proved_scope':'Exact all-array decomposition and source partner involution; logarithmic coherent tail and polynomial first normal for repeated maximal face; polynomial first-normal differences along the involution; all-high cotangent identity.',
        'remaining_gap':'Unique maximal face residual and higher generic normal jets remain uncontrolled.',
    }
    path=Path(__file__).with_name('actual_coherent_racah_tail_fourier_residues_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',result['balanced_array_checks'],'balanced arrays;',repeated,
          'repeated minimum;',unique,'unique minimum; 32 all-high identities')

if __name__=='__main__':
    main()
