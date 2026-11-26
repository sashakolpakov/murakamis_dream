# Full microscopic endpoint products on marked reducible forests

Private written proof, 16 November 2026.

A closed forest has a polynomial source bound with arbitrary fixed
microscopic endpoint products if it has a leaf-reduction order that
never turns a decorated leaf. The decorations remain at their original
vertices until an isolated trace or an exact zero-leaf evaluation
consumes them. This preserves the entire endpoint product, including
all its first normals.

For an original microscopic current whose surviving forest has this
marked reduction order, the whole current has polynomial growth.
No top Newton band is selected. This is an actual source estimate
under a finite combinatorial hypothesis, not a bound for arbitrary
decorated forests or arbitrary short fillings.

## 1. The original decorated source and its certificate

Use
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad q=e^{\pi i/N},
 \quad \kappa=q^{D^2/2},\quad
 c_a=2\cos((2a+1)\pi/N),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 e_k(Z)=S_k^{-2}\prod_{a<k}(c_a-Z),\qquad
 S_k=\prod_{a=1}^k2\sin(a\pi/N),\quad S_0=1,
\]
\[
 K_N(Z,w)=\sum_{k=0}^{D}e_k(Z)e_k(w),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad Te_j=e_{D-j}.
 \tag{1}
\]
The original signed crossing powers \(R^n\), including their carriers
and first normals, are used throughout.

Let \(F=(V,E)\) be a fixed finite forest, with every vertex traced
and no extra untraced kernel incidences. Fix integer powers \(n_v\).
At each vertex place a fixed number \(r_v\ge0\) of full endpoint
factors
\[
 Q_{v,N}(Z;\boldsymbol\alpha)
   =\prod_{i=1}^{r_v}K_N(2\cosh(\alpha_{v,i}/N),Z),\qquad
 |\alpha_{v,i}|\le A<\infty .
 \tag{2}
\]
All products are ordinary products before the original trace.
Parameters at different incidences may subsequently be identified;
uniform estimates are taken before or after such an identification.
An empty product is one. Mark a set \(T\subseteq V\) containing every
vertex with \(r_v>0\). The source is
\[
 Z_{F,N}(\boldsymbol\alpha)
 =\left(\prod_{v\in V}\phi_N^{(v)}\right)
   \left[\prod_{v\in V}R(z_v)^{n_v}Q_{v,N}(z_v)
                  \prod_{vw\in E}K_N(z_v,z_w)\right].
 \tag{3}
\]

A **marked reduction certificate** is a fixed finite sequence ending
at the empty forest, using only the following operations on its current
graph, powers, and surviving marks:

* Remove an isolated vertex, marked or unmarked, with any current
  integer power.
* Remove an unmarked leaf \(v\) whose current power is
  \(\sigma\in\{1,-1\}\), and replace its neighbor's power \(n_w\)
  by \(n_w-\sigma\).
* If \(v\) is an unmarked zero-power leaf with neighbor \(w\),
  remove both \(v,w\) and all their incident edges. The neighbor
  may be marked. Powers on all other vertices stay unchanged.

Marks are never transferred. They disappear only with their vertices.
The certificate is independent of \(N\) and all endpoint parameters.
It is stronger than an unmarked reduction certificate: a leaf carrying
a full endpoint product cannot be used in either leaf operation.

Write \(v_0=|V|\), \(r_0=\sum_v r_v\), and
\[
                    n_*=\max(\{\,|n_v|:v\in V\,\}\cup\{0\})+v_0.
 \tag{4}
\]
All current powers occurring in a certificate have absolute value at
most \(n_*\). The empty forest has source one.

## 2. Polynomial bounds and exact removal identities

The full endpoint-product source proves that, on every bounded
complex parameter disk, there are constants \(C_A,p_A\) such that
\[
 \sup_{Z\in[-2,2]}|K_N(2\cosh(\alpha/N),Z)|\le C_A N^{p_A}.
 \tag{5}
\]
Consequently a product of \(r_v\) such kernels has real norm at most
\(C_A^{r_v}N^{p_A r_v}\), and ordinary degree at most \(r_vD\).
The bound includes the whole low and high Newton parts. It is not
only a bound for physical values.

