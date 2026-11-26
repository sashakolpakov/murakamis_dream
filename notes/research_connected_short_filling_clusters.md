# Joint estimates for connected sets of short fillings

Research proof, 2 November 2026. Several adjacent vertices must be
estimated together: eliminating them as if they were independent
would omit the edge kernels between them. This note retains those
kernels and proves an asymptotic for the entire boundary polynomial
of a connected selected subtree. The sufficient condition depends
on the whole subtree. In particular, its cumulative action loss is
compared with the loss from a single omitted wire index.

All crossing powers and the finite tree are fixed before the quantum
level tends to infinity. The frozen manuscripts are unchanged.

## 1. The complete boundary polynomial

Let \(\mathcal T\) be a finite tree and \(S\) a nonempty connected
proper set of its vertices. Put \(k=|S|\). An edge with both ends
in \(S\) is called internal; an edge with exactly one end in \(S\)
is called boundary. Let \(E_S\) be the union of these two sets,
and write

\[
 m=|E_S|,\qquad b=\#\{\text{boundary edges}\}.
\]

Since \(S\) is connected and the original graph is a tree,
\(m=k-1+b\). A vertex outside \(S\) cannot meet two vertices
of \(S\), since that would produce a cycle. Thus the boundary edges
have distinct outside endpoints, with angles
\(\mathbf u=(u_1,\ldots,u_b)\). Write \(v(j)\in S\) for
the inside endpoint of the \(j\)-th boundary edge.

For \(v\in S\), retain its original degree
\(d_v=\deg_{\mathcal T}(v)\) and fixed integer crossing power
\(n_v\). Let

\[
 K_N(t,u)=\sum_{a=0}^{N-1}e_a(-2\cos t)e_a(-2\cos u),
 \qquad \mathcal D_{n,N}f=\phi_N(R^nf)
\]

be the original complete edge kernel and trace. Define the exact
polynomial of the selected subtree by

\[
 Z_{S,N}(\mathbf u)
 =\left(\prod_{v\in S}\mathcal D_{n_v,N}^{(v)}\right)
   \left[
     \prod_{vw\text{ internal}}K_N(t_v,t_w)
     \prod_{j=1}^bK_N(t_{v(j)},u_j)
   \right].                                               \tag{1}
\]

Every edge in this formula appears once. Every trace is the full
quotient trace with its first normal derivatives. The product before
tracing is kept as a raw polynomial, even when its degree exceeds
\(N-1\) in a selected variable. The resulting polynomial has degree
at most \(N-1\) in each \(-2\cos u_j\).

Use the original holomorphic edge phase \(\psi\), with

\[
 M_\infty=\psi(0,0)=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                    (\tan(t/2)\cos(u/2)).
\]

Let

\[
 \begin{aligned}
 \Psi(\mathbf t,\mathbf u)
   &=\sum_{vw\text{ internal}}\psi(t_v,t_w)
       +\sum_{j=1}^b\psi(t_{v(j)},u_j),\\
 F(\mathbf t,\mathbf u)
   &=\Psi(\mathbf t,\mathbf u)
          +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
          -i\sum_{v\in S}t_v.
 \end{aligned}                                             \tag{2}
\]

All branches begin at the complete edge configuration.

## 2. An explicit criterion and the theorem

Set

\[
 R_v=(d_v^2+n_v^2)^{1/2},\qquad
 \rho=\sum_{v\in S}\frac{d_v}{R_v^2},\qquad a_0=\frac6{25}.
\]

Assume

\[
 \begin{gathered}
 R_v\ge32\quad(v\in S),\qquad \rho\le\frac1{256},\\
 \gamma:=\min_{v\in S}
       \frac{d_v}{32}\left(a_0-\frac7{R_v}\right)^2
                    -64\rho>0.                          \tag{3}
 \end{gathered}
\]

The last inequality is a bound on all mixed horizontal and vertical
faces of the exact trace contour. It is not merely a condition for a
stationary point to exist.

**Theorem.** Under (3), the function \(F(\cdot,\mathbf0)\) has
a unique critical point in the polydisk \(|t_v|\le1/4\), denoted
\(\mathbf t_*\). Every coordinate is nonzero and has negative
imaginary part. On a complex polydisk in the remaining variables it
continues holomorphically to \(\mathbf t_*(\mathbf u)\). Put

\[
 S(\mathbf u)=F(\mathbf t_*(\mathbf u),\mathbf u),\qquad
 M=\Re S(\mathbf0),\qquad
 C_{N,n}=\exp\left(\frac{\pi i n(N-1)^2}{4N}\right).
\]

Then

