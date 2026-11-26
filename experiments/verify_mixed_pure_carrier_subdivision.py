#!/usr/bin/env python3
"""Exact checks for the pure-carrier mixed rational word.

The diagram faces, cubic arithmetic, cusp completeness and rational angle
bounds are checked here, without using a numerical hyperbolic solver.
The recorded local moves are replayed by the inspectable t3mlite routines.
Run with .venv/bin/python; requires sympy and the installed SnapPy package.
"""
from __future__ import annotations

import collections
import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s
from spherogram import Crossing, Tangle, OneTangle, MinusOneTangle, InfinityTangle
from snappy.exterior_to_link.mcomplex_with_memory import McomplexWithMemory
from snappy.snap.t3mlite import Mcomplex
from snappy.snap.t3mlite.arrow import Arrow

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "repro/fixtures/research-mixed-pure-carrier-subdivision.json"
DATA = json.loads(FIXTURE.read_text())
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output",type=Path,default=ROOT/"repro/results/research-mixed-pure-carrier-subdivision.json")
ARGS=parser.parse_args()
X = s.Symbol("X")
POLY = X**3 + 2*X**2 + 1
CHECKS = collections.Counter()


def reduced(expr):
    num, den = s.fraction(s.cancel(expr))
    return s.rem(s.rem(num, POLY, X) * s.invert(s.rem(den, POLY, X), POLY, X), POLY, X)


def equal(a, b=0, category="algebra"):
    assert reduced(a-b) == 0, (a, b)
    CHECKS[category] += 1


def diagram_faces(pd):
    """Four tetrahedra per crossing, as in the diagram crossing-ball proof."""
    ends = collections.defaultdict(list)
    for c, row in enumerate(pd):
        for j, arc in enumerate(row):
            ends[arc].append((c, j))
    assert all(len(es) == 2 for es in ends.values())
    neighbors = [[None]*4 for _ in range(4*len(pd))]
    for c in range(len(pd)):
        for j in range(4):
            neighbors[4*c+j][0] = 4*c+3-j
            neighbors[4*c+j][1] = 4*c+(j ^ 1)
    for es in ends.values():
        for (c, j), (d, k) in [es, es[::-1]]:
            neighbors[4*c+(j+1)%4][2] = 4*d+(k+2)%4
            neighbors[4*c+(j+2)%4][3] = 4*d+(k+1)%4
    return [[ns, [[0, 1, 3, 2] for _ in range(4)]] for ns in neighbors]


def face_data(T):
    T.rebuild()
    faces = [14, 13, 11, 7]
    return [[[tet.Neighbor[f].Index for f in faces],
             [list(tet.Gluing[f].tuple()) for f in faces]] for tet in T]


raw = diagram_faces(DATA["pd"])
assert raw == DATA["raw_gluing"]
CHECKS["diagram_faces"] = 4*len(raw)
# Relabel the four signed crossing tetrahedra from crossing_fundamental_cycle.
# This calibrates the raw numbering and records its global orientation sign.
old_to_new=[0,3,1,2]
vertex_maps=[[1,3,2,0],[1,2,3,0],[1,2,3,0],[1,3,2,0]]
for i,fi,j,fj in [(0,0,2,0),(1,0,3,0),(0,3,1,3),(2,3,3,3)]:
    pi,pj=vertex_maps[i],vertex_maps[j]
    newperm=[pj[pi.index(v)] for v in range(4)]
    assert newperm==[0,1,3,2]
    assert pi[fi]==pj[fj]
    a0,b0=old_to_new[i],old_to_new[j]
    assert raw[a0][0][pi[fi]]==b0
    CHECKS["crossing_ball_relabelling"]+=1
slots=[[(0,2),(2,2)],[(1,2),(3,2)],[(2,1),(3,1)],[(0,1),(1,1)]]
for old_slot,new_slot in zip(slots,[3,1,0,2]):
    actual={(old_to_new[i],vertex_maps[i][f]) for i,f in old_slot}
    assert actual=={((new_slot+1)%4,2),((new_slot+2)%4,3)}
    CHECKS["crossing_ball_relabelling"]+=1
