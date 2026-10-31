# Phase exclusion for an original regular spectral window

31 October 2026. **Internally reviewed local theorem.** The straddling-window
proof in §§1–6 received root and independent full analytical review. It
estimates a literal start/end window, with every unused row, omitted-half
mode and raw sign retained. Its conclusion is a local exponential loss
relative to that window's positive envelope, not a bound by hyperbolic
volume. The full-row extension and shared-torus consequence in §§7–8
also received independent full analytical review.

## 1. Literal window and hypotheses

Put \(d=N-1\), \(m=\lfloor N/2\rfloor\), \(M=m-1\),
\(\theta=\pi/N\), \(\sigma=-2\cos(2\pi\delta)\), and
\[
 \alpha_r=2\cos((2r+1)\theta)-\sigma,\qquad
 \beta_r=s_r^2,\quad \gamma_r=s_rs_{r-1}\alpha_{r-1},
 \quad s_r=2\sin(r\theta),\qquad
 A_{\mathrm{rest}}^\alpha=\prod_{r=m}^{d}\alpha_r.
\]
The active companion and its tail are
\[
 C_r=\begin{pmatrix}\beta_r(x+y)&\gamma_rxy\\1&0\end{pmatrix},
 \qquad K_{i,j}=e_1^TC_j\cdots C_{i+1}e_1,
 \quad K_{i,i}=1.\tag{1}
\]
All face moduli \(x_0,y_0,b_0,c_0\) are strictly positive and range over
a fixed compact set. The real spectral coordinate ranges over a compact
subset of \((0,1/2)\). Write
\[
 \begin{aligned}
 \alpha(t)&=4[\cos^2(\pi t)-\sin^2(\pi\delta)],\\
 \Lambda_+(t)&=2\sin(\pi t)\left[(x_0+y_0)\sin(\pi t)
  +\sqrt{\sin^2(\pi t)(x_0-y_0)^2+4x_0y_0\cos^2(\pi\delta)}\right],\\
 L_\delta(t)&=\Lambda_+(t)/|\alpha(t)|.
 \end{aligned}
\]
Assume the original positive weighted endpoint action
\[
 F(\mu,\nu)=\mu\log b_0+(1-\nu)\log c_0
                     +\int_{\mu}^{\nu}\log L_\delta(t)\,dt,
 \tag{2}
\]
has uniformly strict interior endpoint maxima
\(\mu_*<t_c<\nu_*\), where \(t_c=1/2-\delta\). The logarithmic pole
in (2) is integrable. Choose disjoint closed row windows
\(I_\mu,I_\nu\Subset(0,1/2)\), away from \(t_c\), whose maxima are
uniformly interior. Work on one compact parameter chart with fixed windows;
a finite collection covers a compact family.

The action separates into a function of the start and a function of the
stop. Strict maximality therefore gives a fixed loss at either boundary
of either window, uniformly in the other endpoint. Shrink the windows
further so that the middle modulus \(b_0|\alpha(t)|\), respectively
\(c_0|\alpha(t)|\), stays strictly above the active secondary eigenvalue's
modulus. This is possible: at the maximum it equals \(\Lambda_+\), while
\(|\Lambda_-|<\Lambda_+\) uniformly on the compact chart.

Let \(i\) and \(j\) run over all integers in \(NI_\mu\) and \(NI_\nu\).
The exact raw window is
\[
 W_N=(-1)^dA_{\mathrm{rest}}^\alpha\sum_{i,j}
 b^ic^{d-j}\prod_{r<i}\alpha_r\prod_{j<r\le M}\alpha_r
 K_{i,j}(x,y),\tag{3}
\]
where \(x=x_0e^{i\vartheta_x}\), and similarly for \(y,b,c\).
Define \(E_N\) by taking the face moduli in each summand, the absolute
values of both unused products and \(A_{\mathrm{rest}}^\alpha\), and the
positive tail \(K_{i,j}(x_0,y_0)\). This is the original positive window
envelope. No division by \(A_{\mathrm{rest}}^\alpha\) is used.

For each \(\varepsilon>0\), there are uniform constants
\(c,C>0\) and \(N_0\) such that
\[
 \boxed{|W_N|\le Ce^{-cN}E_N}\tag{4}
\]
whenever the phase quadruple is at distance at least \(\varepsilon\),
modulo \(2\pi\), from
\[
 \vartheta_x=\vartheta_y=\vartheta_b=\vartheta_c-\pi.
 \tag{5}
\]
One can use the maximum of these three relative phase distances. If the
omitted-half scalar is zero, both sides of (4) are zero exactly.

