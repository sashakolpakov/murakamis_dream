# A general convex action gap for split endpoint currents

Private written proof, 15 November 2026.

At an original positive primitive solution, every admitted deleted
angle action associated with a nonzero endpoint current of a suitable
even-factor Ward implementation is strictly smaller than the full
action. The comparison does not require that
the deleted assignment extend to the original unit-charge constraint
face. Instead it uses the supporting affine function of the original
angle energy on the whole angle body. Its charge correction has the
favorable sign.

This is a general geometric comparison for arbitrary signed powers
and arbitrary vertex subsets in a fixed original circle tree. It also
compares every nonzero integer charge of the deleted forest. The exact
finite current is a scalar times that forest, with all original
closures retained. A bound on the complete quantum forest still has
to be proved before the geometric comparison becomes a bound on its
whole current; no contour or geometric coefficient is inferred here.

## 1. The original angle body without the filling constraints

Fix an original finite circle tree, a nonempty selected vertex set
\(S\), and every edge incident to \(S\), counted once. Each selected
vertex has positive original degree. Denote the number of these edges
by \(e_G\). Fix the full outside angles \(t_b=s_b+i h_b\), the signed
integer powers \(n_v\), and the original unit-charge equations
\[
 \sum_{e\ni v}r_{v,e}-\frac{i n_vt_v}{2}=-\pi i
                                        \qquad(v\in S).
 \tag{1}
\]
Assume they have a positive solution on the canonical original edge
branches. In physical filling notation \(n_v=\eta_v-2p_v\); neither
the original marking \(\eta_v\) nor the slope \(p_v\) will be changed.

Write \(t_v=s_v+i h_v\) and \(r_{v,e}=k_{v,e}+i g_{v,e}\).
The variables of the real angle body are the selected \(s_v\)'s and
all endpoint incidences \(g_{v,e}\), including incidences at fixed
outside vertices. The outside \(s_b\)'s stay fixed. Define \(X\) by
the strict inequalities
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi \qquad(e=\{v,w\}),
 \tag{2}
\]
and let \(\overline X\) use their weak versions. There are no filling
constraints in the definition of \(X\). Since the positive solution
belongs to \(X\), it is nonempty, and \(\overline X\) is its compact
closure in the affine space with the outside \(s_b\)'s fixed.

For an edge oriented from \(v\) to \(w\), use the original square
coordinates
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{3}
\]
The square energy is the normalized original function
\[
 dE_\square=x\,dA+B\,dy,\qquad E_\square(0,0)=0,
 \quad
 x=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\quad
 B=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{4}
\]
It is strictly convex on the open square and continuous on the closed
square. Its simultaneous reflection satisfies
\(E_\square(-A,-y)=E_\square(A,y)\), by (4) and normalization.
The full energy, with the prescribed imaginary outside angles, is
\[
 \mathcal E(z)=4\sum_e(E_{\square,P,e}+E_{\square,Q,e})
                    -\sum_{b\notin S}h_b\sum_{e\ni b}g_{b,e}.
 \tag{5}
\]
The square-coordinate map is injective: all selected vertex angles
are recoverable because every selected vertex has an incidence.
Thus \(\mathcal E\) has positive definite Hessian on \(X\), and is
continuous and convex on \(\overline X\). The outside work in (5) is
linear and does not affect this Hessian.

Let \(z_0\in X\) be the original solution. Put
\[
 \rho_v(z)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 h_v^0=\operatorname{Im}t_v^0,\qquad H_v=-h_v^0.
 \tag{6}
\]
The original edge differential and the real parts of (1) imply,
as an identity on the full ambient tangent space,
\[
 d\mathcal E(z_0)=\sum_{v\in S}h_v^0\,d\rho_v,\qquad
 \rho_v(z_0)=-\pi.
 \tag{7}
\]
Indeed the selected \(ds_v\)-coefficient is
\(\sum k_{v,e}=-n_vh_v^0/2\); each selected incidence has
coefficient \(h_v^0\); and each outside incidence has coefficient
\(h_{b,e}-h_b=0\). Thus (7) includes the outside boundary term.

