#!/usr/bin/env python3
"""One outward cap-cut comparison at an already certified actual open root.

No search, new root proposal, full cap asymptotic, or invariant conclusion.
"""
import hashlib
import json
from pathlib import Path
import sys
from fractions import Fraction as F
from flint import acb, arb, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'experiments'))
import certify_mixed_open_word_critical_localization as roots

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator

def main():
    ctx.prec=320
    script_hash=sha(__file__)
    bindings={}
    def bind(path,expected=None):
        digest=sha(ROOT/path)
        if expected is not None:assert digest==expected,path
        assert path not in bindings or bindings[path]==digest,path
        bindings[path]=digest
        return digest
    author_path='repro/results/research-mixed-open-word-critical-localization.json'
    replay_path='repro/results/research-mixed-open-word-critical-localization-replay.json'
    author=json.loads((ROOT/author_path).read_text());bind(author_path)
    replay=json.loads((ROOT/replay_path).read_text());bind(replay_path)
    assert author['status']==replay['status']=='passed'
    assert replay['input_sha256']==bindings[author_path]
    assert replay['one_vertex'][1]['witness']==author['one_vertex'][1]['witness']
    bind('notes/research_mixed_open_word_critical_localization.md',author['proof_sha256'])
    bind('experiments/certify_mixed_open_word_critical_localization.py',author['script_sha256'])
    for p,h in author['dependencies_sha256'].items():bind(p,h)
    for p in ['notes/research_mixed_conditional_torus_composition.md',
              'notes/research_mixed_endpoint_packet_extension_criterion.md',
              'notes/research_mixed_three_first_cap_packet.md',
              'notes/research_mixed_three_first_cap_fourier_reduction.md']:
        bind(p)
    witness=author['one_vertex'][1]['witness']
    assert roots.test(witness,acb(0),1,one=True) is not None
    radius=ar(witness['radius'])
    z=roots.cp(witness['centers'][0])+acb(arb(0,radius),arb(0,radius))
    pi,ii=arb.pi(),acb(0,1)
    def J(v):return (pi*pi/6-(2*pi*ii*v).exp().polylog(2))/(2*pi*ii)+ii*pi*v*(1-v)/2
    def g(v):return J(v)+ii*pi*v*(1-v)/2
    def uc(e):return ((ii+(1-2*(2*pi*ii*e).exp()).sqrt())/2).atan()/pi
    def S(e):
        u=uc(e)
        return -2*J(ar('1/2')-u)-3*J(u)-J(e-u)+ii*pi*e*u
    def phase(e,t):return S(e)+J(e+t)-J(t)-ii*pi*e*t-g(e)
    cut=acb(ar('33/100'))
    excess=(phase(cut,z)-phase(z,z)).real
    assert excess>ar('13/1000')
    # The original summand factors are regular at N multiple 100:
    # e=.33, t=z, and e+t are strictly within their sine strips.
    assert 0<z.real<ar('1/2') and 0<(cut+z).real<1
    assert sha(__file__)==script_hash
    for p,h in bindings.items():assert sha(ROOT/p)==h,p
    output={'status':'passed_fixed_comparison','precision_bits':320,
            'scope':'Failure of discarding all real outer rows to the left of the E-only cap cut .33. Not failure of the full cap or original invariant.',
            'type_word':[4],'outgoing_parameter':'the actual symmetric type4 one-vertex private critical leg',
            'cut':'33/100','critical_parameter_enclosure':str(z),
            'original_log_root_selfmap_rechecked':True,
            'excess':str(excess),'strict_floor':'13/1000',
            'physical_levels':'N divisible by 100; row i=33N/100',
            'dependencies_sha256':bindings,'script_sha256':script_hash}
    (HERE/'result.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS fixed original type4 cap-cut excess',excess)

if __name__=='__main__':main()
