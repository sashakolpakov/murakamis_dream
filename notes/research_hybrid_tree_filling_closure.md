# A common criterion for long powers and large valence

Two proved source estimates have complementary hypotheses. A large
number of controlled children permits every fixed power at the next
vertex. A sufficiently large power permits a bounded number of
children. The same boundary disk and exponential estimates can be
used in both operations. This note gives the common choice of
constants and proves closure under an arbitrary finite mixture,
including the final trace.

The result concerns original marked circle trees, not only paths.
It still does not allow an arbitrary short power at a vertex with
few children.

## 1. Exact sources and the statement

Use the original Newton algebra, complete edge kernel \(K_N\),
crossing \(R\), and full closing functional \(\phi_N\). A terminal
vertex has the source
\[
 H_{p,N}(u)=\phi_N^{(t)}[R^pK_N(t,u)],\qquad |p|\ge2.
 \tag{1}
\]
At a vertex with \(m\) incoming children and one outgoing edge,
the source is exactly
\[
 F_{\rm new,N}(u)=\phi_N^{(t)}\!\left[
       R^nK_N(t,u)\prod_{\nu=1}^mF_{\nu,N}(t)\right].
 \tag{2}
\]
At the final root there is no outgoing edge:
\[
 Z_N=\phi_N^{(t)}\!\left[R^n\prod_{\nu=1}^mF_{\nu,N}(t)\right].
 \tag{3}
\]
All incident children occur. The raw products are formed before
taking the original trace. Values and first normals at repeated
roots are both retained.

**Theorem.** There are finite integers \(M\ge3\), \(B\ge2\) with
the following property. Root any fixed finite original marked
circle tree at a vertex with at least one child. Every other
terminal vertex has a fixed signed power of magnitude at least
two. At each remaining vertex, including the root, require
\[
                    m\ge M\quad\hbox{or}\quad |n|\ge B,
 \tag{4}
\]
where \(m\) is its number of children. When \(m\ge M\), the
power may be any fixed integer, including \(0,\pm1\).
The same constants work for every fixed size, depth, ordering
and branching pattern, with unrelated signs and magnitudes.

Every nonroot source has a full nonzero boundary expansion
\[
 F_N(u)=\varepsilon_N A(u)e^{NW(u)}(1+O_F(N^{-1})),
                         \qquad |\varepsilon_N|=1,
 \tag{5}
\]
on one common complex disk. Its amplitude is holomorphic and
nonzero there, and its phase and global estimates satisfy the
common constants below. The final source has
\[
 Z_N=\Omega_N N^{3/2}D_0e^{NS}(1+O_{\rm tree}(N^{-1})),
                  \qquad |\Omega_N|=1,\quad D_0\ne0.
 \tag{6}
\]
Both parities are included. Errors, amplitude sizes and starting
levels may depend on the entire fixed tree and power assignment.

Under the original framing and component conditions giving a
knot, the marked geometry identifies
\(2\pi\Re S=\operatorname{Vol}(S^3\setminus K)\). Therefore
the original reduced zero-framed Kashaev invariant satisfies
the volume conjecture for these knots.

## 2. Choose the invariant class before either threshold

Use the common terminal estimates for all \(|p|\ge2\), and
the full bare-edge packet and global two-angle Gaussian bound.
Also use Lemmas 1--2 of
[the fixed-domain long-turn theorem](research_fixed_domain_long_power_turns.md):
\[
\begin{split}
 |K_N(t,u)|&\le CN^d
 e^{N\{\Re\psi(0,u)-\gamma_e(1-\cos t)\}},
             &&t\in[-\pi,\pi],\ |u|\le r_e,\\
 |K_N(t,u)|&\le CN^d
 e^{N\{\Re\psi(t,0)-\gamma_w(1-\cos u)\}},
             &&|t|\le r_w,\ u\in[-\pi,\pi].
\end{split}
 \tag{7}
\]
The first includes the outer first-normal bound at polynomial
cost on each fixed real spectral interval away from the
complete endpoint. These are estimates of the full kernel.

