# Analytic probes of the whole kernel retain exact boundary currents

Research note, 6 November 2026.

The [quantitative Ward estimate](research_quantitative_power_ward_exclusion.md)
can be applied on the test-function side of a contour pairing.
This removes the requirement of a fixed-complex-neighborhood norm
for the kernel from that pairing estimate. It retains the kernel's
norm on the integration contour, every translated boundary current,
and any inhomogeneous original source term. The construction does
not give a separately invariant saddle or a geometric cycle
coefficient.

## 1. Exact change of variables

First use one complex coordinate. Let the whole original kernel
\(u_N\) obey
\[
 L_Nu_N(x)=\sum_{\nu\in\mathcal V}a_{\nu,N}(x)
                  u_N(x+\sigma_\nu)=r_N(x),
 \qquad \sigma_\nu=\nu/N .
 \tag{1}
\]
Let \(\Gamma\) be an oriented path from \(a\) to \(b\), and suppose
the path, its translations and their connecting strips lie in
a common regular chart where the kernel and the coefficients used
below are holomorphic. For a holomorphic probe \(\phi\), define
\[
 L_N^{\mathrm t}\phi(y)
       =\sum_\nu a_{\nu,N}(y-\sigma_\nu)\phi(y-\sigma_\nu).
 \tag{2}
\]
Changing variables in each term and applying Cauchy's theorem
on the translated strip gives the exact identity
\[
 \int_\Gamma\phi r_N\,dy
   =\int_\Gamma u_N L_N^{\mathrm t}\phi\,dy
       +\mathcal E_N(\phi),
 \tag{3}
\]
where
\[
 \mathcal E_N(\phi)
 =\sum_\nu\left(\int_b^{b+\sigma_\nu}
                  -\int_a^{a+\sigma_\nu}\right)
       u_N(y)a_{\nu,N}(y-\sigma_\nu)
                         \phi(y-\sigma_\nu)\,dy .
 \tag{4}
\]
The sign follows from traversing \(\Gamma\), then its right
connector, then the reverse translated path, then the reverse
left connector. No Ward equation is assigned to a restricted
piece of \(u_N\).

For a real \(d\)-dimensional product contour in \(\mathbb C^d\),
the identical translation argument uses the prisms swept out by
its boundary faces and the holomorphic volume form. Each prism
has thickness \(O(N^{-1})\). The sum of these face currents is
the multidimensional version of (4), including the orientation
from the translation homotopy. The formula requires that the
prisms avoid every retained divisor. A pole crossed by a prism
adds its residue; it is not part of the estimate below.

## 2. An analytic inverse acting only on the probe

Let \(S\) and the coefficients be holomorphic on fixed nested
polydisks \(D_r\Subset D_R\), with all contours, connectors
and their necessary translates inside \(D_r\). Assume, as in
the quantitative Ward note, that
\[
 a_{\nu,N}=a_{\nu,0}+O(N^{-1}),\qquad
 \ell(x)=\sum_\nu a_{\nu,0}(x)e^{\nu\cdot dS(x)},\qquad
 |\ell|\ge\delta>0 .
 \tag{5}
\]
The transpose has the same principal multiplier after conjugation:
\[
 \mathcal A_N^{\mathrm t}v
  :=e^{NS}L_N^{\mathrm t}(e^{-NS}v)
  =\sum_\nu a_{\nu,N}(x-\sigma_\nu)
       e^{N\{S(x)-S(x-\sigma_\nu)\}}v(x-\sigma_\nu)
  =\ell v+\mathcal R_Nv .
 \tag{6}
\]
Set \(\mathcal T_N=\mathcal R_N\ell^{-1}\), with multiplication
by \(\ell^{-1}\) performed before \(\mathcal R_N\). On nested
domains the same Cauchy estimate gives
\(\|\mathcal T_Nv\|_{D_s}\le C(Nt)^{-1}\|v\|_{D_{s+t}}\).
The derivative bounds of \(\ell^{-1}\) are included in \(C\).

For a holomorphic amplitude \(\psi\) on \(D_R\), choose
\[
 m=\left\lfloor\frac{(R-r)N}{4M}\right\rfloor,\qquad
 b_{m,N}=\ell^{-1}\sum_{j=0}^{m-1}(-\mathcal T_N)^j\psi,
 \qquad
 \epsilon_{m,N}=(-\mathcal T_N)^m\psi ,
 \tag{7}
\]
where \(M\) is fixed and large enough for each successive
domain loss to give norm at most \(1/4\). Exact telescoping gives
\[
 L_N^{\mathrm t}(e^{-NS}b_{m,N})
       =e^{-NS}(\psi-\epsilon_{m,N}),\qquad
 \|\epsilon_{m,N}\|_{D_r}\le4^{-m}\|\psi\|_{D_R},\qquad
 \|b_{m,N}\|_{D_r}\le\frac4{3\delta}\|\psi\|_{D_R}.
 \tag{8}
\]
There is no asymptotic equality in the first identity of (8).
The amplitudes and coefficients are differentiated, not \(u_N\).

## 3. The resulting localized pairing estimate

Insert \(\phi=e^{-NS}b_{m,N}\) into (3). For
\(I_N=\int_\Gamma e^{-NS}u_N\psi\,dy\), one obtains exactly
\[
 I_N=\int_\Gamma e^{-NS}u_N\epsilon_{m,N}\,dy
       +\int_\Gamma e^{-NS}b_{m,N}r_N\,dy
       -\mathcal E_N(e^{-NS}b_{m,N}).
 \tag{9}
\]
Since
\(e^{N\{S(y)-S(y-\sigma_\nu)\}}\) is uniformly bounded
on this fixed chart, (4) and (8) imply
\[
 \begin{split}
 |I_N|\le \|\psi\|_{D_R}\bigg[
   4^{-m}\int_\Gamma|e^{-NS}u_N|\,|dy|
   +\frac4{3\delta}\int_\Gamma|e^{-NS}r_N|\,|dy|\\
   +\frac{C_\partial}{N}
       \sup_{\text{endpoint connectors}}|e^{-NS}u_N|
                         \bigg].
 \end{split}
 \tag{10}
\]
For a fixed product contour, its boundary areas are included
in \(C_\partial\), and the supremum is over all translation prisms.
If the translated cycles are closed and homologous in the regular
domain, their boundary term is absent. If (1) contains a physical
endpoint or truncation source, that source remains in \(r_N\).

Thus an exponential gain for this probe follows from a calibrated
weighted contour norm, a smaller residual rate, and a smaller
connector rate. No analytic upper bound for \(u_N\) on all of
\(D_R\) is needed. Conversely, the factor \(N^{-1}\) in the last
term is only a polynomial improvement: a connector at the original
rate prevents a fixed exponential conclusion. A crude
\(\exp(CN)\) norm for the finite polynomial is not automatically
the desired geometrically calibrated norm.

This is an exact route for using a Ward equation of the whole
original kernel while localizing its observation. It does not
yet establish the three rate inputs for a short-filled source,
nor identify the chosen probe with its original contributing
cycle. The original all-pole
[full-\(\Psi\) presentation](actual_full_psi_scalar_flow_cycle.md)
has additional ray and cut currents; (3) does not remove them.
Likewise positivity of a local canonical graph does not imply
that its coefficient survives the original root-of-unity cycle.
