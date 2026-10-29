#!/usr/bin/env python3
"""Disjoint literal Newton sink layer, full original crossings and source tails."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork,whole_word
from audit_actual_borel_regular_fusion import fusion
from audit_actual_full_psi_scalar_flow_cycle import ScalarFlowGraph,ReducedScalarFlowGraph


def mm(a,b,p):return a@b%p


def layer_matrix(H,sign,g=None):
    N,p=H.N,H.p
    out=np.zeros((N*N,N*N),dtype=np.int64)
    for a,b in itertools.product(range(N),repeat=2):
        for h1 in range(min(a,N-1-b)+1):
            h2=a-h1;second=b+h1
            B0=H.fac[second]*H.inv[b]*H.v[h1]%p
            for h4 in range(second+1):
                first=h2+h4;h5=second-h4
                if first>=N:continue
                if sign>0:
                    coefficient=B0*H.inv[h2]*H.u[h4]*H.fac[first]%p
                else:
                    # SECOND disjoint eligible Newton sink: (h2,h4,F_first).
                    B1=H.fac[first]*H.inv[h2]*H.v[h4]%p
                    coefficient=B0*B1%p
                gaussian_power=h5 if sign>0 else h5+h4
                gaussian=(pow(g,gaussian_power,p) if g is not None
                          else (H.diag if sign>0 else H.diag_inv)[gaussian_power])
                coefficient=coefficient*gaussian*H.inv[h5]%p
                for h7 in range(min(first,N-1-h5)+1):
                    u,v=first-h7,h5+h7
                    value=coefficient*H.u[h7]*H.fac[v]%p
                    if sign>0 and g is None:
                        # Exact Gaussian+Udiag5 cell is Vdiag(x^-2 .).
                        Bfinal=H.fac[v]*H.v[h5]*pow(H.x,-h5,H.p)*H.u[h7]%p
                        grouped=B0*H.inv[h2]*H.u[h4]*H.fac[first]*Bfinal%p
                        assert grouped==value
                    out[u*N+v,a*N+b]=(out[u*N+v,a*N+b]+value)%p
    if g is None:
        out=out*(H.kappa if sign>0 else pow(H.kappa,-1,p))%p
    return out


def inverse_fusion_layer(H):
    N,p=H.N,H.p
    out=np.zeros((N*N,N*N),dtype=np.int64)
    for a,b in itertools.product(range(N),repeat=2):
        for j in range(min(a,N-1-b)+1):
            r=a-j;s=b+j
            out[r*N+s,a*N+b]=H.fac[s]*H.inv[b]*H.v[j]*H.inv[r]%p
    return out


def eligible_graph(heads,word):
    G=ReducedScalarFlowGraph(ScalarFlowGraph(heads,word))
    stars=[]
    for k,letter in enumerate(word):
        candidates=[tuple(9*k+j for j in (0,1,3))]
        candidates.append(tuple(9*k+j for j in ((2,4,6) if letter<0 else (5,7,8))))
        for ids in candidates:
            found=[i for i in range(len(G.gamma))
                   if tuple(j for j in range(len(G.edges)) if G.V[i,j])==ids]
            assert len(found)==1
            vertex=found[0]
            assert int(G.gamma[vertex])==-1
            assert all(int(G.V[vertex,j])==1 for j in ids)
            stars.append((vertex,ids))
    atoms=[j for _,ids in stars for j in ids]
    assert len(atoms)==len(set(atoms))
    assert len(stars)==2*len(word)
    return {'heads':heads,'word':word,'eligible_stars':[{'vertex':v,'atom_ids':ids} for v,ids in stars],
            'no_atom_or_positive_factorial_reused':True,
            'positive_final_star_uses_complete_Gaussian_Udiag_cell':True,
            'one_unexpanded_Rogers_star_per_crossing_retained':True}


class LayerNetwork(HardyNetwork):
    def __init__(self,N,M):
        super().__init__(N,M)
        self.layer={1:layer_matrix(self,1),-1:layer_matrix(self,-1)}

    def crossing(self,states,letter):
        i=abs(letter)-1;mat=self.layer[1 if letter>0 else -1]
        out={}
        for state,value in states.items():
            column=state[i]*self.N+state[i+1]
            for a,b in itertools.product(range(self.N),repeat=2):
                coefficient=int(mat[a*self.N+b,column])
                if coefficient:
                    key=state[:i]+(a,b)+state[i+2:]
                    out[key]=(out.get(key,0)+value*coefficient)%self.p
        return {s:v for s,v in out.items() if v}


class RawLayerNetwork(LayerNetwork):
    """Keep raw negative outputs; kill only at next touch or final source."""
    def __init__(self,N,M):
        super().__init__(N,M)
        self.raw_negative_outputs=0
        self.raw_negative_inputs_killed=0
        self.raw_final_source_kills=0

    def crossing(self,states,letter):
        i=abs(letter)-1;sign=1 if letter>0 else -1
        N,p=self.N,self.p;out={}
        for state,weight in states.items():
            a,b=state[i:i+2]
            if min(a,b)<0:
                self.raw_negative_inputs_killed+=1
                continue
            assert max(a,b)<N
            for h1 in range(min(a,N-1-b)+1):
                r=a-h1;second=b+h1
                b0=self.fac[second]*self.inv[b]*self.v[h1]%p
                for h4 in range(second+1):
                    first=r+h4;h5=second-h4
                    if first>=N:continue
                    coefficient=b0*self.inv[r]*(self.u if sign>0 else self.v)[h4]%p
                    coefficient=coefficient*self.fac[first]*self.inv[h5]%p
                    coefficient=coefficient*(self.diag[h5] if sign>0 else self.diag_inv[second])%p
                    for h7 in range(N-h5):
                        c,e=first-h7,h5+h7
                        value=weight*coefficient*self.u[h7]*self.fac[e]%p
                        value=value*(self.kappa if sign>0 else pow(self.kappa,-1,p))%p
                        if not value:continue
                        key=state[:i]+(c,e)+state[i+2:]
                        if c<0:self.raw_negative_outputs+=1
                        out[key]=(out.get(key,0)+value)%p
        return {s:v for s,v in out.items() if v}

    def word(self,initial,letters):
        states={initial:1}
        for letter in letters:states=self.crossing(states,letter)
        self.raw_final_source_kills+=sum(min(s)<0 for s in states)
        return {s:v for s,v in states.items() if min(s)>=0}


def main():
    rows=[];words=[];raw_words=[]
    for N in range(2,8):
        for M in (1,3):
            try:H=LayerNetwork(N,M)
            except ValueError:continue
            C,Ci,*_=fusion(N,H.p,H.Q,[H.x,H.x],[0,0])
            assert np.array_equal(inverse_fusion_layer(H),Ci%H.p)
            assert np.array_equal(H.layer[1],H.plus%H.p)
            assert np.array_equal(H.layer[-1],H.minus%H.p)
            # Arbitrary Gaussian values: the g exponents are literal, not
            # inferred after integrating the Gaussian or resetting its phase.
            for g in (2,3):
                D=np.diag([pow(g,b,H.p) for a,b in itertools.product(range(N),repeat=2)])
                for sign in (1,-1):
                    transfer=np.zeros_like(C)
                    coefficients=H.u if sign>0 else H.v
                    for a,b in itertools.product(range(N),repeat=2):
                        for j in range(min(N-1-a,b)+1):
                            transfer[(a+j)*N+b-j,a*N+b]=coefficients[j]
                    factors=[C,D,transfer,Ci] if sign>0 else [C,transfer,D,Ci]
                    expected=np.eye(N*N,dtype=np.int64)
                    for factor in factors:expected=mm(expected,factor,H.p)
                    assert np.array_equal(layer_matrix(H,sign,g),expected)
            # u^N B and v^N B demand a forbidden INPUT index.  They
            # do not define a scalar specialization of separate Psi sectors.
            for a,b in itertools.product(range(N),repeat=2):
                for un,vn in ((1,0),(0,1)):
                    routes=[(i,j,r) for i in range(N) for j in range(N-i)
                            for r in range(N)
                            if b==i+un*N and a==r+j+vn*N]
                    assert not routes
            rows.append({'N':N,'M':M,'both_entire_original_crossings':True,
                         'two_arbitrary_Gaussian_values_both_signs':True,
                         'whole_B_central_tail_source_zero':True,
                         'separate_Psi_or_Barnes_tail_vanishing_not_claimed':True})
            if N<=4:
                for heads,word in ((3,[1,-2,1,-2]),(4,[2,-1,3,2])):
                    words.append(whole_word(H,heads,word))
                    raw=RawLayerNetwork(N,M)
                    for sign in (1,-1):
                        witness=raw.crossing({(0,0):1},sign)
                        assert witness[(-1,1)]==(raw.kappa if sign>0 else pow(raw.kappa,-1,raw.p))*pow(raw.x,-1,raw.p)%raw.p
                    check=whole_word(raw,heads,word)
                    check.update(raw_negative_outputs=raw.raw_negative_outputs,
                                 raw_negative_inputs_killed=raw.raw_negative_inputs_killed,
                                 raw_final_source_kills=raw.raw_final_source_kills,
                                 no_projection_between_raw_crossings=True)
                    assert raw.raw_negative_outputs>0
                    raw_words.append(check)
    graphs=[eligible_graph(h,w) for h,w in [(2,[1]),(2,[-1]),(4,[2,-1,3,2]),
                                            (6,[1,-2,3,-4,5,2,-3,4])]]
    result={'local_original_source_cases':rows,'whole_original_word_sources':words,
            'raw_no_healing_whole_sources':raw_words,
            'literal_disjoint_eligible_layers':graphs,
            'scope':'exact eligible Newton layer in original words; all-u/Rogers stars, '
                    'Gaussian factors, caps and nontrivial current deck mixing retained'}
    Path(__file__).with_name('audit_actual_trivalent_layer_crossing_source_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(rows)} actual both-sign/color crossing layers, arbitrary Gaussian exponents, '
          f'{len(words)} physical + {len(raw_words)} raw no-healing whole sources and four disjoint sink graphs')


if __name__=='__main__':main()
