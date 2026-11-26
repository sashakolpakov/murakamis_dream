# Optimized physical blocks close the critical two-power fold

Private written proof, 16 November 2026.

The optimized cutoff can change with the physical row without changing
the original trace. First compare each physical jet to its actual
fold-normalized baseline. Then contour the baseline on each maximal
constant-cutoff block. Adjacent cutoffs differ by one, so their
vertical currents retain an exact last-summand jump and an actual
anchor correction. Their aggregate is smaller than the decorated
two-power scale.

The two exterior sides remain explicit until the fixed compact
patches are joined. This is a fold assembly theorem, not a local
saddle or general composition theorem.

## 1. Original trace and block choice

Use \(h=N^{-1}\), \(\eta=(-1)^{N-1}\),
\[
 C_N(x)=2\cos(2\pi x+\pi h),\quad t(x)=\pi-2\pi x-\pi h,
 \quad x_j=jh,\quad w_i=2\cosh(\alpha_i h).
 \tag{1}
\]
Here \(c_j=C_N(x_j)\),
\(e_k(C)=S_k^{-2}\prod_{a<k}(c_a-C)\),
\(S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N)\), and
\(K_N(w,C)=\sum_{k=0}^{N-1}e_k(w)e_k(C)\).
Fix \(r\ge1\), real \(|\alpha_i|\le A\), and \(n=2\sigma_0\),
\(\sigma_0=\pm1\). The actual source is
\[
 B_N(C)=\prod_{i=1}^rK_N(w_i,C),\qquad
 \phi_N[R_N^n B_N(C)K_N(C,-2)] .
 \tag{2}
\]
All products precede the original full trace. Write
\[
 L_N(t)=\sum_{k<\lfloor N/2\rfloor}e_k(-2)e_k(-2\cos t),\quad
 R_{N,n}(t)=\mathfrak c_{N,n}e^{inNt^2/(4\pi)},\quad
 \mathfrak c_{N,n}=e^{\pi i n(N-1)^2/(4N)}.
 \tag{3}
\]
The high outgoing sector is retained separately below.

Choose a sufficiently small fixed \(T_0>0\), and mirrored midpoint
cuts with \(T_N=T_0+O(h)\). Their physical rows form
\(\mathcal C_N=\{j_L,\ldots,N-1-j_L\}\), where
\(T_N=\pi-2\pi j_Lh\). At each row set
\[
 \delta(t)=\frac1\pi\arcsin\frac{\cos(t/2)}{\sqrt2},\qquad
 m_j=\lfloor N\delta(t_j)\rfloor,\qquad t_j=t(x_j).
 \tag{4}
\]
The function is even and decreases for positive \(t\). For small
\(T_0\), \(N|\delta(t+2\pi h)-\delta(t)|\le CT_0<1\), so
adjacent physical cutoffs differ by at most one. Combine
equal adjacent cutoffs into maximal blocks. Reflect the positive
blocks, using the same cutoff on the mirrored block. The central
block is a single mirrored block, including the odd simple color
when it is present.
The largest cutoff need not equal \(\lfloor N/4\rfloor\);
the definition (4), including its literal flooring, is used.

