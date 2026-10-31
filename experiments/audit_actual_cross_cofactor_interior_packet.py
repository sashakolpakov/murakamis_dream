#!/usr/bin/env python3
"""Exact cofactor/node adapter checks; no asymptotic is inferred."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mpmath as mp
from audit_actual_q_hahn_negative_clock_boundary import matrix


def source(N, n, b, x, y, u):
    th=mp.pi/N
    a=[4*mp.cos((j+mp.mpf('.5'))*th)**2+u for j in range(n+1)]
    s=[2*mp.sin(j*th) for j in range(n+1)]
    R=[];prefix=mp.mpf(1)
    for j in range(n+1):
        z=b**j*prefix
        if j:z+=s[j]**2*(x+y)*R[-1]
        if j>1:z+=s[j]*s[j-1]*a[j-1]*x*y*R[-2]
        R.append(z);prefix*=a[j]
    return R,a,s


def run():
    mp.mp.dps=85
    counts=Counter();worst=mp.mpf(0)
    def check(a,b):
        nonlocal worst
        err=abs(a-b)/max(1,abs(a),abs(b));worst=max(worst,err)
        assert err<mp.mpf('1e-70'),(a,b,err)
    faces=[(mp.mpf('1.2'),mp.mpf('.7'),mp.mpf('1.6')),
           (mp.mpf(0),mp.mpf('.9'),mp.mpf('1.3')),
           (mp.mpf('1.1'),mp.mpf('.8'),mp.mpf(0)),
           (mp.mpc('1.2','.1'),mp.mpc('.8','-.2'),mp.mpc('1.7','.3'))]
    for N in range(3,19):
        M=(N-1)//2
        for x,b,y in faces:
            for u in (mp.mpf(0),mp.mpf('-.017'),mp.mpc('.013','.021')):
                R,a,s=source(N,M,b,x,y,u)
                for j in range(M+1):
                    B=mp.matrix(j+1)
                    for v in range(j+1):
                        B[v,v]=a[v]
                        if v:B[v-1,v]=-s[v]**2*(x+y)
                        if v>1:B[v-2,v]=-s[v]*s[v-1]*x*y
                    for v in range(j+1):B[j,v]=b**v
                    check(mp.det(B),R[j]);counts['literal_row_replacement_determinants']+=1
            sins=[mp.mpf(1)]
            for j in range(1,N):sins.append(sins[-1]*2*mp.sin(j*mp.pi/N))
            for aidx in range(M+1):
                node=-4*mp.cos((aidx+mp.mpf('.5'))*mp.pi/N)**2
                R,alpha,s=source(N,M,b,x,y,node)
                D=mp.mpf(1) if not aidx else b**aidx*mp.det(matrix(N,aidx,x/(2*b),y/(2*b)))
                check(R[aidx],sins[2*aidx]*D)
                check(mp.fprod(alpha[:aidx]),sins[2*aidx])
                counts['original_positive_matrix_node_adapters']+=1
                counts['exact_node_scalars']+=1
                K=[mp.mpf(1)]
                for j in range(aidx+1,M+1):
                    z=s[j]**2*(x+y)*K[-1]
                    if j>aidx+1:z+=s[j]*s[j-1]*alpha[j-1]*x*y*K[-2]
                    K.append(z)
                    check(R[j],K[-1]*R[aidx]);counts['physical_node_tail_factorizations']+=1
    return dict(status='PASS',precision_digits=mp.mp.dps,counts=dict(counts),
                maximum_relative_error=str(worst),
                scope='Exact original row-replacement cofactor, independently built positive q-Hahn matrix at physical nodes, sine scalar and cleared tail factorization, including one protected outer face. No off-node determinant identification, relative packet, spectral derivative or contour claim is inferred from these tests.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_cross_cofactor_interior_packet_results.json'))
    a=p.parse_args();r=run();a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
