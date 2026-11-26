# Radial charge compactness and the sharp corner alternative

Private written proof, 15 November 2026.

A positive unit-charge solution with complete outside angles gives
uniform bounds on every height, real return and square covector at
every positive solution with common charge \(0<\chi\le1\). The bounds
do not assume that those positive solutions form a connected charge
interval. Any first loss of positivity at a positive charge must
therefore have a finite corner limit satisfying the sharp
gradient-limit equality, rather than only the weaker corner
subgradient inequality.

This does not exclude that corner event. In particular it does not
prove that existence at charge one implies existence at every smaller
charge. The original finite quantum cycle is not changed or estimated.

## 1. Original graph, branches and constants

Take a finite graph of the original positive edge blocks, with the
incidence-counted peripheral sums of the pinned period theorem. An
original ordered circle tree is a special case. Let \(S\ne\varnothing\)
be its selected vertices, and include each edge incident to \(S\)
once. Each selected vertex has positive original degree. A loop
contributes two endpoint incidences to its vertex. The graph extension
uses these same block formulas and sums; it asserts no new topological
realization for an arbitrary graph.

Prescribe real powers \(n_v\), and put every outside angle equal to
zero. For the original integer filling data the relation
\(n_v=\eta_v-2p_v\), including its marking, stays fixed. The radial
equations are
\[
 R_v(t)-\frac{i n_v}{2}t_v=-\pi i\chi,\qquad
 R_v=\sum_{e\ni v}r_{v,e},\qquad 0\le\chi\le1.
 \tag{1}
\]
All returns and angles use the canonical branches continued from
completeness. In particular,
\[
 r_{v,e}=\operatorname{arsinh}
       \bigl(\tan(t_v/2)\cos(t_w/2)\bigr),\qquad
 |\operatorname{Re}t_v|<\pi,\quad
 |\operatorname{Im}r_{v,e}|<\pi/2
 \tag{2}
\]
at a positive edge \(e=(v,w)\).

Assume there is a positive solution at \(\chi=1\), and denote its
real angle assignment by \(z_1\). Write
\[
 t_v=s_v-iH_v,\qquad h_v=\operatorname{Im}t_v=-H_v,\qquad
 r_{v,e}=k_{v,e}+i g_{v,e}.
 \tag{3}
\]
The sign \(H_v>0\) at a positive solution with \(\chi>0\) is proved
below, not included in the definition of positivity.

For each oriented edge the square coordinates and covectors are
\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,&A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,&y_Q&=g_{v,e}/2-s_w/4,
 \end{aligned}
 \tag{4}
\]
\[
 x=E_A=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\qquad
 B=E_y=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{5}
\]
The square energy is normalized by \(E(0,0)=0\). The pinned convex
theorem gives its positive definite Hessian in
\((-\pi/4,\pi/4)^2\), continuous extension to the closed square,
and constant boundary value \(G_{\rm Cat}/2\). Consequently
\[
 0\le E(A,y)\le G_{\rm Cat}/2.
 \tag{6}
\]
Let \(e_G\) be the number of included edges, and set
\[
 \begin{split}
 \alpha&=\min_{\text{all square coordinates at }z_1}
                      \left(\frac{\pi}{4}-|\text{coordinate}|\right)>0,\\
 E_{\max}&=4e_GG_{\rm Cat}=\pi e_GM_\infty,\qquad
                         M_\infty=4G_{\rm Cat}/\pi,\\
 H_*&=E_{\max}/\alpha,\\
 K_*&=\max\left\{3H_*,
                  \operatorname{arsinh}\bigl(\cosh(H_*/2)\bigr)\right\},\\
 L_*&=K_*/2+H_*/4.
 \end{split}
 \tag{7}
\]
These are finite constants determined by the supplied positive unit
point and original graph. No numerical value of them is needed.

## 2. The closed minimizers at every radial charge

Let \(X\) be the ambient open angle body, with outside \(s_b=0\),
defined by
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi.
 \tag{8}
