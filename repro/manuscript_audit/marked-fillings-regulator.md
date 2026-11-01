# Bounded marked-filling regulator read

Source: `papers/marked-fillings/main.tex`, SHA-256 `a0d792eea4336ea0bbe7c9c274780539db2b57e80836525210ba16728661000e`.
Scope: Section 7, with the original peripheral definitions and the metric
completion interfaces in Sections 4–6. This is not a fresh audit of every
packing, collar and developing-map step in the complete paper. The adjacent
snapshot records exact current label anchors and lines.

## Concrete issue found and fixed

The original normal-flow polynomial identity did not by itself establish
that its coefficient rows were the actual cusp similarity-log rows. In the
usual ordered display `(infinity,0,1,z)`, both the ambient orientation and
the edge-type assignment differ from the implicit convention in that draft.
There was also no explicit distinction between the symplectic bracket of
coefficient rows and the reduced form on edge-equation tangent vectors.

The current text at `mf:regulator` (line 1024) repairs
both points. It uses the positively ordered model `(0,infinity,1,z)` in
standard upper-half-space orientation: the finite-height determinant is
`H Im z > 0`. The cross-ratio displayed there sends exactly that model to z.
At infinity the outward cusp orientation is the usual complex orientation.
This agrees with the original auxiliary rectangle basis, whose longitude
translation divided by its meridian translation has positive imaginary part.

For u=log z and v=log(1-z^(-1)), the normalized third cusp vertices are
z^(-1), z, (1-z^(-1))^(-1), (1-z)^(-1). The four rows of side logs,
ordered by the other face labels, are respectively

- `(v,-u,0)`;
- `(u+v,u,0)`;
- `(-u-v,-v,0)`;
- `(-v,-u-v,0)`.

I independently obtained these by normalizing each chosen vertex to
infinity and its first two remaining vertices to 0,1. Fixed signs change
only constant multiples of pi*i. Substitution of the zero total flow at
each cusp triangle makes these rows exactly the displayed d_j(r).

The actual multiplier sign is also determined: if a_i is the scale from a
canonical cusp triangle to the common developed chart, a glued side gives
`a_(i+1)/a_i = - side_out(i)/side_in(i+1)`. Around a closed path this
is the product of outgoing sides divided by incoming sides. Thus the
outgoing-flow-weighted row is the actual similarity-log row, not its
negative. In the selected P_- flag sent to infinity, the paper's U,V are
indeed affine similarity logs, twice the selected centered eigenvalue logs.

## Intersection and tangent factor

With this dictionary, the displayed local normal-flow identity is used
with the correct actual rows. Face skew terms cancel under the original
orientation-reversing face identifications. Its global bracket is minus
twice oriented intersection. The edge-row dependency proof gives rank t-c;
small edge circles are null-homologous and have zero bracket with closed
peripheral rows. The primitive rows consequently span the 2c-dimensional
boundary quotient.

The new tangent calculation is explicit. For the block matrix J of the
shape symplectic form and edge-row span E, the actual constraint tangent
space is W=ann(E), with null directions J E^t. If a,b are one cusp's U,V
rows, `a J b^t=-2`. The tangent vectors `-Jb^t/2` and `Ja^t/2` evaluate to
the U,V coordinate basis and have pairing -1/2. Therefore the reduced form
is exactly `-1/2 sum dU wedge dV`, without confusing rows and tangent
coordinates. Applying it to the real shape-log vector and the imaginary
variation gives `mf:volume-differential` (line
1176). Fixed imaginary constants in lifted
peripheral logs have zero real part and zero derivative, as required.

## Absolute action and filling correction

From the actual word identity `d A_epsilon = sum U ddelta` and
`V=-4 pi i delta`, the differential is
`d(2 pi i A_epsilon)=-1/2 sum U dV`. Its imaginary part is
`-1/2(Re U dIm V + Im U dRe V)`. Combining with the established volume
differential proves that
`2 pi Re A_epsilon - V_chain + 1/2 sum Im U Re V` is constant. The source
uses the complete original polyhedral volume to fix that constant to zero;
it does not infer an absolute constant from a tangent identity.

At the critical point `U=4 pi i p delta-2 pi i` and `V=-4 pi i delta`.
For delta=a+ib, the two sides of `mf:boundary-cancel` (line
1211) equal `4 pi p a b - 2 pi b`. Hence the
linear and quadratic filling action cancels exactly the regulator boundary
term. No sign restriction on p is used.

## The same-chain comparison

The comparison uses the original boundary triangulation and the same
peripheral flags. After the auxiliary axis is sent to (0,infinity), both
height functions in the displayed homotopy transform by the same positive
multiplier, and its horizontal coordinate transforms by the same complex
multiplier. On each finite fundamental boundary triangle, the horizontal
derivatives are bounded, while a height derivative is O(Y) and the height
is comparable to Y. Thus the top homotopy prism has hyperbolic volume
O(Y^(-2)), which vanishes on truncation. At a main parabolic cusp the same
estimate is applied to two conical maps with the common translation action;
no axis fixed by a nontrivial translation is assumed.

The primitive killed slope and the exact small-log period identification
from Section 6 permit extension of this same axis-valued triangulation over
the actual solid torus. Added simplices lie on the axis and have zero signed
volume. Stokes on finite truncations therefore identifies the original
ideal-chain volume with the filled representation volume. Comparing this
map with the developing map of the constructed complete metric uses the
same filled fundamental class and the same remaining cusp flags. It does
not replace unrelated ideal vertices by axis points and then assert equality.

The final metric-independence argument is consistent with that definition:
a compact-core-smoothed, affine-conical equivariant map is Lipschitz;
smearing a fixed finite regular tetrahedron has integrable volume and
face-homotopy currents. Congruence of ordered faces and Haar invariance
cancel their alternating boundary contributions. Straightened tetrahedra
have absolute volume at most v3, and the limit of finite regular tetrahedra
provides the two volume inequalities. This does not require a rigidity
equality case.

## Conclusion and retained premises

After the explicit orientation/row dictionary and tangent-quotient repairs,
no further concrete defect was found in this bounded Section 7 read. The
complete positive original triangulation, the full original peripheral
representation, and the primitive smooth metric with exact logarithmic
periods remain earlier written premises of this section. This read checks
how they are used; it does not replace their proofs or claim a formalization
of the whole geometry. The author's finite symbolic checker was not rerun
or counted as independent analytic verification here.
