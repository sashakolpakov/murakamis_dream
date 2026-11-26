from pathlib import Path
import hashlib,json,subprocess,datetime,shutil
base=Path('/private/tmp/murakamis_dream-publication')
draft=Path('/private/tmp/md-directed-allorders-source-and-geometric-factor.md')
initial=Path('/private/tmp/md-directed-allorders-inputs.json')
old=json.loads(initial.read_text())
snapshot=Path('/private/tmp/md-directed-allorders-dependency-snapshot')
snapshot.mkdir(exist_ok=True)
# This records theorem inputs and their exact use; it is not a replay of their proofs.
rows=[
('actual_all_circle_directed_volume.md','directed analytic theorem','§§1–7; (3)–(9), (13)–(46)','Fixed certificate; exact degree and recurrence; conditional rectangle; normalized phases, nonzero first charge and all tail/current margins; original filled critical-point restoration.','§§1–7','The new draft extends these actual inputs to translated compacts and every finite order; the old first-order conclusion is not itself an all-order input.'),
('actual_main_meridian_filtered_characteristic.md','formal and operator framework','§§1–6; especially §§2–4.1 and exact gauge in §5','Canonical insertion, existing shifted-chart mechanisms, degree-filtered formal regrading, exact meridian gauge and first-symbol extraction.','§§3–6,8','Its published source-class list does not yet include the directed cases; the new draft supplies that missing analytic extension.'),
('exact_factorial_interpolation_and_complex_contours.md','canonical interpolation','§§1–5','The specified Gamma product, exact recurrence/reflection, complex bulk expansion and finite cotangent contours.','§§4,6','Arbitrary finite-order uniform remainders are established in the draft by taking sufficiently many finite Stirling terms; no unspecified periodic interpolation factor is allowed.'),
('actual_main_meridian_regular_circle_trace.md','canonical circle interpolation','§10, with normalizations from §§1–3','The literal Newton interpolant, midpoint d/2, G(s)G(-s)=H^-1, and exact physical coefficient normalization.','§§4,6','Only the exact interpolation and normalization are used; its local leaf asymptotic is not substituted for a whole directed contraction bound.'),
('actual_main_meridian_direct_crossing_trace.md','finite physical trace','§§1–5, especially §§2–4','Full fixed-power shifted-grid trace, first coefficient one, U-polynomial charge factors, translated endpoints and zero-mode currents, canonical analytic wire interpolation.','§§2–5','The directed proof supplies the conditional charge/tail comparison, not the older independent-long-slope hypothesis of a local asymptotic statement.'),
('actual_main_meridian_source_bounds.md','canonical full polynomial estimates','§§1.1–1.4; (D2)–(D17), especially (D9)–(D14)','Full Hermite norm, fixed metric, quotient folding, top functional, fixed-power crossing polynomial and mixed carriers.','§§2–5','Uses whole polynomial norms; no pointwise one-high tensor comparison. In (D14), lambda is stripped and kappa is retained separately.'),
('all_circle_uniform_newton_bounds.md','full kernel source estimates','§§1–3','Uniform high/complement loss, actual complex angular product bounds, and the explicit one-edge action.','§§2–4','Bounds retain high indices and derivative normals; they are not inferred from positivity of moving paired weights.'),
('actual_all_circle_curvature_filling_limit.md','one-edge phase and contour','§§2–6, especially §§4–5','Exact full edge action and canonical complex wire saddle, source normalization, edge Hessian and finite contour currents.','§§2,4,6','The summed criterion of its global conclusion is not assumed here; only its local algebra/edge contour inputs are used.'),
('actual_all_circle_local_message_volume.md','exact finite tree recurrence','§§1–7, especially §§2–3 and §§5–6','Original full kernel and exact message contraction; full real-kernel estimates and normal-channel conventions.','§§2–5','The old maximum-based criterion is not imported. The directed inequalities replace its numerical error budgets.'),
('actual_main_meridian_grouped_wire_packet.md','canonical primitive interpolation interface','§§5–6; (21)–(27), plus scalar separation in §8','Exact circle and edge G interpolants, integer/midpoint offsets, primitive finite contour normalization and outside scalar separation.','§§4,6','The all-circle directed proof does not import its long-filling global pressure conclusion or a bare-component restriction.'),
('actual_main_meridian_newton_compiler.md','actual typed compiler and cut','§§4–5','Original orientation objects, compatible mixed references, actual serial composition, and the single reduced-cut H factor.','§§1–5','No untyped multiplication or independent physical rerooting is assumed; reordering is finite scalar contraction only.'),
('actual_main_meridian_turn_comparison.md','physical turn and normal coordinates','§§1–4, with full norm description in §6','Six ordered turn types, fixed-basis metric and paired H/W factors, exact full normal data.','§§2–3,5','The extension uses bounded paired products directly; it does not extend the separate small-disk full-J comparison theorem by fiat.'),
('actual_conway_root_star_full_jet_localization.md','complete-basis norm foundation','Complete Newton/Hermite estimates cited by source_bounds §1','Polynomial complete Hermite/sup comparison and low/high complete-basis envelopes.','§§2–4','An inherited full-norm input, not a fresh proof of every localization lemma in this turn.'),
('actual_main_meridian_exact_scalar.md','exact global scalar','§§1–6; full physical source qualification in §7','Actual duality, six turn phases, signed mixed powers, closing/pivot/writhe factors, and A_N=q^{(-w-sum n)s^2/2}.','§§1,3–8','Full Cartan factors stay in the ledger. The new analytic conclusion is not inferred from the finite scalar identity alone.'),
('kashaev_ado_pointing.md','actual state and pointing','§§1–3','M=-qx, zero-framed reduced cut scalar, K_N=F_N(1), full modified dimension and eta_N.','§§1,5,8','Reduced state and full modified trace are kept distinct; one H is removed in Z, and the exact d_N gauge is restored in the recurrence.'),
('actual_all_circle_vertexwise_geometry.md','directed geometric completion input','§§1–4','The 630 vertexwise radius criterion, positive charge path, uniqueness polydisk, actual metric and absolute volume.','§7','The directed certificate forces sqrt(d^2+n^2)>=2pi*2^15; no old summed source criterion is needed for this geometric path.'),
('actual_all_circle_geometric_characteristic.md','geometric longitude and selected germ','§§2–10, especially §5, §§6–9 and §10; §11 for existing gauge exposition','Actual ordered representation reconstruction, marked filled anchor, rational preferred longitude, constants/units argument, and negative SL lift.','§§7–8','Its published operator list is not assumed to include the new class; the algebraic geometric identity is applied only after the new directed analytic/filled anchor is supplied.'),
('actual_all_circle_octahedral_decomposition.md','ordered topological foundation','Ordered page/terminal-attachment and primitive cusp construction','Literal physical ordering, actual rotated child balls, disk seams and original primitive peripheral paths.','Inherited by §7','Used through vertexwise geometry and geometric-characteristic reconstruction; no identification from scalar commutativity is substituted.'),
('actual_all_circle_angular_octahedra.md','local geometric chart foundation','Local angular edge charts and disk-side seam calculation','The actual C-composed-turn charts and marked angle/shape branches at the complete source.','Inherited by §7','Geometric anchor, not a deduction from the quantum saddle.'),
('actual_all_circle_geometric_completion.md','charge-path completion foundation','Marked log-link, smooth filling and regulator identity','Primitive U+pV=-2pi i continuation, positive completion and original actual filled complement.','Inherited by §7','The vertexwise theorem supplies the applicable radius condition; no unsupported large-slope analytic theorem is imported.'),
('actual_all_circle_preferred_cusp.md','preferred-cusp continuation foundation','Original marked branch and preferred surgery correction','Cusp translation identification along the positive charge path.','§7 first-correction calibration','The full germ identity in geometric_characteristic is stronger and is the direct source of S double-prime; tangent matching is not used to prove the full factor.'),
('actual_geometric_normal_period.md','filled meridian-germ rigidity','§3, as cited in geometric_characteristic §5','Smooth actual geometric knot germ and meridian local coordinate.','§7','Used with the actual filled representation and retained marking, not an arbitrary root of the exponentiated source equations.'),
('general_marked_multicusp_gluing_rigidity.md','marked all-cusp rigidity foundation','§§2–3,5 within stated positive-triangulation hypotheses','Full peripheral Jacobian, representation/decorated germ comparison and marking.','Inherited by §7','Its triangulation hypotheses are retained; it is not cited as a universal statement for an unconstructed positive triangulation.'),
('finite_sum_annihilator.md','existence of genuine all-level operator','§§1–6','Fixed all-level finite-sum annihilator with boundary strata and specialization retained.','§8','The factor theorem is for every specified genuine operator. Existence is an independent input; it does not identify the full operator ideal or AJ polynomial.')
]
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=base,text=True).strip()
entries=[]
for name,kind,sections,use,draft_sections,qualification in rows:
    rel='notes/'+name
    p=base/rel
    data=p.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    out=snapshot/rel;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
    assert p.read_bytes()==data, f'Changed during snapshot: {rel}'
    q=subprocess.run(['git','show',f'HEAD:{rel}'],cwd=base,capture_output=True)
    e={'path':str(p),'relative_path':rel,'sha256':digest,'bytes':len(data),'snapshot_path':str(out),'snapshot_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'matches_recorded_HEAD_blob':q.returncode==0 and q.stdout==data,'input_kind':kind,'source_sections':sections,'used_for':use,'draft_sections':draft_sections,'qualification':qualification}
    if rel in old['source_sha256']:
        e['original_proof_input_sha256']=old['source_sha256'][rel]
        e['unchanged_since_original_proof_input_record']=digest==old['source_sha256'][rel]
    entries.append(e)
qualifications=[
'The draft remains private and is not installed in the workspace or publication notes. No public all-order/operator source-class list has been changed by this task.',
'Fixed finite literal ordered circle tree, at least one edge, original orientation and endpoint words, one knot and no internally closed component. Powers, certificate, compacts and requested finite expansion order are fixed before N tends to infinity.',
'Both level parities and full constant/moving normal channels remain. Lower amplitudes may be organized by parity; the selected leading phase is common.',
'Translated-chart estimates hold on fixed compacts in the open upper half-plane, and separately on original |s|<=R<1 disks. They do not assert uniform nonvanishing across nonzero integer resonances.',
'The auxiliary t=s/N analytic family is only a local coefficient-organizing family. No physical fixed-M WKB or s proportional to N asymptotic follows.',
'All-order constants and starting levels may depend on the fixed diagram, certificate, compact, finite expansion order and derivative order. The numerical certificate itself is unchanged.',
'Every genuine fixed all-level reduced annihilator has the selected complex factor in its first nonzero classical symbol; over Q use the contracted prime. No full A-polynomial, multiplicity, full-ideal or AJ equality is asserted.',
'No graph-with-cycles theorem or multi-boundary replacement for arbitrary short-power islands follows from this single-boundary tree induction.',
'The proof uses the actual whole trace outside each local contour. The all-order local remainder is not substituted for the exact global real/strip bounds.',
'Exact crossing normalization: source D14 interpolates stripped lambda values; kappa_sigma^n and all mixed-reference scalars stay in the exact global ledger. The draft now states this explicitly without changing an equation.'
]
coverage={
'author_work':'The new draft derives the shifted-source extension, arbitrary-order normalized recursion and canonical degree filtration; it references the source theorem inputs listed here rather than reproving every theorem in their ancestry.',
'parent_read':'Root read draft sections 3–8 and found the new remainder, auxiliary-family, exact gauge and prime steps coherent. This is not recorded as an independent reproving or blanket verification of every dependency.',
'geometry_peer_read':'Geometry independently read section 7 against vertexwise geometry and the filled-germ reconstruction, including the actual anchor, Q^2!=1, selected eigenline, scalar and preferred-cusp correction. It did not re-audit the new all-order induction.',
'cluster_peer_challenge':'Cluster reported no translated-compact obstruction in bounded H/W or fixed-power canonical norms and retained the independent sigma=0 channel. Its other priority prevented a complete all-order proof read; none is claimed.',
'remaining_integration_work':'Dedicated integration/review before publication, preserving the current old source-class list until authorization. No mathematical obstruction was identified in the current derivation; this record does not turn limited peer reads into full dependency validation.'
}
draft_bytes=draft.read_bytes();draft_sha=hashlib.sha256(draft_bytes).hexdigest()
(snapshot/'draft.md').write_bytes(draft_bytes)
manifest={'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'publication_checkout':str(base),'publication_HEAD':head,'original_proof_input_HEAD':old['publication_head'],'draft_path':str(draft),'draft_sha256':draft_sha,'draft_snapshot':str(snapshot/'draft.md'),'draft_at_parent_read_sha256':'06b616a1c5fd17f0e1a5072467209c79b7c6ac2e2e52259e64ca002153427a3a','post_parent_read_change':'Crossing-normalization prose only: specifies D14 stripped lambda and retained kappa; all displayed formulas unchanged. Prior file preserved privately.','dependency_coverage':'Direct and explicitly named foundational theorem inputs actually used; not a recursive hash of every citation in the repository. Unused long-filling global/bare-component hypotheses are not imported.','inputs':entries,'qualifications':qualifications,'read_coverage':coverage}
out=Path('/private/tmp/md-directed-allorders-dependency-manifest.json');out.write_text(json.dumps(manifest,indent=2)+'\n')
lines=['# Dependency record for the directed all-order proof','',f'Private draft: `{draft}`',f'','SHA256: `'+draft_sha+'`','',f'Publication checkout: `{base}`; recorded HEAD `{head}`. The original proof-input record was made at `{old["publication_head"]}`.','',
'The dependency files below have been copied byte-for-byte into `md-directed-allorders-dependency-snapshot/notes/`. This record preserves their current SHA256 values and their exact role. It is not a declaration that every inherited theorem was independently reproved during this turn.','',
'The parent-read draft at `06b616a1…427a3a` is preserved in `md-directed-allorders-source-before-crossing-normalization-wording.md`. The sole subsequent clarification identifies (10) as the stripped interpolation and explicitly retains its full Cartan scalar. No displayed formula changed.','',
'## Exact inputs','']
for e in entries:
    lines+=['### '+e['relative_path'],'',f'SHA256: `{e["sha256"]}`','',f'**Use:** {e["used_for"]}',f'','**Locations:** '+e['source_sections']+'; draft '+e['draft_sections']+'.','',e['qualification'],'']
lines+=['## Qualifications','']+[f'- {q}' for q in qualifications]+['','## Extent of the readings','']
for k,v in coverage.items(): lines += [v,'']
lines+=['The machine-readable manifest records per-file snapshot hashes, exact byte counts, HEAD-blob agreement and comparison with the initial 13-file input record. No repository file was changed by creating this record.','']
Path('/private/tmp/md-directed-allorders-dependency-manifest.md').write_text('\n'.join(lines))
# Refresh the lightweight index while preserving its original version.
shutil.copy2(initial,Path('/private/tmp/md-directed-allorders-inputs-before-manifest.json'))
old['draft_sha256']=draft_sha
old['expanded_dependency_manifest']=str(out)
initial.write_text(json.dumps(old,indent=2)+'\n')
print(json.dumps({'draft_sha256':draft_sha,'manifest_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'inputs':len(entries),'all_snapshot_hashes_match':all(e['sha256']==e['snapshot_sha256'] for e in entries),'all_current_inputs_match_HEAD':all(e['matches_recorded_HEAD_blob'] for e in entries),'original_input_changes':[e['relative_path'] for e in entries if e.get('unchanged_since_original_proof_input_record') is False]},indent=2))
