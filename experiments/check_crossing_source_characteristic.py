#!/usr/bin/env python3
"""Exact symbolic check of source characteristics against original trace transport.

The all-power proof is in research_crossing_source_characteristic_and_reset.md.
This check builds the polynomial source matrices directly and compares
their determinants with independently iterated original trace symbols.
"""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-power", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    z, y = sp.symbols("z y")
    h = 2-z-1/z
    trace_a = z+1/z-h/y
    trace_b = z+1/z-h*y
    trace_c = 4*z-2*z*z-(1-z)**2*(y+1/y)
    records = []
    for power in range(1, args.max_power+1):
        trace_b, trace_c = sp.expand(8-trace_a*trace_b-trace_c), trace_b
        size = (power+1)//2
        matrix_b = sp.zeros(size)
        for i in range(size):
            for j in range(size):
                tail = size-1-max(i, j)
                matrix_b[i, j] = z**(abs(i-j)+1)*(
                    sum(z**(2*r) for r in range(tail+1))
                    - z*sum(z**(2*r) for r in range(tail)))
        diagonal = [1-1/z]*size
        if power % 2:
            diagonal[0] = -1/z
        transfer = matrix_b*sp.diag(*diagonal)
        characteristic = sp.factor((y*sp.eye(size)-transfer).det())
        multiplier = (-1)**power*(z-1)**2/(z**(power+1)*y**power)
        if power % 2 == 0:
            multiplier *= 1+y
        cap_residual = sp.cancel(trace_b-2-multiplier*characteristic**2)
        determinant_residual = sp.factor(
            transfer.det()-(-1)**size*(1-z)**(power-1))
        reset = transfer.subs(z, 1)
        expected_reset = sp.zeros(size)
        if power % 2:
            for i in range(size):
                expected_reset[i, 0] = -1
            assert sp.cancel(characteristic.subs(y, -1)) == 0
        assert reset == expected_reset
        assert matrix_b.subs(z, 1) == sp.ones(size)
        assert cap_residual == 0, (power, cap_residual)
        assert determinant_residual == 0, (power, determinant_residual)
        records.append({"power": power, "channel_dimension": size,
                        "characteristic": str(characteristic),
                        "cap_square_residual": str(cap_residual),
                        "determinant_residual": str(determinant_residual),
                        "reset_rank": reset.rank()})
    report = {
        "status": "pass", "arithmetic": "exact rational symbolic",
        "scope": "Source characteristic, original cap square, elementary factors, "
                 "and actual limiting reset; not a whole-color asymptotic test.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "pass", "powers": len(records),
                      "residuals": "zero exactly", "output": str(args.output)}))


if __name__ == "__main__":
    main()
