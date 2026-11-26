# When an endpoint current has an original angle-boundary action

Private written proof, 15 November 2026.

The exact grouped endpoint current deletes vertices and decorates the
remaining forest with full Ward coupons. Its deleted-forest action is
not automatically a boundary value of the original constrained angle
problem. There is an explicit necessary and sufficient condition for
the endpoint-pinned boundary realization that preserves the surviving
angle data. When it holds, the action comparison is exact and the
original convex minimum gives a strict gap.

The condition can fail at positive primitive fillings. Its failure
does not prove that the current has a larger action; it identifies
why the proposed boundary-value proof cannot cover all currents.
No quantum contour or scalar asymptotic is inferred from the angle
comparison alone.

## 1. The original polytope and the deleted angle assignment

Let \(G\) be the original finite circle tree, with selected vertices
\(S\), fixed full outside angles \(t_b=s_b+i h_b\), and signed integer
powers \(n_v\). Include every edge incident to \(S\), counted once,
and suppose each selected vertex has positive original degree.
The full primitive equations are assumed to have a positive
solution in the original edge decomposition.

Use the original real angle variables \(s_v=\Re t_v\) and
\(g_{v,e}=\Im r_{v,e}\). The closed angle polytope is given by
\[
 |s_v|+2|g_{w,e}|\leq\pi,\qquad
 |s_w|+2|g_{v,e}|\leq\pi
                         \quad(e=\{v,w\}),
 \tag{1}
\]
\[
 \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v=-\pi
                                      \quad(v\in S).
 \tag{2}
\]
The prescribed outside \(s_b\)'s are unchanged. The original energy is
\[
 \mathcal E_G
   =4\sum_e(E_{P,e}+E_{Q,e})
       -\sum_{b\notin S}h_b\sum_{e\ni b}g_{b,e}.
 \tag{3}
\]
The square coordinates and their energy are those of the pinned convex
variation theorem. In particular, if \(v\) is the first endpoint,
\[
 A_P=s_v/4-g_{w,e}/2,\quad A_Q=s_v/4+g_{w,e}/2,\qquad
 y_P=g_{v,e}/2+s_w/4,\quad y_Q=g_{v,e}/2-s_w/4.
 \tag{4}
\]

Let \(z_0\) be the positive full solution, \(m\) the number of included
edges, and \(M_G\) its calibrated real action. The existing theorems give
\[
 M_G=mM_\infty-\mathcal E_G(z_0)/\pi,\qquad
 \Delta_G=\min_{\partial\mathcal P_G}\mathcal E_G
                                      -\mathcal E_G(z_0)>0.
 \tag{5}
\]
Here \(M_\infty=\psi(0,0)=4G_{\rm Cat}/\pi\), where
\(G_{\rm Cat}=\sum_{j\geq0}(-1)^j/(2j+1)^2\).
The boundary and interior are relative to the original affine
constraint space.

