# The complete symmetric 343 kernel and its two ordinary boundaries

Private finite-source assembly, 10 November 2026.
The conclusion concerns the exact ordinary two-boundary
polynomial for the selected path \(343\). It retains the original
trace normalization, its nonzero full-source packet, both whole real
boundary periods, and the marked boundary germ. It does not identify
this polynomial with an arbitrarily chosen knot invariant, permit
arbitrary adjacent short compositions, or prove finite exceptions.
No mathematical numerical evaluation is used.

**Theorem.** The exact polynomial (2) has the full nonzero
ordinary-bidisk asymptotic (17), with its original scalar and
all fixed normalized derivatives. Its entire two real boundary
periods satisfy the calibrated angular bound (18), with
\(\mathcal L_N\) there replaced by \(Z_N\), and hence the
quadratic complex-strip estimate (21). Its angular boundary
Hessian is (20). The original marked geometric boundary germ
and complete-point volume calibration are retained in Section 5.
Consequently this kernel satisfies the hypotheses of the
existing finite two-boundary kernel induction. The exact
additional short-block operation that induction permits is
stated in (25); the intervening and final powers must be
sufficiently long as specified there.

## 1. Original polynomial and local contribution

Keep
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad
 C_{N,n}=q^{nD^2/4},\\
 \phi_N(f)=\eta_NN^2[x^D]\operatorname{rem}_{2T_N(x/2)+2}f,
 \qquad v(w)=(e_0(w),\ldots,e_D(w))^T,\quad A_n=JM^n,\\
 Q_N(w,u)=\phi_N^{(x)}
   [R_N(x)^3K_N(w,x)K_N(x,-2\cos u)] .
\end{gathered}                                                       \tag{1}
\]
The exact symmetric contraction is
\[
 Z_N(w_L,w_R)=v(w_L)^TA_3A_4A_3v(w_R)
       =\phi_N^{(z)}
          [R_N(z)^4Q_N(w_L,z)Q_N(w_R,z)] .
 \tag{2}
\]
In the second expression \(Q_N(w,z)\) denotes the ordinary
outgoing polynomial, evaluated angularly by (1). This is
[the original full identity](research_mixed_symmetric_343_closing_trace_and_domain.md),
not a cyclic matrix trace or a value-only quadrature.
Its separate ordinary degrees in \(w_L,w_R\) are at most \(D\).
All double-root normals and the odd simple node remain.

Let \(t_g,u_g=\beta_g-iK_g\) be the actual original positive
geometric solution. The adopted local outer theorem gives
\[
 0<\beta_g<\pi/2,\qquad17/30<K_g<7/10,\qquad
 M_g=\Re\Xi(u_g),\qquad
 \Xi(u)=2S_3(0,u)+iu^2/\pi-iu .
 \tag{3}
\]
On a fixed ordinary bidisk about \((-2,-2)\), its full inner
action \(S(w,u)\) and amplitude \(A(w,u)\) give
\[
\begin{split}
 \Xi(u;\mathbf w)&=S(w_L,u)+S(w_R,u)+iu^2/\pi-iu,\\
 \Xi_u(u_*(\mathbf w);\mathbf w)&=0,\qquad
 \Theta(\mathbf w)=\Xi(u_*(\mathbf w);\mathbf w),\\
 \mathcal B(\mathbf w)
 &=i\sqrt{2/\pi}\,
 \frac{\sin u_*(\mathbf w)
       A(w_L,u_*(\mathbf w))A(w_R,u_*(\mathbf w))}
      {\sqrt{-\Xi_{uu}(u_*(\mathbf w);\mathbf w)}}\ne0 .
\end{split}                                                        \tag{4}
\]
The square root is the original horizontal Gaussian branch.
The implicit point continues \(u_g\), with no new log lift.

Choose the fixed small horizontal interval \(J_g\) from that
theorem. Its exact local source is
\[
 \mathcal L_N(\mathbf w)
 =-\frac{N^2C_{N,4}}{\pi i}
  \int_{J_g}\sin u\,Q_N(w_L,u)Q_N(w_R,u)
       e^{iNu^2/\pi}W_N(u)\,du,\qquad
 W_N(u)=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
 \tag{5}
\]
It is an ordinary polynomial of degree at most \(D\) in
each free color, since the endpoints are fixed. The proved
local asymptotic is
\[
 \mathcal L_N(\mathbf w)
 =C_{N,4}C_{N,3}^{\,2}N^{-3/2}
   \mathcal B(\mathbf w)e^{N\Theta(\mathbf w)}
                           (1+O_{\rm hol}(N^{-1})).
 \tag{6}
\]
All normalizations in (5)--(6) are literal.

