# A bounded whole-domain reference partition pass

Research specification, 6 November 2026. This is a reference-classification
pass for first flags \((1,1,\beta)\), \(m\ge4\), with both
\(\beta=0,1\). It evaluates no scalar budget or finite source.
The old providers and all earlier diagnostic records remain unchanged.

## 1. The complete starting partition

The [coverage-transfer theorem](research_mixed_second_selected_reference_cover_reuse.md)
proves that every actual auxiliary reference lies in the union of the
678 accepted cells of the complete
[old adaptive record](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json).
Its other 2613 leaves are necessary-reference exclusions valid for
the present problem. Preserve those excluded leaf objects unchanged.
The 678 old scalar acceptances are now pending reference cases; their
old scalar signs are not reused.

For each beta, the root rectangle is
\[
 R=[217/1000,117/500]+i[27/1000,9/200].
 \tag{1}
\]
The original 3291 binary addresses are prefix-free and have total
mass one. The 678 candidate leaves have mass \(2587/65536\).
Decode every candidate rectangle exactly by the original alternating
real/imaginary dyadic split rule. No new subdivision is allowed.
The driver checks these invariants and the inherited hashes before
any reference calculation.

## 2. Full-box arithmetic with a sufficient Cartesian zero test

The arithmetic uses the reviewed
[exact-shift specification](research_mixed_second_selected_shifted_reference_evaluation.md)
and the same canceled rational maps, derivatives, integer factor
contents, common dyadic Gaussian midpoint, and exact integer shift
recurrence. Each starting cell has fresh caches; its two beta cases
share those caches. No clipped coordinate is fed into a rational
map, polynomial shift, or derivative enclosure.

For a finite complex rectangle with real and imaginary intervals
\(I=[l,r]\), \(J=[s,t]\), define
\[
 d(I)=\max(0,l,-r),\qquad
                  \eta=\max\{d(I),d(J)\}.
 \tag{2}
\]
If \(\eta>0\), every point in the rectangle is nonzero.
A positive outward radial-modulus lower bound is another sufficient
test. The new driver accepts either certificate, recording both.
This fixes the conservative guard documented by the
[saved-data exclusion](research_mixed_second_selected_saved_reference_exclusion.md);
it changes no mathematical reference domain.

For each canceled map, first enclose its direct quotient on the full
parameter rectangle, after separating its denominator factors and
product from zero. Save that value immediately. The mean-value
enclosure from the separately canceled derivative is an optional
refinement. If its denominator, derivative, or interval intersection
is inconclusive, retain the already proved finite direct quotient.
Record the refinement failure and use no derivative from that stage.
No second attempt is made. If the direct quotient itself is not
rigorously finite, the map is inconclusive and its failed status is
cached for the other beta case if needed.

The direct-only fallback is rigorous because the direct quotient
inclusion does not depend on the derivative refinement. A fallback
does not assert a usable derivative enclosure, nor does it discard
an original source denominator.

## 3. Staged necessary filters

Within each beta case evaluate shapes in the order
\[
                        E,A,U,Z,V,B_\beta,C_\beta.
 \tag{3}
\]
As soon as a shape is available, apply its original necessary
negative-imaginary sign, logarithmic-branch and coordinate conditions.
The endpoint and ordinary rectangles, reduced disks and sum bounds
are exactly those in the
[reference-curve theorem](research_mixed_second_selected_reference_curve.md).
Apply each pair-sum filter as soon as both coordinates are available.
In particular \(B_\beta\)'s sign and ordinary rectangle are tested
before the expensive final external map is requested.

An upper-half-plane shape with strictly positive imaginary lower
endpoint is excluded immediately. If its whole interval is not in
the lower half-plane and cannot be excluded, decoding is inconclusive.
All other exclusions also require strict contradictions of necessary
conditions. Equality and uncertain comparisons remain.

Coordinate intersections with necessary rectangles may be performed
as each coordinate is decoded. These are pointwise containing
enclosures of every admissible reference and may tighten subsequent
pair-sum tests. They do not alter the full parameter arithmetic or
its derivative inputs. The final external coordinate retains the
union of both typed suffix envelopes; both alternatives must fail
before the union is excluded. No new height bound for \(z\) is used.

An early strict contradiction excludes every possible actual point
in that cell even if later maps are not evaluated: every actual
point has regular original equations and must satisfy that necessary
condition. Conversely, before a case is marked reference-retained,
test every original uncanceled denominator, shape zero and sine
factor, including the exact denominator identities in Section 3 of
the shifted specification. The reference theorem then supplies the
original zero logarithmic lifts on the admitted subset.

## 4. Finite execution and saved coverage

The proposed run uses 160 bits and visits the 678 starting cells in
lexicographic address order, with beta zero followed by beta one.
There are at most 1356 reference calls, with no retries, alternate
points, subdivisions or old inspect calls. A cell's cache permits at
most nine rational maps, 27 polynomial shifts, 20962 exact Gaussian
multiplications and 714 interval Horner multiplications. The respective
global arithmetic caps are obtained by multiplying by 678. The
driver prints progress every 20 cells and at completion.

Every case has status `excluded`, `retained`, or `inconclusive`.
Reference-retained means only that the necessary tests do not exclude
the case and the required arithmetic/branch guards passed. It proves
neither word realization nor a scalar rate inequality.

The output retains each candidate address, exact rectangle, original
leaf hash, both beta outcomes, completed shapes, untruncated and
intersected coordinate endpoints, necessary-filter reasons, original
regularity tests, map and derivative/refinement bounds, and operation
counts. Per-cell polynomial endpoints and midpoint data are saved;
the large exact shifted integer-coefficient arrays are omitted from
this partition record because their algorithm and original integer
inputs are already bound. This omission does not change evaluation.

Together with the unchanged inherited exclusions, these candidate
outcomes form a full partition for each beta. Counts, exact status
masses, prefix-freeness, rectangle reconstruction and total mass one
are checked before writing. A fatal unexpected error stops the pass
and preserves every unvisited candidate as `unvisited` in both
partition accounting and the saved frontier; it cannot yield a
completed-pass status. Ordinary arithmetic inconclusiveness remains
recorded and does not authorize more work.

Frozen bindings are checked before repository imports and after the
pass, including the coverage-transfer proof, complete old record,
exact rational data, all reused providers, and this specification.
The old source/main programs, primitive routines and scalar-budget
callbacks are disabled. No continuation into scalar budgets follows
automatically from this reference-only pass.
