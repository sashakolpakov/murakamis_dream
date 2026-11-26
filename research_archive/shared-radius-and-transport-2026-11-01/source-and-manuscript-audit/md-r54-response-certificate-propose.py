from pathlib import Path
import json,hashlib,importlib.util
import numpy as np
from fractions import Fraction as F
spec=importlib.util.spec_from_file_location('locate','/private/tmp/md-r54-boundary-response-locate.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
logs=json.loads(Path('/private/tmp/md-r54-boundary-response-locate.json').read_text())['logs']
weights={str(v):F(format(np.exp(logs[str(v)]),'.15g')) for v in m.I};weights.update({'0':F(1),'16':F(1)})
q=np.array([np.log(float(weights[str(v)])) for v in m.I]);_,g,H=m.evaluate(0.,q)
trial=-np.linalg.solve(H[1:,1:],H[1:,0]);hh={str(v):F(format(x,'.15g')) for v,x in zip(m.I,trial)};hh.update({'0':F(0),'16':F(1)})
source=m.repo/'experiments/actual_singleton_sector_obstruction_certificate.json'
out={'scope':'Rational witnesses proposed from a floating-point solve; verifier uses exact arithmetic only.','source_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'radius':[1,1000],'weights':{k:[v.numerator,v.denominator] for k,v in weights.items()},'potential_trial':{k:[v.numerator,v.denominator] for k,v in hh.items()}}
Path('/private/tmp/md-r54-response-certificate.json').write_text(json.dumps(out,indent=2)+'\n')
