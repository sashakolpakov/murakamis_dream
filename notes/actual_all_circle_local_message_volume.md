# A volume theorem with a twist bound independent of the number of tangles

A knot in this theorem is built from a finite ordered tree of integer
two-strand braids. Turn each child tangle through a quarter-turn before
stacking it on its specified side of the parent braid. Close at a terminal
vertex by the prescribed cylindrical closure. Each vertex, including
each terminal vertex, has its own crossing circle in the augmented
diagram. The [construction and strand test](actual_all_circle_quantitative_volume.md#the-knot-construction)
fix the endpoint orders and require that all the main strands form one
knot, with no additional component closed inside a tangle.

The number of vertices, their degrees, and the nesting depth may be
arbitrary. We prove a sufficient condition at each vertex that does
not depend on any of those global quantities. Write \(d_v\) for the
number of incident tree edges and \(n_v\) for the signed number of
half-twists in its braid. If
\[
             \max_v\frac{d_v}{d_v^2+n_v^2}\le2^{-120},
\]
then the original knot complement is hyperbolic and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                      =\operatorname{Vol}(S^3\setminus K).
\]
In particular, requiring every \(|n_v|\ge2^{119}\) suffices for every
finite tree in this construction. This very coarse constant is a
sufficient bound, not an estimate of the shortest twists for which
the equality holds. The tree and all powers are fixed before \(N\)
tends to infinity.

The proof evaluates a subtree while leaving its attaching edge
unevaluated. The result is a polynomial in the variable at the parent
vertex. Dividing by its value at zero factors out the contribution
already supplied by that subtree. When the next crossing trace is
taken, its error can therefore be compared with the change at that
one vertex. The proof below establishes the nonvanishing needed for
this division and bounds the entire finite polynomial, including its
high indices and repeated-root derivatives.

The earlier [summed criterion](actual_all_circle_quantitative_volume.md)
remains useful and has a much better numerical constant. The two
criteria are alternatives. The local criterion removes a restriction
on the total number of vertices; it does not subsume the earlier
criterion for every individual diagram.

## 1. The theorem and its finite-source inputs

Fix an ordered circle-only tree with at least one edge, its actual
strand frames, retained signs, disk markings and integer powers
\(n_v\). Its original closed main strands must form a knot. Let
\(d_v\) be the graph degree. Define
\[
 \kappa=\max_v\frac{d_v}{d_v^2+n_v^2}.
 \tag{1}
\]
The sufficient local condition proved below is
\[
                         \kappa\le 2^{-120}.
 \tag{2}
\]
The number of vertices is arbitrary but fixed before the quantum
level tends to infinity. Constants in polynomial prefactors, error
constants and starting levels may depend on that entire fixed tree.
The numerical condition (2) does not.

Under (2), the exact reduced zero-framed invariant has the same
nonzero first-charge asymptotic and microscopic profile as in the
published all-circle theorem:
\[
 \frac{F_N(q_N^s)}{F_N(1)A_N(s)H_N(s)}
       =1+O_{\mathcal T,\mathbf n,R}(N^{-1}),\qquad |s|\le R<1,
 \tag{3}
\]
\[
 \frac{2\pi}{N}\log|F_N(q_N^s)|
       \longrightarrow 2\pi\Re\mathcal C(\mathbf1).
 \tag{4}
\]
Here
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
 A_N(s)=q_N^{a(D)s^2/2},\qquad a(D)=-w(D)-\sum_vn_v.
 \tag{5}
\]
Every factor in (5) has its original normalization. Both parities,
all sufficiently large composite levels, and all fixed signed
powers satisfying (2) are included.

The analytic conclusion (3)--(4) is proved here. For its volume
interpretation use the already published ordered octahedral
decomposition, angular charts and primitive completion. Their
explicit positive-path hypotheses follow from the simultaneous
contraction recorded in Section 7 below; they do not require the
sum condition once such a path has been supplied. The same selected
action therefore equals the volume of the original knot complement.
This last implication uses the actual marked completion, not a
source identity.

