from pathlib import Path
from fractions import Fraction as F
import sys,json,inspect
sys.path.insert(0,str(Path.cwd()/'experiments'))
import certify_mixed_optimized_half_row_support as new
from flint import ctx,arb,acb
ctx.prec=256
fixed=new.fixed;old=new.old
fixed.PI=old.PI=old.base.PI=arb.pi();fixed.II=old.II=old.base.I=acb(0,1)

def table(path):
 r=json.loads(Path(path).read_text());todo=[('',[(F(0),F(1))]*3,0)];leaves={}
 for n in r['incomplete_domain']['tree']:
  addr,box,d=todo.pop()
  if n[0]=='S':
   ax=n[1];lo,hi=box[ax];mid=(lo+hi)/2;l,rr=list(box),list(box);l[ax]=(lo,mid);rr[ax]=(mid,hi)
   todo.extend([(addr+'0',l,d+1),(addr+'1',rr,d+1)])
  else:leaves[addr]=(box,d,n[1])
 return leaves
A=table('repro/diagnostics/2026-11-05-half-row-support-pilot/result-partial.json')
B=table('repro/diagnostics/2026-11-05-optimized-half-row-support-pilot/result-partial.json')
# Instrument only the returned diagnostic data in memory; mathematical operations unchanged.
s=inspect.getsource(new.check_optimized).replace('meanvalue=str(meanvalue), upper_bound=', 'meanvalue=str(meanvalue), parameter_costs=[str(abs(gradient[j])*halfwidth[j]) for j in range(3)], upper_bound=')
ns=dict(vars(new));exec(s,ns);optimized=ns['check_optimized']
s=inspect.getsource(fixed.check_source).replace('midpoint=str(midpoint),meanvalue=str(meanvalue),','midpoint=str(midpoint),meanvalue=str(meanvalue), parameter_costs=[str(abs(parameter_derivative[j])*halfwidth[j]) for j in range(3)],')
ns=dict(vars(fixed));exec(s,ns);original=ns['check_source']
chosen=[('old_only_parent','11111111100001010',A),('new_only_parent','11111111101011101',B),('common',max(set(A)&set(B)),B)]
result=[]
for label,address,records in chosen:
 box,depth,data=records[address]
 pp,dp=fixed.parameters(box,(1,1),0);p0,_=fixed.parameters([((lo+hi)/2,)*2 for lo,hi in box],(1,1),0)
 cert=old.root_box(data['witness'],pp,p0,0);assert cert is not None
 components=old.components(data['witness'],pp,p0,0)
 entry=dict(label=label,address=address,depth=depth,box=[[str(x)for x in pair]for pair in box], nonlinearity_radii=data['witness']['radii'], affine_root_halfwidths=[[str(z.real.rad()),str(z.imag.rad())]for z in components[4]], root_halfwidths=[[str(z.real.rad()),str(z.imag.rad())]for z in cert['root']],parameters=[str(z)for z in pp])
 for name,fn in [('fixed',original),('optimized',optimized)]:
  rows,detail=fn(box,pp,p0,dp,cert,(1,1),0,data['targets'])
  entry[name]=dict(passes=rows is not None,**detail)
 result.append(entry)
p=Path(__file__).with_name('result.json');p.write_text(json.dumps(result,indent=2)+'\n')
for r in result:
 print(r['label'],r['address'],'depth',r['depth'],'nonlinear',r['nonlinearity_radii'],'root_halfwidths',r['root_halfwidths'])
 for name in ['fixed','optimized']:
  z=r[name];print(name,z['passes'])
  for row in z['rows']:
   print(' side',row['side'],'midpoint',float(arb(row['midpoint']).mid()),'costs',[float(arb(x).upper())for x in row['parameter_costs']],'upper',row['upper_bound'])
   if 'optimizer_intervals'in row:print(' optimizer',row['optimizer_intervals'],'mid gains',row['midpoint_gains'])
print('saved',p)
