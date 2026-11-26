# Targeted manuscript scope reread

This is a read-only scope check of the publication checkout. It does
not claim a fresh proof audit of every appendix. No public file was
edited and no build was run.

## Prior checks retained

I first read the earlier records
md-manuscript-editorial-check.json and
md-morse-manuscript-scope-inventory.json. The latter already resolved
the obsolete geometric-identification deferral in Appendix H and
distinguished the conclusions of Appendices E, K, N and O. Those
findings were not repeated as new defects.

The present read covers the abstract and introduction, the scope
statements and source qualifications of Chapters 2–3 and the
quantitative/geometric chapters, and the theorem statements and
transfer interfaces of Appendices H, N, O and P. The checks below
compare an asserted conclusion with its actual written input.

## Concrete corrections

The parent subsequently applied all three corrections below. They are
retained here as the bounded review record, not as outstanding issues.

1. **manuscript/sections/03-entropy.tex, line 3.**
   The opening says: “At complete auxiliary color, every elementary
   coefficient and every multiplication coefficient is positive.”
   This needs the pure-source qualification. Chapter 2, lines
   225–233, explicitly retains complex phases after a half twist,
   while Chapter 3, line 8, correctly specifies the “complete pure
   case.”

   Suggested replacement:

   > For the pure complete-color source, before retained half twists,
   > every elementary coefficient and every multiplication coefficient
   > on the admissible support is positive.

   This changes no subsequent action or proof.

2. **manuscript/sections/01-introduction.tex, line 161.**
   The explanation for excluding \(C(hh)\) says that “its
   even-level evaluation vanishes and its odd-level contribution
   lies on a flat boundary.” Without a source qualification, this
   can be read as a statement about filled knot invariants.
   The actual input is the pure Newton-support calculation:
   at even \(N=2m\), the leaf support ends at \(m-1\), so the
   top product output \(d=2m-1\) is absent. At odd levels the
   surviving closed support is flat. This is stated in
   notes/actual_conway_two_leaf_seed_geometry.md, §5.

   Suggested replacement:

   > The isolated \(C(hh)\) is excluded: its pure complete-color
   > source vanishes at even levels, and its odd-level support
   > lies on a flat boundary.

   The following exclusions remain explicitly limited to the first
   theorem, as they should.

3. **manuscript/sections/01-introduction.tex, line 40.**
   The “Preferred longitude and recurrence” row in the scope table
   does not name its knot class. The surrounding detailed section
   and abstract correctly restrict it to the covered tree sources.
   The row follows the planar weak-balance result and should retain
   that restriction locally as well.

   Suggested replacement:

   > For the covered strict-tree and circle-tree source classes,
   > the longitude identity and full meridian expansion force one
   > geometric factor in any existing all-level annihilator.
   > No recurrence-ideal equality is asserted.

## Conclusions whose narrower scope is already explicit

- The recursive theorem retains its exact completed-box grammar,
  original knot/parity test, and independently sufficiently long
  fixed signed twists. It does not classify all arborescent knots.
- The circle-tree theorems retain their numerical sufficient
  conditions, original component test and fixed-diagram quantum
  limit. The metric condition \(630\) is explicitly distinguished
  from a quantum volume estimate.
- Appendix P assumes the stated weak-balance inequalities in the
  actual complete packing. Its use of a single changed coefficient
  weight does not claim that every matched sphere satisfies them.
- Appendix N proves a finite norm estimate and an implication
  conditional on a complementary-source gap. It explicitly does
  not establish that gap universally.
- Appendix O identifies the original knot or link complement and
  proves the nonzero all-CROSS contribution through the entire
  Fourier period. It explicitly excludes a universal estimate for
  the complementary source.
- The geometric-longitude and all-order arguments assume the
  specified existing annihilator when deriving its selected
  classical factor. They do not assert equality with the full
  A-polynomial or recurrence ideal, and they do not transfer the
  operator conclusion to the new weakly balanced planar class.

I found no additional conjectural comparison presented as an
established full knot-volume theorem in these inspected statements.
The private R54 entropy/energy and phase investigations are absent
from the manuscript, as required.
