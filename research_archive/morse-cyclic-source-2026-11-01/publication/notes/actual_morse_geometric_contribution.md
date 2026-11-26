# The original complement and its geometric contribution

A simple triangulated sphere with a perfect matching of its cubic dual determines an actual augmented link diagram when the cyclic orders, strand pairings and crossing disks are retained. This note follows that diagram through its exact finite source, its geometric critical point, and the filling of its original auxiliary cusps.

For independently sufficiently long fixed signed twists, the geometric contribution to the original invariant is nonzero and has the exponential rate of the actual filled hyperbolic volume. The proof keeps the primitive peripheral words, the finite scalar factors and both parities of the quantum level. No terminal tangles are inserted, and no local balance assumption is imposed.

The name CROSS denotes the central recurrence-path piece of each original homogeneous numerator. Selecting it at every crossing region is an algebraic decomposition of the original evaluation, not a new invariant. The [analytic companion](actual_morse_cross_filling_period.md) proves its full Fourier asymptotic. To conclude the same limit for the full invariant of an undecorated diagram, one must additionally control the remaining pieces.

## 1. Precise diagram and filling scope

Let \(\mathcal T\) be a finite simple triangulated oriented sphere with
at least four vertices. Choose a perfect matching of its cubic dual.
The two triangles in each matched pair form a quadrilateral with
four distinct white vertices. Record a cyclic order
\((x_e,b_e,y_e,c_e)\); its common diagonal is \(x_ey_e\), its input
middle is \(b_e\), and its output middle is \(c_e\). There are \(R\)
matched pairs and \(R+2\) white vertices. Mark a nonmatching edge
\(uv\). It is a strand edge in the link diagram.

There are two equivalent permitted inputs:

* an actual connected augmented diagram in \(S^3\), whose projection
  and crossing-disk cut has exactly these labels and orders; or
* the literal inverse-cut construction in section 2 below.

Fix the retained half twist
\(\epsilon_e\in\{-1,0,1\}\) and its sign at every disk. Its auxiliary
peripheral basis \((\mu_e,\lambda_e)\) is the original disk-framed
primitive basis. The longitude \(\lambda_e\) is represented by the
ordered two-head product \(P_e=B_eA_e\). Integer filling coordinate
\(p_e\) means filling the slope \(\mu_e+p_e\lambda_e\); the main
crossing power is
\[
                    n_e=\epsilon_e-2p_e.                 \tag{1}
\]
The original outside terminal matching and the even/odd pairing at
each disk determine the main components. When their terminal graph is
connected, denote the filled knot by \(K_{\boldsymbol p}\).
We keep this original parity test. We do not change the parity vector
to obtain a different knot.

A supplied labeled positive right-angled cut certificate is sufficient
for everything below. In this simple-sphere class such a certificate
also follows from the constructive packing theorem in
[the balanced-fan note, section 2](actual_balanced_terminal_fan_volume.md).
That section constructs the packing **before any fan is inserted**.
Only that initial geometric construction is used here.

**Theorem.** For each fixed diagram and the recorded choices above
there is a number \(T_D\) such that, for every fixed integer vector
\(\boldsymbol p\) with \(\min_e|n_e|>T_D\), independently in sign
and relative size, the following assertions hold.

1. Filling the specified auxiliary components gives a complete
   finite-volume hyperbolic metric on the original filled link
   exterior, with every main cusp unfilled. If the recorded component
   test is a knot, it is \(S^3\setminus K_{\boldsymbol p}\).
2. The all-CROSS term of the original complete-color Morse contraction
   has a nonzero relative first-charge asymptotic, at both parities
   of the level \(N\). Its selected critical action
   \(S_{\boldsymbol 1}\) satisfies
   \[
       2\pi\operatorname{Re}S_{\boldsymbol 1}
          =\operatorname{Vol}(S^3\setminus K_{\boldsymbol p})
                                                        \tag{2}
   \]
   in the knot case, and the analogous original link-complement
   identity otherwise.
3. In particular, for that all-CROSS contraction
   \(\mathcal I_{N,\mathrm C}\),
   \[
       \lim_{N\to\infty}\frac{2\pi}{N}
            \log|\mathcal I_{N,\mathrm C}|
          =\operatorname{Vol}(S^3\setminus K_{\boldsymbol p}).
                                                        \tag{3}
   \]
   The exact raw phase is retained in section 3. An ordinary
   zero-framing phase does not change (3).

The diagram, its matching, its signs, and all powers are fixed before
\(N\). The threshold can depend on this entire finite diagram.
There is no short-filling assertion and no uniformity in a growing
sphere. The theorem does not yet assert (3) for the full invariant:
that requires a bound on the remaining sectors.

## 2. Why the manifold and its complete anchor are the original ones

