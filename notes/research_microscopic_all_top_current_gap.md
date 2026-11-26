# An actual gap for microscopic all-top current packets

Private written proof, 16 November 2026.

Take the top Newton piece at every surviving vertex decorated by a
microscopic vertical current. Its exact radical contraction leaves
only low-degree physical-row coupons. If the resulting closed forest
has a fixed original leaf-reduction certificate, the entire packet
has rate tending to zero with the width of the top band. This includes
the original current integration, all crossing carriers, shared colors,
and edges joining evaluated vertices.

This is an actual source bound for the specified packet. It assumes
no descendant action estimate or positive descendant geometry. It
does not cover packets retaining a complementary high-degree coupon.

## 1. The original current and the safe packet

Fix a finite original circle tree \(G\), a nonempty selected set \(S\),
and all edges incident to \(S\), counted once. Every selected vertex
has an original incidence. Write \(B\) for the outside vertices.
Outside colors remain ordinary variables; estimates
below are on \(z_b\in[-2,2]\). Keep fixed integer powers \(n_v\) and
unit charges at all selected vertices. Use
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 \eta=(-1)^D,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
\]
\[
 P_N(z)=2T_N(z/2)+2,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),\quad
 S_j=\prod_{k=1}^j2\sin(k\pi/N),
\]
\[
 K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w),\qquad
                 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{1}
\]

