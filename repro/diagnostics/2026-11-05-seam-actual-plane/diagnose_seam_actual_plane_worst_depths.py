"""A4/A5 only at the preserved positive actual-plane A3 witness; not a bound."""
from pathlib import Path
import hashlib, importlib.util, json, time
s=importlib.util.spec_from_file_location('common','/tmp/diagnose_seam_common_incoming.py')
common=importlib.util.module_from_spec(s);s.loader.exec_module(common)

def main():
 outpath=Path('/tmp/seam-actual-plane-worst-depths-diagnostic.json')
 assert not outpath.exists(),'refuse overwrite'
 start=time.time();inputpath=Path('/tmp/seam-actual-plane-common-a3-diagnostic.json')
 case=json.loads(inputpath.read_text())['maximum']
 ref,_,_=common.a4.a3.reference(tuple(case['word']));cc=common.a4.a3.Candidate(tuple(case['word']),ref)
 xm2,xm1,xp1,xp2,lam=case['variables_xm2_xm1_xp1_xp2_lambda'];sm2,sl,sr=case['selection_xm2_xm1_xp1']
 states=[(0,[xm2,xm1,case['virtual_left']],(sm2,sl,0)),(2,[case['virtual_right'],xp1,xp2],(0,sr,0))]
 values=[]
 for n,(i,state,sig) in enumerate(states):
  v3=float(cc.V(i,state,sig)[0]);v4=common.a4.A4(cc,i,state,sig);v5=common.A5(cc,i,state,sig,v4,18400+20*n)
  values.append(dict(layer=i,state=state,selection=sig,A3=v3,A4=v4,A5=v5));print('STATE',json.dumps(values[-1]),flush=True)
 comparisons=[]
 for h in (3,4,5):
  vo,vi=[v['A'+str(h)] if h==3 else v['A'+str(h)]['value'] for v in values]
  comparisons.append(dict(h=h,Aout=vo,Ain=vi,difference=vo-vi,actual_plane_comparison=vo-vi-case['endpoint_debit']+case['source_ceiling']+case['collar']-case['plane']))
 output=dict(scope='Only the single preserved worst positive A3 witness. A4/A5 enumerate all permitted free predecessor selections and estimate compact maxima from below. Differences of these estimates are neither upper bounds nor counterexamples to the true incoming-potential seam comparison.',input_sha256=hashlib.sha256(inputpath.read_bytes()).hexdigest(),witness=case,states=values,comparisons=comparisons,elapsed_seconds=time.time()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 outpath.write_text(json.dumps(output,indent=2)+'\n');print('COMPARISONS',json.dumps(comparisons),flush=True)
if __name__=='__main__':main()
