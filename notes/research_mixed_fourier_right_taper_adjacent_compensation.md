# The exact adjacent compensation on the incoming Fourier taper

Research deduction, 7 November 2026. The completed finite Fourier-cap
envelope combines with its adjacent ordinary factor through the original
complex stationary equation. The resulting estimate retains both
branches of the cap envelope, the protected coherent extension and the
relative pinning fee.

There is a concrete limitation to this combination. At every ordinary
incoming type-four reference, the cap's imaginary incoming marginal is
greater than \(1/6\). Its present envelope consequently exceeds its
complex tangent at the real taper endpoint by more than \(1/7000\).
Even where the older two-taper ordinary theorem is eligible, inserting
only its published quadratic loss does not pay this excess. This is a
limitation of those upper estimates, not a lower bound or an obstruction
for the actual product. No numerical evaluation is used.

## 1. The adjacent literal factors and their reference equation

Use an actual Fourier-ended word from
[the boundary-window source](research_mixed_fourier_ended_boundary_windows.md).
Write \(n=m-1\) for the last retained coordinate, assume \(n\ge2\),
and put
\[
 a_*=r_n,\quad v_*=r_{n-1},\quad
 \eta=\epsilon_n,\quad\lambda=\epsilon_{n-1}.
 \tag{1}
\]
In the finite boundary problem the protected cut is strictly before
these coordinates. The coordinate \(a_*\) and the private index \(u_*\)
of vertex \(n\) are the outputs of the same original ordinary map.
Their correlation and original logarithmic lifts are retained.

Let \(r=e^{-2\pi i/N}\), \(P_k=(r;r)_k\), \(p_k(Z)=(rZ;r)_k\).
For \(V=e^{-2\pi iv}\), \(A=e^{-2\pi ia}\), the literal factor is
\[
 C_{\eta,N}(V,A)=\sum_{k=0}^{N-1}
            \frac{V^{-k}p_k(V)p_k(A)}{P_k^{2+\eta}}.
 \tag{2}
\]
This is the complete Laurent polynomial in
[conditional composition](research_mixed_conditional_torus_composition.md),
not the maximum of selected physical-row rates. The last pair has
allocated modulus
\[
 \mathcal P_N(v,a)=
 |C_{\eta,N}(V,A)|\,|V_N^{\rm F}(x_0,A)|
                 |d_N(V)|^{\lambda/2}|d_N(A)|^\eta .
 \tag{3}
\]
Thus one half of the last weight belongs to each adjacent factor.
No weight is divided out, including at its zeros.

The original allocated ordinary phase and the cap phase are
\[
\begin{split}
 \phi(v,a)&=\operatorname{crit}_u
  \{g(u+v)+g(u+a)-(2+\eta)g(u)+2\pi ivu\}\\
 &\hspace{12mm}-(1+\lambda/2)g(v)-(1+\eta/2)g(a),\\
 \Pi_\eta(a)&=\operatorname{crit}_{s,z}
 \{g(s+a)+g(s+z)-3g(s)-g(a)-g(z)
                      +2\pi ias+\ell_z(x_0)\}-\eta g(a)/2 .
\end{split}
 \tag{4}
\]
Their values at the reference, including all constants, are those of
the original action. Only their reference germs are needed below;
equation (4) does not define a new conditional packet at a tapered
target. Set
\[
 P=\Pi_\eta'(a_*),\qquad p=\Re P,\qquad
 P_v=\partial_v\phi(v_*,a_*),\qquad M_\eta=\Re\Pi_\eta(a_*).
 \tag{5}
\]
The original retained-coordinate equation is
\[
 g'(u_*+a_*)+g'(s_*+a_*)-(2+\eta)g'(a_*)+2\pi is_*=0.
 \tag{6}
\]
Consequently
\[
\begin{split}
 \partial_a\phi(v_*,a_*)&=-P,\\
 P&=(1+\eta/2)g'(a_*)-g'(u_*+a_*),\\
 p&=(1+\eta/2)\log|1-e^{-2\pi ia_*}|
                    -\log|1-e^{-2\pi i(u_*+a_*)}|.
\end{split}
 \tag{7}
\]
This uses the actual adjacent index \(u_*\); it does not replace it
by an independent point in a containing rectangle.

