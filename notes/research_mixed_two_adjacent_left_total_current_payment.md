# Paying the complete left current of the fixed-total source

Research deduction, 7 November 2026. At the actual merged-pair
critical total, the complete left endpoint current of the fixed
cutoff interpolant is exponentially below the original inner action.
The proof retains the full midpoint weight, both infinite directions,
and the original upper and lower factorial branches. Its strict gap
persists on a fixed complex parameter neighborhood. No source or
critical point is evaluated numerically.

## 1. The actual parameters and the exact current

Use the source \(T_N(a;c,x,y)\), cuts, and complete contour identity
from [the fixed-total interpolant](research_mixed_two_adjacent_fixed_total_interpolant.md).
Initially fix
\[
 c=c_*=2a_*=C+iv,\qquad x=y=x_0=\xi+i\upsilon,\qquad h=v/2.
 \tag{1}
\]
The proved original geometry gives
\[
 2/3<C<4/5,\quad 1/10<v<1/6,\quad
 .18299<\xi<.18301,\quad .07871<\upsilon<.07873.
 \tag{2}
\]
The slightly sharper bound \(v<1/6\) follows from
\(v<2\operatorname{atanh}(1/4)/\pi\): using
\(\operatorname{atanh}(1/4)<23/90\) and \(\pi>157/50\)
gives \(v<230/1413<1/6\).

The exact left contribution, including its sign in the source, is
\[
 \mathcal L_N(c,x,y)
   =-iN\int_{-\infty}^{\infty}w_{N,h}(t)
                         T_N(\alpha_N+it;c,x,y)\,dt,
 \quad \alpha_N=-1/(2N).
 \tag{3}
\]
At (1) its original rate profile is
\[
\begin{split}
 D(t)={}&\Re\{g(c)+g(x_0+it)+g(c+x_0-it)
                          -2g(c-it)-2g(x_0)\}-2\pi Ct,\\
 P(t)={}&D(t)+2\pi t\boldsymbol1_{\{t<h\}}.
\end{split}
 \tag{4}
\]
All arguments of \(g\) here have real part in \((0,1)\).
This is the profile obtained from the exact cancellation
\(|E_N(\alpha_N+it)|^2=(1+e^{2\pi Nt})/N\) against the
whole sampling denominator. Neither half of that denominator is
replaced by an unrelated Fourier bound.

## 2. Radial bounds and elementary dilogarithm estimates

Put
\[
 r=e^{-2\pi\upsilon},\quad b=e^{-2\pi v},\quad
 \theta=2\pi\xi,\quad \psi=2\pi(1-C),\quad
                         \chi=2\pi(1-C-\xi).
 \tag{5}
\]
All three angles lie in \((0,\pi)\). In particular
\(2\pi/5<\psi<2\pi/3\), so \(\sin\psi>6/7\).
The inherited bounds imply
\[
 \frac35<r<\frac8{13},\qquad
 \frac9{25}<b<\frac59,\qquad \sqrt b<\frac34.
 \tag{6}
\]
Here \(2\pi\upsilon<1/2\), and
\(e^{1/2}\le33/20<5/3\), giving the lower bound for \(r\).
For its upper bound, \(2\pi\upsilon>49/100\) and the positive
cubic exponential sum gives \(e^{49/100}>13/8\).
The exact bound \(v<2\operatorname{atanh}(1/4)/\pi\) gives
\(b>e^{-4\operatorname{atanh}(1/4)}=9/25\).
Also \(2\pi v>3/5\) and \(e^{3/5}>9/5\), giving
\(b<5/9<9/16\). These exponential comparisons follow from
positive finite series or the majorant
\(e^u\le1+u+u^2/[2(1-u/3)]\), for \(0<u<3\).

For \(0<\omega<\pi\), \(0\le z\le1\), define
\[
 F_\omega(z)=\Im\operatorname{Li}_2(ze^{i\omega}),\qquad
 A_\omega(z)=\Arg(1-ze^{-i\omega}).
 \tag{7}
\]
These are the original disk branches, continuous at \(z=1\).
They satisfy
\[
 zF_\omega'(z)=A_\omega(z)>0\quad(z>0),\qquad
 F_\omega(z)\ge\sin\omega\log(1+z),\qquad
 F_\omega(z)\le\operatorname{Li}_2(z).
 \tag{8}
\]
For the middle inequality, write
\(A_\omega(z)=\int_0^z\sin\omega/(1-2u\cos\omega+u^2)\,du\).
Since the denominator is at most \((1+u)^2\),
\(A_\omega(z)\ge z\sin\omega/(1+z)\), and integrate once
more. For estimates of the positive real dilogarithm we use
\[
 \operatorname{Li}_2(z)
 \le z+z^2/4+\frac{z^3}{9(1-z)},\qquad 0\le z<1.
 \tag{9}
\]

