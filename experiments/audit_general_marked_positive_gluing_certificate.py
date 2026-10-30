#!/usr/bin/env python3
"""Exact marked gluing, edge winding and variational-certificate checks.

Eight positive tetrahedra obtained by doubling a regular ideal octahedron
with its two shaded bowties. Checks the actual tetrahedral quotient and
compatible cusp decorations; no general source asymptotic is inferred.
"""
import json
from collections import defaultdict
from pathlib import Path
import sympy as S

class DSU:
    def __init__(self): self.p={}
    def find(self,x):
        self.p.setdefault(x,x)
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def join(self,a,b): self.p[self.find(a)]=self.find(b)


def quotient():
    tet={}
    for h in range(2):
        for j in range(4):
            equator=[j,(j+1)%4]
            if h: equator.reverse()
            tet[(h,j)]=['A','B']+equator
    pair={}
    def glue(a,b,m):
        assert a not in pair and b not in pair
        pair[a]=(b,m); pair[b]=(a,{v:k for k,v in m.items()})
    # Internal faces containing both opposite octahedral vertices.
    for h in range(2):
        for j in range(4):
            a=(h,(j-1)%4); b=(h,j)
            ia=next(i for i,v in enumerate(tet[a]) if v not in ['A','B',j])
            ib=next(i for i,v in enumerate(tet[b]) if v not in ['A','B',j])
            glue((a,ia),(b,ib),{v:v for v in ['A','B',j]})
    # Original white faces copied across the projection sphere.
    for j in range(4):
        omitted=1 if j%2 else 0
        names=[v for i,v in enumerate(tet[(0,j)]) if i!=omitted]
        glue(((0,j),omitted),((1,j),omitted),{v:v for v in names})
    # Actual even shaded pairings, fixing each crossing-circle apex.
    for h in range(2):
        glue(((h,0),1),((h,2),1),{'A':'A',0:3,1:2})
        glue(((h,1),0),((h,3),0),{'B':'B',1:0,2:3})
    assert len(pair)==32
    edges,vertices,linkvertices=DSU(),DSU(),DSU()
    for t,vs in tet.items():
        for i in range(4):
            vertices.find((t,i))
            for j in range(4):
                if i!=j: linkvertices.find((t,i,j))
            for j in range(i+1,4): edges.find((t,i,j))
    for (t,missing),((u,missing2),m) in pair.items():
        p={i:tet[u].index(m[v]) for i,v in enumerate(tet[t]) if i!=missing}
        full=[p[i] if i!=missing else missing2 for i in range(4)]
        inversions=sum(full[i]>full[j] for i in range(4) for j in range(i+1,4))
        assert inversions%2==1, 'face maps reverse oriented boundaries'
        for i in p:
            vertices.join((t,i),(u,p[i]))
            for j in p:
                if i==j:continue
                linkvertices.join((t,i,j),(u,p[i],p[j]))
                edges.join((t,min(i,j),max(i,j)),(u,min(p[i],p[j]),max(p[i],p[j])))
    shape={ (0,1):S.I,(2,3):S.I,
            (0,2):(1+S.I)/2,(1,3):(1+S.I)/2,
            (0,3):1+S.I,(1,2):1+S.I }
    quarter={ij:2 if w==S.I else 1 for ij,w in shape.items()}
    products=defaultdict(lambda:S.Integer(1)); turns=defaultdict(int)
    incidences=defaultdict(list)
    for t in tet:
        for ij,w in shape.items():
            e=edges.find((t,*ij)); products[e]*=w
            turns[e]+=quarter[ij]; incidences[e].append((t,ij))
    assert len(products)==len(tet)==8
    assert all(S.simplify(p-1)==0 for p in products.values())
    assert set(turns.values())=={8}, 'all edge angles are exactly 2pi'
    # Every vertex link is an oriented compact surface; calculate its chi.
    link_f=defaultdict(int); link_v=defaultdict(set)
    for t in tet:
        for i in range(4):
            c=vertices.find((t,i)); link_f[c]+=1
            for j in range(4):
                if i!=j:link_v[c].add(linkvertices.find((t,i,j)))
    chis=[]
    for c,f in link_f.items():
        assert f%2==0
        chi=len(link_v[c])-3*f//2+f
        assert chi==0; chis.append(chi)
    assert len(chis)==3
    # Compatible horospheres: corner sine-law scale squared is 1 at
    # octahedral apices and 2 at equator vertices. A face corner segment
    # is C_i sin(theta_(i,missing)). Its squared length is exact rational.
    def segment2(t,i,missing):
        c2=1 if tet[t][i] in ['A','B'] else 2
        return S.Rational(c2)*(1 if quarter[tuple(sorted((i,missing)))]==2 else S.Rational(1,2))
    decoration_checks=0
    for (t,missing),((u,missing2),m) in pair.items():
        for i,v in enumerate(tet[t]):
            if i==missing:continue
            j=tet[u].index(m[v])
            assert segment2(t,i,missing)==segment2(u,j,missing2)
            decoration_checks+=1
    # Independently verify stationary-angle multipliers. The decorated
    # ideal-face identity gives every truncated edge length -log(s_a s_b).
    # Here these are integer multiples of log(2)/2, so keep that unit exact.
    edge_length_units={}
    corner_u_units={}
    # S=sin(alpha)sin(beta)sin(gamma)=1/2; u=-log C - 1/2 log S.
    for t in tet:
        for i,v in enumerate(tet[t]): corner_u_units[(t,i)]=1 if v in ['A','B'] else 0
    # log(sin(theta)) in units log(2)/2 is 0 for pi/2 and -1 for pi/4.
    for e,incs in incidences.items():
        values=[]
        for t,(i,j) in incs:
            logsin=0 if quarter[(i,j)]==2 else -1
            values.append(logsin+corner_u_units[(t,i)]+corner_u_units[(t,j)])
        assert len(set(values))==1
        edge_length_units[e]=values[0]
    # eta_e=-L_e/2, Lambda_t=(sum u)/2-log(2). Check derivative rows.
    cusp_scales=dict(zip(link_f,S.symbols(f'decoration0:{len(link_f)}',positive=True)))
    for t in tet:
        lam=S.Rational(sum(corner_u_units[(t,i)] for i in range(4)),2)-2
        for ij,opposite in [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]:
            eta=-S.Rational(edge_length_units[edges.find((t,*ij))],2)
            eta2=-S.Rational(edge_length_units[edges.find((t,*opposite))],2)
            minus_log_2sin=-2+(0 if quarter[ij]==2 else 1)
            assert lam+eta+eta2==minus_log_2sin
            # The same condition in the finite real-algebraic certificate.
            sine=S.Integer(1) if quarter[ij]==2 else S.sqrt(2)/2
            A=S.Pow(2,lam/2); B=S.Pow(2,eta/2); C=S.Pow(2,eta2/2)
            assert S.simplify(2*sine*A*B*C-1)==0
            ts=[cusp_scales[vertices.find((t,i))] for i in range(4)]
            gauge_A=S.prod(ts)
            gauge_B=1/S.prod(ts[i] for i in ij)
            gauge_C=1/S.prod(ts[i] for i in opposite)
            assert S.cancel(gauge_A*gauge_B*gauge_C)==1
    return {'tetrahedra':len(tet),'global_edges':len(products),'cusps':len(chis),
            'all_link_euler_characteristics':chis,
            'all_edge_products_one':True,'all_edge_angles_2pi':True,
            'face_corner_decoration_checks':decoration_checks,
            'exact_stationary_multipliers':True,
            'positive_algebraic_phase_multiplier_equations':True,
            'cusp_decoration_monomial_action':True}


