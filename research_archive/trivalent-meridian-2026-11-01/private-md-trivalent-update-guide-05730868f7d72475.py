from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication');tmp=Path('/private/tmp');changed=set(json.loads((tmp/'md-trivalent-initial-changed.json').read_text()))
def edit(rel,old,new):
 p=root/rel;s=p.read_text();assert old in s,(rel,old[:90]);p.write_text(s.replace(old,new,1));changed.add(rel)
packet='notes/actual_main_meridian_grouped_wire_packet.md'
edit(packet,'In (4) every edge index stays in one such compact interval.','In (4) every circle-incident edge index stays in one such compact interval.')
edit(packet,'adjacent bare components failing (1),','bare components outside the three alternatives in Section 1,')
edit(packet,'For \\(u=N\\tau/(2\\pi)\\), use','For the circle-incidence factors, put \\(u=N\\tau/(2\\pi)\\) and use')
results='book/chapters/results.md'
edit(results,
'The theorem applies when no two bare junctions are joined by an edge. The number of pieces, their nesting depth, and their valences can be arbitrary fixed finite quantities.',
'The theorem applies when each connected group of bare junctions is either a single vertex or a tree in which every vertex has three incident branches. In counting those branches, include both connections within the group and attachments to the rest of the construction. Such a tree is called trivalent. Its size and nesting depth may be any fixed finite quantities; there is no lower bound on the number of outside branches at each vertex.')
edit(results,
'It also permits some connected groups of bare junctions. Here is a simple sufficient test.',
'Groups containing adjacent higher-valence junctions are also allowed under a separate condition. Here is a simple sufficient test.')
anchor='These conditions control intermediate sums in the proof. They are additional conditions for the moving-meridian result; the earlier complete-value volume theorem has the broader scope stated above.'
edit(results,anchor,anchor+r'''

![A path and a branching tree of trivalent product junctions. Each unfilled vertex has three incident branches; filled vertices carry crossing-circle operators.](../figures/trivalent-bare-components.svg)

The [trivalent extension](../../notes/actual_main_meridian_trivalent_filled_volume.md) treats a whole connected group at once. Moving the meridian adds terms to the multiplication traces. The proof bounds each collection of these extra terms by a boundary state of the original positive volume problem. Its unique maximum is interior, so these terms have a strictly smaller exponential rate. The comparison changes the shared boundary labels together and keeps every internal summation index. It therefore applies to an arbitrary fixed trivalent tree, including the branching example in the figure.

The vertices in this criterion are those remaining after consecutive products have been grouped. An artificial splitting of a larger product does not satisfy the condition: its new edges would not be physical quarter-turns.''')
edit(results,
'The [component extension](../../notes/actual_main_meridian_component_extension.md) proves them under the path condition described above as well.',
'The [path estimate](../../notes/actual_main_meridian_component_extension.md) and the [trivalent extension](../../notes/actual_main_meridian_trivalent_filled_volume.md) prove them for both additional component classes described above.')
frontier='book/chapters/frontier.md'
edit(frontier,
'It includes all presentations in which no two bare junctions are adjacent. A bare junction is a product with no original crossing-circle operator at that vertex.',
'It includes singleton bare junctions of any allowed valence and arbitrary fixed trees of adjacent trivalent bare junctions. A bare junction is a product with no original crossing-circle operator at that vertex. Trivalence counts all three branches at a vertex of the actual reduced tree. The [trivalent theorem](../../notes/actual_main_meridian_trivalent_filled_volume.md) has no size or outside-branch requirement on such a component.')
edit(frontier,
'The open extensions are the moving-meridian theorem for bare components failing the path test,',
'The open extensions are the moving-meridian theorem for components containing adjacent higher-valence junctions and failing the path test,')
edit(frontier,
'The [component theorem](../../notes/actual_main_meridian_component_extension.md) extends both estimates to the path condition stated above.',
'The [path theorem](../../notes/actual_main_meridian_component_extension.md) and [trivalent theorem](../../notes/actual_main_meridian_trivalent_filled_volume.md) extend both estimates to the additional component classes stated above.')
edit(frontier,
'The component theorem extends that comparison across adjacent bare junctions when its path inequality holds.',
'The component theorem extends that comparison across adjacent bare junctions when its path inequality holds. The trivalent theorem covers arbitrary fixed trees of degree-three bare junctions by a simultaneous variational comparison, retaining all their old-supported internal indices.')
index='book/chapters/index.md'
edit(index,
'for long-twist presentations satisfying an additional condition on their multiplication junctions.',
'for long-twist presentations whose bare multiplication components are singleton junctions, arbitrary fixed trivalent trees, or satisfy the stated path criterion.')
readme='README.md'
edit(readme,
'an additional condition on their multiplication junctions. The first',
'a condition on their multiplication junctions. It permits arbitrarily\nlarge fixed trees of junctions with three incident branches, as well as\nthe other component classes stated in the theorem. The first')
(tmp/'md-trivalent-initial-changed.json').write_text(json.dumps(sorted(changed),indent=2)+'\n')
print(json.dumps({'changed_source_files':len(changed)}))
