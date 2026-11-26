# The complete lower continuation of the shortened second edge

Private written finite-source proof, 8 November 2026. The entire
remaining lower integral in the joined-contour representation is
exponentially below the selected wire action. Its path continues
the first-quarter horizontal to the quarter face, descends there,
and uses a deep lower horizontal before returning to the paid
right endpoint. No internal real cut is introduced.

The upper continuation is unchanged and remains unestimated.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original source and statement

Use the actual compact positive outer family and selected cubic
branch from
[the first-quarter theorem](research_mixed_next_two_angle_bare_first_quarter_contour.md):
\[
 u=b-iK,\quad 0\le b\le\pi/2,\quad0\le K\le1/2,
 \qquad t=t(u)=a-iH,\quad0<a<\pi/2,\quad0<H<1.
 \tag{1}
\]
Their cosines have nonnegative real and imaginary parts, with
\(\Re\cos t>0\), \(\Im\cos t>0\) uniformly on this compact
family. The original selected wire action and height are
\[
 \psi(t,u)=F(y_*;t,u),\qquad h_*=\Im y_*>0 .
 \tag{2}
\]
All logarithmic lifts and additive constants are those of the
original factorial source.

Keep precisely the cuts and interpolation of
[the adopted joined-contour representation](research_mixed_next_shortened_edge_joined_contour.md):
\[
 U=\lfloor N/2\rfloor-1,\qquad
 \alpha_N=(\lfloor N\alpha\rfloor+1/2)/N,\qquad
 \gamma_N=(\lceil N\gamma\rceil-1/2)/N,
 \tag{3}
\]
where \(\gamma=1/2-\delta/2\) lies inside the already paid
right physical interval \([1/2-\delta,1/2]\).
Its fixed cap height satisfies \(0<h_c<\tfrac12\min h_*\).
The old first-quarter cut is
\[
 \beta_N=(\lfloor N\beta\rfloor+1/2)/N,\qquad
 \max_{\mathcal U_+}\Re y_*<\beta<1/4.
 \tag{4}
\]
The complete canonical product is
\[
\begin{split}
 B_N(y,z)
 &=\frac{N}{
  G_N(N(1/2-y+z/(2\pi))-1/2)
  G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u).
\end{split} \tag{5}
\]
It is holomorphic throughout \(0<\Re y<1/2\), at all finite
heights, with the original reciprocal reflection factors
retained. Its lattice values are the exact Newton rows.

For any piecewise smooth lower-half-strip path \(\Upsilon_-\)
from \(\beta_N-ih_*\) to \(\gamma_N-ih_c\), set
\[
 \mathcal R_N^-=
 N\int_{\Upsilon_-}
       \frac{T_N(y;t,u)}{e^{2\pi iNy}-1}\,dy .
 \tag{6}
\]
This integral is independent of the chosen path in the indicated
simply connected half-strip. Its denominator is the exact sum of
the original lower Fourier corrections.

**Theorem.** There is a fixed \(\epsilon_->0\) such that
\[
 \boxed{\qquad
 |\mathcal R_N^-|\le C e^{N(\Re\psi(t(u),u)-\epsilon_-)},
                   \qquad u\in\mathcal U_+ ,
 \qquad} \tag{7}
\]
for all sufficiently large levels of either parity.
No assumption about the upper continuation is used.

## 2. Strict lower-height decrease on and to the right of the quarter

Let \(y=x-iv\), \(1/4\le x<1/2\), \(v>0\).
For either angular parameter \(z=\theta-iA\) in (1), the
original lower phase is holomorphic in these wire variables:
\[
 b(y,z)=
 -J(1/2-y+z/(2\pi))-J(1/2-y-z/(2\pi))-2J(y).
 \tag{8}
\]
The first shifted argument has positive real part; the second
has positive imaginary part, even when its real part is negative.
Thus its upper reciprocal-factorial continuation is the original
one throughout this lower wire strip. In particular the original
sidewise upper exponent is exactly \(\Re b\) here, with no reset
of its logarithm.

Write
\[
 \zeta=\cos(2\pi y)=p+iq,\qquad
 \cos z=A_0+iB_0 .
 \tag{9}
\]
On this strip \(p\le0,\ q>0,\ A_0,B_0\ge0\).
The exact derivative satisfies
\[
 e^{b_y(y,z)}=\frac{\zeta+\cos z}{1-\zeta}.
 \tag{10}
\]
The imaginary numerator after division is
\[
 q(1+A_0)+B_0(1-p)>0 .
 \tag{11}
\]
Neither numerator nor denominator vanishes. Hence the quotient
in (10) is strictly in the upper half-plane.

The original lift in (10) has
\[
                  0<\Im b_y(y,z)<\pi .
 \tag{12}
\]
To check the lift rather than only its exponential, send \(v\)
to infinity in the original \(J\) derivatives in (8).
They give \(b_y(y,z)\to i\pi\). The upper-half-plane quotient
is continuous and nonzero for all \(v>0\), so its principal
argument is the original one. The same argument applies when
an angular height or its real part is zero.

