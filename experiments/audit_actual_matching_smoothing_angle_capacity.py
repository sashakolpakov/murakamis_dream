#!/usr/bin/env python3
"""Literal Morse smoothing, Hall cuts, entropy transfers and degenerate factors.

Incidence/entropy samples test the finite certificate; they do not establish
that every geometric matching-edge deletion satisfies it.
"""
import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.optimize import linprog, root
from scipy.integrate import quad
from audit_actual_original_marked_face_coefficient import morse_faces
from audit_actual_positive_face_channel_rate import matrix, forced, sine_factorials


def source_incidence():
    counts={'literal_deleted_box_identifications':0,'Hall_LP_comparisons':0,
            'feasible_Hall_systems':0,'infeasible_Hall_systems':0,'exact_cut_inequalities':0}
    for k in (2,3):
        odd=list(range(1,2*k-2,2));even=list(range(0,2*k-1,2))
        for word in (odd+even+odd,odd+even+odd+even+odd):
            for mark in range(k):
                old=morse_faces(k,word,mark)
                for deleted,(x,b,c,y) in enumerate(old['circles']):
                    shorter=word[:deleted]+word[deleted+1:]
                    if not all(j in shorter for j in odd):continue
                    new=morse_faces(k,shorter,mark)
                    parent={f:f for f in range(old['faces'])};parent[c]=b
                    def rep(f):
                        while parent[f]!=f:f=parent[f]
                        return f
                    mapping={}
                    def identify(f,g):
                        f=rep(f)
                        if f in mapping:assert mapping[f]==g
                        else:mapping[f]=g
                    remain=[t for j,t in enumerate(old['circles']) if j!=deleted]
                    for before,after in zip(remain,new['circles']):
                        for f,g in zip(before,after):identify(f,g)
                    for a,z in zip(old['bottom'],new['bottom']):identify(a,z)
                    for a,z in zip(old['top'],new['top']):identify(a,z)
                    assert len(set(mapping.values()))==len(mapping)==new['faces']
                    assert mapping[rep(0)]==0 and mapping[rep(old['v'])]==new['v']
                    counts['literal_deleted_box_identifications']+=1
                    marked={0,old['v']}
                    if b==c or b in marked or c in marked:continue
                    tri=[(a,m,z) for a,bb,cc,z in remain for m in (bb,cc)]
                    faces=sorted(set(f for t in tri for f in t)-marked)
                    if b not in faces or c not in faces:continue
                    corners=[(t,j) for t,row in enumerate(tri) for j,f in enumerate(row) if f not in marked]
                    for slack in (Fraction(0),Fraction(1,50)):
                        demand={f:Fraction(1 if f in (b,c) else 2) for f in faces}
                        supply=[Fraction(1) for _ in tri]
                        for t,j in corners:supply[t]-=slack;demand[tri[t][j]]-=slack
                        hall=min(supply)>=0 and min(demand.values())>=0 and sum(supply)==sum(demand.values())
                        for flags in itertools.product((False,True),repeat=len(faces)):
                            subset={f for f,on in zip(faces,flags) if on}
                            left=sum(demand[f] for f in subset)
                            right=sum(supply[t] for t,row in enumerate(tri) if subset.intersection(row))
                            hall=hall and left<=right;counts['exact_cut_inequalities']+=1
                        A=np.zeros((len(tri)+len(faces),len(corners)))
                        rhs=np.array([float(r) for r in supply]+[float(demand[f]) for f in faces])
                        for col,(t,j) in enumerate(corners):
                            A[t,col]=1;A[len(tri)+faces.index(tri[t][j]),col]=1
                        lp=linprog(np.zeros(len(corners)),A_eq=A,b_eq=rhs,bounds=(0,None),method='highs')
                        assert bool(lp.success)==bool(hall),(k,word,deleted,slack,hall,lp.message)
                        counts['Hall_LP_comparisons']+=1
                        counts['feasible_Hall_systems' if hall else 'infeasible_Hall_systems']+=1
    return counts


