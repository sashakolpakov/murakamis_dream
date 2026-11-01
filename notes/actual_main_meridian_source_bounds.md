# Source growth near the complete main meridian

Fix a knot construction made by stacking and turning two-strand tangles, with \(H\ge2\) original pieces. Before inserting their long twists, keep the crossing circle around each piece. The resulting **augmented complement** is the complement with these crossing circles left unfilled. Their integer colors \(j_i\in\{1,\ldots,N\}\) label the ordinary representations used in the quantum calculation; they have not yet been summed with filling coefficients.

A **product junction**, also called a hub below, is a place where several tangle operators are multiplied without intervening turns. Combine adjacent product junctions until every remaining internal edge carries a quarter-turn. Mark a junction when one of its original crossing-circle operators occurs there without that outer turn; such a junction is called flagged. A junction without this operator is called bare. We assume that **no two bare junctions are adjacent**. The number of junctions and their valences may be any fixed finite numbers.

The construction must also satisfy the existing [strict Conway conditions](actual_conway_all_strict_tree_long_twist_volume.md): its retained angle inequalities have an interior solution, its prescribed endpoint tracing gives one main component, and it has no internal closed component. These conditions refer to the original ordered tangle diagram. For two pieces, retain the knot-producing half-twist choices; those contain the pure leaf needed by the two-leaf asymptotic theorem.

**Supremum-volume theorem.** Let \(\mathcal F_{N,\mathbf j}^{\epsilon}(M)\) be the reduced quantum scalar obtained by cutting the specified main strand, with reduced unknot value one and the original framing retained. The main meridian color variable has complete value \(M=1\). Write \(M=q^s\), \(q=e^{\pi i/N}\); bounded \(s\) describes a neighborhood of size \(O(1/N)\) in \(M\). Let \(Y^\epsilon\) be the complete augmented complement of the original construction. For every fixed \(0\le R<1\),
\[
\boxed{\displaystyle
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\sup_{\substack{|s|\le R\\\mathbf j\in\{1,\ldots,N\}^{H}}}
 \left|\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\right|
 =\operatorname{Vol}(Y^\epsilon).}
\]
The limit runs through both parities. The upper bound is uniform over the displayed meridian disk and every auxiliary color. The matching lower bound uses the particular complete value \(s=0\), \(\mathbf j=(N,\ldots,N)\). It is therefore an equality for the supremum, not a lower bound at each displaced meridian or at each color tuple.

![Two bare multiplication junctions feed a central junction carrying the original crossing-circle operator, with a quarter-turn on each internal edge.](../book/figures/separated-product-junctions.svg)

Two bare product junctions are separated by a junction carrying the original crossing-circle operator \(p_0\). Multiply each outer pair, apply the quarter-turn \(T\) along each junction edge, and close after multiplying by \(p_0\). The definitions \(p_i=R^{\epsilon_i}L_{j_i}\), \(h_i=T(p_i)\) retain every original auxiliary color. Here \(R^{\epsilon_i}\) is the prescribed half-twist and \(L_{j_i}\) encircles the strands by the circle of color \(j_i\). The drawing represents algebraic operations and their order; it is not a knot projection.

The theorem concerns the quantum sum **before the auxiliary fillings**. It does not identify the generally smaller volume of the resulting filled knot at a displaced main meridian. The previously established complete-meridian filled-knot equalities remain separate results. A limiting normalized meridian profile and a general estimate for adjacent bare junctions also remain open.

Moving the main meridian changes both the multiplication of polynomial operators and the physical turn. The extra multiplication terms have alternating signs; estimating them separately can lose the correct exponential rate. The proof instead first controls a turn preceded by the actual crossing-circle operator, and then compares a whole bare junction with the positive complete calculation after summing its signed terms. At even levels, an adjacent odd level is used only inside the estimate; an exact map of positive summation paths returns the bound to the original level. The detailed definitions of the polynomial norm, repeated-root derivatives, and geometric action follow below.

The finite physical inputs are the [typed main-meridian compiler](actual_main_meridian_newton_compiler.md), the [six physical turn formulas](actual_main_meridian_turn_comparison.md), the [actual crossing-circle normalization](actual_crossing_circle_source_and_filling.md), and the [positive complete Newton multiplication law](actual_positive_newton_multiplication.md). The needed crossing, loop, quotient, Fourier, and adjacent-level estimates are proved explicitly below. The complete geometric pressure comparisons are identified where they enter.

## 1. Actual decorated turns: coefficients, norms, and angular localization

### 1.1. The fixed coordinates and the two actual algebras

Fix
\[
N\ge2,\quad d=N-1,\quad m=\lfloor d/2\rfloor,
\quad \theta=\pi/N,\quad q=e^{i\theta},\quad Q=q^2,
\quad x=-q^{-1}q^s,\quad y=-q^{-1}q^{-s}.
\tag{D1}
\]
The microscopic main meridian is \(M=q^s\). The two roots \(x,y\) give the actual dual modules, denoted by signs \(+,-\). Write \(\mathsf T_N(t+t^{-1})=t^N+t^{-N}\). Equal-color ordered pairs have relation
\[
P_s(z)=\mathsf T_N(z)+2\cos(2\pi s),
\tag{D2}
\]
whereas opposite-color pairs have the constant relation \(P_0\). The same relation (D2) applies to the two equal-color orders, since it is even in \(s\). At every vertex use the relation of its actual ordered object; these two quotient multiplications are not identified.

