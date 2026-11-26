# Completing the prepared cap after coherent private contraction

Research proof, 7 November 2026. The literal first cap must remain
coherent when its three outer indices are deformed. Its existing
whole-source envelopes, combined with the fifteen successful saved
comparisons, control every outer alias, vertical correction and
zero-mode join. The failed private-face comparison is not used.
No new function, proposal, gain or supporting plane is evaluated.

This proves a local outgoing asymptotic for the original prepared
three-four cap. It is not a whole outgoing-period bound or a theorem
about arbitrary mixed words or knot families.

## 1. Original source and proved inputs

Use
\[
 G_N(y,w)=v_N(w)^TA_{3,N}A_{4,N}h_N(y),\qquad
 (y,w)=(x_0,-2),\qquad K=e^{2\pi ix_0},\quad\rho=|K|.
 \tag{1}
\]
The exact original source, including its scalar, is equation (2) of
[the coherent three-index sheet theorem](research_mixed_prepared_cap_three_index_sheet.md):
\[
 G_N=\kappa_N^3Nc_y
 \sum_{\substack{j+k<N\\k+l<N}}
 U_{0,N}(w,r^j)
 \frac{Y^lQ^{jk}P_{j+k}P_{k+l}}
 {P_jP_k^3P_l(Y;r)_{l+1}}.
 \tag{2}
\]
All indices are nonnegative, \(Y=e^{2\pi iy}\),
\(r=e^{-2\pi i/N}\), \(Q=r^{-1}\), \(P_j=(r;r)_j\),
and \(c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N)\).
The first factor is the entire original cap polynomial. No
terminating identity is substituted for it at a complex argument.

Put
\[
 \begin{split}
 C_3&=[.22,.5]\times[.2,.42]^2,\qquad z=(t,p,q),\\
 H_t&=[-.072,.021],\qquad H_p=H_q=[-.102,.015],\\
 E_c&=[.27,.49]+i[-.055,.04].
 \end{split}
 \tag{3}
\]
The original critical point \((s_*,z_*)\) exists strictly inside
the corresponding four-variable rectangle. Write
\(h_s=\Im s_*\), \(h=\Im z_*\), and
\(M=\Re\Phi_{\rm cap}(x_0,-2)\). In particular,
\[
 \Re t_*\in(.278,.391),\quad
 \Re p_*,\Re q_*\in(.24,.36),\quad
 h_s\in(-.019,.037).
 \tag{4}
\]
These are actual coupled reference coordinates.

Define the original phases
\[
 \begin{split}
 \Psi(s,t)&=S(s)+J(s+t)-J(t)-i\pi st,\\
 R(t,p,q)&=V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(x_0),\\
 V(a,b)&=g(a+b)-g(a)-g(b),\qquad F(s,z)=\Psi(s,t)+R(z).
 \end{split}
 \tag{5}
\]
All additive constants and logarithms are the original ones.
The [typed-height theorem](research_mixed_prepared_cap_typed_height_rectangle.md)
and [whole-rectangle gradient proof](research_mixed_prepared_cap_full_source_criterion.md)
give
\[
 -\Re F''\succeq\mu I_4,\qquad
 |\Im F_j|<2\pi\quad(j=s,t,p,q)
 \tag{6}
\]
on the full rectangle, for some \(\mu>0\). The sheet theorem
also proves \(-\Re R''\succeq\mu_R I_3\), \(\mu_R>0\),
on all of the outer tube in (3), including \(\Re t=.5\).

The same sheet theorem supplies the nonzero original main current
\[
 \mathcal M_N^{(3)}
  =\kappa_N^3N^{-1}\mathcal B_{\rm cap}(y,w)
        e^{N\Phi_{\rm cap}(y,w)}(1+O(N^{-1})),
       \qquad\mathcal B_{\rm cap}\ne0,
 \tag{7}
\]
and a physical-complement upper rate \(M-1/400+\eta\),
for every \(\eta>0\). These use the coherent cap in (2).

