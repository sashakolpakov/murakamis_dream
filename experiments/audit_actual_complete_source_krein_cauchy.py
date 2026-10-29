#!/usr/bin/env python3
"""Full source module: common indefinite form and positive Hermite Cauchy."""

import json
from pathlib import Path

import mpmath as mp


def close(A,B,tol='1e-60'):
    assert mp.norm(A-B)<=mp.mpf(tol)*max(1,mp.norm(B))


def case(N):
    q=mp.exp(mp.j*mp.pi/N); Q=q*q; d=N-1; x=q**d
    F=[mp.mpc(1)]
    for j in range(1,N):F.append(F[-1]*(1-Q**j))
    # Actual original E/F coproduct restricted to physical degree d.
    A=mp.matrix(N)
    for a in range(N):
        b=d-a
        A[a,a]+=q+1/q
        intermediates=[]
        if a:intermediates.append((a-1,b,(Q**(-a)-1)*x*Q**(-b)))
        if b:intermediates.append((a,b-1,Q**(-b)-1))
        for u,v,weight in intermediates:
            if u<d:A[u+1,a]+=weight*(1-Q**(u+1))
            if v<d:A[u,a]+=weight*x**(-1)*Q**u*(1-Q**(v+1))
    B,J,R=mp.matrix(N),mp.matrix(N),mp.matrix(N)
    kappa=q**(mp.mpf(d*d)/2)
    for j in range(N):
        B[j,j]=q**(2*j+1)+q**(-2*j-1)
        if j:B[j-1,j]=Q**j+Q**(-j)-2
        for i in range(N-j):
            binomial=F[d-j]/(F[i]*F[d-j-i])
            J[i,j]=(-x*Q)**(d-i)*x**j*Q**((i*(i+1)-d*(d+1))//2)*binomial
        a,b=j,d-j
        for k in range(min(a,d-b)+1):
            R[b+k,a]=(kappa*x**(-a-b+k)*Q**(b*(a-k))
                      *F[b+k]*F[a]/(F[k]*F[b]*F[a-k]))
    R2=J**-1*R*J
    P=mp.matrix(N)
    for j in range(N):P[d-j,j]=1
    close(J**-1*A*J,B)
    close(A.H*P,P*A);close(B.H*P,P*B)
    close(R.H*P*R,P);close(R2.H*P*R2,P)
    cup=mp.matrix([N*x**(j-d) for j in range(N)])
    ell=mp.matrix([[x**(-j)*Q**(-j)/N for j in range(N)]])
    mark=mp.matrix([[x**(d-j)/N**2 for j in range(N)]])
    close(ell,cup.H*P/N**2);close(mark,cup.H/N**3)
    assert abs((cup.H*P*cup)[0])<mp.mpf('1e-60')
    V0=mp.matrix([[x**(u-d)*Q**(-k*u)*q**(-k)/mp.sqrt(N)
                   for k in range(N)] for u in range(N)])
    close(V0.H*V0,mp.eye(N))
    A0,B0=V0.H*A*V0,V0.H*B*V0
    At,Bt=mp.matrix(N),mp.matrix(N)
    for k in range(N):
        c=lambda j:q**(2*j+1)+q**(-2*j-1)
        At[k,k]=c(k); Bt[k,k]=2*q**(-2*k-1)
        if k:
            At[k-1,k]=8*mp.sin(mp.pi*k/N)**2
            Bt[k-1,k]=1-Q**(-k)
        if k>=2:At[k-2,k]=c(k-1)-c(0)
        if k<d:Bt[k+1,k]=1-Q**(-k-1)
    close(A0,At);close(B0,Bt)
    close(V0.H*P*V0,(-1)**d*P)
    ep=mp.matrix(N,1);ep[0]=N**mp.mpf('1.5')
    el=mp.matrix(1,N);el[0,d]=(-1)**d/mp.sqrt(N)
    close(V0.H*cup,ep);close(ell*V0,el)
    # Full physical degree-d Hermite frame, including all derivative columns.
    columns=[];meta=[]
    for j in range((N+1)//2):
        c=mp.re(q**(2*j+1)+q**(-2*j-1))
        f,w=mp.matrix(N,1),mp.matrix(N,1);f[0]=1
        for u in range(N-1):
            prev=A[u,u-1]*f[u-1] if u else 0
            prevw=A[u,u-1]*w[u-1] if u else 0
            f[u+1]=((c-A[u,u])*f[u]-prev)/A[u,u+1]
            w[u+1]=(f[u]+(c-A[u,u])*w[u]-prevw)/A[u,u+1]
        columns.append(f);meta.append((c,'value'))
        if 2*j+1<N:columns.append(w);meta.append((c,'derivative'))
    VH=mp.matrix([[col[i] for col in columns] for i in range(N)])
    L=VH**-1*J; u=L*cup; a=ell*L**-1
    for k,(c,kind) in enumerate(meta):
        expected=(N*(-1)**d*x**(-d)*(-c if kind=='value' else 4-c*c)
                  if abs(c+2)>mp.mpf('1e-60') else N*x**(-d))
        assert abs(u[k]-expected)<mp.mpf('1e-55')*max(1,abs(expected))
        expected_a=x**d/N if kind=='value' else 0
        assert abs(a[k]-expected_a)<mp.mpf('1e-60')
    capdual=N*mp.norm(a)**2; initial=mp.norm(u)**2/N
    assert capdual<=1+mp.mpf('1e-60') and initial<=8*N*N
    W=mp.eye(N)
    for letter in [2,-1,2,2]:
        M=R if abs(letter)==1 else R2
        W=(M if letter>0 else M**-1)*W
    K=(ell*W*cup)[0]
    W0=V0.H*W*V0
    assert abs(K-(-1)**d*N*W0[d,0])<mp.mpf('1e-55')*max(1,abs(K))
    energy=mp.norm(L*W*cup)**2/N
    assert abs(K)**2<=capdual*energy*(1+mp.mpf('1e-55'))
    # An explicit positive P-compatible metric, without the word in its definition.
    h=mp.matrix(N)
    for j in range(N):
        h[j,j]=mp.mpf(j)/N
        if j+1<N:h[j,j+1]=mp.j/7;h[j+1,j]=-mp.j/7
    X=h-P*h*P; G=mp.expm(X)
    close(G*P*G,P)
    dual=(cup.H*P*G**-1*P*cup)[0]
    close(mp.matrix([[dual]]),cup.H*G*cup)
    rhs=mp.re(dual*(cup.H*W.H*G*W*cup)[0]/N**4)
    assert abs(K)**2<=rhs*(1+mp.mpf('1e-55'))
    return {'N':N,'literal_P_unitary_both_braids':True,
            'complete_source_unitary_endpoints':True,
            'complete_Hermite_cap_dual':mp.nstr(capdual,12),
            'complete_Hermite_initial_energy':mp.nstr(initial,16),
            'actual_coherent_word_energy':mp.nstr(energy,18),
            'positive_and_P_compatible_Cauchy':True}


if __name__=='__main__':
    mp.mp.dps=105
    result={'status':'PASS','complete_source_metrics':[case(N) for N in range(2,14)],
            'scope':'Exact all-channel metric/source conservation and Cauchy; no geometric word-energy bound.'}
    Path(__file__).with_name('actual_complete_source_krein_cauchy_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS 12 complete original Casimir/braid/source modules; full Hermite boundary metrics; '
          'actual coherent word Cauchy and P-compatible positive metrics')
