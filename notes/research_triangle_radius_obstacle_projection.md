# Concave triangle radii and the overload obstacle projection

31 October 2026. **Research reduction; the universal comparison remains open.**
The concavity, clipping theorem and exact counterexamples below have received
independent analytical reviews. They concern one fixed actual
LEFT/CROSS/RIGHT sector and preserve its original protected faces and targets.
They do not establish a new general filling theorem.

The [finite-sector criterion](general_actual_sector_cover_filling_volume.md)
explains the desired application. The
[fractional forest analysis](research_fixed_sector_fractional_forest_reduction.md)
records why a local completion cannot simply discard shared face loads.

## 1. An ordinary-radius concavity theorem

For the original triangle entropy \(C(\alpha)\), with
\(\sum\alpha_i=1/2\), put

$$
\begin{aligned}
p&=2\alpha,\qquad K(p)=2C(p/2),\qquad
H(p)=-\sum_i p_i\log p_i,\\
G(p)&=K(p)-H(p),\\
F(w)&=\exp(2Q(w))
 =\exp\max_{p\in\Delta}\left(K(p)+\sum_i p_i\log w_i\right).
\end{aligned}\tag{1}
$$

The [triangle Shannon inequality](actual_triangle_entropy_algebraic_balance.md)
gives \(G\ge0\). Its ambient diagonal second derivatives satisfy

$$
\frac{\partial^2G}{\partial p_i^2}
 =\frac1{p_i}-\frac{\pi}{\sin(\pi p_i)}<0.\tag{2}
$$

Thus \(G\) is strictly concave and extends continuously to the closed
simplex. A supporting plane at an interior point has the form
\(G(p)\le a\cdot p+b\). The ordinary entropy variational formula gives

$$
F(w)\le e^b\sum_i e^{a_i}w_i.\tag{3}
$$

For any positive \(w^0\), choose the supporting point to be its optimizer
in (1). Stationarity gives \(p_i^0\propto w_i^0e^{a_i}\), so equality
holds in (3) at \(w^0\). Therefore \(F\) is the infimum of positive
linear forms. In particular it is **concave in ordinary radii**, homogeneous
of degree one and coordinate-monotone. Equivalently,

$$
F(w)\le F(w^0)\sum_i p_i^0\frac{w_i}{w_i^0}.\tag{4}
$$

Original zero-face continuity extends this to nonnegative coordinates,
with \(F(0)=0\). The absolute normalization also gives

$$
F(w)\ge\sum_iw_i\ge\max_iw_i,\tag{5}
$$

strictly in the first inequality when at least two weights are positive.
This is a stronger statement than convexity of \(Q\) in logarithmic radii;
the two statements are compatible.

## 2. A convergent, order-independent clipping procedure

At each surviving one-sided port let \(o_e\) be its overloaded ordinary
middle and \(I_e=(x,p,y)\) its retained triangle. Its actual weighted bound is

$$
A_e(L)=\max\left(\log L_o,Q(L_I)+\frac12\log L_o\right).
\tag{6}
$$

A protected overloaded middle makes the original sector zero and is omitted.
The input triangle has three distinct vertices and at least one ordinary
vertex. The child \(o\) is not an input vertex. The pure branch is active
exactly when \(L_o\ge F(L_I)\).

Starting with any finite positive ordinary vector, choose a selected port
and perform

$$
L_o\longleftarrow\min\{L_o,F(L_I)\}.\tag{7}
$$

Both protected coordinates remain exactly zero. If \(m,M\) are the minimum
and maximum starting ordinary radii, every iterate lies in \([m,M]\): an
input has an ordinary coordinate at least \(m\), and (5) bounds its new
child below by \(m\). No marked-radius regularization is needed.

Let the full fixed-sector cost be

$$
V_s(L)=\sum_{e\in C}X_e(L)+\sum_{e\notin C}A_e(L)
                          -\sum_{f\text{ ordinary}}\log L_f.
\tag{8}
$$

