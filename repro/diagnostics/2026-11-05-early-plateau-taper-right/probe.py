"""Fixed-grid E-P-U-R two-edge comparison; diagnostic arithmetic only."""
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HELPER = HERE.parent/"2026-11-05-low-terminal-right-interfaces/diagnose.py"
spec = importlib.util.spec_from_file_location("original_float_sources", HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def main():
    start = time.monotonic()
    rows = []
    for word in itertools.product((0, 1), repeat=4):
        ref, residual = old.reference(word)
        cc = old.Candidate(word, ref)
        for orientation in ("EPUR", "RUPE"):
            p, u, rawedge, forward = (1, 2, 3, True) if orientation == "EPUR" else (2, 1, 1, False)
            credit = (5.5 if forward else 7.55)*ref[p].imag**2
            real_p = np.unique(np.r_[.22, .27, .30, .33, .39, .45, ref[p].real])
            real_p = real_p[(real_p >= .22) & (real_p <= .45)]
            points = np.array(list(itertools.product(real_p, (.45, .475, .5), (0., 1/6))))
            x, t, ell = points.T
            for sp, su in itertools.product(range(word[p]+1), range(word[u]+1)):
                zp = x+1j*(.014*6*ell if sp else ref[p].imag*ell)
                zu = t+1j*(.014 if su else ref[u].imag)*400*(.5-t)**2
                a, b = (zp, zu) if forward else (zu, zp)
                f, grad = cc.base[2]
                plane = f+grad[0]*(a-ref[1])+grad[1]*(b-ref[2])
                coherent = (old.phase(a, b, word[1], word[2])[0]-plane).real
                coherent += .5*sp*np.maximum(old.g(zp).real, -2*old.PI*zp.imag)
                coherent += .5*su*np.maximum(old.g(zu).real, -2*old.PI*zu.imag)
                raw, row = old.raw_endpoint(cc, rawedge, zu, su, forward)
                assert np.all((row > .2) & (row < .4))
                value = coherent+raw-credit
                k = int(np.argmax(value))
                assert np.isfinite(value).all()
                result = dict(
                    word=list(word), orientation=orientation, selected_P=sp, selected_U=su,
                    maximum_found=float(value[k]), grid_points=len(points),
                    witness=dict(P_real=float(x[k]), U_real=float(t[k]), early_fraction=float(ell[k]),
                                 P_height=float(zp[k].imag), U_height=float(zu[k].imag),
                                 coherent_PU_defect=float(coherent[k]), full_raw_UR_defect=float(raw[k]),
                                 oriented_credit=float(credit), maximizing_row=float(row[k])),
                    reference=[[float(z.real), float(z.imag)] for z in ref],
                    reference_gradient_residual=residual)
                rows.append(result)
                print(json.dumps({k: result[k] for k in ("word", "orientation", "selected_P", "selected_U", "maximum_found")}), flush=True)
    paths = [Path(__file__), HELPER,
             HERE.parent/"2026-11-05-right-short-connectors/phase_helpers.py",
             ROOT/"notes/research_mixed_early_upper_transition_support.md",
             ROOT/"notes/research_mixed_complex_right_row_reduction.md",
             ROOT/"notes/research_mixed_right_boundary_row_bracket.md"]
    result = dict(
        scope="Fixed grid only: all16 four-letter actual-reference proposals, both E-P-U-R orientations, all physical P/U selections, three U reals, at most7 P reals and two early fractions. No target optimizer, outward enclosure, new reference cover, universal bound, or finite-source counterexample. R is already clamped to .5 in the global mixed raw envelope; the UR edge remains its complete raw row maximum.",
        cases=rows, total_grid_evaluations=sum(r["grid_points"] for r in rows),
        maximum=max(rows, key=lambda r: r["maximum_found"]),
        elapsed_seconds=time.monotonic()-start,
        dependencies={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in paths})
    (HERE/"result.json").write_text(json.dumps(result, indent=2)+"\n")
    print("MAX", json.dumps(result["maximum"]), flush=True)


if __name__ == "__main__":
    main()