All polynomial coordinates below are in the fixed complete basis
\[
S_n=\prod_{r=1}^n2\sin(r\theta),\qquad
c_j=2\cos((2j+1)\theta),\qquad
 e_n(z)=S_n^{-2}\prod_{j=0}^{n-1}(c_j-z),\quad0\le n<N.
\tag{D3}
\]
Empty products are one. A canonical polynomial always has degree less than \(N\), independently of the relation used to obtain it. Let
\[
\|F\|_{\mathrm J}=\max\bigl\{|F(c_j)|:0\le j\le m;
\ |F'(c_j)|:c_j\text{ is a double root of }P_0\bigr\}.
\tag{D4}
\]
At odd levels the last node \(-2\) is simple and has no derivative coordinate. This is a norm on canonical polynomials. It is polynomially equivalent, uniformly in level and parity, to the canonical sup norm on \([-2,2]\) and to the Chebyshev coefficient norm. This comparison uses full Hermite interpolation; it does not discard first normals or evaluate only on the moving simple nodes.

For either relation define
\[
\phi_{\sigma}(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
\qquad \sigma=s\text{ or }0.
\tag{D5}
\]
Then the exact fixed-basis metric is
\[
\phi_\sigma(e_i e_j)=\mathbf1_{i+j=d}.
\tag{D6}
\]
Indeed, at \(\sigma=0\) this is the complete Newton metric. For \(\deg(e_i e_j)\le2N-2\), divide \(e_i e_j=P_0A+B\). The degree of \(A\) is at most \(N-2\), so the moving remainder \(B-\Delta_s A\), \(\Delta_s=2\cos2\pi s-2\), has the same coefficient of \(z^d\). This proves (D6), including the return sectors of the multiplication. If \(F=\sum f_n e_n\) is canonical, it follows that
\[
f_{d-k}=\phi_\sigma(e_kF).
\tag{D7}
\]
The product in (D7) is reduced in the input object's relation.

### 1.2. Polynomial quotient estimates, with returns retained

Set \(C_n(t+t^{-1})=(t^n+t^{-n})/2\), \(C_0=1\), and use \(\|\sum a_nC_n\|_{\mathrm{Ch}}=\sum|a_n|\). The identity \(2C_iC_j=C_{i+j}+C_{|i-j|}\) makes this norm submultiplicative. In (D2), \(C_N=-b\), \(b=\cos2\pi s\), so
\[
\operatorname{rem}C_{N+r}=-2bC_r-C_{N-r}\quad(0<r<N),
\qquad
\operatorname{rem}C_{kN+r}=-2b\operatorname{rem}C_{(k-1)N+r}
 -\operatorname{rem}C_{(k-2)N+r}.
\tag{D8}
\]
For \(r=0\), start with \(1,-b\). For \(|s|\le R\), put \(L_R=2\cosh(2\pi R)+1\). Induction gives
\[
\|\operatorname{rem}_{P_s}F\|_{\mathrm{Ch}}\le L_R^h\|F\|_{\mathrm{Ch}}
\quad(\deg F\le hN).
\tag{D9}
\]
The same estimate includes the opposite-color relation by setting \(s=0\). It is a polynomial identity argument, valid even at repeated roots. In particular, a fixed number of canonical factors obeys
\[
\left\|\operatorname{rem}_{P_\sigma}\prod_{a=1}^h F_a\right\|_{\mathrm J}
 \le C_{R,h}N^{C_h}\prod_a\|F_a\|_{\mathrm J}.
\tag{D10}
\]
Here and below a displayed power of \(N\) is independent of the physical auxiliary colors and of \(s\) in its specified disk. It can depend on fixed word length or tree size. The sup-to-Chebyshev comparison follows from the cosine integral for coefficients, and the derivative bound from Markov's inequality. Combining it with full complete Hermite interpolation proves (D10).

For a canonical polynomial, its top monomial coefficient is a fixed multiple of its top Chebyshev coefficient: \([z^d]C_d=1/2\) for \(d\ge1\). Hence
\[
|\phi_\sigma(F)|\le C N^2\|\operatorname{rem}_{P_\sigma}F\|_{\mathrm{Ch}}.
\tag{D11}
\]
Equations (D9)--(D11) control the whole quotient operation. They do not majorize a return term separately by an old positive gate and do not require an increasing return-permitting open profile.

### 1.3. The physical crossing and circle character

On the equal-color object \(++\), the actual checked crossing has common scalar and stripped spectral values
\[
\kappa_s=q^{(d+s)^2/2},\qquad
 t_j=q^{-2j-1}Q^s,\quad c_j(s)=t_j+t_j^{-1},\qquad
\lambda_j=(-1)^jq^{j(j+1)}Q^{-sj}.
\tag{D12}
\]
For a fixed integer crossing power \(n\), including negative \(n\), let \(r^{[n]}_{N,s}\) denote the canonical polynomial with values \(\lambda_j^n\). Its full physical representative is \(\kappa_s^n r^{[n]}_{N,s}\). The \(--\) object uses \(-s\).

For every fixed \(0\le R<1\) and \(n\),
\[
\sup_{|s|\le R}\|r^{[n]}_{N,s}\|_{[-2,2]}+
\sup_{|s|\le R}\|\partial_zr^{[n]}_{N,s}\|_{[-2,2]}
 \le C_{R,n}N^4.
\tag{D13}
\]
Here is the collision-safe argument. Away from \(\sin2\pi s=0\), exact Lagrange interpolation is
\[
r^{[n]}_{N,s}(z)=
-\frac1{N(U-U^{-1})}\sum_{j=0}^{N-1}
\lambda_j^n(t_j-t_j^{-1})\frac{P_s(z)}{z-c_j(s)},
\qquad U=e^{2\pi is}.
\tag{D14}
\]
The quotient is a divided difference of \(\mathsf T_N\). Nodes lie in a Bernstein ellipse of angular height \(2\pi|\operatorname{Im}s|/N\), on which its first two derivatives are \(O_R(N^2),O_R(N^4)\). Integrating along the segment from a real point to a node gives (D13) with the extra factor \(|\sin2\pi s|^{-1}\). Distinct-node collisions inside \(|s|<1\) occur only at \(s=0,\pm1/2\). Their paired indices satisfy \(j+l+1-2s=N\), and exactly
\[
\lambda_l/\lambda_j=(-1)^{l-j}q^{(l-j)(j+l+1-2s)}=1.
\tag{D15}
\]
Both the value difference and the node difference vanish, the latter simply. The resulting divided differences are holomorphic, and the confluent interpolation matrix is invertible. Thus the polynomial coefficients extend holomorphically across those collisions. Apply the maximum principle on a fixed larger parameter circle of radius less than one and different from \(1/2\) to remove the apparent denominator uniformly. This proves (D13). The common scalar \(\kappa_s^n\), its inverse, and each prescribed fixed framing correction are bounded on the same disk: their ratio to the complete scalar has exponent \(O_{R,n}(1)\). They are retained, not set equal to one.

For mixed orders use the physical carrier convention of the turn theorem:
\[
G_{-+}=\check R_{x,y}r_0(\Omega_{x,y})^{-1},\qquad G_{+-}=I,
\qquad r_0=\kappa_0\sum_{n=0}^{d}(-q)^ne_n.
\tag{D16}
\]
The forward mixed crossing has reference polynomial \(r_0\). Reversing the reference order adds the exact monodromy scalar, since
\[
\check R_{y,x}\check R_{x,y}=q^{-s^2}r_0(\Omega)^2.
\tag{D17}
\]
Thus reverse crossings, inverses, and every fixed composable crossing word have the corresponding fixed powers of \(r_0\) and the retained powers of \(q^{-s^2}\). Formula (D13) at \(s=0\) and (D10) bound their canonical norms polynomially. These assertions concern the specified Casimir intertwiner spaces, not arbitrary physical matrix norms.

For an ordinary auxiliary color \(1\le j\le N\), the actual encircling operator is exactly
\[
L_j(\Omega)=(-1)^{j-1}U_{j-1}(\Omega/2).
\tag{D18}
\]
To retain its normalization, take the auxiliary module of weights \(j-1-2a\), \(0\le a<j\), with actual closing pivot \(K_j^{1-N}=(-1)^{j-1}K_j\). First take independent generic target roots. Their tensor product has distinct typical highest summands. On a summand of highest root \(w\), the nilpotent transfers cannot contribute to the highest coefficient of the encircling monodromy, and the Cartan and standard-pivot trace is
\[
\sum_{a=0}^{j-1}(qw)^{j-1-2a}
 =U_{j-1}\bigl((qw+q^{-1}w^{-1})/2\bigr).
\tag{D19}
\]
The actual pivot supplies the sign in (D18). Since the loop intertwines, the generic highest coefficients prove the whole matrix identity. All finite auxiliary transfer denominators are \([r]!\) with \(r<j\le N\), nonzero at this root, so its matrix entries are Laurent regular in the independent target roots. Specialization proves (D18) on equal and opposite objects with every confluent coefficient retained. Rigid duality and the braid carriers transport the same central polynomial; the Casimir is fixed by the antipode. This keeps the prescribed encircling direction and framing. No auxiliary dimension division, extra carrier scalar, or modified main-cut factor is part of (D18).

Finally \(\|U_{j-1}(z/2)\|_{[-2,2]}\le j\le N\), and Markov bounds its derivative by \(CN^3\). Combining (D13), (D16)--(D18), and (D10), the actual fixed-power decorated coupon, written \(R_s^\epsilon L_j\) in its specified frame, has polynomial canonical norm, uniformly in \(j\). The original \(\epsilon\in\{0,\pm1\}\) is allowed; the same argument allows any fixed composable integral crossing power.

### 1.4. Every typed turn gives the same coefficient estimate

Put
\[
H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
W_n(s)=\prod_{r=1}^{n}\left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right),
\quad \mathcal R e_n=e_{d-n},\quad \mathcal D_s e_n=W_n(s)e_n.
\tag{D20}
\]
Removable values at zero are understood. The exact physical turn in fixed polynomial coordinates is \(\gamma_N(s)H_N(s)^{-1}\mathcal R\mathcal D_s\), with the following domains. Mixed morphisms are expressed in (D16)'s reference.

| Input | Output | \(\gamma_N(s)\) |
| --- | --- | --- |
| \(\operatorname{End}(++)\) | \(\operatorname{Hom}(-+,+-)\) | \(q^{-s^2/2}\) |
| \(\operatorname{Hom}(-+,+-)\) | \(\operatorname{End}(--)\) | \(q^{s^2/2}\) |
| \(\operatorname{End}(--)\) | \(\operatorname{Hom}(+-,-+)\) | \(q^{s^2/2}\) |
| \(\operatorname{Hom}(+-,-+)\) | \(\operatorname{End}(++)\) | \(q^{-s^2/2}\) |
| \(\operatorname{End}(+-)\) | \(\operatorname{End}(-+)\) | \(1\) |
| \(\operatorname{End}(-+)\) | \(\operatorname{End}(+-)\) | \(1\) |

The source proof in the turn theorem uses actual currying, with \(J_xw_a=(-x)^aQ^{a(a+1)/2}\varphi_{d-a}\), followed by the carrier. Thus the table retains the duality ratios, cup scalar, and order-change monodromy. It is not obtained by replacing all six spaces by one untyped algebra.

Euler's sine product, applied to the distinct nonzero integers \(r+kN\), gives for every \(|s|\le R<1\)
\[
\left(\frac{\sin\pi R}{\pi R}\right)^2
\le|W_n(s)|\le
\left(\frac{\sinh\pi R}{\pi R}\right)^2,
\qquad W_n(s)W_{d-n}(s)=H_N(s)^2.
\tag{D21}
\]
In particular all the scalars in (D20), their inverses, and the six \(\gamma\)'s are uniformly bounded on that disk.

Let \(E_s\) be any actual canonical input, and form
\[
F_s=\operatorname{rem}_{P_\sigma}(R_s^\epsilon L_jE_s),
\qquad D_s[E_s]=\mathscr T_s^{\mathrm{fix}}F_s=\sum_{k=0}^{d}d_k(s)e_k.
\tag{D22}
\]
Every multiplication and carrier in (D22) uses its specified physical type. Equations (D7) and (D20) give exactly
\[
d_k(s)=\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}
               \phi_\sigma(e_kF_s).
\tag{D23}
\]
This includes the return terms; it is not a projection onto old multiplication support. The norm bounds proved above yield
\[
|d_k(s)|\le C_RN^C\|E_s\|_{\mathrm J}\|e_k\|_{\mathrm J}.
\tag{D24}
\]
Define
\[
J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(u)=J(2u)-4J(u),\quad0\le u\le1/2,
\qquad G_0=g(1/4)=2\,\mathrm{Catalan}/\pi.
\tag{D25}
\]
The [complete Newton bounds](actual_conway_root_star_full_jet_localization.md) are uniform, including both parities and endpoints:
\[
\|e_k\|_{\mathrm J}\le C N^C
\begin{cases}
e_k(-2)=\exp\{Ng(k/N)+O(\log N)\},&0\le k\le m,\\
1,&m<k<N.
\end{cases}
\tag{D26}
\]
Thus (D24) proves the actual deformed low/high coefficient cone. It holds on every fixed \(|s|\le R<1\), not merely the small disk used for the general spectral multiplier comparison. Only its exact diagonal coefficient factors (D21) were needed here.

### 1.5. Reconstruction: the global budget and a fresh Gaussian

