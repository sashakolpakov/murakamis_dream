# The finite wire sum before the crossing traces

The polynomial contraction for a Conway construction sums over integer Newton indices on its internal edges. At a junction carrying a crossing circle, a polynomial trace remains to be evaluated. This note first sums the internal indices while keeping one angular variable for each such trace. The resulting finite function is called the wire packet. Near its geometric critical point, it has a uniform complex asymptotic with a nonzero leading coefficient. An exact representation of the finite lattice sum controls the boundary terms when the integration contours move.

The crossing-circle traces are applied only after this common finite sum has been constructed. This order matters when filling coefficients are independently long: a local Fourier error cannot be compared with a product of independently filled exponents. The theorem below constructs the packet and evaluates its meridian-dependent insertion. The [joint filling transform](actual_main_meridian_joint_filling_transform.md) then compares the Fourier frequencies of the entire contraction.

## 1. Source, class, and the assertion

Fix a [strict ordered Conway source](actual_conway_all_strict_tree_long_twist_volume.md), with the stated knot and absence-of-internal-component hypotheses whenever a knot volume is mentioned. Use its reduced tree of ordered product junctions and physical quarter-turn edges. A **circle vertex** contains one original operator belonging to a crossing circle; an ordinary original leaf is a circle vertex of valence one. A **bare vertex** is a product junction containing no such operator. Thus this tree has \(H\ge2\) circle vertices, \(J\ge0\) bare vertices, and \(E=H+J-1\) edges. Every bare vertex has valence at least three. We retain the original orders, orientation types, closing mark and framing.

For the global source-to-window statement, each maximal bare component is either a singleton, entirely trivalent in the full reduced tree, or satisfies the path hypothesis of the [component extension](actual_main_meridian_component_extension.md). The [trivalent extension](actual_main_meridian_trivalent_filled_volume.md) permits arbitrary fixed component size and retains all internal labels. For the path alternative, if \(b_v\) is the number of incident rigid boundary branches, require \(b_v\ge5\) and
\[
 \eta_{\mathcal U}=2G_0-\max_{\mathcal P\subset\mathcal U}
        \sum_{v\in\mathcal P}\varepsilon_{b_v-1}>0,
 \qquad
 \varepsilon_k=(k+1)\{J(\tfrac14+\tfrac1{k+1})
                +J(\tfrac14-\tfrac1{k+1})-2J(\tfrac14)\}.
 \tag{1}
\]
The maximum is over simple component paths. Here
\(J(x)=\int_0^x\log(2\sin\pi u)\,du\),
\(g(x)=J(2x)-4J(x)\), and \(G_0=g(1/4)\).
The sufficient condition \(b_v\ge\max(8,4|\mathcal U|)\) may be used for the path alternative. Singleton and entirely trivalent components do not require this numerical condition. Trivalence counts all original incidences; an artificial binary resolution of a larger junction does not qualify.

The global inputs are the [component extension](actual_main_meridian_component_extension.md), including its grouped-error argument in Section 6, and the [source-bound theorem](actual_main_meridian_source_bounds.md). The new [trivalent comparison](actual_main_meridian_trivalent_component_bound.md) supplies the additional full-component bound and exact cubic trace replacement. The other local inputs are the [regular bare trace](actual_main_meridian_regular_bare_trace.md), the [regular circle trace](actual_main_meridian_regular_circle_trace.md), and the all-low fixed-power comparison in the [direct crossing trace](actual_main_meridian_direct_crossing_trace.md), Section 7. Their uses are separated below: grouped errors are controlled before localization, and exact finite positive resolutions supply the wire coordinates and the saddle.

Put
\[
 q=e^{\pi i/N},\quad d=N-1,\quad m_N=\lfloor d/2\rfloor,
 \qquad
 S_k=\prod_{a=1}^k2\sin(\pi a/N),
 \qquad
 e_k(z)=\frac{\prod_{a=0}^{k-1}(c_a-z)}{S_k^2},
 \quad c_a=2\cos\frac{(2a+1)\pi}{N}.
 \tag{2}
\]
The main meridian is \(M=q^s\), with \(0\le R<1\) fixed and \(|s|\le R\). The fixed complete basis (2) is used also in the moving quotient. The exact metric is
\(\phi_s(e_a e_b)=\mathbf1_{a+b=d}\).
In lower-index convention the physical edge is
\[
 (T_e\mathbf J)_{ab}=\mathbf1_{a=b}
       \gamma_{e,N}(s)\frac{H_N(s)}{W_a(s)},
 \qquad H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},
 \quad
 W_a(s)=\prod_{r=1}^a
       \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi r/N)}\right).
 \tag{3}
\]
The prescribed six-type compiler determines the scalar \(\gamma_{e,N}\), a retained power of \(q^{s^2/2}\), or one. In particular the two labels on a physical turn edge are equal. Formula (3) must not be replaced by the weighted reversal on an upper coefficient vector. For all indices, \(H_N/W_a\) and its inverse are uniformly bounded on \(|s|\le R<1\).

