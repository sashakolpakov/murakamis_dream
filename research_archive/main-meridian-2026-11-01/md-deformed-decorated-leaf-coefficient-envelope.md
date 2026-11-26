# A deformed decorated-character turn retains the complete coefficient cone

Private derivation, 1 November 2026. No repository file is changed.

This report bounds an actual typed operation: multiply by a fixed crossing power and the ordinary auxiliary-circle character, multiply by the specified input tangle polynomial, and apply the physical quarter-turn. The output retains the same low-index exponential coefficient envelope and polynomial high-index envelope as at completeness. Consequently a fully flagged tree has its complete augmented geometric upper budget throughout every fixed microscopic parameter disk before the first ordinary-color resonance. Each decorated turn also produces a fresh canonical angular Gaussian. Neither assertion supplies a far-auxiliary-color gap or the sharper rate of a filled knot.

The physical turn and its six types are proved in `notes/actual_main_meridian_turn_comparison.md`. The actual moving crossing is bounded in `/private/tmp/md-main-meridian-moving-casimir-twist-bound.md`; the exact loop is proved in `/private/tmp/md-ordinary-circle-character-at-moving-main-color.md`. This report includes the needed arguments and retains their normalizations. Exact polynomial folding is in `/private/tmp/md-moving-casimir-rank-one-folding-and-obstruction.md`. The complete Newton estimates are in `notes/actual_conway_root_star_full_jet_localization.md` and `notes/actual_conway_decorated_character_spectral_closure.md`.

## 1. The fixed coordinates and the two actual algebras

Fix
\[
N\ge2,\quad d=N-1,\quad m=\lfloor d/2\rfloor,
\quad \theta=\pi/N,\quad q=e^{i\theta},\quad Q=q^2,
\quad x=-q^{-1}q^s,\quad y=-q^{-1}q^{-s}.
\tag{1}
\]
The microscopic main meridian is \(M=q^s\). The two roots \(x,y\) give the actual dual modules, denoted by signs \(+,-\). Write \(\mathsf T_N(t+t^{-1})=t^N+t^{-N}\). Equal-color ordered pairs have relation
\[
P_s(z)=\mathsf T_N(z)+2\cos(2\pi s),
\tag{2}
\]
whereas opposite-color pairs have the constant relation \(P_0\). The same relation (2) applies to the two equal-color orders, since it is even in \(s\). At every vertex use the relation of its actual ordered object; these two quotient multiplications are not identified.

