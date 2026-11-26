# The ordinary-next unselected incoming corner at its actual lower height

Research deduction, 8 November 2026. The complete original incoming
union from \(1/2+ih_a\) up to \(1/2\) and then along the real
axis to \(7/10\) has a strict following-action gap when the second
coordinate ranges over its entire unselected plateau at the actual
negative height. The proof calibrates the conditional critical
action against the original reference, transports the complete cap
and that action on a replacement contour, and uses the completed
finite-source deformation with its two distinct error bounds.

No comparison at the old corner is assumed, no negative-depth cap
packet is imported, and no numerical evaluation is used.

## 1. Actual references and the original allocation

Keep the same ordinary-next canonical family as
[the selected incoming-union theorem](research_mixed_next_selected_incoming_corner_union.md):
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
       \qquad(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),
       \quad\beta=0,1 .
                                                               \tag{1}
\]
Both internal indices are ordinary; the external parameter
remains \(s_4^*\in K_3\cup K_4\). Use
\[
 \begin{gathered}
 A=\Re a_*,\quad h_a=\Im a_*,\quad
 h_s=\Im s_*,\quad h_y=\Im y_*,\quad\alpha=\Re y_*,\\
 .278\le A\le.391,\quad -.072<h_a<0,\qquad
 -.102<h_s,h_y<-.001,\\
 .24<\Re s_*,\alpha<.36,\qquad P=[.22,.45],\\
 y=q+ih_y,\quad z=u+i\Im z_*,\qquad q,u\in P .
 \end{gathered}                                                 \tag{2}
\]
The first two blocks are the original half-chain with external
coordinate \(t_*\). The bounds in (2) are its established
following-family bounds; see
[the following right-segment source, equations (1)--(3)](research_mixed_three_four_following_right_segment.md)
and the canonical negative-height identification in
[the selected right-segment proof, Section 2](research_mixed_second_selected_first_three_right_segment.md).
They are not independent replacements for the actual reference.

Retain the original type-four phase
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,
                 \qquad F(s;a,y)=Q(s;a,y)-\tfrac12g(y).
                                                               \tag{3}
\]
At the reference, \(Q_s=0\). Put
\[
 \begin{split}
 p_L&=Q_a(s_*;a_*,y_*),\qquad
 p_y=g'(s_*+y_*)-\tfrac32g'(y_*),\qquad p=\Re p_y,\\
 A_*&=\Re\{T_0(a_*)+F(s_*;a_*,y_*)\},\\
 B_*&=\Re T_0(a_*)-\Re p_L(1/2-A)
                         -\kappa_0(1/2-A)^2,\qquad
 \kappa_0=1/2500000 .
 \end{split}                                                    \tag{4}
\]
The original attached equation is \(T_0'(a_*)+p_L=0\).
The cap plane is the original complete source plane, and
\[
                              B_*>7/8
                                                               \tag{5}
\]
by [the calibrated-plane floor](research_mixed_next_calibrated_cap_plane_floor.md).
Let \(B_3(q,u)\) and \(\Lambda_{123}(z)\) be the unchanged
complete third-factor plane and outgoing affine action from
[paired localization, Section 2](research_mixed_next_low_cardinal_paired_localization.md).
Their exact marginal cancellation gives
\[
                  A_*+p(q-\alpha)+B_3(q,u)
                                     \le\Lambda_{123}(z).
                                                               \tag{6}
\]
In particular \(A_*=\Re\{\mathcal P_{34}(-2,y_*)-g(y_*)/2\}\);
there is no change of phase gauge.

## 2. Joint phase support reaches the incoming half face

Keep the imaginary parts \(h_a,h_s,h_y\) fixed at (2).
On
\[
 a_R,y_R\in P,\qquad 1/8\le s_R\le1/2,
 \]
the original uneliminated \(F\) has negative definite real
Hessian. This is the full three-variable statement of
[zero-mode support, equations (9)--(12)](research_mixed_horizontal_zero_mode_support.md)
and [the type-four left-cut extension, equation (14)](research_mixed_four_left_cut_extension.md).
Here the flags are exactly \((\eta,\epsilon)=(0,1)\),
so their allocated phase is (3).

The real Hessian is negative semidefinite on the extension
\[
        .45\le a_R\le.5,\qquad 1/8\le s_R\le.5,
                                      \qquad y_R\in P.
                                                               \tag{7}
\]
We verify the extension rather than extrapolating the old domain.
Write \(C(v)=\Re\cot\pi v\), and abbreviate
\[
 C_a=C(a),\quad C_s=C(s),\quad C_y=C(y),\quad
 C_{as}=C(a+s),\quad C_{sy}=C(s+y).
 \]
The negative real Hessian of \(F\), divided by \(\pi\),
is the sum of the following matrices in the order \((a,s,y)\):
\[
 \begin{pmatrix}C_a&0&0\\0&0&0\\0&0&0\end{pmatrix}
 -C_{as}\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}
 +\begin{pmatrix}
 0&0&0\\
 0&3C_s-C_{sy}&-C_{sy}\\
 0&-C_{sy}&\tfrac32C_y-C_{sy}
 \end{pmatrix}.
                                                               \tag{8}
\]
The original chirp has purely imaginary Hessian.
On (7), \(C_a\ge0\) and \(C_{as}\le0\), so the first
two summands are positive semidefinite.

