# Corrections to the frozen reference manuscript

These corrections apply to the 374-page [reference PDF](build/main.pdf),
whose SHA-256 is
`e5b384c8fd103c1e1e7209ac97b3862b71abe227f8dc82e49dc0465bf4ae5437`.
The PDF and its TeX sources remain frozen while the results are rewritten
as separate papers. This file records corrections without silently
changing the version that earlier citations refer to.

## Appendix D: the derivative of the filling equations

In Section D.4.3, printed page 127 (page 140 of the PDF), the Jacobian of
the equations

\[
 V_\ell(\chi)+r_\ell U_\ell(\chi)=-2\pi i r_\ell
\]

with respect to \(\chi\), at \(\chi=r=0\), is

\[
 -2\pi i\,\operatorname{diag}(\tau_\ell),
\]

not the printed \(-4\pi i\,\operatorname{diag}(\tau_\ell)\).

Here \(U_\ell=-2\pi i\chi_\ell\),
\(V_\ell=-2\partial_{\chi_\ell}\Phi_\varepsilon\), and
\(\tau_\ell=2ic_\ell/(1-\varepsilon_\ell ic_\ell)\), where
\(c_\ell=\cot(\pi a_\ell)\). Direct differentiation of the leaf
potential gives

\[
 \partial_{\chi_\ell}^2\Phi_\varepsilon(0)
 =\frac{-2\pi c_\ell}{1-\varepsilon_\ell ic_\ell}
 =\pi i\tau_\ell.
\]

The mixed derivatives between an internal edge variable and a leaf
deformation vanish at the complete point. Eliminating the internal
stationary variables therefore leaves this diagonal Hessian unchanged.
Differentiating \(V=-2\nabla\Phi_\varepsilon\) yields the corrected
Jacobian. This also agrees with the complete Hessian in equation (B.41).

The matrix remains invertible because each \(\operatorname{Im}\tau_\ell\)
is positive. The implicit-function argument and its conclusion about
independently sufficiently long signed filling slopes are unchanged.
This correction concerns that classical deformation argument; it supplies
no estimate for the quantum invariant.