## 2. The whole complementary source for independent real colors

There is \(\delta>0\) with
\[
 \sup_{w_L,w_R\in[-2,2]}
      |Z_N(w_L,w_R)-\mathcal L_N(w_L,w_R)|
                         \le CN^A e^{N(M_g-\delta)} .
 \tag{7}
\]
Here is the complete inventory and the exact real-color
scope needed for this claim.

Use the midpoint cutoff
\[
 a_N=\pi-\frac{2\pi\lfloor N/400\rfloor}{N},
               \qquad e^{iNa_N}=-\eta_N ,
 \tag{8}
\]
and the fixed small height \(h_{\rm out}\) of the
[two-current identity](research_mixed_symmetric_closing_two_remaining_currents.md).
That identity splits the full trace into the middle
horizontal, its two connecting currents and the explicit
far derivative samples and short midpoint currents.
In full notation, put
\[
 G_N(u;\mathbf w)=\sin u\,Q_N(w_L,u)Q_N(w_R,u)e^{iNu^2/\pi},
 \qquad \tau_j=2\pi(D/2-j)/N .
 \tag{8a}
\]
For any oriented lower-half-plane path \(\Gamma_N\) from
\(-a_N-ih_{\rm out}\) to \(a_N-ih_{\rm out}\), the exact
identity used here is
\[
\begin{split}
 Z_N(\mathbf w)={}&-\frac{N^2C_{N,4}}{\pi i}
                   \int_{\Gamma_N}G_N(u;\mathbf w)W_N(u)\,du\\
 &+\eta_NC_{N,4}
           \sum_{\substack{0\le j\le D\\|\tau_j|\ge a_N}}
                          \partial_uG_N(\tau_j;\mathbf w)\\
 &+\frac{\eta_NN^2C_{N,4}}{\pi}
       \int_{-h_{\rm out}}^{h_{\rm out}}
          \frac{G_N(a_N+iv;\mathbf w)}
                         {4\cosh^2(Nv/2)}\,dv .
\end{split}
\tag{8b}
\]
The last line is the original pair of short midpoint
currents after exact reflection, with its displayed sign.
The derivative sum retains the full first-normal data.
At odd levels the central simple sample belongs to the
lower contour and is not removed as a far sample.
All the following changes of path stay below the real
sampling poles.

**Positive middle outside \(J_g\).**
The [incoming angular theorem](research_mixed_symmetric_closing_incoming_angular_decay.md)
gives for every real color
\[
 |Q_N(-2\cos\theta,u)|
 \le CN^A e^{N\{s(u)-cD(\theta)\}},\quad
 s(u)=\Re S_3(0,u),\quad D(\theta)=1-\cos\theta,
 \tag{9}
\]
on the entire lower rectangle
\(0\le\Re u\le\pi/2,\ 0\le-\Im u\le7/10\).
Drop the favorable angular terms in the two factors.
The full outer crossing and sampling kernel then give
rate \(\Re\Xi(a-iK_g)\). Its proved horizontal loss is
\[
 \Re\Xi(a-iK_g)\le M_g-(a-\beta_g)^2/(8\pi).
 \tag{10}
\]
The positive part outside \(J_g\) consequently has a
fixed gap, uniformly in both real incoming colors.

**The interval crossing the imaginary axis.**
The [center bridge](research_mixed_symmetric_closing_center_bridge.md)
is stated on a small incoming bidisk, but its only use of
that restriction is its initial positive-interval estimate.
Equation (9) supplies a stronger estimate for every real
color on \(0\le a\le A\). The remainder of that proof is
polynomial and uniform in its coefficients: with
\(F_N(u)=Q_N(w_L,u)Q_N(w_R,u)\) and
\[
 z=\zeta(x)=-2\frac{\cosh K_g(1-x^2)+2i\sinh K_gx}{1+x^2},
 \qquad x=\tan(a/2),
 \tag{11}
\]
the polynomial
\((1+x^2)^{2D}F_N^\sharp(\zeta(x))\) has degree at most
\(4D\). Its same fixed Chebyshev interval extension from
\([0,\tan(A/2)]\) to a sufficiently short negative interval
costs less than its initial strict gap. Restoring the full
\(W_N\) and crossing gives exactly the source proof's
positive gap on \([-\eta,A]-iK_g\), now for both complete
real incoming intervals. No local error is continued from
one incoming color.

