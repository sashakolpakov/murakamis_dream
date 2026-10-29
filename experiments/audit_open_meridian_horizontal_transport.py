#!/usr/bin/env python3
"""Actual open meridian half-character, horizontal source and norm powers."""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries


def local_data(entries,x,i,j,k,sign):
    p,Q,q=entries.p,entries.Q,entries.q
    A,B,C=pow(Q,i,p),pow(Q,j,p),pow(Q,k,p)
    if sign>0:
        J=pow(-1,k,p)*pow(x,-i-j-k,p)*pow(Q,i*j+(i-j)*k-k*(k+1)//2,p)%p
        J=J*entries.gaussian(j+k,k)%p
        z=Q*x*x*pow(A,-1,p)%p
        inserted=x*pow(B*C%p,-1,p)*J*entries.pochhammer(Q*z%p,k)%p
        first=j+k
    else:
        J=pow(x,i+j-k,p)*pow(Q,-i*j,p)*entries.gaussian(i+k,k)%p
        z=Q*x*x*pow(B,-1,p)%p
        inserted=A*pow(x,-1,p)*J*entries.pochhammer(Q*z%p,k)%p
        first=j-k
    shifted=entries.direct(q*x%p,q*x%p,i,j,k,sign)
    expected=pow(x,-sign,p)*pow(q,first-i,p)*inserted%p
    assert shifted==expected
    M=-q*x%p
    # The global position-potential basis removes the half-character
    # at each crossing before composing any braid word.
    horizontal_new=pow(q*M%p,-(first-i),p)*shifted%p
    horizontal_expected=pow(x,-sign,p)*pow(M,-(first-i),p)*inserted%p
    assert horizontal_new==horizontal_expected
    return entries.direct(x,x,i,j,k,sign),shifted,inserted,first-i


def local_cases():
    count=0
    for N in range(2,8):
        p,g,qroot=field(N)
        for q in (qroot,g):
            entries=MixedEntries(N,p,q)
            for M in (1,pow(g,3,p)):
                x=-M*pow(q,-1,p)%p
                for i,j,sign in product(range(N),range(N),(-1,1)):
                    maximum=min(i,N-1-j) if sign>0 else min(j,N-1-i)
                    for k in range(maximum+1):
                        local_data(entries,x,i,j,k,sign)
                        count+=1
    return count


def path_case(N,strands,word,split,slot,generic=False):
    p,g,qroot=field(N);q=g if generic else qroot;Q=q*q%p
    entries=MixedEntries(N,p,q);M=pow(g,3,p);x=-M*pow(q,-1,p)%p
    writhe=sum(sign for _,sign in word);kappa=writhe-strands+1
    gamma=pow(q,(N-1)*kappa,p)
    checked=nonzero_offsets=0
    def recurse(initial,state,t,phase,old,new,inserted,offset=None):
        nonlocal checked,nonzero_offsets
        if t==split and offset is None:
            before=state[slot]
            for after in range(N):
                changed=list(state);changed[slot]=after
                recurse(initial,tuple(changed),t,phase,old,new,inserted,before-after)
            return
        if t==len(word):
            if any(state[j]!=initial[j] for j in range(1,strands)):return
            assert state[0]==initial[0]-offset
            assert phase==-slot*offset
            # Original source ratio, including all old closed pivots/framing.
            lhs=pow(q*x%p,(N-1)*kappa,p)*new%p
            rhs=pow(x,(N-1)*kappa,p)*gamma*pow(x,-writhe,p)%p
            rhs=rhs*pow(q,-slot*offset,p)*inserted%p
            assert lhs==rhs
            # The horizontal gauge cancels this literal endpoint character.
            assert pow(q*M%p,slot*offset,p)*lhs%p == (
                pow(M,slot*offset,p)*pow(x,(N-1)*kappa,p)*gamma
                *pow(x,-writhe,p)*inserted)%p
            checked+=1;nonzero_offsets+=int(offset!=0)
            return
        position,sign=word[t];i,j=state[position:position+2]
        maximum=min(i,N-1-j) if sign>0 else min(j,N-1-i)
        for k in range(maximum+1):
            aa,bb,cc,delta=local_data(entries,x,i,j,k,sign)
            out=(j+k,i-k) if sign>0 else (j-k,i+k)
            changed=state[:position]+out+state[position+2:]
            recurse(initial,changed,t+1,phase+delta,old*aa%p,new*bb%p,inserted*cc%p,offset)
    for initial in product(range(N),repeat=strands):
        recurse(initial,initial,0,0,1,1,1)
    assert checked and nonzero_offsets
    return {"N":N,"strands":strands,"word":word,"split":split,"slot":slot,
            "generic_q":generic,"actual_open_paths":checked,"nonzero_offsets":nonzero_offsets}


def source_rows_and_aliases():
    units=aliases=0
    for N in range(2,9):
        p,g,qroot=field(N)
        for q in (qroot,g):
            Q=q*q%p;M=pow(g,3,p)
            for a,c,ell in product(range(N),range(N),(1,2)):
                lhs=(pow(M,ell*(a-c),p)-1)%p
                if c==a:assert lhs==0
                else:
                    dk=(pow(Q,a-c,p)-1)%p
                    beta=lhs*pow(dk,-1,p)%p
                    assert beta*dk%p==lhs
                # Covariant M derivative, tested on M*E_ca.
                exponent=1+ell*(a-c)
                value=pow(M,exponent,p)
                assert (exponent+ell*(c-a))*value%p==value
                units+=1
        q=qroot;Q=q*q%p
        for ell,nu in product((0,1,2,3),range(-2*N,2*N+1)):
            rho=pow(q,-ell,p)
            left=sum(pow(rho*pow(Q,j,p)%p,nu,p) for j in range(N))*pow(N,-1,p)%p
            right=pow(pow(rho,N,p),nu//N,p) if nu%N==0 else 0
            assert left==right
            assert pow(rho,N,p)==pow(-1,ell,p)
            aliases+=1
    return units,aliases


def scaled_whole_vandermonde():
    units=matrices=0
    for N,generic,ell in product(range(2,7),(False,True),(1,2)):
        p,g,qroot=field(N);q=g if generic else qroot;Q=q*q%p;M=pow(g,3,p)
        V=sp.Matrix([[pow(Q,j*b,p) for b in range(N)] for j in range(N)])
        Vi=V.inv_mod(p)
        diag=lambda f:sp.diag(*(int(f(b))%p for b in range(N)))
        D2=diag(lambda b:pow(M,-ell*b,p))
        W=(V*D2.inv_mod(p))%p;Wi=(D2*Vi)%p
        Wnew=(V*diag(lambda b:pow(q*M%p,ell*b,p)))%p
        rho=diag(lambda b:pow(q,-ell*b,p))
        assert (Wnew*rho-W)%p==sp.zeros(N)
        assert (W*Wi)%p==sp.eye(N)
        DM=sp.Matrix(N,N,lambda j,b:ell*b*W[j,b]%p)
        AM=(ell*V*sp.diag(*range(N))*Vi)%p
        assert (DM*Wi-AM)%p==sp.zeros(N)
        # Entrywise partial trace on every actual four-port unit.
        for a,b,c,d in product(range(N),repeat=4):
            represented=sum(int(W[j,d])*int(Wi[b,j]) for j in range(N))%p
            assert represented==int(b==d)
            units+=1
        matrices+=1
    return matrices,units


def root_cyclic_packet():
    count=0
    for N,ell,theta in product((2,3,4,8,16),(1,2),(0.3,1.2)):
        Q=np.exp(2j*np.pi/N);M=np.exp(1j*theta)
        S=np.zeros((N,N),complex)
        for j in range(N):S[j,(j+1)%N]=1
        for a in (0,N//2,N-1):
            offsets=a-np.arange(N)
            F=np.array([[Q**(j*nu) for nu in offsets] for j in range(N)])
            Fi=F.conj().T/N
            H=(F*(M**(ell*offsets))[None,:])@Fi
            A=(F*(ell*offsets)[None,:])@Fi
            assert np.linalg.norm(H.conj().T@H-np.eye(N))<1e-9
            assert np.linalg.norm(H@S-S@H)<1e-9
            ones=np.ones(N)
            assert np.linalg.norm(ones@H-ones)<1e-9
            assert np.linalg.norm(H@ones-ones)<1e-9
            assert np.linalg.norm(ones@A)<1e-8 and np.linalg.norm(A@ones)<1e-8
            assert np.linalg.norm(A,2)<=ell*(N-1)+1e-8
            count+=1
    return count


def exact_packet_window_carries():
    count=0
    for N,ell in product(range(2,9),(1,2)):
        p,g,q=field(N);Q=q*q%p;M=pow(g,3,p);invN=pow(N,-1,p)
        def packet(a):
            F=sp.Matrix([[pow(Q,j*(a-c),p) for c in range(N)] for j in range(N)])
            Fi=sp.Matrix([[invN*pow(Q,-j*(a-c),p)%p for j in range(N)] for c in range(N)])
            H=(F*sp.diag(*(pow(M,ell*(a-c),p) for c in range(N)))*Fi)%p
            A=(ell*F*sp.diag(*(a-c for c in range(N)))*Fi)%p
            return H,A
        for a in range(N-1):
            H,A=packet(a);H1,A1=packet(a+1)
            Pi=sp.Matrix(N,N,lambda j,k:invN*pow(Q,int(j-k)*(a+1),p)%p)
            assert (A1-A-ell*N*Pi)%p==sp.zeros(N)
            assert (H1*H.inv_mod(p)-sp.eye(N)-(pow(M,ell*N,p)-1)*Pi)%p==sp.zeros(N)
            count+=1
    return count


def pointed_wrap_and_norm_filter():
    M,z=sp.symbols('M z',nonzero=True)
    for N,ell in product(range(2,6),(1,2)):
        D=sp.diag(*(M**(ell*j) for j in range(N)))
        P=sp.zeros(N);W=sp.zeros(N);W[0,N-1]=1
        for j in range(N):P[(j+1)%N,j]=1
        hor=D.inv()*P*D
        assert hor==M**(-ell)*(P+(M**(ell*N)-1)*W)
        assert hor**N==sp.eye(N)
        characteristic=hor.charpoly()
        assert sp.expand(characteristic.as_expr().subs(characteristic.gen,z)-(z**N-1))==0
        row=sp.ones(1,N)*D
        assert row*hor==row
    filters=0
    for N in range(2,9):
        p,g,q=field(N);Q=q*q%p
        for S,v in ((1,1),(-1,q)):
            for lam in (2,3,5):
                den=(S-pow(lam,N,p))%p
                if not den:continue
                points=[v*pow(Q,j,p)%p for j in range(N)]
                actual=sum(t*pow((t-lam)%p,-2,p) for t in points)*pow(N,-1,p)%p
                expected=N*S*pow(lam,N-1,p)*pow(den,-2,p)%p
                assert actual==expected
                filters+=1
    ell,N,L=sp.symbols('ell N L',nonzero=True)
    u=sp.symbols('u')
    ratio=sp.exp(ell*N*u)*((1-L)/(1-sp.exp(ell*N*u)*L))**2
    assert sp.simplify(sp.diff(ratio,u).subs(u,0)-ell*N*(1+L)/(1-L))==0
    return filters


def source_metric():
    cases=0
    for N,ell,a,theta in product((2,3,4,8,16,32),(1,3),(0,1),(0.0,0.3,1.2)):
        if a>=N:continue
        Q=np.exp(2j*np.pi/N);M=np.exp(1j*theta)
        differences=np.array([a-c for c in range(N) if c!=a])
        gaps=Q**differences-1
        beta=(M**(ell*differences)-1)/gaps
        assert np.linalg.norm(beta)**2 <=(N*N-1)/3+1e-8
        for k in (1,2,3):
            jet=(ell*differences)**k/gaps
            assert np.linalg.norm(jet)<=ell**k*N**(k+1)/np.sqrt(12)+1e-6
        cases+=1
    return cases


def main():
    paths=[]
    for N,generic in product((2,3),(False,True)):
        for word in (((0,1),),((0,1),(0,1),(0,1)),((0,-1),(0,-1),(0,-1))):
            for split,slot in ((0,1),(1,0),(len(word),1)):
                paths.append(path_case(N,2,word,split,slot,generic))
        word=((0,1),(1,-1),(0,1),(1,-1))
        for split,slot in ((1,1),(2,2)):
            paths.append(path_case(N,3,word,split,slot,generic))
    units,aliases=source_rows_and_aliases()
    scaled_matrices,scaled_units=scaled_whole_vandermonde()
    result={"status":"PASS","literal_local_M_shifts":local_cases(),
            "actual_open_path_cases":paths,"whole_source_rows":units,
            "semilinear_alias_powers":aliases,
            "whole_scaled_Vandermonde_matrices":scaled_matrices,
            "whole_scaled_four_port_source_units":scaled_units,
            "root_cyclic_source_current_packet_isometries":root_cyclic_packet(),
            "exact_unwrapped_packet_window_carries":exact_packet_window_carries(),
            "pointed_wrap_and_periodic_antiperiodic_filters":pointed_wrap_and_norm_filter(),
            "unit_arc_source_metric_checks":source_metric(),
            "scope":"Actual word/source transport and geometric principal-filter compatibility; "
                    "no selected global geometric map or norm limit is inferred."}
    out=Path(__file__).with_name('open_meridian_horizontal_transport_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","local_M_shifts":result['literal_local_M_shifts'],
                      "path_families":len(paths),"actual_open_paths":sum(x['actual_open_paths'] for x in paths),
                      "source_rows":units,"alias_powers":aliases,
                      "scaled_whole_matrices":scaled_matrices,"scaled_source_units":scaled_units,
                      "cyclic_packet_isometries":result['root_cyclic_source_current_packet_isometries'],
                      "packet_window_carries":result['exact_unwrapped_packet_window_carries'],
                      "root_filters":result['pointed_wrap_and_periodic_antiperiodic_filters'],
                      "metric_cases":result['unit_arc_source_metric_checks'],"output":str(out)},indent=2))


if __name__=='__main__':main()
