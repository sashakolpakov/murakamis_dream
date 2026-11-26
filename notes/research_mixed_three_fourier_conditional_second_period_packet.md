# The complete second conditional period has a nonzero vertical packet

Research deduction, 7 November 2026. The explicit second homogeneous
period of the twice-crossed source admits a pole-free original factorial
chart on a negative real strip. Its complete vertical contour can be
moved through the other conditional root. The real phase is strictly
concave along that entire vertical line, and the exact factorial
remainders control both infinite tails uniformly in the level.

This proves a nonzero packet for that whole period on the entire
actual type-three containing rectangle. It does not identify the
complete homogeneous remainder with that period or with the selected
left critical contribution. No numerical evaluation is used.

## 1. The exact source after cancellation of the kernel poles

Keep \(r=e^{-2\pi i/N}\), \(X=e^{-2\pi ia}\),
\(W=e^{-2\pi iy}\), \(\alpha_N=-1/(2N)\), and the original row
\[
 T_N(s)=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+y)
                              E_N(a)E_N(y)E_N(s)^2 .
 \tag{1}
\]
The [second homogeneous period](research_mixed_three_fourier_conditional_homogeneous_period.md)
is the actual upward integral
\[
 \mathcal I_{2,N}(a,y)=
 \int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
              \frac{t}{(1-t)^2}T_N(s)\,ds,
 \qquad t=e^{-2\pi iNs}.
 \tag{2}
\]
There is no outside index density \(N\) in (2).
Here \(0<\Re a,\Re y<1/2\), as in its original parameter domain.

The original one-period factorial identity gives the exact equality
\[
 \boxed{\quad
 \frac{t}{(1-t)^2}T_N(s)
   =\widetilde T_N(s):=
    e^{2\pi iN(a-1)s}\Pi_N(s+a)\Pi_N(s+y)
                          E_N(a)E_N(y)E_N(s+1)^2 .
 \quad}
 \tag{3}
\]
Indeed \(\Pi_N(s+1)=(1-t)\Pi_N(s)\). Thus (3) is an
undivided identity after the prescribed reciprocal continuations.
In the whole vertical strip
\[
                  -\min(\Re a,\Re y)<\Re s<0
 \tag{4}
\]
both numerator real parts are positive and below one, and
\(0<\Re(s+1)<1\). All factors on the right of (3) are
holomorphic and nonzero there. Every apparent negative physical
kernel pole on the left has been canceled by the actual reciprocal
factorial zeros. No row or residue has been removed.

For sufficiently large \(N\), \(\alpha_N\) lies in (4).
The original fixed-level factorial formulas give, uniformly in
bounded real substrips,
\[
 \begin{array}{ll}
 \widetilde T_N(s)\sim C_{-,N}(a,y)e^{2\pi iN(a-1)s},
                         &\Im s\to-\infty,\\
 \widetilde T_N(s)\sim C_{+,N}(a,y)e^{2\pi iN(1-y)s},
                         &\Im s\to+\infty .
 \end{array}
 \tag{5}
\]
The constants are nonzero and fixed at each level. To check the
upper exponent, apply the marked quadratic phase
\(i\pi\{N(z-z^2)-z\}\) to \(s+a,s+y,s+1,s+1\);
its \(s\)-dependent part, plus the chirp in (3), is
\(2\pi iN(1-y)s\). The lower factorial constants cancel
directly in the ratio. Both horizontal connecting integrals
therefore vanish, with decay rates \(2\pi N(1-\Re a)\) and
\(2\pi N(1-\Re y)\). Consequently (2) equals the upward
integral of (3) on any other vertical line in (4).

## 2. The other root belongs to this original strip

Fix \(y=x_0\) and the full rectangle
\[
       \mathcal A=[267/1000,433/1000]+i[-9/125,17/250].
 \tag{6}
\]
Write the cotangents and the selected left root as
\[
 P=p+i\alpha,\qquad Q=q-ib,\qquad S_1=u-iv .
 \]
