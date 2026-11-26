#!/usr/bin/env python3
"""Bounded test of minimum transport with a literal right raw envelope.

All numbers are floating diagnostics. Row grids are not upper certificates.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
HELP = ROOT/'repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py'
REFS = Path(__file__).resolve().with_name('reference_inputs.json')
spec = importlib.util.spec_from_file_location('original_phase_diagnostic',HELP)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def evaluate(word, ref, reals, selection, rows):
    x=np.asarray(reals)
    sig=np.asarray(selection)
    m=len(word)
    taper=np.where(x<=.45,1,np.where(x<.5,400*(.5-x)**2,0))
    h=np.zeros_like(x)
    for j in range(m):
        end=.12 if sig[j] else .22
        cut=np.clip((x[:,[(j-1)%m,j,(j+1)%m]]-.1)/(end-.1),0,1).min(axis=1)
        h[:,j]=(.014 if sig[j] else ref[j].imag)*taper[:,j]*cut
    z=x+1j*h
    total=np.zeros(len(x))
    maximizing=[]
    for j in range(m):
        k=(j+1)%m
        a,b=z[:,j],z[:,k]
        eta,eps=word[j],word[k]
        if j==0 or k==0:
            u=rows[None,:]
            def integral(w):
                return ((q.g(w.real[:,None]+u-1j*np.abs(w.imag[:,None]))
                         -q.g(w.real[:,None]-1j*np.abs(w.imag[:,None]))).real
                        +2*np.pi*np.maximum(w.imag[:,None],0)*u)
            row=(integral(a)+integral(b)-(2+eps)*q.g(u).real
                 -2*np.pi*a.imag[:,None]*u)
            for w,kind,s in ((a,eta,sig[j]),(b,eps,sig[k])):
                row += kind/2*(np.maximum(-q.g(w).real,2*np.pi*np.maximum(w.imag,0))
                               -2*np.pi*s*w.imag)[:,None]
            indices=row.argmax(axis=1)
            total+=row[np.arange(len(x)),indices]
            maximizing.append(rows[indices])
        else:
            total+=q.phase(a,b,eta,eps)[0].real
            total+=sig[j]/2*np.maximum(q.g(a).real,-2*np.pi*a.imag)
            total+=sig[k]/2*np.maximum(q.g(b).real,-2*np.pi*b.imag)
    return total,np.asarray(maximizing).T


def main():
    saved=json.loads(REFS.read_text())
    references=[r for r in saved['references'] if len(r['word']) in (3,4)]
    levels=np.linspace(.12,.22,101)
    rowgrid=np.linspace(0,1,2049)
    cases=[]
    for reference in references:
        word=reference['word']
        ref=np.array([complex(*v) for v in reference['reference']])
        for right in (.5,.7,.9):
            for side in ('left','right','both'):
                initial=ref.real.copy();initial[0]=right
                if side in ('right','both'): initial[1]=.12
                if side in ('left','both'): initial[-1]=.16 if side=='both' else .12
                for selected in (False,True):
                    sig=[int(selected and typ and j!=0) for j,typ in enumerate(word)]
                    x=np.maximum(initial[None,:],levels[:,None]);x[:,0]=right
                    values,indices=evaluate(word,ref,x,sig,rowgrid)
                    delta=np.diff(values)
                    k=int(delta.argmin())
                    cases.append(dict(word=word,reference=reference['reference'],selection=sig,
                                      right=right,side=side,minimum_sample_increment=float(delta[k]),
                                      level_pair=levels[k:k+2].tolist(),
                                      real_pair=x[k:k+2].tolist(),
                                      maximizing_rows=indices[k:k+2].tolist(),
                                      rate_pair=values[k:k+2].tolist()))
    worst=min(cases,key=lambda r:r['minimum_sample_increment'])
    result=dict(scope='Floating diagnostic only. Raises all nonright coordinates below the current minimum level, with the exact hybrid heights and a dense raw-row grid on the two right-incident edges. No continuous row maximum, transport theorem or finite-source counterexample is certified.',
                row_grid_size=len(rowgrid),transport_levels=levels.tolist(),
                cases=cases,worst=worst,
                dependencies_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in(HELP,REFS,Path(__file__).resolve())})
    Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(worst))


if __name__=='__main__':
    main()