Fix a nonempty removed set \(C\subseteq S\). Delete every edge
incident to \(C\), and let \(r\) be the number of deleted edges.
Retain an angle assignment \(z'\) on the resulting forest that
satisfies its weak edge inequalities and all its surviving
primitive rows, with \(|s_w|\leq\pi\) at every surviving vertex,
including isolated ones. All surviving real angles, incidence variables and
outside data are prescribed by \(z'\). An isolated surviving vertex
must still satisfy its row (2) with an empty incidence sum; it is
not silently removed. If these conditions have no solution, there is
no assignment \(z'\) to which the theorem applies. A degenerate
assignment is given only its angle-energy value (16), not a
geometric or quantum action without further justification.

For a removed vertex let
\[
 d_C(v)=\#\{e=\{v,w\}:w\notin C\},\qquad
 L_v(z')=\sum_{\substack{e=\{v,w\}\\w\notin C}}
                           (1-|s_w|/\pi).
 \tag{6}
\]
All incidences in this sum are counted individually, including those
to prescribed outside vertices.

## 2. Exact feasibility of the endpoint face

The actual current is supported at
\(c_0=2\cos(\pi/N)\) in the original spectral coordinate
\(c=-2\cos t\). Its two real angular endpoints tend to
\(s=\pi\) and \(s=-\pi\). Keep a specified sign
\(\varepsilon_v\in\{-1,1\}\) at each removed vertex.

**Theorem 1.** There is an extension \(\widetilde z\) of \(z'\) to
the original closed polytope, with
\[
                         s_v=\varepsilon_v\pi\quad(v\in C),
 \tag{7}
\]
if and only if
\[
                  |\varepsilon_v n_v-2|\leq L_v(z')
                                             \quad(v\in C).
 \tag{8}
\]
Here an extension retains all surviving coordinates and all original
rows (2). If the endpoint signs may be chosen independently,
the equivalent condition is
\[
 \boxed{\qquad
   \bigl||n_v|-2\bigr|
       +\sum_{\substack{e=\{v,w\}\\w\notin C}}|s_w|/\pi
                       \leq d_C(v)\quad(v\in C).
 \qquad}
 \tag{9}
\]

**Proof.** Equation (1) at a removed endpoint immediately forces
\[
                g_{w,e}=0
                \quad\hbox{whenever }v\in C,\ e=\{v,w\}.
 \tag{10}
\]
Consequently both incidences of an internal \(C\)-edge are zero.
At a surviving vertex every restored incidence is zero, so its old
primitive row remains exactly the deleted-forest row.

At \(v\in C\), the only adjustable incidences are on its edges
to \(w\notin C\). Independently, each has the allowed closed interval
\[
             -\frac{\pi-|s_w|}{2}\leq g_{v,e}
                               \leq\frac{\pi-|s_w|}{2}.
 \tag{11}
\]
Its primitive row requires
\[
                 \sum_{\substack{e\ni v\\e\notin E(C)}}g_{v,e}
                         =\frac\pi2(\varepsilon_v n_v-2).
 \tag{12}
\]
The sum of the intervals (11) is the closed interval with endpoint
magnitudes \(\pi L_v/2\). Thus (12) is possible exactly when (8)
holds. These choices are independent for different removed vertices,
even if they share a surviving neighbor: the opposite incidences
at that neighbor have already been fixed to zero. This proves both
necessity and sufficiency, including equality and \(d_C(v)=0\).

Finally
\(\min_{\varepsilon=\pm1}|\varepsilon n-2|=||n|-2|\).
Since the signs have no further coupling, this proves (9).
\(\square\)

This theorem concerns an angle-boundary value. It does not assert a
matched complex degeneration along which every reconstructed imaginary
angle remains the prescribed one. At corner squares those reconstructions
can depend on the approach. Such a complex path is unnecessary for the
energy comparison below and is not supplied by the theorem.

## 3. The exact boundary energy and the strict action gap

The absolute energy of a removed edge is fixed, not an estimate.

**Lemma 2.** The square energy is constant on its entire boundary,
with value
\[
               E_\square\big|_{\partial[-\pi/4,\pi/4]^2}
                      =G_{\rm Cat}/2=\pi M_\infty/8.
 \tag{13}
\]

**Proof.** On an open vertical side the derivative in the side direction
is the continuous limit
\[
 E_y(A,y)=\tfrac12\operatorname{arsinh}
                       (\tan(2y)\cos(2A))\longrightarrow0.
 \tag{14}
\]
The convergence is uniform on compact subintervals of that side,
so integrating before taking the limit shows that its value is constant.
The same argument works on a horizontal side. The established continuous
extension to the closed square joins their constants at the corners.

At \(y=0\), integrate the other original derivative:
\[
 \begin{split}
 E_\square(\pi/4,0)
 &=\frac12\int_0^{\pi/4}\operatorname{arsinh}(\tan(2A))\,dA\\
 &=\frac14\int_0^{\pi/2}\log(\sec u+\tan u)\,du
   =\frac12\int_{\pi/4}^{\pi/2}\log\tan v\,dv
   =G_{\rm Cat}/2.
 \end{split}
 \tag{15}
\]
The last equality follows by reflection from
\(\int_0^{\pi/4}\log\tan v\,dv=-G_{\rm Cat}\).
For instance, integrate the Abel-regularized sine/cosine logarithm
series and then let its regularization tend to one; the integrated
series is absolutely convergent. The normalization of \(M_\infty\)
in (5) gives the second equality in (13). \(\square\)

Let \(\mathcal E_{G\setminus C}(z')\) denote the sum (3) over
surviving edges, with the same outside term on those edges, and put
\[
           \mathcal M_{G\setminus C}(z')
              =(m-r)M_\infty-\mathcal E_{G\setminus C}(z')/\pi.
 \tag{16}
\]
This definition is an angle-energy value; no stationary or quantum
interpretation is assumed at a general \(z'\).

**Theorem 3.** Whenever (8) holds, every extension constructed in
Theorem 1 satisfies the exact identity
\[
       \mathcal E_G(\widetilde z)
           =\mathcal E_{G\setminus C}(z')+r\pi M_\infty.
 \tag{17}
\]
Consequently
\[
 \boxed{\qquad
           \mathcal M_{G\setminus C}(z')
                    \leq M_G-\Delta_G/\pi<M_G .
 \qquad}
 \tag{18}
\]
If \(z'\) is a positive primitive solution of the deleted forest,
with its original outside data, then (16) is its actual calibrated
classical action. Thus (18) is a strict geometric-action comparison
in that case.

**Proof.** Every deleted edge has at least one removed endpoint.
If that endpoint is first in (4), equations (7) and (10) put both
square \(A\)-coordinates on the boundary. If it is second, both
square \(y\)-coordinates are on the boundary. Lemma 2 therefore gives
\[
                      4(E_{P,e}+E_{Q,e})=\pi M_\infty
 \tag{19}
\]
for each deleted edge, including an edge with two removed endpoints.
Every surviving square is unchanged. Any original outside incidence
on a deleted edge is zero by (10), so the outside linear term in
(3) loses exactly zero. Summing proves (17).

Because \(C\ne\varnothing\) and its vertices have positive original
degree, at least one square of \(\widetilde z\) lies on its boundary.
The full original polytope has an interior positive solution.
Hence \(\widetilde z\in\partial\mathcal P_G\), and (5) gives
\(\mathcal E_G(\widetilde z)\geq\mathcal E_G(z_0)+\Delta_G\).
Combining this with (17) gives (18).
For a positive deleted-forest solution, the pinned action-energy
identity identifies (16) with its actual action, with the unchanged
outside imaginary-angle term. An isolated surviving vertex, if
present, has period equation \(n_vt_v=2\pi\). Thus \(n_v\ne0\),
its \(t_v\) is real and its crossing-plus-charge action is purely
imaginary; it contributes zero to both sides of (16).
This observation does not supply its quantum asymptotic.
\(\square\)

## 4. What this says about the grouped original currents

The actual finite source identity is kept before making a comparison.
For the removed set \(C\), its simultaneous one-step Ward insertions
give exactly
\[
 \mathcal E_{C,N}(\mathbf w)=
     \sum_{\substack{M\subset E(C_{\rm odd})\\M\ {\rm matching}}}
          d_N^{|M|}\prod_{v\in C\setminus V(M)}A_v(\mathbf w),
 \tag{20}
\]
with the original monomers, outside coupons \(T\Pi_0\), and
\(d_N=s_1^2(N^2-1)/3\) from the grouped-current theorem.
All first and mixed normals are included, and shared outside
variables remain shared. Multiplying (20) by the original exterior
and performing its prescribed traces is the exact current.
The removed crossing carriers are the original modulus-one units.
This is the specified simultaneous one-step current. An arbitrary
logarithmic-window translation or other relative-cycle defect is
not identified with (20).

An even zero power makes this particular current identically zero.
Otherwise the matching boundary-unit theorem proves that (20) is
a unit at every full physical boundary assignment for \(N\geq3\),
with polynomially bounded inverse mixed normals. Thus a failure
of the angle-face condition is not explained by algebraic vanishing
of the grouped current.

If a complete contour theorem for the deleted exterior already
justifies the full Ward representatives and its selected nonzero
packet, Section 3 of the grouped-current theorem gives a nonzero
common-phase leading coefficient for (20). Its extra factors are
powers of \(\log N\) and fixed powers of \(N\); its exponential
action is the deleted exterior's action. When that action satisfies
the endpoint-face test, (18) then puts this packet strictly below
the original positive action. A whole-current bound still requires
the stated exterior contour and complement bounds. In particular,
ordinary free-boundary polynomial evaluation is not replaced by a
different Hermite representative without its original trace adapter.

The endpoint-face test is not automatic. It is already impossible
if, for one removed vertex,
\[
                            |n_v|>d_C(v)+2.
 \tag{21}
\]
This failure occurs within the original positive geometry: the
isolated positive-branch theorem recalled in the pinned action note
applies for \(d+|n|>2\), whereas removing that selected vertex with
\(|n|>d+2\) violates (9) for every endpoint sign. This observation
is only a nonvacuity check of the face obstruction, not an action-gap
counterexample or a new knot case.

More generally the actual neighboring real angles enter (9), so even
the degree inequality alone is insufficient. Internal edges of the
removed set provide no capacity in (12): both of their incidences
are forced zero. These are constraints of the original primitive
rows and original endpoint support, not a norm estimate.

Thus one cannot identify every decorated deleted forest with the
endpoint boundary of the original constrained problem and invoke
convexity without a test. Failure of (9) does not disprove a strict
action gap obtained by another argument. Nor does the boundary
identity construct the relative contour, bound other lattice modes,
or establish the desired arbitrary-short-filling volume theorem.

## Direct sources

The complete written proofs below were read; archived numerical
records and computational instructions are not used.

* [Grouped endpoint currents](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_grouped_endpoint_current_matchings.md),
  SHA256 \(\texttt{4047782f665e9e6631e73aac42d55057d6f3cd5ae1e813d89111a0a5caaa21bb}\):
  exact original endpoint support, simultaneous matching polynomial,
  and the stated controlled-exterior leading-coefficient theorem.
* [Original convex filling problem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_filling_convex_variation.md),
  SHA256 \(\texttt{2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0}\):
  square derivatives, original angle inequalities and primitive rows,
  continuous boundary energy and strict interior minimum.
* [Calibrated inverse-period energy](research_positive_period_inverse_descent.md),
  SHA256 \(\texttt{b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565}\):
  action-energy identity with full outside data and the positive
  original boundary gap \(\Delta_G\).
* [Full boundary current unit](research_endpoint_matching_boundary_unit.md),
  SHA256 \(\texttt{ce79146b4a69206ec3daef0f6cd6db73ac2fc99ad88f61499b58b67bdbc6889f}\):
  all-node nonvanishing and the polynomial inverse including mixed
  first normals, with its prescribed-closing limitation.
* [Original isolated action normalization](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_isolated_vertex_action_gap.md),
  SHA256 \(\texttt{106edadc0c02b086af35d594566b086df7cb55d2491418622e30213726bed7d5}\):
  the original value \(M_\infty=4G_{\rm Cat}/\pi\) and the recalled
  positive isolated branch used only to check that (21) is nonvacuous.

Only written mathematics, text reads and file hashes are used.
No mathematical execution, numerical evaluation, tests or compilation
were performed. Other notes and frozen or public files are unchanged.