The [actual-input](research_mixed_three_conditional_actual_input_subdomain.md),
[left zero-mode](research_mixed_three_fourier_conditional_left_zero_mode.md),
and [action-height](research_mixed_three_fourier_conditional_action_height.md)
proofs give
\[
 \begin{gathered}
 0<p<9/10,\quad |\alpha|<387/1000,\quad q>127/100,\\
 17/25<b<73/100,\qquad u,v>0,\quad |S_1|<1 .
 \end{gathered}
 \tag{7}
\]
The other root is
\[
 S_2=-P-Q-S_1=-(p+q+u)+i(b-\alpha+v).
 \tag{8}
\]
Choose its inverse cotangent \(s_2\) with \(1/2<\Re s_2<1\).
Equation (8) implies
\[
                      3/4<\Re s_2<1,\qquad \Im s_2<0.
 \tag{9}
\]
The first follows from \(|S_2|>q>1\), and the second from
\(b-\alpha>293/1000\).

We also need \(\Re(s_2+y)>1\), not just the weaker bound
\(\Re(s_2+y)>.933\). The exact root identity gives
\[
 (P+S_1)(Q+S_1)=(P-i)(Q+i),\qquad
 \cot\pi(s_2+y)
       =Q+\frac{(Q-i)(Q+S_1)}{P-i}.
 \tag{10}
\]
Put \(C=1-\alpha>613/1000\). The real numerator of the
fraction in (10), after multiplication by \(p+iC\), is
\[
 p\{q(q+u)-(b+1)(b+v)\}
       +C\{q(b+v)+(b+1)(q+u)\}.
 \tag{11}
\]
Its first term is greater than \(-621/500\), and its second
is greater than \((613/1000)(127/100)(59/25)\).
Their sum exceeds \(1488209/2500000>0\).
Thus \(\Re\cot\pi(s_2+y)>q>0\). The real argument lies
between .93 and 1.19; its positive cotangent real part
therefore places it above one.

Set \(z_2=s_2-1\). We have proved
\[
 \boxed{\quad
 -\min(\Re a,\Re y)<\Re z_2<0,\qquad
 \begin{cases}
 0<\Re(z_2+a)<1/2,\\
 0<\Re(z_2+y)<1/2,\\
 3/4<\Re(z_2+1)<1.
 \end{cases}
 \quad}
 \tag{12}
\]
Every inequality is strict uniformly on the compact family (6).
The roots are simple and holomorphic there. Thus (12) persists
on a fixed small complex neighborhood of \(\mathcal A\times\{x_0\}\).
No shifted-height classification is required for this chart.

## 3. The original phase has a unique complete vertical maximum

On (4), use only the original regular-strip primitive:
\[
 \Psi(s;a,y)=g(s+a)+g(s+y)-2g(s+1)-g(a)-g(y)
                                  +2\pi i(a-1)s .
 \tag{13}
\]
Its exponentiated critical equation is the original conditional
quadratic, because \(e^{-2\pi iz_2}=e^{-2\pi is_2}\).
At \(s=z_2\), its derivative has imaginary part strictly between
\[
                  -2\pi(1-\Re a)\quad\hbox{and}\quad
                                      2\pi(1-\Re y).
 \tag{14}
\]
Indeed the shifted real coordinates in (12) have positive
logarithmic arguments, the own coordinate has negative argument,
and the original all-height strip bounds apply. The lower bound
comes from the chirp alone. The upper bound is the sum
\[
 \pi(1-2\Re(s+a))+\pi(1-2\Re(s+y))
 -2\pi(1-2\Re(s+1))+2\pi(\Re a-1)
                      =2\pi(1-\Re y).
 \]
Both endpoints of (14) lie strictly between \(-2\pi\) and
\(2\pi\). The exact logarithmic lift is consequently zero:
\[
                            \Psi_s(z_2)=0.
 \tag{15}
\]

Along the entire vertical line \(\Re s=\Re z_2\), the
real-coordinate conditions (12) remain fixed. Hence
\[
 \Re\Psi_{ss}(s)
  =\pi\Re\{\cot\pi(s+a)+\cot\pi(s+y)
                                  -2\cot\pi(s+1)\}>0
                         \qquad(-\infty<\Im s<\infty).
 \tag{16}
\]
Thus \(v\mapsto\Re\Psi(\Re z_2+iv)\) is strictly concave,
and its unique global maximum is at \(v=\Im z_2\).
The derivative tends to \(2\pi(1-\Re a)>0\) at the lower
infinite end and to \(-2\pi(1-\Re y)<0\) at the upper end.
These limits are uniform over the parameter compact and follow
also from the original upper/lower primitive formulas.

## 4. Uniform infinite tails and the whole-period Gaussian