\]
Its closure \(\overline X\) uses weak inequalities. It is compact:
every selected vertex has an incidence, all selected real angles
are bounded by \(\pi\), and every incidence is bounded by \(\pi/2\).
Define the row maps and total energy by
\[
 \rho_v(z)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 \mathcal E(z)=4\sum_e(E_{P,e}+E_{Q,e}).
 \tag{9}
\]
There is no outside work term, because the full outside angles are
zero. The edge-square map is injective, so \(\mathcal E\) has positive
definite Hessian on \(X\), and
\[
                          0\le\mathcal E\le E_{\max}
                                        \quad\hbox{on }\overline X.
 \tag{10}
\]

For \(0\le\chi\le1\), put
\[
 \overline{\mathcal P}_\chi
       =\{z\in\overline X:\rho_v(z)=-\pi\chi\ (v\in S)\}.
 \tag{11}
\]
The test assignment \(\chi z_1\) means scaling all selected \(s_v\)
and all incidence variables, including outside incidences. Since
the fixed outside real angles are zero, every square coordinate
scales by \(\chi\), and
\[
 \rho_v(\chi z_1)=-\pi\chi,\qquad
 \text{each square margin at }\chi z_1\text{ is at least }\alpha.
 \tag{12}
\]
Thus strict feasibility is uniform even at \(\chi=0\). This is a
primal test assignment, not a claim that geometric angles or periods
scale to another solution.

The existing convex theorem gives a unique closed minimizer
\(z_\chi\) of \(\mathcal E\) on (11), for every \(\chi\in[0,1]\).
It has no open-side square; it may have corners.
The map \(\chi\mapsto z_\chi\) is continuous on \([0,1]\).
Here is a direct proof of the last assertion. A sequence of minimizers
has convergent subsequences in \(\overline X\), and any limit at
\(\chi_0\) is feasible there. Given a comparison \(z\) feasible at
\(\chi_0\), first replace it by
\[
 z^\varepsilon=(1-\varepsilon)z+\varepsilon\chi_0z_1\in X.
 \tag{13}
\]
For \(\chi_j\to\chi_0\), the assignment
\(z^\varepsilon+(\chi_j-\chi_0)z_1\) stays in \(X\) for large \(j\)
and has the exact rows at \(\chi_j\). Pass to the minimum inequality
and then let \(\varepsilon\downarrow0\). The limiting minimizer is
optimal at \(\chi_0\), hence equals its unique \(z_{\chi_0}\).

By the original variational theorem, \(z_\chi\in X\) if and only if
the original equations (1) have a positive solution. Define
\[
                I=\{\chi\in[0,1]:z_\chi\in X\}.
 \tag{14}
\]
It is relatively open and contains neighborhoods of both zero and
one. At zero the minimizer is the complete assignment \(z_0=0\).
The original complete Jacobian is
\(\tfrac12\operatorname{diag}(d_v-i n_v)\), so it is invertible;
the positive solution for small real \(\chi\) has
\[
 t_v(\chi)=-\frac{2\pi i}{d_v-i n_v}\chi+O(\chi^2).
 \tag{15}
\]
At one, and at any other positive solution, the original period
Jacobian is nonsingular. Neither this fact nor (12)--(14) asserts
that \(I\) is connected.

## 3. Uniform height and return bounds on the whole positive set

**Theorem 1.** At every positive solution with
\(\chi\in I\cap(0,1]\), independently of its component in \(I\),
\[
 0<H_v,\qquad \sum_{v\in S}H_v\le H_*,
 \qquad |k_{v,e}|\le K_*,
 \qquad |x_P|,|x_Q|,|B_P|,|B_Q|\le L_*.
 \tag{16}
\]
All outside returns and heights are zero.

**Proof.** The proper-prefix positivity lemma gives, for each selected
endpoint of a positive edge,
\[
 \ell_{v,e}=\operatorname{Re}(r_{v,e}\overline{t_v})>0
                                                \quad(t_v\ne0).
 \tag{17}
\]
It is an edge statement, so it also applies individually to both
incidences of a loop. If \(t_v=0\), every return at that vertex is
zero by (2), contrary to (1) with \(\chi>0\). Pairing (1) with
\(\overline{t_v}\) therefore gives
\[
              \sum_{e\ni v}\ell_{v,e}=\pi\chi H_v>0.
 \tag{18}
\]
In particular \(H_v>0\).

