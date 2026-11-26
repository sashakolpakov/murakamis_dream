"""Bounded exact checks for Appendix N; no norm samples or asymptotic inference."""
from pathlib import Path
import hashlib,json
import sympy as sp
if not __debug__:
    raise SystemExit('Assertions must be enabled.')


def run(N):
    K=sp.QQ.cyclotomic_field(4*N); zeta=K.unit; q=zeta**2; Q=q*q
    zero,one=K.zero,K.one; d=N-1; x,y=K(2),K(3)
    I=[[one if i==j else zero for j in range(N)] for i in range(N)]
    Z=lambda:[[zero for _ in range(N)] for _ in range(N)]
    def add(A,B):return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
    def scale(a,A):return [[a*v for v in row] for row in A]
    def mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(N)),zero) for j in range(N)] for i in range(N)]
    def mpow(A,n):
        out=I
        for _ in range(n):out=mul(out,A)
        return out
    def pmul(a,b):
        out=[zero]*(len(a)+len(b)-1)
        for i,v in enumerate(a):
            for j,w in enumerate(b):out[i+j]+=v*w
        return out
    def padd(a,b):
        out=[zero]*max(len(a),len(b))
        for i,v in enumerate(a):out[i]+=v
        for i,v in enumerate(b):out[i]+=v
        return out
    t=sp.Symbol('t'); chi=sp.Poly(2*sp.chebyshevt(N,t/2)+2,t)
    p=[K(int(chi.nth(j))) for j in range(N+1)]
    def rem(a):
        a=a[:]
        while len(a)>N:
            c=a.pop(); k=len(a)-N
            for j in range(N):a[k+j]-=c*p[j]
        return a+[zero]*(N-len(a))
    def ppow(a,n):
        out=[one]
        for _ in range(n):out=rem(pmul(out,a))
        return rem(out)
    def ev(a,c):
        out=zero
        for v in reversed(a):out=v+c*out
        return out
    def deriv(a):return [K(j)*a[j] for j in range(1,len(a))]
    def matrix_ev(a,A):
        out=Z()
        for v in reversed(a):out=add(scale(v,I),mul(A,out))
        return out
    im=zeta**N
    s=[(q**j-q**(-j))/im for j in range(N)]
    nodes=[q**(2*j+1)+q**(-2*j-1) for j in range(N)]
    O=Z()
    for j in range(N):
        O[j][j]=nodes[j]
        if j>=1:O[j-1][j]=-s[j]**2*(x+y)
        if j>=2:O[j-2][j]=-s[j]*s[j-1]*x*y
    assert matrix_ev(p,O)==Z()
    def crossing(sign):
        qq=q**sign; QQ=qq**2; fac=[one]
        for j in range(1,N):fac.append(fac[-1]*(one-QQ**j))
        A=Z()
        for j in range(N):
            for i in range(j+1):
                for k in range(j-i+1):
                    l=j-i-k
                    A[i][j]+=K((-1)**j)*qq**(j+i*i)*fac[j]/(fac[i]*fac[k]*fac[l])*x**k*y**l
        return scale(zeta**(sign*d*d),A)
    Rp,Rm=crossing(1),crossing(-1)
    assert mul(Rp,Rm)==I and mul(Rm,Rp)==I
    # Independently construct the crossing polynomial from its finite Newton expansion.
    basis=[one]; rr=[zero]; ss=one
    for j in range(N):
        rr=padd(rr,[(-q)**j*v/ss for v in basis])
        if j<d:
            basis=pmul(basis,[nodes[j],-one]);ss*=s[j+1]**2
    rp=[zeta**(d*d)*v for v in rr]
    basis=[one]; rr=[zero];ss=one
    for j in range(N):
        rr=padd(rr,[(-q**-1)**j*v/ss for v in basis])
        if j<d:basis=pmul(basis,[nodes[j],-one]);ss*=s[j+1]**2
    rm=[zeta**(-d*d)*v for v in rr]
    assert matrix_ev(rp,O)==Rp and matrix_ev(rm,O)==Rm
    powers=[I]
    for _ in range(N-1):powers.append(mul(powers[-1],O))
    def V(c,normal=False):
        out=Z()
        for k in range(1,N+1):
            for j in range(k):
                e=k-1-j
                if normal:
                    if e:out=add(out,scale(p[k]*K(e)*c**(e-1),powers[j]))
                else:out=add(out,scale(p[k]*c**e,powers[j]))
        return out
    scalar_checks=0
    for n in (-2,-1,0,1,2):
        f=ppow(rp if n>=0 else rm,abs(n));df=deriv(f)
        reconstructed=Z()
        for a in range(N//2):
            c=nodes[a];h=2*a+1
            fn=zeta**(n*d*d)*K((-1)**(a*n))*q**(n*a*(a+1))
            gamma=-K(N-h)/(K(2)*(q**h-q**(-h)))
            assert ev(f,c)==fn and ev(df,c)==K(n)*gamma*fn
            reconstructed=add(reconstructed,scale(one/K(N*N),add(
                scale((K(4)-c*c)*fn,V(c,True)),scale(((K(4)-c*c)*K(n)*gamma-c)*fn,V(c)))))
        if N%2:
            fn=zeta**(n*d*d)*K((-1)**((N//2)*n))*q**(n*(N//2)*(N//2+1))
            assert ev(f,K(-2))==fn
            reconstructed=add(reconstructed,scale(fn/K(N*N),V(K(-2))))
        assert reconstructed==mpow(Rp if n>=0 else Rm,abs(n))
        for j in range(2*N+1):
            H=[zero]*j+[one];FH=pmul(f,H);dFH=deriv(FH)
            value=zero
            for a in range(N//2):
                c=nodes[a];value+=((K(4)-c*c)*ev(dFH,c)-c*ev(FH,c))/K(N*N)
            if N%2:value+=ev(FH,K(-2))/K(N*N)
            assert value==rem(FH)[d]
            scalar_checks+=1
        # Actual value-vanishing one-sided diagonal; the retained normal yields a unit phase.
        H=sp.div(chi.as_expr(),t-sp.sympify(2*sp.cos(sp.pi/N)),t) if N==3 else None
        c=nodes[0];coeff=[one]
        for j in range(N-1,-1,-1):coeff.insert(0,p[j]+c*coeff[0])
        assert coeff[0]==zero
        H=coeff[1:]
        assert len(H)==N
        for c0 in nodes:assert ev(H,c0)==zero
        FH=pmul(f,H);dFH=deriv(FH);value=zero
        for a in range(N//2):
            c0=nodes[a];value+=(K(4)-c0*c0)*ev(dFH,c0)/K(N*N)
        assert value==ev(f,nodes[0])
    return {'N':N,'field_order':4*N,'signed_powers':[-2,-1,0,1,2],
            'original_triangular_crossing_vs_Newton_polynomial':True,
            'full_resolvent_reconstruction_including_normals':True,
            'scalar_Hermite_vs_quotient_checks':scalar_checks,
            'node_vanishing_diagonal_retains_unit_phase':True}

results=[run(N) for N in (2,3,4,5)]
out=Path('/private/tmp/md-audit-hermite-resolvent-reproduction-results.json')
record={'scope':'Exact bounded cyclotomic identities; no sampled norm ratios, no all-level inference. The independent original triangular crossing is evaluated at x=2,y=3; the all-level source identity remains a written proof.', 'checks':results,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
