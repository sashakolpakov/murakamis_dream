# A holomorphic packet for the complete Fourier right cap

Research theorem, 7 November 2026. The completed right-cap
asymptotic persists on a small complex neighborhood of each
actual incoming reference and the original Fourier output.
The proof keeps the global contours at their center values,
extends the strict estimates on their bounded parts, and
uses the exact uniform factorial bounds on their infinite
ends. The finite main rectangle is then translated to the
nearby holomorphic critical point, retaining its boundary faces.

This supplies fixed derivatives of the normalized whole-source
packet. No new root certificate, source evaluation or numerical
run is used.

## 1. Fixed center and moving original phase

Fix
\[
 \lambda_0=(a_0,y_0),\qquad a_0\in K_{3+\eta},\quad
 y_0=x_0,\quad \eta\in\{0,1\},
\]
and its original critical pair \(z_0=(s_0,q_0)\).
Use the finite function \(V_N^{\rm F}(y,e^{-2\pi ia})\)
and unallocated phase \(F_0(s,a,q;y)\) of
[the full actual-reference theorem](research_mixed_fourier_right_cap_full_asymptotic.md).
The finite function is holomorphic in \((a,y)\): its
finite sum uses \(X^{-j}p_j(X)\), \(X=e^{-2\pi ia}\ne0\),
and the entire cardinal coefficients in the lifted \(y\).
No principal logarithm of \(Y=e^{2\pi iy}\) replaces that lift.

The analytic implicit-function theorem and the center
accretive Hessian give a small parameter polydisk \(U_0\)
and a holomorphic critical pair
\[
 z(\lambda)=(s(\lambda),q(\lambda)),\qquad
 F_{0,s}=F_{0,q}=0,\qquad z(\lambda_0)=z_0.
\tag{1}
\]
All local factorial and cardinal arguments retain their
original branches after shrinking \(U_0\). Set
\[
\begin{split}
 \Phi(\lambda)&=F_0(s(\lambda),a,q(\lambda);y),\\
 H(\lambda)&=-F_{0,(s,q)(s,q)}
                       (s(\lambda),a,q(\lambda);y),\\
 \mathcal A(\lambda)&=
       \frac{2\pi\,\mathfrak b(s(\lambda),a,q(\lambda);y)}
                                  {\sqrt{\det H(\lambda)}},\\
 m_\eta(\lambda)&=\Re\Phi(\lambda)-\frac{\eta}{2}\Re g(a).
\end{split}
\tag{2}
\]
The symbol \(\mathfrak b\) and accretive Gaussian branch
are those of the cited theorem. Thus \(\Phi,\mathcal A\)
are holomorphic, \(\mathcal A\ne0\), and \(H\) remains
accretive. These local facts alone do not prove the result.

Freeze \(h_s=\Im s_0\), \(h_q=\Im q_0\), the left taper,
all real half-grid cuts, the retained caps, and the outgoing
main path at their center values. In particular these
contours are not defined using the real or imaginary parts
of (1). Their exact identities remain valid for nearby
parameters. The numerator uses its original holomorphic
global continuation. No shifted meromorphic chart is
needed for this proof.

## 2. Persistence of the bounded source comparisons

The exact reductions in
[the main-contour proof](research_mixed_fourier_right_cap_main_reduction.md),
[the complete right-horizontal theorem](research_mixed_fourier_right_horizontal_completion.md),
and the actual-reference theorem use the following groups.

| Group | Representation retained before estimation |
|---|---|
| High physical retained indices | The complete outgoing Wall contraction at each physical retained index |
| Bounded outgoing vertical current | The left-period polynomial interpolation and the two distinct zero-safe cardinals |
| Short real segment, left taper, right return | Their complete retained contours, with small physical rows separate |
| Right main and nonpositive retained corrections | The original joint chart with its complete Fourier denominators |
| Positive retained corrections | Coupled transport, left face on the high cap, right face on its two replacement paths |
| Central plateau corrections | Original inner aliases, both vertical sides and negative-height joins |

