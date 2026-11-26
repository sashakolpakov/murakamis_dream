# A quantitative quantum limit allowing short twists at large junctions

The number of branches incident to a crossing circle can supply part of
the estimate previously obtained by taking its twist number large.
This note proves the finite-sum limit under an explicit inequality in
those two integers. The [volume theorem](actual_all_circle_quantitative_volume.md)
combines it with the ordered octahedral decomposition and positive
filling path. The limiting action is therefore the volume of the
original knot complement throughout the stated class, including the
short coefficients permitted by the inequality.

## 1. Assertion and scope

Consider an actual reduced Conway operation tree in which every product
junction carries an original crossing-circle operator. Include ordinary
terminal crossing circles as degree-one vertices. The resulting circle
graph \(\mathcal T\) is a finite tree, with physical quarter-turn edges
and no bare junctions. Keep the ordered branches, orientations, knot pattern, primitive cut
and zero framing. For the literal construction defined in the
[volume theorem](actual_all_circle_quantitative_volume.md), the strict
angle condition follows inductively from the product intervals; it is
not a further restriction on these trees.

Let \(d_v\ge1\) be the graph degree of circle \(v\), and let \(n_v\in
\mathbb Z\) be its actual fixed crossing power. The graph degree \(d_v\)
is unrelated to the quantum degree \(N-1\). Put
\[
 \mathfrak S(\mathcal T,\mathbf n)
       =\sum_v\frac{d_v}{d_v^2+n_v^2}.
 \tag{1}
\]
The following conservative sufficient condition will be proved:
\[
                         \mathfrak S\le2^{-25}.
 \tag{2}
\]
It implies a nonzero first joint Fourier charge and the actual reduced
microscopic profile through both level parities, on every \(|s|\le R<1\).
The exponential rate is the real part of the explicitly continued
first-charge action. Conditions (1)–(2) are quantitative finite-action
conditions, not an assumption that this saddle dominates.

Short, even zero, crossing powers are permitted by this certificate.
Section 11 explains how the companion geometric proofs identify the
action with the actual knot volume under the same bound.
The graph and all powers are fixed before \(N\) tends to infinity.

The invariant in the conclusion is the reduced, zero-framed ADO polynomial \(F_N(M)\), normalized to one on the unknot. Its complete value is \(F_N(1)=K_N(K)\). Set \(q_N=e^{\pi i/N}\) and \(M=q_N^s\). The explicit elementary factors are
\[
H_N(s)=\frac{\sin(\pi s)}{N\sin(\pi s/N)},\qquad
A_N(s)=q_N^{a(D)s^2/2},\qquad a(D)=-w(D)-\sum_v n_v.
\]
Here \(w(D)\) is the writhe of the fixed original diagram. The [scalar calculation](actual_main_meridian_exact_scalar.md) specifies the same framing convention, including all orientation types. The critical action in the limit is defined in Sections 4 and 7.

## 2. Dependencies and where the old proof used longness

The dependencies are the current authoritative notes:

* [the exact crossing trace](actual_main_meridian_direct_crossing_trace.md), Sections 2–4 and 7:
  exact translated-grid trace, full crossing scalar, Fourier
  coefficients, normal limits and fixed-power polynomial bounds;
* [the finite sum over internal edge indices](actual_main_meridian_grouped_wire_packet.md), Sections 2 and 4–8:
  primitive lattice, canonical \(G_N\), finite cotangent currents
  and the saddle insertion rule;
* [the joint Fourier calculation](actual_main_meridian_joint_filling_transform.md), Sections 3–5:
  real-spectator telescoping and the exact coefficient of charge one;
* [bounds for the full polynomial traces](actual_main_meridian_source_bounds.md), Sections 1–4, with its cited
  full spectral-jet and Chebyshev folding bounds;
* [the crossing and framing scalar](actual_main_meridian_exact_scalar.md): the unchanged exact scalar
  identity for fixed integer powers.

