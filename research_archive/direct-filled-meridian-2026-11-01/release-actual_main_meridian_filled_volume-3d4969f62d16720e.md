# The meridian profile and volume for Conway knots with long twists

1 November 2026.

This proof concerns the actual reduced ADO invariant of a filled knot, with its zero framing and its prescribed meridian coordinate. The meridian moves by an amount of order \(1/N\), while the quantum parameter remains at the exact \(2N\)-th root of unity. For the class of presentations described below, the invariant has a nonzero asymptotic on every fixed microscopic disk before the first ordinary-color resonance. Its logarithmic growth is the volume of the resulting knot complement.

The proof keeps the whole finite quantum sum. It obtains a nonzero leading term by treating the Fourier variables for all filled circles together. The geometric input is the original strict augmented geometry, its marked deformation and its smooth long fillings. The resulting volume is the volume of the knot complement after the auxiliary crossing circles have been filled; the knot cusp itself remains unfilled.

## 1. The presentations and the theorem

Start with one fixed literal closed Conway construction in ordered products, physical quarter-turns and the original crossing-circle leaves. Its endpoint orders, knot pattern and local disk framings are fixed. Assume its positive wire domain has a strict state: original leaf parameters lie in \((0,1/2)\), and each retained multiplication gate satisfies
\[
                 \max(x,y)<z<x+y<1.
 \tag{1}
\]
Only the forced final flat gate is deleted, with its exact complementary-index relation retained. The original geometric construction then gives a complete augmented exterior with a unique strict positive source optimizer. We retain the original knot/component qualifications; in particular the strict two-leaf knot case includes a pure leaf, rather than the two-odd-leaf link pattern.

There is a useful graph description of the additional condition in this theorem. Collapse consecutive multiplications with no intervening turn into a product junction. Each edge of the resulting tree carries a physical quarter-turn. A junction is **marked by a circle operator** if it contains one original crossing-circle operator; an ordinary original leaf is such a vertex of valence one. A **bare junction** contains none. This is a tree of source operations, not a new knot diagram or a permission to commute arbitrary tangles.

The theorem includes trees with no adjacent bare junctions. More generally, let \(\mathcal U\) be a maximal connected component of bare junctions. A singleton component may have any allowed valence. For every nonsingleton component, let \(b_v\) be the number of incident boundary branches at its vertex \(v\), after the component's internal edges are removed. These are the rigid branches supplied by the neighboring circle-marked parts of the tree. Require \(b_v\ge5\) and the finite path inequality
\[
 \max_{\mathcal P\text{ a simple path in }\mathcal U}
       \sum_{v\in\mathcal P}\varepsilon_{b_v-1}<2G_0,
 \qquad
 \varepsilon_k=(k+1)
 \left[
 J\left(\frac14+\frac1{k+1}\right)
 +J\left(\frac14-\frac1{k+1}\right)-2J\left(\frac14\right)
 \right],
 \tag{2}
\]
where
\[
 J(x)=\int_0^x\log(2\sin\pi u)\,du,\qquad
 g(x)=J(2x)-4J(x),\qquad G_0=g(1/4).
 \tag{3}
\]
A simpler sufficient condition is \(b_v\ge\max(8,4|\mathcal U|)\) at every vertex of each nonsingleton component. Condition (2) controls the loss accumulated when an error passes through adjacent bare products. It is a condition on the fixed finite presentation, not on the level \(N\) or on a filling slope.

At circle \(i\), retain the original parity representative \(\epsilon_i\in\{0,\pm1\}\) and fill that auxiliary cusp with the integer disk-filling coefficient \(p_i\). The remaining physical crossing power is exactly
\[
                         n_i=\epsilon_i-2p_i.
 \tag{4}
\]
Thus all allowed \(n_i\) have their prescribed parity. The resulting knot is denoted by \(K_{\mathbf n}\). Every auxiliary circle is filled in this statement; the main knot cusp stays unfilled.

There is a single constant \(B\), depending on the fixed strict presentation and its original knot/parity conventions, such that the following holds whenever all the fixed signed integers \(n_i\) satisfy \(|n_i|\ge B\). Their signs are independent, and no ratio between their absolute values is bounded. They and the presentation are fixed before \(N\) tends to infinity. The constant \(B\) is independent of the subsequently chosen radius \(0\le R<1\).

Put \(q_N=e^{\pi i/N}\). Let \(F_N(M)\) be the actual zero-framed reduced ADO invariant of \(K_{\mathbf n}\), in the marked coordinate \(M\), with unknot value one. Section 2 fixes this normalization and defines an explicit scalar \(A_N(s)\) from the original finite compiler. Then, uniformly for \(|s|\le R<1\), through both even and odd levels,
\[
 \boxed{\displaystyle
 \frac{F_N(q_N^s)}{F_N(1)}
        =A_N(s)H_N(s)\bigl(1+O_{\mathbf n,R}(N^{-1})\bigr),
 \qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\quad H_N(0)=1.}
 \tag{5}
\]
The denominator \(F_N(1)\) is nonzero for every sufficiently large level. The right side is also uniformly nonzero on the stated disk for large \(N\). Moreover,
\[
 \boxed{\displaystyle
 \sup_{|s|\le R}
 \left|\frac{2\pi}{N}\log|F_N(q_N^s)|
       -\operatorname{Vol}(S^3\setminus K_{\mathbf n})\right|
                      \longrightarrow0.}
 \tag{6}
\]
The starting level and the error constants may depend on the fixed integers \(\mathbf n\) and on \(R\). The threshold \(B\) does not.

