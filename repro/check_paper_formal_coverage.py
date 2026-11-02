#!/usr/bin/env python3
"""Validate a paper/formal coverage snapshot; does not compile or prove it."""
import argparse
import hashlib
import json
import pathlib
import re

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--root',type=pathlib.Path,default=pathlib.Path.cwd())
p.add_argument('--coverage',type=pathlib.Path,required=True)
p.add_argument('--output',type=pathlib.Path,required=True)
args=p.parse_args()
args.output.unlink(missing_ok=True)
if not __debug__:
    raise SystemExit('Assertions must be enabled; old output removed.')
root=args.root.resolve();data=json.loads(args.coverage.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for path,wanted in data['input_sha256'].items():
    actual=sha(root/path)
    assert actual==wanted,('source hash mismatch',path,wanted,actual)
std=json.loads((root/'repro/results/proof-logic/summary.json').read_text())
real=json.loads((root/'repro/results/concrete-limits/summary.json').read_text())
known=set(std['theorems'])|set(real['theorems'])
for record in [std,real]:
    for path,wanted in record['source_sha256'].items():
        assert sha(root/path)==wanted,('compiled record hash mismatch',path)
cat=json.loads((root/'papers/catalog.json').read_text())['papers']
current={p['directory'] for p in cat if p.get('edition')!='earlier'}
assert {r['article'] for r in data['rows']}==current
assert len(data['rows'])==len(current)==data['current_articles']
locators=set();decls=set()
for row in data['rows']:
    entries=row['conclusion_sources']+row['compiled_results']
    for imp in row['written_dependency_locator_inventory']:entries+=imp['sources']
    for e in entries:
        text=(root/e['path']).read_text()
        assert e['anchor'] in text,('missing anchor',e)
        assert text[:text.index(e['anchor'])].count('\n')+1==e['line'],('wrong source line',e)
        locators.add((e['path'],e['anchor']))
    for e in row['compiled_results']:
        assert e['declaration'] in known,('declaration not compiled',e)
        namespace=re.findall(r'^namespace\s+(\S+)',(root/e['path']).read_text(),re.M)
        assert len(namespace)==1 and e['anchor'].startswith('theorem '),('ambiguous declaration namespace',e)
        assert e['declaration']==namespace[0]+'.'+e['anchor'].removeprefix('theorem '),('declaration/anchor mismatch',e)
        decls.add(e['declaration'])
result={'result':'All source hashes, current-paper rows, declaration inventories and literal locators match.',
 'scope':'Snapshot consistency only; no proof certification, source analysis or Lean replay.',
 'papers':len(current),'distinct_decl_references':len(decls),'distinct_locators':len(locators),
 'coverage_sha256':sha(args.coverage),'checker_sha256':sha(pathlib.Path(__file__)),
 'record_sha256':{f:sha(root/f) for f in ['repro/results/proof-logic/summary.json','repro/results/concrete-limits/summary.json']}}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
