"""Own generic Newton products and the complete repeated-root source algebra."""
from fractions import Fraction
from pathlib import Path
import json
import sympy


def mul(a, b, p=None):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return [x % p for x in out] if p else out


def add_scaled(out, values, scale, p=None):
    if len(out) < len(values):
        out.extend([0] * (len(values) - len(out)))
    for k, x in enumerate(values):
        out[k] += scale*x
        if p:
            out[k] %= p


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def reduce_poly(a, monic, p):
    a = trim([x % p for x in a])
    while len(a) >= len(monic):
        shift = len(a) - len(monic)
        v = a[-1]
        for i, x in enumerate(monic):
            a[i+shift] = (a[i+shift] - v*x) % p
        a = trim(a)
    return a


def generic_products():
    count = 0
    for q in (Fraction(3, 2), Fraction(5, 3), Fraction(7, 5)):
        dlt = q - 1/q
        t = -dlt*dlt
        f = [Fraction(1)]
        for n in range(1, 15):
            f.append(f[-1]*(q**n-q**(-n))/dlt)
        bs = [[Fraction(1)]]
        for n in range(14):
            bs.append(mul(bs[-1], [q**(2*n+1)+q**(-2*n-1), -1]))
        for i in range(7):
            for j in range(7):
                expected = [Fraction(0)]*(i+j+1)
                for k in range(max(i,j), i+j+1):
                    a = (t**(i+j-k)*f[i]*f[j]*f[i+j]
                         /(f[k]*f[k-i]*f[k-j]*f[i+j-k]))
                    add_scaled(expected, bs[k], a)
                assert trim(expected) == trim(mul(bs[i],bs[j]))
                count += 1
    return count


def root_field(N):
    p = 1 + 2*N*((2000//(2*N))+1)
    while not sympy.isprime(p):
        p += 2*N
    gen = int(sympy.primitive_root(p))
    q = pow(gen, (p-1)//(2*N), p)
    assert pow(q,N,p) == p-1 and sympy.n_order(q,p) == 2*N
    return int(p), q


def root_products(N):
    p,q = root_field(N)
    d = N-1
    qinv = pow(q,-1,p)
    dlt = (q-qinv) % p
    t = -dlt*dlt % p
    f=[1]
    for n in range(1,N):
        f.append(f[-1]*(pow(q,n,p)-pow(q,-n,p))*pow(dlt,-1,p)%p)
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(N)]
    bs=[[1]]
    for c in nodes:
        bs.append(mul(bs[-1],[c,-1],p))
    pn=[(-1)**N*x % p for x in bs[N]]
    bh=[]
    for r in range(N):
        scale=pow(pow(t,r,p)*f[r]*f[r] % p,-1,p)
        bh.append([x*scale%p for x in bs[r]])
    table={}
    for i in range(N):
        for j in range(N):
            expected=[0]*N
            coeff=[0]*N
            if i+j<N:
                for k in range(max(i,j),i+j+1):
                    mu=f[i+j]*f[k]*pow(f[i]*f[j]*f[k-i]*f[k-j]*f[i+j-k]%p,-1,p)%p
                    coeff[k]=mu
                    add_scaled(expected,bh[k],mu,p)
            assert trim(expected)==reduce_poly(mul(bh[i],bh[j],p),pn,p)
            table[i,j]=coeff

    # U_d(z/2), as an integer polynomial reduced in the exact root field.
    u0,u1=[1],[0,1]
    if d==0:
        ud=u0
    elif d==1:
        ud=u1
    else:
        for r in range(2,d+1):
            u2=[0]+u1
            add_scaled(u2,u0,-1)
            u0,u1=u1,u2
        ud=u1
    circle=[(-1)**d*x % p for x in ud]
    lambdas=[]
    for r in range(N):
        v=d-r
        trace=sum(sum(x*pow(c,k,p) for k,x in enumerate(bh[v])) for c in nodes)%p
        lambdas.append(N*trace%p)
    rebuilt=[0]*N
    for r,lam in enumerate(lambdas):
        add_scaled(rebuilt,bh[r],lam,p)
    assert trim(rebuilt)==trim(circle)
    assert all(lambdas[r]==0 for r in range(d-d//2))
    assert lambdas[d]==N*N%p

    def product_coeff(a,b):
        out=[0]*N
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if x and y:
                    add_scaled(out,table[i,j],x*y,p)
        return out

    square=reduce_poly(mul(circle,circle,p),pn,p)
    if N%2==0:
        assert square==[0]
        odd=None
    else:
        m=d//2
        e_st=reduce_poly(mul(bh[m],bh[m],p),pn,p)
        assert square==trim([N*N*x%p for x in e_st])
        h=[0]*N
        for v in range(m+1):
            h[v]=f[m]**2*pow(f[v]**2*f[m-v]**2%p,-1,p)%p
        actual_e=table[m,m]
        assert h==list(reversed(actual_e))
        hsquared=product_coeff(h,h)
        h4=product_coeff(hsquared,hsquared)
        phi=sum(hsquared[k]*hsquared[d-k] for k in range(N))%p
        assert h4[d]==phi
        # This verifies equality in the field, not real positivity by residue sign.
        odd={'N':N,'prime':p,'phi_h4_residue':phi}
    return N*N,odd


def main():
    generic=generic_products()
    root_pairs=0
    odd=[]
    for N in range(2,26):
        count,value=root_products(N)
        root_pairs+=count
        if value:
            odd.append(value)
    result={'status':'PASS','generic_exact_products':generic,
            'root_families':24,'full_root_products':root_pairs,
            'complete_circle_full_normal_families':24,
            'odd_projector_and_positive_period_checks':odd,
            'scope':'Exact rational generic products and finite-field full polynomial quotient checks. Real positivity is proved by principal-root sine factors, not finite-field signs. No quantum-growth claim.'}
    Path(__file__).with_name('actual_positive_newton_multiplication_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
