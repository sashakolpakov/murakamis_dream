#!/usr/bin/env python3
"""Three fixed real faces of conditioned distance-two-R half expressions.

Floating diagnostic only. No optimizer or universal sign certificate.
"""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py"
GEOMETRY = ROOT / "repro/results/research-mixed-neighbor-conditioned-critical-boxes.json"
spec = importlib.util.spec_from_file_location("conditioned_phase_helper", HELPER)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
TABLE = json.loads(GEOMETRY.read_text())["limits_in_thousandths"]


def gp(z):
    return np.log(1-np.exp(-2j*np.pi*z))


def interval(word, index):
    own = word[index]
    lo, hi = ((-.03, .02) if own == 0 else (-.057, -.02))
    prev, _, nxt = word[index-1:index+2]
    middle = TABLE["".join(map(str, (prev, own, nxt)))][1]
    lo, hi = max(lo, middle[0]/1000), min(hi, middle[1]/1000)
    # Retain the known "first leg" output of the following window;
    # when its last type is unspecified take the union over that type.
    futures = [word[index+2]] if index+2 < len(word) else [0, 1]
    first = [TABLE["".join(map(str, (own, nxt, f)))][2] for f in futures]
    lo = max(lo, min(v[0] for v in first)/1000)
    hi = min(hi, max(v[1] for v in first)/1000)
    if own == nxt == 1:
        hi = min(hi, -.048)
        if prev == 1:
            hi = min(hi, -.053)
    assert lo < hi
    return (lo, hi)


def raw_row(z, eps, d):
    r = np.exp(-2*np.pi*abs(z.imag))
    lam = 2*np.pi*(max(z.imag, 0)-d*z.imag)
    L = np.exp(2*lam)
    A, B = np.cos(2*np.pi*z.real), np.sin(2*np.pi*z.real)
    P, Q, R = 1+r*r-2*r*A, 4*r*B, 1+r*r+2*r*A
    def polynomial(w):
        return 4**(1+eps)*w**(4+2*eps)-L*(P+Q*w+R*w*w)*(1+w*w)**eps
    lo, hi = np.tan(np.pi*.2), np.tan(np.pi*.4)
    assert polynomial(lo) < 0 < polynomial(hi)
    for _ in range(60):
        mid = (lo+hi)/2
        if polynomial(mid) < 0:
            lo = mid
        else:
            hi = mid
    u = np.arctan((lo+hi)/2)/np.pi
    residual = (np.log(2*np.cos(np.pi*u))+gp(z+u).real
                -(2+eps)*np.log(2*np.sin(np.pi*u))-2*np.pi*d*z.imag)
    assert abs(residual) < 1e-10
    return u, polynomial(1)


def evaluate(word, side, sc, sn, t, y, cc, cn):
    ci, ni = (1, 2) if side == "right" else (2, 1)
    ac, an = word[ci], word[ni]
    right_type = word[3] if side == "right" else word[0]
    rho = (t-.1)/.12
    taper = 1 if y <= .45 else 400*(.5-y)**2
    zc = complex(t, .014 if sc else cc*rho)
    zn = complex(y, .014*taper if sn else cn*taper*rho)
    bc, bn = (0 if sc else cc/.12), (0 if sn else cn*taper/.12)
    if side == "right":
        _, gradient = q.phase(zc, zn, ac, an)
        gc, gn = gradient
        d, eps, gauge, real_gauge = 1, right_type, -1.5j, -.1*sc
    else:
        _, gradient = q.phase(zn, zc, an, ac)
        gn, gc = gradient
        d, eps, gauge, real_gauge = 0, an, 1.5j, .1*sc
    u, quarter_polynomial = raw_row(zn, eps, d)
    def rawK(row):
        return gp(zn+row)-(1+an/2)*gp(zn)+2j*np.pi*d*row
    values = []
    for chi in range(1 if sc else 2):
        for xi in range(1 if sn else 2):
            inner = ((1+1j*chi*bc)*(gc+gauge)).real+real_gauge
            coherent_height = (1j*xi*bn*gn).real
            raw_height = (1j*xi*bn*rawK(u)).real
            if not xi or bn == 0:
                endpoint = .2
            elif (d == 0 and bn > 0) or (d == 1 and bn < 0):
                endpoint = .25 if quarter_polynomial <= 0 else .2
            else:
                endpoint = .25 if quarter_polynomial >= 0 else .4
            # A floating branch sign at this point is only diagnostic.
            relaxed = inner+coherent_height+(1j*xi*bn*rawK(endpoint)).real
            values.append(dict(chi=chi, xi=xi,
                value=float(inner+coherent_height+raw_height),
                inner=float(inner), coherent_height=float(coherent_height),
                raw_height=float(raw_height), relaxed=float(relaxed),
                row_endpoint=endpoint))
    worst = min(values, key=lambda v: v["value"])
    relaxed = min(values, key=lambda v: v["relaxed"])
    return dict(word=list(word), side=side, selected=[sc, sn],
        real=[t, y], coefficients=[cc, cn],
        coefficient_boxes=[interval(word, ci), interval(word, ni)],
        raw_row=float(u), quarter_polynomial=float(quarter_polynomial),
        worst=worst, relaxed_worst=relaxed)


def main():
    started = time.monotonic()
    cases = []
    for word in itertools.product((0, 1), repeat=4):
        for side in ("left", "right"):
            ci, ni = (1, 2) if side == "right" else (2, 1)
            cb, nb = interval(word, ci), interval(word, ni)
            for sc in range(word[ci]+1):
                for sn in range(word[ni]+1):
                    for t, y in ((.22, .22), (.12, .12), (.22, .5)):
                        for cc, cn in itertools.product(
                                [0] if sc else cb, [0] if sn else nb):
                            cases.append(evaluate(word, side, sc, sn, t, y, cc, cn))
    best = min(cases, key=lambda v: v["worst"]["value"])
    relaxation = min(cases, key=lambda v: v["relaxed_worst"]["relaxed"])
    files = [Path(__file__).resolve(), HELPER, GEOMETRY,
        ROOT/"notes/research_mixed_four_before_four_height.md",
        ROOT/"notes/research_mixed_three_consecutive_four_height.md",
        ROOT/"notes/research_mixed_algebraic_right_row.md"]
    out = dict(scope="Floating fixed-face diagnostic only. Three real pairs, "
        "every four-type word/orientation and permitted center/neighbor selection, "
        "conditioned height-box corners. Boxes contain actual references but "
        "a point in them is not asserted realized by a cyclic reference. "
        "No optimization, uniform positivity, or whole-flow conclusion.",
        fixed_real_pairs=[[.22,.22],[.12,.12],[.22,.5]],
        evaluations=len(cases), worst=best, relaxed_worst=relaxation, cases=cases,
        elapsed_seconds=time.monotonic()-started,
        dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in files})
    Path(__file__).with_name("result.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:out[k] for k in ["evaluations","worst","relaxed_worst","elapsed_seconds"]},
                     indent=2))


if __name__ == "__main__":
    main()
