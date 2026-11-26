# The original five-vertex three-crossing chain

Research proof, 4 November 2026. Completed source artifacts and frozen
manuscripts are unchanged.

Closing the actual two-vertex cap against the actual three-vertex cap
gives a nonzero leading coefficient for the original five-vertex word.
The critical wire is certified with its complex displacement retained;
a bound using only the separate gradient magnitudes is not needed.
The proof includes both ordinary outside variables, their whole real
periods and a quadratic complex strip. It concerns the original marked
source; knot applications retain the separate component conditions.

## 1. Actual sources and the statement

Put \(A_N=JM^3\), \(x_h=1/6+i\log2/(2\pi)\), and
\[
 F_{1,N}(x,w)=v(w)^TA_N^2h(x),\qquad
 F_{2,N}(x,w)=v(w)^TA_N^3h(x),\qquad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad K=|k_0|.
 \tag{1}
\]
These are the undeleted original finite sources. Use their calibrated
phases \(S_1,S_2\), nonzero amplitudes \(a_1,a_2\), and centers
\(M_i=\Re S_i(x_h,-2)\). The
[quantified two-vertex theorem](research_three_prepared_cap_quantified_source.md)
and [three-vertex entrance theorem](research_three_first_entrance_real_extension.md)
give their uniform holomorphic packets on a neighborhood of
\(|x-x_h|\le R=1/200\), with a small fixed ordinary outside-color
neighborhood. Their original carriers and powers are
\[
 F_{1,N}=C_{N,3}\kappa N^{-1}a_1e^{NS_1}(1+O(N^{-1})),
 \qquad
 F_{2,N}=C_{N,3}\kappa^2 N^{-1}a_2e^{NS_2}(1+O(N^{-1})).
 \tag{2}
\]
The exact all-level cardinal identity and \(A_N^T=A_N\) give
\[
 Z_{5,N}(w_L,w_R):=
 N\int_{x_h-1/2}^{x_h+1/2}F_{1,N}(x,w_L)F_{2,N}(x,w_R)\,dx
                 =v(w_L)^TA_N^5v(w_R).
 \tag{3}
\]
This is the bilinear source identity, with no complex conjugation and
no replacement of an ordinary boundary by a Fourier endpoint.

**Theorem 1.** On a fixed ordinary-color neighborhood of \((-2,-2)\),
\[
 Z_{5,N}(w_L,w_R)=C_{N,3}^2\kappa^3 N^{-3/2}
       a_5(w_L,w_R)e^{N\Xi_5(w_L,w_R)}(1+O(N^{-1})),
 \qquad a_5(-2,-2)\ne0.
 \tag{4}
\]
The error is uniform and holomorphic, including every fixed ordinary
derivative and both level parities. At completeness,
\[
 2\pi\Re\Xi_5(-2,-2)=\operatorname{Vol}(M_5),
 \qquad
 \lim_{N\to\infty}\frac{2\pi}{N}\log|Z_{5,N}(-2,-2)|
                       =\operatorname{Vol}(M_5),
 \tag{5}
\]
where \(M_5\) is the original marked partial filling with its two
outside ends complete. This does not by itself identify a knot closure.

## 2. The correlated actual critical wire

Write \(t_1,\ldots,t_5\) for the original positive geometric
angles, with \(t_0=t_6=0\). The certificate verifies the actual
five-complex-variable system
\[
 3t_j+2i\left[
 \operatorname{asinh}\{\tan(t_j/2)\cos(t_{j-1}/2)\}
 +\operatorname{asinh}\{\tan(t_j/2)\cos(t_{j+1}/2)\}\right]
                           =2\pi,\qquad 1\le j\le5.
 \tag{6}
\]
It uses a single complex Newton self-map with rational centers and a
fixed rational preconditioner. The five closed disks have radius
\(10^{-23}\); their rectangular enclosures are used only to bound
the derivatives on those disks. All row contractions are below \(1/4\)
and all self-map margins are positive. The disks lie in the established
geometric rectangle \(1.3<\Re t<1.82\), \(.82<-\Im t<1.21\).
The rational centers are exactly those of the length-five reference
in the [all-length chamber theorem](research_three_chain_geometric_chamber.md).
That theorem places its positive geometric root within
\(\varepsilon=8/(3\cdot10^{25})\) in each real coordinate.
Its complex-coordinate distance is less than \(2\varepsilon<10^{-23}\),
so the known original root belongs to this new Newton polydisk.
Uniqueness of the fresh self-map identifies the two roots. This fixes
the positive solution and its full logarithmic lifts, without selecting
a different exponentiated or local branch.