These are mathematical inputs, not numerical diagnostics.
The [earlier source transfer theorem](general_original_source_long_filling_transfer.md) and
[the pretzel filling calculation](actual_pretzel_long_filling_charge_selection.md) use reciprocal-slope
implicit functions; the geometric source-regulator theorem uses a
neighborhood of the complete framed representation.

Longness enters the present published joint proof in four analytic
places: existence and charge ordering of a nearby critical branch;
a nonempty finite charge cutoff with a fixed tail loss; the angular
connectors; and comparison of the total critical drop with fixed
discarded-source losses. The geometric completion is a separate fifth
use. This proof replaces the four analytic uses in the all-circle class.

## 3. A graph-independent discarded-source gap

Use the fixed complete Newton basis \(e_k\), \(0\le k<N\), and write
\[
 J(x)=\int_0^x\log(2\sin\pi u)\,du,\quad
 g(x)=J(2x)-4J(x),\quad G_0=g(1/4).
 \tag{3}
\]
The physical turn on a covariant edge retains equal indices and the
actual factor \(\gamma_e(s)H_N(s)/W_k(s)\). This factor and its inverse
are bounded on any fixed \(|s|\le R<1\), including all indices.
Reference, pivot, framing and the single reduced-cut scalar are kept.

At a circle vertex the actual typed tensor is the prescribed version of
\[
                \phi_\sigma\!\left(R_\sigma^{n_v}
                                          \prod_{e\sim v}e_{k_e}\right),
                   \qquad \sigma=0,s,-s.
 \tag{4}
\]
The canonical polynomial of a fixed \(R_\sigma^{n_v}\) has polynomial
complete spectral-jet norm. Low \(e_k\) have norm rate \(g(k/N)\);
high \(e_k\) have polynomial norm, including their first normals.
Finite-degree Chebyshev folding and exact top-coefficient extraction
therefore give rate at most the sum of \(g\) over low incidences in (4).
The polynomial exponent can depend on the fixed valence and power.
This is the full carrier-normalized tensor, not a distinct-node trace.
Opposite-color types retain their explicit outside scalar.

Each physical edge has two incidences. The whole absolute rate is at
most \(2\sum_{\text{low }e}g(k_e/N)\), and the positive complete action is
\[
                          F_0=2|E(\mathcal T)|G_0.
 \tag{5}
\]
Retain the box \(k_e/N\in I=[1/5,3/10]\). Since
\[
 g'(1/4)=0,\qquad
 g''(x)=-4\pi/\sin2\pi x\le-4\pi,\qquad
 2[G_0-g(x)]\ge4\pi(x-1/4)^2,
 \tag{6}
\]
one low edge outside \(I\) loses at least \(\pi/100\). A high edge
loses \(2G_0\ge\pi/4\). Closed factorial bounds and polynomial state
counting consequently give a grouped scalar error
\[
          N^{A_{\mathcal T,\mathbf n,R}}
              e^{N(F_0-\eta_0)},\qquad \eta_0=\pi/200.
 \tag{7}
\]
This loss is independent of the tree size and the fixed powers;
prefactors and starting levels are not uniform in those data.
There are no bare-tensor replacement errors. No generic conversion
from a small spectral norm to a low/high coefficient cone is used:
the physical vertex trace (4) is bounded directly.

## 4. Exact edge action

