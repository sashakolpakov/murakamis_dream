from collections import defaultdict

def ports(m,opposite=True):
    out=[]
    for j in range(m):
        if j%2:out.append((m,(j-1)%m,j,(j+1)%m))
        elif opposite:out.append((m+1,(j+1)%m,j,(j-1)%m))
    return out

def circuits(m,odd):
    ps=ports(m); at=defaultdict(list)
    for j,p in enumerate(ps):
        for k in range(4):at[tuple(sorted((p[k],p[(k+1)%4])))].append((j,k))
    assert all(len(v)==2 for v in at.values())
    adj=defaultdict(list)
    for a,b in at.values():adj[a].append(b);adj[b].append(a)
    for j in range(m):
        for a,b in ([(0,2),(1,3)] if j in odd else [(0,3),(1,2)]):
            adj[j,a].append((j,b));adj[j,b].append((j,a))
    seen=set();cc=[]
    for a in adj:
        if a in seen:continue
        path=[];prev=None;v=a
        while v not in seen:
            seen.add(v);path.append(v);w=next(w for w in adj[v] if w!=prev);prev,v=v,w
        cc.append(path)
    return cc
if __name__=='__main__':
 for m in range(4,34,2):
    rules={'none':set(),'all':set(range(m)),'north':set(range(1,m,2)),'south':set(range(0,m,2)),'one':{0},'allbutone':set(range(1,m)),'two':{0,1}}
    print(m,{k:len(circuits(m,v)) for k,v in rules.items()})