\[
 Z_{S,N}(\mathbf u)
   =\left(\prod_{v\in S}C_{N,n_v}\right)
       N^{-3(b-1)/2}A(\mathbf u)e^{NS(\mathbf u)}
                         (1+O(N^{-1})),                  \tag{4}
\]

uniformly on a sufficiently small fixed complex polydisk, through
all sufficiently large integer levels. The amplitude \(A\) is
holomorphic and nonzero. The normalized error is holomorphic and has
the same order with fixed derivatives on smaller polydisks.

Moreover, there are positive constants \(c,B,h,C\) and a finite
constant \(A_0\), depending on the fixed selected subtree and its
powers, such that

\[
 |Z_{S,N}(\mathbf x+i\mathbf y)|
 \le CN^{A_0}\exp N\left\{
       M-c\sum_{j=1}^b(1-\cos x_j)+B\sum_{j=1}^b y_j^2
                         \right\}                       \tag{5}
\]

for all \(|x_j|\le\pi\), \(|y_j|\le h\). The boundary phase
is separately even, with

\[
 S_{u_iu_j}(\mathbf0)
   =-\delta_{ij}\frac{\cos(t_{*,v(j)}/2)}{2\pi}.
                                                               \tag{6}
\]

Its real Hessian is negative definite.

**A sufficient degree condition.** For a selected connected subtree
with \(k\) vertices, (3) holds for every assignment of fixed signed
powers, including all zero powers, if

\[
                  d_v\ge256k\qquad(v\in S).              \tag{7}
\]

Indeed \(R_v\ge d_v\), \(\rho\le\sum_vd_v^{-1}\le1/256\),
and \(a_0-7/R_v>1/5\). Hence the minimum in (3) exceeds
\(\min_v d_v/800\ge8k/25\), while \(64\rho\le1/4\).
The resulting gap is at least \(7/100\). This sufficient bound
depends on the number of selected vertices. A degree bound of 128
at each vertex separately does not imply the theorem for arbitrarily
large selected subtrees.

## 3. Uniform estimates for the two-variable edge phase

We first record elementary bounds used throughout the proof. For
\(|t|,|u|\le1/4\), put

\[
 a=\tan(t/2),\qquad c=\cos(u/2),\qquad
 q(t,u)=\frac{2}{t}\operatorname{arsinh}(ac).
\]

The quotient has its removable value at \(t=0\). Since

\[
 q(t,u)=\int_0^1
 \frac{\cos(u/2)\sec^2(st/2)}
      {\sqrt{1+\cos^2(u/2)\tan^2(st/2)}}\,ds,
\]

all its branches are fixed on this polydisk. The elementary estimates
\(|a|<0.128\), \(|c-1|<0.008\), and
\(|\sin(u/2)|<0.126\) imply

\[
 |q-1|<\frac1{25},\qquad
 |q_t|<\frac18,\qquad |q_u|<\frac1{12}.                  \tag{8}
\]

Here are details sufficient to check the constants. The quantity
\(|a^2c^2|\) is less than \(0.017\), so
\(|(1+a^2c^2)^{-1/2}|<1.009\), and its difference from one has
modulus less than \(0.009\). Thus

\[
 \left|\frac{c(1+a^2)}{\sqrt{1+a^2c^2}}-1\right|<0.034.
\]

Its derivative in \(t\) has modulus less than \(0.21\), as
follows by differentiating the displayed quotient and using
\(|(1+a^2c^2)^{-3/2}|<1.027\). Integrating the additional factor
\(s\) gives \(|q_t|<0.105<1/8\). Direct differentiation of
\(q\) in \(u\) gives

\[
 |q_u|\le
 \frac{|\sin(u/2)|\,|\tan(t/2)/t|}
      {|\sqrt{1+a^2c^2}|}
 <0.126(0.512)(1.009)<\frac1{12}.
\]

The edge Hessian satisfies

\[
 \psi_{tt}=-\frac1{2\pi}
        \frac{c(1+a^2)}{\sqrt{1+a^2c^2}},\qquad
 \psi_{tu}=\frac1{2\pi}
        \frac{a\sin(u/2)}{\sqrt{1+a^2c^2}}.              \tag{9}
\]

The difference of this Hessian from \(-(2\pi)^{-1}I\) has
absolute row sums less than \(1/100\): each diagonal difference
is less than \(0.006\), and the off-diagonal entry is less than
\(0.003\). Therefore its real quadratic form is at most
\(-\tfrac18 I\), and its complex operator norm is less than
\(1/5\).

Sum these edge estimates, counting a selected endpoint once for each
incident edge, and write \(D=\operatorname{diag}(d_v)\). On the
whole selected polydisk, at \(\mathbf u=\mathbf0\),

