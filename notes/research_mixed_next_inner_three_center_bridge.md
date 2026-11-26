# A finite polynomial bound across the center of the inner contour

Private source proof, 8 November 2026. Polynomial continuation from
a short positive angular interval controls a fixed interval across
the imaginary axis. This estimates the actual two-edge source
without assuming a kernel asymptotic at a wire saddle on the real
sampling line. No mathematical numerical evaluation or frozen-source
edit is used.

## 1. The original source and the interval to be estimated

Keep the complete and shortened edges
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{\lfloor N/2\rfloor-1}
                      e_j(-2\cos t)e_j(-2\cos u),
\]
with the original Newton polynomials and normalization. Put
\[
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\qquad
 d_N=N-1+\lfloor N/2\rfloor-1<3N/2.
 \tag{1}
\]
Thus \(f_N(t,u)=F_N(-2\cos t,u)\), where \(F_N\) is a polynomial
of degree at most \(d_N\) in its first variable. The complete
first edge and every retained second-edge row remain present.

For
\[
 \mathcal U_+=\{b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
\]
write the original cubic point as
\[
 t_*(u)=a_*(u)-iH(u),\qquad
 0<a_*(u)<\pi/2,\quad 1/2<H(u)<1.
 \tag{2}
\]
Let \(s(u)=\Re S_3(0,u)\). The complete inner trace uses
\[
 \widetilde g_N(t,u)
      =\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},
 \quad \eta_N=(-1)^{N-1}.
 \tag{3}
\]
These are the exact factors of
[the inner boundary theorem](research_mixed_next_inner_three_far_samples_and_verticals.md).

**Theorem.** There are fixed \(\eta>0\) and \(\epsilon_c>0\) such
that, uniformly for \(u\in\mathcal U_+\) and both level parities,
\[
 \sup_{-\eta\le a\le\eta}
 |\widetilde g_N(a-iH(u),u)W_N(a-iH(u))|
       \le C e^{N(s(u)-\epsilon_c)}.
 \tag{4}
\]
The same exponential gap bounds the absolute integral along this
entire horizontal interval, including the original trace prefactor
\(N^2/\pi\), after increasing the sufficiently large level threshold.
The interval stays strictly below the real axis. No physical
central sample or pole is removed.

## 2. A positive interval with a known finite-source gap

Put
\[
 a_0=\min_{\mathcal U_+}a_*(u)>0,\qquad
 \epsilon_0=\frac{a_0^2}{32\pi}>0.
 \tag{5}
\]
Choose a fixed \(A\) with \(0<A<a_0/2\), small enough that
\[
             \frac32\log(1+\tan^2(A/2))<\epsilon_0/8 .
 \tag{6}
\]
This choice is possible by continuity at zero. We will then choose
\(0<\eta<A\) sufficiently small. All choices are fixed before
letting \(N\) tend to infinity.

The [positive-horizontal source theorem](research_mixed_next_shortened_edge_positive_horizontal_packet.md),
equation (45), gives on \(\eta\le a\le A\)
\[
 |f_N(a-iH(u),u)|
 \le C N^B
   e^{N\Re\{\psi(a-iH(u),0)+\psi(a-iH(u),u)\}} .
 \tag{7}
\]
The constants may depend on the fixed \(\eta,A\), but are uniform
in \(u,N\). This input includes the full first edge through its
existing complete-edge bound.

By the [horizontal concavity theorem](research_mixed_next_inner_three_horizontal_concavity.md),
the unchanged inner phase satisfies
\[
 \Re\Phi(a-iH(u),u)
 \le s(u)-\frac{(a-a_*(u))^2}{8\pi}
 \le s(u)-\epsilon_0,\qquad \eta\le a\le A.
 \tag{8}
\]
The real contribution of its crossing and trace charge is
\[
 \Re\left\{\frac{3i(a-iH)^2}{4\pi}-i(a-iH)\right\}
                         =\frac{3aH}{2\pi}-H.
\]
Consequently (7)--(8) imply the convenient uniform bound
\[
 |f_N(a-iH(u),u)|
       \le C N^B e^{N\{s(u)-\epsilon_0+H(u)\}},
                      \qquad \eta\le a\le A .
 \tag{9}
\]
The favorable term \(-3aH/(2\pi)\) has only been omitted from
this upper bound.

## 3. Exact polynomial continuation through the imaginary axis