For every cutoff \(m\) appearing in (4), let \(H_m=(H_{m,0},H_{m,1})\)
be the fold theorem's two sharp modes, with their common factorial
normalization and coalesced frame at \(\alpha=0\). Put
\[
 \mathcal V_f=\binom{f(x)}
 {[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},\quad
 \mathcal F_m=(\mathcal V_{H_{m,0}},\mathcal V_{H_{m,1}}),
 \tag{5}
\]
\[
 j_*=\begin{cases}N/2-1,&N\ {\rm even},\\(N-1)/2,&N\ {\rm odd},
 \end{cases}
 \quad a_m=\mathcal F_m(x_{j_*})^{-1}
                  \mathcal V_{K_N(w,C_N(\cdot))}(x_{j_*}),
 \quad V_m=H_ma_m .
 \tag{6}
\]
Use (6) separately for every factor in (2); denote its product by
\(B_m^0\). Thus all cutoffs use the same actual two source values.
No source coefficient or normal is chosen independently.

Let \(H_2=|\Im t_2|\) be the calibrated two-power saddle height.
On each block contour the baseline source
\[
 g_m(x)=\sin t(x)\,R_{N,n}(t(x))L_N(t(x))B_m^0(x)
 \tag{7}
\]
with its original sampling kernel
\[
 D_h(x)=(\pi/h)^2\csc^2(\pi x/h).
 \tag{8}
\]
Let \(\mathcal V_{\rm out,N}\) denote the four surviving vertical
half-sides at the two exterior midpoint cuts, reaching heights
\(\pm H_2/(2\pi)\) in \(x\), using the adjacent block's \(g_m\).
Their orientations and normalization are exactly those inherited
from the sum of the block rectangles, namely
\(-\eta/(4\pi^2 i)\) times the integrals of \(D_hg_m\,dx\).
This definition retains the exterior currents, rather than
estimating them separately.

**Theorem.** With \(T_0\) fixed sufficiently small, for all
sufficiently large \(N\), uniformly for the stated real parameters
and both parities,
\[
 \boxed{\quad
 \left|\phi_{\mathcal C_N}[R_N^n B_NK_N(\cdot,-2)]
                   -\mathcal V_{\rm out,N}\right|
 \le C(1+\log N)^{2r}N^{-r-1/4}e^{N\mathcal I_2}.
 \quad}
 \tag{9}
\]
Here \(\mathcal I_2=2G/\pi\), with \(G\) Catalan's integral.
The error is \(o(N^{-r}e^{N\mathcal I_2})\). The result is at
complete output and does not assert output-derivative estimates.
For \(r=0\), the baseline replacement and all cutoff jumps vanish,
and the remaining horizontal and high-sector estimates below apply.

At the fixed outer cuts, the usual compact patch can be chosen
with this same fold anchor. Its difference from the adjacent
baseline has a strict \(\mathcal I_2\) gap by the pinned compact
seam theorem. Hence (9) supplies the missing fold part of that
fixed compact assembly. It does not by itself prove its local
nonzero coefficient.

## 2. Uniform optimized physical error

Put
\[
 I_v(X)=\int_0^v\log
       \frac{\sin^2(\pi X)-\sin^2(\pi s)}{\sin^2(\pi s)}\,ds,
 \quad J_*(t)=I_{\delta(t)}((\pi-t)/(2\pi)).
 \tag{10}
\]
All cutoffs \(m/N\) in this note lie in a fixed closed interval
\([\delta_0,1/4]\) close to \(1/4\). The exact-mode/frame bounds
and the residual prefactors in the direct-cap proof are uniform
on this interval. In particular its proof gives, at physical rows,
\[
 \begin{split}
 |u-V_m|&\le Ch\Lambda_N
                  e^{-N I_{m/N}((\pi-t_j)/(2\pi))},\\
 |(u-V_m)'|&\le C\Lambda_N(|t_j|+\sqrt h)
                  e^{-N I_{m/N}((\pi-t_j)/(2\pi))},\\
 |u|+|V_m|+|V_m'|&\le Ch\Lambda_N,\qquad
                  \Lambda_N=(1+\log N)^2 .
 \end{split}
 \tag{11}
\]
Primes here are actual angular or \(x\) derivatives, with their
fixed conversion factor. The derivative is taken with \(m\)
held fixed at the row in question.

For precision about this uniform use: the raw last summand is
\(h^{2z+2}A_z(x,m/N)e^{-NI_{m/N}(x)}\), with bounded spatial
amplitude and at most one coalescence logarithm. The actual
anchor has norm \(O(h(1+\log N))\). Thus the residual and its
first derivative have the same \(h^2\Lambda_N\) bounds as in
the direct-cap theorem. The regular forcing coefficient is
\(O(|t|/h)\). The action has
\(-\partial_t I_v((\pi-t)/(2\pi))\asymp t\), uniformly in
\(v\in[\delta_0,1/4]\). Its discrete Gaussian sums therefore
give (11), including the independent normal fixed by
differentiated reflection. No constants worsen as the number
of blocks grows.

At each row \(m_j/N=\delta(t_j)+O(h)\), and \(I_v\) has its
maximum at \(v=\delta(t_j)\), with bounded second derivative
there. Hence the cutoff rounding costs \(O(h^2)\) in the action.
The actual factorial coordinate differs from the centered
coordinate in (10) by \(O(h)\); its exponential cost is bounded,
since \(I_v'=O(|t|+h)\). The original phases obey
\[
 \psi(t,0)-J_*(t)
       =\mathcal I_2-\frac{t^4}{64\pi}+O(t^6)
       \le \mathcal I_2-ct^4
                         \quad(|t|\le T_0).
 \tag{12}
\]
This follows with its additive constant from
\(\psi'=-\pi^{-1}\operatorname{asinh}(\tan(t/2))\) and
\(J_*'=-\pi^{-1}\operatorname{asinh}(\sin(t/2))\).

Apply (11) factorwise before the full product rule, and use the
direct-cap theorem's exact real outgoing bounds
\[
 |L_N(t)|\le Ch^{3/2}e^{N\psi(t,0)},\quad
 |L_N'(t)|\le Ch^{3/2}(1+|t|/h)e^{N\psi(t,0)}.
 \tag{13}
\]
The original mirrored trace is
\(-\eta/(2\pi)\sum_j\partial_x[\sin t\,f](x_j)\).
Consequently the absolute sum of its actual-minus-baseline
terms is bounded by
\[
 C\Lambda_N^r h^{r+1/2}e^{N\mathcal I_2}
       \sum_{j\in\mathcal C_N}
          (h+t_j^2+|t_j|\sqrt h)e^{-ct_j^4/h}
 \le C\Lambda_N^r h^{r+1/4}e^{N\mathcal I_2}.
 \tag{14}
\]
The last inequality is a mesh comparison with the integrals of
\(1,t,t^2\) against \(e^{-ct^4/h}\), including the endpoint
terms. In (14) the chosen baseline can vary between blocks;
only its fixed-cutoff physical jets have been used.

## 3. Exact neighboring jump and the anchor term

For one factor and neighboring cutoffs, the raw difference
\(H_{m+1}-H_m\) is exactly one last summand in each mode,
or its parameter divided difference in the coalesced column.
Uniformly on a fixed tall fold rectangle,
\[
 |H_{m+1}(x)-H_m(x)|
       \le Ch(1+\log N)
                     e^{-N\Re I_{(m+1)/N}(x)} .
 \tag{15}
\]
At the physical fold anchor its divided-color frame difference
has the sharper explicit size
\[
 \|\mathcal F_{m+1}(x_{j_*})-\mathcal F_m(x_{j_*})\|
       \le C(1+\log N)e^{-N I_{(m+1)/N}(1/2)}.
 \tag{16}
\]
Indeed these last summands descend holomorphically to \(C\)
through the fold. On a spectral disk of radius \(ch\) around
\(-2\), the two angular lifts are \(O(\sqrt h)\) from the fold.
The change in \(NI_v\) is bounded there, so (15) gives
\(Ch(1+\log N)e^{-NI_v(1/2)}\). Cauchy in \(C\) costs \(h^{-1}\).
Both colors in the anchor differ from \(-2\) by \(O(h^2)\);
their divided difference is bounded by this derivative. This
proves (16) without division by their small separation.

The actual state used in (6) has norm \(O(h(1+\log N))\), and
the frames and their inverses are bounded. The inverse identity
therefore gives
\[
 |a_{m+1}-a_m|
       \le Ch\Lambda_Ne^{-N I_{(m+1)/N}(1/2)}.
 \tag{17}
\]
Thus the actual normalized scalar jump splits exactly as
\[
 V_{m+1}-V_m=(H_{m+1}-H_m)a_m
                         +H_{m+1}(a_{m+1}-a_m).
 \tag{18}
\]
The first term is bounded by \(Ch^2\Lambda_N\) times the
spatial exponential in (15); the second is bounded by
\(Ch\Lambda_N\) times the anchor exponential in (17).
For \(r\) factors the product jump has the corresponding bound
\[
 C\Lambda_N^r\left[
 h^{r+1}e^{-N\Re I_v(x)}
              +h^r e^{-N I_v(1/2)}\right],
 \tag{19}
\]
where \(v=(m+1)/N\). This uses the bound \(Ch(1+\log N)\)
for each other baseline on the same tall rectangle.

At the midpoint seam angle \(t_s>0\), this cutoff is within
\(Ch\) of \(\delta(t_s)\). Hence
\[
 \psi(t_s,0)-I_v((\pi-t_s)/(2\pi))
                         \le\mathcal I_2-ct_s^4+Ch^2,
 \tag{20}
\]
\[
 \psi(t_s,0)-I_v(1/2)
                         \le\mathcal I_2-ct_s^2+Ch^2 .
 \tag{21}
\]
For (21), use
\(\delta(t)=1/4-t^2/(8\pi)+O(t^4)\) and
\(I_v(1/2)=\mathcal I_2-2\pi(v-1/4)^2+O((v-1/4)^3)\),
together with \(\psi(t,0)=2\mathcal I_2-t^2/(4\pi)+O(t^4)\).
The \(O(h)\) source-coordinate shifts cost only bounded
exponential factors. In particular (17) is not being assigned
the incorrect exact saving \(\mathcal I_2\).

## 4. Vertical integration and the number of seams

There are fixed small \(H_0,T_0>0\) for which the outgoing
kernel has the uniform complex extension
\[
 |L_N(t-i\sigma H)|
  \le Ch^{3/2}\exp\{N[\psi(t,0)+C H^2]\},
 \quad |t|\le T_0,\quad 0\le H\le H_0,\quad \sigma=\pm1.
 \tag{22}
\]
To verify this, use the central midpoint product expansion
from the direct-cap proof on its fixed complex neighborhood.
Its real logarithmic phase at height \(H\) differs from that
at \(H=0\) by \(O(H^2)\): the linear term is imaginary.
The negative second derivative in the real summation variable
persists. Thus the same \(N^{-2}\) central summand and
\(O(\sqrt N)\) Gaussian count apply. The tail logarithmic
integrals depend continuously on \(t,H\), including their
integrable zero singularities. Their upper mesh estimate is
uniform also for a zero displaced off the real axis, by the
same cell split. For small fixed \(H_0,T_0\), their strict
central gap persists, and absorbs their polynomial factors.
This proves (22) with its displayed prefactor.
Enlarge \(C\) if necessary so that the ordinary analytic Taylor
bound \(\Re\psi(t-i\sigma H,0)\le\psi(t,0)+CH^2\) also holds.

At a midpoint vertical the exact sampling kernel satisfies
\[
 |D_h|=(\pi/h)^2\operatorname{sech}^2(H/(2h))
                                      \le 4\pi^2h^{-2}e^{-H/h}.
 \tag{23}
\]
The signed crossing contributes
\(\exp[\sigma nt_sH/(2\pi h)]\), and
\(|\sin(t_s-i\sigma H)|\le C(t_s+H)\).
Also \(\Re I_v(X+iY)\ge I_v(X)\).
Choose \(T_0,H_0\) small enough that
\[
 -H+\frac{\sigma n t_sH}{2\pi}+CH^2\le-cH
                       \quad(0\le H\le H_0).
 \tag{24}
\]
Combining (19)--(24), and integrating
\((t_s+H)e^{-cH/h}\), bounds the low part of each seam by
\[
 C\Lambda_N^r e^{N\mathcal I_2}
 \left[
 h^{r+3/2}(t_s+h)e^{-ct_s^4/h}
       +h^{r+1/2}(t_s+h)e^{-ct_s^2/h}
 \right].
 \tag{25}
\]
This uses the effective height \(h\), not a fixed-height upper
bound for the integral.

The remaining heights \(H_0\le H\le H_2\) have a uniform
strict action gap. The actual half-plane low-kernel bound is
a polynomial times \(e^{N\Re\psi(t-i\sigma H,0)}\).
The phase
\[
 \mathcal P_{n,\sigma}(t,H)=
 \Re\psi(t-i\sigma H,0)+(\sigma nt/(2\pi)-1)H
 \tag{26}
\]
is convex in \(H\). At \(H_0\), (22)--(24) give a strict gap
after either saving in (19); at \(H_2\), calibration gives
\(\mathcal P_{n,\sigma}\le\mathcal I_2\), and both savings
are bounded below by a fixed positive constant. Convexity
proves the claim on the intervening interval. Polynomial
factors and the \(O(N)\) seams do not remove this gap.

It remains to count (25) accurately. A seam lies within \(Ch\)
of a threshold \(N\delta(t)\in\mathbb Z\). Since
\(1/4-\delta(t)\asymp t^2\), successive thresholds can be
indexed by \(k\ge0\) so that
\[
 t_s^2\le Ch(k+1),\qquad
 t_s^2\ge ch(k-1)_+ .
 \tag{27}
\]
There is at most one positive seam per threshold; the finite
initial ambiguity and the fractional part of \(N/4\) are
absorbed in the two shifts in (27). Midpoint displacement is
at most \(Ch\) and preserves these bounds. Therefore
\[
 \sum_s(t_s+h)e^{-ct_s^4/h}\le Ch^{-1/4},\qquad
 \sum_s(t_s+h)e^{-ct_s^2/h}\le C\sqrt h .
 \tag{28}
\]
For example the respective bounds reduce to
\(\sqrt h\sum_{k\ge0}\sqrt{k+1}e^{-c h(k-1)_+^2}\)
and \(\sqrt h\sum_{k\ge0}\sqrt{k+1}e^{-c(k-1)_+}\).
Thus the aggregate of all internal vertical jumps is
\[
 O\!\left(\Lambda_N^r
             [h^{r+5/4}+h^{r+1}]e^{N\mathcal I_2}\right)
             +O(e^{N(\mathcal I_2-c)}).
 \tag{29}
\]
The reflected seams obey the identical bound.

## 5. Exact assembly, fold multiplicity, and exterior sides

For each block use the ordinary holomorphic baseline, not a
cardinal repair. The double-pole residue of (8) gives
\[
 -\frac{\eta}{2\pi}\sum_{j\ {\rm in\ block}}g_m'(x_j)
       =-\frac{\eta}{4\pi^2i}\oint_{\partial{\rm block}}D_hg_m\,dx .
 \tag{30}
\]
Pair reflected blocks, retaining the half normalization in
(30). The central block is already mirrored. Thus every
double spectral root is counted once. At odd levels its
central angular derivative contributes precisely the original
simple value; no additional spectral normal is imposed.
All baselines descend through the fold, so no extra central
side is introduced.

On every internal midpoint side, the two oriented terms in
(30) combine into the actual difference (18), with the product
rule (19). They are exactly the currents bounded in (29).
At heights \(H_2\), the baseline horizontal phase has a strict
\(\mathcal I_2\) gap on the small fixed fold interval: the
calibrated horizontal has its unique maximum at the positive
real part of the two-power saddle, separated from this interval.
Both halves and their reflections obey this gap. The total
horizontal length is bounded independently of the block count.
Their polynomial factors therefore remain exponentially small.

The complete high outgoing sector has polynomial real norm
and fixed first normals, including the odd middle term.
Its original restricted trace with the actual microscopic
product and crossing is polynomial, as proved in the compact
source theorem. We keep this entire source in the error term;
no off-grid high-kernel replacement is made.

Now add the exact physical errors (14), the actual internal
currents (29), the horizontal bounds, and this retained high
sector. The only remaining sides are those defining
\(\mathcal V_{\rm out,N}\). The largest error is (14), proving
(9). At the fixed exterior cuts, the same-anchor compact
patch comparison has a strict real gap by (12), and a strict
top gap by calibration; its vertical convexity estimate
joins these sides with no unaccounted current.

The proof controls every growing internal block count by
actual finite last-summand and anchor identities. It makes
no claim that a written unit exponential is a frequency gap,
or that an inner source estimate survives an arbitrary
physical turn.

## 6. Direct sources

* [Actual shrinking-cap trace error](research_critical_fold_actual_trace_error.md),
  SHA256 08a6a612536931629567733d63b2161eca52000f3bea0973c79528c023677bb8.
* [Uniform full-normal fold cap](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Compact interface and seams](research_sharp_endpoint_compact_interface_and_seams.md),
  SHA256 178e49b99b51fe767bc29ceadafb00159c179cd42f9ba5469921f64a6eabdde9.

The new steps are the optimized original physical-jet sum, the
separate raw and anchor prefactors of the exact adjacent-cutoff
jump, and their aggregate midpoint-vertical estimates.
