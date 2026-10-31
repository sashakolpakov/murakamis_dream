"""Universal single-leaf attachment dual gap: exact rational verification."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json

_spec=importlib.util.spec_from_file_location('block_intervals',str(Path(__file__).with_name('verify_conway_two_leaf_block_alias_certificate.py')))
arith=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(arith)
I,S,LOG2=arith.I,arith.S,arith.LOG2

VERTICES=arith.VERTICES[2]
MARGIN=F(1,1000)

def leaf_bounds(box,pure,alias):
    assert arith.feasible(pure) and pure[0]<F(1,2)
    assert arith.feasible(alias)
    P=arith.g(pure[0])+arith.m(pure)
    H=arith.k(alias[0])+arith.m(alias)
    grad=arith.grad_m(alias)
    grad[0]+=-arith.logi(2*arith.sinpi(alias[0]/2))
    lows=[]
    for mu in box[0]:
        for lam in box[1]:
            for w in VERTICES:
                tangent=H+sum((grad[j]*(w[j]-alias[j]) for j in range(3)),I(0))
                gap=P-tangent+mu*LOG2*(pure[1]-w[1])-lam*LOG2*(pure[2]-w[2])
                lows.append(gap.lo)
    return min(lows)

def subdivide(box):
    a,b=box[0];c,d=box[1];m=(a+b)/2;n=(c+d)/2
    return [((a,m),(c,n)),((a,m),(n,d)),((m,b),(c,n)),((m,b),(n,d))]

def verify(data_path,output=None):
    data=json.loads(Path(data_path).read_text());den=data['denominator']
    assert isinstance(den,int) and den>0
    assert data['domain_over_log2']==[['-2','0'],['-2','0']]
    assert F(data['gap'])==MARGIN
    records=[]
    def walk(node,box,path):
        if 'children' in node:
            assert set(node)=={'children'} and len(node['children'])==4
            for i,(child,b) in enumerate(zip(node['children'],subdivide(box))):walk(child,b,path+str(i))
        else:
            assert set(node)=={'pure','alias'}
            assert len(node['pure'])==len(node['alias'])==3
            assert all(isinstance(x,int) for x in node['pure']+node['alias'])
            pure=[F(x,den) for x in node['pure']];alias=[F(x,den) for x in node['alias']]
            lo=leaf_bounds(box,pure,alias)
            assert F(lo,S)>MARGIN,(path,F(lo,S))
            records.append({'path':path,'box_over_log2':[[str(x) for x in v] for v in box],
                            'gap_lower':str(F(lo,S))})
    walk(data['tree'],((F(-2),F(0)),(F(-2),F(0))),'')
    result={'status':'PASS','exact_rational_arithmetic':True,
            'domain':'mu,lambda in [-2log2,0]; entire original product tetrahedron',
            'certified_gap':str(MARGIN),'rectangle_count':len(records),
            'endpoint_vertex_inequalities':16*len(records),
            'minimum_lower':str(min(F(r['gap_lower']) for r in records)),'records':records}
    if output:Path(output).write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',type=Path,default=Path(__file__).with_name('conway_single_leaf_attachment_certificate.json'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    r=verify(args.data,args.output)
    print(json.dumps({k:v for k,v in r.items() if k!='records'},indent=2))
