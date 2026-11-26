# Bounding the outer closing contour across the imaginary axis

Private written finite-source deduction, 9 November 2026.
The complete inner asymptotic is proved on the positive lower
rectangle. It gives a strict bound near the left end of the outer
horizontal contour. Polynomial continuation extends that bound
across the imaginary axis to a fixed negative interval.
The argument keeps the full inner traces and the full outer
sampling denominator. It does not assume an inner asymptotic on
the negative half of the contour.

## 1. The exact functions and the interval to be bounded

Write \(D=N-1\). In the notation of the
[incoming-color theorem](research_mixed_symmetric_closing_incoming_neighborhood.md),
let
\[
 Q_N(w,u)=\phi_N\!\left[
 R_N^3\mathcal K_N(w,x)\mathcal K_N(x,-2\cos u)\right].
 \tag{1}
\]
For every fixed \(w\), this is a polynomial of degree at most
\(D\) in the ordinary outgoing coordinate \(z=-2\cos u\).
This is a property of the exact finite sum: only the traced
variable \(x\) is reduced in the original algebra.

For two incoming colors \(w_L,w_R\), put
\[
 \begin{split}
 F_N(u)&=Q_N(w_L,u)Q_N(w_R,u),\\
 W_N(u)&=\frac{e^{-iNu}}
              {(1-(-1)^{N-1}e^{-iNu})^2},\\
 G_N(u)&=\sin u\,F_N(u)e^{iNu^2/\pi}.
 \end{split}
 \tag{2}
\]
Thus \(F_N(u)=F_N^\sharp(-2\cos u)\), with
\(\deg F_N^\sharp\le2D\). These are exactly the functions in
the [outer closing contour](research_mixed_symmetric_343_closing_trace_and_domain.md),
whose horizontal prefactor is \(-N^2C_{N,4}/(\pi i)\), where
\(|C_{N,4}|=1\).

Let
\[
 u_g=\beta_g-iK_g,\qquad
 0<\beta_g<\pi/2,\quad17/30<K_g<7/10
 \tag{3}
\]
be the original geometric closing point. Let \(S_0(u)=S(-2,u)\)
be the original complete-color inner action and set
\[
 \Xi(u)=2S_0(u)+iu^2/\pi-iu,\qquad
 M_g=\Re\Xi(u_g).
 \tag{4}
\]
The [horizontal concavity theorem](research_mixed_symmetric_closing_horizontal_concavity.md)
proves
\[
 \Re\Xi(a-iK_g)
 \le M_g-\frac{(a-\beta_g)^2}{8\pi},
 \qquad 0\le a\le\pi/2.
 \tag{5}
\]
Both the actual point and the action in (4) keep their original
logarithmic normalization.

**Proposition.** There are fixed \(A,\eta,r,\epsilon>0\), with
\(0<\eta<A<\beta_g/2\), such that, uniformly for
\(|w_L+2|,|w_R+2|\le r\) and both parities,
\[
 \frac{N^2}{\pi}\int_{-\eta}^{A}
 \left|G_N(a-iK_g)W_N(a-iK_g)\right|\,da
 \le C e^{N(M_g-\epsilon)}
 \tag{6}
\]
for all sufficiently large \(N\).
This estimates the absolute integral of the original source,
not an integral of a proposed limiting phase alone.

## 2. A short positive interval

Define
\[
 \delta=\frac{\beta_g^2}{32\pi}>0.
 \tag{7}
\]
Choose \(A\) with \(0<A<\beta_g/2\), so small that, writing
\(x_A=\tan(A/2)\),
\[
                  2\log(1+x_A^2)<\delta/8.
 \tag{8}
\]
For \(0\le a\le A\), equation (5) gives
\(\Re\Xi(a-iK_g)\le M_g-\delta\).
The incoming-color theorem proves the full relative asymptotic
for \(Q_N(w,u)\) on a fixed incoming disk times the positive
lower rectangle. Its phase \(S(w,u)\) is continuous on that
compact product and equals \(S_0(u)\) at \(w=-2\).
Consequently one may choose a fixed smaller disk such that
\[
 \left|\Re\{S(w,a-iK_g)-S_0(a-iK_g)\}\right|<\delta/8
 \quad(0\le a\le A).
 \tag{9}
\]
The same theorem bounds its amplitude and relative error
uniformly there. Its two full kernels therefore give
\[
 |F_N(a-iK_g)|
 \le C N^{-3}
       \exp N\{M_g-3\delta/4+K_g\},
 \qquad 0\le a\le A.
 \tag{10}
\]
Indeed the real part of the crossing and unit-charge term is
\(2aK_g/\pi-K_g\). In solving for the exponent of \(F_N\),
we have only dropped the nonpositive term \(-2aK_g/\pi\).
No sign assumption on \(F_N\) is used.