There is a precise first correction after the exact scalar factors are divided out. If \(x_e^{\mathrm{fill}}\) is the generally complex normalized label of physical edge \(e\) at the selected filled joint saddle, then
\[
 \frac{F_N(q_N^s)}
      {F_N(1)A_N(s)H_N(s)}
  =1-\frac{\pi s^2}{N}
                 \sum_e\cot(\pi x_e^{\mathrm{fill}})
                      +O_{\mathbf n,R}(N^{-2}).
 \tag{7}
\]
The sum is over the physical turn edges, not the artificial edges introduced when resolving a bare product into binary gates. It is evaluated at the filled saddle, not at the complete augmented optimizer. Formula (7) makes no identification with a cusp shape or with a classical \(A\)-polynomial factor.

## 2. The actual invariant and its scalar factors

Set \(d=N-1\). The actual color module has highest weight \(\alpha=d+s\), with highest-root coordinate \(x=q_N^\alpha\). The marked meridian is
\[
                 M=-q_Nx=q_N^s.
 \tag{8}
\]
In particular \(s=0\) is the complete marked value \(M=1\), not \(M=-1\). Use the original finite quantum-group crossing, pivotal matrix \(K^{1-N}\), and ribbon twist
\[
       \theta_\alpha
          =q_N^{(\alpha^2+2(1-N)\alpha)/2}.
 \tag{9}
\]
The reduced \((1,1)\)-tangle scalar, corrected to zero framing, is \(F_N(M)\). It is equivalently the full modified-trace ADO invariant divided by its modified dimension. It is not obtained by dividing an already reduced cut scalar a second time. The exact source comparison in [the exact ADO normalization](kashaev_ado_pointing.md) gives
\[
                       F_N(1)=K_N(K_{\mathbf n}),
 \tag{10}
\]
where \(K_N\) is the original reduced enhanced Kashaev invariant. The quotient and its framing equality are valid for knots at both parities.

The full modified-trace invariant, denoted here by \(\mathcal N_N(M)\), is
\[
 \mathcal N_N(M)=d_N(M)F_N(M),\qquad
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},
 \quad \eta_N=i^{N+3}.
 \tag{11}
\]
Whole-germ evaluation gives
\[
 d_N(1)=\frac{\eta_N}{N},\qquad
 \frac{d_N(q_N^s)}{d_N(1)}=\frac1{H_N(s)}.
 \tag{12}
\]
Thus the single factor \(H_N\) in the reduced profile (5) is canceled, exactly, in the profile of the full modified-trace invariant. Both normalizations have the same logarithmic volume on the disk. No numerator or denominator of (11) is separately set to zero.

Here is the ledger defining \(A_N\). Fix the actual six-type compiler and its original reference carriers once. In lower-index convention an edge has the exact propagator
\[
 (T_e\mathbf J)_{ab}
    =\mathbf1_{a=b}\,\gamma_{e,N}(s)
                   \frac{H_N(s)}{W_a(s)},\qquad
 W_a(s)=\prod_{r=1}^a
       \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi r/N)}\right),
 \quad \mathbf J_{ab}=\mathbf1_{a+b=d}.
 \tag{13}
\]
The factor \(\gamma_{e,N}\) is the specified typed scalar, a power of \(q_N^{s^2/2}\) or one. It is not included again in a vertex or in the closing factor.

At an equal-color circle vertex the actual grid parameter is \(\sigma_i(s)=s\) or \(-s\). The full crossing-power scalar is
\[
 C_{N,n_i}(\sigma)=q_N^{n_i(d^2/4-\sigma^2/2)},\qquad
 \frac{C_{N,n_i}(\sigma_i(s))}{C_{N,n_i}(0)}
                      =q_N^{-n_i\sigma_i(s)^2/2}.
 \tag{14}
\]
At an opposite-color vertex the Casimir relation is constant and the grid parameter is zero. Denote its exact fixed-power reference factor, divided by its value at \(s=0\), by \(\rho_{i,N}^{(n_i)}(s)\). This is computed by the prescribed crossing word and reference map. The derivation below gives its exact floor or ceiling exponent, according to the starting order of the two strands, including negative powers. A change from an original negative-odd reference is made once, before this factor is entered in the ledger.