orientation=[]
for sign,perm in zip([-1,1,1,-1],vertex_maps):
    inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    orientation.append(sign*(-1)**inversions)
assert orientation==[-1]*4
negative_tets=[1,2,0,3]
negative_vertices=[[1,2,3,0],[1,3,2,0],[1,3,2,0],[1,2,3,0]]
for i,fi,j,fj in [(0,0,2,0),(1,0,3,0),(0,3,1,3),(2,3,3,3)]:
    pi,pj=negative_vertices[i],negative_vertices[j]
    assert [pj[pi.index(v)] for v in range(4)]==[0,1,3,2]
    assert pi[fi]==pj[fj]
    assert raw[negative_tets[i]][0][pi[fi]]==negative_tets[j]
    CHECKS["negative_crossing_ball_relabelling"]+=1
for old_slot,new_slot in zip(slots,[3,1,2,0]):
    actual={(negative_tets[i],negative_vertices[i][f]) for i,f in old_slot}
    assert actual=={((new_slot+1)%4,2),((new_slot+2)%4,3)}
    CHECKS["negative_crossing_ball_relabelling"]+=1
negative_orientation=[]
for sign,perm in zip([1,-1,-1,1],negative_vertices):
    inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    negative_orientation.append(sign*(-1)**inversions)
assert negative_orientation==[-1]*4

# The four additional crossings draw the crossing-circle oval: it is over
# both vertical strands along its top arc and under both along its bottom.
cross = [Crossing("aux"+str(j)) for j in range(4)]
cross[3][3]=cross[0][0]
cross[2][3]=cross[1][0]
cross[0][3]=cross[3][0]
cross[0][1]=cross[1][3]
cross[1][1]=cross[2][2]
cross[2][0]=cross[3][2]
aug=Tangle(2,cross,[(cross[3],1),(cross[2],1),(cross[0],2),(cross[1],2)])
def crossing_word(n):
    word=InfinityTangle()
    for _ in range(abs(n)):
        word=(OneTangle() if n>0 else MinusOneTangle())*word
    return word
turn=lambda word:word.rotate(-1)
pendant=turn(turn(crossing_word(2))*crossing_word(-2))
original=(pendant*aug).braid_closure()
assert [list(row) for row in original.PD_code()] == DATA["pd"]
CHECKS["literal_word_PD"] = 1
T = McomplexWithMemory(raw)
collapse_count=0
for move, edge, face, index in DATA["moves"]:
    T._relabel_tetrahedra()
    arrow = Arrow(edge, face, T[index])
    if move == "smash_star":
        T.rebuild()
        e = arrow.Tetrahedron.Class[edge]
        assert e.distinct() and e.Vertices[0] != e.Vertices[1]
        assert sorted(v.link_genus() for v in e.Vertices) == ([0,0] if collapse_count==0 else [0,1])
        collapse_count+=1
        assert T.smash_star(e)
    else:
        e=arrow.Tetrahedron.Class[edge]
        expected_valence={"two_to_zero":2,"three_to_two":3,"four_to_four":4}[move]
        assert e.IntOrBdry=="int" and e.valence()==expected_valence and e.distinct()
        if move=="two_to_zero":
            left,right=e.Corners
            assert left.Tetrahedron.Class[15^left.Subsimplex] != right.Tetrahedron.Class[15^right.Subsimplex]
            for corner in e.Corners:
                assert sum(n in (left.Tetrahedron,right.Tetrahedron)
                           for n in corner.Tetrahedron.Neighbor.values())==2
        assert getattr(T, move)(arrow, must_succeed=True)
    CHECKS["recorded_local_moves"] += 1
assert face_data(T) == DATA["minimal_gluing"]

# Independently check every face of the recorded relabelling to the eight-tet
# complex. This does not use an isometry finder or a census identification.
iso = DATA["isomorphism_to_eight"]
for t, (ns, ps) in enumerate(DATA["minimal_gluing"]):
    dest, perm = iso[t]
    assert sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2==0
    for f in range(4):
        target, target_perm = iso[ns[f]]
        n, p = DATA["eight_gluing"][dest]
        assert n[perm[f]] == target
        assert [p[perm[f]][perm[v]] for v in range(4)] == [target_perm[ps[f][v]] for v in range(4)]
        CHECKS["relabelled_faces"] += 1

