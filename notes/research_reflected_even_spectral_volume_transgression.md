# The real-parameter transgression of the reflected even spectral rate

Research note, 3 November 2026.

The sharp reflected-even source rate has an exact real-parameter
variation and a fixed absolute anchor. After multiplication by
\(2\pi\), its continuation to real \(k\ge2\) has derivative
\(4\eta_k\varphi_k\) and tends to \(8G\), where \(G\) is Catalan's
constant. The continuation is a classical holomorphic integral;
no matrix of noninteger dimension or noninteger quantum crossing
power is introduced.

This proves the analytic action identity and its normalization.
The [reflected even knot theorem](research_reflected_even_kashaev_volume_theorem.md)
combines it with the original geometric period calculation to
identify the rate with the volume of the marked knot complement.

## 1. A real-parameter critical point and its logarithms

For every real \(k\ge2\), let \(a_k=\eta_k-i\varphi_k\) be the
unique solution with
\[
 \eta_k>0,\qquad
 \frac{2\pi}{2k+1}<\varphi_k<\frac{\pi}{k}
 \tag{1}
\]
of
\[
 \begin{split}
 F_k(\eta,\varphi)
   &=\cosh(2k\eta)-\cos(2k\varphi)-\cosh\eta+\cos\varphi=0,\\
 B_k(\eta,\varphi)
   &=\sinh(2k\eta)\sinh\eta
                     +\sin(2k\varphi)\sin\varphi=0.
 \end{split}                                                    \tag{2}
\]
The uniqueness proof in Lemma 2 of
[the sharp reflected-growth theorem](research_even_run_sharp_reflected_growth.md)
works for every real \(k\ge2\): none of its inequalities uses
integrality. In detail, \(F_k=0\) defines a strictly increasing
positive function \(\eta_c(\varphi)\) on the interval (1).
Along it, \(B_k\) strictly increases from a negative value to a
positive one. Moreover
\[
 (F_k)_\eta>0,\qquad
 \frac{d}{d\varphi}B_k(\eta_c(\varphi),\varphi)>0.
 \tag{3}
\]
The Jacobian in \((\eta,\varphi)\) is therefore nonzero.
The critical point depends real analytically on \(k\), with
the one-sided interpretation at \(k=2\).

Use the simply connected strip
\[
 \mathscr S_k=
   \{a:\operatorname{Re}a>0,\ -\pi/k<\operatorname{Im}a<-\pi/(2k)\},
 \qquad a_0(k)=-i\pi/k.
 \tag{4}
\]
On this strip define
\[
 X_k(a)=-\frac{\sinh((k+\tfrac12)a)}
                  {\sinh((k-\tfrac12)a)},\qquad
 L_k(a)=-\left(\frac{\sinh(a/2)}{\sinh(ka)}\right)^2,
 \qquad u=\log X_k,\quad v=\log L_k .
 \tag{5}
\]
Every displayed hyperbolic sine is nonzero there, since its
argument has positive real part. Thus both logarithms exist
holomorphically on the entire strip. Choose the branches by their
boundary expansions at \(a_0\). With \(\delta=a-a_0\), these are
\[
 \begin{split}
 u(k,a)&=2ik\cot\!\left(\frac{\pi}{2k}\right)\delta+O_k(\delta^2),\\
 v(k,a)&=-2\log\delta+
           \log\!\left(\frac{\sin^2(\pi/(2k))}{k^2}\right)
                                                    +O_k(\delta).
 \end{split}                                                    \tag{6}
\]
Here \(\log\delta\) is the branch with argument between zero
and \(\pi/2\) in the local part of the strip. The constant in
the second line is real. The branches are smooth in \(k\) on
compact real intervals: scaling \(b=ka\) identifies the strips
with one fixed simply connected strip, and the nonzero factors
in (5) have joint continuous logarithms with normalization (6).

The equations (2) say exactly
\[
                   |X_k(a_k)|=|L_k(a_k)|=1.
 \tag{7}
\]
In particular \(u(k,a_k)\) and \(v(k,a_k)\) are purely
imaginary, with the chosen full logarithms, not only modulo
\(2\pi i\).

## 2. The action and its endpoint-safe variation

