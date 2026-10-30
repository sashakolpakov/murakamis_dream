#!/usr/bin/env python3
"""Original endpoint normalization and the fully shared positive Fourier sum.

Finite-field endpoint identities are exact. The finite positive/Cauchy
checks use high precision and are diagnostics, not asymptotic evidence.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp

from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from audit_actual_two_cut_ports import balanced_data


def data(N, q, imag, modulus=None, eta=None):
    d=N-1; Q=q*q
    reduce=(lambda z:z%modulus) if modulus else (lambda z:z)
    power=(lambda z,n:pow(int(z),n,modulus)) if modulus else (lambda z,n:mp.mpc(z)**n)
    divide=lambda z,w:reduce(z*power(w,-1))
    Q=reduce(Q); fac=[1]
    for h in range(1,N):fac.append(reduce(fac[-1]*(1-power(Q,h))))
    sf=[reduce(power(imag,h)*power(q,-h*(h+1)//2)*fac[h]) for h in range(N)]
    W={};pi={};h0={};omega={};polys={}
    for a in range(d//2+1):
        ell=d-a;cols=[]
        first=[0]*(N*N)
        for u in range(ell+1):
            first[u*N+ell-u]=divide((-1)**u*power(q,-d*u)
                *power(Q,u*(ell-1)-u*(u-1)//2)*fac[a+u]*fac[d-u],fac[a]*fac[d])
        cols.append(first)
        for r in range(1,2*a+1):
            nxt=[0]*(N*N)
            for u in range(N):
                for v in range(N):
                    z=cols[-1][u*N+v]
                    if u<d:nxt[(u+1)*N+v]+=z*(1-power(Q,u+1))
                    if v<d:nxt[u*N+v+1]+=z*power(q,-d+2*u)*(1-power(Q,v+1))
            cols.append([divide(z,1-power(Q,r)) for z in nxt])
        W[a]=cols;dual=[]
        gamma=divide(power(q,2-a*a),N*N)
        for r in range(2*a+1):
            s=2*a-r
            cup=divide((-1)**s*power(q,s*(2*a-s-1))*fac[s]*fac[r],fac[2*a])
            row=[]
            for u in range(N):
                for v in range(N):
                    row.append(divide(cup*cols[s][(d-v)*N+d-u]*power(q,d*(u+v)),N*N*gamma))
            dual.append(row)
        pi[a]=dual
        ka=1 if 2*a==d else 2
        h0[a]=divide(ka*N*sf[2*a],sf[a]**2)
        omega[a]=reduce(power(eta,d*d)*(-1)**a*power(q,a*(a+1))) if eta else mp.exp(mp.pi*1j*d*d/(2*N))*(-1)**a*q**(a*(a+1))
        ac=[1]
        sine=lambda h:divide(power(q,h)-power(q,-h),2*imag)
        for n in range(a+1):
            h=a-n
            bc=[divide(sf[h],sf[k]*sf[h-k]) for k in range(h+1)]
            pc=[reduce(sum(ac[k]*bc[r-k] for k in range(max(0,r-h),min(n,r)+1))) for r in range(a+1)]
            polys[d-h,a]=pc
            if h:
                get=lambda k:ac[k] if 0<=k<=n else 0
                ac=[divide(sine(a+h-k)*get(k)+2*sine(a-k+1)*get(k-1)+sine(n-k+2)*get(k-2),sine(h)) for k in range(n+2)]
    return dict(N=N,d=d,q=q,Q=Q,fac=fac,sf=sf,W=W,pi=pi,h0=h0,omega=omega,polys=polys)


def exact_endpoints():
    count=dict(actual_original_entries=0,endpoint_norms=0,white_endpoint_norms=0,
               high_chevalley_entries=0,full_source_scalar_squares=0)
    for N in range(2,15):
        p,eta,q,*_=balanced_data(N);imag=pow(eta,N,p);d=N-1
        D=data(N,q,imag,p,eta);bar=data(N,pow(q,-1,p),-imag%p,p,pow(eta,-1,p))
        if N<=8:
            original=Local(N)
            for a,cols in D['W'].items():
                for r,col in enumerate(cols):
                    for u,z in enumerate(col):
                        assert z==int(original.W[a][0][u,r])
                        assert D['pi'][a][r][u]==int(original.pi[a][0][r,u])
                        count['actual_original_entries']+=2
        s=D['sf']
        for a,cols in D['W'].items():
            high=cols[2*a][a*N+d]
            kap=pow(q,-N*(d-a),p)*pow(high,-1,p)%p
            assert kap*kap%p==pow(q,-2*N*d+2*a*(2*a+1),p)
            for r,col in enumerate(cols):
                T=d-a+r;t=min(T,2*d-T);b=max(0,T-d);w=abs(r-a)
                endpoint=b*N+T-b
                cw=col[endpoint];cwbar=bar['W'][a][r][endpoint]
                expected=s[a]*pow(s[w]*s[a-w],-1,p)%p
                assert cw*cwbar%p==expected*expected%p
                count['endpoint_norms']+=1
                cp=D['pi'][a][r][endpoint];cpbar=bar['pi'][a][r][endpoint]
                metric=s[2*a]*pow(s[r]*s[2*a-r],-1,p)%p
                assert cp*cpbar%p==expected*expected*pow(metric,-2,p)%p
                count['white_endpoint_norms']+=1
                ka=1 if 2*a==d else 2
                scalar=ka*N*s[a+w]*pow(s[a]**2*s[w]**2*s[a-w],-1,p)%p
                actual=D['h0'][a]**2*cw*cwbar*cp*cpbar*pow(s[a],-4,p)%p
                assert actual==scalar*scalar%p
                count['full_source_scalar_squares']+=1
                for u in range(N):
                    v=T-u
                    if not 0<=v<N:continue
                    left=pow(q,-N*T,p)*col[u*N+v]%p
                    right=kap*pow(q,-(2*a+1)*r,p)*cols[2*a-r][(d-v)*N+d-u]%p
                    assert left==right
                    count['high_chevalley_entries']+=1
    return count


def convolution(a,b):
    n=len(a);out=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[(i+j)%n]+=x*y
    return out


def graph(k):
    nodes=[];edges={};current=[]
    def add(kind,circle=None):
        v=len(nodes);nodes.append((kind,circle));return v
    def connect(a,b):edges[a]=b;edges[b]=a
    for h in range(k):
        v=add('cup');current.extend([(v,0),(v,1)])
    boxes=list(range(1,2*k-2,2))+list(range(0,2*k-1,2))+list(range(1,2*k-2,2))
    for i,slot in enumerate(boxes):
        vi=add('pi',i);vo=add('W',i)
        connect(current[slot],(vi,0));connect(current[slot+1],(vi,1))
        current[slot],current[slot+1]=(vo,0),(vo,1)
    for h in range(k):
        v=add('cap');connect(current[2*h],(v,0));connect(current[2*h+1],(v,1))
    mark=len(nodes)-1;cycles=[];seen=set()
    for start in [mark]+list(range(len(nodes))):
        if start in seen:continue
        entry=1 if start==mark else 0
        order=[];v,port=start,entry
        while True:
            order.append((v,port));seen.add(v);v,port=edges[v,1-port]
            if (v,port)==(start,entry):break
        cycles.append(order)
    return nodes,cycles,boxes


def original_morse(D,boxes,signs,k):
    N,d,q=D['N'],D['d'],D['q'];state={}
    for us in itertools.product(range(N),repeat=k):
        key=tuple(y for u in us for y in (u,d-u))
        state[key]=mp.fprod(N*q**(-d*d+d*u) for u in us)
    for i,slot in enumerate(boxes):
        matrix={}
        for a,cols in D['W'].items():
            scale=D['h0'][a]*D['omega'][a]**signs[i]
            for r,col in enumerate(cols):
                T=d-a+r
                for u in range(N):
                    v=T-u
                    if not 0<=v<N:continue
                    for x in range(N):
                        y=T-x
                        if 0<=y<N:
                            key=(u,v,x,y)
                            matrix[key]=matrix.get(key,0)+scale*col[u*N+v]*D['pi'][a][r][x*N+y]
        nxt={}
        for key,z in state.items():
            x,y=key[slot:slot+2]
            for u in range(N):
                v=x+y-u
                if 0<=v<N:
                    out=key[:slot]+(u,v)+key[slot+2:]
                    nxt[out]=nxt.get(out,0)+matrix.get((u,v,x,y),0)*z
        state=nxt
    value=0
    for key,z in state.items():
        if any(key[2*h]+key[2*h+1]!=d for h in range(k-1)):continue
        value+=z*mp.fprod(q**(d*key[2*h])/N for h in range(k-1))*q**(d*key[-1])/(N*N)
    return value


def full_partition(N,k,signs):
    q=mp.exp(mp.pi*1j/N);D=data(N,q,1j);d=N-1;s=D['sf']
    nodes,cycles,boxes=graph(k);R=len(boxes);C=len(cycles)
    labels=[(a,w) for a in D['W'] for w in range(-a,a+1)]
    exact=0;positive=mp.mpf(0);state_count=0;flow_count=0;phase_checks=0
    for lab in itertools.product(labels,repeat=R):
        defects=[sum((1 if nodes[v][0]=='W' else -1)*lab[nodes[v][1]][1]
                     for v,_ in order if nodes[v][0] in ('W','pi')) for order in cycles]
        assert sum(defects)==0
        if any(defects):continue
        flow_count+=1;coherent=1;posprod=1;number=1;endpointprod=1
        for ci,order in enumerate(cycles):
            actual=[1]+[0]*(2*N-1);pos=[1]+[0]*(2*N-1);num=[1]+[0]*(2*N-1)
            eps,shift=1,0;E=0;vertex_eps=0;cup_eps=0
            for v,entry in order:
                kind,i=nodes[v];T=d+(lab[i][1] if i is not None else 0)
                se=eps if entry==0 else -eps;sb=shift if entry==0 else T-shift
                E+=se
                aa=[0]*(2*N);pp=[0]*(2*N);nn=[0]*(2*N)
                if i is not None:
                    a,w=lab[i];r=a+w;t=d-abs(w);b=max(0,w)
                    src=D['W'][a][r] if kind=='W' else D['pi'][a][r]
                    cv=src[b*N+T-b]
                    ct=q**(a*(t+a-d))/D['fac'][a]
                    endpointprod*=abs(cv*ct);vertex_eps+=se
                    for h,pcoef in enumerate(D['polys'][t,a]):
                        assert abs(mp.im(pcoef))<mp.mpf('1e-65') and mp.re(pcoef)>0
                        pcoef=mp.re(pcoef);carrier=d-2*a+2*h;index=carrier*se%(2*N)
                        aa[index]+=cv*ct*pcoef*q**(carrier*(sb-b)-t*h)
                        pp[index]+=pcoef*pcoef;nn[index]+=1
                        # Literal source character equals q^-1 times the selected coefficient momentum.
                        Y=mp.exp(2*mp.pi*1j*(mp.mpf(h)/N+mp.mpf('.5')-mp.mpf(a)/N))
                        assert abs(q**carrier-Y/q)<mp.mpf('1e-65');phase_checks+=1
                else:
                    scale=N*q**(-d*d) if kind=='cup' else mp.mpf(1)/N
                    aa[d*se%(2*N)]=scale*q**(d*sb)
                    pp[d*se%(2*N)]=nn[d*se%(2*N)]=1;cup_eps+=se
                actual=convolution(actual,aa);pos=convolution(pos,pp);num=convolution(num,nn)
                eps,shift=-eps,T-shift
            assert eps==1 and shift==0 and E%2==0
            assert all(abs(actual[h])<mp.mpf('1e-60') for h in range(1,2*N,2))
            charge=1 if ci==0 else 0
            coherent*=actual[2*charge];posprod*=pos[2*charge];number*=num[2*charge]
        B=mp.fprod((1 if 2*a==d else 2)*N*s[a+abs(w)]/(s[a]**2*s[abs(w)]**2*s[a-abs(w)]) for a,w in lab)
        hprod=mp.fprod(D['h0'][a] for a,w in lab)
        assert abs(hprod*endpointprod/B-1)<mp.mpf('1e-60')
        twist=mp.fprod(D['omega'][a]**signs[i] for i,(a,w) in enumerate(lab))
        exact+=hprod*twist*coherent;positive+=mp.re(B*B)*posprod;state_count+=number
    exact*=q**(-d*d)*N**(C-1)
    original=original_morse(D,boxes,signs,k)
    relative=abs(exact-original)/max(1,abs(original))
    assert relative<mp.mpf('1e-55')
    upper=state_count*N**(2*C-2)*positive
    assert abs(original)**2<=upper*(1+mp.mpf('1e-55'))
    assert state_count<=N**(4*R)
    return dict(N=N,width=k,circles=R,cycles=C,flow_states=flow_count,
                fully_constrained_coefficient_states=int(state_count),momentum_phase_checks=phase_checks,
                relative_full_source_error=mp.nstr(relative,18),
                source_absolute=mp.nstr(abs(original),18),positive_partition=mp.nstr(positive,18),
                Cauchy_ratio=mp.nstr(abs(original)**2/upper if upper else 0,18))


def main():
    mp.mp.dps=80
    exact=exact_endpoints()
    rows=[full_partition(N,2,signs) for N,signs in [(3,[0,0,0,0]),(3,[1,-1,1,0]),(4,[1,0,-1,1]),(5,[0,1,0,-1])]]
    result=dict(status='PASS',exact=exact,full_shared_partitions=rows,
                scope='Original endpoint norms, actual Chevalley high adapter, full marked source coefficient extraction and joint Cauchy comparison. Finite diagnostics do not prove a volume or noncancellation theorem.')
    Path(__file__).with_name('actual_matching_graph_positive_fourier_partition_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