Choose one fixed ordered binary resolution of each complete bare tensor. Section 2 specifies its exact primitive coordinates and their offsets. Let \(\mathcal W\) be a sufficiently small rectangular box about their complete maximizing value. Define the finite polynomial
\[
 B_N(\boldsymbol\tau,s)=
 \sum_{\mathbf k/N\in\mathcal W}
  \left(\prod_{g\text{ bare gate}}\mu_{N,g}(\mathbf k)\right)
  \left(\prod_{v\text{ circle}}\prod_{e\sim v}
                  e_{n_e(\mathbf k)}(-2\cos\tau_v)\right)
  \left(\prod_{e}\gamma_{e,N}(s)
                      \frac{H_N(s)}{W_{n_e(\mathbf k)}(s)}\right).
 \tag{4}
\]
Every affine index in (4) is the exact integer index, including all occurrences of \(d=N-1\). No crossing chirp and no factor \(\sin\tau_v\) is in (4). These belong to the subsequent trace functional. The packet is exactly separately even and \(2\pi\)-periodic in the angular variables.

There are a real analytic action \(\Psi\), a nonzero analytic amplitude \(a\), a fixed complex angular polydisk, and a fixed small strip around the entire real angular cube, with the following properties. Write
\(\Gamma_{\mathrm{edge},N}(s)=\prod_e\gamma_{e,N}(s)\).
Then on the local polydisk
\[
 B_N(\boldsymbol\tau,s)
   =N^{3(1-H)/2}\Gamma_{\mathrm{edge},N}(s)
       a(\boldsymbol\tau)e^{N\Psi(\boldsymbol\tau)}
                        (1+O_R(N^{-1})).
 \tag{5}
\]
The error is uniformly holomorphic on a slightly larger polydisk. Both \(\Psi\) and \(a\) are separately even. If \(x_e^*\) is the complete normalized edge label, then
\[
 \Psi(0)=F_0,
 \qquad
 \Psi_{\tau_v\tau_w}(0)
   =-\mathbf1_{v=w}\frac1{2\pi}
                   \sum_{e\sim v}\tan(\pi x_e^*).
 \tag{6}
\]
All diagonal curvatures in (6) are positive. Here \(F_0\) is the original complete positive source action, so the existing marked geometry identifies \(2\pi F_0\) with the volume of the original augmented complement.

For constants \(A,c,C,y_0>0\), the exact finite packet also obeys
\[
 |B_N(\mathbf t+i\mathbf y,s)|
 \le N^A\exp N\{F_0-c\|\mathbf t\|^2+C\|\mathbf y\|^2\},
 \quad |t_v|\le\pi,\quad |y_v|\le y_0,\quad |s|\le R.
 \tag{7}
\]
The same estimate, up to a constant factor, holds at endpoint translates of size \(O_R(N^{-1})\). Every fixed angular or main-parameter derivative satisfies the corresponding estimate with an additional power of \(N\) on a smaller strip.

There is a more precise normalized insertion formula. Let \(y_*(\boldsymbol\tau)\) be the wire saddle below, and \(x_e(\boldsymbol\tau)\) its limiting edge labels. Uniformly on a smaller fixed complex polydisk,
\[
 \frac{B_N(\boldsymbol\tau,s)}
      {\Gamma_{\mathrm{edge},N}(s)B_N(\boldsymbol\tau,0)}
 =1-\frac{\pi s^2}{N}
           \sum_e\cot(\pi x_e(\boldsymbol\tau))+O_R(N^{-2}).
 \tag{8}
\]
No first-order meridian-dependent amplitude is hidden in (8).

## 2. The exact bare resolution and primitive lattice

At a bare vertex of valence \(D\ge3\), order its incident labels \(n_1,\ldots,n_D\) according to the chosen original multiplication association. Associativity permits a sequential notation for the same positive resolution; it does not assert a tangle isotopy. The original nonnegative multiplication coefficient is
\[
 \mu_{ij}^{r}=
 \frac{S_{i+j}S_r}
      {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}},
 \quad i+j\le d,\quad\max(i,j)\le r\le i+j,
 \tag{9}
\]
and is zero outside this support. Set \(r_1=n_1\) and \(r_{D-1}=d-n_D\). The exact complete trace is
\[
 \phi_0\left(\prod_{a=1}^D e_{n_a}\right)
  =\sum_{r_2,\ldots,r_{D-2}}
        \prod_{a=2}^{D-1}\mu_{r_{a-1},n_a}^{r_a}.
 \tag{10}
\]
The final multiplication by \(e_{n_D}\), followed by the trace, has coefficient one after the exact condition \(r_{D-1}+n_D=d\) is imposed. It contributes no additional free variable or nontrivial gate. Thus (10) has \(D-3\) hidden integer variables and \(D-2\) nontrivial gates. All signs and factors in (9) are the complete source factors, not an asymptotic surrogate.