The same lower phase \(F_-=b(\,\cdot\,,t)+b(\,\cdot\,,u)\)
is defined throughout \(0<\Re y<1/2,\ \Im y<0\). Define its
penalized real rate on that whole strip by
\[
       G_x(v)=\Re F_-(x-iv;t,u)-2\pi v .
 \tag{13}
\]
Equations (12)--(13) give the strict inequality
\[
                 G_x'(v)=\Im F_{-,y}(x-iv;t,u)-2\pi<0,
                  \qquad 1/4\le x<1/2,\quad v>0.
 \tag{14}
\]
The rates extend continuously to \(v=0\), including real
numerator zeros. Thus (14) bounds each entire lower vertical
segment by its shallower endpoint. It is a direct original
lower-branch comparison, not the reflected-ray inequality
that fails near the right endpoint.

## 3. A uniformly paid lower horizontal at height one

The original additive constants can be kept explicitly.
On the argument ranges used here, at positive or negative
imaginary part respectively,
\[
\begin{split}
 J_+(w)&=-\frac{i\pi}{2}(w^2-w+1/6)
                  +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iw}),\\
 J_-(w)&=\frac{i\pi}{2}(w^2-w+1/6)
                  -\frac{i}{2\pi}\operatorname{Li}_2(e^{-2\pi iw}).
\end{split} \tag{15}
\]
Differentiation gives the original logarithmic sine derivatives;
the constant follows from \(J(0)=0\) and
\(\operatorname{Li}_2(1)=\pi^2/6\).
These are the sidewise branches used in (8).

At \(y=x-i\), both shifted arguments in each leg have positive
imaginary part, while \(y\) has negative imaginary part.
Substitution in (8) yields the exact polynomial part
\[
 b(y,z)=i\pi y+\frac{i z^2}{4\pi}-\frac{i\pi}{4}
                    +\mathcal E_z(y),
 \tag{16}
\]
where \(\mathcal E_z\) is the sum of its three indicated
dilogarithms in (15), with coefficients of magnitudes
\(1/(2\pi),1/(2\pi),1/\pi\).
Every dilogarithm argument has modulus at most
\[
 r_*=e^{1-2\pi}<e^{-5}<1/100 .
 \tag{17}
\]
For a written elementary witness to the last inequality,
\[
 e^5>
 1+5+\frac{25}{2}+\frac{125}{6}
       +\frac{625}{24}+\frac{3125}{120}+\frac{15625}{720}
 =\frac{81445}{720}>100 .
 \tag{18}
\]
The convergent power series gives
\(|\operatorname{Li}_2(w)|\le |w|/(1-|w|)\) for \(|w|<1\).
For the two legs together this proves
\[
 |\mathcal E_t(x-i)+\mathcal E_u(x-i)|
       <\frac{4}{99\pi}<\frac{4}{297}<\frac1{50}.
 \tag{19}
\]
All bounds are uniform for \(0<x<1/2\) and for the actual
family (1).

The real polynomial part in (16), after the full lower Fourier
penalty is included, is
\[
 \Re F_-(x-i;t,u)-2\pi
       =\frac{aH+bK}{2\pi}
                   +\Re(\mathcal E_t+\mathcal E_u).
 \tag{20}
\]
Since \(a,b\le\pi/2\), its first term is at most
\((H+K)/4\). The adopted
[right-end action gap](research_mixed_next_shortened_edge_endpoint_gap.md)
gives the original selected comparison
\[
                 \Re\psi(t,u)>\frac{H+K}{2}+\frac1{25}.
 \tag{21}
\]
Combining (19)--(21) gives the uniform deep-horizontal bound
\[
           G_x(1)<\Re\psi(t,u)-\frac1{50}.
 \tag{22}
\]
No phase constant or integer charge has been removed.

## 4. The quarter endpoint of the established lower horizontal

We need the first-quarter lower comparison through its limiting
quarter face. Write the reflected difference of the original
sidewise upper exponents as
\[
 D_x(v)=\mathfrak F(x-iv;t,u)-\mathfrak F(x+iv;t,u).
 \tag{23}
\]
For \(x<1/4\), its derivative is the sum, for the two angles,
of
\[
 \Arg\{R_v+i(B_0+B_v)\}
       +\Arg\{R_v+i(B_0-B_v)\},
 \quad
 R_v=\cos(2\pi x)\cosh(2\pi v)+A_0,\quad
 B_v=\sin(2\pi x)\sinh(2\pi v).
 \tag{24}
\]
This is the exact first-quarter argument comparison, not a
new source interpolation.

For the \(t\) leg, \(\Re\cos t>0\) uniformly on the compact
family. Thus \(R_v\) stays uniformly positive up to \(x=1/4\).
Its contribution in (24) remains uniformly less than \(\pi\)
on the bounded height range \(0\le v\le\max h_*\).
The \(u\) contribution is at most \(\pi\) through that face.
If its numerator vanishes at \(x=1/4\), the assertion is
understood by a one-sided limit and integration; the
sidewise exponent is continuous, and the argument bound
holds away from the zero. Consequently, on the compact
interval from the old right cut to the quarter, some fixed
\(\eta>0\) satisfies
\[
                   D_x(v)\le(2\pi-\eta)v .
 \tag{25}
\]
One may first prove this for \(x<1/4\), where all real
denominators in (24) are positive, and then pass to the
quarter using the zero-safe continuity of the integrated
logarithms.

