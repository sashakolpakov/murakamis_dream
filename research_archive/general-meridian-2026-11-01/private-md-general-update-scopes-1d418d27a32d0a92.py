from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication'); before=Path('/private/tmp/md-general-public-before');changed=[]
def save(rel,s):
 p=root/rel
 if p.read_text()==s:return
 b=before/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 p.write_text(s);changed.append(rel)
def para(s,start,new):
 a=s.index(start);b=s.find('\n\n',a)
 if b<0:b=len(s)
 return s[:a]+new+s[b:]
def block(s,start,end,new):
 a=s.index(start);b=s.index(end,a);return s[:a]+new+'\n\n'+s[b:]
rel='notes/actual_main_meridian_grouped_wire_packet.md';s=(root/rel).read_text()
s=para(s,'First, the grouped component induction',r'''First, the [general component comparison](actual_main_meridian_general_component_comparison.md) gives a fixed loss for every nonempty multiplication correction and every high component-boundary contribution. Its clean term uses complete tensors and retains all internal indices in their complete support. The estimate applies to the actual fixed crossing \(R_s^n\) in place of \(R_s^\epsilon L_j\): a fixed power and its inverse have polynomial spectral norm on \(|s|\le R<1\), and the actual decorated extractor produces the required low/high coefficient cone. Inherited full-cone losses pass through the component by homogeneity in its boundary constants. The finite minimum of the structural gaps is positive. Prefactors may depend on the fixed powers; these exponential losses do not.''')
s=para(s,'For the remaining contraction,',r'''For the remaining contraction, the component boundary indices are low and every bare tensor is complete. Its positive resolution gives a coefficientwise majorant with the original boundary profiles; a spectral norm is not substituted for that comparison. At a circle vertex and for any low product \(E\), the actual fixed-power trace has the same-level bound''')
s=para(s,'Complete bare tensors have the positive expansion',r'''Complete bare tensors have the positive expansion (10). Together with (18), the clean component comparison bounds the remaining contraction by a polynomial times the original pure positive reference. An edge assignment outside the neighborhood in (13) misses its unique optimizer and has a fixed action loss. This proves the off-edge-window estimate before any circle contour is moved.''')
s=s.replace('At the other allowed vertices, the regular bare estimate is','At every nonexceptional vertex, the local replacement used by the component theorem has the regular estimate')
s=s.replace('Multiplying out the finitely many errors in (19), and using (18) and the positive reference, bounds their total by', 'These finitely many local replacements are already included in the grouped component error. Equivalently, multiplying them out with (18) and the positive reference bounds their total by')
save(rel,s)
rel='notes/actual_main_meridian_filled_volume.md';s=(root/rel).read_text()
s=s.replace('Use (18) to multiply out the finitely many replacements (20), and then localize the positive binary-resolution variables. The result is one fixed source error', 'The general component comparison includes the local replacements (20). Together with (18) and localization of the positive binary-resolution variables, it gives one fixed source error')
# Add the intrinsic topological transport consequence without changing the strict-source ledger.
s += r'''

## 10. Net twists and other Conway closures

The same intrinsic conclusions hold for the presentations admitted by the [ordered net-twist reduction](actual_conway_net_twist_volume.md) and the [arbitrary-closure reduction](actual_conway_arbitrary_closure_volume.md). These reductions use actual ambient isotopies of the tangles, including the recorded endpoint orders and rotations. A net twist is the signed sum attached to one surviving block of the original twist boxes; large opposite signs in that block can cancel.

For a fixed ordered cylindrical input, apply its deterministic reduction. If the output is a strict knot presentation and every surviving net twist is sufficiently long, the uniform volume limit (6), nonvanishing, and intrinsic cusp expansion (7b) hold for the input knot. For an input with either the cylindrical or cap closure, zero net weights may also be removed by the prescribed topological reduction. If the input is hyperbolic and every surviving strict factor has sufficiently long net twists, the reduction theorem shows that exactly one strict knot factor remains and all other factors are unknots. The input is ambient isotopic to that strict knot.

Here is why this transfers the whole meridian family. Orient the strict knot by the transported orientation of the input, and use zero framing on both. The reduced ADO invariant is the same Laurent family \(F_N(M)\) under this ambient isotopy, not merely the same value at \(M=1\). Any ribbon twist introduced in a diagram calculation is canceled by the full twist scalar at color \(d+s\). The meridian and the preferred zero-linking longitude are transported as well. The complete hyperbolic volume and the preferred cusp shape therefore agree. Applying (6) and (7b) to the strict representative proves those same formulas for the input.

There are finitely many reduced outputs for a fixed input expression, including its parity and zero-weight branches. Take the maximum of their strict-presentation thresholds and of the hyperbolicity thresholds used in the topological reduction. This gives one net-twist threshold independent of the later radius \(R<1\). All net weights and their zero relations stay fixed before \(N\) tends to infinity.

The presentation-dependent scalar \(a(D)\) and the individual physical-edge cotangents may be computed on the strict representative. No equality between the raw scalar ledgers, auxiliary circle sources, or augmented complements of two different presentations is needed. The transferred statements use the zero-framed invariant and the intrinsic preferred-cusp formula (7b).
'''
save(rel,s)
rel='notes/actual_main_meridian_preferred_cusp.md';s=(root/rel).read_text()
s=para(s,'The preceding geometry applies to', 'The geometry above and the [filled meridian-profile theorem](actual_main_meridian_filled_volume.md) apply to every fixed strict Conway construction under the stated knot, marking and long-twist hypotheses. The [general component comparison](actual_main_meridian_general_component_comparison.md) removes the former adjacency, valence and path restrictions from the analytic theorem.')
a=s.find('An entirely trivalent connected component is allowed')
if a>=0:
 b=s.index('Fix a presentation in this analytic class',a);s=s[:a]+s[b:]
