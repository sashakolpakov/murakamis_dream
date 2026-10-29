#!/usr/bin/env python3
"""Audit actual moment transport, original trace scale and free defect charges.

The finite canonical theorem and its source hypotheses are in
notes/actual_resolved_head_defect_moment_gluing.md. This script does not
claim a quantum endpoint-current deletion or a full period estimate.
"""
from pathlib import Path
import json
import numpy as np
from audit_actual_projected_transfer_cot_completion import Projected


E21=np.array([[0,0],[1,0]],complex)


def lower(k,f):
    return np.array([[1,0],[-k*f,k]],complex)


def product_lower(ks,fs):
    result=np.eye(2,dtype=complex)
    for k,f in zip(ks,fs):
        result=lower(k,f)@result
    return result


def quantum_checks():
    rows=[]
    for n in range(2,8):
        model=Projected(n)
        q=np.exp(2j*np.pi/n)
        x=-np.exp(-1j*np.pi/n)
        k=np.diag([x*q**(-a) for a in range(n)])
        f=np.zeros((n,n),complex)
        for a in range(n-1):f[a+1,a]=1-q**(a+1)
        ft=np.kron(f,np.eye(n))+np.kron(np.linalg.inv(k),f)
        kt=np.kron(k,k)
        for sig in (1,-1):
            r=model.original(sig)
            ef=np.linalg.norm(r@ft-ft@r)/max(1,np.linalg.norm(r)*np.linalg.norm(ft))
            ek=np.linalg.norm(r@kt-kt@r)/max(1,np.linalg.norm(r)*np.linalg.norm(kt))
            assert max(ef,ek)<1e-12,(n,sig,ef,ek)
            rows.append({"N":n,"sign":sig,"relative_F_Ward_error":float(ef),
                         "relative_K_Ward_error":float(ek)})
        g=np.diag([x**(1-n)*q**(-a) for a in range(n)])
        comm=np.linalg.norm(g@f-f@g,2)
        assert comm<=2*abs(q-1)*(1+1e-12)
    return rows


def moment_jumps():
    rows=[]
    for b in range(2,10):
        for j in range(b):
            ks=[complex(0.7+0.11*h,0.13-0.02*h) for h in range(b)]
            ks[j]=-1
            fs=[complex(0.3+0.07*h,-0.2+0.03*h) for h in range(b)]
            change=complex(.23,-.17)
            out=fs.copy();out[j]+=change
            actual=product_lower(ks,out)-product_lower(ks,fs)
            expected=-np.prod(ks[j:])*change*E21
            err=np.linalg.norm(actual-expected)
            assert err<1e-12,(b,j,err)
            # The F-total normalization has the claimed exact unit weight.
            before=sum(fs[h]/np.prod(ks[:h]) for h in range(b))
            after=sum(out[h]/np.prod(ks[:h]) for h in range(b))
            weight=1/np.prod(ks[:j])
            assert abs(after-before-weight*change)<1e-12
            rows.append({"heads":b,"defect_head":j,"matrix_jump_error":float(err)})
    return rows


def based(zs):
    hs=[];prefix=np.eye(2,dtype=complex)
    for j,z in enumerate(zs):
        f=(-1)**j*z
        g=-np.eye(2,dtype=complex)-f*E21
        h=np.linalg.inv(prefix)@g@prefix
        assert np.linalg.norm(h+np.eye(2)+z*E21)<1e-12
        hs.append(h)
        prefix=lower(-1,f)@prefix
    return hs


def commuting_hurwitz():
    rows=[]
    for b in range(2,8):
        zs=[complex(1+.21*j,.1+.03*j) for j in range(b)]
        hs=based(zs)
        for i in range(b-1):
            for sig in (1,-1):
                target=hs.copy()
                if sig>0:
                    target[i]=hs[i+1]
                    target[i+1]=hs[i+1]@hs[i]@np.linalg.inv(hs[i+1])
                else:
                    target[i]=np.linalg.inv(hs[i])@hs[i+1]@hs[i]
                    target[i+1]=hs[i]
                zz=zs.copy();zz[i],zz[i+1]=zz[i+1],zz[i]
                result=based(zz)
                err=max(np.linalg.norm(a-bb) for a,bb in zip(target,result))
                assert err<1e-12,(b,i,sig,err)
                rows.append({"heads":b,"crossing":i+1,"sign":sig,"swap_error":float(err)})
    return rows