## 2. The complete cap envelope and the exact paired remainder

Put \(b=9/20\), \(\kappa=1/2500000\), \(a_R=\Re a_*\),
\(c=\Im a_*\le0\), and
\[
 a=x+iH,\quad b\le x\le1/2,\quad c\le H\le0,\qquad
 \chi_0=1989/4489,\quad\chi_1=171/196.
 \tag{8}
\]
The actual unselected terminal taper is
\(H=400(1/2-x)^2c\) whenever the preceding left-cutoff factor is one.
The formulas below also retain every height in (8). The preceding
coordinate \(v\) may have its actual admissible hybrid height; no
ordinary-source bound at that height is assumed.

The complete finite cap theorem, equation (24) of
[small rows and full assembly](research_mixed_fourier_right_taper_small_rows.md),
has rate
\[
\begin{split}
 B_b&=M_\eta+p(b-a_R)-\kappa(b-a_R)^2,\\
 B_{\rm ext}(x)&=M_\eta+p(x-a_R)-\kappa\chi_\eta(x-a_R)^2,\\
 \gamma_\eta(x,H)&=\pi(1-\eta/2)(1/2-x)(H-c),\\
 \mathfrak B_\eta(x,H)&=\max\{B_b,B_{\rm ext}(x)\}
                                      -\gamma_\eta(x,H).
\end{split}
 \tag{9}
\]
It bounds the entire original finite cap with its incoming halfweight,
at both parities, with a uniform polynomial and any fixed rate
tolerance.

Define the exact ordinary-source defect, with \(\log0=-\infty\), by
\[
\begin{split}
 \Delta_{{\rm ord},N}(v,a)
 ={}&\frac1N\log\{
       |C_{\eta,N}(V,A)|\,|d_N(V)|^{\lambda/2}
                              |d_N(A)|^{\eta/2}\}\\
 &-\Re\{\phi(v_*,a_*)+P_v(v-v_*)-P(a-a_*)\}.
\end{split}
 \tag{10}
\]
The definition uses the finite source itself, so it is valid even
where no moving conditional saddle theorem is available.

**Proposition 1.** For every fixed \(\tau>0\), uniformly on the cap
targets (8) and compact admissible neighboring targets,
\[
\begin{split}
 \frac1N\log\mathcal P_N(v,a)
 \le{}&\Re\{\phi(v_*,a_*)+\Pi_\eta(a_*)+P_v(v-v_*)\}\\
 &+\Delta_{{\rm ord},N}(v,a)+\mathcal R_\eta(x,H)
                         +\tau+O_\tau(\log N/N),
\end{split}
 \tag{11}
\]
where the exact remaining cap term is
\[
\boxed{\quad
 \mathcal R_\eta=
 \Im P(H-c)-\gamma_\eta(x,H)
 +\max\{-p(x-b)-\kappa(b-a_R)^2,\,
                       -\kappa\chi_\eta(x-a_R)^2\}.
 \quad}
 \tag{12}
\]

*Proof.* Multiply the complete cap inequality by the other half
allocation in (10). The two full complex \(a\)-tangents cancel by
(7). Subtracting the cap tangent from (9) gives (12) exactly.
Both maxima and the full integer allocation in (3) remain.
\(\square\)

Stationarity cancels the two complex tangent planes once. It does
not cancel the first term of (12) a second time. In particular a
bound for the ordinary source relative to its own full tangent must
still pay this displayed term.

