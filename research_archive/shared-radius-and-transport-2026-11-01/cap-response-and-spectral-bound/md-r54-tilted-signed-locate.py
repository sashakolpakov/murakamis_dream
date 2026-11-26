from pathlib import Path
source=Path('/private/tmp/md-r54-boundary-response-locate.py').read_text()
exec(source[:source.index('\nweights={int')])
old=json.loads(Path('/private/tmp/md-r54-boundary-response-locate.json').read_text())
w=np.array([old['logs'][str(v)] for v in I])
rows=[]
for z in np.linspace(0,4,41):
 rr=root(lambda v:evaluate(z,v,False)[1][1:],w,jac=lambda v:evaluate(z,v,False)[2][1:,1:],tol=1e-11)
 w=rr.x
 f,g,H=evaluate(z,w)
 k=H[0,0]-H[0,1:]@np.linalg.solve(H[1:,1:],H[1:,0])
 row={'z':float(z),'F':float(f),'nu':float(g[0]),'kappa':float(k),'weighted_positive_rate':float(f-z/2),'weighted_squared_bound':float(f-z/2+.5*np.log(1-4*k)),'residual':float(max(abs(g[1:])))}
 rows.append(row)
out={'scope':'Exploratory floating-point pressure curve; no interval certificate.','rows':rows}
Path('/private/tmp/md-r54-tilted-signed-locate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'max_to_half_load':max(r['weighted_squared_bound'] for r in rows if r['nu']<=.5),'rows':rows[::5]},indent=2))
