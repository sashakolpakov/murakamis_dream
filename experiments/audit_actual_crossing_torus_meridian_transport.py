"""Exact original Gauss matrices versus the signed crossing-torus maps."""
import argparse
import json
from pathlib import Path
import sympy as s

x,y,b,p=s.symbols('x y b p',nonzero=True)
A0=x+y;P0=x*y;f=lambda z:(z+x)*(z+y)

def gauss(X,S):
    K=-1/X;F=S*(1-X);E=(1/X-1)/S
    return s.Matrix([[K,E],[F*K,F*E+1/K]]),s.Matrix([[1,0],[-K*F,K]])

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_crossing_torus_meridian_transport_results.json'))
args=parser.parse_args()
counts={}
def scalar(expr,label):
    assert s.factor(expr)==0,(label,s.factor(expr))
    counts[label]=counts.get(label,0)+1

def matrix(expr,label):
    for entry in expr:scalar(entry,label)

# Envelope derivatives of the literal H_R/(bc)^(d/2) principal phase.
I,K,T,uu,vv,tt,gg=s.symbols('I K T u_head v_head total gamma')
LL=1-I-K-T
lx=gg+2*s.pi*s.I*tt
lb=gg+2*s.pi*s.I*(tt-vv)+s.pi*s.I
lc=gg+2*s.pi*s.I*(tt-uu)+s.pi*s.I
ly=gg
linear_phase=K*lx+I*lb+T*lc+LL*ly-(lb+lc)/2
for variable,expected in [(vv,-2*s.pi*s.I*(I-s.Rational(1,2))),
                          (uu,-2*s.pi*s.I*(T-s.Rational(1,2))),
                          (tt,-2*s.pi*s.I*LL),(gg,0)]:
    scalar(s.diff(linear_phase,variable)-expected,'full_physical_phase_derivatives')

A,L=gauss(-x/b,-p);G2,_=gauss(-b/y,1)
B=s.simplify(L.inv()*G2*L);P=s.simplify(B*A)
sigma=2+(p-1)**2*f(b)/(p*b*b)
scalar(s.trace(P)-sigma,'actual_trace')
scalar(P[0,0]-y/x,'actual_total_clock')
for M in (A,B):
    scalar(M.det()-1,'meridian_determinants')
    scalar(s.trace(M)+2,'meridian_traces')

for eps in (1,-1):
    if eps==1:
        c=(P0-f(b)/p)/b
        S1=b*p/(-b+p*x-x);S2=-(-b+p*y-y)/b
        rn=(P0-b*c)/f(c)
        expected1=A.inv()*B*A;expected2=A
    else:
        c=(P0-p*f(b))/b
        S1=-(b*p+p*x-x)/b;S2=b*p/(b*p+p*y-y)
        rn=f(c)/(P0-b*c)
        expected1=B;expected2=B*A*B.inv()
    scalar(x*expected1[0,0]-c,'literal_clock_advances')
    scalar(-S1/S2-rn,'literal_magnetic_advances')
    EI=(P0-b*c)/f(b);ET=(P0-b*c)/f(c)
    EL=-(b+y)*(c+y)/(P0-b*c)
    scalar(EI**(-eps)-p,'phase_input_momentum')
    scalar(ET**eps-rn,'phase_output_momentum')
    scalar(EL**eps-S2,'phase_common_scale')
    Anew,Lnew=gauss(-x/c,S1);G2new,_=gauss(-c/y,S2)
    Bnew=Lnew.inv()*G2new*Lnew
    matrix(Anew-expected1,'first_hurwitz_meridian_entries')
    matrix(Bnew-expected2,'second_hurwitz_meridian_entries')
    matrix(Bnew*Anew-P,'whole_product_entries')
    scalar(2+(rn-1)**2*f(c)/(rn*c*c)-sigma,'source_casimir_transport')

C=A.inv()*B*A
matrix(C.inv()*A*C-P.inv()*A*P,'two_positive_first_entries')
matrix(C-P.inv()*B*P,'two_positive_second_entries')
matrix((A*B-B*A).subs(p,1),'commuting_endpoint_entries')
# The opposite magnetic sign is not the actual Casimir dictionary.
Awrong,Lwrong=gauss(-x/b,p)
Bwrong=Lwrong.inv()*G2*Lwrong
assert s.factor(s.trace(Bwrong*Awrong)-sigma)!=0
counts['wrong_magnetic_sign_rejected']=1

out={'status':'PASS','exact_symbolic_counts':counts,'scope':
     'Original rational Gauss/Hurwitz identities on the recorded regular chart only; '
     'no finite-period selection or quantum growth estimate.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