All polynomial coordinates below are in the fixed complete basis
\[
S_n=\prod_{r=1}^n2\sin(r\theta),\qquad
c_j=2\cos((2j+1)\theta),\qquad
 e_n(z)=S_n^{-2}\prod_{j=0}^{n-1}(c_j-z),\quad0\le n<N.
\tag{3}
\]
Empty products are one. A canonical polynomial always has degree less than \(N\), independently of the relation used to obtain it. Let
\[
\|F\|_{\mathrm J}=\max\bigl\{|F(c_j)|:0\le j\le m;
\ |F'(c_j)|:c_j\text{ is a double root of }P_0\bigr\}.
\tag{4}
\]
At odd levels the last node \(-2\) is simple and has no derivative coordinate. This is a norm on canonical polynomials. It is polynomially equivalent, uniformly in level and parity, to the canonical sup norm on \([-2,2]\) and to the Chebyshev coefficient norm. This comparison uses full Hermite interpolation; it does not discard first normals or evaluate only on the moving simple nodes.

For either relation define
\[
\phi_{\sigma}(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_\sigma}F,
\qquad \sigma=s\text{ or }0.
\tag{5}
\]
Then the exact fixed-basis metric is
\[
\phi_\sigma(e_i e_j)=\mathbf1_{i+j=d}.
\tag{6}
\]
Indeed, at \(\sigma=0\) this is the complete Newton metric. For \(\deg(e_i e_j)\le2N-2\), divide \(e_i e_j=P_0A+B\). The degree of \(A\) is at most \(N-2\), so the moving remainder \(B-\Delta_s A\), \(\Delta_s=2\cos2\pi s-2\), has the same coefficient of \(z^d\). This proves (6), including the return sectors of the multiplication. If \(F=\sum f_n e_n\) is canonical, it follows that
\[
f_{d-k}=\phi_\sigma(e_kF).
\tag{7}
\]
The product in (7) is reduced in the input object's relation.

## 2. Polynomial quotient estimates, with returns retained

Set \(C_n(t+t^{-1})=(t^n+t^{-n})/2\), \(C_0=1\), and use \(\|\sum a_nC_n\|_{\mathrm{Ch}}=\sum|a_n|\). The identity \(2C_iC_j=C_{i+j}+C_{|i-j|}\) makes this norm submultiplicative. In (2), \(C_N=-b\), \(b=\cos2\pi s\), so
\[
\operatorname{rem}C_{N+r}=-2bC_r-C_{N-r}\quad(0<r<N),
\qquad
\operatorname{rem}C_{kN+r}=-2b\operatorname{rem}C_{(k-1)N+r}
 -\operatorname{rem}C_{(k-2)N+r}.
\tag{8}
\]
For \(r=0\), start with \(1,-b\). For \(|s|\le R\), put \(L_R=2\cosh(2\pi R)+1\). Induction gives
\[
\|\operatorname{rem}_{P_s}F\|_{\mathrm{Ch}}\le L_R^h\|F\|_{\mathrm{Ch}}
\quad(\deg F\le hN).
\tag{9}
\]
The same estimate includes the opposite-color relation by setting \(s=0\). It is a polynomial identity argument, valid even at repeated roots. In particular, a fixed number of canonical factors obeys
\[
\left\|\operatorname{rem}_{P_\sigma}\prod_{a=1}^h F_a\right\|_{\mathrm J}
 \le C_{R,h}N^{C_h}\prod_a\|F_a\|_{\mathrm J}.
\tag{10}
\]
Here and below a displayed power of \(N\) is independent of the physical auxiliary colors and of \(s\) in its specified disk. It can depend on fixed word length or tree size. The sup-to-Chebyshev comparison follows from the cosine integral for coefficients, and the derivative bound from Markov's inequality. Combining it with full complete Hermite interpolation proves (10).

For a canonical polynomial, its top monomial coefficient is a fixed multiple of its top Chebyshev coefficient: \([z^d]C_d=1/2\) for \(d\ge1\). Hence
\[
|\phi_\sigma(F)|\le C N^2\|\operatorname{rem}_{P_\sigma}F\|_{\mathrm{Ch}}.
\tag{11}
\]
Equations (9)--(11) control the whole quotient operation. They do not majorize a return term separately by an old positive gate and do not require an increasing return-permitting open profile.

## 3. The physical crossing and circle character

On the equal-color object \(++\), the actual checked crossing has common scalar and stripped spectral values
\[
\kappa_s=q^{(d+s)^2/2},\qquad
 t_j=q^{-2j-1}Q^s,\quad c_j(s)=t_j+t_j^{-1},\qquad
\lambda_j=(-1)^jq^{j(j+1)}Q^{-sj}.
\tag{12}
\]
For a fixed integer crossing power \(n\), including negative \(n\), let \(r^{[n]}_{N,s}\) denote the canonical polynomial with values \(\lambda_j^n\). Its full physical representative is \(\kappa_s^n r^{[n]}_{N,s}\). The \(--\) object uses \(-s\).

For every fixed \(R<1\) and \(n\),
\[
\sup_{|s|\le R}\|r^{[n]}_{N,s}\|_{[-2,2]}+
\sup_{|s|\le R}\|\partial_zr^{[n]}_{N,s}\|_{[-2,2]}
 \le C_{R,n}N^4.
\tag{13}
\]
Here is the collision-safe argument. Away from \(\sin2\pi s=0\), exact Lagrange interpolation is
\[
r^{[n]}_{N,s}(z)=
-\frac1{N(U-U^{-1})}\sum_{j=0}^{N-1}
\lambda_j^n(t_j-t_j^{-1})\frac{P_s(z)}{z-c_j(s)},
\qquad U=e^{2\pi is}.
\tag{14}
\]
The quotient is a divided difference of \(\mathsf T_N\). Nodes lie in a Bernstein ellipse of angular height \(2\pi|\operatorname{Im}s|/N\), on which its first two derivatives are \(O_R(N^2),O_R(N^4)\). Integrating along the segment from a real point to a node gives (13) with the extra factor \(|\sin2\pi s|^{-1}\). Distinct-node collisions inside \(|s|<1\) occur only at \(s=0,\pm1/2\). Their paired indices satisfy \(j+l+1-2s=N\), and exactly
\[
\lambda_l/\lambda_j=(-1)^{l-j}q^{(l-j)(j+l+1-2s)}=1.
\tag{15}
\]
Both the value difference and the node difference vanish, the latter simply. The resulting divided differences are holomorphic, and the confluent interpolation matrix is invertible. Thus the polynomial coefficients extend holomorphically across those collisions. Apply the maximum principle on a fixed larger parameter circle of radius less than one and different from \(1/2\) to remove the apparent denominator uniformly. This proves (13). The common scalar \(\kappa_s^n\), its inverse, and each prescribed fixed framing correction are bounded on the same disk: their ratio to the complete scalar has exponent \(O_{R,n}(1)\). They are retained, not set equal to one.

For mixed orders use the physical carrier convention of the turn theorem:
\[
G_{-+}=\check R_{x,y}r_0(\Omega_{x,y})^{-1},\qquad G_{+-}=I,
\qquad r_0=\kappa_0\sum_{n=0}^{d}(-q)^ne_n.
\tag{16}
\]
The forward mixed crossing has reference polynomial \(r_0\). Reversing the reference order adds the exact monodromy scalar, since
\[
\check R_{y,x}\check R_{x,y}=q^{-s^2}r_0(\Omega)^2.
\tag{17}
\]
Thus reverse crossings, inverses, and every fixed composable crossing word have the corresponding fixed powers of \(r_0\) and the retained powers of \(q^{-s^2}\). Formula (13) at \(s=0\) and (10) bound their canonical norms polynomially. These assertions concern the specified Casimir intertwiner spaces, not arbitrary physical matrix norms.

For an ordinary auxiliary color \(1\le j\le N\), the actual encircling operator is exactly
\[
L_j(\Omega)=(-1)^{j-1}U_{j-1}(\Omega/2).
\tag{18}
\]
To retain its normalization, take the auxiliary module of weights \(j-1-2a\), \(0\le a<j\), with actual closing pivot \(K_j^{1-N}=(-1)^{j-1}K_j\). First take independent generic target roots. Their tensor product has distinct typical highest summands. On a summand of highest root \(w\), the nilpotent transfers cannot contribute to the highest coefficient of the encircling monodromy, and the Cartan and standard-pivot trace is
\[
\sum_{a=0}^{j-1}(qw)^{j-1-2a}
 =U_{j-1}\bigl((qw+q^{-1}w^{-1})/2\bigr).
\tag{19}
\]
The actual pivot supplies the sign in (18). Since the loop intertwines, the generic highest coefficients prove the whole matrix identity. All finite auxiliary transfer denominators are \([r]!\) with \(r<j\le N\), nonzero at this root, so its matrix entries are Laurent regular in the independent target roots. Specialization proves (18) on equal and opposite objects with every confluent coefficient retained. Rigid duality and the braid carriers transport the same central polynomial; the Casimir is fixed by the antipode. This keeps the prescribed encircling direction and framing. No auxiliary dimension division, extra carrier scalar, or modified main-cut factor is part of (18).

Finally \(\|U_{j-1}(z/2)\|_{[-2,2]}\le j\le N\), and Markov bounds its derivative by \(CN^3\). Combining (13), (16)--(18), and (10), the actual fixed-power decorated coupon, written \(R_s^\epsilon L_j\) in its specified frame, has polynomial canonical norm, uniformly in \(j\). The original \(\epsilon\in\{0,\pm1\}\) is allowed; the same argument allows any fixed composable integral crossing power.

## 4. Every typed turn gives the same coefficient estimate

Put
\[
H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
W_n(s)=\prod_{r=1}^{n}\left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right),
\quad \mathcal R e_n=e_{d-n},\quad \mathcal D_s e_n=W_n(s)e_n.
\tag{20}
\]
Removable values at zero are understood. The exact physical turn in fixed polynomial coordinates is \(\gamma_N(s)H_N(s)^{-1}\mathcal R\mathcal D_s\), with the following domains. Mixed morphisms are expressed in (16)'s reference.

