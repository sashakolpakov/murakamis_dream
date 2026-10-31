# Regular stop-window exclusion with a protected input middle

31 October 2026. **Internally reviewed research local theorem.**
This keeps the original specialization \(b=0\) exactly, hence the start
row is \(i=0\). It assumes a strict regular maximum only for the stop.
There is no regular start maximum, inverse zero-face weight, or inverse
initial-row gauge. The conclusion is a phase loss relative to the original
window envelope, not a comparison with complete volume.

The reflected protected-output case is proved by an exact finite row
reflection in §6. No double-zero specialization is included.

## 1. The exact fixed-start source

Use \(N\ge3\), \(d=N-1\), \(\theta=\pi/N\),
\(\sigma=-2\cos(2\pi\delta)\), and
\[
 s_r=2\sin(r\theta),\quad
 \alpha_r=2\cos((2r+1)\theta)-\sigma,\quad
 \beta_r=s_r^2,\quad
 \gamma_r=s_rs_{r-1}\alpha_{r-1}.
\]
Let \(A=x+y\), \(P=xy\), and retain the original continuant
\[
 K_{0,0}=1,\quad K_{0,1}=\beta_1A,\qquad
 K_{0,r}=\beta_rA K_{0,r-1}+\gamma_rP K_{0,r-2}.
 \tag{1}
\]
The [literal source expansion](research_original_one_sided_four_state_transfer.md)
has the factor \(b^i\). Since every exponent is nonnegative,
specializing \(b=0\) selects exactly \(i=0\):
\[
 (-1)^dH_{V,\mathrm{LEFT}}(x,0,c,y)
   =A_{\mathrm{rest}}^\alpha
      \sum_{j=0}^{M}c^{d-j}
         \prod_{j<r\le M}\alpha_r\,K_{0,j}(x,y),
 \quad
 M=\lfloor N/2\rfloor-1,\quad
 A_{\mathrm{rest}}^\alpha=\prod_{r=M+1}^{d}\alpha_r.
 \tag{2}
\]
For the full numerator use \(M=d\), the empty omitted product, and
\(H_V\) instead of \(H_{V,\mathrm{LEFT}}\). The start-at-zero diagonal
term \(j=0\) is present in (2). It lies outside the regular stop window
considered below; it has not been discarded from the full source.

Let \(I=[\nu_-,\nu_+]\Subset(0,1)\) be a fixed stop window. In the half-row case
take \(I\Subset(0,1/2)\). Write \(q_-\le j\le q_+\) for all integers
in \(NI\). Restrict the sum in (2) to these rows and call the resulting
raw polynomial \(W_N\). Let \(E_N\) be the same sum with positive face
moduli and absolute values of every unused scalar factor.

Throughout, \(x_0,y_0,c_0\) range over a fixed positive compact set,
and \(\delta\) over a compact subset of \((0,1/2)\). The window stays
away from the two zeros \(1/2\pm\delta\) of
\[
 \alpha(t)=4[\cos^2(\pi t)-\sin^2(\pi\delta)].
\]
All compactness assumptions are uniform on the chosen parameter chart.

## 2. An exact positive seed, including the initial singular rows

For \(r\ge2\), put
\[
 \eta_r=1+\frac{\alpha_{r-1}}{s_rs_{r-1}}
   =\frac{\cos\theta+\cos(2\pi\delta)}
          {\cos\theta-\cos((2r-1)\theta)},\qquad
 M_r=\begin{pmatrix}x&\eta_rx\\y&y\end{pmatrix}.
 \tag{3}
\]
For all sufficiently large \(N\), every \(\eta_r\), \(2\le r\le d\),
is positive. They need not be uniformly bounded near the initial row.
The following identities use them exactly:
\[
 \begin{aligned}
 Z_1&=\beta_1(x,y)^T,\\
 Z_r&=\beta_rM_rZ_{r-1},\qquad r\ge2,\\
 Z_r&=G_r(K_{0,r},K_{0,r-1})^T,\qquad
 G_r=\begin{pmatrix}1&-\beta_ry\\0&\beta_ry\end{pmatrix},\\
 \mathbf1^TZ_r&=K_{0,r}.
 \end{aligned}\tag{4}
\]
At \(r=1\), (4) follows from \(K_{0,1}=\beta_1(x+y)\).
Thereafter it is the exact gauge identity
\(G_rC_rG_{r-1}^{-1}=\beta_rM_r\), where
\[
 C_r=\begin{pmatrix}\beta_r(x+y)&\gamma_rxy\\1&0\end{pmatrix}.
\]
No \(G_0^{-1}\) occurs. Equivalently, (4) is the exact positive
word expansion beginning with \((x,y)\), rather than an invented
initial asymptotic amplitude.