## 2. Every active subproduct has a positive comparison

Set
\[
 \eta_r=1+\frac{\alpha_{r-1}}{s_rs_{r-1}},\qquad
 G_r=\begin{pmatrix}1&-\beta_ry\\0&\beta_ry\end{pmatrix}.
\]
On the present row range, \(G_r\) and its inverse are uniformly bounded.
Direct multiplication gives the exact identity
\[
 G_rC_rG_{r-1}^{-1}
   =\beta_r\begin{pmatrix}x&\eta_rx\\y&y\end{pmatrix}.
 \tag{6}
\]
The real \(\eta_r\) are bounded above and below by positive constants.
The absolute entries on the right of (6), at arbitrary outer phases, are
exactly their positive-modulus entries. Products inherit this bound.
Moreover, the two columns of a nonempty positive product are uniformly
comparable: compare the columns in its rightmost factor, then multiply
on the left by positive matrices.

Since \(G_ue_1=e_1\) and \(e_1^TG_v^{-1}=(1,1)\), the positive
\(K_{u,v}\) is the product of the \(\beta\)'s times the first-column
sum of the positive word product. Column comparability and bounded gauge
endpoints consequently give, for every active subinterval,
\[
 \|C_v(x,y)\cdots C_{u+1}(x,y)\|
       \le C_0K_{u,v}(x_0,y_0).\tag{7}
\]
The empty product uses \(K_{u,u}=1\). This does not replace the signed
companion recurrence by its entrywise absolute value.

Split products can also be reassembled at bounded cost. For consecutive
positive word products \(P_1,P_2\), column comparability gives
\[
 (\mathbf1^TP_2e_1)(\mathbf1^TP_1e_1)
       \le C_1\mathbf1^TP_2P_1e_1.
\]
The empty cases are immediate. Restoring the \(\beta\) factors yields
\[
 K_{v,w}(x_0,y_0)K_{u,v}(x_0,y_0)
          \le C_1K_{u,w}(x_0,y_0),\qquad u\le v\le w.
 \tag{8}
\]
This is used for a fixed number of consecutive pieces, not with a fixed
loss multiplied over \(O(N)\) pieces.

The [exact positive-word angular estimate](research_positive_eta_word_transfer.md)
implies
\[
 |K_{i,j}(x,y)|\le e^{-c_1N}K_{i,j}(x_0,y_0)\tag{9}
\]
when the outer relative phase is separated from zero. Each selected
interval has macroscopic length. Summing (9) termwise proves (4) in this
case, retaining all scalar factors and their zeros.

## 3. The two restricted switches are literal finite matrices

Write \(p_-\le i\le p_+\), \(q_-\le j\le q_+\) for the integer
windows, with \(p_+<q_-\). On the start window use
\[
 T_r^{\mathrm{start}}=
 \begin{pmatrix}C_r&u\\0&b\alpha_r\end{pmatrix},
 \qquad u=e_1.\tag{10}
\]
Let \(U_N\) be its product's \(2\)-by-\(1\) off-diagonal block. On the
stop window use
\[
 T_r^{\mathrm{stop}}=
 \begin{pmatrix}c\alpha_r&w_r\\0&C_r\end{pmatrix},
 \qquad w_r=e_1^TC_r=(\beta_r(x+y),\gamma_rxy).
 \tag{11}
\]
Let \(V_N\) be its product's \(1\)-by-\(2\) off-diagonal block. Then
\[
 \begin{aligned}
 W_N={}&(-1)^d A_{\mathrm{rest}}^\alpha c^{d-M}
 \left(\prod_{q_+<r\le M}c\alpha_r\right)
 V_N(C_{q_--1}\cdots C_{p_++1})U_N
 \left(\prod_{r<p_-}b\alpha_r\right).
 \end{aligned}\tag{12}
\]
Empty products are identities. A start at \(i\) supplies the seed
\(e_1\); a stop at \(j\) reads \(e_1^T\) after \(C_j\) acts.
Thus its active factor is precisely (1). The disjoint windows exclude
\(i=j\) because that path is outside their specified support. The
[unrestricted four-state identity](research_original_one_sided_four_state_transfer.md)
retains that diagonal path. Formula (12) introduces no pivot, factor of
\(N\), or source renormalization.

## 4. A mismatched middle separates the whole active block