The last block is positive definite. This is immediate if
\(C_{sy}\le0\), since \(C_s\ge0,C_y>0\); when \(C_s=0\)
at \(s_R=.5\), one also has \(C_{sy}<0\).
If \(C_{sy}>0\), then \(s_R+y_R<1/2\). For each fixed
height \(h\in[-.102,0]\), the function
\[
 C(r+ih)=\frac{\sin2\pi r}{\cosh2\pi h-\cos2\pi r}
 \]
strictly decreases on \(1/8\le r\le1/2\). Its derivative
has the sign of
\(\cosh(2\pi h)\cos(2\pi r)-1<0\), using
\(\cosh(.204\pi)<5/4\) and
\(\cos(\pi/4)<4/5\), already established in the following
right-segment proof. Since the two heights are both negative,
adding them increases their absolute value and decreases a
positive real cotangent. Consequently
\[
                         0<C_{sy}<\min(C_s,C_y).
                                                               \tag{9}
\]
The determinant of the last block in (8) is
\[
          \frac92 C_sC_y-3C_sC_{sy}-\frac32C_yC_{sy}.
 \]
If \(C_s\le C_y\), (9) makes it strictly greater than
\(3C_s(C_y-C_s)\ge0\). If \(C_y\le C_s\), it is
strictly greater than \(\tfrac32C_y(C_s-C_y)\ge0\).
The diagonals are positive as well. Thus the full Hessian
is negative semidefinite on (7), which is sufficient for
the straight-segment supporting inequality.
At the corner \(a_R=s_R=.5\), the incoming sum has
strictly negative imaginary part \(h_a+h_s\); its original
lower-half continuation is regular there. The Hessian
argument includes that boundary by continuity, with a zero
\(a\)-direction because \(C_a=C_{as}=0\); no strict
three-variable curvature is asserted at that corner.

The straight segment from the actual reference to any point
with \(a_R=.5\), \(s_R\in[1/8,.5]\), \(y_R=q\in P\)
first lies in the old domain and then in (7). Integrating
the nonpositive real Hessian along it gives
\[
 \Re F(s;.5+ih_a,y)
 \le\Re F(s_*;a_*,y_*)+\Re p_L(.5-A)+p(q-\alpha).
                                                               \tag{10}
\]
Adding the exact \(B_*\) in (4) leaves the strict deficit
\[
 \begin{split}
 B_*+\Re F(s;.5+ih_a,y)
 &\le A_*+p(q-\alpha)-\kappa_0(.5-A)^2,\\
 \kappa_0(.5-A)^2
 &\ge\frac{11881}{2500000000000}>\frac4{10^9}.
 \end{split}                                                    \tag{11}
\]
Only the cap's already retained quadratic loss is needed
for this explicit reserve.

## 3. Comparing the moving critical action with that fixed-height plane

For \(2/25\le t\le1/8\), keep \(a=.5+ih_a\) and
the private height \(h_s\). Put
\[
 r=e^{2\pi h_s}\in(1/2,1),\quad
 R=e^{2\pi h_y}\in(0,1),\quad T=e^{-2\pi h_a}\ge1.
 \]
