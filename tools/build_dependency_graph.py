#!/usr/bin/env python3
"""Validate and render the mathematical dependency graph.

Edges are manually traced uses of results, not links inferred from file names.
This checks the graph and its source locators, not the underlying proofs.
Only the Python standard library is required.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
from html import escape
import json
from pathlib import Path
import textwrap
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/sashakolpakov/murakamis_dream/blob/main/"


def topological(nodes, edges):
    incoming = {n: set() for n in nodes}
    outgoing = {n: set() for n in nodes}
    for a, b in edges:
        incoming[b].add(a)
        outgoing[a].add(b)
    order = []
    ready = sorted(n for n in nodes if not incoming[n])
    remaining = {n: set(v) for n, v in incoming.items()}
    while ready:
        n = ready.pop(0)
        order.append(n)
        for other in sorted(outgoing[n]):
            remaining[other].remove(n)
            if not remaining[other]:
                ready.append(other)
                ready.sort()
    if len(order) != len(nodes):
        unresolved = sorted(set(nodes) - set(order))
        raise ValueError("Cycle in declared dependencies: " + ", ".join(unresolved))
    return order, incoming, outgoing


def closure(start, adjacency):
    found, pending = set(), list(adjacency[start])
    while pending:
        item = pending.pop()
        if item not in found:
            found.add(item)
            pending.extend(adjacency[item])
    return found


def reduce_edges(edges, outgoing):
    """Remove edges whose endpoint is already reached through another neighbor."""
    result = set(edges)
    for a, b in edges:
        if any(b in closure(other, outgoing) for other in outgoing[a] if other != b):
            result.remove((a, b))
    return result


def svg_graph(groups, edges):
    order, incoming, outgoing = topological(groups, edges)
    ranks = {}
    for group in order:
        ranks[group] = max((ranks[p] + 1 for p in incoming[group]), default=0)
    rows = defaultdict(list)
    for group in order:
        rows[ranks[group]].append(group)
    box_w, box_h, gap_x, gap_y = 260, 110, 28, 85
    width = max(len(row) for row in rows.values()) * (box_w + gap_x) + 160
    height = len(rows) * (box_h + gap_y) + 12
    positions = {}
    for rank, row in rows.items():
        left = (width - len(row) * (box_w + gap_x) + gap_x) / 2
        for column, group in enumerate(row):
            positions[group] = (left + column * (box_w + gap_x), 20 + rank * (box_h + gap_y))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="graph-title graph-desc">',
             '<title id="graph-title">Dependencies between mathematical components</title>',
             '<desc id="graph-desc">Arrows point from a prerequisite to the component that uses it. Select a component to inspect the statements and source locations. Transitive arrows are omitted in this overview.</desc>',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#52717e"/></marker></defs>',
             '<rect width="100%" height="100%" fill="white"/>']
    long_index = 0
    for a, b in sorted(reduce_edges(edges, outgoing)):
        ax, ay = positions[a]
        bx, by = positions[b]
        x1, y1, x2, y2 = ax + box_w / 2, ay + box_h, bx + box_w / 2, by - 5
        middle = (y1 + y2) / 2
        if ranks[b] - ranks[a] > 1:
            # Route long dependencies around the boxes on intermediate rows.
            # Passing through a box would visually invent a false dependency.
            inset = 12 + 9 * (long_index % 5)
            rail = inset if x1 + x2 < width else width - inset
            long_index += 1
            path = f'M{x1} {y1} V{y1+30} H{rail} V{y2-30} H{x2} V{y2}'
        else:
            path = f'M{x1} {y1} C{x1} {middle} {x2} {middle} {x2} {y2}'
        parts.append(f'<path d="{path}" fill="none" stroke="#52717e" stroke-width="1.6" stroke-linejoin="round" marker-end="url(#arrow)"/>')
    for group in order:
        x, y = positions[group]
        lines = textwrap.wrap(groups[group]["title"], 29)
        parts.append(f'<a href="dependencies.html#{escape(group)}" data-group="{escape(group)}"><g>')
        fill = '#fff3e8' if groups[group].get('open') else '#f1f6f8'
        parts.append(f'<rect id="{escape(group)}" x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" fill="{fill}" stroke="#38677c" stroke-width="1.4"/>')
        first_y = y + 32 if len(lines) <= 2 else y + 23
        for j, line in enumerate(lines):
            parts.append(f'<text x="{x+box_w/2}" y="{first_y+j*23}" text-anchor="middle" font-family="Georgia,serif" font-size="18" fill="#183444">{escape(line)}</text>')
        parts.append(f'<text x="{x+box_w/2}" y="{y+91}" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#52646b">{groups[group]["count"]} recorded statements</text></g></a>')
    parts.append('</svg>')
    return "\n".join(parts)


HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mathematical dependencies · Murakami’s Dream</title>
<style>
:root{font-family:system-ui,sans-serif;color:#203945;background:#fff}body{max-width:1450px;margin:auto;padding:24px}h1,h2,h3{font-family:Georgia,serif;font-weight:500}h1{font-size:36px}p,li{line-height:1.6}a{color:#146580}button,select,input{font:inherit}button{padding:7px 12px;background:#edf4f7;border:1px solid #b8cbd4;border-radius:5px;cursor:pointer}button:hover,button:focus{background:#dbeaf0}#overview{overflow:auto;border:1px solid #d6e2e6;border-radius:8px}#overview svg{display:block;width:100%;min-width:600px;max-height:850px}#overview a:hover rect{fill:#dcecf2}.controls{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:22px 0}.controls input{padding:8px;width:340px;max-width:90%}.layout{display:grid;grid-template-columns:minmax(250px,1fr) minmax(350px,2fr);gap:26px}#nodes{display:flex;flex-direction:column;gap:5px;max-height:800px;overflow:auto}#nodes button{text-align:left}#nodes button.selected{background:#cee5ef;border-color:#30657c}#details{border:1px solid #d7e3e8;border-radius:8px;padding:22px;min-height:260px}#details h2{margin-top:0}.label{font-size:13px;color:#536b77}.small{font-size:14px;color:#536b77}.dep{margin-bottom:14px}.dep button{margin-bottom:3px}code{overflow-wrap:anywhere;font-size:13px}.facts{border-top:1px solid #d7e3e8;margin-top:26px;padding-top:12px}#details .open{color:#9b4a17}summary{cursor:pointer} @media(max-width:800px){.layout{grid-template-columns:1fr}#nodes{max-height:300px}body{padding:15px}}
</style></head><body>
<p><a href="index.html">Finite quantum invariants and hyperbolic volume</a> · <a href="../index.html">Illustrated guide</a></p>
<h1>Which results use which?</h1>
<p>An arrow points from a prerequisite to the component that uses it. The overview groups related statements and omits transitive arrows. Select a component, then a statement, to see its direct inputs, the reason each is needed, its downstream uses and the exact source locations.</p>
<p class="small">This is an explicit, manually traced proof inventory. The checks detect missing source anchors and cycles in the recorded graph. They do not establish the truth of a statement or prove that every dependency has been found. Component boundaries are proposals for organizing papers, not additional theorems.</p>
<div id="overview">__SVG__</div>
<div class="controls"><label for="groups">Component </label><select id="groups"><option value="">All components</option></select><input id="search" aria-label="Search mathematical statements" placeholder="Find a statement or mathematical term"><button id="clear">Show all</button></div>
<div class="layout"><div><h2>Statements</h2><div id="nodes"></div></div><section id="details" aria-live="polite"></section></div>
<section class="facts"><h2>What the graph tells us</h2><div id="analysis"></div><p><a href="dependencies.json">Download the mathematical inventory</a> · <a href="dependencies.svg">Open the overview as a vector image</a> · <a href="dependency-analysis.json">Checks and source hashes</a></p></section>
<script id="graph-data" type="application/json">__DATA__</script>
<script>
const data=JSON.parse(document.getElementById('graph-data').textContent), nodes=new Map(data.nodes.map(n=>[n.id,n]));
const groups=document.getElementById('groups'),search=document.getElementById('search'),list=document.getElementById('nodes'),details=document.getElementById('details');let selected=null;
const h=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
Object.entries(data.groups).forEach(([id,g])=>{let o=document.createElement('option');o.value=id;o.textContent=g.title;groups.append(o)});
function button(n){return '<button data-node="'+h(n.id)+'">'+h(n.title)+'</button>'}
function renderList(){list.innerHTML=data.nodes.filter(n=>(!groups.value||n.group===groups.value)&&(!search.value||(n.title+' '+n.statement).toLowerCase().includes(search.value.toLowerCase()))).map(n=>'<button class="'+(n.id===selected?'selected':'')+'" data-node="'+h(n.id)+'">'+h(n.title)+'</button>').join('')||'<p>No matching statements.</p>'}
function select(id){const n=nodes.get(id);if(!n)return;selected=id;renderList();let users=data.nodes.filter(x=>x.depends_on.some(d=>d.id===id));details.innerHTML='<p class="label">'+h(data.groups[n.group].title)+'</p><h2>'+h(n.title)+'</h2><p>'+h(n.statement)+'</p>'+(n.status==='open'?'<p class="open">This result remains open.</p>':'')+'<h3>Where it is stated or proved</h3><ul>'+n.sources.map(s=>'<li><a href="'+h(s.url)+'">'+h(s.path)+'</a><br><code>'+h(s.anchor)+'</code></li>').join('')+'</ul><h3>Direct prerequisites</h3>'+(n.depends_on.length?n.depends_on.map(d=>'<div class="dep">'+button(nodes.get(d.id))+'<br>'+h(d.reason)+'</div>').join(''):'<p>No earlier result in this inventory is required. Definitions and standard background are stated in the source; this is not a claim of logical independence from all mathematics.</p>')+'<h3>Used directly by</h3>'+(users.length?users.map(u=>'<div class="dep">'+button(u)+'<br>'+h(u.depends_on.find(d=>d.id===id).reason)+'</div>').join(''):'<p>No downstream use is recorded here.</p>')+(n.coverage?'<p class="small">'+h(n.coverage)+'</p>':'');location.hash=id}
document.addEventListener('click',e=>{let b=e.target.closest('[data-node]');if(b){select(b.dataset.node);return}let a=e.target.closest('[data-group]');if(a){e.preventDefault();groups.value=a.dataset.group;search.value='';renderList();location.hash=groups.value;document.querySelector('.controls').scrollIntoView({block:'start'})}});
groups.addEventListener('change',renderList);search.addEventListener('input',renderList);document.getElementById('clear').addEventListener('click',()=>{groups.value='';search.value='';renderList()});
document.getElementById('analysis').innerHTML='<p>'+data.nodes.length+' statements and '+data.analysis.edges+' direct uses are recorded. The statement graph and the proposed component graph have no directed cycles.</p><p>The most widely used prerequisites, counted by distinct downstream statements in this inventory, are:</p><ul>'+data.analysis.shared_prerequisites.slice(0,6).map(x=>'<li>'+button(nodes.get(x.id))+' — '+x.downstream+' downstream statements</li>').join('')+'</ul><p>These counts locate shared foundations; they measure neither mathematical importance nor how much of a proof has been verified.</p>';
const initial=decodeURIComponent(location.hash.slice(1));if(data.groups[initial])groups.value=initial;renderList();select(nodes.has(initial)?initial:data.nodes[0].id);
</script></body></html>'''


def main():
    source = ROOT / "papers/dependencies.json"
    data = json.loads(source.read_text())
    nodes = {n["id"]: n for n in data["nodes"]}
    if len(nodes) != len(data["nodes"]):
        raise ValueError("Repeated statement identifier")
    groups = data["groups"]
    hashes = {}
    edges = set()
    for name, node in nodes.items():
        if node["group"] not in groups or not node["statement"].strip() or not node["sources"]:
            raise ValueError(f"{name}: missing group, statement or source")
        for location in node["sources"]:
            path = ROOT / location["path"]
            content = path.read_text()
            if not location["anchor"] or location["anchor"] not in content:
                raise ValueError(f"{name}: missing anchor {location}")
            line = content[:content.index(location["anchor"])].count("\n") + 1
            location["url"] = REPO + quote(location["path"]) + f"#L{line}"
            hashes[location["path"]] = hashlib.sha256(path.read_bytes()).hexdigest()
        for item in node["depends_on"]:
            if item["id"] not in nodes or not item["reason"].strip():
                raise ValueError(f"{name}: missing prerequisite or explanation: {item}")
            edges.add((item["id"], name))
    order, incoming, outgoing = topological(nodes, edges)
    for name in order:
        if nodes[name].get("status", "written") != "open":
            open_inputs = [p for p in closure(name, incoming) if nodes[p].get("status") == "open"]
            if open_inputs:
                raise ValueError(f"{name}: written result imports open statements {open_inputs}")
    group_edges = {(nodes[a]["group"], nodes[b]["group"]) for a, b in edges if nodes[a]["group"] != nodes[b]["group"]}
    topological(groups, group_edges)
    for group in groups:
        groups[group]["count"] = sum(n["group"] == group for n in nodes.values())
        groups[group]["open"] = any(n["group"] == group and n.get("status") == "open" for n in nodes.values())
    analysis = {"scope": "Consistency and source-location checks on the declared mathematical dependency graph, not proof verification.",
                "nodes": len(nodes), "edges": len(edges), "component_edges": sorted(group_edges),
                "topological_order": order,
                "shared_prerequisites": sorted([{"id": n, "downstream": len(closure(n, outgoing))} for n in nodes], key=lambda x: (-x["downstream"], x["id"])),
                "source_sha256": hashes}
    analysis["source_sha256"]["papers/dependencies.json"] = hashlib.sha256(source.read_bytes()).hexdigest()
    data["analysis"] = analysis
    svg = svg_graph(groups, group_edges)
    html = HTML.replace("__SVG__", svg).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("<", "\\u003c"))
    destination = ROOT / "docs/papers"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "dependencies.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    (destination / "dependency-analysis.json").write_text(json.dumps(analysis, indent=2) + "\n")
    (destination / "dependencies.svg").write_text(svg + "\n")
    (destination / "dependencies.html").write_text(html)
    print(f"Recorded {len(nodes)} statements and {len(edges)} direct uses in {len(groups)} components; both graphs are acyclic.")


if __name__ == "__main__":
    main()
