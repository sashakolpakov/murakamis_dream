"""Evaluate the proved acute formula at floating references; no certificate."""
from pathlib import Path
import json,hashlib
from phase_helpers import Candidate,phase,PI,THETA

HERE=Path(__file__).resolve().parent
old=json.loads((HERE/'results.json').read_text())
rows=[]
for row in old['cases']:
 ref=[complex(*p) for p in row['reference']];cc=Candidate((0,1),ref)
 a,b=cc.r(-2),cc.r(-1);x=row['left'];alpha,beta=cc.t(-2),cc.t(-1)
 val,gr=phase(a,b,alpha,beta)
 actual_gamma=(val+gr[0]*(a.real-a)+gr[1]*(x-b)).real
 real_defect=float(phase(a.real,x,alpha,beta)[0].real-actual_gamma)
 fee=float(max(0,a.imag*(gr[0].imag-alpha*PI*(.5-a.real)/2)+PI*max(-a.imag,0)/2))
 upper=real_defect+fee+THETA*float(cc.om(-1,x,0))/2
 entry=next(p['maximum_found'] for p in row['paths'] if p['mode']=='incoming' and p['depth']==5 and p['layer']==2)
 last=row['comparisons'][-1]
 rows.append(dict(name=row['name'],real_block_defect=real_defect,acute_fee=fee,
                  acute_formula_value=upper,
                  adjusted_formula_value=last['raw_defect_sum']+upper-entry-last['endpoint_occupation_share']))
out=dict(scope='The symbolic acute inequality is proved in the research note. These evaluations use floating references/phases and floating raw/entry values; no numerical upper bound, universal interface inequality, or finite-source conclusion is certified.',cases=rows)
(HERE/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
files=sorted(p for p in HERE.iterdir() if p.is_file() and p.name!='manifest.json')
(HERE/'manifest.json').write_text(json.dumps(dict(scope='Diagnostic provenance only; not a mathematical certificate.',files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')
print(json.dumps(out,indent=2))
