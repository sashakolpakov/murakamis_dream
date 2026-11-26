# The complete left connection for the shortened inner source

Private finite-source theorem, 8 November 2026. This proof bounds
the path from the original negative far endpoint to the controlled
negative horizontal. Both edges have their literal cutoff
\(U=\lfloor N/2\rfloor-1\), and the angular Fourier denominator
and original trace prefactor are retained. No mathematical numerical
evaluation or change to a frozen source is used.

## 1. Source, path, and assertion

Put
\[
\begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N^{<<}(t,u)=K_N^<(t,0)K_N^<(t,u),\\
 g_N^{<<}(t,u)=\sin t\,f_N^{<<}(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered} \tag{1}
\]
The Newton normalization and the full Hermite trace are those in
[the first-edge tail contraction](research_mixed_next_inner_three_first_edge_tail_contraction.md).
That trace-level reduction has already paid the deleted first-edge
rows. It is not used as a pointwise equality in this proof.

Keep the original outgoing family and selected critical data:
\[
\begin{gathered}
 u=b-iK,\quad 0\le b\le\pi/2,\quad0\le K\le1/2,\\
 t_*(u)=a_*(u)-iH(u),\quad0<a_*<\pi/2,\quad1/2<H<1,\\
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u),\\
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it .
\end{gathered} \tag{2}
\]
All constants and logarithmic determinations are unchanged.

Let \(h_c>0\) be the fixed small endpoint height in the
[inner boundary theorem](research_mixed_next_inner_three_far_samples_and_verticals.md),
and use its exact half-grid cut
\[
 T_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},
 \qquad a_F=\pi-\frac{\pi}{2000}.
 \tag{3}
\]
For all sufficiently large \(N\),
\[
 a_F\le T_N\le \pi-\frac{\pi}{4000}<\pi,\qquad
 e^{iNT_N}=-\eta_N .
 \tag{4}
\]
For example the upper inequality follows from
\(\lfloor N/4000\rfloor\ge N/8000\) when \(N\ge8000\).

Choose the following particular left connection:
\[
 \Gamma_L:
 -T_N-ih_c\ \longrightarrow\ -T_N-iH(u)\
             \longrightarrow\ -\pi/2-iH(u).
 \tag{5}
\]
Its first segment is vertical downwards and its second segment
is horizontal from left to right. It is entirely in the open
lower half-plane.

**Theorem.** Uniformly on the family (2), for sufficiently large
levels of both parities,
\[
 \boxed{\quad
 \frac{N^2}{\pi}\int_{\Gamma_L}
       |g_N^{<<}(t,u)W_N(t)|\,|dt|
             \le C e^{N(s(u)-1/5)} .
 \quad} \tag{6}
\]
In particular the signed original current along this path has
the same upper bound, because \(|C_{N,3}|=1\). This estimates
the whole left connection, not just its endpoints. The negative
middle interval and the right connection are separate.

## 2. A finite bound with a real outgoing angle

We use the actual all-row and real-period conclusions of
[the slit-plane source theorem](research_mixed_next_first_short_edge_slit_plane_bound.md).
For every fixed compact set of first angles
\[
 t=a-ih,\qquad \pi/2\le a\le\pi-\pi/4000,\qquad 0\le h\le1,
 \tag{7}
\]
and every \(\epsilon>0\), that theorem gives
\[
 \sup_{v\in[-\pi,\pi]}|K_N^<(t,v)|
       \le C_\epsilon N^{A_\epsilon}
                 e^{N(\Re\psi(t,0)+\epsilon)}.
 \tag{8}
\]
These first angles map by \(w=-2\cos t\) to a compact subset
of \(\mathbb C\setminus[2,\infty)\). At \(h=0\) their real
values are strictly below \(2\); at \(h>0\) their imaginary
parts are strictly negative. Thus the slit theorem is being
used on its stated finite-source domain, including the real
bottom of every vertical segment.

