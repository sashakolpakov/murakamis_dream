#!/usr/bin/env python3
"""One bounded floating diagnostic, not an interval or source certificate.

25 prescribed inputs; no replacement after any rejected reference.
8 height values per admitted input; at most 40 Newton/KKT iterations.
The only endpoint refinement starts from an inherited original witness.
"""
import hashlib
import json
import platform
import time
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
import scipy
from scipy.special import spence

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "result.json"
ENDPOINT = "repro/results/research-mixed-open-word-critical-localization.json"
ENDPOINT_SHA = "ac2991d4cd5b7a78d202a237efebf98a9ad7ab77b6bacc4ab82568b8aa3cdad5"
DEPENDENCIES = [
    ENDPOINT,
    "repro/results/research-mixed-open-word-critical-localization-replay.json",
    "notes/research_mixed_open_word_critical_localization.md",
    "experiments/certify_mixed_open_word_critical_localization.py",
    "notes/research_mixed_selected_boundary_height_envelope.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_first_four_attached_height_bound.md",
    "repro/results/research-mixed-first-four-attached-height-bound.json",
]
P = np.pi
BOUNDS = {0: np.array([[.27,.49],[.15,.5],[.22,.45],[.22,.45]]),
          1: np.array([[.27,.49],[.125,.5],[.22,.45],[.22,.45]])}
DISKS = [(Q(".35"), Q("-.01"), Q(".09")),
         (Q(".30"), Q("-.052"), Q(".064"))]
INPUTS = [(0, x, y) for x in [".31", ".34", ".37", ".40"]
          for y in ["-.05", "-.025", "0", ".025", ".05"]]
INPUTS += [(1,x,y) for x,y in [(".28","-.065"),(".295","-.055"),
                              (".31","-.045"),(".325","-.035"),
                              (".34","-.025")]]
MAX_SECONDS = 120
MAX_REFERENCE_STEPS = 12
MAX_OPTIMIZER_STEPS = 40
HEIGHT_COUNT = 8


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pair(z):
    return [float(np.real(z)), float(np.imag(z))]


def jp(z):
    return np.log(2*np.sin(P*z))


def gp(z):
    return np.log(1-np.exp(-2j*P*z))


def cot(z):
    return 1/np.tan(P*z)


def primitive_g(z):
    return (spence(1-np.exp(-2j*P*z))-P*P/6)/(2j*P)


def primitive_j(z):
    return primitive_g(z)-.5j*P*(z-z*z)


def canonical_u(e):
    disc = 1-2*np.exp(2j*P*e)
    assert disc.real > 1
    u = np.arctan((1j+np.sqrt(disc))/2)/P
    assert 0 < u.real < .5 and 0 < (e-u).real < .5
    return u


def endpoint_equation(q, s):
    e,z,u = q
    return np.array([
        -jp(e-u)+jp(e+z)-jp(e)+1j*P*(u-z+e-.5),
        jp(e+z)+jp(z+s)-3*jp(z)+1j*P*(s-e+z-.5),
        2*np.log(np.cos(P*u))+np.log(np.sin(P*(e-u)))
        -3*np.log(np.sin(P*u))+1j*P*e])


def endpoint_jacobian(q):
    e,z,u = q
    eta, d = P*cot(e-u), P*cot(e+z)
    xi = P*(2*np.tan(P*u)+3*cot(u))
    return np.array([
        [-eta+d-P*cot(e)+1j*P, d-1j*P, eta+1j*P],
        [d-1j*P, d+P*cot(z+endpoint_jacobian.external)-3*P*cot(z)+1j*P, 0],
        [eta+1j*P, 0, -xi-eta]], dtype=complex)


