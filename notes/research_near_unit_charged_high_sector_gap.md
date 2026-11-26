# A uniform high-sector gap for lattice charges near one

Private written proof, 16 November 2026.

For a fixed zero-power subtree whose unit-charge optimizer has strictly
low original edge indices, the full high-index contribution remains
exponentially smaller on a fixed one-sided neighborhood of unit charge.
The charges may vary with the level. The estimate keeps every boundary
high index, every shared internal index, and the original full Hermite
closing functional. It holds at both level parities.

The mechanism is an exact polynomial bound for the charged closing row,
followed by compactness of the original positive Newton optimization
with its final output constraints relaxed. No positivity of the charged
trace itself is asserted.

## 1. Original source and hypotheses

Let \(T\) be a fixed finite tree and \(S\) a nonempty connected proper
set of its vertices. Every selected crossing power is zero. Each
selected vertex has original degree \(d_v\ge3\), including edges to the
complement. Write \(E_S\) for all edges incident to \(S\), and
\(\partial S\) for those with exactly one selected endpoint. Put
\(s=|S|\) and \(b=|\partial S|\). Thus
\[
 b=\sum_{v\in S}d_v-2(s-1)\ge s+2.
 \tag{1}
\]
Every outside endpoint is distinct, so its boundary angle \(u_e\)
remains an independent variable.

Use the original full algebra and Newton normalization
\[
 D=N-1,\quad \eta=(-1)^D,\quad
 \mathcal A_N=\mathbb C[z]/(P_N),\quad
 P_N(z)=2T_N(z/2)+2,
\]
\[
 s_j=2\sin(\pi j/N),\qquad S_j=\prod_{h=1}^j s_h,\qquad
 c_a=2\cos((2a+1)\pi/N),
\]
\[
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
Here \(S_0=1\). The repeated roots of \(P_N\), including their first
normal data, are retained. In particular
\[
 \phi_N(e_i e_j)=\mathbf1_{i+j=D},\qquad
 \phi_N\!\left(\sum_j f_j e_j\right)=f_D.
 \tag{3}
\]
The original edge kernel is
\[
 K_N(t,u)=\sum_{a=0}^D e_a(-2\cos t)e_a(-2\cos u).
 \tag{4}
\]

The entire cosine charge coupon \(\mathcal C_{N,c}\) is the class
having the full spectral jets of \(\cos(N(1-c)t)\) at the physical
angles. At a lattice charge
\[
 c=J/N,\qquad 1\le J\le N,\qquad k=N-J,
\]
it is exactly
\[
 \mathcal C_{N,J/N}=T_k(-z/2)\quad\hbox{in }\mathcal A_N.
 \tag{5}
\]
Indeed \(\cos(kt)=T_k(-z/2)\) for \(z=-2\cos t\), and \(k<N\).
This identifies the polynomial and all its normals, not just its
physical values. The separate identity with \(\eta T_J(-z/2)\)
usually holds only in values; it is not substituted for (5).

Define the original charged boundary source
\[
 Z_{N,\mathbf c}(\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[
 \prod_{v\in S}\mathcal C_{N,c_v}(z_v)
 \prod_{vw\subset S}K_N(t_v,t_w)
 \prod_{\substack{e=vw\in\partial S\\v\in S}}
                         K_N(t_v,u_e)\right].
 \tag{6}
\]
Let \(Z^{\mathrm{low}}_{N,\mathbf c}\) retain exactly the assignments
with \(2a_e<N\) on every original edge \(e\in E_S\). No quotient or
trace convention changes in this restriction.

We assume that the unique unit-charge height minimizer is regular:
\[
 \sinh(H_v^*/2)\sinh(H_w^*/2)<1
                  \qquad(vw\subset S).
 \tag{7}
\]
Outside heights are zero. Under this hypothesis the
unit positive Newton optimizer has every original physical edge
coordinate strictly below \(1/2\). The internal-gap source proves
this identification and the equality of the Newton and height actions.
Write their common value as \(M_1\). Condition (7), rather than an
assumption on the charged trace's signs, is the hypothesis used below.

**Theorem.** There are \(\varepsilon,\delta>0\), \(C,A<\infty\), and
\(N_0\), depending only on the fixed selected subtree, such that
\[
 \sup_{\mathbf u\in\mathbb R^{\partial S}}
 |Z_{N,\mathbf c}(\mathbf u)-Z^{\mathrm{low}}_{N,\mathbf c}(\mathbf u)|
       \le C N^A e^{N(M_1-\delta)}
 \tag{8}
\]
whenever \(N\ge N_0\) and all \(c_v=J_v/N\) lie in
\([1-\varepsilon,1]\). Both level parities and every lattice tuple in
that box are included. The bound persists, with a smaller gap, on a
fixed complex strip about the real boundary torus and with every fixed
angular boundary derivative.

The charged height action
\[
 M(\mathbf c)=\min_{\mathbf H\ge0}
 \left\{\sum_{vw\in E_S}V(H_v,H_w)
                      -\sum_{v\in S}c_vH_v\right\}
 \tag{9}
\]
satisfies \(M(\mathbf c)\ge M_1\) for \(0<c_v\le1\).
Consequently (8) is also a strict gap below \(M(\mathbf c)\).
Near \(\mathbf c=\mathbf1\) the minimizing heights, original regular
edge indices, and action vary real analytically.

## 2. Exact charged closing rows with polynomial cost

Put \(m=\lfloor N/2\rfloor\). For \(0\le r<m\), the exact radical
divided-difference formula is
\[
 [e_r]f=\phi_N(e_{D-r}f)
       =\sum_{a=0}^r b_{ra}f(c_a),\qquad |b_{ra}|\le2.
 \tag{10}
\]
The double-node normal in the original trace is precisely what makes
(10) true. It is not an evaluation replacement for a general trace.

Suppose \(k<m\), and expand the actual coupon
\[
 T_k(-z/2)=\sum_{r=0}^k q_{k,r}e_r(z).
 \tag{11}
\]
Its degree gives the exact support in (11). Since
\(-c_a/2\in[-1,1]\), \(|T_k(-c_a/2)|\le1\). Equation (10) gives
\[
 |q_{k,r}|\le2(r+1)\le2N,\qquad
 \sum_{r=0}^k|q_{k,r}|\le(k+1)(k+2).
 \tag{12}
\]
For every \(f=\sum_{j=0}^D f_j e_j\), full Frobenius duality now gives
the exact identity
\[
 \boxed{\quad
 \phi_N(\mathcal C_{N,J/N}f)
          =\sum_{r=0}^{k}q_{k,r}f_{D-r},
             \qquad k=N-J<m.
 \quad}
 \tag{13}
\]
Thus charging the selected vertex relaxes its final output from \(D\)
to one of \(D,D-1,\ldots,D-k\), at polynomial cost.

For comparison, multiplication by \(X=-z/2\) in the full Newton basis is
\[
 Xe_j=-\frac{c_j}{2}e_j+\frac{s_{j+1}^2}{2}e_{j+1},
 \tag{14}
\]
with the last raised term zero in the quotient. The Chebyshev recurrence
therefore gives bandwidth \(k\) and the safe general matrix bound
\(\|T_k(X)\|_\infty\le7^k\). For the actual row (13), (12) is stronger:
no exponential \(7^k\) loss will be used.

Apply (13) separately at each selected vertex after expanding the
original edge kernels. For a fixed edge assignment, the uncharged
product at that vertex has nonnegative Newton coefficients, because
the original multiplication coefficients are
\[
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}}
 \quad\hbox{on}\quad
 \max(i,j)\le r\le i+j\le D,
 \tag{15}
\]
and zero off that support. All indices on the two ends of an original
edge remain the same index. Taking absolute values of the \(q_{k,r}\)
in (13) does not separate any of these shared indices.