T = Mcomplex(DATA["eight_gluing"])
ti,fmask=DATA["final_move"]
assert T[ti].Neighbor[fmask] is not T[ti]
assert T.two_to_three(fmask,T[ti],must_succeed=True)
T.rebuild()
final_iso=DATA["final_isomorphism"]
for t,(ns,ps) in enumerate(face_data(T)):
    dest,perm=final_iso[t]
    assert sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2==0
    for f in range(4):
        target,target_perm=final_iso[ns[f]]
        dn,dp=DATA["nine_gluing"][dest]
        assert dn[perm[f]]==target
        assert [dp[perm[f]][perm[v]] for v in range(4)]==[target_perm[ps[f][v]] for v in range(4)]
        CHECKS["final_relabelled_faces"]+=1
CHECKS["final_two_to_three"]=1
NINE=Mcomplex(DATA["nine_gluing"])
assert sorted(v.link_genus() for v in NINE.Vertices)==[1,1,1]
CHECKS["torus_links"]=3

# Relative to the accepted odd gluing exactly two shaded pairs change.
oddpath=ROOT/"repro/fixtures/research-mixed-two-crossing-subdivision.json"
odd=json.loads(oddpath.read_text())
expected=json.loads(json.dumps(odd["nine_gluing"]))
for t,f,n,perm in [(3,1,5,[0,2,1,3]),(0,1,1,[3,0,1,2])]:
    expected[t][0][f]=n;expected[t][1][f]=perm
    nf=perm[f];inverse=[perm.index(i) for i in range(4)]
    expected[n][0][nf]=t;expected[n][1][nf]=inverse
assert expected==DATA["nine_gluing"]
CHECKS["pure_face_repairing"]=4

# Cubic shape field and the source-to-word character identity.
Y = 1+2*X+2*X**2
z = 1+1/X
equal(X**2*Y-X, (1-X)**3)
equal((1-X*Y)*(1+Y)**2, (1-Y)**4)
R = lambda a,b,c: (a,c,8-a*c-b)
RI = lambda a,b,c: (a,8-a*b-c,b)
TURN = lambda a,b,c: (b,a,8-a*b-c)
traces = (z, s.Integer(2), 4-z)
for op in (R,R,TURN,RI,RI,TURN):
    traces = tuple(reduced(t) for t in op(*traces))
equal(traces[0], -2, "marked_word")
equal(traces[1], 2*(3*Y**2-2*Y+3)/(Y+1)**2, "marked_word")
equal(traces[2], 2*(9*Y**2+2*Y+1)/(Y+1)**2, "marked_word")

a = 1-1/X
b = X*(1-X)
c = ((Y-1)/(Y+1))**2
l = (Y+1)/2
k = 2*Y/(Y+1)
shapes = [sum(s.Rational(q)*X**i for i,q in enumerate(cs)) for cs in DATA["shape_coefficients"]]
expected = [(k-1)/k, (k-1)/k, c, 1/(1-l), (b-1)/b, l, b, 1/(1-a), (a-1)/a]
# k and (Y-1)/(2Y) are cyclic shape companions; the first two entries are
# represented by 1/(1-k), rather than (k-1)/k.
expected[0] = expected[1] = 1/(1-k)
for left,right in zip(shapes,expected):
    equal(left,right,"shape_identification")

# The two new shaded face maps are the literal pure leaf maps S,S#.
rho=(Y+1)**2/(4*Y)
plus=s.Matrix([[Y+1,-Y-1],[2,-2*Y]])
minus=s.Matrix([[Y+1,-Y-1],[2*Y,-2]])
S=s.Matrix([[0,-Y*rho],[1,-1-Y]])
Ssharp=s.Matrix([[0,-rho/Y],[1,-1-1/Y]])
for frame,map_,shift in [(plus,S,1-Y),(minus,Ssharp,1-1/Y)]:
    actual=(frame.inv()*map_*frame).applyfunc(reduced)
    expected=s.Matrix([[1,shift],[0,1]])
    residual=(actual*expected.inv()).applyfunc(reduced)
    equal(residual[0,1],0,"pure_shaded_maps")
    equal(residual[1,0],0,"pure_shaded_maps")
    equal(residual[0,0],residual[1,1],"pure_shaded_maps")

