# Terminal fans and the full original Morse source

A terminal crossing-circle tangle is inserted into an actual ordered pair of strips on one side of an old crossing disk. This note proves that its source is the original shared-face coefficient with one new target \(N-1\). It then checks the extension of the complete-radius balance filling theorem to that source. All circles, signed powers, endpoint frames, the physical mark and full Casimir normals are retained.

The diagrams, number of insertions and integer filling powers are fixed before the level tends to infinity. No scalar kernel on an abstract cyclic graph is substituted for the physical source.

## 1. The literal insertion

Start with a connected augmented diagram whose labeled white triangulation is a simple sphere and whose matched cubic dual is its actual projection/crossing-disk cut. At a matching side \(xy\), write the triangles as
\[
 (x,b,y),\qquad (y,c,x).
 \tag{1}
\]
The old box has outer faces \(x,y\), input middle \(b\), and output middle \(c\). A terminal insertion on the first shaded side gives
\[
 (x,b,y)\longmapsto (x,b,w),\ (b,y,w),\ (y,x,w).
 \tag{2}
\]
The triples in (1)–(2) carry the orientation of the original projection sphere. Removing the common side \(bw\) from the first two new triangles leaves the boundary walk \(b\to y\to w\to x\to b\); hence its cyclic quartet is \((b,y,w,x)\). The triangle \((y,x,w)\) and the unchanged neighbor \((y,c,x)\), joined across \(xy\), have boundary walk \(x\to w\to y\to c\to x\). Thus their retained quartet is \((x,w,y,c)\). This derives both frames from their oriented boundaries, not from a reflection symmetry of the entropy.

The old matching side \(xy\) now has input/output middles \(w,c\). The new matching side \(bw\) has the orientation-preserving cyclic quartet \((b,y,w,x)\): its outer faces are \(b,w\), its input middle is \(y\), and its output middle is \(x\). Its signed crossing power is measured in precisely that frame. No reflection of the new coupon is used.

This is a physical insertion, not an arbitrary change of matching. Expose the old box as \(P_v=T^{-1}h_v\), with half-segment tuple \((v_3,v_0,v_1,v_2)\). A terminal child on its right changes exactly
\[
 \begin{array}{c|c}
 v_1-x_1&v_1-w_1,\quad w_2-x_1\\
 v_2-x_2&v_2-w_0,\quad w_3-x_2 .
 \end{array}
 \tag{3}
\]
On the other side the changes are
\[
 \begin{array}{c|c}
 v_3-x_3&v_3-w_3,\quad w_0-x_3\\
 v_0-x_0&v_0-w_2,\quad w_1-x_0 .
 \end{array}
 \tag{4}
\]
These are the actual stack and inverse-turn formulas in [the ordered disk decomposition](/Users/sasha/volume-conjecture/notes/actual_all_circle_octahedral_decomposition.md), sections 2–3. The formulas use only the two specified strips, and explicitly allow their other ends to lie outside the local ball. They therefore apply inside a non-tree exterior. All other strips remain fixed. The accompanying shaded-sector boundary walk gives precisely (2). There is no use of \(T^2=1\) on a labeled ball, no movement of a box through its neighbors, and no omission of an odd seam.

An odd two-strand braid has the diagonal pairing \(X=\{(0,2),(1,3)\}\). Its physical quarter-turn preserves this pairing, so every inserted odd terminal still has \(X\) in the exposed product frame used in (3) or (4). Two such consecutive factors compose to the through pairing, with no internal closed component: each of the two through arcs is concatenated once. Any even stack therefore preserves the original four external pairings. This argument uses rotations and the actual strip matches; it invokes neither a mirror reflection nor cancellation of the signed braid operators.

For the dependency paths below, note names refer to the workspace notes directory. These private links are only navigation; every local finite argument needed here is given explicitly.

## 2. Endpoint support and the new coefficient target

Fix \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\). Let \(H_f(x,b,c,y)\) be the original homogeneous degree-\(d\) face polynomial of an arbitrary full coupon \(f(\Omega)\). This includes actual signed crossing powers and cleared resolvent numerators, with all repeated-node data.

The local adapter of *actual_homogeneous_casimir_face_source*, equations (6)–(7a), is
\[
 f(\Omega)_{r,s;u,v}
 =N^{-1}q^{-d(r-u)}c^{-d}H_f(x,b,c,y)
 =N^{-1}\frac{H_f(x,b,c,y)}{(bc)^{d/2}} .
 \tag{5}
\]
The last equality uses the coherent integer face-log lifts of that physical state. No head is independently reduced modulo \(N\). The physical Casimir lowering arrows vanish at their genuine endpoints; hence a modular output with a wrong unwrapped total has zero coefficient before it is interpreted as a physical state. This is valid for every polynomial in the full Casimir, not only for the complete circle.