The retained packet factorizes over physical edges. Apart from its
edge scalar, each factor is
\[
 K_N(t,u;s)=\sum_{k/N\in I}e_k(-2\cos t)e_k(-2\cos u)
                                      \frac{H_N(s)}{W_k(s)}.
 \tag{8}
\]
The canonical interpolation has phase
\[
 b(x,t)=\int_0^x\log(2\cos2\pi v+2\cos t)\,dv-2J(x),\qquad
 \psi(t,u)=\operatorname{stat}_x[b(x,t)+b(x,u)].
 \tag{9}
\]
All branches are continued from \(x=1/4,t=u=0\).
Writing \(c=\cos2\pi x\), the stationary equation gives exactly
\[
 c=\frac{1-\cos t\cos u}{2+\cos t+\cos u},\qquad
 \tan^2\pi x=\frac1{1+\tan^2(t/2)+\tan^2(u/2)}.
 \tag{10}
\]
Substitution \(z=\tan\pi v\) in \(b_t\) yields
\[
 \psi_t=-\pi^{-1}\operatorname{arsinh}(\tan(t/2)\cos(u/2)).
 \tag{11}
\]
For \(Q=\sqrt{1-\sin^2(t/2)\sin^2(u/2)}\),
\[
 \psi_{tt}=-\frac{\cos(u/2)}{2\pi\cos(t/2)Q},\qquad
 \psi_{tu}=\frac{\sin(t/2)\sin(u/2)}{2\pi Q}.
 \tag{12}
\]
The Hessian determinant is exactly \(1/(4\pi^2)\). Thus
\[
 \Psi(\boldsymbol\tau)=\sum_{\{v,w\}\in E}\psi(\tau_v,\tau_w)
 =F_0-\tfrac12\sum_va_v\tau_v^2+\mathcal E(\boldsymbol\tau),
                 \qquad a_v=d_v/(2\pi).
 \tag{13}
\]
In particular the diagonal curvature grows with graph degree.

## 5. An available complex packet and nonlinear bounds

Take \(r=1/4\). Formula (10) gives
\(|x(t,u)-1/4|<0.003\) on \(|t|,|u|\le r\):
\(|\tan(t/2)|<0.128\), hence
\(|c|\le2(0.128)^2/[2-2(0.128)^2]<0.017\), and
\(x=1/4-\arcsin(c)/(2\pi)\).

Here the radius is valid for the finite packet, not only its formal
action. Put \(A=b(x,t)+b(x,u)\). On \(\Re x\in I\),
\(|\Im x|\le1/50\), \(|t|,|u|\le1/4\),
\[
 A_{xx}=\sum_{\xi=t,u}
 \left[-\frac{2\pi\sin2\pi x}{\cos2\pi x+\cos\xi}
                                    -2\pi\cot\pi x\right],
 \qquad |A_{xx}|<44,\quad \Re A_{xx}<-12.
 \tag{14}
\]
For completeness, \(|\cos2\pi x|<0.338\),
\(|\cos\xi-1|<0.032\), \(|\sin2\pi x|<1.009\).
Also \(\Re\cot\pi x>0.72\), while the real part of the first
fraction without \(2\pi\) exceeds \(0.328\): its conjugated
numerator is at least \(0.95(0.655)-0.040(0.159)\) and its
squared denominator is at most \(1.37^2\).
These bounds imply (14).

Use a finite cotangent contour of height \(h=1/500\) for the
original integer sum. With \(X=\Re(x-x_*)\), \(Y=\Im(x-x_*)\),
Taylor's formula gives
\[
 \Re[A(x)-A(x_*)]\le-6X^2+44|XY|+22Y^2.
 \tag{15}
\]
On a vertical endpoint side, \(|X|\ge0.047\), \(|Y|\le0.005\);
the right side is below \(-0.002\). On a horizontal side its
maximum in \(X\) is at most
\((308/3)Y^2\le77/30000\), below the nonconstant cotangent-mode
loss \(2\pi h=\pi/250\). The constant-mode integral translates
to \(x_*\) with the same endpoint loss, and (14) gives a
nondegenerate Gaussian on its real tangent. All canonical \(G_N\)
arguments stay in regular bulk strips; no periodic normalization
of the interpolation has been changed.

Thus each exact edge sum has a nonzero analytic amplitude and the
usual uniform \(O_R(N^{-1})\) relative expansion on this disk,
with all midpoint offsets retained. Its leading factors and
\(-A_{xx}(x_*)\) never vanish. Multiplication gives the whole
packet expansion with phase (13), uniformly for the fixed tree.