\[
  \Re\Psi_{\mathbf t\mathbf t}\le-\frac18D,
 \qquad
 \|D^{-1/2}\Psi_{\mathbf t\mathbf t}D^{-1/2}\|<\frac15.
                                                               \tag{10}
\]

For the norm estimate one may bound the bilinear form edge by edge
and apply Cauchy–Schwarz to the edge sums; the sum of endpoint
squares is exactly the degree-weighted norm. Boundary edges contribute
only their selected diagonal entry. Thus internal edges are included
with their full mixed derivative, not treated as diagonal factors.

## 4. The coupled stationary equations and cumulative action loss

For a charge vector \(0\le\lambda_v\le1\), replace the final
term of (2) by \(-i\sum_v\lambda_vt_v\). Define

\[
 Q_v(\mathbf t)=\frac1{d_v}
   \left[\sum_{w\in S:\,w\sim v}q(t_v,t_w)
      +\#\{j:v(j)=v\}\,q(t_v,0)\right].
\]

The stationary equations are precisely

\[
 t_v=\frac{-2\pi i\lambda_v}{d_vQ_v(\mathbf t)-in_v}.
                                                               \tag{11}
\]

Equation (8) gives \(|Q_v-1|<1/25\). Its derivative has absolute
row sum less than \(1/8+1/12<1/4\). Thus the denominator in
(11) has modulus at least \(24R_v/25\). The map in (11) sends
the closed selected polydisk into itself, with

\[
 |t_v|\le\frac{7\lambda_v}{R_v},
 \qquad
 \sum_w\left|\frac{\partial t_v^{\rm map}}{\partial t_w}\right|
       <\frac{2d_v}{R_v^2}\le2\rho\le\frac1{128}.
                                                               \tag{12}
\]

It is a contraction, uniformly for the entire charge cube. Every
critical point in the polydisk must satisfy (11), so uniqueness there
is also proved. Taking the imaginary part gives

\[
 -\Im t_v
  =\frac{2\pi\lambda_vd_v\Re Q_v}
        {|d_vQ_v-in_v|^2},\qquad
 0<-\Im t_v\le\frac{8\lambda_vd_v}{R_v^2}
                           \quad(\lambda_v>0).           \tag{13}
\]

At unit charge put \(h_v=-\Im t_{*,v}\). Then
\(h_v\le8\rho\le1/32\), and every rectangle with real
endpoints \(\pm a_0\) and heights \(\pm h_v\) lies strictly
inside \(|t_v|<1/4\). The unit critical point is inside its lower
horizontal side because \(7/R_v\le7/32<a_0\).

Scale all charges by a common \(0\le\lambda\le1\). The real
derivative of the stationary action is
\(\sum_v\Im t_v(\lambda)\). Since the complete value is
\(mM_\infty\), integration of (13) proves

\[
 0<mM_\infty-M\le4\rho\le\frac1{64}<\frac\pi{100}.
                                                               \tag{14}
\]

This is a bound on the total selected action loss. It is the reason
for using \(\rho\), rather than separate degree inequalities at
each vertex. Equation (10) also proves that the full complex Hessian
at the critical point is invertible: its negative has positive
definite real part, since the crossing quadratic contributes only
an imaginary diagonal matrix. Holomorphic continuation in the free
boundary angles follows.

## 5. All omitted wire assignments and outer grid points

Retain \(I=[1/5,3/10]\) in every edge kernel in (1). The
[finite Hermite norm estimates](../papers/circle-tree-volume/finite-bounds.tex)
give rate at most \(2g(a/N)\) to a low wire index, with
\(2g(1/4)=M_\infty\) and \(g''\le-4\pi\). A low index
outside \(I\) loses at least \(\pi/100\); high indices have
only polynomial complete Hermite norm. The original fixed signed
crossing elements, multiplication and every trace have polynomial
cost in that norm. Therefore the complete contribution of wire
assignments with at least one omitted index satisfies

\[
 |\text{omitted wire contribution}|
   \le CN^A e^{N(mM_\infty-\pi/100)},                   \tag{15}
\]

uniformly for all real free boundary angles. There are only
polynomially many assignments for the fixed subtree. Equation (14)
places (15) strictly below the selected action.

For the retained kernels the real-angle estimate in
[the isolated-vertex proof](research_high_degree_short_internal_vertex.md)
gives rate at most \(\psi(a_0,0)\) when at least one angle of
the edge is real and has magnitude at least \(a_0\), while its
other angle is arbitrary and real. Its unrestricted real rate is at
most \(M_\infty\). Thus, if a selected real grid coordinate
\(t_v\) is outside \((-a_0,a_0)\), all its \(d_v\) incident
edges give a total loss at least

\[
 d_v\delta_0,\qquad
 \delta_0=M_\infty-\psi(a_0,0)\ge\frac{a_0^2}{4\pi}.
                                                               \tag{16}
\]

Each incident edge is counted once in this estimate. Other edges have
their unrestricted rate. Mixed normal derivatives needed by the
selected traces have polynomial cost by applying the polynomial Markov
inequality successively on the product of the relevant real spectral
intervals. Fixed crossing chirps have unit modulus at real grid points
and their derivatives also have polynomial cost.

Condition (3) implies
\(d_v a_0^2/32>64\rho\) at every selected vertex. In particular
\(d_v\delta_0>4\rho\). Hence (14) and (16) show that the union
of all these outer grid contributions has a strict gap below \(M\).
This estimates the original finite sum before deforming any contour.

Choose physical midpoint cutoffs
\(a_N=\pi-2\pi m_N/N\ge a_0\), with
\(a_N-a_0=O(N^{-1})\), in all selected coordinates. The estimates
above permit discarding exactly the grid points outside the central
box. For all large levels its contour rectangles still lie in the
edge-expansion polydisk.

## 6. Mixed endpoint faces of the exact trace

Apply the midpoint-cutoff identity in
[the exact rational trace](research_exact_complete_trace_contour.md)
in every selected coordinate, at depth \(h_v\). The resulting
finite expansion has \(2^k\) types of term: each coordinate is
either integrated along its lower horizontal side with kernel

\[
 W_N(t_v)=\frac{e^{-iNt_v}}{(1-\eta e^{-iNt_v})^2},
 \qquad \eta=(-1)^{N-1},
\]

or along an exact vertical endpoint current with kernel
\(1/(4\cosh^2(Ny_v/2))\). The original integrand includes
\(\prod_v\sin t_v\) and all crossing chirps. It is separately
odd in the selected angles, because the edge product and chirps are
separately even. Consequently each upper vertical half can be folded
to the negative lower endpoint without changing the other variables.
After folding, a vertical coordinate has
\(t_v=\pm a_N-iy_v\), \(0\le y_v\le h_v\).

On a horizontal side, \(|W_N(t_v)|\le4e^{-Nh_v}\) for all
sufficiently large levels. On a folded vertical side its kernel is
at most \(e^{-Ny_v}\). Thus every term is bounded, up to polynomial
factors, by the same phase \(\Re F\) evaluated on its mixed face.
This retains all endpoint currents and all Fourier charges.

We now bound these mixed faces directly. Write a point on one of them
as \(\mathbf t_*+\mathbf X+i\mathbf Y\), with real
\(\mathbf X,\mathbf Y\). Here
\(0\le Y_v\le h_v\), and \(Y_v=0\) on horizontal coordinates.
Let \(\mathcal R_\Psi\) be the Taylor remainder after subtracting
the constant and linear terms of \(\Psi\) at \(\mathbf t_*\).
Taylor's formula and (10) give

\[
 \Re\mathcal R_\Psi\le
 -\frac1{16}\|\mathbf X\|_D^2
 +\frac15\|\mathbf X\|_D\|\mathbf Y\|_D
 +\frac1{10}\|\mathbf Y\|_D^2,
\]

The linear terms of the full phase cancel because its gradient
vanishes at \(\mathbf t_*\). The crossing quadratic adds exactly
\(-\sum_v n_vX_vY_v/(2\pi)\) to its quadratic remainder.
Use Young's inequality on the two mixed terms, allocating
\(\|\mathbf X\|_D^2/64\) to each. Since
\(16/25+1/10<1\) and \(4/\pi^2<1\), the result is

\[
 \Re\{F(\mathbf t_*+\mathbf X+i\mathbf Y,0)-S(0)\}
 \le-\frac1{32}\sum_vd_vX_v^2
       +\sum_v\left(d_v+\frac{n_v^2}{d_v}\right)Y_v^2.
                                                               \tag{17}
\]

The straight Taylor segment stays in the same convex polydisk.
Equation (13) bounds the second sum by

\[
 \sum_v\frac{R_v^2}{d_v}h_v^2\le64\rho.                \tag{18}
\]

If at least one coordinate, say \(v\), is vertical, then
\(|X_v|\ge a_0-7/R_v\). Equations (3), (17), and (18)
give a strict gap at least \(\gamma\) below \(M\) on the
entire face. This argument permits arbitrary signs and unrelated
magnitudes of all selected crossing powers. In particular it does
not bound the chirps by a term that grows unchecked with \(|n_v|\).

## 7. The horizontal integral and nonzero leading term

On the all-horizontal box, \(\mathbf Y=0\). The real Hessian of
\(F\) is the real Hessian of \(\Psi\), so (10) gives strict
concavity throughout the box. Its unique maximum is the selected
critical point. On this box the exact edge theorem gives

\[
 \prod_{e\in E_S}K_{N,I}(t_{e,-},t_{e,+})
 =N^{-3m/2}a(\mathbf t,\mathbf u)
      e^{N\Psi(\mathbf t,\mathbf u)}(1+O(N^{-1})),
\]

where \(a\) is the product of the original nonzero edge amplitudes.
For a boundary edge its second argument is the corresponding \(u_j\).
The exact edge expansion already includes all its wire-lattice
corrections.

Each horizontal rational kernel is
\(e^{-iNt_v}(1+O(e^{-Nh_v}))\). Replacing their denominators
by one changes the integral by a term with rate at most
\(M-\min_vh_v\). Thus all higher Fourier charges are controlled
on the same contour as the unit charge. The unit-charge coefficient
is one. Uniform multivariate Gaussian expansion gives the nonzero
coefficient

\[
 A(\mathbf u)
 =\left(-\frac1{\pi i}\right)^k(2\pi)^{k/2}
   \frac{a(\mathbf t_*(\mathbf u),\mathbf u)
                     \prod_{v\in S}\sin t_{*,v}(\mathbf u)}
        {\sqrt{\det[-F_{\mathbf t\mathbf t}
                          (\mathbf t_*(\mathbf u),\mathbf u)]}}.
                                                               \tag{19}
\]

The square root is the accretive Gaussian branch. The edge amplitudes
are nonzero; the sines are nonzero by (11)–(13); and the Hessian is
invertible by (10). Every exterior gap above persists on a sufficiently
small complex polydisk in \(\mathbf u\), where the selected saddle
and the local integration cycle continue holomorphically. This proves
the uniform holomorphic expansion.

The exponent of \(N\) is

\[
 -\frac{3m}{2}+2k-\frac k2
       =\frac32(k-m)=-\frac32(b-1),
\]

which proves (4) with its original crossing scalars. Nothing in the
argument restricts the parity or arithmetic nature of the level.

## 8. The entire remaining boundary

For real \(|u_j|\le\pi\), apply the
[weighted edge bound](research_weighted_edge_contour_bound.md)
on each boundary edge. It inserts
\(-(1-\cos u_j)/20\) in the exponent on every central contour
piece. The internal edges still use their full complex edge expansion.
Thus the central estimates above retain the sum of these boundary
losses. The discarded wire and outer-grid terms have fixed strict
gaps below \(M\), uniformly on the real boundary torus. Decrease
the angular constant so that these gaps also dominate
\(c\sum_j(1-\cos u_j)\); the sum is bounded by \(2b\).
This proves (5) for real boundary angles.

At \(\mathbf u=0\), each mixed derivative
\(\Psi_{t_vu_j}\) vanishes by separate evenness. Differentiating
the critical equations therefore gives
\(\partial\mathbf t_*/\partial u_j=0\). The Hessian of its
stationary action is consequently the explicit boundary Hessian of
\(\Psi\), which is (6). Its real part is strictly negative since
\(|t_{*,v}|<1/4\).

Near zero, Taylor's theorem and this Hessian give a quadratic complex
strip bound for \(\Re S\), with the mixed real-imaginary terms
absorbed by Young's inequality. Away from a small neighborhood of zero,
the real angular bound has a fixed gap. The polynomial
Bernstein–Walsh estimate, applied in the boundary spectral variables
on a finite cover by products of real intervals, preserves half that
gap on a sufficiently thin fixed complex neighborhood. The separate
degrees are at most \(N-1\). Combining the local quadratic bound
and this exterior estimate proves (5) on the whole stated strip.

## 9. Scope and the remaining partial-filling problem

The polynomial in (1) contains all shared edges of the connected
selected subtree. The theorem therefore provides an analytic closure
result for adjacent selected vertices, rather than a product of
isolated-vertex results. Condition (7) permits every fixed short-power
assignment on such a subtree, with all neighboring angles left free.
The full amplitude and the boundary Hessian in (6) are the analytic
inputs required for a subsequent long-filling argument.

The volume interpretation additionally requires the original positive
geometric deformation, its full primitive logarithmic periods, and
an absolute volume anchor. Those geometric assertions are not inferred
here from the scalar stationary equations. The present theorem is an
estimate of the original quantum polynomial.

The cumulative condition (3) is sufficient, not necessary. It still
fails for many low-degree short-filled subtrees. In particular, the
proof compares all omitted-wire terms with the complete action minus
a single fixed gap. To remove the dependence on cumulative action loss,
one would need a stronger estimate on omitted-edge sectors that retains
the stationary contributions from the rest of the selected subtree.
No such estimate is assumed in this proof. Arbitrary fixed short
partial fillings, and hence the finite-exception theorem, remain open.

## 10. A volume theorem after further long fillings

The [positive cluster geometry](research_connected_short_filling_geometry.md)
supplies the geometric input for the degree range (7). There is also
a different construction for components whose powers are all zero:
the [primitive Newton estimate](research_all_zero_subtree_newton_packet.md)
and the [literal strict Conway geometry](research_zero_subtree_conway_geometry.md)
apply whenever their original degrees are at least three, with no
bound on component size. The
[adjacent two-crossing boundary theorem](research_adjacent_two_crossing_boundary_theorem.md)
also supplies a component consisting of a terminal vertex and its
degree-two neighbor, both of crossing power two.
We record the resulting theorem for the original Kashaev invariant,
allowing these components together and shared remaining boundary
variables.

Use a fixed ordered circle-tree knot template with at least one edge
and with the original stacks, quarter-turns, disk framings,
orientations, closure and reduced cut. As in
[the nonadjacent-filling theorem](research_nonadjacent_short_fillings_and_long_remainder.md),
retain the original carriers and integer coefficients
\(n_v=\eta_v-2p_v\), \(\eta_v\in\{-1,0,1\}\). Fix the
parity pattern whose original strand tracing produces one main
component and no internal closed component. There are no unrecorded
product junctions.

Choose any proper subset \(S\) of the original vertices and fix
its crossing powers, with their original parities. Let \(\mathcal C\)
be the connected components of its induced subgraph. Require the
following at each component \(C\):

- For a singleton \(C=\{s\}\), allow every \(|n_s|\ge2\)
  if \(d_s=1\); allow \(|n_s|=2\) if \(d_s=2\); and allow
  \(n_s=0\) if \(d_s\ge3\). Any internal pair satisfying
  \(d_s^2+n_s^2\ge\max\{1024,128d_s\}\) is also allowed
  by the degree-and-power theorem.
- For \(|C|\ge2\), require \(d_v\ge256|C|\) for every
  \(v\in C\). Every fixed signed power is then allowed, including
  zero. More generally one may use criterion (3) for that component
  together with \(R_v\ge448\) at all its vertices; this is precisely
  the additional range covered by the positive cluster geometry.
- As an alternative, allow any component with \(n_v=0\) and
  original degree \(d_v\ge3\) at every vertex. Its vertices may
  be adjacent and its size is unrestricted. This alternative uses
  the strict Conway cells, including when the former imaginary-angle
  edge coordinates reach an endpoint.
- Also allow a component consisting of exactly two adjacent vertices
  \(s,t\), with original degrees \(d_s=1\), \(d_t=2\), and
  \(n_s=n_t=2\). Its only other incident edge joins \(t\) to
  a remaining vertex. These are pendant paths of two selected
  vertices. Any finite number of them is allowed, including several
  attached to the same remaining vertex. Their original carriers
  are zero and their integer filling coefficients are both \(-1\).

Let \(V_0=V\setminus S\), \(r=|V_0|\ge1\), and let \(E_0\)
be the edges with both endpoints in \(V_0\).

**Theorem.** There is a finite threshold \(B\), depending on the
fixed marked tree, the selected set and its fixed powers, such that
every choice of remaining powers

\[
 n_v\equiv\eta_v\pmod2,\qquad |n_v|\ge B
                         \quad(v\in V_0)
\]

produces a hyperbolic knot \(K\) and has

\[
 \langle K\rangle_N
   =\Omega_NN^{3/2}D e^{N\mathcal A}(1+O_{\mathbf n}(N^{-1})),
 \qquad |\Omega_N|=1,\qquad D\ne0,
\]

\[
       2\pi\Re\mathcal A=\operatorname{Vol}(S^3\setminus K).
                                                               \tag{20}
\]

The statement holds through all sufficiently large integer levels.
The remaining signs and magnitudes are independent. There is no
claim that \(B\) is uniform over different choices of the already
fixed powers.

**Proof.** Let \(k_C=|C|\) and let \(m_C\) be the number of
original edges with at least one endpoint in \(C\). Each component
has its complete boundary polynomial \(Z_{C,N}\), geometric phase
\(G_C\), and nonzero local amplitude. For a component all of whose
powers are zero and degrees at least three, use the full primitive
Newton theorem and its strict Conway interpretation; its phase is
\(G_C=W_C\). For a pendant component of degrees \((1,2)\)
and powers \((2,2)\), use the adjacent boundary theorem:
its exact source is the successive pair of original traces,
its geometric phase is the full germ \(G_C\) with
\(S_C=G_C+i\pi\), and its local power of \(N\) is zero.
Here \(k_C=m_C=2\), so this agrees with (21) below.
For the remaining nontrivial components, use (1), (4), and
(19), with the positive geometric identification just cited.
Singleton components use their proved complete boundary
theorems, including the
[degree-two phase comparison](research_degree_two_power_two_geometric_phase.md)
and the
[zero-power theorem](research_zero_power_internal_boundary_theorem.md).
In every case the local expansion has the form

\[
 Z_{C,N}=\varepsilon_{C,N}N^{-3(m_C-k_C)/2}
          a_C e^{NG_C}(1+O(N^{-1})),\qquad
 |\varepsilon_{C,N}|=1.                                  \tag{21}
\]

For a zero-power component, \(\varepsilon_{C,N}=1\). Its number
of boundary edges is \(b_C=m_C-k_C+1\), so the power
\(-3(b_C-1)/2\) in its Newton expansion is exactly the power in
(21). For every other nontrivial component,
\(\varepsilon_{C,N}=\prod_{v\in C}C_{N,n_v}\), except for a
pendant \((2,2)\) component, whose exact phase comparison gives
\(\varepsilon_{C,N}=(-1)^N\). The same product formula
holds for a singleton except when it has degree one or two
and \(n_s=2\sigma\), \(\sigma=\pm1\). In those cases
the precise source-to-geometric phase difference gives
\(\varepsilon_{C,N}=e^{\sigma i\pi N/2}\). In degree one the
amplitude is \(e^{-\sigma i\pi/4}/(2\sqrt{\cos(u/2)})\).
In degree two it is the nonzero two-boundary amplitude in equation
(18) of the phase-comparison note. A zero-power singleton uses
\(C_{N,0}=1\) and the unshifted geometric action.
No boundary-dependent phase is discarded.

Different components have no edge between them, though they may share
a free boundary vertex. Taking their original finite traces leaves
exactly

\[
 B_N(\mathbf u)
   =\prod_{vw\in E_0}K_N(u_v,u_w)
          \prod_{C\in\mathcal C}Z_{C,N}(\mathbf u_{\partial C}),
                                                               \tag{22}
\]

followed by the original traces at all vertices in \(V_0\). Every
edge is counted once. The local phase of (22) is

\[
 P(\mathbf u)=\sum_{vw\in E_0}\psi(u_v,u_w)
                    +\sum_{C\in\mathcal C}G_C(\mathbf u_{\partial C}).
                                                               \tag{23}
\]

All factors are separately even and have nonzero local amplitudes.
Their full Gaussian strip bounds multiply. At a shared free variable
the positive angular losses add, as do the negative real diagonal
Hessian entries. If \(s(C,v)\) is the unique vertex of \(C\)
adjacent to a free vertex \(v\), define the positive real number

\[
 \gamma_{C,v}=
 \begin{cases}
 \tan(\pi a^*_{C,v}),&\text{for a zero-power component},\\
 \sqrt7/4,&\text{for a pendant \((2,2)\) component},\\
 \Re\cos(t_{*,s(C,v)}/2),&\text{for the other components}.
 \end{cases}
\]

Here \(a^*_{C,v}\in(0,1/2)\) is the boundary leaf coordinate
at the strict Newton maximum of the zero-power component, and
\(t_*\) is the geometric stationary angle in the other boundary
theorems. The pendant component has
\(G_C''(0)=-(\sqrt7+3i)/(8\pi)\), so its contribution to
\(-\Re P_{vv}(0)\) is \(\sqrt7/(8\pi)\).
Their respective Hessian formulas give

\[
 -\Re P_{vv}(0)=\frac1{2\pi}\left[
   \deg_{E_0}(v)+\sum_{C:\,v\in\partial C}
       \gamma_{C,v}\right]>0,
 \qquad P_{vw}(0)=0\quad(v\ne w).                       \tag{24}
\]

Each remaining vertex has an incident original edge, so at least one
positive term occurs. The uniqueness of \(s(C,v)\) follows from
the tree property; no uniqueness is required across different
components. Thus (22) satisfies all hypotheses of the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).