The [saved comparison assessment](research_mixed_prepared_cap_face_alias_attempt.md)
checks the immutable action record `271c82db...` and comparison record
`ad1b0c1b...`, including all source bindings. The six outer real faces
have gap \(>1/400\), and all eight original single-height aliases
have gap \(>1/20\). Also
\[
                 2.120165258<M<2.120165259.
 \tag{8}
\]
Only these already established rational inequalities are used below.
The old upper-\(s\) test remains a failed test of its old decomposition.

## 2. Literal cap envelopes and the true-endpoint reserve

The [hybrid-height envelope](research_mixed_boundary_window_real_color_envelopes.md),
equation (5), and its
[upper-target extension](research_mixed_cap_upper_target_extension.md),
Theorem 2, apply to every \(t\) in the full tube (3).
For **any** private main height \(v\in(-.055,.04)\), define
\[
 \begin{split}
 A_0(t;v)&=\max_{.27\le x\le.49}\Re\Psi(x+iv,t),\\
 A_L(t)&=\Re\Psi(.27,t),\qquad
 A_R(t)=\Re\Psi(.49,t),\\
 A_\pm(t)&=\max_{.27\le x\le.49}
       \Re\Psi(x+ih_{s,\pm},t)-2\pi|h_{s,\pm}|,\\
 h_{s,-}&=-.055,\qquad h_{s,+}=.04,\qquad
 A(t;v)=\max(A_0,A_L,A_R,A_-,A_+).
 \end{split}
 \tag{9}
\]
These are source profiles, not independently chosen geometric
references. The theorem is uniform for \(v\) in any fixed compact
subinterval of the private-height interval. In particular it permits
both \(v=0\) and \(v=\theta h_s\), \(0\le\theta\le1\),
with one uniform constant, by (4).

The separate true-index ceiling in that envelope may be sharpened
from \(3/4\) to \(37/50\) throughout the same tube. The lower
true end has ceiling \(1/4\). At the upper true end the original
finite-product estimate, including the revived rows, gives
\[
 \frac35+2\pi(\Im t)_+
      +\frac1{100}\log(40/19)<\frac{37}{50},
 \tag{10}
\]
because \((\Im t)_+\le21/1000\), \(\pi<22/7\), and
\(\log(40/19)<4/5\). Thus, with an arbitrarily small aggregate
rate tolerance, the literal whole cap obeys
\[
 |U_{0,N}(w,e^{-2\pi it})|
 \le C_\eta N^{a_\eta}
 \left[e^{N(A(t;v)+\eta)}
              +e^{N(37/50+\eta)}\right].
 \tag{11}
\]
The estimates retain the original ordinary-color neighborhood,
fixed jets, both parities, all private currents and both physical
tails. The real-color angular loss is unnecessary for this proof.

There is also the simpler real-private-index bound established in
[the outer-alias reduction](research_mixed_prepared_cap_outer_alias_reduction.md):
\[
 |U_{0,N}(w,e^{-2\pi it})|
 \le C_\eta N^{a_\eta}
 \left[
 e^{N\{\max_{.27\le s\le.49}\Re\Psi(s,t)+\eta\}}
             +e^{N(37/50+\eta)}\right].
 \tag{12}
\]
It expands the literal polynomial at complex \(t\), then uses the
coherent coefficient and zero-safe product bounds at real private
indices. It does not impose a false off-grid terminating support.
We use (12) for penalized lattice corrections and (11) for unpenalized
joins.

The constant term in either envelope has a uniform absolute reserve
after including the residual factor. On the real outer box the
elementary estimate in Section 3 of
[the terminating-chart tail theorem](research_mixed_prepared_cap_terminated_tails.md)
gives
\[
 \Re R<\frac56+
       \left(\frac12+\frac{21}{50}\right)\frac{13}{25}
        =\frac{4919}{3750}.
 \tag{13}
\]
For completeness, each supported real triangle
\(V_{\mathbb R}(a,b)=J(a+b)-J(a)-J(b)\) is less than
\(1/3\), and \(-J(p)<1/6\). The remaining incidence is
\(-\tfrac12\log\rho+L(q)\), where
\(L(q)\le q\log(\rho/(1-\rho))\). The inherited bounds
\(3/5<\rho<5/8\), \(q\le21/50\) and
\(\log(5/3)<13/25\) prove (13). Thus
\[
 \frac{37}{50}+\Re R(t,p,q)
   <\frac{37}{50}+\frac{4919}{3750}
    =\frac{7694}{3750}<M-\frac1{20}.
 \tag{14}
\]
The last inequality follows already from \(M>53/25\), a weaker
form of (8). This comparison imports neither the paired critical
action nor a far-region estimate outside its domain.

