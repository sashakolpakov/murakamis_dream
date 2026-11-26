# A regular half-twist matrix for two equal-trace meridians

1 November 2026. Private local algebra, for the marked geometric adapter.

Let A,B be determinant-one 2 by 2 matrices over a characteristic-zero
field, with tr A=tr B=m. Put C=AB and H=C-I. Assume tr C is not 2.

Cayley-Hamilton gives A²=mA-I and B²=mB-I. Therefore
\[
 HB=AB^2-B=mAB-A-B=A^2B-A=AH.
\]
The matrix H commutes with C. Consequently
\[
 HBH^{-1}=A,\qquad
 HAH^{-1}=CA^{-1}=ABA^{-1}.
\]
Conjugation by H implements the Hurwitz action
\[
                  (A,B)\longmapsto(ABA^{-1},A).
\]
Its inverse implements the inverse half twist. This statement concerns
the stated based generator convention; its direction must be matched
to the actual diagram before use.

Cayley-Hamilton applied to C gives
\[
 H^2=(C-I)^2=(\operatorname{tr}C-2)C,\qquad
 \det H=2-\operatorname{tr}C.
\]
Thus H is a projective square root of C without choosing a singular
scalar square-root normalization. At the auxiliary complete lift
tr C=-2, det H=4, so this construction is regular.

If the eigenvalues of C on the chosen two flags are -Q and -Q^{-1},
the corresponding eigenvalues of H are -Q-1 and -Q^{-1}-1. Their
ratio is exactly Q. The projective multiplier of C is Q², whereas
the multiplier of the half twist is Q. With Q=e^{i tau}, the local
logarithmic change is half the primitive longitude period 2i tau,
with sign reversed for the inverse half twist. The logarithms are
continued from the original flags, not reset after applying H.

The hypothesis on the two main meridians is only equality of trace.
It allows a nonparabolic main meridian with trace M+M^{-1}. The
lemma may therefore extend the old odd-seam identification to that
deformation, provided its generator ordering and original seam paths
are matched. It does not by itself identify those words or the
global preferred longitude.
