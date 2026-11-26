# The central comparison when the first block has type three

Research theorem, 6 November 2026.

The second-position central estimate now holds when the first block
has type three and the second has type four. The third block may have
either type. The estimate is uniform in all five original real target
coordinates and throughout both permitted external parameter domains.
Both alternatives of the original Fourier polynomial have a deficit
greater than \(1/200\). For an outgoing type-three block the deficit
is greater than \(1/100\).

This is a central phase comparison. The finite-product reduction
also requires its other row and contour estimates; the complete knot
invariant requires further assembly and estimates outside the plateau.

## 1. Reference, target and original phase

Write
\[
 g(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}{2\pi i},
 \qquad V(s,t)=g(s+t)-g(s)-g(t),
 \qquad
 Q_\epsilon(s;a,b)=V(s,a)+V(s,b)-\epsilon g(s)+2\pi ias.
 \tag{1}
\]
Use the original holomorphic branch on \(0<\Re w<1\). Every
argument used below remains strictly inside this strip.
The first three flags are \((0,1,\beta)\), where \(\beta=0\)
means outgoing type three and \(\beta=1\) means outgoing type four.

The [canonical-prefix theorem](research_mixed_second_selected_reference_curve.md)
and its [first-type-three specialization](research_mixed_second_selected_first_three_extension.md)
give a unique holomorphic original reference near each external domain.
In the notation of those proofs, its five coordinates used here are
\[
 r(c)=(a_*,u_*,z_*,v_*,b_*)
      =(r_1,s_2^*,r_2,s_3^*,r_3),\qquad c=s_4^*.
 \tag{2}
\]
For a word of length at least four, \(u_*,v_*\) are ordinary
indices. The next coordinate \(c\) is attached at length four and
ordinary at greater lengths. The private and auxiliary coordinates
remain in the original seven-equation reference system when (2) is
certified.

The allocated phase and its two boundary derivatives are
\[
 \begin{split}
 F_0(a,u,z,v,b)&=Q_1(u;a,z)+Q_\beta(v;z,b)
                              -g(z)-\frac\beta2g(b),\\
 p_L(c)&=g'(a_*+u_*)-g'(a_*)+2\pi iu_*,\\
 p_R(c)&=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \end{split}
 \tag{3}
\]
There is no incoming allocated halfweight. The original stationary
equations give \(F_{0,u}=F_{0,z}=F_{0,v}=0\) at \(r(c)\);
the derivatives in (3) need not vanish.

Put \(H=1/100\), \(P=[.22,.45]\), and
\[
 X_\beta=P\times[1/8,1/2]\times P
                         \times[\ell_\beta,1/2]\times P,
 \qquad \ell_0=3/20,\quad \ell_1=1/8.
 \tag{4}
\]
For \(x=(x_a,x_u,x_z,x_v,x_b)\in X_\beta\), set
\[
 w=(x_a+i\Im a_*,\,x_u+i\Im u_*,\,x_z+iH,\,
                         x_v+i\Im v_*,\,x_b+i\Im b_*).
 \tag{5}
\]
The factorial alternative has \(\nu=1\), and the forced alternative
has \(\nu=0\). Their original phase differences are
\[
 \begin{split}
 \Psi_\nu(w)&=F_0(w)+(1-\nu)g(w_z)+2\nu\pi iw_z,\\
 D_\nu(c;x)&=\Re\{\Psi_\nu(w)-F_0(r(c))
             -p_L(c)(w_a-a_*)-p_R(c)(w_b-b_*)\}.
 \end{split}
 \tag{6}
\]
In particular, the factorial alternative retains its frequency debit
\(-2\pi H\). Both original complex boundary derivatives are subtracted.

The two external domains are
\[
 \begin{split}
 K_3={}&\{|c-(.35-.01i)|\le.083\}
        \cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4={}&\{|c-(.30-.052i)|\le.060\}
        \cap\{-.108\le\Im c\le-.001\}.
 \end{split}
 \tag{7}
\]
All finite decimals in this note denote exact rational numbers.

**Theorem 1.** For \(\beta=0,1\), \(c\in K_3\cup K_4\), and
every \(x\in X_\beta\),
\[
                   \max_{\nu=0,1}D_\nu(c;x)<-\frac1{200}.
 \tag{8}
\]
For \(\beta=0\), the right side may be replaced by \(-1/100\).
These quantifiers include parameters not known to be realized by a
finite suffix; no realization claim is needed for the uniform bound.