| Input | Output | \(\gamma_N(s)\) |
| --- | --- | --- |
| \(\operatorname{End}(++)\) | \(\operatorname{Hom}(-+,+-)\) | \(q^{-s^2/2}\) |
| \(\operatorname{Hom}(-+,+-)\) | \(\operatorname{End}(--)\) | \(q^{s^2/2}\) |
| \(\operatorname{End}(--)\) | \(\operatorname{Hom}(+-,-+)\) | \(q^{s^2/2}\) |
| \(\operatorname{Hom}(+-,-+)\) | \(\operatorname{End}(++)\) | \(q^{-s^2/2}\) |
| \(\operatorname{End}(+-)\) | \(\operatorname{End}(-+)\) | \(1\) |
| \(\operatorname{End}(-+)\) | \(\operatorname{End}(+-)\) | \(1\) |

The source proof uses actual currying, with \(J_xw_a=(-x)^aQ^{a(a+1)/2}\varphi_{d-a}\), followed by the carrier. Thus the table retains the duality ratios, cup scalar, and order-change monodromy. It is not obtained by replacing all six spaces by one untyped algebra.

Euler's sine product, applied to the distinct nonzero integers \(r+kN\), gives for every \(|s|\le R<1\)
\[
\left(\frac{\sin\pi R}{\pi R}\right)^2
\le|W_n(s)|\le
\left(\frac{\sinh\pi R}{\pi R}\right)^2,
\qquad W_n(s)W_{d-n}(s)=H_N(s)^2.
\tag{21}
\]
In particular all the scalars in (20), their inverses, and the six \(\gamma\)'s are uniformly bounded on that disk.

