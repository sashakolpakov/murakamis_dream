# The outgoing type-three half row at the second selection

Research theorem, 6 November 2026.

The two main/right-half-row comparisons are now proved when the first
two blocks have type four and the third has type three. The estimates
hold throughout the entire geometric reference family, with every
retained real target free on its original interval. Their uniform
deficit is greater than \(1/20\). Together with the completed central
comparison, this bounds the entire two-factor finite product incident
to the second selected coordinate.

## 1. The original half-row defect

Use the primitive \(g\), canonical reference
\(r(c)=(a_*,u_*,z_*,v_*,b_*)\), and allocated phase \(F\)
of the [central completion](research_mixed_second_selected_central_completion.md),
with \(\alpha=1,\beta=0\). The next external leg \(c=s_4^*\)
belongs to \(K_3\) or \(K_4\); the word has length at least four.
Set
\[
 P=[.22,.45],\qquad H=1/100,\qquad
 p_L=F_a(r),\quad p_R=F_b(r),\quad M=\Re F(r).
 \tag{1}
\]
The internal derivatives \(F_u,F_z,F_v\) vanish at the original
reference. The boundary derivatives do not generally vanish.

For the bare ordinary phases
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                         -g(a)-g(b)+2\pi ias,
 \tag{2}
\]
put
\[
 \begin{split}
 a&=x_a+i\Im a_*,\quad u=x_u+i\Im u_*,
       \quad z=x_z+iH,\quad b=x_b+i\Im b_*,\\
 \Xi_\nu&=Q_1(u;a,z)+Q_0(1/2;z,b)-\tfrac12g(a)-\nu g(z),\\
 D_{R,\nu}(c;x)&=
   \Re\{\Xi_\nu-p_L(a-a_*)-p_R(b-b_*)\}-2\nu\pi H-M .
 \end{split}
 \tag{3}
\]
Here \(\nu=1\) denotes the factorial alternative and \(\nu=0\)
the forced alternative. The target interval is
\[
             x\in P\times[1/8,1/2]\times P\times P.
 \tag{4}
\]
The outgoing coordinate \(b\) has no allocated factorial halfweight
because its type is three. Its original tangent \(p_R\) is still
subtracted.

**Theorem 1.** Uniformly in \(c\in K_3\cup K_4\), in (4),
and in both alternatives,
\[
                         D_{R,\nu}(c;x)<-\frac1{20}.
 \tag{5}
\]
The assertion compares the complete coupled half-row phase to the
original geometric reference. It does not assert that the half row
of one bare factor is pointwise smaller than that factor's main contour.

## 2. The boundary estimate retains the original action

The [half-row budget](research_mixed_second_selected_half_row_budget.md)
first restricts the left index to \([.22,.5]\) by its proved
positive-gradient barrier. At the trial \((a_*,u_*,z_H^*,b_*)\),
where \(z_H^*=\Re z_*+iH\), the exact relative value is
\[
 \begin{split}
 T_\nu=\Re\{&
 g(u_*+z_H^*)-g(u_*+z_*)
 +g(1/2+z_H^*)-g(v_*+z_*)\\
 &+g(1/2+b_*)-g(v_*+b_*)
 -2[g(1/2)-g(v_*)]\\
 &+3g(z_*)-(2+\nu)g(z_H^*)
       +2\pi i[\tfrac12z_H^*-z_*v_*]\}-2\nu\pi H .
 \end{split}
 \tag{6}
\]
In particular the original reference term at \(v_*\), the chirp,
and the exact complex constant \(g(1/2)=i\pi/8\) remain in
the expression before its real part is taken.

Write \(U=e^{-2\pi iu_*}\), \(Z=e^{-2\pi iz_*}\),
\(V=e^{-2\pi iv_*}\), \(B=e^{-2\pi ib_*}\), and
\(\lambda=e^{2\pi(H-\Im z_*)}\). The three nonzero trial
gradients are
\[
 A=\log\left|\frac{1-\lambda UZ}{1-UZ}\right|,\quad
 P_\nu=\log\left|\frac{(1-\lambda UZ)(1+\lambda Z)}
                         {(1-\lambda Z)^{2+\nu}}\right|,\quad
 D_b=\log\left|\frac{1+B}{1-VB}\right|.
 \tag{7}
\]
The left index contributes its original convex conjugate
\(\phi_u^*(A)\). The joint Hessian inequality gives lower
curvatures \(32/5,69/10\) for the two selected-coordinate
potentials and \(57/10\) for the outgoing potential. Their
clipped quadratic conjugates therefore give the upper bound
\[
 \sup_x D_{R,\nu}\le
 T_\nu+\phi_u^*(A)
 +\Gamma_{\mu_\nu}(P_\nu;.22-\Re z_*,.45-\Re z_*)
 +\Gamma_{57/10}(D_b;.22-\Re b_*,.45-\Re b_*),
 \quad \mu_0=32/5,\quad\mu_1=69/10.
 \tag{8}
\]
Every quantity in (6)--(8) belongs to the same reference. Both
alternatives are bounded on the whole selected interval \(P\).
The [evaluation specification](research_mixed_second_selected_half_row_evaluation.md)
proves the exact signed endpoint rule used to bound each quadratic
conjugate over its force and center enclosures.