At complex face phases, entrywise absolute values satisfy
\[
 |Z_r(x_0e^{i\vartheta_x},y_0e^{i\vartheta_y})|
       \le Z_r(x_0,y_0).
 \tag{5}
\]
This uses only positivity of the exact \(\eta_r\), not a bound on their
size. In particular \(|K_{0,r}(x,y)|\le K_{0,r}(x_0,y_0)\).
On any regular row interval, both \(G_r,G_r^{-1}\) are bounded, so
the norm of the original active state is bounded by a constant times
the positive \(K_{0,r}\). The same holds after further active propagation:
it is still the exact state in (4), with the full initial seed retained.

Choose once a macroscopic bulk interval strictly between \(0\) and
the left endpoint of \(I\). On this interval the entries of \(M_r\)
lie in one fixed positive compact set. Apply the
[two-step word contraction](research_positive_eta_word_transfer.md)
only there, and ordinary entrywise majorants before and after it.
For any fixed separation of the outer relative phase,
\[
 |K_{0,j}(x,y)|\le e^{-\kappa_1N}K_{0,j}(x_0,y_0)
 \quad\text{for every }j\in NI.
 \tag{6}
\]
The early unbounded \(\eta_r\)'s introduce no loss: they occur identically
in the positive majorant. Summation proves the window estimate in this
outer-mismatch case.

## 3. Stop-action differences do not require a start-rate formula

The limiting positive active root is
\[
 \Lambda_+(t)=2\sin(\pi t)
 \left[(x_0+y_0)\sin(\pi t)
 +\sqrt{(x_0-y_0)^2\sin^2(\pi t)
                      +4x_0y_0\cos^2(\pi\delta)}\right],
 \quad L_\delta(t)=\Lambda_+(t)/|\alpha(t)|.
 \tag{7}
\]
Choose a reference point \(\nu_0\in I\) and define the stop primitive
\[
 F_{\mathrm{stop}}(\nu)
    =(1-\nu)\log c_0+\int_{\nu_0}^{\nu}\log L_\delta(t)\,dt.
 \tag{8}
\]
Changing the lower limit to zero adds a constant; that normalization
is unnecessary here. Assume (8) has a uniformly strict interior maximum
\(\nu_*\), with a fixed positive gap to both window boundaries.
This is the only endpoint-maximum hypothesis.

Here is a uniform relative estimate valid for the exact initial seed.
Let \(u_r>0\) be positive left Perron vectors of \(M_r(x_0,y_0)\),
chosen smoothly and with a fixed normalization on a regular neighborhood
of \(I\), and let \(\rho_r\) be their Perron roots. Their components
are bounded above and below, and
\(u_r/u_{r-1}=1+O(N^{-1})\) componentwise. Since the state \(Z_{r-1}\)
is positive, (4) gives
\[
 u_r^TZ_r=\beta_r\rho_r u_r^TZ_{r-1}.
\]
Comparing \(u_r^TZ_{r-1}\) with \(u_{r-1}^TZ_{r-1}\) and multiplying
over any subinterval of that neighborhood yields
\[
 \log\frac{K_{0,j}(x_0,y_0)}{K_{0,q}(x_0,y_0)}
     =\sum_{r=q+1}^{j}\log(\beta_r\rho_r)+O(1).
 \tag{9}
\]
For \(j<q\) use the reversed scalar ratio. The error is uniform for all
such rows and all \(N\), independent of the magnitude or direction of
the earlier positive seed. No matrix inverse or secondary-root inverse
is used. Smooth Riemann comparison replaces the sum by
\(N\int_{q/N}^{j/N}\log\Lambda_+(t)\,dt+O(1)\).

