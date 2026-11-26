"""Exact selected minimum-neighbor flow and an outward negative derivative."""
from flint import arb,acb,ctx
from fractions import Fraction as F
import numpy as np,json,argparse,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PROOF=ROOT/'notes/research_mixed_selected_minimum_flow_obstruction.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
pa=argparse.ArgumentParser(description=__doc__);pa.add_argument('--precision',type=int,default=256);pa.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-selected-minimum-flow-obstruction.json');args=pa.parse_args();assert args.precision>=128;ctx.prec=args.precision;P=arb.pi();I=acb(0,1)
proof_hash=sha(PROOF);script_hash=sha(__file__);deps={}
for pp,ss,rr in (
 ('notes/research_mixed_minimum_neighbor_contour.md','experiments/check_mixed_minimum_neighbor_contour.py','repro/results/research-mixed-minimum-neighbor-contour.json'),
 ('notes/research_mixed_global_cotangent_roots.md','experiments/check_mixed_global_cotangent_roots.py','repro/results/research-mixed-global-cotangent-roots.json'),
 ('notes/research_mixed_transition_pair_source.md','experiments/certify_mixed_transition_pair_source.py','repro/results/research-mixed-transition-pair-source.json')):
 for path in(pp,ss,rr):deps[path]=sha(ROOT/path)
 rec=json.loads((ROOT/rr).read_text());assert rec['status']=='passed'and rec['proof_sha256']==deps[pp]and rec['script_sha256']==deps[ss]
 for field in('dependencies','dependencies_sha256'):
  assert all(sha(ROOT/path)==dig for path,dig in rec.get(field,{}).items())

def ar(x):x=F(x);return arb(x.numerator)/x.denominator
def cot(z):return(P*z).cot()
def gp(z):return(1-(-2*P*I*z).exp()).log()
def g(z):return((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def fp(s,a,b):return gp(s+a)+gp(s+b)-3*gp(s)+2*P*I*a
def hh(s,a,b):return P*(cot(s+a)+cot(s+b)-3*cot(s))+P*I
xs=['9/20','197/1000','49/250','197/1000','23/100','7/20','7/20'];xx=list(map(F,xs));rho=[max(F(0),min(F(1),(v-F(1,10))/F(3,25)))for v in xx];hs=[F(7,500)*min(rho[(j-1)%7],rho[j],rho[(j+1)%7])for j in range(7)];zz=[acb(ar(xx[j]),ar(hs[j]))for j in range(7)]
assert hs==list(map(F,['679/60000','7/625','7/625','7/625','679/60000','7/500','7/500']))
assert xx.index(min(xx))==2 and sorted(xx)[1]-xx[2]==F(1,1000)
assert F(7,500)/F(3,25)==F(7,60)
# The exact active minima show which heights change under the unique-minimum lift.
active=[]
for j in range(7):
 inds=((j-1)%7,j,(j+1)%7);mn=min(rho[k]for k in inds)
 if 2 in inds and rho[2]==mn:active.append(j)
assert active==[1,2,3]
partials=[];checks=[]
for j in range(4):
 a,b=zz[j],zz[j+1];af,bf=[complex(float(v.real),float(v.imag))for v in(a,b)];p,q=1/np.tan(np.pi*af),1/np.tan(np.pi*bf)
 roots=np.roots([1,p+q+1j,p*q+1j*(p+q),1j*p*q-2j*(p-1j)*(q+1j)]);c=[v for v in roots if v.real>0 and abs(v.imag)<1];assert len(c)==1
 sf=np.log((c[0]+1j)/(c[0]-1j))/(2j*np.pi);s0=acb(ar(str(sf.real)),ar(str(sf.imag)));rad=ar('1e-12');s=s0+acb(arb(0,rad),arb(0,rad));Y=1/hh(s0,a,b)
 margin=rad-abs(Y*fp(s0,a,b))-abs(1-Y*hh(s,a,b))*rad;assert margin>0
 assert 0<s.real<ar('1/2')and 0<(s+a).real<1 and 0<(s+b).real<1
 sc=cot(s);assert sc.real>0 and abs(sc.imag)<1 and abs(fp(s,a,b).imag)<P
 partials.append((gp(s+a)+2*P*I*s-ar('3/2')*gp(a),gp(s+b)-ar('3/2')*gp(b)))
 checks.append({'edge':j,'selfmap_margin':str(margin),'root':str(s)})
G=[partials[j-1][1]+partials[j][0]+2*P*I for j in(1,2,3)]
D=G[1].real-ar('7/60')*sum((v.imag for v in G),arb(0));assert D<ar('-4/5')
branch=[]
for j in(1,2,3):
 margin=-g(zz[j]).real-2*P*zz[j].imag;assert margin>ar('1/20');branch.append(str(margin))
universal=[]
for xr in('1/10','11/50'):
 z=acb(ar(xr),ar('7/500'));v=-g(z).real-2*P*z.imag-ar('3/40');assert v>0;universal.append({'x':xr,'margin':str(v)})
assert sha(PROOF)==proof_hash and sha(__file__)==script_hash and all(sha(ROOT/path)==dig for path,dig in deps.items())
out={'status':'passed','precision_bits':args.precision,'exact_graph_checks':4,'universal_branch_bounds':universal,'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies_sha256':deps,'coordinates':xs,'heights':[str(v)for v in hs],'minimum_coordinate':2,'moving_real_coordinates':[2],'moving_height_coordinates':[1,2,3],'height_derivative':'7/60','derivative':str(D),'strict_frequency_branch_margins':branch,'root_checks':checks,'scope':'Failure of nondecreasing selected minimum-level flow at a genuine seven-cycle configuration. No failure of a selected-phase bound or finite-sum asymptotic.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS 4 exact graph checks, 4 root self-maps, 3 local and 2 universal branch margins; derivative',D)
