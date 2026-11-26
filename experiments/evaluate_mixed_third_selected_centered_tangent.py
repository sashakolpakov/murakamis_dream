"""Centered third-selection profile supports with original compensation.

Import-safe. Evaluation uses the supplied reference and exact trial only;
no reference solve, optimization, subdivision or direct full-box action
difference is performed by evaluate(). Proposal delegation is explicit.
"""
from fractions import Fraction as F
import hashlib
from pathlib import Path

from flint import acb, ctx
import evaluate_mixed_third_selected_tangent as old

ROOT = Path(__file__).resolve().parents[1]
PINNED = {
    'experiments/evaluate_mixed_third_selected_tangent.py':
        'e8ec90f9024a9242961a23e81fa31843c9abf519d7eecdbecc68495822d07b13',
    'notes/research_mixed_third_selected_recentered_defect.md':
        '7bb5864714f64eb55792096c12072d59207f37056cef16a4b0ba4ee11e4d4e1d',
    'notes/research_mixed_third_selected_centered_tangent_evaluation.md':
        'f5a7eace4e41e121f406799049af3537383c23f8a48fb873451ffb74cc67b2d6',
}
PRECISION = 256
NAMES = ('a', 'u', 'z', 'v', 'b')
H = F(1, 100)
Inconclusive = old.Inconclusive
_STATE = None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def initialize():
    global _STATE
    if any(digest is None for digest in PINNED.values()):
        raise ValueError('unfinished centered tangent bindings')
    for name, digest in PINNED.items():
        if sha(ROOT/name) != digest:
            raise ValueError('changed centered tangent input: '+name)
    bindings = dict(PINNED)
    inherited = old.initialize()
    for name, digest in inherited['bindings'].items():
        if name in bindings and bindings[name] != digest:
            raise ValueError('conflicting centered tangent binding: '+name)
        bindings[name] = digest
    own_name = str(Path(__file__).resolve().relative_to(ROOT))
    bindings[own_name] = sha(Path(__file__))
    _STATE = {'bindings': bindings}
    return {
        'bindings': dict(bindings),
        'precision_bits': PRECISION,
        'target_coordinates': list(NAMES),
        'method': 'midpoint action difference plus full-box reference derivatives',
        'complete_evaluation_counts': {'g': 27, 'gp': 56, 'cotangent': 4},
        'proposal_role': 'unchanged frozen proposal; exact trial and outward bound supply proof',
    }


def propose_trial(reference, alpha, beta, left, right, nu):
    if _STATE is None:
        initialize()
    return old.propose_trial(reference, alpha, beta, left, right, nu)


def _gradient(q, alpha, beta, p):
    """Original F-gradient; cache the own logarithms for target support."""
    a, u, z, v, b = q
    own = {name: p.gp(w) for name, w in zip(NAMES, q)}
    au, uz, zv, vb = [p.gp(w) for w in (a+u, u+z, z+v, v+b)]
    result = [
        au-old.rat(1+F(alpha, 2))*own['a']+2*p.pi*p.ii*u,
        au+uz-3*own['u']+2*p.pi*p.ii*a,
        uz+zv-3*own['z']+2*p.pi*p.ii*v,
        zv+vb-(2+beta)*own['v']+2*p.pi*p.ii*z,
        vb-old.rat(1+F(beta, 2))*own['b'],
    ]
    return result, own


def _target(q, trial, left, right):
    out = [acb(old.rat(x), w.imag) for x, w in zip(trial, q)]
    out[2] = acb(old.rat(trial[2]), old.rat(H))
    if left != 'main':
        out[1] = acb(old.rat(trial[1]))
    if right != 'main':
        out[3] = acb(old.rat(trial[3]))
    return out


