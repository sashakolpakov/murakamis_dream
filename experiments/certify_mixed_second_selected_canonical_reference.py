#!/usr/bin/env python3
"""Two prescribed canonical prefixes, certified by the original gradient residual.

The outside coordinate is exactly 1/3. Floating proposals have no proof
role: an exact rational center, outward original-log residual, and the
proved global accretivity bound localize the already existing solution.
No source, scalar budget, rational transport, or alternate input is tried.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
NAMES = ("e", "xi", "a", "u", "z", "v", "b")
RADIUS = F(1, 10**40)
PROOF = "notes/research_mixed_prefix_residual_localization.md"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rat(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def exact_endpoint(value):
    return F(str(value.fmpq()))


def ends(value):
    if not value.is_finite():
        raise ValueError("nonfinite residual or enclosure")
    return exact_endpoint(value.lower()), exact_endpoint(value.upper())


def interval_record(value):
    lo, hi = ends(value)
    return {"lower_rational": str(lo), "upper_rational": str(hi)}


def complex_record(value):
    return {"real": interval_record(value.real), "imag": interval_record(value.imag)}


def cp(pair):
    return acb(rat(pair[0]), rat(pair[1]))


def gradient(values, outside, beta, xp, log, sin, cos, pi, ii):
    e, xi, a, u, z, v, b = values
    half = xp(1)/2
    def jp(w):
        return log(2*sin(pi*w))
    return [
        -jp(e-xi)+jp(e+a)-jp(e)+ii*pi*(xi-a+e-half),
        2*log(cos(pi*xi))+log(sin(pi*(e-xi)))-3*log(sin(pi*xi))+ii*pi*e,
        jp(e+a)+jp(a+u)-3*jp(a)+ii*pi*(u-e+a-half),
        jp(u+z)+jp(a+u)-3*jp(u)+ii*pi*(a-z+u-half),
        jp(u+z)+jp(z+v)-3*jp(z)+ii*pi*(v-u+z-half),
        jp(v+b)+jp(z+v)-(2+beta)*jp(v)+ii*pi*(z-b+beta*(v-half)),
        jp(v+b)+jp(b+outside)-(2+beta)*jp(b)+ii*pi*(outside-v+beta*(b-half)),
    ]


def propose(beta):
    import mpmath as mp
    with mp.workdps(80):
        def c(real, imag):
            return mp.mpc(real, imag)
        tail = c('.35', '-.01') if beta == 0 else c('.30', '-.052')
        initial = (c('.35', '-.035'), c('.225', '.036'),
                   c('.30', '-.052'), c('.30', '-.052'),
                   c('.30', '-.052'), tail, tail)
        def function(*values):
            return gradient(values, mp.mpf(1)/3, beta, mp.mpf,
                            mp.log, mp.sin, mp.cos, mp.pi, mp.j)
        solution = mp.findroot(function, initial, maxsteps=30,
                               tol=mp.mpf('1e-65'), verify=True)
        return [[mp.nstr(w.real, 60), mp.nstr(w.imag, 60)] for w in solution]


def check_center(centers, beta):
    if len(centers) != 7 or any(len(row) != 2 for row in centers):
        raise ValueError("invalid seven-variable witness")
    exact = [[F(t) for t in row] for row in centers]
    domain_checks = {}
    for name, (x, y) in zip(NAMES, exact):
        if name == 'e':
            bounds = tuple(map(F, ('.33', '.47', '-.09', '.08')))
        elif name == 'xi':
            bounds = tuple(map(F, ('.21', '.25', '.01', '.10')))
        else:
            bounds = tuple(map(F, ('.23', '.45', '-.12', '.12')))
        lo, hi, bot, top = bounds
        if not (lo < x-RADIUS < x+RADIUS < hi and bot < y-RADIUS < y+RADIUS < top):
            raise ValueError("center and localization square outside convex domain: "+name)
        domain_checks[name] = dict(bounds=list(map(str, bounds)), strict=True)
    values = list(map(cp, exact))
    pi, ii = arb.pi(), acb(0, 1)
    residual = gradient(values, acb(rat(F(1, 3))), beta, arb,
                        lambda w: w.log(), lambda w: w.sin(),
                        lambda w: w.cos(), pi, ii)
    squared = F(0)
    for value in residual:
        for component in (value.real, value.imag):
            lo, hi = ends(component)
            squared += max(abs(lo), abs(hi))**2
    mu_lower = F(6, 49)*ends(pi)[0]
    required = mu_lower**2*RADIUS**2
    if not squared < required:
        raise ValueError("original gradient residual does not certify the prescribed radius")
    # Existence is supplied by the bound input theorem, not inferred
    # from a small residual. Strong accretivity bounds the distance.
    enclosures = {}
    for name, (x, y) in zip(NAMES, exact):
        enclosures[name] = {
            "real": {"lower_rational": str(x-RADIUS), "upper_rational": str(x+RADIUS)},
            "imag": {"lower_rational": str(y-RADIUS), "upper_rational": str(y+RADIUS)},
        }
    enclosures['c'] = {"real": {"lower_rational": "1/3", "upper_rational": "1/3"},
                       "imag": {"lower_rational": "0", "upper_rational": "0"}}
    return dict(beta=beta, alpha=1, status="canonical prefix localized",
                centers=centers, radius_rational=str(RADIUS),
                common_convex_domain_checks=domain_checks,
                original_gradient_residual=[complex_record(v) for v in residual],
                residual_squared_norm_upper_rational=str(squared),
                accretivity_lower_rational=str(mu_lower),
                required_squared_residual_upper_rational=str(required),
                strict_residual_test=True, coordinate_enclosures=enclosures,
                suffix_realization_claimed=False, scalar_gap_claimed=False)


def input_bindings():
    bindings = {}
    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None and digest != expected:
            raise ValueError("inherited dependency mismatch: "+name)
        if name in bindings and bindings[name] != digest:
            raise ValueError("inconsistent input binding: "+name)
        bindings[name] = digest
        return digest
    for name in (PROOF, "notes/research_mixed_second_selected_reference_curve.md",
                 "notes/research_mixed_second_selected_canonical_reference_fallback.md"):
        bind(name)
    stem = 'repro/results/research-mixed-open-word-critical-localization'
    record = json.loads((ROOT/(stem+'.json')).read_text())
    replay = json.loads((ROOT/(stem+'-replay.json')).read_text())
    author_sha = bind(stem+'.json')
    bind(stem+'-replay.json')
    if record['status'] != 'passed' or replay['status'] != 'passed' or replay['input_sha256'] != author_sha:
        raise ValueError("missing completed original geometry and saved replay")
    for data in (record, replay):
        bind('notes/research_mixed_open_word_critical_localization.md', data['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py', data['script_sha256'])
        for name, digest in data['dependencies_sha256'].items():
            bind(name, digest)
    bind(str(Path(__file__).resolve().relative_to(ROOT)))
    return bindings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--input', type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    bindings = input_bindings()
    ctx.prec = 256
    old = json.loads(args.input.read_text()) if args.input else None
    if old is not None:
        if old['status'] != 'both prescribed canonical prefixes localized' or old['input_sha256'] != bindings:
            raise ValueError('saved replay bindings or status differ')
        if [row['beta'] for row in old['cases']] != [0, 1]:
            raise ValueError('saved case inventory differs')
    cases = []
    for beta in (0, 1):
        centers = old['cases'][beta]['centers'] if old else propose(beta)
        result = check_center(centers, beta)
        cases.append(result)
        print(json.dumps({'beta': beta, 'status': result['status'],
                          'centers': dict(zip(NAMES, centers))}), flush=True)
    for name, digest in bindings.items():
        if sha(ROOT/name) != digest:
            raise ValueError('input changed during certification: '+name)
    result = dict(status='both prescribed canonical prefixes localized', cases=cases,
                  outside_coordinate=['1/3', '0'], precision_bits=256,
                  proposal_precision_digits=80, proposal_maxsteps=30,
                  proposal_tolerance='1e-65', proposal_saved_digits=60,
                  proposals=0 if old else 2, source_evaluations=0,
                  rational_transport_evaluations=0, scalar_evaluations=0,
                  parameter_subdivisions=0, input_sha256=bindings)
    if args.input:
        result['saved_input_sha256'] = sha(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'record_sha256': sha(args.output)}))


if __name__ == '__main__':
    main()
