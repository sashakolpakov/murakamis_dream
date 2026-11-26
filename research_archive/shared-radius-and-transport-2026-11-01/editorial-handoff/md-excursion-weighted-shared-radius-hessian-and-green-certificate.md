# Shared face reweighting from the triangle Hessian

This note gives a quantitative way to construct the shared vectors in a genuine-sector certificate. It keeps the original coefficient targets and every spectator envelope. It does not assert that the resulting test succeeds for every matched sphere.

There are three conclusions. The exact triangle Hessian is an electrical-network Laplacian. Scaling a large set of faces costs at most a quantity determined by the complete angles across its boundary, which generalizes the global compression in the all-even bipyramid proof. Finally a finite convex quadratic program, with an exact dual involving the network Green operator, supplies sufficient shared vectors for arbitrary genuine-sector branches. A separate zero-load dual condition proves that some proposed branch tests cannot succeed.

The existing seventeen-port certificate separation already rules out universal success for one anchor with unrestricted spectators. Refining genuine source labels can remove that obstruction. Splitting the two comparison atoms inside a one-sided bound into separate fictitious quantum sectors is not allowed.

## 1. Original face data and branch costs

Fix a simple triangulated sphere with a perfect matching of its cubic dual, its original ordered ports, and a protected adjacent MAIN pair. Write \(V\) for the ordinary white faces. Protected weights remain exactly zero, while
\[
 w_f=e^{q_f}>0,\qquad f\in V.
 \tag{1}
\]
Every ordinary coefficient target remains \(d=N-1\). The logarithmic variable \(q_f\) is shared by all incidences of the face \(f\). These weights are source curvatures.

For each original triangle \(t\), let \(Q_t(q)\) be the absolutely normalized complete triangle potential. At a triangle with positive weights \(a,b,c\), put
\[
 D^2=ab+bc+ca,\qquad
 \alpha_a=\arctan(a/D),\qquad
 \partial_{q_a}Q_t=\alpha_a/\pi .
 \tag{2}
\]
The same formula holds on the two-positive-coordinate stratum. A row with just one ordinary coordinate is exactly \(Q_t=q_f/2\). Protected coordinates are absent from the differentiation. The supported angles sum to \(\pi/2\).

Let
\[
 P(q)=\sum_t Q_t(q)-\sum_{f\in V}q_f,\qquad
 P(q_*)=\Phi,\qquad \nabla P(q_*)=0 .
 \tag{3}
\]
Here \(q_*\) is the complete marked curvature vector supplied by the original packing, and \(2\pi\Phi\) is its augmented volume. The face-star equation is
\[
 \sum_{t\ni f}\alpha_{tf}(q_*)/\pi=1
 \quad(f\in V).
 \tag{4}
\]
The two triangles at each matched port are the original triangles of the sphere, so none has been duplicated or reassigned.

For a port \(e=(x,b,c,y)\), write \(Q_b=Q(x,b,y)\), \(Q_c=Q(x,c,y)\), and \(X_e=Q_b+Q_c\). The genuine local labels have the established weighted value bounds
\[
 \begin{aligned}
 A_{e,C}&=X_e,\\
 A_{e,L}&=\max(q_c,Q_b+q_c/2),\\
 A_{e,R}&=\max(q_b,Q_c+q_b/2).
 \end{aligned}
 \tag{5}
\]
A one-sided label with protected overloaded middle is absent. Thus no logarithm of zero occurs.

A branch \(B\) chooses an allowed subset of \(\{C,L,R\}\) at each port. Expand its maxima into the finite list \(\mathcal A_{B,e}\) of scalar comparison atoms: \(X_e\), \(q_c\), \(Q_b+q_c/2\), \(q_b\), or \(Q_c+q_b/2\), as appropriate. Its exact envelope cost is
\[
 G_B(q)=\sum_e\max_{A\in\mathcal A_{B,e}}A(q)
                    -\sum_{f\in V}q_f.
 \tag{6}
\]
Each atom is convex in \(q\), has total logarithmic degree one, and contains a subset of the two original triangle potentials plus a linear function. Consequently \(G_B\) is convex and invariant under a common shift of all \(q_f\).