Use the edge indices together with the hidden variables in (10) as coordinates. They are independent integer coordinates before inequalities are imposed. There are
\[
 K=E+\sum_{v\text{ bare}}(D_v-3),
 \qquad G=\sum_{v\text{ bare}}(D_v-2)
 \tag{11}
\]
free coordinates and nontrivial bare gates, respectively. Every remaining index has the form \(N\ell(\mathbf y)+\delta\), where \(\mathbf y=\mathbf k/N\), \(\ell\) is integral affine and \(\delta\) is a fixed integer. In particular \(d-n_D=N(1-y_D)-1\). The full coordinate lattice is \(\mathbb Z^K\); there is no parity-dependent sublattice or determinant factor. The tree has no further closing equation after the covariant edge variables and the local complements in (10) are imposed.

This count is different from \(2H-3\), the count before circle vertices are contracted. Indeed a pure circle tensor at valence \(D\) can be positively expanded using the complete leaf \(h_N=T_0L_N\) and \(D-1\) multiplication outputs. Those \(D-1\) variables have already been eliminated in (4). Restoring all of them recovers exactly \(2H-3\).

Let \(D_c=\sum_{v\text{ circle}}D_v\) and \(D_b=\sum_{v\text{ bare}}D_v\). Since \(D_c+D_b=2E\), the number \(G\) and the lattice dimension satisfy
\[
 G=D_b-2J,
 \qquad K=E+D_b-3J,
 \qquad -D_c-\frac32G+\frac12K=\frac32(1-H).
 \tag{12}
\]
This is the power of \(N\) in (5). Each basis evaluation has power \(N^{-1}\), each nontrivial bare gate \(N^{-3/2}\), and the primitive wire Gaussian contributes \(N^{K/2}\). Subsequent circle integrations, each with \(N^2\) trace factor and \(N^{-1/2}\) Gaussian factor, recover \(N^{3/2}\) for the whole source. This last bookkeeping does not itself prove any filled asymptotic.

## 3. Original action and the strict grouped optimizer

There are two kinds of edge regularity. A circle-incident label is strictly in \((0,1/2)\), by the original intrinsic-probe statement and the leaf boundary barrier. An edge inside a trivalent bare component is strictly in \((0,1)\); its complete maximizing label may equal or exceed one half. The full old support of these internal edges is retained. The [global trivalent proof](actual_main_meridian_trivalent_filled_volume.md) explains why this distinction suffices for the complex packet.

