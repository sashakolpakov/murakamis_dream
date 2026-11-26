#!/usr/bin/env python3
"""Correlated Schur bound for a larger analytic source class.

This concerns the original analytic phase, not a full-source tail bound.
The cover has one real output and two real critical-wire displacements.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


class Jet:
    """Value and two exact first holomorphic derivatives."""
    def __init__(self, value, dz=0, dw=0):
        self.v, self.z, self.w = acb(value), acb(dz), acb(dw)
    @staticmethod
    def cast(other): return other if isinstance(other, Jet) else Jet(other)
    def __add__(self, other):
        q=self.cast(other)
        return Jet(self.v+q.v,self.z+q.z,self.w+q.w)
    __radd__=__add__
    def __neg__(self): return Jet(-self.v,-self.z,-self.w)
    def __sub__(self,other): return self+-self.cast(other)
    def __rsub__(self,other): return self.cast(other)+-self
    def __mul__(self,other):
        q=self.cast(other)
        return Jet(self.v*q.v,self.z*q.v+self.v*q.z,self.w*q.v+self.v*q.w)
    __rmul__=__mul__
    def inverse(self):
        return Jet(1/self.v,-self.z/self.v**2,-self.w/self.v**2)
    def __truediv__(self,other): return self*self.cast(other).inverse()
    def __rtruediv__(self,other): return self.cast(other)*self.inverse()
    def __pow__(self,n):
        assert n>=0
        out=Jet(1)
        for _ in range(n):out=out*self
        return out
    def sqrt(self):
        root=self.v.sqrt()
        return Jet(root,self.z/(2*root),self.w/(2*root))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--max-cells', type=int, default=50000)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-real-output-phase-schur.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    pi, ii = arb.pi(), acb(0,1)
    sq = arb(21).sqrt()
    rho = (5-sq)/2
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    xh = acb(arb(1)/6,arb(2).log()/(2*pi))

    def a(q):
        q = Q(q)
        return arb(q.numerator)/q.denominator

    def interval(lo,hi):
        return arb(a((lo+hi)/2),a((hi-lo)/2))

    scalar_checks=[]
    def positive(name,value):
        assert value>0,(name,value)
        scalar_checks.append({'name':name,'strict_positive_margin':str(value)})
    R,W,H,b,e=map(a,[Q(1,200),Q(9,1000),Q(13,2000),Q(9,50),Q(13,50)])
    D=5+sq
    positive('complex-disk outgoing derivative below .16',
             a(Q(4,25))-(a(Q(1,10))+a(Q(21,10))**2/(D-b-a(Q(1,10)))-4/D))
    positive('real-output kernel Hessian defect below .26',e-18*(R+W))
    positive('real-output critical contraction below .05',a(Q(1,20))-rho*(b+e)/2)
    positive('real-output critical disk is a strict self-map',
             R-rho*W-rho*(H+b*R+e*(R+W))/2)
    critical_radius=(rho*(1+e/2)*W+rho*H/2)/(1-rho*(b+e)/2)
    residual_radius=rho*(H+e*W+(b+e)*critical_radius)/2
    positive('critical modulus below .002936',a(Q(367,125000))-critical_radius)
    positive('correlated critical residual below .00106',a(Q(53,50000))-residual_radius)

    def phase_data(z,w):
        x,y=xh+z,xh+w
        xv,yv=(2*pi*ii*x).exp(),(2*pi*ii*y).exp()
        X,Y=Jet(xv,2*pi*ii*xv,0),Jet(yv,0,2*pi*ii*yv)
        al,be=1/X-1,1/Y-1
        delta=1-2*(al+be)+(al-be)**2
        root=delta.sqrt()
        U,V=(1+al-be-root)/2,(1-al+be-root)/2
        ax,by=-2*pi*ii/X,-2*pi*ii/Y
        Ux,Uy,Vy=ax*(1-U)/root,by*U/root,by*(1-V)/root
        pxx=(-Ux/(U*(1-X*U))+2*pi*ii*X*(1-U)/((1-X)*(1-X*U)))/k0
        pxy=(-Uy/(U*(1-X*U)))/k0
        pyy=(-Vy/(V*(1-Y*V))+2*pi*ii*Y*(1-V)/((1-Y)*(1-Y*V)))/k0
        base=pyy+sq-pxy**2/(pxx-sq)
        return base,pxx.v,pxy.v,delta.v

    domain = [(Q(-9,1000),Q(9,1000)),
              (Q(-53,50000),Q(53,50000)),
              (Q(-53,50000),Q(53,50000))]
    pending = [(domain, '')]
    cells = []
    visits = 0
    while pending:
        box, address = pending.pop()
        visits += 1
        assert visits <= args.max_cells, 'Explicit visit budget exhausted'
        w, xi, eta = [interval(*pair) for pair in box]
        z = rho*w+acb(xi,eta)
        basejet,pxx,pxy,delta=phase_data(z,w)
        wc,xc,yc=[a((lo+hi)/2) for lo,hi in box]
        center=phase_data(rho*wc+acb(xc,yc),wc)[0].v
        radii=[arb(0,a((hi-lo)/2)) for lo,hi in box]
        base=center+(rho*basejet.z+basejet.w)*radii[0]+basejet.z*radii[1]+ii*basejet.z*radii[2]
        denom = abs(pxx-sq)
        perturb = abs(pxy)**2*a(Q(9,50))/(denom*(denom-a(Q(9,50))))
        bound = abs(base)+perturb
        good = (delta.imag > 0 and a(Q(1,200))-abs(z) > 0
                and denom > a(Q(9,50)) and a(Q(3,20))-bound > 0)
        if good:
            cells.append({'address':address,'box':[[str(lo),str(hi)] for lo,hi in box],
                          'Schur_base':base.str(30,more=True),
                          'incoming_perturbation_bound':str(perturb),
                          'strict_margin_below_3_20':str(a(Q(3,20))-bound),
                          'root_branch_margin':str(delta.imag),
                          'critical_disk_margin':str(a(Q(1,200))-abs(z)),
                          'denominator_margin':str(denom-a(Q(9,50)))})
            if len(cells)%2048 == 0:
                print(f'Accepted {len(cells)}, visited {visits}, pending {len(pending)}',flush=True)
            continue
        # Split the largest actual coordinate diameter; output w enters
        # both wires and is not artificially downweighted by rho.
        axis = max(range(3),key=lambda i:box[i][1]-box[i][0])
        lo,hi = box[axis]
        mid = (lo+hi)/2
        left,right = list(box),list(box)
        left[axis],right[axis] = (lo,mid),(mid,hi)
        pending.extend([(right,address+str(axis)+'1'),(left,address+str(axis)+'0')])

    # Independently reconstruct each binary path from the original box.
    # A complete prefix tree, not only total volume, checks multiplicity.
    leaves = {c['address'] for c in cells}
    assert len(leaves) == len(cells)
    for cell in cells:
        reconstructed = list(domain)
        address = cell['address']
        assert len(address)%2 == 0
        for i in range(0,len(address),2):
            axis,side = map(int,address[i:i+2])
            lo,hi = reconstructed[axis];mid=(lo+hi)/2
            reconstructed[axis]=(lo,mid) if side==0 else(mid,hi)
        assert [[str(lo),str(hi)] for lo,hi in reconstructed] == cell['box']
    tree={}
    for address in leaves:
        node=tree
        for i in range(0,len(address),2):
            assert 'leaf' not in node
            axis,side=address[i:i+2]
            assert node.setdefault('axis',axis)==axis
            node=node.setdefault(side,{})
        assert not node
        node['leaf']=True
    def check_tree(node):
        if 'leaf' in node:
            assert set(node)=={'leaf'}
        else:
            assert set(node)=={'axis','0','1'}
            check_tree(node['0']);check_tree(node['1'])
    check_tree(tree)
    deps=['notes/research_three_larger_phase_class.md',
          'notes/research_three_vertex_input_rectangle.md',
          'notes/research_three_phase_graph_transform.md']
    result={'status':'passed','precision_bits':args.precision,
            'scope':'Analytic Schur derivative bound for w real +/- .009 and z=rho*w+xi+i*eta, |xi|,|eta|<=.00106, incoming derivative defect <=.18. No global source propagation or entrance hypothesis is certified.',
            'cell_count':len(cells),'visited_cells':visits,'cells':cells,
            'domain':[[str(lo),str(hi)] for lo,hi in domain],
            'outgoing_derivative_bound':'3/20','incoming_derivative_bound':'9/50',
            'strict_scalar_comparisons':len(scalar_checks),'scalar_checks':scalar_checks,
            'method':'Centered holomorphic mean-value enclosure of the full correlated Schur expression, with exact forward derivative jets; direct outward denominator and incoming-defect perturbation bounds.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
            'elapsed_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['status','cell_count','visited_cells','elapsed_seconds']},indent=2))


if __name__=='__main__':main()
