from pathlib import Path
import re

src=Path('/private/tmp/md-star-absolute-cap-pressure-algebraic-holonomy.md').read_text()
math=[
r'''\mathcal F(z,w)=\sum_tQ_t(L)-\sum_{i\in I}w_i.\tag{1}''',
r'''\begin{aligned}
\operatorname{rec}(v)
 &=\sum_t\frac12\max_{f\in\operatorname{supp}t}v_f-\sum_{i\in I}v_i\\
 &=\sum_t\left[\frac12\max_{f\in\operatorname{supp}t}v_f
     -\sum_{f\in\operatorname{supp}t}\alpha^0_{t,f}v_f\right].
\end{aligned}\tag{2}''',
r'''\mathcal F(z,w)\ge c\lVert w\rVert-C(1+|z|).\tag{3}''',
r'''F_{\mathrm{cl}}(z)=\min_w\mathcal F(z,w).\tag{4}''',
r'''F_\mu(z)=M_{\mathrm{cap}}+\int_{[0,1]}
 \log(1-p+pe^z)\,d\mu_D(p).\tag{5}''',
r'''F_{\mathrm{cl}}(z)=F_\mu(z)\qquad(z\in\mathbb R).\tag{6}''',
r'''\begin{aligned}
F_{\mathrm{cl}}(z)&=\max_{0\le s\le1}\{R(s)+sz\},\\
R(s)&=\inf_{z\in\mathbb R}\{F_{\mathrm{cl}}(z)-sz\}.
\end{aligned}\tag{7}''',
r'''\begin{aligned}
\mu_D(\{1\})&=\lim_{z\to-\infty}F_{\mathrm{cl}}'(z)=0,\\
1-\mu_D(\{0\})&=\lim_{z\to+\infty}F_{\mathrm{cl}}'(z)=1.
\end{aligned}\tag{8}''',
r'''\begin{gathered}
T_t^2=ab+ac+bc,\qquad T_t>0,\\
Z_{t,f}=\frac{T_t+iL_f}{T_t-iL_f}
       =\exp(2\pi i\alpha_{t,f}).
\end{gathered}\tag{9}''',
r'''\prod_{t\ni f}Z_{t,f}=1\qquad(f\in I).\tag{10}''',
r'''B_D(w)=\prod_{t\ni A}Z_{t,A}
        =\exp(2\pi i m_D(w)).\tag{11}''',
r'''\mathcal A_D(w,B_D(w))=0.\tag{12}''',
r'''m_D(w)=\int_{(0,\infty)}\frac{w}{w+r}\,d\sigma_D(r).\tag{13}''',
r'''B_D(w)=\exp(2\pi i m_D(w)),\qquad 0<|B_D(w)|<1.\tag{14}''',
r'''\operatorname{Im}m_D(-r_0+iy)\ge\frac{ar_0}{y},\qquad
 |B_D(-r_0+iy)|\le\exp\!\left(-\frac{2\pi ar_0}{y}\right).\tag{15}''',
r'''\frac{d\sigma_D(r)}{dr}
 =\frac{\operatorname{Im}m_D(-r+i0)}{\pi r}
 =-\frac{\log|B_D(-r+i0)|}{2\pi^2r}.\tag{16}''',
r'''\frac{d\mu_D(p)}{dp}
 =-\frac{\log\left|B_D\!\left(-\frac{1-p}{p}+i0\right)\right|}
          {2\pi^2p(1-p)},\qquad 0<p<1.\tag{17}''',
r'''df_D=m_D(w)\frac{dw}{w}
 =\left[\frac{\operatorname{Log}B_D(w)}{2\pi i}
       +\text{the retained integer}\right]\frac{dw}{w}.\tag{18}''',
r'''\begin{gathered}
q(z)=\frac2\pi\operatorname{Ti}_2(e^{z/2}),\qquad
q'(z)=\frac{\arctan(e^{z/2})}{\pi},\\
\operatorname{Ti}_2(x)=\int_0^x\frac{\arctan t}{t}\,dt.
\end{gathered}\tag{19}''',
r'''\Phi_D-M_{\mathrm{cap}}
 =\inf_{z\in\mathbb R}\{f_D(e^z)+q(z)-z\}.\tag{20}''',
r'''B_{\mathrm{cap}}(w)=\frac{1+i\sqrt w}{1-i\sqrt w},\qquad
 a_{\mathrm{cap}}(w)=\frac{\arctan\sqrt w}{\pi}.\tag{20a}''',
r'''B_D(w_*)B_{\mathrm{cap}}(w_*)=1,\qquad
 m_D(w_*)+a_{\mathrm{cap}}(w_*)=1.\tag{20b}''',
r'''\Phi_D=M_{\mathrm{cap}}+C_0
 +\int_1^{w_*}\bigl[m_D(w)+a_{\mathrm{cap}}(w)-1\bigr]\frac{dw}{w}.
\tag{20c}''',
r'''-\chi_D=\sup_{r>0}\{U(r)-\max(0,\log r)\}.\tag{21}''',
r'''\sup_{r>0}\{\operatorname{Re}f_D(-r+i0)-\log_+r\}
 \le\inf_{z\in\mathbb R}\{f_D(e^z)+q(z)-z\}.\tag{22}''',
]
blocks=list(re.finditer(r'(?:^    .*(?:\n|$))+',src,re.M))
assert len(blocks)==len(math)==25
for b,m in reversed(list(zip(blocks,math))):
    src=src[:b.start()]+'\\[\n'+m+'\n\\]\n'+src[b.end():]
