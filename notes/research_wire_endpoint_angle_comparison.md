# Angle comparison for original wire-endpoint strata

Private written proof, 17 November 2026.

Deleting a wire at its zero endpoint retains both vertex equations.
This differs from deleting a vertex or making its charge zero. We
prove a uniform strict angle-action gap for every such nonempty
wire deletion. For a mixture of zero and middle endpoints, an exact
incidence-capacity test identifies the assignments which admit the
same comparison. An explicit signed defect formula applies without
that test. These are comparisons of the original angle functional;
they are not a decomposition or bound for a quantum integration cycle.

## 1. Original variables and the parent solution

Fix a finite graph of original same-index edges, a selected vertex
set \(S\), and real signed powers \(n_v\), \(v\in S\).
Every included edge has a selected endpoint, and every selected
vertex has positive original degree. Parallel edges and loops are
allowed; a loop has two endpoint incidences. All outside angles
are complete: \(t_b=0\). No knot interpretation of an arbitrary
graph is asserted.

For an edge oriented from \(v\) to \(w\), put
\[
 t_v=s_v+ih_v,\qquad r_{v,e}=k_{v,e}+ig_{v,e},
\]
\[
 A_{P,e}=s_v/4-g_{w,e}/2,\quad
 A_{Q,e}=s_v/4+g_{w,e}/2,\qquad
 y_{P,e}=g_{v,e}/2+s_w/4,\quad
 y_{Q,e}=g_{v,e}/2-s_w/4.
 \tag{1}
\]
For a loop, the two symbols \(g_{v,e},g_{w,e}\) mean its two
distinct incidence coordinates, with the same vertex angle.
Outside real angles are zero, but their incidence coordinates
remain present. The closed ambient angle body \(\overline{\mathcal X}\)
is defined by
\[
 |s_v|\le\pi,\qquad
 |s_v|+2|g_{w,e}|\le\pi,\qquad
 |s_w|+2|g_{v,e}|\le\pi.
 \tag{2}
\]
Its interior uses strict edge inequalities. These are exactly the
two original closed squares in (1). There are no filling constraints
in the definition of the ambient body.

Write \(E_\square\) for the original normalized convex square
energy and define
\[
 \mathcal E(X)=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 \rho_v(X)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,
 \qquad M_\infty=4G_{\rm Cat}/\pi.
 \tag{3}
\]
Assume a supplied positive parent solution \(X^*\) satisfies the
original full complex unit equations
\[
 \sum_{e\ni v}r_{v,e}-in_vt_v/2=-\pi i
                         \quad(v\in S).
 \tag{4}
\]
All branches and constants are the original ones. By [V,S],
\[
 d\mathcal E(X^*)=\sum_v h_v^*\,d\rho_v,
 \qquad \rho_v(X^*)=-\pi,
 \qquad M_G=|E|M_\infty-\mathcal E(X^*)/\pi.
 \tag{5}
\]
The same identities hold on this arbitrary fixed graph: the
one-edge differential is summed over its actual incidences, and
the real part of (4) supplies each selected angle coefficient.
At an outside incidence its coefficient is the prescribed height
zero. No tree decomposition is used in this calculation.

Let
\[
 D_*(X)=\mathcal E(X)-\mathcal E(X^*)
                    -d\mathcal E(X^*)(X-X^*),\qquad H_v^*=-h_v^*.
 \tag{6}
\]
The square energy is continuous on its closed square and strictly
convex in its interior. The square-coordinate map is injective
because every original selected vertex has an incidence. Thus
\(D_*\ge0\) on the whole compact body, with equality only at
\(X^*\), including its boundary [S, Section 2]. In square-coordinate
Euclidean norm, [V, (35)--(39)] also gives
\[
 D_*(X)\ge\kappa\|X-X^*\|_2^2,\qquad
 \delta=\min_\nu(\pi/4-|X^*_\nu|)>0,
 \qquad \kappa=\frac\delta\pi\sin^2\delta>0.
 \tag{7}
\]
Here and below \(X\) inside this norm denotes the vector of all
four square coordinates per edge.

