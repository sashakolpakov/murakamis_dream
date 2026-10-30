#!/usr/bin/env python3
"""Exact identities behind global injectivity; domain proof is analytical."""
import json
from pathlib import Path
import sympy as s


def main():
    w,z,c,C,ss,r1,r2=s.symbols('w z c C ss r1 r2')
    B=lambda x:x*x+2*c*x+C*C
    assert s.expand(B(-2*c-w)-B(w))==0
    assert s.expand(B(w)-B(z)-(w-z)*(w+z+2*c))==0
    mobius=lambda r:(ss+s.I*r)/(ss-s.I*r)
    assert s.simplify(mobius(r1)-mobius(r2)
                     -2*s.I*ss*(r1-r2)/((ss-s.I*r1)*(ss-s.I*r2)))==0
    result=dict(status='PASS',slit_reflection_identity=1,
                only_two_quadratic_fibers=1,momentum_injectivity_identity=1,
                scope='Exact algebra; convex-cone, root calibration and global-domain proof are analytical. No finite complex coefficient claim.')
    Path(__file__).with_name('actual_q_hahn_global_fourier_legendre_chart_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
