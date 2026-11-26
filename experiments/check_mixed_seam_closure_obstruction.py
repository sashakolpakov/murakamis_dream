#!/usr/bin/env python3
"""Fixed original-root obstruction to a crude seam closure estimate; no search."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_seam_closure_obstruction.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(q):
    q = F(q)
    return arb(q.numerator)/q.denominator


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=320)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-seam-closure-obstruction.json')
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, primary = {}, set(), []
    checks, margins, roots = [], {}, []

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in dependencies:
            assert dependencies[path] == digest, path
        dependencies[path] = digest
        return digest

    def inherit(path):
        bind(path)
        record = json.loads((ROOT/path).read_text())
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for p, h in record.get(field, {}).items():
                if p in bindings:
                    assert bindings[p] == h
                bindings[p] = h
                bind(p, h)
        # Recursive records are provenance, not additional theorem assumptions.
        for p in bindings:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherit(p)
        return record

    for stem, prefix, proof in [
        ('mixed_global_cotangent_roots', 'check', 'mixed_global_cotangent_roots'),
        ('mixed_half_endpoint_conditional_packet', 'check', 'mixed_half_endpoint_conditional_packet'),
        ('mixed_cyclic_block_localization', 'certify', 'mixed_cyclic_critical_localization'),
        ('mixed_finite_depth_boundary_potential', 'check', 'mixed_finite_depth_boundary_potential'),
        ('mixed_seam_boundary_potential_reduction', 'check', 'mixed_seam_boundary_potential_reduction'),
    ]:
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        pp, ss = f'notes/research_{proof}.md', f'experiments/{prefix}_{stem}.py'
        r = inherit(rp)
        assert r['status'] == 'passed', rp
        bind(pp, r['proof_sha256'])
        bind(ss, r['script_sha256'])
        primary.append(rp)
        if stem == 'mixed_seam_boundary_potential_reduction':
            assert F(r['finite_pair_gap']) == F(7, 25)
            assert r['validated_boundary_products'] == 2048
            assert r['validated_saved_cells'] == 18988

    def exact(name, value):
        assert value, name
        checks.append(name)

    def positive(name, value):
        assert value > 0, (name, str(value))
        margins[name] = str(value.lower())

    S, P, Q, D, zeta, ell = sp.symbols('S P Q D zeta ell')
    poly = S*S+(P+Q)*S-1+sp.I*(Q-P)
    exact('original exponent ratio gives the selected quadratic',
          sp.expand((S+P)*(S+Q)-(P-sp.I)*(Q+sp.I)-poly) == 0)
    disc = (P+Q)**2+4-4*sp.I*(Q-P)
    exact('explicit quadratic solution has the exact discriminant',
          sp.expand(poly.subs(S, (-(P+Q)+D)/2)-(D*D-disc)/4) == 0)
    original_exp = (1-zeta*zeta)**2-zeta*(1-zeta)**2
    exact('homogeneous exponential equation holds at the primitive cube root',
          sp.rem(original_exp, zeta*zeta+zeta+1, zeta) == 0)
    gp1, gp2 = ell+sp.I*sp.pi/6, ell-sp.I*sp.pi/6
    exact('homogeneous internal equation has original logarithmic lift zero',
          sp.expand(2*gp2-2*gp1+2*sp.pi*sp.I/3) == 0)
    ga, gb = gp2+2*sp.pi*sp.I/3-gp1, gp2-gp1
    exact('original tangent coefficients have the calibrated opposite signs',
          sp.expand(ga-sp.I*sp.pi/3) == 0 and sp.expand(gb+sp.I*sp.pi/3) == 0)
    exact('actual outer critical equation vanishes', sp.expand(ga+gb) == 0)
    exact('zero reference heights give zero reserved Q',
          F(151, 20)*0**2+F(11, 2)*0**2 == 0)

    pi, ii = arb.pi(), acb(0, 1)

    def g(z):
        return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)

    def gp(z):
        return (1-(-2*pi*ii*z).exp()).log()

    def phase(aq, bq):
        a, b = acb(ar(aq)), acb(ar(bq))
        p, q = (pi*a).cot(), (pi*b).cot()
        cot = (-(p+q)+((p+q)**2+4-4*ii*(q-p)).sqrt())/2
        name = aq+','+bq
        positive(name+' cotangent real part', cot.real)
        positive(name+' cotangent imaginary strip', 1-abs(cot.imag))
        s = ((cot+ii)/(cot-ii)).log()/(2*pi*ii)
        residual = gp(s+a)+gp(s+b)-2*gp(s)+2*pi*ii*a
        assert residual.contains(0)
        positive(name+' original logarithmic lift', pi-abs(residual.imag))
        for k, z in enumerate((s, s+a, s+b)):
            positive(name+f' regular strip{k} lower', z.real)
            positive(name+f' regular strip{k} upper', 1-z.real)
        roots.append(dict(a=aq, b=bq, cotangent=str(cot), root=str(s),
                          original_zero_lift=str(residual)))
        return (g(s+a)+g(s+b)-2*g(s)+2*pi*ii*a*s-g(a)-g(b)).real

    M0 = phase('1/3', '1/3')
    pairs = [('1/2', '1/10'), ('1/10', '1/3'),
             ('1/3', '1/10'), ('1/10', '1/2')]
    values = [phase(a, b) for a, b in pairs]
    cost = 4*M0-sum(values, arb(0))

    kappa, theta = F(1, 4000), F(1, 2)
    op, ol, oh = F(0), kappa, kappa+F(1, 10)*(F(1, 2)-F(9, 20))
    exact('low clamp occupation is saturated',
          400*(F(11, 50)-F(1, 3))**2 > 1)
    exact('upper clamp occupation is saturated',
          400*(F(9, 20)-F(1, 3))**2 > 1)
    exact('three exact symbol occupations',
          op == 0 and ol == F(1, 4000) and oh == F(21, 4000))
    psi = op+oh+ol
    closure_credit = theta*(oh+2*ol)
    terminal_credit = (1-theta)*psi
    component_credit = theta*(oh+oh)/2
    exact('left terminal triple occupation', psi == F(11, 2000))
    exact('entry and exit t shares', closure_credit == F(23, 8000))
    exact('stronger cyclic exit occupation credit', terminal_credit == F(11, 4000))
    exact('physical nonseam run endpoint-half occupation', component_credit == F(21, 8000))
    total_credit = closure_credit+terminal_credit+component_credit
    exact('all original occupation debits sum to33/4000', total_credit == F(33, 4000))
    proxy = cost-ar(total_credit)-ar('7/25')
    positive('four-action cost lower', cost-ar('0.88564961478'))
    positive('four-action cost upper', ar('0.88564961479')-cost)
    positive('closure proxy lower', proxy-ar('0.59739961478'))
    positive('closure proxy upper', ar('0.59739961479')-proxy)
    positive('crude closure proxy exceeds59/100', proxy-ar('59/100'))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in dependencies.items())
    out = dict(
        status='passed', precision_bits=args.precision, exact_checks=len(checks),
        checks=checks, strict_comparisons=len(margins), margins=margins,
        primary_records=len(primary), current_bindings=len(dependencies),
        reference='homogeneous type3, inner and outer coordinates1/3',
        physical_cycle_length_at_least=5, seam_fraction='0', theta='1/2',
        exit_state=['1/3', '1/2', '1/10'], entry_state=['1/10', '1/2', '1/3'],
        original_root_checks=roots, reference_action=str(M0),
        four_action_values=list(map(str, values)), four_action_cost=str(cost),
        total_occupation_debit='33/4000', finite_pair_gap='7/25', reserved_Q='0',
        closure_upper_proxy=str(proxy), certified_proxy_lower='59/100',
        optimizer_calls=0, sampled_parameter_boxes=0,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='A fixed outward obstruction to paying the explicit crude entry/exit upper estimate by the seam reserve. No sign of the actual common-potential difference, original signed source failure or whole-period asymptotic obstruction is inferred.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', len(checks), 'exact;', len(margins), 'outward;',
          len(primary), 'primary;', len(dependencies), 'bindings; proxy', proxy, flush=True)


if __name__ == '__main__':
    main()
