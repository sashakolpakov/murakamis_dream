# Bounded full-disk terminal raw test and one fixed obstruction

The first driver checks the unchanged old endpoint cells meeting the
circles of the two smaller attached disks. It adds no endpoint roots or
parameter subdivisions. There are 622 retained cells:

| Own type | External type | Cells | Failed whole-cell lower bounds |
|---|---|---:|---:|
| 3 | 3 | 165 | 22 |
| 3 | 4 | 184 | 0 |
| 4 | 3 | 135 | 0 |
| 4 | 4 | 138 | 0 |

All failures are in the lower-row branch, not the new explicit upper-row
allowances. The raw lower bounds in the other three families are positive
on their complete old circle cover. These are recorded as a bounded test,
not promoted here to a new three-family source theorem.

## A fixed obstruction to the proposed uniform raw bound

One failing old cell has a midpoint **strictly inside** the smaller
type-three disk. Its exact input is
\[
 a=\frac{967}{3200}+\frac7{128}i,\qquad
 \left|a-\left(\frac7{20}-\frac1{100}i\right)\right|^2
 =\frac{33129}{5120000}<\left(\frac{83}{1000}\right)^2.
\]
Both own and external types are three. Original endpoint-map domain zero,
tree node 1685, has normalized cell
\[
 [-9/16,-1/2]\times[11/16,3/4].
\]
Its archived rational center and inverse validate a radius-\(10^{-10}\)
original-log root disk **at this exact midpoint**, in addition to the
original whole-cell witness. No root solve or new proposal is used.

Let \(P_0(a)\) be the full optimized terminal phase in the
[calibrated half-point theorem](../../../notes/research_mixed_terminal_half_endpoint_gap.md),
including the endpoint coefficient, adjacent kernel and own factorial
allocation. For the exact real row \(v=67/250<1/2\), put
\[
 E_0(a,v)=\Re\{J(a+v)-J(a)+J(v+1/2)-2J(v)+i\pi av\}.
\]
This is the original raw row, with the first-target chirp retained.
The focused 320-bit outward check proves
\[
 h(1/2)+E_0(a,67/250)-\Re P_0(a)>\frac7{10000}.
\]
The excess is approximately .0007337. The literal raw envelope is at
least this one row, so the uniform inequality
\(\Re P_0(a)>h(1/2)+R_0(a,1/2)\) is false on the full allowed smaller
disk. This conclusion does not depend on an optimizer or on the new
upper-row majorant.

This is an obstruction to an **absolute raw comparison on an enlarged
endpoint-map domain**. The particular external leg has not been shown to
occur as an actual open word's critical reference. Nor is a large absolute
row a lower bound for the oscillatory conditional sum. No failure of the
coherent source, invariant or volume conjecture is asserted. The completed
restricted \(R_3/R_4\) terminal theorem remains unchanged.

Reproduce the fixed old-cell test and the separate point obstruction:

    python3 repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/diagnose.py
    python3 repro/diagnostics/2026-11-05-terminal-raw-full-disk-boundary/check_fixed_obstruction.py

Both records include input/helper hashes. The fixed check has no dependence
on the cardinal-point archive or the floating endpoint proposals.