Every update (7) makes \(V_s\) nonincreasing. Along a nontrivial update the
chosen row stays on its pure branch down to the tie, so its \(\log L_o\)
cancels the target \(-\log L_o\). Every other local term is
coordinate-monotone, including through changes of its maximizing branch.
Thus decreasing \(L_o\) cannot increase the remaining expression. This
also handles repeated overloaded children and arbitrary interactions between
branches; no differentiability is required.

Visit each selected port infinitely often, in any fair asynchronous order.
Every coordinate decreases to a limit \(L^\infty\in[m,M]\). Continuity
along the update subsequence at a fixed port gives

$$
L_o^\infty\le F(L_I^\infty)\quad\text{for every selected port}.\tag{9}
$$

In fact this limit is independent of the fair order. If \(B\) is any
feasible positive vector with \(B\le L^{\mathrm{start}}\), monotonicity of
\(F\) preserves \(B\le L\) under every update. Hence
\(B\le L^\infty\). The limit is the **greatest feasible vector below the
starting vector**, uniquely characterized this way.

The feasible domain is convex in ordinary radii, since each constraint in
(9) is a hypograph of a concave function. It is also closed under
coordinatewise maximum. At any coordinate that decreased, at least one
constraint having it as child is tight: otherwise that coordinate could
be raised slightly, improving input constraints and preserving its strict
child constraints, contradicting greatestness. No uniform convergence rate
is claimed.

Define the half-triangle potential

$$
V_{\mathrm{half}}(L)=\sum_{e\in C}X_e(L)
 +\sum_{e\notin C}\left(Q(L_{I_e})+\frac12\log L_{o_e}\right)
 -\sum_{f\text{ ordinary}}\log L_f.\tag{10}
$$

At the clipped limit \(V_s=V_{\mathrm{half}}\). Therefore the exact
variational restriction is

$$
\boxed{\quad
\inf_{L>0}V_s(L)
 =\inf_{\substack{L>0\\L_{o_e}\le F(L_{I_e})\ \forall e}}
                         V_{\mathrm{half}}(L).
\quad}\tag{11}
$$

The clipping procedure gives a finite positive admissible vector of no
larger full cost from every starting vector. Attainment of either infimum
is unnecessary.

## 3. Half descent fails even from a complete packing

The monotonicity in §2 applies to \(V_s\), not to \(V_{\mathrm{half}}\).
An exact example uses the original reduced width-three word
\((1,3,2,1,3)\), first cap mark, protected faces \(0,1\). Its actual
[complete packing](general_anchored_shared_radius_filling_volume.md) has

$$
(L_2,L_3,L_4,L_5,L_6)=(1,\varphi^2,\varphi^2,\varphi^3,1),
\qquad\varphi=\frac{1+\sqrt5}{2}.
$$

Select only port \(0\) LEFT. Its retained triangle is monomial, so clipping
changes only \(c=L_4\), from \(\varphi^2\) to \(1\). The exact derivative is

$$
\frac{\partial V_{\mathrm{half}}}{\partial\log c}
=-\frac12+\frac2\pi
 \arctan\frac{c}{\sqrt{c(1+\varphi^3)+\varphi^3}}
 +\frac1\pi\arctan\sqrt c.\tag{12}
$$

At the starting packing it is \(1/2-\arctan(\varphi)/\pi>0\), using
\(\varphi^2(1+\varphi^3)+\varphi^3=\varphi^6\). At the endpoint it is

$$
-\frac14+\frac2\pi\arctan\frac1{\sqrt{1+2\varphi^3}}<0,\tag{13}
$$

because \(1+2\varphi^3=5+2\sqrt5>(1+\sqrt2)^2\). Thus the half potential
increases on a final subinterval of the clipping path, although the full
sector cost continues to decrease. With one selected port there is no
alternative update ordering that repairs this pointwise assertion.

## 4. The greatest geometric projection can end above volume

A stronger example uses the literal width-three word