## 3. Polynomial continuation to the negative interval

For real \(a\), put \(x=\tan(a/2)\). The exact outgoing
coordinate on the fixed horizontal line is
\[
 z=-2\cos(a-iK_g)
   =-2\frac{\cosh K_g(1-x^2)+2i\sinh K_g\,x}{1+x^2}
   =:\zeta(x).
 \tag{11}
\]
It follows that
\[
 P_N(x)=(1+x^2)^{2D}F_N^\sharp(\zeta(x))
 \tag{12}
\]
is an ordinary polynomial of degree at most \(4D<4N\).
Every coefficient still depends on the actual incoming colors.
The degree assertion and all estimates below are uniform for
those colors in the fixed disk.

Equation (10) implies
\[
 \sup_{0\le x\le x_A}|P_N(x)|
 \le C N^{-3}e^{N(M_g-3\delta/4+K_g)}
                          (1+x_A^2)^{2D}.
 \tag{13}
\]
Map this interval to \([-1,1]\) by
\(\xi=2x/x_A-1\). If \(x_\eta=\tan(\eta/2)\), then the
interval \(-x_\eta\le x\le0\) maps into
\([-1-2x_\eta/x_A,-1]\). Set
\[
 \rho_\eta=\operatorname{arcosh}(1+2x_\eta/x_A).
 \tag{14}
\]
Expanding the polynomial in Chebyshev polynomials gives
\[
 \sup_{-x_\eta\le x\le0}|P_N(x)|
 \le 2(4D+1)e^{4D\rho_\eta}
                       \sup_{0\le x\le x_A}|P_N(x)|.
 \tag{15}
\]
For completeness, each Chebyshev coefficient is bounded by
twice the interval supremum, by the cosine integral formula.
On the extended real interval,
\(|T_j(\xi)|\le e^{j\rho_\eta}\). Summing its at most
\(4D+1\) terms proves (15), for complex as well as real
coefficients.

Now choose \(0<\eta<A\) so small that
\[
                          4\rho_\eta<\delta/8.
 \tag{16}
\]
This is possible because \(A\) has already been fixed and
\(\rho_\eta\to0\) as \(\eta\to0\). Dividing (15) by the
clearing factor in (12), which is at least one on the real
interval, and using (8),(13),(16), yields
\[
 |F_N(a-iK_g)|
 \le C N^B
      e^{N(M_g-\delta/2+K_g)},
 \qquad -\eta\le a\le0.
 \tag{17}
\]
This continuation is applied to an exact polynomial on a whole
real interval. It does not continue an error estimate from a
single point or assume a relative asymptotic on the new interval.

## 4. Restoring the outer trace factors

On the fixed horizontal line,
\[
 |W_N(a-iK_g)|
 \le \frac{e^{-NK_g}}{(1-e^{-NK_g})^2}
 \le C e^{-NK_g}.
 \tag{18}
\]
For \(-\eta\le a\le0\), the crossing factor has modulus
\[
             |e^{iN(a-iK_g)^2/\pi}|
                        =e^{2NaK_g/\pi}\le1.
 \tag{19}
\]
Also \(|\sin(a-iK_g)|\) is bounded. Thus (17)--(19)
give rate at most \(M_g-\delta/2\) on the negative interval.
On \(0\le a\le A\), use the original asymptotic and (5),(9)
directly: retaining the crossing factor gives the stronger
rate \(M_g-3\delta/4\).
After the fixed integration length and the original
\(N^2/\pi\) prefactor, polynomial factors can be absorbed
in \(\delta/4\). This proves (6) with
\(\epsilon=\delta/4\).

The estimate includes the complete rational sampling kernel,
so all its Fourier charges remain present. Nothing has been
changed in the underlying Hermite trace or in its odd-level
central sample. The bound concerns a fixed interval on the
deformed contour; the rest of the negative horizontal, the
far connections, and the full closing remainder still require
their own estimates.

## Source versions

- Exact ordinary closing polynomial and contour:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Complete incoming-color neighborhood:
  fedd23ea3d5d8aea8132af828f358bb0b0884e1e599a5dc31f457b33dd261aae.
- Actual geometric point inside the larger rectangle:
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
- Original closing phase and positive-horizontal curvature:
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.

The polynomial continuation follows the argument in
[the earlier inner-contour bridge](research_mixed_next_inner_three_center_bridge.md),
with the new exact degree \(2D\) of the outer product.
No mathematical numerical evaluation is used.