For fixed \(t\), the polynomial \(K_N^<(t,v)\) has degree
at most \(U\) in \(-2\cos v\). The real period covers
\([-2,2]\). Its Chebyshev coefficients have modulus at most
twice the supremum in (8), and
\[
 |T_j(\cos(b+iK))|\le e^{jK}.
 \tag{9}
\]
Consequently (8) continues to either sign of the outgoing
height with the additional rate \(UK\le NK/2\):
\[
 |K_N^<(a-ih,b\pm iK)|
 \le C_\epsilon N^{B_\epsilon}
          e^{N(\Re\psi(a-ih,0)+K/2+\epsilon)}.
 \tag{10}
\]
This is continuation of the exact polynomial, rather than
continuation of a local asymptotic expansion.

The original Newton polynomials have real coefficients and
are even functions of their angular arguments. Hence
\[
\begin{split}
 |K_N^<(-a-ih,0)|&=|K_N^<(a-ih,0)|,\\
 |K_N^<(-a-ih,b-iK)|&=|K_N^<(a-ih,b+iK)|.
\end{split} \tag{11}
\]
Multiplying (8) at \(v=0\) and (10), we obtain the uniform
finite-source estimate
\[
 |f_N^{<<}(-a-ih,u)|
 \le C_\epsilon N^{B_\epsilon}
    e^{N\{2\Re\psi(a-ih,0)+K/2+2\epsilon\}}
 \tag{12}
\]
on all of (7). No lower bound or nonvanishing of either
kernel is required for (12).

## 3. The horizontal part is uniformly smaller

On the fixed-height horizontal \(t=-a-iH(u)\),
\[
 |W_N(t)|\le C e^{-NH(u)},\qquad
 \left|e^{3iNt^2/(4\pi)}\right|
                            =e^{-3NaH(u)/(2\pi)}.
 \tag{13}
\]
The sine factor is bounded on (7). Thus the rate of the
whole integrand in (12), apart from its arbitrarily small
\(2\epsilon\), is
\[
 E(a,u)=2\Re\psi(a-iH,0)+K/2-H-\frac{3aH}{2\pi}.
 \tag{14}
\]
For \(0<a<\pi\), the original return
\[
 r_0=\operatorname{arsinh}\tan((a-iH)/2)
 \tag{15}
\]
has positive real part. The calibrated derivative is
\(\psi_t=-r_0/\pi\). Therefore
\[
 \partial_a\Re\psi(a-iH,0)<0,
 \qquad E(a,u)\le E(\pi/2,u)
                       \quad(\pi/2\le a\le T_N).
 \tag{16}
\]
These original branches extend throughout (7), as also
verified in the
[positive phase extension](research_mixed_next_inner_three_positive_horizontal_phase_extension.md).

It remains to compare the rate at \(\pi/2\) with the
critical action. The calibrated comparison in
[the far-negative source, equations (21)--(27)](research_mixed_next_inner_three_far_negative_source.md)
extends to that endpoint by continuity and gives
\[
 \Re\psi(\pi/2-iH,0)-\Re\psi(\pi/2-iH,u)
                         <\frac{263}{1250}+\frac{HK}{2\pi}.
 \tag{17}
\]
Its assumptions remain strict there:
\(|\cos((\pi/2-iH)/2)|^2=\cosh H/2<4/5<1\)
and \(\arg\cos((\pi/2-iH)/2)<H/2\).
The actual horizontal supporting inequality is
\[
 s(u)\ge
 \Re\psi(\pi/2-iH,0)+\Re\psi(\pi/2-iH,u)-H/4 .
 \tag{18}
\]
Subtracting (14) at \(a=\pi/2\) yields
\[
\begin{split}
 s(u)-E(\pi/2,u)
 &>\frac{3H}{2}-\frac K2-\frac{263}{1250}
                                       -\frac{HK}{2\pi}\\
 &>\frac12-\frac1{8\pi}-\frac{263}{1250}\\
 &>\frac{11}{24}-\frac{263}{1250}
                         =\frac{3719}{15000}>\frac15 .
\end{split} \tag{19}
\]
The second line uses \(H>1/2\), \(K\le1/2\), and the
positive coefficient \(3/2-K/(2\pi)\). The third uses
\(\pi>3\).

