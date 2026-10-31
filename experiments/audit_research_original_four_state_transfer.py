"""Exact finite source checks; no asymptotic or physical-matrix claim."""
from pathlib import Path
import argparse
import json
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local


def audit():
    counts={'levels':0,'spectral_values':0,'four_state_values':0,'exact_scalar_modes':0}
    for N in range(3,13):
     loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d;m=N//2;M=m-1
     nodes=[(q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
     ss=lambda r:(pow(q,r,p)-pow(q,-r,p))%p
     betas=[(2-pow(Q,r,p)-pow(Q,-r,p))%p for r in range(N)]
     for sigma in dict.fromkeys([-2%p,2,0,nodes[0],nodes[M]]):
      aa=[(v-sigma)%p for v in nodes]
      ar=1
      for v in aa[m:]:ar=ar*v%p
      for x,b,c,y in [(2,3,5,7),(0,3,5,7),(2,0,5,7),(2,3,5,0)]:
       A=x+y;P=x*y;B,R,oldR,Z=1,0,0,0
       for r in range(M+1):
        gamma=0 if r<2 else -ss(r)*ss(r-1)*aa[r-1]%p
        matrix=sp.Matrix([[b*aa[r],0,0,0],[1,betas[r]*A,gamma*P,0],[0,1,0,0],[1,betas[r]*A,gamma*P,c*aa[r]]])
        B,R,oldR,Z=[int(t)%p for t in matrix*sp.Matrix([B,R,oldR,Z])]
       direct=0
       for i in range(M+1):
        tail=[1]
        for j in range(i,M+1):
         if j>i:
          val=betas[j]*A*tail[-1]
          if j>=i+2:val+=(-ss(j)*ss(j-1)*aa[j-1]%p)*P*tail[-2]
          tail.append(val%p)
         weight=pow(b,i,p)*pow(c,d-j,p)*tail[j-i]%p
         for r in range(N):
          if r<i or r>j:weight=weight*aa[r]%p
         direct=(direct+weight)%p
       assert direct==ar*pow(c,d-M,p)*Z%p
       counts['four_state_values']+=1
      counts['spectral_values']+=1
     for k in range(N+1):
      zz=pow(loc.eta,k,p)
      sigma=(-zz*zz-pow(zz,-2,p))%p
      ar=1
      for node in nodes[m:]:ar=ar*(node-sigma)%p
      if N%2==0:target=(pow(zz,N,p)+pow(zz,-N,p))%p
      else:target=(zz-pow(zz,-1,p))*(pow(zz,N,p)-pow(zz,-N,p))%p
      assert ar==target,(N,k,ar,target)
      counts['exact_scalar_modes']+=1
     counts['levels']+=1
    return {"status": "PASS", "counts": counts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "research_original_four_state_transfer_results.json"))
    args = parser.parse_args()
    result = audit()
    payload = json.dumps(result, indent=2) + "\n"
    args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