The finite identities and estimates used below are:

* [bounds for the full polynomial source](actual_main_meridian_source_bounds.md), Sections 1.1--1.4:
  complete Newton coordinates, full value/derivative norm, fixed
  crossing power and typed turn;
* [the exact crossing trace](actual_main_meridian_direct_crossing_trace.md), Sections 2--4:
  the exact translated-grid trace, Fourier coefficients, complete
  normal limits, and endpoint currents;
* [the summed finite-sum estimate](actual_all_circle_curvature_filling_limit.md), Sections 3--8:
  the single-edge index gap, canonical edge interpolation, explicit
  edge action and its derivative bounds;
* [uniform Newton estimates](all_circle_uniform_newton_bounds.md):
  the original real and complex Newton estimates;
* [the sum over internal edge indices](actual_main_meridian_grouped_wire_packet.md):
  the fixed Gamma interpolation and insertion rule.

The estimates below use these exact identities on each finite
subtree. No assumed dominance of a global saddle is an input.

## 2. The full finite kernel and exact recursion

![The parent variable remains free while the crossing trace evaluates the current vertex and its child subtree polynomials.](../book/figures/tree-boundary-message.png)

Each triangle in the drawing represents a subtree, whose evaluation
is a polynomial in the current angle \(t\). The edge to the parent
is the only factor containing its angle \(u\).


Put \(d=N-1\), \(c_j=2\cos((2j+1)\pi/N)\), and
\[
 S_k=\prod_{r=1}^k2\sin(\pi r/N),\qquad
 e_k(z)=S_k^{-2}\prod_{j<k}(c_j-z).
 \tag{6}
\]
The fixed pairing is
\(\phi_\sigma(e_i e_j)=\mathbf1_{i+j=d}\). A physical turn,
after lowering this pairing, identifies equal indices and retains
\(\gamma_e(s)H_N(s)/W_k(s)\). Thus define
\[
 K_N(t,u;s)=\sum_{k=0}^{N-1}
       e_k(-2\cos t)e_k(-2\cos u)\frac{H_N(s)}{W_k(s)}.
 \tag{7}
\]
This is the full kernel, not the regular-window truncation. It is
an even trigonometric polynomial of degree at most \(N-1\) in
each variable. The paired factors and their inverses are bounded
uniformly in \(k,N\) on every fixed disk \(R<1\).

Choose a terminal root. For a nonroot vertex \(v\), its message to
the parent angle \(u\) is the exact polynomial
\[
 M_{v,N}(u)=
 \gamma_{e_v}(s)\,
 \mathcal D_{n_v,\sigma_v,N}^{(t)}
 \left[K_N(t,u;s)\prod_{w\text{ child of }v}M_{w,N}(t)\right].
 \tag{8}
\]
The physical trace \(\mathcal D\) includes the full crossing scalar.
The actual \(\sigma_v\) is \(s,-s\), or \(0\), according to the
ordered pair. The reference monodromy factors remain outside in
the same ledger as the published theorem. Formula (8) follows
by expanding the original covariant contraction and doing finite
sums in a different order. It does not commute physical tangles.

At the root the final trace is
\[
 Z_N=
 \mathcal D_{n_0,\sigma_0,N}^{(t)}
                   \left[\prod_{w\text{ child of }0}M_{w,N}(t)\right].
 \tag{9}
\]
The original closing/framing factor, prescribed reference factors,
and one reduced cut factor \(H_N(s)\) multiply (9). There is no
discarded-source remainder in (8)--(9). Every original normal
channel and every \(0\le k<N\) is still present.

In particular \(M_{v,N}\) is always an even trigonometric polynomial
of degree at most \(N-1\) in its parent variable, regardless of the
size of the subtree. This is seen directly from (7): the trace
and all child operations act only in \(t\).