For separated bare vertices all retained labels are low. For components satisfying the path condition (1), a bare–bare edge with label \(a\) contributes the original cut action \(f_A(1-a)+f_B(1-a)\). The product inequality \(f_A',f_B'\ge f_{hh}'\) makes it decrease when \(a>1/2\), and makes its derivative strictly negative at \(a=1/2\) when at least one adjacent product has at least three inputs. The boundary-count hypothesis ensures that strict case. The original strict state excludes \(a=0\). This uses the derivative inequality from the [probe geometry](actual_conway_unflagged_probe_geometry.md), Appendix A, and the original coupled profiles retained in the [component extension](actual_main_meridian_component_extension.md), Sections 2–4.

At a bare vertex, summing its strict binary inequalities gives
\[
             \sum_{e\sim v}x_e^*-1
                =\sum_{g\text{ at }v}(x_g+y_g-z_g)>0.
 \tag{13}
\]
A sufficiently small retained-edge neighborhood therefore has all labels in \([\delta,1-\delta]\), all circle-incident labels in \([\delta,1/2-\delta]\), and every bare incident sum at least \(1+\delta\), for some \(\delta>0\). Components using the old path estimate retain its stronger low internal window.

Here is why the grouped wire action has exactly the original maximum, rather than an independently optimized upper budget. At completeness, for a product \(E=\prod_{a=1}^D e_{n_a}\) of low basis elements,
\[
 \phi_0(L_NE)=N\sum_{r=0}^{N-1}E(c_r),
 \qquad
 N(\pi/4)^D E(-2)\le\phi_0(L_NE)\le N^2E(-2).
 \tag{14}
\]
At odd levels the lower constant is one. At even levels, for the node closest to \(-2\),
\[
 \frac{e_n(-2\cos(\pi/N))}{e_n(-2)}
  =\prod_{a=0}^{n-1}
     \frac{\cos(a\pi/N)\cos((a+1)\pi/N)}
          {\cos^2((a+1/2)\pi/N)}
  \ge\frac N2\tan\frac{\pi}{2N}\ge\frac\pi4.
 \tag{15}
\]
The product decreases over the low range and its endpoint is the displayed value. Every summand in the node sum is nonnegative. Equations (14)–(15) retain both parities and the simple odd endpoint.

The complete leaf has positive coefficients
\([e_r]h_N=N^2S_{2r}/S_r^4\) for \(r\le m_N\) and zero otherwise. Indeed \([e_r]h_N=\phi_0(L_Ne_r)\); the complete node sum is \(N^2\) times the zero Laurent coefficient of \(e_r(-u-u^{-1})\), because its Laurent degree is \(r<N\), and that coefficient is \(S_{2r}/S_r^4\) in the low range. High \(e_r\) vanish at every complete node. Expanding the product \(E\) using (9), the identity \(L_N=T_0h_N\) makes the circle trace (14) an exact positive sum of these leaf coefficients and complete gates. Thus the original positive source can be expanded first at all circle vertices and then at bare vertices, without a signed cancellation or a changed source.

The rate of (14), uniformly on a regular incident-index neighborhood, is \(\sum_{a=1}^D g(x_a)\). Its positive finite expansion has the original compact constrained action; uniform factorial estimates and polynomial state counting imply that its conditional maximum is precisely that sum. At the projected original strict state its hidden maximizer is strict. The leaf and gate Hessians make the hidden Hessian negative definite there, so the maximizing hidden variables continue analytically for nearby incident variables. Therefore eliminating those variables gives the actual analytic phase \(\sum g(x_a)\), including its derivatives, not merely a numerical equality at one point.

For each strict gate write
\[
 m(x,y,z)=J(x+y)+J(z)-J(x)-J(y)
       -J(z-x)-J(z-y)-J(x+y-z).
 \tag{16}
\]
The grouped phase at zero angles is consequently
\[
 A(\mathbf y,0)=\sum_{g\text{ bare}}m(x_g,y_g,z_g)
              +\sum_{v\text{ circle}}\sum_{e\sim v}g(x_e).
 \tag{17}
\]
It has the original maximum \(F_0\) and the projected original strict maximizer \(\mathbf y^*\). The exact positive expansion above also shows that its compact complement has a strict original-source gap. More directly, \(g''<0\) on \((0,1/2)\), and the retained gate action \(m\) has a negative definite three-variable Hessian in its strict domain. These facts are proved from the original volume atoms in the [general core packet theorem](actual_conway_general_core_packet_and_gap.md), Sections 1 and 3–5. Every circle-incident edge variable is covered by a \(g\) term; every remaining edge and every hidden bare variable is an argument of a retained \(m\). Hence the combined Hessian in the primitive coordinates is negative definite. Global concavity then gives uniqueness of the grouped maximum.

Choose the rectangular box \(\mathcal W\) about \(\mathbf y^*\) so its closure is entirely strict. All affine factorial arguments in every bare gate lie in a fixed compact subinterval of \((0,1)\), circle-incident edges are regular low, bare–bare edges stay in the interior of \((0,1)\), and (13) holds throughout the box. For all sufficiently large \(N\), every point of the entire integer box is an actual supported state; no indicator changes there.

## 4. What is replaced before the packet is used

The source-to-window reduction is an absolute error statement at the augmented exponent \(F_0\). It is not a relative error assertion at a filled critical action.

First, the grouped component induction gives a fixed loss for its error terms and for high component-boundary indices. In an entirely trivalent component, the error contains the extra cubic trace terms; the clean part retains all old-supported internal indices, including high ones. Thus no general loss is asserted for a high internal bare–bare edge. The proof applies to the actual fixed crossing \(R_s^n\) in place of \(R_s^{\epsilon}L_j\): a fixed power and its inverse have polynomial spectral norm on every \(|s|\le R<1\), and the exact coefficient extractor sends that bound into the same low/high cone. The old error recursion is multilinear and homogeneous in the boundary constants. Thus an inherited full-cone deficit crosses the next component without paying an extra \(2G_0\); new errors use (1) in the path class and the simultaneous comparison in the trivalent class. This is the distinction proved in the [component extension](actual_main_meridian_component_extension.md), Section 6. The tree is fixed, so the finite minimum of the structural gaps is positive. Prefactors may depend on the fixed integers \(n_v\); the exponential deficits do not depend on their size.

For the remaining contraction, the component boundary indices are low. Trivalent bare tensors are already the positive complete tensors. Other allowed components use their whole-hub majorant before regular replacement. No spectral norm is substituted for that coefficientwise comparison. At a circle vertex and for any low product \(E\), the actual fixed-power trace has the same-level bound
\[
       |\phi_\sigma(R_\sigma^nE)|
             \le C_{n,R,D}N\,\phi_0(L_NE),
       \qquad |\sigma|\le R<1.
 \tag{18}
\]
One direct proof uses the exact shifted root sum for generic \(\sigma\), on a larger parameter circle where \(\sin2\pi\sigma\) is bounded away from zero. Each shifted root has angular imaginary height \(O(N^{-1})\). Positivity of the Laurent coefficients of \(E(-u-u^{-1})\) bounds its value by \(C E(-2)\); the fixed-power full chirp has bounded modulus on this grid. The root sum is at most \(C N^2E(-2)\). Divide by the lower bound (14), then apply the maximum principle to the whole holomorphic trace to include the collisions \(\sigma=0,\pm1/2\). This proves (18) with the full normal data. Constant opposite-color types have the same bound with their prescribed scalar retained.

Complete bare tensors have the positive expansion (10). The all-parity whole-hub comparison for the old component class, the exact old tensors in the trivalent class, and (18) therefore bound the remaining contraction by a polynomial times the original pure positive reference. A retained edge assignment outside the neighborhood in (13) misses the unique original optimizer and loses a fixed action amount. This proves the off-edge-window error before any circle contour is moved.

Inside that neighborhood, a trivalent bare trace is exactly unchanged. Indeed the old pair support gives \(i+j+k\le3d/2<2N-1\). In division by \(P_0\), the quotient has degree at most \(N-2\); the constant change \(P_0\mapsto P_0+\Delta_\sigma\) cannot change the remainder's coefficient of degree \(N-1\). Thus \(\phi_\sigma(e_i e_j e_k)=\phi_0(e_i e_j e_k)\), including the full internal label range.

At the other allowed vertices, the regular bare estimate is
\[
 \phi_\sigma\left(\prod_{e\sim v}e_{n_e}\right)
 =\phi_0\left(\prod_{e\sim v}e_{n_e}\right)
                   (1+O_R(e^{-\kappa_vN})),
 \tag{19}
\]
uniformly over the physical indices, both parities and \(|\sigma|\le R\). It uses precisely the compact low-index and incident-sum hypotheses in (13). For valence at most four the identity is exact. For higher valence it follows from strict Fourier-tail separation in the [regular bare trace](actual_main_meridian_regular_bare_trace.md). Multiplying out the finitely many errors in (19), and using (18) and the positive reference, bounds their total by \(N^A e^{N(F_0-\kappa)}\). No independent relative errors of oscillatory filled tensors are multiplied.

After this replacement, resolve every complete bare tensor by (10). The positive reference now bounds the sum of any subset of these resolved states. Its strict optimizer projects to \(\mathbf y^*\), and removing the grouped primitive box \(\mathcal W\) has a fixed loss. This is the hidden-variable part of the off-window argument, not a claim that an unresolved scalar upper bound controls every uncontracted path.

Consequently the exact original source, after its recorded outer framing and cut factors have been kept, differs from applying the actual circle trace functionals to (4) by
\[
                  O\!\left(N^A e^{N(F_0-\eta_0)}\right),
                  \qquad \eta_0>0.
 \tag{20}
\]
The number \(\eta_0\) can be chosen below the finite minimum of the component losses, the original compact-complement losses, and the regular bare losses. These are geometric or closed coefficient-rate losses. Thus one fixed positive choice works for every compact main disk \(R<1\), with constants and the starting level depending on \(R\); the finite Fourier multipliers, fixed-power polynomial bounds and bounded edge factors affect only those constants. It is also independent of how large the fixed crossing powers subsequently are. This statement does not compare (20) with a filled exponent; that requires the joint saddle.

## 5. Canonical analytic interpolation and the finite summand

Use the canonical marked sine-factorial interpolation
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
  \prod_{a\ge1}
   \frac{\Gamma(Na+z+1)}{\Gamma(Na-z)(Na)^{2z+1}}.
 \tag{21}
\]
It is zero-free on \(-1<\Re z<N\), equals \(S_k\) at integer \(k\), and satisfies
\(G_N(z+1)/G_N(z)=2\sin(\pi(z+1)/N)\).
The positive real marks and their analytic continuations are those in [exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md); no arbitrary continuation of grid values is used. On fixed bulk complex compact sets,
\[
 G_N(N\alpha+c)=\sqrt{2N\sin\pi\alpha}\,
       e^{NJ(\alpha)}(2\sin\pi\alpha)^c
                       (1+O(N^{-1})),
 \tag{22}
\]
with uniform fixed derivatives and further uniform inverse-power expansions. The fixed integer \(c\) must be kept.

