# Uniform convergence to the homogeneous geometry inside a three-crossing path

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The earlier energy comparison showed that some internal edge of a
long homogeneous three-crossing path approaches the homogeneous
positive geometry. In fact every edge sufficiently far from the two
ends does so, uniformly in the path length. This follows from
convexity and finite excess energy, without a numerical packing
calculation or a hypothesis about the quantum sum.

## 1. Statement and coordinates

Take a path with selected vertices \(1,\ldots,m\), all of power
three and charge one, and complete outside vertices \(0,m+1\).
Its unique positive solution is supplied by
[the path existence theorem](research_positive_path_fractional_charge_cube.md).
Use the real angle and return coordinates
\[
 a_v=\Re t_v,\qquad
 g_{v,-}=\Im r_{v,\{v-1,v\}},\qquad
 g_{v,+}=\Im r_{v,\{v,v+1\}}.
 \tag{1}
\]
The exact vertex constraint is
\[
              g_{v,-}+g_{v,+}-\frac32a_v=-\pi.
 \tag{2}
\]
Thus a selected vertex has the two independent real coordinates
\[
 b_v=\frac{g_{v,+}-g_{v,-}}2,\qquad
 g_{v,\pm}=\frac34a_v-\frac\pi2\pm b_v.
 \tag{3}
\]
At each outside vertex \(t=0\) and its return is zero.

Let \(t_*=a_*-iH_*\) be the homogeneous point from
[the exact positive-point calculation](research_bare_kernel_power_three_obstruction.md):
\[
 \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\qquad
 g_*=\frac{3a_*-2\pi}{4},\qquad
                    (a_v,b_v)=(a_*,0).
 \tag{4}
\]
For an oriented edge \(e=\{v,v+1\}\), its four square coordinates are
\[
 X_e=\left(
 \frac{a_v}4-\frac{g_{v+1,-}}2,\
 \frac{g_{v,+}}2+\frac{a_{v+1}}4,\
 \frac{a_v}4+\frac{g_{v+1,-}}2,\
 \frac{g_{v,+}}2-\frac{a_{v+1}}4
 \right).
 \tag{5}
\]
These are \((A_P,y_P,A_Q,y_Q)\) of the original convex
variation. Write \(X_*\) for (5) at the homogeneous point.
All its coordinates lie strictly between \(-\pi/4\) and \(\pi/4\).

**Theorem 1.** For every \(\delta>0\), there is an integer
\(R_\delta\), independent of \(m\), such that every internal edge
\(e_j=\{j,j+1\}\) with
\[
                   \min(j,m-j)\ge R_\delta
 \tag{6}
\]
satisfies \(\|X_{e_j}-X_*\|<\delta\).
In particular the two complex geometric angles at that edge
converge uniformly to \(t_*\) as their distance from the ends
tends to infinity.

No explicit numerical value of \(R_\delta\) is supplied.
Section 5 strengthens this convergence to exponential decay with
constants independent of path length. The results concern the actual
finite paths; an infinite path is used only in the contradiction
argument.

## 2. Nonnegative excess energy

Let \(E(A,y)\) be the original strictly convex square energy and put
\[
 \begin{split}
 \mathscr E_e(X)&=4\{E(A_P,y_P)+E(A_Q,y_Q)\},\\
 B_e(X)&=\mathscr E_e(X)-\mathscr E_e(X_*)
                    -d\mathscr E_e(X_*)(X-X_*).
 \end{split}
 \tag{7}
\]
The letter \(B_e\) denotes the excess above the tangent plane at
the homogeneous point. It is not a boundary matrix.
The [quantitative convexity estimate](research_positive_edge_volume_identity.md),
equation (39), gives a constant \(\kappa>0\), depending only on
the fixed interior reference, such that on the whole closed
square domain
\[
                      B_e(X)\ge\kappa\|X-X_*\|^2.
 \tag{8}
\]
In particular \(B_e\) is continuous and nonnegative there.
Near \(X_*\) it is smooth and has value and first derivative zero.

At the homogeneous point the return has real part \(3H_*/4\).
The differential of the total edge energy therefore contributes,
at a selected vertex,
\[
 \frac{3H_*}{2}\,\Delta a_v
                 -H_*(\Delta g_{v,-}+\Delta g_{v,+})=0
 \tag{9}
\]
for every variation preserving (2). Thus the homogeneous tangent
terms cancel exactly for every finitely supported variation of
the selected vertices.

Use the strictly feasible trial from
[the finite-path comparison](research_bare_kernel_power_three_obstruction.md),
Section 4: keep every selected vertex homogeneous and set both
outside vertices and their returns to zero. All internal edges
then have zero \(B_e\); the two attaching edges have fixed
strictly interior square coordinates. The actual minimizer and this trial
have the same outside angles and returns, so their total tangent
terms in (7) agree, by (9). Minimality gives a constant \(C\)
independent of \(m\) with
\[
                     \sum_{e}B_e(X_e)\le C.
 \tag{10}
\]
One can take \(C\) to be the sum of the two trial attaching-edge
excesses. This is the existing bounded-energy comparison in a
nonnegative form.

