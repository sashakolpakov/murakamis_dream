# A paid central block of the exact outer contour

Private finite-source deduction, 9 November 2026. The complete
imaginary-axis packet and the exact finite polynomial degree give
an exponential bound on a fixed central block of the outer bottom
contour. No packet on a prescribed negative complex corridor is
assumed. The block includes a negative angular segment and retains
the complete rational sampling multiplier, both reflected charges
and both parity normalizations.

The block width depends on the fixed positive lower charge cutoff;
it is independent of the level and frequency. The remaining negative
and positive currents are not estimated here. No mathematical
numerical evaluation, saved-value arithmetic, or frozen-source
edit is used.

## 1. Exact source and claimed block

Use the full and shortened-output sources
\(Q_N^{\mathrm{full}},Q_N^{\mathrm{sh}}\) from
[the paired-contour theorem](research_mixed_next_outer_far_nodes_and_paired_contour.md).
Their ordinary spectral representatives satisfy
\[
Q_N^\star(u)=\widehat Q_N^\star(-2\cos u),\qquad
\deg\widehat Q_N^{\mathrm{full}}\le D=N-1,\qquad
\deg\widehat Q_N^{\mathrm{sh}}\le U=\lfloor N/2\rfloor-1.
\tag{1}
\]
The first edge and full original inner Hermite trace remain
unchanged in the shortened source. Formula (1) is an ordinary
polynomial statement, not equality of the two sources off-grid.

Fix \(0<\delta_1\le1/2\), and keep the original selected curve,
phase, and action
\[
u_\delta=\beta_\delta-iK_\delta,\quad
\Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\quad
\Gamma(\delta)=\Re\Psi_\delta(u_\delta),\quad
                           \delta_1\le\delta\le1/2.
\tag{2}
\]
Define the positive compact constants
\[
\beta_{\min}=\min_{\delta_1\le\delta\le1/2}\beta_\delta>0,\qquad
K_{\min}=\min_{\delta_1\le\delta\le1/2}K_\delta>0,\qquad
K_{\max}=\max_{\delta_1\le\delta\le1/2}K_\delta<2/5,
\qquad g_0=\frac{\beta_{\min}^2}{100\pi}.
\tag{3}
\]
Their existence follows from the adopted selected curve and
its strict depth bound. No numerical value is assigned to them.

For the actual integers \(0\le k\le\lfloor N/2\rfloor\) with
\(\delta=1/2-k/N\) in (2), retain
\[
\begin{gathered}
\eta_N=(-1)^{N-1},\qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)},\\
H_N(u)=\frac1{1-\eta_Ne^{-iNu}},\qquad P_k(u)=1+e^{-2iku},\\
a_N(u)=
\begin{cases}
\sin u,&N\text{ even},\\
\sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\text{ odd},
\end{cases}
\qquad
\chi_N=\begin{cases}i,&N\text{ even},\\-1,&N\text{ odd}.
\end{cases}
\end{gathered}
\tag{4}
\]

**Theorem.** There is a fixed \(\epsilon>0\), with
\(\epsilon<\beta_{\min}/4\), such that the literal bottom
block
\[
\gamma_{\mathrm c,\delta}:
       -\epsilon-iK_\delta\longrightarrow\epsilon-iK_\delta
\tag{5}
\]
satisfies, uniformly at both parities and all these frequencies,
\[
\boxed{\quad
\frac{N}{4\pi}\int_{\gamma_{\mathrm c,\delta}}
 \left|H_N(u)a_N(u)Q_N^\star(u)
 e^{N(3iu^2/(4\pi)-i\delta u)}P_k(u)\right|\,|du|
 \le C e^{N\{\Gamma(\delta)-g_0/2\}},
 \qquad \star\in\{\mathrm{sh},\mathrm{full}\}.
\quad}
\tag{6}
\]
In particular the version with \(\star=\mathrm{sh}\), multiplied
by the unchanged unit scalar \(\chi_NC_{N,3}\), bounds an actual
subcurrent of the original finite observation. The full-source
version is a separate bound, not a pointwise replacement in that
observation.

