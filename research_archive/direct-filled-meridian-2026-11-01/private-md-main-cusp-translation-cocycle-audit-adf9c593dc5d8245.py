"""Exact projective matrix checks for the private main-cusp calculation."""
import hashlib
import json
from pathlib import Path
import sympy as sp

E, R = sp.symbols("E R", nonzero=True)
W = [
    sp.Matrix([[1, 0], [0, E]]),
    sp.Matrix([[1, E-1], [0, E]]),
    sp.Matrix([[E-R, R*(1-E)], [E-1, 1-E*R]]),
    sp.Matrix([[R, 0], [1-E, E*R]]),
]
X = [
    sp.Matrix([[0, E*R], [E-1, 0]]),
    sp.Matrix([[-1, 0], [0, E-1]]),
    sp.Matrix([[0, -E*(R-1)], [E-1, -(E-1)]]),
    sp.Matrix([[0, -R*(R-1)], [E-1, -R*(E-1)]]),
]
S = sp.Matrix([[0, -E*R], [1, -1-E]])
A = sp.Matrix([[R, -R], [1, E*R-1-E]])
B = sp.Matrix([[R/E-1-1/E, R], [-1, R]])
checks = []

def affine_check(name, matrix, slope, shift):
    normalized = matrix / matrix[1, 1]
    expected = sp.Matrix([[slope, shift], [0, 1]])
    assert all(sp.cancel(x) == 0 for x in normalized-expected), name
    checks.append(name)

for j in range(4):
    m = W[(j-1) % 4].inv()*W[j]
    if j % 2:
        m = m.inv()
    affine_check(f"meridian_{j}", X[j]*m*X[j].inv(), 1, 1)

for name, face, source, target, second, shift in [
    ("S10", S, 1, 0, False, (E+1)/(E-1)),
    ("S23", S, 2, 3, False, (R-1)/(E-1)),
    ("A13", A, 1, 3, True, -(E*R-E-1)/(E-1)),
    ("A20", A, 2, 0, True, -1/(E-1)),
    ("B31", B, 3, 1, True, (E-R+1)/(E-1)),
    ("B02", B, 0, 2, True, -E/(E-1)),
]:
    target_frame = X[target].subs(E, 1/E) if second else X[target]
    affine_check(name, target_frame*face*X[source].inv(), 1, shift)

for j, shifts in enumerate([(0, 0), (1, 0), (-1, -R), (1-R, 1)]):
    for a, shift in zip([j, (j+1) % 4], shifts):
        affine_check(f"W{j}_corner{a}",
                     X[a].subs(E, 1/E)*W[j]*X[a].inv(), -1, shift)

J = sp.Matrix([[-R, 0], [-1, 1-R]])
SG = J*S.subs(R, 1-R)*J.inv()
longitude = SG*S*SG.inv()*S.inv()
affine_check("two_leaf_preferred_longitude",
             X[0]*longitude*X[0].inv(), 1, -2*(E+1)/(E-1))
report = {
    "method": "exact rational functions in independent E,R",
    "checks": checks,
    "count": len(checks),
    "scope": "matrix identities; topological marking is proved separately in the text",
}
out = Path("/private/tmp/md-main-cusp-translation-cocycle-results.json")
out.write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({"count": len(checks), "result": str(out),
                  "sha256": hashlib.sha256(out.read_bytes()).hexdigest()}))