def forced_flow_checks():
    rows=[]
    eps=.2
    for n in (8,32,128):
        for width in (2,3,5,8):
            r=5
            weights=[]
            for defect in range(r):
                head=defect%width
                clocks=[n**(eps*(2*((h+defect)%7)/6-1))*np.exp(.3j*(h-defect))
                        for h in range(width)]
                weights.append(1/np.prod(clocks[:head]))
            aa=np.array(weights,complex)
            inv=np.conj(aa)/np.vdot(aa,aa).real
            assert np.linalg.norm(inv)<=n**((width-1)*eps)/np.sqrt(r)*(1+1e-12)
            boundary=complex(.7,-.4)
            charges=np.array([complex(.1*j,-.07*j) for j in range(r)],complex)
            pivot=2
            charges[pivot]=(boundary-sum(aa[j]*charges[j] for j in range(r) if j!=pivot))/aa[pivot]
            assert abs(aa@charges-boundary)<1e-11
            projector=np.eye(r)-np.outer(np.conj(aa),aa)/np.vdot(aa,aa).real
            assert np.linalg.norm(projector@projector-projector)<1e-12
            assert np.linalg.norm(projector,2)<=1+1e-12
            rows.append({"N":n,"width":width,"charges":r,
                         "forced_inverse_norm":float(np.linalg.norm(inv)),
                         "rational_charge_residual":float(abs(aa@charges-boundary))})
    return rows


def closed_source_counter():
    word=[1,-2,1,-2]
    initial=[2.,1.,1.]
    final=initial.copy()
    for letter in word:
        i=abs(letter)-1
        final[i],final[i+1]=final[i+1],final[i]
    jumps=np.array(initial)-np.array(final)
    assert np.count_nonzero(jumps)==2 and sum(jumps)==0
    fin=[(-1)**j*z for j,z in enumerate(initial)]
    fout=[(-1)**j*z for j,z in enumerate(final)]
    assert np.linalg.norm(product_lower([-1]*3,fin)-product_lower([-1]*3,fout))<1e-14
    h=based(initial)
    assert np.linalg.norm(h[0]@h[1]-h[1]@h[0])<1e-14
    ratio=initial[1]/initial[0]
    assert ratio!=1 and np.linalg.norm((h[1]+np.eye(2))-ratio*(h[0]+np.eye(2)))<1e-14
    frame=np.array([[2,1],[1,1]],complex) # determinant one, common to both.
    hh=[frame@u@np.linalg.inv(frame) for u in h]
    assert np.linalg.norm((hh[1]+np.eye(2))-ratio*(hh[0]+np.eye(2)))<1e-14
    packets=[]
    for r in range(9):
        a=sum(2.**j for j in range(r+1))
        b=sum(.5**j for j in range(r+1))
        assert a>0 and b>0
        packets.append({"R":r,"K_R_2":a,"K_R_half":b})
    return {"word":word,"initial_based_parameters":initial,"final_based_parameters":final,
            "two_closing_charges":jumps.tolist(),"invariant_crossing_ratio":ratio,
            "actual_endpoint_packets":packets,
            "scope":"All-endpoint action-zero defective graph, not an excess-volume knot or nonzero integrated period."}


def main():
    result={"status":"PASS","original_quantum_borel_checks":quantum_checks(),
            "exact_triangular_defect_weights":moment_jumps(),
            "stable_forced_charge_flow":forced_flow_checks(),
            "actual_both_sign_commuting_hurwitz":commuting_hurwitz(),
            "closed_two_defect_source":closed_source_counter()}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(f"PASS: {len(result['original_quantum_borel_checks'])} original signed Ward checks; "
          f"{len(result['exact_triangular_defect_weights'])} exact defect weights; "
          f"{len(result['actual_both_sign_commuting_hurwitz'])} resolved Hurwitz swaps; "
          f"{len(result['stable_forced_charge_flow'])} stable forced flows; "
          "closed two-charge source and common-frame obstruction")
    print(target)


if __name__=='__main__':main()
