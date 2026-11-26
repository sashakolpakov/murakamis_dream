#!/usr/bin/env python3
"""Outward checks of two specific left-region support obstructions."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_left_support_obstructions.md"
DEPS = [
    "notes/research_mixed_unselected_right_taper_products.md",
    "experiments/certify_mixed_right_square_conditional_packets.py",
    "repro/results/research-mixed-right-square-conditional-packets.json",
    "notes/research_mixed_cyclic_critical_localization.md",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_conditional_torus_composition.md",
    "notes/research_mixed_coupled_outer_graph.md",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--precision", type=int, default=256)
parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-mixed-left-support-obstructions.json")
args = parser.parse_args()
assert args.precision >= 128
ctx.prec = args.precision
initial = {p: sha(ROOT / p) for p in DEPS}
proof_hash, script_hash = sha(PROOF), sha(__file__)
up = json.loads((ROOT / DEPS[2]).read_text())
assert up["status"] == "passed"
assert up["proof_sha256"] == initial[DEPS[0]]
assert up["script_sha256"] == initial[DEPS[1]]
for p, h in up["dependencies"].items():
    assert sha(ROOT / p) == h, p
P, I = arb.pi(), acb(0, 1)
comparisons = []


def ar(v):
    q = Fraction(v)
    return arb(q.numerator) / q.denominator


def ck(name, test, value=None):
    assert test, (name, value)
    comparisons.append({"name": name, "value": str(value)})


def g(z):
    return ((-2 * P * I * z).exp().polylog(2) - P * P / 6) / (2 * P * I)


def gp(z):
    return (1 - (-2 * P * I * z).exp()).log()


def f(s, a, b):
    return gp(s + a) + gp(s + b) - 3 * gp(s) + 2 * P * I * a


def fp(s, a, b):
    return P * ((P * (s + a)).cot() + (P * (s + b)).cot()
                - 3 * (P * s).cot()) + P * I


def value(s, a, b):
    return g(s + a) + g(s + b) - 3 * g(s) + 2 * P * I * a * s - 3 * (g(a) + g(b)) / 2


def root(a, b, center, label):
    c = acb(ar(center[0]), ar(center[1]))
    radius = ar("1e-12")
    box = c + acb(arb(0, radius), arb(0, radius))
    inv = 1 / fp(c, a, b)
    contraction = abs(1 - inv * fp(box, a, b))
    residual = abs(inv * f(c, a, b))
    ck(label + ": contraction", contraction < ar("1/1000"), contraction)
    ck(label + ": self-map", residual + contraction * radius < radius, residual + contraction * radius)
    for j, v in enumerate((box, box + a, box + b)):
        ck(label + ": sine strip " + str(j), 0 < v.real < 1, v.real)
    ck(label + ": source root box",
       ar(".2") < box.real < ar(".46") and abs(box.imag) < ar(".17"), box)
    return box


z = I * ((-1 - I * arb(7).sqrt()) / 4).log() / (2 * P)
r, h = z.real, z.imag
ck("actual reference real", ar(".3075") < r < ar(".3076"), r)
ck("actual reference height", ar("-.0552") < h < ar("-.0551"), h)
ck("reference original zero lift", abs(f(z, z, z)) < ar("1e-60"), f(z, z, z))
ref = value(z, z, z)
ga = gp(2 * z) + 2 * P * I * z - 3 * gp(z) / 2
gb = gp(2 * z) - 3 * gp(z) / 2
ck("reference cyclic stationarity", abs(ga + gb) < ar("1e-60"), ga + gb)

# Exact identities supplying the exponentiated homogeneous equations.
v = sp.Symbol("v")
relation = 2 * v**2 + v + 1
assert sp.rem((1 + v)**2 - v * (1 - v), relation, v) == 0
assert sp.rem((1 + v)**4 - v**2 * (1 - v)**2, relation, v) == 0

x, y, u = ar(".219"), ar(".346"), ar(".285")
a, b = acb(x, h * (x / ar(".22"))**2), acb(y, h)


def integ(u, x, height):
    return (g(acb(x + u, -abs(height))) - g(acb(x, -abs(height)))).real + 2 * P * max(height, arb(0)) * u


raw = integ(u, a.real, a.imag) + integ(u, b.real, b.imag) - 3 * g(acb(u)).real - 2 * P * a.imag * u
raw -= (g(a) + g(b)).real / 2
plane = (ref + ga * (a - z) + gb * (b - z)).real
raw_defect = raw - plane
ck("raw defect > .018", raw_defect > ar(".018"), raw_defect)
for label, w in (("raw a", a), ("raw b", b), ("reset low", acb(ar(".22"))),
                 ("reset neighbor", acb(r)), ("unchanged", z)):
    ck(label + ": relative d domain", 0 < w.real < ar(".5") and w.imag <= 0, w)
    ck(label + ": positive Fourier rate", -g(w).real > ar(".01"), -g(w).real)

pairs = [
    (acb(r), acb(ar(".22")), (".29965506202557324", "-.04385714912809971")),
    (acb(ar(".22")), acb(r), (".3144399085018218", "-.11621646853713892")),
    (acb(r), z, (".2849291024715839", "-.06820877412973518")),
    (z, acb(r), (".32321768536611845", "-.05743453263582737")),
]
vals = []
for j, (a, b, center) in enumerate(pairs):
    for k, w in enumerate((a, b)):
        # The lower endpoint is the exact rational .22 by construction;
        # comparing two rounded balls for this equality is not meaningful.
        real_in_source = ((j, k) in ((0, 1), (1, 0))
                          or ar(".22") < w.real < ar(".50"))
        ck(f"pair{j}: source argument{k}",
           real_in_source and ar("-.057") < w.imag < ar(".0141"), w)
    s = root(a, b, center, "pair" + str(j))
    vals.append(value(s, a, b))
excess = (sum(vals, acb(0)) - 4 * ref).real
ck("reset excess > .0093", excess > ar(".0093"), excess)
ck("reset excess < .0095", excess < ar(".0095"), excess)

assert initial == {p: sha(ROOT / p) for p in DEPS}
assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
record = {
    "status": "passed",
    "scope": "Two pointwise support obstructions only; no obstruction to the cyclic integral or volume asymptotic.",
    "precision_bits": args.precision,
    "exact_identities": 2,
    "outward_comparisons": len(comparisons),
    "comparisons": comparisons,
    "raw_defect": str(raw_defect),
    "actual_seven_cycle_reset_excess": str(excess),
    "root_centers_scope": "Fixed rational-decimal proposals; original logarithmic Newton self-maps are checked independently.",
    "proof_sha256": proof_hash,
    "script_sha256": script_hash,
    "dependencies": initial,
    "validated_source_record": DEPS[2],
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(record, indent=2) + "\n")
print("PASS", len(comparisons), "outward comparisons + 2 identities")
print("raw defect", raw_defect, "reset excess", excess)
