# A smaller height strip for every cyclic type-three leg

Research proof, 4 November 2026. Frozen manuscripts and completed
localization artifacts are unchanged.

The following bound supplies independent conditional-source domains;
it is a geometric critical-point statement, not a finite-sum estimate.

**Theorem 1.** At the original zero-lift critical point of every finite
cyclic word in three and four, every leg belonging to a three-vertex
satisfies
\[
               .30<\Re z<.39,\qquad -.03<\Im z<.02.
 \tag{1}
\]
All cyclic lengths, including repeated one- and two-vertex patterns,
are included.

Use the original typed disks and open-window potential from
[the proved height theorem](research_mixed_cyclic_critical_height_bounds.md),
Section 2. Its Lemma 2 establishes the unique holomorphic root on the
entire product of the two external typed disks before any image bound
is used. Consider the three-vertex windows
\[
             (\epsilon_1,0,\epsilon_3),\qquad
                         \epsilon_1,\epsilon_3\in\{0,1\}.
 \tag{2}
\]
The two external disk types are independently zero or one. Reflection
reverses all five type labels and exchanges the two legs at every
vertex. There are therefore ten representatives among the sixteen
patterns: four patterns are reflection fixed.

The middle root coordinates are holomorphic on the full external
bidisk. Their real and imaginary extrema lie on its distinguished
boundary, parametrized by two unit-circle angles. The checker covers
that angle square by exact dyadic rectangles. On each rectangle it
uses the unchanged affine Newton primitive from the earlier window
certificate. This retains all six original logarithmic equations,
their tridiagonal Jacobian, and the external linear response. It
produces an enclosure
\[
 z(p)=z_0+D(p-p_0)+w,\qquad |w_j|\le R_j,
 \tag{3}
\]
by the strict componentwise self-map inequalities
\[
 b_i+\sum_j E_{ij}R_j<R_i,
 \quad b_i\ge |(Y\nabla\mathcal W)_i|,
 \quad E_{ij}\ge|(I-Y\mathcal W'')_{ij}|.
 \tag{4}
\]
The residual and Jacobian variation are enclosed throughout the
whole affine parameter rectangle. The original point test makes
the approximate inverse nonsingular. Every root enclosure remains
in the original regular chamber, and both middle coordinates obey
all four strict inequalities in (1). Polynomial or floating root
proposals alone never enter acceptance.

The 192-bit author run passes all ten cases with 8,525 accepted cells.
The separate sine/cotangent replay evaluates the saved cells using
the earlier independent implementation, without importing the author
Newton routine. It also verifies the new upper-height and both
real-coordinate bounds and the complete list of reflection cases.

Successive harmonic maximum and minimum principles extend (1) from
the covered distinguished boundary to each entire external disk
product. To apply this to an arbitrary cyclic word, repeat its period
until the three-vertex window and its two external neighbors occupy
distinct positions. Restrict the repeated original critical point
to the window centered at the desired three-vertex. Its external
legs lie in their original typed disks, and uniqueness of the open
window identifies it with the certified root. This proves (1).

Together with the existing type-four bound, the resulting independent
domains for actual cyclic legs are
\[
 T_3=(.30,.39)+i(-.03,.02),\qquad
 T_4=(.27,.33)+i(-.057,-.001).
 \tag{5}
\]
The small strip in (1) is useful even when the real part of a later
outer integration variable is allowed to range more widely. Such a
source or contour assertion requires its own proof; (1) supplies
only the actual critical heights and positions.

Run:

    python3 experiments/certify_mixed_type_three_window_strip.py
    python3 experiments/replay_mixed_type_three_window_strip.py

The record retains every exact accepted address, verifies all ten
reflection representatives and their full dyadic covers, and hashes
the unchanged Newton primitive and its proof inputs. It performs no
new four-real-dimensional global existence search.