The inverse linear relations in (5), together with (3), imply
from (8)--(10) that
\[
 \sum_{v=1}^{m}\bigl((a_v-a_*)^2+b_v^2\bigr)\le C_1
 \tag{11}
\]
for another constant independent of \(m\). Each vertex is incident
to only two edges, so the bounded multiplicity in this linear
estimate is independent of path length.

## 3. There is no nonconstant finite-energy interior limit

Suppose Theorem 1 is false. There are paths and internal edges
whose distances from both ends tend to infinity, while their
deviations from \(X_*\) are at least a fixed positive number.
Translate each such edge to \(\{0,1\}\).
The real angle domain is bounded. A diagonal subsequence
therefore converges at every fixed vertex and edge to a
configuration indexed by all integers. It obeys (2), the closed
square inequalities and (5).

By (10)--(11) and nonnegativity, this limit satisfies
\[
 \sum_{j\in\mathbb Z}B_{e_j}(X_{e_j})\le C,\qquad
 \sum_{j\in\mathbb Z}\bigl((a_j-a_*)^2+b_j^2\bigr)\le C_1.
 \tag{12}
\]
Consequently \((a_j,b_j)\to(a_*,0)\) as \(j\to\pm\infty\).
The central edge still has a nonzero deviation.

For a large integer \(R\), replace the vertices
\(-R,\ldots,R\) of this limit by their homogeneous values.
All constraints (2) remain exact. The internal replacement
edges are the strictly positive homogeneous edges. The two
joining edges are also strictly positive for large \(R\),
because their unchanged outside vertices tend to the same
homogeneous values. The identical replacement is therefore
feasible in each sufficiently far member of the finite-path
subsequence.

Compare the original finite minimizer with that competitor.
Only the edges \(e_{-R-1},\ldots,e_R\) change. The tangent
terms cancel by (9). Passing to the limit, using continuity
of the closed-square energy, gives
\[
 \sum_{j=-R-1}^{R}B_{e_j}(X_{e_j})
 \le B\bigl((a_{-R-1},b_{-R-1}),(a_*,0)\bigr)
       +B\bigl((a_*,0),(a_{R+1},b_{R+1})\bigr).
 \tag{13}
\]
Here \(B(y,z)\) means (7) on the oriented edge determined by
the two vertex states via (3)--(5).
The two right-hand terms tend to zero: near the homogeneous
pair, their value is bounded by a fixed constant times the
squared deviation of the unchanged endpoint. The left side
is a sum of nonnegative terms and includes the fixed central
edge. Letting \(R\) tend to infinity proves
\(B_{e_0}(X_{e_0})=0\), and (8) forces \(X_{e_0}=X_*\).
This contradicts the choice of the subsequence.

This proves the uniform statement (6). The inverse square map
and its gradients recover the complex angles and returns
smoothly near the fixed interior reference, proving the last
assertion of Theorem 1. \(\square\)

## 4. Relation to the local Fourier calculation

For a pair of complex angles near \((t_*,t_*)\), define the
local edge coordinate \(x(t,u)\) by
\[
 \cos(2\pi x)=
       \frac{1-\cos t\cos u}{2+\cos t+\cos u},\qquad
 x(t_*,t_*)=x_*:=\frac16+\frac{i\log2}{2\pi}.
 \tag{14}
\]
The denominator and \(\sin(2\pi x_*)\) are nonzero, so this
specifies a holomorphic function locally. The value at the
reference follows from
\(\cos(2\pi x_*)=5/8-3\sqrt3\,i/8=(1-\cos t_*)/2\).
Equation (14) is the original edge stationary equation:
writing \(c=\cos(2\pi x)\), the product of its two consecutive
Newton-factor ratios equals one precisely when
\[
              (c+\cos t)(c+\cos u)=(1-c)^2.
 \tag{15}
\]
Expanding (15) gives (14).

Thus every fixed neighborhood of the homogeneous wire
coordinates contains all edge coordinates sufficiently far
from the two ends. In particular a fixed local chart such as
the one in [the retained-vertex theorem](research_traced_three_vertex_endpoint.md)
does not miss geometric vertices arbitrarily deep inside a
homogeneous three-crossing path.

This is a geometric localization theorem. It does not estimate
the quantum integral outside that chart, or prove a nonzero
boundary contribution. The full open-chain source still needs
those analytic estimates.

## 5. Exponential decay of the influence of the ends

Once all sufficiently deep vertices lie in a fixed compact interior
neighborhood, the local Hessian is uniformly elliptic. Its finite
range then gives a stronger conclusion.