The [completed boundary calculation](../repro/results/research-mixed-second-selected-half-row-boundary-attempt01.json)
evaluates (8) on all 785 saved outgoing-type-three reference
intervals: 388 for \(K_3\), and 397 for \(K_4\). The 58
remaining terminal intervals have the original strict geometric
exclusions. The full nine-chart boundary partitions and reference
associations are inherited from the already certified central cover.
No root, new reference derivative or subdivision is used.

All 1570 branch bounds are finite and negative. Taking the minimum
deficit over the entire boundary and both alternatives gives the
following weaker rational bounds. The response bounds come from the
original central certificate and are taken independently over each
entire boundary:

| Domain | Boundary deficit \(\gamma_R\) is greater than | Response upper bound \(B_0\) is less than | \(R^2/2\) |
| --- | ---: | ---: | ---: |
| \(K_3\) | .068 | 1.645 | .0034445 |
| \(K_4\) | .077 | 2.055 | .0018 |

These terminating decimals are exact rationals.

## 3. The unchanged response controls the interior

The [half-row extension theorem](research_mixed_second_selected_half_row_boundary_extension.md)
applies to (3). Its holomorphic target phase is
\[
 \widehat\Psi_\nu(a,u,z,v,b)
       =F(a,u,z,1/2,b)+(1-\nu)g(z)+2\nu\pi iz,
 \tag{9}
\]
which is independent of the formal coordinate \(v\).
Its four-variable real Hessian is nonpositive by the same half-row
budget that proves (8). The original stationary equations consequently
give, at each fixed real target,
\[
 \Delta_c D_{R,\nu}\ge-2\mathcal B(c),\qquad
 \mathcal B=|p_L'a_*'|+|p_R'b_*'|.
 \tag{10}
\]
This is exactly the previously certified boundary response. The
original strict height conditions extend from the full boundary to
the interior by the harmonic maximum and minimum principles. The
subharmonic response and disk barrier argument therefore give
\[
 D_{R,\nu}\le-\gamma_R+\frac{B_0R^2}{2}.
 \tag{11}
\]
The two conservative corrected deficits from the table are
\[
                .0623337975,\qquad .073301.
 \tag{12}
\]
Both exceed \(1/20\). This proves (5) on the restricted left-index
interval; the original gradient barrier restores (4).

## 4. The finite product and its scope

The [four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
retains main/main and main/right-half-row profiles, each with both
original Fourier alternatives. The central completion gives a gap
greater than \(1/100\) for the former, and Theorem 1 gives a gap
greater than \(1/20\) for the latter. The other profiles are already
dominated or have the joint right-last-row gap \(1/400\).
Consequently, for every \(\tau>0\), the exact product satisfies
\[
 \begin{split}
 &|C_{1,N}(X_1,X_2)C_{0,N}(X_2,X_3)
            d_N(X_2)X_2^{-N}|\,|d_N(X_1)|^{1/2}\\
 &\hspace{20mm}\le
       C_\tau N^{A_\tau}
       \exp\{N(\Lambda_{23}-1/400+\tau)\}.
 \end{split}
 \tag{13}
\]
Here \(\Lambda_{23}\) is the original geometric action with both
boundary affine terms. Position one and position three remain
unselected; the real targets are free on \(P\). Both level
parities and all original finite rows are included.
For fixed \(\tau<1/800\), the spare exponent absorbs the polynomial
and gives finite gap \(1/800\).

The [standalone driver](../experiments/certify_mixed_second_selected_half_row_boundary.py)
and its [boundary specification](research_mixed_second_selected_half_row_boundary_evaluation.md)
record the complete calculation. Its result has SHA-256
4911ec98e375e034fa1830a35f710635b9afc8944352faf58a5cc598f062aaba.
The result binds 88 inputs and retains every scalar witness, the
785 reference associations, all terminal geometry, and the separate
global phase and response extrema.

The [exact saved-data checker](../experiments/check_mixed_second_selected_half_row_boundary_record.py)
checks those associations, all nine complete boundary partitions,
the 1570 branch upper bounds, signed quadratic maxima, component
sums, input bindings, and the separate global extrema. Its
[compact record](../repro/results/research-mixed-second-selected-half-row-boundary-saved-audit.json)
has SHA-256
a1c4073d1cb62e1f89c5c9522e42f9a9e474705ab3c3c677ba23ca8f60f1d144.
It also checks the exact weaker table and corrections (12).
No roots, primitive functions or interval providers are evaluated
by that saved-data check.

This completes the outgoing type-three case of the second-selection
local product when the first two blocks have type four. Joining
that product to a cap and suffix requires their original weight
allocation and stationary matching equations. First type three,
simultaneous selection at the first two positions, other boundary
selections, and the regions outside the plateau remain separate.
No full knot-volume or finite-exception theorem is asserted here.
