"""Original numerator supports versus exact bounded-flow and affine-cut tests.

These finite checks do not prove the entropy limit or its volume comparison.
"""
import argparse
import itertools
import json
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces
from audit_actual_gaussian_resolvent_numerator_and_cap import finite_H
from audit_actual_small_circle_polynomial_face_insertion import Local

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_fejer_shared_entropy_variational_results.json'))
args=parser.parse_args()
counts=defaultdict(int)

def data(chart, states, m):
    R=len(states); F=chart['faces']; d=2*m-1
    supply=[d]*R
    demand=[0 if f in (0,chart['v']) else d for f in range(F)]
    cap=defaultdict(int)
    for e,(faces,state) in enumerate(zip(chart['circles'],states)):
        for pos,f in enumerate(faces):
            low=m if (state==1 and pos==2) or (state==2 and pos==1) else 0
            high=m-1 if state==0 and pos in (1,2) else d
            supply[e]-=low;demand[f]-=low
            cap[e,f]+=high-low
    return supply,demand,cap

def feasible(chart, states, m):
    supply,demand,cap=data(chart,states,m)
    if min(supply+demand+list(cap.values()))<0:return False
    R=len(states);F=chart['faces'];S=R+F;T=S+1
    residual=defaultdict(int);adj=defaultdict(set)
    def add(u,v,c):
        residual[u,v]+=c;adj[u].add(v);adj[v].add(u)
    for e,c in enumerate(supply):add(S,e,c)
    for (e,f),c in cap.items():add(e,R+f,c)
    for f,c in enumerate(demand):add(R+f,T,c)
    value=0
    while True:
        prev={S:None};queue=deque([S])
        while queue and T not in prev:
            u=queue.popleft()
            for v in adj[u]:
                if v not in prev and residual[u,v]>0:prev[v]=u;queue.append(v)
        if T not in prev:break
        v=T;amount=sum(supply)
        while prev[v] is not None:amount=min(amount,residual[prev[v],v]);v=prev[v]
        v=T
        while prev[v] is not None:
            u=prev[v];residual[u,v]-=amount;residual[v,u]+=amount;v=u
        value+=amount
    return value==sum(supply)

def cut_values(chart,states,m):
    supply,demand,cap=data(chart,states,m)
    yield from supply;yield from demand;yield from cap.values()
    R=len(states);F=chart['faces']
    for aa in range(1<<R):
        A=[e for e in range(R) if (aa>>e)&1]
        sa=sum(supply[e] for e in A)
        for bb in range(1<<F):
            val=sum(demand[f] for f in range(F) if (bb>>f)&1)-sa
            val+=sum(c for (e,f),c in cap.items() if ((aa>>e)&1) and not((bb>>f)&1))
            yield val

def eventual(chart,states):
    bound=2;ok=True
    for b,v1 in zip(cut_values(chart,states,0),cut_values(chart,states,1)):
        a=v1-b;counts['exact_affine_cut_conditions']+=1
        if a<0 or (a==0 and b<0):ok=False
        elif a>0:bound=max(bound,(-b+a-1)//a)
    return ok,bound

def actual_support(chart,N):
    local=Local(N);H=finite_H(local,-2%local.p)
    d=N-1;m=N//2;F=chart['faces'];R=len(chart['circles'])
    target=tuple(0 if f in (0,chart['v']) else d for f in range(F))
    # These coefficients are the separately source-audited original V polynomial.
    assert len(H)==(N+2)*(N+1)*N//6
    counts['actual_local_numerator_coefficients']+=len(H)
    states={(tuple([0]*F),0)}
    for e,faces in enumerate(chart['circles']):
        choices=set()
        for degrees in H:
            label=1 if degrees[2]>=m else 2 if degrees[1]>=m else 0
            load=[0]*F
            for f,a in zip(faces,degrees):load[f]+=a
            if all(a<=b for a,b in zip(load,target)):choices.add((tuple(load),label))
        nxt=set()
        for old,code in states:
            for load,label in choices:
                new=tuple(a+b for a,b in zip(old,load))
                if all(a<=b for a,b in zip(new,target)):nxt.add((new,code+label*3**e))
        states=nxt
    return {code for load,code in states if load==target}

rows=[]
for k,word in ((2,[1,0,1]),(2,[1,0,2,1]),(3,[1,3,0,2,4,1,3])):
    chart=morse_faces(k,word);R=len(word)
    for N in (4,6):
        support=actual_support(chart,N)
        for states in itertools.product(range(3),repeat=R):
            code=sum(a*3**e for e,a in enumerate(states))
            assert feasible(chart,states,N//2)==(code in support),(k,word,N,states)
            counts['actual_marked_support_vs_flow']+=1
        rows.append({'width':k,'word':word,'N':N,'nonzero_path_assignments':len(support)})
    # All affine cuts at width two; a deterministic collection including
    # nonzero source patterns at width three, where the number of cuts is larger.
    patterns=list(itertools.product(range(3),repeat=R))
    if R>4:
        chosen=set(sorted(support)[:8]+[0,3**R-1,3**R//2])
        patterns=[tuple((code//3**e)%3 for e in range(R)) for code in sorted(chosen)]
    for states in patterns:
        ok,bound=eventual(chart,states)
        assert feasible(chart,states,5*R+1)==ok
        counts['explicit_single_level_certificates']+=1
        # Every affine constant has size bounded by this fixed network;
        # the comparison level also exceeds all recorded positive-slope roots.
        large=max(bound,4*(R+chart['faces'])+10)
        assert feasible(chart,states,large)==ok
        assert feasible(chart,states,large+1)==ok
        counts['eventual_cut_vs_integer_flow']+=2

out={'status':'PASS','counts':dict(counts),'original_marked_charts':rows,
     'scope':'Exact local numerator supports, original marked shared targets, bounded integer flow, and eventual affine-cut feasibility. Finite checks do not prove the entropy asymptotic, geometric maximum, or a Kashaev filling limit.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
