# Compactness over a strict real-angle base and the corner subgradient

Private written proof, 17 November 2026.

Regular fiber minima have uniformly bounded angular heights on every
compact subset of the strictly feasible real-angle base. No bound on
their real periods is an assumption. A uniformly strict section of the
fibers supplies the required supporting comparisons.

For regular fibers, compact-base bounds already follow by combining
convex difference quotients for the reduced energy with the archived
bounded-period theorem. The refinement here is a direct, explicit
bound for every supporting pair, including at nonregular fibers,
together with the exact corner subdifferential.

The closed fiber minimum is unique and continuous throughout that base,
including its nonregular part. Finite convex supporting multipliers
therefore extend the variational graph there. They do not automatically
extend the original geometric graph: at a square corner the convex
subgradient satisfies an inequality, whereas a limit of genuine
positive square covectors satisfies its equality.

The resulting compact boundary and action gap are classical statements.
A corner is not thereby an allowed boundary of the original source
cycle, and no quantum estimate or geometric-cycle coefficient is inferred.

## 1. Original body, fibers, and a uniform strict section

Fix a finite connected original circle tree, a nonempty selected set
\(S\), and all edges incident to \(S\), counted once. Every selected
vertex has an incidence. Outside angles are complete. Retain the original
fixed real powers \(n_v\) and fixed positive charges \(c_v\).
Write \(m\) for the number of included edges and use
\[
 t_v=s_v+ih_v,\qquad r_{v,e}=k_{v,e}+ig_{v,e},\qquad
 \rho_v(s,g)=\sum_{e\ni v}g_{v,e}-n_vs_v/2,\qquad
 \rho^0_v=-\pi c_v .
 \tag{1}
\]
Outside real angles are zero. The ambient positive body \(X\) has
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi \qquad(e=vw).
 \tag{2}
\]
Its closure is compact. The original square coordinates are
\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,& A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,& y_Q&=g_{v,e}/2-s_w/4 .
 \end{aligned}
 \tag{3}
\]
Use precisely the original convex energy
\[
 \mathcal E=4\sum_e(E_{P,e}+E_{Q,e}),\qquad
 0\le\mathcal E\le E_{\max}:=4mG_{\rm Cat}.
 \tag{4}
\]
There is no outside imaginary-work term.
The complete direct sources prove continuity on the closed body,
strict positive square Hessians in its interior, and the differential
\[
 4\,d(E_{P,e}+E_{Q,e})
  =k_{v,e}\,ds_v+k_{w,e}\,ds_w
       +h_{v,e}\,dg_{v,e}+h_{w,e}\,dg_{w,e}.
 \tag{5}
\]

The strictly feasible real-angle base is the explicit convex open set
\[
 D=\left\{s:\ |s_v|<\pi,\quad
 |n_vs_v-2\pi c_v|+\sum_{e=(v,w)}|s_w|<\pi d_v
 \quad(v\in S)\right\}.
 \tag{6}
\]
Outside summands in (6) are zero. Assume \(D\ne\varnothing\).
Define the closed fiber and its value by
\[
 \mathcal P_s=\{(s,g)\in\overline X:\rho=\rho^0\},\qquad
 e(s)=\min_{\mathcal P_s}\mathcal E,\qquad s\in D .
 \tag{7}
\]
The regular locus \(D_{\rm reg}\) consists of the points whose fiber
minimum lies in \(X\).

There is an explicit continuous strict section. Put
\[
 a_{v,e}(s)=\frac{\pi-|s_w|}{2},\qquad
 A_v(s)=\sum_{e\ni v}a_{v,e}(s),\qquad
 b_v(s)=n_vs_v/2-\pi c_v ,
 \tag{8}
\]
and set, at every selected incidence,
\[
 \bar g_{v,e}(s)=b_v(s)\frac{a_{v,e}(s)}{A_v(s)}.
 \tag{9}
\]
Set all outside incidence variables to zero. Equation (6) is exactly
\(|b_v|<A_v\); hence (9) is strictly feasible and has the required
selected sums. For every compact \(K\Subset D\), its square coordinates
have a common margin
\[
 \alpha=\min_{\substack{s\in K\\\text{all square coordinates}}}
                 \{\pi/4-|\text{coordinate of }\bar z_s|\}>0,
 \qquad \bar z_s=(s,\bar g(s)).
 \tag{10}
\]
One may first enlarge \(K\) slightly inside \(D\) when a buffer is
needed. The section need not be analytic; its continuity and uniform
strictness are sufficient.