def evaluate(reference, anchor, alpha, beta, left, right, nu, trial):
    """Enclose one original profile on its full target product."""
    if _STATE is None:
        initialize()
    result = {
        'status': 'inconclusive', 'alpha': alpha, 'beta': beta,
        'left': left, 'right': right, 'nu': nu, 'precision_bits': PRECISION,
        'trial_enclosure_method': 'centered original difference of actions',
    }
    calls = {
        'midpoint_defect_evaluations': 0,
        'full_box_gradient_evaluations': 0,
        'cotangent_evaluations': 0,
        'reference_proposals': 0,
        'target_optimizations': 0,
        'parameter_subdivisions': 0,
    }
    p = None
    try:
        if alpha not in (0, 1) or nu not in (0, 1):
            raise ValueError('invalid type or Fourier flag')
        if ctx.prec != PRECISION:
            raise ValueError('caller must set interval precision to 256 bits')
        box = old.target_box(beta, left, right)
        trial = tuple(map(F, trial))
        if len(trial) != 5 or not all(lo <= x <= hi for x, (lo, hi) in zip(trial, box)):
            raise ValueError('trial is outside the original target box')
        result['trial'] = list(map(str, trial))
        current = old.payload(reference, alpha, beta)
        anchored = old.payload(anchor, alpha, beta, anchor=True)
        current_hash, anchor_hash = old.canonical_hash(current), old.canonical_hash(anchored)
        result['reference_coordinate_sha256'] = current_hash
        result['anchor_coordinate_sha256'] = anchor_hash
        result['reference_coordinate_endpoints'] = current
        result['anchor_coordinate_endpoints'] = anchored
        midpoint, displacements = {}, {}
        for name in NAMES:
            midpoint[name], displacements[name] = {}, {}
            for part in ('real', 'imag'):
                lo, hi = old.bounds(current[name][part])
                middle = (lo+hi)/2
                midpoint[name][part] = str(middle)
                displacements[name][part] = [str(lo-middle), str(hi-middle)]
        result['exact_midpoint'] = midpoint
        result['reference_displacements'] = displacements
        r = [old.read_complex(current[name]) for name in NAMES]
        r0 = [old.read_complex(anchored[name]) for name in NAMES]
        for name, w in zip(NAMES, r):
            real, imag = old.ends(w.real), old.ends(w.imag)
            if not (F(11, 50) < real[0] <= real[1] < F(9, 20)
                    and -F(3, 25) < imag[0] <= imag[1] < F(3, 25)):
                raise Inconclusive('current reference is outside the broad target product: '+name)
        center = [
            acb(old.rat(midpoint[name]['real']), old.rat(midpoint[name]['imag']))
            for name in NAMES
        ]
        w, wc = _target(r, trial, left, right), _target(center, trial, left, right)
        result['reference_box'] = dict(zip(NAMES, map(old.crecord, r)))
        result['target_image'] = dict(zip(NAMES, map(old.crecord, w)))
        result['midpoint_image'] = dict(zip(NAMES, map(old.crecord, center)))
        result['midpoint_target_image'] = dict(zip(NAMES, map(old.crecord, wc)))
        p = old.Primitive()
        calls['midpoint_defect_evaluations'] += 1
        f0, fg0 = p.phase(center, alpha, beta)
        target0, _ = p.phase(wc, alpha, beta)
        da0 = acb(old.rat(trial[0])-center[0].real)
        db0 = acb(old.rat(trial[4])-center[4].real)
        value = target0-f0-fg0[0]*da0-fg0[4]*db0
        value += (1-nu)*p.g(wc[2])-2*p.pi*old.rat(H)*nu
        result['midpoint_defect'] = old.rrecord(value.real)
        result['midpoint_reference_action'] = old.crecord(f0)
        result['midpoint_target_action'] = old.crecord(target0)
        result['midpoint_reference_gradient'] = dict(zip(NAMES, map(old.crecord, fg0)))
        result['midpoint_boundary_displacements'] = {'a': old.crecord(da0), 'b': old.crecord(db0)}

        calls['full_box_gradient_evaluations'] += 1
        fr, _ = _gradient(r, alpha, beta, p)
        calls['full_box_gradient_evaluations'] += 1
        fw, own_w = _gradient(w, alpha, beta, p)
        result['reference_gradient'] = dict(zip(NAMES, map(old.crecord, fr)))
        result['target_gradient'] = dict(zip(NAMES, map(old.crecord, fw)))
        result['target_selected_logarithm'] = old.crecord(own_w['z'])
        result['incoming_marginal'] = old.crecord(fr[0])
        result['outgoing_marginal'] = old.crecord(fr[4])
        cotangents, k = {}, {}
        for name, argument in (
            ('a+u', r[0]+r[1]), ('a', r[0]),
            ('v+b', r[3]+r[4]), ('b', r[4]),
        ):
            p.regular(argument)
            calls['cotangent_evaluations'] += 1
            reciprocal = 1/(p.pi*argument).sin()
            if not reciprocal.is_finite():
                raise Inconclusive('boundary Hessian sine not separated: '+name)
            k[name] = p.pi*(p.pi*argument).cos()*reciprocal-p.pi*p.ii
            cotangents[name] = {'argument': old.crecord(argument), 'g_second': old.crecord(k[name])}
        result['boundary_second_derivatives'] = cotangents
        aa = k['a+u']-old.rat(1+F(alpha, 2))*k['a']
        au = k['a+u']+2*p.pi*p.ii
        bv = k['v+b']
        bb = k['v+b']-old.rat(1+F(beta, 2))*k['b']
        result['boundary_hessian'] = {
            name: old.crecord(entry) for name, entry in
            (('aa', aa), ('au', au), ('bv', bv), ('bb', bb))
        }
        da = acb(old.rat(trial[0])-r[0].real)
        db = acb(old.rat(trial[4])-r[4].real)
        result['boundary_displacements'] = {'a': old.crecord(da), 'b': old.crecord(db)}
        response = [aa*da, au*da, acb(0), bv*db, bb*db]
        lambdas = (1, int(left == 'main'), 0, int(right == 'main'), 1)
        dx = [(-(fr[j] if j not in (0, 4) else 0)-response[j]).real for j in range(5)]
        dy = [-(lambdas[j]*fw[j]-fr[j]-response[j]).imag for j in range(5)]
        result['boundary_response_terms'] = dict(zip(NAMES, map(old.crecord, response)))
        result['lambda'] = list(lambdas)
        lower, upper = old.ends(value.real)
        terms = []
        for name, real_slope, imag_slope in zip(NAMES, dx, dy):
            for part, slope in (('real', real_slope), ('imag', imag_slope)):
                gl, gh = old.ends(slope)
                dl, dh = map(F, displacements[name][part])
                products = [gl*dl, gl*dh, gh*dl, gh*dh]
                low, high = min(products), max(products)
                terms.append({
                    'name': name, 'part': part, 'derivative': old.rrecord(slope),
                    'displacement': [str(dl), str(dh)],
                    'corner_products': list(map(str, products)),
                    'lower_rational': str(low), 'upper_rational': str(high),
                })
                lower += low
                upper += high
        result['mean_value_terms'] = terms
        result['centered_trial_defect'] = old.frecord((lower, upper))
        result['trial_defect'] = result['centered_trial_defect']

        # The Fourier selected logarithm affects target support but not
        # reference derivatives, since the selected target height is fixed.
        target_gradient = list(fw)
        target_gradient[0] -= fr[0]
        target_gradient[4] -= fr[4]
        target_gradient[2] += (1-nu)*own_w['z']
        support = []
        for name, x, (lo, hi), slope in zip(NAMES, trial, box, target_gradient):
            gl, gh = old.ends(slope.real)
            products = [gl*(lo-x), gh*(lo-x), gl*(hi-x), gh*(hi-x)]
            support.append({
                'name': name, 'trial': str(x), 'lower': str(lo), 'upper': str(hi),
                'gradient': old.rrecord(slope.real),
                'corner_products': list(map(str, products)),
                'upper_rational': str(max(products)),
            })
        support_upper = sum((F(term['upper_rational']) for term in support), F(0))
        result['support_terms'] = support
        result['support_correction_rational'] = str(support_upper)
        upper += support_upper
        result['upper_rational'] = str(upper)
        pl0, pr0 = p.marginals(r0, alpha, beta)
        current_values = {
            'pL': old.crecord(fr[0]), 'pR': old.crecord(fr[4]),
            'a': old.crecord(r[0]), 'b': old.crecord(r[4]),
        }
        anchor_values = {
            'pL': old.crecord(pl0), 'pR': old.crecord(pr0),
            'a': old.crecord(r0[0]), 'b': old.crecord(r0[4]),
        }
        compensation = old.compensation_record(
            current_values, anchor_values, current_hash, anchor_hash)
        compensated = upper-F(compensation['C0']['lower_rational'])
        result['compensation_record'] = compensation
        result['compensated_upper_rational'] = str(compensated)
        result['compensated_upper_decimal_display'] = float(compensated)
        result['status'] = 'enclosed'
    except Inconclusive as error:
        result['reason'] = str(error)
    except Exception as error:
        result.update(status='error', reason=repr(error))
    result['primitive_calls'] = dict(p.calls) if p else {'g': 0, 'gp': 0}
    result['enclosure_calls'] = calls
    return result
