# The remaining negative contour and a sufficient source bound

Private research deduction, 9 November 2026. Reflection joins the
remaining upper connector to the negative horizontal segment. Their
sum is one integral entirely in the lower half-plane. Its phase has
a useful monotonicity in height. Together with the already proved
positive-contour estimate, this reduces the remaining outer asymptotic
to a specific upper bound for the inner source.

The upper bound stated below is a hypothesis, not a proved theorem.
In particular this note does not assert the full outer asymptotic
unconditionally. No numerical evaluation is used.

## 1. Exact reflection of the remaining terms

Keep every definition and normalization of
[the positive taper theorem](research_mixed_next_outer_positive_taper_and_midpoint_cap.md).
In particular, fix \(0<\delta_1\le1/2\) and use the actual integer
frequencies \(\delta=1/2-k/N\in[\delta_1,1/2]\). The exact current is
\[
 \mathcal I_{N,k}(\gamma)
  =\frac{\chi_N C_{N,3}N}{4\pi}\int_\gamma g_{N,k}(u)\,du,
 \qquad
 g_{N,k}(u)=H_N(u)f_{N,\delta}(u)(1+e^{-2iku}),
 \tag{1}
\]
where
\[
 H_N(u)=\frac1{1-\eta_Ne^{-iNu}},\qquad
 f_{N,\sigma}(u)=a_N(u)Q_N^{\rm sh}(u)
          e^{N(3iu^2/(4\pi)-i\sigma u)},\qquad
 \eta_N=(-1)^{N-1}.
 \tag{2}
\]
The parity amplitude \(a_N\), unit scalars \(\chi_N,C_{N,3}\),
and shortened source \(Q_N^{\rm sh}\) are unchanged.

Because \(Q_N^{\rm sh}(u)\) is an ordinary polynomial in
\(-2\cos u\), it is even. The original parity amplitudes give
\(a_N(-u)=\eta_N a_N(u)\). Consequently
\[
 f_{N,\sigma}(-u)=\eta_N f_{N,-\sigma}(u),\qquad
 H_N(-u)=1-H_N(u)=-\eta_Ne^{-iNu}H_N(u).
 \tag{3}
\]
The exact frequency relation \(2k/N=1-2\delta\) also gives
\[
 g_{N,k}(u)=H_N(u)\{f_{N,\delta}(u)+f_{N,1-\delta}(u)\}.
 \tag{4}
\]
Equations (3)--(4) imply the meromorphic identity
\[
                         g_{N,k}(-u)=-g_{N,k}(u).
 \tag{5}
\]
This identity includes the complete sampling denominator and both
reflected charges. It holds also when \(k=0\).

The remaining upper segment from \(T_N+i/N\) to \(T_N+iK_\delta\)
therefore satisfies
\[
 \mathcal I_{N,k}([T_N+i/N,T_N+iK_\delta])
 =\mathcal I_{N,k}([-T_N-i/N,-T_N-iK_\delta]).
 \tag{6}
\]
The minus sign in (5) cancels the sign of \(du=-dv\); the
right-hand path is oriented downwards.

Joining it to the negative bottom segment gives a single current
\[
 \mathcal J_{N,k}=\mathcal I_{N,k}(\gamma_{\rm neg}),\qquad
 \gamma_{\rm neg}:
 -T_N-i/N\longrightarrow -T_N-iK_\delta
                         \longrightarrow-\epsilon-iK_\delta.
 \tag{7}
\]
Here \(\epsilon>0\) is the fixed central width in the earlier
decomposition. The positive taper theorem now reads
\[
 \mathcal O_{N,k}=G_{N,k}+\mathcal J_{N,k}
                         +O(e^{N(\Gamma(\delta)-\eta_0)})
 \tag{8}
\]
for some fixed \(\eta_0>0\). Equation (7) alone does not bound
the current.

## 2. The phase decreases downwards on the negative side

Use the original holomorphic functions
\[
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\},\qquad
 S'=-f/\pi,\qquad
 V_\delta(x,h)=\Re\{S(x-ih)+3i(x-ih)^2/(4\pi)-i\delta(x-ih)\}.
 \tag{9}
