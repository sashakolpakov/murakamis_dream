# The full Fourier right cap at its actual reference

Research theorem, 7 November 2026. The complete original Fourier
right cap has a nonzero stationary asymptotic at every actual
incoming reference of type three or four. The preceding coherent
contour bounds reduce its whole finite source to the original
two-index main integral. Its leading power is \(N^{-3/2}\),
with the original cardinal normalization and both level parities.

For type four, a proved relative approximation makes the incoming
Fourier weight nonzero at the actual reference. It is removed only
there, after the weighted remainder has been bounded. No division
at a possible weight zero elsewhere in the horizontal target
interval is used. No new evaluation or source replay is required.

## 1. The actual reference and the literal source

Fix \(\eta\in\{0,1\}\), \(a_*\in K_{3+\eta}\), and \(y=x_0\).
Let \((s_*,q_*)\in O_4^2\) be the original-log critical pair
from the
[correlated endpoint theorem](research_mixed_fourier_right_cap_correlated_endpoint.md).
Its reference eligibility is established by
[the completed annulus theorem](research_mixed_fourier_right_cap_annulus_completion.md).
Set
\[
 X_*=e^{-2\pi ia_*},\quad Y=e^{2\pi iy},\quad
 h_s=\Im s_*,\quad h_q=\Im q_*,\quad
 P=[11/50,9/20].
\tag{1}
\]
The inherited ranges include
\[
 .24\le\Re s_*,\Re q_*\le.36,\qquad
 -.102\le h_s,h_q\le-.001.
\tag{2}
\]
All endpoint logarithms and action constants have their
original continuations.

The finite expression is exactly
\[
\begin{split}
 V_N^{\rm F}(y,X_*)
 &=\sum_{\substack{j,l\ge0\\j+l<N}}
       \frac{X_*^{-j}p_j(X_*)P_{j+l}}{P_j^3P_l}\,f_l(y),\\
 r&=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\\
 f_l(y)&=\frac{e^{-\pi i(N-1)y}}N
                     Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
\end{split}
\tag{3}
\]
In particular no crossing scalar or extra outside power
of \(N\) is inserted. Define the unallocated phase
\[
\begin{split}
 F_0(s,a,q;y)={}&g(s+a)+g(s+q)-3g(s)-g(a)-g(q)
                          +2\pi ias+\ell_q(y),\\
 \ell_q(y)={}&2\pi iy(q-1/2)
 -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})
                         -\operatorname{Li}_2(Y)}{2\pi i},\\
 F_\eta&=F_0-\frac{\eta}{2}g(a),\qquad
 \Phi_*=F_0(s_*,a_*,q_*;y),\\
 M_\eta&=\Re\Phi_*-\frac{\eta}{2}\Re g(a_*).
\end{split}
\tag{4}
\]
The original stationary equations are \(F_{0,s}=F_{0,q}=0\)
at \((s_*,a_*,q_*)\). Removing the incoming allocation does
not change either equation or their two-index Hessian.

## 2. Reduction of the plateau to its joint main current

Let
\[
 L_N=\lceil N/8\rceil,\quad M_N=\lceil N/2\rceil-1,\qquad
 \sigma_-=(L_N-1/2)/N,\quad
 \sigma_+=(M_N+1/2)/N.
\tag{5}
\]
Keep the exact joint row from
[the global chart](research_mixed_fourier_right_cap_joint_global_chart.md):
\[
\begin{split}
 T_N(s,q;a_*,y)
 &=e^{2\pi iNa_*s}\Pi_N(s+a_*)\Pi_N(s+q)
             E_N(a_*)E_N(q)E_N(s)^3\widehat f_N(q;y),\\
 \widehat f_N(q;y)
 &=\frac{e^{-\pi i(N-1)y}}N e^{2\pi iNyq}
                          \Pi_N(1-y-1/N)E_N(q-y).
\end{split}
\tag{6}
\]
Its two zero-mode densities are both \(+N\). Accordingly put
\[
 J_N=N^2\int_{11/50}^{9/20}\int_{\sigma_-}^{\sigma_+}
       T_N(u+ih_s,z+ih_q;a_*,y)\,du\,dz .
\tag{7}
\]
The contour uses the same increasing real-coordinate
orientation at both parities.

Write \(\kappa=1/2500000\) and
\[
 \delta_c=\kappa/2500,\qquad
 \delta_s=\kappa(23/200)^2>\delta_c.
\tag{8}
\]
The
[complete right-horizontal reduction](research_mixed_fourier_right_horizontal_completion.md),
equation (12), gives
\[
 |d_N(X_*)|^{\eta/2}|V_N^{\rm F}-I_N^P|
                         \le e^{N(M_\eta-\delta_c/16)},
\tag{9}
\]
where \(I_N^P\) is the exact low-index conditional polynomial
integrated over \(q\in P+ih_q\). We now keep all its remaining
inner currents rather than infer an asymptotic from an upper bound.