### Lower-half placement

Every \(H_v\) is strictly positive. This already follows from the
proper-prefix theorem: each actual positive return obeys
\(\operatorname{Re}(r_{v,e}\overline{t_v})>0\) when \(t_v\ne0\),
and pairing (1) with \(\overline{t_v}\) gives
\(\sum_e\operatorname{Re}(r_{v,e}\overline{t_v})=-\pi h_v\).
Here \(t_v=0\) would give zero returns and contradict (1).

For a direct convex check, reflect \(s_v\) and all \(g_{v,e}\) at one
selected vertex, leaving every other coordinate fixed. On an edge
where it is the first endpoint, the two squares in (3) are exchanged
and simultaneously negated. Where it is the second endpoint, they
are exchanged. The outside work is unchanged. Thus this reflection
preserves \(X\) and \(\mathcal E\). It is nontrivial at \(z_0\), since
otherwise \(\rho_v(z_0)=0\). Strict convexity and (7) give
\[
 0=\mathcal E(\operatorname{ref}_v z_0)-\mathcal E(z_0)
   >d\mathcal E(z_0)(\operatorname{ref}_v z_0-z_0)
   =2\pi h_v^0.
 \tag{8}
\]
No coordinatewise sign condition on \(s_v\), individual return
imaginary parts, or the powers \(n_v\) is used.

## 2. A supporting gap that allows different charge rows

Define the Bregman remainder at the original point by
\[
 D_0(z)=\mathcal E(z)-\mathcal E(z_0)
                  -d\mathcal E(z_0)(z-z_0).
 \tag{9}
\]
It is continuous on \(\overline X\), zero at \(z_0\), and strictly
positive at every other point of \(\overline X\).
For a boundary point this follows by restricting to the segment
from \(z_0\): its interior lies in \(X\), and the second derivative
in the nonzero segment direction is strictly positive there.
Consequently
\[
                  \delta_0=\min_{\partial X}D_0>0.
 \tag{10}
\]
The boundary is relative to the ambient affine space with the
outside \(s_b\)'s fixed. It is not the boundary of the unit-charge
feasible polytope.

If a weak angle assignment \(z\) has rows
\(\rho_v(z)=-\pi c_v\), then (7)--(9) give the exact formula
\[
 \boxed{\quad
 \mathcal E(z)-\mathcal E(z_0)
              =D_0(z)+\pi\sum_{v\in S}H_v(c_v-1).
 \quad}
 \tag{11}
\]
The \(c_v\)'s in this identity can be any real numbers. They are
the row values of a comparison assignment. No Fourier alias,
peripheral change, or source equality is asserted by changing them.
In particular, if all \(c_v\ge1\), the supporting correction is
nonnegative, and a boundary comparison has at least the gap
\(\delta_0\).

## 3. Every deleted forest and every nonzero charge

