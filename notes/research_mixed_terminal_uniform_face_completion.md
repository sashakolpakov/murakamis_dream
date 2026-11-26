# Uniform real-face reserves and the comparison they still require

Research result, 6 November 2026.

The [fixed extraction](research_mixed_terminal_uniform_face_reserves.md)
is complete. It gives finite upper bounds for all nine real-boundary
families in each of the four canonical terminal families. These are
bounds over the varying boundary input, not just the four central
references. They remain relative to the terminal supporting plane;
the effect of joining the neighboring block must still be bounded.

## 1. Statement and source domain

Use the external flag \(\beta\), terminal flag \(\epsilon\), and
canonical suffix of the extraction note. The actual reduced external
domains are \(K_3,K_4\), as defined in
[the source-domain lemma](research_mixed_terminal_canonical_source_domain.md).
That lemma proves that the canonical suffix satisfies the original
terminal-four inverse and orientation conditions throughout
\(K_{3+\beta}\). It also identifies every actual word suffix of
length at least three whose penultimate block has type four with this
canonical family. The source bounds below therefore apply there;
no additional finite-word realization assumption is imposed.

Write \(T_f\) for a terminal profile with its original penalties,
and \(B_T\) for the allocated horizontal supporting plane. The
nine families are the two real transform cuts, two real private cuts,
their four corners, and the physical right-triangle majorant.
At the common selected height \(H=.01\), define
\[
 R_0=43/1000,\qquad R_1=49/1000.
 \tag{1}
\]
For either terminal type, every one of these profiles except the
type-four private left cut satisfies
\[
 T_f+\max\{-\tfrac12\Re g(a)-\pi H,0\}
                  <B_T-R_\beta.
 \tag{2}
\]
The type-four private left cut has the weaker uniform reserve
\[
 T_{\mathrm{left}}+
       \max\{-\tfrac12\Re g(a)-\pi H,0\}
                  <B_T-1/20000.
 \tag{3}
\]
These comparisons retain all original independent real target
variables and the original internal reference heights.

*Proof.* The exact maximum in each family is taken over every original
source cell intersecting the corresponding complete canonical image
rectangle. There are respectively 72, 49, 45 and 25 such cells in
the case order \((0,0),(0,1),(1,0),(1,1)\). The closed partitions
cover each rectangle exactly. None of the required jobs has a null
maximum. The source-domain lemma supplies the original hypotheses at
every canonical reference in the reduced external domain.

The least bare reserves, excluding the type-four private left cut,
have the following conservative rational lower bounds. The displayed
decimals are terminating rationals rounded downward from the saved
reserves, and each is strictly larger than the corresponding constant
in (1).

| External flag | Terminal flag | Least reserve is greater than | Attaining family |
|---:|---:|---:|---|
| 0 | 0 | \(.054655\) | physical right-triangle majorant |
| 0 | 1 | \(.043856\) | left real transform cut |
| 1 | 0 | \(.052993\) | physical right-triangle majorant |
| 1 | 1 | \(.049433\) | left real transform cut |

The two type-four private-left reserves exceed \(.000050970\) and
\(.000065238\), respectively, both greater than \(1/20000\).
All comparisons use the exact rational saved endpoints. The original
selected-height transport for these nine families preserves the bare
reserve after halfweight allocation, proving (2)--(3). \(\square\)

## 2. What these estimates establish after joining

If the joined-plane defect has a valid uniform ceiling
\(E_{\beta,\epsilon,\nu}^+\), the
[halfweight allocation](research_mixed_terminal_reserved_plane_transfer.md)
gives, for the profiles in (2),
\[
 \sup D_{\beta,\epsilon,\nu,f}
           <E_{\beta,\epsilon,\nu}^+-R_\beta.
 \tag{4}
\]
Thus a ceiling below \(49/1000\) would settle all these real-face
comparisons for a type-four external input. The private left cut
requires a separate argument: its much smaller reserve cannot pay
such a ceiling. The separate
[private-left theorem](research_mixed_terminal_private_left_symmetric_transfer.md)
now proves the needed optimizer restriction and retains the same scalar
costs as the main comparison. It gives a direct raw gap \(51/20000\)
over the admissible \(K_4\) family.

The [uniform joined-plane protocol](research_mixed_terminal_uniform_joined_plane.md)
keeps the dependence on the common boundary parameter when estimating
this ceiling. Its outcome is separate from the extraction. Neither
(2) nor (3) alone compares every contribution with the joint geometric
action, and neither gives a complete finite-source or knot theorem.

## 3. Reproducible evidence

The [saved result](../repro/results/research-mixed-terminal-uniform-face-reserves.json)
has SHA256
37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3.
It records all 36 bounds, 1,719 selected-job reads, all cell
intersections and attaining jobs, and 496 unchanged input bindings.
The preceding complete verification of 70,254 source jobs is reused
with its source records unchanged. The extraction used no new root,
source or analytic evaluation, and created no new parameter cells.
