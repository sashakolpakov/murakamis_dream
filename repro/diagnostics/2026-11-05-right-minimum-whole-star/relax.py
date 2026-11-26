#!/usr/bin/env python3
"""Fixed independent-row trials at the four saved whole-gradient candidates."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DRIVER = HERE/'diagnose.py'
SOURCE = HERE/'result.json'
spec = importlib.util.spec_from_file_location('whole_star_diagnostic', DRIVER)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
data = json.loads(SOURCE.read_text())
out = []
for item in data['minima']:
    for pair in itertools.product((.2, .4), repeat=2):
        rows = iter(pair)
        d.brentq = lambda *args, **kwargs: next(rows)
        value = d.evaluate(item['word'],
            np.array([complex(*v) for v in item['reference']]),
            item['real'], item['selection'])
        out.append(dict(word=item['word'], selection=item['selection'],
            fixed_rows=pair, derivative=value['derivative'],
            stars=value['conservative_stars']))
files = [Path(__file__).resolve(), DRIVER, SOURCE]
result = dict(scope='Floating diagnostic of a stronger independent-row relaxation at the four already preserved configurations. Nonstationary row derivatives are not derivatives of the true raw supremum; no transport failure follows.',
    cases=out, parameter_optimizations=0,
    dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in files})
(HERE/'relaxed_rows.json').write_text(json.dumps(result, indent=2)+'\n')
print('Minimum fixed-row trial:', min(row['derivative'] for row in out))
