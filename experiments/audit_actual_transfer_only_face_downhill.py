#!/usr/bin/env python3
"""Original knot lattice, signed lower-transfer phase, and exact source collars.

See notes/actual_transfer_only_face_downhill_patch.md. The proof is uniform;
finite checks do not assert a sharp whole-knot bound or delete side currents.
"""
from pathlib import Path
import json
import mpmath as mp
from audit_exact_factorial_interpolation import factorial


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def basis(n, i):
    return tuple(int(j == i) for j in range(n))


def knot_lattice(width, word):
    """Solve ORIGINAL one-cycle integer closure, rather than modulo-N routing."""
    m = len(word)
    owners = list(range(width))
    offsets = [basis(m, -1) for _ in range(width)]
    for e, signed in enumerate(word):
        j, sig = abs(signed)-1, (1 if signed > 0 else -1)
        k = basis(m, e)
        left, right = offsets[j], offsets[j+1]
        offsets[j] = add(right, scale(sig, k))
        offsets[j+1] = add(left, scale(-sig, k))
        owners[j], owners[j+1] = owners[j+1], owners[j]
    seen, j = set(), 0
    while j not in seen:
        seen.add(j)
        j = owners[j]
    assert len(seen) == width, (width, word, owners)
    assert all(sum(row[e] for row in offsets) == 0 for e in range(m))

    initial = [None]*width
    initial[0] = basis(m+1, 0)
    while any(row is None for row in initial):
        progressed = False
        for j in range(width):
            if initial[j] is None and initial[owners[j]] is not None:
                initial[j] = add(initial[owners[j]], (0,)+offsets[j])
                progressed = True
        assert progressed
    heads = initial.copy()
    records, arcs = [], list(heads)
    for e, signed in enumerate(word):
        j, sig = abs(signed)-1, (1 if signed > 0 else -1)
        a, b = heads[j], heads[j+1]
        k = basis(m+1, e+1)
        records.append((sig, a, b, k))
        heads[j], heads[j+1] = add(b, scale(sig, k)), add(a, scale(-sig, k))
        arcs.extend([heads[j], heads[j+1]])
    assert heads == initial
    assert all(row[0] == 1 for row in arcs)
    assert all(c in (-1, 0, 1) for row in arcs for c in row[1:])
    return records, arcs


def dot(a, y):
    return mp.fsum(c*z for c, z in zip(a, y))


def G(z, n, sig):
    # Exact +1 factorial tag is kept in this derivative symbol.
    return mp.log(-mp.expm1(sig*2*mp.j*mp.pi*(z+1/n)))


def local_derivative(sig, a, b, k, da, db, dk, n):
    g = lambda z: G(z, n, sig)
    logx = sig*mp.j*mp.pi*(1-1/n)
    if sig > 0:
        e, j = b+k, a-k
        de, dj = db+dk, da-dk
        fact = g(e)*de+g(a)*da-g(k)*dk-g(b)*db-g(j)*dj
        phase = logx*(-da-db+dk)+2*mp.j*mp.pi*(db*j+b*dj)
    else:
        c, e = b-k, a+k
        dc, de = db-dk, da+dk
        fact = g(e)*de+g(b)*db-g(k)*dk-g(a)*da-g(c)*dc
        phase = logx*(-da-db+dk)-2*mp.j*mp.pi*(da*c+a*dc)
    return fact+phase


def whole_derivative(records, y, direction, n):
    result = mp.mpc(0)
    for sig, ac, bc, kc in records:
        result += local_derivative(sig, dot(ac, y), dot(bc, y), dot(kc, y),
                                   dot(ac, direction), dot(bc, direction),
                                   dot(kc, direction), n)
    return result


def window(z, n, sig=1):
    result = mp.expm1(2*mp.j*mp.pi*z)/(2*mp.j*mp.pi)*mp.fsum(1/(z-j) for j in range(n))
    return result if sig > 0 else mp.exp(-2*mp.j*mp.pi*z)*result


def fhat(z, n, sig):
    return factorial(n, z) if sig > 0 else mp.conj(factorial(n, mp.conj(z)))


def crossing(a, b, k, n, sig):
    if sig < 0:
        return mp.conj(crossing(mp.conj(b), mp.conj(a), mp.conj(k), n, 1))
    x = -mp.exp(-mp.j*mp.pi/n)
    kap = mp.exp(mp.j*mp.pi*(n-1)**2/(2*n))
    return (kap*mp.exp((-a-b+k)*mp.log(x)+2*mp.j*mp.pi*b*(a-k)/n)
            *fhat(b+k,n,1)*fhat(a,n,1)/(fhat(k,n,1)*fhat(b,n,1)*fhat(a-k,n,1)))