Finally, the residual phase obeys
\[
             |\Im R_j|<2\pi,\qquad j=t,p,q.
 \tag{15}
\]
For \(p,q\) these are the corresponding derivatives of \(F\).
For \(t\),
\(R_t=g'(t+p)-g'(t)+2\pi ip\); its three imaginary parts
divided by \(\pi\) belong to
\([-.84,.16]\), \([-.56,0]\), and \([.4,.84]\).
The original argument bounds are strict at their possible extrema,
so \(|\Im R_t|<\pi\). Consequently
\[
 W_R(x,v)=\Re R(x+iv)-2\pi\sum_j|v_j|
                   \le\Re R(x).
 \tag{16}
\]
The same height-reset property holds for \(F\) by (6).

## 3. All outer lattice corrections are paid

Let \(a_N(t,p,q;y,w)\) denote the exact interpolation of the
three-index row in (2), leaving \(U_{0,N}\) as its literal
polynomial. The remaining factors have rate \(\Re R\), with
uniform polynomial prefactors, on the whole tube (3). Their original
factorial arguments stay regular and \(|Y|,|Ye^{-2\pi iq}|<1\).

Apply the exact one-coordinate identity
\[
        \text{physical nodes}=I+A^-+A^++V
 \tag{17}
\]
from the [vertical-current regrouping](research_exact_vertical_current_regrouping.md),
with zero-frequency height zero. Its horizontal alias kernel has
modulus at most
\(e^{-2\pi N|h_{j,\pm}|}/(1-e^{-2\pi N|h_{j,\pm}|})\).
Its vertical kernel obeys
\(|w_{N,0}(v_j)|\le e^{-2\pi N|v_j|}\), and is supported on
one of the two real endpoints of that coordinate. The signed vertical
subtraction is retained before this bound.

Tensoring (17) yields \(4^3-1=63\) nonmain products, or
\(5^3-1=124\) after splitting vertical sides. In every product
the total exponential debit is exactly
\(2\pi\sum_{j=t,p,q}|v_j|\). Unused coordinates have height zero.
All finite alias denominators and polynomial residue factors are
retained.

For the regular part of (12), the exponent after this debit is
\[
 \max_{.27\le s\le.49}
 \{\Re F(s,x+iv)-2\pi\textstyle\sum_j|v_j|\}.
 \tag{18}
\]
If the product contains a vertical side, reset all its heights to
zero using (6). The real outer endpoint remains fixed. The result
belongs to one of the six saved outer physical faces, whose upper
rate is below \(M-1/400\). If all nonzero factors are horizontal
aliases, retain one nonzero outer height and reset all others. The
result is one of the six saved outer single-height aliases, whose
upper rate is below \(M-1/20\). This includes every one of the
\(3^3-1=26\) horizontal products.

For the constant part of (12), equations (14)--(16) give the same
uniform upper bound \(M-1/20\), for every product, with or without
a vertical side. Thus the complete outer lattice correction has
upper rate at most \(M-1/400+\eta\). No comparison at the failed
private upper face appears in this argument.

Equivalently, one may use (11) with private main height zero in
this step: its real cuts lie in (18), and its private aliases have
the additional original debit \(2\pi|h_{s,\pm}|\). Resetting
that private height gives the same bounds. This explicitly includes
the private currents if the five-profile envelope is used instead
of the shorter real-index estimate (12).

## 4. The unpenalized common-height joins are also paid