At the positive solution the full ambient gradient identity is
\[
                  d\mathcal E(z_\chi)
                           =-\sum_{v\in S}H_v\,d\rho_v.
 \tag{19}
\]
This includes the outside incidence directions: their gradient
coefficients are their prescribed outside imaginary angles, zero.

Choose one selected endpoint incidence at each vertex. Starting from
\(\chi z_1\), decrease the chosen \(g\) at each selected vertex by
\(\alpha\), and leave all other coordinates unchanged. Call the
result \(y_\chi\). Each square coordinate changes by at most
\(\alpha/2\). Perturbations at opposite endpoints affect its \(A\)
and \(y\) coordinates separately, including when the edge is a loop.
Thus (12) gives a strict margin at least \(\alpha/2\), and
\[
                       \rho_v(y_\chi)=-\pi\chi-\alpha.
 \tag{20}
\]
This point need not satisfy the original radial charge rows. It is
an admitted comparison in the ambient angle body.
The supporting inequality at \(z_\chi\), (19), and (10) yield
\[
 \alpha\sum_{v\in S}H_v
       \le\mathcal E(y_\chi)-\mathcal E(z_\chi)
       \le E_{\max}.
 \tag{21}
\]
This proves the uniform height bound.

For a selected incidence, (3), (17) and (18) give
\[
 s_vk_{v,e}=\ell_{v,e}+H_vg_{v,e},\qquad
 0<\ell_{v,e}\le\pi\chi H_v,\qquad |g_{v,e}|<\pi/2.
 \tag{22}
\]
If \(|s_v|\ge\pi/2\), it follows that
\[
                         |k_{v,e}|\le3H_v\le3H_*.
 \tag{23}
\]
If \(|s_v|\le\pi/2\), the exact identities
\[
 |\tan((s_v-iH_v)/2)|^2
       =\frac{\cosh H_v-\cos s_v}{\cosh H_v+\cos s_v}\le1,
 \qquad
 |\cos(t_w/2)|^2
       =\frac{\cosh H_w+\cos s_w}{2}\le\cosh^2(H_*/2)
 \tag{24}
\]
hold, with \(H_w=0\) for an outside endpoint. Formula (2) then
implies \(|\sinh r_{v,e}|\le\cosh(H_*/2)\).
Since
\[
 |\sinh(k+i g)|^2=\sinh^2 k+\sin^2 g,
 \tag{25}
\]
we obtain the other bound in the definition of \(K_*\).
At an outside endpoint \(t_b=0\), (2) gives \(r_{b,e}=0\).

Finally the original edge identities give
\[
 x_P=k_{v,e}/2-h_w/4,\qquad x_Q=k_{v,e}/2+h_w/4,\qquad
 B_P=h_v/4+k_{w,e}/2,\qquad B_Q=h_v/4-k_{w,e}/2.
 \tag{26}
\]
The preceding bounds imply the claimed \(L_*\). \(\square\)

There is also a direct bound on every original tetrahedron modulus.
The four generating shapes are
\[
 i e^{r_{v,e}}e^{-it_w/2},\quad
 i e^{-r_{v,e}}e^{-it_w/2},\quad
 i e^{it_v/2}e^{-r_{w,e}},\quad
 i e^{it_v/2}e^{r_{w,e}},
 \tag{27}
\]
and the other four are their negative reciprocals. Every shape \(Z\)
therefore obeys
\[
 e^{-(K_*+H_*/2)}\le |Z|\le e^{K_*+H_*/2}.
 \tag{28}
\]
Approach to the real axis, including the value one, is not excluded
by this annulus bound.

## 4. Every limiting alternative, including the zero endpoint

**Theorem 2.** Let \(\chi_j\in I\cap(0,1]\) tend to
\(\chi_*\in[0,1]\).

1. The primal assignments converge to the unique closed minimizer
   \(z_{\chi_*}\). The finitely many heights, returns and square
   covectors admit a jointly convergent subsequence with the bounds
   (16).