## 3. Two full-kernel bounds

Use the following constants:
\[
 r=2^{-12},\quad c_K=2^{-16},\quad c=2^{-18},
 \quad y_0=2^{-56},\quad \rho=2^{-14},\quad t_0=2^{-16}.
 \tag{10}
\]
All bounds allow polynomial factors in \(N\), depending on \(R\).
Let \(G_0=g(1/4)\), and let \(\psi(t,u)\) be the published edge
action, with \(\psi(0,0)=2G_0\).

First, for real \(t,u\in[-\pi,\pi]\),
\[
 |K_N(t,u;s)|
 \le C_RN^{A_R}
 \exp N\{2G_0-c_K[(1-\cos t)+(1-\cos u)]\}.
 \tag{11}
\]
To prove this, split (7) into \(k/N\in I=[1/5,3/10]\) and its
complement. On \(I\), the published product bound gives a factor
\(\exp[-\alpha N\sin^2(t/2)]\) at each end, with
\(\alpha>1/250\). The positive endpoint sum has rate \(2G_0\)
and a polynomial prefactor. Outside \(I\), full Hermite
interpolation gives a real sup bound with the single-edge loss
\(\eta_K=\pi/200\), including high indices. Since
\(4c_K<\eta_K\) and \(c_K<\alpha/2\), both pieces satisfy (11).

Second, for complex \(|u|\le r\), real \(|t|\le\pi\), and
\(|y|\le y_0\),
\[
 |K_N(t+iy,u;s)|
 \le C_RN^{A_R}
 \exp N\{\Re\psi(0,u)-c_K(1-\cos t)+16y^2\}.
 \tag{12}
\]
This conditional normalization is essential. Replacing
\(\Re\psi(0,u)\) by \(2G_0+O(r^2)\) would introduce an unnecessary
error larger than some of the later local tail losses.

Here are the details. The complementary kernel, by the polynomial
ellipse bound at each end, is at most
\[
 C_RN^{A_R}
 \exp N\{2G_0-\eta_K+|y|+|\Im u|\}.
 \tag{13}
\]
Since \(|\psi(0,u)-2G_0|\le r^2\), its fixed gap absorbs the
entire claimed angular loss in (12), uniformly in \(t\).
Indeed \(r+r^2+y_0+2c_K<\eta_K/2\).

For the retained kernel and \(|t|\le1/8\), the published exact
edge-sum saddle is uniform on \(|t+iy|,|u|\le1/4\).
The exact formula for \(\psi_{tt}\) gives
\[
 |\psi_{tt}+1/(2\pi)|\le \frac1{50}\frac1{2\pi}.
 \tag{14}
\]
Separate evenness implies \(\psi_t(0,u)=0\). Integrating (14)
on the segment from zero to \(t+iy\) proves a stronger version
of the exponent in (12). Its polynomial amplitude and its
exponentially small lattice currents are retained.
For \(|t|\ge1/8\), use the explicit global bound
\[
 |e_k(-2\cos(t+iy))|
 \le e^2e_k(-2)e^{N[-\alpha\sin^2(t/2)+11y^2]}.
 \tag{15}
\]
The product at the other end satisfies
\(|e_k(-2\cos u)|\le e_k(-2)e^{Nr^2}\) on \(I\):
the normalized product factors have denominators
\(\cos^2((j+1/2)\pi/N)\ge1/3\), and
\(|\sin(u/2)|^2<r^2/3\). The additional change from \(2G_0\)
to \(\Re\psi(0,u)\) costs at most another \(r^2\).
Now
\[
 2r^2<\frac{\alpha}{2}\sin^2(1/16),\qquad
                    c_K<\alpha/4.
 \tag{16}
\]
These inequalities prove (12) on the remaining real angles.
The first follows already from
\(\alpha>1/250\), \(\sin(1/16)>1/(8\pi)\), and \(\pi^2<10\).
No quadratic complex bound for an individual high basis element
has been used in this argument.