## 3. One compact action for all relaxed outputs

Root the selected tree. At each nonroot vertex resolve the factors
other than its parent edge first, then multiply their product by the
parent-edge factor in the final binary product. At the root choose
any fixed binary resolution. Retain **every** binary product,
including its final product. Denote that final output by \(o_v\).
All physical edge indices and all intermediate product outputs are
independent labels subject to the original product supports and the
shared-edge equalities.

For real boundary angles use the positive coefficient envelope
\[
 w_{N,a}=
 \begin{cases}
 e_a(-2),&2a<N,\\
 1,&2a\ge N .
 \end{cases}
 \qquad
 |e_a(-2\cos u)|\le C N^{A_0}w_{N,a}.
 \tag{16}
\]
The high part is a bound for the whole original polynomial on the
real interval, with its full normals already accounted for. This is
the boundary envelope from the high-boundary source.

Scale every label by \(D\). For \(0\le\rho<1\), let \(P_\rho\) be the
closed polytope with all labels in \([0,1]\), every product satisfying
\[
 \max(x,y)\le z\le x+y\le1,
 \tag{17}
\]
the original shared-edge identifications, and
\[
                         1-\rho\le o_v\le1.
 \tag{18}
\]
These are compact nested polytopes, and
\(\bigcap_{\rho>0}P_\rho=P_0\).

Put
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 g(x)=J(2x)-4J(x)\quad(0\le x\le1/2),
\]
\[
 \psi(x)=
 \begin{cases}g(x),&0\le x\le1/2,\\0,&1/2\le x\le1,\end{cases}
 \tag{19}
\]
\[
 m(x,y,z)=J(x+y)+J(z)-J(x)-J(y)
                  -J(z-x)-J(z-y)-J(x+y-z).
 \tag{20}
\]
Since \(J(1)=J(1/2)=0\), the two values of \(\psi\) agree at
\(1/2\). The action
\[
 \mathcal A=\sum_{\text{boundary edges }e}\psi(a_e)
              +\sum_{\text{all retained products}}m(x,y,z)
 \tag{21}
\]
is continuous on the entire compact support body.

