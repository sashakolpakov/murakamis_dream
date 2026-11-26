from pathlib import Path
from fractions import Fraction
import hashlib
source=Path('/private/tmp/md-r54-boundary-response-locate.py').read_text()
exec(source[:source.index('\nweights={int')])
old=json.loads(Path('/private/tmp/md-r54-boundary-response-locate.json').read_text())
w0=np.array([old['logs'][str(v)] for v in I]);T=Fraction(17,5);z=np.log(float(T))
rr=root(lambda w:evaluate(z,w,False)[1][1:],w0,jac=lambda w:evaluate(z,w,False)[2][1:,1:],tol=1e-11)
f,g,H=evaluate(z,rr.x)
weights={str(v):Fraction(str(float(np.exp(w)))).limit_denominator(10**10) for v,w in zip(I,rr.x)}
weights[str(A)]=T;weights[str(C)]=Fraction(1)
cert={'scope':'Rational trial weights only; verify with exact outward arithmetic.','source_certificate_sha256':hashlib.sha256((repo/'experiments/actual_singleton_sector_obstruction_certificate.json').read_bytes()).hexdigest(),'tilt':[T.numerator,T.denominator],'weights':{v:[x.numerator,x.denominator] for v,x in weights.items()}}
Path('/private/tmp/md-r54-tilted-pressure-certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'residual':float(max(abs(g[1:]))),'weighted_pressure':float(f-z/2),'nu':float(g[0]),'T':str(T)},indent=2))