Let \(E_s\) be any actual canonical input, and form
\[
F_s=\operatorname{rem}_{P_\sigma}(R_s^\epsilon L_jE_s),
\qquad D_s[E_s]=\mathscr T_s^{\mathrm{fix}}F_s=\sum_{k=0}^{d}d_k(s)e_k.
\tag{22}
\]
Every multiplication and carrier in (22) uses its specified physical type. Equations (7) and (20) give exactly
\[
d_k(s)=\frac{\gamma_N(s)W_{d-k}(s)}{H_N(s)}
               \phi_\sigma(e_kF_s).
\tag{23}
\]
This includes the return terms; it is not a projection onto old multiplication support. The norm bounds proved above yield
\[
|d_k(s)|\le C_RN^C\|E_s\|_{\mathrm J}\|e_k\|_{\mathrm J}.
\tag{24}
\]
Define
\[
J(u)=\int_0^u\log(2\sin\pi t)\,dt,\qquad
 g(u)=J(2u)-4J(u),\quad0\le u\le1/2,
\qquad G_0=g(1/4)=2\,\mathrm{Catalan}/\pi.
\tag{25}
\]
The complete Newton bounds are uniform, including both parities and endpoints:
\[
\|e_k\|_{\mathrm J}\le C N^C
\begin{cases}
e_k(-2)=\exp\{Ng(k/N)+O(\log N)\},&0\le k\le m,\\
1,&m<k<N.
\end{cases}
\tag{26}
\]
Thus (24) proves the actual deformed low/high coefficient cone. It holds on every fixed \(|s|\le R<1\), not merely the small disk used for the general spectral multiplier comparison. Only its exact diagonal coefficient factors (21) were needed here.

## 5. Reconstruction: the global budget and a fresh Gaussian

From (24)--(26),
\[
\|D_s[E_s]\|_{\mathrm J}
 \le C_RN^C e^{2NG_0}\|E_s\|_{\mathrm J}.
\tag{27}
\]
Indeed low coefficients reconstruct against a second copy of \(e_k\), giving \(\sum_{k\le m}e_k(-2)^2\), whose unique rate maximum is \(2G_0\). The entire high part has only polynomial cost times the input norm.