The local estimates in (5) are phase-uniform weighted value estimates. The conclusions below concern their actual simultaneous shared-vector cost. Applying them to a full source additionally requires its exact homogeneous Morse identity, the whole-cube local estimates, and a genuine finite cover of the unwanted strings. The existing general-Morse CROSS theorem and finite filling norm are separate analytic inputs. No change to a physical sign, normal or framing factor is made here.

## 2. The exact triangle Laplacian

For two distinct positive coordinates of one triangle, direct differentiation of (2) gives
\[
 \frac{\partial^2Q_t}{\partial q_i\partial q_j}
       =-\kappa^t_{ij},\qquad
 \kappa^t_{ij}
       =\frac{w_iw_j}{2\pi D(w_i+w_j)}.
 \tag{7}
\]
Indeed \(D^2+w_i^2=(w_i+w_j)(w_i+w_k)\), which cancels the remaining factor in differentiating the arctangent. The angle is unchanged by common scaling, so every Hessian row sums to zero. Thus
\[
 v^{\mathsf T}\nabla^2Q_t(q)v
       =\sum_{\{i,j\}\subset t\cap V}
                  \kappa^t_{ij}(q)(v_i-v_j)^2 .
 \tag{8}
\]
For two positive coordinates the same calculation uses \(D=\sqrt{w_iw_j}\). For one positive coordinate the Hessian is zero.

The conductances are positive and obey the global bound
\[
 0<\kappa^t_{ij}\le\frac1{4\pi},
 \tag{9}
\]
since \(D\ge\sqrt{w_iw_j}\) and \(w_i+w_j\ge2\sqrt{w_iw_j}\).

Let \(L(q)=\nabla^2P(q)\) be the sum of these triangle Laplacians, and define the fixed combinatorial Laplacian \(\overline L\) by
\[
 v^{\mathsf T}\overline L v
  =\frac1{4\pi}\sum_t\sum_{\{i,j\}\subset t\cap V}(v_i-v_j)^2 .
 \tag{10}
\]
Multiplicity in this sum is intentional: an ordinary white edge belongs to two original triangles. We have
\[
 0\le L(q)\le\overline L.
 \tag{11}
\]
Removing the protected adjacent pair from a simple triangulated sphere leaves a connected ordinary-face graph. Every remaining white edge appears in the sum. Therefore both Laplacians have kernel exactly the constant vectors. They are positive definite on
\[
 \mathcal H=\{v:\sum_{f\in V}v_f=0\}.
 \tag{12}
\]
Equivalently one may pin one ordinary logarithmic weight.

Taylor's formula and (3) now prove the global bound
\[
 0\le P(q_*+v)-\Phi
     \le\frac12v^{\mathsf T}\overline L v .
 \tag{13}
\]
This is a bound on the entire complete action, not a sum of independently optimized local coefficients.

## 3. A sharper local bound and a general cut-scaling lemma

The geometric conductances can replace the coarse constant \(1/(4\pi)\) on a bounded displacement. Put
\[
 \operatorname{osc}v=\max_fv_f-\min_fv_f.
\]
Along \(q+sv\), logarithmic differentiation of (7) gives
\[
 \frac{d}{ds}\log\kappa^t_{ij}(q+sv)
 =\frac{w_jv_i+w_iv_j}{w_i+w_j}
   -\frac12
       \frac{\sum_{\{a,b\}\subset t\cap V}w_aw_b(v_a+v_b)}
            {\sum_{\{a,b\}\subset t\cap V}w_aw_b}.
 \tag{14}
\]
Both displayed terms are convex averages of the values of \(v\). Hence the absolute value is at most \(\operatorname{osc}v\). The same proof covers two-positive rows. If \(\operatorname{osc}v\le r\), then
\[
 P(q_*+v)-\Phi
   \le F(r)\,v^{\mathsf T}L(q_*)v,\qquad
 F(r)=\frac{e^r-1-r}{r^2},\quad F(0)=\frac12.
 \tag{15}
\]
This follows by integrating
\(L(q_*+sv)\le e^{sr}L(q_*)\) against \(1-s\). It requires no smallness assumption beyond the stated finite oscillation bound.

