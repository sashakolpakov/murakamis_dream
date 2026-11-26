# Simultaneous half-boundary clamping for typed trivalent bare components

Private derivation, 1 November 2026. No repository changes.

This proof retains all labels on internal edges of a bare component. The complete maximum need not put such a label below one half. It instead compares every genuine return sector with a boundary stratum of the original complete positive source. The comparison reoptimizes each intervening old region jointly. Its essential source restriction is that every bare vertex is trivalent and every internal edge is an original physical quarter-turn. Actual orientation types then make return vertices nonadjacent.

## 1. The old cubic action and a constrained region

Let
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 g(x)=J(2x)-4J(x),\quad 0\le x\le\tfrac12.
 \tag{1}
\]
The old symmetric cubic action is
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
Its strict domain has all three labels positive, all pair sums less than one, and total greater than one. Writing its third covariant label as \(z=1-b\) identifies (2) with the original product action \(m(x,y,b)\). Thus it is concave, continuous on (3), and has negative definite Hessian in the strict domain, by the original three-tetrahedron decomposition.

Consider a finite connected tree of old trivalent vertices. Its external incidences have two kinds. An ordinary incidence carries the profile \(g(a)\) with freely varying \(a\in[0,1/2]\); additive constants may be retained separately. A marked incidence has a prescribed label \(z_i\) and no boundary action. Each vertex has at most one marked incidence. Internal edges identify equal covariant labels.

Let \(\Psi(z_1,\ldots,z_r)\) be the maximum of the sum of all old cubic actions and all ordinary profiles. Its domain is the projection of the closed linear support polytope, hence convex. The maximization is over a compact polytope. Concavity of the summands implies joint concavity of \(\Psi\) on its finite domain. The case \(r=0\) is just an ordinary old region; no clamping is required.

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

Root the region at one marked incidence. Each old vertex is now an ordinary binary product with output equal to one minus its outgoing covariant label; each internal edge supplies the physical turn between these output and input coordinates. Other marked incidences are fixed primitive terminals with label \(1/2\), and have no leaf volume atom. Ordinary terminals have the original leaf action \(g\).

The old boundary barrier applies with this one change in the list of terminals. Join any boundary state to the strict state just constructed. A tetrahedron with angles \((0,a,1-a)\), \(0<a<1\), has directional derivative \(+\infty\) along this segment. A vertex-flat tetrahedron \((0,0,1)\) has a finite derivative; a positive tetrahedron has a finite derivative. Thus none can cancel a nonvertex-flat infinite derivative with a negative infinite term.

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

At internal variable wires the usual stationarity equations identify the child response with the reciprocal prism response. Direct differentiation of the unchanged action gives a common positive \(X\) at a product, and, if \(B_1,B_2\) are its input cotangents,
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

## 4. Exact return sectors and actual orientation types

For the fixed Newton basis, the old cubic tensor is supported on
\(i+j,i+k,j+k\le d\) and \(i+j+k\ge d\). Its action is (2). The extra tensor has support
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
For the finite-to-continuous rate comparison use \(d=N-1\) and complementary variables \(a=1-i/d,b=1-j/d,c=1-k/d\). Exact return support then gives \(a,b,c\ge0\) and \(a+b+c\le1-1/d\), so every argument below lies in the real domain of \(J\). Its absolute closed rate is
\[
 \mathcal R(a,b,c)
 =J(a)+J(b)+J(c)+J(a+b+c)
              -J(a+b)-J(a+c)-J(b+c)
 =-\pi^2\int_0^a\int_0^b\int_0^c
               \csc^2\pi(u+v+w)\,dw\,dv\,du\le0.
 \tag{15}
\]
Replacing the factorial arguments divided by \(N\) by these \(d\)-normalized arguments changes each by \(O(1/N)\). The endpoint modulus of continuity of \(J\) is \(O(\varepsilon\log(1/\varepsilon))\); hence uniform closed factorial rates still have only \(O(\log N)\) error in the logarithm. In particular, no finite tuple with complementary sum \(1+1/N\) is substituted into (15). The exact coefficient itself is uniformly polynomially bounded after its displayed common \(\Delta_s\) factor. This retains every endpoint and repeated-root normal.

In the actual six-type table an equal-color endomorphism turns into an opposite-order mixed morphism, and the next turn into the other equal-color endomorphism; the two opposite-color endomorphism spaces turn into one another. Only the equal-color endomorphism classes have moving relations. Thus two moving vertices cannot be joined by an original physical turn. Compatible products share their Casimir class. Return vertices, which must be moving, consequently form an independent set in the original reduced trivalent tree.

A return vertex has at least two high incidences, where high means the exact index exceeds \(M_N=\lfloor d/2\rfloor\). An old vertex has at most one. In a closed limiting sector, retain which incidences were high before taking the limit; those recorded labels may become exactly half. A return with two recorded high arms has one remaining low arm; a return with three has none. This convention prevents false counts at tied endpoints.

## 5. Replacing all returns at once, including their low arms

Consider one closed trivalent component with effective boundary profiles \(g+c_i\) on low indices and \(c_i\) on high indices. Its pure old comparison replaces all boundaries by their full pure profiles \(g+c_i\). Assume the original strict-source hypotheses, so that this old reference has a compact support polytope, a unique strict maximizing state, and action \(F_0\). The output probe is one of these effective boundary profiles when bounding an open component.