From (D24)--(D26),
\[
\|D_s[E_s]\|_{\mathrm J}
 \le C_RN^C e^{2NG_0}\|E_s\|_{\mathrm J}.
\tag{D27}
\]
Indeed low coefficients reconstruct against a second copy of \(e_k\), giving \(\sum_{k\le m}e_k(-2)^2\), whose unique rate maximum is \(2G_0\). The entire high part has only polynomial cost times the input norm.

The same coefficient argument gives more precise angular control. There are \(c,C,y_0>0\) and \(e_N\to0\), independent of \(s,j,E_s\) on the stated families, such that the canonical output satisfies
\[
|D_s[E_s](2\cos(\vartheta+iy))|
\le\|E_s\|_{\mathrm J}
 \exp N\{2G_0-c(\vartheta-\pi)^2+Cy^2+e_N\},
\quad0\le\vartheta\le2\pi,\quad |y|\le y_0.
\tag{D28}
\]
For clarity, this is a fresh estimate from the coefficient cone, not an assertion that the general turn preserves any input Gaussian. The low Newton strip rate is
\[
b(u,\vartheta,y)=\int_0^u
 \log|2\cos2\pi v-2\cos(\vartheta+iy)|\,dv-2J(u).
\tag{D29}
\]
Uniform truncated logarithmic Riemann sums give the closed upper rate even at moving numerator zeros. Circular rearrangement gives \(b(u,\vartheta,0)\le g(u)\), with strictness for \(0<u<1/2\) away from \(\vartheta=\pi\). Thus \(g(u)+b(u,\vartheta,0)\) has its unique maximum \(2G_0\) at \((1/4,\pi)\). In that regular neighborhood its holomorphic action has angular second derivative \(-\tan(\pi u)/(2\pi)\); strict concavity in \(u\) supplies the index quadratic term. This proves the low-part bound (D28); the compact complement has a strict rate gap. The high part has J norm \(\operatorname{poly}(N)\|E_s\|_{\mathrm J}\). Complete Hermite interpolation bounds its canonical values by \(\operatorname{poly}(N)e^{N|y|}\|E_s\|_{\mathrm J}\). Choose \(y_0\) small and \(c\pi^2<G_0\) to absorb that part under (D28). No angular hypothesis on \(E_s\) was used.

Fixed derivatives in \(s\) obey the same rate bounds on smaller parameter disks by Cauchy's estimate. Angular derivatives cost powers of \(N\) on a smaller fixed strip, using radius \(1/N\). These statements require the input family to be holomorphic on the corresponding larger disk, as actual pre-resonance typed coupons are. They do not define an analytic interpolation of a discrete auxiliary-color array.

### 1.6. What can be iterated, and what has not been obtained

Consider the actual fully flagged reduced-hub recursion: an unturned root character multiplies its satellite operators and is then closed; each satellite is either an ordinary decorated leaf \(D_s[1]\), or \(D_s[\prod_a E_{a,s}]\) with the products evaluated in the proper typed quotient. Every internal hub has its specified original character, and every original auxiliary color is retained. For a fixed tree, (D10) and (D27) give by induction
\[
\|E_s\|_{\mathrm J}\le C_RN^{C_{\mathcal T}}
 \exp\{2N G_0\,n(E)\},
\tag{D30}
\]
where \(n(E)\) counts the decorated turns in this recursive subtree. The root coupon has polynomial norm, and (D10)--(D11) bound its normalized closing scalar with the same total budget. In a closed tree with \(H\) original characters, the root is unturned and the other \(H-1\) characters occur in decorated turns. Therefore
\[
|\phi_\sigma(F_{{\mathrm{root}},s})|
 \le C_RN^{C_{\mathcal T}}e^{2NG_0(H-1)}.
\tag{D31}
\]
This is an upper bound for the specified physical auxiliary-colored contraction, uniform over its full finite color cube, fixed half-twist choices, both parities, and \(|s|\le R<1\). The [rigid-profile geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md) identifies \(F_0=2G_0(H-1)\) as its complete augmented action. The result is therefore at that augmented pressure, not a generic sum of costs assigned to arbitrary bare turns or unflagged hubs.

The main reduced cut must still retain its primitive moment factor. For the actual zero-framed cut, the [typed compiler](actual_main_meridian_newton_compiler.md) gives
\[
F_N(M)=\frac{s_x}{s_0}\phi_\sigma(F_{{\mathrm{root}},s}),
\qquad \frac{s_x}{s_0}=H_N(s),\qquad M=q^s.
\tag{D32}
\]
Thus its moving normalization contributes a bounded nonvanishing factor on these disks. The full modified dimension, if used, is retained separately. Equation (D31) concerns the auxiliary-colored contraction; identifying a summed filled invariant requires its original color kernel, framings, and normalization. In particular the filled knot usually has a smaller volume than its augmented parent, so (D31) alone is not the desired filled-knot comparison.

Each individual decorated output has (D28). A moving-quotient product is known here to obey the J budget (D10); its Gaussian localization does not follow from that norm estimate. A subsequent decorated turn nevertheless creates (D28) afresh. The separate [auxiliary-color gap theorem](actual_main_meridian_auxiliary_color_gap.md) uses these fresh Gaussians and an exact half-twist contour to prove a strict loss for the same tree class whenever any original color satisfies \(j_i\le(1-\delta)N\), with fixed \(\delta>0\). That theorem is uniform on \(|s|\le R<1/2\), through both parities and over all other colors; the upper bound here holds on the larger disks \(R<1\).

Neither result gives a lower bound at every displaced meridian, convergence of the normalized regular meridian profile, or a selected classical main-meridian factor. These questions also require more than the complete-value witness used in Section 4.6. No argument here requires a monotonicity claim for an absolute return-sector profile.

## 2. A signed low-coordinate trace comparison at every level

A multiplication hub is a junction where several tangle operators are multiplied without intervening turns; its output may then be turned or closed. The following estimate keeps the whole product inside the exact trace. At even levels, the Fourier terms alternate; an adjacent odd level is used only as an auxiliary bound, then a positive-path map returns the estimate to the original level.

### 2.1. Statement and the exact finite trace

At level \(N\ge2\), put \(d=N-1\), \(m_N=\lfloor d/2\rfloor\), and
\[
S_r^{(N)}=\prod_{a=1}^{r}2\sin(\pi a/N),\qquad
 e_n^{(N)}(z)=\frac{\prod_{a=0}^{n-1}(2\cos((2a+1)\pi/N)-z)}{(S_n^{(N)})^2}.
\tag{F1}
\]
For the moving quotient \(P_{N,s}=\mathsf T_N+2\cos2\pi s\), define
\[
\phi_{N,s}(F)=(-1)^{N-1}N^2[z^{N-1}]\operatorname{rem}_{P_{N,s}}F.
\tag{F2}
\]
Fix the number \(B\) of multiplied factors and a finite parameter radius \(R\). There exist constants \(C_{B,R},A_B\), independent of level and all low indices, such that
\[
\boxed{\quad
\left|\phi_{N,s}\left(\prod_{i=1}^{B}e_{n_i}^{(N)}\right)\right|
 \le C_{B,R}N^{A_B}
 \phi_{N,0}\left(\prod_{i=1}^{B}e_{n_i}^{(N)}\right),
\quad n_i\le m_N,\quad |s|\le R.
\quad}
\tag{F3}
\]
At odd levels the polynomial factor can be omitted, as the positive trace weights below show. A zero on the right forces the left to vanish as well. The radius restriction \(R<1\) is not needed for this trace identity; it is needed separately when applying a physical pre-resonance turn or crossing bound.

Write \(D=\sum_i n_i\), and
\[
F_N(-u-u^{-1})=\sum_{k=-D}^{D}a_k^{(N)}u^k,
\quad d_l^{(N)}=a_{lN-1}^{(N)}-a_{lN+1}^{(N)},
\quad L_N=\lfloor(D+1)/N\rfloor.
\]
The exact trace formula is
\[
\phi_{N,s}(F_N)=N^2\sum_{l=1}^{L_N}
 (-1)^{(N+1)(l+1)}d_l^{(N)}
 U_{l-1}(\cos2\pi s).
\tag{F4}
\]
Here is the full trace calculation. Put \(\eta=(-1)^{N+1}\) and, at generic \(s\), choose \(u_j^N=\eta e^{2\pi is}\). Then \(z_j=-u_j-u_j^{-1}\) are the distinct roots of \(P_{N,s}\), and differentiation gives
\[
P'_{N,s}(z_j)=\frac{2iN\sin2\pi s}{u_j-u_j^{-1}},\qquad
\phi_{N,s}(F_N)=\frac{\eta N}{2i\sin2\pi s}
 \sum_{j=0}^{N-1}(u_j-u_j^{-1})F_N(-u_j-u_j^{-1}).
\tag{F4a}
\]
The root sum selects precisely the Laurent exponents divisible by \(N\). Pair their positive and negative values using \(a_{-k}=a_k\); their contribution is \(\eta^{l+1}N^2d_l\sin(2\pi ls)/\sin(2\pi s)\). This is (F4). Both its sides are polynomials in \(2\cos2\pi s\), because the left is monic quotient reduction and the right uses \(U_{l-1}\). It therefore extends to every collision with the full coefficient trace, including first normals. The factor count bounds \(L_N\le B\).

