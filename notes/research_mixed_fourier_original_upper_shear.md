# Decay along a coupled displacement of the original contour

Research deduction, 7 November 2026. The opposite displacement of
the two imaginary coordinates also decreases the original upper
Fourier phase when the sum of their real parts exceeds one. The
reason is an elementary monotonicity in the retained real index.
The two coordinates can therefore move with their total imaginary
part fixed and negative, without introducing the diagonal poles
of the shifted interpolation.

This note proves a phase estimate and its consequence on bounded
contours. It does not bound a connecting integral whose initial
phase is uncontrolled. Uniform estimates at infinite height and
the complete contour identity are separate requirements.

## 1. The original integrand and the displacement

Keep the original incoming parameter and output of
[the diagonal shear estimate](research_mixed_fourier_diagonal_shear_monotonicity.md):
\[
 a=x+i h_a,\qquad 11/50\le x\le9/20,\qquad
 |h_a|\le.108,\qquad e^{-2\pi h_a}<2,
\]
\[
 y=\xi+i\upsilon,\qquad Y=e^{2\pi iy}=\rho e^{i\phi},
 \qquad 0<\rho<5/8,\qquad \phi=2\pi\xi<7/6.
 \tag{1}
\]
The actual output also has \(0<\xi<.184\).
Let
\[
 \frac18\le u\le\frac12,\qquad \frac9{20}\le z\le1,
 \qquad h>0,\qquad H\ge0,
 \qquad s=u+iH,\qquad q=z-i(H+h).
 \tag{2}
\]
In particular \(\Im(s+q)=-h<0\). There is no restriction
on \(u+z\). Define the allocated original phase by
\[
 F_\eta(s,a,q)=g(s+a)+g_-(s+q)-3g(s)
       -(1+\eta/2)g(a)-g_-(q)+2\pi ias+\ell_q(y),
 \tag{3}
\]
where \(g\) is the original regular-strip primitive and
\[
 g_-(w)=\frac{\operatorname{Li}_2(e^{-2\pi iw})-\pi^2/6}
                       {2\pi i}\qquad(\Im w<0),
\]
\[
 \ell_q(y)=2\pi iy(q-1/2)
       -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})-
                    \operatorname{Li}_2(Y)}{2\pi i}.
 \tag{4}
\]
The disk series specify the latter branches. They agree with the
original source on their common domain. The arguments \(s\) and
\(s+a\) stay in their original real strips, while \(q\) and
\(s+q\) stay strictly below the real axis.

**Theorem 1.** Throughout (1)--(2),
\[
 \frac{d}{dH}\bigl\{\Re F_\eta(u+iH,a,z-i(H+h))-2\pi H\bigr\}
                                                    <-\frac1{20}.
 \tag{5}
\]
The bound is independent of \(h>0\), \(z\) in its full interval,
and the incoming allocation \(\eta\).

## 2. Removing the support restriction