Useful explicit nonlinear constants follow from (12). Let
\(\sigma=\sinh(r/2)\), \(k=\cosh(r/2)-1\),
\(C=(1-\sigma^4)^{-1/2}\). The normalized diagonal error is at
most \(2kC/(1-k)+C-1<1/50\), and the off-diagonal bound is
\(\sigma^2C\); their sum is below \(1/25\).
For example \(k<0.008\), \(\sigma<0.126\) prove these estimates.
Set \(\delta=1/50\), \(\varepsilon=1/25\). Edgewise summation gives
\[
 \left|\mathcal E_v/\tau_v\right|\le\delta a_v,\qquad
 \sum_w|\mathcal E_{vw}|\le\varepsilon a_v,\qquad
 |\mathcal E(\boldsymbol\tau)|
                      \le\tfrac\varepsilon2\sum_va_v|\tau_v|^2.
 \tag{16}
\]
The quotient extends at \(\tau_v=0\). For the first bound
integrate the diagonal Hessian error with other coordinates fixed.
The last bound uses \(2|zw|\le|z|^2+|w|^2\) on each edge, not
a dimension-dependent maximum-norm estimate.

## 6. A uniform raw angular Gaussian

For \(k/N\in I\) the exact product is
\[
 \frac{e_k(-2\cos t)}{e_k(-2)}
 =\prod_{j<k}\left(1-
          \frac{\sin^2(t/2)}{\cos^2((j+1/2)\pi/N)}\right).
 \tag{17}
\]
Put \(u=\sin^2(t/2)\) for real \(t\). The first
\(\lfloor N/5\rfloor\) factors have absolute value at most
\(1-\alpha_1u\), \(\alpha_1=2\sqrt5-4\); the remaining
at most \(N/10+1\) factors are bounded by
\(1+\alpha_2u\), \(\alpha_2=2\sqrt5/5\).
These follow by checking the two linear pieces of \(|1-u/c|\)
with \(c\ge\cos^2(\pi/5)\) and \(c\ge\cos^2(3\pi/10)\),
respectively. Therefore
\[
 \left|\frac{e_k(-2\cos t)}{e_k(-2)}\right|
 \le e^2e^{-\alpha N\sin^2(t/2)},\qquad
 \alpha=\frac{9\sqrt5-20}{25}>\frac1{250}.
 \tag{18}
\]
For complex \(t+iy\), \(|y|\le1\), one factor's squared modulus
is at most its real squared value plus \(18y^2\). Indeed its
denominator \(c>1/3\), its real absolute value is below two,
\(\cosh y-1\le y^2\), and \(|\sinh y|\le2|y|\).
The real linear majorants above are at least \(1/2\); consequently
the additional factor is at most \(e^{36y^2}\).
Since \(k\le3N/10\),
\[
 |e_k(-2\cos(t+iy))|
 \le e^2e_k(-2)
              e^{N[-\alpha\sin^2(t/2)+11y^2]}.
 \tag{19}
\]
Use \(\sin^2(t/2)\ge t^2/\pi^2\) for \(|t|\le\pi\).
Summing the positive edge references and retaining the bounded
edge insertions yields
\[
 |B_N(\mathbf t+i\mathbf y,s)|
 \le N^A\exp N\left[
  F_0-\frac1{400}\sum_va_vt_v^2+70\sum_va_vy_v^2\right].
 \tag{20}
\]
We used \(2\alpha/\pi>1/400\), \(22\pi<70\).
Endpoint translations \(O_R(N^{-1})\) affect only prefactors.

## 7. Critical branches without reciprocal-slope smallness

Set
\[
 b_v=n_v/(2\pi),\quad D_v=a_v-ib_v,\quad t_0=1/16,\quad
                   L_v=\lfloor t_0|D_v|\rfloor.
 \tag{21}
\]
Condition (2) implies \(|D_v|>32\) for all \(v\), so \(L_v\ge1\).
For real continuous \(0\le\ell_v\le L_v\), the critical equation is
\[
             D_v\tau_v=-i\ell_v+\mathcal E_v(\boldsymbol\tau).
 \tag{22}
\]
The right-hand map after division by \(D_v\) is a contraction
on the radius-\(1/4\) polydisk, with Lipschitz constant at most
\(\varepsilon\). Its image has radius at most
\(t_0+\delta/4<1/4\). Thus there is one analytic critical branch,
also when some \(n_v=0\).

