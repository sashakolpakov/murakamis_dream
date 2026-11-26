# The full original power-three kernel at the alternating reference

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note proves a nonzero packet for the **undeleted** original
power-three kernel near the same two-wire reference as the full
power-four packet. Every real-index endpoint, side current and alias
is controlled before the Gaussian is extracted. The assertion is a
vertex theorem; it does not estimate the complementary wire cycle of
a mixed word.

## 1. Exact source and statement

Use the original matrices and cardinal vector from the
[retained-vertex source](research_traced_three_vertex_endpoint.md).
Write \(r=e^{-2\pi i/N}\), \(X=e^{2\pi ix}\),
\(Y=e^{2\pi iy}\), and
\[
 c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N),\qquad
 V_{3,N}(x,y)=h(x)^TJM^3h(y)
 =\kappa c_xc_y\sum_{i,j\ge0\atop i+j<N}
 \frac{X^iY^j(r;r)_{i+j}}{(X;r)_{i+1}(Y;r)_{j+1}}.
 \tag{1}
\]
The sum is exact at both parities. In particular no Fourier corner
projection or error matrix is present.

Let \(a\) be the validated upper-half-plane root of
\(4a^4-6a^3+4a^2-2a+1=0\) in the
[alternating geometry](research_three_four_source_interface.md).
Put
\[
 K=\frac1{1+2a-4a^2},\quad x_0=\frac{\Log K}{2\pi i},\quad
 U_0=1-2a,\quad z_0=-\frac{\Log U_0}{2\pi i}.
 \tag{2}
\]
The quadratic relation \(K+K^{-1}=2-4\sin^2(\pi x_{34})\)
and the certified first-quadrant, unit-disk branch identify
\(x_0=x_{34}\), without a numerical phase choice. Approximately,
\(z_0=.353583333-.016783825i\).

For the original sine primitive \(J\), define
\[
 \begin{split}
 F_3(s,t;x,y)&=J(s+t)+\frac{i\pi}{2}\{s+t-(s+t)^2\}
       +s\Log X+t\Log Y-I_X(s)-I_Y(t),\\
 I_X(s)&=\frac{\operatorname{Li}_2(Xe^{-2\pi is})
                                  -\operatorname{Li}_2(X)}{2\pi i}.
 \end{split}
 \tag{3}
\]
All logarithms are the original interpolation lifts. Let
\((S(x,y),T(x,y))\) be the local critical branch through
\((z_0,z_0)\), and put
\[
 \Phi_3=F_3(S,T;x,y)-\pi i(x+y),\qquad
 H_3=F''_{3;s,t}(S,T;x,y),\quad
 U=e^{-2\pi iS},\quad V=e^{-2\pi iT}.
 \tag{4}
\]

**Theorem 1.** On a fixed complex neighborhood of
\((x_0,x_0)\), the full original kernel has the uniform expansion
\[
 V_{3,N}(x,y)=\kappa N^{-1/2}a_3(x,y)e^{N\Phi_3(x,y)}
                              \{1+O(N^{-1})\},
 \tag{5}
\]
where the nonzero holomorphic coefficient is
\[
 a_3=\frac{2\pi e^{\pi i(x+y)}}{\sqrt{\det(-H_3)}}
 \frac{\sqrt{2\sin\pi(S+T)}e^{-i\pi(S+T)/2}}
      {\sqrt{(1-X)(1-XU)(1-Y)(1-YV)}}.
 \tag{6}
\]
The symbol roots come from the exact factorial interpolants; the
determinant uses the accretive Gaussian branch. Every fixed wire
derivative of the normalized error is uniform. The actual angular
phase \(\Xi_3\) satisfies
\(\Phi_3=\Xi_3+i\gamma\), with exactly the same fixed real
\(\gamma\) as the homogeneous three-vertex calibration. In
particular their real parts agree. The carrier \(i\gamma\) is
retained in (5), not reset.

## 2. Uniform concavity and original logarithmic lifts

Set
\[
 A=\tfrac14,\quad B=\tfrac9{20},\quad
 h_-=-\tfrac3{100},\quad h_+=\tfrac3{200},\qquad
 \mathcal R=[A,B]+i[h_-,h_+].
 \tag{7}
\]
On \(\mathcal R^2\), \(1/2\le\Re(s+t)\le9/10\),
and \(|K|e^{2\pi h_+}<7/10\). Thus the exact numerator
factorial and both denominator interpolants are regular on a fixed
neighborhood of the entire rectangle.