2. If \(\chi_*=0\), all these coordinates tend to their complete
   values. In particular \(t_v,r_{v,e},x_P,B_P,x_Q,B_Q\to0\).
3. If \(\chi_*>0\) and \(z_{\chi_*}\in X\), it is the original
   positive solution at \(\chi_*\), and the period implicit-function
   theorem extends it through that parameter.
4. Otherwise at least one square is a corner and no square is on an
   open side. At every corner
   \((A,y)=(\varepsilon_A\pi/4,\varepsilon_y\pi/4)\), each limiting
   covector satisfies
\[
 U=\varepsilon_Ax>0,\qquad V=\varepsilon_yB>0,\qquad
                         \sinh(2U)\sinh(2V)=1.
 \tag{29}
\]
   All original affine rows, endpoint matching relations and real
   period equations remain valid in the limit, with those covectors.

**Proof.** Primal convergence follows from Section 2, and Theorem 1
gives the stated subsequential compactness. At zero,
\[
 0\le\mathcal E(z_{\chi_j})\le\mathcal E(\chi_jz_1)\longrightarrow0.
 \tag{30}
\]
The unique zero of the nonnegative square sum is the complete angle
assignment, since its square-coordinate map is injective. Thus every
square coordinate tends to zero, where its inverse and gradient (5)
are continuous. Equations (26) and the original edge-coordinate
identities give all the claimed complete limits.

An interior limit reconstructs the original matched positive solution
by the convex variation theorem. Its nonsingular complex period
Jacobian gives the extension in part 3.

An open-side limit would contradict the bounded covectors: for
example, if \(A\to\varepsilon_A\pi/4\) and
\(|y|\le\pi/4-\epsilon\), then (5) makes \(|x|\to\infty\).
The other three open sides are identical. Hence a boundary limit
has a corner.

At an interior square the exact algebraic identity is
\[
              \sinh(2x)\sinh(2B)=\sin(2A)\sin(2y).
 \tag{31}
\]
Also \(x\) has the sign of \(A\), and \(B\) has the sign of \(y\).
At a corner the right side tends to
\(\varepsilon_A\varepsilon_y\). The finite covector limit
therefore has \(U,V\ge0\) and
\(\sinh(2U)\sinh(2V)=1\), forcing both to be positive.
This proves (29) with equality.

For clarity, the matching and real-period relations being passed
to the limit are
\[
 h_{v,e}=2(B_P+B_Q)=h_v,\qquad
 h_{w,e}=-2(x_P-x_Q)=h_w,\qquad
 k_{v,e}=x_P+x_Q,\qquad k_{w,e}=B_P-B_Q,
 \tag{32}
\]
\[
 \rho_v=-\pi\chi,\qquad
                     \sum_{e\ni v}k_{v,e}+n_vh_v/2=0.
 \tag{33}
\]
They are finite linear identities, so they survive subsequential
limits without choosing new logarithmic branches. \(\square\)

**Corollary 3 (no zero-height limit at positive charge).**
For every \(0<\chi_0\le1\), there is a constant \(h_0>0\) such that
\[
 H_v(\chi)\ge h_0
       \qquad(v\in S,\ \chi\in I\cap[\chi_0,1]).
 \tag{33a}
\]
This does not require a complete outside neighbor in every selected
component. In particular, uniformly on this set,
\[
 |\sin t_v|\ge\sinh h_0,\qquad
 |\sin(t_v/2)|\ge\sinh(h_0/2),\qquad
 |\cos(t_v/2)|\ge\sinh(h_0/2).
 \tag{33b}
\]

**Proof.** If (33a) failed, choose a sequence as in Theorem 2, with
\(\chi_*\ge\chi_0\), and a vertex \(v\) whose height tends to zero.
Pass to a joint limit of all bounded coordinates. Prefix pairings
are nonnegative in the limit and sum to \(\pi\chi_*H_v=0\), so
\[
                    s_vk_{v,e}=0
                                  \quad\hbox{for every incidence at }v.
 \tag{33c}
\]
All limiting \(H_w\) are nonnegative, all \(|s_w|\le\pi\), and all
returns stay in the closed range \(|g_{w,e}|\le\pi/2\).
Use the exact original identity in a form that has no division:
\[
 \sinh r_{v,e}\,\cos(t_v/2)
                       =\sin(t_v/2)\cos(t_w/2).
 \tag{33d}
\]
It holds before the limit by (2), and every factor is bounded by
Theorem 1. Thus it passes to the limit even at an angular endpoint;
no inverse-hyperbolic branch is extended across a cut.