The exact chirp-folded index force is
\[
 e^{\Re Q_s(t+ih_s;a,y)}
 =\frac{|T-r e^{-2\pi i(.5+t)}|
             |1-Rr e^{-2\pi i(q+t)}|}
            {|1-r e^{-2\pi it}|^3}>1 .
                                                               \tag{12}
\]
Both numerator factors exceed one because their cosines are
negative: \(.5+t\in[.58,.625]\) and
\(q+t\in[.30,.575]\). Also
\(\cos(2\pi t)\ge\sqrt2/2>7/10\); convexity in \(r\)
gives a squared denominator at most \(3/5\).
Thus the phase increases up to \(t=1/8\), and (11) also
holds on this additional strip.

Let \(\Theta(a,y)\) denote the original conditional critical
action from [the algebraic transport domain](research_mixed_four_conditional_algebraic_transport_domain.md).
For \(a_L=.5+ih_a\), define the continuous height profile
\[
 m(\sigma)=\max_{\,2/25\le t\le1/2}
                    \Re Q(t+i\sigma;a_L,y),
                 \qquad |\sigma|\le\frac{\log5}{2\pi}.
                                                               \tag{13}
\]
At \(t=1/2\), use the original continuous prewall boundary
value. The strict horizontal concavity in
[the middle-source reduction, Section 5](research_mixed_conditional_lower_output_middle_reduction.md)
implies vertical convexity for each \(t<1/2\).
Its continuous boundary limit is convex too. Therefore the
maximum in (13) is convex in \(\sigma\).

At the actual critical height, that same theorem places the
unique horizontal maximum strictly between \(2/25\) and
\(1/2\). Its height derivative is
\(-\Im Q_s=0\). The maximum is differentiable there by
uniqueness and its regular interior location, so this is a
minimum of the convex function \(m\). The reference height
\(h_s\in[-.102,-.001]\) lies in the height interval in (13),
since \(.204\pi<1<\log5\).
It follows that
\[
 \Re\Theta(a_L,y)\le m(h_s).
 \]
Combining this with (11)--(12), and recalling that
\(-\Re g(y)/2\) is constant in the private variable, proves
the actual critical-action comparison
\[
 B_*+\Re\Theta(a_L,y)-\tfrac12\Re g(y)
       \le A_*+p(q-\alpha)-\frac4{10^9}.
                                                               \tag{14}
\]
This uses the reference-height phase support and the proved
critical strip. It does not infer a critical bound from a
signed finite kernel or assume convexity of the eliminated
action in an outside height.

## 4. Complete product bounds on the replacement contour

The cap-only statement
[selected incoming union, equation (18)](research_mixed_next_selected_incoming_corner_union.md)
gives
\[
 |U_{0,N}(w,e^{-2\pi i(x+ih_a)})|
       \le C_\tau N^{A_\tau}e^{N(B_*+\tau)},
                \qquad .5\le x\le.7,\quad w\in[-2,2].
                                                               \tag{15}
\]
Its proof transports every fixed cap current with both
factorial branches and bounds all physical tails separately.
It is independent of the outgoing variable, so (15) applies
to the present lower \(y\). On the right vertical segment,
[the complete seven-tenths column bound](research_mixed_cap_seven_tenths_vertical_bound.md)
gives the stronger cap rate
\[
                  3907/4500<7/8<B_*.
                                                               \tag{16}
\]

The algebraic transport theorem proves
\(\Re\Theta_a<0\) and \(\Im\Theta_a>0\) on the whole
parameter domain used here. Hence moving \(a\) rightward
at fixed height, or upward at fixed real part, decreases
\(\Re\Theta\). In particular
\[
 \Re\Theta(a,y)\le\Re\Theta(a_L,y)
 \]
on both replacement segments
\[
 a_L\longrightarrow .7+ih_a,\qquad .7+ih_a\longrightarrow .7.
                                                               \tag{17}
\]
All these parameters satisfy the original algebraic chamber
conditions; this is a statement about its original logarithmic
action, not an assumed finite-kernel ratio.

