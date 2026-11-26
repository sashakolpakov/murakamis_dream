from pathlib import Path
import json
import re
import subprocess

root = Path('/private/tmp/murakamis_dream-publication')
tmp = Path('/private/tmp')
stem = 'actual_uniform_filling_supremum_bound'
note = (tmp/'md-undecorated-cancellation-uniform-filling-norms.md').read_text()
note = note.replace('# Uniform finite norms for the original filling functionals',
                    '# Uniform bounds for inserting twist powers')
old = note.split('\n\n', 2)[1]
note = note.replace(old, r'''The finite formula for a diagram can be organized in two steps. First, take the prescribed coefficient in its shared face variables. This gives a polynomial \(S_N\) in one spectral variable for each crossing region. Then apply a linear functional in each spectral variable to insert the chosen signed twist power.

This note bounds the second step. Inserting \(n\) crossings costs at most \(1+|n|/2\) in the supremum norm on the real spectral interval, independently of the quantum level \(N\). There is a stronger estimate for the two one-sided pieces of the local polynomial: their values vanish at all spectral nodes, and the cost is then at most \((N-1)/N\), independently of \(n\) as well. The derivatives at repeated nodes remain in the calculation.

The estimate applies after the face coefficient has been taken. All crossing regions therefore retain their common face constraints. To obtain a volume theorem from it, one must still bound this shared polynomial and prove that the geometric contribution survives.''', 1)
note = note.replace('For \\(r\\) ports,', 'For \\(r\\) crossing regions,')
note = note.replace('with \\(J\\) its one-sided ports.', 'with \\(J\\) its one-sided crossing regions.')
note = note.replace('every original LEFT/RIGHT sector',
                    'each term containing a specified lower or upper one-sided factor')
note = note.replace('the original LEFT and RIGHT numerators',
                    'the original lower and upper one-sided numerators')
note = note.replace('Every LEFT entry', 'Every lower one-sided entry')
note = note.replace('the same statement for RIGHT', 'the same statement for the upper piece')
note = note.replace('LEFT and RIGHT have the factor (21), and FULL is the sum of CROSS, LEFT and RIGHT, with the central odd row assigned to CROSS.',
    'the lower and upper pieces have the factor (21). The full numerator is the sum of those pieces and the central crossing piece, denoted CROSS in the source formulas. At odd levels the central row belongs to that crossing piece.')
note = note.replace('md-undecorated-cancellation-audit-uniform-filling-norms.py',
                    'experiments/audit_actual_uniform_filling_supremum_bound.py')