def symbolic_checks():
    a,b,c=S.symbols('a b c',positive=True)
    # Hessian restricted to alpha+beta+gamma=pi: cot identity.
    x,y=S.symbols('x y',real=True)
    z=(1-x*y)/(x+y)
    assert S.factor((x+z)*(y+z)-z*z)==1
    # Opposite-pair equal sums are exactly the compatibility for u_i+u_j.
    U=S.symbols('u0:4'); six={(i,j):U[i]+U[j] for i in range(4) for j in range(i+1,4)}
    assert six[(0,1)]+six[(2,3)]==six[(0,2)]+six[(1,3)]
    assert six[(0,1)]+six[(2,3)]==six[(0,3)]+six[(1,2)]
    recovered=(six[(0,1)]+six[(0,2)]-six[(1,2)])/2
    assert S.simplify(recovered-U[0])==0
    return {'restricted_hessian_determinant':1,'corner_length_compatibility':True}

if __name__=='__main__':
    result={'status':'PASS','actual_octahedral_quotient':quotient(),
            'symbolic_variational_checks':symbolic_checks(),
            'scope':'Finite positive geometric/variational certificates only; no quantum period selection.'}
    Path(__file__).with_name('general_marked_positive_gluing_certificate_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 8 positive tetrahedra, 8 exact edge equations, 3 torus links, 96 matching corner segments, exact variational multipliers')