On the small bidisk \(|t|,|u|\le r\), the full kernel also has
the same nonzero analytic saddle expansion as its retained part.
The complementary estimate (13) has a fixed gap there. In
particular,
\[
 K_N(t,u;s)=N^{-3/2}a_e(t,u)
 e^{N\psi(t,u)}(1+O_R(N^{-1})),
 \tag{17}
\]
with the paired insertion included in the error and with the
published exact midpoint normalization. The leading
\(a_e\) is holomorphic and nonzero on a slightly larger disk.
The outside \(\gamma_e(s)\) in (8) is not included in \(a_e\).

## 4. A closed class of boundary phases

Write \(a_0=1/(2\pi)\). A boundary phase \(h(u)\) will satisfy
\[
 h(0)=h'(0)=0,\qquad h(-u)=h(u),\qquad
                 |h''(u)+a_0|\le a_0/20,\quad |u|\le r.
 \tag{18}
\]
Assume the child phases have this property. At a nonroot vertex
put
\[
 a_v=d_v/(2\pi),\quad b_v=n_v/(2\pi),\quad D_v=a_v-ib_v,
\]
\[
 A_v(t,u)=\psi(t,u)+\sum_w h_w(t),\qquad
 C_{v,\ell}(u)=\operatorname{stat}_t
 \{A_v(t,u)+ib_vt^2/2-i\ell t\}.
 \tag{19}
\]
There are exactly \(d_v\) incidences in the \(t\) variable.
Consequently
\[
 A_v(t,u)=\psi(0,u)-a_vt^2/2+E_v(t,u),\qquad
 |E_{v,tt}|\le a_v/20,\quad |E_{v,t}/t|\le a_v/20.
 \tag{20}
\]
The last quotient is removable at zero, by evenness in \(t\).
For \(0\le\ell\le L_v=\lfloor t_0|D_v|\rfloor\), the equation
\[
             D_vt=-i\ell+E_{v,t}(t,u)
 \tag{21}
\]
is a contraction on \(|t|\le r\). Its Lipschitz constant is at
most \(1/20\), and its image has radius
\(t_0+r/20<r\). The solution has
\[
 |t_\ell|\le\frac{\ell}{(1-1/20)|D_v|},\qquad
 \frac{380}{441}\frac{\ell a_v}{|D_v|^2}
 \le-\Im t_\ell\le
 \frac{420}{361}\frac{\ell a_v}{|D_v|^2}.
 \tag{22}
\]
These inequalities hold also for complex \(u\). Indeed
\(t_\ell=-i\ell/(D_v-Q_v)\), where \(|Q_v|\le a_v/20\);
the real part of \(D_v-Q_v\) is positive. No reality assertion
about a child phase is needed.

The normalized outgoing phase is
\[
                    h_v(u)=C_{v,1}(u)-C_{v,1}(0).
 \tag{23}
\]
Stationarity gives the exact derivative
\[
 h_v'(u)=\psi_u(t_1(u),u),\qquad
 h_v''(u)=\psi_{uu}
 -\frac{\psi_{ut}^2}{A_{v,tt}+ib_v}.
 \tag{24}
\]
The denominator has modulus at least
\((19/20)|D_v|\). The explicit edge bounds on the radius \(1/4\)
disk give
\(|\psi_{uu}+a_0|\le a_0/50\) and
\(|\psi_{ut}|\le a_0/50\). Since \(|D_v|\ge a_v\ge a_0\),
the right side differs from \(-a_0\) by at most
\[
                 a_0\left(\frac1{50}+\frac{20}{19\cdot2500}\right)
                      <a_0/20.
 \tag{25}
\]
Thus (18) closes without a depth or vertex-count constant.
The same calculation starts the recursion when there are no children.

