"""Positive actual Newton period and exact fourteen-tetrahedron core geometry."""
from itertools import product
from pathlib import Path
import json
import sympy as s
import mpmath as mp


def clean(z):
    return s.simplify(s.expand_complex(z))


def geometry():
    rt=s.sqrt(2)
    vertices=[]
    for zero in range(3):
        axes=[i for i in range(3) if i!=zero]
        for a,b in product((-1,1),repeat=2):
            x=[s.S.Zero]*3
            x[axes[0]],x[axes[1]]=a/rt,b/rt
            vertices.append(x)
    z=[clean((x+s.I*y)/(1-w)) for x,y,w in vertices]
    tris=[(4,8,5),(4,5,9),(6,10,7),(6,7,11),
          (2,9,3),(2,3,11),(1,5,3),(1,3,7),
          (1,5,8),(2,4,9),(3,5,9),(1,7,10),(2,6,11),(3,7,11)]
    representatives={'A':s.Rational(2,3)+s.I*rt/3,
                     'B':s.Rational(1,3)+2*s.I*rt/3,
                     'E':s.Rational(2,3)+s.I*rt/6}

    def orbit(w):
        base=[w,1/(1-w),1-1/w]
        base += [1/s.conjugate(v) for v in base]
        return [clean(v) for v in base]

    orbits={k:orbit(v) for k,v in representatives.items()}
    counts=dict.fromkeys(representatives,0)
    shapes=[]
    for tri in tris:
        a,b,c,d=[z[i] for i in (0,*tri)]
        w=clean((a-c)*(b-d)/((a-d)*(b-c)))
        if s.im(w)<0:
            w=clean(s.conjugate(w))
        assert s.im(w)>0
        found=[k for k,vs in orbits.items() if any(clean(w-v)==0 for v in vs)]
        assert len(found)==1,(tri,w,found)
        kind=found[0]
        counts[kind]+=1
        shapes.append({'vertices':[0,*tri],'type':kind,'shape':str(w)})
    assert counts=={'A':10,'B':2,'E':2}

    mp.mp.dps=90
    theta=mp.atan(mp.sqrt(2));delta=mp.pi/2-theta
    def lob(t):return mp.im(mp.polylog(2,mp.exp(2j*t)))/2
    vq=12*lob(theta)+12*lob(delta)-2*lob(2*theta)+2*lob(2*theta-mp.pi/2)
    def dw(w):return mp.im(mp.polylog(2,w))+mp.arg(1-w)*mp.log(abs(w))
    direct=mp.mpf(0)
    for row in shapes:
        w=s.sympify(row['shape'])
        wc=mp.mpc(str(s.re(w).evalf(95)),str(s.im(w).evalf(95)))
        direct+=dw(wc)
    assert abs(direct-vq)<mp.mpf('1e-80')
    return {'exact_shape_counts':counts,'tetrahedra':shapes,'volume':mp.nstr(vq,65)},vq


def positive_period(N):
    assert N%2==1
    mp.mp.dps=80
    d=N-1;m=d//2
    sn=[mp.mpf(1)]
    for k in range(1,N):sn.append(sn[-1]*2*mp.sin(mp.pi*k/N))
    beta2=[sn[m]**2/(sn[i]**2*sn[m-i]**2) for i in range(m+1)]
    a=[mp.mpf(0)]*N
    for i in range(m+1):
        for j in range(i,m+1):
            factor=beta2[i]*beta2[j]*(1 if i==j else 2)
            for k in range(j,i+j+1):
                mu=sn[i+j]*sn[k]/(sn[i]*sn[j]*sn[k-i]*sn[k-j]*sn[i+j-k])
                assert mu>0
                a[k]+=factor*mu
    assert all(x>0 for x in a)
    value=sum(a[k]*a[d-k] for k in range(N))
    return value


def main():
    geo,vq=geometry()
    theta=mp.atan(mp.sqrt(2));t=theta/mp.pi
    L=lambda u:-mp.im(mp.polylog(2,mp.exp(2j*mp.pi*u)))/(2*mp.pi)
    g=lambda u:-2*L(u)-2*L(mp.mpf('.5')-u)
    maximum=6*g(t)+2*(L(2*t)-L(2*t-mp.mpf('.5')))
    assert abs(mp.pi*maximum-vq)<mp.mpf('1e-75')
    assert abs(-12*mp.log(mp.tan(theta))+4*mp.log(-mp.tan(2*theta)))<mp.mpf('1e-75')
    rows=[]
    for N in (3,5,9,17,33,65):
        val=positive_period(N)
        if N==3:assert abs(val-11)<mp.mpf('1e-70')
        rows.append({'N':N,'positive':True,'pi_log_period_over_N':mp.nstr(mp.pi*mp.log(val)/N,30),
                     'N_power_9_over_2_calibration_only':mp.nstr(val*mp.power(N,mp.mpf('4.5'))*mp.exp(-N*vq/mp.pi),30)})
    result={'status':'PASS','exact_cuboctahedron_geometry':geo,
            'algebraic_saddle':'tan(pi*t)^2=2; t=atan(sqrt(2))/pi',
            'positive_partition_levels':rows,
            'scope':'Exact algebraic tetrahedron shapes and positive Newton sums. Log-limit proof is uniform factorial asymptotics plus strict concavity and interior lattice rounding; displayed power-prefactor values are diagnostics only. Odd central period, not the full graph color sum.'}
    Path(__file__).with_name('actual_positive_newton_cuboctahedral_period_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','exact_shape_counts':geo['exact_shape_counts'],'volume':geo['volume'],'positive_levels':len(rows)},indent=2))


if __name__=='__main__':main()