Write \(u=e^{-2\pi is}\), \(v=e^{-2\pi it}\).
Differentiating the original primitive gives
\[
 (F_3)_s=\Log X+\log(1-uv)-\log(1-Xu),\qquad
 (F_3)_t=\Log Y+\log(1-uv)-\log(1-Yv).
 \tag{8}
\]
At the reference, \(K(1-U_0^2)=1-KU_0\) exactly.
The checker encloses the actual gradients in the strip
\(|\Im(F_3)_s|,|\Im(F_3)_t|<\pi\). Their exponentials
are one, so both gradients are zero. The selected critical point
lies strictly inside (7).

**Lemma 2.** At the reference,
\[
                  -\Re F''_{3;s,t}\succ\tfrac25 I_2
                              \quad\hbox{on }\mathcal R^2.
 \tag{9}
\]
The inequality persists, with a smaller constant, for nearby
independent wire parameters.

*Proof.* The negative real Hessian is
\[
 -\Re F_3''=
 \frac{2\pi\Im(uv)}{|1-uv|^2}\mathbf1\mathbf1^T
 +\operatorname{diag}\left(
 \frac{-2\pi\Im(Xu)}{|1-Xu|^2},
 \frac{-2\pi\Im(Yv)}{|1-Yv|^2}\right).
 \tag{10}
\]
The first coefficient is nonnegative, since
\(1/2\le\Re(s+t)<1\). Put \(\theta=\arg K\) and
\(d_0=2\pi A-\theta\), \(d_1=2\pi B-\theta\).
The certified inequalities give
\(0<d_0<d_1<\pi\) and \(\sin d_1>\sin d_0\).
Thus the sine is bounded below by \(\sin d_0>0\) on
the entire intervening interval. With
\(r_-=|K|e^{2\pi h_-}\), \(r_+=|K|e^{2\pi h_+}\),
each diagonal coefficient is at least
\[
             \frac{2\pi r_-\sin d_0}{(1+r_+)^2}
                           >\frac25.
 \tag{11}
\]
This proves (9), and compactness gives its parameter extension.
\(\square\)

Consequently the critical point is nondegenerate and continues
holomorphically. The phase is strictly concave on every horizontal
real-index plane and separately convex in each imaginary index
coordinate. These are bounds on the entire contour rectangle,
not merely a saddle Hessian.

## 3. Real complement, all currents and aliases

The separate [full-real-triangle complement theorem](research_three_vertex_alternating_reference_complement.md) gives a strict
absolute upper rate below \(651/1000\) outside \([A,B]^2\)
on a fixed neighborhood of the reference, including the origin
corner and all physical factorial endpoints. At the reference
\[
                         \Re\Phi_3>\frac{3281}{5000}=.6562.
 \tag{12}
\]
The real complement therefore has an exponential gap for the
original sum (1). The reference complement certificate is an
independent input; no absolute estimate is asserted by deleting
the small corner.

The [index-contour certificate](../repro/results/research-three-vertex-mixed-reference.json)
covers all sixteen products of the four sides of
\(\partial\mathcal R\) by 176 exact rational rectangles at
256-bit precision. For
\(F_c=F_3(z_0,z_0;x_0,x_0)\), it proves
\[
 \begin{array}{ll}
 \Re(F_c-F_3)>1/1000,&\text{if either side is vertical},\\
 \Re(F_3-F_c)<1/50,&\text{if both sides are horizontal}.
 \end{array}
 \tag{13}
\]
Each leaf is an outward mean-value bound on its full rectangle.
The binary tree is retained for independent coverage/replay. Strict
margins permit the actual half-grid displacements of the cuts and
a fixed complex neighborhood in both wire parameters.

For a vertical side times an intermediate horizontal height,
separate imaginary convexity from Lemma 2 reduces the upper bound
to the two endpoint heights in (13). This controls every join when
the main integral moves to \((\Im S,\Im T)\). The maximum
principle in the two complex index variables also bounds the
entire rectangle excess by \(1/50\).

At each half-grid cut use the exact lattice kernel
\(N\pi\cot(\pi Ns)\), of residue one. On its upper and
lower sides subtract the constant limits \(-i\pi N\) and
\(i\pi N\). The respective remainders cost
\(e^{-2\pi Nh_+}\) and \(e^{-2\pi N|h_-|}\), up to
polynomial factors. On each vertical midpoint side the cotangent
has modulus at most one. Tensoring both exact formulas produces
the original zero Fourier coefficient \(N^2\), all vertical
currents, and every horizontal alias. The first line of (13)
controls products with vertical sides. All remaining alias products
have a strict gap because
\[
                       2\pi h_+-\frac1{50}>\frac7{100}.
 \tag{14}
\]
Thus every complementary piece of the original central lattice sum
is accounted for before stationary phase.

