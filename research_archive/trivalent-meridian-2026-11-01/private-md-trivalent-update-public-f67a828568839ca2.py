from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication');changed=set()
def edit(rel, old, new):
 p=root/rel;s=p.read_text();assert old in s,(rel,old[:110]);p.write_text(s.replace(old,new,1));changed.add(rel)
main='notes/actual_main_meridian_filled_volume.md'
edit(main,
'The theorem includes trees with no adjacent bare junctions. More generally, let \\(\\mathcal U\\) be a maximal connected component of bare junctions. A singleton component may have any allowed valence. For every nonsingleton component, let \\(b_v\\) be the number of incident boundary branches at its vertex \\(v\\), after the component\'s internal edges are removed. These are the rigid branches supplied by the neighboring circle-marked parts of the tree. Require \\(b_v\\ge5\\) and the finite path inequality',
r'''For each maximal connected component \(\mathcal U\) of bare junctions, require at least one of the following conditions:

- It consists of one junction, of any allowed valence.
- Every junction in it has valence three in the full reduced tree. Count both edges within the component and branches leading out of it. The number of junctions is any fixed finite number.
- It satisfies the path inequality below.

The second condition is proved by the [trivalent-component bound](actual_main_meridian_trivalent_component_bound.md) and its [global extension](actual_main_meridian_trivalent_filled_volume.md). It requires no lower bound on the number of outside branches. The vertices must be those of the actual reduced tree: splitting a higher-valence product into artificial binary products does not establish this condition.

For the third condition, let \(b_v\) be the number of incident boundary branches at vertex \(v\), after the component's internal edges are removed. These are the branches supplied by the neighboring circle-marked parts of the tree. Require \(b_v\ge5\) and''')
edit(main,
'A simpler sufficient condition is \\(b_v\\ge\\max(8,4|\\mathcal U|)\\) at every vertex of each nonsingleton component. Condition (2) controls the loss accumulated when an error passes through adjacent bare products. It is a condition on the fixed finite presentation, not on the level \\(N\\) or on a filling slope.',
'A simpler sufficient test for the third condition is \\(b_v\\ge\\max(8,4|\\mathcal U|)\\) at every vertex. Condition (2) controls accumulated errors in these components. Entirely trivalent components use the second condition instead. All three alternatives concern the fixed finite presentation; they do not depend on the level \\(N\\) or on a filling slope.')
edit(main,
'New high-state errors consume only the component path budget (2). This is why the condition is componentwise rather than a sum of all losses over the tree.',
'For components satisfying (2), newly created errors use that path budget. For an entirely trivalent component, the [simultaneous comparison](actual_main_meridian_trivalent_component_bound.md) instead bounds every extra cubic trace term by a boundary state of the same complete positive source. That boundary has a strict gap below the original maximum. The clean part keeps every old-supported internal index, including indices above one half; only its effective boundary and output indices are restricted to the low range.')
edit(main,
'The summed high-edge contribution and the complement of the original strict retained-edge window have a fixed loss below \\(F_0\\). The same statement holds after resolving complete bare vertices into their positive binary multiplication coefficients. On the regular retained window, every incident edge is in a fixed compact subinterval of \\((0,1/2)\\), and every bare vertex has incident sum greater than \\(1+\\delta\\). The [regular bare-tensor theorem](actual_main_meridian_regular_bare_trace.md) therefore gives',
r'''The grouped component errors, high component-boundary contributions, and the complement of the original strict window have a fixed loss below \(F_0\). Internal edges of a trivalent bare component remain unrestricted within their old support. At the maximizing state their labels lie in \((0,1)\); they need not lie below one half. Circle-incident labels are in a compact subinterval of \((0,1/2)\).

At every new trivalent vertex the three old pair sums are at most \(d\), so the degree of \(e_i e_j e_k\) is less than \(2N-1\). Write that product as \(P_0Q+R_0\), with \(\deg Q\le N-2\). Replacing the relation \(P_0\) by \(P_0+\Delta_\sigma\) changes the remainder to \(R_0-\Delta_\sigma Q\), without changing its coefficient of degree \(N-1\). Its trace is therefore exactly the complete trace on the old support. This also holds when one internal label exceeds one half.

For the other allowed components, the regular window retains the original compact low labels and incident-sum condition. The [regular bare-tensor theorem](actual_main_meridian_regular_bare_trace.md) gives''')
edit(main,
'This is exact at valence at most four. At larger fixed valence it follows from the strict Fourier-tail separation of regular low Newton products.',
'On those low windows, this is exact at valence at most four; at larger fixed valence it follows from strict Fourier-tail separation. At the new trivalent vertices the preceding polynomial division proves the exact equality on their full old support. Pre-existing higher-valence components retain their whole-hub majorant until this regular replacement; their moving trace is not prematurely expanded into individual errors.')
edit(main,
'the narrower class specified by the bare-component condition (2).',
'the narrower class specified by the three bare-component alternatives in Section 1.')
edit(main,
'No theorem for arbitrary adjacent bare components failing (2) is obtained.',
'An entirely trivalent bare component is covered without (2). Components containing adjacent higher-valence junctions remain outside the theorem unless they satisfy the stated path condition.')
edit(main,
'The [regular bare trace](actual_main_meridian_regular_bare_trace.md) then replaces moving bare tensors by their complete tensors on the strict window.',
'The [trivalent-component comparison](actual_main_meridian_trivalent_component_bound.md) covers arbitrary-size trivalent components. Its [global extension](actual_main_meridian_trivalent_filled_volume.md) traces the complete source and complex estimates while retaining their full internal labels. The [regular bare trace](actual_main_meridian_regular_bare_trace.md) supplies the other allowed components on their strict low windows.')
packet='notes/actual_main_meridian_grouped_wire_packet.md'
edit(packet,
'For the global source-to-window statement, a maximal bare component is either a singleton, or satisfies the path hypothesis of the [component extension](actual_main_meridian_component_extension.md). More explicitly, if \\(b_v\\) is its number of incident rigid boundary branches, assume \\(b_v\\ge5\\) and',
'For the global source-to-window statement, each maximal bare component is either a singleton, entirely trivalent in the full reduced tree, or satisfies the path hypothesis of the [component extension](actual_main_meridian_component_extension.md). The [trivalent extension](actual_main_meridian_trivalent_filled_volume.md) permits arbitrary fixed component size and retains all internal labels. For the path alternative, if \\(b_v\\) is the number of incident rigid boundary branches, require \\(b_v\\ge5\\) and')
edit(packet,
'The sufficient condition \\(b_v\\ge\\max(8,4|\\mathcal U|)\\) may be used. Singleton bare components use the existing arbitrary-valence theorem, not this sufficient numerical condition.',
'The sufficient condition \\(b_v\\ge\\max(8,4|\\mathcal U|)\\) may be used for the path alternative. Singleton and entirely trivalent components do not require this numerical condition. Trivalence counts all original incidences; an artificial binary resolution of a larger junction does not qualify.')
edit(packet,
'The local inputs are the [regular bare trace]',
'The new [trivalent comparison](actual_main_meridian_trivalent_component_bound.md) supplies the additional full-component bound and exact cubic trace replacement. The other local inputs are the [regular bare trace]')
old='All relevant complete retained edge labels are strictly in \\((0,1/2)\\). For separated bare vertices this is the original intrinsic-probe statement.'
new=r'''There are two kinds of edge regularity. A circle-incident label is strictly in \((0,1/2)\), by the original intrinsic-probe statement and the leaf boundary barrier. An edge inside a trivalent bare component is strictly in \((0,1)\); its complete maximizing label may equal or exceed one half. The full old support of these internal edges is retained. The [global trivalent proof](actual_main_meridian_trivalent_filled_volume.md) explains why this distinction suffices for the complex packet.

For separated bare vertices all retained labels are low.'''
edit(packet,old,new)
edit(packet,'For the additional components in (1), a bare–bare edge','For components satisfying the path condition (1), a bare–bare edge')
edit(packet,
'Consequently a fixed sufficiently small retained edge neighborhood has \\(x_e\\in[\\delta,1/2-\\delta]\\) and every bare incident sum at least \\(1+\\delta\\), for some \\(\\delta>0\\).',
'A sufficiently small retained-edge neighborhood therefore has all labels in \\([\\delta,1-\\delta]\\), all circle-incident labels in \\([\\delta,1/2-\\delta]\\), and every bare incident sum at least \\(1+\\delta\\), for some \\(\\delta>0\\). Components using the old path estimate retain its stronger low internal window.')
edit(packet,'every edge is regular low, and (13) holds throughout the box.',
'circle-incident edges are regular low, bare–bare edges stay in the interior of \\((0,1)\\), and (13) holds throughout the box.')
edit(packet,
'First, the grouped component induction gives a fixed loss for the summed high-edge part.',
'First, the grouped component induction gives a fixed loss for its error terms and for high component-boundary indices. In an entirely trivalent component, the error contains the extra cubic trace terms; the clean part retains all old-supported internal indices, including high ones. Thus no general loss is asserted for a high internal bare–bare edge.')
edit(packet,
'newly created high errors use (1).',
'new errors use (1) in the path class and the simultaneous comparison in the trivalent class.')
edit(packet,
'For the low sector, no spectral norm is substituted for a coefficientwise majorant.',
'For the remaining contraction, the component boundary indices are low. Trivalent bare tensors are already the positive complete tensors. Other allowed components use their whole-hub majorant before regular replacement. No spectral norm is substituted for that coefficientwise comparison.')
edit(packet,
'The all-parity whole-hub comparison and (18) therefore bound the low contraction by a polynomial times the **original** pure positive reference.',
'The all-parity whole-hub comparison for the old component class, the exact old tensors in the trivalent class, and (18) therefore bound the remaining contraction by a polynomial times the original pure positive reference.')
edit(packet,
'Inside that neighborhood, the regular bare estimate is',
r'''Inside that neighborhood, a trivalent bare trace is exactly unchanged. Indeed the old pair support gives \(i+j+k\le3d/2<2N-1\). In division by \(P_0\), the quotient has degree at most \(N-2\); the constant change \(P_0\mapsto P_0+\Delta_\sigma\) cannot change the remainder's coefficient of degree \(N-1\). Thus \(\phi_\sigma(e_i e_j e_k)=\phi_0(e_i e_j e_k)\), including the full internal label range.

At the other allowed vertices, the regular bare estimate is''')
# Later canonical edge insertion already explicitly permits full bulk; leave its proof intact.
scalar='notes/actual_main_meridian_exact_scalar.md'
edit(scalar,
'The moving theorem includes strict trees with no adjacent bare junctions, and the larger class satisfying the explicit finite component-path inequality in that theorem.',
'The moving theorem includes singleton bare components of any allowed valence, arbitrary-size components whose vertices all have valence three, and components satisfying its explicit finite path inequality. The [trivalent extension](actual_main_meridian_trivalent_filled_volume.md) counts valence in the full original reduced tree.')
cusp='notes/actual_main_meridian_preferred_cusp.md'
edit(cusp,
'For each nonsingleton connected component \\(\\mathcal U\\) of bare junctions, let \\(b_v\\) count the incidences at vertex \\(v\\) that leave that component. Require \\(b_v\\ge5\\) and',
'An entirely trivalent connected component is allowed at any fixed finite size, by the [trivalent extension](actual_main_meridian_trivalent_filled_volume.md). Valence counts both its internal edges and outside branches in the actual reduced tree. For a nonsingleton component \\(\\mathcal U\\) that is not entirely trivalent, let \\(b_v\\) count the incidences at vertex \\(v\\) that leave that component. Require \\(b_v\\ge5\\) and')
for rel in ['notes/actual_main_meridian_source_bounds.md','notes/actual_main_meridian_auxiliary_color_gap.md']:
 p=root/rel;s=p.read_text();pos=s.index('\n\n');s=s[:pos]+'''\n\nThe [trivalent-component extension](actual_main_meridian_trivalent_filled_volume.md) extends this result to arbitrary-size connected components of trivalent bare junctions, together with the previously covered component classes. The proof below establishes the original separated-junction case; the extension retains its invariant and normalization.''' +s[pos:];p.write_text(s);changed.add(rel)
Path('/private/tmp/md-trivalent-initial-changed.json').write_text(json.dumps(sorted(changed),indent=2)+'\n')
print(json.dumps({'changed':sorted(changed)}))