# Exact field selection of the complete cap character. Both cubics are
# irreducible by the rational-root test; discriminant -59 is not a square.
zvar=s.Symbol("z")
f=zvar**3-3*zvar**2+5*zvar-2
g=zvar**2-5*zvar+7
assert all(POLY.subs(X,q)!=0 for q in [1,-1])
assert all(f.subs(zvar,q)!=0 for q in [1,-1,2,-2])
assert s.discriminant(f,zvar)==-59
assert s.discriminant(g,zvar)==-3
assert s.discriminant(POLY,X)==-59
equal(f.subs(zvar,1+1/X))
equal(1/(z-1),X)
CHECKS["cap_field_selection"]=7

# Five-term certificate of the Bloch--Wigner identity. Each triple below is
# the right side of D(u)+D(v)=D(uv)+D(u(1-v)/(1-uv))+D(v(1-u)/(1-uv)).
Z = X**2/(1-b)
w = (1-X)**2/(1-b)
triples = [
    (X,1-X,(b,Z,w)),
    (b,1-Z,(X*w,c/(c-1),(Y-1)/Y)),
    (X,w,(X*w,1/Y,(X*Y-1)/(X*Y))),
    (l,k,(Y,s.Rational(1,2),Y/(1+Y))),
    (Y,Y,(Y**2,Y/(1+Y),Y/(1+Y))),
]
for u,v,rhs in triples:
    for left,right in zip((u*v,u*(1-v)/(1-u*v),v*(1-u)/(1-u*v)),rhs):
        equal(left,right,"five_term_arguments")

params = [reduced(q) for zz in shapes for q in (zz,1/(1-zz),(zz-1)/zz)]
# Reconstruct the edge exponents from the gluing, independently of the
# stored equation array.
parents={}
def find_edge(e):
    parents.setdefault(e,e)
    if parents[e]!=e: parents[e]=find_edge(parents[e])
    return parents[e]
def join_edges(a,b): parents[find_edge(a)]=find_edge(b)
for t,(ns,ps) in enumerate(DATA["nine_gluing"]):
    for face in range(4):
        for a0,b0 in itertools.combinations([i for i in range(4) if i!=face],2):
            join_edges((t,a0,b0),(ns[face],*sorted((ps[face][a0],ps[face][b0]))))
edge_parameters={(0,1):0,(2,3):0,(0,2):1,(1,3):1,(0,3):2,(1,2):2}
edge_rows={}
for t in range(9):
    for edge in itertools.combinations(range(4),2):
        row=edge_rows.setdefault(find_edge((t,*edge)),[0]*27)
        row[3*t+edge_parameters[edge]]+=1
assert sorted(edge_rows.values())==sorted(DATA["nine_gluing_equations"][:9])
CHECKS["reconstructed_edge_equations"]=9
for row in DATA["nine_gluing_equations"]:
    product = s.Integer(1)
    for p,e in zip(params,row):
        product = reduced(product*p**e)
    equal(product,1,"edge_and_peripheral_products")

# Stronger than checking two chosen cusp curves: check the linear similarity
# holonomy on EVERY cycle of each triangulated cusp's dual graph.
def cusp_coordinates(zz,v):
    return [{1:0,2:1,3:zz}, {0:0,2:1,3:1/zz},
            {0:0,1:-1,3:1/(zz-1)}, {0:0,1:-1/zz,2:1/(1-zz)}][v]

potentials = {}
for t in range(9):
    for v in range(4):
        if (t,v) in potentials:
            continue
        potentials[t,v] = s.Integer(1)
        queue = collections.deque([(t,v)])
        while queue:
            i,w0 = queue.popleft()
            ns,ps = DATA["nine_gluing"][i]
            for face in range(4):
                if face == w0:
                    continue
                n,p = ns[face],ps[face]
                aa,bb = [j for j in range(4) if j not in (face,w0)]
                ci,cn = cusp_coordinates(shapes[i],w0),cusp_coordinates(shapes[n],p[w0])
                ratio = reduced((cn[p[bb]]-cn[p[aa]])/(ci[bb]-ci[aa]))
                target = (n,p[w0])
                wanted = reduced(potentials[i,w0]*ratio)
                if target not in potentials:
                    potentials[target] = wanted
                    queue.append(target)
                else:
                    equal(potentials[target],wanted,"all_cusp_similarity_cycles")

