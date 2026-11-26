"""Exact original N=6 central extraction on small matched spheres.

The coefficient ring is Z[sqrt(3)]. Numeric roots only locate candidates;
any reported Newton defect is an exact ordered-field sign calculation.
"""
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path

Z=(0,0); O=(1,0)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,n): return (a[0]*n,a[1]*n)
def sign(a):
    x,y=a
    if not x:return (y>0)-(y<0)
    if not y:return (x>0)-(x<0)
    if x>0 and y>0:return 1
    if x<0 and y<0:return -1
    if x>0:return (x*x>3*y*y)-(x*x<3*y*y)
    return (3*y*y>x*x)-(3*y*y<x*x)
def numeric(a): return a[0]+3**.5*a[1]
def padd(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=add(out.get(k,Z),v)
    return {k:v for k,v in out.items() if v!=Z}
def pmul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            t=tuple(x+y for x,y in zip(k,l))
            out[t]=add(out.get(t,Z),mul(v,w))
    return {k:v for k,v in out.items() if v!=Z}
def pscale(a,c):return {k:mul(v,c) for k,v in a.items()}
def var(i):
    t=[0]*4;t[i]=1
    return {tuple(t):O}
ONE={(0,0,0,0):O}
x,b,c,y=[var(i) for i in range(4)]
A=padd(x,y);xy=pmul(x,y)
def cofactor(mid):
    v=var(mid)
    r1=padd(pscale(v,(2,1)),A)
    r2=padd(padd(pscale(pmul(v,v),(4,2)),
                  pscale(pmul(A,r1),(3,0))),pscale(xy,(0,2)))
    # s2*s1*a1 = 2sqrt3.
    return r2,pscale(r1,(2,-1))
Db,Eb=cofactor(1);Dc,Ec=cofactor(2)
PC=padd(pscale(pmul(A,pmul(Db,Dc)),(4,0)),
        pscale(pmul(xy,padd(pmul(Db,Ec),pmul(Eb,Dc))),(0,2)))
assert all(sum(k)==5 and k[1]<=2 and k[2]<=2 and sign(v)>0 for k,v in PC.items())

def pairs(faces):
    adj=defaultdict(list)
    for i,t in enumerate(faces):
        for k in range(3):adj[tuple(sorted((t[k],t[(k+1)%3])))].append(i)
    assert all(len(v)==2 for v in adj.values())
    neighbors=defaultdict(list)
    for e,(i,j) in adj.items():
        neighbors[i].append(j);neighbors[j].append(i)
    def rec(left,out):
        if not left:yield out;return
        i=min(left)
        for j in neighbors[i]:
            if j in left:yield from rec(left-{i,j},out+[(i,j)])
    return adj,list(rec(set(range(len(faces))),[]))

def quartet(f,g):
    common=set(f)&set(g);assert len(common)==2
    for k in range(3):
        xx,bb,yy=f[k],f[(k+1)%3],f[(k+2)%3]
        if {xx,yy}==common:
            cc=next(z for z in g if z not in common)
            assert any(tuple(g[l:]+g[:l])==(xx,yy,cc) for l in range(3))
            return xx,bb,cc,yy
    raise AssertionError

def exterior(quartets,anchor):
    xx,bb,zz,yy=quartets[anchor]
    protected={bb,yy}
    ordinary=sorted(set(sum((list(t) for t in quartets),[]))-protected)
    index={f:i for i,f in enumerate(ordinary)}
    targets={f for f in ordinary if f not in {xx,zz}}
    active=[t for e,t in enumerate(quartets) if e!=anchor]
    # Greedy order closes most original target variables early.
    remaining=set(range(len(active)));order=[];seen=set()
    while remaining:
        def priority(e):
            t=set(active[e])-protected
            future=set().union(*(set(active[f]) for f in remaining-{e})) if len(remaining)>1 else set()
            return (len((seen|t)&targets-future),len(t&seen))
        e=max(remaining,key=priority);remaining.remove(e);order.append(e);seen|=set(active[e])
    state={(0,)*len(ordinary):O};closed=set()
    for step,e in enumerate(order):
        q=active[e];local={}
        for k,v in PC.items():
            if any(k[i] and q[i] in protected for i in range(4)):continue
            z=[0]*len(ordinary)
            for i,f in enumerate(q):
                if f in index:z[index[f]]+=k[i]
            z=tuple(z);local[z]=add(local.get(z,Z),v)
        future=set().union(*(set(active[f]) for f in order[step+1:])) if step+1<len(order) else set()
        nowclose=targets-future-closed
        out={}
        for k,v in state.items():
            for l,w in local.items():
                z=tuple(a+b for a,b in zip(k,l))
                if max(z)>5:continue
                if any(z[index[f]]!=5 for f in nowclose):continue
                out[z]=add(out.get(z,Z),mul(v,w))
        state=out;closed|=nowclose
    out=[Z]*6
    for k,v in state.items():
        assert all(k[index[f]]==5 for f in targets)
        assert k[index[xx]]+k[index[zz]]==5
        # A=L_z, C=L_x, as in the actual cap polynomial.
        out[k[index[zz]]]=add(out[k[index[zz]]],v)
    return out

def newton_defects(p):
    out=[]
    for j in range(1,5):
        value=add(scale(mul(p[j],p[j]),j*(5-j)),
                  neg(scale(mul(p[j-1],p[j+1]),(j+1)*(6-j))))
        if sign(value)<0:out.append({'j':j,'exact':value})
    return out

def sphere_link_check(faces):
    edges,matching=pairs(faces)
    vertices=set(sum((list(f) for f in faces),[]))
    assert len(vertices)-len(edges)+len(faces)==2
    for e,(i,j) in edges.items():
        assert sum(1 if (t[k],t[(k+1)%3])==e else -1
                   for t in (faces[i],faces[j]) for k in range(3)
                   if tuple(sorted((t[k],t[(k+1)%3])))==e)==0
    for v in vertices:
        graph=defaultdict(set)
        for t in faces:
            if v in t:
                a,b=[x for x in t if x!=v];graph[a].add(b);graph[b].add(a)
        assert all(len(x)==2 for x in graph.values())
        seen=set();todo=[next(iter(graph))]
        while todo:
            a=todo.pop()
            if a in seen:continue
            seen.add(a);todo.extend(graph[a]-seen)
        assert len(seen)==len(graph)
    return matching

def stellar(faces,i):
    n=max(sum((list(f) for f in faces),[]))+1
    a,b,c=faces[i]
    return faces[:i]+faces[i+1:]+[(a,b,n),(b,c,n),(c,a,n)]

def main():
    base=[(0,1,2),(0,3,1),(1,3,2),(0,2,3)]
    octa=[(0,2+j,2+(j+1)%4) for j in range(4)]
    octa +=[(1,2+(j+1)%4,2+j) for j in range(4)]
    spheres=[('tetrahedron',base),('one_stellar',stellar(base,0)),
             ('two_stellar',stellar(stellar(base,0),0)),('octahedron',octa)]
    records=[];found=[]
    for name,faces in spheres:
        matchings=sphere_link_check(faces)
        for match in matchings:
            qs=[quartet(faces[i],faces[j]) for i,j in match]
            for anchor in range(len(qs)):
                p=exterior(qs,anchor)
                defects=newton_defects(p)
                if defects:
                    found.append({'sphere':name,'faces':faces,'matching':match,'quartets':qs,
                                  'anchor':anchor,'coefficients':p,'newton_defects':defects})
                # Root calculation is only a locator when Newton is inconclusive.
                try:
                    import numpy as np
                    vals=np.array([numeric(v) for v in p]);nz=np.flatnonzero(vals)
                    roots=np.roots(vals[nz[0]:nz[-1]+1][::-1])
                    nonreal=bool(max(abs(roots.imag),default=0)>1e-6)
                except Exception:nonreal=None
                records.append({'sphere':name,'matching':match,'anchor':anchor,
                                'coefficients':p,'newton_defect':bool(defects),
                                'located_nonreal_roots':nonreal})
        print(name,len(records),len(found),flush=True)
    data={'local_coefficients':len(PC),'records':records,'exact_defects':found}
    Path('/private/tmp/md-even-coherent-exterior-check-results.json').write_text(json.dumps(data,indent=2)+'\n')
    print('exact defects',len(found),'numeric nonreal',sum(r['located_nonreal_roots'] is True for r in records))
if __name__=='__main__':main()