After (2), the two local factors in the numerator are exactly
\[
 H_f(x,w,c,y)\,H_g(b,y,x,w).
 \tag{6}
\]
Here \(g\) is the new coupon in its actual four-leg frame. Equation (6) identifies the refined source; it does not equate the old and new invariants or posit a multiplicative rule for quarter-turns.

Let \(M_f\) count middle incidences at boxes and \(T_f\) count outside minus inside Morse turns in face \(f\), temporarily restoring the cap at the marked edge. The change of the two quartets gives
\[
 \delta M_b=-1,\qquad \delta M_x=\delta M_y=1,
 \qquad M_w=1,\qquad \delta M_c=0 .
 \tag{7}
\]
Round the boxes in their actual frames. Each middle passage contributes \(+\pi\) to boundary turning; the outer pair contributes zero. Inside and outside turns contribute respectively \(+\pi\) and \(-\pi\). The boundary winding is one in a bounded face and minus one in the exterior \(a\). Thus
\[
 M_f-T_f=2\quad(f\ne a),\qquad M_a-T_a=-2 .
 \tag{8}
\]
This is the literal face-boundary turning calculation of *research_matched_sphere_morse_source*, section 5. It uses no flat-plat sweep or assumption of constant headcount.

Every old face retains its winding, while \(w\) is a new bounded face. Subtracting (8), with (7), gives
\[
 \delta T_b=-1,\qquad \delta T_x=\delta T_y=1,
 \qquad T_w=-1,\qquad \delta T_c=0 .
 \tag{9}
\]
A local Morse drawing can have one extra cup and one extra cap; additional cancelling Morse pairs do not change (9). Therefore all old exponents are unchanged, and the new exponent is
\[
 \frac d2(T_w-M_w)=-d .
 \tag{10}
\]
The new ordinary coefficient target is exactly \(d\), rather than a free boundary condition.

For even \(N\), the face parity cochain differs by one across MAIN edges and by zero across matching sides. Since \(xy\) is matching, \(t_x=t_y\), and the old triangle has \(t_b=t_x+1\). The unique local extension is
\[
 t_w=t_b,\qquad t_w-t_x=t_w-t_y=1\pmod2 .
 \tag{11}
\]
Thus \(bw\) has zero parity difference, every new MAIN side has difference one, and all old clocks are unchanged. Swapping the order in which the two new middle faces are read does not change these equations: in the actual frame the input is \(y\), the output is \(x\), and \(t_x=t_y\). The original even-level coset is therefore still exactly (11).

## 3. The physical mark, measure and normals

Keep a MAIN edge outside the insertion as the mark, with adjacent protected faces \(a,b_*\). The spherical whole-source mark transport may expose it as a top cap; it does not replace an internal marked row by an ordinary cap. The regular generic pivot is \((-1)^HK\), specializing to the original \(K^{1-N}\). Its self-duality and equal left/right traces are proved in *research_arbitrary_main_edge_mark_transport*, sections 2–3, for arbitrary Morse presentations.