def leaves(record, own, neighbor):
    domain = next(d for d in record["domains"] if
                  (d["epsilon"],d["neighbor_epsilon"]) == (own,neighbor))
    stack = [[(Q(-1),Q(1)),(Q(-1),Q(1))]]
    out = []
    for node_index,node in enumerate(domain["tree"]):
        box = stack.pop()
        if node[0] == "S":
            axis = node[1]; lo,hi=box[axis]; mid=(lo+hi)/2
            for interval in [(lo,mid),(mid,hi)]:
                child=list(box);child[axis]=interval;stack.append(child)
        elif node[0] == "L":
            out.append((node_index,box,node[1]))
        else:
            assert node[0] == "X"
    assert not stack and len(out)==domain["leaves"]
    return out


def inherited_witness(all_leaves, eps, xr, yi):
    cr,ci,r=DISKS[eps]
    p=((Q(xr)-cr)/r,(Q(yi)-ci)/r)
    assert p[0]**2+p[1]**2 <= 1
    for idx,box,w in all_leaves[eps]:
        if all(lo <= v <= hi for (lo,hi),v in zip(box,p)):
            return idx,box,w
    raise AssertionError("missing original containing leaf")


def refine_inherited(w,s):
    center=np.array([complex(float(Q(a)),float(Q(b))) for a,b in w["centers"]])
    radius=float(Q(w["radius"])); q=center.copy()
    endpoint_jacobian.external=s
    history=[]
    for iteration in range(MAX_REFERENCE_STEPS):
        f=endpoint_equation(q,s); residual=float(np.max(np.abs(f)))
        history.append(residual)
        if residual < 2e-12:
            break
        step=np.linalg.solve(endpoint_jacobian(q),f)
        for backtrack in range(12):
            trial=q-(2.0**(-backtrack))*step
            if np.max(np.abs(trial-center)) >= radius:
                continue
            if np.max(np.abs(endpoint_equation(trial,s))) < residual:
                q=trial;break
        else:
            return None,{"status":"refinement_stalled","residual_history":history}
    residual=float(np.max(np.abs(endpoint_equation(q,s))))
    info={"residual_history":history,"final_residual":residual,
          "maximum_distance_from_saved_center":float(np.max(np.abs(q-center))),
          "saved_radius":radius,"roots":[pair(z) for z in q]}
    if residual >= 2e-12 or np.max(np.abs(q-center)) >= radius:
        info["status"]="refinement_not_accepted";return None,info
    uc=canonical_u(q[0]);info["canonical_u_difference"]=float(abs(q[2]-uc))
    if abs(q[2]-uc)>2e-11:
        info["status"]="canonical_branch_mismatch";return None,info
    info["status"]="small_residual_inside_inherited_witness"
    return q,info


def in_disk(z, eps):
    center=(.35-.01j) if eps==0 else (.30-.052j)
    radius=.083 if eps==0 else .060
    return abs(z-center)<radius


def ordinary(z, eps):
    lo,hi=(-.065,.068) if eps==0 else (-.102,-.001)
    return in_disk(z,eps) and lo<z.imag<hi


def attached(z, eps):
    xr,xi,yr,yi=(.278,.391,-.072,.021) if eps==0 else (.246,.350,-.108,-.020)
    return in_disk(z,eps) and xr<z.real<xi and yr<z.imag<yi


def ordinary_equations(s,b,z,c,eps):
    return np.array([
        jp(s+b)+jp(s+z)-(2+eps)*jp(s)+1j*P*(z-b+eps*(s-.5)),
        jp(s+b)+jp(b+c)-(2+eps)*jp(b)+1j*P*(c-s+eps*(b-.5))])


