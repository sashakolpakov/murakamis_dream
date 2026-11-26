# The outgoing half row with a first block of type three

Research theorem, 6 November 2026.

When the first three blocks have types \(343\), the right half row
is the remaining comparison in the second-position finite-product
estimate. Both of its original Fourier alternatives now have a
uniform deficit greater than \(1/20\), over the complete external
parameter domains and all four real target coordinates.

The calculation uses the new first-type-three reference family.
It reuses no first-type-four reference values or numerical bounds.
This theorem concerns the half-row term; the finite-product and
restricted plateau conclusions require their separate assembly.

## 1. The target on the real half row

Use \(g,V,Q_\epsilon\), the canonical reference
\[
                 r(c)=(a_*,u_*,z_*,v_*,b_*),
 \tag{1}
\]
and the domains \(K_3,K_4\) from the
[first-type-three central theorem](research_mixed_second_selected_first_three_central_completion.md).
Here the outgoing flag is \(\beta=0\). The reference phase and
boundary derivatives are
\[
 \begin{split}
 F_0(a,u,z,v,b)&=Q_1(u;a,z)+Q_0(v;z,b)-g(z),\\
 p_L&=g'(a_*+u_*)-g'(a_*)+2\pi iu_*,\\
 p_R&=g'(v_*+b_*)-g'(b_*).
 \end{split}
 \tag{2}
\]
Neither boundary has an allocated halfweight in this case.
The original reference equations are
\(F_{0,u}=F_{0,z}=F_{0,v}=0\).

Let \(P=[.22,.45]\), \(H=1/100\), and take real targets
\[
       x_a,x_z,x_b\in P,\qquad x_u\in[1/8,1/2].
 \tag{3}
\]
Their active complex coordinates are
\[
 a=x_a+i\Im a_*,\qquad u=x_u+i\Im u_*,
 \qquad z=x_z+iH,\qquad b=x_b+i\Im b_*.
 \tag{4}
\]
The outgoing index is exactly the real number \(1/2\), rather than
its reference value \(v_*\). For \(\nu=0,1\), define a formal
five-variable phase, independent of its fourth argument, by
\[
 \widehat\Psi_\nu(a,u,z,v,b)
       =F_0(a,u,z,1/2,b)+(1-\nu)g(z)+2\nu\pi iz.
 \tag{5}
\]
The forced alternative is \(\nu=0\); the factorial alternative is
\(\nu=1\). The half-row difference is
\[
 \widehat D_\nu(c;x)=
 \Re\{\widehat\Psi_\nu(a,u,z,v,b)-F_0(r(c))
                      -p_L(a-a_*)-p_R(b-b_*)\}.
 \tag{6}
\]
The unused formal argument \(v\) in (5)--(6) causes no ambiguity.
In particular the original reference subtraction still contains
\(v_*\), and the factorial frequency debit remains \(-2\pi H\).

**Theorem 1.** For every \(c\in K_3\cup K_4\) and all targets
in (3),
\[
                  \max_{\nu=0,1}\widehat D_\nu(c;x)<-\frac1{20}.
 \tag{7}
\]
Both Fourier alternatives use the full selected interval \(P\).
The forced-domain restriction used in the central theorem is not
used here.

## 2. The unchanged scalar inequality at the new reference

The [coupled half-row budget](research_mixed_second_selected_half_row_budget.md)
proves, for both first flags, an upper bound of the form
\[
 \widehat D_\nu\le T_\nu+\phi_u^*(A)
    +\Gamma_{\mu_\nu}(P_\nu;.22-\Re z_*,.45-\Re z_*)
    +\Gamma_{57/10}(D_b;.22-\Re b_*,.45-\Re b_*),
 \quad \mu_0=\frac{32}{5},\quad\mu_1=\frac{69}{10}.
 \tag{8}
\]
Here \(T_\nu\) is the literal relative trial value, \(A\) is the
left-index force, and \(P_\nu,D_b\) are the two remaining real
forces, all defined in that proof from this same original reference.
For a real force \(p\), a positive curvature \(\mu\), and an allowed
displacement interval \([s,t]\),
\[
                 \Gamma_\mu(p;s,t)
                    =\max_{y\in[s,t]}(py-\mu y^2/2).
 \tag{9}
\]
The function \(\phi_u^*\) in (8) is the one-dimensional conjugate
of the original left-index convex cost, with displacement restricted
to \([.22-\Re u_*,.5-\Re u_*]\).