Every low Newton factor has positive symmetric unimodal Laurent coefficients
\[
[u^{k-n}]e_n^{(N)}(-u-u^{-1})
 =\frac{S_{2n}^{(N)}}{(S_n^{(N)})^2S_k^{(N)}S_{2n-k}^{(N)}},
\qquad0\le k\le2n<N.
\tag{F5}
\]
To verify (F5), factor the Newton numerator exactly as
\[
e_n^{(N)}(-u-u^{-1})=
\frac{u^{-n}}{(S_n^{(N)})^2}
\prod_{j=0}^{n-1}(1+q^{2j+1}u)(1+q^{-2j-1}u).
\tag{F5a}
\]
The exponents are consecutive odd integers. The finite identity
\[
\prod_{j=0}^{h-1}(1+Q^jv)
 =\sum_{k=0}^h
   Q^{k(k-1)/2}\frac{(Q;Q)_h v^k}{(Q;Q)_k(Q;Q)_{h-k}}
\]
follows by multiplying by its last factor; its coefficients obey the two-term recurrence \(A_{h+1,k}=A_{h,k}+Q^hA_{h,k-1}\), and the displayed factorial expression satisfies that recurrence and the endpoints. Here \((Q;Q)_h=\prod_{r=1}^h(1-Q^r)\). Applying this formula to (F5a) cancels all phases and gives (F5). No factorial has index \(N\), since \(2n<N\).

The coefficients are symmetric. For the increasing half their consecutive ratio is \(\sin((2n-k+1)\pi/N)/\sin(k\pi/N)\ge1\), since \(2n+1\le N\). Thus they are unimodal. A symmetric unimodal sequence is a nonnegative sum of centered interval indicators; convolution of two such indicators is symmetric unimodal. Products consequently preserve the property, so all \(d_l^{(N)}\ge0\). The bound
\[
|U_{l-1}(\cos2\pi s)|\le l e^{2\pi(l-1)R}
\tag{F6}
\]
proves (F3) immediately at odd levels. At even levels it only gives an absolute sum; the following two comparisons recover the original complete trace.

If \(D<N-1\), both sides of (F3) are zero by degree, regardless of the quotient. Hence assume \(N\) is even and \(D\ge N-1\). The case \(N=2\) cannot satisfy this assumption because every low index is zero. We may take \(N\ge4\), set \(L=N-1\), and use the same indices at the odd level \(L\). Their common low bound is
\[
m=m_N=m_L=(N-2)/2.
\tag{F7}
\]

### 2.2. Adjacent sine factorials have polynomial ratios

For \(1\le a\le N-2\), concavity of sine and the monotonicity of \(\sin t/t\) on \((0,\pi)\) give
\[
\frac{N(N-1-a)}{(N-1)(N-a)}
\le\frac{\sin(\pi a/(N-1))}{\sin(\pi a/N)}
\le\frac N{N-1}.
\tag{F8}
\]
For the lower bound reflect both sine arguments about \(\pi/2\), and apply \(\sin(\lambda t)\ge\lambda\sin t\) with
\(\lambda=N(N-1-a)/((N-1)(N-a))\le1\). Multiplication telescopes:
\[
\left(\frac N{N-1}\right)^r\frac{N-1-r}{N-1}
\le\frac{S_r^{(L)}}{S_r^{(N)}}
\le\left(\frac N{N-1}\right)^r,
\qquad0\le r\le N-2.
\tag{F9}
\]
There is a sharper exact bound in the even-level case used here:
\[
\frac1L\le\frac{S_r^{(L)}}{S_r^{(N)}}\le\sqrt2,
\qquad0\le r\le N-2.
\tag{F9a}
\]
To see it, write \(N=2h\), so \(L=2h-1\). The individual sine ratio in (F8) is at least one exactly when \(r\le NL/(N+L)\), whose floor is \(h-1\). The partial product ratio therefore increases to \(r=h-1\) and decreases afterward. Its maximum is
\(S_{h-1}^{(L)}/S_{h-1}^{(N)}=\sqrt{2L/N}<\sqrt2\), by reflection of the full sine products. Its endpoint value is \(2L\sin(\pi/N)/N\ge4L/N^2\ge1/L\); the other endpoint is one. This proves (F9a).

In particular these ratios and their reciprocals are polynomial in \(N\), uniformly in \(r\). Replacing an index by one more or one less still costs only a polynomial whenever both indices are allowed: every added factor lies between \(4/N\) and \(2\).