For \(q\in P\) and \(h_y<0\), the original complete Fourier
weight bound gives
\[
 |d_N(Y)|^{1/2}
   \le C_\tau N^{A_\tau}e^{N\{-\Re g(y)/2+\tau\}} .
                                                               \tag{18}
\]
Here \(-\Re g(y)>0\) on the entire compact lower strip,
as proved in
[Fourier continuation, Section 5, equation (22)](research_mixed_fourier_weight_continuation.md).
Its absolute bound retains the polynomial forcing term;
that term has no larger rate on this lower strip.
No division by \(d_N(Y)\) is made.

The full ordinary third-factor estimate is
\[
 |C_{\beta,N}(Y,Z)|\,|d_N(Y)|^{1/2}|d_N(Z)|^{\beta/2}
       \le C_\tau N^{A_\tau}e^{N\{B_3(q,u)+\tau\}},
                                                               \tag{19}
\]
with its original source domains. Equations (6), (14)--(19)
therefore imply, on both segments in (17),
\[
 \begin{split}
 &|U_{0,N}(w,X)d_N(Y)C_{\beta,N}(Y,Z)|
      |d_N(Z)|^{\beta/2}e^{N\Re\Theta(a,y)}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
        e^{N\{\Lambda_{123}(z)-4/10^9+\tau\}} .
 \end{split}                                                    \tag{20}
\]

Finally apply the complete finite-source
[Gaussian deformation with two error bounds](research_mixed_conditional_lower_output_gaussian_deformation.md).
Its local nonzero Gaussian, conditional-action error, and
actual-next-plane error are all bounded using (20).
This proves the literal whole-density estimate
\[
 \begin{split}
 &|U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{\beta,N}(Y,Z)|
                                  |d_N(Z)|^{\beta/2}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
        e^{N\{\Lambda_{123}(z)-4/10^9+\tau\}}
 \end{split}                                                    \tag{21}
\]
on the replacement contour. All rows, both level parities,
the complete cap, both Fourier forcing alternatives, and every
conditional boundary current are included. Choosing the total
tolerance and then absorbing polynomial factors gives a finite
gap \(1/10^9\).

## 5. The exact original union and scope

Define the unselected finite incoming density
\[
 \mathcal F_N(a)=
 U_{0,N}(w,e^{-2\pi ia})
 C_{1,N}(e^{-2\pi ia},Y)d_N(Y)C_{\beta,N}(Y,Z).
 \]
It is an entire function of \(a\): the first two factors
form a finite Laurent polynomial in \(e^{-2\pi ia}\).
The original incoming measure is \(N\,da\). Cauchy's
theorem on the exact rectangle gives
\[
 \begin{split}
 N\int_{a_L}^{1/2}\mathcal F_N(a)\,da
 +N\int_{1/2}^{7/10}\mathcal F_N(a)\,da
 ={}&N\int_{a_L}^{7/10+ih_a}\mathcal F_N(a)\,da\\
   &+N\int_{7/10+ih_a}^{7/10}\mathcal F_N(a)\,da .
 \end{split}                                                    \tag{22}
\]
Thus (21) pays the whole original incoming union, while
retaining its cancellation at the artificial half-face corner.
It does not assert separate absolute bounds for the two
old pieces on the left of (22).

At the actual output \(z_*\),
\[
 \Lambda_{123}(z_*)=
       \Re\mathcal P_\beta^+(-2,z_*)-\frac\beta2\Re g(z_*).
 \]
For \(\beta=1\), the established nonzero outgoing factorial
packet removes the halfweight on a fixed neighborhood of
that actual output. For \(\beta=0\), no outgoing factor
is inserted. After reducing the strict reserves, the
unweighted union normalized by the original next action,
and all fixed normalized mixed jets, have gap \(1/10^{10}\)
on smaller fixed ordinary-color and output neighborhoods.
The paths, heights and integer cuts are held at their base
values when outside parameters vary. The original next
factor \(N\,dy\) and integration over a fixed lower plateau
segment cost only polynomial factors.

The all-real ordinary-color bound is retained separately.
The entire statement concerns the actual ordinary-next
canonical family and the independent lower plateau
\(y\in P+ih_y\). Incoming pieces outside the union (22)
retain their separate source obligations. This note does
not estimate the lower period
outside that plateau, substitute a terminal reference,
or establish a whole next-transfer asymptotic.
