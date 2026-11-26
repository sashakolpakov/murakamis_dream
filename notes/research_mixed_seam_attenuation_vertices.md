# Reducing seam attenuation to finitely many values

Research deduction, 5 November 2026. Keep the original hybrid contour,
finite conditional sums, and actual geometric reference. Once the real
coordinates outside the zero collars are fixed, the upper bounds below
need only be checked at finitely many values of the collar coordinates.
For a single collar there are at most four such values. This eliminates
the attenuation parameters from a continuous maximization; it does not
prove the sign of the resulting comparison.

## 1. Fixed data and the variables to be eliminated

Fix an original cyclic three/four word of length \(m\ge1\). Write
\(\epsilon_j\in\{0,1\}\) for its type minus three, and
\(\sigma_j\in\{0,1\}\), \(\sigma_j\le\epsilon_j\), for a fixed
Fourier selection. Keep its actual geometric reference \(r\) fixed.
Edge \(j\) joins positions \(j-1,j\); all indices are cyclic.
Let \(\phi_j\) be its original allocated critical phase and
\[
 \Gamma_j(u,v)=\phi_j(r_{j-1},r_j)
       +\phi_{j,a}(r)(u-r_{j-1})+\phi_{j,b}(r)(v-r_j),
 \qquad M=\Re\sum_j\phi_j(r_{j-1},r_j).
 \tag{1}
\]
Cyclic stationarity gives \(\sum_j\Re\Gamma_j(z_{j-1},z_j)=M\)
at every target. The planes in (1) are retained even when a target
coordinate is zero; no critical phase at that zero is required.

Fix a positive collar width \(\rho\le1/1000\) small enough for
the single-edge loss \(d_s=1/4000\) in
[the seam interface theorem](research_mixed_seam_boundary_potential_reduction.md),
Section 1. Its existence is proved there; the full allowed radius is
not numerically specified. Let \(S\) be a fixed nonempty set of collar
positions. At positions outside \(S\), fix real coordinates
\(x_j\in[\rho,1/2]\). At each \(s\in S\) vary
\[
             \lambda_s\in[0,1],\qquad x_s=\rho(1-\lambda_s).
 \tag{2}
\]
Boundary points can be assigned to either closed piece. The types,
selections and all reference coordinates stay fixed during this variation.

Use the cutoffs of the
[periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md).
For a row \(j\notin S\), put
\[
 b_j=\begin{cases}.22,&\sigma_j=0,\\ .12,&\sigma_j=1,\end{cases}
 \qquad
 c_j=\begin{cases}\Im r_j,&\sigma_j=0,\\ .014,&\sigma_j=1,\end{cases}
 \qquad k_{jk}=L_{b_j}(x_k)\quad(k\notin S).
 \tag{3}
\]
Here \(L_b\) is zero on \([\rho,.1]\), affine from zero to one on
\([.1,b]\), and one on \([b,.5]\). The row chooses \(b_j\),
including when its argument is a neighbor of a different type. On the
collar the same cutoff equals \(\lambda_s\), independently of the row.
Write \(N(j)=\{j-1,j,j+1\}\), with repeated cyclic indices understood
only once in a minimum. The physical heights are exactly
\[
 \begin{split}
 h_s&=0\quad(s\in S),\\
 h_j(\lambda)&=c_jR_\rho(x_j)
    \min\bigl(\{k_{jk}:k\in N(j)\setminus S\}
                    \cup\{\lambda_s:s\in N(j)\cap S\}\bigr)
                      \quad(j\notin S),\\
 z_j(\lambda)&=x_j+i h_j(\lambda).
 \end{split}
 \tag{4}
\]
The minimum is nonempty because it includes the row's own coordinate.
The fixed multiplier \(R_\rho(x)\) equals one on \([.1,.45]\) and
\(400(.5-x)^2\) on \([.45,.5]\). Its value below .1 is irrelevant
in (4), where the own cutoff vanishes.

Let \(K\) consist of 0, 1, and all constants \(k_{jk}\) occurring
in (4). Constants from rows not adjacent to a collar may be omitted.
Thus \(K\) is finite, lies in \([0,1]\), and depends only on the
fixed noncollar real coordinates and selections.

## 2. Convexity of the complete coherent upper rate

For an edge with neither endpoint in \(S\), its allocated upper rate is
\[
 e_j(z_{j-1},z_j)=\Re\phi_j(z_{j-1},z_j)
       +\frac{\sigma_{j-1}}2\chi(z_{j-1})
       +\frac{\sigma_j}2\chi(z_j),\qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\},
 \quad g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
 \tag{5}