## 4. Coefficient and original angular calibration

The exact numerator sine-factorial and the exact root-Pochhammer
denominators give the full holomorphic symbol
\[
 T_N(s,t)=N^{1/2}g_3(s,t;X,Y)e^{NF_3(s,t;x,y)}
                      \{1+O(N^{-1})\},\qquad
 g_3=\frac{\sqrt{2\sin\pi(s+t)}e^{-i\pi(s+t)/2}}
 {\sqrt{(1-X)(1-Xe^{-2\pi is})(1-Y)(1-Ye^{-2\pi it})}}.
 \tag{15}
\]
This interpolation matches each original lattice summand exactly
before its uniform expansion. The symbols are nonzero on a
neighborhood of \(\mathcal R^2\). Moving the zero Fourier
integral to the critical heights is justified by the preceding
current bounds. Lemma 2 gives a unique horizontal maximum there.
The two-dimensional Gaussian, its \(N^2\) lattice coefficient
and the original outside factor are
\[
 N^2\cdot N^{1/2}\cdot\frac{2\pi}{N}
       \frac{g_3(S,T)}{\sqrt{\det(-H_3)}},\qquad
 \kappa c_xc_y=\kappa N^{-2}e^{-N\pi i(x+y)}e^{\pi i(x+y)}
                                  (1-X^N)(1-Y^N).
 \tag{16}
\]
Their product is exactly (5)--(6). All omitted terms have strict
gaps or the usual holomorphic symbol expansion, so the normalized
relative error is \(O(N^{-1})\). Cauchy's formula on a smaller
wire neighborhood supplies every fixed derivative.

It remains to retain the angular constant; the old calibration box
does not contain the present \(U_0\). Join
\(U_*=e^{-2\pi i/3}\) to \(U_0\) by the straight segment
\(U_\lambda=(1-\lambda)U_*+\lambda U_0\), set \(V=U\),
and use
\[
 X=Y=(1+U-U^2)^{-1},\quad
 W=(U^2-2U-1)/2,\quad
 \tau=-i\Log\{W+\sqrt{W-1}\sqrt{W+1}\}.
 \tag{17}
\]
Two outward interval cells cover the whole path. They prove
\(U\) stays in the lower-left quadrant, \(X\) is in the
first-quadrant disk, \(|XU|<1\), \(\Im W>0\), and every
original angular factorial argument
\(1/2-x\pm\tau/(2\pi)\) has real part in \((0,1)\).
The index primitive stays in its regular strip too. All margins
are strict, so these paths have one connected open neighborhood.

The rational identities and original logarithmic equations in
the [absolute three-phase calibration](research_three_chain_action_volume_calibration.md#2-the-exact-vertex-identity-and-its-real-constant)
apply on that neighborhood. Their lifts are zero at homogeneity
and remain zero by connectedness; the coordinate Jacobian
\((1-U-V)X^2Y^2\) does not vanish. Hence the exact wire
derivative equality continues to the reference and to independent
nearby wires. The same homogeneous constant, already calibrated
without a numerical dilogarithm comparison, gives
\[
                  \Phi_3=\Xi_3+i\gamma,\qquad
                  \Re\Phi_3=\Re\Xi_3.
 \tag{18}
\]
The index packet is thus an actual source theorem with the original
marking and constant. No conclusion for a full mixed wire integral
is inferred.

Reproduce the finite current/branch checks with
`python3 experiments/certify_three_vertex_mixed_reference.py` and
`python3 experiments/replay_three_vertex_mixed_reference.py`.
The [independent replay](../experiments/replay_three_vertex_mixed_reference.py)
uses the opposite-frequency sine primitive, original sine-log
gradients, the geometric cosine for the wire, and principal-acos
calibration. At 320 bits it checks all 176 contour leaves and refines
the two calibration cells to 15, with 21 scalar comparisons and
two exact identities. Its
[record](../repro/results/research-three-vertex-mixed-reference-replay.json)
retains exact coverage and current dependency hashes. These checks
remain distinct from the all-level contour argument and the
independent real-complement proof.
