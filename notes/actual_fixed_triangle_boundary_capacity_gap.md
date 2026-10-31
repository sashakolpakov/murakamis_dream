# Quantitative loss on a fixed boundary face of the complete angle flow

31 October 2026. analytical lemma. This concerns
the original complete triangle capacity and its actual shared face equations.
It does not turn the weighted LEFT envelope into a coefficientwise comparison.

## 1. Strong concavity with the source normalization

For every actual triangle corner use the normalized load
\(a=\theta/(2\pi)\in[0,1/2]\), with each triangle row summing to \(1/2\).
Protected-face corners are zero, and every ordinary face has total load one.
Let \(\mathcal P\) be this compact feasible polytope, retaining all actual
corner incidences. Its complete source entropy is

\[
 E(a)=\sum_{t,f}f(a_{tf}),\qquad
 f(s)=\frac{\Lambda(\pi s)+\Lambda(\pi/2-\pi s)}{\pi}.
\]

This is the normalization in the [triangle Legendre identity](actual_triangle_entropy_algebraic_balance.md).
For \(0<s<1/2\), direct differentiation gives

\[
 f''(s)=-\frac{2\pi}{\sin(2\pi s)}\leq-2\pi.
\]

Consequently \(f(s)+\pi s^2\) is concave, including both endpoints by
continuity. Summing this fact proves, for \(a,b\in\mathcal P\) and
\(0\leq t\leq1\),

\[
 E((1-t)a+tb)\geq(1-t)E(a)+tE(b)
       +\pi t(1-t)\lVert a-b\rVert_2^2. \tag{1}
\]

Let \(a^*\) maximize \(E\) on \(\mathcal P\), and set
\(\Phi=E(a^*)\). In the actual geometric case,
\(\Phi=\operatorname{Vol}(Y_D)/(2\pi)\). Since the left side of (1),
with \(a=a^*\), is at most \(\Phi\), dividing by \(t>0\) and letting
\(t\downarrow0\) gives

\[
 \boxed{\quad E(b)\leq\Phi-\pi\lVert b-a^*\rVert_2^2.\quad} \tag{2}
\]

No derivative at a forced zero or at a singleton row is used. In particular
the maximizing assignment is unique even on a proper supported face.

## 2. Fixing selected triangles to their corner vertices

Choose a set \(J\) of distinct original triangles and an allowed ordinary
corner \(c(t)\) in each. Impose the additional constraints

\[
 a_t=v_t:=\tfrac12 e_{c(t)},\qquad t\in J.
\]

Write \(\mathcal P_J\) for the resulting face of \(\mathcal P\). If it is
nonempty, (2) proves the explicit bound

\[
 \max_{\mathcal P_J}E
 \leq\Phi-\pi\sum_{t\in J}\lVert v_t-a_t^*\rVert_2^2. \tag{3}
\]

If it is empty, its entropy maximum is \(-\infty\). The loss in (3) is
strict as soon as one chosen row was not already that singleton row at
the complete solution. Distinct rows make the displayed squared losses
additive; their shared face constraints remain in force.

There is an exact shared-radius dual formulation. Write \(h_f=\log l_f\)
for ordinary faces and retain protected zeros by deleting their allowed
corners. With the same half-degree triangle function \(Q\), put

\[
 B_J(h)=\sum_{t\notin J}Q((e^{h_f})_{f\in t})
            +\tfrac12\sum_{t\in J}h_{c(t)}-\sum_f h_f. \tag{4}
\]

Then

\[
 \inf_{h\in\mathbb R^{F_{\mathrm{ord}}}} B_J(h)
       =\max_{\mathcal P_J}E. \tag{5}
\]

Here the right side has value \(-\infty\) when infeasible; positive
minimizing radii need not exist. To verify (5), take the product of all
remaining compact triangle simplexes and the selected singleton rows,
let \(A\) be its original face-incidence map, and define
\(H(d)=\max_{Aa=d}E(a)\). Its hypograph is closed and convex, because
the domain is compact and \(E\) is continuous and concave. Weak duality
follows directly from the local Legendre formula. Strict separation of
\((\mathbf1,H(\mathbf1)+\varepsilon)\) from that hypograph gives an affine
majorant of height at most \(H(\mathbf1)+\varepsilon\) at \(\mathbf1\).
The separating coefficient of the vertical coordinate is positive:
it is nonnegative by downward closure, and if it were zero the feasible
point with the same face coordinate would contradict strict separation.
Normalizing that coefficient to one produces (4). Let
\(\varepsilon\downarrow0\). When \(\mathbf1\) is outside the compact
incidence image, separation in face coordinates and scaling the
separator sends (4) to \(-\infty\).

## 3. What this resolves in the one-sided envelope

For a LEFT port \((x,b,c,y)\), its term

\[
 Q(x,b,y)+\tfrac12\log c
\]

is exactly (4)'s local expression when the original \((x,c,y)\) triangle
is fixed to its \(c\)-corner vertex. At the actual complete packing with
\(c>0\) and \(x+y>0\), this triangle has at least two positive weights,
so its maximizing row is not that vertex. Thus (3) gives a strict,
explicit capacity loss for any fixed nonempty collection of these
triangle restrictions, with the original common face constraints.
The reflected statement applies to RIGHT ports.

This proves a statement about the specified comparison capacities. It
does not bound the full LEFT polynomial by that one comparison: the
[proved weighted envelope](actual_global_left_weighted_spectral_envelope.md)
also has the branch \(\log c\). A pointwise maximum of the two branches
does not permit each branch to choose its own Cauchy radii before the
original coefficient is extracted. An additional finite comparison,
or a bound for their convex mixtures with the same face constraints,
is still necessary for a general full-invariant theorem.

## Validation

The proof is analytic: scalar differentiation, strong concavity on the closed simplex, and finite convex separation. No finite-width experiment is used to infer (2), (3), or (5). No comparison with the complete one-sided envelope is supplied.