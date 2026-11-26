#!/usr/bin/env python3
"""Independent factorized replay of the upper-row endpoint certificate."""
import argparse
import hashlib
import json
import time
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_high_row_endpoint_reduction.md'
AUTHOR = ROOT/'experiments/certify_mixed_high_row_endpoint_reduction.py'
SOURCE = ROOT/'repro/results/research-mixed-high-row-endpoint-reduction.json'
DOMAIN = (F(13,100), F(1,2), F(0), F(57,1000), F(0), F(1))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def ar(x):
    return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)

def interval(a,b):
    return ar(a).union(ar(b))

def cover(addresses):
    """Check the full binary tree, independently of the author's mass test."""
    assert addresses and len(set(addresses)) == len(addresses)
    tree = {}
    for address in addresses:
        assert set(address) <= {'0','1'}
        node = tree
        for bit in address:
            assert 'leaf' not in node
            node = node.setdefault(bit,{})
        assert not node
        node['leaf'] = True
    def visit(node):
        if 'leaf' in node:
            assert node == {'leaf':True}
            return 1
        assert set(node) == {'0','1'}
        return visit(node['0'])+visit(node['1'])
    assert visit(tree) == len(addresses)
    return True

def box_at(address):
    box = list(DOMAIN)
    for depth,bit in enumerate(address):
        k=2*(depth%3)
        middle=(box[k]+box[k+1])/2
        box[k+1 if bit=='0' else k]=middle
    return box

def criterion(box,eps):
    y=interval(*box[:2]); H=interval(*box[2:4]); w=interval(*box[4:])
    pi=arb.pi()
    sy=(pi*y).sin(); cy=(pi*y).cos()
    t=w*cy/sy
    # This is the positive-square representation; no expanded author coefficients.
    A=4*(pi*H).sinh()**2
    z=sy*t-cy
    P=A*(1+t**2)+4*z**2
    Pprime=2*A*t+8*sy*z
    Q=t**2*P*(1+t**2)**eps
    threshold=2**(2+2*eps)*(-2*pi*H).exp()
    if Q < threshold:
        return 0
    direct=P+t*Pprime/2
    if eps:
        direct=direct*(1+t**2)+t**2*P
    if direct > 0:
        return 1
    return None

def identities():
    t,s,c,A=sp.symbols('t s c A',real=True)
    P=A*(1+t*t)+4*(s*t-c)**2
    results=[]
    for eps in (0,1):
        Q=t*t*P*(1+t*t)**eps
        B=(P+t*sp.diff(P,t)/2)*(1+t*t)**eps
        if eps:
            B+=t*t*P
        assert sp.expand(sp.diff(Q,t)-2*t*B)==0
        results.append(f'direct positive-square derivative epsilon={eps}')
    K=sp.symbols('K',real=True)
    expanded=(2*K-2*(c*c-s*s))*t*t-8*s*c*t+2*K+2*(c*c-s*s)
    factored=P.subs(A,2*K-2)
    assert sp.expand(expanded-factored-2*(1-s*s-c*c)*(1+t*t))==0
    results.append('positive-square and trigonometric polynomial identity')
    return results

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=320)
    parser.add_argument('--input',type=Path,default=SOURCE)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-high-row-endpoint-reduction-replay.json')
    args=parser.parse_args()
    assert args.precision>=192
    ctx.prec=args.precision
    start=time.time()
    source_hash=sha(args.input)
    data=json.loads(args.input.read_text())
    assert data['status']=='passed'
    assert data['script_sha256']==sha(AUTHOR)
    assert data['proof_sha256']==sha(PROOF)
    assert data['domain']=={'y':['13/100','1/2'],'absolute_height':['0','57/1000'],'w':['0','1'],'upper_rows':['1/2','1']}
    dependencies={str(AUTHOR.relative_to(ROOT)):sha(AUTHOR),str(PROOF.relative_to(ROOT)):sha(PROOF)}
    for path,digest in data['dependencies'].items():
        assert sha(ROOT/path)==digest,path
        dependencies[path]=digest
    selfhash=sha(__file__)
    assert len(data['cases'])==2 and {c['epsilon'] for c in data['cases']}=={0,1}
    exact=identities()
    total=0; refinements=0; records=[]
    for case in sorted(data['cases'],key=lambda c:c['epsilon']):
        eps=case['epsilon']; addresses=case['addresses']
        cover(addresses)
        assert case['accepted_cells']==len(addresses)
        counts=[0,0]; refined=0
        for address in addresses:
            stack=[(address,box_at(address))]
            leaves=[]
            while stack:
                current,box=stack.pop()
                check=criterion(box,eps)
                if check is not None:
                    counts[check]+=1
                    leaves.append(current[len(address):])
                    continue
                assert len(current)<48,(eps,current)
                k=2*(len(current)%3)
                midpoint=(box[k]+box[k+1])/2
                left,right=box[:],box[:]
                left[k+1]=midpoint; right[k]=midpoint
                stack.extend(((current+'1',right),(current+'0',left)))
                refined+=1
            cover(leaves)
        row={'epsilon':eps,'original_cells':len(addresses),'replay_cells':sum(counts),
             'refinements':refined,'below_threshold_cells':counts[0],'positive_derivative_cells':counts[1]}
        records.append(row); total+=sum(counts); refinements+=refined
        print(json.dumps(row),flush=True)
    assert data['accepted_cells']==sum(r['original_cells'] for r in records)
    assert source_hash==sha(args.input) and selfhash==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in dependencies.items())
    result={'status':'passed','precision_bits':args.precision,'case_count':2,
            'original_cells':data['accepted_cells'],'replay_cells':total,'refinements':refinements,
            'cases':records,'exact_identity_count':len(exact),'exact_identities':exact,
            'input_path':str(args.input.resolve()),'input_sha256':source_hash,
            'proof_sha256':sha(PROOF),'script_sha256':selfhash,'dependencies':dependencies,
            'elapsed_seconds':time.time()-start,
            'method':'Independent exact tree coverage and positive-square P with direct differentiated Q; no author import.',
            'scope':'Upper-row endpoint maximum only for y in [13/100,1/2], |h|<=57/1000, both types/orientations; no geometric gap.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',total,'factorized cells;',refinements,'refinements.',flush=True)

if __name__=='__main__':
    main()