Take disjoint small neighborhoods of the matched edges of the cubic
dual. Each is a four-terminal disk. In cyclic terminal order
\(0,1,2,3\), the two shaded halves group \((1,2)\) and \((3,0)\).
Draw the physical untwisted strands instead with pairs
\((0,1),(2,3)\), and connect outside terminals along the nonmatching
dual edges. In the corresponding disjoint three-balls put the
perpendicular crossing circles and their twice-punctured disks.
This constructs a link in \(S^3\), not a manifold assigned to an
abstract tensor graph. Retained odd half twists use the physical
pairing \((0,2),(1,3)\), with their original signed collar paths.

The two main pairings and the shaded grouping must not be confused.
The graph of main components is the union of the outside terminal
matching and these physical pairings. Every terminal has degree two.
Its connectedness is exactly the knot test, and adding full twists
does not change it.

Cut along the projection sphere. In each projection ball a crossing
circle semicircle is boundary parallel by its original half disk.
Drilling that semicircle and opening that same half disk cancels the
introduced handle. These operations occur in disjoint collars, so
opening all of them leaves one ball in each projection copy. The
boundary cellulation is the prescribed medial sphere. Thus cycles
in the matched graph create no unidentified handle or extra gluing.

Let \(Q\) be its positive ideal right-angled cut polyhedron. The even
shaded pairing fixes the crossing-circle vertex and sends
\(C_1\mapsto C_0,\ C_2\mapsto C_3\). An odd pairing exchanges the
projection copies and the two punctures, using the literal signed
half-twist collar. The two odd signs have the same corner permutation
but different primitive paths. White faces pair by their original
projection labels.

At every ideal vertex, the link of \(Q\) is a rectangle. Normalize its
opposite shaded sides to length one. Each shaded triangle map then
preserves the canonical horocycles at all three corners, including
the odd corner permutation. Each alternating white/shaded edge cycle
has four right-angle pieces. It fixes both ideal endpoints, preserves
the chosen horospheres there, and rotates by \(2\pi\), so its whole
holonomy is the identity. The ideal links are the actual link's
torus links and have no cone or dilation defect. Their horoball ends
are complete. Hence
\[
                \operatorname{Vol}(Y_D)=2\operatorname{Vol}(Q),
       \qquad \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
                                                        \tag{4}
\]
Here \(Y_D\) is the same augmented exterior, with the recorded half
twists and peripheral bases.

These are the local cut and gluing arguments in
[the matching-geometry proof, sections 4–6](general_augmented_plat_matching_geometry.md).
They use a sphere projection, disjoint half disks, and the prescribed
corner maps. Moving cups and caps to a flat plat is not a premise.
The inverse construction and its general Morse realization are
spelled out in
[the matched-sphere source, sections 1–4](research_matched_sphere_morse_source.md).

For completeness, the initial simple-sphere packing theorem does not
require the absence of separating triangles. Remove one triangular
face and pool its three boundary angle demands. Strict Hall
inequalities for every nonempty proper destination subset give a
positive allocation of angles. The strictly concave calibrated
triangle entropy has an interior maximizer, whose multipliers give
positive radii. The center triangles have zero interior rotational
and translational holonomy. Their boundary develops once around a
convex triangle, so the degree argument makes the development
injective. Vertex-disk sectors stop before opposite center edges;
this proves disjointness, including across separating triangles.
The contact circles and outward halfspaces therefore give the
labeled strict support certificate. Sending the marked contact to
infinity gives the two protected parallel lines. No radius-balance
inequality enters this construction.

## 3. The exact source and the phases which remain outside the action

Put \(d=N-1\), \(q=e^{\pi i/N}\). In the recorded four-leg order the
full local homogeneous numerator is
\(H_e(L_{x_e},L_{b_e},L_{c_e},L_{y_e})\). The original reduced
Morse contraction is
\[
 [\prod_{f\ne u,v}L_f^d]\,
       \prod_e H_e(L_{x_e},L_{b_e},L_{c_e},L_{y_e})
             \big|_{L_u=L_v=0}.                       \tag{5}
\]
This statement includes the complete root Hermite normals and the
unrestricted physical mark.

Here is the part of its proof that matters for changing the Morse
height function. Each full coupon contributes
\(N^{-1}H_e/(b_ec_e)^{d/2}\). If \(M_f\) counts middle passages
and \(T_f\) counts outside minus inside turns, the actual boundary
turning number gives
\[
       M_f-T_f=2 \quad(f\ne u),\qquad
       M_u-T_u=-2.                                    \tag{6}
\]
The ordinary caps and cups give the same powers as these winding
numbers; replacing the exposed cap by the original reduced mark
contributes \(N^{-1}(L_v/L_u)^d\). Thus the full summand is
\(N^{-R-1}\prod H_e/\prod_{f\ne u,v}L_f^d\).
The primitive face-potential lattice has \(R+1\) independent
\(N\)-point grids after the exterior gauge is fixed. Their count
cancels \(N^{-R-1}\). Exact endpoint support is imposed before the
root reduction, so no coefficient is aliased into a wrong endpoint.
This proves (5) with its original phases at arbitrary Morse height
and both level parities.

