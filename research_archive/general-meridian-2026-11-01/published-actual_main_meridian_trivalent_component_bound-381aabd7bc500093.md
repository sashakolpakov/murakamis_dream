# Controlling meridian deformations in trivalent Conway regions

This special-case argument is retained in full. The [general component theorem](actual_main_meridian_general_component_comparison.md) and [filled-meridian theorem](actual_main_meridian_filled_volume.md) now permit every fixed strict bare component, without an additional valence or path condition.

1 November 2026.

A Conway construction joins two-string tangles by ordered products and physical quarter-turns. Consecutive products with no intervening turn can be collected into a single product junction. A junction is **bare** if it contains no original crossing-circle operator. A connected bare region can have many such junctions. This note proves a uniform source estimate when each junction in that region is **trivalent**, meaning that exactly three branches meet there, including branches attached to the rest of the construction.

The valence is measured in the reduced tree of actual operations. A junction with four or more branches cannot be made eligible by drawing it as several binary products: the new edges would have no physical quarter-turn. That distinction is used in the proof. The number of trivalent junctions is otherwise unrestricted, provided the whole construction is fixed before the level tends to infinity.

Moving the main meridian changes the polynomial relation used by the quantum calculation. A product that was zero in the complete quotient can acquire an additional term. We will call these **additional trace terms**; in a finite expansion one chooses either the complete term or an additional term at each junction. Such a choice is a *sector*. The theorem controls every sector with at least one additional term by the same original complete geometric action, with a strict loss. It retains all labels on internal edges. In particular an internal maximizing label is allowed to equal or exceed one half.

## The component estimate

Set \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and let \(s\) be the microscopic main-meridian parameter, so the marked meridian is \(M=q^s\). The fixed complete Newton polynomials and the moving quotient are
\[
\begin{gathered}
 c_j=2\cos\frac{(2j+1)\pi}{N},\qquad
 S_r=\prod_{a=1}^r2\sin\frac{\pi a}{N},\quad S_0=1,\\
 e_r(z)=\frac{\prod_{j=0}^{r-1}(c_j-z)}{S_r^2},\qquad
 P_s(z)=\mathcal T_N(z)+2\cos(2\pi s)=P_0(z)+\Delta_s,\\
 \mathcal T_N(2\cos t)=2\cos Nt,\qquad
 \Delta_s=2\cos(2\pi s)-2,\\
 \phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
\end{gathered}
\tag{T1}
\]
Here \(\operatorname{rem}\) is the polynomial remainder of degree less than \(N\). The [typed polynomial compiler](actual_main_meridian_newton_compiler.md) places equal-color operators in this moving quotient and opposite-color operators in the constant quotient \(P_0\). Its orientation types, circle pivots and physical turn scalars remain fixed throughout the argument. Polynomial identities retain the first derivatives at repeated spectral nodes as well as the nodal values; these derivatives are the first Hermite normal coordinates of the invariant.

A boundary operator has an independent coefficient array \(F_i=\sum_r f_{i,N,r}e_r\). Put \(M_N=\lfloor d/2\rfloor\), and call \(r\le M_N\) low and \(r>M_N\) high. Assume, uniformly in all specified physical colors and on every fixed \(|s|\le R<1\),
\[
 |f_{i,N,r}(s)|\le e^{N(c_i+\epsilon_N)}
 \begin{cases}
 e^{Ng(r/N)},&r\le M_N,\\
 1,&r>M_N,
 \end{cases}
 \qquad \epsilon_N\longrightarrow0,
\tag{T2}
\]
where \(g\) is defined in (1), and the real constant \(c_i\) records the action already accumulated in that boundary branch. These are bounds on the entire coefficient array; no physical alias decomposition is assumed for an effective branch.

View the region as an unturned expression \(A\) with one output, and let \(Q=T(A)\). Replace its boundary profiles by the pure complete profiles \(g+c_i\), and close it against the usual pure comparison leaf. The resulting strict positive source has action
\[
                 \Omega_Q=\Phi_{C(hA^0)}+\sum_i c_i.
\tag{T3}
\]
The comparison leaf specifies a scalar inequality; it is not an extra crossing circle in the knot. The [intrinsic-probe geometry](actual_conway_unflagged_probe_geometry.md), Sections 1–4, identifies (T3) with the pressure assigned to this same original branch.

