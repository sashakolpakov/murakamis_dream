# A coupled height bound for attached type-four endpoints

Research deduction, 5 November 2026. Compatibility of two already
validated, full-dimensional local maps improves the height range of
an actual attached type-four endpoint. The argument uses exact rational
arithmetic on their saved enclosures. It does not evaluate a root,
repeat a source comparison, or subdivide a parameter box. The bound
does not hold merely because an independent auxiliary endpoint input
lies in a typed disk.

## 1. Actual references and the two full covers

Consider an arbitrary fixed open word of length \(m\ge3\), whose first
type is four. Write
\[
 a=t_1,\qquad b=s_2,\qquad c=s_3,\qquad
 n_2=3+\beta,\quad n_3=3+\gamma,\qquad \beta,\gamma\in\{0,1\}.
 \tag{1}
\]
The first endpoint map has attached output \(a=E_4(b)\).
Vertex 2 is ordinary, including at length three. Its original block
map \(B_\beta\) obeys
\[
 B_\beta(a,c)=(b,t_2),\qquad
 B_\beta(c,a)=(t_2,b).
 \tag{2}
\]
The exchange follows from the original equations and their unique
zero-lift root. It is not symmetry of a chirped finite kernel. Thus
the required ordinary output is the **second** output of the saved
family with flags \((\beta,\gamma,1)\).

Use the reduced disks and the typed domains \(K_3,K_4\) from
[the typed-envelope deduction](research_mixed_typed_last_row_envelopes.md).
Every actual reference in (1) satisfies
\[
\begin{split}
 a&\in P_4\cap
       ([.246,.350]+i[-.108,-.020])=:A_4,\\
 c&\in K_{3+\gamma},\\
 b&\in P_{3+\beta}\cap
 \begin{cases}
 [.267,.433]+i[-.072,.068],&\beta=0,\\
 [.259,.360]+i[-.108,-.001],&\beta=1.
 \end{cases}
\end{split}                                                    \tag{3}
\]
The endpoint rectangle and the reduced-disk inclusions are the
[saved endpoint extraction](research_mixed_open_word_endpoint_rectangles.md)
and [local-factor coverage](research_mixed_open_local_factor_coverage.md).
The extra \(\Re b>.259\) in the second case is the independently
proved, oriented bound in
[the adjacent-four input deduction](research_mixed_first_cap_oriented_plateau_certificate.md),
equations (2)--(5): the leg \(s_2\) is adjacent to a type-four
endpoint. It is not a universal lower bound for every type-four leg.
The rectangles in (3) are deliberately closed enlargements. At
\(m=3\), \(c=s_3\) is attached; at larger lengths it is ordinary.
Both roles belong to the same stated \(K\), so no extra length or
word assumption enters the argument.

There are two existing full covers:

* The endpoint author and independent replay cover each original
  normalized input square \([-1,1]^2\). An X leaf is strictly
  outside the unit input disk; an L leaf encloses the original
  endpoint root at **every** parameter in its entire box. Its
  attached enclosure is \(|a-a_0|<R\).
* The ordinary localization covers the full four-dimensional
  normalized input square. Its exact dyadic addresses and affine
  witnesses are saved in
  [the full-product image record](../repro/results/research-mixed-cyclic-block-images.json.gz).
  This is not the separate boundary-image record. Every witness
  applies throughout its complete parameter box, with the original
  physical midpoint \(p_0\):
  \[
   z_i(p)=z_{0,i}+\sum_{j=1}^2D_{ij}(p_j-p_{0,j})+w_i,
                       \qquad |w_i|\le R_i.
   \tag{4}
  \]

The physical disk radii in the address decoding are \(9/100\)
and \(8/125\). They are the original input radii, not the smaller
image radii \(.083,.060\). Clipping a saved box does not change
its midpoint, affine coefficients or remainder radii in (4).
No maximum principle on a boundary-only cover is used.

## 2. Exact compatibility extraction

Only a potential attached height at or below \(-7/100\) needs
testing. An endpoint leaf whose attached disk has imaginary lower
bound above this value is already harmless. For every other leaf:

1. Intersect its input \(b\)-rectangle with (3). Retain every equality
   and crossing box. A disk disjointness test discards a rectangle
   only if its exact minimum squared distance exceeds the squared
   radius.
2. Intersect its attached disk's bounding rectangle with \(A_4\)
   and \(\Im a\le-7/100\). Pair this with each old ordinary
   witness whose second input rectangle intersects that set.
3. Clip the ordinary first input \(c\) to \(K_{3+\gamma}\).
   The type-three slanted inequality \(x-3h\le.608\) uses only
   necessary rectangle restrictions; boxes which cross a disk or
   slanted boundary remain.
4. On the resulting rectangle, compute the second output enclosure
   of (4), using interval extrema of each exact linear term and
   the unchanged remainder radius. Keep the pair if this enclosure
   intersects the endpoint's admitted input \(b\)-rectangle.