Use
\[
 A_R(t)=\arg(1-Re^{-2\pi it}),\qquad
 r=e^{-2\pi H},\qquad \theta=e^{-2\pi h}\in(0,1).
 \tag{6}
\]
For the regular-strip arguments use the continuous principal
determination already fixed in the diagonal shear estimate.
The disk arguments at \(q\) and \(q-y\) have no branch ambiguity.
The cancellation of the shared \(g_-'(s+q)\) terms gives
\[
 \begin{split}
 P&:=2\pi+\Im(F_{\eta,s}-F_{\eta,q})\\
  &=4\pi u-\phi+3A_r(u)-A_{r e^{-2\pi h_a}}(u+x)
                   +A_{r\theta}(z)+A_{\rho r\theta}(z-\xi).
 \end{split}
 \tag{7}
\]
The derivative in (5) is \(-P\). Equation (7) remains valid
across \(u+z=1\): the shared term is evaluated below the real
axis, and is canceled before any estimate.

The crucial monotonicity is
\[
 \frac d{du}\{4\pi u+3A_r(u)\}
 =\frac{2\pi(2-r\cos(2\pi u)-r^2)}
                  {1-2r\cos(2\pi u)+r^2}>0
       \qquad(1/8\le u\le1/2).
 \tag{8}
\]
For \(r<1\), the numerator is at least
\((1-r)(2+r)>0\); for \(r=1\), it is
\(1-\cos(2\pi u)>0\). Therefore
\[
 4\pi u+3A_r(u)\ge\frac\pi2+3b(r),\qquad
 b(r)=\arctan\frac{r}{\sqrt2-r}.
 \tag{9}
\]
The incident-argument estimate from equation (17) of the
diagonal shear note holds on this whole retained interval:
\[
 A_{r e^{-2\pi h_a}}(u+x)\le\arctan t_r,
                  \qquad t_r=\frac{5r}{3(1+r)}.
 \tag{10}
\]
Indeed it is nonpositive for \(u+x\ge1/2\). Otherwise
\(u+x\ge.345\), and the same radius and trigonometric bounds
apply. Finally the two disk arguments satisfy
\[
 A_{r\theta}(z)\ge-\arcsin r,
             \qquad A_{\rho r\theta}(z-\xi)>-7r/10.
 \tag{11}
\]
The second bound uses \(\arcsin(\rho r\theta)
\le r\arcsin\rho<7r/10\). Since \(\pi/2-\phi>1/3\),
equations (7)--(11) imply
\[
 P>\frac13+3b(r)-\arctan t_r-\arcsin r-\frac7{10}r.
 \tag{12}
\]

## 3. A uniform positive margin

For \(0<r\le1/\sqrt2\), put
\[
 m(r)=\min\{\arctan r,b(r)\}.
\]
One has \(b(r)\ge m(r)\). Lemma 2 and equations (18)--(21)
of the diagonal shear note therefore apply directly to (12).
For clarity, the two resulting lower bounds are
\[
 \begin{array}{ll}
 0<r\le1/2:
 &P>1/3+7r/20+9r^2/20-t_r>1/20,\\[2pt]
 1/2\le r\le1/\sqrt2:
 &P>1/3+4r/5-r^3/2-t_r+t_r^3/5>1/20.
 \end{array}
 \tag{13}
\]
Their proofs are the exact positive polynomial comparisons in
that note; no index-support inequality occurs in them.

Suppose next \(1/\sqrt2\le r\le9/10\). The function \(b\)
increases, and \(b(1/\sqrt2)=\pi/4\). Also
\(\sin(3\pi/8)>9/10\), so
\[
              3b(r)-\arcsin r>3\pi/8.
 \tag{14}
\]
For the sine inequality, square the positive terms and use
\(\sin^2(3\pi/8)=(2+\sqrt2)/4>(2+7/5)/4=17/20>81/100\).
Equation (10) gives \(\arctan t_r<3/4\), since
\(t_r\le5/6<\tan(3/4)\). Thus
\[
 P>1/3+3\pi/8-3/4-7/10>1/20,
 \tag{15}
\]
where the last inequality follows from \(\pi>28/9\).

Finally let \(9/10\le r\le1\). The rational upper bound
\(\sqrt2<99/70\) gives
\[
 \frac{r}{\sqrt2-r}\ge\frac{9/10}{\sqrt2-9/10}
                  >\frac74>\sqrt3.
\]
Consequently \(b(r)>\pi/3\), and
\(3b(r)-\arcsin r>\pi/2\). Equation (12) now gives the
stronger bound
\[
                     P>1/3+\pi/2-3/4-7/10>1/20.
 \tag{16}
\]
This proves Theorem 1.

## 4. Consequence for the original upper Fourier kernel

Let \(T_N(s,q)\) be the original row, equation (2) of
[the interpolation identity](research_mixed_fourier_right_cap_shifted_current_identity.md).
Its upper Fourier kernel is
\[
 k_N^+(s)=\frac{e^{2\pi iNs}}{1-e^{2\pi iNs}}.
 \tag{17}
\]
For every fixed \(H_0>0\) and \(H\ge H_0\),
\[
 |k_N^+(u+iH)|\le
              \frac{e^{-2\pi NH}}{1-e^{-2\pi NH_0}}.
 \tag{18}
\]
On any fixed compact height interval, with \(h\) in a compact
subset of \((0,\infty)\), the original factorial estimates
therefore transfer (5) to an upper bound for
\(T_N(s,q)k_N^+(s)\), including the incoming weight.
For every fixed rate tolerance \(\epsilon>0\), its bound has
the form
\[
 C_\epsilon N^{A_\epsilon}
 \exp\left[N\left(
  \Re F_\eta(u+iH_0,a,z-i(H_0+h))-2\pi H_0
       -\frac{H-H_0}{20}+\epsilon\right)\right].
 \tag{19}
\]
The constants are uniform on those compact families. The
\(O(1/N)\) retained half-grid displacements cost a bounded
factor on such a compact set.

The use of the original row is important. Its shared numerator
\(\Pi_N(s+q)\) remains below the real axis for the entire
displacement; it acquires no diagonal poles. The upper kernel
also has no pole at \(H\ge H_0>0\). The sides of the moving
two-dimensional contour still produce connecting integrals.
Neither their initial rates nor uniform infinite-height bounds
follow from (19). Those are required before this phase theorem
can give a bound for the complete right-hand correction.