The zero-frequency three-index integral is translated from height
zero to \(h=\Im z_*\) using a single common parameter
\(0\le\theta\le1\). Its exact boundary currents lie on the
six outer real faces of \(C_3\), with outer height \(\theta h\).
They have **no** alias debit. We therefore use (11) with
\[
                     v=\theta h_s.
 \tag{19}
\]
This is a choice of a valid bound for the same literal polynomial
at each \(\theta\), not a new reference or a replacement of its
outgoing argument. Uniformity in (11) follows from (4).

Fix an outer face point \(x\in\partial C_3\). Every regular
profile, after adding \(\Re R(x+i\theta h)\), is a maximum of
functions of the following forms:
\[
 \begin{array}{ll}
 \Re F(s+i\theta h_s,x+i\theta h),& .27\le s\le.49,\\
 \Re F(c,x+i\theta h),&c=.27,.49,\\
 \Re F(s+ih_{s,\pm},x+i\theta h)-2\pi|h_{s,\pm}|,
                                          &.27\le s\le.49.
 \end{array}
 \tag{20}
\]
All these functions are convex in \(\theta\): their second
derivatives are \(-v^T\Re F''v\ge0\), using respectively the
full height vector \((h_s,h)\) or \((0,h)\). Their paths remain
inside the same original rectangle. Taking maxima preserves
convexity. The constant profile
\(37/50+\Re R(x+i\theta h)\) is convex for the same reason,
using \(-\Re R''>0\).

At \(\theta=0\), the first two rows of (20) are bounded by the
six saved outer physical faces, with gap \(>1/400\). The last
row is bounded by the saved private single-height alias on the
full four-dimensional real box, with gap \(>1/20\). Its outer
face restriction only reduces the maximum. Equation (14) supplies
gap \(>1/20\) for the constant profile.

At \(\theta=1\), use the original own-three supporting plane.
Let \(T(t)=\mathcal T_0(t,-2)\) and
\[
 B(t_R)=\Re T(t_*)+\Re T'(t_*)(t_R-\Re t_*)
                   -\frac{(t_R-\Re t_*)^2}{2500000}.
 \tag{21}
\]
Its source eligibility is proved in Section 2 of the sheet theorem:
the actual external input \(p_*\) belongs to the reduced type-four
disk, and the additional oriented/inverse exclusions concern only
an own-four cap. The
[upper-target completion](research_mixed_cap_upper_target_completion.md)
therefore bounds **each** regular profile in (9), at its original
private main height \(h_s\) and outgoing height \(h_t\), by
\(B(t_R)\). It also proves \(B(t_R)>149/200\), so
\[
                      37/50<B(t_R)-1/200.
 \tag{22}
\]
In particular the constant ceiling is not incorrectly compared as
\(3/4< B\).

The original stationary identities and the strict residual curvature
give the sheet inequality
\[
 B(t_R)+\Re R(x+ih)
 \le M-\frac{\mu_R}{2}\|x-\Re z_*\|^2
       -\frac{(t_R-\Re t_*)^2}{2500000}.
 \tag{23}
\]
By (4), every point on an outer real face is at distance greater
than \(1/25\) from \(\Re z_*\). Thus every profile at
\(\theta=1\) has gap at least \(\mu_R/1250>0\), with
an additional reserve for the constant profile.

Convex interpolation between these two endpoints now gives the
uniform join gap
\[
          \delta_J=\min\{1/400,\mu_R/1250\}>0.
 \tag{24}
\]
This is a convexity argument for the explicit original source
profiles. It does not assert that \(\log|U_{0,N}|\) is convex in
height, or that two horizontal bounds alone control an arbitrary
holomorphic function on an incomplete rectangle. All real side
data have been supplied by the six original outer faces and the
actual-height supporting plane.

## 5. Whole prepared source and exact scope