One possible branch simplification has an exact scalar formulation.
Set \(d=b-a_R>0\), \(L=1/2-b=1/20\). Then
\[
 B_{\rm ext}(x)\ge B_b\quad\hbox{for every }x\in[b,1/2]
 \quad\Longleftrightarrow\quad
 p\ge\frac{\kappa}{L}\{\chi_\eta(d+L)^2-d^2\}.
 \tag{13}
\]
Indeed, after writing \(w=x-b>0\), the threshold is
\(\kappa[\chi_\eta w+2\chi_\eta d-(1-\chi_\eta)d^2/w]\),
which increases with \(w\). At \(w=0\) the difference is already
positive. Equation (7) is the original coupled expression for the
left side of (13); no sign for it is inferred from independent
containing boxes. Both branches in (12) are retained here.

## 3. The protected extension and the remaining boundary inequality

Use the safe cut \(q_c\), the last pin \(\ell\), and fee coordinate
\(j_f\) of
[the shallow right-boundary theorem](research_mixed_fourier_right_boundary_shallow_taper.md).
In particular the protected strip through \(q_c+1\) is unchanged and
the coherent extension is the original one. For each extension edge
let \(\delta_j^{\rm coh}\) be its original phase minus its full complex
reference tangent, taking real parts. For each literal ordinary edge
before the last one, let \(\delta_{j,N}^{\rm src}\) be the analogue of
(10), with that edge's own two halfweights. Define
\[
 \Xi_N=
 \sum_{j=\ell+1}^{q_c}\delta_j^{\rm coh}
 +\sum_{j=q_c+1}^{n-1}\delta_{j,N}^{\rm src}
                  +a_d(x_{j_f}-\Re r_{j_f})^2,
 \qquad a_d<1/1296.
 \tag{14}
\]
This retains any admissible hybrid heights in the literal prefix.
It is an exact prefix excess, not an assertion that its factors
have a favorable sign at arbitrary targets.

The cancellation identity (4) of the shallow-boundary note and all
original internal stationary equations give
\[
 \mathcal C_{R,N}^{\rm F}
 \le \Xi_N+\Delta_{{\rm ord},N}(v,a)
              +\mathcal R_\eta(x,H)+\tau+O_\tau(\log N/N).
 \tag{15}
\]
There is no remaining cut tangent: \(z_\ell=r_\ell\), the protected
closing terms cancel exactly, and the tangent in \(v\) in (11)
cancels the preceding original edge's tangent.

If all preceding free targets through \(v=z_{n-1}\) are on their
original-height plateaux, the complete ordinary planes apply
directly. The safe coherent fee edge contributes \(1/10\) at
\(j_f\), so \(1/10-a_d>\kappa\) pays the same fee as before.
Retaining the other edge losses yields
\[
 \Xi_N\le-\kappa\left[
       2\sum_{j=\ell+1}^{n-2}(x_j-\Re r_j)^2
                  +(\Re v-\Re v_*)^2\right]
                    +\tau+O_\tau(\log N/N).
 \tag{16}
\]
This is a source statement: the literal prefix uses the complete
ordinary theorem, not a central-row replacement.

Thus, on this plateau-prefix sector, the precise remaining last-pair
comparison is a uniform bound of the form
\[
 \Delta_{{\rm ord},N}(v,a)+\Im P(H-c)-\gamma_\eta(x,H)
 +\max\{-p(x-b)-\kappa(b-a_R)^2,\,
                    -\kappa\chi_\eta(x-a_R)^2\}
 \le \kappa(\Re v-\Re v_*)^2-\delta+o(1),
 \tag{17}
\]
with both branches, \(H=400(1/2-x)^2c\), and a fixed
\(\delta>0\) on a closed nonshallow sector. For a neighboring
hybrid prefix, the exact condition is instead (15) with its
original \(\Xi_N\). The completed shallow theorem already pays
a fixed initial neighborhood; it is not iterated to infer (17).

## 4. A positive height marginal and a limitation of the published bounds

**Lemma 2.** At every actual ordinary type-four vertex immediately
before the Fourier cap,
\[
                           \Im P_1>1/6.
 \tag{18}
\]