Exponential decay of inverses of band matrices is classical; see
Demko, Moss and Smith,
[“Decay rates for inverses of band matrices”](https://doi.org/10.1090/S0025-5718-1984-0758197-9),
*Mathematics of Computation* **43** (1984), 491--499.
The estimate needed here is proved directly in (21), with constants
coming from the original filling energy.

**Corollary 2.** There are constants \(C>0\) and \(0<q<1\),
independent of \(m\), such that the actual selected states satisfy
\[
 |a_v-a_*|+|b_v|
       \le C q^{\min(v,m+1-v)}\qquad(1\le v\le m).
 \tag{16}
\]
The same conclusion, with a different \(C\), holds for
\(|t_v-t_*|\). On sufficiently deep edges it also holds for
the local wire coordinate in (14).

*Proof.* Write \(y_v=(a_v-a_*,b_v)\). On any edge between
selected vertices, (3)--(5) give
\[
 X_{\{v,v+1\}}-X_*
   =K\binom{y_v}{y_{v+1}},\qquad
 K=\begin{pmatrix}
 1/4&0&-3/8&1/2\\
 3/8&1/2&1/4&0\\
 1/4&0&3/8&-1/2\\
 3/8&1/2&-1/4&0
 \end{pmatrix}.
 \tag{17}
\]
The two eigenvalues of \(K^TK\), each of multiplicity two, are
\((29\pm3\sqrt{65})/64\). In particular
\[
                    \frac1{16}I_4<K^TK<\frac78 I_4.
 \tag{18}
\]
Choose a small convex neighborhood of the homogeneous square
coordinates, whose closure is strictly interior. There are fixed
numbers \(\ell,u>0\) with
\(\ell I_2\preceq E''\preceq uI_2\) on it.
Theorem 1 and the linear inverse of (17) put all sufficiently
deep vertices and their neighboring edges in this neighborhood.
The segment from their states to the homogeneous states stays
there as well.

Choose an interval \(I=\{r,\ldots,m+1-r\}\) of such vertices,
with its two neighboring vertices also in that neighborhood.
The choice of \(r\) is independent of \(m\). The energy is a sum
over neighboring pairs. Both its actual gradient and its homogeneous
gradient vanish at every vertex in \(I\), because (3) has already
eliminated each filling constraint. Integrating the Hessian along
the straight segment between these two states gives
\[
                  A_{II}y_I=-A_{I,\partial I}y_{\partial I},
 \tag{19}
\]
where \(\partial I=\{r-1,m+2-r\}\).
The matrix \(A_{II}\) is real symmetric and block tridiagonal,
with two coordinates per vertex.

Each vertex of \(I\) is incident to two of the included edges.
Equations (17)--(18), the factor four in the edge energy,
and the bounds for \(E''\) therefore give
\[
             \lambda I\preceq A_{II}\preceq\Lambda I,
               \qquad \lambda=\ell/2,\quad\Lambda=7u.
 \tag{20}
\]
The same local estimates bound each nonzero boundary coupling
block by \(\Lambda\). No bound grows with the number of vertices.

Here the decay of the inverse has an elementary proof. Put
\(R=I-A_{II}/\Lambda\). It has block bandwidth one and
\(\|R\|_2\le q:=1-\lambda/\Lambda<1\). Hence
\[
 A_{II}^{-1}=\frac1\Lambda\sum_{k=0}^{\infty}R^k,
 \qquad
 \|(A_{II}^{-1})_{vw}\|
       \le\frac{q^{|v-w|}}{\lambda}.
 \tag{21}
\]
The block in \(R^k\) vanishes when \(k<|v-w|\); summing the
remaining geometric series proves the bound. The right side of
(19) is supported only at the first and last vertices of \(I\).
The boundary states are bounded independently of \(m\).
Consequently (19)--(21) give a fixed constant \(C_0\) with
\[
 \|y_v\|\le C_0\{q^{v-r}+q^{m+1-r-v}\}\qquad(v\in I).
 \tag{22}
\]
Increasing the constant absorbs the fixed \(r\) and covers every
vertex outside \(I\), using boundedness of the closed angle domain.
It also covers paths too short to contain this interval. This proves
(16), with \(q=1-\ell/(14u)\).

On the compact interior neighborhood, the inverse square map and
the edge-energy gradients are Lipschitz, as is (14). They give
the asserted decay of the complex angles and local wire coordinates
at deep vertices and edges. The global bounds
\(0<a_v<\pi\), \(0<H_v<23/20\) enlarge the angle constant to
cover the finitely many distances omitted near the ends.
\(\square\)

This is a quantitative propagation estimate for the geometric
equations. It does not propagate a lower bound for a quantum
coefficient: that would additionally require the actual boundary
state and control of the rest of the finite integral.

## 6. Reproduction

Run `python3 experiments/check_three_path_interior_localization.py`.
The [saved calculation](../repro/results/research-three-path-interior-localization.json)
verifies the constrained edge map, its exact Gram bounds, the tangent
cancellation, and the incidence factors in (20). The compactness
argument, the length-independent interior neighborhood, and the
inverse-matrix estimate are proved in the text. These finite
calculations do not test or imply a quantum lower bound.