One sharper bound on the unchanged outgoing angle will be useful:
\[
                         F_\theta(r)<33/50.
 \tag{10}
\]
Indeed the original output witnesses give
\(9/8<\theta<29/25\) and \(\sin\theta<23/25\).
The \(n=3,4\) terms of its sine series are negative.
Also \(\sin(2\theta)<4/5\): write
\(0<\pi-2\theta<25/28\) and use
\(\sin u\le u-u^3/7\) for \(0\le u\le1\), which follows
from the alternating Taylor polynomial. At \(25/28\) this
last expression is \(121575/153664<4/5\).
Consequently (6) gives
\[
\begin{split}
 F_\theta(r)
 &<r\frac{23}{25}+\frac{r^2}5+\frac{r^5}{25(1-r)}\\
 &<\frac{184}{325}+\frac{64}{845}+\frac{32768}{3570125}
  <\frac{57}{100}+\frac{77}{1000}+\frac1{100}
  <\frac{33}{50}.
\end{split}
 \tag{11}
\]

The following additional consequences of (6)--(9) will be used:
\[
\begin{split}
 F_\psi(b)&>13/50, & F_\psi(b)&<7/10,\\
 F_\psi(z)&>3/20&& (z\ge rb),\\
 \operatorname{Li}_2(15/32)&<11/20,\qquad&
 \operatorname{Li}_2(7/20)&<2/5.
\end{split}
 \tag{12}
\]
For the first lower bound, (8) gives
\((6/7)\log(34/25)>(6/7)(18/59)=108/413>13/50\).
For the second lower bound, \(rb>27/125\), so (8) gives
\((6/7)\log(152/125)>(6/7)(54/277)=324/1939>3/20\).
The logarithm witnesses are their first positive
\(2\operatorname{atanh}\) terms. For the upper bounds, (9)
at \(5/9,15/32,7/20\) gives respectively
\[
              985/1458<7/10,\qquad
              341685/626688<11/20,\qquad
              72625/187200<2/5.
 \tag{13}
\]

## 3. The full lower branch on \(-\upsilon\le t<h\)

For positive imaginary part the original marked primitive has
\[
 \Re g(u+iH)
   =\pi H(2u-1)
       -\frac1{2\pi}\Im\operatorname{Li}_2(e^{-2\pi H+2\pi iu}).
 \tag{14}
\]
Its limit at \(H=0\), away from a real integer, agrees with the
original real-strip branch. Apply it to every factor in (4) on
\(-\upsilon\le t<h\), and set
\[
                   z=b e^{2\pi t},\qquad a=r e^{-2\pi t}.
\]
Here the letter \(a\) denotes a positive radius only in this
display and (15), not a summation coordinate. The exact polynomial
terms cancel all dependence on \(t\), leaving
\[
\begin{split}
 P(t)=Q+\frac1{2\pi}\{&F_\psi(b)-2F_\psi(z)
          +F_\chi(rz)+2F_\theta(r)-F_\theta(a)\},\\
 Q&=2\pi(\xi v+C\upsilon)<591/1000.
\end{split}
 \tag{15}
\]
For the last inequality, (2) gives
\[
 Q<\frac{44}{7}
       \left\{\frac{23}{750}+\frac{316}{5000}\right\}
       =\frac{15488}{26250}<\frac{591}{1000}.
 \tag{16}
\]
This calculation retains the original chirp and the \(2\pi t\)
part of the midpoint weight; omitting either would change (15).

If \(0\le t<h\), then \(z\ge b\) and
\(rz\le r\sqrt b<6/13<15/32\). Monotonicity in (8) and
(10)--(12) give
\[
\begin{split}
 &F_\psi(b)-2F_\psi(z)+F_\chi(rz)
                       +2F_\theta(r)-F_\theta(a)\\
 &\hspace{15mm}< -13/50+11/20+33/25=161/100.
\end{split}
 \tag{17}
\]
Since \(1/(2\pi)<25/157\) and \(161/628<257/1000\),
\[
                         P(t)<106/125.
 \tag{18}
\]

If \(-\upsilon\le t\le0\), then \(a\ge r\),
\(z\ge rb\), and \(rz\le rb<40/117<7/20\). Thus
\[
\begin{split}
 &F_\psi(b)-2F_\psi(z)+F_\chi(rz)
                       +2F_\theta(r)-F_\theta(a)\\
 &\hspace{15mm}<7/10-3/10+2/5+33/50=73/50.
\end{split}
 \tag{19}
\]
Now \(73/314<233/1000\), so this part has the stronger
bound \(P(t)<103/125<106/125\).

## 4. Both entire remaining height directions

