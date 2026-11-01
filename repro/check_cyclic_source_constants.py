"""Rational enclosures for the fixed constants of the cyclic source proof.

This verifies finitely many analytic constants, not a sample of diagram
sizes. The all-size statement is the separate trigonometric argument.
The interval engine uses integer outward rounding and rational series
with explicit remainders. No floating-point operation is used here.
"""
from fractions import Fraction as F
from math import isqrt
import hashlib
from pathlib import Path
import argparse
import importlib.util
import json

if not __debug__:
    raise SystemExit("Run this verifier without Python's -O option.")

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "experiments/verify_conway_two_leaf_block_alias_certificate.py"
spec = importlib.util.spec_from_file_location("cyclic_interval_engine", ENGINE)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)
I, S, PI, ZETA, logi = engine.I, engine.S, engine.PI, engine.ZETA, engine.logi


def sqrti(x):
    x = engine.iv(x)
    assert x.lo >= 0
    lo = isqrt(x.lo * S)
    hi = isqrt(x.hi * S)
    if hi * hi < x.hi * S:
        hi += 1
    return I(lo, hi, raw=True)


def atani(x):
    x = engine.iv(x)
    assert x.lo >= 0
    multiplier = 1
    while 2 * x.hi > S:
        x = x / (1 + sqrti(1 + x*x))
        multiplier *= 2
    # atan(x) = 2 atan(x/(1+sqrt(1+x*x))), and the alternating
    # remainder after n terms has magnitude at most x^(2n+1)/(2n+1).
    n = 80
    term = x
    value = I(0)
    for j in range(n):
        value += (-1)**j * term / F(2*j+1)
        term = term*x*x
    tail = term / F(2*n+1)
    return multiplier*(value + I(-tail.hi, tail.hi, raw=True))


def integrated_log_sine(t):
    """Enclose integral_0^t log(2*sin(pi*u)) du for 0<t<1/2."""
    t = engine.iv(t)
    assert 0 < t.lo <= t.hi < S//2
    value = t*logi(2*PI*t)-t
    for n in range(1, 21):
        value -= ZETA[n]*(t**(2*n+1))/F(n*(2*n+1))
    # zeta(2n)<2 and (n(2n+1)) >= 21*43 for n>=21.
    tail = 2*(t**43)/(F(21*43)*(1-t*t))
    return value + I(-tail.hi, 0, raw=True)


cache = {}
def Q(*weights):
    key = tuple(sorted(F(w) for w in weights))
    assert len(key) == 3 and key[0] >= 0 and key[-1] > 0
    if key in cache:
        return cache[key]
    positive = [w for w in key if w]
    if len(positive) == 1:
        result = logi(positive[0])/2
    else:
        D = sqrti(sum(key[i]*key[j] for i in range(3) for j in range(i+1,3)))
        result = I(0)
        for w in positive:
            t = atani(I(w)/D)/PI
            result += (-integrated_log_sine(t)
                       -integrated_log_sine(F(1,2)-t) + t*logi(w))
    cache[key] = result
    return result


def one_edge(r):
    return Q(1, r, 0)


def verify():
    a, c = F(9,4), F(27,4)
    distortion = I(F(16,9))-1+logi(F(9,16))
    boundary_balance = one_edge(a)-logi(a)
    near_one = one_edge(a)+Q(1,c,a)-logi(c)
    near_two = Q(1,c,a)-logi(c)/2
    interior_one = one_edge(F(1,3))+one_edge(2)-logi(2)
    interior_two = one_edge(2)-logi(2)/2
    changed_neighbor = one_edge(F(4,27))+one_edge(2)-logi(2)
    change = 2*(one_edge(1)-one_edge(a)+Q(1,1,c)-Q(1,a,c))+logi(a)
    penalty = logi(c)-one_edge(1)-Q(1,1,c)
    # This verifies which branch of max(0, penalty) is used.
    assert penalty.lo > 0
    saving = one_edge(1)-change-penalty
    values = {
        "distortion": distortion, "boundary_balance": boundary_balance,
        "near_one": near_one, "near_two": near_two,
        "interior_one": interior_one, "interior_two": interior_two,
        "changed_neighbor": changed_neighbor,
        "boundary_change": change, "boundary_penalty": penalty,
        "boundary_saving": saving,
    }
    assert F(distortion.hi,S) < F(203,1000)
    lower_tests = [
        ("boundary_balance", boundary_balance, F(0)),
        ("near_one", near_one, F(28,100)),
        ("near_two", near_two, F(42,100)),
        ("interior_one", interior_one, F(43,100)),
        ("interior_two", interior_two, F(42,100)),
        ("changed_neighbor", changed_neighbor, F(32,100)),
        ("boundary_saving", saving, F(37,100)),
    ]
    for label, value in [("near_one",near_one),("near_two",near_two),
                         ("interior_one",interior_one),("interior_two",interior_two)]:
        lower_tests.append((label+"_net_gap",value-distortion,F(7,100)))
    lower_tests.append(("boundary_net_gap",saving-distortion,F(16,100)))
    for label, value, threshold in lower_tests:
        assert F(value.lo,S) > threshold, (label,value.bounds(),str(threshold))
    return {
        "status": "verified",
        "arithmetic": "rational interval endpoints with outward integer rounding",
        "uniform_anchor_margin": "7/100",
        "diagram_sizes_sampled": 0,
        "scope": "Fixed constants only; the proof for every even number of syllables is separate.",
        "source_sha256": {
            str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (Path(__file__).resolve(), ENGINE)
        },
        "values": {name:value.bounds() for name,value in values.items()},
        "strict_lower_tests": [
            {"name":name,"lower":str(F(value.lo,S)),"threshold":str(threshold)}
            for name,value,threshold in lower_tests],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