*Proof.* Both \(a_*\) and \(u_*\) belong to the ordinary type-four
image \(O_4\). By
[the actual reference domains](research_mixed_actual_last_row_reference_domains.md),
their real parts are in \([.24,.36]\), their heights are negative,
and \(\Im a_*\ge-.108\). Put \(A_*=e^{-2\pi ia_*}\).
Its radius is greater than \(1/2\): indeed
\[
 -2\pi\Im a_*\le27\pi/125<594/875<56/81<\log2,
 \tag{19}
\]
where the last inequality is the first two positive terms of
\(\log2=2\operatorname{arctanh}(1/3)\). Also
\(\sin(2\pi\Re a_*)>\sqrt2/2>2/3\), while
\(\Re(1-A_*)<2\) and is positive. The original argument therefore obeys
\[
 \arg(1-A_*)>\arctan(1/6)
                       >1/6-(1/6)^3/3=107/648.
 \tag{20}
\]
For the incident sum, its real part is at least .48 and less than
one, and its height is negative. If its real part is below \(1/2\),
the argument is at most its unit-radius value
\(\pi(1/2-\Re(u_*+a_*))\le\pi/50\). If it is at least \(1/2\),
the argument is nonpositive. These are the original \(g'\) lifts,
since both arguments lie in \(0<\Re z<1\) with negative height.
Equation (7) now gives
\[
 \Im P_1>\frac32\frac{107}{648}-\frac{\pi}{50}
       >\frac{107}{432}-\frac{11}{175}>\frac16 .
 \tag{21}
\]
\(\square\)

At the actual taper endpoint \(x=1/2,H=0\), the reset credit
\(\gamma_1\) vanishes. Since \(c\le-1/1000\) and
\((1/2-a_R)^2\le(13/50)^2<1/10\), (12), (18) imply
\[
 \mathcal R_1(1/2,0)>
                  \frac1{6000}-\frac{\kappa}{10}>
                  \frac1{7000}.
 \tag{22}
\]
This is an inequality for the completed cap envelope itself.
It does not evaluate or lower-bound the finite cap.

There is a sharper limitation even on the narrower domain of the
published ordinary
[two-taper theorem](research_mixed_unselected_right_taper_products.md).
That theorem supplies the whole-source defect upper estimate
\[
 \Delta_{{\rm ord},N}
 \le-c_T\{(\Re v-\Re v_*)^2+(x-a_R)^2\}
                     +\tau+O_\tau(\log N/N),
 \qquad c_T=181/24200,
 \tag{23}
\]
when all its reference and target hypotheses hold. For an eligible
type-four reference, \(.27<a_R<.33\) and \(c<-.02\).
At \(v=v_*,x=1/2,H=0\), the numerical expression obtained by
substituting just (23) into (11) is strictly positive:
\[
\begin{split}
 \mathcal R_1(1/2,0)-c_T(1/2-a_R)^2
 &>\frac1{300}-(c_T+\kappa)(1/2-a_R)^2\\
 &>\frac1{300}-\frac1{1440}
   =\frac{19}{7200}>\frac1{400}.
\end{split}
 \tag{24}
\]
Here \(c_T+\kappa<1/90\) and
\((1/2-a_R)^2<1/16\). Thus these two published upper estimates
alone do not prove the desired sign, even if the ordinary theorem's
domain is available. Equation (24) is not a lower estimate for the
true defect in (10), nor does it assert that every point of the older
reference family occurs in a Fourier-ended word.

For general actual endpoint references there is a further domain
distinction. The broad complete ordinary plateau theorem covers the
actual typed products at their reference heights. The older
two-taper packet and Hessian proof use type-three heights
\([-.03,.02]\) and type-four heights \([-.057,0]\), with their
tighter reference rectangles. The Fourier-ended window theorem
does not put every last adjacent pair into those rectangles.
Consequently neither that packet nor its quadratic estimate can
be silently promoted to the full terminal hybrid family.

The remaining task is therefore the calibrated coupled estimate
(17), or an estimate of the literal product (3) that improves the
present separate cap envelope. Protected pinning fees and the
original prefix excess are already explicit in (14)--(16).
Selected targets, moved protected cuts and ordinary closing
observations are not covered by this deduction.