For \(t< -\upsilon\), put \(q=-\upsilon-t>0\).
The factor \(g(x_0+it)\) is on the lower half-plane. Its
original real part is
\(-F_\theta(e^{-2\pi q})/(2\pi)\); it has no upper-branch
quadratic term. Keeping that branch gives exactly
\[
\begin{split}
 P(t)={}&Q-\pi(1-2\xi)q\\
 &+\frac1{2\pi}\{F_\psi(b)-2F_\psi(rb e^{-2\pi q})
      +F_\chi(r^2b e^{-2\pi q})\\
 &\hspace{37mm}+2F_\theta(r)-F_\theta(e^{-2\pi q})\}.
\end{split}
 \tag{20}
\]
Differentiating in \(q\), (8) yields
\[
 \frac{dP}{dq}
 =-\pi(1-2\xi)+2A_\psi(rb e^{-2\pi q})
       -A_\chi(r^2b e^{-2\pi q})+A_\theta(e^{-2\pi q}).
 \tag{21}
\]
For a disk of radius \(u<1\) centered at one,
\(|\Arg z|\le\arcsin u\le u/\sqrt{1-u^2}\).
Since \(rb<7/20\),
\[
 A_\psi(rb e^{-2\pi q})<7/18,\qquad
 A_\theta(e^{-2\pi q})\le A_\theta(1)=\pi(1/2-\xi).
\]
The remaining argument in (21) is nonnegative. Therefore
\[
 \frac{dP}{dq}< -\pi(1/2-\xi)+7/9
                 <-93/100+7/9=-137/900<-3/20.
 \tag{22}
\]
The two branch formulas agree at \(q=0\). Thus no maximum
is lost below \(t=-\upsilon\), and this entire direction
is strictly decreasing toward infinity.

For \(t\ge h\), the profile is \(P(t)=D(t)\). On the
original strips, \(\Im g'(x_0+it)>0\),
\(\Im g'(c+x_0-it)<0\), and
\(\Im g'(c-it)>\pi(1-2C)\). Consequently
\[
 D'(t)=-\Im g'(x_0+it)+\Im g'(c+x_0-it)
                          -2\Im g'(c-it)-2\pi C
           <2\pi(C-1)<-2\pi/5.
 \tag{23}
\]
At the cut its upper value is the lower limiting value minus
\(2\pi h>0\). Equations (18), (22), (23) therefore prove
the entire two-sided profile estimate
\[
                           \sup_{t\in\mathbb R}P(t)<106/125.
 \tag{24}
\]

## 5. Comparison with the original inner action and finite current

Let \(\phi_* =F_{c_*}(c_*/2)\) be the original inner action
from the fixed-total note. The outside pair chirp has not been
included in \(\phi_*\), so its exact relation to the full
pair action is
\[
                  \Re\phi_*=M_{22}+2\pi\upsilon>43/50.
 \tag{25}
\]
Indeed the proved \(M_{22}>187049/504000>37/100\), and
the original output bounds give \(2\pi\upsilon>49/100\).
Thus (24) leaves a raw gap greater than \(3/250\).

**Theorem.** At the actual parameters (1), the complete original
left endpoint current satisfies
\[
             |\mathcal L_N|
              \le C N^{-1/2}e^{N(\Re\phi_*-1/100)}
 \tag{26}
\]
for all sufficiently large integer levels, with both parities.
There is a fixed complex neighborhood of \((c_*,x_0,x_0)\)
on which the corresponding bound holds with the continued original
inner critical action and gap \(1/200\).

*Proof.* On every bounded height interval, the exact midpoint
factor and the regular-strip estimates in the fixed-total note
give the current-density upper bound
\(CN^{-1/2}e^{NP(t)}\). Use (24)--(25), preserving both
one-sided cut values. The exact uniform nonreal tail estimate
(14a) of that note makes both remaining unbounded pieces smaller
than the same action by a fixed margin, once the height cutoff
is chosen sufficiently large. This proves (26), with a reserve
between the raw and asserted gaps.

For parameter persistence, keep the cut height fixed at the
center value \(h_*\). The complete contour identity permits this.
Both one-sided compact profile families are continuous in the free
parameters, and the nonreal tail estimate is uniform on a compact
parameter neighborhood. Shrinking that neighborhood preserves
gap \(1/200\). The inner critical action is its original
holomorphic implicit-function branch. The integral with fixed
\(h_*\) is holomorphic by the same uniform tail bounds.
Cauchy estimates on a smaller neighborhood therefore also bound
every fixed normalized mixed derivative of
\(N^{1/2}e^{-N\phi(c,x,y)}\mathcal L_N(c,x,y)\)
exponentially, for example with gap \(1/400\).
\(\square\)

This pays the whole left correction of the legitimate fixed-total
source. Its right correction, the complementary physical totals,
the outer sampling currents, and the prescribed closing observation
are separate. No whole adjacent-pair packet or new knot-family
conclusion is inferred here.