Define the spectral action
\[
            \mathcal V(k)
             =2\,\operatorname{Im}
                   \int_{a_0(k)}^{a_k}v(k,a)\,u_a(k,a)\,da .
 \tag{8}
\]
The integral can use any path in \(\mathscr S_k\) approaching
the lower endpoint. It converges by (6), and is path independent:
the integrand is a holomorphic one-form on a simply connected
domain, and its primitive extends continuously to \(a_0\).
For example, the straight segment from \(a_0\) to \(a_k\),
with its endpoint omitted, lies in the strip.

Changing \(v\) by a constant multiple of \(2\pi i\) changes
the integral by \(2\pi i\) times the purely imaginary endpoint
difference of \(u\); this changes only its real part. The
normalization in (6) is nevertheless retained for all derivative
calculations.

**Theorem 1.** The action (8) is continuously differentiable for
real \(k\ge2\), and
\[
                    \boxed{\quad
                    \mathcal V'(k)=4\eta_k\varphi_k .
                    \quad}
 \tag{9}
\]

*Proof.* All partial derivatives below hold \(a\) fixed.
Put \(A=(k+\tfrac12)a\), \(B=(k-\tfrac12)a\), and \(K=ka\).
Direct differentiation gives
\[
 \begin{split}
 u_k&=a(\coth A-\coth B),&
 u_a&=(k+\tfrac12)\coth A-(k-\tfrac12)\coth B,\\
 v_k&=-2a\coth K,&
 v_a&=\coth(a/2)-2k\coth K .
 \end{split}                                                    \tag{10}
\]
The addition identities for \(\coth(K\pm a/2)\) imply
\[
 \begin{split}
 &[\coth K+\coth(a/2)]\coth(K+a/2)\\
 &\qquad+[\coth K-\coth(a/2)]\coth(K-a/2)=2.
 \end{split}
\]
Substitution in (10) proves the exact identity
\[
                  v_k u_a-v_a u_k=-2a .
 \tag{11}
\]

