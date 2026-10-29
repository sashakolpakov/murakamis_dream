#!/usr/bin/env python3
"""Exact audits for notes/whole_source_newton_transport.md.

The generic tests use integral Laurent dictionaries.  Finite-root tests use
exact cyclotomic fields and rational functions in the un-specialized U.
Neither floating point nor ordinary-color interpolation is used.
"""

from __future__ import annotations

import json
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


Poly = dict[tuple[int, int], int]  # exponent of Q, exponent of Y


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for p in polys:
        for mon, c in p.items():
            out[mon] = out.get(mon, 0) + c
            if not out[mon]:
                del out[mon]
    return out


def scale(p: Poly, c: int) -> Poly:
    return {m: c * v for m, v in p.items() if c * v}


def mul(p: Poly, r: Poly) -> Poly:
    out: Poly = {}
    for (a, b), c in p.items():
        for (d, e), f in r.items():
            mon = (a + d, b + e)
            out[mon] = out.get(mon, 0) + c * f
    return {m: c for m, c in out.items() if c}


def mon(q: int = 0, y: int = 0, c: int = 1) -> Poly:
    return {(q, y): c} if c else {}


ONE, X = mon(), add(mon(y=1), mon(y=-1))


def shift(p: Poly, j: int = 1) -> Poly:
    return {(a + j * b, b): c for (a, b), c in p.items()}


def involution(p: Poly) -> Poly:
    return {(a, 1 - b): -c for (a, b), c in p.items()}


def sop(p: Poly) -> Poly:
    return add(shift(p), mul(mon(q=1), shift(p, -1)))


def zop(p: Poly) -> Poly:
    return add(mul(mon(y=1), shift(p)),
               mul(mon(q=1, y=-1), shift(p, -1)))


def delta(n: int) -> Poly:
    return mul(mon(q=-2 * n),
               mul(add(ONE, mon(q=2 * n, c=-1)),
                   add(ONE, mon(q=2 * n + 1, c=-1))))


def make_sources(nmax: int) -> list[Poly]:
    out = [add(ONE, mon(y=1, c=-1))]
    for n in range(nmax):
        out.append(mul(out[-1], add(
            X, mon(q=n + 1, c=-1), mon(q=-n - 1, c=-1))))
    return out


def generic_checks(v: list[Poly], nmax: int) -> int:
    checks = 0
    for n in range(nmax + 1):
        prev = v[n - 1] if n else {}
        assert involution(v[n]) == v[n]
        checks += 1
        assert mul(X, v[n]) == add(
            v[n + 1], mul(add(mon(q=n + 1), mon(q=-n - 1)), v[n]))
        checks += 1
        assert sop(v[n]) == add(
            mul(add(mon(q=n + 1), mon(q=-n)), v[n]), mul(delta(n), prev))
        checks += 1
        assert zop(v[n]) == add(
            mul(mon(q=n + 1), v[n + 1]),
            mul(add(mon(q=2 * n + 1), mon(q=2 * n + 2)), v[n]),
            mul(mul(mon(q=n), delta(n)), prev))
        checks += 1
        assert add(mul(X, sop(v[n])),
                   scale(mul(mon(q=1), sop(mul(X, v[n]))), -1)) == mul(
                       add(ONE, mon(q=2, c=-1)), zop(v[n]))
        checks += 1
        poch = mon(y=n + 1, c=-1)
        for j in range(2 * n + 1):
            poch = mul(poch, add(ONE, mon(q=-n + j, y=-1, c=-1)))
        assert poch == v[n]
        checks += 1
    return checks


def zero_matrix(n, field):
    return [[field.zero for _ in range(n)] for _ in range(n)]


def dm(rows, field):
    # Entries already belong to field.  from_list re-coerces ANP elements
    # through QQ in some SymPy versions, so use the typed constructor.
    return DomainMatrix(rows, (len(rows), len(rows[0])), field)