Charge ordering and the current vertex's action drop follow directly
from \(\partial_\ell\Re C_{v,\ell}=\Im t_\ell\):
\[
 \Re C_{v,\ell}(u)\le\Re C_{v,1}(u)
 -\frac{190}{441}\frac{a_v}{|D_v|^2}(\ell^2-1),
 \tag{26}
\]
\[
 0\le \Re\psi(0,u)-\Re C_{v,1}(u)
 \le\frac{210}{361}\frac{a_v}{|D_v|^2}
 =\frac{420\pi}{361}\frac{d_v}{d_v^2+n_v^2}<4\kappa .
 \tag{27}
\]
There is no sum over descendants in (27).

## 5. The exact finite-message induction

The inductive assertions are these, for all sufficiently large \(N\)
depending on the fixed subtree, uniformly on each fixed main-parameter
disk \(R<1\).

1. \(M_{v,N}(0)\ne0\), and on \(|u|\le r\),
   \[
   \frac{M_{v,N}(u)}{M_{v,N}(0)}
     =\frac{\alpha_v(u)}{\alpha_v(0)}
       e^{Nh_v(u)}(1+O(N^{-1})).
   \tag{28}
   \]
   The amplitude is holomorphic and nonzero; (18) holds.
2. For real \(|u|\le\pi\),
   \[
   \left|\frac{M_{v,N}(u)}{M_{v,N}(0)}\right|
        \le C N^A e^{-Nc(1-\cos u)}.
   \tag{29}
   \]
3. For real \(|t|\le\pi\), \(|y|\le y_0\),
   \[
   \left|\frac{M_{v,N}(t+iy)}{M_{v,N}(0)}\right|
    \le C N^A e^{N[-(c/2)(1-\cos t)+y^2]}.
   \tag{30}
   \]

Only the phase bound and displayed exponential constants are uniform
in the subtree. Amplitude bounds, polynomial powers and thresholds
are allowed to depend on the fixed subtree.

In (28) the normalization is the exact value \(M_{v,N}(0)\).
It retains all \(N\)-dependent crossing, carrier and edge phases.
More explicitly one may write
\[
 M_{v,N}(u)=\Omega_{v,N}(s,\boldsymbol\sigma)\,
       \alpha_v(u)e^{N\mathcal F_v(u)}(1+O(N^{-1})).
 \tag{28a}
\]
Here \(\Omega_{v,N}\) is the original nonzero scalar ledger for
that subtree, including the full
\(q^{n_v(d^2/4-\sigma_v^2/2)}\) factors. It need not converge
as \(N\) varies. The ratio in (28) cancels it exactly.
The leading normalized amplitude
\(\alpha_v(u)/\alpha_v(0)\) is independent of the microscopic
parameters: the first charge coefficient is one and the paired
edge insertion has leading value one. The next coefficients may
depend on them. No oscillatory scalar has been hidden in a claimed
\(N\)-independent amplitude.

To obtain (30) from (28)--(29), use the exact degree bound following
(9). For a Laurent polynomial \(f\) of degree at most \(N-1\), the
polynomial \(z^{N-1}f(z)\), and its reciprocal, give the elementary
Poisson bound
\[
 |f(t+iy)|\le CN^A
 e^{N[-c(1-\cos t)+(1+c)|y|]}
 \tag{31}
\]
when its real bound is (29). It follows either by integrating the
harmonic majorant \( -c(1-\cos t)\), or by the maximum principle
on the disk. For \(|t|\ge r/2\), our \(y_0\) satisfies
\[
 (1+c)y_0<\frac c2(1-\cos(r/2)).
 \tag{32}
\]
For \(|t|<r/2\), use (28) and (18):
\[
 \Re h_v(t+iy)\le
 -\frac{19a_0}{40}t^2+\frac{21a_0}{40}y^2.
 \tag{33}
\]
Since \(|t+iy|<r\), these two estimates prove (30).
The amplitude costs only a fixed polynomial factor.