If \(s_v=0\), then \(t_v=0\), and (33d) gives
\(\sinh r_{v,e}=0\) at every incidence. The closed canonical range
forces \(r_{v,e}=0\). Equation (1) would then have zero left side
and nonzero right side, a contradiction.

If \(0<|s_v|<\pi\), (33c) gives \(k_{v,e}=0\).
Taking real parts of (33d) forces
\[
 0=\operatorname{Re}\cos(t_w/2)
            =\cos(s_w/2)\cosh(H_w/2),
 \tag{33e}
\]
since \(\sin(s_v/2)\ne0\). Hence \(|s_w|=\pi\) at every neighbor.
The weak edge inequality then gives \(g_{v,e}=0\), so
\(r_{v,e}=0\). The full identity (33d) now gives
\(\cos(t_w/2)=0\), hence \(H_w=0\) as well. Apply (33d) at
this neighboring endpoint \(w\): its cosine is zero and its sine
is \(1\) or \(-1\), so \(\cos(t_v/2)=0\). This contradicts
\(0<|s_v|<\pi\). The same argument includes a loop.

The only remaining zero-height possibility is therefore
\[
                            s_v=\pi\ \hbox{or}\ -\pi.
 \tag{33f}
\]
At such an endpoint (33d) forces \(\cos(t_w/2)=0\) at every
neighbor: \(|s_w|=\pi\) and \(H_w=0\). This propagates along all
edges of the selected component. A complete outside neighbor would
contradict it immediately, since its cosine is one.

If the propagated component has no outside neighbor, it is a whole
connected component of the included graph. Every vertex in it has
\(|s|=\pi,H=0\). Every incidence is zero by the weak inequalities.
Consequently both square factors of every edge are corners. If
the component has \(e_C\) edges, its energy is exactly
\(4e_CG_{\rm Cat}\).

Replace only this component of \(z_{\chi_*}\) by the corresponding
component of \(\chi_*z_1\). There is no outside edge to change.
The replacement has the same charge rows and is strictly interior
by (12). Every square energy is strictly less than
\(G_{\rm Cat}/2\): the boundary energy is constant, while strict
convexity excludes that maximum in the interior. Thus the replacement
strictly lowers the energy of this component. Its edge count is
positive because every selected vertex has positive degree.
This contradicts the minimizing property of \(z_{\chi_*}\).

All zero-height alternatives have been excluded. Compactness and
the finiteness of \(S\) prove a uniform \(h_0\) in (33a).
Finally
\[
 |\sin(s-iH)|^2=\sin^2s+\sinh^2H,\qquad
 |\cos(s-iH)|^2=\cos^2s+\sinh^2H
 \tag{33g}
\]
give (33b), also at half angles. \(\square\)

The lower bound prevents these sine and half-angle observation
factors from vanishing even along a corner approach at positive
charge. It does not prevent square corners or make their Hessians
nonsingular, and it is not a lower bound on the original scalar.

The general corner KKT condition permits
\(\sinh(2U)\sinh(2V)\ge1\). Theorem 2 requires equality at a
corner reached from actual positive radial solutions.
An arbitrary corner certificate with strict inequality is therefore
not a counterexample to radial continuation from a positive unit
point. Conversely, equality does not itself exclude a corner.
The square Hessian can have a collapsing and a diverging eigenvalue
there, so interior nonsingularity does not justify continuation
through it.

Thus the component of \(I\) containing one can fail to reach zero
only through the specific finite boundary system (29), (32), (33).
The component containing zero also exists by (15). This note
does not prove that the two components coincide, or that any
intervening corner event actually occurs. It gives a necessary
boundary system, not a sufficient criterion for such an event.

## 5. The comparison at an existing positive charge vector

