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

## Appendix R: the unchanged matched pair in the explicit core

In Section R.8, printed page 356 (page 369 of the PDF), immediately
after equation (R.39), the sentence
“The other unchanged region has positive outer weights” describes the
wrong support. The outer weights are \((2,0)\), and the two middle
weights are \((1,1)\). This is the pair of triangles \(T_3,Z_3\),
whose common edge is \(v_3v_0\). Equation (R.36) assigns curvatures
\(v_3=2\), \(v_0=0\), and \(P=S=1\).

The required strict inequalities still hold, with quantitative bounds.
To see this directly, use the triangle potential \(Q\) defined in
equation (R.3), and write

\[
 f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
 \qquad g=f(1/4),
 \qquad \Lambda(s)=-\int_0^s\log(2\sin r)\,dr.
\]

For weights \((2,1,0)\), the admissible loads
\((1/4,1/4,0)\) give

\[
 Q(2,1,0)\ge 2g+\tfrac14\log2.
\]

Both triangles have those weights, so their complete rate satisfies
\(X=2Q(2,1,0)\ge4g+\tfrac12\log2\). Each overloaded middle
has weight \(h=1\). Its pure-middle comparison is therefore
\(X-\log h=X\), and its mixed comparison satisfies

\[
 Q(2,h,0)-\tfrac12\log h
 \ge 2g+\tfrac14\log2>\frac3{50}.
\]

The last inequality follows already from the stronger comparison
\(2g-\tfrac34\log2>3/50\) in (R.39). Thus this correction
preserves the stated uniform core gap and the insertion theorem.
It changes neither the matching nor the protected zero weight.
The corrected description and its branch bounds appear in Section 9
of [the triangular-insertion paper](../papers/triangular-insertion/main.tex),
after equation (9.5) and in the table following (9.10). The
[insertion audit](../repro/PLANAR_INSERTION_AUDIT.md) also records
the correction.