def construct_reference(q,s,eps):
    e,z,u=q; S=np.exp(-2j*P*s);Z=np.exp(-2j*P*z)
    B=(1-Z*(1-S)**(2+eps)/(1-Z*S))/S
    info={"ordinary_B":pair(B)}; reasons=[]
    if not np.isfinite(B) or B.imag>=0 or abs(B)<1e-12:
        return None,{**info,"filter_rejections":["B_not_in_original_lower_half_plane"]}
    b=-np.log(B)/(2j*P)
    Wnext=B+(1-B)**(2+eps)/(1-S*B)
    info.update({"b":pair(b),"next_reciprocal_exponential":pair(Wnext)})
    if not np.isfinite(Wnext) or Wnext.imag<=0 or abs(Wnext)<1e-12:
        return None,{**info,"filter_rejections":["next_exponential_wrong_half_plane"]}
    c=np.log(Wnext)/(2j*P)
    info["next_external"]=pair(c)
    if not ordinary(s,eps):reasons.append("s_not_in_typed_ordinary_domain")
    if not ordinary(b,eps):reasons.append("b_not_in_typed_ordinary_domain")
    if not attached(z,1):reasons.append("first_output_not_in_attached_four_domain")
    if z.imag <= (-.07 if eps==0 else -.078):reasons.append("first_height_below_coupled_floor")
    if eps==1 and s.real<=.259:reasons.append("oriented_next_four_floor")
    memberships=[name for name,pred in [("O3",ordinary(c,0)),("A3",attached(c,0)),
                                       ("O4",ordinary(c,1)),("A4",attached(c,1))] if pred]
    info["next_external_domain_memberships"]=memberships
    if not memberships:reasons.append("next_external_outside_typed_union")
    if not all(0<v.real<1 for v in [s,b,z,c,s+b,s+z,b+c]):
        reasons.append("ordinary_original_sine_strip")
    residual=float(np.max(np.abs(ordinary_equations(s,b,z,c,eps))))
    info["ordinary_zero_lift_residual"]=residual
    if residual>2e-10:reasons.append("ordinary_nonzero_log_lift_or_large_residual")
    # Independent rational endpoint parametrization; no solve or branch choice.
    U=np.exp(2j*P*u);D=5*U*U-2*U+1
    Er=(U+1)**2/D
    Zr=(D*D+4*(1-U)**4)/(D*(U+1)**2)
    Ar=-4*(1-U)**4/D**2
    Sr=Ar/(Zr*Ar+(1-Zr)**3)
    check=max(abs(Er-np.exp(-2j*P*e)),abs(Zr-Z),abs(Sr-S))
    info["rational_endpoint_consistency_residual"]=float(check)
    if check>2e-10:reasons.append("rational_endpoint_inconsistency")
    info["filter_rejections"]=reasons
    if reasons:return None,info
    pb=gp(s+b)-(1+eps/2)*gp(b)
    return {"eps":eps,"star":np.array([e,s,z,b]),"c_next":c,"pb":pb},info


def phase_gradient_hessian(x,k,ref):
    eps=ref["eps"];height=ref["star"].imag.copy();height[2]=k
    e,s,z,b=x+1j*height;u=canonical_u(e)
    cap=-2*primitive_j(.5-u)-3*primitive_j(u)-primitive_j(e-u)+1j*P*e*u
    value=(cap+primitive_g(e+z)+primitive_g(s+z)+primitive_g(s+b)
           -(2+eps)*primitive_g(s)-3*primitive_g(z)-(1+eps/2)*primitive_g(b)
           -primitive_g(e)-.5j*P*(e-e*e)+2j*P*z*s)
    value=float(value.real-ref["pb"].real*(x[3]-ref["star"][3].real))
    Sp=-jp(e-u)+1j*P*u
    gradient=np.array([Sp+gp(e+z)-gp(e)-.5j*P+1j*P*e,
                       gp(s+z)+gp(s+b)-(2+eps)*gp(s)+2j*P*z,
                       gp(e+z)+gp(s+z)-3*gp(z)+2j*P*s,
                       gp(s+b)-(1+eps/2)*gp(b)-ref["pb"]])
    eta=cot(e-u);xi=2*np.tan(P*u)+3*cot(u)
    sigma=eta-(eta+1j)**2/(xi+eta)
    pe,ps,pz,pb=map(cot,[e,s,z,b]);d,f,g0=map(cot,[e+z,s+z,s+b])
    H=np.diag([sigma+pe-d-1j,(2+eps)*ps-f-g0-1j*eps,
               3*pz-d-f-1j,(1+eps/2)*pb-g0-.5j*eps])
    H[0,2]=H[2,0]=-d+1j;H[1,2]=H[2,1]=-f-1j;H[1,3]=H[3,1]=-g0+1j
    return value,gradient.real,P*H