The original one-edge angle-volume and its normalized value are
\[
 V_e(X_e)=8G_{\rm Cat}-8(E_{P,e}+E_{Q,e}),\qquad
 v_e(X_e)=V_e(X_e)/(2\pi).
 \tag{8}
\]
They are nonnegative on the closed squares and strictly positive
when both squares are interior. Indeed \(E_\square\) has the
constant boundary value \(G_{\rm Cat}/2\) [S, (18)], and is
strictly below that value in the interior by convexity. At zero
incidences, the original real-angle action satisfies
\[
 v_e(s_v,s_w,0,0)=\psi(s_v,s_w).
 \tag{9}
\]
This follows from [V, (1)] at real angles. Its continuation to
\(|s_v|,|s_w|\le\pi\) is nonnegative and is positive if both
absolute angles are less than \(\pi\). Thus (9) fixes the constant,
not just the derivatives, of this real function.

## 2. The endpoint pattern and its angle action

Let \(E_0,E_m\) be disjoint sets of edges, put
\(D=E_0\cup E_m\ne\varnothing\), and let \(m_v\) be the number
of \(E_m\)-incidences at \(v\). The original low Newton summand
at index zero is exactly \(e_0(w)e_0(w')=1\), by the empty
products in [F, (1)]. At its middle
endpoint, the growing lower-half exponential at both parities is
\(e^{iN(t_v+t_w)/2}\), with action \(i(t_v+t_w)/2\), as calibrated
in [M, (2)--(4)]. The full finite middle polynomial, its other
exponential and its prefactor are not identified with this action.

Accordingly the specified endpoint-phase expression is
\[
 \Phi_B(t)=\sum_{e\notin D}\psi(t_v,t_w)
       +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
       -i\sum_{v\in S}c'_vt_v,
 \qquad c'_v=1-m_v/2.
 \tag{10}
\]
Complete outside ends contribute zero to the middle linear term.
Every selected vertex is retained in (10), even when deletion
makes it isolated. This is an exact identity between the displayed
classical phases; no assertion that a quantum contour has such a
boundary decomposition is made.

Let \(\mathcal B_D\) be the closed set of surviving angle
assignments \(X_B\) satisfying the weak inequalities for all
remaining edges and
\[
 |s_v|\le\pi\quad(v\in S),\qquad
 \sum_{\substack{e\ni v\\e\notin D}}g_{v,e}-n_vs_v/2
                  =-\pi(1-m_v/2).
 \tag{11}
\]
The explicit angle bound applies also to isolated vertices. The
set is compact and can be empty. Define its angle action by
\[
 M_B(X_B)=(|E|-|D|)M_\infty-\mathcal E_B(X_B)/\pi.
 \tag{12}
\]
If \(X_B\) is supplied by a regular positive critical point of
(10), then \(M_B=\Re\Phi_B\), by the incidence-by-incidence
calculation in [V, Section 4]. It needs neither a complete outside
end in each retained component nor a path of fractional-charge
solutions. An isolated critical vertex obeys \(n_vt_v=2\pi c'_v\):
if \(n_v\ne0\), its angle is real and its contribution to the
real action is zero; if \(n_v=0\), existence requires \(c'_v=0\)
and its phase contribution is again zero. No critical interpretation
is imposed on a general member of \(\mathcal B_D\).

## 3. The exact extension test

An extension retains all surviving coordinates and restores only the
deleted incidence variables, with the original unit rows \(\rho_v=-\pi\).
Such an extension exists if and only if
\[
 \boxed{\qquad
 m_v\le\sum_{\substack{e=vw\in D\\\text{incidences at }v}}
                  (1-|s_w|/\pi)\quad(v\in S).
 \qquad}
 \tag{13}
\]
All occurrences, including two occurrences of a loop, are counted.

To prove this, subtract (11) from the original row. The required
restored sum is \(-\pi m_v/2\). Each restored incidence has the
independent allowed interval
\[
       -\frac{\pi-|s_w|}{2}\le g_{v,e}
                              \le\frac{\pi-|s_w|}{2}.
 \tag{14}
\]
Their Minkowski sum contains the target exactly under (13).
Choices at distinct vertices are independent: an edge couples a
given incidence only to the fixed opposite angle, not to the
opposite incidence. At outside vertices choose the restored
incidences zero. This proves necessity and sufficiency.

Equivalently, (13) is
\[
 d_{E_0}(v)\ge\sum_{\substack{e=vw\in D\\\text{incidences at }v}}
                                  |s_w|/\pi.
 \tag{15}
\]
Every pure-zero pattern therefore extends, by taking all restored
incidences zero. A pure-middle pattern extends only when each
opposite angle in these sums is zero. Having
\(c'_v\in\{0,1/2,1\}\) on a degree-two graph does not by itself
prove (13). Neither extension nor flatness is presumed for a
general middle or mixed pattern.

## 4. A uniform strict gap for every extendable stratum

For any extension \(X\) satisfying (13), its rows agree with the
parent rows, so (5),(6),(8),(12) give the exact identity
\[
 \boxed{\qquad
 M_G-M_B(X_B)=\frac{D_*(X)}\pi
                                  +\sum_{e\in D}\frac{V_e(X_e)}{2\pi}.
 \qquad}
 \tag{16}
\]
The restored edges need not be flat. Their nonnegative volumes
strengthen the comparison. The right side is strictly positive:
if its Bregman term vanished, \(X=X^*\), where every restored
edge has strictly positive volume.

There is one positive lower bound independent of the pattern and
of its extendable assignment. Let \(v_\delta>0\) be the minimum
of the one-edge expression (8) over square coordinates whose
four distances from their square sides are at least \(\delta/2\).
This minimum is positive on that compact interior set. If
\(\|X-X^*\|_2\ge\delta/2\), use (7). Otherwise every square
coordinate has margin at least \(\delta/2\), and any one edge
in the nonempty set \(D\) has volume at least \(v_\delta\).
Consequently
\[
 \boxed{\qquad
 M_B(X_B)\le M_G-\varepsilon_*,\qquad
 \varepsilon_*=
 \min\left\{\frac{\kappa\delta^2}{4\pi},
                         \frac{v_\delta}{2\pi}\right\}>0.
 \qquad}
 \tag{17}
\]
This applies to every nonempty endpoint pattern and every assignment
which passes (13). If its feasible set is empty, no assignment is
asserted. In particular (17) holds for **every closed pure-zero
wire-endpoint assignment at unchanged charges**, without requiring
a positive boundary critical point. All original vertex equations,
including isolated rows, are retained.

## 5. The signed half-charge defect without extension

For any \(X_B\in\mathcal B_D\), restore all deleted incidences
as zero, and denote the resulting ambient assignment by \(X^0\).
It always satisfies (2), but its row values remain \(-\pi c'_v\).
Thus
\[
 d\mathcal E(X^*)(X^0-X^*)
       =-\frac\pi2\sum_v H_v^*m_v.
 \tag{18}
\]
Combining (6),(9),(12) proves the exact formula
\[
 \boxed{\qquad
 M_G-M_B(X_B)=\frac{D_*(X^0)}\pi
       +\sum_{e\in D}\psi(s_v,s_w)
       -\frac12\sum_{v\in S}H_v^*m_v.
 \qquad}
 \tag{19}
\]
The formula uses the parent's heights, not those of a boundary
critical point. It is valid with their displayed signs. For a
positive parent unit solution here, \(H_v^*>0\) follows by the
vertex-block reflection proof [S, (8)]: negate \(s_v\) and all
its incidence coordinates, leaving the other blocks fixed.
The squares are exchanged or simultaneously negated, so their
total energy is unchanged. This distinct assignment changes
\(\rho_v\) from \(-\pi\) to \(\pi\). Strict convexity and (5)
give \(0>2\pi h_v^*\). The argument also covers a loop, whose
two square pairs are simultaneously negated. This height sign
is unnecessary for (16),(17). Formula (19) identifies exactly the half-charge work
which would have to be paid if (13) fails. The two remaining terms
are nonnegative, but no sign for their difference with that work
is inferred. The identity is not replaced by a fixed-angle wire
phase comparison at the parent critical point.

There is a useful refinement for high middle-incidence counts.
Independently reflect each selected boundary block with \(c'_v<0\).
These reflections preserve its energy and all weak edge inequalities,
and replace its charge by \(|c'_v|\). They also preserve each
real-angle function in (9). Restore zero incidences after these
reflections and call the ambient assignment \(X^{\rm ref}\).
The same supporting identity gives
\[
 \boxed{\quad
 M_G-M_B(X_B)=\frac{D_*(X^{\rm ref})}\pi
      +\sum_{e\in D}\psi(s_v,s_w)
      +\sum_{v\in S}H_v^*
                        \bigl(|1-m_v/2|-1\bigr).
 \quad}
 \tag{20}
\]
No row is dropped by reflection, including an isolated row.
For integer \(m_v\ge0\), the last coefficient is adverse only
at \(m_v=1,2,3\), where it equals \(-1/2,-1,-1/2\), respectively.
It is zero at \(m_v=0,4\) and positive for \(m_v\ge5\).
Consequently, if
\[
                    m_v\in\{0\}\cup\{4,5,\ldots\}
                                    \quad\hbox{for every }v\in S,
 \tag{21}
\]
every member of \(\mathcal B_D\) satisfies the same bound (17),
even when it fails the original-row capacity test (13).
Indeed all terms in the last sum of (20) are nonnegative.
Apply (7) to \(X^{\rm ref}\); if it is within \(\delta/2\)
of \(X^*\), one deleted edge has volume at least \(v_\delta\).
This is a comparison in the ambient angle body, not an assertion
that the reflected assignment has the original unit rows.

## 6. Scope and coverage

The existing edge-cut comparison deletes an edge while making its
two endpoint charges zero. The split-current comparison [S] deletes
vertices, saturates their angles, and retains its changed-charge
supporting term. The endpoint-current angle-face test pins removed
vertices to \(\pm\pi\); the first-turn capacity test concerns a new
zero-power row. None is the operation in (10),(11), which retains
every vertex and deletes only wires. The independent-incidence
interval method and ambient Bregman method are existing tools; the
new application is the uniform unchanged-row pure-zero wire gap,
its mixed-pattern extension test, and the exact defects (19),(20).

The comparison allows arbitrary fixed signed powers and the stated
graph incidences, provided the positive parent solution is supplied.
It does not establish such geometry for an arbitrary short filling.
It assigns an angle action to every closed comparison assignment,
and a classical critical action only when its geometric realization
has separately been supplied. It gives no bound on a whole deleted
quantum source, negative or singular sectors, aliases, moving wire
currents, the other middle exponential, or the original closing.
In particular no relative-cycle coefficient or scalar lower bound
follows from (17). Frozen notes and public papers are unchanged.

## Complete direct sources

The entire following texts were read and their used implications
checked; all work was written mathematics, source reading and hashes.
No mathematical program, numerical experiment, test or build was run.

* [V: Original action and ambient quantitative comparison](research_positive_edge_volume_identity.md),
  SHA256 669722d49e292bf64d839901b350226b9d878c1b240d148193b09a927ef7b88e.
* [S: Ambient Bregman identity and distinct vertex-deletion comparison](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc.
* [M: Literal middle endpoint and its retained scope](research_filled_path_middle_endpoint_phase_separation.md),
  SHA256 5e13a523b2cc7ccadc6aaf43bde0e277bafd076983a22bf0077b3e3ce9106cd5.
* [F: Original finite low-Newton kernel](research_actual_low_newton_fold_packet.md),
  SHA256 849e626407ed9e9c985d86e10fc93c111a1f305cdc32cb470fafa08c6406edfb.
