#!/usr/bin/env python3
"""Six bounded floating local tests; no uniform sign or actual-reference claim."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time
import numpy as np
from scipy.optimize import differential_evolution

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT/'repro/diagnostics/2026-11-05-right-short-connectors/phase_helpers.py'
spec = importlib.util.spec_from_file_location('phase_helpers', HELPER)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def gp(z):
    return np.log(1-np.exp(-2j*np.pi*z))


def taper(x):
    return np.where(x <= .45, 1, 400*(.5-x)**2)


def evaluate(parameters, kind, pattern, details=False):
    p = np.atleast_2d(parameters)
    t = p[:, 0]
    rho = (t-.1)/.12
    xl = t+(.5-t)*p[:, 1]
    xo = t+(.5-t)*p[:, 2]
    cmin, cmax = ((-.03, .02) if kind == 0 else (-.057, -.02))
    cc, cl, co = (cmin+(cmax-cmin)*p[:, j] for j in (3, 4, 5))
    lammax = np.minimum(np.clip((xl-.1)/.12, 0, 1),
                        np.clip((xo-.1)/.12, 0, 1))
    lam = rho+(lammax-rho)*p[:, 6]
    zc = t+1j*cc*rho
    zl = xl+1j*cl*taper(xl)*rho
    zo = xo+1j*co*taper(xo)*lam
    answers, metadata = [], []
    for rows in itertools.product((.2, .4), repeat=2 if pattern != 'one_right' else 1):
        uc = rows[0]
        gc = gp(zc+uc)-(1+kind/2)*gp(zc)+2j*np.pi*uc
        if pattern == 'both_neighbors_right':
            ul = rows[1]
            gc += gp(zc+ul)-(1+kind/2)*gp(zc)
            gl = np.zeros_like(gc)
        else:
            adjacent = q.phase(zl, zc, kind, kind)[1]
            gc += adjacent[:, 1]
            gl = adjacent[:, 0]
            if pattern == 'outer_left_right':
                ul = rows[1]
                gl += gp(zl+ul)-(1+kind/2)*gp(zl)
            else:
                gl += q.phase(zo, zl, kind, kind)[1][:, 1]
        center_cost = -cc/.12*gc.imag
        left_cost = -cl*taper(xl)/.12*gl.imag
        value = gc.real+np.minimum(center_cost, 0)+np.minimum(left_cost, 0)
        answers.append(value)
        metadata.append(dict(rows=rows, horizontal=gc.real,
                             center_height_cost=center_cost,
                             left_height_cost=left_cost))
    arr = np.array(answers)
    choice = arr.argmin(axis=0)
    value = arr[choice, np.arange(len(p))]
    if not details:
        return value
    assert len(p) == 1
    info = metadata[int(choice[0])]
    return dict(value=float(value[0]), rows=info['rows'],
        horizontal=float(info['horizontal'][0]),
        center_height_cost=float(info['center_height_cost'][0]),
        left_height_cost=float(info['left_height_cost'][0]),
        real=[float(xo[0]), float(xl[0]), float(t[0]), .5],
        height_coefficients=[float(co[0]), float(cl[0]), float(cc[0])],
        targets=[[float(z.real), float(z.imag)] for z in (zo[0], zl[0], zc[0])],
        exterior_cutoff=float(lam[0]), parameters=p[0].tolist())


def main():
    started = time.monotonic()
    cases = []
    for kind in (0, 1):
        for pattern in ('one_right', 'outer_left_right', 'both_neighbors_right'):
            result = differential_evolution(
                lambda p: evaluate(np.asarray(p).T, kind, pattern),
                [(.12, .22)]+[(0, 1)]*6,
                maxiter=40, popsize=6, seed=20261105+len(cases),
                polish=False, vectorized=True, updating='deferred', tol=0, atol=0)
            row = dict(kind=kind, pattern=pattern, evaluations=int(result.nfev),
                       **evaluate(result.x, kind, pattern, details=True))
            cases.append(row)
            print(json.dumps(row), flush=True)
    paths = [Path(__file__).resolve(), HELPER]
    out = dict(scope='Floating diagnostic only, with independent typed reference-height intervals, unselected endpoints and two row endpoints. A negative value refutes only this enlarged-domain relaxation if certified separately; a positive minimum found is not a uniform lower bound. No actual-reference, finite-source, or transport theorem.',
        fixed_patterns=3, type_choices=2, maximum_iterations=40,
        population_multiplier=6, cases=cases,
        elapsed_seconds=time.monotonic()-started,
        dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    Path(__file__).with_name('result.json').write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