def metric(H):
    h=H/P;A=h.real;q=h.imag[:,2]
    eig=np.linalg.eigvalsh(A)
    if eig[0]<=0:return {"positive_real_hessian":False,"eigenvalues_over_pi":eig.tolist()}
    exact=float(A[2,2]+q@np.linalg.solve(A,q))
    E=A[0,0];B=A[3,3];T=A[1,1]-A[1,3]**2/B
    be=A[0,2];bs=A[1,2];a=A[2,2]
    D=a-be*be/E-bs*bs/T;Qnum=q[2]-be*q[0]/E-bs*q[1]/T
    scalar=float(a+q[0]**2/E+q[1]**2/T+Qnum**2/D)
    assert abs(scalar-exact)<2e-10
    return {"positive_real_hessian":True,"eigenvalues_over_pi":eig.tolist(),
            "K_over_pi":exact,"scalar_formula_difference":scalar-exact,
            "pivots":[float(E),float(B),float(T),float(D)],
            "Q_residual":float(Qnum)}


def optimize(start,k,ref,deadline):
    bounds=BOUNDS[ref["eps"]];lo,hi=bounds.T;x=np.clip(start.copy(),lo,hi)
    history=[];evaluations=0
    for iteration in range(MAX_OPTIMIZER_STEPS):
        if time.monotonic()>deadline:raise TimeoutError("fixed120-second budget")
        value,g,H=phase_gradient_hessian(x,k,ref);evaluations+=1
        residual=x-np.clip(x+g,lo,hi);norm=float(np.max(np.abs(residual)))
        history.append({"iteration":iteration,"projected_gradient":norm,"value":value})
        if norm<2e-10:break
        active=((x<=lo+2e-12)&(g<=0))|((x>=hi-2e-12)&(g>=0))
        free=~active;step=np.zeros(4)
        A=H.real
        if np.min(np.linalg.eigvalsh(A[np.ix_(free,free)]))>1e-9:
            step[free]=np.linalg.solve(A[np.ix_(free,free)],g[free])
        else:
            step[free]=g[free]/max(1.,float(np.linalg.norm(A,2)))
        if np.dot(g,step)<=0:step=g/max(1.,float(np.linalg.norm(A,2)))
        for backtrack in range(20):
            trial=np.clip(x+2.0**(-backtrack)*step,lo,hi);change=trial-x
            if np.max(np.abs(change))<1e-15:continue
            trial_value,_,_=phase_gradient_hessian(trial,k,ref);evaluations+=1
            if trial_value>=value+1e-4*np.dot(g,change)-2e-14:
                x=trial;break
        else:
            return x,{"status":"line_search_stalled","history":history,
                      "evaluations":evaluations}
    value,g,H=phase_gradient_hessian(x,k,ref);evaluations+=1
    norm=float(np.max(np.abs(x-np.clip(x+g,lo,hi))))
    active=[i for i in range(4) if min(x[i]-lo[i],hi[i]-x[i])<1e-9]
    info={"status":"KKT_candidate" if norm<2e-10 else "iteration_cap",
          "x":x.tolist(),"gradient":g.tolist(),"projected_gradient":norm,
          "active_coordinates":active,"value":value,"history":history,
          "evaluations":evaluations,**metric(H)}
    return x,info


