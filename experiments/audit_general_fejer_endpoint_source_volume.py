#!/usr/bin/env python3
"""Exact hybrid support tests on literal flat-plat identity smoothings."""
import argparse
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path
import sys

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces


class DSU:
    def __init__(self, values):
        self.p = {v: v for v in values}

    def root(self, v):
        while self.p[v] != v:
            self.p[v] = self.p[self.p[v]]
            v = self.p[v]
        return v

    def join(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        self.p[b] = a
        return True


def A(a, b):
    return ('A', min(a, b), max(a, b))


def smoothing(data, deleted):
    quads = data['circles']
    original = []
    for e, (x, b, c, y) in enumerate(quads):
        original += [(e, (x,b,y), (A(x,b),A(b,y),('M',e))),
                     (e, (x,y,c), (('M',e),A(y,c),A(c,x)))]
    all_edges = set(ed for _,_,es in original for ed in es)
    assert set(Counter(ed for _,_,es in original for ed in es).values()) == {2}
    vd, ed = DSU(range(data['faces'])), DSU(all_edges)
    for e in sorted(deleted):
        x,b,c,y = quads[e]
        if not vd.join(b,c):
            return None, 'identity_cycle'
        ed.join(A(x,b), A(x,c)); ed.join(A(y,b), A(y,c))
    marks = {vd.root(0), vd.root(data['v'])}
    if len(marks) != 2:
        return None, 'merged_protected_faces'
    faces = [(e, tuple(vd.root(v) for v in vs), tuple(ed.root(x) for x in es))
             for e,vs,es in original if e not in deleted]
    if not faces:
        return None, 'empty_remainder'
    if any(len(set(vs)) != 3 for _,vs,_ in faces):
        return None, 'loop_cellulation'
    occurrences = defaultdict(list)
    endpoints = {}
    for i,(_,vs,es) in enumerate(faces):
        for j,e in enumerate(es):
            pair = frozenset((vs[j], vs[(j+1)%3]))
            assert e not in endpoints or endpoints[e] == pair
            endpoints[e] = pair; occurrences[e].append(i)
    assert all(len(x)==2 for x in occurrences.values())
    vertices = set(v for _,vs,_ in faces for v in vs)
    assert marks <= vertices
    assert len(vertices)-len(occurrences)+len(faces) == 2
    assert any(endpoints[e] == marks and e[0]=='A' for e in occurrences)
    dual = nx.MultiGraph(); dual.add_nodes_from(range(len(faces)))
    for e,ij in occurrences.items():
        dual.add_edge(*ij, key=e)
    assert nx.is_connected(dual)
    ports = sorted(set(e for e,_,_ in faces))
    tris = {e: [i for i,(f,_,_) in enumerate(faces) if f==e] for e in ports}
    assert all(len(v)==2 for v in tris.values())
    ordinary = sorted(vertices-marks)
    assert len(ordinary)==len(ports)
    # Find actual cut disks from distinct dual edge pairs, not Hall subsets.
    by_pair = defaultdict(list)
    for e,pair in endpoints.items(): by_pair[pair].append(e)
    disks=[]
    for pair, edges in by_pair.items():
        for ea,eb in combinations(edges,2):
            assert ea[0]==eb[0], (ea,eb,'mixed-type digon')
            cut=dual.copy()
            cut.remove_edge(*occurrences[ea], key=ea)
            cut.remove_edge(*occurrences[eb], key=eb)
            comps=list(nx.connected_components(cut))
            assert len(comps)==2
            for part in comps:
                inside=set(v for i in part for v in faces[i][1])-set(pair)
                if inside & marks or not inside or inside==set(ordinary): continue
                assert len(part)==2*len(inside)
                assert not any(v in inside for i in set(range(len(faces)))-part for v in faces[i][1])
                disks.append((frozenset(inside), frozenset(part), (ea,eb)))
    return dict(faces=faces,ports=ports,tris=tris,ordinary=ordinary,marks=marks,
                disks=disks,quads={e:tuple(vd.root(v) for v in quads[e]) for e in ports}), None


def hybrid_nodes(chart, green):
    nodes=[]
    for e in chart['ports']:
        if e in green:
            nodes.append((('g',e),2,chart['quads'][e]))
        else:
            nodes += [(('c',i),1,chart['faces'][i][1]) for i in chart['tris'][e]]
    return nodes


def exact_flow(nodes, ordinary, required=None):
    G=nx.DiGraph(); source=('s',); sink=('t',)
    total=2*len(ordinary)
    for name,supply,vertices in nodes:
        G.add_edge(source,name,capacity=supply-(1 if required and required[0]==name else 0))
        for f in set(vertices)&set(ordinary):
            G.add_edge(name,('f',f),capacity=total)
    for f in ordinary:
        G.add_edge(('f',f),sink,capacity=2-(1 if required and required[1]==f else 0))
    return nx.maximum_flow_value(G,source,sink)==total-(1 if required else 0)


def check_chart(chart, green, counts, check_arcs):
    nodes=hybrid_nodes(chart,green); ordinary=chart['ordinary']; allset=set(ordinary)
    assert exact_flow(nodes,ordinary)
    counts['exact_integral_hybrid_flows']+=1
    permitted=[]
    for inside,part,edges in chart['disks']:
        crossing=[e for e in green if sum(i in part for i in chart['tris'][e])==1]
        if not crossing:
            permitted.append(inside)
            counts['permitted_actual_cut_disks']+=1
    tight=[]
    for mask in range(1,(1<<len(ordinary))-1):
        S={f for j,f in enumerate(ordinary) if mask>>j&1}
        C0=sum(bool(set(vs)&S) for _,vs,_ in chart['faces'])
        g=sum(sum(bool(set(chart['faces'][i][1])&S) for i in chart['tris'][e])==1 for e in green)
        CH=sum(supply for _,supply,vs in nodes if set(vs)&S)
        assert CH==C0+g and C0>=2*len(S)
        counts['exact_complete_and_hybrid_Hall_cuts']+=1
        if CH==2*len(S):
            tight.append(S)
            cover=set().union(*(set(T) for T in permitted if set(T)<=S))
            assert cover==S,(chart['quads'],green,S,permitted)
            counts['tight_sets_covered_by_actual_permitted_disks']+=1
    for T in permitted:
        assert sum(supply for _,supply,vs in nodes if set(vs)&set(T))==2*len(T)
    forced_by_hall=set(); forced_by_disks=set()
    for name,supply,vs in nodes:
        for f in set(vs)&allset:
            arc=(name,f)
            if any(f not in S and set(vs)&S for S in tight): forced_by_hall.add(arc)
            if any(f not in T and set(vs)&set(T) for T in permitted): forced_by_disks.add(arc)
            if check_arcs:
                assert exact_flow(nodes,ordinary,arc)==(arc not in forced_by_hall)
                counts['independent_positive_arc_maxflow_tests']+=1
    assert forced_by_hall==forced_by_disks
    counts['exact_forced_arc_set_comparisons']+=1
    counts['forced_ordinary_arcs']+=len(forced_by_hall)
    counts['hybrid_patterns']+=1


def run():
    counts=Counter(); reasons=Counter(); fixture_records=[]
    fixtures=[(2,[1,0,2,1]),(3,[1,3,0,2,4,1,3]),
              (4,[1,3,5,0,2,4,6,1,3,5])]
    for width,word in fixtures:
        data=morse_faces(width,word); R=len(word); valid=0
        selections=range(1<<R) if width<4 else [0]+[1<<j for j in range(R)]
        for mask in selections:
            deleted={j for j in range(R) if mask>>j&1}
            chart,reason=smoothing(data,deleted)
            if reason: reasons[reason]+=1; continue
            valid+=1; counts['literal_loopless_identity_smoothings']+=1
            ports=chart['ports']; r=len(ports)
            patterns=range(1<<r) if width<4 else sorted(set([0,(1<<r)-1]+[1<<j for j in range(r)]+[((1<<r)-1)^(1<<j) for j in range(r)]))
            for p in patterns:
                green={ports[j] for j in range(r) if p>>j&1}
                check_chart(chart,green,counts,check_arcs=(width<4 and p in (0,(1<<r)-1)))
        fixture_records.append(dict(width=width,word=word,loopless_smoothings=valid))
    return dict(status='PASS',arithmetic='Exact integer Hall counts and networkx integer-capacity max-flow',
        counts=dict(counts),excluded_smoothing_charts=dict(reasons),fixtures=fixture_records,
        scope='Literal flat-plat incidence, true identity smoothing, typed dual digon disks, hybrid Hall/forced-arc classification. No numerical volume or asymptotic proof is inferred.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('general_fejer_endpoint_source_volume_results.json'))
    args=parser.parse_args();result=run();args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