Its initial power of \(N\) is

\[
 \alpha=-\frac32\left[|E_0|+\sum_C(m_C-k_C)\right]
        =-\frac32(|E|-|S|)=-\frac32(r-1).
                                                               \tag{25}
\]

The remaining \(r\) traces add \(3r/2\), proving the final
power \(3/2\). The long-filling theorem gives a nonzero coefficient
and the action

\[
 \mathcal A=\operatorname{stat}_{\mathbf u}
  \left[P(\mathbf u)+\frac{i}{4\pi}\sum_{v\in V_0}n_vu_v^2
                                      -i\sum_{v\in V_0}u_v\right].
                                                               \tag{26}
\]

With \(w(D)\) the writhe of the original diagram, its exact unit
scalar is

\[
 \Omega_N=q^{(N-1)^2w(D)/2}
       \prod_C\varepsilon_{C,N}\prod_{v\in V_0}C_{N,n_v}.
                                                               \tag{27}
\]

This retains the original zero-framing correction.

For completeness, the volume calibration uses the actual geometric
construction of each component. For a zero-power component, delete
its through boxes in the original ordered tangle. Section 1 of the
strict Conway interpretation proves that this is meridian filling
on exactly those original circles. The remaining disk seams and
peripheral curves are retained. The strict Conway metric gives the
resulting piece volume \(2\pi W_C(0)\), and Sections 4--5 of
that note identify its entire boundary maps and primitive periods.
This construction does not require a positive continuation of an
edge chart through a degenerate tetrahedron.