def main():
    assert not OUTPUT.exists(),"preserve the sole run; output already exists"
    start=time.monotonic();deadline=start+MAX_SECONDS
    dependencies={p:digest(ROOT/p) for p in DEPENDENCIES}
    assert dependencies[ENDPOINT]==ENDPOINT_SHA
    record=json.loads((ROOT/ENDPOINT).read_text());assert record["status"]=="passed"
    replay=json.loads((ROOT/DEPENDENCIES[1]).read_text())
    assert replay["status"]=="passed" and replay["input_sha256"]==ENDPOINT_SHA
    all_leaves={eps:leaves(record,1,eps) for eps in [0,1]}
    out={"status":"running","scope":"Floating necessary-feasible references and continued KKT points only; not a certificate or word-realizability claim",
         "budget":{"references":25,"heights_per_reference":HEIGHT_COUNT,
                   "reference_newton_steps":MAX_REFERENCE_STEPS,
                   "optimizer_iterations":MAX_OPTIMIZER_STEPS,
                   "seconds":MAX_SECONDS,"no_replacement_references":True},
         "script_sha256":digest(__file__),"dependencies_sha256":dependencies,
         "versions":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__},
         "references":[]}
    try:
        for number,(eps,xr,yi) in enumerate(INPUTS):
            item={"number":number,"next_epsilon":eps,"input_rationals":[xr,yi],"heights":[]}
            out["references"].append(item)
            idx,box,w=inherited_witness(all_leaves,eps,xr,yi)
            item.update({"endpoint_tree_node":idx,"endpoint_parameter_box":[[str(a),str(b)] for a,b in box],
                         "original_witness_sha256":hashlib.sha256(json.dumps(w,sort_keys=True).encode()).hexdigest()})
            s=complex(float(Q(xr)),float(Q(yi)))
            q,refinfo=refine_inherited(w,s);item["endpoint_refinement"]=refinfo
            if q is None:item["status"]="endpoint_refinement_rejected";continue
            ref,filters=construct_reference(q,s,eps);item["filters"]=filters
            if ref is None:item["status"]="necessary_filter_rejected";continue
            x=ref["star"].real.copy();c=ref["star"][2].imag
            baseline,grad,_=phase_gradient_hessian(x,c,ref)
            item.update({"status":"necessary_feasible_not_word_realized","reference":[pair(z) for z in ref["star"]],
                         "cut_p_b":pair(ref["pb"]),"baseline":baseline,
                         "baseline_real_gradient":grad.tolist()})
            assert np.max(np.abs(grad))<2e-10
            height_nodes=np.r_[np.linspace(c,0.0,HEIGHT_COUNT-1),.01]
            for step,k in enumerate(height_nodes):
                x,info=optimize(x,float(k),ref,deadline)
                info.update({"step":step,"height":float(k)})
                if "value" in info:
                    info["base_excess_over_reference"]=info["value"]-baseline
                    info["factorial_excess_over_reference"]=info["value"]-baseline-2*P*k
                item["heights"].append(info)
                if info["status"]!="KKT_candidate":
                    item["status"]="optimizer_incomplete";break
        out["status"]="bounded_diagnostic_complete"
    except Exception as error:
        out["status"]="bounded_diagnostic_stopped"
        out["error"]={"type":type(error).__name__,"message":str(error)}
    out["elapsed_seconds"]=time.monotonic()-start
    out["dependencies_unchanged"]={p:digest(ROOT/p)==h for p,h in dependencies.items()}
    assert all(out["dependencies_unchanged"].values())
    out["script_unchanged"]=digest(__file__)==out["script_sha256"]
    assert out["script_unchanged"]
    good=[(r,h) for r in out["references"] for h in r["heights"] if h.get("status")=="KKT_candidate"]
    out["summary"]={"references_processed":len(out["references"]),"necessary_feasible":sum(bool(r["heights"]) for r in out["references"]),
                    "KKT_points":len(good),"positive_hessian_points":sum(h.get("positive_real_hessian",False) for r,h in good)}
    for eps in [0,1]:
        candidates=[(r,h) for r,h in good if r["next_epsilon"]==eps and "K_over_pi" in h]
        if candidates:
            r,h=max(candidates,key=lambda rh:rh[1]["K_over_pi"])
            out["summary"][f"next_{3+eps}_maximum"]={"reference":r["number"],"step":h["step"],"K_over_pi":h["K_over_pi"]}
    temp=OUTPUT.with_suffix(".tmp");temp.write_text(json.dumps(out,indent=2)+"\n");temp.replace(OUTPUT)
    print(json.dumps({"status":out["status"],"summary":out["summary"],"elapsed_seconds":out["elapsed_seconds"]},indent=2))


if __name__=="__main__":main()