note += r'''

## 7. The estimate needed for long fillings

It is useful to state the remaining comparison with its quantifiers. Fix the diagram, and write
\[
 \mathcal D_N=S_{N,\mathrm{full}}-S_{N,\mathrm{CROSS}}.
\]
This polynomial does not depend on the twist powers. Suppose one proves, for some fixed \(\eta>0\),
\[
 \|\mathcal D_N\|_{[-2,2]^r}
       \le \exp\bigl(N(\Phi-\eta)+o(N)\bigr).
 \tag{26}
\]
Here \(\Phi\) is the complete augmented action in the normalization of the source. When it is identified geometrically, \(\Phi=\operatorname{Vol}(M_{\mathrm{aug}})/(2\pi)\).

For each fixed tuple \(\boldsymbol n\), equation (4) then gives
\[
 \left|\left(\bigotimes_e\mathcal L_N^{n_e}\right)\mathcal D_N\right|
       \le \exp\bigl(N(\Phi-\eta)+o(N)\bigr).
 \tag{27}
\]
The finite factor in (4) is absorbed in \(o(N)\); this argument does not claim uniformity in twist powers growing with \(N\).

Suppose separately that the crossing contribution has a nonzero asymptotic
\[
 Z_{N,\mathrm{CROSS}}(\boldsymbol n)
       =a_N\exp(N\mathcal A_{\boldsymbol n}),\qquad
       N^{-1}\log|a_N|\longrightarrow0,
 \tag{28}
\]
where \(\Re\mathcal A_{\boldsymbol n}>\Phi-\eta\). Equations (27) and (28) show that the complementary contribution divided by the crossing contribution tends to zero exponentially. Consequently
\[
 \lim_{N\to\infty}N^{-1}\log|Z_N(\boldsymbol n)|
       =\Re\mathcal A_{\boldsymbol n}.
 \tag{29}
\]
The subexponential normalization factors in section 1 preserve this limit. Identifying \(2\pi\Re\mathcal A_{\boldsymbol n}\) with the hyperbolic volume still requires the geometric filling argument for that diagram.

This implication explains why a strict gap in (26) is useful for sufficiently long fixed fillings. The desired filled action approaches the augmented action as the auxiliary fillings become long. A bound for the full twist-independent polynomial at the augmented rate alone would give only that larger rate; it would not prove the smaller filled volume. The norm theorem proves the passage from (26) to (27). It does not prove (26) or supply (28) for a new diagram.
'''
(root/'notes'/f'{stem}.md').write_text(note)
script = (tmp/'md-undecorated-cancellation-audit-uniform-filling-norms.py').read_text()
script = script.replace("default=Path.cwd()", "default=Path(__file__).resolve().parents[1]")
script = script.replace("'md-undecorated-cancellation-uniform-filling-norms-results.json'",
                        "'actual_uniform_filling_supremum_bound_results.json'")
(root/'experiments'/f'audit_{stem}.py').write_text(script)

groups_path=root/'repro/research_check_groups.json'
groups=json.loads(groups_path.read_text())
assert all(g['name']!='filling-supremum' for g in groups['groups'])
groups['groups'].append(dict(
    name='filling-supremum',
    description='Exact Chebyshev residues, finite derivative interpolation, and original signed crossing matrices for the level-uniform filling bound. The norm inequalities are proved in the text.',
    commands=[['python3',f'experiments/audit_{stem}.py']]))
groups_path.write_text(json.dumps(groups,indent=2)+'\n')

catalog_path=root/'book/catalog.json'
catalog=json.loads(catalog_path.read_text())
catalog[stem]=['Source and transport','Finite norm theorem; shared source estimate remains']
catalog_path.write_text(json.dumps(catalog,indent=2)+'\n')
collections_path=root/'book/collections.json'
collections=json.loads(collections_path.read_text())
entry=next(c for c in collections
           if 'actual_spectral_total_derivative_source' in c['notes'])
entry['notes'].append(stem)
collections_path.write_text(json.dumps(collections,indent=2)+'\n')

frontier=root/'book/chapters/frontier.md'
text=frontier.read_text()
needle='\n\nThe volume limit is proved for fixed ordered cylindrical'
assert needle in text
paragraph=r'''

### What remains after the finite filling estimate

The [uniform filling estimate](../../notes/actual_uniform_filling_supremum_bound.md)
separates two parts of the calculation. After taking the common face
coefficient, let \(S_N(\sigma_1,\ldots,\sigma_r)\) be the resulting
spectral polynomial. Applying the original twist functionals gives
\[
 |Z_N(\boldsymbol n)|
 \le \prod_{e=1}^r(1+|n_e|/2)\,
                       \|S_N\|_{[-2,2]^r}.
\]
The diagram and twist powers are fixed, so this factor adds no
exponential growth as \(N\) increases. The proof retains derivatives
at double spectral roots and the simple endpoint at odd levels.

For a term containing a one-sided local factor, that coordinate costs
at most \((N-1)/N\), independently of its twist power. The full
complementary polynomial vanishes on the product of the spectral
node sets. This yields a bound without first taking the absolute
value of each local path.

The missing estimate concerns the supremum of that shared
complementary polynomial: it must lie strictly below the augmented
geometric rate. Such a gap would make it negligible beside a
separately established nonzero geometric term for sufficiently long
fixed fillings. The full spectral polynomial is independent of the
twists; bounding it at the augmented volume alone cannot prove the
smaller filled volume. Thus the finite norm result simplifies the
remaining estimate without adding a new knot family to the volume
theorems.
'''
frontier.write_text(text.replace(needle,paragraph+needle,1))

