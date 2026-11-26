# Exact boundary coverage for the direct external-coordinate route

Research specification, 6 November 2026. Nine rational charts cover the
entire boundaries of the two actual external-coordinate domains. For
each fixed first flag there are eighteen beta/chart cases. This supplies
parameter geometry and exact finite-frontier bookkeeping only; no
reference, scalar comparison or boundary estimate is evaluated here.

## 1. The domains and nine charts

Use the original typed domains from the
[reference-curve theorem](research_mixed_second_selected_reference_curve.md):
\[
\begin{split}
 K_3={}&\{|c-c_3|\le r_3\}
       \cap\{-9/125\le\Im c\le17/250,\ \Re c-3\Im c\le76/125\},\\
 c_3={}&7/20-i/100,\qquad r_3=83/1000,\\
 K_4={}&\{|c-c_4|\le r_4\}
       \cap\{-27/250\le\Im c\le-1/1000\},\\
 c_4={}&3/10-13i/250,\qquad r_4=3/50.
\end{split}
 \tag{1}
\]
They lie strictly inside their original disks \(D_3,D_4\).
The next external coordinate can be attached at length four or ordinary
at greater lengths; (1) contains both original possibilities. It is
never identified with a private endpoint coordinate.

All chart parameters range over the closed interval \([-1,1]\).
For either type use two semicircles
\[
             c_{j,\pm}(t)=c_j\pm r_j\frac{1+it}{1-it}.
 \tag{2}
\]
The plus chart covers the right semicircle and the minus chart covers
the left. Their endpoints coincide at the top and bottom of the circle.
Since \(1-it\ne0\) for real \(t\), no chart pole occurs.

For each lower and upper clipping height \(h\) in (1), add the
horizontal chart
\[
                 c_{j,h}(t)=\Re c_j+r_jt+ih.
 \tag{3}
\]
Every point of the corresponding disk chord has its real coordinate
between \(\Re c_j-r_j\) and \(\Re c_j+r_j\), so it is
covered by (3). For \(K_3\) also use
\[
 y(t)=-1/500+(7/100)t,\qquad
 c_{3,\mathrm{oblique}}(t)=76/125+3y(t)+iy(t).
 \tag{4}
\]
Here \(y([-1,1])=[-9/125,17/250]\), and
\(\Re c-3\Im c=76/125\) identically. Thus every relevant
oblique chord point is covered. The line's real coordinate is
\(301/500+(21/100)t\); these exact rational coefficients are
the ones used in the module.

There are five charts for \(K_3\) and four for \(K_4\).
The boundary of an intersection of the closed disk and these halfplanes
is contained in the union of their individual boundary pieces. Equations
(2)--(4) cover every such piece after restriction to \(K_j\).
This proves full boundary coverage, including every arc/chord junction
and every intersection of clipping lines. Overlap at junctions and at
the two semicircle endpoints is intentional. No selected half-open
convention removes any junction.

## 2. Exact images and strict exclusions

The module
[mixed_second_selected_external_boundary.py](../experiments/mixed_second_selected_external_boundary.py)
uses only rational arithmetic. For \(t\in[l,h]\subset[-1,1]\),
write
\[
 R(t)=\frac{1-t^2}{1+t^2},\qquad I(t)=\frac{2t}{1+t^2}.
 \tag{5}
\]
The function \(R\) decreases with \(|t|\), while \(I\) is
increasing on \([-1,1]\). Therefore their exact interval extrema
come from the two endpoints and, for the maximum of \(R\), zero
when the interval contains it. Scaling and translating these ranges
gives the full exact Cartesian image hull of each semicircle interval.
Line-image hulls follow from their two affine endpoint values. All
reported bounds are Fractions; no floating or transcendental evaluation
enters the chart image.

An interval is excluded only if a necessary condition of its own
\(K_j\) fails strictly throughout its chart image. The following
tests are used:

* Its image lies strictly below the lower clipping height or strictly
  above the upper clipping height.
* For \(K_3\), its whole image satisfies
  \(\Re c-3\Im c>76/125\). On a line this linear functional
  is bounded by its exact endpoint values; on a semicircle the
  Cartesian image lower bound \(x_- -3y_+\) is sufficient.