It remains to consider small outer relative phase. Remove the common
outer phase \(\vartheta_o=\vartheta_y\). At exactly equal outer phases,
a constant unitary diagonal change of basis makes the active companion
\(e^{i\vartheta_o}\) times its real companion. Both active eigenvalues
have this common phase relative to their real, signed values.

On the start window \(\alpha>0\), so the scalar phase is
\(\vartheta_b\). A mismatch from \(\vartheta_o\) separates it from the
Perron eigenvalue; the window's modulus condition separates it from the
secondary eigenvalue for every phase. On the stop window \(\alpha<0\),
the scalar phase is \(\vartheta_c+\pi\), and the same argument applies.
If the quadruple stays away from (5), either (9) applies or at least one
of these middle mismatches stays uniformly nonzero. Taking the outer-phase
threshold sufficiently small preserves the full Sylvester separation.

The exact coefficients are analytic in \(t\) and \(h=1/N\):
\[
 \begin{aligned}
 \alpha_h(t)&=4\cos^2(\pi(t+h/2))-4\sin^2(\pi\delta),\\
 \beta(t)&=4\sin^2(\pi t),\\
 \gamma_h(t)&=4\sin(\pi t)\sin(\pi(t-h))\alpha_h(t-h).
 \end{aligned}\tag{13}
\]
The uniform real separation extends to a fixed complex neighborhood of
the relevant window. The bounded analytic Sylvester inverse there checks
all hypotheses of the
[analytic discrete-switch theorem](research_analytic_switching_suppression.md).
There is no guessed interpolation of the discrete start or stop.

Apply that theorem to (10) or (11), whichever has the mismatch. Its exact
off-diagonal product consists of two pure endpoint terms and a sum with
an exponentially small residual coupling. The scalar blocks remain
\(b\alpha_r\) or \(c\alpha_r\). They do not occur in the same
Sylvester equation, so no separation between them is required.

## 5. Both endpoints and the residual return to the original envelope

Let \(T_{ij}\) be the positive summand of (3) without the common
\(|A_{\mathrm{rest}}^\alpha|\). The compact positive-transfer Perron
bounds and the unused-interval Riemann products give uniformly
\[
 \log T_{ij}=NF(i/N,j/N)+O(\log N),\qquad
 \sum_{i,j}T_{ij}=\exp\{NF(\mu_*,\nu_*)+O(\log N)\}.
 \tag{14}
\]
The unused intervals stay away from the pole. The active interval crosses
it, but the positive word matrix remains regular. The identity
\(\int_0^{1/2}\log|\alpha(t)|\,dt=0\) is used only to rewrite the
already bounded products into (2); it creates no finite division at a
sampled zero.

Use (7) to bound complex active subproducts and (8) to reassemble a fixed
number of pieces into the original unsplit \(K_{i,j}\). Bounded gauge
vectors can replace the endpoint \(e_1\)'s at bounded cost. Each of the
two pure gauge terms fixes the relevant switch at a window boundary,
within one mesh step, while all other starts or stops and exterior factors
remain unchanged. Strict maximality and separability of (2) therefore give
\[
 \text{each endpoint term}
  \le \operatorname{poly}(N)
       \exp\{N[F(\mu_*,\nu_*)-\gamma]\},\qquad \gamma>0.
 \tag{15}
\]
Both terms are kept. Neither is assumed absent.

For a residual insertion, (7)–(8) and bounded one-row couplings compare
its weight with a constant times the original positive summand at that
row, up to one mesh shift. The unused \(\alpha\)'s on the two windows
are bounded away from zero, so these shifts cost bounded factors.
Only polynomially many locations are summed. Thus
\[
 \text{residual contribution}
   \le \operatorname{poly}(N)e^{-c_2N}\sum_{i,j}T_{ij}.
 \tag{16}
\]
Together (14)–(16) prove (4). Multiply the common omitted-half scalar back
exactly, including its zeros; no nonvanishing scalar amplitude is asserted.

## 6. Limits of the local conclusion

The proof requires positive ordinary face moduli and strict regular
endpoint maxima. It does not cover spectral caps, row-endpoint or
pole-touching windows, or a maximum on its window boundary. One zero
outer weight reduces the active recurrence to first order and admits a
scalar version under the same strict-window assumptions, but that case
is not used here. A protected middle needs a different start specification.

Incompatible local phase requirements may permit (4) at one port of a
shared torus. They do not by themselves compare the resulting envelope
with complete volume or show that these windows cover the full source.

## 7. Full-row regular windows

