# One bounded attached-face last-row pilot

**Status: incomplete. No uniform sign on this face is established.**

The run followed the reviewed
[pilot specification](../../../notes/research_mixed_attached_last_row_face_pilot.md)
and [driver](../../../experiments/pilot_mixed_attached_last_row_face.py).
It examined exactly the own-type-three face

\[
 c=.391+i(-.072+.093t),\qquad
 a=.30-.052i+.060\rho e^{2\pi i\theta}\in A_4,
 \qquad(t,\rho,\theta)\in[0,1]^3,
\]

with both original conditional orientations, all four revived carrier
branches, the original halfweight allocations and every target real
pair in \([.22,.45]^2\). No other face or type was run.

The hard limits were 511 visited nodes and 30 seconds. The node cap
ended this sole run after about 2.03 seconds:

- 233 parameter boxes passed the original whole-box root witness and
  all 24 target/carrier acceptance inequalities;
- 17 boxes were rigorously outside the type-four clipping rectangle;
- 12 boxes remain pending; their full exact addresses and intervals
  are saved;
- the accepted and excluded parameter volume is exactly
  \(69/8192\), and the pending volume is \(8123/8192\);
- no outward positive midpoint satisfying the clipping constraints
  was encountered.

The volume statements concern the **unit parameter cube**, not the
Euclidean volume of the clipped reference domain. All accepted upper
bounds were below \(-.01067\), but this is only a bound on the accepted
boxes. The depth-first traversal reached accepted boxes with
\(t\in[13/16,1]\), \(\rho,\theta\in[3/4,1]\).
In particular it did not settle the low-height end of the type-three
chord. The negative accepted bounds must not be extrapolated to the
remaining boxes.

The result binds 26 current inputs, the reviewed proof and the driver.
The exact dyadic accepted/excluded/pending partition has total volume
one. The timer protects the short bookkeeping commits so an interrupted
box cannot be counted twice or lost from the pending partition.
There is no continuation or broadened run in this archive.

Record SHA256:

```text
e29d6ef790302176ebac223507bb0e849384a27292bd53d8a9c638c7602cd06a
```

Reproducing this command repeats only the same bounded pilot:

```sh
python3 experiments/pilot_mixed_attached_last_row_face.py --precision 256 --output repro/diagnostics/2026-11-05-attached-last-row-face-pilot/result.json
```

The geometric domain is a sufficient enclosure for the length-three
two-attached-input case described in the
[actual-reference reduction](../../../notes/research_mixed_actual_last_row_reference_domains.md).
It is not a claim that every independent point on this face is realized
by an actual word. This incomplete pilot proves neither a full last-row
comparison nor a finite-source noncancellation statement.
