# A strict phase loss on the negative inner horizontal

Private phase theorem, 8 November 2026. The original edge phase
continues to the signed first-angle box with its principal returns
and complete additive constant. An explicit second-derivative
bound then compares the negative inner horizontal with the
positive one. On the actual critical height, the entire negative
horizontal has a uniform strict action loss.

This is a phase comparison. A finite shortened-kernel estimate at
the corresponding mixed angular heights is a separate source
obligation. No mathematical numerical evaluation or frozen-source
edit is used.

## 1. The original phase on a signed box

Consider
\[
 \mathcal Q_\pm=
 \{(t,u):|\Re t|\le\pi/2,\ |\Im t|\le1,\quad
             0\le\Re u\le\pi/2,\ -1/2\le\Im u\le0\}.
\tag{1}
\]
Put
\[
 c=\cos(t/2),\qquad C=\cos(u/2),\qquad
 A=c^2,\quad B=C^2,\quad D=A+B-AB .
\tag{2}
\]
The same elementary bounds used in
[full-box horizontal concavity](research_mixed_next_inner_three_horizontal_concavity.md)
give, throughout (1),
\[
 |1-A|<4/5,\qquad |1-B|<4/7,\qquad
                 |1-D|<16/35<1/2 .
\tag{3}
\]
Indeed, for \(t=a+is\),
\(|1-A|=(\cosh s-\cos a)/2\), and the real-angle
cosines in (1) are nonnegative. The bounds
\(\cosh1<8/5\) and \(\cosh(1/2)<8/7\) are the same
written series inequalities as in that source.
In particular
\[
                       \Re D>19/35>1/2 .
\tag{4}
\]

We verify the principal-return cuts explicitly on this larger
box. First,
\[
 |\arg c|<\pi/6,\qquad 0\le\arg C<\pi/12,\qquad
                         |\arg D|<\pi/6 .
\tag{5}
\]
For the first assertion,
\[
 \left|\frac{\Im c}{\Re c}\right|
      =|\tan(a/2)\tanh(s/2)|
        \le\tanh(1/2)<1/2<\tan(\pi/6).
\]
For the second use
\(\tanh(1/4)<1/4<2-\sqrt3=\tan(\pi/12)\);
the displayed strict rational comparison follows from
\(\sqrt3<7/4\). The cosines have positive real parts.
Finally the disk \(|D-1|<1/2\) lies in
\(|\arg D|<\pi/6\). For example, if \(D=re^{i\theta}\)
with \(\Re D>0\), then
\[
                 |D-1|^2=(r-\cos\theta)^2+\sin^2\theta,
 \qquad -\pi/2<\theta<\pi/2,
\]
which proves the assertion.

Define the original two return arguments
\[
 z_t=\tan(t/2)C,\qquad z_u=\tan(u/2)c .
\tag{6}
\]
Their exact identities are
\[
                   1+z_t^2=D/c^2,\qquad
                   1+z_u^2=D/C^2 .
\tag{7}
\]
By (5), the first ratio in (7) has argument strictly between
\(-\pi/2\) and \(\pi/2\), and the second has argument
strictly between \(-\pi/3\) and \(\pi/3\).
Both therefore have positive real part. In particular neither
\(z_t\) nor \(z_u\) belongs to either principal inverse-hyperbolic-sine
cut \(i[1,\infty)\) or \(-i[1,\infty)\) for
\(\operatorname{arsinh}\): at such a point \(1+z^2\)
would be nonpositive real.

The original one-form
\[
 d\psi=-\frac1\pi\{
     \operatorname{arsinh}(z_t)\,dt+
     \operatorname{arsinh}(z_u)\,du\},\qquad
                         \psi(0,0)=-8J(1/4)
\tag{8}
\]
is consequently holomorphic on a fixed complex neighborhood
of (1). Its closedness uses the unchanged branch calculation.
The functions
\[
 c\sqrt{1+z_t^2},\qquad C\sqrt{1+z_u^2}
\]
have square \(D\), are nonzero, and agree with the principal
\(\sqrt D\) at completeness. Connectedness, (4) and the
specified principal returns identify both with that same root
throughout the box. Hence
\[
 \partial_u\operatorname{arsinh}(z_t)
 =-\frac{\sin(t/2)\sin(u/2)}{2\sqrt D}
 =\partial_t\operatorname{arsinh}(z_u).
\tag{9}
\]
Choose a convex neighborhood of the compact box small enough
to retain these strict guards. The primitive in (8) is then
holomorphic there. On the original lower positive box it
agrees with
[the endpoint phase primitive](research_mixed_next_shortened_edge_endpoint_gap.md),
by its derivatives and complete constant. It is therefore the
analytic continuation of that original phase, not a new phase
with a reassigned logarithmic charge.