To retain the moving singular endpoint, set
\[
 a_\varepsilon(k)=a_0(k)+\varepsilon[a_k-a_0(k)],
 \qquad
 I_\varepsilon(k)=\int_{a_\varepsilon(k)}^{a_k}v\,du ,
                        \qquad 0<\varepsilon<1.
 \tag{12}
\]
The cutoff stays in the strip. Differentiating this nonsingular
integral and integrating the \(v\,u_{ak}\) term by parts gives
\[
 \frac{d I_\varepsilon}{dk}
  =v(k,a_k)\frac{d}{dk}u(k,a_k)
   -v(k,a_\varepsilon)\frac{d}{dk}u(k,a_\varepsilon)
   -a_k^2+a_\varepsilon^2 .
 \tag{13}
\]
The derivatives of \(u\) here are total endpoint derivatives.
The first product is real by (7). On any compact interval of
real \(k\)'s, (6) gives uniformly
\[
 v(k,a_\varepsilon)=O(1+|\log\varepsilon|),\qquad
 \frac{d}{dk}u(k,a_\varepsilon)=O(\varepsilon).
 \tag{14}
\]
The second estimate uses the exact cancellation
\(u_k(k,a_0)+u_a(k,a_0)a_0'(k)=0\), since
\(u(k,a_0(k))=0\). It is incorrect to replace the total
lower-end derivative in (13) by either partial term separately.
Equivalently, the singular terms
\(v_k=2a_0'/\delta+O(1)\) and
\(v_a a_0'=-2a_0'/\delta+O(1)\) cancel in a shifted
\(\delta\)-coordinate.

The imaginary parts of (13) consequently converge uniformly
on compact \(k\)-intervals. The integrals themselves converge
uniformly, with error \(O(\varepsilon|\log\varepsilon|)\).
Integrating their derivatives on a compact \(k\)-interval
therefore justifies differentiation of the limit in (8).
Since \(a_0^2=-\pi^2/k^2\) is real, the result is
\[
 \mathcal V'(k)
     =2\,\operatorname{Im}(-a_k^2+a_0^2)
     =4\eta_k\varphi_k .
 \tag{15}
\]
\(\square\)

Integration by parts also gives the useful, endpoint-regular
formula
\[
       \mathcal V(k)=-2\,\operatorname{Im}
                      \int_{a_0(k)}^{a_k}u(k,a)v_a(k,a)\,da .
 \tag{16}
\]
Indeed the lower product \(uv\) tends to zero by (6), while
the upper product is real by (7). The product \(uv_a\)
has a removable limit at \(a_0\).

## 3. The absolute anchor at large real \(k\)

**Theorem 2.** With
\[
          G=\int_0^1\frac{\arctan t}{t}\,dt
             =\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^2},
 \tag{17}
\]
one has
\[
 \boxed{\quad
       \lim_{k\to\infty}\mathcal V(k)=8G,\qquad
       \mathcal V(k)=8G-4\int_k^\infty
                                \eta_s\varphi_s\,ds .
 \quad}                                                        \tag{18}
\]
In particular \(\mathcal V\) strictly increases, and
\[
                 \mathcal V(k)
                      =8G-\frac{\pi^2}{k^2}+O(k^{-4}).
 \tag{19}
\]

*Proof.* First obtain quantitative control of the critical
endpoint, entirely from (2). The first equation gives
\[
 \frac{(4k^2-1)\eta_k^2}{2}
 \le \cosh(2k\eta_k)-\cosh\eta_k
 =\cos(2k\varphi_k)-\cos\varphi_k
 \le\frac{\varphi_k^2}{2}.
 \tag{20}
\]
The first inequality follows coefficientwise from the hyperbolic
cosine series. Therefore \(\eta_k=O(k^{-2})\).
Put \(\delta_k=\pi-k\varphi_k\). From (1),
\(0<\delta_k<\pi/(2k+1)\), and the second equation in (2) is
\[
          \sin(2\delta_k)\sin\varphi_k
                 =\sinh(2k\eta_k)\sinh\eta_k=O(k^{-3}).
 \tag{21}
\]
Here \(\sin\varphi_k\) is bounded below by a positive constant
times \(k^{-1}\), and
\(\sin(2\delta_k)\ge4\delta_k/\pi\).
Thus \(\delta_k=O(k^{-2})\). Expanding the first equation
in (2) now yields
\[
 \eta_k=\frac{\pi}{2k^2}+O(k^{-4}),\qquad
 \varphi_k=\frac{\pi}{k}+O(k^{-3}).
 \tag{22}
\]
For example,
\(\cosh(2k\eta)-\cosh\eta=2k^2\eta^2+O(k^{-4})\)
and
\(\cos(2\delta)-\cos\varphi=\pi^2/(2k^2)+O(k^{-4})\),
which give the first assertion in (22) with its indicated error.

Use the scaled coordinate
\[
       \xi=\frac{2k^2}{\pi}\left(a+\frac{i\pi}{k}\right),
       \qquad \xi_k=\frac{2k^2}{\pi}
                              \left(a_k+\frac{i\pi}{k}\right).
 \tag{23}
\]
Equation (22) shows
\(\operatorname{Re}\xi_k=1+O(k^{-2})\) and
\(\operatorname{Im}\xi_k=O(k^{-1})\).
The straight segment from \(0\) to \(\xi_k\) is the
admissible path already used in (12).

Put \(t_k=\pi/(2k)\). In this coordinate, the functions (5)
have the explicit forms
\[
 \begin{split}
 X_k(\xi)
  &=-\frac{\sinh(t_k[(1+(2k)^{-1})\xi-i])}
           {\sinh(t_k[(1-(2k)^{-1})\xi+i])},\\
 \xi^2 L_k(\xi)
  &=-\left[
       \frac{\sinh(t_k[-i+\xi/(2k)])}{t_k}
      \right]^2
        \left[\frac{t_k\xi}{\sinh(t_k\xi)}\right]^2 .
 \end{split}                                                    \tag{24}
\]
Both expressions are holomorphic and nonzero on a fixed open
neighborhood of the segment \([0,1]\), for all sufficiently
large \(k\); the apparent singularity at \(\xi=0\) in the
second expression is removed. Uniformly on a slightly larger
such neighborhood,
\[
        X_k(\xi)\longrightarrow
             X_\infty(\xi)=\frac{1+i\xi}{1-i\xi},\qquad
        \xi^2L_k(\xi)\longrightarrow1 .
 \tag{25}
\]
These claims follow directly from (24): the limiting zeros
and poles of \(X_k\) are at \(i,-i\), away from the segment,
and the second limit is nonzero. One may use, for example,
a sufficiently small fixed tubular neighborhood of \([0,1]\).

Choose logarithms there with \(u_k(0)=0\) and
\(\log[\xi^2L_k(\xi)]|_{\xi=0}\) real.
They agree with (6) on the original segment.
Writing \(l_k(\xi)=\xi^2L_k(\xi)\), the integrand in (16) is
\[
       u_k(\xi)\left[\frac{l_k'(\xi)}{l_k(\xi)}
                                      -\frac2{\xi}\right].
 \tag{26}
\]
It extends holomorphically through zero because \(u_k(0)=0\).
The uniform holomorphic limits (25), and Cauchy's formula on
the larger neighborhood, show that (26) converges uniformly to
\(-2\log X_\infty(\xi)/\xi\), with its removable value at zero.
This proves the needed domination at the moving singular
endpoint, rather than discarding that endpoint after a formal
pointwise limit.

As \(\xi_k\to1\), formula (16) consequently gives
\[
 \begin{split}
 \lim_{k\to\infty}\mathcal V(k)
   &=4\,\operatorname{Im}
            \int_0^1\frac{\log X_\infty(\xi)}{\xi}\,d\xi\\
   &=8\int_0^1\frac{\arctan\xi}{\xi}\,d\xi=8G.
 \end{split}                                                    \tag{27}
\]
Here \(\log X_\infty(\xi)=2i\arctan\xi\) on the real segment,
with the branch zero at the origin.

Finally (22) gives
\(\eta_k\varphi_k=\pi^2/(2k^3)+O(k^{-5})\).
It is integrable at infinity. Integrating Theorem 1 from
\(k\) to infinity proves (18), its strict increase, and
the more precise expansion (19). \(\square\)

## 4. Relation to the proved original quantum rate

At an integer \(k\ge2\), take the conjugate-coordinate
parametrization of the actual top spectral branch from the
sharp reflected-growth theorem. Its parameter
\(a(\theta)\) lies in \(\mathscr S_k\), starts at \(a_0\),
and ends at the unique point (2). Because the original backward
matrix uses \(e^{-i\theta}\) while (5) uses \(X=e^{i\theta}\),
the precise normalized eigenvalue identity is
\(L_k(a(\theta))=\overline{\lambda_*(\theta)}/(2-2\cos\theta)\),
while
\(X_k(a(\theta))=e^{i\theta}\).
The logarithm normalized in (6) therefore gives
\(u=i\theta\) along that path. Consequently
\[
 \begin{split}
 \mathcal V(k)
   &=2\int_0^{\theta_k}
       \log\left|
          \frac{\lambda_*(\theta)}{2-2\cos\theta}
           \right|\,d\theta\\
   &=4\pi B_k(x_k)
    =\lim_{N\to\infty}\frac{2\pi}{N}
          \log\phi_N(R^{-2k}T(R^{2k})) .
 \end{split}                                                    \tag{28}
\]
Here \(B_k(x_k)\) is the spectral action defined in (25) of
the cited sharp-growth note; it is not the second function
in the critical equations (2).
The first integral converges at zero, as already proved in (6).
The last equality uses the original endpoint mode,
normalization, low-color estimate, and middle-color contraction
in that theorem. It is not inferred from the classical
transgression alone.

All asymptotic statements in the last equality hold with the
integer crossing power fixed before \(N\to\infty\). The
separate limit \(k\to\infty\) in Theorem 2 calibrates the
classical action; it asserts no uniform quantum error estimate
over increasing crossing powers.

## 5. Supplemental finite checks

The focused
[period checker](../experiments/check_even_reflected_volume_period.py)
evaluates the regularized integral (16) on both a straight and
a bent path. It also checks the exact transgression (11), the
original primitive returns, the eight positive cell shapes,
and their Bloch--Wigner volume against the spectral period.
At integer ranks it compares the same point with the original
classical Jacobi characteristic equation.

The [100-digit record](../repro/results/research-even-reflected-volume-period-root.json)
and [140-digit record](../repro/results/research-even-reflected-volume-period-review.json)
each passed the eight fixed values
\(k=2,\,2.5,\,3,\,4,\,7.25,\,10,\,20,\,50\).
Their largest relative identity residuals were respectively
\(6.052\cdot10^{-98}\) and \(1.7242\cdot10^{-137}\).
The noninteger values test the classical action continuation,
not a manifold or quantum crossing assignment. These finite
checks supplement the written endpoint and large-\(k\) arguments;
they do not certify an asymptotic limit.
