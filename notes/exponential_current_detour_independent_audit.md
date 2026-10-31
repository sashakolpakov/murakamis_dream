# Independent audit of the exponential compact-current detour

Audit, 27 October 2026. The revised proof in
[compact_exponential_cech_current_detour.md](compact_exponential_cech_current_detour.md)
passes its whole-form, relative-source and normal-pole checks.
The algebraic-to-holomorphic domain qualification added during
this audit is necessary.

The exponential fibre map has the correct south expression,
fixes the base, and is holomorphic on the whole compact source
for the stated nonresonant parameters. The affine-fibre difference
transforms linearly, so
\[
 B_{C,\lambda}=
  -\left[\int_a^{a_\lambda}f_C(v,b)\,db\right]dv
\]
is global and differentiates to
\(\Phi_\lambda^*(f_C\,dv\wedge da)-f_C\,dv\wedge da\).
The sign follows from \(d(-F\,dv)=F_a\,dv\wedge da\).
The identity matrix formula and normalized compact trace agree.

The interpolation \(a+\tau(a_\lambda-a)\) is global in the affine
torsor, fixes the deleted base fibre, and gives the printed Cartan
operator on both \(X\) and its affine complement. In the support
cone with differential
\(D(\alpha,\beta)=(d\alpha,\alpha|-d\beta)\),
\[
 \Phi_\lambda^*(\alpha_C,\beta_C)-(\alpha_C,\beta_C)
      =D(B_{C,\lambda},-K_\lambda\beta_C)
\]
has the correct second-component sign:
it is \(B_{C,\lambda}+dK_\lambda\beta_C\).
This retains the explicit polar-fibre primitive and source residue.

Near resonance, \(a_\lambda=\eta_{\mathrm{phys}}/k+a e^{-cT}+O(k)\)
and the printed Jacobian expansion follow from
\(e^{-c\lambda T}=e^{-cT}(1-k)^T\).
Since \(f_C\) has degree at most \(n\) in \(a\), its
antiderivative and the relative homotopy have pole order at most
\(n+1=N\). The chosen affine primitive has the same degree bound.
Comparing Laurent coefficients proves that every negative
coefficient is relatively exact and the finite part retains the
original source class. This assumes the matrix coefficients are
fixed or regular in this auxiliary normal, as the note states.
Meridian-coupled coefficient poles require their additional
chain-rule and divisor contributions.

The important domain repair is explicit in the revised note:
\(\Phi_\lambda\) is holomorphic exponential, so it maps the
algebraic support complex into a holomorphic or specified
whole exponential-period complex. It is not an algebraic
endomorphism of the original complex. Its normal coefficients
and finite-part forms can be nonalgebraic. Consequently this
identity does not invoke the bounded algebraic cyclotomic
reconstruction theorem.

The note correctly also keeps the two clocks distinct. The physical
clock at the pulled-back compact point is
\(e^{cva_\lambda}\), while the meridian detour clock is
\(h_\lambda/u_\lambda\). Their equality, a star-product
intertwiner, and actual quantum dressing are not proved by
the current homotopy. Nor does it identify the Gaussian
coefficient map or select a nonzero full geometric period.
