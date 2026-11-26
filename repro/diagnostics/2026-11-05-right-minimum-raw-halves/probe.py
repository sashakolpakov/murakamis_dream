#!/usr/bin/env python3
"""Four fixed floating raw-half values; no parameter search or certificate."""
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / 'notes/research_mixed_complex_right_row_reduction.md'


def gp(z):
    return np.log(1-np.exp(-2j*np.pi*z))


def main():
    t, h, slope = .22, -.057, -.057/.12
    z = t+1j*h
    values = []
    for epsilon in (0, 1):
        for first in (0, 1):
            def row_derivative(u):
                return (np.log(2*np.cos(np.pi*u))+gp(z+u).real
                        -(2+epsilon)*np.log(2*np.sin(np.pi*u))
                        -2*np.pi*first*h)
            row = brentq(row_derivative, .2, .4)
            gradient = gp(z+row)-1.5*gp(z)+2j*np.pi*first*row
            gauge = -1.5 if first else 1.5
            values.append(dict(
                epsilon=epsilon, moving_endpoint_is_first=bool(first),
                row=float(row), row_residual=float(row_derivative(row)),
                horizontal_derivative=float(gradient.real),
                path_derivative=float(((1+1j*slope)*gradient).real),
                old_gauged_half=float(((1+1j*slope)*(gradient+1j*gauge)).real)))
    files = [Path(__file__).resolve(), INPUT]
    result = dict(
        scope='Floating fixed-point diagnostic only. The four pairs (own type, orientation) are independent enlarged domains; they are not four actual cyclic configurations. No interval root, full transport failure, finite-source failure or uniform sign is asserted.',
        moving_type=1, t=t, h=h, height_derivative=slope,
        selection=0, right_target=.5, values=values,
        parameter_optimizations=0, fixed_scalar_root_solves=4,
        dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    Path(__file__).with_name('result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(values, indent=2))


if __name__ == '__main__':
    main()