There is a useful different estimate for a cut. Let \(U\subset V\), and change \(q\) to \(q_*+s\mathbf1_U\). Only triangles meeting both \(U\) and \(V\setminus U\) contribute a nonlinear change. Define their complete angle masses
\[
 a_U=\frac1\pi\sum_{t\text{ crossing }U}\sum_{f\in t\cap U}\alpha_{tf}(q_*),
 \qquad
 b_U=\frac1\pi\sum_{t\text{ crossing }U}\sum_{f\in t\cap(V\setminus U)}\alpha_{tf}(q_*).
 \tag{16}
\]
Here the inner sums use ordinary positive coordinates; protected zeros carry no angle. The face equations imply \(a_U\le|U|\), \(b_U\le|V\setminus U|\).

For \(s\le0\),
\[
 P(q_*+s\mathbf1_U)-\Phi
       \le b_U(e^{-s}-1+s).
 \tag{17}
\]
To prove this, let \(b(s)\) be the moving outside angle mass on the same crossing triangles. Its derivative is minus the sum of the crossing conductances. For each angle in a row with at least two positive coordinates,
\[
 0\le \partial_{q_i}\alpha_i
      =\sin\alpha_i\cos\alpha_i
          \left(1-\frac{w_i\sum_{j\ne i}w_j}{2D^2}\right)
      \le\alpha_i .
 \tag{18}
\]
Thus \(-b'(s)\le b(s)\), and \(b(s)\le e^{-s}b(0)\) for \(s\le0\). Since the complete derivative vanishes, the derivative of \(P(q_*+s\mathbf1_U)\) is \(b(0)-b(s)\). Integrating backwards from zero gives (17).

By common-scale invariance, positive scaling of \(U\) is negative scaling of its complement. Consequently
\[
 P(q_*+s\mathbf1_U)-\Phi
       \le a_U(e^s-1-s)\qquad(s\ge0).
 \tag{19}
\]
These estimates can be independent of the number of faces in \(U\). They depend on boundary angle mass, not the number of separately bounded coupons.

In the all-even bipyramid, take \(U\) to be the ordinary rim faces. The two pole stars have total mass two; their two one-positive-coordinate rows have total mass one and are not crossing rows. Therefore \(b_U=1\). Equation (17), with \(s=\log\lambda\), is precisely the bound
\(\lambda^{-1}-1+\log\lambda\) used in the three-witness argument. This identifies a general source-geometric mechanism behind that size-independent estimate.

## 4. A finite convex quadratic sufficient certificate

At the complete vector define, for every retained atom,
\[
 c_{e,A}=A(q_*)-X_e(q_*),\qquad
 p_{e,A}=\nabla A(q_*)-\nabla X_e(q_*).
 \tag{20}
\]
Each \(p_{e,A}\) has total sum zero. All entries are explicit complete angles and the original half- or full-face loads.

Define the piecewise-linear function
\[
 \ell_B(v)=\sum_e\max_{A\in\mathcal A_{B,e}}
                         \{c_{e,A}+p_{e,A}\cdot v\}.
 \tag{21}
\]
Then, for every \(v\),
\[
 G_B(q_*+v)-\Phi
       \le \mathcal U_B(v)
       :=\frac12v^{\mathsf T}\overline L v+\ell_B(v).
 \tag{22}
\]
Here is a proof that retains all envelopes. Choose one atom at every port. The resulting smooth cost is convex and its Hessian is a sum of a subset of the original triangle Hessians, hence is bounded above by \(\overline L\). Taylor expansion at \(q_*\) gives the corresponding affine expression from (20) plus the same quadratic term. Take the maximum over all choices. Because choices at different ports are independent inside a branch, that maximum is exactly (21).

In the anchored case this also reads
\[
 \mathcal U_B(v)=\frac12v^{\mathsf T}\overline L v
  +\sum_{j\ne e}\max(0,\ \text{affine left defect},\
                                      \text{affine right defect})
  -\min(\text{two affine anchor losses}).
 \tag{23}
\]
In particular, no unanchored \(H_j-X_j\) has been omitted. Convexity of \(Q\) bounds each such excess from above by its affine defect and bounds each anchor-loss branch from below by its affine tangent.

**Sufficient criterion.** If a finite vector \(v_B\) satisfies
\(\mathcal U_B(v_B)<0\), then the single shared vector
\(w_f^B=e^{q_{*,f}+v_{B,f}}\) satisfies \(G_B(q_*+v_B)<\Phi\).
If such vectors are supplied for a genuine finite cover of all unwanted strings, they are the required source certificates. The assertion is valid for any branch, including refinements that restrict several spectators.

The program in (22) is a finite convex quadratic program after introducing one epigraph variable at each port. It does not involve the quantum level. A rigorous negative upper evaluation at any candidate vector is sufficient; an optimizer need not be certified. The local version replaces its quadratic term by \(F(r)v^{\mathsf T}L(q_*)v\) under \(\operatorname{osc}v\le r\), by the same subset-Hessian argument and (15).

## 5. Green response and an exact dual of the sufficient program

Let \(\overline L^+\) be the inverse on \(\mathcal H\), extended by zero on constants. Choose at each port probability weights \(\theta_{e,A}\) on its retained comparison atoms, and set
\[
 c(\theta)=\sum_{e,A}\theta_{e,A}c_{e,A},\qquad
 p(\theta)=\sum_{e,A}\theta_{e,A}p_{e,A}.
 \tag{24}
\]
The exact optimal value of the sufficient program is
\[
 \min_{v\in\mathcal H}\mathcal U_B(v)
   =\max_{\theta}
       \left\{c(\theta)
          -\frac12p(\theta)^{\mathsf T}\overline L^+p(\theta)\right\}.
 \tag{25}
\]
This is duality for the explicit quadratic majorant, not an identification with the nonlinear source capacity.

An elementary proof avoids an unverified minimax exchange. For each fixed \(\theta\), minimizing its affine expression plus the quadratic gives the right-hand expression in (25), hence weak duality. The left-hand side has a minimizer because it is strongly convex and coercive on \(\mathcal H\). At a minimizer, zero is in its subgradient. The subgradient of a finite maximum is the convex hull of the gradients of its active affine functions; this follows directly from directional derivatives and finite-dimensional separation. Thus there are active weights \(\theta_*\) with
\[
 \overline L v_*+p(\theta_*)=0.
 \tag{26}
\]
Every atom with positive weight is active, so equality holds in its affine maximum at \(v_*\). Substitution gives equality in (25).

For a balanced load \(p\), the quantity
\(p^{\mathsf T}\overline L^+p\) is the energy of its Green response. For a unit dipole \(p=e_f-e_g\), it is the effective resistance between those faces. The witness therefore responds to the entire shared load, rather than independently rescaling each incidence.

For a simpler explicit test, choose one affine atom at each port that remains maximal in (21) along \(v(t)=-t\overline L^+p\), \(0\le t\le t_0\). This condition is finitely many linear inequalities in \(t\). If their sums at zero are \(c,p\) and \(R=p^{\mathsf T}\overline L^+p\), then
\[
 \mathcal U_B(v(t))=c-tR+\frac{t^2R}{2}.
 \tag{27}
\]
Any admissible \(t\) with \(t(1-t/2)R>c\) certifies the branch. This condition is sufficient only; it does not assume that the nonlinear envelope keeps the same active atom.

One may instead allow changes only on a prescribed proper face set \(W\). Fix \(v=0\) outside \(W\) and use the principal Dirichlet matrix \(\overline L_{WW}\). It is positive definite, and the same proof applies with restricted loads and this inverse. Every occurrence of a changed face is still changed simultaneously. All spectator constants and all edges meeting the patch remain in the program.

## 6. An exact obstruction to a proposed branch certificate

The same atom data yield a lower bound with no Hessian approximation. Every chosen smooth atom cost is convex, so its tangent at \(q_*\) is a global lower bound. Averaging with any \(\theta\) from (24) gives
\[
 G_B(q_*+v)-\Phi\ge c(\theta)+p(\theta)\cdot v.
 \tag{28}
\]
Consequently,
\[
 p(\theta)=0,\quad c(\theta)\ge0
 \quad\Longrightarrow\quad
 G_B(q)\ge\Phi\ \text{for every shared }q.
 \tag{29}
\]
Such a zero-load mixture proves failure of the actual branch test, not merely failure of the quadratic sufficient criterion. The mixture concerns comparison atoms and cannot be treated as a new genuine quantum sector.

Conversely, failure of (22) alone does not establish (29): the coarse Hessian bound may simply be too expensive. A sharper geometric matrix, the exact cut estimate, a different base point, or a smaller genuine branch can improve the sufficient test.

The published seventeen-port source in actual_shared_radius_certificate_separation.md gives a stronger, already rigorous obstruction using triangle allocations not restricted to the complete angles. Its RIGHT anchor has cost above \(\Phi\) by more than \(0.025\) for every shared vector, while forty genuine refinements have strict witnesses. Therefore no proof that all matched spheres pass the unrefined anchored test is possible. Neither that example nor (29) is a counterexample to the full quantum volume limit.

## 7. How the three-witness mechanism generalizes, and where it stops

The all-even proof uses a global compression and then a local repair at either marked boundary. Equation (17) generalizes the first step to any face cut with controlled complete boundary angle mass. Equations (22) and (27), or their local geometric versions, control the second step while retaining the cost at every spectator touched by the repair.

At a noncritical base vector \(q_0\), the same construction remains valid, but the missing linear term must be restored:
\[
 G_B(q_0+v)-\Phi
 \le P(q_0)-\Phi+\nabla P(q_0)\cdot v
       +\frac12v^{\mathsf T}\overline L v+\ell_{B,q_0}(v).
 \tag{30}
\]
The constants and gradients in \(\ell_{B,q_0}\) are those of (20) at \(q_0\). Thus a first cut compression with a proved cost can be followed by a local response. One must not reuse the stationary formula (22) after compression without this gradient.

There is no automatic graph-gluing or cycle-insertion theorem here. Such an operation changes the face-star equations, the complete vector, and possibly the original target incidences. Nor does a finite covering of the geometric manifold give a covering formula for this marked coefficient. The valid object is a finite cover of genuine sector strings on the unchanged diagram.

The new criterion is quantitative and computable from complete angles, but universal negativity for all genuine branches remains unproved. Its precise output is a shared-vector witness or a certified obstruction to the chosen comparison. The all-even family supplies one nontrivial structural instance by additional trigonometric inequalities; those inequalities are not presumed on a general sphere.

## 8. Dependency scope

The source inputs are the complete triangle potential and its gradient, the original complete face stars, and the phase-uniform local CROSS/LEFT/RIGHT bounds. The finite-cover and anchored notes already state how negative shared-vector costs imply a remainder estimate in their specified source classes. The general Morse extension of that transfer is being handled separately, with the original cups, caps, protected variables and full Hermite filling functional retained.

The Hessian, cut-scaling, quadratic certificate, Green dual and obstruction proofs above are finite real-variable arguments. No numerical sampling, literature asymptotic, quantum positivity, or survival of a signed sum is assumed. They produce no new unqualified knot-family theorem by themselves.