In step 4, if a coefficient is \(d_{\rm r}+id_{\rm i}\) and
the original-midpoint displacements range over intervals
\(\Delta x,\Delta h\), its real and imaginary contributions are
\[
 d_{\rm r}\Delta x-d_{\rm i}\Delta h,\qquad
 d_{\rm i}\Delta x+d_{\rm r}\Delta h.
 \tag{5}
\]
The same stored coefficient is used in both bounds. No absolute
coordinate hull from an independent reference replaces the affine
dependence. The endpoint disk is also tested against the clipped
\(a\)-rectangle before retaining a pair.

A rational square index of mesh \(1/100\) only selects candidate
pairs. Every square touched by a closed rectangle is indexed,
including both endpoints. Two intersecting rectangles therefore
share an indexed square. This acceleration deletes no candidate
which could contain an actual common point.

For completeness, an actual reference with \(\Im a\le-7/100\)
lies in some endpoint L leaf and some ordinary accepted box, by
the two full covers. Conditions (3), (4), and (2) put its \(a,b,c\)
in every intersection used for that pair. It survives every test.
Thus the union of the retained pair rectangles contains all such
actual \(a\)'s. Taking their smallest imaginary lower endpoint is
a valid one-sided bound, even if some surviving pairs are not
realizable by a word.

## 3. Completed extraction and the resulting theorem

The verbatim [raw extraction program](../experiments/extract_mixed_first_four_attached_height_raw.py)
was run once, to completion, using only exact Fraction arithmetic on
the saved files. Its immutable
[raw result](../repro/results/research-mixed-first-four-attached-height-raw.json)
has SHA256
af744080d271f208ff50351d8156902e0859be10293e8da1a243ccc718ed5e32;
the program has SHA256
88f3a93a3154c5416f9978aedcf66845ee84429b1207f662a1e763e2fb559642.
The result is:

| Ordinary type / other external type | Tested old-box pairs | Compatible pairs below the threshold | Lower endpoint |
|---|---:|---:|---|
| \(3/3\) | 192,812 | 0 | no \(\Im a\le-.07\) remains |
| \(3/4\) | 165,255 | 0 | no \(\Im a\le-.07\) remains |
| \(4/3\) | 72,288 | 491 | \(-38608669884819457/500000000000000000\) |
| \(4/4\) | 50,648 | 275 | \(-1505860369933393/20000000000000000\) |

There are 481,003 exact pair tests. The last two lower endpoints
are approximately \(-.07721733977\) and \(-.07529301850\);
both are strictly greater than \(-39/500=-.078\).
These are certified enclosure endpoints, not sampled extrema or
claimed values of an actual word.

The separate [provenance checker](../experiments/check_mixed_first_four_attached_height_bound.py)
validates all old author/replay/source bindings and the original
geometric-domain deductions. It checks all six ordinary case sets,
full prefix-free address coverage and exclusions, all endpoint
S/L/X trees, and the affine image address lists and coordinate
convention. It consumes the immutable raw record rather than
repeating the compatibility arithmetic. A successful provenance
check, together with the reviewed extraction in Section 2, supplies
the following deduction.

**Theorem 1.** At either attached type-four endpoint of every
actual mixed three/four open word of length \(m\ge3\),
\[
                         -.078<\Im a<-.020.
 \tag{6}
\]
If its adjacent vertex has type three, the stronger lower bound
\[
                              \Im a>-.070
 \tag{7}
\]
holds.

The lower bounds follow from the completed compatibility extraction
and the preceding containment argument. The strict slack between
the two rational minima and \(-.078\) avoids any open-versus-closed
box issue in (6). In (7), every potential point with
\(\Im a\le-.070\), including equality, was excluded.
The upper bound is the original endpoint rectangle. Reflection of
the original critical equations proves the same statement at the
right endpoint; no finite-kernel argument symmetry is used.

The archived raw program retains its original workspace/output paths
verbatim for provenance. Its input record hashes specify the complete
data used; the separate checker uses repository-relative paths and
performs no root or source evaluation. No second compatibility run,
new cover, or new floating proposal is part of this deduction.

## 4. Scope

This improves an **actual coupled-reference** height. It does not
improve the image of the independent endpoint map on its whole typed
input disk: the old witnesses include auxiliary heights below
\(-.10\). It also does not impose the cyclic \(-.057\) floor.
Length two has two mutually attached endpoint maps and is not covered
by (2); its fixed-point or two-endpoint compatibility must be treated
separately. No length-two assertion is made here.

The theorem changes neither a finite contour nor its original action.
In particular it does not by itself prove a selected first-cap bound,
pay its imaginary affine tangent, or establish the whole open-source
comparison. It supplies a sharper admissible reference height for
those subsequent estimates, uniformly in word length and type pattern.