There are finitely many contour pieces and source-profile
types. The physical row and layer counts grow polynomially
in \(N\), not through an increasing list of analytic
estimates. The old growing upper profile and the failed
raw physical-face criterion are not used instead of the
paid representations in the table.

Fix for now finite cutoffs for the vertical and shear
parameters. All regular factorial profiles range over
fixed compact sets. Their rates are continuous in
\(\lambda\), and their exact finite upper bounds are
uniform on a small parameter neighborhood. The endpoint
cases use upper bounds rather than nonzero symbols:

1. Physical factorials retain
   \(\log|P_j|=N J(j/N)+O(\log N)\), including endpoints.
   Incoming finite products use the original truncated-log
   upper bound, also at zeros.
2. The short outgoing endpoint and reciprocal zeros use
   finite-shift product bounds for \(E_N\); no vanishing
   product is inverted.
3. On the bounded vertical current, the line
   \(v=\Im y\) moves with the parameter. The two cardinal
   rates \(K(v;y)\) join continuously there, and their
   finite upper bound is zero-safe on the whole compact
   set, not just on either nonzero-symbol region.

For item 3 the sources are
[the real-endpoint envelope](research_mixed_fourier_real_endpoint_vertical_envelope.md)
and
[the full vertical-current proof](research_mixed_fourier_right_cap_vertical_current_completion.md).
The exact midpoint factorial handles the remaining
\(N\)-dependent endpoint; its modulus identity is parameter
independent. The right output uses physical periodicity
before the left interpolation and retains its own cardinal.

Each paid bounded profile has a strict gap at \(\lambda_0\).
This includes the pointwise profiles on the replacement
high and negative caps in
[the right-endpoint shear comparison](research_mixed_fourier_right_endpoint_shear_comparison.md).
It does not assert that the unreplaced right upper profiles
are individually small. Compact continuity preserves a
smaller gap relative to the continuous \(m_\eta(\lambda)\).
The finite-source tolerances are chosen once below it.

The left-taper certificate is used in the same way. The
center taper remains fixed. Its bounded profiles have
the strict calibrated gaps of
[the full left-taper source theorem](research_mixed_fourier_left_taper_source_completion.md).
Their continuous rates and zero-safe endpoint upper
bounds persist on a neighborhood. A new parameter is
not declared an input of the frozen certificate, and
its test is not repeated.

## 3. The coherent high rows already have a complex parameter packet

The high group is not estimated term by term in its
outgoing index. The
[half-degree Wall theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md),
Theorem 1, is uniform on a complex neighborhood of
\(Y_0=e^{2\pi iy_0}\), including degree zero. Its exact
original identity is
\[
 H_{j,N}(y)=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}
                  P_jW_{N-j-1,N}(Y;Y).
\tag{3}
\]
For \(\lceil N/2\rceil\le j<N\), its degree
\(n=N-j-1\) is in the certified half-degree range.
Write \(I_{\rm W}(t,Y)\) for the initialized action,
with its original logarithmic lift. It is analytic
near the closed interval \(0\le t\le1/2\), uniformly
for nearby \(Y\). Its derivative \(\log R(t,0,Y)\)
is bounded. Replacing \(n/N\) by \(1-j/N\) in the
rate thus costs only a uniformly bounded factor.

Put
\[
 I_a(s)=\int_0^s\log|1-e^{-2\pi ia}e^{-2\pi iv}|\,dv .
\]
The allocated upper rate from (3) and the original
physical products is
\[
\begin{split}
 E_{\rm hi,\eta}(s;\lambda)
 ={}&I_a(s)-2J(s)-2\pi(\Im a)s+\pi\Im y\\
 &+\Re I_{\rm W}(1-s,Y)-\frac{\eta}{2}\Re g(a),
                         \qquad 1/2\le s\le1.
\end{split}
\tag{4}
\]
This is the original calibrated coherent retained rate.
It is continuous also at \(s=1\). The integral \(I_a(s)\)
is jointly continuous when a logarithmic zero crosses
its integration interval. The finite product upper bound
remains uniform across \(|X|=1\), as proved in
[the retained-rate source theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md),
Section 1.

