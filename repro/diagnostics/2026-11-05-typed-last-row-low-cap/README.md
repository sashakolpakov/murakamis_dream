# One low-height typed last-row pilot

This records one authorized 256-bit pilot of the design in
[research_mixed_typed_last_row_support_design.md](../../../notes/research_mixed_typed_last_row_support_design.md).
It stopped at the prescribed **511-node limit**. There was no continuation,
second run, external-input optimization, or sweep of other boundary cases.

The result is **incomplete**: 253 cells were accepted, with 258 binary
splits and six pending boxes. Accepted cells occupy exactly \(5/8\) of
the parameter cube; the pending frontier occupies exactly \(3/8\).
These are parameter volumes, not Euclidean volumes in the complex inputs.
The driver verified the complete address tree, each address-derived dyadic
box, both children of every split, and total terminal-plus-pending volume
equal to one. Its elapsed time was 1.814 seconds, below the separate
30-second cap.

Every accepted cell bounds the complete target square
\([11/50,9/20]^2\), both original conditional orientations, and all four
revived carriers per orientation. The 24 carrier/target envelopes use
whole-box optimizer enclosures and midpoint-only target gains. The largest
accepted upper bound was approximately \(-5.06645419\,10^{-6}\); no
positive fixed trial was certified. Neither fact settles the pending region.

## Exact subset and scope

The own type is three. External input order is type-three \(c\), then
type-four \(a\). Write
\[
\begin{split}
c_-&=49/125-9i/125,\\
h_*&=-49/625+\sqrt{16906}/10000,\qquad
x_*=233/625+3\sqrt{16906}/10000,\\
c(t)&=(1-t)c_-+t(x_*+ih_*),\\
h(u)&=-27/250+(3/500)u,\\
a(u,v)&=3/10+(2v-1)
\sqrt{(3/50)^2-(h(u)+13/250)^2}+ih(u),
\qquad (t,u,v)\in[0,1]^3.
\end{split}
\]
This is the slanted boundary chord of \(K_3\) times the entire bottom
cap of \(K_4\), with \(-.108\le\Im a\le-.102\). The square-root
radicand is at least \(29/62500>0\), so the direct chart has no
singular endpoint and does not require a floating membership test.
The original coupled root and its validated response were retained;
no output leg was replaced by an independent interval.

The whole slanted chord has \(\Im c<-.065\) and \(\Re c>.391\).
It therefore lies outside both actual type-three role domains \(O_3\)
and \(A_3\). This is a test of a sufficient typed envelope. Even a
positive point here would not be an actual-open-word counterexample.
This partial negative result proves no universal sign on the typed
domains, no new finite-kernel conclusion, and no noncancellation theorem.

## Retained frontier

Splits cycle through \(t,u,v\). The visited child is low for \(t,u\)
and high for \(v\), while every other child remains in the saved frontier.
The six unresolved closed boxes are:

| Address | \(t\) | \(u\) | \(v\) |
|---|---|---|---|
| 11 | \([1/2,1]\) | \([1/2,1]\) | \([0,1]\) |
| 1001 | \([3/4,1]\) | \([0,1/2]\) | \([0,1/2]\) |
| 10001 | \([1/2,3/4]\) | \([1/4,1/2]\) | \([0,1/2]\) |
| 100000 | \([1/2,3/4]\) | \([0,1/4]\) | \([0,1/4]\) |
| 1000011 | \([5/8,3/4]\) | \([0,1/4]\) | \([1/4,1/2]\) |
| 1000010 | \([1/2,5/8]\) | \([0,1/4]\) | \([1/4,1/2]\) |

Up to their common boundaries, the accepted union is
\([0,1/2]\times[0,1]^2\) together with
\([1/2,1]\times[0,1/2]\times[1/2,1]\).
Thus the run did reach the intended low-height chart; its incomplete
status is not the earlier right-first pilot's failure to visit low heights.
There were 31 root-enclosure failures and 227 deficit-enclosure failures
among the split nodes. Those failures are interval uncertainties, not
positive mathematical deficits.

## Files and exact run

The [driver](../../../experiments/pilot_mixed_typed_last_row_low_cap.py)
was reviewed before execution. It imports the frozen previous pilot's
original-log root/proposal, Schur, and concave-target helpers; it does
not mutate or rerun that pilot.

    python3 experiments/pilot_mixed_typed_last_row_low_cap.py \
      --precision 256 \
      --output repro/diagnostics/2026-11-05-typed-last-row-low-cap/result.json

Exit status 2 is the driver's explicit incomplete-pilot status.
The [record](result.json) saves all accepted witnesses, every visited
node and pending box, exact chart identity, target intervals, and 29
current dependency bindings. There is no independent replay claim.

| Artifact | SHA256 |
|---|---|
| Design note | 1fe596a46cc050a871f2b8f70427e42e47672de6ede78c79b714056248a3b840 |
| Driver | 7a4bf27dca2f87cf600573ea697f2e55924b8eb2b811664cdff4d81881c29b48 |
| Result | 3032ec6861743b8bd2e73e9d477e90173db847365442640b25c2be8225ce26e4 |
