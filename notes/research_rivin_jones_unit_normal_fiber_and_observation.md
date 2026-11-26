# A supplementary normal-fiber calculation for the exact boundary bridge

Private written calculation, 14 November 2026. This records one concrete
consequence of the [prescribed-cut recovery](research_rivin_jones_prescribed_cut_and_hermite_recovery.md).
It is not a new general lower-bound theorem. The
[closing stability-radius theorem](research_observed_closing_stability_radius.md)
already gives the abstract obstruction under arbitrary linear constraints;
the calculation here identifies the relevant fiber inside the unit group
of the actual full Hermite algebra.

Use \(\mathcal A_N=\mathbb C[z]/(P_N)\),
\(P_N(z)=2T_N(z/2)+2\), and its distinct double nodes \(c\).
Put \(a_c=4-c^2\ne0\). The exact prescribed external cut is
\[
 L(f)=\sum_{c\ {\rm double}}\{a_cf'(c)-cf(c)\}
               +\mathbf1_{N\ {\rm odd}}f(-2).
\]
Here \(L(f)\) means the original highest-head cut of
\(f(\Omega_{\rm ext})\), not an unmarked matrix trace.
The canonical nilpotent coupons \(V_c\) of the cited recovery have
jets \((0,1)\) at \(c\), zero jets elsewhere, and satisfy
\[
 V_cV_{c'}=0\quad\hbox{for all }c,c',\qquad
 fV_c=f(c)V_c,\qquad L(V_c)=a_c.
\]

Fix a unit \(f\in\mathcal A_N\). Its entire fiber with the same
values at every distinct spectral node is
\[
 f_{\boldsymbol\tau}=f\left(1+\sum_c\tau_cV_c\right),
                       \qquad \boldsymbol\tau\in\mathbb C^{\lfloor N/2\rfloor}.
\]
Indeed the radical consists of the span of these \(V_c\), and
division by the unit \(f\) preserves it. Every displayed element is
still a unit: the inverse of the parenthesis is
\(1-\sum_c\tau_cV_c\). It has the same represented eigenvalues and
determinant as \(f\), because the parenthesis is \(I+B\) with
\(B^2=0\), commutes with \(f\), and has determinant one.

For any finite collection of prescribed closing coupons \(h_r\),
the exact observation vector is
\[
 L(h_rf_{\boldsymbol\tau})
       =L(h_rf)+\sum_c a_ch_r(c)f(c)\tau_c.
\]
Its affine image therefore has dimension
\(\operatorname{rank}(h_r(c))_{r,c}\), since every \(a_cf(c)\)
is nonzero. In particular, for a single closing unit \(h\) and
any double node \(c\), choosing
\[
          \tau_c=\frac{z_0-L(hf)}{a_ch(c)f(c)},
                         \qquad \tau_{c'}=0\ (c'\ne c)
\]
sets the prescribed observation equal to any \(z_0\in\mathbb C\),
including zero, while preserving all spectral values and invertibility.
This includes \(h=R^n\) for every fixed integer \(n\).

These changed coupons are not asserted to satisfy the Ward equations,
endpoint pointing, or fixed-expression constraints of an actual short
tangle. The calculation thus blocks an inference from unit spectral
data alone; it makes no assertion about the coefficient of a fixed
hyperbolic knot source.

The existing positive criteria remain the
[source-adapted composition criterion](research_source_adapted_observation_composition.md),
the [joint analytic sewing criterion](actual_six_port_analytic_sewing_criterion.md),
and [transport of the original top relative cycle](research_dominant_saddle_transport.md).
The exact external/Newton bridge transports their maps and prescribed
observations, but does not establish their source overlap, transverse
joint saddle, nonzero original contour intersection, or total
complementary-current gap for arbitrary fixed short components.
No stronger lower-bound implication is claimed here.

Only written mathematics is used. No numerical evaluation, test,
import, compilation, public-document edit, or frozen-proof edit was
performed.
