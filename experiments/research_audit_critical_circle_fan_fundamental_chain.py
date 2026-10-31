"""Direct actual white/shaded cut-ball fans at the signed critical collar.

The imported engine supplies rational head-independent factor/differential
utilities only. Its quarantined complete-color mixed-source interpretation
is not used. This audit does not prove global source compatibility or topology.
"""
import sys,json,argparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import research_audit_critical_signed_green_word_regulator as a
s=a.s;I=s.I;b,t,v=a.b,a.t,a.v;x,c=a.x,a.c;sn,kk=a.sn,a.kk;clean=a.clean
D=(x+1)**2-4*x*sn*sn;L=D/x;aa=(1+x*(1-2*sn*sn))/x;O=aa-2*I*sn*kk

def triangle(q,T):
 co=1-2*sn*sn
 Nx=x*(1-x)+q*(1+x*co)+2*I*x*kk*T
 Nybar=(x-1)+q*(x+co)-2*I*kk*T
 Ox=1+x*co-2*I*x*sn*kk;Oy=x+co+2*I*sn*kk
 sh=(q+1)*(x*kk-I*(T+sn*(q+x)))/(kk*(q*(x+1)+2*x)+I*T*(x-1))
 return [(1,clean(Nx/((q+x)*Ox))),
         (1,clean(-(q+x)*Nybar/((q+1)*Nx))),
         (1,clean((q+1)*Oy/Nybar)),(-2,clean(sh))]

coordinate_checks=0
# Prove these identities before imposing the critical x(b,T,v): otherwise
# a harmless rational-coordinate substitution causes a very large CAS expansion.
xx,qq,tt=s.symbols('xx qq tt',real=True,nonzero=True)
co=1-2*sn**2
LL=((xx+1)**2-4*xx*sn**2)/xx
aa0=(1+xx*co)/xx
OO=aa0-2*I*sn*kk
ZZ=aa0+(1-xx)/qq+2*I*kk*tt/qq
px=qq*ZZ/(qq+xx);py=LL+qq*(ZZ-LL)/(qq+1)
nx=xx*(1-xx)+qq*(1+xx*co)+2*I*xx*kk*tt
ny=(xx-1)+qq*(xx+co)-2*I*kk*tt
simple=[nx/((qq+xx)*(1+xx*co-2*I*xx*sn*kk)),
 -(qq+xx)*ny/((qq+1)*nx),(qq+1)*(xx+co+2*I*sn*kk)/ny,
 (qq+1)*(xx*kk-I*(tt+sn*(qq+xx)))/(kk*(qq*(xx+1)+2*xx)+I*tt*(xx-1))]
for actual,expected in zip(simple,[px/OO,(py-ZZ)/(px-ZZ),(OO-LL)/(py-LL),(OO-px)/(py-px)]):
 assert clean(actual-expected)==0
 coordinate_checks+=1
print('actual contact-coordinate ratios PASS',coordinate_checks,flush=True)
atoms=triangle(b,t)+[(-n,z) for n,z in triangle(-c,-t)]
pin=(t-I*b*kk)/(t+I*b*kk);pout=(t-I*c*kk)/(t+I*c*kk)
nxb=x*(1-x)+b*(1+x*(2*kk*kk-1))+2*I*x*kk*t
nxc=x*(1-x)-c*(1+x*(2*kk*kk-1))-2*I*x*kk*t
forces=[(b,clean(pin),1),(clean(c),clean(pout),-1),(clean(x),clean(nxb/nxc),-1)]
print('generated8fans',flush=True)
size=a.differential_certificate(atoms,forces)
print('DIRECT FAN tensor PASS',size,flush=True)
vals=[];leading_checks=0
expected=[1,1,1,-2*(3+s.sqrt(6))/s.sqrt(6),1,1,1,3*(2+s.sqrt(6))/s.sqrt(6)]
for n,z in atoms:
 r=a.valuation_at_one(z)
 assert r['order']==0
 for key in ['uncancelled_leading_numerator','uncancelled_leading_denominator']:
  leading=s.sympify(r[key],locals={'b':b,'t':t,'T':t,'v':v})
  leading_anchor=s.simplify(leading.subs({b:1,t:s.sqrt(6)}))
  assert not leading_anchor.free_symbols and leading_anchor!=0
  leading_checks+=1
 anchor=s.simplify(s.sympify(r['leading'],locals={'b':b,'t':t,'T':t,'v':v}).subs({b:1,t:s.sqrt(6)}))
 assert not anchor.free_symbols
 assert s.simplify(anchor-expected[len(vals)])==0,(anchor,expected[len(vals)])
 r.update({'coefficient':n,'shape':str(z),'anchor':str(anchor)});vals.append(r)
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('research_critical_circle_fan_fundamental_chain_results.json'))
args=parser.parse_args()
args.output.write_text(json.dumps({'status':'PASS','actual_coordinate_ratios':coordinate_checks,
 'tensor_positions':size,'endpoint_values':len(vals),'uncancelled_anchor_units':leading_checks,
 'scope':'Exact actual cyclic white/shaded fan ratios, differential, and a nonvanishing real endpoint calibration; conditional global source/group/topology hypotheses are not numerically certified.',
 'atoms':vals},indent=2)+'\n');print('FAN calibration PASS',flush=True)