Apply (F9) to (F5). Every individual Laurent coefficient at level \(N\) is bounded by a fixed power of \(N\) times the corresponding coefficient at level \(L\). Convolution of the \(B\) positive factors preserves this comparison term by term. Thus there is a constant exponent \(A'_B\) such that
\[
a_k^{(N)}\le C_B N^{A'_B}a_k^{(L)}
\quad\text{for every integer }k.
\tag{F10}
\]
This comparison preserves the support exactly. It is not an asymptotic approximation of the two trigonometric products.

### 2.3. A discrete tail difference controls the tail coefficient

**Lemma.** Let \(f_1,\ldots,f_B\) be nonnegative symmetric unimodal sequences, each supported on the integers \([-m,m]\). Let \(a=f_1*\cdots*f_B\). Then, for every integer \(k\ge m\),
\[
a_k\le(2m+1)^B(a_k-a_{k+2}).
\tag{F11}
\]

Write each sequence as a nonnegative linear combination of interval indicators:
\(f_i=\sum_{r=0}^{m}(f_i(r)-f_i(r+1))\mathbf1_{[-r,r]}\).
It suffices to prove (F11) for convolutions of these indicators. Let the radii be \(r_1,\ldots,r_B\), with largest radius \(r\). Such a convolution \(C\) is symmetric unimodal, positive at every integer of its support, and satisfies
\[
C(k)>C(k+1)\quad\text{whenever }k\ge r\text{ and }C(k)>0.
\tag{F12}
\]
For completeness, prove (F12) by induction on \(B\), choosing a factor with largest radius \(r\). If \(H\) is the convolution of the other factors, then
\(C(k)-C(k+1)=H(k-r)-H(k+r+1)\).
For \(k\ge r\), both arguments are nonnegative. If \(C(k)>0\), the first lies in the support of \(H\). If the second is outside that support the difference is positive. Otherwise the induction hypothesis gives a strict decrease at its last step, since \(k+r\) is at least the largest radius of \(H\); monotonicity handles the intervening steps. The one-factor case is immediate. This also covers zero radii.

The quantities in (F12) are integers. Thus \(C(k)-C(k+2)\ge1\) whenever \(C(k)>0\) and \(k\ge r\), while \(C(k)\le\prod_i(2r_i+1)\le(2m+1)^B\). The same inequality is trivial if \(C(k)=0\). Sum the interval decompositions to obtain (F11).

For each even-level alias \(1\le l\le L_N\), put \(k_l=lL-1\). Then \(k_l\ge L-1=2m\). Unimodality, (F10), and (F11) give
\[
\begin{aligned}
d_l^{(N)}
&\le a_{lN-1}^{(N)}
 \le C_BN^{A'_B}a_{lN-1}^{(L)}
 \le C_BN^{A'_B}a_{lL-1}^{(L)}\\
&\le C_BN^{A'_B+B}
 \bigl(a_{lL-1}^{(L)}-a_{lL+1}^{(L)}\bigr).
\end{aligned}
\tag{F13}
\]
The odd-level alias range contains this range because \(L<N\). Its complete trace has only positive terms. Equations (F4), (F6), and (F13) therefore prove
\[
|\phi_{N,s}(F_N)|\le C_{B,R}N^{A''_B}\phi_{L,0}(F_L).
\tag{F14}
\]
No cancellation of the even alternating terms has been assumed. They were bounded by the actual positive odd trace.

### 2.4. Returning to the original even-level positive trace

The complete Newton law is
\[
e_i^{(K)}e_j^{(K)}=
\sum_{r=\max(i,j)}^{i+j}\mu_K(i,j;r)e_r^{(K)},
\qquad
\mu_K(i,j;r)=
\frac{S_{i+j}^{(K)}S_r^{(K)}}
 {S_i^{(K)}S_j^{(K)}S_{r-i}^{(K)}S_{r-j}^{(K)}S_{i+j-r}^{(K)}}>0,
\tag{F15}
\]
when \(i+j<K\); the product is zero when \(i+j\ge K\). The trace extracts the last basis coefficient. Expand \(F_L\) by successive multiplication in the original fixed order. An admissible path starts with \(r_1=n_1\), ends with \(r_B=L-1=N-2\), and at every gate has
\[
r_{j-1}+n_j\le N-2,\qquad
\max(r_{j-1},n_j)\le r_j\le r_{j-1}+n_j.
\tag{F16}
\]
Define its slack at gate \(j\) to be \(r_{j-1}+n_j-r_j\). The sum of its slacks is \(D-(N-2)\ge1\). Choose the first gate \(j_0\) with positive slack, and construct an even-level path by
\[
r'_j=r_j\quad(j<j_0),\qquad
r'_j=r_j+1\quad(j\ge j_0).
\tag{F17}
\]
At the first changed gate the positive slack makes its new output admissible. At subsequent gates both the incoming running index and output increase by one, so the upper and lower gate inequalities persist; their input sum increases from at most \(N-2\) to at most \(N-1\), still strictly below the even level \(N\). The path now closes at \(r'_B=N-1\). All leaf indices stay unchanged.

For a given image path and \(j_0\), its preimage is unique, so the map has multiplicity at most \(B-1\). Each factorial argument in an image gate differs from its old argument by at most one. The only decrease, at the first changed slack, is legitimate because that slack was positive. Equations (F9) and (F15) thus bound each old gate coefficient by a fixed polynomial in \(N\) times its image coefficient. There are \(B-1\) gates. Summing these positive path weights yields
\[
\phi_{L,0}(F_L)\le C_BN^{A'''_B}\phi_{N,0}(F_N).
\tag{F18}
\]
If there are no old paths, the left side is zero and the inequality remains valid. The construction itself is exact and includes all support-boundary cases; no interior saddle or lower asymptotic coefficient estimate is used.

Combining (F14) and (F18) proves (F3) at even levels. Together with the odd proof and the trivial degree cases, it proves the all-level theorem.

### 2.5. Actual low arrays, low outputs, and the remaining scope

Let \(F_i=\sum_{n\le m_N}f_{i,n}e_n^{(N)}\), and \(F_i^{\mathrm{abs}}=\sum|f_{i,n}|e_n^{(N)}\). Multilinear expansion of the inputs and (F3), followed by the triangle inequality, give
\[
\left|\phi_{N,s}\left(\prod_{i=1}^B F_i\right)\right|
 \le C_{B,R}N^{A_B}
 \phi_{N,0}\left(\prod_{i=1}^B F_i^{\mathrm{abs}}\right).
\tag{F19}
\]
This is a finite whole-hub comparison for arbitrary complex low-coordinate arrays. The factor count is fixed before taking \(N\to\infty\). It is not an assertion that an absolute value can be passed through a Laurent-coefficient difference.

For a physical turned output \(k\le m_N\), insert the additional low probe \(e_k\) before the trace and retain the exact paired prefactor
\[
[e_k]\mathscr T_s^{\mathrm{fix}}\left(\prod_iF_i\right)
 =\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}
   \phi_{N,s}\left(e_k\prod_iF_i\right).
\tag{F20}
\]
On \(|s|\le R<1\), that prefactor is uniformly bounded. Thus (F19) gives the original positive low-probe comparison, at both parities, with only polynomial cost. It can be combined with any established complete positive-probe estimate at its actual geometric pressure.

This theorem does not yet control a high input or high output/probe. Those basis polynomials lack the positive unimodal Laurent coefficients used here. An intermediate physical turn may produce high coordinates, so arbitrary trees do not follow by iterating (F19) alone. The adjacent-level comparison is only an algebraic estimate inside this proof: it does not identify invariants, colors, framings, or knot volumes at different levels.

## 3. A full hub at its original intrinsic action

The low-coordinate comparison alone does not cover high inputs or high output coordinates. For one unturned hub with effective-leaf inputs, the strict geometric pressure comparison controls those remaining sectors. This section keeps the input constants and the original output pressure explicit, so it does not assign the same cost to an arbitrary bare turn.

### 3.1. Inputs, output, and the two intrinsic pressures

Let \(N\) tend to infinity through either parity, \(d=N-1\), \(m=\lfloor d/2\rfloor\), and fix \(R<1\). The fixed complete Newton polynomials are \(e_0,\ldots,e_d\), and the multiplication relation is
\[
P_s=P_0+\Delta_s,\qquad \Delta_s=2\cos(2\pi s)-2,
\qquad |s|\le R.
\]
Use the full complete spectral-jet norm \(\|\cdot\|_{\mathrm J}\). Define
\[
J(u)=\int_0^u\log(2\sin\pi v)\,dv,
\qquad g(u)=J(2u)-4J(u),\qquad G_0=g(1/4)>0.
\tag{H1}
\]
Here \(g\) is used on \([0,1/2]\), where its maximum is \(G_0\).

Fix an integer \(B\ge2\). Suppose
\[
F_{b,N}(s)=\sum_{r=0}^d f_{b,N,r}(s)e_r,
\qquad 1\le b\le B,
\]
are arbitrary complex arrays satisfying, uniformly in the specified parameters,
\[
|f_{b,N,r}(s)|\le
\begin{cases}
\exp\{N(c_b+g(r/N)+\epsilon_N)\},&r\le m,\\
\exp\{N(c_b+\epsilon_N)\},&r>m,
\end{cases}
\qquad \epsilon_N\longrightarrow0.
\tag{H2}
\]
The constants \(c_b\) are fixed. No sign, root location, or physical alias identity is assumed for these arrays. Their product and its actual fixed-frame turn are
\[
A_N(s)=F_{1,N}*_s\cdots *_sF_{B,N},\qquad
Q_N(s)=\mathscr T_s^{\mathrm{fix}}A_N(s).
\tag{H3}
\]
The typed turn is the proved weighted reversal, with its scalar retained.

The positive complete reference uses
\[
h_N=\sum_{r=0}^{m}\frac{N^2S_{2r}}{S_r^4}e_r,
\qquad A^0_{B,N}=h_N^B,
\qquad Q^0_{B,N}=T_0(h_N^B)=\sum_{r=0}^d q^0_{B,N,r}e_r.
\tag{H4}
\]
The product in (H4) is in the complete quotient. Every coefficient \(q^0_{B,N,r}\) is nonnegative. Let \(f_B(x)\) be the original positive coefficient action of the unturned product \(h^B\), including the exact old support. Define
\[
\begin{aligned}
\omega_B&=\max_{0\le x\le1/2}\{f_B(x)+g(x)\},\\
\widehat\omega_B&=\max_{0\le x\le1/2}\{f_B(1-x)+g(x)\},\\
\Omega_A&=\sum_bc_b+\omega_B,\qquad
\Omega_Q=\sum_bc_b+\widehat\omega_B.
\end{aligned}
\tag{H5}
\]
Thus \(\Omega_Q\) is the original intrinsic low-probe action of the turned hub, equivalently the complete closing action of \(C(hh^B)\), with all effective-leaf constants added. It is not a newly chosen norm budget.

These actions can also be defined directly from the positive multiplication formula (F15). Put \(f_1(y)=g(y)\) for \(0\le y\le1/2\), and exclude other values. For \(B\ge2\),
\[
\begin{aligned}
f_B(b)&=\max_{\substack{0\le x\le1,\ 0\le y\le1/2\\
\max(x,y)\le b\le x+y\le1}}
 \{f_{B-1}(x)+g(y)+m(x,y,b)\},\\
m(x,y,b)&=J(x+y)+J(b)-J(x)-J(y)\\
&\quad-J(b-x)-J(b-y)-J(x+y-b).
\end{aligned}
\tag{H5a}
\]
The maximum retains the original gate support. Uniform sine-factorial estimates give its closed upper action, and positive integer approximation at a strict maximizing state gives the matching rate used in the original [complete source analysis](actual_positive_conway_variational_limit.md). The additive constants \(c_b\) do not enter this reference recursion; they are restored explicitly in (H5).


The exact classical comparison needed below is
\[
\omega_B=2BG_0,\qquad
\widehat\omega_2=4G_0,\qquad
\delta_B:=\widehat\omega_B-2BG_0>0\quad(B\ge3).
\tag{H6}
\]
A proof is given in Section 3.2.

**Theorem.** There is \(\gamma_{B,R}>0\) and a uniform error \(o(1)\) such that
\[
\|Q_N(s)\|_{\mathrm J}\le\exp\{N(\Omega_Q+o(1))\}.
\tag{H7}
\]
More precisely, let \(Q_N^{\mathrm{clean,lo}}\) be the low-coordinate part of the output when every input in (H3) is restricted to its low coordinates. Then
\[
\left|[e_r]Q_N^{\mathrm{clean,lo}}\right|
\le \exp\{N(\sum_bc_b+o(1))\}\,q^0_{B,N,r}
\quad(0\le r\le m),
\tag{H8}
\]
and
\[
\|Q_N-Q_N^{\mathrm{clean,lo}}\|_{\mathrm J}
\le\exp\{N(\Omega_Q-\gamma_{B,R})\}.
\tag{H9}
\]
Thus all high outputs and every contribution with a high input have a strict deficit. The clean term has an actual old positive coordinate majorant, not merely a spectral norm bound.

### 3.2. Why these are the original pressures

At odd levels, \(-2\) is the simple complete Casimir node. All high Newton polynomials vanish there, and all low ones are positive. Consequently the exact equality
\[
\sum_{r=0}^{m}[e_r]A^0_{B,N}\,e_r(-2)
=A^0_{B,N}(-2)=h_N(-2)^B.
\tag{H10}
\]
retains only the original low coefficient sum. The uniform low coefficient and basis rates are both \(g\). The positive sum for \(h_N(-2)\) therefore has rate \(2G_0\). Applying the established positive coefficient Laplace principle to the left side of (H10) gives \(\omega_B=2BG_0\). The coefficient profile \(f_B\) and the basis profile \(g\) are the same uniform closed sine-factorial actions at both parities, so this resulting variational identity is parity-independent. Equivalently, at even levels use the closest complete node to \(-2\), where all high Newton values vanish and \(h_N\) has the same rate \(2G_0\). The exact product evaluation gives the lower rate. Positivity bounds the low endpoint sum by the canonical polynomial value at \(-2\), whose size is bounded by the polynomial equivalence of the canonical sup and full spectral norms and the product of the complete input norms. No deformed norm is used to calibrate the original action.

For the pressure comparison, associate the last binary gate of the unturned product as \(h^{B-1}\cdot h\). For \(B=2\), its two inputs have rigid type L. For \(B\ge3\), the first is a completed type-A product and the second is type L. The [original product equations](actual_conway_unflagged_probe_geometry.md) give
\[
f_B'(x)\ge f_2'(x)\quad(0<x<1),
\tag{H11}
\]
strictly when \(B\ge3\). To recall the actual geometric inequality, write \(B_x=\cot\pi x\) for the output cotangent and \(X,Y\) for the positive boundary parameters. The unsquared product relation is
\[
Y^2=(B_1-B_x)(B_2-B_x)\le(X-B_x)^2,
\qquad B_x<B_i\le X.
\]
Together with \(Y^2=1+B_x^2-X^2\), it gives
\[
X\ge X_2(B_x)=\frac{B_x+\sqrt{B_x^2+2}}2,
\qquad f_B'(x)\ge2\log(2X_2(B_x)^2)=f_2'(x).
\tag{H12}
\]
One inequality is strict if an input is type A. All additive constants differentiate to zero and have already been retained in (H5).

Since \(X_2(B)X_2(-B)=1/2\), the two-leaf profile is symmetric:
\(f_2(x)=f_2(1-x)\). Integrating (H11) between \(x\) and \(1-x\) therefore proves
\[
f_B(1-x)\ge f_B(x)\quad(0<x<1/2),
\tag{H13}
\]
strictly for \(B\ge3\). The intrinsic positive probe has a maximizer in \((0,1/2)\): its value at zero is zero and it has positive interior values, while the logarithmically negative derivative of \(g\) excludes the upper endpoint (the profile \(f_B\) is regular there). Evaluating the left-hand pressure at this maximizer proves strict \(\widehat\omega_B>\omega_B\) for \(B\ge3\). For \(B=2\), symmetry gives equality. This proves (H6).

### 3.3. Low outputs with all inputs low: preserve the signed hub

Section 2 gives the exact all-parity whole-hub trace comparison, for any fixed number of low-coordinate arrays,
\[
\left|\phi_s\left(e_r\prod_bF_{b,N}^{\mathrm{lo}}\right)\right|
\le C_{B,R}N^{A_B}\phi_0\left(e_r\prod_b(F_{b,N}^{\mathrm{lo}})^{\mathrm{abs}}\right),
\qquad r\le m.
\tag{H14}
\]
The left product is reduced in the moving quotient only for taking the trace. This estimate sums all return contributions before the absolute value. At odd levels its proof uses the nonnegative symmetric unimodal Laurent coefficients of each low Newton basis factor and the exact finite Fourier formula. At even levels a finite adjacent-odd comparison, the discrete unimodal tail-difference lemma, and the first-slack positive-path map return the bound to the original even-level positive trace, at polynomial cost. Neither argument compares individual return terms or changes the physical level of the source.

The positive reference coefficients in (H4) have the uniform closed rate \(g(r/N)+O(\log N/N)\). Equation (H2) therefore gives
\[
(F_{b,N}^{\mathrm{lo}})^{\mathrm{abs}}
\le N^{C}\exp\{N(c_b+\epsilon_N)\}\,h_N.
\tag{H15}
\]
coefficientwise. The old multiplication and trace are positive. Apply (H15) to the right side of (H14), and use the exact coefficient extractor for the fixed-frame turn:
\[
[e_r]Q_N^{\mathrm{clean,lo}}
=\frac{\gamma_N(s)W_{d-r}(s)}{H_N(s)}
 \phi_s\left(e_r\prod_bF_{b,N}^{\mathrm{lo}}\right).
\tag{H16}
\]
The paired scalar in (H16) is uniformly bounded on \(|s|\le R<1\). Since \(B\) is fixed, all polynomial factors and \(B\epsilon_N\) can be absorbed in one uniform \(o(1)\). This proves (H8).

The low-coordinate norm satisfies the original positive-probe bound
\[
\|Q_N^{\mathrm{clean,lo}}\|_{\mathrm J}
\le\operatorname{poly}(N)\sum_{r\le m}e_r(-2)
             |[e_r]Q_N^{\mathrm{clean,lo}}|
\le\exp\{N(\Omega_Q+o(1))\}.
\tag{H17}
\]
The reference weighted sum has precisely the second action in (H5).

### 3.4. The other sectors and the exceptional two-input cases

The canonical sup norm, complete spectral-jet norm, and Chebyshev coefficient norm are polynomially equivalent at degree less than \(N\). Fixed-valence quotient multiplication modulo \(P_s\) has polynomial norm cost on every bounded parameter disk, by exact Chebyshev folding. The top-coefficient functional also has polynomial cost. These facts give, for any specified input-band assignment with \(h\) high inputs,
\[
\|A_{N,\mathrm{band}}(s)\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h)G_0+o(1)\right]\right\}.
\tag{H18}
\]
Indeed a low input has norm at most \(\exp\{N(c_b+2G_0+o(1))\}\), while a high input has norm at most \(\exp\{N(c_b+o(1))\}\). The latter uses the polynomial full-normal norm of every high complete Newton basis element, not its zero node values alone.

For a high output \(r>m\), insert the polynomially bounded \(e_r\) in the exact trace extractor. The basis element at that output also has polynomial norm. Summing the finitely many coordinates gives
\[
\|Q_{N,\mathrm{band}}^{\mathrm{hi}}\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h)G_0+o(1)\right]\right\}.
\tag{H19}
\]
For a low output, the trace insertion and the subsequent reconstruction each cost at most \(\exp(NG_0)\). Hence
\[
\|Q_{N,\mathrm{band}}^{\mathrm{lo}}\|_{\mathrm J}
\le\exp\left\{N\left[\sum_bc_b+2(B-h+1)G_0+o(1)\right]\right\}.
\tag{H20}
\]
These estimates retain signs within the polynomial products; no positive moving-Newton multiplication majorant is used.

If \(B\ge3\), (H19) with \(h=0\) has rate \(\Omega_A<\Omega_Q\). If \(h\ge1\), (H20) has rate at most \(\Omega_A\), and (H19) is even smaller. Thus every sector covered by (H9) has a fixed loss at least \(\delta_B\) before absorbing its uniform errors. The finitely many band choices cost no exponential factor.

When \(B=2\), \(\Omega_A=\Omega_Q\), so two cases require their actual source support rather than this strict pressure comparison.

1. If both inputs are low, their ordinary polynomial product has degree at most \(2m\le d<N\). There is no return correction. The high-output positive majorant is exactly the old high-probe sector, with the outgoing paired factors bounded coefficientwise. The [isolated three-leaf high-probe estimate](actual_conway_unflagged_core_probe_bound.md) has a fixed strict gap below \(4G_0+\sum c_b\).

2. If exactly one input is high and the output is low, the cubic trace has two low incident indices. A return vertex requires all pair sums at least \(N\), whereas those two low indices have sum at most \(2m\le d\). Thus this particular scalar has no return term. Its remaining complete positive majorant is an old sector with one high effective input, which has the established strict high-sector gap. This statement concerns low output only.

3. If exactly one input is high and the output is high, returns are allowed. They are controlled by (H19), which saves \(2G_0\) relative to \(\Omega_Q\). They are not excluded by the preceding two-low support observation.

4. If both inputs are high, (H20) is at most \(\sum c_b+2G_0\), again strictly below \(\Omega_Q=\sum c_b+4G_0\); (H19) is smaller still.

The [complete two-input gaps](actual_conway_unflagged_core_probe_bound.md) invoked in cases 1–2 are upper statements for arbitrary coefficient-cone arrays. They use the exact complete positive kernel and the isolated three-leaf comparison, including its true target and both finite support endpoints. No physical alias relation is assumed for the present arrays.

Choose a smaller fixed gap than the positive minima just obtained, and absorb the uniform errors and fixed number of sectors. This proves (H9), and then (H7).

### 3.5. The usable invariant and its limit

The conclusion has two separate parts: an old positive low-coordinate majorant (H8), and a spectrally small remainder (H9). The usual original low-output localization of the reference probe therefore passes to the clean majorant without changing its maximizing interval. This is stronger than the whole output norm alone.

It also gives a fresh canonical angular Gaussian. The original probe action
\(u\mapsto f_B(1-u)+g(u)\) has a unique strict maximizer \(u_*\in(0,1/2)\). The clean low reconstruction uses the strip rate (D29), so its real angular action is
\[
\sum_b c_b+f_B(1-u)+b(u,\vartheta,0)
 \le\sum_b c_b+f_B(1-u)+g(u)\le\Omega_Q.
\tag{H21}
\]
The first inequality is strict away from \(\vartheta=\pi\) at every interior \(u\), and the second is strict away from \(u_*\). Near \((u_*,\pi)\), strict concavity of the old profile and the Newton angular second derivative used in Section 1.5 give a quadratic loss in the real angle and a quadratic cost in its imaginary part. On the complementary compact set there is a fixed gap. The remainder in (H9) has canonical strip size at most its J norm times \(\operatorname{poly}(N)e^{N|y|}\), so its strict deficit absorbs that linear height cost on a sufficiently small fixed strip. Consequently there are \(c_B,C_B,y_B>0\) with
\[
|Q_N(s)(2\cos(\vartheta+iy))|
 \le\exp N\{\Omega_Q-c_B(\vartheta-\pi)^2+C_By^2+o(1)\},
\quad |y|\le y_B,\quad |s|\le R.
\tag{H22}
\]
This conclusion uses the original low-coordinate majorant, not just the total J norm. It does not assert that arbitrary quotient products preserve an angular Gaussian.


It is not a free replacement of an arbitrary completed child by an effective leaf with profile \(g+c\). A general type-A output has its own old boundary coefficient profile, and a \(\mathrm J\)-small remainder need not save a full \(2G_0\) when inserted at a later hub. Iteration through an arbitrary connected unflagged component needs an invariant that tracks that old low-coordinate profile and the remaining error budget across the next product and turn. No such iteration is asserted here. The even-level Fourier signs have been handled by the exact all-parity comparison in Section 2. The remaining limitation here is iteration with general intermediate type-A boundary profiles and their error budgets, not parity.

## 4. A geometric upper bound when bare hubs are separated

### 4.1. The fixed construction and the statement

Fix a literal strict Conway construction with separately labeled physical leaves, prescribed half-twists, ordered tangle endpoints, and its original reduced cut. A physical leaf is
\[
 p_i(s)=R_s^{\epsilon_i}L_{j_i},\qquad h_i(s)=\mathscr T_s(p_i(s)),\qquad
 1\le j_i\le N,\qquad \epsilon_i\in\{0,\pm1\}.
 \tag{T1}
\]
The type of \(R_s\) and \(\mathscr T_s\) is the one dictated by the ordered strands, as in Section 1. Arguments \(s\) are omitted below when unambiguous. The color tuple is allowed to vary over its entire finite cube. The construction and the half-twist choices are fixed before the level tends to infinity.

Use the [reduced product-hub tree](actual_conway_reduced_hub_source_normal_form.md) of the original construction. A hub is a maximal product junction after internal edges without a turn have been contracted. Every remaining hub-to-hub edge carries a physical quarter-turn. An unflagged external leaf is \(h_i\); a flagged external leaf is its turn, namely the original unturned coupon \(p_i\), with the typed dual identification retained. Strictness gives at most one flagged leaf at each hub. The hubs have degree at least three; the two-leaf case is treated separately below.

Assume the following additional combinatorial condition:

> No edge joins two unflagged hubs.

Equivalently, every maximal connected component of hubs without a flagged leaf consists of a single hub. A hub without a flag is called bare below. Its degree is arbitrary but fixed. A tree may have arbitrarily many bare hubs, and a flagged hub may have arbitrarily many bare-hub descendants. The restriction concerns adjacent bare hubs, not the size or branching of the construction.

Let \(F_0\) be the original complete positive action of the construction, with all original shared-wire constraints and additive constants. In the geometric hypotheses of the strict Conway theorem, the complete augmented exterior satisfies
\[
                    2\pi F_0=\operatorname{Vol}(Y^\epsilon).
 \tag{T2}
\]
No geometric interpretation is needed for the algebraic bound if only the action is being considered.

Write \(q=e^{\pi i/N}\), \(d=N-1\), and deform the main meridian by \(M=q^s\). Let \(\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\) denote the actual reduced cut scalar of this auxiliary-colored source, with the prescribed framing and all repeated-root normal data. For every fixed \(0\le R<1\),
\[
 \sup_{|s|\le R}\ \sup_{\mathbf j\in\{1,\ldots,N\}^{H}}
 \left|\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)\right|
 \le \exp\{N(F_0+o(1))\}.
 \tag{T3}
\]
The error is uniform over the displayed disk and color cube and over any fixed finite set of half-twist choices. The limit runs through both parities, without a primality restriction. The full modified dimension is not included in this reduced scalar. In the retained normalization it has removable value \(\eta_N/N\) at completeness, with \(\eta_N=i^{N+3}\) in the [fixed normalization](actual_conway_pointed_quantum_a_volume.md); its ordinary-color poles occur outside the pre-resonance disk considered here.

### 4.2. The exact pairing transfer and the two induction bounds

Use the fixed basis, relations and physical carrier conventions of Section 1. The unchanged pairing (D6) is
\[
\langle f,g\rangle=\sum_{n=0}^d f_n g_{d-n}.
\tag{T7}
\]
The exact turn is \(\mathscr T_\gamma=\gamma_NH_N^{-1}\mathcal R\operatorname{diag}(W_n)\), with the six specified scalars in Section 1.4. Because \(W_nW_{d-n}=H_N^2\), successive turns cancel their paired factors and their successive \(\gamma\)'s. The result is the same polynomial on the dual endomorphism space. This is the typed meaning of removing a double turn in the source; it is not a tangle isotopy.

The turn is self-adjoint for (T7), up to the scalar when the applicable type changes:
\[
\langle\mathscr T_{\gamma_1}f,g\rangle
 =\frac{\gamma_1(s)}{\gamma_2(s)}
     \langle f,\mathscr T_{\gamma_2}g\rangle.
\tag{T10}
\]
After their displayed scalars, both sides equal \(H_N^{-1}\sum_nW_nf_ng_n\). Thus a closing turn can be transferred without dropping its carrier phase. Associativity in compatible carrier coordinates, typed double-turn removal, and (T10) perform the source regrouping. Any root scalar \(\chi_N(s)\) is the product of the specified turn ratios; it and its inverse are bounded on \(|s|\le R<1\) because the tree is fixed. The original coupons retain their crossing scalars, auxiliary pivots and framing throughout. No noncentral carrier is inserted by this pairing adjunction.

There are two different induction bounds. A rigid, leaf-like branch, called type L in the complete geometry, is assigned a constant \(c\) when
\[
|[e_r]L_N(s)|\le
\begin{cases}
\exp\{N(c+g(r/N)+o(1))\},&r\le\lfloor d/2\rfloor,\\
\exp\{N(c+o(1))\},&r>\lfloor d/2\rfloor.
\end{cases}
\quad
\|L_N(s)\|_{\mathrm J}\le\exp\{N(c+2G_0+o(1))\}.
\tag{T13}
\]
A completed product branch, called type A, instead carries its own intrinsic spectral budget
\[
\|Q_N(s)\|_{\mathrm J}\le\exp\{N(\Omega_Q+o(1))\}.
\tag{T15}
\]
No assertion of (T13) is made for a general A branch. The decorated operation in Section 1 accepts (T15), or a product of such spectral bounds, and creates (T13) with the sum of those input budgets as \(c\). An ordinary physical leaf has \(c=0\). The bare-hub theorem of Section 3 accepts L cones with constants \(c_1,\ldots,c_B\), and creates an A spectral budget
\[
\Omega_Q=\sum_{b=1}^B c_b+\widehat\omega_B.
\tag{T18}
\]
Both statements are uniform over the actual independent auxiliary colors. They also give fresh canonical angular Gaussians at their outgoing modules, by (D28) and (H22), but the recursion below needs only the displayed coefficient and spectral bounds.

### 4.3. Finite recursion and exact action accounting

First assume that there is a flagged hub, and choose its flagged physical leaf as the root. Direct every other hub edge toward that root, and let \(\mathcal C(v)\) denote the child branches of a hub \(v\), apart from its distinguished coupon when it is flagged. Ordinary leaves send their coupons \(h_i\) to their incident hub. Every nonroot flagged hub sends
\[
                  L_v=D_{i(v)}\left[\prod_{w\in\mathcal C(v)}Q_w\right].
 \tag{T19}
\]
The children \(Q_w\) can be ordinary L leaves, other flagged L modules, or bare-hub A modules. Assign
\[
             c_v=\sum_{w\in\mathcal C(v)}\Omega_w,
             \qquad \Omega_v=c_v+2G_0.
 \tag{T20}
\]
Equations (D10), (D24)--(D27) prove (T13) for this outgoing module whenever the children satisfy their spectral budgets. This step requires no coefficient-profile hypothesis on an A child.

A nonroot bare hub of degree \(d_v\) has \(B=d_v-1\ge2\) children. The separation hypothesis ensures that all these children are ordinary L leaves or flagged L modules. In particular every child has the coefficient cone (T13), with a specified constant \(c_w\). Its outgoing module is
\[
 Q_v=\mathscr T\left(\prod_{w\in\mathcal C(v)}L_w\right),\qquad
 \Omega_v=\sum_{w\in\mathcal C(v)}c_w+\widehat\omega_{d_v-1}.
 \tag{T21}
\]
Section 3 and (T18) prove its spectral budget (T15). We do not apply (T13) to this A output; when it reaches its flagged parent, (T19) creates a new L cone from the spectral budget.

This is a terminating induction: every input in (T19) or (T21) belongs to a strictly smaller rooted subtree, and the finite tree ends at ordinary leaves. The errors and polynomial losses remain uniform because the number of hubs, their valences, and all fixed twist powers are independent of \(N\). Thus (T13) and (T15) hold for all modules in the tree, uniformly over all physical color tuples.

These same constants have their original geometric meaning. The [rigid-profile theorem](actual_conway_rigid_spine_and_flagged_tree_geometry.md) gives
\[
 f_{L_v}(b)=g(b)+c_v,\qquad
 \Omega_{L_v}=\max_{0\le b\le1/2}\{g(b)+f_{L_v}(b)\}=c_v+2G_0.
 \tag{T22}
\]
Its absolute constant is precisely the sum (T20), not a free normalization. At a bare hub the children have the original profiles \(g+c_w\). Optimizing their internal states therefore gives
\[
 f_{A_v}(z)=f_{d_v-1}(z)+\sum_wc_w,
 \quad f_{Q_v}(u)=f_{A_v}(1-u),
 \quad \Omega_{Q_v}=\sum_wc_w+\widehat\omega_{d_v-1}.
 \tag{T23}
\]
These are identities of the original positive action with its fixed output. They do not replace the signed child coupons by physical bare leaves. The intrinsic probe in (H5) computes an action constant; no new crossing circle or auxiliary color has been inserted.

At the selected flagged root, the exact typed scalar has the form
\[
 Z_{N,\mathbf j}^{\epsilon}(s)
   =\chi_N(s)\,\phi_\sigma\left(
               p_0\prod_{w\in\mathcal C(0)}Q_w\right).
 \tag{T24}
\]
The products and the root type are those determined by the compiler; \(\chi_N\) records (T10) if root transfers were needed. The root coupon has polynomial norm. The polynomial product and trace bounds (D10)--(D11), together with (T13) and (T15), give
\[
 |Z_{N,\mathbf j}^{\epsilon}(s)|
      \le\exp\left\{N\left(\sum_{w\in\mathcal C(0)}\Omega_w+o(1)\right)\right\}.
 \tag{T25}
\]
The [original rigid root profile](actual_conway_rigid_spine_and_flagged_tree_geometry.md) is
\(g(1-z)+\sum_w\Omega_w\). Its coefficient-one closing endpoint is \(z=1\), at which \(g(0)=0\). The [intrinsic probe geometry](actual_conway_unflagged_probe_geometry.md) therefore gives exactly
\[
                         F_0=\sum_{w\in\mathcal C(0)}\Omega_w.
 \tag{T26}
\]
There is no additional charge for the distinguished root leaf. Equations (T25)--(T26) are the required upper bound at the original coupled action.

### 4.4. The cases without a flagged root

If the reduced tree has hubs but none is flagged, the separation condition forces it to have one hub only. Let its degree be \(m\ge3\), so its source is the closure of the product of its \(m\) original ordinary leaves. Choose one of those existing leaves, \(h_0=\mathscr T_{\gamma_1}p_0\), as the closing leaf. Write \(A=\prod_{i=1}^{m-1}h_i\). Equation (T10), with the actual compatible turn type on \(A\), gives
\[
 \phi_\sigma(h_0 A)
   =\frac{\gamma_1}{\gamma_2}\,
     \phi_{\sigma'}\left(p_0\,\mathscr T_{\gamma_2}A\right).
 \tag{T27}
\]
The right pairing is taken in the transferred typed frame; its coefficient pairing is still (T7). The scalar ratio is retained. No external leaf is added, and no unproved norm for the general turn is used.

Each input of \(A\) has the cone with \(c_i=0\). The whole-hub theorem with \(B=m-1\), followed by the polynomial root coupon and trace bounds, yields
\[
             |\phi_\sigma(h_0A)|
                   \le\exp\{N(\widehat\omega_{m-1}+o(1))\}.
 \tag{T28}
\]
The original closure is precisely the probe defining this constant, so \(F_0=\widehat\omega_{m-1}\). This handles the isolated three-leaf case \(m=3\) with \(\widehat\omega_2=4G_0\), as well as every fixed larger valence. The comparison has not added a \(2G_0\) norm cost for its closing leaf.

For two physical leaves there is no reduced hub. The strict edge parity is one. The exact Frobenius transfer exposes one unturned physical coupon and one decorated leaf, up to its specified typed scalar. The same estimate gives action \(2G_0\). When a volume interpretation is asserted, retain the separate two-leaf knot and framing hypotheses of the original strict theorem; in particular the source estimate does not turn a multicomponent parity choice into a knot. The main statement may instead be restricted to \(H\ge3\) without using this exceptional case.

As an optional check on constants, expansion of the recursive identities gives the root-independent formula
\[
 F_0=2G_0(H-1)+
   \sum_{v\ \mathrm{bare}}
     \left(\widehat\omega_{d_v-1}-2(d_v-1)G_0\right).
 \tag{T29}
\]
Each nonroot flagged distinguished leaf and each ordinary leaf contributes one \(2G_0\); the chosen root leaf contributes none. A bare hub replaces the sum of its \(d_v-1\) child L budgets by (T21), producing the displayed correction. In the unflagged single-hub case, the same formula reduces to (T28). Equation (T29) is action accounting, not a decomposition of a hyperbolic manifold into pieces with these volumes.

### 4.5. The main cut and the limits of the conclusion

The primitive partial-trace formula for the actual reduced cut gives exactly
\[
 \mathcal F_{N,\mathbf j}^{\epsilon}(q^s)
    =\frac{s_x}{s_0}\,Z_{N,\mathbf j}^{\epsilon}(s),\qquad
                    \frac{s_x}{s_0}=H_N(s).
 \tag{T30}
\]
The common complete normalization \(s_0\), the prescribed pivot and all physical crossing and framing phases are the ones already present in the source compiler. Switching the orientation of the exposed main strand replaces \(s\) by \(-s\), and \(H_N\) is even. This does not introduce an untracked modified dimension. On \(|s|\le R<1\), \(H_N\) is uniformly bounded and nonzero, so (T25) or (T28) proves (T3). The exact root scalar in (T24) and (T27) is bounded as well and has already been retained.

Under the original strict geometric assumptions, substitution of (T2) states the upper bound as
\[
 \limsup_{N\to\infty}\frac{2\pi}{N}
    \log\sup_{|s|\le R,\,\mathbf j}
      |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
       \le\operatorname{Vol}(Y^\epsilon).
 \tag{T31}
\]
If an individual supremum is zero, its logarithm is interpreted as \(-\infty\). Holomorphy and Cauchy's estimate give the same exponential upper rate for every fixed derivative in \(s\) on a smaller disk. They give no asymptotic lower bound away from completeness.

### 4.6. The complete value gives the matching supremum rate

For the original knot-producing strict construction, the existing [complete source asymptotic](actual_conway_all_strict_tree_long_twist_volume.md), Section 6, equations (24)--(25), supplies a nonzero value inside the supremum. At \(s=0\) and \(j_i=N\), the exact complementary-color identity has \(h_0^\epsilon=0\), so its alias term vanishes at every leaf. The whole complete-color source therefore has
\[
\begin{aligned}
Z_N^\epsilon(\mathbf N)
 &=\upsilon_N^\epsilon N^{3/2}a_\epsilon(0)e^{NF_0}
        (1+O(N^{-1}))
   +O\!\left(N^C e^{N(F_0-\gamma)}\right),\\
\upsilon_N^\epsilon
 &=\exp\!\left(\frac{i\pi(N-1)}4\sum_i\epsilon_i\right),
\qquad a_\epsilon(0)\ne0.
\end{aligned}
\tag{T32}
\]
The factor \(\upsilon_N^\epsilon\) is the retained unit source phase. The [actual cut normalization](actual_complete_augmented_source_normalization.md) changes this complete scalar to the reduced zero-framed invariant only by its specified unit framing character; the main-cut factor in (T30) is \(H_N(0)=1\). Thus the same exponential rate holds for \(\mathcal F_{N,\mathbf N}^{\epsilon}(1)\).

This uses the actual nonzero complete asymptotic, not positivity of an absolute majorant. It holds along both parities under the original strict knot and absence-of-internal-component hypotheses. For \(H=2\), the knot patterns have a pure leaf; the both-odd two-component pattern is not included in this lower-bound assertion.

For every \(0\le R<1\), the complete point belongs to the supremum in (T3). Equation (T32) gives its lower logarithmic rate \(F_0\), while (T3) gives its upper rate. Therefore
\[
\lim_{N\to\infty}\frac{2\pi}{N}
 \log\sup_{\substack{|s|\le R\\\mathbf j\in\{1,\ldots,N\}^{H}}}
  |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
   =2\pi F_0=\operatorname{Vol}(Y^\epsilon).
\tag{T33}
\]
No lower bound at fixed \(s\ne0\), no pointwise meridian-profile limit, and no new filling statement follows from taking this supremum.

### 4.7. The remaining scope

The separation condition is essential to this proof's recursive invariant. A general adjacent bare hub receives an A module whose low coefficient profile is not \(g+c\); a small spectral remainder also need not retain the full saving required by the next bare hub. Nothing above resets that module for free. Conversely, every bare hub in the stated class is fed only L modules, so this missing step is never used.

For this same separated-junction class, the [auxiliary-color gap theorem](actual_main_meridian_auxiliary_color_gap.md) additionally proves a strict exponential loss below the rate \(F_0\) whenever at least one original color satisfies \(j_i\le(1-\delta)N\). It retains every other color, both parities, and the actual half-twist and cut factors. Its parameter disks satisfy \(R<1/2\), whereas (T31)'s upper bound holds for \(R<1\).

Both results concern the unsummed auxiliary-colored source at the complete augmented action. They do not supply a cancellation-preserving filling contour, a lower bound for a filled invariant, or a bound at the generally smaller filled-knot volume. They also do not prove convergence of the ordinary-color-subtracted microscopic meridian profile. Those conclusions require additional control of the signed filling transform or normalized profile.

The subsequent [component theorem](actual_main_meridian_component_extension.md) provides the intermediate-profile estimate under an explicit condition on paths through adjacent bare junctions. The [filled-meridian theorem](actual_main_meridian_filled_volume.md) combines that estimate with a joint Fourier calculation and the original marked filling geometry. For the resulting class it proves a pointwise normalized profile and a uniform knot-complement volume limit on every \(|s|\le R<1\). These conclusions use those additional arguments, not just the supremum in (T33).


## 5. Finite reproduction

The portable [reproduction script](../experiments/audit_main_meridian_source_bounds.py) compares the trace formula with direct polynomial division in exact cyclotomic fields. It separately checks the interval-tail inequality by integer convolutions and the first-slack map by enumerating positive paths. The [saved results](../experiments/main_meridian_source_bounds_results.json) record 131 exact trace identities, 911 interval-tail inequalities, 148 mapped positive paths, and 255 adjacent-factorial ratio checks at 80-digit precision. The factorial checks are numerical; the trace and combinatorial checks are exact.

From the repository root, with SymPy and mpmath installed, run

```sh
python3 experiments/audit_main_meridian_source_bounds.py --output /tmp/main_meridian_source_bounds_results.json
```

These finite checks test the identities and boundary conventions used by the proof. The uniform estimates, the terminating source induction, and the geometric identification are proved in the sections above; they are not inferred from the checked levels.
