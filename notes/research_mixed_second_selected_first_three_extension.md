# The second-selection theory with a first block of type three

Research deduction, 6 November 2026. The existing original-reference,
residual-localization, directional-budget and boundary-extension proofs
already include first flag zero. Their central scalar formulas therefore
apply to prefixes of types \(343\) and \(344\), with a changed
original reference and incoming marginal. The completed first-type-four
reference certificates and numerical response bounds do not transfer.
This note identifies the precise mathematical and implementation changes.
No root, primitive, reference enclosure or parameter cover is evaluated.

## 1. Original reference and endpoint ranges

Fix a mixed word of length \(m\ge4\) with first three flags
\((0,1,\beta)\), \(\beta\in\{0,1\}\). Position 1 is
unselected and position 2 is selected at \(H=1/100\). Use
\[
 q=(e,\xi,a,u,z,v,b),\qquad
 (a,u,z,v,b)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad c=s_4^*.
 \tag{1}
\]
Both indices \(u,v\) are ordinary, including at length four;
\(c\) is attached at length four and ordinary at greater lengths.
The [endpoint rectangle theorem](research_mixed_open_word_endpoint_rectangles.md)
gives the following strict first-type-three bounds:
\[
 \begin{split}
 e&\in(.376,.438)+i(-.019,.037),\\
 \xi&\in(.218,.242)+i(.049,.077),\\
 a&\in(.278,.391)+i(-.072,.021).
 \end{split}
 \tag{2}
\]
In addition \(a\in P_3\), with
\[
 P_3=\{|w-(.35-.01i)|\le.083\},\qquad
 P_4=\{|w-(.30-.052i)|\le.060\}.
 \tag{3}
\]
The attached coordinate \(a\) is not an ordinary type-three index;
one must not replace its lower height bound \(-.072\) by \(-.065\).
In particular neither the first-type-four endpoint rectangles nor
its stronger attached bound \(\Im a<-.020\) applies.

The remaining mandatory ranges are unchanged:
\[
 \begin{split}
 u,z&\in O_4=P_4\cap([.24,.36]+i[-.102,-.001]),\\
 v,b&\in O_{3+\beta},\qquad
 O_3=P_3\cap([.267,.433]+i[-.065,.068]),\\
 c&\in K_3\cup K_4,\\
 K_3&=P_3\cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4&=P_4\cap\{-.108\le\Im c\le-.001\}.
 \end{split}
 \tag{4}
\]
As usual these closed intervals enclose strict actual bounds. The
[reference-curve theorem](research_mixed_second_selected_reference_curve.md),
Sections 2--4, proves these assertions also for its canonical prefixes
at every \(c\in K_3\cup K_4\), not merely at parameters known
to be realized by finite suffixes.

The same theorem gives a unique holomorphic canonical prefix near each
of the larger disks \(D_3,D_4\), with the centers in (3) and
radii \(.09,.064\). Its fixed-point construction uses the genuine
\(\operatorname{endpoint}_0\) map in the first group. Existence,
uniqueness and zero original logarithmic lifts are therefore already
available. No first-type-four certificate is needed to assert this
first-type-three existence theorem.

## 2. The two changed gradient rows