Split its physical retained indices at \(L_N\). The rows
\(0\le j<L_N\) are bounded by the original left-cut rate,
with gap \(1/35000\), by Section 4 of
[the bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md)
and the three completed margins in
[the inner-source completion](research_mixed_fourier_right_cap_bare_inner_completion.md).
This is the individual real-row comparison at negative
outgoing height, including \(j=0\).

Apply the exact one-index cotangent decomposition to
\(L_N\le j\le M_N\), at each fixed \(q=z+ih_q\).
Its main term is exactly the inner integral in (7).
The two horizontal aliases retain their full denominators
and the original heights \(-1/5,5/4\). Their pointwise
reserves are \(1893\pi/25000\) and \(7/50\), respectively,
relative to the same critical-height main sheet.
Every penalized vertical part is bounded by its real cut,
with gap \(1/35000\). The unpenalized negative-height
joins retain both endpoints: vertical convexity bounds
them by the maximum of the real cut and the critical-height
cut. The latter has gap at least \(\delta_s\), since
both retained cuts have limiting distance at least
\(23/200\) from \(\Re s_*\).

These are precisely the inner-source estimates on
\(q\in P+ih_q\). They apply to (6): the cardinal factor
is independent of the retained index, and its specified
factorial interpolation has the same calibrated phase
and nonzero leading symbol as the original inner cardinal
on this compact strip. The equality of interpolations
off-grid is not assumed. Their proved ratio is
\(1+O(N^{-1})\), as stated in equation (8a) of the
inner-source completion.

The half-grid shifts are absorbed in fixed regular
neighborhoods of these contours. Choosing one prescribed
source tolerance below the strict gaps and absorbing
the polynomial factors and the outgoing \(N\) gives
\[
 |d_N(X_*)|^{\eta/2}|I_N^P-J_N|
                         \le e^{N(M_\eta-\delta_c/16)}
\tag{10}
\]
for sufficiently large \(N\) of either parity. No old
physical outgoing face or artificial real-height corner
is used in this step. Combining (9)--(10), including
their fixed factor two, proves the explicit joint reduction
\[
 \boxed{\quad
 |d_N(X_*)|^{\eta/2}|V_N^{\rm F}-J_N|
                         \le e^{N(M_\eta-\delta_c/32)} .
 \quad}
\tag{11}
\]

## 3. The original nonzero row symbol and its Gaussian integral

Let
\[
 \mathfrak a(w)=\sqrt{2\sin\pi w}\,e^{-\pi iw/2}
\]
with the square root continued from its positive value
on \(0<w<1\). On the whole compact rectangle of (7),
all individual factorial arguments and both sum arguments
stay in their original regular strips. The cardinal
has \(|Y|<1\), \(|Ye^{-2\pi iq}|<1\).
The factorial expansion and equation (6) of
[the outgoing cardinal chart](research_mixed_fourier_right_cap_outer_contour.md)
give
\[
 T_N(s,q;a_*,y)
 =N^{-5/2}\mathfrak b(s,a_*,q;y)
                e^{NF_0(s,a_*,q;y)}(1+O(N^{-1})),
\tag{12}
\]
uniformly on a neighborhood of that rectangle, where
\[
 \mathfrak b(s,a,q;y)=
 \frac{\mathfrak a(s+a)\mathfrak a(s+q)}
      {\mathfrak a(a)\mathfrak a(q)\mathfrak a(s)^3}
 \frac{e^{\pi iy}}
          {\sqrt{(1-Y)(1-Ye^{-2\pi iq})}} .
\tag{13}
\]
The last square root uses the original two logarithms,
as in the root-Pochhammer and factorial-cardinal expansions.
It is not reset as the level changes. Formula (12) also
appears explicitly in equations (10)--(11) of
[the right-main source proof](research_mixed_fourier_right_cap_upper_main_arc.md).
All factors in (13) are nonzero. The finite
\(e^{\pi iy}\) factor accounts for the \(N-1\) in (3).

Lemma 1 and equation (14) of the bare inner-contour theorem
give
\[
 -\Re F_{0,(s,q)(s,q)}\succ\mu I_2,\qquad
                     \mu=1/1250000,
\tag{14}
\]
throughout the critical-height plateau. In particular the
complex symmetric matrix
\[
                 H_*=-F_{0,(s,q)(s,q)}(s_*,a_*,q_*;y)
\tag{15}
\]
is accretive and nonsingular. Integrating the same curvature
from the actual stationary pair gives
\[
 \Re F_0(u+ih_s,a_*,z+ih_q;y)
 \le\Re\Phi_*-\kappa\{(u-\Re s_*)^2+(z-\Re q_*)^2\}.
\tag{16}
\]
The \(O(1/N)\) changes of the outer retained endpoints
preserve a fixed positive loss near those endpoints.

