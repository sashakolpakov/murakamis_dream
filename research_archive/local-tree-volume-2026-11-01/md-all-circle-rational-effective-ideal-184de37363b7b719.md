# The finite rational equations for the all-circle effective action

1 November 2026. This derivation concerns the exact filtered phase of
the physical source, not yet a nonparabolic geometric realization.

Use t for the scaled main parameter, M=exp(pi i t),
E_e=exp(2pi i x_e), and Q_v=exp(i tau_v). All logarithms are the
ones continued from the selected filled saddle at t=0. The local
incidence phase is
\[
 b(x,\tau)=\int_0^x\log(2\cos(2\pi z)+2\cos\tau)\,dz-2J(x).
\]
Its derivative in x gives
\[
 \exp b_x=-\frac{(E+Q)(E+Q^{-1})}{(E-1)^2}.
\]
For the angular derivative put y=tan(pi z), p=tan(tau/2).
Integration gives
\[
 b_\tau=-\pi^{-1}\operatorname{artanh}
                    \bigl(p\tan(\pi x)\bigr),\qquad
 \exp(-2\pi b_\tau)=\frac{Q+E}{1+QE}.
\]
The inverse hyperbolic tangent is its branch at tau=0; the integral
fixes its continuation. The rational equality does not replace
that logarithm marking.

The main-parameter perturbation is
\[
 K(x,t)=2J(x)-J(x+t)-J(x-t).
\]
The sine identities give
\[
 e^{K_x}=\frac{(1-E)^2}{(1-EM^2)(1-E/M^2)},\qquad
 e^{K_t}=\frac{M^2-E}{1-M^2E}.
\]
Consequently the exponentiated stationary equation at the edge
e=vw is
\[
 (E_e+Q_v)(E_e+Q_v^{-1})
 (E_e+Q_w)(E_e+Q_w^{-1})
 =(E_e-1)^2(1-E_eM^2)(1-E_e/M^2).
\]
The angular stationary equation includes the original first charge:
\[
 \sum_{e\ni v}b_{\tau_v}+\frac{in_v\tau_v}{2\pi}=i.
\]
Exponentiating its negative 2pi multiple gives
\[
 \prod_{e\ni v}\frac{Q_v+E_e}{1+Q_vE_e}=Q_v^{n_v}.
\]
At the selected analytic critical point, the effective longitude is
\[
 L_{\mathrm{eff}}
 =-M^{a(D)}\prod_e\frac{M^2-E_e}{1-M^2E_e}.
\]
These equations are finite and rational. Denominators are nonzero
at the complete local configuration E=i, Q=1, M=1 and on a
sufficiently small neighborhood of the selected small filling.
Clearing denominators is justified only after restricting to this
regular open set or saturating by their product. The analytic
first-charge marking selects a germ of the algebraic solution set;
the exponentiated equations alone admit other branches.

The effective phase is even in t. Its unique local stationary point
therefore satisfies E_e(M^{-1})=E_e(M) and Q_v(M^{-1})=Q_v(M).
The longitude satisfies
\[
 L_{\mathrm{eff}}(M^{-1})=L_{\mathrm{eff}}(M)^{-1}.
\]
In particular the irreducible Laurent polynomial of the selected
curve is reciprocal up to a nonzero monomial factor.

At M=1, L_eff=-1. Differentiating with u=log M gives
\[
 \frac{d\log(-L_{\mathrm{eff}})}{du}\bigg|_0
 =a(D)+2\sum_e\frac{1+E_e}{1-E_e}
 =a(D)+2i\sum_e\cot(\pi x_e)=\tau_K.
\]
This verifies the cusp tangent and the scalar convention.

A useful next geometric problem is local: realize the edge equation
as the marked nonparabolic deformation of the original two-octahedron
piece, and identify its main and crossing-circle holonomies with the
displayed rational products. Such a realization would respect the
existing tree gluing. It is not proved here. Agreement at M=1 and
agreement of the cusp tangent do not establish it.
