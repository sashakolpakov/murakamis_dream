#!/usr/bin/env python3
"""Test a deliberately coarse, explicit seam comparison. Not a certificate."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
REAL = ROOT / 'repro/results/research-mixed-low-endpoint-connector-lower.json'
PROFILES = ROOT / 'repro/results/research-mixed-height-resolved-seam-sources.json'


def scalar(text):
    return float(text.split()[0].lstrip('['))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--constant-middle', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    real = json.loads(REAL.read_text())
    profiles = json.loads(PROFILES.read_text())['profiles']

    def source(name, height):
        knots = profiles[name]
        xs = [float(Fraction(row['height'])) for row in knots]
        ys = [float(Fraction(row['upper'])) for row in knots]
        return np.interp(height, xs, ys)

    def cutoff(x, b):
        return np.clip((x - .1) / (b - .1), 0, 1)

    def side(x, typ, selection, name, left):
        theta = np.pi * (.5 - x)
        taper = np.where(x <= .45, 1, 400 * (.5 - x) ** 2)
        factor = taper * cutoff(x, .12 if selection else .22)
        heights = [.014] if selection else ([-.057] if typ else [-.03, .02])
        options = [np.zeros_like(x)]
        for coefficient in heights:
            repaired = coefficient * factor
            for physical in (np.zeros_like(x), repaired):
                change = repaired - physical
                common = (-typ * theta / 2 + np.pi * selection)
                cost = common * (repaired + change)
                if left:
                    cost += np.pi / 2 * (np.maximum(repaired, 0)
                                        + np.maximum(-change, 0))
                else:
                    cost += np.pi / 2 * (np.maximum(-repaired, 0)
                                        + np.maximum(change, 0))
                options.append(source(name, physical) - source(name, 0) + cost)
        return np.maximum.reduce(options)

    grid = np.unique(np.r_[np.linspace(.1, .5, 801), .12, .22, .45])
    a, c = np.meshgrid(grid, grid, indexing='ij')
    wa, wc = (a - .1) / .4, (c - .1) / .4
    middle_factor = np.minimum(cutoff(a, .22), cutoff(c, .22))
    if args.constant_middle:
        middle_factor = np.ones_like(a)
    cases = []
    for alpha, beta, gamma in itertools.product((0, 1), repeat=3):
        for t in (real['middle_real_intervals'][str(beta)]):
            corners = {}
            for row in real['comparisons']:
                if row['types'] == [alpha, beta, gamma] and row['middle_real'] == t:
                    corners[(row['left_real'], row['right_real'])] = scalar(row['margin_lower'])
            margin = ((1-wa)*(1-wc)*corners[('1/10', '1/10')]
                      + wa*(1-wc)*corners[('1/2', '1/10')]
                      + (1-wa)*wc*corners[('1/10', '1/2')]
                      + wa*wc*corners[('1/2', '1/2')])
            tr = float(Fraction(t))
            middle_cost = middle_factor * np.pi * (.057 * (1-tr) if beta else .015)
            for sl, sr in itertools.product(range(alpha+1), range(gamma+1)):
                defect = (-margin + middle_cost
                          + side(a, alpha, sl, f'A{beta}{alpha}', True)
                          + side(c, gamma, sr, f'B{gamma}', False))
                index = np.unravel_index(np.argmax(defect), defect.shape)
                cases.append({'types': [alpha, beta, gamma], 'middle_real': t,
                              'selections': [sl, sr], 'maximum_on_grid': float(defect[index]),
                              'location': [float(a[index]), float(c[index])]})
    result = {
        'scope': 'Floating grid of an explicit conservative upper expression; no uniform sign certificate.',
        'construction': 'Corner concavity interpolation for the real pair; acute gradient bounds for the pair and AA corrections; independent physical/repaired height triangles; actual source height profiles.',
        'grid_size_each_axis': len(grid),
        'constant_middle_bound': args.constant_middle,
        'cases': cases,
        'worst': max(cases, key=lambda row: row['maximum_on_grid']),
        'dependencies_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (REAL, PROFILES)},
    }
    destination = args.output or Path(__file__).with_name(
        'constant-middle-result.json' if args.constant_middle else 'result.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['worst']))


if __name__ == '__main__':
    main()