Let \(\zeta_N(s)\) contain only the remaining original closing, pivotal and zero-framing scalar. All local edge and crossing/reference factors just described are excluded from it. This scalar is fixed by the finite source compiler before any asymptotic is taken; it is not defined by dividing the answer by a proposed profile. A root reference factor placed outside the vertex ledger must be assigned explicitly to \(\zeta_N\), and then omitted from \(\rho\). With normalized \(\gamma_{e,N}(0)=\rho_{i,N}^{(n_i)}(0)=1\), set
\[
 \boxed{\displaystyle
 A_N(s)=\frac{\zeta_N(s)}{\zeta_N(0)}
     \prod_e\gamma_{e,N}(s)
     \prod_{i\text{ equal}}q_N^{-n_i\sigma_i(s)^2/2}
     \prod_{i\text{ opposite}}\rho_{i,N}^{(n_i)}(s).}
 \tag{15}
\]
If a convention does not normalize an individual reference to one at completeness, its complete-value ratio is used in (15). No factor is then counted twice.

The packet and joint-transform notes abbreviate the closing and opposite-reference product by \(\widehat\zeta_N=\zeta_N\prod_{i\text{ opposite}}\rho_{i,N}^{(n_i)}\), and reserve \(\Gamma_{\mathrm{edge},N}\) for \(\prod_e\gamma_{e,N}\). Formula (15) writes the same factors separately. Using \(\widehat\zeta_N\) therefore removes the separate \(\rho\)-product from that formula; it does not add another copy.

For example, a zero-framing correction of writhe \(w\) has the exact ratio \(q_N^{-ws^2/2}\), since \(\theta_{d+s}=q_N^{(s^2-d^2)/2}\). This is one part of the ledger, not a reason to discard any other prescribed closing factor. The finite ledger consists of known nonzero elementary phases and monomials, with only polynomial level factors in the absolute complete normalization. In particular
\[
  \log|\zeta_N(0)|=o(N),\qquad
  \sup_{|s|\le R}
      \left|\log\left|\frac{\zeta_N(s)}{\zeta_N(0)}\right|\right|
                          =o(N).
 \tag{16}
\]
These statements follow from the original scalar formulas, not from a bound on the unknown knot invariant. The other factors in (15) and their inverses are uniformly bounded on every fixed disk. Keeping \(A_N\) exact is stronger and safer than silently replacing it by one.

### Why mixed-order products have no missing crossing factor

The reference maps used to encode a tangle must be distinguished from physical crossings. Write \(A=V_x\otimes V_y\), \(B=V_y\otimes V_x\), where \(x=-q_N^{-1}q_N^s\) and \(y=-q_N^{-1}q_N^{-s}\). These are the two possible orders of opposite colors. Both use the constant Casimir relation. Let \(r_0\) be the full complete checked-crossing polynomial, including its Cartan scalar and its first-normal coefficients at repeated roots. It is an invertible polynomial element of that relation.

The [actual Newton compiler](actual_main_meridian_newton_compiler.md), §4 (16b)–(18), chooses
\[
 G_A=I,\qquad
 G_B=\check R_{x,y}r_0(\Omega_A)^{-1},\qquad
 C_{D,C}=G_DG_C^{-1}.
 \tag{16a}
\]
Thus a morphism from object \(C\) to object \(D\) has coordinates \(C_{D,C}f(\Omega_C)\). The Casimir is natural under these intertwiners. For compatible \(X:C\to D\), \(Y:D\to E\), one has exactly
\[
 \bigl(C_{E,D}g(\Omega_D)\bigr)
 \bigl(C_{D,C}f(\Omega_C)\bigr)
       =C_{E,C}(gf)(\Omega_C).
 \tag{16b}
\]
This is why serial composition is polynomial multiplication. The inverse map in (16a) is the true coherent inverse, not a positive reverse crossing.

The [physical turn calculation](actual_main_meridian_turn_comparison.md), §3 (41)–(42), proves the full monodromy identity
\[
 \check R_{y,x}\check R_{x,y}
       =q_N^{-s^2}r_0(\Omega_A)^2,\qquad
 G':=\check R_{y,x}r_0(\Omega_B)^{-1}
       =q_N^{-s^2}G_B^{-1}.
 \tag{16c}
\]
The proof retains the coefficients at repeated roots: perturb the sum of the two highest weights to separate the channels, compare the physical monodromy there, and continue the polynomial identity using the nondegenerate moment pairing. Thus (16c) is not only an equality at distinct eigenvalues.

After the coherent reference map is removed, the four signed mixed crossings have the following polynomials.

| Starting order | Physical crossing | Target order | Polynomial |
| --- | --- | --- | --- |
| \(A\) | \(\check R_{x,y}\) | \(B\) | \(r_0\) |
| \(B\) | \(\check R_{y,x}\) | \(A\) | \(q_N^{-s^2}r_0\) |
| \(A\) | \(\check R_{y,x}^{-1}\) | \(B\) | \(q_N^{s^2}r_0^{-1}\) |
| \(B\) | \(\check R_{x,y}^{-1}\) | \(A\) | \(r_0^{-1}\) |

In particular two positive crossings retain the polynomial \(q_N^{-s^2}r_0^2\). That polynomial is not a carrier that can be canceled. Conversely, no extra \(r_0^2\) should be inserted after multiplying the two displayed polynomials.