Replace each homogeneous factor in (5) by its CROSS cofactor factor
and retain the physical spectral trace. Write
 \(C_N^{\mathrm{raw}}(\boldsymbol\delta)\) for the resulting entire
spectral numerator, with each node
\(-2\cos(2\pi\delta_e)\). It is even separately in every coordinate,
has degree at most \(d\) in each node, and satisfies
\(C_N^{\mathrm{raw}}=(-1)^{dR}C_N^+\) in the positive cofactor
normalization. The exact original filling period is
\[
\begin{split}
\mathcal I_{N,\mathrm C}
={}&q^{d^2\sum_e n_e/4}(-i)^R
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
 \Bigl(\prod_e\ell_e\Bigr)(-1)^{(N+1)\sum_e\ell_e}\\
&\quad\cdot
 \int_{[-1/2,1/2]^R}
  \Bigl(\prod_e\sin(2\pi\delta_e)\Bigr)
  C_N^{\mathrm{raw}}(\boldsymbol\delta)
  \exp\!\left[
   N\sum_e\{\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e\}
       \right]\,d\boldsymbol\delta .
\end{split}                                             \tag{7}
\]
The sum is the original trace identity with its endpoint currents;
it is not defined by an unqualified termwise Poisson rearrangement.
The odd-level simple node and the double-node normals are included.
The same finite proof is
[the matched-sphere source, sections 5–7](research_matched_sphere_morse_source.md).

No operation in (5)–(7) changes a disk, a strand pairing, or a
peripheral curve. In particular the all-CROSS source for the original
sphere exists before a fan construction, and its ordinary-face
targets are still \(d\).

## 4. One marked circle pattern on the whole sphere

Normalize the complete protected white disks to
\(\operatorname{Im}z\le0\) and \(\operatorname{Im}z\ge1\).
For each finite face use center \((X_f,Y_f)\) and radius \(r_f\).
At a strand edge set \(I_{fg}=1\); at matching edge \(e\) set
\(I_{fg}=\cos(2\pi\delta_e)\). The equations are
\[
\begin{aligned}
(X_f-X_g)^2+(Y_f-Y_g)^2
 &=r_f^2+r_g^2+2I_{fg}r_fr_g,\\
Y_f&=r_fI_{fu},\qquad
1-Y_f=r_fI_{fv},
\end{aligned}                                            \tag{8}
\]
where the last two equations are imposed at the appropriate marked
line incidences. Fix one horizontal translation. The marked
line-line edge is automatic; the remaining system has \(3R-1\)
equations and variables.

Its complete Jacobian is invertible. The infinitesimal angle sums
and the positive finite-face source Hessian first force all
logarithmic radius variations to be one common scale. Each of the
two triangles adjacent to \(uv\) contains a finite circle tangent
to both fixed lines. Its radius is \(1/2\), so its scale variation
is zero. All radius variations are therefore zero.

With radii fixed, each finite center triangle has one infinitesimal
Euclidean motion. A one-line triangle has only a horizontal
translation. Removing the two triangles at \(uv\) leaves a
triangulated disk with connected triangle adjacency, containing all
finite vertices and at least one one-line triangle. Two adjacent
finite triangles agree at two distinct centers; two adjacent
one-line triangles agree at their finite center. These comparisons
propagate one horizontal translation through the disk, and the
normalization removes it. The kernel is zero.

The holomorphic implicit-function theorem now gives one circle
pattern on a fixed polydisk in all \(\delta_e\). The variables
\(X,Y,r\) are complexified independently, without conjugating
parameters. The solution is real on real parameters and even in
each \(\delta_e\).

For one source triangle put \(x=1/r_x,\ b=1/r_b,\ y=1/r_y\),
\[
\begin{aligned}
A&=x+y,& s&=\sin(\pi\delta),\\
D&=A^2-4xy s^2,&
T_b&=\sqrt{bA+xy+b^2s^2},\\
E_b&=A+2bs^2+2sT_b .
\end{aligned}                                            \tag{9}
\]
Use positive complete roots and their analytic continuations.
The original determinant, beta, and forced-product rate \(Q_b\)
obeys
\[
\partial_\delta Q_b=-\operatorname{Log}(E_b/\sqrt D),
\qquad
\partial_{\log L_f}Q_b=\frac{\theta_f}{2\pi},
\qquad Q_b(0)=F(x,b,y).                                 \tag{10}
\]
The angles are those of (8), with their marked-line limits. Thus
the developed angles sum to \(2\pi\) exactly when the finite-face
source is stationary. Uniqueness of the finite-face critical point
identifies these curvatures with the limiting source saddle.