Fix a sector containing at least one return, including its recorded high/low pattern. Remove every return vertex. Since returns are nonadjacent, every remaining edge from a return ends either at an old region or directly at an original boundary leaf. Mark each high incidence on an old region, including any high original external boundary. There is at most one such marked incidence at each old vertex, by old support.

A low arm of a return requires special accounting. After its two high arms are clamped to half, the replacement old vertex has action
\[
                         t(1/2,1/2,x)=g(x)\ge0.
 \tag{16}
\]
If that low arm ends in an old region, regard this additional \(g(x)\) as an ordinary boundary profile of that region and optimize \(x\) there. At the starting returned state this adds a nonnegative amount, whereas the discarded return action is nonpositive. Because returns are nonadjacent, the low arm belongs to exactly one old region and this \(g\) is counted exactly once.

If a low arm ends directly in an original low boundary leaf, retain its original label or optimize it independently. The new old vertex and original boundary contribute \(g(x)+g(x)+c\), at least the old boundary contribution \(g(x)+c\). A high original boundary incidence is replaced by half; its original high profile is \(c\), and the new pure boundary profile is \(g(1/2)+c=c\). A return with three high arms becomes \((1/2,1/2,1/2)\), whose old action is zero. No boundary constant is lost.

Apply the half-boundary lemma to each old region, including the new pure low-arm profiles just described. It jointly reoptimizes that region at all its marked half boundaries, with action at least its previous old action plus the assigned nonnegative profiles. Regions without any marked boundary can simply be optimized with their ordinary profiles. Distinct regions have disjoint free variables. Their low-arm values are determined by their own optimizers; each is used by exactly one replaced return vertex. All high interfaces agree at half.

Reassemble the unchanged tree. At every replaced return vertex use either \((1/2,1/2,x)\) with the optimized adjacent low-arm value, or \((1/2,1/2,1/2)\). These are feasible old triples. Equation (16) makes their action exactly the profile assigned to the adjacent old region, not an extra copy. Every remaining vertex is an old feasible vertex, and each original boundary now has a feasible pure label. The total action of the resulting old state is at least the entire absolute return-sector action.

At least one replaced vertex has a pair sum equal to one. The resulting state therefore lies in the fixed old boundary stratum
\[
 \mathcal B=\{\text{old feasible states with at least one retained
                         cubic pair sum equal to }1\}.
 \tag{17}
\]
The original maximizing state is strict. Compactness gives
\[
                    \delta=F_0-\max_{\mathcal B}\mathcal A_0>0.
 \tag{18}
\]
Thus every nonempty return sector has absolute action at most \(F_0-\delta\). This uses a feasible comparison state in the same coupled old source. It does not add separately optimized caps or assign a representation to an absolute stationary return state.

All endpoint and exact-half configurations are included. The record of finite high incidences gives at most one marked incidence per old vertex and at least two per return vertex; it persists in the closed sector. The entropy functions are continuous on their closed domains. Equation (12) applies to closed feasible boundary values, so no limiting division by a zero sine or a strict-label counting shortcut is needed.

## 6. Consequence for the finite source and the remaining scope

At a fixed finite trivalent component there are finitely many old/return assignments and polynomially many integer states. The paired edge factors and all prescribed typed scalars are bounded on \(|s|\le R<1\). Uniform closed coefficient rates and (18) therefore bound the entire absolute sum of all nonempty return sectors by
\[
                         e^{N(F_0-\delta+o(1))}.
 \tag{19}
\]
No return cancellation is used for this estimate. In sectors without returns, the bounded paired weights are compared termwise with the original positive complete contraction. A high original boundary input or high output probe has the old complete-component strict gap. This is the arbitrary-array theorem in `notes/actual_conway_unflagged_core_probe_bound.md`; it permits low rates \(g+c\) and high rates \(c\). Thus the component has its original full norm budget, and its clean part retains all old-supported internal labels while keeping its boundary inputs and output low. The remainder has a strict spectral deficit. Inherited full-cone deficits pass by affine homogeneity in the constants, as in the published component refinement.

Near the original strict maximizing state, every cubic has total normalized degree less than \(3/2\). Consequently its raw polynomial trace has degree less than \(2N-1\) on a fixed window, and the moving trace equals the complete trace exactly there. The regular internal labels may cross half, but stay in a compact subinterval of \((0,1)\), where the canonical paired-edge interpolation is regular. Circle-incident labels remain in the original regular low interval. These are the corrected local inputs for the grouped-window argument; no high cutoff is imposed on bare–bare edges.

The theorem established here is a component comparison for arbitrary-size **trivalent** bare components in the actual typed tree. It is independent of the earlier many-boundary condition. It can coexist with singleton higher-valence components and other already controlled components in the mutual source induction. A full filled theorem still requires stating this enlarged class in the global source-to-window argument and retaining the joint filling contour and exact scalar ledger; those are not republished or modified here.

Higher-valence bare components are not settled by this proof. Their binary resolutions have unturned complementary-label edges, on which adjacent moving return vertices can occur. A raw low higher-valence product can also have a return trace without a high exterior incidence. The independent-return and unique-low-arm accounting above must not be applied to such artificial resolutions.