Factor out the unused product above \(q_+\) and
\(A_{\mathrm{rest}}^\alpha\) exactly. If this common product vanishes,
both \(W_N\) and \(E_N\) vanish. Otherwise, for positive summands
\(T_j=c_0^{d-j}\prod_{j<r\le M}|\alpha_r|\,K_{0,j}(x_0,y_0)\),
their nonzero ratios obey
\[
 \log(T_j/T_q)
   =N[F_{\mathrm{stop}}(j/N)-F_{\mathrm{stop}}(q/N)]+O(1).
 \tag{10}
\]
Only the varying unused factors in the pole-free stop window enter
this estimate. Thus each boundary summand is exponentially below the
positive window sum. No absolute estimate for a potentially tiny common
scalar, no regular starting row, and no start saddle has been assumed.

## 4. Only the stop switch is gauged

Put \(A_{q_--1}=(K_{0,q_--1},K_{0,q_--2})^T\) and use the exact
stop matrices
\[
 T_r^{\mathrm{stop}}
  =\begin{pmatrix}c\alpha_r&w_r\\0&C_r\end{pmatrix},
 \qquad w_r=e_1^TC_r=(\beta_r(x+y),\gamma_rxy).
 \tag{11}
\]
If \(V_N\) is the off-diagonal block of their ordered product over
\(q_-\le r\le q_+\), the original window is exactly
\[
 W_N=(-1)^dA_{\mathrm{rest}}^\alpha c^{d-M}
       \left(\prod_{q_+<r\le M}c\alpha_r\right)
       V_N A_{q_--1}.
 \tag{12}
\]
The stop at \(j\) includes \(C_j\), giving \(K_{0,j}\), not a shifted
continuant. Equation (12) contains the complete original seed at row zero.

Let \(s_\nu=\arg\alpha(\nu_*)\in\{0,\pi\}\). The supported alignment is
\[
 \vartheta_x=\vartheta_y=\vartheta_c+s_\nu
          \pmod{2\pi}.
 \tag{13}
\]
There is no phase for \(b=0\). At the maximum of (8),
\(c_0|\alpha(\nu_*)|=\Lambda_+(\nu_*)\).
The positive root is strictly larger in modulus than the secondary
root on the strict compact chart. Shrink the window, retaining its
interior maximum and boundary gap, so that \(c_0|\alpha(t)|\) stays
strictly above that secondary modulus throughout it.

Away from (13), either the outer relative phase has a fixed separation,
already covered by (6), or it is small and the scalar phase
\(\vartheta_c+s_\nu\) is separated from the common outer phase.
At exactly equal outer phases a constant unitary diagonal change of
basis makes \(C_r\) that common phase times its real companion.
The scalar therefore misses the Perron root by phase and the secondary
root by modulus. A sufficiently small outer-phase perturbation preserves
this full Sylvester separation. Analyticity in the scaled row variable
extends it to one fixed complex neighborhood of the stop window.

Apply the [analytic switch theorem](research_analytic_switching_suppression.md)
only to (11). It retains
\[
 V_N=H_{\mathrm{end}}(C_{q_+}\cdots C_{q_-})
       -\left(\prod_{r=q_-}^{q_+}c\alpha_r\right)H_{\mathrm{start}}
       +\sum_j\left(\prod_{r=j+1}^{q_+}c\alpha_r\right)
                    R_j(C_{j-1}\cdots C_{q_-}),
 \quad \|R_j\|\le Ce^{-\kappa_2N}.
 \tag{14}
\]
Multiply each term by the actual seed in (12). Equation (5), the
regular \(G\)-bounds, and (4) bound the first endpoint by a constant
times \(K_{0,q_+}(x_0,y_0)\), and the second by a constant times
\(K_{0,q_--1}(x_0,y_0)\), with their exact after-products.
These are the two stop-boundary summands, within one mesh step.
Their fixed loss follows from (10).

