# Matrix filling on the closure of the nonunit longitude locus

Research note, 6 November 2026.

The full matrix filling equation extends across a unit longitude on the
scheme-theoretic closure of the nonunit filling locus. This repairs the
eigenvalue argument on components which actually meet that locus. It
does not justify removing components supported entirely on unit
longitudes from an original quantum source.

The saturation here concerns the **primitive peripheral filling
equation**. It is distinct from the already proved
[critical-regulator shape compactification](saturated_critical_regulator_compactification.md).

## 1. A matrix relation extends on the saturated scheme

Let \(A\) be a finitely generated complex algebra with regular commuting
matrices \(P,C\in\mathrm{GL}_2(A)\). Work on a specified longitude
eigenvalue cover, with \(P\in\mathrm{SL}_2(A)\),
\[
 \lambda\in A^\times,\qquad
 \operatorname{tr}P=\lambda+\lambda^{-1},\qquad
 \Delta=\lambda-\lambda^{-1}.
 \tag{1}
\]
Fix an integer \(p\). Suppose a specified ideal \(I\) imposes the
correctly oriented filling eigenratio equation and, after inverting
\(\Delta\), that equation gives \(CP^p\) scalar. Set
\[
                         I^{\rm sat}=I:\Delta^\infty .
 \tag{2}
\]
Then \(CP^p\) is scalar over \(A/I^{\rm sat}\), including its
nonreduced structure. Indeed its two off-diagonal entries and the
difference of its diagonal entries vanish in \((A/I)_\Delta\).
Each entry is therefore killed by some power of \(\Delta\) modulo
\(I\), and belongs to (2). Negative \(p\) cause no difficulty because
\(P^{-1}\) is regular.

This is precisely the scheme-theoretic closure of the nonunit locus
inside \(\operatorname{Spec}(A/I)\), not a new equation deduced from
eigenvalues at \(\Delta=0\) alone. Equivalently, multiplication by
\(\Delta\) is injective on its coordinate ring. If determinant-one
lifts are used, the resulting scalar is locally \(+I\) or \(-I\);
both give the identity in PSL.

In particular a **reduced irreducible component not contained in**
\(\{\Delta=0\}\), on which the generic eigenratio equation holds,
satisfies the matrix filling relation everywhere. For several filled
cusps, use the product of their \(\Delta\)'s. Reducedness alone without
the noncontainment condition is insufficient. Generic validity on the
reduced points of a nonreduced component is also insufficient for a
scheme-level conclusion; (2) supplies the needed torsion condition.

## 2. The undivided equation in a noncentral commutant chart

Suppose \(P\) remains noncentral on the chart in question. Locally its
commutant is the free span of \(I,P\); this follows by solving the
commutator equations using a nonzero off-diagonal entry, or a nonzero
diagonal difference. Put
\[
 Q=P-\lambda^{-1}I,\qquad Q^2=\Delta Q,\qquad
 C=uI+vQ .
 \tag{3}
\]
Invertibility of \(C\) makes both \(u\) and \(u+v\Delta\) units.
For every signed integer \(p\), the expression
\[
 L_p(\lambda)=\frac{\lambda^p-\lambda^{-p}}{\lambda-\lambda^{-1}}
 \tag{4}
\]
is a Laurent polynomial: for \(p>0\) it is
\(\lambda^{p-1}+\lambda^{p-3}+\cdots+\lambda^{1-p}\);
\(L_0=0\) and \(L_{-p}=-L_p\). Cayley--Hamilton now gives
\[
 \begin{split}
 P^p&=\lambda^{-p}I+L_pQ,\\
 CP^p&=u\lambda^{-p}I+T_pQ,\qquad
 T_p=uL_p+v\lambda^p .
 \end{split}
 \tag{5}
\]
The difference between the two filling eigenvalues is exactly
\[
 (u+v\Delta)\lambda^p-u\lambda^{-p}
                         =\Delta T_p.
 \tag{6}
\]
On the noncentral chart, the matrix relation is \(T_p=0\).
Thus (6) displays explicitly what saturation retains.

At \(\lambda=\sigma\in\{1,-1\}\), write
\(P=\sigma I+H\), \(H\ne0\), \(H^2=0\). Formula (4) gives
\[
 L_p(\sigma)=p\sigma^{p-1},\qquad
 T_p(\sigma)=\sigma^p(v+p\sigma u).
 \tag{7}
\]
The additive filling equation is therefore \(v+p\sigma u=0\).
For the original endpoint convention \(\sigma=-1\) and
\(C_{\rm aux}=I+(\epsilon/2-c)H\), it is
\[
                              c+p-\epsilon/2=0.
 \tag{8}
\]
The formulas for this actual auxiliary meridian and primitive
longitude are established in
[the endpoint regulator, Section 3](actual_augmented_plat_endpoint_regulator.md).
No centralizer is selected merely from an eigenvalue.