The common strip also handles a triangle containing both protected
lines. If its finite radius is \(r\), its strip width is
\(r(1+\cos(2\pi\delta))\). This shared width cannot be chosen
independently at two triangles. The corresponding repeated scalar
root does not remove the selected eigenflag: the noncentral
complete parabolic has a nonzero off-diagonal matrix entry, and
its eigenline for
\[
                  J=-e^{-2\pi i\delta}                 \tag{11}
\]
continues holomorphically, including its collision at zero.

This is the complete rank and face-identification mechanism in
[the marked-pattern proof](actual_marked_deformed_circle_pattern.md).
No part of it refers to the number of strands at a Morse slice.
Simplicity is important: in particular a matching edge cannot join
the two protected faces, since their unique common edge is the
marked strand edge. Hence \(A>0\) in every local formula.

## 5. Full group relations and the original primitive peripheral words

Choose the two holomorphic white-reflection matrices
\(\mathcal R_f^\pm\), with
\(\mathcal R_f^-\mathcal R_f^+=I\), from the one pattern.
At a regular Morse slice with regions \(F_0,\ldots,F_k\), the
original heads and prefixes are
\[
 H_j=\mathcal R_{F_j}^+\mathcal R_{F_{j-1}}^-,
 \qquad
 H_j\cdots H_1=\mathcal R_{F_j}^+\mathcal R_{F_0}^- .
                                                        \tag{12}
\]
Their marked lifts give the original parabolic main meridians.
Shared physical wire ends have the same adjacent region labels.
At a cup or cap the consecutive regions are \(F,G,F\), so the
inserted ordered pair has product \(I\), and all later prefixes
are unchanged. This proves the relations also when \(k\) changes.

At one crossing disk the ordered input pair is
\[
 A_{\mathrm{in}}=\mathcal R_b\mathcal R_x,\qquad
 B_{\mathrm{in}}=\mathcal R_y\mathcal R_b,\qquad
 P=B_{\mathrm{in}}A_{\mathrm{in}}=\mathcal R_y\mathcal R_x,
                                                        \tag{13}
\]
and the output pair replaces \(b\) by \(c\).
The labeled contact map of the disk, taking
\(C_1\mapsto C_0,\ C_2\mapsto C_3\), is
\[
 R_0=\frac{E_bE_c}{D},\qquad
 C=I+\frac{R_0-1}{J-J^{-1}}(P-J^{-1}I).                 \tag{14}
\]
It sends both input generators to their respective output
generators by simultaneous conjugation and commutes with \(P\).

The primitive normalization in (14) is geometric. Sending the two
outer intersection points to \(0,\infty\) makes the two shaded
contact circles concentric, with radii \(\sqrt D/E_b\) and
\(E_c/\sqrt D\). Their ordered corner map is multiplication by
\(R_0\); the product of their reflections would instead give
\(R_0^2\). The original threading word \([2,1,1,2]\) follows the
inverse of the first map. At zero, (14) retains the nontrivial
parabolic divided-difference limit. Setting \(C=I\) merely because
its eigenratio is one would give the wrong group representation.

Marked lines are treated by one common Möbius regularization of the
whole pattern. The input/output side signs are calibrated by the
same complete cusp rectangle. Nonvanishing middle contributions
have the original opposite signs; an exceptional two-line triangle
has \(T_b=0\) and contributes ratio one. Its actual eigenflag still
comes from (8). This proves (14) with the correct labels at every
zero pattern, not just at positive local curvatures.

The positive crossing acts by
\((A,B)\mapsto(A^{-1}BA,A)\), represented by \(P^{-1}-I\).
For \(\epsilon\) equal to \(0,1,-1\), put
\[
\begin{aligned}
 U&=-\operatorname{Log}R_0-\epsilon\operatorname{Log}(-J),\\
 V&=2\operatorname{Log}(-J)=-4\pi i\delta,\qquad
 m=e^{U/2}.
\end{aligned}                                            \tag{15}
\]
All logarithms are the germs vanishing at the complete point.
The actual determinant-one auxiliary meridian is
\[
 {\mathsf M}
 =mR_0(J^{-1}-1)^{-\epsilon}
        C^{-1}(P^{-1}-I)^\epsilon.                      \tag{16}
\]
Its selected eigenvalue is \(m\), and
\(\det{\mathsf M}=m^2R_0(-J)^\epsilon=1\).
The factor \(J^{-1}-1\) is a unit near completeness, including for
negative \(\epsilon\). Formula (16), not just (15), verifies the
original threading and signed Hurwitz relations.