In applying the next trace, factor out the exact constants
\(\prod_wM_{w,N}(0)\). Do not replace them by absolute
complete-source bounds. On the local disk, the exact normalized
child message has a holomorphic logarithm. More explicitly, (28)
implies, on any fixed smaller disk,
\[
 \frac1N\log\frac{M_{w,N}(t)}{M_{w,N}(0)}
 =h_w(t)+\frac1N\log\frac{\alpha_w(t)}{\alpha_w(0)}
                         +O(N^{-2}).
 \tag{34}
\]
The branches vanish at zero, and all fixed derivatives have the same
orders by Cauchy. The thresholds in (34) may depend on the subtree.
For a fixed vertex the sum of these corrections tends to zero.
It therefore perturbs the local nondegenerate saddle by \(O(N^{-1})\),
or equivalently is retained in its analytic amplitude.
This is why inherited errors do not spend another exponential gap
at every ancestor.

## 6. Conditional trace tails and connectors

After extracting the exact child constants, (12) and (30) give
the global bound for the actual input of the next trace:
\[
 |K_N(t+iy,u)\prod_w M_{w,N}(t+iy)/M_{w,N}(0)|
 \le CN^A e^{N[\Re\psi(0,u)-2^{-20}a_vt^2+128a_vy^2]}.
 \tag{35}
\]
Indeed \(1-\cos t\ge2t^2/\pi^2\),
\(d_v=2\pi a_v\), and \(2\pi<8\). At a root with no outgoing
edge, omit \(K_N\), replace \(\psi(0,u)\) by zero, and retain
the same bound because there are \(d_v\) incoming messages.