## 2. A strict action gap on the axis

The original [two-sided charged descent theorem](research_mixed_next_charged_curve_two_sided_descent.md)
gives on its symmetric rectangle
\[
\Re\Psi_\delta''(u)<-\frac1{50\pi}.
\tag{7}
\]
The horizontal segment from \(-iK_\delta\) to
\(\beta_\delta-iK_\delta\) lies in that rectangle:
\(\beta_\delta<8/7<4/3\) and \(K_\delta<2/5<1/2\).
The full complex derivative vanishes at \(u_\delta\).
Integrating (7) twice along this segment therefore gives
\[
\Re S(-iK_\delta)-\delta K_\delta
 =\Re\Psi_\delta(-iK_\delta)
 \le\Gamma(\delta)-\frac{\beta_\delta^2}{100\pi}
 \le\Gamma(\delta)-g_0.
\tag{8}
\]
The quadratic crossing is purely imaginary on the axis.
This uses the calibrated original \(S\), not a fresh choice
of a stationary-action constant.

## 3. Finite-degree continuation from an axis interval

Write \(s_{\mathrm a}(v)=\Re S(-iv)\).
The independently proved
[complete imaginary-axis theorem, (2)](research_mixed_next_imaginary_axis_inner_packet.md)
gives for both sources
\[
|Q_N^\star(-iv)|\le C N^A e^{Ns_{\mathrm a}(v)}
                       \qquad (0\le v\le2/5),
\tag{9}
\]
uniformly in \(v,N\) and parity. This is a full finite-source
upper bound; no relative error is inserted into a cancelling sum.

Choose a fixed \(r>0\) so small that
\[
[K-r,K+r]\subset(0,2/5),\qquad
|s_{\mathrm a}(v)-s_{\mathrm a}(K)|\le g_0/8
\tag{10}
\]
whenever \(K_{\min}\le K\le K_{\max}\) and \(|v-K|\le r\).
Compactness, (3), and continuity of the original action
give this choice.
For each such \(K\), the spectral images form the real interval
\[
I_K=[-2\cosh(K+r),-2\cosh(K-r)].
\tag{11}
\]
It has a uniformly positive length. Its interior point
\(X_K=-2\cosh K\) has uniformly positive distance from
both endpoints. This follows from \(K-r>0\), strict
monotonicity of \(\cosh\), and compactness.

Set \(\mu=g_0/8\). Let \(\mathcal E_K(\mu)\) be the filled
ellipse obtained from the standard ellipse
\[
z=\cos(\theta+i\mu),\qquad-\pi\le\theta\le\pi,
\]
by the real affine map from \([-1,1]\) onto \(I_K\).
Each \(X_K\) lies in its interior. The compact set of pairs
\((K,X_K)\) consequently has a uniform positive distance
from these ellipse boundaries. By continuity of
\((x,K)\mapsto-2\cos(x-iK)\), there is a fixed
\(\epsilon>0\) such that
\[
-2\cos(x-iK)\in\mathcal E_K(\mu)
       \quad (|x|\le\epsilon,\ K_{\min}\le K\le K_{\max}).
\tag{12}
\]
Decrease \(\epsilon\), if necessary, to impose
\[
\epsilon<\beta_{\min}/4,\qquad
\frac{3\epsilon K_{\max}}{2\pi}\le g_0/8.
\tag{13}
\]
All these are choices in fixed compact domains, with no
level-dependent limiting width.

Here is the elementary polynomial estimate being used.
For a complex polynomial \(P\) of degree at most \(d\),
rescale \(I_K\) to \([-1,1]\) and expand in Chebyshev
polynomials. Its constant coefficient is bounded by
\(\|P\|_{I_K}\), and every other coefficient by
\(2\|P\|_{I_K}\), from the cosine integral formulas.
On \(\mathcal E_K(\mu)\), each polynomial of order \(j\)
has modulus at most \(e^{j\mu}\), first on the boundary
and then by the maximum principle. Thus
\[
|P(X)|\le(2d+1)e^{d\mu}\|P\|_{I_K},
                              \qquad X\in\mathcal E_K(\mu).
\tag{14}
\]
The argument applies to complex coefficients and uses no
positivity of either quantum kernel.