The center comparison in
[the coherent high-tail payment](research_mixed_fourier_right_cap_coherent_high_tail_payment.md)
is
\[
 E_{\rm hi,\eta}(s;\lambda_0)
          \le m_\eta(\lambda_0)-1/35000
                         \qquad(1/2\le s\le1).
\tag{5}
\]
Compact continuity of (4), the uniform complex-\(Y\)
Wall packet, and the zero-safe products preserve a
strict gap for the entire group on a neighborhood.
No new degree root or sign selection is needed.
The row \(j=N-1\) uses the exact degree-zero
initialization in (3).

## 4. Fixing the infinite-height cutoffs before perturbing

There are two kinds of noncompact ends. Both retain
their exact finite-level damping.

For the original outgoing upper tail, the proof in
[the uniform outgoing-tail theorem](research_mixed_fourier_vertical_tail_payment.md)
uses the rate
\[
 I_a(s)-3J(s)-2\pi(\Im a)s+D_+(y)
 -\frac{\eta}{2}\Re g(a)-\pi(1-2s)H,\qquad
 D_+(y)=\Re g(1-y)-2\pi(\Re y)(\Im y).
\tag{6}
\]
At \(s=1/2\) the center has a fixed strict gap, supplied
by the coherent half-index comparison. It persists on
a small fixed \(s\)-collar and parameter neighborhood.
On the rest of \(0\le s\le1/2\), \(1-2s\) has a fixed
positive lower bound. Choose one large \(H\) paying the
center compact excess with strict room, then shrink the
parameter neighborhood to preserve that room.

The exact residual upper damping for \(j\le M_N\) is
\[
 e^{-\pi(N-2j)(v-H)},\qquad
 N-2M_N=
 \begin{cases}2,&N\text{ even},\\1,&N\text{ odd}.\end{cases}
\tag{7}
\]
It is independent of \(a,y\). The parity reserve is not
replaced by the limiting zero slope at \(s=1/2\).
The lower outgoing end has damping coefficient
\(2\pi N(1-\Re y)\), uniformly positive nearby; its
continuous compact excess is paid by the same fixed-height
method. The exact remainder per level is bounded by
\(\epsilon(H)\to0\), using an upper bound for \(\Im y\)
on the enlarged parameter box. Thus no fixed-\(N\)
constant is promoted to a uniform one. The bounded
interval \([-H,H]\) is then covered by Section 2,
including its moving reciprocal-zero line.

For the coupled shear tails, Lemma 3 of
[the uniform connector proof](research_mixed_fourier_retained_side_shear_connectors.md)
comes from
\[
 |e^{2\pi iNs(t)}T_N(s(t),q(t))|
       =C_N e^{-\Lambda_N(u)t+\Re R_N(t)},\qquad
 \Lambda_N(u)=2\pi\{N(2u-\Re y)+1\}.
\tag{8}
\]
The shared numerator is constant along the shear.
The identity covers all fixed replacement-cap offsets.
On a slightly enlarged parameter box one may require
\(|\Im a|<.12\), \(\Re y<.19\), \(0<\Im y<.1\).
The lower remainder arguments then have depth at least
\(t-.32\) and modulus at most \(t+3\). For example,
\[
 r_t=e^{-2\pi(t-.32)},\qquad
 \psi_U(t)=\frac{t+4}{2}\frac{r_t^2}{1-r_t^2}
                         +\frac12\frac{r_t}{1-r_t}
\tag{9}
\]
gives \(|R_N(t)|\le6N\psi_U(t)\) for \(t\ge1\),
uniformly on that box, and \(\psi_U(t)\downarrow0\).
The exact half-grid slope satisfies
\[
 N(2u-\Re y)+1
 \ge2\lceil N/8\rceil-N\Re y
 \ge N(1/4-\Re y)>0,\qquad u\ge\sigma_-.
\tag{10}
\]

