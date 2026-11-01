"""Certify a fixed deprotection of the original 17-region source cover.

Only finite exact source incidence and outward interval rate inequalities
are checked. The all-chain source theorem, conditional disk geometry and
full invariant/metric transfer are separate written proofs.
"""
if not __debug__:
    raise SystemExit("Run without -O or PYTHONOPTIMIZE: certificate checks require assertions.")

from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import argparse, hashlib, itertools, json, sys
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=ROOT)
    ap.add_argument('--chain-length',type=int,default=2**20)
    ap.add_argument('--terms',type=int,default=2048)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/triangular-boundary', help='Directory for fresh finite certificate records.')
    ap.add_argument('--anchor-terms',type=int,default=8192)
    args=ap.parse_args(); n=args.chain_length; K=args.terms
    args.repo=args.repo.resolve()
    args.output.mkdir(parents=True,exist_ok=True)
    summary_path=args.output/'summary.json'
    summary_path.unlink(missing_ok=True)
    assert n>0 and n%2==0 and K>=1 and args.anchor_terms>=1
    ctx.prec=192
    cp=args.repo/'experiments/actual_sector_cover_certificate.json'
    d=json.loads(cp.read_text()); ports=d['ports']; R=len(ports)
    zero=set(d['protected']); ordinary=d['ordinary']; bad=d['bad_ports']
    assert zero=={0,16} and R==17 and ports[15]==[16,14,0,17]
    sys.path.insert(0,str(args.repo/'experiments'))
    from audit_actual_original_marked_face_coefficient import morse_faces
    from audit_actual_shared_radius_anchor_obstruction import verify as verify_anchor
    sys.path.insert(0,str(args.repo/'repro'))
    from check_protected_sums import check_sphere
    chart=morse_faces(d['k'],d['word'],d['mark'])
    assert chart['circles']==list(map(tuple,ports))
    assert (0,chart['v'])==tuple(d['protected'])
    assert ordinary==[f for f in range(chart['faces']) if f not in zero]
    tris=[t for x,b,c,y in ports for t in ((x,b,y),(x,c,y))]
    assert all(len(set(t))==3 for t in tris)
    assert len({tuple(sorted(t)) for t in tris})==2*R
    edges=Counter(tuple(sorted((t[j],t[(j+1)%3]))) for t in tris for j in range(3))
    assert len(edges)==3*R and set(edges.values())=={2}
    vals=[F(*v['value']) for v in d['complete_variables']]
    assert min(vals)>=0
    assert {(r['port'],r['side']) for r in d['triangle_rows']}==set(itertools.product(range(R),range(2)))
    assert sorted(i for r in d['triangle_rows'] for i in r['variables'])==list(range(len(vals)))
    loads={f:F(0) for f in ordinary}
    for row in d['triangle_rows']:
        e=row['port']; fs=[f for f in (ports[e][0],ports[e][1+row['side']],ports[e][3]) if f not in zero]
        assert fs==row['faces'] and len(fs)==len(row['variables'])
        assert sum((vals[i] for i in row['variables']),F(0))==F(1,2)
        for f,i in zip(fs,row['variables']):
            assert d['complete_variables'][i]['name']==[e,row['side'],f]
            loads[f]+=vals[i]
    assert all(v==1 for v in loads.values())
    expected=[]
    for mask in itertools.product([False,True],repeat=len(bad)):
        if any(mask):
            tags=['H']*R
            for e,on in zip(bad,mask): tags[e]='R' if on else '!R'
            expected.append(tags)
    for e,(x,b,c,y) in enumerate(ports):
        for tag,f in [('L',c),('R',b)]:
            if f in zero or (e in bad and tag=='R'): continue
            tags=['H']*R
            for j in bad: tags[j]='!R'
            tags[e]=tag; expected.append(tags)
    assert [b['tags'] for b in d['branches']]==expected and len(expected)==40
    new_anchors=[(e,tag,f) for e,(x,b,c,y) in enumerate(ports)
                 for tag,f in [('L',c),('R',b)] if f in zero]
    assert new_anchors==[(0,'R',0),(1,'R',0),(12,'L',16),(15,'L',0),(16,'L',0)]


    # These finite incidence checks supplement the all-length oriented proof.
    # The two boundary faces are removed and only the actual retained partners
    # are rematched. No quantum contraction or knot-component test is inferred.
    def cyc(t): return min(t[i:]+t[:i] for i in range(3))
    def qtri(q):
        x,b,c,y=q
        return [(x,b,y),(x,y,c)]
    def ordered_pair(t1,t2):
        shared=set(t1)&set(t2)
        assert len(shared)==2
        j=next(j for j in range(3) if {t1[j],t1[(j+1)%3]}==shared)
        y,x=t1[j],t1[(j+1)%3]
        b=t1[(j+2)%3]; c=next(z for z in t2 if z not in shared)
        q=(x,b,c,y)
        assert [cyc(t) for t in qtri(q)]==[cyc(t1),cyc(t2)]
        return q
    def oriented(regions,protected):
        counts=check_sphere(regions,protected)
        ee={}
        for q in regions:
            for t in qtri(q):
                for j in range(3):
                    e=(t[j],t[(j+1)%3]); ee.setdefault(tuple(sorted(e)),[]).append(e)
        assert all(len(es)==2 and es[0]==tuple(reversed(es[1])) for es in ee.values())
        return counts
    def core(k):
        P,S=0,1; rim=[2,3,4,5]; protected={2,3}
        T=[(P,rim[(j+1)%4],rim[j]) for j in range(4)]
        Z=[(S,rim[j],rim[(j+1)%4]) for j in range(4)]
        u,v,b0,c=4,0,5,1
        bs=[b0]+list(range(6,6+k))
        A={j:(u,bs[j],bs[j-1]) for j in range(1,k+1)}
        B={j:(v,bs[j-1],bs[j]) for j in range(1,k+1)}
        F=(u,v,bs[k])
        actual_faces=T[:2]+T[3:]+Z+[A[j] for j in A]+[B[j] for j in B]+[F]
        regions=[ordered_pair(T[0],T[1]),ordered_pair(Z[0],Z[1]),ordered_pair(T[3],Z[3]),
                 (u,bs[1],c,b0)]
        for j in range(1,k):
            regions.append(ordered_pair(B[j],B[j+1]) if j%2 else ordered_pair(A[j+1],A[j]))
        tip=len(regions); regions.append((u,v,bs[k-1],bs[k]))
        assert len(regions)==4+k
        assert Counter(cyc(t) for q in regions for t in qtri(q))==Counter(cyc(t) for t in actual_faces)
        counts=oriented(regions,protected)
        assert counts['vertices']==6+k and counts['regions']==4+k
        return regions,protected,tip,counts
    topology=[]
    for k in (2,4,8,16):
        cc,protected,tip,ccount=core(k)
        u,v,c,b=cc[tip]; fresh=1+max(z for q in cc for z in q)
        vm={16:u,0:v,17:b}
        for z in range(R+2):
            if z not in vm: vm[z]=fresh;fresh+=1
        mapped=[tuple(vm[z] for z in q) for q in ports]
        assert mapped[15]==(u,vm[14],v,b)
        before=Counter(cyc(t) for q in cc for t in qtri(q))
        before.update(cyc(t) for q in mapped for t in qtri(q))
        before.subtract([cyc((u,v,b)),cyc((u,b,v))])
        assembled=list(cc);assembled[tip]=(u,vm[14],c,b)
        locations={}
        for e,q in enumerate(mapped):
            if e!=15:locations[e]=len(assembled);assembled.append(q)
        after=Counter(cyc(t) for q in assembled for t in qtri(q))
        assert +before==after
        acount=oriented(assembled,protected)
        assert acount['regions']==ccount['regions']+R-1
        assert all(assembled[locations[e]]==mapped[e] for e in (2,4,7,12))
        core_ordinary=set(z for q in cc for z in q)-protected
        target=Counter({z:1 for z in core_ordinary})
        target.update(vm[z] for z in ordinary);target[b]-=1
        assert set(target)==set(z for q in assembled for z in q)-protected
        assert set(target.values())=={1}
        topology.append({'chain_length':k,'core':ccount,'with_17_region_block':acount,
                         'marked_edge':sorted(protected),'retained_failure_regions':[2,4,7,12],
                         'final_ordered_quartets':assembled})
    anchor_path=args.repo/'experiments/actual_shared_radius_anchor_obstruction_certificate.json'
    anchor_data=json.loads(anchor_path.read_text())
    assert anchor_data['ports']==ports and anchor_data['protected']==[0,16]
    assert anchor_data['anchor']==12 and set(anchor_data['spectator_mixed_ports'])=={2,4,7}
    assert all(not(set(row['faces']) & zero) for row in anchor_data['triangles'])
    anchor_result=verify_anchor(anchor_data,M=args.anchor_terms)
    anchor_result.pop('status',None)
    anchor_result['deprotection_scope']='The same rational allocation has zero boundary loads. Its restricted bound with mixed spectators only 2,4,7 remains valid when faces0,16 are positive but have no block targets.'

    def ab(f): return arb(f.numerator)/f.denominator
    pi=arb.pi()
    def lob(x):
        s=arb(0)
        for k in range(1,K+1): s+=(2*k*x).sin()/(2*k*k)
        return s+arb(0,arb(1)/(2*K))
    ec={}
    def ent(a):
        if a in (F(0),F(1,2)): return arb(0)
        a=min(a,F(1,2)-a)
        if a not in ec: ec[a]=(lob(pi*ab(a))+lob(pi*ab(F(1,2)-a)))/pi
        return ec[a]
    lower=sum((ent(a) for a in vals),arb(0))
    def maxb(xs):
        lo=max(x.lower() for x in xs); hi=max(x.upper() for x in xs)
        return (arb(lo)+arb(hi))/2+arb(0,(arb(hi)-arb(lo))/2)
    def Qw(w):
        pos=[v for v in w if not v.is_zero()]
        if len(pos)==1: return pos[0].log()/2
        D=(w[0]*w[1]+w[1]*w[2]+w[2]*w[0]).sqrt(); ans=arb(0)
        for v in pos:
            t=(v/D).atan()
            ans+=(lob(t)+lob(pi/2-t))/pi+(t/pi)*v.log()
        return ans
    bn=3*arb(n)**2+4*arb(2).sqrt()*n+2
    boundary={16:2/bn,0:1/bn}
    assert all(w>0 for w in boundary.values())
    def witness(branch):
        rat={int(f):F(*v) for f,v in branch['radii'].items()}
        scale=rat[17]; L={f:ab(v/scale) for f,v in rat.items()}
        L.update(boundary)
        assert L[17]==1 and set(L)==set(range(R+2)) and all(w>0 for w in L.values())
        return L
    def rates(L):
        qc={}
        def Q(t):
            key=tuple(sorted(t))
            if key not in qc: qc[key]=Qw([L[f] for f in t])
            return qc[key]
        out=[]
        for x,b,c,y in ports:
            qb=Q((x,b,y)); qcc=Q((x,c,y)); X=qb+qcc
            out.append({'H':maxb([X,L[b].log(),L[c].log()]),
                        '!R':maxb([X,L[c].log()]),
                        'L':maxb([L[c].log(),qb+L[c].log()/2]),
                        'R':maxb([L[b].log(),qcc+L[b].log()/2])})
        return out
    def cost(tags,L,rr):
        return sum((row[tag] for row,tag in zip(rr,tags)),arb(0))-sum((L[f].log() for f in ordinary),arb(0))
    def it(v): return {'lower':str(v.lower()),'upper':str(v.upper())}
    results=[]; fixedL=None; fixedr=None
    for i,br in enumerate(d['branches']):
        L=witness(br); rr=rates(L); value=cost(br['tags'],L,rr); gap=lower-value
        assert gap>arb('0.02'),('old-branch',i,gap)
        results.append({'kind':'old-branch','index':i,'rate':it(value),'gap':it(gap),'root_a_minus_v':it(L[14]-L[0])})
        if i==0: fixedL,fixedr=L,rr
    for e,tag,f in new_anchors:
        tags=['H']*R;tags[e]=tag
        value=cost(tags,fixedL,fixedr);gap=lower-value
        assert gap>arb('0.02'),('new-anchor',e,tag,gap)
        results.append({'kind':'new-anchor','region':e,'side':tag,'overload':f,'rate':it(value),'gap':it(gap),'root_a_minus_v':it(fixedL[14]-fixedL[0])})
    delta=2*Qw([boundary[16],boundary[0],arb(1)])
    assert delta<arb('0.025'),delta
    # Uniform complete-vector core certificate: mixed branch margins, as well
    # as the three pure-middle margins in the written all-chain proof.
    g=ent(F(1,4)); b1=5+4*arb(2).sqrt(); b2=14+8*arb(2).sqrt()
    core={
      'protected_pure':2*g-arb(3)/4*arb(2).log(),
      'root_pure':2*ent(F(1,12))+ent(F(1,3))+2*ent(F(1,5))+ent(F(1,10))+arb(17)/30*arb(2).log()-arb(2)/3*b1.log(),
      'internal_pure':4*g-(b2**3/(2*b1*b1)).log()/4,
      'protected_mixed':2*g-arb(2).log()/4,
      'root_large_middle_mixed':2*g+(2/b1).log()/4,
      'internal_large_middle_mixed':2*g-(b2/b1).log()/4,
      'small_middle_vertex':arb(2).log()/2,
      'quarter_quarter':2*g,
    }
    assert all(v>arb('0.06') for v in core.values()),core
    result={
      'scope':'Finite 17-region deprotected source cover, restricted dual obstruction, and the listed oriented attachment checks. Forty old branches plus five new overload anchors cover every locally allowed noncentral string. The all-length construction, conditional disk geometry, asymptotic source estimates, knot-component choice and metric-volume transfer remain written proofs. No optimizer or invariant samples are used.',
      'finite_topology_checks':topology,'restricted_dual':anchor_result,
      'extension_to_larger_even_lengths':'Each fixed-witness rate is nondecreasing in the boundary weights and the block has no targets there. Since 2/b_n and 1/b_n decrease with n, all certified branch upper rates and Delta only decrease at larger even n. This is a written monotonicity argument, not a sweep over chain lengths.',
      'dependencies':'python-flint; NumPy through the original Morse source helper; repository helpers and certificates listed in source_sha256.',
      'chain_length':n,'boundary':{str(f):it(v) for f,v in boundary.items()},
      'counts':{'regions':R,'old_branches':40,'new_anchors':5,'total_branches':len(results),'complete_flow_variables':len(vals)},
      'precision_bits':ctx.prec,'fourier_terms':K,'lobachevsky_tail_radius':'1/(2K)',
      'complete_entropy_lower':it(lower),'certified_block_gap':'0.02',
      'Delta':it(delta),'Delta_upper_bound':'0.025',
      'Delta_nonnegativity':'The exact correction is nonnegative by the vertex allocation; the displayed finite Fourier enclosure can have a negative lower endpoint.',
      'uniform_zigzag_core_gap':'0.06','core_margins':{k:it(v) for k,v in core.items()},
      'bridge_defect':'At most Delta/2 in noncentral blocks, absorbed by the subtraction -Delta. A wholly central block uses its conditional packing and has zero bridge defect.',
      'assembled_source_gap_lower_bound':'0.02, including any fixed finite number of these attachments to the stated strictly balanced cores',
      'weak_balance_persistence':'Delta<0.025; uses the separately certified old restricted dual with zero boundary loads',
      'branches':results,'source_sha256':{str(p.relative_to(args.repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [cp,anchor_path,args.repo/'experiments/audit_actual_original_marked_face_coefficient.py',args.repo/'experiments/audit_actual_shared_radius_anchor_obstruction.py',args.repo/'repro/check_protected_sums.py']},
    }
    result['source_sha256']['repro/check_triangular_boundary_certificate.py']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    summary_path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in {'branches','core_margins','finite_topology_checks'}},indent=2))

if __name__=='__main__':main()