Writing \(Q_v=\mathcal E_v/\tau_v\), the exact identity is
\[
                         \tau_v=-i\ell_v/(D_v-Q_v).
 \tag{23}
\]
For positive \(\ell_v\), \(\Im\tau_v<0\). With
\[
 \gamma_+=\frac{1+\delta}{(1-\delta)^2}=\frac{2550}{2401},
 \qquad
 \gamma_-=\frac{1-\delta}{(1+\delta)^2}=\frac{2450}{2601},
 \tag{24}
\]
one obtains
\[
 \gamma_-\frac{\ell_va_v}{|D_v|^2}
       \le-\Im\tau_v\le
 \gamma_+\frac{\ell_va_v}{|D_v|^2}.
 \tag{25}
\]
For \(\Phi_\ell=\Psi+\tfrac i2\sum b_v\tau_v^2-i\sum\ell_v\tau_v\)
and its stationary value \(\mathcal C(\ell)\),
\(\partial_{\ell_v}\Re\mathcal C=\Im\tau_v\). Integration in
the independent charges proves
\[
 \Re\mathcal C(\ell)\le\Re\mathcal C(\mathbf1)
  -\frac{\gamma_-}{2}\sum_v
             \frac{a_v}{|D_v|^2}(\ell_v^2-1),\quad\ell_v\ge1,
 \tag{26}
\]
\[
 F_0-\beta\le\Re\mathcal C(\mathbf1)\le F_0,\qquad
 \beta=\frac{\gamma_+}{2}\sum_v\frac{a_v}{|D_v|^2}
                                  =\pi\gamma_+\mathfrak S.
 \tag{27}
\]
Each positive-charge coordinate is nonzero and has modulus below
\(t_0/(1-\delta)<\pi/2\), so the actual factor
\(\prod\sin\tau_v\) is nonzero. On a real tangent the Hessian
has real part at most \(-(1-\varepsilon)\operatorname{diag}(a_v)\).
The Gaussian determinant is nonzero.

## 8. Infinite tails and connectors

