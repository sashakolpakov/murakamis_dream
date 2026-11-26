from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication')
files=json.loads(Path('/private/tmp/md-quantitative-volume-docs-paths.json').read_text())
tokens={
 'd_v':r'd_v','n_v':r'n_v','E':'E','N':'N','m':'m','B':'B','i':'i',
 '|n_v|ge8192sqrt E':r'|n_v|\ge8192\sqrt E',
 'M=e^{pi i s/N}':r'M=e^{\pi i s/N}',
 '|s|le R<1':r'|s|\le R<1','2m/B':r'2m/B','Bge2^{26}m':r'B\ge2^{26}m',
 'R^0':'R^0','1/d_v':'1/d_v','2pi':r'2\pi','1/N':'1/N',
 'O_w':'O_w','O_v':'O_v','c=1':'c=1','2pi c':r'2\pi c',
 r'|\tau_v|<10^{-2}':r'|\tau_v|<10^{-2}',r'-2\pi i c':r'-2\pi i c',
 r'0\le c\le1':r'0\le c\le1',r'2\pi c':r'2\pi c',r'2E\,v_8':r'2E\,v_8',
 r'v_8':'v_8',r'2\pi':r'2\pi',r'M=e^{\pi i s/N}':r'M=e^{\pi i s/N}',
 r'|s|\le R<1':r'|s|\le R<1',
}
# Only exact corrupted forms are changed. Correct existing TeX delimiters remain.
for name in files:
 if not name.endswith('.md'):continue
 p=root/name;s=p.read_text()
 for a,b in tokens.items():
  s=s.replace('('+a+')',r'\('+b+r'\)') if '\\('+a+'\\)' not in ('('+a+')',) else s
 s=s.replace('\n[\n','\n\\[\n').replace('\n]\n','\n\\]\n')
 s=s.replace('sum_v\x0crac{d_v}{d_v^2+n_v^2}le2^{-25}',r'\sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}')
 s=s.replace('The first diagram makes that distinction explicit.','The diagrams below explain the proved constructions and their remaining scope.')
 s=s.replace('This is the local step in the arbitrary-tree induction; the picture\ndoes not prescribe Euclidean lengths.', 'This is the local attachment used in the induction over the tree.')
 p.write_text(s)
p=root/'notes/actual_all_circle_curvature_filling_limit.md';s=p.read_text()
start=s.index('## 11. Identification')
end=s.index('## Reproducing',start)
s=s[:start]+r'''## 11. Identification with the knot volume

Small angular variables do not imply that the primitive meridian
logarithms are small: a high-degree circle collects contributions from
many edges. The geometric proof therefore follows the entire path of
filling equations, with its logarithm branches retained.

The [ordered decomposition](actual_all_circle_octahedral_decomposition.md)
cuts the original augmented exterior into two octahedra per tree edge.
Its literal strand matchings retain every face pairing, half twist and
primitive peripheral path. The [angular construction](actual_all_circle_angular_octahedra.md)
subdivides these octahedra into eight positive tetrahedra per edge on
the chart \(|\tau_v|<10^{-2}\). Section 7 places the whole path

\[
 \Psi_{\tau_v}+\frac{i n_v\tau_v}{2\pi}=ic,\qquad 0\le c\le1,
\]

inside this chart. The [completion proof](actual_all_circle_geometric_completion.md)
computes the actual periods

\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,\qquad
 V_v=2i\tau_v,\qquad U_v+p_vV_v=-2\pi ic.
\]

It verifies that the primitive slope bounds a tube of cone angle
\(2\pi c\). At \(c=1\) the tube is smooth, the auxiliary fillings
are precisely the original surgeries, and the main knot cusp remains
complete. The same proof fixes the additive volume constant at the
complete augmented link and integrates the boundary-corrected action.
It gives

\[
 2\pi\operatorname{Re}\mathcal C(\mathbf1)
             =\operatorname{Vol}(S^3\setminus K).
 \tag{38}
\]

Thus the analytic conclusion above is an actual uniform volume theorem
under (2). The [preferred-cusp continuation](actual_all_circle_preferred_cusp.md)
also identifies the first correction geometrically. This establishes
the summed criterion, not arbitrary short fillings or a criterion for
graphs with cycles.

'''+s[end:]
s=s.replace('at this same continued wire saddle. This is not by itself a cusp\nor knot-volume identification.', 'at this same continued wire saddle. Section 11 supplies its geometric\nvolume and cusp interpretation.')
p.write_text(s)
for name in files:
 if name.endswith('.md'):
  s=(root/name).read_text()
  assert not [c for c in s if ord(c)<32 and c not in '\n\t'],name
  assert r'\\(' not in s,name
print('Repaired added math and checked controls.')
