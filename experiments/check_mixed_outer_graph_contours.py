#!/usr/bin/env python3
"""Exact algebra for the periodic outer graph; no source-gap certificate."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_outer_graph_contours.md"
DEPS = [
    "notes/research_mixed_conditional_torus_composition.md",
    "notes/research_mixed_boundary_strip_bounds.md",
    "notes/research_mixed_right_half_source_reduction.md",
    "notes/research_mixed_central_alias_gap.md",
    "notes/research_mixed_type_three_window_strip.md",
    "notes/research_mixed_type_four_height_refinement.md",
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-mixed-outer-graph-contours.json")
    args = parser.parse_args()
    checks = []
    def equal(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        checks.append(name)
    def positive(name, expression):
        assert expression > 0, name
        checks.append(name)
    R = sp.Rational
    x = sp.symbols("x", real=True)
    left, right = 16*x**2, 100*(R(1,2)-x)**2
    equal("left plateau value", left.subs(x,R(1,4))-1)
    equal("right plateau value", right.subs(x,R(2,5))-1)
    equal("left seam value", left.subs(x,0))
    equal("right zero value", right.subs(x,R(1,2)))
    equal("left seam derivative", sp.diff(left,x).subs(x,0))
    equal("right seam derivative", sp.diff(right,x).subs(x,R(1,2)))
    equal("left derivative endpoint", sp.diff(left,x).subs(x,R(1,4))-8)
    equal("right derivative endpoint", sp.diff(right,x).subs(x,R(2,5))+20)
    equal("left taper coefficient", 16*R(57,1000)-R(114,125))
    positive("left pair budget using pi greater than three", 3-R(114,125))
    positive("Jacobian budget", R(38,25)**2-1-R(57,50)**2)
    u,v,p,q=sp.symbols("u v p q", real=True)
    den=(u+p)**2+(v+q)**2
    cotreal=((u*p-v*q-1)*(u+p)+(u*q+v*p)*(v+q))/den
    det=(u-cotreal)*(p-cotreal)-cotreal**2
    equal("pair determinant",det-((u+p)**2-(p*v-u*q)**2)/den)
    h=sp.Function("h")
    f=sp.Function("f")
    z=x+sp.I*h(x)
    equal("graph second derivative",sp.diff(f(z),x,2)-
          (sp.Subs(sp.diff(f(x),x,2),x,z)*(1+sp.I*sp.diff(h(x),x))**2+
           sp.I*sp.diff(h(x),x,2)*sp.Subs(sp.diff(f(x),x),x,z)))
    ell=sp.symbols("ell",integer=True,nonzero=True)
    zz=sp.symbols("z")
    primitive=sp.exp(-2*sp.pi*sp.I*ell*zz)/(-2*sp.pi*sp.I*ell)
    assert sp.simplify(sp.diff(primitive,zz)-sp.exp(-2*sp.pi*sp.I*ell*zz))==0
    checks.append("nonzero Fourier primitive")
    assert sp.simplify(primitive.subs(zz,zz+1)-primitive)==0
    checks.append("periodic primitive endpoint cancellation")
    record={
        "status":"passed","exact_checks":len(checks),"checks":checks,
        "scope":"Exact periodic graph deformation and pointwise pair Hessian; no transition-source or exterior supporting-plane gap.",
        "script_sha256":sha(__file__),"proof_sha256":sha(PROOF),
        "dependencies_sha256":{p:sha(ROOT/p) for p in DEPS},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(f"PASS {len(checks)} exact identities/rational comparisons")

if __name__=="__main__":
    main()
