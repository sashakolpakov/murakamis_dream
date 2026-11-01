#!/usr/bin/env python3
"""Local algebra in the bare-junction zero-circle argument.
These finite identities do not replace the ordered collar or global
representation proof. The script writes only its requested JSON output.
"""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
E,R,Q,P,a,b,c,Xm,Yn=s.symbols("E R Q P a b c Xm Yn",nonzero=True)
checks=[]
def check(name,value):
    result=s.factor(s.cancel(value))
    if result!=0:
        raise AssertionError((name,result))
    checks.append(name)
W=[
s.Matrix([[1,0],[0,E]]),
s.Matrix([[1,E-1],[0,E]]),
s.Matrix([[E-R,R*(1-E)],[E-1,1-E*R]]),
s.Matrix([[R,0],[1-E,E*R]])]
L=1/E
c2=(1/E-1)/(R-1);c3=(1/E-1)/R
N=[s.diag(L,1),s.Matrix([[L,1-L],[0,1]]),
s.Matrix([[c2+L,1-c2-L],[c2,1-c2]]),
s.Matrix([[L,0],[c3,1]])]
scales=[1/E,1/E,1/(E*(1-R)),1/(E*R)]
for j,(old,new,sc) in enumerate(zip(W,N,scales)):
 for i in range(4):check(f"native_white_{j}_{i}",(new-sc*old)[i])
disk=W[1].inv()*W[3]/R
check("disk_determinant_one",disk.det()-1)
check("disk_trace",s.trace(disk)-(2+(E+1/E-2)/R))
beta=(2*R-E-1/E)/(1-R)
gamma=(2-E-1/E-2*R)/R
check("edge_source",((E+1/E)+beta)*((E+1/E)+gamma)-(E+1/E-2)**2)
Qbeta=Q+1/Q
Rv=(Qbeta+E+1/E)/(Qbeta+2)
check("native_v_radius",Rv-(E+Q)*(E*Q+1)/(E*(Q+1)**2))
check("native_w_radius",(2-E-1/E)/(P+1/P+2)+P*(E-1)**2/(E*(P+1)**2))
k2=(a+b+c)/(a*b*c)
for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]:
 check(f"cubic_derivative_{x}",(k2+1/x**2)/(1-k2)-(x+y)*(x+z)/(x*(a*b*c-a-b-c)))
check("response_trace",2-4/Xm**2+2*(2/Xm**2-1))
fold=(4/Xm**2-4)*(4/Yn**2-4)-16
check("fold_metric",fold-16*(1-Xm**2-Yn**2)/(Xm**2*Yn**2))
if __name__=="__main__":
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument("--output",type=Path,default=Path(__file__).with_name("strict_tree_zero_circle_results.json"))
 args=parser.parse_args()
 result={"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"checks":len(checks),"all_exact_zero":True,"identities":checks,
 "scope":"Local rational identities only; full marked collar and representation assembly are proved in the accompanying note."}
 text=json.dumps(result,indent=2)+"\n"
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(text)
 print(text,end="")