Choose a nonempty current set \(C\subseteq S\) satisfying
\[
 \{v\in S:\text{\(v\) has an edge to \(B\)}\}\subseteq C.
 \tag{2}
\]
Set \(Y=S\setminus C\),
\[
 T=\{t\in Y:\text{\(t\) has an edge to \(C\)}\},\qquad
 U=Y\setminus T,\qquad H=G[U].
 \tag{3}
\]
Thus \(G[Y]\), and in particular \(H\), has no untraced kernel
incidences. Let \(r_t\ge1\) be the number of edges from \(C\) to
\(t\in T\). Fix \(0<A<\pi\), and choose integration heights
\[
 H_v^{\rm end}=\alpha_v/N,\qquad 0\le\alpha_v\le A
                                    \quad(v\in C).
 \tag{4}
\]
During the integration \(0\le h_v\le H_v^{\rm end}\), put
\[
 w_v=2\cosh h_v,\qquad
 Q_{t,N,\mathbf h}(z)=\prod_{\substack{v\in C\\vt\in E}}K_N(w_v,z),
\]
\[
 D_{C,N}(\mathbf h;\mathbf z_B)=
 \prod_{\substack{vv'\in E\\v,v'\in C}}K_N(w_v,w_{v'})
 \prod_{\substack{vb\in E\\v\in C,\ b\in B}}K_N(w_v,z_b).
 \tag{5}
\]
Internal \(C\)-edges and all original outside incidences are retained.

Write the full-Hermite remainder of each whole shared product as
\[
 \operatorname{can}Q_t=\sum_{j=0}^Dq_{t,j}(\mathbf h)e_j,\qquad
 M=\lfloor\varepsilon N\rfloor,\qquad
 \mathcal T_t=\sum_{r=0}^{M}q_{t,D-r}(\mathbf h)e_{D-r}.
 \tag{6}
\]
Only \(M<m\) will be used. The reduction in (6) is in its original
traced variable, after multiplying all incident endpoint coupons.
Define the packet
\[
 \begin{split}
 I_{C,N}^{\rm top}(\mathbf z_B)
 ={}&\int_{\prod_{v\in C}[0,\alpha_v/N]}
       \prod_{v\in C}\{\rho_{N,n_v,1}(h_v)\,dh_v\}
       D_{C,N}(\mathbf h;\mathbf z_B)\\
 &\quad\cdot
 \left(\prod_{y\in Y}\phi_N^{(y)}\right)
 \left[
   \prod_{y\in Y}R(z_y)^{n_y}
   \prod_{yy'\in E(G[Y])}K_N(z_y,z_{y'})
   \prod_{t\in T}\mathcal T_t(z_t)
 \right],
 \end{split}
 \tag{7}
\]
where the exact original paired current is
\[
 \rho_{N,n,1}(h)=
 \frac{2i\eta N^2 C_{N,n}}{\pi}
 \frac{\sinh h\,e^{inN(\pi^2-h^2)/(4\pi)}
                         \sinh(nNh/2)}{4\cosh^2(Nh/2)},
 \qquad C_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{8}
\]
This is one term of the literal expansion of the original full-survivor
current: at **every** decorated survivor use
\(\operatorname{can}Q_t=\mathcal T_t+
(\operatorname{can}Q_t-\mathcal T_t)\), and choose the first summand
at all \(t\in T\). Its coefficient is one. The outer inclusion--exclusion
sign of the \(C\)-current, when present, is \((-1)^{|C|+1}\).
Neither sign is changed in (7).

## 2. Quantitative coefficient and physical-row bounds

Define continuous functions at zero by
\[
 u(x)=2x\log\frac{e}{2x},\qquad
 h(x)=2x\log\frac{\pi e^2}{2x},\qquad u(0)=h(0)=0.
 \tag{9}
\]
Both are increasing on \([0,1/4]\).

The microscopic full-kernel bound in the current source gives,
uniformly in (4),
\[
 \sup_{z\in[-2,2]}|Q_t(z)|\le C_{G,A}N^{2r_t}.
 \tag{10}
\]
This is a bound for the ordinary product. Its degree is at most
\(r_tD\), so Markov's inequality also gives
\(\sup|Q_t'|\le C_{G,A}N^{2r_t+2}\).
In particular its original first normals have not been omitted.

For \(0\le r\le M\le N/4\), the Frobenius identity in (1) implies
\[
                      q_{t,D-r}=\phi_N(e_rQ_t).
 \tag{11}
\]
For \(r\ge1\), \(|c_a-z|\le4\) on the real interval and
\(2\sin(k\pi/N)\ge4k/N\) for \(k\le r\) yield
\[
 \|e_r\|_{[-2,2]}
 \le\frac{4^r}{S_r^2}
 \le\frac{(N/2)^{2r}}{(r!)^2}
 \le\left(\frac{eN}{2r}\right)^{2r}
 \le e^{Nu(\varepsilon)} .
 \tag{12}
\]
The same bound holds for \(r=0\). Markov adds at most \(N^2/2\)
for its first derivative. The full original trace is
\[
 \phi_N(F)=\eta\sum_{a<m}
   \{(4-c_a^2)F'(c_a)-c_aF(c_a)\}
             +\mathbf1_{N\ {\rm odd}}F(-2).
 \tag{13}
\]
Substituting (10)--(12), including both terms of the product derivative,
proves
\[
 |q_{t,D-r}|\le C_{G,A}N^{2r_t+3}e^{Nu(\varepsilon)}.
 \tag{14}
\]
All these bounds hold at both parities. At \(N=2\) the allowed band
is \(M=0\), and the same identities and estimates apply.

The exact radical coefficients are
\[
 b_{ra}=(-1)^{r+a}
 \frac{2\sin((2a+1)\pi/N)\,S_r^2}{S_{r-a}S_{r+a+1}}
                  \quad(0\le a\le r<m),\qquad |b_{ra}|\le2.
 \tag{15}
\]
Consequently
\[
 \phi_N(R^{n_t}\mathcal T_t f)
   =\sum_{a=0}^{M}\lambda_{t,a}R(c_a)^{n_t}f(c_a),
 \qquad
 \lambda_{t,a}=\sum_{r=a}^{M}q_{t,D-r}b_{ra},
 \tag{16}
\]
and
\[
 \sum_{a=0}^{M}|\lambda_{t,a}|
 \le C_{G,A}N^{2r_t+5}e^{Nu(\varepsilon)}.
 \tag{17}
\]
Indeed \(\sum_a|\lambda_{t,a}|\le
2\sum_{r\le M}(r+1)|q_{t,D-r}|\).
The odd simple node contributes zero to (16). Each local original
normal differentiates the radical; no normal of a surviving source
is discarded. The exact crossing values in (16), with their original
carriers, have modulus one.

For the actual physical row \(F_{a,N}(z)=K_N(c_a,z)\), the pinned
row theorem gives
\[
 \deg F_{a,N}=a,\qquad
 \|F_{a,N}\|_{\cos,1}=M_{a,N}=F_{a,N}(-2),\qquad
 M_{a,N}\le N e^{Nh(\varepsilon)}\quad(a\le M),
 \tag{18}
\]
where the cosine coefficient norm includes all ordinary polynomial
data, not just the physical values. Also
\[
 0<K_N(c_a,c_b)\le\min(M_{a,N},M_{b,N})
                                      \le M_{a,N}M_{b,N}.
 \tag{19}
\]
These facts retain the positive physical-row law and its shared index.

## 3. Exact descendant and its certified bound

Assume the fixed closed forest \(H=G[U]\), with powers \(n_u\),
has the following finite certificate ending at the empty forest:
remove an isolated vertex of any current integer power; remove a
leaf of current power \(\sigma=\pm1\) and subtract \(\sigma\) from
its neighbor's power; or remove a zero-power leaf and its neighbor
with all their incident edges. The order and current power updates
are independent of \(N,\mathbf h\), and every physical color.
The empty forest has the empty certificate.

For an assignment \(\mathbf a=(a_t)_{t\in T}\), \(0\le a_t\le M\),
put
\[
 p_{u,\mathbf a}(z)=
       \prod_{\substack{t\in T\\tu\in E(G[Y])}}F_{a_t,N}(z)
                                                    \quad(u\in U),
 \qquad
 D_T(\mathbf a)=
       \prod_{\substack{tt'\in E(G[Y])\\t,t'\in T}}
                       K_N(c_{a_t},c_{a_{t'}}).
 \tag{20}
\]
Applying (16) in every \(T\)-variable turns the surviving contraction
in (7) into exactly
\[
 \sum_{0\le a_t\le M}
   \left[\prod_{t\in T}\lambda_{t,a_t}R(c_{a_t})^{n_t}\right]
       D_T(\mathbf a)\,
             Z_{H,N}(\{p_{u,\mathbf a}\}_{u\in U}).
 \tag{21}
\]
Here \(Z_{H,N}\) is the original fully traced source of \(H\), with
all its kernels, original integer powers, and full local normals.
Each \(a_t\) is the same at all its incident edges. In particular
the \(T\)--\(T\) edges in (20) remain. The formula is also valid when
\(T\) or \(U\) is empty, with the usual empty products.

Let
\[
 d_*=\max\{1,\max_{v\in S}\deg_G(v)\},\qquad
 D_T^{Y}=\sum_{t\in T}\deg_{G[Y]}(t).
 \tag{22}
\]
Then \(\deg p_{u,\mathbf a}\le d_*\varepsilon N\), and (18)--(19)
give
\[
 D_T(\mathbf a)\prod_{u\in U}\|p_{u,\mathbf a}\|_{\cos,1}
 \le\prod_{t\in T}M_{a_t,N}^{\deg_{G[Y]}(t)}
 \le N^{D_T^{Y}}e^{ND_T^{Y}h(\varepsilon)}.
 \tag{23}
\]

For \(v_H=|U|>0\), define
\[
 d_H=\max\{2,\max_{u\in U}\deg_H(u)\},\quad
 B_H=v_Hd_H^{v_H},\quad p_H=v_H(d_H+3),
\]
\[
 g(x)=x\log2+u(x),\qquad
 \Phi_H(x)=v_H\{g(B_Hx)+(d_H-1)h(B_Hx)\}.
 \tag{24}
\]
For empty \(H\), use \(B_H=1,\ p_H=0,\ \Phi_H=0\).
The adopted certificate theorem gives
\[
 |Z_{H,N}(\{p_u\})|
 \le C_{H,\mathbf n}N^{p_H}e^{N\Phi_H(d_*\varepsilon)}
                         \prod_u\|p_u\|_{\cos,1}
 \tag{25}
\]
whenever \(d_*\varepsilon\le1/(4B_H)\).
This is the proved bound for the exact inserted source in (21);
no descendant quantum hypothesis is being supplied in its place.

## 4. Integrated packet theorem and parent gap

Let \(e_C\) be the number of edges within \(C\), and \(b_C\) the
number with exactly one endpoint in \(C\), including outside edges.
Set
\[
 \varepsilon_0=\frac1{4B_Hd_*},\qquad
 \omega_C(\varepsilon)
   =|T|u(\varepsilon)+D_T^{Y}h(\varepsilon)
                                      +\Phi_H(d_*\varepsilon).
 \tag{26}
\]
Thus \(\varepsilon_0\le1/4\), all bands in (6) have \(M<m\), and
\(\omega_C(\varepsilon)=O_G(\varepsilon\log(1/\varepsilon))\to0\).

**Theorem.** Under (2) and the certificate in Section 3, uniformly
for \(0\le\varepsilon\le\varepsilon_0\), all levels, all heights (4),
and real outside colors,
\[
 \boxed{\quad
 |I_{C,N}^{\rm top}(\mathbf z_B)|
 \le C_{G,\mathbf n,A}N^{p_C}e^{N\omega_C(\varepsilon)},\qquad
 p_C=2(e_C+b_C)+5|T|+D_T^{Y}+p_H .
 \quad}
 \tag{27}
\]
A fixed ordinary outside derivative of total order \(|\nu|\)
satisfies the same rate with \(p_C+2|\nu|\).

*Proof.* Apply (25) to every actual source in (21), uniformly over
its shared colors. Use (23), then sum its coefficients with (17).
Since \(\sum_{t\in T}r_t\) is the number \(b_{CT}\) of \(C\)--\(T\)
edges, the resulting polynomial power is
\(2b_{CT}+5|T|+D_T^{Y}+p_H\), and its exponent is (26).
Crossing values are left in (21) before this upper estimate.

The microscopic current source proves, uniformly for the fixed
integer powers and \(0\le\alpha_v\le A<\pi\),
\[
 \int_0^{\alpha_v/N}|\rho_{N,n_v,1}(h)|\,dh\le C,
 \qquad
 |D_{C,N}(\mathbf h;\mathbf z_B)|
                    \le C N^{2(e_C+b_{CB})}.
 \tag{28}
\]
The first bound also follows directly from (8): \(N^2\), \(\sinh h\),
and the interval length cost \(N^2,N^{-1},N^{-1}\); every remaining
factor is bounded when \(Nh\le A\). The second retains all internal
and outside removed edges. Here \(b_{CB}\) counts \(C\)--\(B\) edges,
and \(b_C=b_{CT}+b_{CB}\) by (2)--(3). Inserting (28) into (7)
proves (27). For outside derivatives, (2) places all outside variables
in \(D_{C,N}\). Markov's inequality gives \(N^2\) per derivative,
with the finite product rule absorbed in the constant. \(\square\)

Suppose additionally that the same original unit-charge parent has
a supplied positive solution at complete outside angles. Its
calibrated action is
\[
 M_G=e_GM_\infty-\mathcal E(z_0)/\pi>0.
 \tag{29}
\]
Here \(e_G\) counts the included original edges and
\(M_\infty=4G_{\rm Cat}/\pi\), with \(G_{\rm Cat}\) Catalan's constant.
For completeness, the strict inequality uses no descendant geometry.
At complete outside data the energy is the sum of its square energies
without outside work. Every square at the positive parent is interior;
strict convexity and the constant boundary value
\(E_\square=\pi M_\infty/8\) give
\(E_\square<\pi M_\infty/8\). There are two squares per original edge
and \(\mathcal E=4\sum E_\square\), proving (29).

Choose any fixed \(0<\varepsilon\le\varepsilon_0\) so small that
\(\omega_C(\varepsilon)\le M_G/2\). Then, at complete outside colors
and with any fixed outside normals,
\[
            |I_{C,N}^{\rm top}|
                \le C N^{p}e^{N(M_G-M_G/2)}.
 \tag{30}
\]
This is a genuine strict parent-rate upper gap for the specified
actual packet. A finite collection of admissible \(C\)'s and fixed
certificates permits one common sufficiently small \(\varepsilon\).

There is also a controlled complex outside neighborhood. Let \(d_b\)
be the number of original included edges incident to \(b\in B\).
The packet is an ordinary polynomial of degree at most \(d_bD\)
in \(z_b\). Tensor cosine expansion of this polynomial, using (27)
on the real cube, gives
\[
 |I_{C,N}^{\rm top}(\{-2\cos u_b\})|
 \le C N^{p'}\exp N\left\{\omega_C(\varepsilon)
                                  +\sum_{b\in B}d_b|\Im u_b|\right\}.
 \tag{31}
\]
Indeed each cosine coefficient is bounded by \(2^{|B|}\) times
the real-cube norm, there are only polynomially many coefficients,
and \(|\cos(ku)|\le e^{k|\Im u|}\). Apply the same argument after
any fixed spectral derivative, using the real bound in (27).
If \(\omega_C(\varepsilon)\le M_G/2\), the fixed strip
\(\sum_b d_b|\Im u_b|\le M_G/4\) therefore retains a parent gap
\(M_G/4\). This continuation pays its explicit exponential loss;
no polynomial bound at arbitrary complex outside colors is claimed.
No quotient has been imposed on any outside variable.

## 5. Scope and direct sources

All decorated survivors were put in the top band. If a complementary
coupon \(\operatorname{can}Q_t-\mathcal T_t\) remains at a surviving
vertex, (25) does not apply merely because the underlying forest has
a certificate. Such a coupon generally has degree comparable to \(N\).
Similarly an untouched complete or free boundary kernel is not a
low-degree row coupon. Condition (2) excludes those incidences here.
No arbitrary joint spectator is included in this theorem.

Closedness alone is not a source bound: the reduction certificate is
essential. The result covers one explicit packet in the original
microscopic current, not its complementary packets, macroscopic
height interval, or full scalar source. It asserts neither a geometric
leading coefficient nor arbitrary-short-component coverage.

The exact full-survivor current, physical-row contraction and local
leaf identities are prior results. The additional assertion is their
uniform completion for the safe all-decorated-top packet, including
its shared endpoint-normal coefficient budget and the original
current integration.

The following complete direct proofs were read at the listed versions;
their used implications and hashes were checked:

* [Full-period current and charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  original current, full-survivor graph, microscopic kernel and
  integrated scalar bounds, and all crossing carriers.
* [Certified charged forest pruning](research_charged_forest_leaf_pruning_bound.md),
  SHA256 53e401677dc75e264717abe12ef66f950b240952d78533b71e364be5a57a1fa5:
  exact certificate, full-normal source bound, and the constants (24).
* [Physical-row charge transport](research_physical_row_charge_transport.md),
  SHA256 d09d5c669848f0389504cea613244570eca18be03f2b608a359773e423e97040:
  shared row polynomials, positive cosine mass, degree and rate bounds.
* [Full radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  Frobenius coefficients, exact consumed-normal functional and
  uniform \(b_{ra}\) bound.
* [Ambient split-current action gap](research_split_current_convex_action_gap.md),
  SHA256 8e42b3e549cebd45fa301ae3c41858ab2def475fa072985a49f5bc639ee204dc:
  original action normalization and square-boundary energy used
  solely to establish \(M_G>0\).

Only written mathematics, source reads and hashes were used. No
mathematical programs, tests, numerical experiments or builds were
run. All earlier private notes and public manuscripts remain unchanged.