At a central \(P\), formula (3) need not describe the entire commutant.
The general matrix-ideal argument in Section 1 still applies there;
the noncentral coordinate calculation is not being used outside its
domain.

## 3. A transverse normal condition is sufficient, but not automatic

Let a family of peripheral data have
\(\lambda=\sigma+\varepsilon\) over
\(\mathbb C[\varepsilon]/(\varepsilon^2)\), with the same conventions
as (3). Since \(\Delta=2\varepsilon\) modulo \(\varepsilon^2\),
equation (6) to first order forces
\[
                              T_p(\sigma)=0.
 \tag{9}
\]
Arbitrary first variations of \(u,v\) do not alter this conclusion:
they multiply \(\Delta(0)=0\). A first-order *solution of the filling
equations transverse to the longitude divisor* thus suffices.
Retaining a derivative coefficient of a quantum source is a different
statement.

The actual q-Hahn root chart makes the distinction explicit. Its
original normalized conjugator has eigenratio \(R_0\), and
[the channel-Hessian calculation, Section 2](actual_augmented_plat_channel_hessian.md)
proves, following the chosen simple internal roots,
\[
 R_0|_{J=-1}=1,\qquad
 \left.\frac{dR_0}{dJ}\right|_{J=-1}=2c .
 \tag{10}
\]
For \(n=\epsilon-2p\), the scalar primitive filling equation is
\[
 F_p(J)=R_0(J)(-J)^n-1=0,\qquad
 F_p'(-1)=2(c+p-\epsilon/2).
 \tag{11}
\]
This follows from the literal auxiliary eigenratio
\(R_0(-J)^\epsilon\) and multiplication by the longitude to power \(p\);
it is not a claim identifying an unspecified quantum filling
interpolation.

The endpoint equation \(F_p(-1)=0\) holds identically on its magnetic
root chart. If the right side of (11) is nonzero, locally
\[
                         F_p=(J+1)\times\text{unit}.
 \tag{12}
\]
Such a point belongs only to the unit-longitude part of this local
eigenvalue scheme; it is absent from the closure of its nonunit part.
The factor in (12) occurs in the original regular eigenratio equation,
not from clearing a forbidden denominator. Saturation removes a genuine
component of that scalar equation; a source argument is needed to
justify removing its contribution.
The rational coupon in
[the critical-scope note](research_global_filled_critical_scope.md)
has \(c=17/12\), so (12) holds for every integer \(p\) and every allowed
\(\epsilon\). This identifies the obstruction as a vertical component,
rather than an ambiguous limit of correctly filled matrices.

The original full-normal source does not already impose (9) or
\(F_p'(-1)=0\). Its Hermite data are derivatives of finite source
coefficients in the Casimir variable
\[
 \Omega=J+J^{-1},\qquad \Omega+2=\frac{(J+1)^2}{J}.
 \tag{13}
\]
That coordinate is ramified at \(J=-1\); it is not a prescribed
transverse solution of the stationary equations. The
[complete marked-density formula](actual_augmented_plat_local_marked_density.md),
Section 1, retains the full circle normal explicitly and has nonzero
endpoint coefficients at both level parities. Its actual stationary
normal response is the channel Hessian, not an extra equation setting
that Hessian or (11) to zero.

Likewise the saturated integer incidence lattice in
[the local critical-scheme theorem](actual_augmented_plat_critical_scheme.md),
Section 2, reconstructs shared wire momenta. It is not saturation of
the filling ideal by \(J^2-1\). That theorem fixes its local geometric
germ and does not assert the latter global saturation.

## 4. The resulting valid extension and the remaining source question

Consider a reduced irreducible component of a collapsed, correctly
marked regular critical scheme. Suppose:

- its actual peripheral matrices are regular on the component;
- every filled longitude is generically nonunit;
- on that dense open locus, the original equations impose the full
  primitive filling eigenratio and have the calibrated action-volume
  identity.

The matrix filling relations then hold on the whole component by
Section 1, including regular unit-longitude points. Thus the
representation descends to the same final filled group there.
If the original action, marked shapes and representation-volume
normalization extend continuously at such a point, the same
action-volume identity follows by continuity from the dense locus.
This last continuity is an explicit additional hypothesis at a
singular phase chart, not a consequence of matrix saturation.

This removes the unit-longitude exclusion on the stated generic
components. Components supported entirely on one of the unit
divisors remain separate. To use the extension for the whole original
source, one must prove that its relevant critical scheme is the
saturated scheme, or retain and analyze those other components with
their actual amplitudes and source cycles. Neither full-normal
retention, the local geometric scheme theorem, nor equality of two
finite quantum formulas supplies that conclusion automatically.

No vertical component is discarded here, and no lower bound or
whole-source asymptotic is inferred.