The same coefficient argument gives more precise angular control. There are \(c,C,y_0>0\) and \(e_N\to0\), independent of \(s,j,E_s\) on the stated families, such that the canonical output satisfies
\[
|D_s[E_s](2\cos(\vartheta+iy))|
\le\|E_s\|_{\mathrm J}
 \exp N\{2G_0-c(\vartheta-\pi)^2+Cy^2+e_N\},
\quad0\le\vartheta\le2\pi,\quad |y|\le y_0.
\tag{28}
\]
For clarity, this is a fresh estimate from the coefficient cone, not an assertion that the general turn preserves any input Gaussian. The low Newton strip rate is
\[
b(u,\vartheta,y)=\int_0^u
 \log|2\cos2\pi v-2\cos(\vartheta+iy)|\,dv-2J(u).
\tag{29}
\]
Uniform truncated logarithmic Riemann sums give the closed upper rate even at moving numerator zeros. Circular rearrangement gives \(b(u,\vartheta,0)\le g(u)\), with strictness for \(0<u<1/2\) away from \(\vartheta=\pi\). Thus \(g(u)+b(u,\vartheta,0)\) has its unique maximum \(2G_0\) at \((1/4,\pi)\). In that regular neighborhood its holomorphic action has angular second derivative \(-\tan(\pi u)/(2\pi)\); strict concavity in \(u\) supplies the index quadratic term. This proves the low-part bound (28); the compact complement has a strict rate gap. The high part has J norm \(\operatorname{poly}(N)\|E_s\|_{\mathrm J}\). Complete Hermite interpolation bounds its canonical values by \(\operatorname{poly}(N)e^{N|y|}\|E_s\|_{\mathrm J}\). Choose \(y_0\) small and \(c\pi^2<G_0\) to absorb that part under (28). No angular hypothesis on \(E_s\) was used.

Fixed derivatives in \(s\) obey the same rate bounds on smaller parameter disks by Cauchy's estimate. Angular derivatives cost powers of \(N\) on a smaller fixed strip, using radius \(1/N\). These statements require the input family to be holomorphic on the corresponding larger disk, as actual pre-resonance typed coupons are. They do not define an analytic interpolation of a discrete auxiliary-color array.

## 6. What can be iterated, and what has not been obtained

Consider the actual fully flagged reduced-hub recursion: an unturned root character multiplies its satellite operators and is then closed; each satellite is either an ordinary decorated leaf \(D_s[1]\), or \(D_s[\prod_a E_{a,s}]\) with the products evaluated in the proper typed quotient. Every internal hub has its specified original character, and every original auxiliary color is retained. For a fixed tree, (10) and (27) give by induction
\[
\|E_s\|_{\mathrm J}\le C_RN^{C_{\mathcal T}}
 \exp\{2N G_0\,n(E)\},
\tag{30}
\]
where \(n(E)\) counts the decorated turns in this recursive subtree. The root coupon has polynomial norm, and (10)--(11) bound its normalized closing scalar with the same total budget. In a closed tree with \(H\) original characters, the root is unturned and the other \(H-1\) characters occur in decorated turns. Therefore
\[
|\phi_\sigma(F_{{\mathrm{root}},s})|
 \le C_RN^{C_{\mathcal T}}e^{2NG_0(H-1)}.
\tag{31}
\]
This is an upper bound for the specified physical auxiliary-colored contraction, uniform over its full finite color cube, fixed half-twist choices, both parities, and \(|s|\le R<1\). The original rigid-profile geometry independently identifies \(F_0=2G_0(H-1)\) as its complete augmented action. The result is therefore at that augmented pressure, not a generic sum of costs assigned to arbitrary bare turns or unflagged hubs.

The main reduced cut must still retain its primitive moment factor. For the actual zero-framed cut, the compiler gives
\[
F_N(M)=\frac{s_x}{s_0}\phi_\sigma(F_{{\mathrm{root}},s}),
\qquad \frac{s_x}{s_0}=H_N(s),\qquad M=q^s.
\tag{32}
\]
Thus its moving normalization contributes a bounded nonvanishing factor on these disks. The full modified dimension, if used, is retained separately. Equation (31) concerns the auxiliary-colored contraction; identifying a summed filled invariant requires its original color kernel, framings, and normalization. In particular the filled knot usually has a smaller volume than its augmented parent, so (31) alone is not the desired filled-knot comparison.

Each individual decorated output has (28). A moving-quotient product is known here to obey the J budget (10); its Gaussian localization does not follow from that norm estimate. A subsequent decorated turn nevertheless creates (28) afresh. No bound in this report supplies a strict loss when an original auxiliary color moves away from completeness, a deformation of the exact complete Fourier cancellation, a lower bound preventing cancellation in the whole scalar, convergence of the normalized regular meridian profile, or a selected classical main-meridian factor. Those remain separate whole-source questions. The absolute return-profile obstruction in `/private/tmp/md-return-sector-open-profile-monotonicity-obstruction.md` is consistent with every estimate above.
