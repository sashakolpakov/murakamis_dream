#!/usr/bin/env python3
"""Exact primitive-cusp and endpoint-channel Hessian normalization."""
import json
from pathlib import Path
import sympy as s
from audit_actual_augmented_plat_endpoint_regulator import T,a,b,rat,mat,head

J,X,Y,Z,W=s.symbols('J X Y Z W')
P=lambda X,Z:T*(J-Z)**2*(X-Z)+(Z-1)**2*(T*Z-X*J)
R=Z*W*(J-1)**4*(T*Z-X*J)*(T*W-Y*J)/(J*X*Y*(J-Z)**2*(J-W)**2*(T-J)*(T*J-1))
sub={J:-1,X:T*(a-1)**2/(T*a*a+1),Y:T*(b-1)**2/(T*b*b+1),Z:(a-1)/(a+1),W:(b-1)/(b+1)}
p=P(X,Z);q=P(Y,W)
zj=rat((-s.diff(p,J)/s.diff(p,Z)).subs(sub))
wj=rat((-s.diff(q,J)/s.diff(q,W)).subs(sub))
R0=rat(R.subs(sub))
RJ=rat(s.diff(R,J).subs(sub)+s.diff(R,Z).subs(sub)*zj+s.diff(R,W).subs(sub)*wj)
bc=(2*T*a*b-T*a-T*b+a+b-2)/(2*(T+1)*(a-1)*(b-1))
assert R0==1 and rat(RJ-2*bc)==0
# Identically one on the ENTIRE rational endpoint chart, not only at one saddle.
assert all(s.diff(R0,x)==0 for x in (T,a,b))
rows=[]
U,V,zz,ww=sub[X],sub[Y],sub[Z],sub[W]
magnetic=lambda x,z:rat(-(1-x)*(T*z+x)/((x-z)*(T-x)))
D=rat(zz*ww*(T-U)*(T-V)/((T*zz+U)*(T*ww+V)))
for high in (False,True):
 G1,L1,_=head(V/T if high else V,magnetic(V,ww))
 G2,_,_=head(1/V if high else T/V,1)
 prod=mat(L1.inv()*G2*L1*G1);H=mat(prod+s.eye(2))
 out=head(U/T,D*magnetic(V,ww))[0] if high else head(U,1/(D*magnetic(U,zz)))[0]
 derived=rat(s.trace((H*G1-G1*H)*out)/32)
 assert rat(derived-bc)==0 and mat(H*H)==s.zeros(2)
 for epsilon in (0,1,-1):
  mu=mat(s.eye(2)+(s.Rational(epsilon,2)-bc)*H)
  longitude=mat(-prod)
  tau=rat(1/(bc-s.Rational(epsilon,2)))
  assert mat(longitude-s.eye(2)-tau*(mu-s.eye(2)))==s.zeros(2)
  assert rat(mu.det()-1)==0 and rat(longitude.det()-1)==0
  # dJ/dxi=-2pi i at J=-1. R_epsilon=R0*(-J)^epsilon.
  hessian=rat(-2*s.pi*s.I*(RJ-epsilon))
  assert rat(hessian+4*s.pi*s.I/tau)==0
  rows.append({'physical_chamber':'high' if high else 'low','epsilon':epsilon,
    'primitive_translation_ratio':str(tau),'Hessian':str(hessian),
    'marked_cusp_matrix_relation':True})
c=s.symbols('c',positive=True)
rectangle=[]
for epsilon in (0,1,-1):
 tau=2*s.I*c/(1-epsilon*s.I*c)
 hc=rat(-4*s.pi*s.I/tau)
 assert s.simplify(s.re(hc)+2*s.pi/c)==0
 # The stationary channel responds xi_chi=-tau/2; the color Hessian is pi i tau.
 xi_chi=rat(2*s.pi*s.I/hc)
 assert s.simplify(xi_chi+tau/2)==0
 color_hessian=rat(-2*s.pi*s.I*xi_chi)
 assert s.simplify(color_hessian-s.pi*s.I*tau)==0
 rectangle.append({'epsilon':epsilon,'tau':str(tau),'channel_Hessian':str(hc),
                   'color_Hessian':str(color_hessian)})
result={'status':'PASS','endpoint_R_is_identically_one':True,
 'all_endpoint_magnetic_derivatives_zero':True,'exact_implicit_root_normal':str(RJ),
 'normal_equals_twice_transport_coefficient':True,'physical_cases':rows,
 'primitive_rectangle_crosschecks':rectangle,
 'scope':'Local root-reduced phase, exact channel block and primitive cusp normalization. No magnetic quotient nondegeneracy or selected finite cycle.'}
Path(__file__).with_name('actual_augmented_plat_channel_hessian_results.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact root normal and endpoint tangential derivatives, 6 primitive cusp/channel cases, 3 signed rectangle/color-Hessian checks')