s=s.replace('Fix a presentation in this analytic class','Fix such a strict presentation')
s=s.replace('The cotangent identity itself does not require the separated-bare or component-path conditions used in the newer analytic source estimates.','The calculation uses no analytic source-growth assumption. The general source theorem now has the same strict-tree scope under its separate long-twist hypotheses.')
s=para(s,'The implication in this section uses two separate established inputs:', 'The implication uses the moving asymptotic and the independent geometric translation identity proved above. The geometric proof determines the actual preferred cusp; the analytic proof determines the quantum correction. Neither statement identifies a classical factor of a quantum annihilator.')
s=s.replace('The additional analytic hypothesis is stated there; the geometric proof does not require it.','Its long-twist analytic hypotheses are stated there; the geometric calculation is proved directly from the marked representation.')
save(rel,s)
rel='notes/actual_main_meridian_exact_scalar.md';s=(root/rel).read_text()
# Replace only any old scope paragraph, retaining the physical proof verbatim.
for p in s.split('\n\n'):
 if 'trivalent' in p and 'component' in p:
  s=s.replace(p,'The [general filled-meridian theorem](actual_main_meridian_filled_volume.md) uses this exact scalar for every fixed strict Conway knot presentation with independently sufficiently long signed twists. Its analytic proof now permits arbitrary bare components. The scalar identity itself follows from the finite crossing and duality calculation above.')
save(rel,s)
# Clearly preserve earlier valid special-case arguments.
for rel in ['notes/actual_main_meridian_source_bounds.md','notes/actual_main_meridian_auxiliary_color_gap.md']:
 s=(root/rel).read_text();parts=s.split('\n\n')
 if parts[1].startswith('The [trivalent-component extension]'):
  parts[1]='The [general component theorem](actual_main_meridian_general_component_comparison.md) extends this result to every fixed strict Conway tree. The proof below establishes the original separated-junction case and its physical input estimates. The general theorem retains the same invariant, normalization and radius restrictions.'
 else:parts.insert(1,'The [general component theorem](actual_main_meridian_general_component_comparison.md) extends the source and auxiliary-color estimates to arbitrary bare components, with their existing radius restrictions. The argument below remains the earlier special-case proof.')
 save(rel,'\n\n'.join(parts))
for rel in ['notes/actual_main_meridian_component_extension.md','notes/actual_main_meridian_trivalent_component_bound.md','notes/actual_main_meridian_trivalent_filled_volume.md']:
 s=(root/rel).read_text();a=s.index('\n\n')
 notice='This special-case argument is retained in full. The [general component theorem](actual_main_meridian_general_component_comparison.md) and [filled-meridian theorem](actual_main_meridian_filled_volume.md) now permit every fixed strict bare component, without an additional valence or path condition.'
 s=s[:a+2]+notice+'\n\n'+s[a+2:];save(rel,s)
Path('/private/tmp/md-general-scope-paths.json').write_text(json.dumps(changed,indent=2)+'\n')
print('Updated',len(changed),'scope and proof pages.')