$$
(1,3,0,2,4,1,3),\qquad\text{first cap mark, protected }(0,6),
$$

with complete curvatures

$$
(L_0,\ldots,L_8)=(0,16,9,25,1,4,0,1,9).\tag{14}
$$

These are certified without a numerical packing solve. The original compiler
gives seven ports, fourteen distinct triangles and twenty-one edges, each
incident to two triangles. Every triangle discriminant
\(D=\sqrt{\sum_{i<j}L_iL_j}\) is an integer. At ordinary face \(f\),
multiply \(D+iL_f\) over its incident triangles, using \(i\) for a monomial
triangle. In face order \(1,2,3,4,5,7,8\), the products are

$$
-6800,\ -994500,\ -24650,\ -1700,\ -490100,\ -100,\ -1170.
$$

Each angle is positive; elementary \(\pi/4\) or \(\pi/2\) bounds put
each total below \(2\pi\) (in fact at most \(7\pi/4\)). The negative
real products therefore make every total exactly \(\pi\). All original
ordinary angle loads equal one. The convex complete potential is stationary
and hence minimizes at (14), giving its actual complete rate \(\Phi_D\).
Uniqueness modulo scale identifies the complete geometry.

Select only port \(2\) RIGHT. Its quartet is \((0,1,6,4)\), with sole
ordinary retained input \(L_4=1\). Greatest clipping changes only
\(L_1:16\to1\). After cancelling unchanged original factors, the endpoint
half potential minus the complete rate is exactly

$$
\begin{aligned}
\Delta={}&Q(1,0,9)+Q(1,1,9)-Q(16,0,9)-Q(16,1,9)\\
&-Q(0,16,1)+\log16.
\end{aligned}\tag{15}
$$

A 192-bit Arb evaluation with 2,048 Fourier terms for each Lobachevsky
function and the explicit tail \(1/(2M)\) certifies

$$
0.22616591009<\Delta<0.22989612898,\qquad\Delta>0.22.
\tag{16}
$$

The finite check verifies the original chart, all seven exact angle products,
the single clipping constraint and both the cancelled expression (15) and
the full potential difference. Its inputs are exact integers; no optimized
or rounded packing is used as proof.

There is only one constraint, so simultaneous or reordered clipping gives
the same endpoint. Consequently the greatest projection of the geometric
vector need not pass the desired bound. Equation (11) remains valid: a
different feasible vector, potentially smaller than the greatest one or
obtained by changing other faces, may still pass. This is not a fixed-sector
capacity excess or an original quantum-rate counterexample.

## 5. The remaining global inequality

On the feasible domain,

$$
V_{\mathrm{half}}(L)=V_{\mathrm{complete}}(L)
 -\sum_{e\text{ selected}}
       \left(Q(L_x,L_o,L_y)-\frac12\log L_o\right).\tag{17}
$$

Every bracket is strictly positive: a surviving overloaded middle is
ordinary, and the outer pair is MATCHING, so cannot be the two protected
MAIN vertices. The deleted triangle has at least two positive coordinates.
At the complete geometric vector this puts the half potential below
\(\Phi_D\). Equations (13) and (16) show why clipping alone does not
preserve that certificate. The open step is to find an appropriate feasible
vector whose deleted-triangle defect exceeds the complete-potential excess.

Equalizing middle radii also needs its original target correction. For one
unprotected edge \(b=c=B\), the old cost is the identity-smoothed remaining
potential **plus**

$$
Q(x,B,y)-\frac12\log B\ge0.\tag{18}
$$

These terms add over a selected forest. A protected component cannot impose
middle equality at positive ordinary radii at all: equality with its root
sets those radii to zero and requires a separate target adapter. Neither
(18) nor concavity of \(F\) is an existing smoothing-volume upper bound.

The source identities, clipping reduction, exact obstruction and their scope
were independently reviewed. The focused exact source and interval checks
were independently replayed. They establish (11) and refute the proposed
monotonicity and greatest-projection bounds; the universal optimized
fixed-sector inequality remains open.