* A line interval lies strictly outside its typed disk. Writing the
  line as \(c(t)=a+bt\), its squared distance from the disk center
  is a real quadratic. The exact minimum on \([l,h]\) occurs at
  the quadratic vertex clipped to \([l,h]\), or at an endpoint
  for a constant line. Exclude only when that rational minimum is
  strictly greater than \(r_j^2\).

A semicircle's squared distance is identically \(r_j^2\), so no
disk exclusion is attempted there. Every exclusion record includes the
parameter interval, its Cartesian image, the violated inequality and
an exact positive rational margin. Equality and crossing intervals are
retained. A missing exclusion witness says only that these tests did
not exclude the interval; it asserts neither source feasibility nor a
scalar comparison.

## 3. Module interfaces and the complete interval trees

The exported interfaces are:

* `chartlist()` gives the nine frozen descriptors with stable names.
* `paramimage(chart, (l,h))` returns exact Fractions
  `(x_lower,x_upper,y_lower,y_upper)`.
* `exactsourceexclusionwitness(chart, (l,h))` gives the strict witness
  described above, or `None`.
* `split((l,h))` gives the two closed rational halves, retaining their
  common midpoint in both; it does not evaluate any reference.
* `parameter_interval(address)` decodes a binary interval-tree address
  from the exact root `[-1,1]`.
* `case_list()` gives every `(beta, chart)` case with beta zero or one.
* `validate_partition(addresses)` checks a complete prefix-free
  frontier with exact normalized mass one. Unresolved and unvisited
  leaves must be included alongside all completed leaves.
* `validate_coverage(frontiers)` requires exactly all eighteen cases
  and checks each complete frontier separately.

For an address \(a\), the normalized interval length is
\(2^{-|a|}\). A finite binary prefix-free set whose total normalized
length is one covers the whole root interval. Its full binary tree has
\(2L-1\) nodes when it has \(L\) leaves. These identities concern
each parameter chart, not a disjoint partition of the geometric
boundary; duplicated chart junctions cause no gap.

The driver must additionally reconstruct each leaf's interval and image
from its address, validate every exclusion or comparison witness, and
retain the exact pending frontier whenever it stops. The module's tree
check does not validate scalar signs or reference enclosures. The two
values of beta do not change the chart geometry, but both case
inventories are compulsory. The eighteen-case inventory is for one
fixed first flag; adding both first flags would require two explicitly
identified copies, not an implicit extension of one computation.

## 4. Reference-provider and boundary-comparison obligations

Let \(T=[l,h]\) be a retained parameter interval and let \(C_T\)
be its Cartesian image. A comparison is required only for
\[
                    c\in c_j(T)\cap K_j.
 \tag{6}
\]
The bounding rectangle can include points outside \(K_j\), and
an initial line-chart image can extend beyond the common regular strip.
This never permits asserting a canonical solution at every point of
that rectangle without a separate domain check.

For a whole-box residual enclosure, the provider must check its
entire affine approximation \(q_{\rm aff}(C_T)\) lies in
\(E\times U\times Q^5\), and every original gradient argument
is regular on the entire enclosing set and connecting segments. The
simple sufficient check \(C_T\subset Q\), together with this
affine-product inclusion, supplies those regular strips. If these
checks fail, the cell is unresolved or subdivided; it is not thereby
excluded from the source domain.

Existing canonical-prefix existence is then invoked only at the actual
points (6), which lie in \(K_j\subset D_j\). The
[residual-localization theorem](research_mixed_prefix_residual_localization.md)
applies pointwise there, using the uniform residual bound over \(C_T\).
It does not require existence on the portions of \(C_T\) outside
\(D_3\cup D_4\). Conversely any proposal or residual calculation
must enclose the entire relevant chart interval, rather than a midpoint
or an independently clipped set of derivative coordinates.

To obtain the interior comparison from a completed boundary calculation,
the driver must establish both the original central defect bound and
the response bound on all eighteen applicable boundary cases. The
[stationary-reference extension theorem](research_mixed_stationary_reference_boundary_extension.md)
then charges the correct clipped-disk barrier. It does not assert that
the raw fixed-height defect is subharmonic. A completed chart inventory
alone supplies no boundary sign, interior gap, finite-source estimate,
or suffix realization for a canonical prefix.