Replace the factorials in (9) by (21), with their exact affine arguments. For the circle-incidence factors, put \(u=N\tau/(2\pi)\) and use
\[
 \mathcal E_N(x,\tau)=
 \frac{G_N(d/2+u)G_N(d/2-u)}
 {G_N(d/2-Nx+u)G_N(d/2-Nx-u)G_N(Nx)^2}.
 \tag{23}
\]
The shift equation proves \(\mathcal E_N(n/N,\tau)=e_n(-2\cos\tau)\) exactly. On a fixed complex neighborhood of the regular wire box and a fixed small angular polydisk, every argument is in a regular bulk strip. Formula (22), including the \(-1/2\) midpoint offsets, gives
\[
 \mathcal E_N(x,\tau)
   =\frac{e^{Nb(x,\tau)}}{2N\sin\pi x}(1+O(N^{-1})),
 \quad
 b(x,\tau)=\int_0^x
       \log\{2\cos(2\pi u)+2\cos\tau\}\,du-2J(x).
 \tag{24}
\]
The logarithm is continued from its positive value at real \(x\in(0,1/2)\), \(\tau=0\). In particular \(b(x,0)=g(x)\). If an exact index is \(N\ell(\mathbf y)+\delta\), substitute \(x=\ell+\delta/N\) in (23). Its leading amplitude then includes \(e^{\delta b_x(\ell,\tau)}\). The proof retains these factors by the exact interpolation rather than renormalizing them away.