**Negative middle and far left.**
Section 8 of the
[upper-inner theorem](research_mixed_symmetric_closing_upper_inner_packet.md)
is an all-real incoming upper estimate with any prescribed
positive tolerance. Exact evenness sends
\(Q_N(w,-a-iK_g)\) to \(Q_N(w,a+iK_g)\).
Its Section 9 combines this with the symmetric phase
loss to pay \([-\pi/2,-\eta]-iK_g\). The proof uses the
all-real estimate before its optional ordinary-neighborhood
continuation, so its fixed gap is uniform in the two
independent real colors.
The [far-left theorem](research_mixed_symmetric_closing_left_far_connection.md)
already states the complete negative far horizontal and
deep vertical estimate on neighborhoods of both whole
real incoming intervals. Its proof uses the original
full matrix and all-row evaluation norms.

**Right hyperbola.**
The [complete right-source theorem](research_mixed_symmetric_closing_complete_right_connection.md),
equation (9), explicitly proves the all-real bound for
the full inner trace on
\[
 u(\beta)=\beta-i\frac{\pi K_g}{2\beta},
                       \qquad\pi/2\le\beta\le2\pi/3 .
 \tag{12}
\]
Multiplying its two independent real-color bounds and
the exact outer sampling denominator gives its stated
fixed outer gap. Both inner edge deletions and both
sampling denominators were already retained there.

**Right descending column.**
Although the final theorem in the
[descending-column note](research_mixed_symmetric_closing_right_descending_column.md)
is stated on an ordinary bidisk, its equation (24) is
explicitly uniform in \(w\in[-2,2]\). Its entire smaller-height
inner source inventory precedes that estimate. Section 5
uses only the resulting upper envelope, the original
vertical phase convexity and the exact outer multiplier.
It therefore gives the same positive gap for both real
colors on the column
\[
 2\pi/3-3iK_g/4\longrightarrow2\pi/3-i/10000 .
 \tag{13}
\]

**Low and final far connection.**
The [all-real column theorem](research_mixed_symmetric_closing_all_real_column_bounds.md),
Theorem 1, proves
\[
 \sup_{w\in[-2,2]}\|M_N^3v(w)\|_2
 \le C_\tau N^{A_\tau}
      e^{N\{b_2+\lambda_*-1/19+\tau\}}
 \tag{14}
\]
for every prescribed \(\tau>0\), with every original row
and both parities. In fact its real bound has no \(\tau\)
and has a fixed incoming angular loss. Its direct proof
keeps the true two index-end groups; their coupled reserve
exceeds \(1/120\), so no compact cap asymptotic is continued
to an index endpoint. Corollary 2 of that theorem applies
the exact outgoing evaluation profile and (14) to the
[coupled low-outer theorem](research_mixed_symmetric_closing_coupled_column_and_low_outer.md)
for both real incoming colors. The original crossing
and full \(W_N\) are independent of those colors. It pays
\[
 2\pi/3-i/10000\longrightarrow4\pi/5-i/10000 .
 \tag{15}
\]
Its recorded continuation through \(4\pi/5-i/100\)
and the original far-right path to \(a_N-ih_{\rm out}\)
uses the same norm bound and retains a common gap
\(1/400\), on fixed neighborhoods of both complete
real incoming intervals.

**Far physical samples and both short midpoint currents.**
The [far-boundary theorem](research_mixed_symmetric_closing_far_boundary_payment.md),
Sections 2--3, already proves all these bounds uniformly
in both real incoming colors. Its Markov argument is
applied to a genuine whole real spectral interval and
the exact degree \(2D\); its continuation pays both
short midpoint columns. It keeps all first-normal
samples and the odd simple node.

There are finitely many pieces and every indicated gap
is positive. Choose all permitted tolerances inside
their minimum and absorb the fixed polynomial factors.
The exact source identity then gives (7).
No small-disk norm is substituted for an all-real
source bound in this assembly.

## 3. Full bidisk packet and normalized derivatives

Both \(Z_N\) and \(\mathcal L_N\) have separate ordinary
degrees at most \(D\), hence so does their exact difference.
The real-square estimate (7), followed by tensor Chebyshev
continuation, gives on a sufficiently small fixed product
of filled ellipses about \([-2,2]^2\)
\[
             |Z_N-\mathcal L_N|
                  \le C'N^{A'}e^{N(M_g-\delta/2)} .
 \tag{16}
\]
Indeed, logarithmic ellipse parameter \(\rho\) in each
variable costs at most \(2D\rho\), and \(\rho\) is chosen
before \(N\). The coefficient count is polynomial.
The ellipses contain ordinary disks about \(-2\).

