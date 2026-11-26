#!/usr/bin/env python3
"""Exact algebra and scalar constants for the central index chart."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import sympy as sp


def main():
    u,v=sp.symbols('u v')
    a=u*(1-v); b=v*(1-u)
    checks=[]
    def zero(name,e):
        assert sp.factor(e)==0,(name,e)
        checks.append(name)
    zero('difference identity',u-v-(a-b))
    zero('quadratic for U',u*u-(1+a-b)*u+a)
    zero('quadratic discriminant', (1-u-v)**2-(1-2*(a+b)+(a-b)**2))
    zero('other U branch', (1-v)*u-a)
    zero('other V branch', (1-u)*v-b)
    x=1/(1+u-u*v); y=1/(1+v-u*v)
    zero('first critical ratio',x*(1-u*v)/(1-x*u)-1)
    zero('second critical ratio',y*(1-u*v)/(1-y*v)-1)
    margins={
        'height exponent':F(33,175)-2*F(22,7)*F(3,100),
        'exponential majorant':F(5,4)-F(175,142),
        'inverse exponential':F(142,175)-F(4,5),
        'curvature margin':F(12,125)-F(9,100),
        'sine strip margin':1-2*F(49,100),
    }
    # The first comparison is exact equality because pi<22/7 is strict.
    assert margins.pop('height exponent')==0
    assert all(x>0 for x in margins.values())
    root=Path(__file__).resolve().parents[1]
    proof=root/'notes/research_three_vertex_central_index_chart.md'
    out=root/'repro/results/research-three-vertex-central-index-chart.json'
    deps=['notes/research_traced_three_vertex_endpoint.md',
          'notes/research_root_pochhammer_interpolation.md',
          'notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','exact_algebra_identities':len(checks),'identities':checks,
            'strict_rational_comparisons':len(margins),'rational_identity_count':1,
            'margins':{k:str(v)for k,v in margins.items()},
            'scope':'Central exact summand chart only; no global packet or geometric path enclosure.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((root/p).read_bytes()).hexdigest()for p in deps}}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(checks)} algebra identities, {len(margins)} strict comparisons and 1 rational identity.\n{out}')

if __name__=='__main__': main()