The exact edge continuation is
\[
 \mathcal I_N(x,s)
    =\frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}.
 \tag{25}
\]
Indeed \(G_N(s)G_N(-s)=1/H_N(s)\), and the shift equation gives \(\mathcal I_N(n/N,s)=H_N(s)/W_n(s)\). Uniformly on the fixed complex regular wire tube and \(|s|\le R<1\),
\[
 \mathcal I_N(x,s)
       =1-\frac{\pi s^2}{N}\cot(\pi x)+O_R(N^{-2}).
 \tag{26}
\]
To verify the sign, put \(L_N(z)=\log G_N(z)\). Then \(L_N''(Nx)=\pi\cot(\pi x)/N+O(N^{-2})\), and
\[
2L_N(Nx)-L_N(Nx-s)-L_N(Nx+s)
 =-s^2L_N''(Nx)+O(N^{-3}).
\]
All fixed derivatives have the same uniform bounds on smaller tubes.

Let \(\mathcal A(\mathbf y,\boldsymbol\tau)\) be the sum of the gate actions (16) and the circle-incidence actions \(b(x_e,\tau_v)\). Combining (22)–(26), the exact interpolated summand of (4), divided by \(\Gamma_{\mathrm{edge},N}\), is
\[
 N^a\,\beta_N(\mathbf y,\boldsymbol\tau)
       e^{N\mathcal A(\mathbf y,\boldsymbol\tau)}
       \prod_e\mathcal I_N(n_e/N,s),
 \qquad a=-D_c-\frac32G,
 \tag{27}
\]
where \(\beta_N=\beta+O(N^{-1})\) is uniformly holomorphic and \(\beta\) is nonzero, positive at real zero angles. It contains every \(d\)-offset and every square-root mark. The phase is independent of \(s\) and is separately even in the angular variables.

## 6. The finite lattice contour and its endpoint currents

The exact finite lattice sum, rather than a formal integral, is treated as follows. At zero angles its phase has the strict nondegenerate maximum \(\mathbf y^*\) in the primitive box. The implicit-function theorem gives a unique holomorphic wire saddle \(y_*(\boldsymbol\tau)\) on a fixed complex angular polydisk. Put
\[
 \Psi(\boldsymbol\tau)=\mathcal A(y_*(\boldsymbol\tau),\boldsymbol\tau),
 \qquad Q(\boldsymbol\tau)=-\mathcal A_{yy}(y_*,\boldsymbol\tau).
 \tag{28}
\]
The matrix \(Q\) is positive definite at zero. Choose its determinant square root by the original positive real Gaussian.

For each primitive coordinate enclose precisely its retained finite integer interval by a rectangle whose vertical sides are half-grid lines and whose horizontal sides have imaginary heights \(\pm h\). The product residue formula with kernels \(\pi N\cot(\pi Nz)\) is exactly the sum (4). The endpoints differ from the chosen real box by \(O(N^{-1})\). On a vertical half-grid side the cotangent has modulus at most one; on horizontal sides,
\[
 \cot(\pi N(x+ih))=-i+O(e^{-2\pi Nh}),
 \qquad
 \cot(\pi N(x-ih))= i+O(e^{-2\pi Nh}).
 \tag{29}
\]
At zero angular parameter the phase gains at most \(O(h^2)\) under these imaginary translations. The real boundary has a fixed strict loss. Choose \(h\) first so this gain is smaller than both half the boundary loss and \(\pi h\), and then shrink the fixed angular polydisk. Every contour with a vertical coordinate is exponentially below \(\Re\Psi\); every nonconstant cotangent mode has the factor \(e^{-2\pi Nh}\) and loses an exponential after allowing the phase gain. Uniformly bounded edge insertions and their derivatives do not change these losses.