src=src.replace('31 October 2026. Private analytical draft for independent review.',
'''31 October 2026. **Internally reviewed analytical research theorem.**
Unpublished. The original source boundary curve has an atom-free,
log-algebraic pressure-root density and an exact selected logarithmic
period equal to the original **drilled** hyperbolic volume. No filled
quantum limit or ordinary knot A-polynomial identification is asserted.''')
src=src.replace('in research_cap_root_measure_from_classical_pressure.',
'''in [the original pressure/root-measure theorem](research_cap_root_measure_from_classical_pressure.md).''')
src=src.replace('the geometric double gives', 'the geometric double gives')
src=src.replace('The geometric double gives',
'''The [one-cap geometric double](research_one_cap_geometric_double.md) gives''')
src=src.replace('Gaussian-rational', 'Gaussian-rational')
start=src.index('## Inputs / status')
src=src[:start]+'''## Inputs and internal review

The [original effective-response theorem](research_global_cap_effective_response_criterion.md),
sections 1–3, supplies the local complex pressure germ and the grounded
ordinary graph. The [pressure/root-measure theorem](research_cap_root_measure_from_classical_pressure.md),
sections 1–2 and 6, supplies the same original odd-level measure and the
exact negative-axis supremum rates. The
[constrained cap capacity](research_cap_constrained_capacity_budget.md),
sections 1–2, retains the original targets and compact concave duality.
The [triangle entropy theorem](actual_triangle_entropy_algebraic_balance.md)
fixes the half-supply normalization and local Legendre potentials.
The [complete packing capacity](actual_smoothed_source_capacity_blocks.md)
identifies the selected complete value with the original drilled volume.
The [one-cap original chain budget](research_one_cap_original_chain_volume_budget.md)
supplies the still separate geometric upper bound discussed after (22).

The root independently reviewed all sections, including the final
complete-cap closure (20a)–(20c): PASS. Coherent independently reviewed
sections 1–2 in full: PASS. Cluster independently reviewed sections 3–5
in full, including the algebraic branch, density, endpoint integrability,
selected primitive and complete-volume closure: PASS. The complementary
independent reviews cover the whole proof. These are internal analytical
and original-source reviews, not external peer review.

Preservation changes mathematical formatting and supplies durable links.
No numerical audit, signed coefficient lower asymptotic, arbitrary complex
saddle continuation, knot A-polynomial identification, or general filled
volume theorem is claimed. Inequality (22) remains open.
'''
assert '/private/' not in src and '/Users/' not in src
out=Path('/Users/sasha/volume-conjecture/notes/research_cap_algebraic_boundary_curve_and_volume_period.md')
assert not out.exists()
out.write_text(src)
print(out)