## 2. Every strict-base fiber has a unique continuous minimum

**Lemma 1.** Each fiber in (7) has a unique minimum \(z(s)\).
Every square factor of \(z(s)\) is either interior or a corner.
The maps \(s\mapsto z(s)\) and \(s\mapsto e(s)\) are continuous on \(D\).

**Proof.** Existence follows from compactness. Join a proposed
minimum to \(\bar z_s\) while keeping the real angles fixed.
The original square calculation gives derivative \(-\infty\)
on entering an open side, finite derivatives on entering a corner,
and finite derivatives at an interior factor. Thus no open-side
factor can occur at a minimum.

If two distinct minima existed, their segment would consist of
minima by convexity. The linear square map (3) is injective on the
fiber variables, so some square factors differ. A factor with an
interior endpoint, or a pair of opposite corners, gives a segment
through the square interior and strictly positive second derivative.
Two distinct adjacent corners instead give an open-side midpoint,
already excluded. This is the same strict-convexity argument as for
the full charged minimum, applied on the fixed fiber.

Here is the parameter-continuity point explicitly. Let \(s_\ell\to s\)
in \(D\), and let \(z\in\mathcal P_s\). Mix \(z\) with \(\bar z_s\)
by a coefficient \(\epsilon_\ell\downarrow0\) satisfying
\(|s_\ell-s|=o(\epsilon_\ell)\). The mixture has a square margin
at least a fixed multiple of \(\epsilon_\ell\). Change its selected
real angles to \(s_\ell\), and, at one chosen incidence of each
selected vertex, add \(n_v(s_{\ell,v}-s_v)/2\). This keeps
\(\rho=\rho^0\). The changes of all square coordinates are
\(O(|s_\ell-s|)\), so the resulting point belongs to
\(\mathcal P_{s_\ell}\) for large \(\ell\), and tends to \(z\).

Any subsequential limit of \(z(s_\ell)\) is feasible at \(s\).
The preceding approximation of a minimum at \(s\), together with
continuity of \(\mathcal E\), proves that this limit is a minimum
at \(s\). Uniqueness identifies it with \(z(s)\), proving both
continuity assertions. \(\square\)

The function \(e\) is convex, by taking convex combinations of fiber
minima. On \(D_{\rm reg}\), the already proved regular-fiber theorem
gives the original analytic graph
\[
 t(s)=s+ih(s),\qquad
 P(t(s))=u(s)-\pi i c,\qquad u(s)=\nabla e(s),
 \quad P_v=\sum_{e\ni v}r_{v,e}-in_vt_v/2 .
 \tag{11}
\]
No equality \(D_{\rm reg}=D\) is used.

## 3. Bounded supporting multipliers without a period assumption

It is useful to vary the affine right sides temporarily. Let
\[
 V(s,\rho)=\min\{\mathcal E(s,g):(s,g)\in\overline X,\
                                      \rho(s,g)=\rho\}.
 \tag{12}
\]
This notation is used wherever the fiber is nonempty. The section
(9), with small changes of one incidence per selected vertex, shows
that \(V\) is finite on an open neighborhood of
\(\{(s,\rho^0):s\in K\}\), for every \(K\Subset D\).
It is a convex function there. Its epigraph supporting-hyperplane
theorem therefore gives a finite subgradient
\((u,h)\in\partial V(s,\rho^0)\) at every such point.
Equivalently, for every ambient \(y\in\overline X\),
\[
 \mathcal E(y)\ge e(s)
     +u\cdot(s(y)-s)+h\cdot(\rho(y)-\rho^0).
 \tag{13}
\]
Indeed a subgradient of the marginal value gives (13) because
\(V(s(y),\rho(y))\le\mathcal E(y)\). Conversely, minimize
(13) in each nonempty fiber to obtain the subgradient inequality.
This also explains why the supporting inequality is ambient:
the comparison point need not obey the original charged rows.