## 2. Complete boundary inequalities

The [calculation specification](research_mixed_second_selected_first_three_external_boundary_evaluation.md)
uses the nine original rational charts, with both values of \(\beta\).
The [completed record](../repro/results/research-mixed-second-selected-first-three-external-boundary-attempt01.json.gz)
has 3,046 nodes and 1,532 terminal intervals in eighteen complete
binary trees. Of these intervals, 1,419 carry estimates and 113 are
excluded by strict rational geometric inequalities. There are no
reference-domain exclusions, pending intervals or unresolved intervals.

At every accepted interval, the new original-gradient provider encloses
the canonical first-type-three reference by its full affine residual
bound and the already proved coercivity \(6\pi/49\). Existence
precedes the calculation; a Newton seed is only a proposal. The
analytic Jacobian and certified inverse enclose the derivative with
respect to complex \(c\). The response provider uses these same
coordinate and derivative enclosures to bound
\[
                   \mathcal B_0(c)=|p_L'a_*'|+|p_R'b_*'|.
 \tag{9}
\]
The changed incoming derivative is evaluated explicitly. No
first-type-four reference or numerical response bound is substituted.

The scalar calculation uses the unchanged, proved
[directional majorant](research_mixed_second_selected_directional_budget.md)
and its [guarded curvature refinements](research_mixed_second_selected_curvature_evaluation.md)
at the new reference. The factorial bound uses all \(x_z\in P\).
For the forced alternative it suffices to use \(x_z\in[.4,.45]\):
on the rest of \(P\), the exact inequality
\[
 D_1-D_0=-\Re g(x_z+iH)-2\pi H>0\qquad(x_z<.4)
 \tag{10}
\]
makes the already bounded factorial alternative larger. The original
index barriers justify the reduced ordinary-index optimizations.
The two Fourier alternatives remain an additive bound, not a minimum.

The resulting conservative boundary table is as follows. The deficit
and response extrema are taken separately over the complete boundary
for each fixed flag and domain.

| Outgoing flag | Domain | Deficit \(\gamma\) is greater than | Response \(B_0\) is less than | \(R^2/2\) |
| --- | --- | ---: | ---: | ---: |
| 0 | \(K_3\) | .02327 | 1.637 | .0034445 |
| 0 | \(K_4\) | .02142 | 2.050 | .0018 |
| 1 | \(K_3\) | .01119 | 1.363 | .0034445 |
| 1 | \(K_4\) | .01616 | 1.671 | .0018 |

Here \(D_\nu\le-\gamma\) for both alternatives and all targets,
and \(\mathcal B_0\le B_0\). The
[saved-data check](../repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json)
reconstructs the
chart images, exclusions and full partitions, verifies the reference,
response and scalar associations, and recomputes these separate extrema
from the exact rational endpoints. The complete record preserves every
input binding and arithmetic witness.

## 3. Extension to the interiors

Every accepted interval verifies the strict bounds
\[
 \begin{gathered}
 -.102<\Im u_*<-.001,\qquad -.078<\Im a_*<.021,\\
 (\Im v_*,\Im b_*)\in
 \begin{cases}
 (-.065,.068)^2,&\beta=0,\\
 (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{11}
\]
The actual attached type-three height lies in \((-.072,.021)\);
the containing bound in (11) is the one required by the common
target-concavity theorem. Harmonic maximum and minimum principles
extend the strict boundary margins throughout each closed domain.
Consequently the original target phases are holomorphic and have
nonpositive real Hessian on the entire target image.

For each fixed \(x\), the
[stationary-reference boundary identity](research_mixed_stationary_reference_boundary_extension.md)
therefore gives \(\Delta_cD_\nu\ge-2\mathcal B_0\).
The response is subharmonic, so its complete boundary upper bound
holds throughout the domain. Subtracting the nonnegative disk barrier
\(B_0(R^2-|c-c_{\rm center}|^2)/2\) and applying the maximum
principle yields
\[
                        D_\nu\le-\gamma+\frac{R^2B_0}{2}.
 \tag{12}
\]
This argument includes all straight clipping segments. It is applied
to the original phase before any supremum over targets.

Using the exact rational entries of the table, the four strict
corrected deficits are greater than
\[
 .0176313535,\qquad .017730,\qquad .0064951465,\qquad .0131522.
 \tag{13}
\]
All exceed \(1/200\), and the first two exceed \(1/100\).
This proves Theorem 1. The signed-compensation criterion developed
separately is not an input to this calculation or proof.