The adopted first-quarter horizontal curvature is strictly
negative all the way up to that limiting face. Therefore
the horizontal through \(y_*\), to the right of \(\beta_N\),
stays below its value at \(\beta_N+ih_*\). By its established
strict endpoint gap and compactness, a fixed \(\epsilon_\beta>0\)
gives
\[
 \mathfrak F(x+ih_*;t,u)\le\Re\psi-\epsilon_\beta,
            \qquad \beta_N\le x\le1/4
 \tag{26}
\]
for all large levels. A possible quarter-face numerator zero
uses the continuous upper rate in (26), not a relative
factorial symbol. Equations (25)--(26) prove
\[
                G_x(h_*)\le\Re\psi-\epsilon_\beta
                      \qquad(\beta_N\le x\le1/4).
 \tag{27}
\]
The \(O(N^{-1})\) displacement of the original half-grid cut
is absorbed in this fixed positive reserve.

Finally \(h_*<1\). For example, the original tangent-ray graph
has height
\[
 \frac1{2\pi}
   \operatorname{arsinh}\{\tan(\arg\sqrt W)\sin(2\pi x)\},
 \qquad0<\arg\sqrt W<\pi/4,
 \tag{28}
\]
so its maximum is less than
\(\operatorname{arsinh}(1)/(2\pi)<1\).
In particular the vertical descent used next starts above
the level \(-1\).

## 5. One complete lower path and the exact remaining term

Choose the following lower path, always directed from left
to right overall:
\[
\begin{split}
 \beta_N-ih_*&\longrightarrow1/4-ih_*\\
             &\longrightarrow1/4-i\\
             &\longrightarrow\gamma_N-i\\
             &\longrightarrow\gamma_N-ih_c .
\end{split} \tag{29}
\]
Its first segment is bounded by (27). On its second segment,
(14) decreases the penalized rate from the same paid
quarter endpoint. Its third segment has the explicit gap
(22). On the final segment, (14) bounds the rate at every
depth by its continuous real endpoint value.
For all large \(N\), \(\gamma_N\) is inside the fixed paid
right interval, where the right-end theorem proves
\[
 \mathfrak F(\gamma_N;t,u)<\Re\psi-\frac3{100}.
 \tag{30}
\]
Thus every point of (29), with the lower Fourier penalty
included, has a fixed positive deficit. There is no separate
vertical side or estimate at the old real cut \(\beta_N\).

The path has uniformly bounded length and stays at height
at most \(-h_c<0\). The exact denominator obeys
\[
 \left|\frac1{e^{2\pi iN(x-iv)}-1}\right|
 \le\frac{e^{-2\pi Nv}}{1-e^{-2\pi Nv}}
 \le2e^{-2\pi Nv}
 \qquad(v\ge h_c)
 \tag{31}
\]
for all large levels. The original uniform factorial upper
bound on this fixed compact path retains both reciprocal
reflection terms, with only a fixed polynomial prefactor.
Multiplying it by (31), integrating the four segments, and
retaining the original prefactor \(N\) in (6) proves (7).
For example, after decreasing the fixed gaps if necessary,
one may take any sufficiently small positive number below
\(\tfrac14\min(\epsilon_\beta,1/50,3/100)\).

All deformations stay in the open lower half-strip, where
both the canonical source and the exact Fourier denominator
are holomorphic. Cauchy's theorem identifies the result with
the literal lower continuation in the adopted joined
representation, for any originally chosen eligible path.
There is no crossing of a physical pole, no truncation of
integer Fourier frequencies, and no parity-dependent row loss.

It follows from equation (17) of that representation that
\[
 \boxed{\quad
 K_N^{<}(t(u),u)
   = I_N^{\rm edge}
       +N\int_{\Upsilon_+}
          \frac{T_N(y;t(u),u)}{1-e^{2\pi iNy}}\,dy
       +O(e^{N(\Re\psi-\epsilon)}),
 \quad} \tag{32}
\]
where \(\epsilon>0\) is fixed and the original nonzero
Gaussian integral is
\[
 I_N^{\rm edge}
    =N^{-3/2}a_e(t(u),u)e^{N\psi(t(u),u)}(1+O(N^{-1})).
 \tag{33}
\]
The integral in (32) is still the complete upper continuation
from \(\beta_N+ih_*\) to \(\gamma_N+ih_c\), with its exact
upper Fourier denominator. It is not included in the error.
The known Gaussian relative error in (33) is also not relabeled
as an exponential error.

This result pays one complete remaining finite-source current.
It does not yet prove a packet for the shortened edge, a
complete inner trace estimate, an outer signed-observation
bound, new parameter jets, or noncancellation of the transfer.