Choose \(\epsilon=1/1000\) in (12). After the loss
\(2\epsilon=1/500\), the reserve above \(1/5\) is still
\[
 \frac{3719}{15000}-\frac1{500}-\frac15
                           =\frac{689}{15000}>0.
 \tag{20}
\]
It absorbs the polynomial prefactor, the original \(N^2/\pi\),
and the uniformly bounded horizontal length. This proves
(6) for the horizontal part.

## 4. The whole far vertical is also paid

On \(t=-T_N-ih\), \(h_c\le h\le H(u)\), the half-grid
identity (4) gives the exact modulus
\[
 |W_N(-T_N-ih)|
       =\frac{e^{-Nh}}{(1+e^{-Nh})^2}\le e^{-Nh}.
 \tag{21}
\]
This bound would remain valid even at \(h=0\); no small
height denominator is being ignored.

For a fixed \(a\) in (7), the first return in (15) has
\[
 -\pi/2<\Im r_0\le0,\qquad
 \partial_h\Re\psi(a-ih,0)=-\frac{\Im r_0}{\pi}<\frac12 .
 \tag{22}
\]
Indeed \(\tan((a-ih)/2)\) is in the fourth quadrant
when \(h>0\), and its principal inverse hyperbolic sine
is on the same side with imaginary part strictly between
\(-\pi/2\) and zero. At \(h=0\) it is positive real.
The real source rate on the vertical,
\[
 E_v(a,h,u)=2\Re\psi(a-ih,0)+K/2-h-\frac{3ah}{2\pi},
 \tag{23}
\]
is consequently strictly decreasing in \(h\). In particular
\[
 E_v(T_N,h,u)\le 2\psi(T_N,0)+K/2 .
 \tag{24}
\]

Here is an exact small upper bound at the real far endpoint.
The complete phase has \(\psi(\pi,0)=0\), with its original
constant. Integrating its real derivative and using
\(\operatorname{arsinh}(\cot(x/2))=\log\cot(x/4)\) gives
\[
 \psi(\pi-\delta,0)
 =\frac1\pi\int_0^\delta\log\cot(x/4)\,dx
 <\frac{\delta}{\pi}\left(1+\log\frac4\delta\right).
 \tag{25}
\]
The strict inequality follows from \(\tan(x/4)>x/4\).
At \(\delta=\pi/2000\), it is less than \(1/200\):
\(\log(8000/\pi)<9\), since
\[
 e^3>1+3+\frac{3^2}{2}+\frac{3^3}{6}+\frac{3^4}{24}
       =\frac{131}{8}>16,\qquad
 e^9>4096>\frac{8000}{3}>\frac{8000}{\pi}.
 \tag{26}
\]
Since the real phase decreases in \(a\) and \(T_N\ge a_F\),
\[
 2\psi(T_N,0)+K/2<\frac1{100}+\frac14=\frac{13}{50}.
 \tag{27}
\]
The original action floor \(s(u)>79/63\), proved in the
inner boundary theorem, is greater than this rate by more
than \(1/2+1/500\). Thus the same choice of \(\epsilon\)
in (12), followed by polynomial absorption, proves
\[
 \frac{N^2}{\pi}\int_{h_c}^{H(u)}
 |g_N^{<<}(-T_N-ih,u)W_N(-T_N-ih)|\,dh
                     \le C e^{N(s(u)-1/2)} .
 \tag{28}
\]
Combining (28) with the horizontal bound proves (6).

## 5. Consequence for the remaining contour

The left path (5) is one of the eligible paths in
[the shortened-source transfer](research_mixed_next_inner_three_short_pair_source_transfer.md).
Its complete current is therefore exponentially smaller
than the original nonzero partial Gaussian contribution.
The proof uses a coarse bound on the second edge, whose
loss is offset by the sign of the crossing on the negative
angle. It supplies no corresponding positive-angle estimate.

After this connection is removed, the two unestimated
pieces of that decomposition are the negative middle
horizontal and the right connection. The outer trace
and the theorem for arbitrary fixed short fillings remain
subsequent obligations.
