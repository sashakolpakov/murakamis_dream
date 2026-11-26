#!/usr/bin/env python3
"""Bounded floating whole mixed-envelope derivative test; no certificate."""
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import brentq, differential_evolution

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT/'repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py'
INPUT = ROOT/'repro/diagnostics/2026-11-05-right-minimum-transport/reference_inputs.json'
spec = importlib.util.spec_from_file_location('phase_diagnostic', HELPER)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def gp(z):
    return np.log(1-np.exp(-2j*np.pi*z))


def geometry(x, reference, selection, moving):
    m = len(x)
    right = np.maximum((.5-x)/.05, 0)**2
    right[x <= .45] = 1
    height, velocity = np.zeros(m), moving.astype(float).astype(complex)
    for j in range(m):
        neighbors = [(j-1) % m, j, (j+1) % m]
        if selection[j]:
            height[j] = .014*right[j]
        else:
            cut = np.clip((x[neighbors]-.1)/.12, 0, 1)
            height[j] = reference[j].imag*right[j]*min(cut)
            if moving[neighbors].any():
                velocity[j] += 1j*reference[j].imag*right[j]/.12
    return x+1j*height, velocity


def raw(a, b, eta, eps, sa, sb, da, db, right_a):
    z = b if right_a else a
    dz = db if right_a else da
    typ = eps if right_a else eta
    sig = sb if right_a else sa
    first = int(not right_a)
    def rowder(u):
        return (np.log(2*np.cos(np.pi*u))+gp(z+u).real
                -(2+eps)*np.log(2*np.sin(np.pi*u))
                -2*np.pi*first*z.imag)
    u = brentq(rowder, 1e-9, .5-1e-9)
    value = (q.g(u+.5)+q.g(z+u)-q.g(z)
             -(2+eps)*q.g(u)+2j*np.pi*first*z*u).real
    grad = gp(z+u)-gp(z)+2j*np.pi*first*u
    nu, forcing = -q.g(z).real, 2*np.pi*max(z.imag, 0)
    branch = 'factorial' if nu >= forcing else 'forcing'
    if typ:
        value += .5*max(nu, forcing)-np.pi*sig*z.imag
        grad += -.5*gp(z) if branch == 'factorial' else -1j*np.pi*(z.imag > 0)
        grad += 1j*np.pi*sig
    return float(value), float((grad*dz).real), dict(row=float(u), branch=branch,
        complex_first=bool(first), row_residual=float(rowder(u)),
        target_gradient=[float(grad.real), float(grad.imag)])


def evaluate(word, reference, x, selection, moving=None):
    x, selection = np.asarray(x), np.asarray(selection)
    m = len(word)
    is_right = x >= .5
    if moving is None:
        minimum = min(x[~is_right])
        moving = (~is_right) & (x <= minimum+1e-12)
    z, dz = geometry(x, reference, selection, moving)
    rates, derivatives, edges = [], [], []
    gradient = np.zeros(m, dtype=complex)
    for j in range(m):
        k = (j+1) % m
        if is_right[j] and is_right[k]:
            # These fixed edges have zero derivative; their values are unused.
            rates.append(0.); derivatives.append(0.); edges.append(dict(kind='RR'))
        elif is_right[j] or is_right[k]:
            value, derivative, meta = raw(z[j], z[k], word[j], word[k],
                selection[j], selection[k], dz[j], dz[k], is_right[j])
            rates.append(value); derivatives.append(derivative)
            edges.append(dict(kind='raw', **meta))
            gradient[k if is_right[j] else j] += complex(*meta['target_gradient'])
        else:
            value, grad = q.phase(z[j], z[k], word[j], word[k])
            derivative = (grad[0]*dz[j]+grad[1]*dz[k]).real
            gradient[j] += grad[0]; gradient[k] += grad[1]
            value = value.real
            for v in (j, k):
                if selection[v]:
                    gval, linear = q.g(z[v]).real, -2*np.pi*z[v].imag
                    value += .5*max(gval, linear)
                    derivative += .5*((gp(z[v])*dz[v]).real if gval >= linear
                                       else -2*np.pi*dz[v].imag)
                    gradient[v] += .5*gp(z[v]) if gval >= linear else 1j*np.pi
            rates.append(float(value)); derivatives.append(float(derivative))
            edges.append(dict(kind='coherent'))
    stars = []
    for i in np.flatnonzero(moving):
        costs = []
        for j in ((i-1) % m, i, (i+1) % m):
            coefficient = 0 if selection[j] else reference[j].imag*max(0, min(1, 400*(.5-x[j])**2))/.12
            costs.append(float(-coefficient*gradient[j].imag))
        stars.append(dict(center=int(i), conservative=float(gradient[i].real+sum(min(v,0) for v in costs)),
                          horizontal=float(gradient[i].real), height_costs=costs))
    return dict(derivative=float(sum(derivatives)), edge_derivatives=derivatives,
        envelope_value=float(sum(rates)), real=x.tolist(),
        heights=z.imag.tolist(), velocities=[[float(v.real), float(v.imag)] for v in dz],
        moving=np.flatnonzero(moving).tolist(), edges=edges, conservative_stars=stars)


