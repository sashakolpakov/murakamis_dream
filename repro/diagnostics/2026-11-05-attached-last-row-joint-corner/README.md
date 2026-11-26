# One exact joint-domain corner: negative last-row maximum

This archive checks **one fixed auxiliary reference**, with outward
256-bit arithmetic. It is not a parameter cover or an actual-word
realization. No neighborhood estimate or uniform clipped-domain sign
is asserted.

The exact inputs, in the original map order, are

\[
 c=\frac{391}{1000}-\frac9{125}i,
 \qquad
 a=\frac3{10}+\frac{\sqrt{29}}{250}-\frac{27}{250}i.
\]

Thus \(c\) is the lower-right corner of the attached type-three
rectangle, while \(a\) is the right intersection of the type-four
reduced circle with its attached lower height boundary. Membership
in the closed \(A_3\times A_4\) domain is proved from exact
rational/square-root identities. No floating `inside_clip` test is
used to decide the boundary equalities.

The checker validates one original-log coupled root witness, then
uses fourteen fixed mean-value enclosure steps with its same rational
inverse. Both original logarithmic residual enclosures contain zero.
The roots, in the external order \((c,a)\), are approximately

\[
 r_0=.34075754063928+.01343508910295i,
 \qquad r_1=.39510781605061+.02224650808188i.
\]

These are new enclosures for the original coupled map at the displayed
inputs. The roots from the earlier height-only diagnostic are not
held fixed when \(c\) changes.

Both conditional orientations use own flag \(\epsilon=0\):

| Orientation | Index and retained inputs | First halfweight flag | Certified all-target maximum deficit |
|---|---|---|---|
| 0 | \((r_0;c,r_1)\) | \(\eta=0\) | less than \(-.12276826718\) |
| 1 | \((r_1;a,r_0)\) | \(\eta=1\) | less than \(-.01683818017\) |

The deficit is the full revived last-row rate minus the original
allocated affine-quadratic plane, with \(\kappa_0=1/2500000\).
Every carrier \((v,w)\in\{0,1\}^2\) is retained. The
maximum is over all target real coordinates in \([.22,.45]^2\).
For orientation 0, separate target convexity reduces the maximum
exactly to four corners. For orientation 1, the first target function
has second derivative below \(-1/5\); its derivative at the right
endpoint is greater than \(.1076\). It is therefore increasing on
the whole interval, and its unique clipped maximum is at \(.45\).
The other target coordinate is convex, so both endpoints are checked.
All these decisions use outward inequalities, not sampled target
values.

The full maximum enclosure is

```text
[-0.01683818017894141084264042285031958653031368816677234242797163055551923
 +/- 6.15e-72]
```

The result contains 14 checks, 24 current input bindings, the exact
point definition, the original witness, every carrier/target value,
and the certified target-maximum decisions. This negative point check
shows that the joint attached real/height restriction removes the
nearby height-only diagnostic's positive excess **at this point**.
It does not settle the pending boxes of the
[bounded face pilot](../2026-11-05-attached-last-row-face-pilot/README.md).

The inputs lie on boundaries of the sufficient geometric enclosure.
The actual endpoint equations impose further correlations. Nothing
here asserts that this independent pair is an actual open-word
reference, or proves any lower bound or noncancellation for a finite
conditional sum.

The sole author evaluation was:

```sh
python3 repro/diagnostics/2026-11-05-attached-last-row-joint-corner/check_point.py --precision 256
```

If separately requested, saved-witness mode can replay this same point
without a new root proposal:

```sh
python3 repro/diagnostics/2026-11-05-attached-last-row-joint-corner/check_point.py --precision 320 --input repro/diagnostics/2026-11-05-attached-last-row-joint-corner/result.json --output /tmp/attached-last-row-joint-corner-replay.json
```

Source conventions and the target estimates are those of the
[reviewed pilot specification](../../../notes/research_mixed_attached_last_row_face_pilot.md),
the [actual-reference domain reduction](../../../notes/research_mixed_actual_last_row_reference_domains.md),
and the [revived endpoint formula](../../../notes/research_mixed_horizontal_revived_endpoint.md).

Record SHA256:

```text
5e249985e53c31da2894dbdb977f157452d713dfbeaeb6d09e8e22d65afa1b98
```