For completeness, finite supporting vectors here do not require a
boundary differentiability assumption. A convex function finite on
an open neighborhood has a supporting hyperplane to its epigraph
with nonzero vertical coefficient; local finiteness excludes a
vertical support. Normalize that coefficient to obtain the
subgradient. To verify the restriction rule, let
\(u\in\partial e(s)\). The finite directional derivative
\(p(a,b)=V'((s,\rho^0);(a,b))\) is sublinear and satisfies
\(u\cdot a\le p(a,0)\). The finite-dimensional dominated-extension
theorem extends \(u\cdot a\) to \(u\cdot a+h\cdot b\le p(a,b)\).
The convex directional-derivative criterion then gives
\((u,h)\in\partial V(s,\rho^0)\), which is exactly (13).

Put
\[
 n_{\max}=\max_{v\in S}|n_v|,\qquad
 \beta=\frac{\alpha}{1+n_{\max}} .
 \tag{14}
\]

**Theorem 2.** For every \(s\in K\Subset D\), every supporting pair
in (13) obeys the explicit bounds
\[
                 \|h\|_1\le E_{\max}/\alpha,\qquad
                 \|u\|_1\le E_{\max}/\beta.
 \tag{15}
\]
At a regular fiber these are bounds for the actual angular heights
and real primitive periods in (11).

**Proof.** Start at the uniformly strict section \(\bar z_s\),
not at the possibly boundary minimum \(z(s)\). Choose one incidence
at each selected vertex and add
\(\alpha\,\operatorname{sgn}(h_v)\) to it, changing no real angle.
Each square coordinate changes by at most \(\alpha/2\):
opposite endpoint changes enter its two coordinates separately.
The new point \(y\) is in \(X\), and
\[
 s(y)=s,\qquad
 \rho_v(y)-\rho^0_v=\alpha\,\operatorname{sgn}(h_v).
 \tag{16}
\]
Use (13), \(e(s)\ge0\), and \(\mathcal E(y)\le E_{\max}\).
The \(u\)-term is exactly zero. This proves the first estimate
in (15) without any preliminary bound on \(u\).

For the second estimate again start at \(\bar z_s\). Change
\(s_v\) by \(\beta\,\operatorname{sgn}(u_v)\) and change its
chosen incidence by \(n_v\beta\,\operatorname{sgn}(u_v)/2\).
Then \(\rho(y)=\rho^0\). Equation (3) bounds each square-coordinate
change by
\[
                  \beta(1+n_{\max})/4=\alpha/4.
 \tag{17}
\]
Thus \(y\in X\). The \(h\)-term in (13) is now exactly zero,
and \(\beta\|u\|_1\le\mathcal E(y)-e(s)\le E_{\max}\).

At a regular fiber the original differential (5), its incidence
stationarity, and the fixed affine rows give precisely
\(d\mathcal E=u\cdot ds+h\cdot d\rho\). Hence its actual
period/height pair is a supporting pair in (13), proving the
last assertion. \(\square\)

In particular \(e\) is locally Lipschitz on all of \(D\), and
its subgradients are uniformly bounded on compact subsets.
This regular compact-base implication can also be recovered from
the prior results: if \(s\pm r e_i\in D\) uniformly on \(K\), then
\(0\le e\le E_{\max}\) and convex difference quotients give
\(|u_i|\le E_{\max}/r\) at every regular \(s\in K\). The archived
bounded-period theorem then bounds the heights. The direct argument
above instead gives explicit bounds for every full supporting pair,
without first assuming regularity or choosing a period bound.

## 4. Compact genuine corner limits and their action

Fix \(K\Subset D\), and choose \(\epsilon>0\) with
\(|s_v|\le\pi-\epsilon\) on \(K\). Theorem 2 bounds all actual
heights at its regular points by \(H=E_{\max}/\alpha\).
Consequently the tangents are bounded. More explicitly,
\[
 \left|\tan\frac{s+ih}{2}\right|^2
       =\frac{\cosh h-\cos s}{\cosh h+\cos s}
       \le\max\{1,\cot^2(\epsilon/2)\}.
 \tag{18}
\]
The original branch identity
\[
 \sinh r_{v,e}=\tan(t_v/2)\cos(t_w/2),\qquad
                         |\Im r_{v,e}|<\pi/2
 \tag{19}
\]
then bounds every real return, since
\(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\).
The square covectors are bounded by the exact linear identities
\[
 x_P=k_{v,e}/2-h_w/4,\quad x_Q=k_{v,e}/2+h_w/4,\qquad
 B_P=h_v/4+k_{w,e}/2,\quad B_Q=h_v/4-k_{w,e}/2 .
 \tag{20}
\]
Outside heights are zero. All these bounds depend only on the
fixed data and \(K\).

**Corollary 3.** The graph of the actual \(t\), returns and square
covectors over \(K\cap D_{\rm reg}\) has compact closure. Along
any sequence \(s_\ell\to s_*\in K\), the primal data converge to
the unique \(z(s_*)\). Every convergent subsequence of the lifted
data satisfies the unchanged matching, charge and real-period rows.
If \(s_*\notin D_{\rm reg}\), at least one square is a corner,
and every noninterior square is a corner with
\[
 (A,y)=(\varepsilon_A\pi/4,\varepsilon_y\pi/4),\qquad
 U=\varepsilon_Ax>0,\quad W=\varepsilon_yB>0,\qquad
                       \sinh(2U)\sinh(2W)=1 .
 \tag{21}
\]

**Proof.** Compactness follows from (15),(18)--(20).
Lemma 1 identifies the primal limit. The linear rows pass to
the limit without a branch reset. A regular point has the
already established analytic graph, so a limit over a nonregular
point has at least one boundary factor. Lemma 1 excludes open
sides. At a corner use the exact square identity
\[
                  \sinh(2x)\sinh(2B)=\sin(2A)\sin(2y).
 \tag{22}
\]
The signs of the interior \(x,B\) agree with \(A,y\). Their finite
limits and (22) give (21), including strict positivity of both
signed limits. \(\square\)

The corollary does not assert that every point of
\(K\setminus D_{\rm reg}\) is approached by regular points, or
that the lifted limit above a given corner is unique.

Suppose now an original positive charged filling center is supplied.
Let its assignment be \(z_0\), its base point \(s_0\), and set
\[
 E_0=\mathcal E(z_0),\qquad
 M_0=mM_\infty-E_0/\pi,\qquad M_\infty=4G_{\rm Cat}/\pi .
 \tag{23}
\]
It is the unique global minimum on the original charged polytope
\(\overline{\mathcal P}_c=\{\rho=\rho^0\}\cap\overline X\).
Its strict boundary gap is
\[
 \Delta=\min_{\partial\mathcal P_c}\mathcal E-E_0>0.
 \tag{24}
\]
The action on every regular fiber graph, with its original
logarithms, is exactly
\[
 \Re\Phi_c(t(s))=mM_\infty-e(s)/\pi,\qquad
 \Phi_c=\sum_e\psi(t_v,t_w)+\frac{i}{4\pi}\sum_v n_vt_v^2
                                      -i\sum_v c_vt_v .
 \tag{25}
\]
Thus every genuine nonregular limit in Corollary 3 has limiting
action at most \(M_0-\Delta/\pi\). This is uniform; the limit
of the real action is determined by the primal fiber even if
its limiting covectors are not unique.

More generally, for every open neighborhood \(U\) of \(s_0\)
and every \(K\Subset D\) with \(K\setminus U\ne\varnothing\),
\[
       \delta_{K,U}:=\min_{s\in K\setminus U}\{e(s)-E_0\}>0.
 \tag{26}
\]
Continuity gives the minimum, and equality would imply
\(z(s)=z_0\), hence \(s=s_0\), which is excluded.
All genuine graph points and limits over this compact set
therefore have action at most \(M_0-\delta_{K,U}/\pi\).
This applies in particular to the component containing the center.

## 5. The finite convex extension is larger than sharp corner geometry

The multipliers in Theorem 2 exist at every fiber over \(D\).
It is important to compute what this says at a single corner.
Extend the original square energy by \(+\infty\) outside its
closed square. At the corner
\((A,y)=(\varepsilon_A\pi/4,\varepsilon_y\pi/4)\), write a candidate
covector as \((\varepsilon_A U,\varepsilon_y W)\).

**Proposition 4.** Its exact convex subdifferential is
\[
 \boxed{\qquad U>0,\quad W>0,\quad
                         \sinh(2U)\sinh(2W)\ge1.\qquad}
 \tag{27}
\]
The equality part is the sharp finite-gradient limit curve (21).
Strict inequality gives additional genuine supporting covectors.

**Proof.** The original corner directional derivative along
\[
 A(r)=\varepsilon_A(\pi/4-ar),\qquad
 y(r)=\varepsilon_y(\pi/4-br),\qquad a,b>0,
\]
is
\[
 -\frac12\{a\,\operatorname{arsinh}(b/a)
                  +b\,\operatorname{arsinh}(a/b)\}.
 \tag{28}
\]
For a convex function, a covector is a subgradient exactly when
its pairing with every admissible direction is at most the
one-sided directional derivative. Directions along a side follow
by limits; their energy derivative is zero. Hence the condition is
\[
 Ua+Wb\ge\frac12\{a\,\operatorname{arsinh}(b/a)
                         +b\,\operatorname{arsinh}(a/b)\}
                         \quad\text{for all }a,b>0.
 \tag{29}
\]
The limits \(b/a\to0,\infty\) first give \(U,W\ge0\).
Neither can be zero: for example, with \(U=0\), divide by \(b\)
and let \(b/a\downarrow0\); the right side diverges.

For \(U>0\), the equality curve in (27) is
\[
                   W=f(U)=\tfrac12\log\coth U.
 \tag{30}
\]
It is decreasing and strictly convex, with
\(f'(U)=-1/\sinh(2U)\). Parametrize it by
\[
 U(r)=\tfrac12\operatorname{arsinh}r,\qquad
 W(r)=\tfrac12\operatorname{arsinh}(1/r),\qquad r>0.
 \tag{31}
\]
For fixed \(a,b>0\), the minimum of \(aU+b f(U)\) occurs
where \(r=b/a\), and is precisely the right side of (29).
Thus the epigraph in (30) satisfies all of (29).
Conversely, a point below this graph violates its positive-normal
tangent support at that \(U\). This proves equivalence with (27).
The directional criterion also proves the global subgradient
inequality on the closed square, not only a local test.
Finally (31) is approached by genuine interior square gradients
with corner-distance ratio \(b/a=r\), as in (28).
This identifies its equality part with the sharp limit curve.
\(\square\)

For instance \(U=W=1\) is a finite supporting covector with
strict inequality in (27); it cannot be the finite gradient
limit of this corner along positive squares.
Accordingly finite convex multipliers supplied by (12)--(15)
are not automatically original corner shapes or matched limiting
period branches. The required equality is extra information.
The note asserts no failure of its existence for a particular
fiber; it proves that the convex subgradient condition alone
does not provide it.

## 6. What this supplies for a relative-contour construction

Over a compact strict base, the center component cannot escape
through unbounded angular heights or real periods. Its genuine
interior-base exits are compact sharp corners and have the
strict calibrated action gap (24). This is stronger than
the bounded-period theorem's stated hypothesis, although its regular
compact-base consequence already follows by the convex
difference-quotient argument just explained.

It still does not identify the closure of that graph with the
original integration class. In particular:

* an original angular endpoint or wire seam is a prescribed
  relative face, whereas a sharp corner in (21) is not;
* compact lifted data do not by themselves provide a unique
  corner continuation or a bounded stationary-wire chart;
* the full convex subgradient extension includes (27)'s
  nonsharp covectors and cannot simply be used as that continuation;
* reaching the boundary of \(D\) is outside the compact strict-base
  estimate, and all source poles, detours and remaining faces
  must still be retained.

Thus (25)--(26) are bounds for the original classical action on
genuine graph limits. They are not upper bounds for the canonical
quantum kernel or for a corner current. A source-preserving
relative-chain adapter and its estimate remain separate.

## Complete direct sources and author procedure

* [Original convex variation](research_positive_filling_convex_variation.md),
  SHA256 2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0:
  original square energy, exact differential, strict feasibility,
  open-side and corner derivatives, and unique full minima.
* [Reduced-angle inverse-period graph](research_reduced_angle_inverse_period_graph.md),
  SHA256 9575d0231700e49e46ddea42c989921ce23adaafaa6e81b4f4b83c16f227f0af:
  original fixed fibers, explicit base, regular graph and exact
  calibrated action, with the earlier low-energy collar scope.
* [Finite real-period compactness](research_real_period_image_compactness.md),
  SHA256 8ecdecc2c71e8a47a83fe60986ed618abaa926937920f376abebed779fb0c37e:
  energy bound, original return and square identities, sharp finite
  corner normalization and the retained source-relative boundary.

All three complete texts were read in this author sequence and
their directly used implications checked. Only written mathematics,
source reads and metadata hashes were used. No mathematical programs,
tests, numerical evaluations or builds were run. Frozen notes and
public manuscripts are unchanged.
