#!/usr/bin/env python3
"""Actual q-Pascal fusion, literal turn sources, and arbitrary-plat transport.

Every crossing is independently evaluated by MixedEntries.direct, from
the original E coefficients and Cartan diagonal. Common Cartan and the
external dimension/framing lines multiply both network realizations
unchanged. They are not assigned new numerical values here.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import inv
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def fusion(N, p, x, F):
    C = np.zeros((N*N, N*N), dtype=np.int64)
    for a, k in product(range(N), repeat=2):
        for u in range(a+1):
            v = a+k-u
            if v < N:
                C[u*N+v, a*N+k] = (pow(x, u-a, p)*F[a]*F[v]
                    *pow(F[a-u]*F[k] % p, -1, p)) % p
    return C


def crossing(E, x, y, sign):
    N, p = E.N, E.p
    R = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in product(range(N), repeat=2):
        maximum = min(a, N-1-b) if sign > 0 else min(b, N-1-a)
        for h in range(maximum+1):
            u, v = (b+h, a-h) if sign > 0 else (b-h, a+h)
            R[u*N+v, a*N+b] = E.direct(x, y, a, b, h, sign)
    return R


def euler_core(E, x, y, sign):
    N, p, Q = E.N, E.p, E.Q
    U = np.zeros((N*N, N*N), dtype=np.int64)
    D = np.diag([pow(-1,k,p)*pow(Q,k*(k-1)//2,p)*pow(x*y,-k,p) % p
                 for a,k in product(range(N),repeat=2)]).astype(np.int64)
    # The negative core is v(y^-1 X_+) D^-1, with no cyclic arrows.
    color = x if sign > 0 else y
    for a,k in product(range(N),repeat=2):
        for h in range(min(N-1-a,k)+1):
            coeff = pow(color,-h,p)*pow(E.F[h],-1,p)
            if sign < 0:
                coeff *= pow(-1,h,p)*pow(Q,h*(h-1)//2,p)
            U[(a+h)*N+k-h,a*N+k] = coeff % p
    return D@U % p if sign > 0 else U@inv(D,p) % p


def local_cases():
    result=[]
    for N in range(2,9):
        p,g,q=field(N); E=MixedEntries(N,p,q); Q=E.Q;d=N-1
        for kind,x in [('generic',g),('complete',-pow(q,-1,p)%p)]:
            y=pow(x,-1,p)*pow(Q,-1,p)%p
            C=fusion(N,p,x,E.F);Ci=inv(C,p)
            assert np.array_equal(Ci@C%p,np.eye(N*N,dtype=np.int64))
            blocks=0
            for total in range(2*N-1):
                indices=range(max(0,total-d),min(d,total)+1)
                for u,a in product(indices,repeat=2):
                    actual=int(C[u*N+total-u,a*N+total-a])
                    expected=0
                    if u<=a:
                        gaussian=E.gaussian(a,u)
                        expected=pow(x,u,p)*E.F[u]*E.F[total-u]*gaussian\
                            *pow(x,-a,p)*pow(E.F[total-a],-1,p)%p
                    assert actual==expected
                    inverse_expected=0
                    if u<=a:
                        h=a-u
                        inverse_expected=pow(x,u-a,p)*pow(-1,h,p)*pow(Q,h*(h-1)//2,p)\
                            *E.F[total-u]*pow(E.F[u]*E.F[h]*E.F[total-a]%p,-1,p)%p
                    assert int(Ci[u*N+total-u,a*N+total-a])==inverse_expected
                blocks+=1
            # Root Rogers matrix is an exact diagonal gauge on the cap block.
            for k,n in product(range(N),repeat=2):
                actual=int(C[k*N+d-k,n*N+d-n])
                row=pow(Q,1-k,p)*pow(x,-k,p)\
                    *pow(E.F[k]*E.F[d-k]%p,-1,p)%p
                col=pow(Q,n,p)*pow(x,n,p)*E.F[d-n]%p
                expected=pow(Q,n-k+1,p)*E.gaussian(n,k)%p if k<=n else 0
                assert row*actual*col%p==expected
            # Literal left cup, right cap, and original averaged marked cap.
            cup=np.zeros(N*N,dtype=np.int64)
            cap=np.zeros(N*N,dtype=np.int64)
            mark=np.zeros(N*N,dtype=np.int64)
            for u,v in product(range(N),repeat=2):
                if u+v==d:
                    cup[u*N+v]=N*pow(x,u-d,p)%p
                    cap[u*N+v]=pow(y,u,p)*pow(N,-1,p)%p
                mark[u*N+v]=pow(x,v,p)*pow(N,-2,p)%p
            corner=np.zeros(N*N,dtype=np.int64);corner[d*N]=1
            assert np.array_equal(C@corner%p,cup)
            wantcap=np.zeros(N*N,dtype=np.int64);wantcap[d]=pow(N,-1,p)
            assert np.array_equal(cap@C%p,wantcap)
            pulled=mark@C%p
            for a,k in product(range(N),repeat=2):
                value=sum(E.gaussian(k+h,k) for h in range(min(a,d-k)+1))%p
                expected=pow(x,k,p)*E.F[a]*pow(N,-2,p)*value%p
                assert int(pulled[a*N+k])==expected
            for r in range(N):
                expected=pow(x,d-r,p)*pow(-1,r,p)*pow(Q,-r*(r+1)//2,p)\
                    *E.F[r]**2*pow(N,-2,p)%p
                assert int(pulled[r*N+d-r])==expected
            assert int(mark@cup)%p==1
            # Also test the right cup / left cap, in the opposite color order.
            Cv=fusion(N,p,y,E.F)
            rcup=np.zeros(N*N,dtype=np.int64);lcap=np.zeros_like(rcup)
            for u in range(N):
                rcup[u*N+d-u]=N*pow(x,-u,p)*pow(x,d,p)*pow(Q,d-u,p)%p
                lcap[u*N+d-u]=pow(x,u,p)*pow(N,-1,p)%p
            assert np.array_equal(Cv@corner%p,rcup)
            assert np.array_equal(lcap@Cv%p,wantcap)
            for x1,x2 in ((x,y),(y,x),(g,pow(g,2,p))):
                Cin=fusion(N,p,x1,E.F);Cout=fusion(N,p,x2,E.F)
                for sign in (-1,1):
                    direct=crossing(E,x1,x2,sign)
                    predicted=Cout@euler_core(E,x1,x2,sign)@inv(Cin,p)%p
                    assert np.array_equal(direct,predicted),(N,kind,x1,x2,sign)
            result.append({'N':N,'color':kind,'all_total_degree_blocks':blocks,
                           'Rogers_gauge':True,'four_turn_corners':True,
                           'whole_marked_cap_row':True,'six_actual_crossings':True})
    return result


def add(out,key,value,p):
    if value%p:out[key]=(out.get(key,0)+value)%p


def pair_operator(state,matrix,position,N,p):
    out={}
    for index,value in state.items():
        col=index[position]*N+index[position+1]
        for row in range(N*N):
            c=int(matrix[row,col])
            if c:
                u,v=divmod(row,N)
                add(out,index[:position]+(u,v)+index[position+2:],value*c,p)
    return {k:v for k,v in out.items() if v}


def frame(state,colors,E,inverse=False):
    for position in range(0,len(colors),2):
        C=fusion(E.N,E.p,colors[position],E.F)
        state=pair_operator(state,inv(C,E.p) if inverse else C,position,E.N,E.p)
    return state


def scalar(state,colors,E,fused):
    N,p,Q=E.N,E.p,E.Q;d=N-1;total=0
    for index,value in state.items():
        coefficient=value
        for pair in range(len(colors)//2):
            x=colors[2*pair];a,k=index[2*pair:2*pair+2]
            if pair==0:
                if fused:
                    hsum=sum(E.gaussian(k+h,k) for h in range(min(a,d-k)+1))
                    coefficient*=pow(x,k,p)*E.F[a]*pow(N,-2,p)*hsum
                else:coefficient*=pow(x,k,p)*pow(N,-2,p)
            elif fused:
                if (a,k)!=(0,d):coefficient=0;break
                coefficient*=pow(N,-1,p)
            else:
                if a+k!=d:coefficient=0;break
                dual=pow(x,-1,p)*pow(Q,-1,p)%p
                coefficient*=pow(dual,a,p)*pow(N,-1,p)
            coefficient%=p
        total=(total+coefficient)%p
    return total


def word_cases():
    output=[]
    for N in range(2,5):
        p,g,q=field(N);E=MixedEntries(N,p,q)
        for bridges in (2,3):
            dual=pow(g,-1,p)*pow(E.Q,-1,p)%p
            colors0=[c for pair in range(bridges)
                     for c in ((g,dual) if pair%2==0 else (dual,g))]
            # Every elementary square returns the color order; no cap is redefined.
            choices=[(2*bridges-3,1),(0,-1),(1,1),(2*bridges-2,-1),(1,-1)]
            # First join the bridges through equal-color middle crossings.
            word=[(2*j+1,1 if j%2==0 else -1) for j in range(bridges-1)]
            word += [(i,sign) for i,sign in choices for _ in range(2)]
            colors=colors0[:]
            corners={(N-1,0)*bridges:1}
            actual=frame(corners,colors,E)
            fused=corners
            for position,sign in word:
                R=crossing(E,colors[position],colors[position+1],sign)
                actual=pair_operator(actual,R,position,N,p)
                physical=frame(fused,colors,E)
                physical=pair_operator(physical,R,position,N,p)
                colors[position],colors[position+1]=colors[position+1],colors[position]
                fused=frame(physical,colors,E,inverse=True)
            assert colors==colors0
            assert frame(fused,colors,E)==actual
            a=scalar(actual,colors,E,False);b=scalar(fused,colors,E,True)
            assert a==b
            marked_channel=[]
            for r in range(N):
                index=(r,N-1-r)+(0,N-1)*(bridges-1)
                amplitude=fused.get(index,0)
                marked_channel.append(amplitude)
                if r<N-1:assert amplitude==0
            corner_value=marked_channel[-1]*pow(N,-(bridges-1),p)%p
            assert b==corner_value
            output.append({'N':N,'bridges':bridges,'crossings':len(word),
                           'original_marked_source_value':a,'whole_source_transport':True,
                           'exact_marked_Ward_channels':marked_channel,
                           'single_corner_value':corner_value})
    return output


def channel_leakage():
    out=[]
    for N in range(2,9):
        p,g,q=field(N);E=MixedEntries(N,p,q);d=N-1
        # The constant route at indices (0,d,0,d) crosses the middle pair
        # (d,0) to (0,d), with nonzero original coefficient.
        coeff=E.direct(pow(g,-1,p)*pow(E.Q,-1,p)%p,g,d,0,0,1)
        assert coeff
        out.append({'N':N,'initial_pair_totals':[d,d],
                    'output_pair_totals':[0,2*d],'nonzero_original_coefficient':coeff})
    return out


if __name__=='__main__':
    result={'scope':'exact root families; no moving-q or volume claim',
            'local':local_cases(),'whole_words':word_cases(),
            'interbridge_cap_block_leakage':channel_leakage()}
    target=Path(__file__).with_name('actual_rogers_bridge_transport_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(result['local']),'local root/color families;',
          len(result['whole_words']),'whole pointed plats;',
          len(result['interbridge_cap_block_leakage']),'leakage witnesses')
