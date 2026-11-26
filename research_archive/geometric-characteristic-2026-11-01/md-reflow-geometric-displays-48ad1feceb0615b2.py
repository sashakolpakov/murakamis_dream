from pathlib import Path
import re,json,hashlib
p=Path('/private/tmp/murakamis_dream-publication/notes/actual_all_circle_geometric_characteristic.md');s=p.read_text();old=s
bodies={
'C0':r'''\begin{gathered}
 t=M+M^{-1},\quad D=M^2+M^{-2}=t^2-2,\\
 \beta=Q+Q^{-1},\quad\gamma=P+P^{-1},\\
 A_0=X+X^{-1},\quad S=\beta+\gamma+t^2.
 \end{gathered}''',
'C7':r'''\begin{gathered}
 c=\frac{M\mathcal X+M^{-1}q-2t}{D-p},\qquad
 d=\frac{q-M^2-1+hc}{p-2},\\
 e=\mathcal X-1-M^{-2}-hc,\qquad
 C=\begin{pmatrix}c&d\\e&t-c\end{pmatrix}.
 \end{gathered}''',
'R2':r'''\begin{gathered}
 u=\log M,\quad q=\log Q,\quad p=\log P,\quad z=\log X,\\
 f=\frac{M^2-X}{1-M^2X},\quad
 \rho_Q=\frac{Q+X}{1+QX},\quad
 \rho_P=\frac{P+X}{1+PX}.
 \end{gathered}'''}
def norm(t):
 t=re.sub(r'\\(?:begin|end)\{gathered\}|\\(?:quad|qquad)|\\\\|\s+','',t)
 return t
for tag,new in bodies.items():
 matches=[m for m in re.finditer(r'\\\[(.*?)\\\]',s,re.S) if r'\tag{'+tag+'}' in m.group(1)]
 assert len(matches)==1
 m=matches[0];prior=re.sub(r'\\tag\{[^}]*\}','',m.group(1));assert norm(prior)==norm(new),(tag,prior,new)
 s=s[:m.start()]+'\\[\n '+new+'\n \\tag{'+tag+'}\n\\]'+s[m.end():]
w=Path('/Users/sasha/volume-conjecture/notes/actual_all_circle_geometric_characteristic.md');assert w.read_text()==old
p.write_text(s);w.write_text(s)
Path('/private/tmp/md-geometric-display-reflow.json').write_text(json.dumps({'old_sha256':hashlib.sha256(old.encode()).hexdigest(),'new_sha256':hashlib.sha256(s.encode()).hexdigest(),'reflowed_tags':list(bodies),'formula_changes':False},indent=2)+'\n')