On every bounded portion of the line in (12), the literal row (3)
has the uniform holomorphic expansion
\[
 \widetilde T_N(s)=N^{-1}\mathcal A_2(s;a,y)
                                  e^{N\Psi(s;a,y)}(1+O(N^{-1})),
 \tag{17}
\]
\[
 \mathcal A_2(s;a,y)=
 \frac{\mathfrak a(s+a)\mathfrak a(s+y)}
      {\mathfrak a(a)\mathfrak a(y)\mathfrak a(s+1)^2}.
 \tag{18}
\]
Here \(\mathfrak a\) is the original nonzero regular-strip
factorial symbol. All arguments in (18) have their actual
strip branches. The power \(N^{-1}\) comes from two numerator
and four reciprocal square-root factorial powers.

We record the uniform tail argument rather than replacing it by
fixed-\(N\) convergence. The exact
[cyclotomic factorial remainder](research_exact_cyclotomic_factorial.md),
equations (8)--(9), bounds each varying factorial remainder at
height magnitude \(v\ge H\) by \(N\epsilon(v)\), where
\(\epsilon_H=\sup_{v\ge H}\epsilon(v)\to0\). This is the same
explicit remainder construction used for the original endpoint
current, with the fixed shifts \(a,y,1\) in place of its shifts.
There are four varying factorials, counted with multiplicity.
Comparing their values at \(v\) and at \(H\) costs at most
\(8N\epsilon_H\).

Let \(c=\Re z_2\). Formula (5) and this exact remainder give,
for \(v\ge H\), uniformly on the compact parameter family,
\[
 \begin{split}
 |\widetilde T_N(c+iv)|
   &\le C|\widetilde T_N(c+iH)|
       e^{-2\pi N(1-\Re y)(v-H)+8N\epsilon_H},\\
 |\widetilde T_N(c-iv)|
   &\le C|\widetilde T_N(c-iH)|
       e^{-2\pi N(1-\Re a)(v-H)+8N\epsilon_H}.
 \end{split}
 \tag{19}
\]
Only zero-free original strip factorials on this line are divided
in these same-source ratios. Fixed parameter factors cancel.
The upper marked linear terms have already been retained in (5).

Write \(M_2=\Re\Psi(z_2)\). By (16) and the uniform nonzero
limiting slopes, choose one sufficiently large fixed \(H\) so that
\[
 M_2-\Re\Psi(c\pm iH)>\gamma_H>0,\qquad
                              8\epsilon_H<\gamma_H/2
 \tag{20}
\]
uniformly. Using (17) at the two finite starting points and
integrating (19) bounds both complete tails by
\(CN^{-2}e^{N(M_2-\gamma_H/2)}\).
On the remaining compact vertical segment, strict concavity gives
a uniform gap away from any fixed small neighborhood of \(z_2\).
Near the root, (16) gives an accretive vertical Gaussian.

Consequently the complete integral (2), with its upward orientation,
has the nonzero packet
\[
 \boxed{\quad
 \mathcal I_{2,N}(a,y)
  = i\sqrt{2\pi}\,N^{-3/2}
      \frac{\mathcal A_2(z_2;a,y)}
           {\sqrt{\Psi_{ss}(z_2;a,y)}}
          e^{N\Psi(z_2;a,y)}(1+O(N^{-1})).
 \quad}
 \tag{21}
\]
The square root is the accretive one supplied by
\(\Re\Psi_{ss}>0\). The factor \(i\) is the upward line element.
Odd cubic and linear corrections vanish on the symmetric local
vertical segment, giving the stated relative \(O(N^{-1})\).
Both level parities use the same original interpolation.

The integral and its critical data are holomorphic on the common
parameter neighborhood from (12). Vertical lines are interchangeable
by (3)--(5), so their moving real parts introduce no new endpoint
terms. The estimates above are uniform there; normalized fixed
parameter derivatives follow on smaller neighborhoods by Cauchy's
estimate.

The existing exponential-flatness theorem for (2) is consistent with
(21) and implies a uniform negative upper bound for
\(\Re\Psi(z_2)\) on each smaller parameter compact. This is a
nonzero exponentially small period, not an identically vanishing
one. It is not the same object as the full homogeneous remainder
of \(C_{0,N}\), whose exact contour and Casoratian data must still
determine the observed combination of critical contributions.
