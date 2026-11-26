# The geometric action of the ordinary three/four pair

Research record, 7 November 2026. One prescribed interval computation
encloses the original critical action more sharply than the earlier
analytic lower bound. This makes the independently proved upper bound
for the middle physical sector sufficient. The six lower witnesses
tested in the same run do not themselves prove that upper bound.

## 1. What was computed

The [written protocol](research_mixed_three_four_half_face_witness_protocol.md)
fixes the original six-variable action, its logarithmic branches,
one starting point, 24 Newton proposals, and one inclusion test at
256-bit precision. The proposals only choose rational centers and an
approximate inverse. The subsequent strict contraction test proves
existence of an actual zero in a product of six complex disks.
The disks lie in the original open-word chamber, where the established
uniqueness theorem identifies this zero with the prescribed ordinary
three/four critical point.

The action is the original action of the finite source:

\[
 M=\Re\mathcal F_2(z_*)=\Re\{T_0(a_*)+P_1(a_*)\},
 \qquad a_*=A+ic.
\]

There is no change of additive normalization or of the boundary
observation. The first equality uses the six-variable action in the
protocol; the second is the matching identity in the original plateau
proof. Evaluation on the entire certified coordinate enclosure gives

\[
 2.7049005<M<2.7049012,
 \qquad -.033943377<c<-.033943374.
\]

The less precise rational consequences needed below are

\[
                         M>\frac{27}{10},
             \qquad -\frac7{200}<c<0.                 \tag{1}
\]

These are enclosures of the actual solution, rather than decimal
approximations to a proposed stationary point. The saved result also
contains every rational proposal, the rational inverse, the coordinate
enclosures, and the strict contraction inequalities.

## 2. The diagnostic outcome and a separate consequence

The protocol tests six lower bounds for the proposed half-face
envelope. Each uses one of the two compulsory real private cuts
\(e=27/100,49/100\) and one of the transform parameters
\(t=1/5,1/4,3/10\). All six lie below the certified action.
The diagnostic therefore has its prescribed verdict: **inconclusive**.
It has not found an obstruction to the sufficient criterion.
Lower witnesses below the action do not imply that the whole envelope
is below the action.

There is, however, an independent written upper bound. The
[analytic half-face proof](research_mixed_three_four_physical_half_face_ceiling.md)
establishes, with private main height zero,

\[
                   \mathcal E(1/2;0)<\frac{529}{200}.
\]

Combining this theorem with (1), rather than with the lower witnesses,
gives

\[
                  \mathcal E(1/2;0)<M-\frac{11}{200}. \tag{2}
\]

Thus the sufficient comparison in the
[physical middle-sector reduction](research_mixed_three_four_physical_middle_reduction.md)
is now established. After reserving a fixed part of the strict margin
for the finite-sum and boundary-color tolerances, that reduction bounds
the whole corresponding physical sector below the geometric rate.
This conclusion concerns sampled incoming roots. A continuous contour
still requires its own argument, including the segment joining the
stationary height to the real line.

## 3. The saved computation

The protocol and complete checker received a full root and independent
static review before their hashes and all 52 input files were frozen.
The checker ran once. All six prescribed witnesses were processed;
there were no retries, source-cover evaluations, or unprocessed cases.
The original diagnostic verdict has not been changed.

| Artifact | SHA256 |
|---|---|
| Protocol | `628aace6ce85f5e7a8a19819255efb9fa119fb58d0ad11739bed0b8d64f40ad0` |
| Checker | `eaa699d2d1e01758e923eab77f65cb2226508461e48013b5704e9a509cc935cd` |
| Manifest | `6cab93f7480b7e7aad55efd3a7edabc5804a47b4f25ef8c35cb183ff94912493` |
| Result | `fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70` |

The [manifest](../repro/protocols/research-mixed-three-four-half-face-witnesses.json)
binds the exact inputs. The
[result](../repro/results/research-mixed-three-four-half-face-witnesses-attempt01.json)
records the computation and its failure inventory, which is empty.
Subsequent review checked the saved evidence and its source
identification without running the computation again. This result
does not assert a new knot family or the finite-exceptions theorem.