Choose a small fixed real box about
\((\Re s_*,\Re q_*)\) within the plateau. On its complement
(16) gives an exponential loss. On the box, apply the
ordinary complex Gaussian expansion to (12), with the
two increasing real-coordinate orientations in (7).
After the \(N^{-1/2}\) rescaling, the terms of relative
order \(N^{-1/2}\), from the linear symbol and cubic phase,
are odd and integrate to zero on the symmetric local box.
The quartic Taylor remainder, the quadratic products of
those odd terms and the symbol error are \(O(N^{-1})\)
after Gaussian integration; accretivity controls their
tails uniformly.
The determinant root is the analytic accretive Gaussian
branch: it is positive on real positive-definite matrices
and continued within the accretive cone. This is the
same convention used in the
[original Fourier local-current proof](research_mixed_fourier_prefix_local_current.md),
Section 4. It cannot vanish.

Consequently
\[
 J_N=N^{-3/2}\mathcal A_*
                        e^{N\Phi_*}(1+O(N^{-1})),\qquad
 \mathcal A_*=
       \frac{2\pi\,\mathfrak b(s_*,a_*,q_*;y)}
                         {\sqrt{\det H_*}}\ne0 .
\tag{17}
\]
The power is exactly \(N^2N^{-5/2}N^{-1}=N^{-3/2}\).
All constants in the phase and coefficient come from
the literal source (3), not from an allocated absolute
rate or a selected contour chosen by its modulus.

## 4. Removing the incoming weight only at the actual reference

If \(\eta=0\), equation (11) is already an unweighted
remainder estimate, and \(M_0=\Re\Phi_*\).

If \(\eta=1\), the actual reference belongs to
\[
 K_4\subset[.24,.36]+i[-.108,-.001]
       \Subset E_4=[59/250,91/250]+i[-29/250,3/250].
\tag{18}
\]
The compact containment uses the original typed disk
of radius \(.060\), with its stated height filter.
Corollary 2, equation (24), of
[the actual Fourier-weight comparison](research_mixed_fourier_weight_continuation.md)
proves, at both parities,
\[
 d_N(e^{-2\pi ia})=\Pi_N(a)^{-1}
                           (1+O(e^{-N/200})),\qquad a\in E_4 .
\tag{19}
\]
Its equation (19) supplies the nonzero leading coefficient
of the reciprocal factorial. Thus at \(a=a_*\),
\[
 |d_N(X_*)|^{1/2}
 =N^{-1/4}|\mathfrak a(a_*)|^{-1/2}
             e^{-N\Re g(a_*)/2}(1+O(N^{-1})).
\tag{20}
\]
In particular this exact polynomial value is nonzero for
all sufficiently large \(N\), with a matching lower bound.

Only at this actual reference may we divide (11) by
(20). The exponential correction changes \(M_1\) back
to \(\Re\Phi_*\), and the cost \(N^{1/4}\) is polynomial.
Together with the \(\eta=0\) case this gives, eventually,
\[
                    |V_N^{\rm F}-J_N|
              \le e^{N(\Re\Phi_*-\delta_c/64)} .
\tag{21}
\]
No nonvanishing of the incoming weight on the whole
horizontal target interval was required or asserted.

**Theorem.** For either incoming type and every fixed actual
reference specified in (1), the complete original finite
source satisfies
\[
 \boxed{\quad
 V_N^{\rm F}(x_0,e^{-2\pi ia_*})
       =N^{-3/2}\mathcal A_*e^{N\Phi_*}
                               (1+O(N^{-1})),\qquad
                         \mathcal A_*\ne0 .
 \quad}
\tag{22}
\]
The assertion holds along both integer level parities.
In particular the source is nonzero for all sufficiently
large \(N\), and there are constants \(c_*,C_*>0\) such that
\[
 c_*N^{-3/2}e^{N\Re\Phi_*}
 \le |V_N^{\rm F}(x_0,e^{-2\pi ia_*})|
 \le C_*N^{-3/2}e^{N\Re\Phi_*}.
\tag{23}
\]
Hence \(N^{-1}\log|V_N^{\rm F}|\to\Re\Phi_*\).

The local critical phase and symbol have their usual
holomorphic continuations. A theorem for parameter
derivatives of the whole finite source would additionally
require the global remainder estimate on a common complex
parameter neighborhood. Such a theorem is not inferred
from the local Gaussian calculation here. Nor does (22)
provide an arbitrary-message attachment bound or a new
knot-family noncancellation theorem.