Its original wires are
\[
 x_j=\frac1{2\pi}\arccos
 \frac{1-\cos t_j\cos t_{j+1}}{2+\cos t_j+\cos t_{j+1}},
 \quad 1\le j<5,
 \qquad z_*=x_2-x_h.
 \tag{7}
\]
The selected inverse cosine has positive imaginary part. Outward
arithmetic gives
\[
 \begin{split}
 z_*&\in(.0026975971863,.0026975971865)
       +i(-.0023808477168,-.0023808477165),\qquad |z_*|<.0036<R,\\
 x_1,x_4&\in(.17783,.17784)+i(.10083,.10084),\qquad
 |x_3-x_h|<R.
 \end{split}
 \tag{8}
\]
The certificate also checks every original cap, retained index and
logarithm branch in the
[common source chamber](research_three_chain_geometric_chamber.md).
The end wires lie inside the actual directed cap domain, the end
angles lie in \(1.5<\Re t<1.55\), \(.97<-\Im t<1\), and
all retained indices have real parts in \((.25,.45)\), heights
of modulus less than \(.02\) and the selected lower-left algebraic
branches. The independent replayer uses cosine-based returns and a
factored inverse-cosine lift instead of the author's direct tangent
and inverse-hyperbolic implementation.

This geometric point identifies an actual source critical point.
Cut the chain between vertices 2 and 3. The left two-vertex source
has fixed output \(x_2\); the right three-vertex source, read from
the right end, has that same output and its hidden prepared wire
\(x_3\). By (8) both outputs requiring the prepared packet are
inside their true disks. The exact open-chart identities of the
[action calibration](research_three_chain_action_volume_calibration.md)
identify the source and original angular critical equations, with
their unreset logarithmic lifts. Both source branches and the geometric
subsystems lie in the convex chamber with accretive negative Hessian.
The gradient is injective there, so their stationary eliminations
agree. The remaining original wire equation is exactly
\[
 U'(z_*)=0,\qquad
 U(z)=S_1(x_h+z,-2)+S_2(x_h+z,-2).
 \tag{9}
\]
This conclusion uses the original branch identities and uniqueness,
not a numerical residual of a guessed effective phase.

## 3. The central contour and the actual action normalization