Keep the exact full-normal charge coefficients
\[
 c_{\ell,N}(\sigma)=
 (-1)^{(N-1)(\ell-1)}U_{\ell-1}(\cos2\pi\sigma),\qquad c_{1,N}=1.
 \tag{28}
\]
Initially use formal parameter circles avoiding their removable
sine denominators, as in the current joint-transform proof.
Let \(A_0=1/400\) and choose
\[
                         y_v=A_0t_0a_v/|D_v|.
 \tag{29}
\]
With spectators real or on physical translated grids, the exponent
for this coordinate is bounded by
\[
 F_0-a_vt^2/400+|b_vty_v|-\ell y_v+70a_vy_v^2.
 \tag{30}
\]
After maximizing \(t\), the positive quadratic coefficient is
\(70a_v+100b_v^2/a_v\le100|D_v|^2/a_v\).
Since \(L_v+1>t_0|D_v|\), every omitted charge loses at least
\[
                  \tfrac12A_0t_0^2a_v
                              \ge1/(409600\pi).
 \tag{31}
\]
Further charges carry \(e^{-N(\ell-L_v-1)y_v}\).
The coefficient bound \(\ell e^{2\pi R'(\ell-1)}\) is absorbed
for large \(N\) at this fixed tree.

Original endpoint loss is \(\pi^2a_v/400\). The chirp, finite-charge
connector and imaginary Gaussian costs are bounded respectively
by \(\pi A_0t_0a_v\), \(A_0t_0^2a_v\), and
\(70A_0^2t_0^2a_v\), less than half that loss in total.
The zero-mode current obeys the same estimate. Exact telescoping
of physical functionals and finite real-integral approximants
therefore gives the finite-charge formula with (31). No spectator
uses another coordinate's complex filling contour.

Next restrict real angles to \([-\rho,\rho]^m\), \(\rho=1/8\).
The complement loses \(1/(51200\pi)\) by (20).
Translate this box to the imaginary part of its critical point.
On any connector write \(\tau_v=t_v-i v_v\), with
\(0\le v_v\le-\Im\tau_{\ell,v}\). These points stay in the
radius-\(1/4\) polydisk. From (16) and Young's inequality,
\[
 \Re\Phi_\ell(\mathbf t-i\mathbf v)\le
 F_0-\tfrac18\sum_va_vt_v^2+
 \sum_v\left[\tfrac{1+\varepsilon}{2}a_v+
       \frac{2b_v^2}{(3-4\varepsilon)a_v}\right]v_v^2
                                      -\sum_v\ell_vv_v.
 \tag{32}
\]
The last two sums are at most \(-\tfrac14\sum_v\ell_vv_v\),
because
\[
 \gamma_+\max\{(1+\varepsilon)/2,\;2/(3-4\varepsilon)\}<3/4.
 \tag{33}
\]
A connector face has some \(|t_v|=\rho\), and hence loss at least
\(1/(1024\pi)\). This retains the negative Fourier contributions
of all spectator coordinates instead of adding their imaginary
growth costs independently. The translated real box has uniformly
negative Hessian. Its translated horizontal integral has a relative
Gaussian expansion at its own critical point. After the connectors
are restored, the estimate for a nonminimal charge is its saddle
term plus \(O(\operatorname{poly}(N)e^{N(F_0-\eta)})\), with \(\eta\)
as chosen below. A connector need not be below that nonminimal
charge's much smaller critical action. It is below the first-charge
action, which is all that is required: (26) and this additive error
give strict first-charge dominance. Only the first charge is asserted
to have a relative asymptotic for the original contour.

## 9. The actual analytic conclusion

Allowing polynomial prefactors, all source, real-box and charge-tail
errors above have loss at least
\[
                              \eta=1/(819200\pi).
 \tag{34}
\]
The finite-sum contour errors have larger fixed edge losses from Section 5. Condition (2) gives
\[
                   \beta\le\pi(2550/2401)2^{-25}<\eta/2.
 \tag{35}
\]
Thus all discarded errors lie below the same nonzero first-charge
action. Only these fixed losses are compared with the total drop.
The charge-dependent gaps (26) are compared directly with that
filled action, not with the augmented reference.

The first coefficient (28) is exactly one for both parities.
The entire difference of physical traces and their finite-charge
approximation is holomorphic through the collisions. The maximum
principle gives the estimates on every \(|s|\le R<1\), including
actual constant and moving types, without assuming separate
removability of divided endpoint currents.

The unchanged primitive count gives final power \(N^{3/2}\).
All original crossing, mixed-reference, pivot and zero-framing
factors are retained exactly. The resulting reduced invariant has
\[
 \frac{F_N(q_N^s)}{F_N(1)}
       =A_N(s)H_N(s)(1+O_{\mathcal T,\mathbf n,R}(N^{-1})),
 \qquad
 \frac{2\pi}{N}\log|F_N(q_N^s)|
                  \longrightarrow2\pi\Re\mathcal C(\mathbf1),
 \tag{36}
\]
uniformly on the disk, and is nonzero there for sufficiently large
levels. The edge insertion rule also gives its cotangent correction
at this same continued wire saddle. Section 11 supplies its geometric
volume and cusp interpretation.

## 10. Explicit analytic nonvacuity

For a star with center degree \(B\), arbitrary fixed center power
\(n_0\), and leaf powers \(|n_j|\ge B\),
\[
 \mathfrak S=\frac{B}{B^2+n_0^2}
                    +\sum_{j=1}^B\frac1{1+n_j^2}<2/B.
 \tag{37}
\]
Thus \(B\ge2^{26}\) suffices, even for short or zero \(n_0\).
For two adjacent centers each of degree \(B+1\), with \(B\) leaves
at each and every leaf power of magnitude at least \(B\), both center powers may be arbitrary fixed short
integers: \(\mathfrak S<4/B\), so \(B\ge2^{27}\) suffices.
The large constants reflect deliberately coarse global estimates.
The general quantity (1) allows any number and arrangement of
short high-degree circles within the sum budget.

There is also an intrinsic interpretation at the original complete
auxiliary cusps. The [marked peripheral calculation](actual_conway_general_mask_marked_filling.md) gives
\(U=\epsilon v-2\pi i t\), \(V=-2v\), with
\(v=\log[\sin\pi(x-t)/\sin\pi(x+t)]\).
At completeness, \(v_t=-2\pi c\), where \(c=\cot(\pi x)\).
Consequently the primitive cusp shape is
\[
\tau_{\mathrm{aux}}=\frac{dV}{dU}
             =\frac{2ic}{1-i\epsilon c}.
\]
The [complete tree geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md), Section 5, gives \(c_v=1/d_v\) for the circle of degree \(d_v\). For the original filling slope \(\mu_v+p_v\lambda_v\), direct substitution now gives
\[
 \mathcal L_v^2
   =\frac{|1+p_v\tau_{\mathrm{aux},v}|^2}{\Im\tau_{\mathrm{aux},v}}
   =\frac{1+n_v^2c_v^2}{2c_v}
   =\frac{d_v^2+n_v^2}{2d_v},\qquad
                 \mathfrak S=\frac12\sum_v\mathcal L_v^{-2}.
 \tag{37a}
\]
Here \(\mathcal L_v\) is the length of the actual primitive filling
slope divided by the square root of cusp area; the retained
half-twist is included through \(n_v=\epsilon_v-2p_v\).
Thus (2) is equivalently \(\sum_v\mathcal L_v^{-2}\le2^{-24}\)
for this class. This is a translation of the analytic hypothesis
using the proved cusp shape, not an imported geometric filling
criterion.

These examples retain the original knot/parity qualification.
They are not claims of a new topological family or priority.
Some star presentations overlap the existing long-pretzel and
fixed-outer-power belt-stack results; zero boxes may admit the
already known topological reduction. The graph-wide analytic
criterion does not use those reductions.

## 11. Identification with the knot volume

Small angular variables do not imply that the primitive meridian
logarithms are small: a high-degree circle collects contributions from
many edges. The geometric proof therefore follows the entire path of
filling equations, with its logarithm branches retained.

The [ordered decomposition](actual_all_circle_octahedral_decomposition.md)
cuts the original augmented exterior into two octahedra per tree edge.
Its literal strand matchings retain every face pairing, half twist and
primitive peripheral path. The [angular construction](actual_all_circle_angular_octahedra.md)
subdivides these octahedra into eight positive tetrahedra per edge on
the chart \(|\tau_v|<10^{-2}\). Section 7 places the whole path

\[
 \Psi_{\tau_v}+\frac{i n_v\tau_v}{2\pi}=ic,\qquad 0\le c\le1,
\]

inside this chart. The [completion proof](actual_all_circle_geometric_completion.md)
computes the actual periods

\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,\qquad
 V_v=2i\tau_v,\qquad U_v+p_vV_v=-2\pi ic.
\]

It verifies that the primitive slope bounds a tube of cone angle
\(2\pi c\). At \(c=1\) the tube is smooth, the auxiliary fillings
are precisely the original surgeries, and the main knot cusp remains
complete. The same proof fixes the additive volume constant at the
complete augmented link and integrates the boundary-corrected action.
It gives

\[
 2\pi\operatorname{Re}\mathcal C(\mathbf1)
             =\operatorname{Vol}(S^3\setminus K).
 \tag{38}
\]

Thus the analytic conclusion above is an actual uniform volume theorem
under (2). The [preferred-cusp continuation](actual_all_circle_preferred_cusp.md)
also identifies the first correction geometrically. This establishes
the summed criterion, not arbitrary short fillings or a criterion for
graphs with cycles.

## Reproducing the edge calculations

The [elementary Newton estimates](all_circle_uniform_newton_bounds.md) give a second direct proof of the uniform discarded-state and complex-strip bounds. The exact edge equations and finite samples of that strip inequality can be checked with:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

The [script](../experiments/audit_all_circle_curvature_packet.py) verifies four symbolic identities and samples the printed complex inequality at both even and odd levels. Its [recorded output](../experiments/all_circle_curvature_packet_results.json) states that finite scope. The uniform inequalities, contour argument and asymptotic conclusion are proved above; the script does not establish geometric completion.