The constant horizontal terms add to \(N^K\) times the ordinary integral over the real box. Their connectors and the \(O(N^{-1})\)-wide changes of endpoints have the same boundary loss. Deform this integral to \(y_*(\boldsymbol\tau)+(\mathcal W-\mathbf y^*)\). This stays inside the fixed tube, its connecting faces have a fixed loss, and its real translated tangent plane has a uniformly negative real quadratic part. Gaussian expansion now gives
\[
 a(\boldsymbol\tau)=
   \frac{(2\pi)^{K/2}\beta(y_*(\boldsymbol\tau),\boldsymbol\tau)}
        {\sqrt{\det Q(\boldsymbol\tau)}}.
 \tag{30}
\]
It is nonzero near zero. Odd Gaussian corrections integrate to zero; the first relative remainder is \(O(N^{-1})\), holomorphic on a fixed neighborhood. Equation (12) gives the power in (5). This is the same finite-contour argument as the [finite complex-window Laplace theorem](actual_conway_complex_window_laplace.md), Section 3, applied to the actual grouped lattice rather than reusing its ungrouped dimension.

Every factor in (27) is separately even in each angle. Uniqueness gives the same symmetry to \(y_*,\Psi,a\). Also \(\mathcal A_{y\tau_v}(\mathbf y,0)=0\) identically in the wire variables. Direct differentiation of (24) gives
\[
 b_{\tau\tau}(x,0)=-\frac{\tan\pi x}{2\pi}.
 \tag{31}
\]
Thus the usual Schur-complement correction to the angular Hessian vanishes at zero, proving (6). This is an exact consequence of the even source, not an assumed diagonal approximation.

The same contour proves the insertion rule used in (8). For any fixed holomorphic function \(c(\mathbf y,\boldsymbol\tau)\), the normalized finite sum with this extra factor is \(c(y_*(\boldsymbol\tau),\boldsymbol\tau)+O(N^{-1})\), uniformly holomorphically. To see the error order, expand \(c\) about the saddle: its linear Gaussian term is odd, while the quadratic term and the linear term paired with the cubic phase correction cost \(N^{-1}\). The exponentially small finite-grid currents remain negligible. Expand the product of (26), apply this insertion rule to \(-\pi s^2\sum_e\cot(\pi x_e)\), and bound its \(O(N^{-2})\) remainder on the deformed Gaussian contour. Dividing by the nonzero saddle expansion at \(s=0\) proves (8). No unknown common coefficient of order \(N^{-1}\) is needed, because it cancels in the ratio.

## 7. Global angular bounds and real spectators

Fix a compact regular interval \(I\subset(0,1/2)\). For a physical \(n/N\in I\), there are \(c,C,y_0>0\) such that
\[
 |e_n(-2\cos(t+iv))|
       \le N^A e^{Ng(n/N)}e^{-Nct^2+NCv^2},
       \qquad |t|\le\pi,\quad |v|\le y_0.
 \tag{32}
\]
Here is a proof that separates the regular center from moving numerator zeros. On a fixed small disk about \(t=0\), every numerator factor is nonzero. The exact finite product is even, and its logarithmic second derivative at zero is
\[
 -\frac12\sum_{a=0}^{n-1}
       \sec^2\frac{\pi(a+1/2)}N
       =-\frac{N}{2\pi}\tan(\pi n/N)+O(N^{-1}).
 \tag{33}
\]
All fixed higher derivatives of the logarithm are \(O_I(N)\). Together with
\(e_n(-2)=e^{Ng(n/N)}[2N\sin(\pi n/N)]^{-1}(1+O(N^{-1}))\), this gives (32) near the center by an even analytic Taylor estimate.

On the compact real complement, the limiting numerator logarithmic integral is strictly smaller than its value at zero. In fact it is the integral of \(\log|1-e^{iu}|\) over a circular arc of fixed length \(4\pi x\); for \(0<x<1/2\) this is uniquely largest when the arc is centered opposite its singularity. This is exactly the circular rearrangement argument in the [root-star localization theorem](actual_conway_root_star_full_jet_localization.md), Section 7. Uniform truncated logarithmic Riemann sums provide the closed upper bound even when numerator zeros move or coalesce. The negative logarithmic tails of the two circle-distance factors are uniformly integrable; denominator factorial errors are \(O(\log N)\). Thus the compact complement has a fixed exponential loss, uniformly in \(x\in I\).

Continuity of this logarithmic integral preserves half the loss on a sufficiently small complex strip. The uniform \(o(1)\) in the finite upper estimate is absorbed in another quarter of that loss for all sufficiently large \(N\). Reducing \(c\) so \(c\pi^2\) is smaller than the remaining loss proves (32) on the complement. This absorption is why a polynomial prefactor is legitimate in (32), although a global complete-core recurrence bound at arbitrary indices only has a uniform \(e^{No(1)}\) prefactor. No uniform polynomial core bound at collisions has been assumed.

In (4) every circle-incident edge index stays in one such compact interval. Apply (32) at every circle incidence. All bare coefficients in (4) are nonnegative, and the edge ratios are uniformly bounded. The zero-angle positive sum has rate \(F_0\) with a polynomial bound, either by (5) at zero or directly by the regular factorial expansion and fixed-dimensional Laplace estimate. Summing yields (7), with a strictly positive angular loss for every circle since every circle has an incident edge.

