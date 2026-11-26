# Smaller endpoint ranges from the existing critical-point certificates

Research corollary, 5 November 2026. No new roots or parameter
subdivisions are required.

At either end of an open word, write \(e\) for the private leg,
\(t\) for its attached leg and \(u\) for the ordinary endpoint
coordinate. The four maps in the
[open critical-point theorem](research_mixed_open_word_critical_localization.md)
solve for these three coordinates as the neighboring attached leg
ranges over either of the original typed disks.

**Corollary 1.** For an endpoint of type three or four, its coordinates
lie in the following open rectangles:

| Type | Private leg \(e\) | Attached leg \(t\) | Endpoint coordinate \(u\) |
|---|---|---|---|
| Three | \((.376,.438)+i(-.019,.037)\) | \((.278,.391)+i(-.072,.021)\) | \((.218,.242)+i(.049,.077)\) |
| Four | \((.333,.363)+i(-.051,-.019)\) | \((.246,.350)+i(-.108,-.020)\) | \((.217,.234)+i(.027,.045)\) |

This holds at every word length \(m\ge2\), without a condition on
the neighboring type. For \(m=1\), the two legs coincide. Their
separately certified value lies in both the private and attached
rectangles of its type, and the ordinary endpoint coordinate lies
in the same third column.

*Proof.* Every accepted leaf of the original endpoint certificate
contains an exact rational complex center \(z_0\) and an exact
rational radius \(\rho>0\). Its validated Newton argument puts
the root in the product of complex disks
\(|z_i-z_{0,i}|<\rho\). In particular its real and imaginary
coordinates lie strictly between the corresponding coordinates of
\(z_0\) minus and plus \(\rho\).

The accompanying exact checker visits all 5,258 leaf witnesses in
the four original complete trees and checks these rational intervals
against the table. The trees still cover their full parameter squares;
an excluded rectangle is checked to lie strictly outside the input
unit disk. The two original one-vertex witnesses are checked in the
same way. The original author record, higher-precision replay and
their proof and code bindings are retained. Displayed decimal root
hulls play no role in the comparisons. The critical-point theorem
identifies every endpoint of an arbitrary open word with one of these
maps, or with a one-vertex root. This proves the corollary.

Both private rectangles are strictly contained in
\[
 E_{\mathrm{cap}}=[.27,.49]+i[-.055,.04].
\]
Thus the [extended endpoint packet](research_mixed_endpoint_cap_rectangle.md)
applies at every private critical index, with a common positive
separation from the boundary of this rectangle. The sum of a real
coordinate in \(E_{\mathrm{cap}}\) and one in either attached
rectangle is always between \(.516\) and \(.881\). These
simple bounds keep the vertex sine argument strictly between
\(1/2\) and \(1\) on a proposed outer cap contour.

The table does not assert that every independent pair \((e,t)\) in
these rectangles solves the critical equations. Where a proof needs
their correlation, it must retain the original parameter-dependent
Newton witnesses. Nor do these inclusions estimate the outer cap sum.

Run the exact extraction with

```sh
python3 experiments/check_mixed_open_word_endpoint_rectangles.py
```

It performs rational comparisons only and does not repeat the root
search or the interval Newton calculations.
