"""Bounded saved-witness seam test with exact AA halo repair differences."""
from pathlib import Path
import hashlib,importlib.util,itertools,json,time
import numpy as np

s=importlib.util.spec_from_file_location('closure','/tmp/diagnose_seam_three_step_closure.py')
cl=importlib.util.module_from_spec(s);s.loader.exec_module(cl)
ROOT=Path('/Users/sasha/volume-conjecture')
INPUT=ROOT/'repro/diagnostics/2026-11-05-seam-height-profiles/saved-case-evaluation.json'
OUT=Path('/tmp/seam-exact-halo-repairs-diagnostic.json')
THETA=.5

def evaluator(cc,c,selection2):
 xm2,xm1,xp1,xp2,lam=c['physical_variables'];sm2,sl,sr=c['selection_xm2_xm1_xp1']
 xiL=.1+(.02 if sl else .12)*lam;xiR=.1+(.02 if sr else .12)*lam;p0=cc.r(0).real
 outstate=[xm2,xm1,p0];instate=[p0,xp1,xp2]
 E=float(cl.exit3(cc,0,outstate,(sm2,sl,0))[0]);A=float(cc.V(2,instate,(0,sr,selection2))[0])
 psi=float(cc.om(-2,xm2,sm2)+cc.om(-1,xm1,sl)+cc.om(0,p0,0))
 endpoint=THETA*.5*float(cc.om(-1,xm1,sl)+cc.om(1,xp1,sr))
 # The old comparison data retain the actual plane and unchanged pair collar.
 original=json.loads((ROOT/'repro/diagnostics/2026-11-05-seam-actual-plane/seam-actual-plane-common-a3-diagnostic.json').read_text())
 old=next(r for r in original['cases'] if r['word']==c['word'] and r['selection_xm2_xm1_xp1']==c['selection_xm2_xm1_xp1'])
 assert old['variables_xm2_xm1_xp1_xp2_lambda']==c['physical_variables']
 pairdefect=c['height_resolved_source']+old['collar']-old['plane']
 base=-E-A-(1-THETA)*psi-endpoint+pairdefect
 def evaluate(v,details=False):
  v=np.asarray(v).reshape(-1,2);xm3,xp3=v.T;n=len(v)
  column=lambda z:np.full(n,z)
  exphys=np.column_stack((xm3,column(xm2),column(xm1),column(xiL)))
  exbase=exphys.copy();exbase[:,3]=p0
  enphys=np.column_stack((column(xiR),column(xp1),column(xp2),xp3))
  enbase=enphys.copy();enbase[:,0]=p0
  de=cc.w(-1,exphys,(0,sm2,sl,0),True)[0]-cc.w(-1,exbase,(0,sm2,sl,0),True)[0]
  di=cc.w(2,enphys,(0,sr,selection2,0),True)[0]-cc.w(2,enbase,(0,sr,selection2,0),True)[0]
  total=base+de+di
  if details:return dict(value=total,Delta_exit=de,Delta_entry=di,base_closure=np.full(n,-E-A),strengthened_closure=np.full(n,-E-A-(1-THETA)*psi),Psi_out=np.full(n,psi),endpoint_occupation_debit=np.full(n,endpoint),pair_source_defect=np.full(n,pairdefect),exit_E3=np.full(n,E),entry_A3=np.full(n,A))
  return total
 return evaluate,outstate,instate

def main():
 assert not OUT.exists(),'refuse overwrite'
 start=time.time();data=json.loads(INPUT.read_text());rows=[]
 for index,c in enumerate(data['cases']):
  ref,_,_=cl.a3.reference(tuple(c['word']));cc=cl.a3.Candidate(tuple(c['word']),ref)
  for selection2 in range(cc.t(2)+1):
   fn,ost,ist=evaluator(cc,c,selection2);halos=[cc.r(-3).real,cc.r(3).real]
   d={k:float(v[0]) for k,v in fn(halos,True).items()}
   row=dict(original_case=index,word=c['word'],selection_xm2_xm1_xp1=c['selection_xm2_xm1_xp1'],selection_xp2=selection2,physical_parameters=c['physical_variables'],inner_halos_xm3_xp3=halos,base_out_state=ost,base_in_state=ist,**d)
   rows.append(row);print('CASE',len(rows),json.dumps(row),flush=True)
 assert len(rows)==49
 result=dict(scope='Floating evaluation of a mathematically valid repaired three-step closure proxy on 29 saved physical witnesses, including both allowed q2 selection values (49 fixed evaluations). q±3 are reference-valued. Original AA physical-minus-repaired weights include their full complex planes and selected halfcorrections; the source uses actual height profiles, actual pair plane and fixed collar. This is neither a global bound nor a proof of failure of the actual potential criterion. Length-two shared-edge overlap and singleton runs are not represented by independent two-end corrections.',theta=THETA,input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=rows,maximum=max(rows,key=lambda r:r['value']),positive_count=sum(r['value']>0 for r in rows),optimization_jobs=0,elapsed_seconds=time.time()-start)
 OUT.write_text(json.dumps(result,indent=2)+'\n');print('MAX',json.dumps(result['maximum']),flush=True)
if __name__=='__main__':main()