The actual polynomial in each angle is periodic. Therefore replacing a real endpoint \(\pm\pi\) by \(\pm\pi+O(N^{-1})\) changes the relevant squared distance to the nearest multiple of \(2\pi\) by only \(O(N^{-1})\). This costs a bounded factor in (7). Complex translations of height \(O(N^{-1})\) are also permitted. Consequently endpoint currents with real spectator variables, or spectators on their physical translated grids, retain a fixed angular loss. No spectator is required to lie on a slope-dependent complex contour for this assertion. Cauchy's estimate on disks of radius \(1/N\), and on a slightly larger main-parameter disk, supplies the stated derivative bounds.

## 8. Applying the crossing traces

Let \(\mathcal D_{n,\sigma,N}[f]=\phi_\sigma(R_\sigma^n f^\sharp)\), where \(f(\tau)=f^\sharp(-2\cos\tau)\). With its full crossing scalar,
\[
 R_\sigma^n(z_r(\sigma))
   =C_{N,n}(\sigma)e^{inN\tau_r(\sigma)^2/(4\pi)},
 \quad C_{N,n}(\sigma)=q^{n(d^2/4-\sigma^2/2)},
 \quad\tau_r(\sigma)=\frac{2\pi}{N}(d/2+\sigma-r).
 \tag{34}
\]
The actual orientation type selects \(\sigma_v=s,-s\), or \(0\), and supplies its recorded reference scalar \(\rho_{v,N}(s)\). Keep the original closing/framing scalar \(\zeta_N(s)\) separate, and define
\[
 \widehat\zeta_N(s)=\zeta_N(s)\prod_v\rho_{v,N}(s).
 \tag{34a}
\]
The per-type factors are specified in the [filled-volume theorem](actual_main_meridian_filled_volume.md); the [joint filling transform](actual_main_meridian_joint_filling_transform.md), (4a), uses the same combined-factor convention. The edge product remains exactly \(\Gamma_{\mathrm{edge},N}\). The exact polynomial functionals in distinct angular variables commute as evaluations of a fixed tensor contraction. This is not a statement that physical tangles commute.

The source-to-packet conclusion has the form
\[
 \mathcal F_N(q^s)
   =\widehat\zeta_N(s)H_N(s)
       \left(\prod_{v=1}^H\mathcal D_{n_v,\sigma_v(s),N}^{(v)}\right)
                 B_N(\boldsymbol\tau,s)
        +O\!\left(N^Ae^{N(F_0-\eta_0)}\right),
 \tag{35}
\]
with the harmless outer elementary factors understood in the displayed normalization. Equation (34a) records the closing/framing and reference factors explicitly; there is exactly one primitive main-cut factor \(H_N\). The edge scalars in (4) are not counted again in \(\widehat\zeta_N\). Formula (35) includes the high-state, off-window and moving-bare replacement errors described in Section 4. It asserts neither that the error is relative to a filled scalar nor that a first local Fourier charge may be selected independently at every circle.

The packet is precisely suitable for the joint transfer: exact separate evenness, a nonzero complex wire saddle, diagonal negative angular Hessian, a fixed angular corridor, and real-spectator endpoint bounds. The [joint filling transform](actual_main_meridian_joint_filling_transform.md), Sections 3–5, proves the charge comparison and controls the nonperiodic endpoint currents. It uses (4)–(8) as inputs; it is not used to prove them. The resulting invariant statement appears in the [filled-volume theorem](actual_main_meridian_filled_volume.md).

The present proof uses the original positive source action and its strict geometric optimizer, but does not import an old filled-invariant volume asymptotic. A subsequent joint first-charge calculation can supply its own nonzero filled amplitude; identifying that action geometrically is a separate marked-action statement.

If that later transfer selects a nondegenerate joint first-charge saddle, the analytic insertion proof above can be applied once more to the combined wire-and-angle contour. After retaining the exact product of edge, crossing, reference and framing scalars outside, the residual edge multiplier is
\[
   1-\frac{\pi s^2}{N}
                \sum_e\cot(\pi x_e^{\mathrm{fill}})
                         +O_R(N^{-2}).
 \tag{36}
\]
Here \(x_e^{\mathrm{fill}}\) denotes the generally complex wire value at that **filled** joint saddle. It must not be replaced by the complete value \(x_e^*\). This is a conditional Gaussian insertion corollary, not a cusp identification. The common first saddle coefficient cancels in the ratio; exponentially smaller charges and endpoint currents must first be controlled by the separate joint argument. No conclusion about a growing slope, bare components outside the three alternatives in Section 1, or an arbitrary main-meridian ordinary-color subtraction follows from the packet theorem.