Equations (12)–(16) cover every shared wire, cup, cap, drilled box,
and half twist in the actual Morse van Kampen presentation.
There is no extra consistency equation at a cycle of the matched
graph: all heads came from the same global reflections and all
ordered box maps use those heads. The resulting family
\(\rho_{\boldsymbol\delta}\) is an actual framed representation
of \(\pi_1(Y_D)\). At zero it is the complete cut representation.
Every main meridian remains noncentral parabolic; its commuting
longitude has multiplier one. Thus every unfilled main peripheral
group is parabolic.

These are full matrix and based-word assertions from
[the primitive collar proof](actual_deformed_circle_primitive_collar.md)
and [the global assembly, section 2](actual_complete_core_geometric_deformation.md).
The latter's displayed \(2k\) head count is replaced event by event
by the actual \(k(t)\) in (12). No other part of its proof changes.

## 6. Absolute action and the first-charge filling equations

Let \(A_0\) be the pure limiting face-critical value
\[
 A_0(\boldsymbol\delta)=
 \operatorname{crit}_{L}
 \left\{\sum_e(Q_{b_e}+Q_{c_e})
                -\sum_{f\ne u,v}\operatorname{Log}L_f\right\}.
                                                        \tag{17}
\]
It is separately even, real on real parameters, and anchored by
\(A_0(0)=\Phi_D\). Put
\[
 A_\epsilon=A_0+\pi i\sum_e\epsilon_e\delta_e^2.
\]
Envelope differentiation of (10), retaining (15), gives
\[
       dA_\epsilon=\sum_e U_e\,d\delta_e,\qquad
       d(2\pi i A_\epsilon)=-\frac12\sum_e U_e\,dV_e.
                                                        \tag{18}
\]
This derivative identifies the actual primitive variables, including
the half-twist shear; it is stronger than a cusp-Hessian match.

The marked regulator boundary formula, in squared multiplier logs,
is
\[
 d\operatorname{Vol}(\rho)
   =\frac12\sum_e
       \{\operatorname{Re}V_e\,d\operatorname{Im}U_e
           -\operatorname{Re}U_e\,d\operatorname{Im}V_e\}.
                                                        \tag{19}
\]
The main terms vanish. Equations (18),(19) have the same differential
after the boundary correction, and (4) fixes the real constant.
Therefore on this one selected branch
\[
 2\pi\operatorname{Re}A_\epsilon
   =\operatorname{Vol}(\rho)
        -\frac12\sum_e
                \operatorname{Im}U_e\,\operatorname{Re}V_e.
                                                        \tag{20}
\]
The logarithms are not reset during continuation.

For the positive unit charge in (7), the limiting phase is
\[
 S_{\boldsymbol1}(\boldsymbol\delta)
    =A_0(\boldsymbol\delta)
       +\pi i\sum_e n_e\delta_e^2+2\pi i\sum_e\delta_e
    =A_\epsilon-2\pi i\sum_e p_e\delta_e^2
                          +2\pi i\sum_e\delta_e .
                                                        \tag{21}
\]
Its stationarity equation is exactly
\[
                       U_e+p_eV_e=-2\pi i.             \tag{22}
\]
For each fixed diagram, existence and uniqueness near zero hold for
all independently long signed powers. Indeed
\[
 A_0''(0)=-2\operatorname{diag}(C_e),\qquad
 C_e=\frac{\pi(T_{b_e}(0)+T_{c_e}(0))}{x_e+y_e}>0,
                                                        \tag{23}
\]
and separate evenness makes \(\partial_e A_0=\delta_e B_e\).
After multiplying the critical equations by \(1/n_e\), the derivative
in \(\boldsymbol\delta\) at reciprocal slopes zero is the invertible
diagonal \(2\pi i I\). The several-parameter implicit-function theorem
gives \(\delta_e=O_D(1/|n_e|)\). It allows independently unbalanced
signed \(n_e\); it does not compare a minimum error rate with a sum of
unrelated filling losses.

At a critical point, substitute (22) into (20). Since
\(V=-4\pi i\delta\), the real part of the two explicit added terms
in (21) is
\[
\operatorname{Re}(-2\pi i p\delta^2+2\pi i\delta)
       =\frac{1}{4\pi}\operatorname{Im}U\,\operatorname{Re}V .
                                                        \tag{24}
\]
The boundary corrections cancel exactly:
\[
              2\pi\operatorname{Re}S_{\boldsymbol1}
                        =\operatorname{Vol}(\rho).
                                                        \tag{25}
\]
There is no omitted complex endpoint term. To replace the right
side by the hyperbolic volume of the filled topology one still
needs the following metric argument.