Choose the same half-grid cuts as in the original residue proof.
They differ from (3) by \(O(N^{-1})\); strict compact-domain
margins absorb these shifts. The exact central physical sum equals
its zero-height integral plus the 63 lattice corrections. Stokes'
formula for common-height translation writes that integral as the
main sheet plus its six oriented boundary currents. Their signs,
Jacobian factors and all residue constants are unchanged. Hence,
with a common positive \(\delta\), Sections 3--4 and the proved
physical-complement estimate give
\[
       G_N(y,w)=\mathcal M_N^{(3)}(y,w)
                   +O\!\left(N^A e^{N(\Re\Phi_{\rm cap}(y,w)-\delta)}\right).
 \tag{25}
\]
Allocate one total source tolerance smaller than the minimum of
the positive margins. Holomorphy, zero-safe product estimates and
compactness preserve the bounds on a sufficiently small fixed
joint neighborhood of \((x_0,-2)\). The local main packet has
the original action, nonzero symbol and normalization in (7).
Consequently
\[
 \boxed{\displaystyle
 v_N(w)^TA_{3,N}A_{4,N}h_N(y)
 =\kappa_N^3N^{-1}\mathcal B_{\rm cap}(y,w)
     e^{N\Phi_{\rm cap}(y,w)}(1+O(N^{-1})),
       \qquad\mathcal B_{\rm cap}\ne0.}
 \tag{26}
\]
The normalized relative error is holomorphic and has the inherited
uniform fixed-derivative bounds on smaller neighborhoods. Both
level parities and all fixed ordinary-color jets are retained.
No nonzero leading coefficient is asserted for an arbitrary
outgoing derivative whose differentiated phase might vanish.

The original sixteen-case record remains inconclusive for its
four-index absolute-tail decomposition. Equation (26) follows
from a different exact grouping of the same finite source and
does not reclassify that failed comparison. It is local in the
outgoing Fourier parameter; whole-period weighted propagation,
arbitrary attachments, mixed-word source closure and cofinite
partial-filling conclusions remain separate obligations.

## 6. The reusable contour implication

**Proposition.** Let an exact finite outer lattice source in a fixed
number of coordinates have a holomorphic literal first factor
\(U_N(t)\) and a regular residual factor of phase \(R\). Suppose:

1. The literal factor has a uniform five-profile envelope of the form
   (9)--(11), with an arbitrary private main height in a fixed compact
   interval containing zero and the actual private critical height,
   and a separate constant true-end ceiling \(c\).
2. Its original regular phase \(F=\Psi+R\) and residual phase have
   strictly negative real Hessians on the required height rectangles.
   Their imaginary gradient components have modulus below \(2\pi\).
3. At the actual outer critical heights, a common supporting plane
   bounds every regular private profile and exceeds \(c\) by a
   positive margin. Its full original marginal cancels the residual
   marginal, leaving strict quadratic decay from the critical point
   on the entire outer real box, hence a uniform gap on its faces.
4. The real outer faces, the outer single-height aliases, and the
   private single-height aliases at zero outer heights have strict
   gaps below the same actual action. The real outer box also obeys
   \(c+\Re R<M\) with a uniform gap.
5. The actual outer physical complement has a strict bound, and near
   the critical point the coherent source has its original nonzero
   local saddle packet. Hypothesis 3 controls the rest of its main sheet.

Then the whole exact source has that packet, with an exponentially
smaller complementary error. All current kernels must be the original
ones in (17), and their finite denominators and vertical subtractions
must be retained.

*Proof.* For every penalized lattice correction choose private main
height zero in the five-profile envelope. Height resets give the
outer-face or outer-single-alias bounds, while its private aliases
are reset with their additional penalties. The constant part is
paid by \(c+\Re R\) on the real box. For the unpenalized joins
choose private height \(\theta h_s\). Convexity of the explicit
profiles gives their endpoint bounds at \(\theta=0,1\), exactly
as in (20)--(24). The finite tensor identity, physical-complement
bound and local packet then give (25). This argument requires no
absolute bound on an artificial private real face independent of
the outer variables. \(\square\)

In the present application all five hypotheses are proved above and
in the cited source theorems. For a longer source they are specific
obligations, not consequences of its formal phase or of agreement
at the critical point.