Uniform sine-factorial estimates, including zero factorial arguments,
give for every positive state weight made from (15) and (16)
\[
          \log w_N=N\mathcal A(\text{labels}/D)+O(\log N).
 \tag{22}
\]
The constant depends only on the fixed tree and resolution. The change
from scale \(N\) to \(D=N-1\) costs \(O(\log N)\), by the endpoint
modulus of continuity of \(J\). The low boundary estimate in (22)
also holds at the odd middle label; its limiting profile is zero.
For high boundary labels the weight is exactly one. There are only
polynomially many states, uniformly in the permitted final outputs.

Let \(H\) denote the closed set where at least one **original** edge
index is at least \(1/2\). Auxiliary product labels do not define this
high set. We claim that
\[
                    \sup_{P_0\cap H}\mathcal A<M_1.
 \tag{23}
\]

First, at \(o_v=1\), the last product at each vertex forces
its two inputs to sum to one. Its coefficient is exactly one, and
its action in (20) is zero. Removing these forced products while
retaining their complementary constraints gives precisely the
original unit-charge product/reversal expression: eliminate nonroot
vertices successively towards the root, so the parent-edge label is
exactly complementary to the child product output. This explains why
they had to be retained before relaxing (18).

On the part of \(P_0\) with all boundary labels at most \(1/2\),
the action is the old concave Newton action. Its unique optimizer has
all original edge labels strictly below \(1/2\), by (7) and the
internal-gap theorem. Compactness therefore gives a strict loss
on its intersection with \(H\).

For boundary labels greater than \(1/2\), use the actual
**positive comparison with shared indices** imported and applied in
the high-boundary source. Applied to the positive arrays \(w_{N,a}\)
themselves, it bounds the sum of positive unit-output weights with
any high boundary index by
\[
                      C N^A e^{N(M_1-\delta_b)}
 \tag{24}
\]
for some \(\delta_b>0\), leaving every internal index unrestricted.
This is the positive comparison used before the absolute-value bound
for the original boundary arrays; it is not deduced from a bound on
an already signed scalar.

To see explicitly that (24) bounds the continuous action, take a
rational point of \(P_0\) with one boundary label strictly greater
than \(1/2\). Along arbitrarily large even \(D\) divisible by its
denominators, it is an exact positive integer state, and that
boundary index satisfies \(2a\ge D+1=N\). Its weight occurs in
(24), so (22) gives \(\mathcal A\le M_1-\delta_b\).
Rational points are dense in the rational support polytope, also
after intersection with this open half-space. Continuity proves the
same inequality at every such real point and every limit of them.
Any remaining point with boundary labels at most \(1/2\), including
labels exactly \(1/2\), was already covered by the preceding
unique-optimizer argument. Taking the smaller of these two losses
proves (23), including the closed high threshold.

Finally, compactness and continuity give \(\rho_0,\delta_0>0\) such
that
\[
          \sup_{P_\rho\cap H}\mathcal A
                       \le M_1-2\delta_0
                    \qquad(0\le\rho\le\rho_0).
 \tag{25}
\]
Otherwise choose \(\rho_j\downarrow0\) and violating states.
A subsequence converges in the fixed compact support body to a point
of \(P_0\cap H\), contradicting (23), after reducing \(\delta_0\).
This argument does not claim concavity for the high boundary envelope
or for the relaxed-output problem.

## 4. The actual charged high sum

Choose \(\varepsilon>0\) small enough that \(2\varepsilon<\rho_0\)
and \(\varepsilon<1/4\). For sufficiently large \(N\),
\[
 k_v=N(1-c_v)\le\varepsilon N<m,\qquad
                  \frac{k_v}{D}\le2\varepsilon .
 \tag{26}
\]
Equation (13) expresses every charged vertex contribution as a finite
sum of the positive uncharged product outputs allowed in \(P_{2\varepsilon}\).
The exact difference \(Z-Z^{\mathrm{low}}\) is the sum of original
edge assignments with at least one \(2a_e\ge N\). Their scaled
indices satisfy \(a_e/D>1/2\), so all these assignments lie in \(H\).

Replace each boundary coefficient by (16), each charged row coefficient
by the bound \(2N\) in (12), and expand all the positive products (15).
This yields an upper bound by a polynomial factor times the positive
state sum on \(P_{2\varepsilon}\cap H\). The output choices add only
polynomially many labels. The common physical edge labels have never
been replaced by independent endpoint labels.