Shrink a fixed such bidisk inside the local chart (4) so
\(\Re\Theta(\mathbf w)>M_g-\delta/4\) and
\(\mathcal B(\mathbf w)\ne0\). Equations (6),(16) prove
the full-source asymptotic
\[
 \boxed{\quad
 Z_N(\mathbf w)
 =C_{N,4}C_{N,3}^{\,2}N^{-3/2}
       \mathcal B(\mathbf w)e^{N\Theta(\mathbf w)}
                         (1+O_{\rm hol}(N^{-1})).
 \quad}                                                            \tag{17}
\]
The exponentially small remainder is compared with the
actual local action; no lower bound for another signed
observation is inferred. Cauchy's formula on smaller
fixed bidisks proves every fixed normalized ordinary
mixed derivative estimate. All constants remain fixed
as \(N\) tends to infinity through both parities.

## 4. Whole boundary estimate and Hessian

The incoming angular theorem bounds the literal local
integral (5) by
\[
 |\mathcal L_N(-2\cos\theta_L,-2\cos\theta_R)|
 \le CN^A e^{N\{M_g-cD(\theta_L)-cD(\theta_R)\}}.
 \tag{18}
\]
Combine (7),(18) and \(D(\theta_L)+D(\theta_R)\le4\).
After decreasing \(c\), the same estimate holds for
the full \(Z_N\).

Put
\[
 \Phi(\theta_L,\theta_R)
       =\Theta(-2\cos\theta_L,-2\cos\theta_R).
 \tag{19}
\]
The local outer theorem's exact ordinary marginals are
\(\Theta_{w_L}=\Theta_{w_R}=-\cos(t_g/2)/(4\pi)\)
at completeness. Separate evenness consequently gives
\[
 \Phi''(0,0)
       =-\frac{\cos(t_g/2)}{2\pi}I_2,\qquad
                           \Re\cos(t_g/2)>0 .
 \tag{20}
\]
Thus a fixed smaller angular bidisk has strictly negative
real Hessian. The local-packet/real-gap lemma in
[mixed stability reduction](research_mixed_open_source_stability_reduction.md)
applies to the full polynomial of separate degree \(D\).
It proves constants \(c_*,B,h>0\) with
\[
 |Z_N(-2\cos(x+iy),-2\cos(v+iw))|
 \le CN^A e^{N\{M_g-c_*D(x)-c_*D(v)+B(y^2+w^2)\}}
 \tag{21}
\]
for the entire real periods and \(|y|,|w|\le h\).
No extra source continuation is required for this step:
it uses (17), the calibrated real bound and the actual
finite degree.

## 5. Marked phase germ and exact scope of composition

Before stationary elimination the original angular
action, with free angles \(s,v\), is
\[
\begin{split}
 \mathcal H(s,v;t_L,u,t_R)
 ={}&\psi(s,t_L)+\psi(t_L,u)+\psi(u,t_R)+\psi(t_R,v)\\
 &+\frac{i}{4\pi}(3t_L^2+4u^2+3t_R^2)
                                      -i(t_L+u+t_R).
\end{split}                                                        \tag{22}
\]
The Hessian in the three selected variables at the actual
positive point has negative definite real part, as proved in the local
outer theorem from the positive-edge Hessian theorem.
The implicit continuation solving its three selected
critical equations therefore exists near \(s=v=0\).
Nested elimination of the two ends and then the middle
is precisely (4), so its stationary value is (19).

The [marked completion theorem](research_positive_point_marked_completion.md),
including its final boundary-germ paragraph, retains the
original face maps, carriers and full primitive periods.
Its hypothesis is the positive original solution,
already identified for (22), not a new polynomial root.
Its nonsingular period Jacobian gives a marked outside
boundary deformation with the selected primitive
periods fixed. Positivity, regular face maps and
positive selected core lengths persist locally.
The complete-boundary volume calibration is
\[
                  2\pi\Re\Theta(-2,-2)=V_{\rm cells}.
 \tag{23}
\]
The original contracted-coordinate action differs by
the recorded \(2i\gamma\); rewriting the exponent in
that convention requires the additional unit scalar
\(e^{-2iN\gamma}\). Equation (17) keeps the original
angular scalars throughout. No volume for arbitrary
independent complex ordinary colors is asserted.

Equations (17),(20),(21) are exactly the analytic
hypotheses of the
[finite two-boundary kernel closure theorem](research_finite_two_boundary_kernel_closure.md).
Thus this kernel may be added to any fixed finite
collection of already eligible original pieces.
That theorem licenses exact operations
\[
 F_N(v)\longmapsto
 \phi_N^{(s)}[R(s)^nF_N(s)Z_N(-2\cos s,-2\cos v)]
 \tag{24}
\]
with independently sufficiently long fixed signed
\(n\), and a sufficiently long final original trace.
It supplies a common threshold for a fixed finite
kernel collection, independent of the length of a
fixed sequence. All endpoints and normals remain
in that exact induction.

