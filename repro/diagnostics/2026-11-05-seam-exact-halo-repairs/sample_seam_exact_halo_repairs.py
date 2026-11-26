"""Fixed one-dimensional halo grids at saved seam configurations; no optimizer."""
from pathlib import Path
import hashlib,importlib.util,json,time
import numpy as np
s=importlib.util.spec_from_file_location('repair','/tmp/diagnose_seam_exact_halo_repairs.py')
repair=importlib.util.module_from_spec(s);s.loader.exec_module(repair)
OUT=Path('/tmp/seam-exact-halo-repairs-grid-diagnostic.json')

def main():
 assert not OUT.exists(),'refuse overwrite'
 start=time.time();data=json.loads(repair.INPUT.read_text());rows=[]
 for index,c in enumerate(data['cases']):
  ref,_,_=repair.cl.a3.reference(tuple(c['word']));cc=repair.cl.a3.Candidate(tuple(c['word']),ref)
  for selection2 in range(cc.t(2)+1):
   fn,ost,ist=repair.evaluator(cc,c,selection2)
   left=np.unique(np.r_[np.linspace(.1,.5,101),.12,.22,.45,cc.r(-3).real])
   right=np.unique(np.r_[np.linspace(.1,.5,101),.12,.22,.45,cc.r(3).real])
   dl=fn(np.column_stack((left,np.full(len(left),cc.r(3).real))),True)['Delta_exit']
   dr=fn(np.column_stack((np.full(len(right),cc.r(-3).real),right)),True)['Delta_entry']
   halos=[float(left[int(dl.argmax())]),float(right[int(dr.argmax())])]
   d={k:float(v[0]) for k,v in fn(halos,True).items()}
   rows.append(dict(original_case=index,word=c['word'],selection_xm2_xm1_xp1=c['selection_xm2_xm1_xp1'],selection_xp2=selection2,physical_parameters=c['physical_variables'],maximizing_sampled_halos=halos,left_grid_count=len(left),right_grid_count=len(right),**d))
 result=dict(scope='Fixed 101-point grids plus profile cutpoints/reference values for each independent inner halo, at the same29 saved seam physical witnesses and49 selection configurations. The two correction functions separate, so their finite-grid maxima can be combined exactly. This remains a floating finite sample, not a continuous bound. No optimizer, outward cover, length-two shared-edge comparison, or singleton inference.',cases=rows,maximum=max(rows,key=lambda r:r['value']),positive_count=sum(r['value']>0 for r in rows),optimization_jobs=0,input_sha256=hashlib.sha256(repair.INPUT.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(Path('/tmp/diagnose_seam_exact_halo_repairs.py').read_bytes()).hexdigest(),elapsed_seconds=time.time()-start)
 OUT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result['maximum'],indent=2));print('positive',result['positive_count'],'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
