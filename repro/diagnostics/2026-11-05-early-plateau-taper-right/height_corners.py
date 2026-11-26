"""Same fixed references/grid, with U-height corners independently enlarged."""
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("fixed_pair_probe",HERE/"probe.py")
probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(probe)
old=probe.old

def main():
 start=time.monotonic();rows=[]
 for word in itertools.product((0,1),repeat=4):
  ref,residual=old.reference(word);cc=old.Candidate(word,ref)
  for orientation in("EPUR","RUPE"):
   p,u,rawedge,forward=(1,2,3,True)if orientation=="EPUR"else(2,1,1,False)
   credit=(5.5 if forward else 7.55)*ref[p].imag**2
   reals=np.unique(np.r_[.22,.27,.30,.33,.39,.45,ref[p].real])
   reals=reals[(reals>=.22)&(reals<=.45)]
   points=np.array(list(itertools.product(reals,(.45,.475,.5),(0.,1/6),(0.,1.))))
   x,t,ell,hu=points.T
   for sp,su in itertools.product(range(word[p]+1),range(word[u]+1)):
    zp=x+1j*(.014*6*ell if sp else ref[p].imag*ell)
    zu=t+1j*(.014 if su else ref[u].imag)*hu
    a,b=(zp,zu)if forward else(zu,zp)
    f,grad=cc.base[2];plane=f+grad[0]*(a-ref[1])+grad[1]*(b-ref[2])
    coh=(old.phase(a,b,word[1],word[2])[0]-plane).real
    coh+=.5*sp*np.maximum(old.g(zp).real,-2*old.PI*zp.imag)
    coh+=.5*su*np.maximum(old.g(zu).real,-2*old.PI*zu.imag)
    raw,row=old.raw_endpoint(cc,rawedge,zu,su,forward)
    val=coh+raw-credit;k=int(val.argmax())
    rows.append(dict(word=list(word),orientation=orientation,selected_P=sp,selected_U=su,
      maximum_found=float(val[k]),witness=dict(P_real=float(x[k]),U_real=float(t[k]),
      early_fraction=float(ell[k]),U_height_fraction=float(hu[k]),
      P_height=float(zp[k].imag),U_height=float(zu[k].imag),
      coherent_PU_defect=float(coh[k]),raw_UR_defect=float(raw[k]),credit=float(credit),
      maximizing_row=float(row[k])),grid_points=len(points),reference_residual=residual))
 result=dict(scope="Fixed-grid diagnostic of the sufficient independent-height-corner enlargement, not the literal quadratic taper. Same16 actual-reference proposals,72 states, no optimizer/outward cover. A positive value would only reject this relaxation; a negative value is not a uniform bound.",
   cases=rows,total_grid_evaluations=sum(r["grid_points"]for r in rows),
   maximum=max(rows,key=lambda r:r["maximum_found"]),elapsed_seconds=time.monotonic()-start,
   dependencies={str(p.relative_to(probe.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
     for p in (Path(__file__),HERE/"probe.py",probe.HELPER,
               HERE.parent/"2026-11-05-right-short-connectors/phase_helpers.py")})
 (HERE/"height-corners.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps(result["maximum"]),flush=True)
if __name__=="__main__":main()