For a residual insertion at \(j\), the same argument bounds its active
input by \(CK_{0,j-1}(x_0,y_0)\). On the stop window the ratio
\(K_{0,j}/K_{0,j-1}\) is bounded above and below by positive constants,
directly from the positive matrix update in (4). Hence the residual
is bounded by \(Ce^{-\kappa_2N}\) times the original positive stop
summand at \(j\). There are only \(O(N)\) insertions.
Both boundary terms and the residual are thus exponentially below
the positive window envelope. Restoring all exact common factors gives,
for every fixed distance \(\varepsilon>0\) from (13),
\[
 \boxed{|W_N|\le C e^{-\kappa N}E_N.}\tag{15}
\]
Constants are uniform on the stated compact chart. Sampled zeros in
common unused factors and either parity's raw prefactor remain exact.

## 5. The protected target and supported incidence graph

The original \(b\)-face target is zero. Nonnegative polynomial
exponents make the substitution \(b=0\) exactly its constant-term
restriction, also when that face occurs at other ports. No new
integration variable or phase is assigned to it.

These ports supply the same two local inequalities used by the
[cycle-packing criterion](research_regular_window_cycle_packing.md):
the unconditional positive-envelope bound and (15). Use the three
supported incidences \((x,y,c)\), with labels \((0,0,s_\nu/\pi)\).
All repeated incidences, shared ordinary radii, original targets,
and external source characters remain as in that criterion.
The local result itself gives no comparison with \(\Phi_D\).

## 6. Exact reflection and the protected output

For every finite level and every spectral value,
\[
 \alpha_{d-r}=\alpha_r,\qquad
 \beta_{N-r}=\beta_r,\qquad
 K_{i,j}(x,y)=K_{d-j,d-i}(x,y).
 \tag{16}
\]
For the last identity reverse a monomer/dimer tiling of the interval
\(i+1,\ldots,j\). A monomer at \(r\), of weight \(\beta_r(x+y)\),
goes to \(N-r\). A dimer ending at \(r\), of weight
\(s_rs_{r-1}\alpha_{r-1}xy\), goes to one ending at \(N+1-r\);
its weight is unchanged because
\(s_{N-r}=s_r\) and \(\alpha_{N-r}=\alpha_{r-1}\).
The reversed interval is \(d-j+1,\ldots,d-i\). This proves (16),
including empty intervals, without a physical-turn or unrecorded duality.

In the full original path expansion, the substitution
\[
 (i,j,b,c)\longmapsto(d-j,d-i,c,b)
\]
preserves every monomial, unused row factor and the raw sign. This is an
internal local polynomial identity, not a relabeling of shared source faces.
Hence
the \(c=0\) specialization, which forces \(j=d\), is the exact
reflection of the \(b=0\) specialization. A regular start window
reflects to a regular stop window, with the explicit mesh shift
\(j'/N=1-N^{-1}-i/N\). Such an \(O(N^{-1})\) boundary shift is covered
by the same boundary-gap and one-row comparisons above.

The genuine RIGHT half-row sector has
\(i\ge\lceil N/2\rceil\). Under reflection this is precisely
\(j'\le\lfloor N/2\rfloor-1=M\), at both parities. Thus (15) applies
to protected-output FULL and RIGHT windows, with supported alignment
\(\vartheta_x=\vartheta_y=\vartheta_b+\arg\alpha(\mu_*)\).
The output-zero incidence is absent. This is an exact source reflection,
not an assertion that a general turned operator is multiplicative.

Both outer weights must remain positive, and the other middle must
remain positive. No double-zero extension, irregular stop/start maximum,
spectral cap, or pole-touching window is included. The theorem controls
these specified source windows only; global window coverage and the
complete-volume comparison remain separate.

Independent analytical review: root and cluster each completed a full proof
read with PASS. The reviews checked the exact positive seed without an initial
gauge inverse, bulk-only angular contraction, the seed-independent Perron
ratio, both stop boundary terms and residual comparisons, exact common zeros,
and the finite reflected FULL/RIGHT source at both parities. No numerical
asymptotic check substitutes for these arguments. The conclusion retains all
strict-window and positive-supported-weight hypotheses above.