Equations (22) and (25), together with the fixed-dimensional polynomial
state count, now give (8), with \(\delta=\delta_0\) if desired.
Nothing in this final estimate uses the odd subsequence employed to
identify the continuous maximum in (23); the finite estimate holds
at every sufficiently large level.

For the boundary continuation, the difference is a Laurent polynomial
of degree at most \(D\) in each angular variable. Each Fourier
coefficient is bounded by its real-torus supremum. Consequently, at
\(\mathbf u=\mathbf x+i\mathbf y\), that supremum times
\[
                    (2D+1)^b e^{D\sum_e|y_e|}
 \tag{27}
\]
bounds the polynomial. Every fixed angular derivative adds only a
power of \(D\). Choose a fixed strip with
\(\sum_e|y_e|<\delta/2\). This proves the asserted complex and
derivative versions. The boundary variables remain ordinary
polynomial variables throughout.

## 5. Relation to the charged action and the remaining low source

The edge potential in (9) is
\[
 V(H,G)=\max_{0\le x\le1/2}
       \{B(x,H)+B(x,G)\},
\]
\[
 B(x,H)=\int_0^x
       \log(2\cos2\pi t+2\cosh H)\,dt-2J(x).
 \tag{28}
\]
The convex-potential source proves its continuity and convexity,
its regular positive Hessian, and
\(V(H,G)\ge(H+G)/2\). For \(0<c_v\le1\),
\[
 \sum_eV(H_v,H_w)-\sum_v c_vH_v
    \ge\sum_v(d_v/2-c_v)H_v
    \ge\frac12\sum_vH_v.
 \tag{29}
\]
Thus its minimum exists. More directly,
\[
 \mathcal L_{\mathbf c}(\mathbf H)
   =\mathcal L_{\mathbf1}(\mathbf H)
                     +\sum_v(1-c_v)H_v
   \ge\mathcal L_{\mathbf1}(\mathbf H),
\]
and taking minima gives
\[
                         M(\mathbf c)\ge M_1.
 \tag{30}
\]
There is no continuity loss to subtract from the high gap.

At the regular unit minimizer every selected coordinate is covered
by a positive definite regular edge form (or by a positive scalar
boundary-edge form). The assembled Hessian is positive definite.
The implicit function theorem therefore continues the positive
minimizer analytically for \(\mathbf c\) near \(\mathbf1\).
Strict regularity persists. Convexity makes this stationary point the
unique global minimizer. Its equations are the original charged
height rows \(\sum_{e\ni v}\alpha_{v,e}=\pi c_v\).
Thus (9) is the same marked charged height action, not an unrelated
comparison maximum.

The theorem removes the entire high-index complement on the stated
lattice-charge neighborhood. In particular, on any charge set there
where an actual all-low asymptotic with a nonzero leading coefficient
and action \(M(\mathbf c)\) has been proved uniformly, the original
full source has that same expansion, up to an exponentially smaller
error. This last inference uses (8); it does not supply the low
expansion.

The uniform high estimate includes \(c_v=1\) and sequences
\(J_v=N-O(1)\). A uniform single low-sector formula across those
sequences requires separate treatment: the Fourier companion with
charge \(2N-J_v\) is not exponentially separated when \(N-J_v=O(1)\).
Neither that issue nor the distinct zero-charge endpoint is removed
by the present estimate. It does not furnish all samples required by
the finite charge reconstruction theorem, a complex-charge initializer
on its own, or arbitrary further-filling noncancellation.

## Direct sources and versions

The full proof was written without mathematical execution. Every
direct source below was read in full at the stated version, and the
entire final proof is reread before freezing.

- [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  original algebra, Frobenius duality, exact low divided differences,
  their uniform coefficient bound, and retained normal interpretation.
- [Internal high-index gap](research_zero_subtree_internal_high_gap.md),
  SHA256 1a2edaa55af545613c20a60158f2cb314bb86c1254f7c53e6cb56a42f5b5f5fa:
  positive multiplication support, uniform action estimates, strict
  optimizer, and regular-unit action identification.
- [High boundary-index gap](research_zero_subtree_high_boundary_gap.md),
  SHA256 e926556ea5862eec1caba939993fe610bc3f1a591efcf16c35f20e7b6ccdeae1:
  actual full-polynomial boundary envelope and the positive
  shared-index comparison for all high boundary assignments.
- [Zero-power convex potential](research_zero_power_subtree_convex_potential.md),
  SHA256 c0ab73c2869ed3db7a0152634cbf3a315c573eed2f5fc99e437dacadcceb8eb8:
  exact height potential, regular Hessians, coercivity and unit rows.
- [Canonical finite charge source](research_polarized_charge_heat_source.md),
  SHA256 860801dedc3f1093d58c0413f580599512bd2566c00f4a94d0ebf99636343db1:
  original cosine coupon with all physical values and normals, and
  its distinction from the separately polarized charge families.
