"""Saved-box compatibility only; no source imports, roots, or subdivisions."""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import gzip,hashlib,json,time

ROOT=Path('/Users/sasha/volume-conjecture')
IP=ROOT/'repro/results/research-mixed-cyclic-block-images.json.gz'
SP=ROOT/'repro/results/research-mixed-cyclic-block-localization.json'
EP=ROOT/'repro/results/research-mixed-open-word-critical-localization.json'
data=json.loads(gzip.decompress(IP.read_bytes()));src=json.loads(SP.read_text());ep=json.loads(EP.read_text())
assert data['status']==src['status']==ep['status']=='passed'
assert data['author_record_sha256']==hashlib.sha256(SP.read_bytes()).hexdigest()
centers=[(F('.35'),F('-.01')),(F('.30'),F('-.052'))];radii=[F('.09'),F('.064')]
small=[F('.083'),F('.060')]
other=[[(F('.267'),F('.433')),(F('-.072'),F('.068'))],
       [(F('.24'),F('.36')),(F('-.108'),F('-.001'))]]
attached=[(F('.246'),F('.350')),(F('-.108'),F('-.020'))]
threshold=F('-.07')

def intersection(a,b):
    z=[(max(x[0],y[0]),min(x[1],y[1])) for x,y in zip(a,b)]
    return None if any(x>y for x,y in z) else z

def outside_disk(box,center,radius):
    return sum(0 if a<=c<=b else min((a-c)**2,(b-c)**2)
               for (a,b),c in zip(box,center))>radius**2

def bins(box):
    for i in range(int(box[0][0]//F('.01')),int(box[0][1]//F('.01'))+1):
        for j in range(int(box[1][0]//F('.01')),int(box[1][1]//F('.01'))+1):
            yield (i,j)

endpoints={};indices={}
for domain in ep['domains']:
    if domain['epsilon']!=1:continue
    typ=domain['neighbor_epsilon'];stack=[[(-F(1),F(1)),(-F(1),F(1))]]
    leaves=[];index=defaultdict(list);allcount=0
    for number,node in enumerate(domain['tree']):
        box=stack.pop()
        if node[0]=='S':
            axis=node[1];a,b=box[axis];mid=(a+b)/2
            for iv in ((a,mid),(mid,b)):
                ch=box.copy();ch[axis]=iv;stack.append(ch)
        elif node[0]=='X':
            assert outside_disk(box,(F(0),F(0)),F(1))
        else:
            assert node[0]=='L';allcount+=1;w=node[1]
            c=list(map(F,w['centers'][1]));rad=F(w['radius'])
            out=[(x-rad,x+rad) for x in c]
            if out[1][0]>threshold:continue
            inp=[(centers[typ][j]+radii[typ]*box[j][0],
                  centers[typ][j]+radii[typ]*box[j][1]) for j in range(2)]
            inp=intersection(inp,other[typ])
            if inp is None or outside_disk(inp,centers[typ],small[typ]):continue
            if typ==1:
                inp=intersection(inp,[(F('.259'),F(1)),(F(-1),F(1))])
                if inp is None:continue
            out=intersection(out,attached)
            if out is None:continue
            out[1]=(out[1][0],min(out[1][1],threshold))
            item=dict(node=number,inp=inp,out=out,center=c,radius=rad)
            ix=len(leaves);leaves.append(item)
            for key in bins(out):index[key].append(ix)
    assert not stack and allcount==domain['leaves']
    endpoints[typ]=leaves;indices[typ]=index

result=dict(arithmetic='Exact Fraction compatibility of old full-dimensional boxes',
            threshold=str(threshold),cases=[],
            inputs={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (IP,SP,EP)})
start=time.time()
for image,source in zip(data['cases'],src['cases']):
    case=image['types'];assert case==source['types']
    assert [r[0] for r in image['rows']]==source['accepted']
    if case[2]!=1:continue
    own,third,_=case;leaves=endpoints[own];index=indices[own]
    compatible=0;tested=0;low=None;worst=None;nodes=set()
    for address,zz,DD,RR in image['rows']:
        lo=[F(-1)]*4;hi=[F(1)]*4
        for depth,bit in enumerate(address):
            j=depth%4;mid=(lo[j]+hi[j])/2
            if bit=='0':hi[j]=mid
            else:assert bit=='1';lo[j]=mid
        types=case[1:]
        old=[(centers[types[k//2]][k%2]+radii[types[k//2]]*lo[k],
              centers[types[k//2]][k%2]+radii[types[k//2]]*hi[k]) for k in range(4)]
        cut=intersection(old,other[third]+attached)
        if cut is None:continue
        if outside_disk(cut[:2],centers[third],small[third]) or outside_disk(cut[2:],centers[1],small[1]):continue
        if third==0:
            if cut[0][0]-3*cut[1][1]>F('.608'):continue
            cut[0]=(cut[0][0],min(cut[0][1],F('.608')+3*cut[1][1]))
            cut[1]=(max(cut[1][0],(cut[0][0]-F('.608'))/3),cut[1][1])
        possible=set(i for key in bins(cut[2:]) for i in index.get(key,()))
        if not possible:continue
        coeff=[[F(DD[1][j][0]),F(DD[1][j][1])] for j in range(2)]
        mid=[(a+b)/2 for a,b in old];zc=list(map(F,zz[1]));rem=F(RR[1])
        for ix in possible:
            en=leaves[ix];ab=intersection(cut[2:],en['out'])
            if ab is None or outside_disk(ab,en['center'],en['radius']):continue
            tested+=1;bounds=cut[:2]+ab;delta=[(a-m,b-m) for (a,b),m in zip(bounds,mid)]
            out=[]
            for coord in range(2):
                lower=upper=zc[coord]
                for j,(re,im) in enumerate(coeff):
                    for k,v in enumerate((re,-im) if coord==0 else (im,re)):
                        a,b=delta[2*j+k];lower+=min(v*a,v*b);upper+=max(v*a,v*b)
                out.append((lower-rem,upper+rem))
            bi=intersection(out,en['inp'])
            if bi is None or outside_disk(bi,centers[own],small[own]):continue
            compatible+=1;nodes.add(en['node'])
            if low is None or ab[1][0]<low:
                low=ab[1][0];worst=dict(endpoint_node=en['node'],ordinary_address=address,
                       endpoint_a=[[str(x),str(y)] for x,y in ab],
                       external_b=[[str(x),str(y)] for x,y in bi])
    q=dict(types=case,candidate_endpoint_leaves=len(leaves),tested_pairs=tested,
           compatible_pairs=compatible,compatible_endpoint_nodes=len(nodes),
           exact_lower=str(min(threshold,low)) if low is not None else str(threshold),
           decimal_lower=float(min(threshold,low)) if low is not None else float(threshold),
           worst=worst)
    result['cases'].append(q);print(json.dumps(q),flush=True)
result['elapsed_seconds']=time.time()-start
Path('/tmp/adjacent_four_saved_compatibility.json').write_text(json.dumps(result,indent=2)+'\n')
