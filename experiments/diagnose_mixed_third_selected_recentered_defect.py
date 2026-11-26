#!/usr/bin/env python3
"""One centered-defect diagnostic on one frozen unresolved cell.

No new reference solve, optimization, subdivision, or input selection.
The source pass and its pending frontier remain unchanged.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz'
SOURCE_SHA = 'e63cdc8ceb70046bac13ba855542657623c4b00e792ad367b0d7369c914a461e'
AUDIT = 'repro/results/research-mixed-third-selected-product-boundary-saved-audit.json'
AUDIT_SHA = '9aa582ab0e3ab3914bd89737ed84e5963ee7bf65280ba1e2084bacf7e7b50647'
PINNED = {
    'notes/research_mixed_third_selected_recentered_defect.md':
        '7bb5864714f64eb55792096c12072d59207f37056cef16a4b0ba4ee11e4d4e1d',
    'notes/research_mixed_third_selected_recentered_diagnostic_protocol.md':
        'ac5885465f6c73cae7db88327f9ae464800a3059f3f19b0298fca763c52f13a5',
    'experiments/check_mixed_third_selected_product_boundary_record.py':
        '7ac82eedb454d2812a0c610b33a54cfb7a96a791cdb8e5844fce60e8c4235615',
}
ADDRESS = '0000110000111110'
NAMES = ('a', 'u', 'z', 'v', 'b')
DELTA = F(1, 2000)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        if sha(ROOT/name) != digest:
            raise ValueError('changed input: ' + name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not PINNED:
        raise ValueError('unfinished centered-defect proof bindings')
    bindings = dict(PINNED)
    bindings.update({SOURCE: SOURCE_SHA, AUDIT: AUDIT_SHA})
    verify(bindings)
    with gzip.open(ROOT/SOURCE, 'rt') as stream:
        original = json.load(stream)
    for name, digest in original['input_sha256'].items():
        if name in bindings and bindings[name] != digest:
            raise ValueError('conflicting source input binding: '+name)
        bindings[name] = digest
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)
    audit = json.loads((ROOT/AUDIT).read_text())
    assert audit['status'] == 'exact saved product-boundary audit passed'
    assert audit['source_sha256'] == SOURCE_SHA and not audit['full_domain_proved']
    assert original['stop_reason'] == 'first unresolved depth-limit cell'
    node = original['nodes'][-1]
    assert node['status'] == 'unresolved' and node['address'] == ADDRESS
    assert node['case_index'] == 0 and node['alpha'] == node['beta'] == node['sigma'] == 0
    assert node['chart_a'] == node['chart_c'] == 'k3_circle_left'
    expected = list(itertools.product(('main', 'left', 'half'), ('main', 'half'), (0, 1)))
    assert [(p['incoming_profile'], p['outgoing_profile'], p['nu'])
            for p in node['profiles']] == expected
    assert all(p['status'] == 'enclosed' for p in node['profiles'])

    # Import the frozen primitive only after its source hash has been checked.
    from flint import acb, ctx
    import evaluate_mixed_third_selected_tangent as old
    ctx.prec = 256
    old.initialize()
    coordinates = node['reference']['coordinates']
    midpoint = {}
    displacements = {}
    for name in NAMES:
        midpoint[name], displacements[name] = {}, {}
        for part in ('real', 'imag'):
            lo, hi = old.bounds(coordinates[name][part])
            middle = (lo+hi)/2
            midpoint[name][part] = str(middle)
            displacements[name][part] = [str(lo-middle), str(hi-middle)]
    counts = dict(reference_proposals=0, target_optimizations=0,
                  parameter_subdivisions=0, midpoint_defect_evaluations=0,
                  full_box_gradient_evaluations=0, cotangent_evaluations=0,
                  primitive_g=0, primitive_gp=0)

    def gradient(q, alpha, beta, p):
        a, u, z, v, b = q
        g = {name: p.gp(w) for name, w in zip(NAMES, q)}
        au, uz, zv, vb = [p.gp(w) for w in (a+u, u+z, z+v, v+b)]
        return [au-old.rat(1+F(alpha, 2))*g['a']+2*p.pi*p.ii*u,
                au+uz-3*g['u']+2*p.pi*p.ii*a,
                uz+zv-3*g['z']+2*p.pi*p.ii*v,
                zv+vb-(2+beta)*g['v']+2*p.pi*p.ii*z,
                vb-old.rat(1+F(beta, 2))*g['b']]

    def target(q, trial, left, right):
        out = [acb(old.rat(x), w.imag) for x, w in zip(trial, q)]
        out[2] = acb(old.rat(trial[2]), old.rat(F(1, 100)))
        if left != 'main':
            out[1] = acb(old.rat(trial[1]))
        if right != 'main':
            out[3] = acb(old.rat(trial[3]))
        return out

    rows = []
    unexpected = None
    for index, saved in enumerate(node['profiles']):
        left, right, nu = expected[index]
        row = dict(profile_index=index, incoming_profile=left,
                   outgoing_profile=right, nu=nu, status='inconclusive',
                   saved_profile_sha256=canonical_hash(saved),
                   trial=saved['trial'])
        rows.append(row)
        p = old.Primitive()
        try:
            trial = tuple(map(F, saved['trial']))
            r = [old.read_complex(coordinates[name]) for name in NAMES]
            center = [acb(old.rat(midpoint[name]['real']), old.rat(midpoint[name]['imag']))
                      for name in NAMES]
            w, wc = target(r, trial, left, right), target(center, trial, left, right)
            row['reference_box'] = dict(zip(NAMES, map(old.crecord, r)))
            row['target_image'] = dict(zip(NAMES, map(old.crecord, w)))
            row['midpoint_image'] = dict(zip(NAMES, map(old.crecord, center)))
            row['midpoint_target_image'] = dict(zip(NAMES, map(old.crecord, wc)))
            counts['midpoint_defect_evaluations'] += 1
            f0, fg0 = p.phase(center, node['alpha'], node['beta'])
            target0, _ = p.phase(wc, node['alpha'], node['beta'])
            da0 = acb(old.rat(trial[0])-center[0].real)
            db0 = acb(old.rat(trial[4])-center[4].real)
            value = target0-f0-fg0[0]*da0-fg0[4]*db0
            value += (1-nu)*p.g(wc[2])-2*p.pi*old.rat(F(1, 100))*nu
            row['midpoint_defect'] = old.rrecord(value.real)
            row['midpoint_reference_action'] = old.crecord(f0)
            row['midpoint_reference_gradient'] = dict(zip(NAMES, map(old.crecord, fg0)))
            row['midpoint_boundary_displacements'] = {'a': old.crecord(da0), 'b': old.crecord(db0)}
            counts['full_box_gradient_evaluations'] += 1
            fr = gradient(r, node['alpha'], node['beta'], p)
            counts['full_box_gradient_evaluations'] += 1
            fw = gradient(w, node['alpha'], node['beta'], p)
            row['reference_gradient'] = dict(zip(NAMES, map(old.crecord, fr)))
            row['target_gradient'] = dict(zip(NAMES, map(old.crecord, fw)))
            kp = {}
            for name, argument in (('a+u', r[0]+r[1]), ('a', r[0]),
                                   ('v+b', r[3]+r[4]), ('b', r[4])):
                p.regular(argument)
                counts['cotangent_evaluations'] += 1
                sine = (p.pi*argument).sin()
                reciprocal = 1/sine
                if not reciprocal.is_finite():
                    raise old.Inconclusive('boundary Hessian sine not separated: '+name)
                kp[name] = p.pi*(p.pi*argument).cos()*reciprocal-p.pi*p.ii
            aa = kp['a+u']-old.rat(1+F(node['alpha'], 2))*kp['a']
            au = kp['a+u']+2*p.pi*p.ii
            bv = kp['v+b']
            bb = kp['v+b']-old.rat(1+F(node['beta'], 2))*kp['b']
            row['boundary_hessian'] = {name: old.crecord(v) for name, v in
                                       (('aa', aa), ('au', au), ('bv', bv), ('bb', bb))}
            da = acb(old.rat(trial[0])-r[0].real)
            db = acb(old.rat(trial[4])-r[4].real)
            row['boundary_displacements'] = {'a': old.crecord(da), 'b': old.crecord(db)}
            response = [aa*da, au*da, acb(0), bv*db, bb*db]
            lambdas = (1, int(left == 'main'), 0, int(right == 'main'), 1)
            real_derivatives = [(-(fr[j] if j not in (0, 4) else 0)-response[j]).real
                                for j in range(5)]
            imag_derivatives = [-(lambdas[j]*fw[j]-fr[j]-response[j]).imag
                                for j in range(5)]
            row['boundary_response_terms'] = dict(zip(NAMES, map(old.crecord, response)))
            row['lambda'] = list(lambdas)
            terms = []
            lower, upper = old.ends(value.real)
            for name, dx, dy in zip(NAMES, real_derivatives, imag_derivatives):
                for part, slope in (('real', dx), ('imag', dy)):
                    gl, gh = old.ends(slope)
                    dl, dh = map(F, displacements[name][part])
                    products = [gl*dl, gl*dh, gh*dl, gh*dh]
                    low, high = min(products), max(products)
                    terms.append({'name': name, 'part': part,
                                  'derivative': old.rrecord(slope),
                                  'displacement': [str(dl), str(dh)],
                                  'corner_products': list(map(str, products)),
                                  'lower_rational': str(low), 'upper_rational': str(high)})
                    lower += low
                    upper += high
            row['mean_value_terms'] = terms
            row['centered_trial_defect'] = old.frecord((lower, upper))
            row['old_trial_defect'] = saved['trial_defect']
            old_lower, old_upper = old.bounds(saved['trial_defect'])
            if max(lower, old_lower) > min(upper, old_upper):
                raise ValueError('centered and direct defect enclosures are disjoint')
            support = sum((F(t['upper_rational']) for t in saved['support_terms']), F(0))
            compensation = saved['compensation_record']['C0']
            result = upper+support-F(compensation['lower_rational'])
            row.update(original_support_terms=saved['support_terms'],
                       support_correction_rational=str(support),
                       original_compensation_record=saved['compensation_record'],
                       original_compensated_upper_rational=saved['compensated_upper_rational'],
                       centered_compensated_upper_rational=str(result),
                       comparison_proved=result < -DELTA,
                       status='centered comparison enclosed')
        except old.Inconclusive as error:
            row['reason'] = str(error)
        except Exception as error:
            row.update(status='unexpected error', reason=repr(error))
            unexpected = repr(error)
        finally:
            row['primitive_calls'] = dict(p.calls)
            counts['primitive_g'] += p.calls['g']
            counts['primitive_gp'] += p.calls['gp']
        print(json.dumps({'profile': [left, right, nu], 'status': row['status'],
                          'upper': float(F(row['centered_compensated_upper_rational']))
                          if 'centered_compensated_upper_rational' in row else None}), flush=True)
        if unexpected is not None:
            for j in range(index+1, len(expected)):
                l, rr, n = expected[j]
                rows.append(dict(profile_index=j, incoming_profile=l, outgoing_profile=rr,
                                 nu=n, status='unexamined after unexpected error'))
            break
    changed = [name for name, digest in bindings.items() if sha(ROOT/name) != digest]
    proved = not changed and all(row.get('comparison_proved') is True for row in rows)
    result = dict(status='fixed saved-cell diagnostic completed' if unexpected is None else 'stopped with unexpected error',
                  source=SOURCE, source_sha256=SOURCE_SHA, source_node_index=node['node_index'],
                  source_node_sha256=canonical_hash(node), address=ADDRESS,
                  source_reference_coordinate_sha256=canonical_hash(coordinates),
                  exact_midpoint=midpoint, reference_displacements=displacements,
                  input_sha256=bindings, changed_inputs=changed, precision_bits=256,
                  delta_rational=str(DELTA), profiles=rows, counts=counts,
                  cell_comparison_proved=proved, whole_domain_proved=False,
                  finite_source_suppression_claimed=False, unexpected_error=unexpected)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({'status': result['status'], 'cell_comparison_proved': proved,
                      'counts': counts, 'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
