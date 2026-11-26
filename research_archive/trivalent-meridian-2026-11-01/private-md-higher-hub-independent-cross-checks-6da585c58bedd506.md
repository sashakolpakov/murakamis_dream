# Independent checks of the higher-hub pressure and trace obstruction

1 November 2026. Private record; no repository edits.

## 1. Whole-hub old pressure

I read the full derivation in /private/tmp/md-old-whole-hub-simultaneous-half-pressure.md, Sections 1–6, source SHA256 a5da4e61b4b0c30504f6d03c132a5c34104a49d5aab9bce6f52418f61ccca729.

The strict arity construction works for the fixed original association. At a parent with prescribed output \(b\), the two restricted child ranges have lower-sum endpoint less than one and upper-sum endpoint greater than \(b\). The individual upper bounds are at most \(b\). Their sum interval therefore meets \((b,1)\); the singleton cases satisfy the same strict inequalities without an extra variable. Induction produces the required hidden wire values. This proves the physical half/three-eighths witness without incorrectly assigning three-eighths to artificial complementary edges.

The endpoint barrier is unchanged along an unturned output/input wire and exchanges zero with one along a physical turn. Descent terminates in the finite rooted tree; fixed half terminals cannot be its endpoint. The subsequent gate-face barrier excludes all remaining saturated faces. Strict gate Hessians cover every free variable and every varying marked coordinate, so the full Hessian and its boundary Schur complement are negative definite.

The response induction correctly distinguishes both edge types. A proper product output stays proper as an ordinary next input; a physical turn swaps the two strict inequalities. Fixed half terminals acquire only the incident positive response and no fictitious action. Re-rooting uses the same symmetric cubic resolution, preserving complementary labels on artificial edges and equal labels on physical ones. At the marked half root, the derivative calculation and joint supporting plane give the simultaneous comparison. The small-segment inequality at a closed endpoint and the negative definite Hessian give strictness away from the all-half boundary.

No moving higher-valence estimate follows from this old-pressure theorem alone. The requirement of at most one marked incidence per original hub remains essential to the strict witness.

## 2. Independent divided-difference obstruction

I read /private/tmp/md-one-high-admissible-hub-trace-exponential-obstruction.md, Sections 1–5. Its family and conclusion agree with the independent positive-Laurent proof in /private/tmp/md-complete-admissible-hub-trace-exponential-obstruction.md.

The exact reflection identity is \(B_hB_{a+1}=B_N\), with \(h=4a\), \(N=5a+1\). Together with the sine-product normalization it gives the polynomial cardinal factor and the exact coefficient of the moving relation. Canceling \(B_a^2\) removes precisely the two copies of every upper node \(c_0,\ldots,c_{a-1}\). The remaining multiset has \(3a+2\) nodes, including the added \(c_a\), all at most \(c_a\). Its divided-difference order is \(3a+1\).

After cancellation the numerator is \(B_a^5/S_a^{14}\). All derivatives below \(c_a\) have alternating fixed sign, and the absolute derivative of the required order is minimized at \(c_a\). The simplex formula therefore provides a valid lower bound even at repeated nodes. The sign of the moving coefficient is \((-1)^a\), matching the original coefficient trace at both level parities.

Dividing by the complete trace leaves \(B_a(c_a)^{-2}\) times an elementary symmetric polynomial in five copies of each reciprocal \(c_r-c_a\). Bounding these distances by \(c_0-c_a<3/2\), and using the mode of the binomial distribution with parameters \(5a,3/5\), gives the printed constant \(25000/6561\). All powers of \(N\), signs and factorial normalizations agree. The reverse triangle inequality gives exponential relative growth for every fixed \(\Delta_s\ne0\); a favorable real or imaginary sign is optional.

These arguments refute the proposed complete-admissible pointwise denominator. They do not refute a source-selected coupled-pressure estimate or a whole invariant asymptotic. The two independent proofs require no numerical extrapolation.
