# Original crossing identities exclude the wrong parabolic transport

Research note, 6 November 2026.

There is a source-specific alternative to assuming that an eigenvalue
critical scheme is saturated. The complete generator identities of an
original signed crossing power constrain any regular formal kernel
packet of that power. At a noncentral parabolic pair product they retain
the additive transport coefficient. A packet with the wrong coefficient
has zero aggregate formal amplitude.

This is a local formal statement about the **whole original kernel**.
It neither bounds its global remainder nor deletes a stationary point
from an arbitrary integral presentation.

## 1. A formal exclusion using exact source equations

Use the original polynomial head realization of the finite crossing
kernel, with the actual dual convention on its input. Put
\(h=2\pi i/N\). On a regular chart a finite quantum shift acts on a
formal packet
\[
       {\cal K}_h=\exp(S/h)\sum_{r\ge0}h^{r+\nu}a_r
 \tag{1}
\]
by its principal multiplier followed by a formal differential series.
The exponent \(\nu\) may be fixed and nonintegral. All coefficients
below are those of the original operator identities. An arbitrary
continued-index interpolation agreeing only at the finite grid is
not assumed to satisfy them.

Suppose an exact kernel identity is \(L_h{\cal K}_h=0\), and its
principal symbol on the phase graph is a scalar \(\ell\). If
\(\ell\) is invertible on the chart, every \(a_r\) in (1) vanishes.
Indeed the leading equation is \(\ell a_0=0\); after the earlier
coefficients vanish, the order-\(r\) equation is \(\ell a_r=0\).
Cleared rational operator identities may be used provided the
cleared factors have invertible principal symbols on this chart.

The same conclusion applies if several stationary contributions
assemble the **same formal phase sector**: it concerns their summed
amplitude. It does not imply that each separate contour contribution
vanishes. Phases identified by an exact root-level alias must be
grouped before applying the statement. Nor does this argument infer
an analytic exponential bound from a zero formal series.

## 2. The exact identities used for an original signed power

For the actual crossing, rational conjugation on all six generators
\(K_i,E_i,F_i\) is proved, with the specified multiplication order, in
[regular holonomy braiding, Section 1](regular_holonomy_braiding.md).
Its inverse is explicit. These are original intertwining identities,
not consequences of a Casimir eigenvalue equation. For each fixed
signed integer \(n\), composition gives the corresponding exact
identities for \(R^n\), on their retained localization.

The polynomial head realization is an exact realization of these
identities. When acting on a regular formal kernel germ, their
commutative principal symbols give the canonical crossing relation.
The original Borel prefix construction in
[marked braid holonomy, Sections 4--5](marked_braid_holonomy.md)
identifies that relation with forward Hurwitz transport
\[
 {\cal H}(A,B)=(A^{-1}BA,A),\qquad P=BA.
 \tag{2}
\]
The inverse point map associated to quantum pullback is not an
opposite physical crossing: passing from pullback to the kernel's
input-output relation accounts for that inverse. Negative powers use
the inverse of (2).

Consequently, if a proposed regular formal packet for the original
\(R^n\) kernel has input and output meridian symbols violating
\({\cal H}^n\), at least one original generator identity has nonzero
principal symbol. After shrinking the chart it is invertible, and
Section 1 excludes that aggregate packet to every formal order.
This argument requires the original localized identities to act on
the germ. A crossed pole, an endpoint correction, or a different
interpolation's unsupported shift rule is not silently included.

## 3. The additive transport for every signed power

Let \(A,B\in\mathrm{SL}_2(\mathbb C)\) have trace \(-2\), retain the
original ordered product \(P=BA\), and assume the original regular
pair chart. Direct multiplication in (2) gives
\[
                  {\cal H}^2(A,B)
                       =(P^{-1}AP,P^{-1}BP).
 \tag{3}
\]
On the chart where \(D=P^{-1}-I\) is invertible, the trace-\(-2\)
pair identity used by the original coupon is
\[
                  {\cal H}(A,B)=(DAD^{-1},DBD^{-1}).
 \tag{4}
\]
The determinant of \(D\) is \(2-\operatorname{tr}P\), so this
localization includes every noncentral parabolic product of trace
\(-2\). Moreover
\[
                        D^2=(\operatorname{tr}P-2)P^{-1}.
 \tag{5}
\]
For \(n=\epsilon-2p\), with \(p\in\mathbb Z\) and
\(\epsilon\in\{0,1,-1\}\) of the appropriate parity, (3)--(5) yield
the simultaneous projective conjugator
\[
                             D^\epsilon P^p.
 \tag{6}
\]
This is valid for negative powers as well.

Now specialize to \(P=-I+H\), \(H\ne0\), \(H^2=0\). Then
\[
 D=-2I-H,\qquad
 D^\epsilon P^p\sim I+(\epsilon/2-p)H.
 \tag{7}
\]
On the original regular noncentral pair chart, two centralizers of
\(P\) giving the same transport of \(A\) differ by a scalar.
Here that fact is algebraic on the entire stated parabolic pair
locus. Cayley--Hamilton gives
\(\operatorname{tr}(PA)=\operatorname{tr}(BA^2)=6\), whence
\(\operatorname{tr}(HA)=4\) and
\(\operatorname{tr}([H,A]^2)=32\). A centralizer \(uI+vH\)
commuting also with \(A\) therefore has \(v=0\). This is the
explicit unit minor used in
[the critical-scheme theorem, Section 4](actual_augmented_plat_critical_scheme.md),
now with its assumptions displayed.
Thus a coupon transport \(I+cH\) agrees with the original power
precisely when
\[
                              c=\epsilon/2-p.
 \tag{8}
\]
The choice of \(\epsilon\) for a fixed odd \(n\) does not affect
\(\epsilon/2-p=n/2\).

**Corollary.** A regular formal kernel packet of the whole original
signed power \(R^n\), in the chart above, cannot have nonzero aggregate
amplitude with \(c\ne n/2\). This is imposed by the original generator
equations, without replacing its critical scheme by a saturation.

For the rational original q-Hahn coupon in
[the critical-scope note](research_global_filled_critical_scope.md),
\(c=17/12\), which differs from \(n/2\) for every integer \(n\).
If such a component appears in an alternative representation of the
same filled power kernel, it therefore cannot by itself give a
nonzero regular formal packet of that kernel. It must cancel in its
phase sector, fail the asserted kernel asymptotic, or belong to a
singular/nonuniform source regime outside this lemma. This is not a
claim that the unfilled complete-circle coupon itself is zero.

## 4. What this settles, and the remaining analytic obligation

The condition in (8) is exactly the additive equation recovered by
[matrix saturation](research_saturated_matrix_filling.md). Here it
comes instead from the actual \(R^n\) generator identities, so no
vertical component is removed merely because it lies on a unit
longitude.

To use the criterion on a proposed collapsed finite-source
decomposition, one must still prove that its assembled local sector
has an expansion of the whole original kernel to which those identities
apply. A local saddle calculation of one summand is insufficient.
Exact equality of finite sources supplies the identities for their
total, but not their separate pieces. The criterion identifies the
necessary aggregate cancellation; it does not estimate its cost,
control source ends, or produce the nonzero coefficient of the allowed
geometric component.

All powers are fixed before \(N\to\infty\). No numerical calculation,
new source interpolation, or change of the original invariant is used.