Choose one large \(T\) for which \(12\psi_U(T)\) is
below a fixed fraction of the center connector gaps.
Compare the infinite end with its same finite source
at \(T\). On \([0,T]\), the paid replacement profiles
have the continuous strict gaps of Section 2.
Shrinking the neighborhood therefore gives uniform
infinite-height connector estimates.

The factors
\[
 \frac{Y^N}{1-Y^Ne^{-2\pi iNq}},\qquad
 \frac{e^{-2\pi iNq}}{1-e^{-2\pi iNq}}
\]
keep their original exponential numerators and zero-free
denominators. At the negative outgoing heights their
denominator ratios to the value at \(T\) are uniformly
bounded. The right comparison's factor
\(e^{-2\pi iN(s+q)}\) is exactly constant along the
shear and stays in that calibrated finite-height value.
It is not discarded as a harmless constant in \(N\).

## 5. A uniform global remainder on the fixed main contour

The infinite cutoffs are chosen first. Thereafter only
finitely many compact source families and the explicitly
uniform tails remain. Intersect their parameter
neighborhoods and choose the finite-source tolerances
below their remaining gaps. Every contour identity keeps
the original half-grid cuts, both parities, triangular
zeros, cardinal scalar and incoming allocation.

Let \(J_N^0(\lambda)\) be the integral (7) of the
actual-reference theorem, at the center heights
\(\Im s_0,\Im q_0\), with its original \(N^2\) density.
There are a polydisk \(U\ni\lambda_0\), \(\gamma>0\),
and \(N_0\) for which
\[
 |d_N(e^{-2\pi ia})|^{\eta/2}
  |V_N^{\rm F}(y,e^{-2\pi ia})-J_N^0(\lambda)|
       \le e^{N(m_\eta(\lambda)-\gamma)}
                         \quad(\lambda\in U,\ N\ge N_0).
\tag{11}
\]
This uses the actual finite-source estimates just
audited. It is not inferred from continuity of the
already summed finite function, whose parameter
derivatives could grow with \(N\).

For \(\eta=1\), choose the \(a\)-projection of \(U\)
inside the interior of the proved \(E_4\) rectangle.
The actual Fourier-weight theorem gives its uniform
nonzero lower bound, as in (19)--(20) of the
actual-reference theorem. Dividing only on this
zero-free neighborhood changes \(m_1(\lambda)\) to
\(\Re\Phi(\lambda)\), with a polynomial cost.
For \(\eta=0\) no division is involved. After decreasing
the gap, both cases give
\[
 |V_N^{\rm F}(y,e^{-2\pi ia})-J_N^0(\lambda)|
                  \le e^{N(\Re\Phi(\lambda)-\gamma/2)}.
\tag{12}
\]
No incoming-weight nonvanishing on an entire horizontal
target interval is asserted.

## 6. Translating the main rectangle to the nearby saddle

The saddle (1) need not lie on the center horizontal
contour. Define the holomorphic displacements
\[
 \Delta_s(\lambda)=s(\lambda)-s_0,\qquad
 \Delta_q(\lambda)=q(\lambda)-q_0 .
\tag{13}
\]
Translate the retained main segment by \(\Delta_s\),
and then the outgoing segment by \(\Delta_q\).
The translated product is
\[
\begin{split}
 \mathcal D_N(\lambda)=
 &\bigl([\sigma_-,\sigma_+]+ih_s+\Delta_s(\lambda)\bigr)\\
 &\quad\times\bigl(P+ih_q+\Delta_q(\lambda)\bigr).
\end{split}
\tag{14}
\]
It contains the moved saddle at the same interior real
parameters \(\Re s_0,\Re q_0\) as before translation.
All its factors stay in a common regular neighborhood.

Apply one-variable Cauchy first to the retained segment
for every outgoing point. This retains both swept
retained endpoint segments, each times the old outgoing
segment. Then apply Cauchy in the outgoing variable
on the translated retained segment, retaining its two
swept outgoing endpoint faces. These are all four
product-boundary faces. No pole is crossed: the sum
arguments and the separate factorial arguments stay
in the original regular strips of this central rectangle.

