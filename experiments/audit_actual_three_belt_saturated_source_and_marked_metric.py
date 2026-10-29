#!/usr/bin/env python3
"""Original six-port source and the exact three-C marked Riesz obstruction."""
import itertools,json
from pathlib import Path
import numpy as np
from audit_actual_two_cut_ports import balanced_data,coproduct
from audit_actual_six_port_divided_power_source_kernel import ActualDivided,states
from audit_actual_pair_casimir_commutant_and_rotated_trace import rank


def circle(A,N,p=None):
    I=np.eye(len(A),dtype=np.int64 if p else complex)
    u,v=I,A.copy()
    for _ in range(2,N):
        u,v=v,A@v-u
        if p:v%=p
    return ((-1)**(N-1)*v)%p if p else (-1)**(N-1)*v


def pair_embed(A,st,slot,N,p=None):
    idx={s:i for i,s in enumerate(st)}
    out=np.zeros((len(st),len(st)),dtype=np.int64 if p else complex)
    for j,s in enumerate(st):
        for row in np.flatnonzero(A[:,s[slot]*N+s[slot+1]]):
            t=s[:slot]+(int(row)//N,int(row)%N)+s[slot+2:]
            if t in idx:out[idx[t],j]=A[row,s[slot]*N+s[slot+1]]
    return out


def projector(A,nodes,p=None):
    I=np.eye(len(A),dtype=np.int64 if p else complex);c=nodes[0]
    value=I.copy();derivative=0
    for b in nodes[1:]:
        inverse=pow((c-b)%p,-1,p) if p else 1/(c-b)
        value=value@(A-b*I)*inverse
        if p:value%=p
        derivative+=inverse
    out=value@value@(I-2*derivative*(A-c*I))
    return out%p if p else out


def field_phi(N,data):
    p,d,x=data.p,N-1,pow(data.q,N-1,data.p)
    st=states(N,4,2*d);six=states(N,6,3*d);idx={s:i for i,s in enumerate(six)}
    result=np.zeros((len(six),len(st)),dtype=np.int64)
    for col,w in enumerate(st):
        power={w:1};H={}
        for c in range(N):
            coef=pow(-x*data.Q,c,p)*pow(data.ff[c],-1,p)%p
            for a,v in power.items():H[a+(c,)]=(H.get(a+(c,),0)+coef*v)%p
            power=data.apply('E',power,1) if power else {}
        power=H
        for a in range(N):
            coef=N*pow(x,a-d,p)*pow(data.ff[a],-1,p)%p
            for s,v in power.items():result[idx[s+(d-a,)],col]=(result[idx[s+(d-a,)],col]+coef*v)%p
            power=data.apply('F',power,1) if power else {}
    return result,six


def apply_sparse(A,V,st,slot,N,p):
    idx={s:i for i,s in enumerate(st)};out=np.zeros_like(V)
    for col,s in enumerate(st):
        for row in np.flatnonzero(A[:,s[slot]*N+s[slot+1]]):
            t=s[:slot]+(int(row)//N,int(row)%N)+s[slot+2:]
            if t in idx:out[idx[t],:]=(out[idx[t],:]+int(A[row,s[slot]*N+s[slot+1]])*V[col,:])%p
    return out


def field_case(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d=N-1;data=ActualDivided(N,p,q);x=pow(q,d,p)
    st=states(N,4,2*d);I=np.eye(len(st),dtype=np.int64)
    Et,Ft,Kt=coproduct(data.rho**2*E%p,F,K,2,N,p)
    O=(Ft@Et+q*Kt+pow(q,-1,p)*np.diag([pow(int(z),-1,p) for z in np.diag(Kt)]))%p
    swap=np.zeros((N*N,N*N),dtype=np.int64)
    for a,b in itertools.product(range(N),repeat=2):swap[a*N+b,b*N+a]=1
    Ec=data.rho**2*E%p;one=np.eye(N,dtype=np.int64)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    currentE=(np.kron(Ec,K-one)-np.kron(K-one,Ec))@swap%p
    currentF=(np.kron(F,one-Ki)-np.kron(one-Ki,F))@swap%p
    assert np.array_equal((Et@swap-swap@Et)%p,currentE)
    assert np.array_equal((Ft@swap-swap@Ft)%p,currentF)
    A=pair_embed(O,st,0,N,p);B=pair_embed(O,st,2,N,p)
    E4=data.matrix('E',4,2*d,1);F4=data.matrix('F',4,2*d-1,1)
    D=(F4@E4+(q+pow(q,-1,p))*I)%p
    JE=data.matrix('E',4,2*d,N);JF=data.matrix('F',4,N-2,N)
    constant=2*(-1)**N*pow(data.rho,2*N,p)%p
    S=(I-pow(constant,-1,p)*(JF@JE%p))%p
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(d//2+1)]
    EA,EB,ED=[projector(X,nodes,p) for X in (A,B,D)]
    E000=EA@EB%p@ED%p
    assert np.array_equal(E000@E000%p,E000)
    assert rank(E000@S%p,p)==5
    T=circle(A,N,p)@circle(B,N,p)%p@circle(D,N,p)%p
    assert not np.any(T@E000@S%p)
    lam=np.array([pow(x,a[0]+a[2],p)*pow(N,-2,p)%p
                  if a[0]+a[1]==d and a[2]+a[3]==d else 0 for a in st],dtype=np.int64)
    w=np.array([N*N*pow(x,-a[2],p)%p if a[0]==0 and a[3]==d and a[1]+a[2]==d else 0
                for a in st],dtype=np.int64)
    assert not np.any(JE@w%p)
    u=E000@w%p
    assert np.array_equal(S@u%p,u)
    assert int(lam@w%p)==int(lam@u%p)==1
    assert not np.any(T@u%p)
    assert np.array_equal(lam@E000@S%p,lam@S%p)
    result={'N':N,'source_rank':(N**3+N)//2,'full_normal_joint000_rank':5,
            'original_marked_evaluation':1,'triple_complete_circle_output':0,
            'exact_divided_source_and_Hermite_cluster_coupons':True,
            'both_exact_marked_pair_moment_currents':True}
    if N<=5:
        Phi,six=field_phi(N,data)
        src=Phi@S%p
        swap=np.zeros((N*N,N*N),dtype=np.int64)
        for a,b in itertools.product(range(N),repeat=2):swap[a*N+b,b*N+a]=1
        marked=apply_sparse(swap,src,six,4,N,p);unmarked=src.copy()
        L=circle(O,N,p)
        last=apply_sparse(O,Phi,six,4,N,p)
        assert np.array_equal(last,Phi@D%p)
        for slot in (0,2,4):
            marked=apply_sparse(L,marked,six,slot,N,p)
            unmarked=apply_sparse(L,unmarked,six,slot,N,p)
        result.update({'literal_all_input_sixhead_lastpair_Casimir':True,
                       'rank_CCC':rank(unmarked,p),'rank_CCH':rank(marked,p)})
        assert not np.any(apply_sparse(L,apply_sparse(L,apply_sparse(L,Phi@u[:,None]%p,six,0,N,p),six,2,N,p),six,4,N,p))
    return result


def complex_case(N):
    d=N-1;q=np.exp(np.pi*1j/N);Q=q*q;x=q**d
    E=np.diag([Q**(-a)-1 for a in range(1,N)],1)
    F=np.diag([1-Q**(a+1) for a in range(d)],-1)
    K=np.diag([x*Q**(-a) for a in range(N)])
    Et=np.kron(E,K)+np.kron(np.eye(N),E)
    Ft=np.kron(F,np.eye(N))+np.kron(np.linalg.inv(K),F)
    Kt=np.kron(K,K);O=Ft@Et+q*Kt+q**-1*np.linalg.inv(Kt)
    st=states(N,4,2*d);low=states(N,4,2*d-1);idx={s:i for i,s in enumerate(st)}
    ilow={s:i for i,s in enumerate(low)}
    E4=np.zeros((len(low),len(st)),complex);F4=E4.T.copy()
    def apply(vector,kind):
        out={}
        for a,value in vector.items():
            for k in range(len(a)):
                if kind=='E':
                    if not a[k]:continue
                    b=a[:k]+(a[k]-1,)+a[k+1:]
                    c=(Q**(-a[k])-1)*np.prod([x*Q**(-z) for z in a[k+1:]])
                else:
                    if a[k]==d:continue
                    b=a[:k]+(a[k]+1,)+a[k+1:]
                    c=(1-Q**(a[k]+1))*np.prod([x**-1*Q**z for z in a[:k]])
                out[b]=out.get(b,0)+c*value
        return out
    for j,a in enumerate(st):
        for b,c in apply({a:1},'E').items():E4[ilow[b],j]=c
    for j,a in enumerate(low):
        for b,c in apply({a:1},'F').items():F4[idx[b],j]=c
    A=pair_embed(O,st,0,N);B=pair_embed(O,st,2,N);D=F4@E4+(q+q**-1)*np.eye(len(st))
    nodes=[2*np.cos((2*j+1)*np.pi/N) for j in range(d//2+1)]
    w=np.array([N*N*x**(-a[2]) if a[0]==0 and a[3]==d and a[1]+a[2]==d else 0 for a in st],complex)
    u=projector(A,nodes)@projector(B,nodes)@projector(D,nodes)@w
    fac=[1]
    for a in range(1,N):fac.append(fac[-1]*(1-Q**a))
    H={};power={a:v for a,v in zip(st,u) if abs(v)>1e-15}
    for c in range(N):
        for a,v in power.items():H[a+(c,)]=H.get(a+(c,),0)+(-x*Q)**c/fac[c]*v
        power=apply(power,'E')
    final={};power=H
    for a in range(N):
        for b,v in power.items():final[b+(d-a,)]=final.get(b+(d-a,),0)+N*x**(a-d)/fac[a]*v
        power=apply(power,'F')
    vector=np.zeros(N**6,complex)
    for a,v in final.items():vector[sum(z*N**(5-j) for j,z in enumerate(a))]=v
    swap=np.zeros((N*N,N*N),complex)
    ell=np.zeros(N*N,complex);mark=np.zeros(N*N,complex)
    for a,b in itertools.product(range(N),repeat=2):
        swap[a*N+b,b*N+a]=1;mark[a*N+b]=x**b/N**2
        if a+b==d:ell[a*N+b]=x**a/N
    marked=np.kron(np.kron(ell,ell),mark)@vector
    assert abs(marked-1)<1e-7
    L=circle(O,N);C=swap@L;H=L@swap
    def pair_apply(A,v,slot):
        order=[slot,slot+1]+[j for j in range(6) if j not in (slot,slot+1)]
        moved=v.reshape((N,)*6).transpose(order)
        result=(A@moved.reshape(N*N,-1)).reshape((N,)*6)
        return result.transpose(np.argsort(order)).reshape(-1)
    cu,hu=vector.copy(),vector.copy()
    for slot in (0,2,4):
        cu=pair_apply(C,cu,slot);hu=pair_apply(H if slot==4 else C,hu,slot)
    assert np.linalg.norm(cu)<1e-7*max(1,np.linalg.norm(vector)*np.linalg.norm(C,2)**3)
    energy=float(np.vdot(vector,hu).real);bound=8*N**11
    assert energy>=bound*(1-1e-7)
    return {'N':N,'original_unrestricted_marked_value':float(marked.real),
            'actual_CCH_energy':energy,'proved_required_lower_bound':bound,
            'CCC_output_relative_residual':float(np.linalg.norm(cu)/max(1,np.linalg.norm(vector)*np.linalg.norm(C,2)**3))}


if __name__=='__main__':
    result={'status':'PASS','exact_source_and_cluster_levels':[field_case(N) for N in range(2,9)],
            'independent_complex_original_marked_forms':[complex_case(N) for N in range(2,5)],
            'scope':'Exact all-N source proof is in the note; finite field and complex audits verify literal maps and retained normal/source typing, not an asymptotic extrapolation.'}
    Path(__file__).with_name('actual_three_belt_saturated_source_and_marked_metric_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 7 exact saturated-source/full-Hermite levels; 4 all-input sixhead marked comparisons; 3 original complex positive forms')