For this kernel the operator in (24) is literally
\[
 \boxed{\quad
 \mathcal U_{343,n}F
   =T\!\left(R^3T\!\left(R^4T\!\left(
                    R^3T(R^nF)\right)\right)\right).
 \quad}                                                            \tag{25}
\]
To check (25), expand (2) into its three finite selected
traces and four original edge kernels. Contract the free
input trace first and then the three selected traces,
in their original order. Each interchange is of finite
linear functionals, including all their first normals.
It is the same exact trace interchange as equation (3)
of the kernel-closure theorem. Thus a fixed sequence may
contain arbitrarily many occurrences of this specified
short cluster, provided consecutive insertions are
separated by the eligible long steps. The common threshold
depends on the finite kernel collection; prefactors and
starting levels may depend on the whole fixed sequence.
Every power and the sequence are fixed before \(N\to\infty\).

This is not closure under arbitrary adjacent short
pieces. A new neighboring short power changes the
source and must satisfy its own calibrated estimates.
An interpretation of (24) as a knot theorem additionally
requires the literal original ordered gluing, carrier
parities, primitive filling coefficients, component
test, reduced cut and zero-framing normalization.
The boundary polynomial (2) is not by itself an
identification with an arbitrary knot invariant.
Neither arbitrary short partial-fillings nor the
all-but-finitely-many assignment statement follows
from this one eligible kernel.

## Frozen direct source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_symmetric_343_closing_trace_and_domain.md | ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a |
| research_mixed_symmetric_closing_local_outer_packet.md | 0ff2c66243a8cc67744d23c4ba51cc87c5d317ebbed6868b2b4127077e2edc8c |
| research_mixed_symmetric_closing_complete_inner_asymptotic.md | 4e6d58951cff746a5daf6b3efcf3df917233e64d773d936a232dbc6bb870c96c |
| research_mixed_symmetric_closing_incoming_neighborhood.md | fedd23ea3d5d8aea8132af828f358bb0b0884e1e599a5dc31f457b33dd261aae |
| research_mixed_symmetric_closing_two_remaining_currents.md | 15c28d0004bfcdebd26e55dfe48419aa54d14c563c95e33e1d32ef5b1ac6cad8 |
| research_mixed_symmetric_closing_incoming_angular_decay.md | 4fa4776cf2bd2f153be257c9e2c5aecc09d92f5e551073e9c3ce62e75dc7dd4e |
| research_mixed_symmetric_closing_horizontal_concavity.md | f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b |
| research_mixed_symmetric_closing_center_bridge.md | 63f0bf0968ae71c40d49b50d01962f215381707b716c482d7f5b43b23a058e6e |
| research_mixed_symmetric_closing_upper_inner_packet.md | 091b075d7a32e06f5d864200c93e4e9174a225069650b46dda8c0ea7bb4dc096 |
| research_mixed_symmetric_closing_left_far_connection.md | d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184 |
| research_mixed_symmetric_closing_complete_right_connection.md | 44bd3ed32a7607f2f9464e1498c35032e173f8f5ec6ebe52903efb41d659240d |
| research_mixed_symmetric_closing_right_descending_column.md | 3096dde75fc21fcb1e84ac8dce0e652e2271c50780c889a82bdee0cd83b53001 |
| research_mixed_symmetric_closing_all_real_column_bounds.md | 02a134c219a5da365316de633e9edc407fbcc3de512d0474888bf8722b1f1059 |
| research_mixed_symmetric_closing_coupled_column_and_low_outer.md | f1a8fb899e580c3953136aaa7aeb86530e2c51d25aaecba28e66b16183083b51 |
| research_mixed_symmetric_closing_far_boundary_payment.md | dc1942698fe442e9995c6bf1ee44ae67f7432c54f2f2d2086e108d83f132fd6b |
| research_mixed_open_source_stability_reduction.md | 5d501024dddb98ff28f1ae3d44110d4a34bfc82d8063ff01353315c3efbfc31c |
| research_positive_edge_global_monotonicity.md | da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500 |
| research_positive_point_marked_completion.md | 28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887 |
| research_mixed_geometric_action_calibration.md | 7fd7032d085cb9055904673a7c3d9dd978a0fa19639670d5ece67ba8093e09d9 |
| research_mixed_geometric_source_identification.md | ac2b6c8993eeae51eb27a449a23f0524dc10a6f1e10b3b816446178754ea5f4b |
| research_finite_two_boundary_kernel_closure.md | 759118c877a9657355d5c457bfc3d0b7a45cc2601a8b247f4e030c90770155cc |