\]
The selected cubic root depends on \(\cos(u/2)\). Its uniqueness
and continuation from zero imply \(c(-u)=c(u)\) on the original
symmetric rectangle. Thus \(f\) is odd and \(S\) is even there,
with the same additive constant as before.

The [two-sided derivative theorem](research_mixed_next_charged_curve_two_sided_descent.md)
gives \(|f'(u)|<3/2\) for \(|\Re u|\le4/3\),
\(|\Im u|\le1/2\). Since \(f(0)=0\), integration first along
the real axis and then upwards shows
\[
 \Im f(a+ih)<\frac32(a+h)
       \qquad (a,h\ge0,\ a\le4/3,\ h\le1/2,\ a+h>0).
 \tag{10}
\]
Oddness and the exact outer charge give
\[
 \partial_h V_\delta(-a,h)
 =-\frac{3a}{2\pi}-\delta+\frac{\Im f(a+ih)}{\pi}
 <-\delta+\frac{3h}{2\pi}.
 \tag{11}
\]
The proved selected-depth bound \(K_\delta<\pi\delta/3\)
therefore yields
\[
       \partial_h V_\delta(-a,h)\le-\delta/2
       \qquad(0\le a\le4/3,\ 0\le h\le K_\delta).
 \tag{12}
\]
At \(a=h=0\) the derivative is exactly \(-\delta\).
This proves (12) also at that endpoint.

Two further phase bounds will be used. Put \(b=8/7\),
\(\beta_-=\min\beta_\delta>0\), \(\beta_+=\max\beta_\delta<b\),
and
\[
                  g=\frac{(b-\beta_+)^2}{100\pi}>0.
 \tag{13}
\]
The positive taper proof, equation (17), gives
\[
                s(4/3):=\Re S(4/3)\le\Gamma(\delta)-g.
 \tag{14}
\]
Its height-minimizing curve has already reached zero before \(4/3\).
The real function \(s(a)\) decreases for \(4/3\le a\le\pi/2\).
Finally, horizontal descent at the selected height gives
\[
 V_\delta(-a,K_\delta)
 \le\Gamma(\delta)-\frac{(a+\beta_\delta)^2}{100\pi}
 \le\Gamma(\delta)-\frac{\beta_-^2}{100\pi}
                          \qquad(0\le a\le4/3).
 \tag{15}
\]
These are proved phase inequalities, without a new source estimate.

## 3. The source estimate that would suffice

The following single upper bound is sufficient:

> For each fixed \(\tau>0\), there is a constant \(C_\tau\)
> such that the entire finite source obeys
> \[
> |Q_N^{\rm sh}(a+ih)|
> \le C_\tau
> e^{N\{\max(\Re S(a+ih),17/10)+\tau\}},
> \quad 0\le a\le4/3,\quad0\le h\le2/5,
> \tag{H}
> \]
> uniformly in \(N\) and both parities.

This hypothesis asks for an absolute upper bound. It does not ask
for an upper-half-plane relative asymptotic or a nonzero coefficient
there. An estimate for a single edge of the inner trace does not
establish (H).

**Conditional proposition.** If (H) holds for the original source,
then for every fixed \(\delta_1>0\),
\[
 \mathcal O_{N,k}
     =G_{N,k}+O(e^{N\{\Gamma(\delta)-\eta\}})
 \tag{16}
\]
with a fixed \(\eta>0\), uniformly at the frequencies above.
In particular the whole observation has the nonzero leading
coefficient given in the local Gaussian theorem.

*Proof.* Put \(a_{\rm R}=4/3\). In the open lower half-plane, deform (7)
to the three segments
\[
 \begin{split}
 -T_N-i/N&\longrightarrow-a_{\rm R}-i/N,\\
 -a_{\rm R}-i/N&\longrightarrow-a_{\rm R}-iK_\delta,\\
 -a_{\rm R}-iK_\delta&\longrightarrow-\epsilon-iK_\delta.
 \end{split}
 \tag{17}
\]
For large \(N\), \(1/N<K_\delta\). The endpoints are unchanged,
and no real sampling pole is crossed.

On the second segment the geometric rate is at most
\(s(a_{\rm R})\le\Gamma-g\), by (12)--(14). On the third it is
at most \(\Gamma-\beta_-^2/(100\pi)\), by (15).
Evenness identifies their actual sources with \(Q_N^{\rm sh}(a+ih)\)
and their actions with \(S(a+ih)\), so (H) is applicable.
The additional constant sector in (H) can only decrease after the
outer crossing and charge are attached, since its added real part is
\[
                    -h\left(\frac{3a}{2\pi}+\delta\right)\le0.
 \tag{18}
\]
The [complete-action lower bound](research_inner_three_complete_action_lower_bound.md)
and the proved charged action loss imply
\[
 \Gamma(\delta)>\frac{46}{25}-\frac{34}{275}
      =\frac{472}{275},\qquad
              \frac{472}{275}-\frac{17}{10}=\frac9{550}.
 \tag{19}
\]
Thus both sectors have a fixed gap on those two segments.

For the first segment in (17), no upper-half-plane source
hypothesis is necessary. Choose a fixed real interval
\([a_-,a_+]\subset(8/7,\pi/2)\) whose interior contains
\([4/3,3/2]\), with \(a_-\) sufficiently close to \(4/3\).
Continuity of \(s\), (14), and its real monotonicity give
\[
            s(a)\le\Gamma(\delta)-3g/4
                        \quad(a_-\le a\le a_+).
 \tag{20}
\]
The already proved real-continuum source bound has rate
\(\max(s(a),33/20)\) on this interval. By (19), both terms
are uniformly below \(\Gamma\).

Here are the details of continuation to height \(1/N\).
Set \(\rho=\min(g/2,9/550)>0\) and take the real-source
tolerance to be \(\rho/8\). The source on the spectral
interval \([-2\cos a_-,-2\cos a_+]\) is then at most
\(C e^{N(\Gamma-7\rho/8)}\). Its ordinary degree is
\(U<N/2\). On a filled Chebyshev ellipse of height
\(\mu=\rho/8\), its modulus is at most \(2U+1\) times
this norm times \(e^{U\mu}\). The additional exponential
cost is at most \(N\rho/16\).

The spectral images of \(a+i/N\), \(4/3\le a\le T_N\),
lie in that fixed ellipse for all sufficiently large \(N\):
their limiting real interval is strictly interior to the chosen
spectral interval. Evenness therefore bounds the source on the
entire first segment in (17), with a fixed gap below \(\Gamma\).
This uses a continuum bound, not interpolation from sampled values.
The outer crossing and charge in (18) do not increase its rate.

All three segments have \(Nh\ge1\). Hence
\[
 |H_N(u)|\le(1-e^{-1})^{-1},\qquad |1+e^{-2iku}|\le2.
 \tag{21}
\]
Their lengths and parity amplitudes are bounded. Choose the
tolerance in (H) smaller than the fixed gaps above, and absorb
the original factor \(N/(4\pi)\) and the polynomial Chebyshev
factor into those gaps. This proves
\(|\mathcal J_{N,k}|\le C e^{N(\Gamma-\eta_1)}\) for some
\(\eta_1>0\). Equation (8) proves (16).

The local coefficient has modulus bounded away from zero.
Its factor \(N^{-1}\) is larger than the exponentially small
relative remainder in (16), so the conditional nonvanishing
conclusion follows. \(\square\)

Hypothesis (H), the subsequent comparison after outgoing coefficients
are attached, and stability under arbitrary fixed short fillings
remain open. Only the exact reflection, the phase monotonicity,
and the displayed implication are proved in this note.

## Source versions

- Positive taper and retained upper connector:
  630fc00e67395f04fd44b8c32618202c67b9f457900d0cced44ed8f6f0da3e22.
- Complete positive real-continuum source bound:
  5994df2b37ebc8bd016300d5285701827add2d8c25cf170629dca00b3181798a.
- Original symmetric phase derivatives:
  102daa403519833ca13414ca2e0e20f351c572a5740ab9ca6ffb1c204d2eda7f.
- Selected-depth and charged action-loss bounds:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Complete-action lower bound:
  dd5153c7eabefe865b6fd1ed03e6f2fb08c63283f20fd48a999b625ec4836c42.
- Local Gaussian and original coefficient:
  6f2b155eee54cfd8a930d9af146ab96c3de277aac70d2de51b5f8318523f45ab.