def equal(a, b):
    return a.sub(b).is_zero_matrix


def chebyshev_matrices(x, nmax, second_kind=False):
    n, _ = x.shape
    field = x.domain
    identity = DomainMatrix.eye((n, n), field).to_dense()
    if second_kind:
        # Store P_j at index j, with P_{-1} handled separately.
        out = [identity]
        if nmax:
            out.append(x)
    else:
        out = [identity.scalarmul(field(2))]
        if nmax:
            out.append(x)
    for j in range(1, nmax):
        out.append(x.matmul(out[j]).sub(out[j - 1]))
    return out


def finite_checks(v, n):
    k = QQ.cyclotomic_field(n)
    q = k.from_sympy(k.ext)
    field = k.frac_field("U")
    u = field.gens[0]
    qf = field.convert(q, k)
    one, zero = field.one, field.zero
    identity = DomainMatrix.eye((n, n), field).to_dense()

    rows = zero_matrix(n, field)
    for col in range(n):
        for (aq, ay), c in v[col].items():
            power_u, row = divmod(ay, n)
            rows[row][col] += field.convert(k(c) * q ** (aq % n), k) * u ** power_u
    basis = dm(rows, field)

    # Original regular clock/shift action on 1,Y,...,Y^{N-1}.
    yy, yi, tt, ti = [zero_matrix(n, field) for _ in range(4)]
    for col in range(n):
        yy[(col + 1) % n][col] = u if col == n - 1 else one
        yi[(col - 1) % n][col] = u ** -1 if col == 0 else one
        tt[col][col] = qf ** col
        ti[col][col] = qf ** (-col)
    yy, yi, tt, ti = [dm(m, field) for m in (yy, yi, tt, ti)]
    actual_x = yy.add(yi)
    actual_s = tt.add(ti.scalarmul(qf))
    actual_z = yy.matmul(tt).add(yi.matmul(ti).scalarmul(qf))

    xx, ss, zz = [zero_matrix(n, field) for _ in range(3)]
    w = u + u ** -1 - 2
    for col in range(n):
        de = qf ** (-2 * col) * (1 - qf ** (2 * col)) * (
            1 - qf ** (2 * col + 1))
        xx[col][col] += qf ** (col + 1) + qf ** (-col - 1)
        ss[col][col] += qf ** (col + 1) + qf ** (-col)
        zz[col][col] += (1 + qf) * qf ** (2 * col + 1)
        if col + 1 < n:
            xx[col + 1][col] += one
            zz[col + 1][col] += qf ** (col + 1)
        else:
            xx[0][col] += w
            zz[0][col] += w  # q^N=1, including at N=2.
        if col:
            ss[col - 1][col] += de
            zz[col - 1][col] += qf ** col * de
    xx, ss, zz = [dm(m, field) for m in (xx, ss, zz)]
    for actual, source in ((actual_x, xx), (actual_s, ss), (actual_z, zz)):
        assert equal(actual.matmul(basis), basis.matmul(source))

    predicted_det = ((1 - u) * (1 - u ** -2) ** ((n - 1) // 2)
                     if n % 2 else -u * (1 - u ** -2) ** (n // 2))
    assert basis.det() == predicted_det

    # Fiber ranks over the exact cyclotomic field, and the normal cut witness.
    ranks = {}
    for sign in (1, -1):
        fiber = zero_matrix(n, k)
        for col in range(n):
            for (aq, ay), c in v[col].items():
                power_u, row = divmod(ay, n)
                fiber[row][col] += k(c) * q ** (aq % n) * k(sign) ** power_u
        _, pivots = dm(fiber, k).rref()
        expected = ((n - 1) // 2 if sign == 1 else (n + 1) // 2) if (
            n % 2) else n // 2
        assert len(pivots) == expected
        ranks[str(sign)] = len(pivots)
        if sign == 1:
            witness = n // 2
            assert all(fiber[row][witness] == k.zero for row in range(n))

    witness = n // 2
    cut = -sum((k(c * ay) * q ** (aq % n)
                for (aq, ay), c in v[witness].items()), k.zero)
    predicted_cut = k.one
    for r in range(1, witness + 1):
        predicted_cut *= 2 - q ** r - q ** (-r)
    assert cut == predicted_cut and cut != k.zero

    # Cleared recovery, so no division by U-U^{-1} or specialization at U=1.
    cc = chebyshev_matrices(xx, n + 1)
    pp = chebyshev_matrices(xx, n - 1, second_kind=True)
    d = u - u ** -1
    recovered_y = cc[n + 1].sub(xx.scalarmul(u ** -1))
    recovered_yi = cc[n - 1].sub(xx.scalarmul(u ** -1))
    recovered_t = pp[n - 1].matmul(zz).sub(
        pp[n - 2].add(identity.scalarmul(u ** -1)).matmul(ss))
    recovered_ti = pp[n - 2].add(identity.scalarmul(u)).matmul(ss).sub(
        pp[n - 1].matmul(zz))
    for actual, cleared, scalar in (
        (yy, recovered_y, d), (yi, recovered_yi, d),
        (tt, recovered_t, d), (ti, recovered_ti, qf * d),
    ):
        assert equal(actual.matmul(basis).scalarmul(scalar),
                     basis.matmul(cleared))

    return {
        "N": n, "matrix_intertwining_checks": 3,
        "determinant_checks": 1, "fiber_rank_checks": 2,
        "normal_cut_witness_checks": 2, "cleared_recovery_checks": 4,
        "fiber_ranks": ranks,
    }


# Normal-ordered quantum-torus monomials Q^q Y^a T^b, for the fixed-algebra
# recurrences; this is a different algebra from the commuting source variable.
def qa(*ps):
    out = {}
    for p in ps:
        for key, value in p.items():
            out[key] = out.get(key, 0) + value
    return {k: c for k, c in out.items() if c}


def qm(p, r):
    out = {}
    for (q, a, b), c in p.items():
        for (s, d, e), f in r.items():
            key = (q + s + b * d, a + d, b + e)
            out[key] = out.get(key, 0) + c * f
    return {k: c for k, c in out.items() if c}


def qs(p, q=0, c=1):
    return {(s + q, a, b): c * v for (s, a, b), v in p.items() if c * v}


def orbit(a, b):
    return qa({(0, a, b): 1}, {(b, -a, -b): 1})


def fixed_algebra_checks():
    x, s, z = orbit(1, 0), orbit(0, 1), orbit(1, 1)
    count = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            assert qm(x, orbit(a, b)) == qa(orbit(a + 1, b), orbit(a - 1, b))
            assert qm(orbit(a, b), s) == qa(
                orbit(a, b + 1), qs(orbit(a, b - 1), q=1))
            assert orbit(-a, b) == qs(orbit(a, -b), q=b)
            count += 3
    assert orbit(1, -1) == qs(qa(qm(x, s), qs(z, c=-1)), q=-1)
    return count + 1


def main():
    v = make_sources(13)
    result = {
        "status": "all exact checks passed",
        "generic_integral_laurent_checks": generic_checks(v, 12),
        "fixed_algebra_orbit_checks": fixed_algebra_checks(),
        "finite_roots": [finite_checks(v, n) for n in range(2, 11)],
        "scope": (
            "Exact boundary transport/lattice audit; no arbitrary-crossing "
            "realization, 5_2 transform, or volume theorem is inferred."
        ),
    }
    result["finite_root_exact_checks"] = sum(
        sum(r[key] for key in (
            "matrix_intertwining_checks", "determinant_checks",
            "fiber_rank_checks", "normal_cut_witness_checks",
            "cleared_recovery_checks"))
        for r in result["finite_roots"])
    path = Path(__file__).with_name("whole_source_newton_transport_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