The proved phase estimates are
\[
 |S_1''/k_0+\sqrt{21}|<\tfrac12,
 \qquad |S_2''/k_0+\sqrt{21}|<\tfrac9{50}
 \quad (|z|\le R).
 \tag{10}
\]
The first is the actual seed estimate in
[Proposition 3 of the phase-class proof](research_three_phase_graph_transform.md#4-the-actual-prepared-phase-is-in-this-class),
not the smaller gradient class reached after later attachments.
Thus with \(D=2\sqrt{21}\), \(\beta=17/25\),
\[
                 |U''+k_0D|<\beta K,
                 \qquad -\Re U''>17.
 \tag{11}
\]
In particular (9) is the unique critical point in the disk.
For \(d_\pm=\pm R-z_*\), the correlated certificate proves
\[
 \begin{split}
 Q_\pm&:=\Re(k_0D d_\pm^2)-\beta K|d_\pm|^2
                                       >\frac3{20000},\\
 \pm\Re(k_0D d_\pm)-\beta K|d_\pm|&>\frac7{100}.
 \end{split}
 \tag{12}
\]
In fact \(Q_-\) is above \(.0002939\) and \(Q_+\) above
\(.0001529\). Their signs use the actual complex displacement (8).

Move only \([-R,R]\) to the two straight segments through \(z_*\),
with endpoints fixed. The whole V lies inside the source disk, where
both exact finite functions have their actual packets. By stationarity,
\[
 \Re U(z_*+s d_\pm)\le\Re U(z_*)-\tfrac12s^2Q_\pm,
                                      \qquad 0\le s\le1.
 \tag{13}
\]
Both endpoints therefore lose more than \(3/40000\).
The directions have opposite real signs and belong to opposite
Gaussian convergence sectors by (12); the orientation is the original
left-to-right one. No side or connector term is removed in this exact
fixed-endpoint holomorphic deformation.

The actual action must retain its center shift. From (9),
\[
 U(z_*)-U(0)=-z_*^2\int_0^1sU''(s z_*)\,ds,
 \qquad
 \Re\{U(z_*)-U(0)\}
 \ge\tfrac12\Re(k_0D z_*^2)-\tfrac12\beta K|z_*|^2
                                      >-\Delta,\quad
 \Delta=\frac{103}{10^6}.
 \tag{14}
\]
The outward lower bound before rounding is \(-.000102461276\).
No homogeneous value or sum of center rates replaces \(U(z_*)\).

On the real annuli \(R\le|t|\le W=.009\), both principal phases
exist. Their certified real curvatures exceed \(9.3\) each, so
\(-\Re U''>18.6\). Integrating (11) from \(z_*\) to the
two real endpoints and using the second line of (12) gives
\(\Re U'(-R)>0\), \(\Re U'(R)<0\). Hence the principal
product decreases outwards throughout these annuli and retains the
endpoint loss in (13). The first source's separate absolute error
is handled next; no relative packet is assumed for it on an annulus
where that error might dominate.

## 4. Every remaining original contribution

The established original real estimates are
\[
 \begin{split}
 |F_{1,N}(x_h+t,-2)|
 &\le CN^q\{e^{N[M_1+.0113|t|-4.65t^2]}+e^{1.9107N}\},
                                      &&|t|\le.02,\\
 |F_{1,N}(x_h+t,-2)|&\le CN^q e^{1.91115N},
                                      &&d_{\mathbb T}(t,0)\ge.02,\\
 |F_{2,N}(x_h+t,-2)|
 &\le CN^q e^{N[M_2+B-(3/2)v(t)^2]},
 &&v(t)=\min\{d_{\mathbb T}(t,0),.03\},\quad
 B=\frac{77}{10^6},
 \end{split}
 \tag{15}
\]
with \(M_1>1.9113\). The first two come from the
[wider original prepared-source theorem](research_three_prepared_cap_real_extension.md),
including its plateau and far-arc proof. The third is the sharper
raw bound in (17) of the
[original entrance theorem](research_three_first_entrance_real_extension.md).
All fixed ordinary derivatives obey the same exponential estimates.

For \(W\le|t|\le.02\), multiply the principal first term by
the third line, and compare with \(\Re U(z_*)>M_1+M_2-\Delta\).
Its loss is increasing with \(|t|\) and at \(W\) exceeds
\[
       6.15W^2-.0113W-B-\Delta=.00021645>.0002.
 \tag{16}
\]
The plateau in (15), wherever it is used, gives the separate loss
\[
                 .0006-B-\Delta=.000420>.0004.
 \tag{17}
\]
Finally the whole far period has loss at least
\[
             .00015+1.5(.02)^2-B-\Delta=.000570>.0005.
 \tag{18}
\]
The output cap \(.03\) only increases the far loss beyond \(.02\).
On \(R\le|t|\le W\), use the principal phases for the first
term and the raw second-source bound for the plateau. This is valid
because the same actual second source obeys both upper estimates.
Thus (13), the real-annulus comparison, and (16)--(18) exhaust the
entire original period in (3).

The central Gaussian gives (4), with
\[
 \Xi_5=U(z_*),\qquad
 a_5(-2,-2)=
 \frac{\sqrt{2\pi}\,a_1(x_h+z_*,-2)a_2(x_h+z_*,-2)}
      {\sqrt{-U''(z_*)}}\ne0.
 \tag{19}
\]
The square root has positive real part, by (11). The original measure
\(N\,dx\), two powers \(N^{-1}\) and one wire Gaussian give
\(N^{-3/2}\). The two actual carriers multiply to
\(C_{N,3}^2\kappa^3\). The absolute gaps prevent cancellation.
Both incoming words are already undeleted, so (3) needs no further
corner restoration.

Unrolling (9) identifies the assembled point with the original
five-chain geometry used in (6). The calibrated full complex identity
is the sum of the six original edge phases, the five original
three-crossing filling phases, and \(3i\gamma\). The last term
is purely imaginary and fixed by the open-chart calibration. Its
real part is the original marked volume divided by \(2\pi\),
proving (5) with its absolute constant.

## 5. The full ordinary outside boundary

**Theorem 2.** There are \(c_5,B_5,h_5>0\) such that, for all
real outside angles and \(|v|,|s|\le h_5\),
\[
 |\partial_{w_L}^{a}\partial_{w_R}^{b}
 Z_{5,N}(-2\cos(u+iv),-2\cos(r+is))|
 \le C_{a,b}N^{q_{a,b}}
 e^{N[M_5-c_5\{1-\cos u+1-\cos r\}+B_5(v^2+s^2)]},
 \quad M_5=\Re\Xi_5(-2,-2).
 \tag{20}
\]
The local packet (4) holds on a fixed ordinary outside neighborhood,
with all fixed ordinary derivatives.

*Proof.* Use Lemmas 1 and 2 of the
[outside-color theorem](research_three_chain_outside_boundary_decay.md).
On the entire central V, the actual sources have their complete-phase
upper profiles minus positive multiples of \(1-\cos u\) and
\(1-\cos r\), respectively. The retained source phases in (13)
therefore give the sum of these two deficits without a new action
comparison. The real principal terms have the same deficits, and
the sharper raw three-vertex bound in (15) retains its deficit as
in (9) of that theorem. Its uniform original corner error is far
below that profile and is absorbed by decreasing the constant.

The two-vertex plateau and far bound are uniformly valid for every
real outside color; no boundary loss is assigned to them prematurely.
Their strict complete losses (17)--(18), and any other complementary
loss, absorb a sufficiently small multiple of the two outside losses,
whose sum is at most four. Thus the actual full source (3) satisfies
\[
 |Z_{5,N}(-2\cos u,-2\cos r)|
   \le CN^q e^{N[M_5-d(1-\cos u+1-\cos r)]},\qquad d>0.
 \tag{21}
\]

The two incoming central packets already have fixed ordinary outside
neighborhoods. All complementary bounds used above are uniform for
real outside angles and concern original polynomials of degree at
most \(N-1\) in each outside variable. The Laurent-polynomial
maximum principle adds at most a linear height cost on a small
complex strip. Strict gaps (13), (16)--(18) therefore persist for
sufficiently small fixed complex outside parameters. The central
critical point, the opposite Gaussian sectors and the nonzero local
coefficient continue holomorphically. This proves the actual local
packet assertion, not just its complete-point jets.

Apply the same polynomial maximum principle to (21). Away from a
small real neighborhood of the complete point, a thin height strip
absorbs its linear cost into the real loss. Near the complete point,
the nonzero packet and separate evenness imply a strictly negative
real diagonal boundary Hessian. Holomorphic Taylor expansion then
gives a quadratic height cost. These two regions prove (20).
Cauchy estimates on ordinary-color circles of radius \(O(N^{-2})\)
retain all fixed derivatives, including both ramified endpoints.
This is exactly the two-region strip argument of Section 4 of the
outside-color theorem, now applied to the actual word \(A_N^5\).
\(\square\)

Consequently the homogeneous-path alternative in
[marked short-filling stability](research_three_chain_short_filling_stability.md)
also permits length five, with either uniform sign. Exact conjugation
gives the negative case and the same original-period argument. This
does not cover lengths three or four, arbitrary sign changes within
a component, or a general cofinite-assignment theorem.

## 6. Reproduction and scope

```sh
python3 experiments/certify_three_chain_five_closure.py --precision 256
python3 experiments/replay_three_chain_five_closure.py --precision 320
```

The [author](../experiments/certify_three_chain_five_closure.py) and
[record](../repro/results/research-three-chain-five-closure.json)
retain exact rational Newton data, the original geometric and source
branch inclusions, both correlated sectors and every scalar budget.
The [independent replayer](../experiments/replay_three_chain_five_closure.py)
uses an alternative return/derivative expression and inverse-cosine
lift, checks the full original Newton self-map and every recorded
domain, and verifies the exact source word, carrier and level power.
The actual packets, open-chart identification and contour proof are
the written dependencies; the checker alone does not establish a
knot interpretation or a whole arbitrary-length short-core theorem.