For an arbitrary signed word, every crossing swaps the order, irrespective of its sign. If its signs are \(\delta_j\in\{1,-1\}\) and its net exponent is \(n=\sum_j\delta_j\), summing the scalar exponents in the table gives
\[
 f_{\mathrm{word},A}=q_N^{-\lfloor n/2\rfloor s^2}r_0^n,
 \qquad
 f_{\mathrm{word},B}=q_N^{-\lceil n/2\rceil s^2}r_0^n.
 \tag{16d}
\]
For example, for a word of length \(L\) starting at \(A\), the exponent of \(q_N^{s^2}\) is
\((L-n)/2-\lfloor L/2\rfloor=-\lfloor n/2\rfloor\).
Starting at \(B\) replaces the floor of \(L/2\) by its ceiling. This also proves (16d) for negative \(n\), and for alternating positive and negative odd blocks. The extra scalar when two odd blocks meet is precisely the carry in the floor of their sum. These are the explicit values of \(\rho^{(n)}\) for the stated reference orders. The original turn table already includes the scalar correction between \(G'\) and \(G_B^{-1}\); it must not be applied a second time.

A product junction is lowered using its compatible reverse morphism. Its carrier product then closes to the identity. For instance,
\[
 C_{A,C}h(\Omega_C)\,
 C_{C,B}g(\Omega_B)\,
 C_{B,A}f(\Omega_A)=(hgf)(\Omega_A).
 \tag{16e}
\]
Its normalized pivotal trace is therefore \(\phi_\sigma(hgf)\), with the actual common cut scalar retained separately. The same cancellation holds at every valence. Crossing polynomials such as \(r_0^n\) remain inside this trace.

This construction is applied to the original typed expression first. Each turn is reconstructed as an actual morphism, curried by the prescribed dualities, and expressed again using (16a). After lowering all vertices, changing the evaluation root only reassociates the same finite tensor contraction, retaining each original edge tensor \(T_e\mathbf J\) and its scalar \(\gamma_e\). It does not create a new untyped physical word. If a reversed edge is described using another forward turn type, the already known ratio of its two typed scalars is kept.

Finally, the actual cylindrical closing cut leaves an endomorphism of its ordered two-strand object; an alternative cap closure retains its physical closing turn first. Its carrier is \(C_{A,A}=I\), so the compiler's partial pivotal trace gives exactly the single factor \(H_N\). This verifies the product and closing conventions used in (15), including their repeated-root data. It asserts no isotopy exchanging arbitrary tangles.

## 3. From the whole finite source to one grouped wire packet

The same fixed complete Newton basis is used at the moving main meridian:
\[
 e_k(z)=\frac{\prod_{a=0}^{k-1}(c_a-z)}{S_k^2},
 \quad c_a=2\cos\frac{(2a+1)\pi}{N},
 \quad S_k=\prod_{a=1}^k2\sin\frac{\pi a}{N},
 \quad 0\le k\le d.
 \tag{17}
\]
Its first-normal coefficients at repeated Casimir roots are part of the algebra. They are not discarded when the main color moves. The exact metric remains \(\phi_s(e_a e_b)=\mathbf1_{a+b=d}\); a physical turn consequently gives the equal-label edge (13).

The [component source theorem](actual_main_meridian_component_extension.md), §6, splits an outgoing branch into a clean low-index part, an internal error with a strict deficit in the entire coefficient profile, and an outgoing high-index part. An original decorated turn converts a spectral error into a full coefficient-profile deficit. A bare component is homogeneous in the constants of these profiles, so an inherited deficit crosses the component without another universal charge. New high-state errors consume only the component path budget (2). This is why the condition is componentwise rather than a sum of all losses over the tree.

These estimates also apply when the circle operator is the actual fixed power \(R_s^{n_i}\). Every fixed power and its inverse have polynomial spectral norm on \(|s|\le R<1\), with constants depending on the fixed power. For a low product \(E=\prod e_{k_a}\), its raw shifted-grid trace satisfies
\[
             |\phi_\sigma(R_\sigma^{n_i}E)|
                   \le C_{\mathbf n,R}N\,\phi_0(L_NE).
 \tag{18}
\]
The comparison uses the complete pure circle tensor on the right, not an absolute filled state sum. It follows from positivity of the Laurent coefficients of the low basis factors, the actual shifted root grid and the bounded full chirp on its \(O(N^{-1})\) height. The exact complete node sum gives
\[
        \phi_0(L_NE)\ge N(\pi/4)^{\deg_{\mathrm{factors}}E}E(-2).
 \tag{19}
\]
The odd-level constant can be replaced by one. The even constant comes from the actual nearest-node ratio and is uniform up to the low endpoints. Holomorphic continuation of the whole trace includes its removable collisions.

Let \(F_0\) be the maximum of the original complete positive source action; the augmented geometric calibration gives \(2\pi F_0=\operatorname{Vol}(Y)\) for the exterior \(Y\) with all crossing circles unfilled. The summed high-edge contribution and the complement of the original strict retained-edge window have a fixed loss below \(F_0\). The same statement holds after resolving complete bare vertices into their positive binary multiplication coefficients. On the regular retained window, every incident edge is in a fixed compact subinterval of \((0,1/2)\), and every bare vertex has incident sum greater than \(1+\delta\). The [regular bare-tensor theorem](actual_main_meridian_regular_bare_trace.md) therefore gives
\[
          \phi_\sigma\left(\prod e_{k_a}\right)
       =\phi_0\left(\prod e_{k_a}\right)
                               (1+O_R(e^{-\kappa N})).
 \tag{20}
\]
This is exact at valence at most four. At larger fixed valence it follows from the strict Fourier-tail separation of regular low Newton products.

Use (18) to multiply out the finitely many replacements (20), and then localize the positive binary-resolution variables. The result is one fixed source error
\[
                    O\!\left(N^C e^{N(F_0-\eta_0)}\right),
                         \qquad \eta_0>0.
 \tag{21}
\]
The loss is geometric or comes from a closed coefficient-rate inequality. It is independent of the sizes of the fixed \(n_i\) and of the compact radius \(R<1\); prefactors and the starting level may depend on them. The summed high-state estimate is grouped through actual modules. It is not an absolute bound on every individual return term of a resolved quotient product.

After these exact reductions, introduce one angular variable \(\tau_i\) at every original circle. Before its crossing trace is applied, the finite packet is
\[
 B_N(\boldsymbol\tau,s)=
 \sum_{\mathbf k/N\in\mathcal W}
    \prod_{g\text{ bare}}\mu_{N,g}(\mathbf k)
    \prod_{i\text{ circle}}\prod_{e\sim i}
                         e_{k_e}(-2\cos\tau_i)
    \prod_e\gamma_{e,N}(s)\frac{H_N(s)}{W_{k_e}(s)}.
 \tag{22}
\]
The source fixes every index and every \(d=N-1\) offset. The box \(\mathcal W\) is an actual primitive integer box. There are no chirps or sine trace factors in \(B_N\). It is exactly even in each angle.

## 4. The finite packet, rather than a real-grid approximation

The [grouped wire-packet theorem](actual_main_meridian_grouped_wire_packet.md) constructs (22) directly. A complete bare vertex of valence \(D\) has \(D-2\) nontrivial positive multiplication coefficients and \(D-3\) hidden integers; its last output is \(d\) minus the closing incident index. Along with the physical edge labels, these give
\[
 K=E+\sum_{\mathrm{bare}\ v}(D_v-3)
 \tag{23}
\]
independent integers, with no parity-dependent lattice density. This is not the uncontracted count \(2H-3\), since the circle vertices have already been collapsed.

The canonical Gamma-product interpolation of the sine factorials is used in every original bare coefficient and every Newton evaluation. It is zero-free in the needed bulk strips, has the exact shift \(G_N(z+1)/G_N(z)=2\sin(\pi(z+1)/N)\), and retains every finite integer offset. In particular
\[
 \frac{H_N(s)}{W_{Nx}(s)}
 \quad\text{has the specified continuation}\quad
 \frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}
   =1-\frac{\pi s^2}{N}\cot(\pi x)+O_R(N^{-2}).
 \tag{24}
\]
The notation on the left means the physical ratio at integer \(Nx\), with the right side its chosen analytic continuation.

