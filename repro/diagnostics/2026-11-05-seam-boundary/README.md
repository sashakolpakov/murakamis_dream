# Seam-boundary diagnostics — not certificates

This archive preserves the exact scripts and outputs of bounded floating
experiments on 5 November 2026. None supplies a universal inequality or
a full-period asymptotic. In particular, subtracting two estimated
incoming maxima does **not** produce an upper bound.

The original scripts retain their `/tmp` helper imports. They are archived
unchanged for provenance. The manifest records every original path and
SHA-256. Reproduction requires those helper files at the recorded paths;
do not overwrite unrelated files or treat this archive as a registered
proof check.

The three main experiments are:

* `diagnose_seam_three_step_closure.py`: 18 bounded searches over four
  independent neighboring real coordinates and the seam attenuation,
  with all endpoint selections. It evaluates the genuine but loose
  three-entry/three-exit upper proxy using exact virtual halos. The
  largest candidate is positive, about 0.76958.
* `diagnose_seam_common_incoming.py`: only two fixed configurations,
  using the **same** incoming functions at depths 3, 4 and 5. The
  alternating example remains positive when compared with the universal
  constant gap; the homogeneous-four example is negative. These are
  differences of estimated suprema, not bounds on the true potential.
* `diagnose_real_seam_half_pair.py`: the two original real endpoint row
  profiles on the complete interval of row fractions. The exact formulas
  are `f_e(u)=J(u+1/2)-(1+e)J(u)`, and the upper half is the negative
  reflection of the lower half. The scalar maxima have exact algebraic
  locations. The numerical evaluation is floating, not outward.

The last output distinguishes three comparisons at the alternating
example, all using its actual correlated critical reference:

1. Universal already-finite gap `G+Q`: net estimate about **+0.09652**.
2. Actual geometric plane minus the existing constant raw-source ceiling,
   including the fixed collar cost: about **−0.13551**.
3. Actual plane minus the angularly retained endpoint profile, including
   the same collar cost: about **−0.36395**.

Thus both the geometric-plane dependence and the angular source savings
were discarded in the first comparison. The negative estimates do not
establish a common-potential inequality.

For a general type star `(alpha,beta,gamma)`, the existing constant pair
source ceiling is

`A[beta,alpha] + B[gamma] + 2*Delta_rho + beta*nu_rho`.

It must be compared with the **actual** complex tangent plane
`Re(C + P_L*z_L + P_R*z_R)`. A second subtraction of `Q` is incorrect:
`G+Q` was a coarser preproved lower bound for that actual pair gap.
The moving chirp, middle Fourier factor, selected moduli and both level
parities remain in the source formulas.