Use the original \(j(w)=J'(w)=\Log(2\sin\pi w)\) and the
unscaled seven-gradient system in
[residual localization](research_mixed_prefix_residual_localization.md),
equation (3). On setting \(\alpha=0\), the changed rows are
\[
 \begin{split}
 f_e^{(0)}&=-j(e-\xi)+j(e+a)+i\pi(\xi-a),\\
 f_a^{(0)}&=j(e+a)+j(a+u)-2j(a)+i\pi(u-e).
 \end{split}
 \tag{5}
\]
The rows \(f_\xi,f_u,f_z,f_v,f_b\) are exactly the same
formulas as for \(\alpha=1\), evaluated at the new coordinates.
Equivalently, as identities between the analytic formulas at a fixed
point, \(f_e^{(0)}=f_e^{(1)}+g'(e)\) and
\(f_a^{(0)}=f_a^{(1)}+g'(a)\), because
\(g'=j-i\pi(w-1/2)\). This is not an identity between the
two canonical solutions.

With \(k(w)=\pi\cot\pi w\), the changed Jacobian entries are
\[
 H_{ee}^{(0)}=-k(e-\xi)+k(e+a),\qquad
 H_{aa}^{(0)}=k(e+a)+k(a+u)-2k(a).
 \tag{6}
\]
All off-diagonal entries and the other five diagonal entries are
unchanged in form. The external forcing remains rank one:
\[
                       f_c=e_b\{k(b+c)+i\pi\}.
 \tag{7}
\]
For a Taylor residual remainder, remove the \(-j(e)\) term from
the first row and change the coefficient of \(j(a)\) from
\(-3\) to \(-2\) in the attached row. The chirps remain affine
and have zero second derivative. The auxiliary row remains the full
\(2j(1/2-\xi)-3j(\xi)+j(e-\xi)+i\pi e\), with no rescaling.

The common convex product is still
\[
 \mathcal D=E\times U\times Q^5,\quad
 E=[.33,.47]+i[-.09,.08],\quad U=[.21,.25]+i[.01,.10],\quad
 Q=[.23,.45]+i[-.12,.12].
 \tag{8}
\]
All boxes (2)--(4) lie in their appropriate common factors.
The [original Hessian theorem](research_mixed_open_word_hessian.md)
proves \(-\Re H\succ\mu I\), \(\mu=6\pi/49\), for every
type pattern on this same product. In its proof the endpoint term
already supplies its coercivity before any additional type-four own
terms are added. Removing those terms at the first vertex therefore
does not require a new constant. Consequently
\[
          \|q_0-q_*^{(0,\beta)}(c)\|_2
          \le \|f^{(0,\beta)}(q_0;c)\|_2/\mu
 \tag{9}
\]
holds under the same existence and domain hypotheses as before.

The full affine Taylor bound, preconditioned inverse and response
enclosures in the
[external-reference specification](research_mixed_second_selected_external_reference_evaluation.md)
are algebraic consequences of (7)--(9). Their proofs transfer with
the changed gradient, Jacobian and Taylor rows. Raw affine images and
connecting segments must still be certified before any necessary
actual-reference clipping. A root proposal, new seed or small
floating residual alone is not a proof.

## 3. Central target curvature and the unchanged three gains

The allocated five-variable reference phase is now
\[
 F_0=Q_1(u;a,z)+Q_\beta(v;z,b)-g(z)-\frac\beta2g(b),
 \tag{10}
\]
using the original bare \(Q_\epsilon\). In particular there is
no incoming \(-g(a)/2\). The correct boundary marginals are
\[
 p_L=g'(a+u)-g'(a)+2\pi iu,\qquad
 p_R=g'(v+b)-(1+\beta/2)g'(b).
 \tag{11}
\]
The original stationary equations still give \(F_{0,u}=F_{0,z}
=F_{0,v}=0\). Only the target height of \(z\) changes to \(H\),
and both marginals in (11) remain subtracted from the target phase.
Explicitly, with \(r=(a_*,u_*,z_*,v_*,b_*)\),
\[
 \begin{split}
 M&=\Re F_0(r),\\
 f_\nu(w)&=\Re\{F_0(w)-p_L(w_a-a_*)-p_R(w_b-b_*)\}
          +(1-\nu)\Re g(w_z)-2\nu\pi H.
 \end{split}
 \tag{11a}
\]
The targets have the same original real product and unselected
reference heights as the cited central budget.

The first-type-three height \(\Im a\in(-.072,.021)\) lies
inside the common interval \((-.078,.021)\) used by the
[horizontal concavity and index-barrier theorem](research_mixed_second_selected_horizontal_concavity.md).
Thus its original product, strict concavity and restrictions
\[
  u_R>.22,\qquad v_R>q_\beta,\qquad q_0=.2,\quad q_1=.22
 \tag{12}
\]
apply unchanged. The diagonal incoming cost in that theorem decreases
from \(g_{h_a}''\) to \(g_{h_a}''/2\); it remains nonnegative.
Its trial force is zero by (11), so the
[directional-budget proof](research_mixed_second_selected_directional_budget.md)
already discards exactly this cost for both values of \(\alpha\).
No extra incoming optimization gain is needed.

For clarity, use \(c_z=\Im z_*<0\), to distinguish the
selected reference height from the external parameter \(c\).
Put \(z_H^*=\Re z_*+iH\). The exact vertical cost is
\[
 \mathcal V=\Re\{g(u_*+z_H^*)-g(u_*+z_*)
 +g(v_*+z_H^*)-g(v_*+z_*)-3g(z_H^*)+3g(z_*)\}
            -2\pi\Re v_*\,(H-c_z).
 \tag{13}
\]
The central forces, \(T_\nu\), and the three-gain majorant
are precisely those of the directional theorem:
\[
 \sup_x\max_{\nu=0,1}(f_\nu-M)
 \le\max_{\nu=0,1}
     \{T_\nu+\mathcal U(A)+\mathcal R_\beta(d)
                      +\mathcal Z_\nu(D_\nu;I_\nu)\},
 \quad I_1=P,\quad I_0=[.4,.45].
 \tag{14}
\]
All quantities use one new original \(\alpha=0\) reference.
The sign proof \(A>0,d>0\) uses the general pair-sum lower
bound \(\Re(u_*+z_*)>.49\), which remains available even
when \((\alpha,\beta)=(0,0)\). It does not require the stronger
first-type-four lower bound. Fourier dominance on \(x_z<.4\)
also depends only on \(g(x_z+iH)\), so it is unchanged.

The stationary vertical constants \(21\pi/10\) for \(\beta=0\)
and \(39\pi/20\) for \(\beta=1\) depend only on the unchanged
ordinary real-coordinate ranges. The
[local curvature improvements](research_mixed_second_selected_local_curvature_gains.md)
and [rational curvature refinement](research_mixed_second_selected_curvature_evaluation.md)
therefore remain valid under their exact local guards. In particular
the cubic left gain still requires its stated \(u_*\) and force
conditions; the sharper right and selected gains still require their
own conditions. None is asserted automatically for a first-type-three
reference.

## 4. The changed incoming response and the same extension criterion

Differentiating (11) along the new holomorphic canonical curve gives
\[
 \begin{split}
 p_L'&=\{k(a+u)-k(a)\}a'+\{k(a+u)+i\pi\}u',\\
 p_R'&=\{k(v+b)-i\pi\}v'
   +\{k(v+b)-(1+\beta/2)k(b)+i\pi\beta/2\}b'.
 \end{split}
 \tag{15}
\]
Thus the incoming \(3/2\) cotangent coefficient becomes one,
and its previous \(+i\pi a'/2\) term disappears. The response
function retains the form
\[
                \mathcal B_0(c)=|p_L'a'|+|p_R'b'|.
 \tag{16}
\]
Its values must be newly bounded on the new reference curve. Neither
the first-type-four derivative boxes nor their numerical upper bounds
for \(\mathcal B\) are certificates for (16).

The [stationary boundary-extension theorem](research_mixed_stationary_reference_boundary_extension.md)
is already stated for both first flags. Its full target height
conditions include (2)--(4), and it uses the same
\(\Lambda=\operatorname{diag}(1,1,0,1,1)\). Therefore a complete
boundary gap \(\gamma\), for both original central alternatives,
and a separate whole-boundary response bound \(B_0\) imply the
same interior lower deficits
\[
 \gamma-\frac{6889}{2000000}B_0\quad(K_3),\qquad
 \gamma-\frac9{5000}B_0\quad(K_4).
 \tag{17}
\]
The reference coordinates are holomorphic on neighborhoods of the
closed domains; complete-boundary strict height margins extend by
harmonic maximum and minimum principles exactly as before. Geometric
chart formulas and strict exclusions depend only on \(K_3,K_4\)
and may be reused. A new complete reference and scalar certificate
on those charts is still required.

## 5. What a new implementation may reuse

The original primitive, its centered enclosure, and the old scalar
node-conjugate method do not encode the first endpoint flag. Static
inspection also shows that the frozen
[directional evaluator](../experiments/evaluate_mixed_second_selected_directional_budget.py)
and [curvature wrapper](../experiments/evaluate_mixed_second_selected_curvature_budget.py)
read only \(u,z,v\), their shapes and \(\beta\). Their arithmetic
contains no \(\alpha\)-dependent term. They may be reused unchanged
after a caller proves the new common-reference premises and explicitly
records first flag zero. In particular neither helper supplies the
endpoint existence or original stationary equations.

The existing original-gradient provider and response module, in
contrast, are fixed to first flag one. A separate provider must use
(5)--(7), their Taylor coefficients, the new endpoint rectangles (2),
and fixed rational proposal seeds. These seeds need not themselves
be certified canonical references: the existing existence theorem
and a certified original-gradient residual of the resulting proposal
supply the localization proof. Independently certifying the two
\(c=1/3\) references may provide useful starting data, but is not
a mathematical requirement for a floating proposal. A separate response
module must use (15) and the same full-box height checks. Output flags,
hash bindings and input associations must identify the new family.
The old providers, two \(c=1/3\) certificates, boundary banks and
completed gap records remain unchanged and do not certify new data.

The residual norm theorem, full affine Taylor argument, Cartesian
regularity checks, Neumann inverse proof, and
[componentwise Neumann refinements](research_mixed_componentwise_neumann_refinement.md)
are reusable mathematical tools. Their inputs must be the changed
original system. In particular a componentwise root refinement still
requires a Jacobian enclosure on the whole segment from its affine
predictor to the enclosed root; the change of first flag does not
relax that premise. The old factored rational maps for first flag one
cannot be substituted for the new endpoint map.

## 6. Exact finite-source scope

The existing [four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
already covers first flag zero. Its literal product becomes
\[
 |C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
                           |d_N(X_3)|^{\beta/2}.
 \tag{18}
\]
There is no incoming \(|d_N(X_1)|^{1/2}\). Both original
complex boundary tangents remain, now given by (11).
For \(\beta=1\), the proved pointwise outgoing-four half-row
comparison has no first-flag premise, so a new uniform central sign
would complete that local finite product, together with the existing
joint last-row bound. For \(\beta=0\), the two joint right-half-row
signs are additional requirements: the completed \(\alpha=1\)
half-row result does not give them. Its analytic half-row budget and
formal-coordinate boundary-extension proof do extend, since their
incoming cost is still nonnegative and its force still zero, but their
numerical data would also have to be replaced.

No central sign, right-half-row sign, finite-product gap or plateau
completion for first flag zero is asserted here. The proved result is
that the original reference theory and the exact scalar and boundary
criteria extend, with the explicit changes above and no loss in their
analytic constants. A completed new certificate remains necessary.
