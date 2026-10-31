"""Exact restricted-window matrix/path identities, not an asymptotic audit."""
from pathlib import Path
import argparse
import json
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local


def audit():
    count = 0
    for N in range(8, 16):
        loc = Local(N)
        p, q, Q, d = loc.p, loc.q, loc.Q, loc.d
        nodes = [(q*pow(Q,r,p)+pow(q,-1,p)*pow(Q,-r,p)) % p for r in range(N)]
        sr = lambda r: (pow(q,r,p)-pow(q,-r,p)) % p
        beta = [(2-pow(Q,r,p)-pow(Q,-r,p)) % p for r in range(N)]
        for M in (N//2-1, d):
            windows = [(0,1,M-1,M)]
            if M >= 4:
                windows.append((1,2,M-1,M))
            for sigma in dict.fromkeys([p-2, 2, 0, nodes[0], nodes[M]]):
                alpha = [(v-sigma) % p for v in nodes]
                for x,b,c,y in [(2,3,5,7), (2*Q % p, 3*pow(Q,-1,p) % p,
                                            5*pow(Q,2,p) % p, 7*pow(Q,3,p) % p),
                               (0,3,5,7)]:
                    A, P = x+y, x*y
                    gamma = [0 if r < 2 else -sr(r)*sr(r-1)*alpha[r-1] % p
                             for r in range(N)]
                    C = [sp.Matrix([[beta[r]*A,gamma[r]*P],[1,0]]) for r in range(N)]
                    for pm, pp, qm, qp in windows:
                        assert pp < qm
                        start = sp.eye(3)
                        for r in range(pm,pp+1):
                            T = sp.Matrix([[beta[r]*A,gamma[r]*P,1],
                                           [1,0,0],[0,0,b*alpha[r]]])
                            start = (T*start).applyfunc(lambda z: z % p)
                        stop = sp.eye(3)
                        for r in range(qm,qp+1):
                            T = sp.Matrix([[c*alpha[r],beta[r]*A,gamma[r]*P],
                                           [0,beta[r]*A,gamma[r]*P],[0,1,0]])
                            stop = (T*stop).applyfunc(lambda z: z % p)
                        middle = sp.eye(2)
                        for r in range(pp+1,qm):
                            middle = (C[r]*middle).applyfunc(lambda z: z % p)
                        value = int((stop[0,1:3]*middle*start[0:2,2])[0]) % p
                        value = value*pow(c,d-M,p) % p
                        for r in range(pm):
                            value = value*b*alpha[r] % p
                        for r in range(qp+1,M+1):
                            value = value*c*alpha[r] % p
                        for r in range(M+1,N):
                            value = value*alpha[r] % p
                        direct = 0
                        for i in range(pm,pp+1):
                            tail = [1]
                            for j in range(i+1,qp+1):
                                z = beta[j]*A*tail[-1]
                                if j >= i+2:
                                    z += gamma[j]*P*tail[-2]
                                tail.append(z % p)
                            for j in range(qm,qp+1):
                                term = pow(b,i,p)*pow(c,d-j,p)*tail[j-i] % p
                                for r in range(N):
                                    if r < i or r > j:
                                        term = term*alpha[r] % p
                                direct = (direct+term) % p
                        assert value == direct, (N,M,sigma,(pm,pp,qm,qp),value,direct)
                        count += 1

    return {"status": "PASS", "exact_window_values": count,
            "scope": "Exact finite half-row/full-row window dictionary only; no asymptotic test."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "research_regular_spectral_window_phase_exclusion_results.json"))
    args = parser.parse_args()
    result = audit()
    payload = json.dumps(result, indent=2) + "\n"
    args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
