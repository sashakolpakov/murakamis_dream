from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication'); before=Path('/private/tmp/md-general-public-before'); changed=[]
def save(rel,s):
 p=root/rel
 if p.exists() and p.read_text()==s:return
 b=before/rel
 if p.exists() and not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s);changed.append(rel)
def block(s,start,end,new):
 a=s.index(start);b=s.index(end,a);return s[:a]+new+'\n\n'+s[b:]
def para(s,start,new):
 a=s.index(start);b=s.find('\n\n',a)
 if b<0:b=len(s)
 return s[:a]+new+s[b:]
rel='notes/actual_main_meridian_filled_volume.md';s=(root/rel).read_text()
s=s.replace('For the class of presentations described below,','For every fixed strict Conway presentation described below,')
s=block(s,'There is a useful graph description','At circle \\(i\\)',r'''Group consecutive multiplications with no intervening turn into a product junction. Each edge of the resulting tree carries a physical quarter-turn. A junction containing an original crossing-circle operator is called a circle junction; a junction containing none is called bare. The theorem allows every finite connected group of bare junctions, with arbitrary valences at least three. There is no additional condition on their adjacency, number of attached branches, or path lengths.

The [general component comparison](actual_main_meridian_general_component_comparison.md) proves the estimate that permits this scope. For a fixed component, let \(\Omega_{\mathcal U}\) be its positive complete action after closing its output with the norm comparison. Replacing its moving multiplication tensors by complete tensors leaves a remainder \(E_{\mathcal U,N}\) satisfying
\[
 \|E_{\mathcal U,N}\|_{\mathcal J}
   \le \exp\{N(\Omega_{\mathcal U}-\eta_{\mathcal U}+o(1))\},
 \qquad \eta_{\mathcal U}>0.
 \tag{2}
\]
Here \(\mathcal J\) measures both values and first derivatives at the complete polynomial roots. The estimate retains the deformed edge factors and boundary arrays. It is a conclusion of the component proof, not an extra hypothesis on the presentation. The positive action uses
\[
 J(x)=\int_0^x\log(2\sin\pi u)\,du,\qquad
 g(x)=J(2x)-4J(x).
 \tag{3}
\]
The proof of (2) compares whole finite contractions. Reflecting one index in an error term can remove a turn in a positive comparison tree, whose pressure is no larger than the original pressure. These comparison trees do not replace the original diagram in the invariant or the geometric volume calculation.''')
s=s.replace('The geometric proof of (7a) applies to the broader strict-tree class; the asymptotic (7b) retains the component condition of this theorem.','The geometric identity (7a) and the asymptotic (7b) now apply to the same strict-tree class under the stated long-twist hypotheses.')
s=para(s,'The [component source theorem]',r'''The [general component theorem](actual_main_meridian_general_component_comparison.md), Sections 3–7, separates an outgoing branch into a contraction of complete tensors and a remainder with a strict loss in its full spectral norm. The complete contraction keeps the actual deformed edge factors, low boundary arrays and every internal index in the complete support. A decorated turn converts an incoming spectral error into the required low/high coefficient bounds. The component comparison then carries that loss through all internal turns by homogeneity in the boundary constants. It does not impose a new loss budget at each junction.

The new local ingredient is the [reflected Fourier estimate](actual_main_meridian_high_fourier_reflection.md). In the difference between a moving and a complete trace, the first Fourier term cancels. With one high index, the remaining terms are bounded by a complete tensor with that index reflected. Exact fusion turns this into a positive comparison tree. With several high indices, the [half-boundary comparison](actual_main_meridian_component_pressure.md) supplies a complete boundary state instead. A strict Fourier or boundary loss controls every nonempty correction pattern.''')
s=block(s,'Let \\(F_0\\) be the maximum','Use (18) to multiply out',r'''Let \(F_0\) be the maximum of the original complete positive action, so \(2\pi F_0=\operatorname{Vol}(Y)\) for the augmented exterior with crossing circles unfilled. The general component theorem controls the grouped corrections, high boundary contributions and the complement of the strict original window with a fixed loss below \(F_0\).

The [complete-edge theorem](actual_main_meridian_component_pressure.md) puts every physical internal label of a bare component strictly below half, except when the entire component consists of two trivalent junctions with two rigid branches at each. Its one internal label is exactly half. Every circle-incident label is in a compact subinterval of \((0,1/2)\). Hidden unturned indices used to resolve products retain their full strict intervals.

At a nonexceptional bare junction, the regular low trace theorem gives
\[
 \phi_\sigma\left(\prod e_{k_a}\right)
 =\phi_0\left(\prod e_{k_a}\right)
                   (1+O_R(e^{-\kappa N})).
 \tag{20}
\]
The incident labels are compactly inside the low range and their sum is greater than one. In the exceptional two-junction component, both tensors are cubic. On their old support the degree of \(e_i e_j e_k\) is less than \(2N-1\); division by \(P_0+\Delta_\sigma\) therefore leaves its top trace coefficient unchanged. Their moving and complete traces agree exactly, including indices crossing half in the retained neighborhood.''')
s=para(s,'The [earlier complete-value volume theorem]',r'''The [complete-value volume theorem](actual_conway_all_strict_tree_long_twist_volume.md) and the present moving-meridian theorem apply to the same fixed strict literal Conway trees, with their knot and long-filling hypotheses. The present result additionally gives a uniform complex profile, nonvanishing and the preferred-cusp correction. The earlier singleton, path and trivalent arguments remain valid special cases of the general component comparison.''')
s=para(s,'An entirely trivalent bare component is covered',r'''There is no remaining bare-component valence or path restriction. The filling integers must still be fixed before \(N\) tends to infinity and sufficiently long in the stated strict presentation. The theorem does not extend the ordinary-color-subtracted remainder through its resonance divisors, or identify a selected classical main-meridian \(A\)-factor. Those are separate problems.''')
s=para(s,'The global estimate begins with',r'''The global estimate uses [source growth near the complete main meridian](actual_main_meridian_source_bounds.md) for the physical leaf and decorated-turn inputs, and the [general component comparison](actual_main_meridian_general_component_comparison.md) for every connected group of bare junctions. Its [Fourier lemma](actual_main_meridian_high_fourier_reflection.md) and [positive-pressure lemmas](actual_main_meridian_component_pressure.md) control the complete correction patterns without discarding their internal correlations. The [regular bare trace](actual_main_meridian_regular_bare_trace.md) then applies on the original strict low windows, with exact cubic equality in the two-junction exception.''')
save(rel,s)
rel='notes/actual_main_meridian_grouped_wire_packet.md';s=(root/rel).read_text()
s=block(s,'For the global source-to-window statement','Put\n',r'''The global source-to-window statement applies to every finite bare component. The [general component theorem](actual_main_meridian_general_component_comparison.md) supplies a complete-tensor contraction and a grouped remainder satisfying
\[
 \|E_{\mathcal U,N}\|_{\mathcal J}
 \le e^{N(\Omega_{\mathcal U}-\eta_{\mathcal U}+o(1))},
 \qquad \eta_{\mathcal U}>0.
 \tag{1}
\]
It retains every internal complete-supported index and the actual deformed edge factors. The losses are fixed before the meridian disk radius and the fixed crossing powers.

The other inputs are the physical cones in the [source-bound theorem](actual_main_meridian_source_bounds.md), the [regular bare trace](actual_main_meridian_regular_bare_trace.md), the [regular circle trace](actual_main_meridian_regular_circle_trace.md), and the all-low fixed-power comparison in the [direct crossing trace](actual_main_meridian_direct_crossing_trace.md), Section 7. Grouped errors are controlled in the original filled scalar before contour deformation; only the retained finite packet is analytically continued in the angular variables.''')
s=block(s,'There are two kinds of edge regularity.','At a bare vertex,',r'''The [complete-edge theorem](actual_main_meridian_component_pressure.md) determines the regularity needed here. Circle-incident labels are strictly in \((0,1/2)\). Physical edges inside a bare component are also strictly below half, except when that component consists of two trivalent junctions with two rigid boundary branches at each. Its one internal label equals half. This follows by cutting an edge and comparing its two unturned profiles; it does not require a lower bound on the number of branches at a junction.

All internal indices remain in the finite sum. In the exceptional two-junction case the edge is allowed to cross half within a compact subset of \((0,1)\). Its two cubic traces agree exactly with their complete traces on the strict old support. Hidden unturned product indices retain their original strict bulk ranges in every component.''')
s=s.replace('Components using the old path estimate retain its stronger low internal window.','Every nonexceptional component also has its physical internal labels in a compact low interval.')
s=para(s,'The grouped component errors, high component-boundary', 'The grouped component errors and the original strict-window complement have a fixed loss by the [general component comparison](actual_main_meridian_general_component_comparison.md).') if 'The grouped component errors, high component-boundary' in s else s
s=s.replace('bare components outside the three alternatives in Section 1, or an arbitrary main-meridian ordinary-color subtraction','a fixed neighborhood in the meridian coordinate, or an arbitrary main-meridian ordinary-color subtraction')
save(rel,s)
rel='notes/actual_main_meridian_joint_filling_transform.md';s=(root/rel).read_text()
s=s.replace('the [component extension](actual_main_meridian_component_extension.md) supplies the grouped high-index error bound','the [general component theorem](actual_main_meridian_general_component_comparison.md) supplies the grouped error bound for arbitrary bare components')
s=s.replace('the [component extension](actual_main_meridian_component_extension.md), Section 6, supply (6)','the [general component theorem](actual_main_meridian_general_component_comparison.md), Sections 6–9, supply (6)')
s=block(s,'The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) supplies these interfaces','The lower bound on',r'''The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md), together with the [general component comparison](actual_main_meridian_general_component_comparison.md), supplies these interfaces for every fixed strict ordered Conway tree. It constructs the original primitive lattice and positive resolutions, proves (2), (7) and (8) with \(\nu=3(1-m)/2\), and proves the fixed grouped error (6).

There is no additional valence, adjacency or path condition on the bare junctions. For the fixed original knot and parity pattern, (37) and (41) therefore hold for every independently sufficiently long fixed signed filling. The original marked geometric calibration identifies the volume. The nonzero quantum lower bound is supplied by (34). The turn deletions used to estimate correction terms do not change this packet, its scalar factors or its filling action.''')
save(rel,s)
# Record all edits, to be combined with the later guide and installation steps.
Path('/private/tmp/md-general-core-paths.json').write_text(json.dumps(changed,indent=2)+'\n')
print(json.dumps({'changed':changed}))