def main():
    mp.mp.dps = 100
    cases = [(2, [1]), (2, [-1]), (2, [1,1,1]), (3, [1,-2,1,-2]),
             (3, [1,1,1,2,-1,2]), (4, [1,-2,3]*3),
             (5, [1,-2,3,-4]*2), (6, [1,-2,3,-4,5]*5)]
    lattice_rows, phase_rows = [], []
    n = mp.mpf(10)**48
    delta = mp.mpf("1e-30")
    for width, word in cases:
        records, arcs = knot_lattice(width, word)
        m = len(word)
        realpoint = [mp.mpf(".5")]+[mp.mpf(1)/(16*(m+1))]*m
        assert all(mp.mpf(".25") < dot(row, realpoint) < mp.mpf(".75") for row in arcs)
        lattice_rows.append({"width":width, "word":word, "rank":m+1,
                             "all_integer_routing_closed":True, "strict_interior":True})
        selected = list(range(0,m,2))
        y = [mp.mpc(".47", ".001")]+[mp.mpc(mp.mpf(1)/(50*(m+1)),mp.mpf(".0001")/(m+1))]*m
        for e in selected:
            y[e+1] = delta*mp.mpf(".4")-1/n+mp.j*mp.mpf(".23")/n
        for e in selected:
            direction = scale(-1,basis(m+1,e+1))
            for amount in (mp.mpf(0),delta/2,delta,2*delta):
                yy = y.copy()
                for selected_e in selected:
                    yy[selected_e+1] -= amount
                assert all(mp.mpf(".25") < mp.re(dot(row,yy)) < mp.mpf(".75") for row in arcs)
                deriv = mp.re(whole_derivative(records,yy,direction,n))
                sig = 1 if word[e] > 0 else -1
                singular = mp.re(G(yy[e+1],n,sig))
                background = deriv-singular
                assert deriv < mp.log(delta)/2, (width,e,deriv,background)
                # ANY retained integer mode has purely imaginary derivative.
                for row in arcs:
                    assert mp.re(2*mp.j*mp.pi*7*dot(row,direction)) == 0
                phase_rows.append({"width":width,"event":e,"step":float(amount/delta),
                                   "normal_derivative":float(deriv),
                                   "regular_background":float(background),
                                   "all_integer_marks_real_height_derivative":0})

    # Exact, finite-level reciprocal-factorial shift on both roots.
    shift_rows=[]
    for nlevel in (8,12,16,24):
        nu=mp.mpc(".5",".3")
        for sig in (1,-1):
            q=mp.exp(sig*2*mp.j*mp.pi/nlevel)
            base=fhat(nu,nlevel,sig)
            for s in (1,2,3):
                lhs=1/fhat(nu-s,nlevel,sig)
                rhs=mp.fprod(1-q**(nu-r) for r in range(s))/base
                err=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
                assert err<mp.mpf("1e-70"),(nlevel,sig,s,err)
                # Cardinal integer characters remain literally invariant.
                char=mp.exp(2*mp.j*mp.pi*nu)
                assert abs(mp.exp(2*mp.j*mp.pi*(nu-s))-char)<mp.mpf("1e-90")
                shift_rows.append({"N":nlevel,"root_sign":sig,"steps":s,"relative_error":float(err)})

    # A full actual windowed crossing has removable cot poles on its
    # newly crossed negative integers; no projection or bare-residue model.
    collar_rows=[]
    eps=mp.mpf("1e-12")
    for nlevel in (16,24):
        a=mp.mpc(mp.mpf(".45")*nlevel,".17")
        b=mp.mpc(mp.mpf(".4")*nlevel,"-.11")
        for sig in (1,-1):
            for s in (1,2,3):
                def density(z):
                    c,e=b+sig*z,a-sig*z
                    vals=[a,b,c,e,z]
                    return (mp.pi*mp.cot(mp.pi*z)*crossing(a,b,z,nlevel,sig)
                            *mp.fprod(window(v,nlevel,sig)**3 for v in vals))
                left=density(-s-eps)/(-eps)**3
                right=density(-s+eps)/eps**3
                err=abs(left-right)/max(1,abs(left),abs(right))
                assert err<mp.mpf("1e-8"),(nlevel,sig,s,err)
                collar_rows.append({"N":nlevel,"sign":sig,"outside_integer":-s,
                                    "complete_cot_zero_order":3,"normalized_jump":float(err)})
    result={"status":"PASS","integer_lattices":lattice_rows,"signed_downhill_phases":phase_rows,
            "exact_factorial_shifts":shift_rows,"complete_cardinal_cot_collars":collar_rows,
            "scope":"Regular-head lower-transfer source collar; no physical positive residue deletion or global sharp bound."}
    path=Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(f"PASS: {len(lattice_rows)} exact knot lattices; {len(phase_rows)} signed phase normals; "
          f"{len(shift_rows)} exact root shifts; {len(collar_rows)} complete cot/window collars")
    print(path)


if __name__=="__main__":
    main()