At the center every point on its boundary has a fixed
positive quadratic loss. The limiting retained distance
is at least \(23/200\), and the outgoing distance is
at least \(1/50\); the finite half-grid changes preserve
a smaller positive loss. For sufficiently small \(U\),
all four swept faces remain close to that boundary.
Compact continuity of the phase, including the moved
critical value \(\Phi(\lambda)\), leaves a uniform
positive loss on every face. The exact row symbol is
uniform there. The short connecting lengths and density
\(N^2\) only contribute bounded or polynomial factors.
Thus, for some \(\gamma_1>0\),
\[
 J_N^0(\lambda)
   =N^2\int_{\mathcal D_N(\lambda)}
              T_N(s,q;a,y)\,ds\,dq
        +O\!\left(e^{N(\Re\Phi(\lambda)-\gamma_1)}\right),
\tag{15}
\]
uniformly on a smaller polydisk.

On the translated rectangle the negative real Hessian
keeps a uniform positive floor. Indeed it does so on
the center compact rectangle, with strict room, and
the parameters and both displacements are small.
The gradient vanishes at (1). Integrating this
curvature along the translated real segments gives
strict quadratic decay from the moved saddle throughout
(14). Consequently no stationary point has been left
off the contour in the following Gaussian calculation.

The row expansion on a common neighborhood is
\[
 T_N(s,q;a,y)=
 N^{-5/2}\mathfrak b(s,a,q;y)e^{NF_0(s,a,q;y)}
                                      (1+O(N^{-1})).
\tag{16}
\]
Its fixed derivatives are uniform on smaller domains.
A small symmetric box around the moved saddle has
the original accretive Gaussian branch, while the
rest of (14) has a fixed exponential loss.
The \(N^{-1/2}\) rescaling cancels the odd linear-symbol
and cubic-phase terms. The remaining Taylor terms and
symbol error give a relative \(O(N^{-1})\) remainder.
It follows that
\[
 N^2\int_{\mathcal D_N(\lambda)}T_N\,ds\,dq
    =N^{-3/2}\mathcal A(\lambda)e^{N\Phi(\lambda)}
                                      (1+O(N^{-1})),
\tag{17}
\]
uniformly in the parameter neighborhood. The coefficient
is exactly (2), with no new scalar or branch choice.
Parameterizing (14) by its fixed real segments also
shows directly that its integral is holomorphic.

**Theorem.** For each center \((a_0,x_0)\) in Section 1,
there is a fixed complex neighborhood \(U\) on which,
at both integer level parities,
\[
 \boxed{\quad
 V_N^{\rm F}(y,e^{-2\pi ia})
   =N^{-3/2}\mathcal A(a,y)e^{N\Phi(a,y)}
                           \{1+\varepsilon_N(a,y)\},
             \qquad \mathcal A\ne0 .
 \quad}
\tag{18}
\]
The normalized errors are holomorphic. On every smaller
\(U'\Subset U\), for every fixed parameter multi-index
\(\alpha\),
\[
           \sup_{U'}|\partial^\alpha\varepsilon_N|
                                 \le C_{\alpha,U'}/N .
\tag{19}
\]

Combine (12), (15) and (17), shrinking once more so
that \(\mathcal A\) is bounded away from zero.
The exponentially small errors remain smaller than
\(O(N^{-1})\) after the normalization in (18).
The normalized finite expression is holomorphic;
Cauchy's estimates on nested parameter neighborhoods
give (19).

The whole finite source is nonzero on each such smaller
neighborhood for all sufficiently large \(N\). At the
center its phase and coefficient are exactly those of
the actual-reference theorem. Their derivatives are
derivatives of the original stationary action.
This is a local holomorphic packet for the complete
right cap. It does not assert a global incoming-period
norm, uniformity under arbitrarily many attachments,
or noncancellation for an unexamined boundary contraction.