For completeness, the supporting-plane comparison has a direct
extension independent of radial continuation. Suppose an original
positive solution with baseline charge vector
\(\boldsymbol\chi\), \(\chi_v>0\), is already given. Complete outside
data are not required for this paragraph; retain their full linear
work in the energy. Put \(H_v=-\operatorname{Im}t_v>0\).
The prefix comparison or vertex reflection gives this strict sign
with \(\pi\chi_vH_v\) in place of (18).

With the Bregman remainder based at this solution,
\[
 D_{\boldsymbol\chi}(z)
  =\mathcal E(z)-\mathcal E(z_{\boldsymbol\chi})
                   -d\mathcal E(z_{\boldsymbol\chi})
                                      (z-z_{\boldsymbol\chi}),
 \tag{34}
\]
the exact ambient formula is
\[
 \mathcal E(z)-\mathcal E(z_{\boldsymbol\chi})
       =D_{\boldsymbol\chi}(z)
                       +\pi\sum_v H_v(c_v-\chi_v)
            \quad\hbox{when }\rho_v(z)=-\pi c_v.
 \tag{35}
\]
The minimum \(\delta_{\boldsymbol\chi}\) of this remainder on the
ambient angle boundary is strictly positive by the same compact
strict-convexity argument as in the adopted split-current gap.

For a nonempty deleted set \(C\), suppose
\(|n_v|/2\ge\chi_v\) there, and suppose an admitted deleted weak
assignment has surviving charges \(|c'_w|\ge\chi_w\). Reflect
negative surviving charges as in that theorem, set each removed
\(s_v=\operatorname{sgn}(n_v)\pi\), and set all restored incidences
to zero. The exact edge-boundary energy gives
\[
 \boxed{\quad
 M_{\boldsymbol\chi}-M_{\rm del}
  \ge\frac{\delta_{\boldsymbol\chi}}{\pi}
     +\sum_{v\in C}H_v\left(\frac{|n_v|}{2}-\chi_v\right)
     +\sum_{w\in S\setminus C}H_w(|c'_w|-\chi_w)>0 .
 \quad}
 \tag{36}
\]
The actions include the charge term \(-i\sum c_vt_v\). Their
normalization follows from the same original edge identity as in
the split-current theorem. Isolated surviving vertices retain their
rows and the bound \(|s_w|\le\pi\); empty deleted assignment sets
are not assigned an action.

Formula (36) compares actions at an existing positive baseline.
It neither constructs that baseline at another charge nor changes
a charge in the original finite source.

## Direct sources and scope

The five pinned source proofs were read in full.

* [Original convex variation](research_positive_filling_convex_variation.md),
  SHA256 2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0:
  square energy, injective coordinates, continuous extension,
  closed minimizer uniqueness, and original charged variational rows.
* [Global original periods](research_positive_edge_global_monotonicity.md),
  SHA256 da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500:
  exact return and shape formulas, canonical branch ranges,
  original finite-network extension, uniqueness and period Jacobian.
* [Positive proper prefixes](research_positive_primitive_prefix_regularity.md),
  SHA256 a01b55a71d133aadff4aac0929e50de03e1059991d6874e81646c770eb5604a6:
  strict individual pairing with the endpoint angle; its proof is
  independent of the value of the later prescribed positive charge.
* [Corner KKT conditions](research_positive_filling_corner_kkt.md),
  SHA256 6c70541966289535c95cd223050ca68e1748b076a2bb3021f941f2744df26a71:
  constant square-boundary energy and the distinction between sharp
  gradient limits and the full corner subdifferential.
* [Split-current action gap](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc:
  ambient Bregman boundary gap, signed-charge reflection, exact
  deleted-edge calibration and source scope of the final comparison.

The new compactness estimate removes divergent heights, returns and
square covectors as possible failures on this radial positive set.
It also excludes zero-height limits on closed positive-charge
intervals.
The sharp equality-corner system remains. No general no-corner
theorem, volume theorem, quantum contour transport or nonzero
geometric coefficient is asserted.

Only written proofs, source-text reads and file hashes were used.
No mathematical code, numerical evaluation, test or compilation was
run. Frozen notes, manuscripts and public documents were unchanged.