For fixed \(u\), put \(H=H(u)\) and \(x=\tan(a/2)\). The exact
spectral coordinate is
\[
 -2\cos(a-iH)
   =-2\,\frac{\cosh H(1-x^2)+2i\sinh H\,x}{1+x^2}
   =:\zeta_H(x).
 \tag{10}
\]
Hence
\[
 P_N(x;u)=(1+x^2)^{d_N}F_N(\zeta_H(x),u)
 \tag{11}
\]
is an ordinary polynomial of degree at most \(2d_N<3N\).
This is an exact identity; no Taylor truncation is used.

Write \(x_\eta=\tan(\eta/2)\), \(x_A=\tan(A/2)\).
Equation (9) yields
\[
 \sup_{x_\eta\le x\le x_A}|P_N(x;u)|
 \le C N^B e^{N\{s(u)-\epsilon_0+H(u)\}}
                         (1+x_A^2)^{d_N}.
 \tag{12}
\]
Map this fixed real interval affinely to \([-1,1]\):
\[
              \xi=\frac{2x-x_A-x_\eta}{x_A-x_\eta}.
 \tag{13}
\]
For \(-x_\eta\le x\le x_\eta\), one has
\[
      -1-\frac{4x_\eta}{x_A-x_\eta}\le\xi\le-1.
 \tag{14}
\]
Define
\[
 \rho_\eta=\operatorname{arcosh}
              \left(1+\frac{4x_\eta}{x_A-x_\eta}\right).
 \tag{15}
\]
Expand the polynomial in (11), after (13), in Chebyshev
polynomials. Each coefficient is bounded in modulus by twice
the supremum in (12), by its cosine integral formula; this
holds for complex coefficients as well. On (14),
\[
                 |T_j(\xi)|\le e^{j\rho_\eta}.
 \tag{16}
\]
There are at most \(2d_N+1\) coefficients. Equations
(12)--(16), and \(1+x^2\ge1\) on the real interval, therefore
give
\[
 \sup_{-\eta\le a\le\eta}|f_N(a-iH(u),u)|
 \le C N^{B+1}
 \exp N\left\{s(u)-\epsilon_0+H(u)
       +\frac32\log(1+x_A^2)+3\rho_\eta\right\}.
 \tag{17}
\]
The degree bounds in (1) are the only finite-dimensional input
to this continuation. In particular it makes no assumption about
the signs of the original quantum coefficients.

## 4. Restoring the exact trace factors

For the fixed \(A\) in (6), \(\rho_\eta\) tends to zero as
\(\eta\) tends to zero. Choose \(0<\eta<A\) so small that
\[
                 3\rho_\eta<\epsilon_0/8,\qquad
                 \frac{3\eta}{2\pi}<\epsilon_0/8 .
 \tag{18}
\]
The independent complex source theorem used in (7) applies for
this fixed positive \(\eta\); no estimate uniform as
\(\eta\to0\) has been invoked.

On the entire interval to be bounded, \(H(u)>1/2\), and
\[
 |W_N(a-iH)|
     \le\frac{e^{-NH}}{(1-e^{-NH})^2}\le C e^{-NH}.
 \tag{19}
\]
This retains every angular Fourier charge in the original
double-pole kernel. Also
\[
 |\sin(a-iH)|\le\cosh1,\qquad
 \left|e^{3iN(a-iH)^2/(4\pi)}\right|
       =e^{3NaH/(2\pi)}
       \le e^{3N\eta/(2\pi)}.
 \tag{20}
\]
Combining (6), (17)--(20) cancels the \(NH\) term exactly and
gives
\[
 |\widetilde g_N(a-iH(u),u)W_N(a-iH(u))|
 \le C N^{B+1} e^{N\{s(u)-5\epsilon_0/8\}} .
 \tag{21}
\]
Multiplication by \(N^2/\pi\), integration over length \(2\eta\),
and absorption of the polynomial factors leave the fixed gap
\(\epsilon_c=\epsilon_0/2\) for all sufficiently large levels.
This proves the theorem, including both parities and the
corresponding absolute integral estimate.

The estimate concerns part of the original lower angular contour.
Its nonzero depth avoids every real pole. It neither removes the
odd central physical contribution nor replaces the full Hermite
trace by a sum over distinct values. The rest of the negative
horizontal and the far connecting contours still need their own
finite-source estimates.