## 7. Completing the specified hyperbolic filling

The construction in
[the general metric completion theorem, sections 1–5](general_source_regulator_hyperbolic_equality.md)
applies to any complete finite-volume exterior. Its neighborhood
is a neighborhood of the **framed representation**, not only of
the peripheral traces. We recall the points preventing an
exponentiated filling equation from being mistaken for a metric.

On a compact truncated core choose a finite lifted partition of
unity \(\eta_{j,\gamma}\). In the future unit hyperboloid form
\[
 Y_\rho(x)=\sum_{j,\gamma}\eta_{j,\gamma}(x)
                \rho(\gamma)\rho_0(\gamma)^{-1}x,\qquad
 E_\rho(x)=\frac{Y_\rho(x)}
                    {\sqrt{-\langle Y_\rho(x),Y_\rho(x)\rangle}} .
                                                        \tag{26}
\]
The future cone is convex; this is defined and equivariant.
On a compact fundamental part it is \(C^1\)-close to the identity,
so is a positive local diffeomorphism.

In a selected cusp frame the peripheral transformations are affine:
\(A_\rho(\lambda)z=a_\lambda z+b_\lambda\), on the original
translation lattice \(\Lambda\). A periodic partition of unity gives
\[
\begin{aligned}
d_\rho(w)&=\sum_{\lambda\in\Lambda}
   \eta(w-\lambda)A_\rho(\lambda)(w-\lambda),\\
F_\rho(w,t)&=(d_\rho(w),e^{t+\chi_\rho(w)}),
\end{aligned}                                            \tag{27}
\]
where \(\chi_\rho\) is the real-linear extension of
\(\lambda\mapsto\log|a_\lambda|\). These maps are exactly equivariant.
The first is a positive local diffeomorphism on a compact
fundamental parallelogram, and by equivariance everywhere. The
second has positive triangular differential on the entire tail.
It can be joined to (26) by a \(C^1\)-small equivariant interpolation
on a fixed compact collar.

At the selected unit-charge critical point, the limiting version of
(33) gives \(\operatorname{Im}\delta_e>0\) for either sign of
\(n_e\), since the limiting \(B_{e,N}\) in (33) has positive real part. Consequently
\(\operatorname{Re}V_e=4\pi\operatorname{Im}\delta_e>0\), so the
longitude multiplier has \(|e^{V_e}|>1\). This is a nonunit
**modulus**, not merely the weaker assertion \(e^{V_e}\ne1\).
The commuting affine maps therefore have a second common fixed
point \(q=b/(1-a)\), using \(a=e^{V_e}\) for the longitude.
As \(\rho\to\rho_0\), \(q\) escapes to infinity, whereas the developed
fundamental parallelogram and its fixed generator paths remain
bounded. They miss \(q\); equivariance makes the entire development
miss it. On its simply connected cover set \(f=\log(d_\rho-q)\).
The nonsingular invariant metric \(|df|^2\) descends to a compact
flat torus and is complete. Consequently its development is the
plane and its log periods are an injective rank-two lattice.

For each fixed generator path of image length at most \(L\), in
\(|d_\rho|\le R\), its logarithmic increment is at most
\(L/(|q|-R)\), hence tends to zero. Its exponential is the corresponding
similarity multiplier. The difference from the small prescribed
log \(U\) or \(V\) is a multiple of \(2\pi i\) tending to zero,
so is exactly zero. This proves the actual log periods **before**
multiplying them by \(p_e\). One neighborhood works for all slopes.

After moving \(q\) to zero, the tail contains a full epigraph
\(y>A|d_\rho|\). With
\[
 R_{\mathrm{tube}}=\operatorname{arsinh}(|d_\rho|/y),\quad
 \vartheta=\operatorname{Im}f,\quad
 X=\operatorname{Re}f+\tfrac12\log(1+y^2/|d_\rho|^2),
\]
its metric becomes
\[
 dR_{\mathrm{tube}}^2+\cosh^2(R_{\mathrm{tube}})\,dX^2
                   +\sinh^2(R_{\mathrm{tube}})\,d\vartheta^2 .
                                                        \tag{28}
\]
The primitive slope in (22) has angle \(-2\pi\) and zero axial
period. A complementary primitive period has nonzero real part,
because the lattice has rank two. Adding \(R_{\mathrm{tube}}=0\)
therefore adds a smooth solid torus with precisely that meridian.
Its holonomy fixes both \(q,\infty\) and has multiplier one, so is
the identity; the representation descends to the filled group.
This excludes the parabolic-slope defect which a bare equation
\(\exp(U+pV)=1\) would permit.