At zero angles, eliminating the hidden positive circle variables from the original constrained action gives exactly the action in (22). The remaining bare gate Hessians and the circle functions \(g\) make its primitive wire Hessian negative definite. This proves a unique strict grouped optimizer at the same original value \(F_0\). It is not a sum of independently maximized boundary budgets.

The exact finite-lattice residue formula with cotangent kernels moves the primitive wire sum to its holomorphic saddle. Its half-grid vertical boundaries, nonzero cotangent modes and all endpoint connectors have fixed source losses. Thus, on one fixed complex angular polydisk,
\[
 B_N(\boldsymbol\tau,s)
  =N^\nu\Gamma_{\mathrm{edge},N}(s)
        a(\boldsymbol\tau)e^{N\Psi(\boldsymbol\tau)}
                         (1+O_R(N^{-1})),
 \quad
 \nu=\frac32(1-H),\quad
 \Gamma_{\mathrm{edge},N}=\prod_e\gamma_{e,N}.
 \tag{25}
\]
Here \(a\) is nonzero, the relative error is uniformly holomorphic, and both \(a\) and \(\Psi\) are separately even. At the complete saddle,
\[
 \Psi(0)=F_0,\qquad
 \Psi''(0)=-\operatorname{diag}(a_1,\ldots,a_H),
 \qquad a_i=\frac1{2\pi}\sum_{e\sim i}\tan(\pi x_e^*)>0.
 \tag{26}
\]
The mixed wire-angle derivatives vanish at zero by exact evenness, so eliminating the wires produces no off-diagonal Hessian correction there.

