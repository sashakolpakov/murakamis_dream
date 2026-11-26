#!/usr/bin/env python3
"""Validate the complete inputs and exact budgets for the half-period assembly."""
import argparse,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_full_nonlow_half_region.md'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-full-nonlow-half-region.json')
    args=ap.parse_args();ph,sh=sha(PROOF),sha(__file__)
    dependencies={};summaries={}
    specs=[
        ('mixed_full_left_region','check',''),
        ('mixed_split_cutoff_hybrid_contour','check',''),
        ('mixed_left_right_interface_source','certify',''),
        ('mixed_right_selected_height_removal','certify',''),
        ('mixed_right_selected_height_removal','certify','-replay'),
        ('mixed_unselected_right_clamping','certify',''),
        ('mixed_unselected_right_clamping','certify','-replay'),
    ]
    for stem,prefix,suffix in specs:
        pp=f'notes/research_{stem}.md';ss=f'experiments/{prefix}_{stem}.py'
        rr=f'repro/results/research-{stem.replace("_","-")}{suffix}.json'
        rec=json.loads((ROOT/rr).read_text())
        for p in (pp,ss,rr): dependencies[p]=sha(ROOT/p)
        assert rec['status']=='passed',rr
        assert rec['proof_sha256']==dependencies[pp] and rec['script_sha256']==dependencies[ss]
        for key in ('dependencies','dependencies_sha256'):
            for p,h in rec.get(key,{}).items():
                assert sha(ROOT/p)==h,(rr,p)
                if p in dependencies:assert dependencies[p]==h
                dependencies[p]=h
        summary={k:rec[k] for k in ('products','leaves','visits','monotone_reductions',
                    'precision_bits','input_sha256','proof_sha256','script_sha256') if k in rec}
        if stem=='mixed_right_selected_height_removal':
            expected=[]
            for clipped in (False,True):
                for eta,gamma in itertools.product((0,1),repeat=2):
                    na=7 if clipped and eta==0 else 6
                    nc=7 if clipped and gamma==0 else 6
                    for sides in itertools.product(range(na),range(3),range(nc)):
                        expected.append(dict(clipped=clipped,types=[eta,gamma],sides=list(sides)))
            assert rec['products']==939 and [r['case']for r in rec['cases']]==expected
            assert sum(r['leaves']for r in rec['cases'])==rec['leaves']
            assert sum(r['visits']for r in rec['cases'])==rec['visits']
            assert all(r['visits']==2*r['leaves']-1 for r in rec['cases'])
            summary['case_counts']=[(r['leaves'],r['visits'])for r in rec['cases']]
        if stem=='mixed_unselected_right_clamping':
            expected=[list(v)for v in itertools.product((0,1),(0,1),(0,1),range(6),range(6))]
            assert rec['products']==288 and rec['product_range']==[0,288]
            assert [r['case']for r in rec['case_summaries']]==expected
            assert [r['index']for r in rec['case_summaries']]==list(range(288))
            for key in ('leaves','visits'):
                assert sum(r[key]for r in rec['case_summaries'])==rec[key]
            assert sum(r['monotone']for r in rec['case_summaries'])==rec['monotone_reductions']
            cover=Path(rec['cover_path']);cover=cover if cover.is_absolute() else ROOT/cover
            assert sha(cover)==rec['cover_sha256']
            dependencies[str(cover.relative_to(ROOT))]=rec['cover_sha256']
            summary['case_counts']=[(r['leaves'],r['visits'],r['monotone'])for r in rec['case_summaries']]
        summaries[(stem,suffix)]=summary
        del rec
    for stem in ('mixed_right_selected_height_removal','mixed_unselected_right_clamping'):
        author=summaries[stem,''];replay=summaries[stem,'-replay']
        source=f'repro/results/research-{stem.replace("_","-")}.json'
        assert replay['input_sha256']==dependencies[source]
        assert replay['precision_bits']>=320 and author['precision_bits']>=256
        for key in ('products','leaves','visits','case_counts','proof_sha256','script_sha256'):
            assert author[key]==replay[key],(stem,key)
    # The pointwise face estimate and the one-time source tolerance budget.
    exact=0
    assert F(1,2)*(F('.45')-F('.39'))**2==F(9,5000)>F(1,800);exact+=1
    assert F(1,1600)<F(1,800) and F(1,2000)<F(1,1000);exact+=2
    assert F(1,2000)/2==F(1,4000) and F(1,1600)/2==F(1,3200);exact+=2
    assert F('.45')>F('.22')>F('.12')>F('.1');exact+=1
    assert F('.014')==F(7,500) and F('.057')==F(57,1000);exact+=2
    assert 400*(F('.5')-F('.45'))**2==1;exact+=1
    assert -F('.057')<=0<=F('.02') and -F('.03')<0;exact+=2
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in dependencies.items())
    result=dict(status='passed',exact_checks=exact,primary_records=len(specs),
        clamping_domains=939+288,cyclic_pattern_enumerations=0,
        file_bindings=len(dependencies),proof_sha256=ph,script_sha256=sh,
        dependencies_sha256=dependencies,
        phase_gap='min(1/2000, mu/1600)',finite_gap='min(1/4000, mu/3200)',
        scope='Written arbitrary-length assembly on [0.1,0.5]^m from completed original source, selected-height and unselected-clamp inputs. No new numerical inequalities, full-period theorem or short-filling conclusion.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',exact,'exact checks,',len(specs),'primary records,',len(dependencies),'current bindings')

if __name__=='__main__':main()