Let \(\varnothing\ne C\subseteq S\) and suppose
\[
                              |n_v|\ge2\qquad(v\in C).
 \tag{12}
\]
Delete every edge incident to \(C\). Let \(r_C\) be the number of
deleted edges. Retain all remaining outside data. Consider any weak
angle assignment \(z'\) of the resulting forest satisfying
\[
 \sum_{\substack{e\ni w\\e\ {\rm survives}}}g_{w,e}
                         -n_ws_w/2=-\pi c'_w,\qquad
 |c'_w|\ge1\quad(w\in S\setminus C).
 \tag{13}
\]
Require \(|s_w|\le\pi\) also at isolated surviving selected vertices.
Their empty-incidence rows in (13) remain in force. If the resulting
assignment set is empty, there is no assignment to which the theorem
applies. No positive critical point is assumed for \(z'\).

Write \(\mathcal E_{\rm del}(z')\) for (5) on the surviving edges,
with the same outside linear work, and define its angle action by
\[
 M_{\rm del}(z')=(e_G-r_C)M_\infty-\mathcal E_{\rm del}(z')/\pi,
 \qquad M_\infty=4G_{\rm Cat}/\pi.
 \tag{14}
\]
The original calibrated action is
\(M_G=e_GM_\infty-\mathcal E(z_0)/\pi\).

**Theorem 1.** Under these hypotheses,
\[
 \boxed{\quad
 M_G-M_{\rm del}(z')
 \ \ge\ \frac{\delta_0}{\pi}
       +\sum_{v\in C}H_v\left(\frac{|n_v|}{2}-1\right)
       +\sum_{w\in S\setminus C}H_w(|c'_w|-1)
 \ >0 .
 \quad}
 \tag{15}
\]
The same \(\delta_0>0\) works for every nonempty \(C\) satisfying
(12), every such charge vector, and every admitted weak assignment.
There is no ratio condition on the powers and no degree restriction.

**Proof.** If a surviving \(c'_w\) is negative, reflect its \(s_w\)
and all its surviving incidences \(g_{w,e}\). The reflection
preserves the weak inequalities, outside data and energy by the
square argument above. It changes its row to \(-\pi|c'_w|\);
every other row stays unchanged. Reflections at different selected
vertices commute. Thus we may use an energy-equivalent assignment
whose surviving charges are all \(|c'_w|\).

Extend it to the original weak angle body by setting
\[
 s_v=\operatorname{sgn}(n_v)\pi\quad(v\in C),\qquad
               g_{a,e}=0
       \quad\hbox{at both ends of every deleted edge}.
 \tag{16}
\]
Every restored edge satisfies (2) weakly. Surviving rows are
unchanged, while a removed row is exactly
\[
                         \rho_v=-\pi|n_v|/2.
 \tag{17}
\]
This assignment \(\widetilde z\) need not belong to the original
unit-charge polytope. It does belong to \(\partial X\), since a
removed vertex had an original incident edge and \(|s_v|=\pi\).
The comparison charges in (17) are at least one by (12).

Each deleted edge has both of its square factors on the square
boundary. The endpoint-face theorem gives the exact constant
\[
 E_\square\big|_{\partial[-\pi/4,\pi/4]^2}
                       =G_{\rm Cat}/2=\pi M_\infty/8.
 \tag{18}
\]
The outside incidence on every deleted edge is zero, so its
outside work is zero as well. Therefore
\[
       \mathcal E(\widetilde z)
                   =\mathcal E_{\rm del}(z')+r_C\pi M_\infty.
 \tag{19}
\]
Combining (11), (17), and (19) yields the exact identity
\[
 M_G-M_{\rm del}(z')
 =\frac{D_0(\widetilde z)}{\pi}
       +\sum_{v\in C}H_v\left(\frac{|n_v|}{2}-1\right)
       +\sum_{w\in S\setminus C}H_w(|c'_w|-1).
 \tag{20}
\]
Use (10) and \(H_v>0\) to obtain (15). \(\square\)

### Action normalization for charged positive points

If \(z'\) comes from a positive solution with its original canonical
logarithms and charges \(c'_w\), its charge action is
\[
 F_{\mathbf c'}(t)
    =\sum_{e\ {\rm survives}}\psi(t_v,t_w)
       +\frac{i}{4\pi}\sum_{w\in S\setminus C}n_wt_w^2
       -i\sum_{w\in S\setminus C}c'_wt_w.
 \tag{21}
\]
Then \(\operatorname{Re}F_{\mathbf c'}=M_{\rm del}\) exactly.
Indeed the pinned edge calibration is
\[
 \pi\operatorname{Re}\psi+4(E_P+E_Q)
                       -g_vh_v-g_wh_w=\pi M_\infty.
 \tag{22}
\]
After summing it, the charged row
\(\sum g=n_ws_w/2-\pi c'_w\) cancels the real parts of
the quadratic and linear terms in (21), exactly as at unit charge.
Thus Theorem 1 compares the actual real classical action of every
positive deleted charged solution, including every nonzero integer
charge vector, to the original primitive action.

For an isolated surviving selected vertex, a charged critical point
must obey \(n_wt_w=2\pi c'_w\). With \(|c'_w|\ge1\), this requires
\(n_w\ne0\) and gives real \(t_w\), so its terms in (21) have zero
real part. A weak isolated row without a critical interpretation is
still covered as an angle assignment. No quantum estimate for an
isolated trace is assumed.

The linear higher-charge term in (15) is a classical comparison,
not by itself an estimate of an infinite quantum charge sum.

### Uniformity under small changes of outside angles

The gap is uniform on a compact continuous family of positive original
unit-charge solutions with the same tree, selected set and powers.
Indeed \(H_v>0\) has a positive family minimum. For the boundary
remainders, consider pairs consisting of a family parameter and an
assignment on the boundary of its ambient body \(X\).
All angle coordinates are bounded. Along a convergent sequence of
such pairs, one of the finitely many weak affine inequalities is
active on a subsequence, and remains active at its limit.
The limiting body has an interior positive point, so this is still
its boundary. Hence the set of pairs is compact. The square energy,
outside work and gradient at the continued original solution are
continuous; \(D_0\) is strictly positive at every pair. Its family
minimum is therefore positive as well.

In particular, the original positive-period implicit-function theorem
continues any fixed solution under sufficiently small complex changes
of the prescribed outside angles. Restricting to a small closed
neighborhood gives a compact family of positive solutions. Shrinking
it if necessary, (15) holds uniformly with \(\delta_0/2\) and
\(H_v/2\) from its center. This is applicable near complete outside
angles whenever the fixed short component has the required original
positive solution there. It supplies no contour transport for the
outside quantum variables.

## 4. An auxiliary even split with no exceptional small-power current

For each original integer \(n_v\), choose the auxiliary factor
\[
 \epsilon_v^*=
 \begin{cases}
  0,&n_v\ {\rm even},\\
  \operatorname{sgn}(n_v),&n_v\ {\rm odd},
 \end{cases}
 \qquad m_v^*=n_v-\epsilon_v^*\in2\mathbb Z.
 \tag{23}
\]
This is an algebraic factorization of the same original \(R^{n_v}\).
The auxiliary \(\epsilon_v^*\) is not a replacement for the physical
marking \(\eta_v\); the original relation \(n_v=\eta_v-2p_v\) stays
fixed. It is possible that the auxiliary factor differs from that
marking, for example at a total power \(n_v=1\) with \(\eta_v=-1\).
The operation then changes the chosen conjugated Ward operator, not
the crossing power or peripheral curve.

To verify its exact validity, use the full original algebra
\[
 \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2),\quad
 q=e^{\pi i/N},\quad \rho=q-q^{-1},\quad
 \kappa=q^{(N-1)^2/2},\quad \sigma=(-1)^N.
 \tag{24}
\]
Let \(f_j\) represent \(r_N^j\), with \(R=\kappa r_N\).
For every signed integer split \(n=m+\epsilon\) with \(m\) even,
\(f_n=f_mf_\epsilon\), including all repeated-node normals.
Conjugating the original even Ward identity by the unit
\(f_\epsilon\) gives, for the original trace and every polynomial
spectator \(A\),
\[
 \phi_N\!\left(f_n\mathcal D_{m,1}^{\epsilon}A\right)
                  =\sigma mN\rho\,A(c_0),\qquad
                  c_0=q+q^{-1}.
 \tag{25}
\]
Its proof uses only this factorization and
\(f_\epsilon\Xi_0=\Xi_0\), not an identification of \(\epsilon\)
with the marking. Hence the adopted full-algebra theorem applies
unchanged to (23). The original carrier is still \(\kappa^n\).

For a simultaneous set \(C\) of these currents on the original
circle tree, its exact source is
\[
 \mathcal J_{C,N}^*
   =\left(\prod_{v\in C}\kappa^{n_v}\sigma m_v^*N\rho\right)
                              Z_{G\setminus C,N}.
 \tag{26}
\]
All surviving traces, outside variables, and their mixed normal data
are retained. This follows from \(K_T(c_0,w)=1\) before any exterior
trace; no independent-component factorization is assumed.
The formula is for the original turn edges. An identity kernel or
another exterior coupon must retain its actual endpoint evaluation.

If \(n_v\in\{0,1,-1\}\), then \(m_v^*=0\), so every current containing
that vertex is zero. Conversely \(m_v^*\ne0\) implies \(|n_v|\ge2\).
Thus **every nonzero scalar prefactor in (26) has a removed set
covered by Theorem 1**. This holds at both parities for every \(N\ge2\).
For fixed powers,
\[
 \left|\prod_{v\in C}\kappa^{n_v}\sigma m_v^*N\rho\right|
                            \le\prod_{v\in C}2\pi|m_v^*|,
 \tag{27}
\]
so these exact prefactors introduce no exponential rate.
The deleted source itself can of course vanish.

For comparison, retaining the original \(\eta_v\) as the split
factor can leave a nonzero even current at total \(n_v=\pm1\).
One must not infer (12) from that different choice. Formula (23)
is the precise auxiliary choice that removes this issue.

## 5. Consequence and the remaining contour problem

No Conway reduction and no charge alias are needed for this geometric
gap whenever the original positive primitive solution exists.
The old endpoint-face condition remains exact for an extension
*within the same unit-charge rows*. The present comparison uses a
different boundary assignment only as a competitor in the ambient
convex body, and keeps its affine charge correction explicitly.
Thus it does not contradict or alter the original face criterion.

For a complete contour induction this removes a particular geometric
comparison problem: every nonzero chosen split current is exactly a
deleted source whose admitted nonzero-charge positive action is
uniformly below the full action. If the original, fully normalized
deleted source has already been bounded by those actions with
subexponential loss, (26)--(27) transfer that bound immediately to
this current, with the strict margin (15).

The outstanding statement is genuinely about the original source.
One must show that the actual deformation produces currents of
the controlled form (26), and bound each entire deleted source,
including its nonpositive sectors, lattice modes, endpoint seams
and exterior closing. A deleted forest can lack a positive critical
point; no action or quantum bound is assigned to it by assumption.
Nor does the present proof supply a positive original chart for an
arbitrary hyperbolic short filling after Conway reductions.
The relative-cycle coefficient of the original geometric block
remains a separate obligation.

The chosen half-factor has the canonical analytic unit from the
even-source theorem. Replacing it by an unwrapped Gaussian across a
logarithmic cut still incurs that theorem's exact rank-two seam.
Those seam currents are not silently identified with (26).

## Direct sources and proof coverage

All listed source proofs were read in full at the pinned versions.

* [Original convex variation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_filling_convex_variation.md),
  SHA256 2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0:
  original square energy, positive Hessian, continuous extension,
  full edge differential, arbitrary-charge rows and outside work.
* [Proper-prefix regularity](research_positive_primitive_prefix_regularity.md),
  SHA256 a01b55a71d133aadff4aac0929e50de03e1059991d6874e81646c770eb5604a6:
  previously proved \(H_v>0\) from the actual positive returns.
  The reflection proof above independently checks the needed sign.
* [Endpoint angle face](research_endpoint_current_angle_face.md),
  SHA256 f84acb848b889a1553b467ba2d040884f7792a5ab0439eaada14a79216f363cc:
  exact square-boundary energy, deleted-edge normalization,
  isolated-vertex scope and the distinct fixed-row face criterion.
* [Original action calibration](research_positive_period_inverse_descent.md),
  SHA256 b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565:
  full edge identity (22), original primitive action and its
  outside-angle normalization.
* [Even-factor source reduction](research_even_twist_ward_source_reduction.md),
  SHA256 7cd055df1b070ecc8a5f4a4b62e821e37c616e1bbb935aa274939cf44e8e0b18:
  exact conjugated even Ward identity, all-subset scalar deletion,
  retained full Hermite data, canonical analytic factor and its seam.

Only written reasoning, source-text reads and file hashes were used.
No mathematical code, numerical evaluation, tests or compilation
were run. No frozen note, public document or manuscript was edited.