repro_text=r'''
## Uniform bounds for inserting twists

With SymPy and NumPy installed, run:

~~~sh
python3 repro/run_research_checks.py filling-supremum
~~~

The program checks the finite derivative interpolation formula in
cyclotomic fields, the repeated and simple Chebyshev residues, and the
reconstruction of positive and negative powers of the original crossing
matrices. It also checks the lower-block numerator derivatives against
the corresponding spectral projectors. The [proof](LINK)
establishes the norm bounds for every level. The finite checks do not
estimate a volume limit.

'''
for name,link in [('repro/README.md','../notes/'+stem+'.md'),
                  ('book/chapters/audits.md','../../notes/'+stem+'.md')]:
    path=root/name
    text=path.read_text()
    first,rest=text.split('\n',1)
    path.write_text(first+'\n\n'+repro_text.replace('LINK',link)+rest.lstrip('\n'))

# Preserve the mathematical displays and give every equation a unique label.
body=note.split('\n',1)[1]
body=re.sub(r'\]\(([^):]+\.md)(#[^)]*)?\)',
            lambda m:'](https://sashakolpakov.github.io/murakamis_dream/notes/'
            +m[1][:-3]+'.html'+(m[2] or '')+')',body)
body=re.sub(r'^## \d+\. ',r'## ',body,flags=re.M)
result=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash',
                       '-t','latex','--top-level-division=chapter'],
                      input=body,text=True,capture_output=True,check=True)
assert not result.stderr,result.stderr
latex=result.stdout
def equation(m):
    expr=m[1]
    tag=re.search(r'\\tag\{(\d+)\}',expr)
    if not tag:
        return m[0]
    expr=re.sub(r'\s*\\tag\{\d+\}', '', expr)
    return '\\begin{equation}\\label{uf:eq-'+tag[1]+'}\n'+expr.strip()+'\n\\end{equation}'
latex=re.sub(r'\\\[(.*?)\\\]',equation,latex,flags=re.S)
latex=re.sub(r'\((\d+)\)',lambda m: r'\eqref{uf:eq-'+m[1]+'}',latex)
latex=re.sub(r'\\label\{(?!uf:)([^}]+)\}',r'\\label{uf:sec-\1}',latex)
latex='\\chapter{Uniform bounds for inserting twist powers}\n\\label{app:uniform-filling-bound}\n\n'+latex
(root/'manuscript/sections/N-uniform-filling-bound.tex').write_text(latex)
main=root/'manuscript/main.tex'
text=main.read_text()
needle='\\input{sections/M-directed-all-orders}\n'
assert needle in text
main.write_text(text.replace(needle,needle+'\\input{sections/N-uniform-filling-bound}\n'))
repro=root/'manuscript/sections/09-reproduction.tex'
with repro.open('a') as f:
    f.write(r'''

\section{Uniform bounds for inserting twists}
Appendix~\ref{app:uniform-filling-bound} proves a level-independent
bound for each original filling functional, measured against the
supremum of the shared spectral polynomial. Its finite identities
can be checked with one command:
\begin{verbatim}
python3 repro/run_research_checks.py filling-supremum
\end{verbatim}
This group requires SymPy and NumPy. It checks the derivative
interpolation and Chebyshev residues exactly, then compares the
functional with independently constructed signed crossing matrices
over finite fields. The shared exponential estimate remains a
separate hypothesis; these checks add no new volume class.
''')
print('Prepared finite norm note, appendix, guide explanation, and reproduction group.')
