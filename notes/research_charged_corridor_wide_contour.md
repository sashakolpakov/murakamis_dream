# A larger nonzero charge interval for arbitrary fixed corridors

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The wide finite-kernel theorem permits a substantial extension of the
proved small-charge initializer. The conclusion concerns the exact
coupon-inserted original source, including its full Hermite data.
It does not continue that source to charge one, and it does not assume
the global relative-homology hypotheses of the dominant-saddle
transport principle.

## 1. Exact family and statement

Let \(\Gamma\) be a fixed nontrivial finite path, let \(I\) be a
nonempty selected set, and retain its original incidence degrees
\(d_v\in\{1,2\}\). All unselected angles are zero. Set
\(m=|I|\), \(e=|E|\). Fix signed integer powers \(n_v\).
Use the original full Newton kernels and Frobenius traces.

For real \(\chi\), let \(\mathcal C_{N,\chi}\) be the unique
degree-less-than-\(N\) polynomial with the full physical jets of
\(\cos(N(1-\chi)t)\). At a double physical node \(w=-2\cos\tau\)
these are the value and ordinary derivative
\[
 \cos(N(1-\chi)\tau),\qquad
 -\frac{N(1-\chi)\sin(N(1-\chi)\tau)}{2\sin\tau}.
 \tag{1}
\]
The odd simple node has value one and no prescribed normal.
This is the exact entire parameter family in
[the transport note, Section 9](research_dominant_saddle_transport.md#9-an-exact-analytic-coupon-family-and-the-proved-initializer).
At \(\chi=j/N\), it is the original Chebyshev coupon
\(T_{N-j}(-w/2)\) in the full quotient. Define
\[
 Z_N(\boldsymbol\chi)=
 \left(\prod_{v\in I}\phi_N^{(w_v)}\right)
 \left[
   \prod_{v\in I}R(w_v)^{n_v}\mathcal C_{N,\chi_v}(w_v)
   \prod_{vw\in E}K_N(t_v,t_w)
 \right],\qquad w_v=-2\cos t_v .
 \tag{2}
\]
Products are taken before tracing. Write
\[
 \Phi_{\boldsymbol\chi}(t)=
 \sum_{vw\in E}\psi(t_v,t_w)
       +\sum_{v\in I}\left(\frac{in_vt_v^2}{4\pi}
                                      -i\chi_vt_v\right).
 \tag{3}
\]
The edge phase has its original complete constant \(M_\infty\).

**Theorem 1.** Either of the following is sufficient:
\[
 \begin{array}{c|c}
 \text{all selected powers}&\text{charge bound }q\\ \hline
 |n_v|\ge2&q=1/10\\
 |n_v|\ge3&q=1/5 .
 \end{array}
 \tag{4}
\]
For every fixed \(0<\epsilon\le q\), uniformly on
\(\boldsymbol\chi\in[\epsilon,q]^I\), the original source satisfies
along all integer levels and at both parities
\[
 Z_N(\boldsymbol\chi)=\varepsilon_N N^{3(m-e)/2}
       A(\boldsymbol\chi)e^{N\Phi_{\boldsymbol\chi}(t^*)}
                         (1+O(N^{-1})),
 \tag{5}
\]
where
\[
 \begin{split}
 \varepsilon_N&=\prod_{v\in I}
             e^{\pi i n_v(N-1)^2/(4N)},\\
 A(\boldsymbol\chi)
 &=\left(\frac{i}{2\pi}\right)^m(2\pi)^{m/2}
 \frac{\displaystyle\prod_{v\in I}\sin t_v^*
                    \prod_{vw\in E}a_e(t_v^*,t_w^*)}
      {\sqrt{\det[-\Phi_{\boldsymbol\chi}''(t^*)]}}\ne0 .
 \end{split}
 \tag{6}
\]
The Gaussian branch is the one for complex symmetric Hessians with
positive definite real part. The modulus of (6) is bounded below
on the stated compact charge box. There is an expansion to every
fixed inverse-power order. In particular the statement applies
to every sequence of integral coupon charges \(j_v/N\) in this
box, using their actual values in the exponent and amplitude.

All vertices may be selected, signs may differ, and no complete
outside end is required. This is a finite-source theorem; no
nonintegral charge is declared to be a knot filling.

## 2. Continuation through the entire charge box

Work first on
\[
 \mathcal B=\{t:|\Re t|\le1,\ |\Im t|\le1/3\}.
 \tag{7}
\]
The original edge estimates in
[the partial-charge proof](research_positive_path_partial_charge_bounds.md#2-the-exact-return-map-is-a-contraction)
give a holomorphic removable quotient
\[
 C_v(t)=2\sum_{w\sim v}\frac{r_{vw}(t)}{t_v},
 \quad
 r_{vw}=\operatorname{asinh}\{\tan(t_v/2)\cos(t_w/2)\},
 \qquad |C_v-d_v|<\frac25d_v .
 \tag{8}
\]
The original stationary equations factor exactly as
\[
 t_v=\frac{2\pi\chi_v}{n_v+iC_v}.
 \tag{9}
\]
Write \(C_v=A_v+iB_v\). On (7), \(A_v>3d_v/5>0\) and
\(|B_v|<2d_v/5\). Thus, at every solution in this box,
\[
 \begin{split}
 |t_v|&\le\frac{2\pi\chi_v}{|n_v|-2d_v/5},\\
 H_v:=-\Im t_v
 &=\frac{2\pi\chi_v A_v}{(n_v-B_v)^2+A_v^2}
 \le\frac{\pi\chi_v}{|n_v|-2d_v/5}.
 \end{split}
 \tag{10}
\]
The last inequality is \(2A/(c^2+A^2)\le1/|c|\).
It does not use the stronger corner-monotonicity condition
\(|n_v|>9d_v/5\), which fails at \((|n|,d)=(3,2)\).
Consequently the two rows of (4) give respectively
\[
 (|t_v|,H_v)\le(\pi/6,\pi/12),\qquad
 (|t_v|,H_v)\le(2\pi/11,\pi/11).
 \tag{11}
\]
These lie strictly inside (7), and \(H_v<3/10\).
Positive charge gives positive depth; zero charge gives exactly
zero angle. The real angle has the sign of \(n_v\).

At zero charges the solution is \(t=0\). Throughout (7) the
known edge bound \(\Re[-2\pi\psi'']\succeq I/5\) makes
\(-\Phi_{\boldsymbol\chi}''\) accretive and invertible. The
implicit function theorem therefore continues the zero solution
along each real charge segment. It cannot leave (7), by (11).
Compactness and the same invertibility extend it through the entire
segment. The solution is unique in the box: for two stationary
points with difference \(h\), integrate the Hessian along their
straight segment and take the real part of its pairing with
\(h^*\). Accretivity makes this strictly positive unless \(h=0\).
The branches from different segments thus agree and are locally
holomorphic on a neighborhood of the full cube \([0,q]^I\).
This argument proves the required continuation directly, including
the all-selected and signed cases.

Let \(M(\chi)=\Re\Phi_\chi(t(\chi))\). Stationarity and (10)
give \(\partial_{\chi_v}M=-H_v\). Completing a subset \(S\)
of vertices by setting their charges to zero costs at most
\[
 M(\boldsymbol\chi^S)-M(\boldsymbol\chi)
 \le\sum_{v\in S}
       \frac{\pi\chi_v^2}{2(|n_v|-2d_v/5)}
 \le
 \begin{cases}
  (\pi/320)\sum_{v\in S}d_v,&q=1/10,\\
  (\pi/130)\sum_{v\in S}d_v,&q=1/5,
 \end{cases}
 <\frac1{40}\sum_{v\in S}d_v .
 \tag{12}
\]
All original edges and their complete constants remain present.

## 3. Every mixed trace current has a strict gap

Choose the largest physical midpoint \(T_N\le\pi/2\); eventually
\(T_N\ge3/2\). Use lower horizontal heights \(-H_v\) and
vertical sides \(\operatorname{sgn}(n_v)T_N\). Retain the
original negative-side orientation factor. The exact identities
(15)--(17) of
[the coupon source proof](research_small_charge_path_source.md#3-the-exact-coupon-contour-and-every-competing-charge)
remain valid for the full-jet family (1), also at nonintegral
real charge. In particular the horizontal scalar kernel is
\[
 \frac12e^{-iN\chi_vt_v}
       \frac{1+e^{-2iN(1-\chi_v)t_v}}
                    {(1-(-1)^{N-1}e^{-iNt_v})^2},
 \tag{13}
\]
and a vertical side has the exact upper penalty
\(-N\chi_v|h_v|\). No periodicity of the nonintegral cosine
representative is assumed: the retained identity uses its actual
even full jets and retains the vertical sides.

For a vertical coordinate the exponent derivative is
\[
 \partial_{h_v}\mathcal E
 =\frac1\pi\sum_{w\sim v}\Im r_{vw}
          -\frac{|n_v|T_N}{2\pi}-\chi_v\operatorname{sign}h_v .
 \tag{14}
\]
All other coordinates may be anywhere on their horizontal or
vertical segments. They lie in the full wide rectangle.
For \(h_v<0\), a positive imaginary return is less than \(5/42\),
by the signed estimate in the
[mixed-current proof](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven).
For \(h_v>0\), put \(z=\tan(t_v/2)\cos(t_w/2)\). The same box gives
\[
 |\Re\tan(t_v/2)|\le1,\quad |\Im\tan(t_v/2)|<3/10,\quad
 |\Im\cos(t_w/2)|<4/35,\quad
 |\Re\cos(t_w/2)|<81/80.
 \tag{15}
\]
Thus \(|\Im z|<4/35+243/800<\sin(1/2)\).
On the original asinh branch,
\(\Im z=\cosh(\Re r)\sin(\Im r)\) and
\(|\Im r|<\pi/2\), so every positive imaginary return is
less than \(1/2\). The elementary cosine bound in (15) follows
from \(\cosh(3/20)<81/80\).

For \(q=1/10, |n|\ge2\), (14) is at most
\(1/10-53/(42\pi)\) below zero height, and less than
\(-1/(2\pi)\) above zero height. Both are less than \(-3/20\).
For \(q=1/5, |n|\ge3\), the corresponding bounds are
\(1/5-169/(84\pi)\) and \(-5/(4\pi)\), which are stronger.
Lowering every vertical height to its bottom endpoint therefore
increases the pointwise upper exponent, with the stated strict
slope throughout the process.

At the resulting horizontal point, the wide Hessian gives
\(-\Re\Phi''\succeq\operatorname{diag}(d_v)/(20\pi)\).
Each vertical coordinate is at real distance greater than
\(3/2-2\pi/11>9/10\) from its saddle. Consequently every
nonempty vertical subset \(S\) satisfies
\[
 \mathcal E_S<
 M(\boldsymbol\chi)-\frac1{200}\sum_{v\in S}d_v
                -\frac3{20}\sum_{v\in S}(h_v+H_v).
 \tag{16}
\]
The full wide-kernel theorem turns this into an estimate on the
actual finite integrand, with all its ordinary normals.

## 4. Removed rows, aliases and the surviving coefficient

Split the original physical sampling formula by its removed-row
subset \(S\). On real physical nodes the coupons have modulus at
most one, and their first normals cost only powers of \(N\),
uniformly on the charge box. The original crossing values and
normals have the same bounds as before. Deform the remaining
traces at the partial-charge point \(\boldsymbol\chi^S\).
The centered full-kernel theorem loses \(21/200\) per removed
incidence, also when both endpoints are removed and at the
rounded physical cut. Together with (12) this gives
\[
             \operatorname{rate}(S)<
                M(\boldsymbol\chi)-\frac2{25}
                                      \sum_{v\in S}d_v.
 \tag{17}
\]
Its product-rule proof retains all double-root normals and the
odd simple row, exactly as in the original initializer.

On \([\epsilon,q]^I\), the heights have a positive uniform lower
bound by (9)--(10) and compactness. Since \(q\le1/5\), the
quotient in (13) is \(1+O(e^{-cN})\), with all fixed spatial
derivatives. This simultaneously controls every higher trace
charge and the companion coupon term. The coefficient of the
remaining horizontal charge is exactly \(1/2\) at each vertex.
Upper and lower copies were already combined in the exact
retained trace; there is no second unexamined leading contribution.

Strict horizontal concavity leaves a unique Gaussian maximum.
The original wide-kernel expansion has nonzero edge amplitudes,
and the strictly negative imaginary saddle coordinates make all
\(\sin t_v^*\) nonzero. The original trace factors, coupon
coefficients, edges and Gaussian contribute respectively
\(N^{2m}\), \(2^{-m}\), \(N^{-3e/2}\), and \(N^{-m/2}\).
This proves (5)--(6), including every fixed expansion order.
The errors in (16)--(17) cannot cancel that term.

For a fixed rational word the exact marked normalization reduces
its nondegenerate corridor to a uniform-sign list of magnitudes
at least two, retaining the two end chirps and proper rotation.
The first row of (4) therefore initializes an actual analytic
source family for every such normalized corridor, of arbitrary
fixed length. At charge one the coupons disappear and the exact
word identities recover the original target source. This theorem
does not estimate that endpoint.

In particular it is not a proof that the full top relative homology
group stays a line up to charge one. Beyond (4), the current phase
box and the full finite-kernel bounds used here need not contain
the geometric contour; previously identified factorial end and
alias contributions cannot simply be discarded. The new result
proves nonzero coefficient transport on the stated interval by
direct control of the entire original period, not by endpoint
volume rigidity or a scalar norm-to-overlap assumption.

## 5. Uniform outside packets and whole-boundary decay

Let \(B\) be any set of nonisolated unselected vertices, whose
ordinary colors \(z_b=-2\cos u_b\) are now left free in (2).
Keep the literal outside polynomial and write it
\(F_{N,\boldsymbol\chi}(\mathbf u)\). Its separate degrees are
at most \(d_b(N-1)\); no canonical reduction is made at an
untraced vertex.

**Corollary 2.** For either row of (4) and every fixed
\(0<\epsilon\le q\), the nonzero packet (5)--(6) continues to
a fixed small complex neighborhood of the outside complete
colors, uniformly over \(\boldsymbol\chi\in[\epsilon,q]^I\).
It is holomorphic in ordinary outside colors and retains all
fixed ordinary derivatives. Put
\(\mathcal U(\mathbf x)=\sum_{b\in B}d_b(1-\cos x_b)\).
There are \(c,B_0,h>0\) such that for every fixed ordinary
outside multi-index \(\alpha\),
\[
 \begin{split}
 |\partial_{\mathbf z}^\alpha F_{N,\boldsymbol\chi}(\mathbf x)|
   &\le C_\alpha N^{A_\alpha}
        e^{N[M(\boldsymbol\chi)-\mathcal U(\mathbf x)/100]},\\
 |\partial_{\mathbf z}^\alpha
          F_{N,\boldsymbol\chi}(\mathbf x+i\mathbf y)|
   &\le C'_\alpha N^{A'_\alpha}
        e^{N[M(\boldsymbol\chi)-c\mathcal U(\mathbf x)
                                     +B_0|\mathbf y|^2]},
 \quad |x_b|\le\pi,\quad |y_b|\le h .
 \end{split}
 \tag{18}
\]
All constants are uniform on the compact charge box and at both
level parities.

*Proof.* Compactness and (9)--(11) give a positive minimum of
the saddle depths on this charge box. The accretive implicit
equations continue jointly in the charges and small outside
angles; their saddles stay strictly within the proved kernel
domain. All current and removed-row inequalities have strict
uniform margins. The full kernel and centered estimates hold
on actual complex neighborhoods with their ordinary normals,
so the complete-source proof persists on a common outside
polydisk. Its sine factors, determinant and edge amplitudes
remain nonzero on a smaller polydisk.

Use now the exact per-edge inequalities (8)--(11) in
[the whole-boundary proof](research_network_whole_boundary_decay.md#2-a-loss-for-every-free-outside-incidence).
They do not depend on the crossing power or the coupon.
Every free outside incidence contributes
\((1-\cos x_b)/100\), while every removed internal incidence
retains its entire \(21/200\) cost. Apply them to the same
complete-outside contours used above. Equations (12), (16) and
(17) retain their gaps and the exterior losses add. This gives
the first bound in (18), including all original ordinary
outside normals.

For the second bound use exactly the multivariable Laurent
majorant (12)--(13) of the whole-boundary proof with degrees
\(d_b(N-1)\). Outside a fixed neighborhood of zero, its linear
height cost is absorbed into half the angular loss on a small
strip. Inside that neighborhood, the just-proved local packet
has a separately even holomorphic phase \(W_\chi\).
The real-period bound implies
\(-\Re W_\chi''(0)\succeq\operatorname{diag}(d_b)/100\).
Holomorphic Taylor expansion and Young's inequality yield the
quadratic height bound. Compactness in \(\chi\) makes the
neighborhood, curvature, derivative bounds and strip uniform.

Separate evenness and the unique local branch make the phase,
amplitude and normalized remainder holomorphic in the ordinary
colors at the ramified angles \(u_b=0\). Cauchy estimates there
and the original ordinary derivative bounds elsewhere retain
every fixed normal at polynomial cost. No assertion is made
that a derivative of the nonzero amplitude is itself nonzero.
This proves (18). \(\square\)

For the one- and two-endpoint corridor sources, the outside
degrees are at most \(N-1\), and this gives controlled relative
boundary packets throughout the stated charge interval. More
general unselected vertices retain their literal degree bound.
This does not extend the charge interval, identify a nonintegral
coupon source with a knot invariant, or remove the original
end chirps when a marked rational word is reexpressed.

The [exact constants checker](../experiments/check_charged_corridor_wide_contour.py)
and its [saved record](../repro/results/research-charged-corridor-wide-contour.json)
verify the rational bounds used here and record all proof dependencies.
They do not replace the exact contour or continuation arguments.
