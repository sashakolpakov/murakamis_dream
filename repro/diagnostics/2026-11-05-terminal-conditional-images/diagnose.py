#!/usr/bin/env python3
"""Fixed old endpoint proposals only: no new roots, search, or certificate."""
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INPUT = ROOT / "repro/diagnostics/2026-11-05-open-word-endpoint-maps/result.json"
ctx.prec = 192
PI, II = arb.pi(), acb(0, 1)


def z(v):
    return acb(str(v[0]), str(v[1]))


def g(w):
    return ((-2*PI*II*w).exp().polylog(2)-PI*PI/6)/(2*PI*II)


def phase(s, a, e, eps):
    return g(s+a)+g(s+e)-(2+eps)*g(s)+2*PI*II*a*s


def f(v):
    return float(v.mid())


def evaluate(a, e, t, eps):
    M = phase(t, a, e, eps).real
    last = (g(a)+g(e)).real + 2*PI*(
        max(-a.imag, arb(0))+max(e.imag, arb(0)))
    cuts = [f(M-phase(acb(str(c)), a, e, eps).real) for c in (.15, .49)]
    aliases = []
    for sign in (-1, 1):
        aliases.append(min(f(M-phase(acb(arb(15)/100+arb(34)*j/3200,
                                            sign*arb(1)/5), a, e, eps).real+2*PI/5)
                           for j in range(33)))
    qa = (2*PI*a.real).sin()/((2*PI*a.imag).cosh()-(2*PI*a.real).cos())
    qe = (2*PI*e.real).sin()/((2*PI*e.imag).cosh()-(2*PI*e.real).cos())
    wl, wr = -1/(49*PI/100).tan(), max(qa, qe)
    ca, sa = (PI*a).cos(), (PI*a).sin()
    ce, se = (PI*e).cos(), (PI*e).sin()
    shape = max(f((2*PI*(e.imag-a.imag)).exp()/4**eps
                  * abs(ca-(wl+(wr-wl)*j/32)*sa)**2
                  * abs(ce-(wl+(wr-wl)*j/32)*se)**2
                  * (1+(wl+(wr-wl)*j/32)**2)**eps) for j in range(33))
    return dict(selected_rate=f(M), left_cut_gap=cuts[0], right_cut_gap=cuts[1],
                last_row_gap=f(M-last), lower_alias_grid_gap=aliases[0],
                upper_alias_grid_gap=aliases[1], tail_shape_grid_upper=shape)


def main():
    old = json.loads(INPUT.read_text())
    out = dict(status="diagnostic_only",
               scope="132 fixed archived endpoint-map proposals plus two old m1 proposals; "
                     "no root search, no interval root validation, no full-circle or "
                     "horizontal-segment cover and no source theorem.",
               cases=[], one_vertex=[])
    for case in old["cases"]:
        rows = []
        for row in case["rows"]:
            a, (e, t, _) = z(row["external"]), map(z, row["root"])
            rows.append(dict(external=row["external"], root=row["root"],
                             values=evaluate(a, e, t, case["epsilon"])))
        names = rows[0]["values"].keys()
        extrema = {name: (max if name.endswith("upper") else min)(
            row["values"][name] for row in rows) for name in names}
        out["cases"].append(dict(epsilon=case["epsilon"],
                                 neighbor_epsilon=case["neighbor_epsilon"],
                                 extrema=extrema, rows=rows))
        print(case["epsilon"], case["neighbor_epsilon"], extrema, flush=True)
    for row in old["one_vertex"]:
        e = z(row["private_e"])
        out["one_vertex"].append(dict(epsilon=row["epsilon"],
            values=evaluate(e, e, e, row["epsilon"]),
            scope="Diagnostic only: m1 one-cap formula has no conditional factor."))
    inputs = [INPUT.relative_to(ROOT).as_posix(),
              "notes/research_mixed_conditional_image_contours.md",
              "notes/research_mixed_open_word_endpoint_rectangles.md",
              "notes/research_mixed_open_word_critical_localization.md"]
    out["dependencies_sha256"] = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                   for p in inputs}
    out["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/"result.json").write_text(json.dumps(out, indent=2)+"\n")


if __name__ == "__main__":
    main()