\]
In particular both Fourier alternatives are kept at height zero and
at real part \(1/2\). All functions use the original logarithmic lift.

**Lemma 1.** At fixed real coordinates, (5) is jointly convex in its
two heights throughout the required vertical intervals.

**Proof.** First suppose both real coordinates are at least .1.
All possible targets belong to the typed convex polygons
\[
 \begin{split}
 \Omega_3&=\operatorname{conv}\{.1,.22-.03i,.45-.03i,.5,
                                         .45+.02i,.22+.02i\},\\
 \Omega_4&=\operatorname{conv}\{.1,.22-.057i,.45-.057i,.5,
                                         .45+.014i,.12+.014i\}.
 \end{split}
 \tag{6}
\]
The quadratic right taper lies below the straight sides of these
polygons. The type-three polygon and the negative part of the type-four
polygon satisfy the cotangent bound (8) of the
[minimum-neighbor theorem](research_mixed_minimum_neighbor_contour.md).
On the positive part of \(\Omega_4\), the bound (6) of
[the early selected source theorem](research_mixed_early_selected_source_cap.md)
applies also through real part .5. Hence throughout (6),
\[
             \Re\cot(\pi z)\ge0,
             \qquad |\Im\cot(\pi z)|<1/2.
 \tag{7}
\]
These are already certified strict scalar bounds, not assumptions about
an untested domain. The
[closed-cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore supplies the original simple inner root and positive triangle
forms on the full independent products.

For one block write its types as \((\eta,\epsilon)\), its outer
variables as \((a,b)\), and choose
\(f_a\in\{0,\sigma_a\}\), \(f_b\in\{0,\sigma_b\}\).
The corresponding holomorphic branch of (5) is
\[
 \psi_f(a,b)=\phi_{\eta\epsilon}(a,b)
       +\tfrac12\{f_ag(a)+f_bg(b)\}
       +\pi i\{(\sigma_a-f_a)a+(\sigma_b-f_b)b\}.
 \tag{8}
\]
Before eliminating its inner coordinate \(s\), its nonlinear part is
\[
 V(s,a)+V(s,b)-\epsilon g(s)
       -\tfrac{\eta-f_a}{2}g(a)
       -\tfrac{\epsilon-f_b}{2}g(b)+2\pi ias,
 \quad V(s,a)=g(s+a)-g(s)-g(a).
 \tag{9}
\]
The remaining own-factorial coefficients are nonnegative. The two
triangle forms are positive definite, and the last chirp has zero real
Hessian. The complex Schur identity therefore gives
\(-\Re\psi_f''>0\), exactly as in Corollary 2 of
[the selected-height extension](research_mixed_selected_height_reference_extension.md).
The inner root has not changed, because the added terms depend only on
the outer variables. At fixed real parts the height Hessian of
\(\Re\psi_f\) is \(-\Re\psi_f''\). Each branch is convex, and
their finite maximum is (5), so (5) is convex as well.

If an endpoint lies in \([\rho,.1]\), its cutoff is zero. Its own
height and the other endpoint's height are then identically zero for
every \(\lambda\). This edge is constant in the present variables.
No independent complex domain below .1 is being asserted. This also
handles boundary values .1, .5 and coincident cyclic indices. \(\square\)

The finite-source upper bounds for (5) are established separately:
the [real half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md)
handles the both-real deep-low edges; the early selected source theorem,
the [independent right products](research_mixed_unselected_right_taper_products.md)
and the [left/right interface source](research_mixed_left_right_interface_source.md)
handle the nonlow products. The absolute bound in
[the Fourier continuation theorem](research_mixed_fourier_weight_continuation.md)
retains the forcing alternative at its ties. Lemma 1 is a curvature
deduction for these original branches, not a replacement for those
finite-source proofs.

## 3. A fixed allocation of the original summation factors

Let \(E(S)\) denote the physical edges incident to \(S\), and let
\(E_A\) be the other edges. For every \(s\in S\), choose a fixed
number \(a_s\ge0\). Let \(n_{js}\) count the incidences of edge
\(j\) at \(s\), and require
\[
                   u_j=\sum_{s\in S}n_{js}a_s\le1.
 \tag{10}
\]
A loop has two incidences. The two edges of a two-cycle are distinct.
Thus (10) is also the correct allocation for those periods.

Use the profiles \(A_{e,d}\) and \(B_e\) defined by the exact
rational table in
[the height-dependent source theorem](research_mixed_height_resolved_seam_sources.md).
For \(s\in S\) put
\[
 U_s(\lambda)=A_{\epsilon_s,\epsilon_{s-1}}(h_{s-1})
       +B_{\epsilon_{s+1}}(h_{s+1})
       +2\Delta_\rho+\epsilon_s\nu_\rho,
 \quad \nu_\rho=-J(\rho),\quad
 \Delta_\rho=\rho\log2-J(\rho),
 \quad J(t)=\int_0^t\log(2\sin\pi u)\,du.
 \tag{11}
\]
This is the complete raw two-edge ceiling, with a uniform collar cost.
In particular its collar cost is not replaced by a function of
\(x_s=\rho(1-\lambda_s)\).

Each profile is convex within each fixed-selection height band. This
follows directly from its rational slopes: the only bands with more
than one segment are the three type-three profiles and the negative
band of \(A_{0,1}\), and in each case the slopes increase. The positive
and negative type-four bands belong to different selections. Convexity
across that selection change is neither needed nor asserted.

Define the upper rate
\[
 \mathcal B(\lambda)=
     \sum_{j\in E_A}e_j(z_{j-1},z_j)
     +\sum_{s\in S}a_sU_s(\lambda)
     +\sum_{j\in E(S)}(1-u_j)
                    \{\Re\Gamma_j(z_{j-1},z_j)-d_s\}.
 \tag{12}
\]
For every fixed \(\tau>0\), the original product of allocated
block moduli is at most
\(C N^A\exp(N(\mathcal B(\lambda)+\tau))\), uniformly in
\(\lambda\). Here \(C,A\) may depend on the fixed word and collar,
and the estimate holds for both level parities.

Indeed, apply the two-edge source bound to the fraction \(a_s\)
at each seam. Each unconsumed fraction \(1-u_j\) uses the complete
single-edge gap, and each edge in \(E_A\) uses (5). For positive
moduli this is obtained by adding their logarithms with these
nonnegative coefficients; if a modulus vanishes the desired product
bound is immediate. Each physical edge and Fourier halfweight is
counted exactly once. Choosing each original block tolerance below
\(\tau/m\) gives the stated total tolerance. Fixed powers of \(N\)
and the hybrid Jacobian do not change the exponential rate.

## 4. The finite-vertex theorem

**Theorem 2.** With the data and allocation fixed as above,
\[
       \max_{\lambda\in[0,1]^S}\mathcal B(\lambda)
                    =\max_{\lambda\in K^S}\mathcal B(\lambda).
 \tag{13}
\]
The same equality holds after subtracting the constant \(M\).
The finite set on the right still depends on the fixed noncollar real
coordinates; those coordinates and the geometric reference have not
been eliminated.

**Proof.** Subdivide the cube by all hyperplanes
\(\lambda_s=\lambda_t\) and \(\lambda_s=k\), \(k\in K\).
On every closed cell, each minimum in (4) is one fixed coordinate
\(\lambda_s\) or one fixed constant. Hence every height is affine
on that cell. Lemma 1 makes each coherent term in (12) convex there.
Each profile term is convex composed with an affine map, even if the
height multiplier is negative. Each tangent term is affine, including
the real seam coordinate (2). All coefficients in (12) are nonnegative.
Thus \(\mathcal B\) is convex on the cell.

Every vertex of such a cell has all coordinates in \(K\). To see this,
group the coordinates joined by active equalities
\(\lambda_s=\lambda_t\). If a group is not fixed to a constant of
\(K\), all inequalities from that group to other groups and constants
are strict. Moving all its coordinates by the same sufficiently small
positive or negative amount preserves those inequalities and the active
equalities. The purported vertex would be the midpoint of a nontrivial
segment in the cell. Therefore every group is fixed to a member of
\(K\). The endpoints 0 and 1 are included, so the argument also
covers the boundary of the cube.

A convex function on a compact polytope is bounded above by its largest
vertex value: express any point as a convex combination of vertices and
apply convexity. There are finitely many cells, and (12) is continuous
at their interfaces. The maximum on the cube is therefore bounded by
the right side of (13). The reverse inequality follows because
\(K^S\subset[0,1]^S\). \(\square\)

For a single seam, at most two nonseam heights vary. For each distinct
neighbor \(j\) of the seam define
\[
             m_j=\min_{k\in N(j)\setminus S}L_{b_j}(x_k).
 \tag{14}
\]
Its height is \(c_jR_\rho(x_j)\min(m_j,\lambda)\).
Consequently the only necessary candidates are
\[
                    \lambda\in\{0,1,m_{s-1},m_{s+1}\},
 \tag{15}
\]
omitting nonexistent or duplicate neighbors. A neighbor with zero
height multiplier contributes no breakpoint. A one-cycle with its
single seam has only the endpoints 0 and 1; a two-cycle has only one
distinct nonseam row. Formula (15) needs no subdivision at source-profile
knots, because those profiles are already convex on the full permitted
band. More generally, with all other seam variables fixed, their values
are included among the constants in the one-variable version of (14).

## 5. The same reduction for exact boundary repairs

The boundary-repair upper bound from
[the admissible-halo theorem](research_mixed_admissible_boundary_halos.md)
also satisfies (13). Here a halo means an auxiliary neighbor used to
compute the height of an endpoint row. For every maximal nonseam run
\(I=[l,r]\) of length at least two, replace its two external halos
by the unselected reference symbols. Keep all physical nonseam symbols
fixed. The repaired targets, their three-step entry and exit functions
\(A_I^{[3]},E_I^{[3]}\), and their occupation quantities
\(\Psi_I,\Omega_I\) are then independent of every \(\lambda_s\).

Let \(\Delta_I(\lambda)\) be the sum of physical minus repaired
weights \(w_j=e_j-\Re\Gamma_j\) on the affected edges. Only the
first and last edge can change. If the run has two symbols, these are
the same edge and its joint two-height change is counted once. If it
has one symbol, there is no edge and no correction. For a nonsingleton
the proved run bound is
\[
 \sum_{j\text{ internal to }I} w_j
 \le C_I+\Delta_I(\lambda),\qquad
 C_I=-E_I^{[3]}-A_I^{[3]}-(1-\theta)\Psi_I-\theta\Omega_I,
 \quad 0<\theta<1.
 \tag{16}
\]
All symbols in \(C_I\) have the definitions and layer alignment of
that theorem. For a singleton use its exact empty sum zero instead.

Subtracting (1) from (12) and substituting (16) gives the valid bound
relative to \(M\)
\[
 \begin{split}
 \mathcal D_{\rm repair}(\lambda)={}&
  \sum_{s\in S}a_s\{U_s(\lambda)
                    -\Re(\Gamma_s+\Gamma_{s+1})(z)\}\\
 &-d_s\sum_{j\in E(S)}(1-u_j)
       +\sum_{I:\,|I|\ge2}\{C_I+\Delta_I(\lambda)\}.
 \end{split}
 \tag{17}
\]
There is no additional subtraction of the reserve from an older
uniform pair bound. Each \(\Delta_I\) is a sum of convex physical
coherent rates minus affine planes and fixed repaired values. In the
two-symbol case this uses their joint convexity from Lemma 1.
Consequently (17) is convex on every cell of the preceding proof, and
\[
 \max_{[0,1]^S}\mathcal D_{\rm repair}
                         =\max_{K^S}\mathcal D_{\rm repair}.
 \tag{18}
\]
No variable-dependent optimization of auxiliary halos is used in (17).
For a mixed cycle the maximal runs are ordinary open chains, including
the case where both ends meet the same seam. If every vertex is a seam,
there are no runs and the same formula applies with an empty final sum.

## 6. What remains after the reduction

Equations (13) and (18) are exact maximization reductions for the specified
upper bounds. A uniform strict negative bound in (18), over the remaining
real coordinates, references, selections and relevant seam patterns,
would supply the corresponding missing seam estimate. No such sign
is proved here. Configurations in the other half of the period and
stability under arbitrary short partial fillings remain separate tasks.

The allocation \(a_s\), boundary repair rule and collar ceiling must
remain fixed while applying the theorem. One may minimize the resulting
valid maxima over different fixed choices afterward. Taking a pointwise
minimum of several convex bounds and testing that minimum only at the
vertices is not justified: that minimum need not be convex. The same
caution applies to a sharper collar cost depending on \(\lambda\),
or to optimizing over admissible halo sets which change with \(\lambda\).
In contrast, the finite maximum of the actual Fourier branches in (5)
is precisely the convex operation used in the proof.

The focused checker verifies the rational profile slopes and their
convex hinge expressions, finite exact instances of the active-equality
argument, and the cited source dependencies. The arbitrary-dimensional
vertex argument and branch-curvature deduction are the written proofs
above. Numerical tests of remaining real parameters are not a substitute
for the missing uniform inequality.

```sh
python3 experiments/check_mixed_seam_attenuation_vertices.py
```