The same exact finite packet has a raw-product bound on a strip around the entire real angular cube:
\[
 |B_N(\mathbf t+i\mathbf y,s)|
       \le N^C
          \exp N\{F_0-c\|\mathbf t\|^2+C'\|\mathbf y\|^2\}.
 \tag{27}
\]
It includes \(O(N^{-1})\) endpoint translations and fixed derivatives on smaller strips. Near zero this follows from the regular analytic Newton product; away from zero, strict circular rearrangement gives a fixed angular loss that absorbs the uniform logarithmic Riemann-sum error. It does not assert that an arbitrary quotient product or turn preserves a Gaussian. This real-spectator bound is what permits one circle contour to be treated while all others stay on their original grids or real integration paths.

## 5. All Fourier charges are compared at one joint saddle

The [direct crossing trace](actual_main_meridian_direct_crossing_trace.md) retains the actual operator and its contour. For an equal-color vertex its exact eigenvalue at
\[
       \tau_r(\sigma)=\frac{2\pi}{N}(d/2+\sigma-r)
 \tag{28}
\]
is \(C_{N,n}(\sigma)e^{inN\tau_r(\sigma)^2/(4\pi)}\). The root trace is continued as a whole through its collisions. A translated rectangle keeps the vertical sides halfway between the original grid poles. Pairing its positive and negative Fourier terms gives coefficients
\[
       \eta^{\ell-1}U_{\ell-1}(\cos2\pi\sigma),
       \qquad \eta=(-1)^{N-1},\quad \ell\ge1.
 \tag{29}
\]
The first coefficient is exactly one. The sine in the trace makes the zero Fourier integral odd; its endpoint currents are retained and estimated, rather than dropped. Opposite-color vertices use \(\sigma=0\), with their separate reference factors still present.

Choose one sufficiently small number \(t_0>0\). At circle \(i\), retain charges \(1\le\ell_i\le L_i=\lfloor t_0|n_i|\rfloor\) and use horizontal height \(y_i=A_0t_0/|n_i|\), with \(A_0\) sufficiently small. The global bound (27) makes every omitted charge lose a fixed amount, not merely \(O(n_i^{-2})\), from \(F_0\). On a translated vertical side the exact kernel is only \(O(N)\); its chirp cost is \(O(Nt_0)\), absorbed by the fixed angular endpoint loss.

Remove these tails by the exact telescoping product of the coordinate trace functionals. While a tail is removed at circle \(i\), all spectators remain on real integrals or on their physical \(O(N^{-1})\)-translated grids. Their fixed-power chirps have bounded modulus there. Consequently no estimate introduces a positive exponential cost involving a different, much larger slope. The divided formulas are initially estimated on parameter circles avoiding the displayed sine denominator; the maximum principle is then applied to the whole holomorphic difference, restoring all collision values and every compact disk \(R<1\).

The [joint filling transform](actual_main_meridian_joint_filling_transform.md) now compares every remaining charge on the same branch. After the finite reduction, a charge vector has joint action
\[
 \mathcal T_{\boldsymbol\ell}(\boldsymbol\tau)
       =\Psi(\boldsymbol\tau)
         +\frac{i}{4\pi}\sum_i n_i\tau_i^2
         -i\sum_i\ell_i\tau_i.
 \tag{30}
\]
Set \(\varepsilon_i=1/n_i\) and \(t_i=\ell_i/n_i\). Its selected critical equation is
\[
        \tau_i=2\pi t_i+
                 2\pi i\varepsilon_i\Psi_i(\boldsymbol\tau).
 \tag{31}
\]
The implicit-function theorem gives one branch on a fixed polydisk in \((\mathbf t,\boldsymbol\varepsilon)\), with no relation between the different \(\varepsilon_i\).

At this branch complete the square. The critical action is a purely imaginary term \(-i\pi\sum t_i^2/\varepsilon_i\) plus an analytic function \(\mathcal W(\mathbf t,\boldsymbol\varepsilon)\), even in each \(t_i\). At \(\boldsymbol\varepsilon=0\), it is \(\Psi(2\pi\mathbf t)\). Hence (26), on a smaller fixed polydisk, implies
\[
 \Re\mathcal T_{\boldsymbol\ell}(\boldsymbol\tau_{\boldsymbol\ell})
 \le\Re\mathcal T_{\mathbf1}(\boldsymbol\tau_{\mathbf1})
       -\sum_i\frac{\pi^2a_i}{n_i^2}(\ell_i^2-1).
 \tag{32}
\]
This compares each charge with the same joint filled action. It does not compare a tiny local alias loss with the total complete-to-filled volume drop.

Separate evenness also writes \(\Psi_i=\tau_iQ_i(\boldsymbol\tau^2)\), with \(\Re Q_i<0\) near zero. Therefore
\[
 \tau_{\boldsymbol\ell,i}
  =\frac{2\pi t_i}
         {1-2\pi i\varepsilon_iQ_i(\boldsymbol\tau_{\boldsymbol\ell}^2)},
 \qquad
 \Im\tau_{\boldsymbol\ell,i}<0,\qquad
 |\Im\tau_{\boldsymbol\ell,i}|
                     \le C|t_i|/|n_i|.
 \tag{33}
\]
These componentwise heights control the endpoint connectors even for independently unequal signed slopes. Every \(\tau_{\boldsymbol\ell,i}\) is nonzero, so the trace amplitude \(\prod_i\sin\tau_i\) is nonzero at the saddle. The real part of the angular Hessian on its translated real tangent plane remains negative definite; the chirp contributes only a purely imaginary Hessian.

The finite wire packet is holomorphic on the contour before this translation, so its uniform error in (25) can be integrated with the Gaussian estimate. The resulting first-charge amplitude is nonzero. Every other retained charge is exponentially smaller by (32). The fixed errors from (21), the high-charge tails and the real angular complement are absorbed by taking all \(|n_i|\) sufficiently large: the real first-charge action tends to \(F_0\) uniformly as \(\max_i|1/n_i|\to0\).

This proves directly, at completeness, an asymptotic of the form
\[
 F_N(1)
   =\zeta_N(0)
       \left(\prod_i q_N^{n_i d^2/4}\right)
       N^{3/2}D_{\mathbf n}\,
       e^{N\mathcal T_{\mathbf1}(\boldsymbol\tau_{\mathbf1})}
                        (1+O_{\mathbf n}(N^{-1})),
 \qquad D_{\mathbf n}\ne0,
 \tag{34}
\]
with any fixed complete reference constants retained in the chosen closing ledger. The \(N^{3/2}\) power is the grouped count \(\nu+3H/2\). Formula (34), rather than an earlier quantum volume theorem, supplies eventual nonvanishing and the lower exponential bound at both parities.

The choices of windows, \(t_0\), structural gaps and geometric reciprocal-slope neighborhood depend only on the fixed source. They determine one lower bound \(B\) for every \(|n_i|\). The radius \(R\) changes only the bounded trace coefficients, prefactors and starting level. Thus \(B\) is independent of \(R<1\). A geometric bound stated originally in \(|p_i|\) is included by increasing \(B\), since \(|p_i|\ge(|n_i|-1)/2\).

## 6. The full action is the original marked filling action

It remains to identify the action in (34), including its linear term and its primitive marking. Let \(\mathbf y\) be the grouped wire variables, \(M_{\mathrm{bare}}(\mathbf y)\) the sum of their complete bare-gate actions, and
\[
 b_i(\mathbf y,\tau_i)
        =\sum_{e\sim i}b(x_e(\mathbf y),\tau_i)
 \tag{35}
\]
the even Newton angular action at circle \(i\). Before eliminating wires, the original selected auxiliary-color source has local action
\[
 \mathfrak f_{\epsilon_i}(\mathbf y,\chi_i)
   =\operatorname{stat}_{\tau_i}
      \left[
       b_i(\mathbf y,\tau_i)
        +\frac{i\epsilon_i\tau_i^2}{4\pi}
        +i\chi_i\tau_i\right].
 \tag{36}
\]
The identity is the [actual regular circle-source branch](actual_main_meridian_regular_circle_trace.md), with its original chirp and shear. It is not a quadratic approximation. The auxiliary Fourier transform adds \(2\pi i\chi_i z_i\), so stationarity in \(\chi_i\) imposes \(\tau_i=-2\pi z_i\). Evenness of \(b_i\) gives
\[
          b_i(\mathbf y,2\pi z_i)+i\pi\epsilon_i z_i^2.
 \tag{37}
\]
The original filling term is \(-2\pi i(p_i z_i^2+z_i)\). Substituting (4) and now writing \(\tau_i=2\pi z_i\), the entire expression is exactly
\[
 b_i(\mathbf y,\tau_i)
            +\frac{in_i\tau_i^2}{4\pi}-i\tau_i.
 \tag{38}
\]
Adding the unchanged bare actions and imposing the common wire stationarity gives (30) with charge \(\mathbf1\). Holomorphic uniqueness near the complete state shows that the two elimination orders select the same branch and the same additive constant.

For clarity, the peripheral variables here belong to the auxiliary crossing circles, not to the microscopic main meridian \(M\). In the original marked convention,
\[
 U_i=-2\pi i\chi_i,\qquad
 V_i=-2\,\partial_{\chi_i}\Phi_\epsilon.
 \tag{39}
\]
The Fourier stationarity gives \(V_i=4\pi iz_i\), and filling stationarity gives \(\chi_i-2p_i z_i=1\). Therefore
\[
                           U_i+p_iV_i=-2\pi i.
 \tag{40}
\]
The sign and primitive coefficient in (40) are retained. They ensure a single \(2\pi\) angular turn in the completed solid-torus collar.

The geometric input is [the marked strict-tree geometry](actual_conway_general_mask_marked_filling.md), §6 (18)–(20) and §7 (22)–(23), with the smooth-completion argument in [the source regulator and metric completion](general_source_regulator_hyperbolic_equality.md). Its absolute regulator and actual cusp marking give
\[
 2\pi\,\Re\mathcal T_{\mathbf1}
                 (\boldsymbol\tau_{\mathbf1})
                       =\operatorname{Vol}(S^3\setminus K_{\mathbf n}).
 \tag{41}
\]
Only the auxiliary crossing-circle cusps are filled. The main knot cusp remains complete and unfilled. This is an identification with the actual hyperbolic metric on the knot exterior, not just with a formal representation or a relative volume. No quantum lower bound is used in this geometric step.

## 7. The profile, its correction, and the uniform logarithmic limit

The first charge coefficient in (29) is one for every parameter and every level parity. Consequently its only main-meridian dependence outside the wire insertion consists of the exact crossing/reference phases in (14)–(15). All other charges and all fixed currents are exponentially smaller, uniformly on each \(|s|\le R<1\), after the single choice of \(B\).

The wire packet contains the product of (24). Its exact normalized finite-contour insertion has the expansion
\[
 \frac{B_N(\boldsymbol\tau,s)}
      {\Gamma_{\mathrm{edge},N}(s)B_N(\boldsymbol\tau,0)}
     =1-\frac{\pi s^2}{N}
          \sum_e\cot(\pi x_e(\boldsymbol\tau))
                       +O_R(N^{-2})
 \tag{42}
\]
on a fixed complex angular neighborhood. This statement comes from the canonical Gamma interpolation and the same finite lattice contour; it is not extrapolated from grid values.

Apply the analytic Gaussian insertion rule once more at the joint first-charge saddle. For a holomorphic function \(c\), its normalized Gaussian expectation is \(c\) at the saddle plus \(O(N^{-1})\): the linear term is odd, and the first surviving corrections cost \(N^{-1}\). Applied to the coefficient already multiplied by \(N^{-1}\) in (42), this gives an \(O(N^{-2})\) remainder. The common first-order saddle correction in numerator and denominator cancels. This proves (7), with all scalars in \(A_N\) and the single cut factor \(H_N\) retained exactly. Its weaker form is (5).

For fixed \(R<1\), \(H_N\) and its inverse are uniformly bounded, and
\[
             H_N(s)\longrightarrow\frac{\sin\pi s}{\pi s}
 \tag{43}
\]
uniformly on the disk, including the value one at zero. The limit has no zero there. The same is true of the elementary nonzero factors after their known phases are retained, with subexponential bounds as in (16). Equation (34) and the geometric equality (41) give the logarithmic rate at \(s=0\); (5) transfers it uniformly to the entire fixed disk, proving (6). Uniform holomorphy on a slightly larger compact disk also gives the corresponding fixed-derivative estimates for the normalized profiles.

The variable \(z=2\pi i s\) converts (7)'s residual term to
\[
       \frac{z^2}{4\pi N}
                    \sum_e\cot(\pi x_e^{\mathrm{fill}}).
 \tag{44}
\]
This is merely a coordinate rewrite. It does not identify the sum, or the sum together with the exact scalar ledger, with the main-cusp modulus. Such an identification requires a separate comparison of the original main peripheral deformation.

## 8. What this theorem does and does not extend

The [earlier complete-value volume theorem](actual_conway_all_strict_tree_long_twist_volume.md) covers every strict literal Conway tree under its stated knot and long-filling hypotheses. The present theorem gives more information—an actual complex microscopic main-meridian profile and a uniform volume rate—but for the narrower class specified by the bare-component condition (2). It does not replace the broader complete-value theorem or reduce its scope.

The disk restriction is essential. The present proof treats \(|s|\le R<1\); it does not cross the first ordinary-color resonances \(s=\pm1\), where the reduced ordinary-color anchor and the full modified dimension have different behavior. The removable same-color Casimir collisions within this disk are included by the full physical source. A zero-free microscopic disk is also not a fixed open disk in the \(M\)-plane.

No theorem for arbitrary adjacent bare components failing (2) is obtained. No filling integer is allowed to grow with \(N\). No conclusion is drawn for the ordinary-color-subtracted regular remainder through its resonance divisors. Finally, the existence of an exact meridian annihilator and the pointed complete period is separate from identifying a selected classical main-meridian \(A\)-factor. The scalar profile and volume theorem here do not make that identification.

## 9. The proof route

The [exact ADO normalization](kashaev_ado_pointing.md) fixes the invariant, the coordinate \(M=-qx\), and the modified dimension. The [oriented source compiler](actual_main_meridian_newton_compiler.md) and [physical quarter-turn theorem](actual_main_meridian_turn_comparison.md) give its polynomial coordinates, compatible reference maps, full normal coefficients and original closing trace.

The global estimate begins with [source growth near the complete main meridian](actual_main_meridian_source_bounds.md). The [component extension](actual_main_meridian_component_extension.md) permits the adjacent bare junctions satisfying (2), and explains why inherited errors retain their original deficit. The [regular bare trace](actual_main_meridian_regular_bare_trace.md) then replaces moving bare tensors by their complete tensors on the strict window.

The local circle operators and their marked analytic continuation are established in the [regular circle trace](actual_main_meridian_regular_circle_trace.md). The [direct crossing trace](actual_main_meridian_direct_crossing_trace.md) keeps the actual filled crossing power, rather than substituting a complete-color expansion. The [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) supplies the exact finite lattice and its complex contour. The [joint filling transform](actual_main_meridian_joint_filling_transform.md) retains all Fourier charges until their common saddle has been compared; it supplies the nonzero lower bound used here.

The [general core action](actual_conway_general_core_packet_and_gap.md) and [strict-mask complete geometry](actual_conway_general_strict_mask_geometry.md) provide the original strict optimizer and augmented metric. The [marked geometric deformation](actual_conway_general_mask_marked_filling.md), §§6–7, and [metric-completion theorem](general_source_regulator_hyperbolic_equality.md) identify the selected long-filling action with the volume of the actual knot complement. The earlier quantum volume limit is not used as an analytic lower-bound input in this route.
