"""Bounded extraction test: enlarge selected-reset target square to [.22,.5]^2.

Uses every old root witness and reference cell, without proposal or refinement.
This is a diagnostic re-evaluation pending source/curvature proof review.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import ast
import importlib.util
import json
import time

from flint import arb, acb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HELPER = ROOT/'experiments/certify_mixed_selected_reset_plateau_support.py'
spec = importlib.util.spec_from_file_location('old_selected_reset', HELPER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def main():
    start = time.monotonic()
    ctx.prec = 256
    m.core.pi, m.core.ii = arb.pi(), acb(0, 1)
    record = ROOT/'repro/results/research-mixed-selected-reset-plateau-support.json'
    paths = [Path(__file__), HELPER, record, m.PROOF, m.HELPER]
    bindings = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    saved = json.loads(record.read_text())
    assert saved['status'] == 'passed'
    assert saved['proof_sha256'] == bindings[str(m.PROOF.relative_to(ROOT))]
    assert saved['script_sha256'] == bindings[str(HELPER.relative_to(ROOT))]
    for p, digest in saved['dependencies'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == digest
        bindings[p] = digest
    # The sole acceptance-domain alteration. All target points remain the old
    # rational points; the new optimization interval is used only in the exact
    # quadratic upper bound, with the same already-proved curvature constant.
    m.HIGH = F(1, 2)
    # Report the actual enlarged bound even when it misses the old -.01 goal.
    # Root/branch assertions and witness verification remain unchanged.
    fn = next(n for n in ast.parse(HELPER.read_text()).body
              if isinstance(n, ast.FunctionDef) and n.name == 'test')
    found = []
    class ReportUpper(ast.NodeTransformer):
        def visit_If(self, node):
            if (isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not)
                and isinstance(node.test.operand, ast.Compare)
                and isinstance(node.test.operand.left, ast.Name)
                and node.test.operand.left.id == 'upper'):
                found.append(True)
                return None
            return self.generic_visit(node)
    fn = ReportUpper().visit(fn)
    assert len(found) == 1
    ast.fix_missing_locations(fn)
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(HELPER), 'exec'), m.__dict__)
    cells, failures, maxima = 0, [], {}
    for row in saved['cases']:
        case = tuple(row['case'])
        m.core.cover([r['address'] for r in row['leaves']])
        for leaf in row['leaves']:
            assert time.monotonic()-start < 120
            ans = m.test(case, leaf['address'], leaf['witness'])
            cells += 1
            if ans is None:
                failures.append(dict(case=list(case), address=leaf['address']))
            else:
                key = str(case[:4])
                val = ans[1].upper()
                maxima[key] = val if key not in maxima else max(val, maxima[key])
    assert len(saved['cases']) == 128 and cells == saved['cells'] == 1023
    assert bindings == {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in bindings}
    result = dict(status='complete', scope='Existing 128 reference domains/1023 cells and original saved root witnesses only. Both target reals enlarged to [.22,.5], selected height .014, other height zero, both forcing branches. No new optimization, root proposal, subdivision or theorem claim.',
                  products=128, cells=cells, failures=failures,
                  target_interval=['11/50', '1/2'], old_threshold_for_comparison='-1/100',
                  maxima={k: str(v) for k, v in maxima.items()},
                  elapsed_seconds=time.monotonic()-start, dependencies=bindings)
    (HERE/'saved-selected-upper.json').write_text(json.dumps(result, indent=2)+'\n')
    print('COMPLETE', cells, 'failures', len(failures), 'worst', max(maxima.values()), 'seconds', result['elapsed_seconds'])


if __name__ == '__main__':
    main()