Set
\[
 A_0=2^{-41},\qquad
 y_v=A_0t_0a_v/|D_v|,\qquad L_v=\lfloor t_0|D_v|\rfloor.
 \tag{36}
\]
Condition (2) gives \(L_v\ge1\), and \(y_v\le2^{-57}<y_0\).
The exact trace formula retains
\[
 c_{\ell,N}(\sigma)=
 (-1)^{(N-1)(\ell-1)}U_{\ell-1}(\cos2\pi\sigma),
                         \qquad c_{1,N}=1.
 \tag{37}
\]
For a charge \(\ell>L_v\), the chirp and (35), maximized in \(t\),
cost at most
\[
 \left(128a_v+\frac{b_v^2}{4\cdot2^{-20}a_v}\right)y_v^2
 \le2^{18}\frac{|D_v|^2}{a_v}y_v^2.
 \tag{38}
\]
The negative Fourier term is at least \(t_0|D_v|y_v\).
Since \(2^{18}A_0<1/2\), the omitted tail has loss at least
\[
 \frac12A_0t_0^2a_v=2^{-74}a_v>2^{-77}
 \tag{39}
\]
relative to \(\Re\psi(0,u)\). Each additional charge contributes
\(e^{-N(\ell-L_v-1)y_v}\). For the fixed subtree, this dominates
the exact coefficient growth
\(\ell e^{2\pi R'(\ell-1)}\) for all sufficiently large \(N\).

At the original real endpoints the Gaussian loss is
\(2^{-20}\pi^2a_v\). The chirp and finite-charge connectors cost
at most
\(\pi A_0t_0a_v+A_0t_0^2a_v+128A_0^2t_0^2a_v\).
Their sum is less than half the endpoint loss. The exact zero-mode
current obeys that endpoint bound. Thus the original finite
functional, including its endpoints and normals, is its finite
charge sum plus a conditional error with loss (39).

For each retained charge, restrict the real integral to
\([-\rho,\rho]\). Its complement loses at least
\(2^{-20}a_v\rho^2>2^{-51}\). Translate the interval to
\(\Im t_\ell\); its endpoints remain in \(|t|<r\). With
\(\delta=1/20\), the same elementary Young inequality as in the
published calculation gives, along the connectors,
\[
 \Re\{A_v(t-iv,u)+ib_v(t-iv)^2/2-i\ell(t-iv)\}
 \le \Re\psi(0,u)-\frac18a_vt^2
 +\left[\frac{1+\delta}{2}a_v+
 \frac{2b_v^2}{(3-4\delta)a_v}\right]v^2-\ell v.
 \tag{40}
\]
For \(0\le v\le-\Im t_\ell\), the last two terms are at most
\(-\ell v/8\), since
\[
 \frac{420}{361}
 \max\left\{\frac{21}{40},\frac{2}{14/5}\right\}
 =\frac{300}{361}<\frac78.
 \tag{41}
\]
Thus each connector has loss at least \(a_v\rho^2/8>2^{-34}\).
The translated horizontal integral has a nondegenerate Gaussian
with real quadratic part bounded above by
\(-(19/20)a_v\). Its leading amplitude is nonzero:
the edge amplitude, the child amplitudes and the actual
\(\sin t_\ell\) are all nonzero.

Combining these estimates, choose
\[
                              \eta=2^{-80}.
 \tag{42}
\]
Every nonminimal charge is its saddle term plus an absolute
conditional error \(CN^Ae^{N(\Re\psi(0,u)-\eta)}\).
It need not have a relative expansion at its own much lower action.
But (27) and (2) give \(4\kappa<\eta/2\).
Consequently these errors are below the first conditional charge.
Equation (26) orders all retained charges relative to that same
charge. Its coefficient in (37) is exactly one, for both parities.
This proves (28), with a nonzero leading amplitude.

The argument initially takes the formal grid parameters on circles
avoiding \(\sin2\pi\sigma=0\). The entire physical trace and its
first-charge approximation are holomorphic through all collisions
inside \(|\sigma|<1\). Apply the maximum principle to their whole
difference on a slightly larger parameter disk. The leading
orientation/crossing factors are explicit and nonzero; no divided
endpoint current is declared separately removable. This extends
the estimate, and the eventual nonvanishing, to every actual
\(\sigma=0,\pm s\) and both complete parity sequences.

Finally, prove (29) freshly from the exact trace rather than from
its local approximation. This step can use polynomial norms
directly, so colliding-grid derivatives cause no additional
assumption. The real sup norm of each canonical child polynomial,
divided by \(|M_{w,N}(0)|\), is polynomial by (29).
For fixed real \(u\), (11) gives the real sup norm in \(t\) of
the canonical kernel polynomial, retaining its factor
\(\exp N[2G_0-c_K(1-\cos u)]\). Real sup and Chebyshev
coefficient norms are polynomially equivalent at degree less
than \(N\). The full crossing polynomial has polynomial norm.
Multiply these polynomials, apply the exact Chebyshev folding
bound in the correct \(P_{\sigma_v}\) quotient, and then its
top-coefficient functional (D9)--(D11) in the published source
bounds. All these are full polynomial identities and retain
every normal channel. They give
\[
 |M_{v,N}(u)|\le
 CN^A\left|\prod_w M_{w,N}(0)\right|
       e^{N[2G_0-c_K(1-\cos u)]}.
 \tag{43}
\]
The nonzero value just proved at \(u=0\) has the exponent
\(2G_0-\Delta_v\), with \(0\le\Delta_v<4\kappa\).
For \(|u|\ge r/2\),
\[
 4\kappa<(c_K-c)(1-\cos(r/2));
 \tag{44}
\]
for \(|u|<r/2\), (28) and (33) give the stronger bound.
Hence (29), and then (30), hold with the same constants for the
outgoing message. This completes the induction. The proof is
unchanged for a leaf, where the child product is empty.

## 7. Root assembly and the original filled action

Apply the same local trace argument to (9). Its normalized input
has \(d_0\) incoming messages and no outgoing edge, so the only
change to (19)--(43) is to omit \(\psi(t,u)\) and its constant.
The current-vertex drop, charge ordering, tails and connector
estimates have the same constants.

Recover the subtree constants recursively rather than summing
their upper bounds. The child envelope identity (24) shows that
the selected angles satisfy, at every original vertex,
\[
 \sum_{e\sim v}\psi_{e,\tau_v}
                  +\frac{in_v\tau_v}{2\pi}=i.
 \tag{45}
\]
Their modulus is bounded by
\(2\pi/[(19/20)\sqrt{d_v^2+n_v^2}]\), which is much less than
the geometric chart radius. Substituting the recursive critical
values makes all child constants telescope. The root action is
exactly
\[
 \mathcal C(\mathbf1)=\operatorname{stat}_{\boldsymbol\tau}
 \left[\sum_e\psi_e+
 \frac{i}{4\pi}\sum_vn_v\tau_v^2-i\sum_v\tau_v\right].
 \tag{46}
\]
It is the original filled action, not a sum of independently
optimized cap actions. Its selected branch agrees with the
unique small simultaneous solution, by the same weighted
contraction used in (21).

For the geometric path replace the right side of (45) by \(ic\),
\(0\le c\le1\). The published explicit edge Hessian estimates give
the simultaneous contraction on the radius \(1/4\) polydisk,
with diagonal nonlinear bound \(a_v/50\) and row bound \(a_v/25\).
Condition (2) implies
\(\sqrt{d_v^2+n_v^2}\ge\kappa^{-1/2}\). Consequently that solution
has
\[
 |\tau_v(c)|\le
 \frac{2\pi c}{(1-1/50)\sqrt{d_v^2+n_v^2}}<10^{-2},
 \qquad \Im\tau_v(c)<0\quad(c>0).
 \tag{46a}
\]
The same factorization of the nonlinear derivative by \(\tau_v\)
proves the sign, just as in (22). These are precisely the published
primitive-completion hypotheses. All original disk periods,
half twists and the calibrated action are therefore retained
along the actual positive path.

Each edge sum contributes \(N^{-3/2}\); each actual circle trace
contributes \(N^2\) times one nondegenerate one-dimensional
Gaussian, hence \(N^{3/2}\). Since a tree has one more vertex
than edge, the final power is \(N^{3/2}\). All its leading
amplitudes are nonzero. The exact first coefficient (37), rather
than separate evenness alone, pairs the reflected Fourier modes.

The edge insertion is still \(H_N/W_k\), with the original
Gamma interpolation and physical offsets. Its leading value is
one and its first correction is the same cotangent insertion
as in the published theorem. The exact scalar ledger is
unchanged by finite summation order. Thus the complete result
is (3)--(5), and the same first correction can be obtained by
the normalized insertion rule if desired.

## 8. Structural consequences and limitations

This removes the sum over vertices from the sufficient analytic
condition. For example
\[
 \frac{d}{d^2+n^2}\le\frac1{2|n|}\quad(n\ne0)
 \tag{47}
\]
shows that every \(|n_v|\ge2^{119}\) satisfies (2), regardless
of the number or degrees of the vertices. The constant is very
coarse; its purpose is a size-independent sufficient hypothesis.
Zero or short powers are also allowed whenever their own degree
makes (1) small. This is not the claim that the graph can grow
with \(N\): every resulting diagram is fixed first.

The proof is specific to the literal all-circle tree. It uses the
exact degree-\(N-1\) boundary message and the one-edge kernel
factorization. Arbitrary bare junctions, graphs with cycles,
and rational slopes have not been included. The former summed
criterion can remain a less restrictive sufficient test for
individual diagrams; no comparison of optimal constants is claimed.

The main analytic point is conditional normalization at the
finite-polynomial level. Expanding child errors as absolute
remainders at the augmented action, or using \(2G_0+O(r^2)\)
instead of \(\psi(0,u)\) in (12), would not prove this theorem.
The proof above keeps the exact child messages until the next
local saddle and retains all source factors and normal channels.