Apply (14) to the exact polynomial in (1), using \(d\le N-1\).
Equations (9)--(12) give the uniform bound
\[
|Q_N^\star(x-iK)|
 \le C N^{A+1}
    \exp N\{s_{\mathrm a}(K)+g_0/4\},
\quad |x|\le\epsilon,\quad K_{\min}\le K\le K_{\max}.
\tag{15}
\]
This is the entire continuation step. It does not infer
an analytic relative packet from one-dimensional asymptotics,
and it does not discard any factorial or Hermite source.

## 4. Full multiplier and exact placement in the left current

On (5), the original outer exponent has real part
\[
\Re\left(\frac{3iu^2}{4\pi}-i\delta u\right)
        =\frac{3xK_\delta}{2\pi}-\delta K_\delta.
\tag{16}
\]
The positive half of this block is included, so the possible
increase is charged explicitly by (13).
Combining (8),(13),(15),(16) bounds the full source before
bounded factors and powers of \(N\) by
\[
\exp N\{\Gamma(\delta)-5g_0/8\}.
\tag{17}
\]
The complete rational sampling kernel obeys
\[
|H_N(u)|\le(1-e^{-NK_{\min}})^{-1},
\qquad
|P_k(u)|\le1+e^{-2kK_\delta}\le2.
\tag{18}
\]
These bounds include every sampling alias and every integer
frequency. At \(k=0\) the paired factor is exactly two.
The functions \(a_N\) are uniformly bounded on this compact
block at both parities. Its length is at most \(2\epsilon\).
The original \(N/(4\pi)\) in (6) and every fixed polynomial
factor in (15) can be absorbed in \(g_0/8\) for sufficiently
large \(N\). This proves (6).

In the exact Gaussian/current assembly
\[
\mathcal O_{N,k}
=G_{N,k}+L_{N,k}+R_{N,k}+V_{N,k}+E_{N,k}^{\mathrm{phys}},
\tag{19}
\]
the left current goes from \(-T_N-iK_\delta\) to
\(u_\delta-r_{\mathrm G}\), where
\(r_{\mathrm G}<\beta_{\min}/4\).
Because of (13), the segment (5) lies strictly inside that
left path. Splitting it is an exact operation:
\[
L_{N,k}=L_{N,k}^{-}+C_{N,k}^{\mathrm{axis}}+L_{N,k}^{+}.
\tag{20}
\]
Here the three left-to-right endpoints are, respectively,
\[
[-T_N,-\epsilon]-iK_\delta,\qquad
[-\epsilon,\epsilon]-iK_\delta,\qquad
[\epsilon,\beta_\delta-r_{\mathrm G}]-iK_\delta,
\]
and each current retains the identical integrand and
\(\chi_NC_{N,3}N/(4\pi)\) scalar. Equation (6) pays the
middle current with gap \(g_0/2\).
The other two pieces, the right bottom current and the
entire right vertical remain explicit. No new endpoint
cap, sampling residue, or normal term is created by (20).

This proof supplies a nonempty fixed paid block on the
negative side and across the central axis. It does not
control the rest of the negative lower corridor or prove
that the local outer Gaussian survives all remaining
currents.

## Frozen source bindings

- Complete imaginary-axis packet:
  8cdfab84a1b0dfb817efe41b79caa5cc74fc62fce01bac54adddd54115507d90.
- Two-sided original charged descent:
  102daa403519833ca13414ca2e0e20f351c572a5740ab9ca6ffb1c204d2eda7f.
- Exact paired contour, source normalization and far nodes:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Selected curve and original charge:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Strict depth bound:
  f3b0b8f8e14adb8beff461e53ec20cdcb7afb4dc07bda3e1247116b55e13c017.
- Exact low-edge and ordinary degree:
  76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a.
- Local outer Gaussian and literal remaining currents:
  6f2b155eee54cfd8a930d9af146ab96c3de277aac70d2de51b5f8318523f45ab.