def entropy_flow():
    rows=[];maximum_divergence_error=0.;minimum_Taylor_margin=float('inf')
    # Actual simplicial bipyramid incidences; vertex splitting supplies a
    # combinatorial original incidence for the test, not a new RA certificate.
    for n in (4,5,6,7,8):
        tri=[(p,j,(j+1)%n) for p in (n,n+1) for j in range(n)]
        marked={n,0};free=[f for f in range(n+2) if f not in marked];variables=free[:-1]
        def angles(z):
            l={f:0. for f in marked};l[free[-1]]=1.;l.update({f:np.exp(w) for f,w in zip(variables,z)})
            aa=[]
            for t in tri:
                a=np.array([l[f] for f in t]);delta=np.sqrt(a[0]*a[1]+a[1]*a[2]+a[2]*a[0])
                aa.append(2*np.arctan2(a,delta))
            return l,np.array(aa)
        def grad(z):
            l,aa=angles(z);s={f:0. for f in free}
            for t,row in zip(tri,aa):
                for f,a in zip(t,row):
                    if f in s:s[f]+=a
            return [s[f]-2*np.pi for f in variables]
        sol=root(grad,np.zeros(len(variables)),tol=1e-11);assert np.linalg.norm(grad(sol.x))<1e-9
        l,aa=angles(sol.x)
        splits=[n//2] if n%2==0 else [n//2,n//2+1]
        for split in splits:
            b,c,x,y=n+1,n+2,split,0
            oldtri=[tuple((b if t[1]<split else c) if f==n+1 else f for f in t) for t in tri]
            delta=sum(aa[i,k] for i,t in enumerate(oldtri) for k,f in enumerate(t) if f==b)-np.pi
            active=[(i,k) for i,row in enumerate(aa) for k,a in enumerate(row) if 1e-9<a<np.pi-1e-9]
            sigma=min(min(aa[i,k],np.pi-aa[i,k]) for i,k in active)
            faces=sorted(set(f for t in oldtri for f in t)-marked)
            A=np.zeros((len(tri)+len(faces),len(active)))
            for col,(i,k) in enumerate(active):A[i,col]=1;A[len(tri)+faces.index(oldtri[i][k]),col]=1
            def direction(items):
                rhs=np.zeros(A.shape[0])
                for f,v in items.items():rhs[len(tri)+faces.index(f)]=v
                result=np.linalg.lstsq(A,rhs,rcond=None)[0]
                assert np.linalg.norm(A@result-rhs)<1e-10
                return result
            db=direction({c:1,b:-1});dx=direction({b:1,c:1,x:-2})
            successful=[]
            for eta in np.geomspace(.0001,.5,90):
                v=delta*db+eta*dx
                if max(abs(v))>sigma/2:continue
                added=4*quad(lambda u:-np.log(np.tan(u/2)),0,eta,epsabs=1e-12)[0]
                linear=2*eta*np.log(l[x]/l[n+1]);penalty=np.dot(v,v)/(2*np.sin(sigma/2))
                G=added+linear-penalty
                if G>0:successful.append((G,eta,v,added,linear,penalty))
            assert successful,(n,split,delta)
            G,eta,v,added,linear,penalty=max(successful,key=lambda item:item[0])
            changed=aa.copy()
            for (i,k),z in zip(active,v):changed[i,k]+=z
            sums={f:0. for f in faces}
            for t,row in zip(oldtri,changed):
                for f,a in zip(t,row):
                    if f in sums:sums[f]+=a
            for t in ((x,b,y),(x,c,y)):
                for f,a in zip(t,(eta,np.pi-eta,0.)):
                    if f in sums:sums[f]+=a
            err=max(abs(sums[f]-2*np.pi) for f in faces)
            maximum_divergence_error=max(maximum_divergence_error,err);assert err<1e-9
            # Integrate the independent exact entropy gradient along each
            # changed corner instead of evaluating the tested Taylor formula.
            change=sum(quad(lambda u:-np.log(np.tan(u/2)),aa[i,k],changed[i,k],epsabs=1e-12)[0] for i,k in active)
            margin=change-linear+penalty;assert margin>-1e-9
            minimum_Taylor_margin=min(minimum_Taylor_margin,margin)
            assert change+added>=G-1e-9
            rows.append({'bipyramid_equator':n,'split':split,'imbalance':float(delta),'sigma':float(sigma),
                         'eta':float(eta),'certified_entropy_gap':float(G),'direct_entropy_gain':float(change+added)})
    return {'finite_flow_entropy_checks':len(rows),'nonzero_imbalances':sum(abs(r['imbalance'])>1e-6 for r in rows),
            'maximum_face_balance_error':maximum_divergence_error,'minimum_Taylor_remainder_margin':minimum_Taylor_margin,
            'samples':rows,'scope':'Combinatorial bipyramid/split incidences and the finite entropy certificate only; no new labeled RA source certificate or family-wide smoothing theorem.'}


def degenerate_circles():
    count=0;worst=mp.mpf(0)
    for N in range(3,15):
        d=N-1;S=sine_factorials(N)
        for a in range(d//2+1):
            beta=S[2*a]/S[a]**2
            for x,b,c,y in ((mp.mpf('1.3'),0,0,0),(0,0,0,mp.mpf('1.7')),(0,mp.mpf('.8'),mp.mpf('1.4'),0),(0,0,mp.mpf('1.4'),0),(0,mp.mpf('.8'),0,0)):
                D1=mp.det(matrix(N,a,x,b,y)) if a else mp.mpf(1)
                D2=mp.det(matrix(N,a,x,c,y)) if a else mp.mpf(1)
                actual=beta**2*D1*D2*forced(N,a,x,y)
                expected=(x+y)**d if x+y else ((b*c)**a if 2*a==d else mp.mpf(0))
                error=abs(actual-expected)/max(1,abs(expected));worst=max(worst,error)
                assert error<mp.mpf('1e-60');count+=1
    return {'actual_degenerate_all_label_factors':count,'maximum_relative_error':str(worst)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_matching_smoothing_angle_capacity_results.json');args=ap.parse_args()
    mp.mp.dps=75
    result={'status':'PASS','precision_digits_source_factors':75,'incidence':source_incidence(),'entropy':entropy_flow(),'degenerate_source':degenerate_circles(),
            'scope':'Finite literal Morse identifications, exact rational Hall cuts versus independent LP, positive and imbalanced angle-flow certificates, and actual original degenerate channel matrices. No general geometric smoothing gap, h>1 source transport, or filled-volume claim.'}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
