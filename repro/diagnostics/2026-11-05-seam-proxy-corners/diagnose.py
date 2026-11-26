#!/usr/bin/env python3
"""Small fixed endpoint-corner test of the exact repaired seam upper proxy."""
from pathlib import Path
import hashlib,importlib.util,itertools,json,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
HELPERS=HERE.parent/'2026-11-05-seam-attenuation-vertices'
sys.path.insert(0,str(HELPERS))
s=importlib.util.spec_from_file_location('vertices',HELPERS/'diagnose.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)

def main():
 output=HERE/'results.json';assert not output.exists()
 begin=time.time();data=json.loads(v.INPUTS['witnesses'].read_text());profiles=json.loads(v.INPUTS['profiles'].read_text())['profiles']
 refs={tuple(r['word']):np.array([complex(*z) for z in r['reference']]) for r in data['references']}
 rows=[]
 for word,ref in refs.items():
  cc=v.Candidate(word,ref)
  for bits in itertools.product(*[range(cc.t(j)+1)for j in(-2,-1,1,2)]):
   sm2,sl,sr,s2=bits
   for left,right in itertools.product((.1,.22,.45,.5),repeat=2):
    witness=dict(variables_xm2_xm1_xp1_xp2_lambda=[cc.r(-2).real,left,right,cc.r(2).real,0.],selection_xm2_xm1_xp1=[sm2,sl,sr])
    halos=[cc.r(-3).real,cc.r(3).real]
    fn,ml,mr=v.evaluator(cc,witness,s2,halos,profiles)
    vals=fn(sorted(set([0.,1.,ml,mr])))
    rows.append(dict(word=word,selection=bits,physical_A_reals=witness['variables_xm2_xm1_xp1_xp2_lambda'][:4],inner_halos=halos,values=vals,worst=max(vals,key=lambda x:x['value'])))
 assert len(rows)==784
 worst=max(rows,key=lambda r:r['worst']['value'])
 result=dict(scope='Fixed broad endpoint corners only: each adjacent endpoint is in{.1,.22,.45,.5}; the two inner A coordinates and next halos are reference-valued; all allowed four A selections for seven actual correlated reference words. Only candidate seam attenuations are evaluated. No optimizer, full real-coordinate coverage, or source/asymptotic counterexample.',cases=rows,fixed_cases=len(rows),phase_values=sum(len(r['values'])for r in rows),positive_fixed_cases=sum(r['worst']['value']>0 for r in rows),maximum=worst,elapsed_seconds=time.time()-begin,input_sha256={str(p.relative_to(ROOT)):v.sha(p)for p in(v.INPUTS['witnesses'],v.INPUTS['profiles'],HELPERS/'diagnose.py',HELPERS/'phase_helpers.py')},script_sha256=v.sha(Path(__file__)))
 output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(maximum=worst,positive=result['positive_fixed_cases'],values=result['phase_values'],seconds=result['elapsed_seconds']),indent=2))
if __name__=='__main__':main()