**Theorem.** Suppose every junction of the region has full valence three, every internal edge is an original physical quarter-turn, and the pure complete comparison has its original strict state. Then, for some fixed \(\delta>0\), its actual canonical output obeys
\[
                         \|Q_{N,s}\|_{\mathcal J}
                       \le e^{N(\Omega_Q+o(1))}.
\tag{T4}
\]
The norm \(\mathcal J\) includes values and first derivatives at the complete double nodes, and the value at the odd simple node. The terms with at least one additional trace term, or with a high boundary input or high output probe, have norm at most
\[
                         e^{N(\Omega_Q-\delta+o(1))}.
\tag{T5}
\]
The remaining part has low boundary inputs and low output, but keeps every complete-supported internal label. It is bounded coefficientwise by a subexponential multiple of the same complete positive reference. The estimates hold at both parities and on every fixed disk \(R<1\); the geometric loss can be chosen independently of that radius. All constants may depend on the fixed region. An inherited loss in one full boundary coefficient array decreases the entire estimate by that same loss.

The exact turned coefficient and its norm comparison make the output probe concrete. Let \(w_{N,r}=e_r(-2)\) for low \(r\), and \(w_{N,r}=1\) for high \(r\). In the actual output type,
\[
\begin{gathered}
 [e_r]T_\gamma(A)=\frac{\gamma_N(s)W_{d-r}(s)}{H_N(s)}\,
                                      \phi_\sigma(e_rA),\\
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 W_r(s)=\prod_{a=1}^{r}
 \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi a/N)}\right),\\
 \|T_\gamma(A)\|_{\mathcal J}
       \le C_RN^C\sum_{r=0}^{d}w_{N,r}|\phi_\sigma(e_rA)|.
\end{gathered}
\tag{T6}
\]
The parameter \(\sigma\) is \(s,-s\) or zero according to the actual orientation type. The prescribed scalar \(\gamma_N(s)\) is \(1\) or \(q^{\pm s^2/2}\). The [turn theorem](actual_main_meridian_turn_comparison.md) proves uniform boundedness of the paired ratios on \(R<1\); the [full-node Newton estimate](actual_conway_root_star_full_jet_localization.md), Sections 2–3, proves the polynomial norm conversion. The sum in (T6) has the same low profile \(g\) and high profile zero as another boundary input. Thus the component theorem treats that probe with its complete finite support and all first normal coordinates.

Sections 1–3 prove a simultaneous boundary inequality for the complete positive action. Sections 4–5 use it to replace all additional terms by a feasible boundary state of the same coupled complete source. Section 6 passes from actions to the finite source. Appendix A derives the exact finite tensor, including its signs, support and uniform endpoint bounds.

## 1. The complete cubic action and a constrained region

Let
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 g(x)=J(2x)-4J(x),\quad 0\le x\le\tfrac12.
 \tag{1}
\]
The complete symmetric cubic action is
\[
 t(x,y,z)=J(x+y)+J(x+z)+J(y+z)
       -J(x)-J(y)-J(z)-J(x+y+z-1),
 \tag{2}
\]
on the closed domain
\[
 x,y,z\ge0,\qquad x+y,\ x+z,\ y+z\le1,
 \qquad x+y+z\ge1.
 \tag{3}
\]
Its strict domain has all three labels positive, all pair sums less than one, and total greater than one. Writing its third covariant label as \(z=1-b\) identifies (2) with the original product action \(m(x,y,b)\). Thus it is concave, continuous on (3), and has negative definite Hessian in the strict domain, by the [three-tetrahedron decomposition](actual_conway_general_core_packet_and_gap.md), Sections 1 and 3. Here and below, an action is the limiting logarithm of a coefficient divided by the level. The explicit sine-factorial formulas determine these limits.

Consider a finite connected tree of complete trivalent vertices. Its external incidences have two kinds. An ordinary incidence carries the profile \(g(a)\) with freely varying \(a\in[0,1/2]\); additive constants may be retained separately. A marked incidence has a prescribed label \(z_i\) and no boundary action. Each vertex has at most one marked incidence. Internal edges identify equal covariant labels.

Let \(\Psi(z_1,\ldots,z_r)\) be the maximum of the sum of all complete cubic actions and all ordinary profiles. Its domain is the projection of the closed linear support polytope, hence convex. The maximization is over a compact polytope. Concavity of the summands implies joint concavity of \(\Psi\) on its finite domain. The case \(r=0\) is just an ordinary complete region; no clamping is required.

**Half-boundary lemma.** If \(r\ge1\), the point \(\mathbf z=\tfrac12\mathbf1\) has a unique strict constrained optimizer. The pressure is analytic near that point and
\[
 \frac{\partial\Psi}{\partial z_i}
       (\tfrac12\mathbf1)\le0\quad(1\le i\le r).
 \tag{4}
\]
Consequently, for every feasible \(\mathbf z\) with \(z_i\ge1/2\),
\[
                  \Psi(\mathbf z)\le\Psi(\tfrac12\mathbf1).
 \tag{5}
\]
This is a simultaneous assertion. It does not assert coordinatewise monotonicity while other marked labels are held above one half.

## 2. Strict feasibility and the boundary barrier

