"""One existing quadrangulation: exact angle equations and rigorous Arb penalty certificate.

No numerical optimizer or level-growth test. The proposed weights are literal
algebraic inputs; exact phase products and interval branch checks prove the
complete angle equations. Rational projection-dual witnesses need not be exact
minimizers. Fourteen nonsimple charts use exact tight-Hall support and Jensen.
"""
import argparse,itertools,json,sys
from pathlib import Path
from collections import Counter
from fractions import Fraction
import sympy as sp
from flint import arb,ctx
ctx.prec=192
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'experiments'))
from audit_actual_original_marked_face_coefficient import morse_faces

OLD=[(1,0,4,2),(2,0,5,3),(4,2,6,5),(1,4,0,6),(6,5,0,3)]
PORTS=[(0,1,2,4)]+OLD[1:]
MARKS={0,1};ORD=set(range(2,7));H=sp.Rational(1,2)
r2=sp.sqrt(2);r5=sp.sqrt(5);q=sp.Rational
W={
0:[1,1,3-2*r2,4-2*r2,3-2*r2],
1:[1,(3+r5)/2,(3+r5)/2,2+r5,1],
2:[1,1,q(1,9),q(4,9),q(1,9)],
3:[1,3+2*r2,2,2,1],
4:[1,q(9,4),q(1,4),7,q(1,4)],
5:[1,4,4,12,1],
6:[1,4,q(1,4),q(9,4),q(1,4)],
7:[1,9,4,4,1],
9:[1,3+2*r2,1,4+2*r2,3+2*r2],
11:[1,25,1,4,9],13:[1,9,1,28,4],15:[1,25,1,9,4],
16:[1,q(25,9),q(1,9),q(4,9),q(1,9)],
17:[1,3+2*r2,2,2,1],
20:[1,q(25,4),q(1,4),q(9,4),q(1,4)],
21:[1,9,4,4,1],25:[1,9,1,4,9],29:[1,16,1,9,4]}

def ball(z):
    z=sp.sympify(z)
    if z.is_Rational:return arb(int(z.p))/int(z.q)
    if z.is_Add:return sum((ball(t) for t in z.args),arb(0))
    if z.is_Mul:
        out=arb(1)
        for t in z.args:out*=ball(t)
        return out
    if z.is_Pow and z.exp==H:return ball(z.base).sqrt()
    raise ValueError(z)

def interval(a):return {'lower':str(a.lower()),'upper':str(a.upper())}
def maxball(a):
    lo=max(x.lower() for x in a);hi=max(x.upper() for x in a)
    return (arb(lo)+arb(hi))/2+arb(0,(arb(hi)-arb(lo))/2)
def minball(a):return -maxball([-x for x in a])

def triangles(mask):
    return [t for e,(x,b,c,y) in enumerate(PORTS)
            for t in ([(b,x,c),(b,y,c)] if mask>>e&1 else [(x,b,y),(x,c,y)])]
def simple(tri):
    ed=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tri for i in range(3))
    return len(ed)==15 and set(ed.values())=={2}

CACHE={};M=8192
def f_angle(a,key):
    if key in CACHE:return CACHE[key]
    if key in ('zero','half'):return arb(0)
    ans=arb(0)
    for n in range(1,M+1):
        ans+=((2*n*a).sin()+(2*n*(arb.pi()/2-a)).sin())/(2*n*n)
    ans=ans/arb.pi()+arb(0,arb(1)/(M*arb.pi()))
    CACHE[key]=ans
    return ans

def complete(mask):
    tri=triangles(mask);assert simple(tri)
    L=list(map(sp.sympify,[0,0]+W[mask]));LB=list(map(ball,L))
    assert all(LB[f]>0 for f in ORD)
    prods={f:sp.Integer(1) for f in ORD};loads={f:arb(0) for f in ORD}
    theta=[];phi=arb(0)
    for row in tri:
        w=[L[f] for f in row];ww=[LB[f] for f in row]
        disc=sp.simplify(w[0]*w[1]+w[0]*w[2]+w[1]*w[2])
        T=sp.sqrtdenest(sp.sqrt(disc))
        assert sp.simplify(T*T-disc)==0
        TB=ball(T);rt=[]
        assert TB.is_zero() if disc==0 else TB>0
        for f,z,zz in zip(row,w,ww):
            if f in MARKS:a=arb(0);key='zero'
            elif T==0:a=arb.pi()/2;key='half'
            else:
                ratio=sp.simplify(sp.radsimp(z/T));a=(zz/TB).atan();key=str(ratio)
                assert a>0 and a<arb.pi()/2
            rt.append(a/arb.pi());phi+=f_angle(a,key)
            if f in ORD:
                loads[f]+=a/arb.pi()
                prods[f]=sp.simplify(sp.radsimp(prods[f]*(T+sp.I*z)/(T-sp.I*z)))
        assert abs(sum(rt,arb(0))-arb(1)/2)<arb('1e-45')
        theta.append(rt)
    for f in ORD:
        assert sp.simplify(prods[f]-1)==0,(mask,f,prods[f])
        assert loads[f]>arb('0.99') and loads[f]<arb('1.01')
        # exp(2pi i load)=1 exactly; this interval selects load=1.
    return theta,phi

