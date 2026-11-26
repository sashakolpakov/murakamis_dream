"""One fixed homogeneous-four endpoint: bounded incoming/tail trials only."""
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import sys
import time

import numpy as np
from scipy.optimize import differential_evolution, minimize

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "2026-11-05-right-short-connectors"
sys.path.insert(0, str(OLD))
from diagnose import optimize_path
from phase_helpers import Candidate, PI, THETA, phase

spec = importlib.util.spec_from_file_location("lowpilot", HERE / "diagnose.py")
lp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lp)


def synchronized(cc, free, selection):
    free = np.asarray(free).reshape(-1, 2)
    n = len(free)
    u = np.column_stack((np.full(n, cc.r(-5).real), free))
    v = np.broadcast_to([cc.r(-2).real, .1, cc.r(0).real], (n, 3))
    p = np.broadcast_to([cc.r(j).real for j in range(-2, 1)], (n, 3))
    a, b = np.column_stack((u, v)), np.column_stack((u, p))
    # The first predecessor and its selection cancel; the middle
    # predecessor selection appears only in that same cancelled weight.
    sig = (0, 0, selection, 0, 0, 0)
    return sum((cc.w(-3+k, a[:, k:k+4], sig[k:k+4])
                - cc.w(-3+k, b[:, k:k+4], sig[k:k+4])
                for k in range(3)), np.zeros(n))


def main():
    start = time.monotonic()
    ref, residual = lp.reference((1,))
    cc = Candidate((1,), ref)
    out = (cc.r(-2).real, .1, cc.r(0).real)
    entry = (cc.r(0).real, .5, .1)
    raw_l, _ = lp.raw_endpoint(cc, 0, np.array([.1+0j]), 0, True)
    raw_r, _ = lp.raw_endpoint(cc, 1, np.array([.5+0j]), 0, False)
    rawsum = float(raw_l[0]+raw_r[0])
    ex = float(cc.E3(0, np.array([out]), (0, 0, 0))[0])
    psi = float(cc.om(-1, .1, 0))
    bonus = .09-7.55*cc.r(-2).imag**2-5.5*cc.r(0).imag**2
    coarse = -ex-(1-THETA)*psi-bonus
    paths = []
    for h in (3, 4, 5):
        paths.append(optimize_path(cc, "incoming", 2, h, entry, (0, 0, 0), 25100+h))
        paths.append(optimize_path(cc, "incoming", 0, h, out, (0, 0, 0), 25200+h))
    choices = []
    for selection in (0, 1):
        fn = lambda v: synchronized(cc, v, selection)
        opt = differential_evolution(lambda x: -fn(np.asarray(x).T),
            [(.1, .5)]*2, seed=25300+selection, maxiter=70, popsize=8,
            polish=False, vectorized=True, updating="deferred", tol=1e-11)
        local = minimize(lambda x: -fn(x)[0], opt.x, method="L-BFGS-B",
            bounds=[(.1, .5)]*2,
            options={"maxiter":100, "ftol":1e-14, "gtol":1e-8})
        grid = np.array(list(itertools.product(
            np.unique(np.r_[np.linspace(.1,.5,101), .12,.22,.45,ref.real]),repeat=2)))
        trial = np.vstack((grid, opt.x, local.x))
        vals = fn(trial); k = int(vals.argmax())
        choices.append(dict(selection=selection, maximum_found=float(vals[k]),
                            predecessor_reals=trial[k].tolist()))
    synced = max(row["maximum_found"] for row in choices)
    a, b = cc.r(-2), cc.r(-1)
    f, gr = cc.base[-1 % cc.m]
    realf = phase(a.real, .1, cc.t(-2), cc.t(-1))[0]
    tangent = f+gr[0]*(a.real-a)+gr[1]*(.1-b)
    fee = max(0, a.imag*(gr[0].imag-PI*(.5-a.real)/2)
                   + PI/2*max(-a.imag,0))
    acute = float((realf-tangent).real)+fee+THETA*psi/2
    comparisons = []
    for h in (3,4,5):
        ain = next(p["maximum_found"] for p in paths if p["depth"]==h and p["layer"]==2)
        aout = next(p["maximum_found"] for p in paths if p["depth"]==h and p["layer"]==0)
        comparisons.append(dict(depth=h, coarse_left_plus_entry=rawsum+coarse-ain,
              acute_left_plus_entry=rawsum+acute-ain,
              synchronized_trial_plus_entry=rawsum+synced-ain,
              same_incoming_trial=rawsum+aout-ain,
              incoming_right_trial=ain, incoming_left_trial=aout))
    files = [Path(__file__), HERE/"diagnose.py", OLD/"diagnose.py", OLD/"phase_helpers.py"]
    result = dict(scope="One fixed homogeneous-four actual-reference configuration only, xlow=.1, R=.5, opposite endpoint=.5, following halo=.1. Finite incoming and synchronized-tail optimizers give lower trials, never upper enclosures. No new outer-state search or uniform interface claim. No favorable endpoint AA occupation has been subtracted.",
        reference=[[float(z.real),float(z.imag)] for z in ref], reference_residual=residual,
        raw_defect_sum=rawsum, coarse_incoming_upper_evaluated=coarse,
        acute_incoming_upper_evaluated=acute, synchronized_upper_maximum_found=synced,
        synchronized_choices=choices, paths=paths, comparisons=comparisons,
        elapsed_seconds=time.monotonic()-start,
        dependencies={str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in files})
    (HERE/"fixed-worst-results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("paths","dependencies")}),flush=True)


if __name__=="__main__":
    main()