Here are the original identities used to remove leaves:
\[
 \phi_N^{(z)}[K_N(z,w)f(z)]=(Tf)(w),\qquad
 T(R^\sigma)=R^{-\sigma}\quad(\sigma=\pm1),
 \qquad T1=e_D,
 \tag{6}
\]
and, for every remaining local factor \(A\) in the traced algebra,
\[
                  \phi_N(e_D R^n A)=\kappa^n A(c_0).
 \tag{7}
\]
The equalities retain the original full Hermite functional. In
particular the normal in (7) is consumed by the radical \(e_D\);
it is not discarded from \(A\) by a values-only approximation.
The two elementary endpoint values are exactly
\[
                  K_N(c_0,Z)=1,\qquad
                  Q_{v,N}(c_0;\boldsymbol\alpha)=1.
 \tag{8}
\]
Indeed every \(e_k(c_0)\) with \(k\ge1\) is zero. Equations (6)--(8)
hold for all complex endpoint parameters and also at \(N=2\).

At an isolated vertex, the full trace provides a uniform polynomial
estimate for its entire endpoint product. Put
\(Q=Q_{v,N}\), \(n=n_v\). At each double root the original crossing
has unit-modulus value and satisfies
\[
       |(R^n)'(c_a)|\le |n|N^2/8 .
 \tag{9}
\]
Its value at the odd simple root also has modulus one. The trace is
\[
 \phi_N(H)=\eta\sum_{\text{double }a}
             \{(4-c_a^2)H'(c_a)-c_aH(c_a)\}
                  +\mathbf1_{N\ {\rm odd}}H(-2).
 \tag{10}
\]
Markov's inequality for the ordinary polynomial \(Q\) gives
\(\|Q'\|_{[-2,2]}\le (r_vD)^2\|Q\|_{[-2,2]}/2\).
This remains valid for complex coefficients, by taking a real part
with the phase of the derivative at a maximizing point. The case
\(r_v=0\) has derivative zero. Substituting the product derivative
of \(R^nQ\) into (10) yields
\[
 |\phi_N(R^nQ)|
       \le C_{r_v}(1+|n|)N^3\|Q\|_{[-2,2]}
       \le C_{A,r_v}(1+|n|)N^{p_A r_v+3}.
 \tag{11}
\]
An ordinary product may have degree larger than \(N\); (10) depends
only on its actual jets and is still exact. No unstable coefficient
bound for its canonical remainder is required.

## 3. Full-product closure on a marked forest

**Theorem 1.** If \((F,\mathbf n,T)\) has a marked reduction
certificate, then, uniformly on bounded complex endpoint parameter
sets and at both parities,
\[
             |Z_{F,N}(\boldsymbol\alpha)|
                 \le C_{F,\mathbf n,A,\mathbf r}
                            N^{p_A r_0+3v_0}.
 \tag{12}
\]
Every fixed derivative in the endpoint parameters satisfies a
polynomial bound as well, by using a larger parameter disk. The
theorem estimates the actual source (3), not a selected Newton
packet or a source with some normal terms omitted.

*Proof.* Follow the prescribed certificate and keep every surviving
factor in its original trace.

At an unmarked unit leaf the endpoint coupon is exactly one.
Equation (6) replaces the leaf and its edge by \(R^{-\sigma}\) at
the neighbor. Multiplication there changes its current integer
power to \(n_w-\sigma\) and leaves \(Q_{w,N}\) untouched. All
other incident edges and joint factors are unchanged. This
operation has no extra scalar.

At an unmarked zero leaf, (6) inserts \(e_D\) at its neighbor.
Equation (7) evaluates the entire remaining neighbor factor at
\(c_0\), with scalar \(\kappa^{n_w}\). Its endpoint product becomes
one by (8), whether or not the neighbor is marked. Every other
incident kernel also becomes one by (8). Thus the exact surviving
source is the source of the forest with these two vertices removed.
All remaining endpoint parameters and products are unchanged.
The scalar has modulus one. No physical-color sum, new coupon, or
new dependence between components is introduced.

At an isolated vertex use (11). Its factor is independent of the
remaining traced variables; any shared endpoint parameters remain
the same parameters in both factors. At most \(v_0\) such factors
are taken, their current powers obey (4), and the sum of their
endpoint multiplicities is at most \(r_0\). Multiplying their
bounds and the unit-modulus zero-step scalars proves (12).
If a factor vanishes, the same upper bound holds.

The source is entire in each microscopic parameter. Applying (12)
on a larger fixed disk and then Cauchy's formula gives the last
assertion. This proof is coefficientwise in the microscopic
parameters, but it does not insert an arbitrary coupled spectator
into (3). \(\square\)

There is no condition on the powers at decorated vertices other
than the current-power restrictions forced by the chosen certificate.
They may be arbitrary fixed integers when isolated or when consumed
as the neighbor of an unmarked zero leaf.

## 4. The whole original microscopic current

We now apply the theorem to the actual source left by a current.
Use the original circle tree \(G\), a nonempty selected set \(S\),
and all original edges incident to \(S\), counted once. Let \(B\)
be its outside vertices. Every selected vertex is assumed to have
an original incidence. Keep the original unit charges and integer
powers. Choose a nonempty current set \(C\subseteq S\) with
\[
       \{v\in S:\text{\(v\) has an edge to \(B\)}\}\subseteq C.
 \tag{13}
\]
Put \(Y=S\setminus C\) and
\[
              T=\{y\in Y:\text{\(y\) has a neighbor in \(C\)}\}.
 \tag{14}
\]
Then \(G[Y]\) has no untraced kernel incidences. It is a closed forest.
For \(0\le h_v\le\alpha_v/N\), \(0\le\alpha_v\le A<\pi\), set
\[
 w_v=2\cosh h_v,\qquad
 Q_{y,N,\mathbf h}(z)=
                  \prod_{\substack{v\in C\\vy\in E}}K_N(w_v,z)
                    \quad(y\in Y),
\]
\[
 D_{C,N}(\mathbf h;\mathbf z_B)=
 \prod_{\substack{vv'\in E\\v,v'\in C}}K_N(w_v,w_{v'})
 \prod_{\substack{vb\in E\\v\in C,\ b\in B}}K_N(w_v,z_b).
 \tag{15}
\]
Vertices in \(Y\setminus T\) have coupon one. Each current parameter
is retained at all its incident factors.

The original paired vertical density is
\[
 \rho_{N,n,1}(h)=
 \frac{2i\eta N^2C_{N,n}}{\pi}\,
 \frac{\sinh h\ e^{inN(\pi^2-h^2)/(4\pi)}
                          \sinh(nNh/2)}{4\cosh^2(Nh/2)},
 \qquad C_{N,n}=e^{\pi i nD^2/(4N)} .
 \tag{16}
\]
The full current, with no survivor-band projection, is
\[
 \begin{split}
 I_{C,N}(\mathbf z_B)=
 \int_{\prod_{v\in C}[0,\alpha_v/N]}
 &\prod_{v\in C}\{\rho_{N,n_v,1}(h_v)\,dh_v\}\,
 D_{C,N}(\mathbf h;\mathbf z_B)\\
 &\times
 \left(\prod_{y\in Y}\phi_N^{(y)}\right)
 \left[\prod_{y\in Y}R(z_y)^{n_y}Q_{y,N,\mathbf h}(z_y)
                   \prod_{yy'\in E(G[Y])}K_N(z_y,z_{y'})\right].
 \end{split}
 \tag{17}
\]
This is the original full-survivor current. If it occurs in the
full inclusion--exclusion formula, its coefficient remains
\((-1)^{|C|+1}\). No such sign or carrier is altered.

**Theorem 2.** Assume that \((G[Y],\mathbf n|_Y,T)\) has a marked
reduction certificate. For real outside colors \(z_b\in[-2,2]\),
\[
                  |I_{C,N}(\mathbf z_B)|\le C N^{p_C},
 \qquad
                  p_C=2(e_C+b_C)+3|Y|.
 \tag{18}
\]
Here \(e_C\) is the number of edges within \(C\), and \(b_C\) the
number with exactly one endpoint in \(C\), including outside edges.
Constants depend on the fixed graph, powers, certificate and \(A\).
Any fixed ordinary outside derivative of total order \(|\beta|\)
has the same bound with exponent \(p_C+2|\beta|\).

*Proof.* For the real microscopic heights in (15), the full current
source gives the sharper product estimate
\[
 \sup_{z\in[-2,2]}|Q_{y,N,\mathbf h}(z)|\le C N^{2r_y},
 \quad r_y=\#\{v\in C:vy\in E\}.
 \tag{19}
\]
Use the proof of Theorem 1 with this bound in place of (5).
The surviving trace in (17) is therefore at most
\(CN^{2b_{CY}+3|Y|}\), where \(b_{CY}=\sum_y r_y\).
This is a bound for its entire shared full-normal contraction.

The same original current source gives
\[
 \int_0^{\alpha_v/N}|\rho_{N,n_v,1}(h)|\,dh\le C,\qquad
 |D_{C,N}(\mathbf h;\mathbf z_B)|\le C N^{2(e_C+b_{CB})}.
 \tag{20}
\]
For the first estimate, \(N^2\), \(\sinh h\), and the integration
length cost \(N^2,N^{-1},N^{-1}\); all remaining factors are bounded
when \(Nh\le A\), with fixed \(n_v\). The second bound retains the
internal \(C\)-edges as well as all \(C\)--outside factors.
Since \(b_C=b_{CY}+b_{CB}\), integration proves (18).

By (13), all outside variables occur in \(D_{C,N}\). More generally
the integrated expression is an ordinary polynomial of degree at
most \(d_bD\) in \(z_b\), where \(d_b\) is its original included
incidence degree. The real-cube bound and Markov's inequality in
each outside coordinate give \(N^2\) per fixed derivative, with
graph-dependent constants. No outside variable is reduced modulo
\(P_N\). \(\square\)

Empty \(Y\) is allowed, with its empty marked certificate. All
remaining traces in (17) were performed by the proved finite
reduction; there is no supplied descendant quantum bound.

## 5. Strict parent gap and the remaining scope

Suppose the same original unit-charge parent has a supplied positive
solution at complete outside angles. Its original calibrated action is
\[
                  M_G=e_GM_\infty-\mathcal E(z_0)/\pi>0,
             \qquad M_\infty=4G_{\rm Cat}/\pi .
 \tag{21}
\]
The pinned current-gap source proves the strict inequality from the
interior square energies: each is strictly below its constant boundary
value, with two squares per included original edge. No positivity
assumption on the surviving forest is used here.

Thus (18), including fixed outside normals, gives
\[
 \limsup_{N\to\infty}N^{-1}\log|I_{C,N}|\le0<M_G
 \tag{22}
\]
at complete outside colors. In particular, for example,
\(|I_{C,N}|\le CN^p e^{N(M_G-M_G/2)}\).
A finite collection of current sets satisfying (13) and the marked
certificate has one common polynomial bound. Unlike the all-top
packet theorem, no small Newton-band width is chosen.

There is also the explicit ordinary outside continuation
\[
 |I_{C,N}(\{-2\cos u_b\})|
 \le CN^{p'}\exp\!\left(N\sum_{b\in B}d_b|\Im u_b|\right).
 \tag{23}
\]
Indeed tensor cosine coefficients are bounded by a fixed constant
times the real-cube norm, there are polynomially many of them, and
their frequencies in coordinate \(b\) are at most \(d_bD\).
The same argument after fixed outside derivatives proves their
corresponding bound. A fixed region
\(\sum_b d_b|\Im u_b|\le M_G/2\) retains a strict parent gap.
There is no polynomial bound at arbitrary complex outside colors.

The marked certificate is essential to this proof. An ordinary
unmarked certificate might require turning a decorated leaf, which
would transmit a full high-degree coupon and leave the present class.
Theorem 1 makes no assertion for that situation. It also excludes
extra untraced kernel incidences and arbitrary coupled spectators.
Theorem 2 covers the whole microscopic current for its specified
current sets, but not macroscopic current heights, other current
patterns, the horizontal whole source, or its nonzero coefficient.

The bulk scalar compatibility theorem is complementary: it handles
the normal defect on thin bulk domains. No step above infers a
global source bound from that local theorem. Here the bound follows
from exact source closure under the marked reduction operations.

## 6. Coverage and direct sources

The original zero/unit leaf identities, isolated trace bound and
microscopic current normalization are prior results. The new closure
keeps arbitrary fixed full endpoint products static at marked vertices,
and consumes them only by their exact endpoint evaluation or an
isolated full trace. It consequently controls the entire current
(17), rather than only the all-decorated-top packet.

All four complete direct sources were read at the following unchanged
versions, their used implications checked, and their hashes verified:

* [Exact zero/unit leaf carriers](research_low_degree_charged_leaf_reduction.md),
  SHA256 80df78ceafaa97182aebc6831651921f7f8040e1356ee07a3d0d3fbadd02846a:
  the literal identities \(T(R^\sigma)=R^{-\sigma}\),
  \(R(c_0)=\kappa\), and the full-normal endpoint evaluation (7),
  including both parities and \(N=2\).
* [Certified charged forest reductions](research_charged_forest_leaf_pruning_bound.md),
  SHA256 53e401677dc75e264717abe12ef66f950b240952d78533b71e364be5a57a1fa5:
  exact signed leaf operations, original full trace and crossing
  normals, and finite certificate bookkeeping.
* [Full endpoint-product source](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  polynomial ordinary real norm on every bounded complex microscopic
  parameter set, with all shared endpoint factors retained.
* [Microscopic all-top current gap](research_microscopic_all_top_current_gap.md),
  SHA256 458debb4f57863a36d2999fb756616c071e167f85ecf95f929da5d9881ffd11f:
  full-survivor current and carrier conventions, safe outside-incidence
  hypothesis, microscopic bounds, and strict parent action positivity.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical experiment, test or build was run.
Adopted files and public manuscripts remain unchanged.