The same construction proves the two symmetries needed below:
\[
 \psi(-t,u)=\psi(t,u),\qquad
                   \psi(\overline t,0)=\overline{\psi(t,0)}.
\tag{10}
\]
For the first, the \(t\)-derivative in (8) is odd in \(t\),
and the values agree at \(t=0\). For the second, the principal
return and tangent commute with conjugation on their stated
domain, and the constant \(-8J(1/4)\) is real.

## 2. An explicit reflected-edge action debit

Differentiating the original return on the signed box gives
\[
                       \psi_{tt}(t,u)
                            =-\frac{C}{2\pi c\sqrt D}.
\tag{11}
\]
The bounds
\[
 |c|^2=\frac{\cosh(\Im t)+\cos(\Re t)}2\ge\frac12,
 \qquad |\sqrt D|>1/\sqrt2,\qquad |C|<8/7
\]
imply the uniform estimate
\[
                  |\psi_{tt}(t,u)|<\frac8{7\pi}.
\tag{12}
\]
The same branch is used along every vertical segment in (1).

Fix \(u\in\mathcal U_+\), \(0\le H\le1\), and define
\[
 \Delta(a)=\Re\{\psi(a+iH,u)-\psi(a-iH,u)\},
                           \qquad0\le a\le\pi/2 .
\tag{13}
\]
Evenness gives \(\Delta(0)=0\). The fundamental theorem of
calculus and (12) give
\[
\begin{split}
 \Delta'(a)
 &=\Re\left\{i\int_{-H}^{H}
                    \psi_{tt}(a+is,u)\,ds\right\},\\
 |\Delta'(a)|&\le\frac{16H}{7\pi}.
\end{split}
\tag{14}
\]
Consequently
\[
                   \Delta(a)\le\frac{16aH}{7\pi}.
\tag{15}
\]
No sign of \(\Delta\) itself is required.

Keep the original charge-one inner phase
\[
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it.
\tag{16}
\]
By (10), the real parts of its first edge agree at
\(-a-iH\) and \(a-iH\). Its second-edge difference is
exactly (13). The unit-charge terms have equal real parts,
while the difference of the quadratic crossing terms is
\(-3aH/\pi\). Thus
\[
 \boxed{\qquad
 \Re\Phi(-a-iH,u)-\Re\Phi(a-iH,u)
                \le-\frac{5aH}{7\pi},
 \quad0\le a\le\pi/2,\quad0\le H\le1 .
 \qquad}
\tag{17}
\]
The comparison includes the original chirp and the original
trace charge. Evenness of the edge alone would not give it.

## 3. The entire actual negative horizontal is below the saddle

Let \(t_*(u)=a_*(u)-iH_*(u)\) be the original cubic branch
on \(\mathcal U_+\), and put \(s(u)=\Re S_3(0,u)\).
The adopted horizontal concavity theorem gives
\[
 \Re\Phi(a-iH_*,u)
       \le s(u)-\frac{(a-a_*)^2}{8\pi},
                         \qquad0\le a\le\pi/2 .
\tag{18}
\]
Combining it with (17) proves the full comparison
\[
 \boxed{\qquad
 \Re\Phi(-a-iH_*,u)
 \le s(u)-\frac{(a-a_*)^2}{8\pi}
                      -\frac{5aH_*}{7\pi}.
 \qquad}
\tag{19}
\]
In particular there is a uniform strict loss, including at \(a=0\).
To state it without evaluating the compact family, put
\[
 a_0=\min_{\mathcal U_+}a_*(u)>0,\qquad
 H_0=\min_{\mathcal U_+}H_*(u)>0,
\]
\[
 \epsilon_-=
      \min\left\{\frac{a_0^2}{32\pi},
                        \frac{5a_0H_0}{14\pi}\right\}>0.
\tag{20}
\]
If \(a\le a_*/2\), the quadratic term in (19) is at least
\(a_0^2/(32\pi)\). If \(a\ge a_*/2\), its linear term
is at least \(5a_0H_0/(14\pi)\). Therefore
\[
 \boxed{\qquad
 \Re\Phi(-a-iH_*(u),u)\le
       \Re S_3(0,u)-\epsilon_-,
 \qquad 0\le a\le\pi/2,\quad u\in\mathcal U_+ .
 \qquad}
\tag{21}
\]
All constants and actions retain their original calibration.

## 4. Exact limitation

At a negative lower inner angle, evenness of the finite second
edge converts it to \(K_N^{<}(a+iH,u)\), whose two angular
heights have opposite signs. The positive-lower shortened-edge
packet and its right-horizontal extension do not automatically
give a bound for that mixed-height source. Equation (21) pays
its continued phase; it does not replace that missing source
theorem.

The complete inner Hermite trace also retains its odd central
pole and its original rational Fourier denominator. Neither
an endpoint connector nor a complete signed angular current
has been deleted here. A full inner packet or an outer-transfer
asymptotic still requires those finite-source estimates.