Set every marked label to \(1/2\), every internal label to \(3/8\), and every ordinary boundary label to \(3/8\). A vertex without a marked incidence has triple \((3/8,3/8,3/8)\): its total is \(9/8\) and its pair sums are \(3/4\). A marked vertex has triple \((1/2,3/8,3/8)\): its total is \(5/4\) and its largest pair sum is \(7/8\). Both are strict. Ordinary leaf profiles are strict. This assignment remains feasible and strict when the marked labels vary in a small open box around \(1/2\).

Root the region at one marked incidence. Each complete vertex is now an ordinary binary product with output equal to one minus its outgoing covariant label; each internal edge supplies the physical turn between these output and input coordinates. Other marked incidences are fixed primitive terminals with label \(1/2\), and have no leaf volume atom. Ordinary terminals have the original leaf action \(g\).

The [boundary barrier](actual_positive_conway_hyperbolic_volume.md), Section 2, applies with this one change in the list of terminals. Join any boundary state to the strict state just constructed. A tetrahedron with angles \((0,a,1-a)\), \(0<a<1\), has directional derivative \(+\infty\) along this segment. A vertex-flat tetrahedron \((0,0,1)\) has a finite derivative; a positive tetrahedron has a finite derivative. Thus none can cancel a nonvertex-flat infinite derivative with a negative infinite term.

No variable wire at a maximum can equal zero or one. An output zero forces both product inputs zero. An output one either has two interior inputs summing to one, which gives a nonvertex-flat atom, or it has an endpoint child and the descent continues. Turns exchange zero and one. A finite descent cannot terminate at a marked terminal, because that terminal is fixed to \(1/2\). It must reach an ordinary leaf at zero, with its nonvertex-flat leaf atom, or an interior pair summing to one. The distinguished root output is fixed to \(1/2\) and cannot be the endpoint causing the descent. This excludes all variable endpoint wires. An ordinary leaf at \(1/2\) has its own nonvertex-flat atom and is also excluded. No atom is assigned to a fixed marked terminal; its prescribed half value is not being varied.

With every variable wire interior, each saturated gate inequality gives the same barrier as in the original strict source. In product coordinates put \(p=b-x,q=b-y,r=x+y-b,w=1-x-y\). If \(w=0\), the first tetrahedron has angles \((y,x,0)\). If \(r=0\), the third has \((b,0,1-b)\). If \(p=0,q>0\), the second has \((0,q,1-q)\); the case \(q=0,p>0\) is symmetric. If \(p=q=0\), the third has \((0,x,1-x)\). All are nonvertex-flat because the relevant wires are interior. Hence every retained gate at the constrained maximum is strict.

Each strict gate Hessian is negative definite in its three labels. Every free variable occurs at a gate. Thus their sum, together with the concave leaf Hessians, is negative definite on the constrained free-coordinate space. The maximum is unique. The implicit-function theorem gives an analytic critical branch under small independent variations of the marked labels; compactness and uniqueness show that it remains the maximum. This proves the asserted interiority and analyticity at the all-half assignment. It uses the existing tetrahedron barrier, not a claimed metric completion for an artificial terminal.

## 3. Boundary derivatives from the actual product equations

