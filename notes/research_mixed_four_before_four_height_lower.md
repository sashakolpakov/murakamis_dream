# A sharper lower height for a type four followed by type four

Research geometric extraction, 5 November 2026. This rechecks the
whole original window enclosures on an existing complete cover.
Displayed decimal hulls are not used as evidence. The earlier
source and geometry artifacts remain unchanged.

**Theorem 1.** In every finite cyclic word in types three and four,
if two consecutive type indicators satisfy
\(\epsilon_j=\epsilon_{j+1}=1\), their first right leg obeys
\[
                         -.056<\Im t_j<-.048.
 \tag{1}
\]
This is a bound on the actual original critical point. It asserts
neither a finite-source bound nor a sign for any transport derivative.

Use the five-vertex windows and typed external rectangles of
[the previous four-before-four theorem](research_mixed_four_before_four_height.md):
\[
 (a,b,1,1,c),\quad a,b,c\in\{0,1\},\qquad
 R_3=[.30,.39]+i[-.03,.02],\quad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{2}
\]
The [open-window theorem](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2, gives a unique holomorphic original critical branch on
a neighborhood of the entire external typed bidisk before any
boundary argument. Each rectangle in (2) is strictly inside its
disk. The output being bounded is the middle right leg \(t_2\),
coordinate 5 in
\((s_0,t_0,s_1,t_1,s_2,t_2,s_3,t_3,s_4,t_4)\).

The existing cover consists of all \(8\cdot4\cdot16=512\)
window/external-type/side products, with 4,745 accepted rational
dyadic cells. The new checker decodes every original address,
reconstructs its complete external parameter intervals, and
reevaluates the original ten-variable affine Newton self-map.
Its independent mode uses the separate sine/logarithm and
cotangent primitive. Root proposals are accepted only after
the full weighted self-map and original chamber tests.
There are no new parameter cells or subdivisions.

On every accepted whole cell the new test requires
\[
               \Im t_2>-\frac7{125},\qquad
               \Im t_2<-\frac6{125}.
 \tag{3}
\]
The second inequality also rechecks the original upper bound.
The exact case set, prefix-free mass-one partitions and agreement
with the original author and independent covers are required.
Every input binding and the proof/script hashes are checked again
after the run. No displayed hull is used to accept (3).

For each window, the imaginary part of the already established
holomorphic coordinate \(t_2\) is separately harmonic in its
two external complex parameters. Two minimum principles extend
the lower bound in (3) from products of rectangle sides to the
whole external rectangle product; the upper bound is analogous.
No actual-reference height is used to clip an auxiliary window
image.

Restrict an actual cyclic solution to a five-vertex window whose
middle two types are four. Its external legs lie in (2), and
it solves the identical original logarithmic equations.
Uniqueness identifies it with the branch just bounded. For
periods shorter than five, repeat the period before extracting
the window, retaining every original incidence. This proves (1),
including one- and two-cycles.

The new interval can replace the independent type-four lower
endpoint \(-.057\) only when the next type is four. It is a
geometric input to a subsequent source or derivative comparison;
that comparison still needs its own proof.

Reproduction:

    python3 experiments/certify_mixed_four_before_four_height_lower.py --precision 256
    python3 experiments/certify_mixed_four_before_four_height_lower.py --precision 320 --independent --input repro/results/research-mixed-four-before-four-height-lower.json --output /tmp/research-mixed-four-before-four-height-lower-review.json
