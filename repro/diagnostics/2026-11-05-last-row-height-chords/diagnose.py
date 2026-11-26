"""One fixed diagnostic; no optimization, cover, or interval acceptance."""
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
from scipy.special import spence

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "experiments"))
import certify_mixed_cyclic_block_localization as source

P = np.pi


def g(z):
    return (spence(1-np.exp(-2j*P*z))-P*P/6)/(2j*P)


def gp(z):
    return np.log(1-np.exp(-2j*P*z))


def main():
    a = .30+np.sqrt(.060**2-.056**2)-.108j
    c = .35+np.sqrt(.083**2-.062**2)-.072j
    roots, _, _ = source.block([a.real, a.imag, c.real, c.imag], 0)
    s, b = roots
    residual = [gp(s+b)+gp(s+a)-2*gp(s)+2j*P*a,
                gp(s+b)+gp(b+c)-2*gp(b)+2j*P*c]
    assert max(abs(v) for v in residual) < 1e-11
    x = z = .45
    M = (g(s+a)+g(s+b)-2*g(s)-1.5*g(a)-g(b)+2j*P*a*s).real
    pa = (gp(s+a)-1.5*gp(a)+2j*P*s).real
    pb = (gp(s+b)-gp(b)).real
    row = 2*P*(max(-a.imag, 0)+max(b.imag, 0))-.5*g(x+1j*a.imag).real
    plane = M+pa*(x-a.real)+pb*(z-b.real)
    quadratic = ((x-a.real)**2+(z-b.real)**2)/2500000
    helper = ROOT / "experiments/certify_mixed_cyclic_block_localization.py"
    result = dict(
        status="diagnostic_only", own_type=3, external_types=[4, 3],
        exact_point_definition=dict(a="3/10+sqrt((3/50)^2-(7/125)^2)-27i/250",
                                    c="7/20+sqrt((83/1000)^2-(31/500)^2)-9i/125"),
        a=str(a), external_c=str(c), s=str(s), b=str(b), target=[x, z],
        original_log_residual=float(max(abs(v) for v in residual)),
        allocated_reference_rate=float(M), marginals=[float(pa), float(pb)],
        allocated_last_row_rate=float(row), affine_plane=float(plane),
        affine_excess=float(row-plane),
        affine_quadratic_excess=float(row-plane+quadratic),
        helper_sha256=hashlib.sha256(helper.read_bytes()).hexdigest(),
        diagnostic_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope="One floating fixed-point diagnostic. Joint actual type3 geometry "
              "excludes the external c; no actual-word or finite-kernel counterclaim.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