The polynomial identity extends to the full numerator by taking
\(M=d\) and \(A_{\mathrm{rest}}^\alpha=1\) in (3) and (12).
It is the same original path sum over \(0\le i\le j\le d\), with all
outside diagonal factors retained. For \(2\le r\le d\),
\[
 \eta_r=
 \frac{\cos\theta+\cos(2\pi\delta)}
      {\cos\theta-\cos((2r-1)\theta)}>0
 \tag{17}
\]
for all sufficiently large \(N\) on the fixed interior spectral chart.
On compact row intervals inside \((0,1)\), it is uniformly positive and
bounded. Hence (6)–(9) apply unchanged. The limiting formulas for
\(\alpha,\Lambda_+\) and \(L_\delta\) also hold throughout \((0,1)\).

Choose two disjoint fixed windows inside \((0,1)\), staying away from
the two zeros \(1/2\pm\delta\) of \(\alpha\). Assume (2)
has strict interior maxima in those windows, and shrink them to satisfy
the same secondary-modulus separation. The proof of (4) is then unchanged,
with alignment
\[
 \vartheta_x=\vartheta_y
   =\vartheta_b+\arg\alpha(\mu_*)
   =\vartheta_c+\arg\alpha(\nu_*),
 \qquad \arg\alpha\in\{0,\pi\}.
 \tag{18}
\]
The signs are constant on the selected windows for large \(N\).
The rate differences in (14) are still given by (2), with the continuous
normalization \(\int_0^1\log|\alpha(t)|\,dt=0\). No absolute rate
formula for a possibly zero common scalar factor is needed.
The before and after unused intervals may contain a pole when a full-row
window lies beyond it. Such a factor is common to every selected term;
factor it out exactly before applying the estimates. Only the varying
parts on the two windows need the smooth Riemann-product bounds.
More explicitly, factoring the products below the first window and above
the second window leaves (12), whose variable scalar products stay in the
pole-free windows. The active middle interval is controlled by (6).
The boundary gaps are differences of (2), so any factored common scalar
has no effect. Its zeros again make both sides zero.

This proves the full-row version with no assumed nonzero sampled factors.
It covers the usual regular sign pairs \((+,+)\), \((+,-)\), and
\((-,+)\) when the corresponding strict-window hypotheses hold; no
classification of all critical or boundary configurations is required.

The [finite window audit](../experiments/audit_research_regular_spectral_window_phase_exclusion.py)
and its [recorded output](../experiments/research_regular_spectral_window_phase_exclusion_results.json)
check 402 exact half-row and full-row matrix/path identities, including
sampled spectral zeros and zero outer weights. This checks the finite
dictionary, not the analytical exponential estimate or a new physical-matrix
interface.

## 8. An exact shared-torus consequence

Fix the original incidence graph and protected-face specialization. Let
\(J\) be a finite set of ports satisfying the full-row or half-row
window theorem above, with all four incident weights positive. Other ports
may have any certified absolute torus majorants \(M_{e,N}(L)\).
Use one shared positive radius \(L_f\) for each ordinary face and the
original coefficient target \(d\) there; protected variables remain zero.

For each regular port impose (18) on its incident face phases. These are
equations of the form \(\vartheta_f-\vartheta_g=0\) or \(\pi\).
They have a simultaneous torus solution exactly when their signed
incidence graph has even label sum around every cycle. Thus an inconsistent
\(\mathbb F_2\) system has no torus solution. Compactness of the phase
torus supplies \(\varepsilon>0\) such that at every phase point some
port in \(J\) is at least \(\varepsilon\) from its alignment locus.

Apply (4) at that port and the ordinary positive-envelope bound at all
other selected ports. The original Cauchy coefficient formula gives
\[
 \left|[\text{original targets}]
       \prod_{e\in J}W_{e,N}\prod_{e\notin J}P_{e,N}\right|
 \le Ce^{-cN}
 \frac{\displaystyle\prod_{e\in J}E_{e,N}(L)
                     \prod_{e\notin J}M_{e,N}(L)}
      {\displaystyle\prod_{f\text{ ordinary}}L_f^d}.
 \tag{19}
\]
There is no independent choice of radii at each incidence and no alteration
of the original target. The homogeneous common phase is harmless. Any
external source characters must be retained separately in their original
normalization.

Formula (19) is an exponential improvement on the specified shared window
envelope, uniform for a fixed diagram and compact regular parameters. It
does not show that this envelope is at most \(e^{N\Phi_D}\), exclude
consistent phase systems, or control the omitted irregular windows.
