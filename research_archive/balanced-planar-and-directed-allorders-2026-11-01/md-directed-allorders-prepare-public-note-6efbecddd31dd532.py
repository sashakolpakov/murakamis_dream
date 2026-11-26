from pathlib import Path
import re,json,hashlib
src=Path('/private/tmp/md-directed-allorders-source-and-geometric-factor.md')
s=src.read_text()
s=s.replace('# All orders on shifted meridian charts under the directed circle-tree criterion','# All orders of the meridian profile under the directed criterion')
s=s.replace('This note proves an extension of the actual directed finite-source theorem. It does not obtain higher orders by differentiating its published first-order estimate. The argument repeats the exact normalized subtree induction with arbitrary finite asymptotic order, using its original positive exponential margins, and then identifies those coefficients by the canonical sine-factorial interpolation. The same proof works on every fixed finite collection of translated microscopic charts required by a fixed quantum recurrence.',
'The directed degree-and-twist criterion gives more than a leading volume limit. For every fixed knot presentation satisfying that criterion, the actual meridian state has an asymptotic expansion to every finite order on the microscopic scale \\(M=q_N^s\\). Its coefficients have a precise polynomial degree bound. This bound allows an exact quantum recurrence to select the preferred geometric meridian–longitude curve of the original knot complement.\n\nThe proof expands the actual normalized subtree integrals, retaining their full normal data and endpoint terms. It also works on the fixed translated parameter regions used by the recurrence. These are separate estimates from the previously established first-order profile.')
s=s.replace('murakamis_dream-publication/notes/actual_all_circle_directed_volume.md','actual_all_circle_directed_volume.md')
s=s.replace('The fixed Newton polynomials','The fixed Newton polynomials')
needle='For the fixed finite tree, the minimum of any finite list'
insert='Here the complete basis is \\(e_k(z)=S_k^{-2}\\prod_{j<k}(c_j-z)\\), with \\(S_k=\\prod_{r=1}^{k}2\\sin(\\pi r/N)\\), \\(c_j=2\\cos((2j+1)\\pi/N)\\), and \\(0\\le k<N\\). The paired factor is \\(W_k(s)=\\prod_{r=1}^{k}[1-\\sin^2(\\pi s/N)/\\sin^2(\\pi r/N)]\\). These are the [physical fixed-basis coordinates](actual_main_meridian_turn_comparison.md), including their repeated-node data.\n\n'
assert needle in s;s=s.replace(needle,insert+needle)
needle='Here \\(\\lambda_j(\\sigma)=(-1)^j q_N^{j(j+1)}(q_N^2)^{-\\sigma j}\\) is the stripped spectral value.'
replace='Here \\(t_j=q_N^{-2j-1+2\\sigma}\\), \\(c_j(\\sigma)=t_j+t_j^{-1}\\), and \\(P_\\sigma(z)=\\mathcal T_N(z)+2\\cos(2\\pi\\sigma)\\), where \\(\\mathcal T_N(t+t^{-1})=t^N+t^{-N}\\). The quantity \\(\\lambda_j(\\sigma)=(-1)^j q_N^{j(j+1)}(q_N^2)^{-\\sigma j}\\) is the stripped spectral value.'
assert needle in s;s=s.replace(needle,replace)
needle='Full canonical polynomial, real-sup and complete Hermite norms differ by polynomial factors in the fixed degree range.'
replace='The full complete Hermite norm is the maximum of the values at the distinct complete Casimir nodes and the first derivatives at their double nodes. At odd levels the final node \\(-2\\) is simple and has no derivative coordinate. This norm, the canonical polynomial sup norm and the Chebyshev coefficient norm differ by polynomial factors in the fixed degree range.'
assert needle in s;s=s.replace(needle,replace)
s=s.replace('## 9. Dependency audit and precise new input','## 9. Proof dependencies and scope')
s=s.replace('The directed theorem is used literally at the following points:','The [directed finite-source theorem](actual_all_circle_directed_volume.md) supplies the following inputs:')
s=s.replace('The exact interpolation theorem and regular-circle §10 fix','The [exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md) and [regular-circle calculation](actual_main_meridian_regular_circle_trace.md), §10, fix')
s=s.replace('The direct-crossing trace §§2–4 fixes','The [direct-crossing trace](actual_main_meridian_direct_crossing_trace.md), §§2–4, fixes')
s=s.replace('Source-bound (D9)–(D14) supplies','The [full source bounds](actual_main_meridian_source_bounds.md), (D9)–(D14), supply')
s=s.replace('The exact-scalar theorem fixes (20)','The [exact scalar calculation](actual_main_meridian_exact_scalar.md) fixes (20)')
s=s.replace('The existing filtered theorem supplies','The [filtered characteristic theorem](actual_main_meridian_filtered_characteristic.md) supplies')
s=s.replace('What is new here is the proof of its analytic hypotheses for the **directed** certificate:','Its analytic hypotheses for the directed certificate are proved here:')
s=s.replace('Finally the geometric-characteristic theorem §§5–10 supplies','Finally the [geometric-characteristic theorem](actual_all_circle_geometric_characteristic.md), §§5–10, supplies')
s=s.replace('This hypothesis is the genuine all-level source equation; an equation fitted to complete values or to finitely many jets is not enough.',
'This hypothesis is the genuine all-level source equation; an equation fitted to complete values or to finitely many jets is not enough. The existence of such fixed operators is proved by the [finite-sum annihilator theorem](finite_sum_annihilator.md), with its boundary terms retained.')
s=s.replace('The vertexwise geometric theorem supplies','The [vertexwise geometric theorem](actual_all_circle_vertexwise_geometry.md) supplies')
s=s.replace('The local rational reconstruction and longitude theorem are algebraic statements','The [local rational reconstruction and longitude theorem](actual_all_circle_geometric_characteristic.md) are algebraic statements')
s=s.replace('the new draft','this proof').replace('new draft','proof')
s=re.sub(r'^\* ', '', s, flags=re.M)
s=s.replace('The first Fourier coefficient is exactly one, at both parities.\nThe outgoing', 'The first Fourier coefficient is exactly one, at both parities.\n\nThe outgoing')
s=s.replace('There is no discarded term in this definition.\nAt a nonroot', 'There is no discarded term in this definition.\n\nAt a nonroot')
s=s.replace('not a new topological rerooting.\nThe conditional', 'not a new topological rerooting.\n\nThe conditional')
s=s.replace('Its physical sine amplitude is nonzero.\nRelative', 'Its physical sine amplitude is nonzero.\n\nRelative')
p=Path('/private/tmp/actual_all_circle_directed_all_orders.md');p.write_text(s)
norm=lambda x:re.sub(r'\s+','',x)
a=[norm(x) for x in re.findall(r'\\\[(.*?)\\\]',src.read_text(),re.S)]
b=[norm(x) for x in re.findall(r'\\\[(.*?)\\\]',s,re.S)]
assert a==b
print(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'display_formulas_preserved':len(a),'private_path_hits':re.findall(r'/private/\S+|/Users/\S+',s)},indent=2))