For the other components, keep all free angles zero and perform
their proved cone paths. A pendant \((2,2)\) component uses
the original two-stage cone deformation in the
[adjacent-pair geometry](research_adjacent_two_crossing_pair.md):
first fill the terminal circle, then fill its degree-two neighbor
while keeping the first filling smooth. That construction retains
all original tetrahedra, face maps and primitive curves, and its
phase comparison is an identity of the entire boundary germ.
The remaining nontrivial components use the positive chart on
every incident edge, including edges between selected vertices;
singleton components use the isolated cone geometry.
Their selected primitive slopes finish with cone angle \(2\pi\).

Different components have disjoint incident-edge sets. Their full
marked face maps match at shared free vertices: at angle zero these
are the same original twice-punctured disk interfaces. Thus their
pieces and the untouched edge pieces give the original partially
filled exterior \(Y'\). The free peripheral derivatives vanish,
so every unfilled auxiliary cusp and every main cusp is complete.
It has

\[
 \operatorname{Vol}(Y')
   =2|E_0|v_{\rm oct}+2\pi\sum_C\Re G_C(0)
   =2\pi\Re P(0).                                      \tag{28}
\]

Each component identity includes its absolute constant. Zero-power
components use the complete strict Conway volume theorem. The other
components start with \(2m_C\) original regular ideal octahedra
and integrate Schläfli's formula along their primitive cone paths.
Thus (28) is an equality of absolute volumes.

The positive cells and their entire marked maps continue for small
free angles. For zero-power components the exact classical Legendre
identity gives their remaining periods. For the other components,
the selected angles continue with their primitive equations kept at
unit charge, and differentiating through them contributes zero to
the stationary action. At a shared free circle the meridian
increments add in the original cyclic order. Its carrier correction
occurs once at its original disk seam, regardless of the number of
incident components. Hence the remaining original periods are exactly

\[
 U_v=-2\pi P_v-i\eta_vu_v,\qquad V_v=2iu_v,
 \qquad U_v+p_vV_v
     =-2\pi\left(P_v+\frac{in_v}{2\pi}u_v\right).        \tag{29}
\]

Solve the small remaining cone path
\(P_v+in_vu_v/(2\pi)=ic\), \(0\le c\le1\), using the
uniform contraction in the long-filling theorem. Increasing \(B\)
keeps the entire path in the positive neighborhood. Its coordinates
have negative imaginary part for \(c>0\), so (29) gives the original
primitive cone angles \(2\pi c\) and positive lengths
\(-2\Im u_v\). The already selected angles remain smooth fillings.
At \(c=1\), the original solid-torus completion gives the complete
hyperbolic metric on the specified knot complement.

The real derivative of the stationary action along this second path
is \(\sum_v\Im u_v\). Schläfli's formula gives \(2\pi\) times
the same derivative for its actual volume. The initial equality is
(28), so integration proves the second equality in (20). Combined
with the nonzero leading coefficient, this proves the theorem.

The analytic criterion (3) without the additional positive-chart
condition \(R_v\ge448\) is not used to claim a volume theorem for
nonzero nontrivial components. Connected low-degree components with
nonzero powers outside the stated pendant \((2,2)\) case and the
other sufficient conditions remain outside the result. All-zero
components with every original degree at least three are included
by the separate strict Conway proof.
The full finite-exception goal is unchanged.