# Rational interval arithmetic for positive shapes and exact 2pi edge winding.
class I:
    def __init__(self,a,b=None): self.a,self.b=Q(a),Q(a if b is None else b)
    def __add__(self,o):
        if not isinstance(o,I): o=I(o)
        return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return I(-self.b,-self.a)
    def __sub__(self,o): return self+-asI(o)
    def __rsub__(self,o): return asI(o)+-self
    def __mul__(self,o):
        o=asI(o); vals=[x*y for x in (self.a,self.b) for y in (o.a,o.b)]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o); assert o.a*o.b>0
        return self*I(1/o.b,1/o.a)
    def __pow__(self,n):
        assert n>=0
        v=I(1)
        for _ in range(n): v=v*self
        return v

def asI(o): return o if isinstance(o,I) else I(o)
def atan_small(q):
    if q<0: return -atan_small(-q)
    assert q<=Q(1,2)
    total=sum((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(40))
    return I(total,total+q**81/Q(81))

# Machin's identity follows by twice applying the tangent double-angle
# formula to atan(1/5), then subtracting atan(1/239); the result is pi/4
# in (0,pi/2). Its alternating rational bounds certify this enclosure.
PI = 16*atan_small(Q(1,5))-4*atan_small(Q(1,239))

def atan(q):
    if q<0: return -atan(-q)
    if q>1: return PI/2-atan(1/q)
    return atan_small(Q(1,2))+atan_small((2*q-1)/(q+2))

alpha=I(Q(102784715200295,10**15),Q(102784715200296,10**15))
f=lambda q:8*q*(1+q)**2-1
assert f(alpha.a)<0<f(alpha.b)
beta=I(Q(665456951152810,10**15),Q(665456951152820,10**15))
assert beta.a**2<(4*alpha+3*alpha**2).a
assert beta.b**2>(4*alpha+3*alpha**2).b

def interval_complex(poly):
    co=[Q(str(s.expand(poly).coeff(X,i))) for i in range(3)]
    return co[0]+co[1]*alpha+co[2]*(alpha**2-beta**2), co[1]*beta+2*co[2]*alpha*beta

arguments=[]
for zz in params:
    real,imag=interval_complex(zz)
    assert imag.a>0
    ratio=real/imag
    angle=PI/2-I(atan(ratio.a).a,atan(ratio.b).b)
    arguments.append(angle)
    CHECKS["positive_shape_parameters"]+=1
edge_intervals=[]
for row in DATA["nine_gluing_equations"][:9]:
    angle=sum(e*a for e,a in zip(row,arguments))
    # Its exact product is one. This interval contains only one multiple
    # of 2pi, namely 2pi; no floating point angle is used in this inference.
    assert Q(6)<angle.a<angle.b<Q(7)
    scale=10**12
    edge_intervals.append([str(Q(angle.a*scale//1,scale)),
                           str(Q(-((-angle.b*scale)//1),scale))])
    CHECKS["exact_edge_winding"]+=1

report={"status":"passed","checks":dict(CHECKS),
        "raw_crossing_orientation_relative_to_signed_shadow_block":orientation,
        "raw_negative_crossing_orientation_relative_to_signed_shadow_block":negative_orientation,
        "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fixture_sha256":hashlib.sha256(FIXTURE.read_bytes()).hexdigest(),
        "edge_argument_intervals_radians":edge_intervals,
        "scope":"Literal pure-carrier PD, local triangulation moves, positive complete nine-tetrahedron geometry, exact pure shaded pairing maps, cap-field selection, and regulator identity. No quantum asymptotic is inferred from these checks."}
out=ARGS.output
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({"status":report["status"],"checks":report["checks"]},indent=2))