At a stationary subtree with output coordinate \(b\), write
\[
 B=\cot\pi b,\qquad \kappa=e^{-f'(b)},\qquad
 X^2=\frac{1+B^2}{1+\kappa},\qquad Y^2=\kappa X^2.
 \tag{6}
\]
At an ordinary leaf \(f=g\), these variables satisfy \(B=X>0,Y=1\). At a fixed marked half terminal there is no intrinsic profile derivative. Instead use its incident strict prism to define its positive boundary response: in an input coordinate take \(\kappa=e^{m_x}\), or the prescribed reciprocal after a turn. Since the terminal has \(B=0\), every such positive response gives
\[
                          -Y<0<X.
 \tag{7}
\]
This is all that is needed from that terminal. It is not an added physical leaf and carries no leaf action.

At internal variable wires the usual stationarity equations identify the child response with the reciprocal prism response. The [product derivative identities](actual_conway_strict_leaf_quarter_bound.md), Section 1, obtained by direct differentiation of the unchanged action, give a common positive \(X\) at a product, and, if \(B_1,B_2\) are its input cotangents,
\[
 B=\frac{B_1B_2+X^2-1}{B_1+B_2},\qquad
 Y=\frac{Y_1Y_2}{B_1+B_2},\qquad B_1+B_2>0.
 \tag{8}
\]
A turn takes \((B,X,Y)\) to \((-B,Y,X)\). In the rooted region an ordinary boundary is an input directly, with \(B=X,Y=1\); a fixed half terminal is a proper input by (7). Every product of these ordinary or proper inputs has a proper output \(-Y<B<X\). Only such completed product outputs are followed by internal physical turns, which preserve the proper condition. No turn of an uncompleted ordinary leaf is invoked. Indeed, rooting a covariant cubic at its outgoing incidence makes the output coordinate one minus that incidence, and each original physical-turn edge supplies exactly the subsequent complement before the next product. Thus this rooted induction is literal for the stated edge convention.

Here is the relevant product verification. The inputs obey \(-Y_i<B_i\le X\). If \(X\ge1\), then each \(B_i>0\) and \(B_i\ge\sqrt{X^2-1}\), with strict inequality for a proper input. Formula (8) gives \(B>0\), and
\[
 B-X=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0.
 \tag{9}
\]
If an input is an ordinary leaf its first factor is zero; otherwise each factor is less than \(X-\sqrt{X^2-1}\le1\). Thus the strict inequality holds, including \(X=1\). If \(0<X<1\), put \(h=\sqrt{1-X^2}\) and write
\(B_i=h\cot\alpha_i,Y_i=h\csc\alpha_i\), with \(0<\alpha_i<\pi\). The upper input bound gives \(\alpha_i\ge\arccos X>0\), and \(B_1+B_2>0\) gives \(\alpha_1+\alpha_2<\pi\). Equation (8) becomes
\(B=h\cot(\alpha_1+\alpha_2),Y=h\csc(\alpha_1+\alpha_2)\), proving \(-Y<B<X\). Turns exchange the two strict inequalities. This proves the needed bound \(B_i\le X\) at every input.

Now root the region separately at marked boundary \(i\), still with all marked labels equal to half. Its last product has output \(b=1-z_i=1/2\), so \(B=0\). Strict support makes its two input labels less than \(1/2\), hence \(B_1,B_2>0\). From (8) and the hyperboloid identity,
\[
 1-X^2=Y^2=B_1B_2\le X^2.
 \tag{10}
\]
The envelope derivative in this root output is therefore
\[
 f'_{\mathrm{out}}(1/2)=\log(X^2/Y^2)\ge0,
 \qquad
 \partial_{z_i}\Psi(\tfrac12\mathbf1)=-f'_{\mathrm{out}}(1/2)\le0.
 \tag{11}
\]
The fixed marked terminals elsewhere were used only through (7), so the argument works for every \(i\) on the same constrained maximum. Joint concavity and the supporting plane at the all-half point now give
\[
 \Psi(\mathbf z)\le\Psi(\tfrac12\mathbf1)
    +\sum_i\partial_{z_i}\Psi(\tfrac12\mathbf1)(z_i-1/2)
 \le\Psi(\tfrac12\mathbf1).
 \tag{12}
\]
This proves the half-boundary lemma, including arbitrary feasible boundary points by continuity of the supporting inequality.

## 4. Where the additional trace terms can occur

The fixed Newton basis and the normalized trace were defined above. At completeness the three-input tensor is supported on
\(i+j,i+k,j+k\le d\) and \(i+j+k\ge d\). Its logarithmic rate is (2). The exact polynomial calculation in Appendix A proves that the difference from this complete tensor has support
\[
 i+j,\ i+k,\ j+k\ge N,\qquad i+j+k\ge2N-1.
 \tag{13}
\]
Writing \(t_0=i+j+k-(2N-1)\), it is exactly
\[
 V_{\mathrm{ret}}(i,j,k)
 =-\Delta_s(-1)^{i+j+k-d}
 \frac{N^2}{S_iS_jS_kS_{t_0}S_{i-t_0}S_{j-t_0}S_{k-t_0}}.
 \tag{14}
\]
For the finite-to-continuous rate comparison use \(d=N-1\) and complementary variables \(a=1-i/d,b=1-j/d,c=1-k/d\). The exact additional support then gives \(a,b,c\ge0\) and \(a+b+c\le1-1/d\), so every argument below lies in the real domain of \(J\). Its absolute closed rate is
\[
 \mathcal R(a,b,c)
 =J(a)+J(b)+J(c)+J(a+b+c)
              -J(a+b)-J(a+c)-J(b+c)
 =-\pi^2\int_0^a\int_0^b\int_0^c
               \csc^2\pi(u+v+w)\,dw\,dv\,du\le0.
 \tag{15}
\]
To justify the integral, first translate the arguments of \(J\) by a small positive number and keep \(a+b+c<1\). Three applications of the fundamental theorem of calculus give the finite difference in (15), since \(J^{(3)}(u)=-\pi^2\csc^2(\pi u)\). Passing to the limit is legitimate at the origin, and at the opposite corner when the total is one: the inverse-square singularity is integrable in three dimensions. Continuity gives the result on the closed domain. In particular it is strictly negative when all three complementary labels are positive, but only nonpositivity is used in the whole-component comparison.

Replacing the factorial arguments divided by \(N\) by these \(d\)-normalized arguments changes each by \(O(1/N)\). The endpoint modulus of continuity of \(J\) is \(O(\varepsilon\log(1/\varepsilon))\); hence uniform closed factorial rates still have only \(O(\log N)\) error in the logarithm. In particular, no finite tuple with complementary sum \(1+1/N\) is substituted into (15). The exact coefficient itself is uniformly polynomially bounded after its displayed common \(\Delta_s\) factor. This retains every endpoint and repeated-root normal.

In the [actual six-type table](actual_main_meridian_turn_comparison.md#the-six-ordered-orientation-types) an equal-color endomorphism turns into an opposite-order mixed morphism, and the next turn into the other equal-color endomorphism; the two opposite-color endomorphism spaces turn into one another. Only the equal-color endomorphism classes have moving relations. Thus two moving vertices cannot be joined by an original physical turn. Compatible products share their Casimir class. Vertices carrying an additional term must be moving, and consequently form an independent set in the original reduced trivalent tree.

A vertex carrying an additional term has at least two high incidences, where high means the exact index exceeds \(M_N=\lfloor d/2\rfloor\). A complete vertex has at most one. In a closed limiting sector, retain which incidences were high before taking the limit; those recorded labels may become exactly half. An additional term with two recorded high arms has one remaining low arm; an additional term with three has none. This convention prevents false counts at tied endpoints.

## 5. Replacing the additional terms simultaneously

Consider one trivalent component after its output has been closed against the comparison probe with effective boundary profiles \(g+c_i\) on low indices and \(c_i\) on high indices. Its complete positive comparison replaces all boundaries by their pure profiles \(g+c_i\). Assume the original strict-source hypotheses, so that this complete reference has a compact support polytope, a unique strict maximizing state, and action \(F_0\). For an open component closed by the probe, this \(F_0\) is precisely \(\Omega_Q\) in (T3). The output probe is one of these effective boundary profiles when bounding an open component.

Fix a sector containing at least one additional term, including its recorded high/low pattern. Remove every vertex carrying an additional term. Since vertices carrying additional terms are nonadjacent, every remaining edge from an additional term ends either at a complete region or directly at an original boundary leaf. Mark each high incidence on a complete region, including any high original external boundary. There is at most one such marked incidence at each complete vertex, by complete support.

A low arm of an additional term requires special accounting. After its two high arms are clamped to half, the replacement complete vertex has action
\[
                         t(1/2,1/2,x)=g(x)\ge0.
 \tag{16}
\]
For the identity in (16), the left side reduces to \(2J(1/2+x)-2J(x)\). Its derivative is \(2\log\cot(\pi x)=g'(x)\), and both functions vanish at zero. Continuity includes both endpoints.

If that low arm ends in a complete region, regard this additional \(g(x)\) as an ordinary boundary profile of that region and optimize \(x\) there. At the starting sector state this adds a nonnegative amount, whereas the discarded additional-term action is nonpositive. Because vertices carrying additional terms are nonadjacent, the low arm belongs to exactly one complete region and this \(g\) is counted exactly once.

If a low arm ends directly in an original low boundary leaf, retain its original label or optimize it independently. The new complete vertex and original boundary contribute \(g(x)+g(x)+c\), at least the complete boundary contribution \(g(x)+c\). A high original boundary incidence is replaced by half; its original high profile is \(c\), and the new pure boundary profile is \(g(1/2)+c=c\). An additional term with three high arms becomes \((1/2,1/2,1/2)\), whose complete action is zero. No boundary constant is lost.

Apply the half-boundary lemma to each complete region, including the new pure low-arm profiles just described. It jointly reoptimizes that region at all its marked half boundaries, with action at least its previous complete action plus the assigned nonnegative profiles. Regions without any marked boundary can simply be optimized with their ordinary profiles. Distinct regions have disjoint free variables. Their low-arm values are determined by their own optimizers; each is used by exactly one replaced vertex carrying an additional term. All high interfaces agree at half.

Reassemble the unchanged tree. At every replaced vertex carrying an additional term use either \((1/2,1/2,x)\) with the optimized adjacent low-arm value, or \((1/2,1/2,1/2)\). These are feasible complete triples. Equation (16) makes their action exactly the profile assigned to the adjacent complete region, not an extra copy. Every remaining vertex is a complete feasible vertex, and each original boundary now has a feasible pure label. The total action of the resulting complete state is at least the action of the entire original sector after absolute values have been taken.

At least one replaced vertex has a pair sum equal to one. The resulting state therefore lies in the fixed complete boundary stratum
\[
 \mathcal B=\{\text{complete feasible states with at least one retained
                         cubic pair sum equal to }1\}.
 \tag{17}
\]
The original maximizing state is strict. Compactness gives
\[
                    \delta=F_0-\max_{\mathcal B}\mathcal A_0>0.
 \tag{18}
\]
Thus every sector containing an additional term has absolute action at most \(F_0-\delta\). This uses a feasible comparison state in the same coupled complete source. It does not add separately optimized caps or assign a representation to a stationary point of the absolute additional-term action.

All endpoint and exact-half configurations are included. The record of finite high incidences gives at most one marked incidence per complete vertex and at least two per vertex carrying an additional term; it persists in the closed sector. The entropy functions are continuous on their closed domains. Equation (12) applies to closed feasible boundary values, so no limiting division by a zero sine or a strict-label counting shortcut is needed.

## 6. Consequence for the finite source and the remaining scope

At a fixed finite trivalent component there are finitely many choices between complete and additional terms and polynomially many integer states. The paired edge factors and all prescribed typed scalars are bounded on \(|s|\le R<1\). Uniform closed coefficient rates and (18) therefore bound the entire absolute sum of all nonempty additional-term sectors by
\[
                         e^{N(F_0-\delta+o(1))}.
 \tag{19}
\]
No cancellation between additional terms is used for this estimate. In sectors with no additional term, the bounded paired weights are compared termwise with the original positive complete contraction. A high original boundary input or high output probe has the complete-component strict gap. This is the [complete coefficient-probe theorem](actual_conway_unflagged_core_probe_bound.md); it permits low rates \(g+c\) and high rates \(c\). Thus the component has its original full norm budget, and its clean part retains all complete-supported internal labels while keeping its boundary inputs and output low. The remainder has a strict spectral deficit. Inherited full-cone deficits pass by affine homogeneity in the constants, as in the [grouped-error argument](actual_main_meridian_component_extension.md), Section 6. The [global trivalent extension](actual_main_meridian_trivalent_filled_volume.md) proves the remaining source-to-window and filling interfaces.

Near the original strict maximizing state, every cubic has total normalized degree less than \(3/2\). Consequently its raw polynomial trace has degree less than \(2N-1\) on a fixed window, and the moving trace equals the complete trace exactly there. The internal labels in this regular neighborhood may cross half, but stay in a compact subinterval of \((0,1)\), where the canonical paired-edge interpolation is regular. Circle-incident labels remain in the original regular low interval. These are the local inputs for the grouped-window argument; no high cutoff is imposed on bare–bare edges.

The theorem established here is a component comparison for arbitrary-size **trivalent** bare components in the actual typed tree. It is independent of the earlier many-boundary condition. It can coexist with singleton higher-valence components and other already controlled components in the mutual source induction. The [global theorem](actual_main_meridian_trivalent_filled_volume.md) supplies the additional conditioned window, joint filling contour and marked scalar arguments required for the volume and meridian-profile conclusions. Those conclusions do not follow from the component norm bound alone.

Higher-valence bare components are not settled by this proof. Their binary resolutions have unturned complementary-label edges, on which adjacent moving vertices carrying an additional term can occur. A raw low higher-valence product can also have an additional trace term without a high exterior incidence. The nonadjacency and unique-low-arm accounting above must not be applied to such artificial resolutions.

## Appendix A. The exact additional tensor and its endpoint bounds

The finite calculation below justifies the tensor used in Section 4 before any exponential estimate is taken. It takes place in fixed polynomial coordinates, so it includes the full repeated-root information.

### A.1. The polynomial quotient producing the additional term

Fix
\[
N\ge2,\quad d=N-1,\quad \theta=\pi/N,\quad
c_j=2\cos((2j+1)\theta),\quad
S_n=\prod_{r=1}^n2\sin(r\theta),\quad S_0=1.
\]
Put
\[
B_n(z)=\prod_{j=0}^{n-1}(c_j-z),\qquad e_n=B_n/S_n^2,
\qquad P_0(z)=\mathcal T_N(z)+2.
\]
Here \(\mathcal T_N(2\cos t)=2\cos Nt\). The actual same-color quotient at meridian displacement \(s\) has relation
\[
P_s=P_0+\Delta_s,\qquad \Delta_s=2\cos(2\pi s)-2.
\tag{A1}
\]
The coefficients below are in the fixed basis \(e_0,\ldots,e_d\), not in the moving basis. All equalities are polynomial quotient equalities and therefore retain every repeated-node normal.

For canonical polynomials \(f,g\), one division gives
\[
fg=P_0Q+R,\qquad \deg R<N,\quad\deg Q\le N-2,
\qquad f*_sg=R-\Delta_sQ.
\tag{A2}
\]
Thus the change of multiplication is affine in \(\Delta_s\). When \(i+j<N\), the product \(e_ie_j\) has degree less than \(N\), and its fixed-basis coefficients are exactly the positive complete coefficients. When \(i+j\ge N\), the complete product is divisible by \(P_0\).

Indeed \(c_{d-j}=c_j\), so
\[
B_iB_{N-i}=B_N=(-1)^NP_0.
\]
Assume \(i\ge j\) and set
\[
a=N-i,\quad b=N-j,\quad h=i+j-N=N-a-b\ge0.
\]
Then \(j\ge a\), and the quotient producing the additional term is the ordinary polynomial
\[
Q_{ij}=\frac{e_ie_j}{P_0}
=\frac{(-1)^N}{S_i^2S_j^2}
       \prod_{r=a}^{j-1}(c_r-z).
\tag{A3}
\]
Its degree is \(h\le N-2\). Consequently
\[
e_i*_se_j=-\Delta_sQ_{ij}.
\tag{A4}
\]
This exact divisibility is special to the complete fixed basis. It is different from the nonzero first derivative of multiplication coefficients in moving coordinates.

### A.2. An exact alternating Newton expansion

The quotient in (A3) has the expansion
\[
\boxed{\quad
Q_{ij}=\sum_{k=0}^{h}(-1)^{N+h-k}\Lambda_{ijk}e_k,
\qquad
\Lambda_{ijk}=
\frac{S_hS_k}
 {S_iS_jS_{h-k}S_{a+k}S_{b+k}}>0.
\quad}
\tag{A5}
\]
Every factorial in (A5) has index between zero and \(d\).

Here is a direct derivation from the [finite factorial connection](actual_main_meridian_newton_compiler.md), Sections 2–3. The interval polynomial in (A3) is \(B_h(-a,z)\), since shifting the meridian parameter by \(-a\) changes \(c_r\) into \(c_{r+a}\). In the finite connection, take \(p=q^2\), initial parameter \(q p^a\), and target parameter \(q\). If \(m=h-k\), cancellation gives
\[
B_h(-a,z)=S_h^2\sum_{k=0}^h C_{hk}e_k,
\qquad
C_{hk}=(-1)^m
\frac{S_kS_jS_{j-k-1}}
 {S_hS_mS_{a+k}S_{a-1}}.
\tag{A6}
\]
For completeness, the two finite Pochhammer products have indices
\(a+k+1,\ldots,a+h\) and \(a,\ldots,a+m-1\). Each factor
\(1-q^{2r}=-iq^r(2\sin r\theta)\). Their combined phase is
\((-1)^m q^{m(2a+h)}\). The connection prefactor and the Gaussian binomial have inverse phase \(q^{-m(2a+h)}\), leaving precisely \((-1)^m\). This argument includes \(m=0\) by empty products.

Use
\[
S_iS_{a-1}=N,\qquad S_{j-k-1}S_{b+k}=N.
\]
Substitution of (A6) into (A3) gives (A5), including its sign and normalization. The finite connection is a polynomial identity; no division by a sampled Casimir difference is used.

The complete turn reverses the fixed basis, so
\[
T_0Q_{ij}=\sum_{k=0}^{h}(-1)^{N+h-k}\Lambda_{ijk}e_{d-k}.
\tag{A7}
\]
The [actual fixed-frame typed turn](actual_main_meridian_turn_comparison.md) multiplies each displayed term by its retained Gaussian scalar and \(W_k(s)/H_N(s)\). These factors and their inverses are uniformly bounded on every fixed \(|s|\le R<1\). The alternating sum in (A7) remains present.

### A.3. Uniform polynomial size, including all endpoints

The individual positive numbers in (A5) obey
\[
\Lambda_{ijk}\le C N^2
\tag{A8}
\]
for one absolute constant, every level, and every admissible \(i,j,k\).

First,
\[
\Lambda_{ij0}=
\frac1{N^2(2\sin a\theta)(2\sin b\theta)}\le\frac1{16}.
\tag{A9}
\]
For \(1\le k\le h\), the exact consecutive ratio is
\[
\frac{\Lambda_{ijk}}{\Lambda_{ij,k-1}}
=\frac{\sin(k\theta)\sin((a+b+k-1)\theta)}
 {\sin((a+k)\theta)\sin((b+k)\theta)}.
\tag{A10}
\]
The elementary identity
\[
\sin((a+k)\theta)\sin((b+k)\theta)
-\sin(k\theta)\sin((a+b+k)\theta)
=\sin(a\theta)\sin(b\theta)>0
\tag{A11}
\]
therefore implies, when \(k<h\),
\[
\Lambda_{ijk}
\le\Lambda_{ij0}
\frac{\sin((a+b)\theta)}{\sin((a+b+k)\theta)}
\le\frac N{32}.
\tag{A12}
\]
The first inequality follows by multiplying (A10) and telescoping the one-step sine shifts. At the final index, if \(h\ge1\), retain its last ratio separately:
\[
\Lambda_{ijh}
\le\Lambda_{ij0}
 \frac{\sin^2((a+b)\theta)}{\sin(a\theta)\sin(b\theta)}
\le\frac{N^2}{64}.
\tag{A13}
\]
The case \(h=0\) is (A9). We used only
\(\sin(r\theta)\ge\sin\theta\ge2/N\) for \(1\le r<N\).
Thus no endpoint can conceal an exponential factor.

This bounds the coefficients of the additional quotient in fixed coordinates. It is not a bound for the positive Newton coefficient norm after all later operations: the basis element \(e_{d-k}\) itself can have exponential spectral size, and the alternating signs in (A7) can matter.

### A.4. The symmetric three-input tensor

Let the fixed closing functional be
\[
\begin{aligned}
\phi_s(F)&=(-1)^dN^2\operatorname{coeff}_{z^d}F.
\end{aligned}\tag{A14}
\]
for the canonical representative modulo \(P_s\). At every \(s\),
\[
\phi_s(e_i*_se_j)=\delta_{i+j,d}.
\tag{A15}
\]
For \(i+j<d\), this follows from degree. At \(i+j=d\), it uses
\(S_iS_j=N\). At \(i+j\ge N\), that quotient has degree at most \(N-2\), so its top coefficient is zero. Thus the Frobenius metric is the same anti-diagonal matrix in these fixed coordinates.

Define the covariant, symmetric vertex tensor
\[
V_s(i,j,r)=\phi_s(e_i*_se_j*_se_r).
\tag{A16}
\]
Its complete part is supported on
\[
i+j,\ i+r,\ j+r\le d,\qquad i+j+r\ge d,
\]
and there the [positive Newton multiplication formula](actual_main_meridian_newton_multiplication.md), Section 3, gives
\[
V_0(i,j,r)=
\frac{S_{i+j}S_{i+r}S_{j+r}}
 {N S_iS_jS_r S_{i+j+r-d}}.
\tag{A17}
\]
The only additional support is
\[
i+j,\ i+r,\ j+r\ge N,\qquad i+j+r\ge2N-1.
\tag{A18}
\]
On (A18),
\[
\boxed{\quad
V_s(i,j,r)
=-\Delta_s(-1)^{i+j+r-d}
\frac{S_{i+j-N}S_{i+r-N}S_{j+r-N}}
 {N S_iS_jS_r S_{i+j+r-2N+1}}.
\quad}
\tag{A19}
\]
Elsewhere it is zero. To prove (A19), use (A5) and the metric (A15): the sole coefficient selected is \(k=d-r\). The resulting expression is symmetric after the sine-product reflection. This also proves that the listed support is independent of which two inputs are multiplied first.

Equivalently, writing \(t=i+j+r-(2N-1)\ge0\), the positive coefficient in (A19) is
\[
\Lambda(i,j,r)=
\frac{N^2}
 {S_iS_jS_r S_t S_{i-t}S_{j-t}S_{r-t}}.
\tag{A20}
\]
This is the same number as (A5), with \(k=d-r\). It has the uniform bound (A8).

There is an important convention for a network built from (A16). In this fully covariant tensor convention, an unturned composition contracts **complementary** incident labels, through the inverse metric (A15). Inserting the complete reversal changes this to **equal** incident labels. At a deformed typed turn there is an additional bounded diagonal paired factor. Thus the edges of a reduced-hub tree, which carry turns, join equal cubic labels. In the alternative raw product input/output convention, a turn reverses the output label; these statements are compatible but must not be interchanged in a flow argument.

The complements of the three labels in (A18) have total at most \(d-1\). They satisfy the complete pair-sum inequalities but fail its required total at least \(d\). Thus complementing the labels does not turn the additional tensor into a complete positive tensor: the required total-degree condition fails.



## Reproducing the finite calculations

Run the dedicated group from the repository root:

```sh
python3 repro/run_research_checks.py trivalent-components
```

The [program](../experiments/audit_main_meridian_trivalent_components.py) constructs the original Newton polynomials over exact cyclotomic fields, divides their products by \(P_0+\Delta\), and extracts the closing trace. It then compares that independently obtained trace with the complete and additional tensor formulas. The [saved results](../experiments/trivalent_return_comparison_results.json) cover levels two through ten, including old supported triples with an internal index above one half and the smallest possible total degree in the additional support. The program also checks the unchanged pairing, the endpoint permutation of the six physical types, and the elementary algebra used in the boundary derivative.

Python and SymPy are sufficient. These are finite algebraic checks. The simultaneous inequality, the strict exponential gap, and the passage to the filled volume are proved in the text and its companion theorem.