Subtracting the correct \(p_L\) in (2) makes the trial force at the
boundary coordinate \(a\) zero. Its remaining convex cost has coefficient \(1/2\),
is nonnegative, and can be discarded. Thus removing the incoming
halfweight does not change (8). The existing index barrier recovers
the original interval \([1/8,1/2]\) from the restricted left-index
calculation. The reference \(g(v_*)\), the original chirp, and the
complex identity \(g(1/2)=i\pi/8\) remain in \(T_\nu\).

The [arithmetic adapter](research_mixed_second_selected_first_three_half_row_evaluation.md)
uses these unchanged formulas with the new certified coordinates.
It preserves both branches, both signs of each quadratic displacement,
and the exact reference centers. Its metadata distinguishes the new
reference family from the preserved arithmetic helper.

## 3. The complete boundary calculation

The [saved reference bank](../repro/results/research-mixed-second-selected-first-three-boundary-reference-bank.json.gz)
comes from the completed first-type-three central cover. Its
\(\beta=0\) part has 782 accepted intervals: 387 for \(K_3\)
and 395 for \(K_4\). Together with 58 inherited strict geometric
exclusions they form complete partitions of all nine boundary charts.
No reference-domain exclusion is used.

The [half-row record](../repro/results/research-mixed-second-selected-first-three-half-row-boundary-attempt01.json.gz)
evaluates (8) once on each of these 782 intervals. Both branches are
finite and strictly negative at every interval. No root, reference
derivative, parameter subdivision or response calculation is repeated.
The [saved-data check](../repro/results/research-mixed-second-selected-first-three-half-row-boundary-saved-audit.json)
verifies the input associations, literal trial and force arithmetic,
both quadratic optimizations, complete partitions and separate
global extrema.

The resulting conservative boundary bounds are
\[
 \widehat D_\nu\le-\gamma,\qquad
 \mathcal B_0=|p_L'a_*'|+|p_R'b_*'|\le B_0
                     \quad\hbox{on }\partial K_j.
 \tag{10}
\]

| Domain | Deficit \(\gamma\) is greater than | Saved response \(B_0\) is less than | \(R^2/2\) |
| --- | ---: | ---: | ---: |
| \(K_3\) | .073 | 1.637 | .0034445 |
| \(K_4\) | .082 | 2.050 | .0018 |

The response bounds are exactly those of the new central family,
not bounds for the previous first-type-four family. The minimum
phase deficit and maximum response are taken independently over
each entire boundary.

## 4. Extension from the boundary and the finite-product consequence

First restrict the left index to \([.22,.5]\), using the barrier
described in Section 2. On this product the
[generic half-row extension](research_mixed_second_selected_half_row_boundary_extension.md)
applies to (5) with
\[
                       \Lambda_R=\operatorname{diag}(1,1,0,0,1).
 \tag{11}
\]
The negative real Hessian in the four active variables is nonnegative
on the full connecting product. Its formal fourth row and column are
zero. The original stationary identities in (2) therefore give the
same boundary-response inequality as for the central comparison:
\[
                         \Delta_c\widehat D_\nu\ge-2\mathcal B_0.
 \tag{12}
\]
All required height and common-domain bounds were already established
for the new canonical family and extended harmonically in the central
theorem. The clipped-disk barrier hence proves
\[
                     \widehat D_\nu\le-\gamma+\frac{R^2B_0}{2}.
 \tag{13}
\]
The exact rational table gives corrected deficits greater than
\[
                       .0673613535\quad(K_3),\qquad
                       .07831\quad(K_4).
 \tag{14}
\]
Both exceed \(1/20\). The original index barrier gives the same
maximum bound on \([1/8,1/2]\), proving (7) on all of (3).

The central comparison has gap greater than \(1/100\) when
\(\beta=0\). Combining it with (7) and the existing joint last-row
gap \(1/400\), the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
now bounds the complete original two-factor product for a \(343\)
prefix with raw gap \(1/400\). Its first coordinate is unselected.
For a \(344\) prefix the central gap \(1/200\), the existing
outgoing-four half-row domination and the same last-row gap give
the same raw gap. The exact weights and subsequent plateau assembly
are stated separately.