def penalty_dual(rows,inputs):
    p,r=rows
    K=arb(1)/2+sum((z*z for row in rows for z in row),arb(0))-p[2]-r[2]
    v=[p[1]-p[2],r[0]-r[2],r[1]-r[2]]
    allowed=[i for i,f in enumerate(inputs) if f not in MARKS]
    assert allowed
    # Choose a rational witness for the projection dual. Its quality is
    # immaterial to validity: the subsequent enclosure is a lower bound
    # for EVERY rational tau, not an assertion that this is the minimizer.
    vf=[float(z.mid()) for z in v];lo=min(vf)-1;hi=max(vf)
    for _ in range(60):
        mid=(lo+hi)/2
        if sum(max(vf[i]-mid,0) for i in allowed)>.5:lo=mid
        else:hi=mid
    tq=Fraction((lo+hi)/2).limit_denominator(10**8)
    tau=arb(tq.numerator)/tq.denominator
    bound=K-arb(1)/4-tau-sum((maxball([arb(0),v[i]-tau])**2 for i in allowed),arb(0))
    beta=arb.pi()*minball([K,bound])
    assert beta>0
    return beta, str(tq)

def penalties(mask,theta):
    data=[];total=arb(0)
    for e,(x,b,c,y) in enumerate(PORTS):
        if not mask>>e&1:continue
        rows=theta[2*e:2*e+2];sides=[];witness=[]
        for child in (c,b):
            if child in MARKS:continue
            rr=rows if child==c else [[row[2],row[1],row[0]] for row in rows]
            other=b if child==c else c
            z,t=penalty_dual(rr,(x,other,y))
            zz,tt=penalty_dual(rr[::-1],(y,other,x))
            sides.append(maxball([z,zz]));witness.append({'child':child,'tau':t,'tau_other_outer':tt})
        bb=minball(sides);total+=bb
        data.append({'port':e,'bound':interval(bb),'witnesses':witness})
    return total,data

def nonsimple_upper(mask):
    tri=triangles(mask);assert not simple(tri)
    support=[set(t)-MARKS for t in tri];cuts=[]
    for size in range(1,len(ORD)):
        for subset in itertools.combinations(sorted(ORD),size):
            S=set(subset);touch=[j for j,t in enumerate(tri) if S.intersection(t)]
            if len(touch)==2*len(S):
                cuts.append({'faces':list(subset),'rows':touch})
                for j in touch:support[j]&=S
    assert all(support)
    sizes=list(map(len,support));upper=arb(0)
    for n in sizes:
        upper+=n*f_angle(arb.pi()/(2*n),'half' if n==1 else f'rational_{n}')
    assert upper<arb('4.18')
    return upper,{'mask':mask,'tight_cuts':cuts,'remaining_support_sizes':sizes,'capacity_upper':interval(upper)}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('research_prescribed_diagonal_flip_penalty_results.json'));args=parser.parse_args()
    chart=morse_faces(3,[1,3,2,1,3],0)
    assert chart['circles']==OLD and chart['v']==1 and chart['faces']==7
    assert PORTS[0]==(OLD[0][1],OLD[0][0],OLD[0][3],OLD[0][2])
    assert {m for m in range(32) if simple(triangles(m))}==set(W)
    base_theta,base_phi=complete(0);assert base_phi>arb('4.999')
    data=[];gaps=[];higher=None
    for mask in range(1,32):
        if mask in W:
            th,phi=complete(mask);pen,detail=penalties(mask,th)
            gap=base_phi-phi+pen;gaps.append(gap)
            assert gap>arb('0.01'),(mask,gap)
            if mask==1:
                higher=phi-base_phi;assert higher>arb('0.17')
            data.append({'mask':mask,'simple':True,'complete_weights':list(map(str,W[mask])),'complete_capacity':interval(phi),'penalty_lower':interval(pen),'certificate_gap':interval(gap),'ports':detail})
        else:
            upper,item=nonsimple_upper(mask);gap=base_phi-upper;gaps.append(gap)
            assert gap>arb('0.8'),(mask,gap)
            data.append({'simple':False,**item,'certificate_gap':interval(gap)})
    out={'status':'PASS','scope':'One already recorded five-face MAIN quadrangulation, prescribed at its single-port-0 flip. Exact finite chart incidence, complete angle equations and branch selection, original protected targets, rigorous Fourier/Arb capacities and rational projection-dual bounds. This certifies a nonmaximal prescribed chart under the geometric penalty theorem; no universal prescribed-chart result, isotopy of choices, or numerical asymptotic claim.',
         'counts':{'original_ports':5,'diagonalizations':32,'simple_complete_charts':18,'exact_ordinary_face_products':90,'nonsimple_hall_supported_charts':14,'nonempty_flip_certificates':31},'precision_bits':ctx.prec,'fourier_terms':M,'base_weights':list(map(str,W[0])),'base_capacity':interval(base_phi),'higher_chart_excess':interval(higher),'certified_uniform_flip_gap':'0.01','minimum_enclosed_gap':interval(minball(gaps)),'charts':data}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='charts'},indent=2))

if __name__=='__main__':main()