def decode(parameters, m, center):
    t = parameters[0]
    x = np.full(m, .5)
    x[center] = t
    free = [j for j in range(1, m) if j != center]
    for j, v in zip(free, parameters[1:]):
        x[j] = t+(.5-t)*v
    return x


def main():
    started = time.monotonic()
    source = json.loads(INPUT.read_text())
    refs = [r for r in source['references'] if len(r['word']) >= 3]
    rng = np.random.default_rng(20261105)
    per_reference = []
    all_trials = []
    for ri, item in enumerate(refs):
        word = item['word']; m = len(word)
        ref = np.array([complex(*v) for v in item['reference']])
        residual = q.Candidate(word, ref).reference_residual()
        assert residual < 1e-9
        trials = []
        for n in range(96):
            center = 1 if n % 2 == 0 else m-1
            selection = [int(j != 0 and word[j] and rng.integers(2)) for j in range(m)]
            p = np.r_[rng.uniform(.12, .22), rng.uniform(0, 1, m-2)]
            x = decode(p, m, center)
            result = evaluate(word, ref, x, selection)
            trials.append(dict(word=word, reference=item['reference'], selection=selection,
                center=center, parameters=p.tolist(), reference_gradient_residual=residual, **result))
        worst = min(trials, key=lambda a:a['derivative'])
        selection, center = worst['selection'], worst['center']
        def objective(p):
            return evaluate(word, ref, decode(p, m, center), selection)['derivative']
        opt = differential_evolution(objective, [(.12, .22)]+[(0, 1)]*(m-2),
            maxiter=24, popsize=5, polish=False, seed=20261105+ri,
            x0=worst['parameters'], tol=0, atol=0)
        result = evaluate(word, ref, decode(opt.x, m, center), selection)
        current = dict(word=word, reference=item['reference'], selection=selection,
            center=center, parameters=opt.x.tolist(), reference_gradient_residual=residual,
            optimizer_evaluations=int(opt.nfev), **result)
        # Independent finite differences of the actual complete envelope.
        x = np.array(current['real']); moving = np.zeros(m, bool)
        moving[current['moving']] = True
        diffs = []
        for step in (1e-5, 1e-6, 1e-7):
            if x[center]+step <= .22:
                xp = x+step*moving
                f = evaluate(word, ref, xp, selection)['envelope_value']
                diffs.append([step, (f-current['envelope_value'])/step])
            else:
                xp = x-step*moving
                f = evaluate(word, ref, xp, selection)['envelope_value']
                diffs.append([-step, (current['envelope_value']-f)/step])
        current['finite_difference_checks'] = diffs
        per_reference.append(current)
        all_trials.extend(trials)
        print(json.dumps(dict(word=word, selection=selection, minimum=current['derivative'],
                              real=current['real'])), flush=True)
    files = [Path(__file__).resolve(), HELPER, INPUT]
    result = dict(scope='Floating diagnostic only. Four archived actual references; one R coordinate fixed at .5; full original hybrid heights and all actual neighboring height derivatives. 384 seeded samples select four fixed selection patterns for bounded optimizations. No certified global minimum, finite-source failure or universal transport theorem.',
        sample_count=len(all_trials), bounded_optimizations=4,
        maximum_iterations=24, population_multiplier=5,
        minima=per_reference, worst=min(per_reference, key=lambda a:a['derivative']),
        worst_sampled_conservative_star=min(all_trials,
            key=lambda a:min(s['conservative'] for s in a['conservative_stars'])),
        elapsed_seconds=time.monotonic()-started,
        dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    Path(__file__).with_name('result.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