At every main cusp all multipliers are one, so (27) gives a complete
Euclidean torus link and a full horoball quotient. The resulting
metric is complete and finite-volume. Its universal developing local
isometry covers \(\mathbb H^3\), proving discrete faithful holonomy.

The representation volume agrees with this filled metric's volume
using the same finite boundary triangulation: compare its cusp map
with the axis-valued map by the common conical boundary homotopy,
whose volume tends to zero, and extend that triangulation through
the solid torus with all vertices on the core axis, so every added
tetrahedron has zero volume. This is the filling-chain comparison in
[the general regulator theorem, section 6](general_source_regulator_hyperbolic_equality.md);
it retains the same oriented fundamental class.

Our family satisfies the neighborhood hypothesis: (8), (14), (16),
and their chosen flags are holomorphic at zero and converge to their
original complete matrices as all \(|n_e|\to\infty\). The first-charge
solution above therefore lies in this fixed neighborhood after one
diagram-dependent threshold. Inserting (25) now gives the volume of
the actual filled manifold.

Finally, filling a crossing circle along its recorded
\(\mu_e+p_e\lambda_e\) is the local surgery in the original
twice-punctured disk collar which inserts \(-2p_e\) crossings.
The disks and collars are those constructed in \(S^3\) in section 2.
Thus the filled topology is the original diagram with powers (1),
not a comparison diagram, a tree replacement, or an unnamed
representation component.

## 8. Analytic interface and the remaining full-source problem

The independent analytic verification is recorded in
[the analytic packet and whole-period proof](actual_morse_cross_filling_period.md).
Its inputs are the exact source (5)–(7),
the positive complete radii and the original primitive face lattice.
The relevant graph facts hold here: deleting the protected adjacent
vertices from a simple triangulated sphere leaves its surviving
ordinary graph connected; a matching outer pair is not the protected
pair; every matching factor has \(x+y>0\) and at least one
nonmonomial triangle. These give the ordinary Hessian rank and
primitive angular differences used by the complex coefficient
saddle. They do not require a flat gap forest.

The companion proof establishes the local holomorphic packet and
global complex-strip spectral gap, including all odd simple-node
normals. It then applies the original contour proof to (7), with
real spectators during infinite-tail removal, exact endpoint
currents, and independent signed reciprocal slopes. That proof
returns the nonzero first-charge asymptotic, not just an upper
bound on its action. Section 9 records its exact normalization.

For an unchanged opposite-offset even bipyramid, its displayed
circle packing is a positive certificate and its oriented top and
bottom quartets are exactly the general Morse source (5).
Consequently this theorem applies to its all-CROSS term at every
fixed size, with the original parity/knot qualification. No
Conway-tree decomposition or new plat presentation is required.

What remains for its **full** invariant is a strict estimate of
the signed contribution outside CROSS, for example
\[
 \bigl|\mathcal I_{N,\mathrm{full}}
            -\mathcal I_{N,\mathrm C}\bigr|
 \le \exp\!\left[
       N\left\{\frac{\operatorname{Vol}(S^3\setminus K_{\boldsymbol p})}
                       {2\pi}-\eta\right\}+o(N)\right].
                                                        \tag{29}
\]
Failure of complete-radius balance at every mark neither invalidates
the all-CROSS theorem nor proves (29) false. It removes one known
sufficient method of proving (29). The present result makes no
claim of cancellation or domination for those remaining sectors.

## 9. The nonzero asymptotic with its finite normalization