Choose \(R>0\) so the closed disk \(|u|\le2R\) lies strictly
inside the common terminal source, zero-free amplitude and
marked geometric charts, inside the bare-edge charts, and
with \(2R<r_e\). Shrink it once so that
\(\Re[-\psi'']\ge a_e^*I>0\), the terminal curvature has a
common lower bound \(a_T>0\), \(2R\) is smaller than the
full edge's global complex strip width, and
\[
 \left|-\frac{2\pi\psi_t(t,u)}t-1\right|\le1/100
                           \quad(|t|,|u|\le2R).
 \tag{8}
\]
The removable value at \(t=0\) is understood. Set
\[
 a_0=\min(a_T,a_e^*),\qquad
 H\ge\max\left\{
 \sup_{|p|\ge2,|u|\le2R}|W_p(u)-W_p(0)|,\
 2R^2\sup\left|\frac{\psi_u(t,u)}u\right|\right\}.
 \tag{9}
\]
The invariant phase bounds will be
\[
 |W(u)-W(0)|\le H,\qquad \Re[-W''(u)]\ge a_0
                                 \quad(|u|\le2R).
 \tag{10}
\]

Let \(c_e,C_e',h_e\) be constants in the full complex edge bound
\[
 |K_N(x+iy,v+iw)|\le CN^d
 e^{N\{M_\infty-c_e(1-\cos x)-c_e(1-\cos v)+C_e'(y^2+w^2)\}}.
\]
Both operations below produce at least the real output loss
\[
 \gamma=\min(c_e/2,a_e^*,\gamma_w)>0,\qquad
 \Delta=\gamma(1-\cos(R/4)).
 \tag{11}
\]
Choose the invariant angular and quadratic constants
\[
\begin{split}
 c&\le\min(c_T,c_e,\gamma/2,\Delta/8,a_0/4),\\
 C&\ge\max(C_T,C_e',L_2^2/a_0+L_2/2),\qquad L_2=2H/R^2.
\end{split}
 \tag{12}
\]
Here \(c_T,C_T\) are common terminal constants. Choose a
positive strip width \(h\) smaller than the terminal and edge
widths and \(R/2\). For
\(I=[-2\cos(R/4),2]\), reduce it further so
\[
 g_I(-2\cos(x+iy))\le\Delta/2,\qquad
 R/2\le|x|\le\pi,\quad |y|\le h.
 \tag{13}
\]
The Green function is continuous and zero on \(I\), so this
is a positive choice. It is the strip-reset construction
in the recursive high-valence proof. It applies to both
operations: both have real output loss at least \(\gamma\),
output spectral degree \(N-1\), and the phase bounds (10).

Thus the invariant whole-source estimate is
\[
 |F_N(x+iy)|\le C_FN^{d_F}
 e^{N\{\Re W(0)-c(1-\cos x)+Cy^2\}},
          \qquad |x|\le\pi,\quad |y|\le h.
 \tag{14}
\]
All data in (8)--(14) are fixed before either threshold.

## 3. The high-valence threshold

The proof of
[recursive high-valence closure](research_recursive_high_valence_source.md),
Sections 3--7, uses only the invariant input estimates. It
does not require that its children were generated by another
high-valence step. Its sufficient constants are recalled here
to make their order of choice explicit.

For a phase satisfying (10), write
\(-W''(0)=a-ib_W\) and put
\[
 Q_W(t)=-\frac{W'(t)-ib_Wt}{at}.
\]
The common Taylor majorant on \(|t|\le2R\) gives one
\(r<R/2\) and \(L_Q<\infty\) such that
\[
 |Q_W-1|\le1/100,\qquad |Q_W'|\le L_Q\quad(|t|\le r).
 \tag{15}
\]
Reduce \(r\) also so \(r<r_w/2\), and include the edge
slope in \(L_Q\). Define
\[
\begin{gathered}
 a_{\rm cut}=r/2,\quad c_0=c(1-\cos(a_{\rm cut}/2)),\quad
 d_{\min}=2\pi a_0,\quad b_{\max}=H/(2R^2),\quad k_0=2c/\pi^2,\\
 L_0=7/(2d_{\min}),\qquad
 \Gamma=4C_e'R^2+\sup_{|u|\le2R}|\psi(0,u)-M_\infty|,\\
 K_0=\frac{49}{d_{\min}^2}
       \left(C+C_e'+\frac{b_{\max}^2}{2k_0}\right)
                         +\frac{49}{32\pi^2k_0}.
\end{gathered}
 \tag{16}
\]
Choose \(M\ge3\) so every \(m\ge M\) satisfies
\[
\begin{gathered}
 d_{\min}m\ge\max(28/r,14/h),\qquad
 \frac{2\pi L_Q}{(99/100)^2d_{\min}m}<1/2,\\
 \Gamma\le mc_0/4,\qquad L_0/m\le mc_0/4,\qquad
 L_0/m\le ma_0a_{\rm cut}^2/4,\\
 (K_0+L_0)/m\le\frac{c_e}{2}(1-\cos(R/2)).
\end{gathered}
 \tag{17}
\]
These are finitely many eventually satisfied inequalities.

For any such \(m\) children, that proof applies to (2) for
every fixed signed \(n\). It uses
\[
 A=\sum_\nu\Re[-W_\nu''(0)]+\frac1{2\pi},\quad
 B_0=\sum_\nu\Im W_\nu''(0),\quad \widetilde n=n+2\pi B_0,
\]
and the positive weighted average of (15) and the edge slope.
The selected charge path obeys \(|t_\lambda|\le r/4\),
has positive lower depth, and has rate loss at most \(L_0/m\).
The finite source still contains the original \(R^n\);
\(\widetilde n\) is only an analytic estimate of its total
imaginary quadratic coefficient.

The exact midpoint proof retains the outer physical nodes,
endpoint currents and all charges. Inequalities (17) put
their errors below the selected action on the unchanged
outside disk. The envelope identity and accretive Schur
complement reset (10). The real output loss is at least
\(\min(c_e/2,a_e^*)\ge\gamma\), so (12)--(13) reset (14).

The final-root proof applies to (3) when \(m\ge M\).
There is no outside-variable cost and no outgoing edge
amplitude. Conditions (17) already use the lower bound
\(2\pi m a_0\), so removing the edge's extra curvature
does not invalidate them. That trace has power \(N^{3/2}\)
and a nonzero Gaussian coefficient.

## 4. Bounded arity and a long original power

The integer \(M\) has now been fixed. For \(1\le m<M\), form
the raw product
\[
 G_N(t)=\prod_{\nu=1}^mF_{\nu,N}(t),\qquad
 V(t)=\sum_{\nu=1}^mW_\nu(t).
 \tag{18}
\]
It has the full local expansion with amplitude
\(\prod A_\nu\ne0\), phase \(V\), and unit scalar
\(\prod\varepsilon_{\nu,N}\). Its spectral degree is at
most \(m(N-1)\); it is not reduced before the estimates.
On \(|t|\le R\),
\[
 |V''(t)|\le(M-1)\frac{2H}{R^2},\qquad
 \Re[-V''(t)]\ge ma_0\ge a_0.
 \tag{19}
\]
Its real global norm has rate at most
\(\sum_\nu\Re W_\nu(0)\), with angular loss at least
\(c(1-\cos(a_{\rm cut}/2))\) on the fixed outer interval.
Markov's inequality gives its first normal with the same
rate and an additional factor \(O(m^2N^2)\). The increased
degree therefore causes no exponential cost.

Choose
\[
 L_b\ge(M-1)\frac{2H}{R^2}
       +\sup_{|t|\le R,|u|\le2R}|\psi_{tt}(t,u)|,\qquad
 C_b=8\pi^2L_b,
 \tag{20}
\]
and
\[
 \delta_b=\min(\gamma_e,c_e,c)(1-\cos(a_{\rm cut}/2))>0.
 \tag{21}
\]
Choose one integer \(B\ge2\) such that all \(|n|\ge B\)
satisfy
\[
\begin{gathered}
 |n|>8\pi L_b,\qquad |n|>16\pi/a_{\rm cut},\\
 \frac{C_b}{2n^2}<\min(\delta_b/4,a_0a_{\rm cut}^2/8),
 \qquad \frac{C_b}{n^2}<a_{\rm cut}/4.
\end{gathered}
 \tag{22}
\]
This choice comes after \(M\), and is independent of a tree,
its children and their powers.

Apply the fixed-domain long-turn proof with \(W\) replaced
by \(V\). Equations (19)--(22) give the same contraction
throughout the unchanged complex outside disk:
\(|t_\lambda|<a_{\rm cut}/4\), positive lower depth
\(O(n^{-2})\), and action loss at most \(C_b/(2n^2)\).
The centered full edge estimate controls all outer nodes
and their first normals at the rate
\(\sum\Re W_\nu(0)+\Re\psi(0,u)-\delta_b\).
The central proof uses the actual product expansion, all
trace charges, and the full endpoint current. The larger
raw product degree only changes the polynomial factors
already recorded.

The resulting phase and amplitude are
\[
\begin{split}
 S_{\rm new}(u)&=\operatorname{stat}_t
 \left[\sum_\nu W_\nu(t)+\psi(t,u)+\frac{in}{4\pi}t^2-it\right],\\
 A_{\rm new}(u)&=i\sqrt{\frac2\pi}\,
 \frac{\sin t_*(u)\,a_e(t_*(u),u)\prod_\nu A_\nu(t_*(u))}
 {\sqrt{-\sum_\nu W_\nu''(t_*(u))-\psi_{tt}(t_*(u),u)-in/(2\pi)}}.
\end{split}
 \tag{23}
\]
The unit scalar is \(C_{N,n}\prod\varepsilon_{\nu,N}\).
The powers are \(N^{-3/2}N^2N^{-1/2}=N^0\).
Every amplitude factor is nonzero on the unchanged disk.

The output returns to \(H,a_0\), not the larger bound
in (19). Indeed \(S_{\rm new}'(u)=\psi_u(t_*(u),u)\);
the same Schur complement has the additional nonnegative
central mass \(\sum\Re[-W_\nu'']\). The central full-kernel
estimate (7) and the outer two-angle real bound give the
real output loss at least
\(\min(c_e,\gamma_w)\ge\gamma\). Hence (12)--(13) also
restore the same \(c,C,h\).

At a final root with \(1\le m<M\), omit the edge and use
\(\Phi=V\). The bound \(L_b\) still controls its second
derivative, and \(\delta_b\) is no larger than the product's
outer angular loss. Conditions (22) therefore suffice for
the complete scalar trace proof as well. It gives
\[
 S=V(s_*)+\frac{in}{4\pi}s_*^2-is_*,\qquad
 D_0=i\sqrt{\frac2\pi}\,
 \frac{\sin s_*\prod_\nu A_\nu(s_*)}
 {\sqrt{-V''(s_*)-in/(2\pi)}}\ne0,
 \tag{24}
\]
and the factor \(N^{3/2}\) in (6).
A root with no children is not included.

## 5. Induction, geometry and the remaining exclusions

The terminal family lies in the invariant class. At every
nonroot internal vertex either Section 3 or Section 4
restores that same class. Their hypotheses depend only on
the common estimates, so the two operations may be interleaved
in any finite ordered rooted tree. Either final-root proof
then gives (6). This proves the analytic claims.

The [recursive marked geometric construction](research_recursive_marked_block_geometry.md)
allows every \(m\ge1\); it needs the whole new charge path
inside the inner child and bare-edge charts. Both operations
provide that bound on the unchanged outside disk. All older
primitive filled slopes remain fixed. Each original carrier
occurs once, and the outgoing original longitude is not
multiplied by the number of children. Schläfli's formula
anchors each new action at the sum of the child volumes and
the complete bare-edge volume. The edge term is omitted
at the final root. This identifies the final real action
with the hyperbolic volume of the original filled complement.

Retain the original disk frames and \(n_v=\eta_v-2p_v\),
so the filled curve is \(\mu_v+p_v\lambda_v\).
Require the literal strand tracing to give one main knot
component and no internal closed component. The original
reduced invariant is (3) times its prescribed writhe unit.
Consequently
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                       =\operatorname{Vol}(S^3\setminus K).
 \tag{25}
\]

One immediate subclass permits every finite rooted tree
whose terminal powers have magnitude at least two and
whose nonterminal powers have magnitude at least \(B\).
The same \(B\) works independently of branching, depth and
size. The larger hybrid class also permits arbitrary short
powers at vertices with at least \(M\) children.

This is not cofinite coverage on a fixed template. A vertex
with \(1\le m<M\) may keep a power \(|n|<B\) while other
powers grow through infinitely many assignments. Those
assignments remain outside this theorem unless another
exact reduction or proved short-piece theorem treats their
particular region. Arbitrary adjacent clusters of short
low-valence vertices remain open.