In literal left-to-right physical order the cup, cap and mark are
\[
 p_{ij}=Nq^{-d^2+di}\mathbf1_{i+j=d},\qquad
 \ell_{ij}=N^{-1}q^{di}\mathbf1_{i+j=d},\qquad
 m_{ij}=N^{-2}q^{dj}.
 \tag{12}
\]
The marked row is initially unrestricted. The whole-network degree conservation, after the other actual caps act, forces its two heads to sum to \(d\). Only then is its ratio to the ordinary cap
\[
 \frac m\ell=N^{-1}(L_{b_*}/L_a)^d .
 \tag{13}
\]
The added cup and cap have cancelling powers of \(N\) and cancelling fixed \(q\)-constants. If the refined diagram has \(R'\) boxes, (5), (8) and (13) make its full marked summand
\[
 N^{-R'-1}\,
 \frac{\prod_{e=1}^{R'}H_{f_e}(L_{x_e},L_{b_e},L_{c_e},L_{y_e})}
      {\prod_{f\ne a,b_*}L_f^d}.
 \tag{14}
\]

The connected spherical graph has \(R'+2\) faces. The conserved integer head lattice identifies primitively with face potentials modulo one common constant. This follows by integrating along dual paths; zero divergence gives independence of the path on the sphere. Bending a physical arc does not change that lattice. After fixing \(L_a\), there are \(R'+1\) independent \(N\)-point grids. Their count cancels the prefactor in (14). Thus one insertion gives one new coupon factor \(N^{-1}\) and one new grid factor \(N\), with no residual quantum dimension.

The numerator is homogeneous of degree \(dR'\), with nonnegative exponents, though its coefficients can be complex. The grid requires exponent \(d\bmod N\) at all \(R'\) ordinary faces, and zero modulo \(N\) at the other protected face. The ordinary minimum degrees already sum to \(dR'\). Hence no higher alias is possible: every ordinary exponent is \(d\), and both protected exponents are zero. At even levels the remaining coset character is one. The exact refined scalar is therefore
\[
 I_N=\left[\prod_{f\ne a,b_*}L_f^d\right]
 \left.\prod_{e=1}^{R'}H_{f_e}
       (L_{x_e},L_{b_e},L_{c_e},L_{y_e})
 \right|_{L_a=L_{b_*}=0}.
 \tag{15}
\]

This holds for arbitrary local full polynomials and their spectral parameters. In particular use
\[
 V_N(\sigma;z)=
  \frac{\chi_N(\sigma)-\chi_N(z)}{\sigma-z},\qquad
 \chi_N(z)=\mathcal T_N(z)+2
 \tag{16}
\]
as a polynomial before setting \(z=\Omega\). It is the actual cleared resolvent at the root and retains the first derivative at every double Casimir node. No value-only interpolation or paired-channel retraction is used.

If an ordinary generic closure is used instead, the full open regular network is a scalar endomorphism of the generic highest-weight object \(V_d\). Its ordinary closure is \((-1)^d[N]_q\) times that scalar. The one genuine normal at the root recovers (15). No additional normal occurs at the inserted circle or at a separator. This uses the regular physical lift, not a derivative of an arbitrary fixed-root identity.

## 4. The original signed Fourier/Hermite period

Put the literal nonzero fixed signed power \(R^{n_e}\) at each refined box, with \(n_e=\epsilon_e-2p_e\) in its own original disk framing. Define the whole spectral numerator
\[
 S_N(\boldsymbol\sigma)=
 \left[\prod_{f\ne a,b_*}L_f^d\right]
 \left.\prod_{e=1}^{R'}H_{V_N(\sigma_e)}\right|_{L_a=L_{b_*}=0}.
 \tag{17}
\]
Apply the source-independent local full-Hermite crossing functional separately to each box. Multilinearity of the original ordered contraction, not commutation of different boxes, gives
\[
 \begin{split}
 I_{N,\boldsymbol n}={}&
 q^{\frac{d^2}{4}\sum_e n_e}(-i)^{R'}
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^{R'}}
 \left(\prod_e\ell_e\right)(-1)^{(N+1)\sum_e\ell_e}\\
 &\times\int_{[-1/2,1/2]^{R'}}
 \left(\prod_e\sin(2\pi\delta_e)\right)
 S_N(-2\cos(2\pi\boldsymbol\delta))\\
 &\qquad\times
 \exp\!\left\{N\sum_e[\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e]\right\}
 d\boldsymbol\delta .
 \end{split}
 \tag{18}
\]
This is *research_matched_sphere_morse_source*, section 6, now on the literal inserted network. The Cartan scalar, charge weights, parity and endpoint sine factors have not changed. The original matrix identity excludes charge zero. Three integrations by parts on whole intervals give absolute summability, retaining the second-derivative endpoint currents. No constant-headcount assumption occurs.

The exterior framing/component character remains separately recorded. At complete main color it has modulus one. The full one-cut modified convention also retains its specified polynomial-level factor. These source conversions do not change the exponential rate. The invariant in (18) belongs to the refined filled link, not to the original unrefined core.

## 5. The balance theorem extends to the refined Morse source

Assume the refined simple white sphere has its actual nondegenerate positive right-angled certificate. At its one complete marked packing, with both protected curvatures zero, put \(A_e=x_e+y_e>0\) and
\[
 X_e=Q_{b_e}(0)+Q_{c_e}(0).
\]
Assume
\[
 X_e>\log b_e\quad(b_e>0),\qquad
 X_e>\log c_e\quad(c_e>0).
 \tag{19}
\]
These use the original source-normalized triangle actions and one shared actual packing.

The full numerator retains the disjoint CROSS/LEFT/RIGHT path partition at both parities. The actual global weighted one-sided estimates on the same face torus have rates
\[
 L_e=\max\{\log c_e,Q_{b_e}(0)+\tfrac12\log c_e\},\qquad
 R_e=\max\{\log b_e,Q_{c_e}(0)+\tfrac12\log b_e\},
 \tag{20}
\]
when the corresponding middle is positive. At a zero middle the respective polynomial vanishes identically. The strict \(Q_t(0)>\frac12\log t\), with (19), gives \(L_e<X_e\), \(R_e<X_e\). The CROSS factor has rate at most \(X_e\), with polynomial loss only. These are the original local cofactor estimates for exactly the local factors in (17).

The same face target therefore bounds every sector containing a one-sided factor, uniformly on the full real spectral cube, by
\[
 |S_{N,\mathrm{noncross}}(\boldsymbol\sigma)|
 \le e^{N(\Phi-\gamma)},\qquad
 \Phi=\frac{\operatorname{Vol}(Y)}{2\pi},\qquad \gamma>0 .
 \tag{21}
\]
The calibrated identity is
\(\sum_eX_e-\sum_{f\ne a,b_*}\log L_f=\Phi\).
There are finitely many sectors. Bernstein and Cauchy extend the bound to a fixed thin complex angular strip and its required derivatives. No separate local radius maximizations are used.

The all-CROSS packet and global gap are the explicitly audited Morse extension in *research_general_morse_cross_action*, section 4. Their actual hypotheses are the simple sphere, protected MAIN edge, original local polynomials and positive certificate. Deleting the protected vertices leaves the ordinary graph connected. The angular proof therefore leaves only one common phase, with primitive difference rows and no new alias. The positive coefficient Hessian lives on the \(R'-1\) dimensional scale quotient. The finite packet is
\[
 C_N^{\mathrm{raw}}(\boldsymbol\delta)=
 \frac{(-1)^{dR'}N^{2R'}e^{NA_N(\boldsymbol\delta)}}
 {(2\pi N)^{(R'-1)/2}\sqrt{\det H_N(\boldsymbol\delta)}}
 (1+O(N^{-1})).
 \tag{22}
\]
It is relative on a fixed complex chart, with the determinant branch continued from the positive complete Hessian. Its phase is separately even, with strictly negative diagonal limiting angular Hessian. The same proof gives the global spectral gap away from its center. This uses only the CROSS assembly; it does not invoke the old flat-forest full-numerator restoration.

The whole-domain proof of *general_all_cross_long_filling_volume* now applies literally to (18). Its finite retained charges, whole-interval far-charge tails, endpoint currents and real-spectator bounds use (22), the global CROSS gap, finite polynomial degree and the sine endpoints. All are present. The first-charge amplitude is nonzero at both parities, and its action tends to \(\Phi\) as the independently signed fixed powers become long.

Apply the same whole-domain integrations by parts to (21). The full-minus-CROSS period has rate at most \(\Phi-\gamma'\), for a fixed \(\gamma'>0\). Increase the diagram-dependent filling threshold so the first-charge drop is less than \(\gamma'/2\). Then
\[
 I_{N,\boldsymbol n}
 =I_{N,\boldsymbol n}^{\mathrm{cross}}
       (1+O_{\boldsymbol n}(e^{-c_{\boldsymbol n}N})).
 \tag{23}
\]
No ratio bound among the different fixed powers is required.

The geometric action is that of the refined Morse link. At each cup or cap, the two original white-reflection head words multiply to the identity, so the group sewing works with variable headcount. The character in (14) supplies the original log-radius targets; each local collar retains its original \(n_e=\epsilon_e-2p_e\). The actual positive complete anchor, marked regulator and primitive unit-charge filling therefore give
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|I_{N,\boldsymbol n}|
 =\operatorname{Vol}(S^3\setminus K_{\boldsymbol n})
 \tag{24}
\]
when the chosen parity gives a knot. More generally the target is the corresponding smooth filled exterior. Its volume is never replaced by that of a scalar comparison graph.

## 6. Scope

The exact identities (15)–(18) require no geometry or balance assumption. The volume conclusion additionally requires the actual positive certificate and (19). A geometric construction proving those inequalities at the true refined complete packing supplies a nonempty class beyond operation trees; that fact is not inferred here from free local curvatures.

The theorem concerns the full complete-main-color invariant with independently sufficiently long fixed signed fillings. It does not establish a new moving-main profile or an all-order operator statement. Even fan counts may preserve the original endpoint pairing and knot condition, but the resulting knot generally differs from the core knot. The new magnetic loop variables of the matching-graph source remain in the full coefficient (17); no projection eliminating them is needed.