Here is the analytic statement actually joined to the geometry,
with the finite quantities retained. On one fixed complex polydisk
there are even holomorphic face-critical actions \(A_N\) and face
Hessians \(H_N\), converging with every fixed derivative to their
limiting quantities, such that
\[
 C_N^{\mathrm{raw}}(\boldsymbol\delta)
 =\frac{(-1)^{dR}N^{2R}\exp(NA_N(\boldsymbol\delta))}
 {(2\pi N)^{(R-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
                      (1+O(N^{-1})).                    \tag{30}
\]
The action includes all finite anchors, sine and beta terms and
any \((\log N)/N\) terms; only the displayed \(N^{2R}\) was
removed. Its limit is (17). The square root in (30) is continued
from the positive complete face Hessian.

For every fixed \(\eta>0\), there are \(\gamma_\eta,\tau_\eta>0\)
such that, on the entire real spectral cube and the indicated
thin strip,
\[
\begin{gathered}
 |C_N^{\mathrm{raw}}(\boldsymbol\delta)|
       \le e^{N(\Phi_D-\gamma_\eta)},\\
 \max_e|\operatorname{Re}\delta_e|\ge\eta,\quad
 \operatorname{Re}\delta_e\in[-1/2,1/2],\quad
 |\operatorname{Im}\delta_e|\le\tau_\eta .
\end{gathered}                                           \tag{31}
\]
Fixed derivatives satisfy the same type of bound on smaller
domains. The local cofactor interpolation retains the odd
simple-node derivative, while the shared angular estimate uses
the connected ordinary graph and its primitive face-difference
rows. The separated real-spectral estimate comes from the
exact cofactor starting-row maximum. Its only monomial exception
is harmless because every crossing factor has a nonmonomial
triangle. These prove (30),(31) for the all-CROSS projection of the exact coefficient (5);
they are not inferred from a value-only local recurrence.

Let \(\boldsymbol\delta_{N,\boldsymbol1}\) be the finite
critical point of
\[
 A_N(\boldsymbol\delta)
       +\pi i\sum_e n_e\delta_e^2+2\pi i\sum_e\delta_e ,
\]
let \(S_{N,\boldsymbol1}\) be its critical value, and let
\(Q_{N,\boldsymbol1}\) be its negative spectral Hessian.
Then the **entire** period (7) is
\[
\begin{split}
\mathcal I_{N,\mathrm C}
={}&q^{d^2\sum_e n_e/4}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}\\
&\ \cdot
\frac{\prod_e\sin(2\pi\delta_{N,\boldsymbol1,e})}
 {\sqrt{\det H_N(\boldsymbol\delta_{N,\boldsymbol1})}
      \sqrt{\det Q_{N,\boldsymbol1}}}
\exp(NS_{N,\boldsymbol1})\\
&\ \cdot
\left(1+O_{\boldsymbol n}(N^{-1})
                +O_{\boldsymbol n}(e^{-\kappa_{\boldsymbol n}N})\right).
\end{split}                                              \tag{32}
\]
The spectral determinant uses the Gaussian branch on the cone
with positive real part. The sine and both determinant factors
have a nonzero limiting product for fixed sufficiently long
powers.

For clarity, the charge proof has four logically separate parts.
Separate evenness writes
\(\partial_eA_N=-2\delta_e B_{e,N}(\boldsymbol\delta^2)\),
where \(B_{e,N}\to C_e>0\). The critical equations for positive
charge magnitudes give
\[
 \delta_e=-\frac{\ell_e/n_e}
       {1+iB_{e,N}(\boldsymbol\delta^2)/(\pi n_e)},\qquad
 \operatorname{Im}\delta_e
  =\frac{\ell_e}{\pi n_e^2}
      \frac{\operatorname{Re}B_{e,N}}
          {|1+iB_{e,N}/(\pi n_e)|^2}>0.                 \tag{33}
\]
An actual outer local cube is shifted to this saddle, with every
side current retained below the saddle value. Its negative
Hessian has positive real part and its Gaussian coefficient is
one. The face and spectral Gaussian powers combine to
\[
 N^{2R}(2\pi N)^{-(R-1)/2}(2\pi/N)^{R/2}
                         =\sqrt{2\pi}\,N^{R+1/2}.       \tag{34}
\]

Next, differentiating the critical value gives the joint comparison
\[
 \operatorname{Re}S_{N,\boldsymbol1}
       -\operatorname{Re}S_{N,\boldsymbol\ell}
   \ge\sum_e\frac{C_e}{2n_e^2}(\ell_e^2-1)
                                                        \tag{35}
\]
on a fixed scaled local charge box. This is why unequal slopes
cause no loss of the theorem: it compares the critical values
in one joint family, rather than discarding local errors
independently.

Third, infinite far charges are removed on whole real intervals,
with the other coordinates kept as real spectators. The sine
factor gives zero endpoint values and equal first derivatives;
three integrations by parts retain the second-derivative endpoint
current. On the shifted contour the two vertical endpoints are
paired before estimation. Their hyperbolic-sine difference and
(31) give a summable strict gap. The degree-\(d\) cosine bound
controls the remaining horizontal interval. Only then is the
remaining finite charge set divided into local and bounded-bad
charges. A separate smaller cube, not the outer saddle cube,
controls the latter by a one-coordinate shift. All connectors
and all original endpoints are included.

Finally, reflecting any charge sign changes both its sine integral
and its charge weight, so all \(2^R\) unit signs agree. The raw
parity sign cancels exactly:
\[
             (-1)^{dR}(-1)^{(N+1)R}=1 .                \tag{36}
\]
This leaves the original \(q\) phase and the factor \((-2i)^R\)
in (32). Neither the sign choice of a power nor the parity of \(N\)
can force cancellation of that leading coefficient.

Equations (30)–(36) give the nonzero lower as well as the upper
asymptotic. Taking its logarithm and using (25) and the metric
construction proves (2),(3). Thus the flat-plat wording in the
older all-CROSS theorem is a limitation of its stated input,
not a remaining mathematical restriction after these separate
Morse source, analytic, and geometric arguments.
