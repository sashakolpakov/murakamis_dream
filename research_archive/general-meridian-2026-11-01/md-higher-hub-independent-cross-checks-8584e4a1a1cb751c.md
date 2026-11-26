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

## 3. The coupled valence-nine example

I read /private/tmp/md-valence-nine-coupled-two-leaf-compensation.md in full, source SHA256 d7001120374e0932b43a0259f599bcb60657fda91d392e78cad72b426ed0420c. The physical turn identifies equal covariant labels, hence both unturned outputs equal the complementary label. At a moving central hub its neighbor has the constant quotient. The two-leaf branch at a low ordinary output forces both actual inputs low, so the retained coefficient cone really has the positive old profile used in the bound; a generic J-only branch estimate would not suffice for this step.

The norm bound, eight low coefficient costs, and original neighboring profile give precisely \(16g(1/5)+f_2(1/5)\). The coupled pressure witness adds no cap volume. Its two strict elementary estimates are correctly normalized: \(g(\arctan(8)/\pi)<1/4\) and \(f_2(1/2)-f_2(1/5)>131/512\). Thus the printed gap is greater than \(3/512\), even before the additional positive \(16(G_0-g(1/5))\). The neighborhood statement is continuity of this same coupled bound, not a claim for all tuples or arbitrary moving neighbors.

## 4. The old complete physical-edge half bound

I read /private/tmp/md-old-bare-tree-complete-edge-half-bound.md in full, source SHA256 a30f1e1d396511675c2c9368720a874f551faebc9cbe27776e65eb6cc51c9ff2. Cutting a physical edge makes each side an unturned product of at least two L/A inputs; turns occur on proper child products. The exact cut pressure is \(f_A(1-z)+f_B(1-z)\). The product identity \(Y^2=(B_1-B)(B_2-B)\le(X-B)^2\), with its positive branch, gives \(f'\ge f_2'\), strictly if either last input is proper. This proves strict decrease of the cut pressure for \(z>1/2\), and excludes equality at half unless each side is exactly one trivalent hub with two rigid leaves. In that exceptional two-hub tree, symmetry of \(f_2\) gives the unique half optimizer.

The statement concerns physical turn edges. It imposes no half bound on hidden unturned-resolution variables and supplies no moving-source estimate. Those qualifications are retained correctly.

## 5. Multiple high incidences at one moving whole hub

I read /private/tmp/md-multiple-high-whole-hub-half-cardinal-comparison.md in full, source SHA256 7caccf46780447ecc622271552b77cd566e4d79263fcd48d8a528db864e1d370. At odd levels \(e_m^2\) is exactly the Hermite projector onto the simple node \(-2\), with trace one: both the top coefficient and all double-node first jets give this normalization. Its powers and the low factors yield the whole-hub boundary action with two or more half incidences. The use of odd levels calibrates a parity-independent continuous action; it does not invent an even simple node.

The moving whole-hub bound uses full J norms and Chebyshev folding, preserving high normals. Its rate is the sum of the low-incidence \(g\) terms. The reassembly assigns each low arm to exactly one old region, possible because the moving hubs are independent along physical turns. The original constants and the two external-arm cases are counted once. The old simultaneous-half theorem applies with at most one mark per surviving old hub. Reinserted half-cardinal hubs lie on original pair-equality faces, so the unique strict complete optimizer gives a fixed compact gap.

The sector hypothesis explicitly excludes other uncontrolled one-high moving hubs. All-low moving hubs have their previously proved positive whole-trace majorant; constant hubs retain their exact positive tensors. No argument uses the false same-index high comparison. Within these stated hypotheses the finite estimate and the source-scope conclusion follow.
