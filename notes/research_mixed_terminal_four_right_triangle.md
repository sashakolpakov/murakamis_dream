# A half-period comparison for the type-four terminal sum

Research deduction, 5 November 2026. The absolute exponential rate of
every type-four summand with outer index at least half the level is
bounded by its maximum on the half-period face. This reduces that
entire part of the physical support to one comparison with the
geometric action. The comparison itself is not proved here. The
argument uses the exact three-index source and elementary inequalities;
it requires no new numerical enclosure.

## 1. The exact summand and its real rate

Use the source of [the joint type-four calculation](research_mixed_terminal_four_joint_source.md).
For \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\), write
\[
 P_j=(r;r)_j,\qquad S_j=\prod_{k=1}^j2\sin(\pi k/N),
 \qquad p_i(X)=(rX;r)_i,\qquad \delta_j=P_j/S_j.
 \tag{1}
\]
The empty products are one. The original Newton polynomial is
\[
 e_l(w)=\frac{\prod_{k=0}^{l-1}
          (2\cos((2k+1)\pi/N)-w)}{S_l^2}.
 \tag{2}
\]
Thus the literal terminal polynomial is
\[
 \mathcal V_{1,N}(w,X)=
 \sum_{\substack{i+j<N\\0\le l\le j}}
 \frac{X^{-i}p_i(X)P_{i+j}}{P_i^3P_j}
 \delta_j^{-1}\frac{q^{jl}e_l(w)}{S_lS_{j-l}}.
 \tag{3}
\]
Every factorial in a denominator has index less than \(N\).
We keep the exact support \(i+j<N\); no vanished numerator is
continued past this wall.

Let \(a=y+iH\), \(X=e^{-2\pi ia}\), and assume
\(y\in[.22,.45]\), \(|H|\le.12\). The external product
has the continuous upper rate
\[
 Q_a(t)=\int_0^t
       \log|e^{-2\pi H}-e^{-2\pi i(y+s)}|\,ds.
 \tag{4}
\]
This is the rate of \(X^{-i}p_i(X)\), including its chirp, when
\(t=i/N\). It remains meaningful at an external product zero.

Put \(e=j/N\), \(u=l/N\), and restrict for now to
\(t\ge1/2\). Then \(0\le u\le e<1-t\le1/2\).
With \(J'(x)=\log(2\sin\pi x)\), \(J(0)=0\), the
complete-color Newton upper rate is
\(-2J(1/2-u)-2J(u)\). The sine-factorial estimates and the
zero-safe Newton estimates used in
[the type-three half-period reduction](research_mixed_terminal_three_right_triangle.md)
therefore give the absolute summand rate
\[
\begin{split}
 R_1(a;t,e,u)={}&-2J(1/2-u)-3J(u)-J(e-u)\\
               &+J(e+t)-3J(t)-J(e)+Q_a(t).
\end{split}
 \tag{5}
\]
Here \(|q^{jl}|=|\delta_j|=1\). Formula (5) is an upper
rate at zeros and endpoints, not a relative asymptotic there.

Set \(L=-J\) on \([0,1/2]\), with continuous endpoint
values, and \(v=1-t\). The reflection identity
\(J(1-x)=-J(x)\) gives
\[
\begin{split}
 R_1(a;1-v,e,u)&=F(v;e,u)+Q_a(1-v),\\
 F(v;e,u)&=2L(1/2-u)+3L(u)+L(e-u)\\
         &\quad+L(v-e)+L(e)-3L(v),
       \qquad 0\le u\le e\le v\le1/2.
\end{split}
 \tag{6}
\]

## 2. The optimized entropy increases faster than the external factor

For \(0<v\le1/2\), define
\[
 M_4(v)=\max_{0\le u\le e\le v}F(v;e,u).
 \tag{7}
\]
The maximizer \((e_*(v),u_*(v))\) is unique and interior.
Indeed, on \(0<u<e<v\), the negative Hessian in \((e,u)\)
has the quadratic form
\[
\begin{split}
 -\pi^{-1}F''={}&(2\tan\pi u+3\cot\pi u)\,du^2\\
 &+\cot\pi(e-u)(de-du)^2\\
 &+(\cot\pi(v-e)+\cot\pi e)\,de^2.
\end{split}
 \tag{8}
\]
It is positive definite. For each \(0<e<v\), the derivative
\(F_u\) tends to \(+\infty\) at zero and to \(-\infty\)
at \(u=e\). Its unique zero satisfies
\[
 \sin\pi(e-u)=\frac{\sin^3\pi u}{\cos^2\pi u}.
 \tag{9}
\]
After maximizing in \(u\), the derivative with respect to \(e\) is
\[
 F_e=\log\frac{\sin\pi(v-e)}
                  {2\sin\pi e\sin\pi(e-u)}.
 \tag{10}
\]
It tends to \(+\infty\) as \(e\downarrow0\), and to
\(-\infty\) as \(e\uparrow v\). For the first limit use
\(u<e\) in (9). For the second, the optimizing \(u\) has an
interior limit for each fixed \(v\), including \(v=1/2\),
where that limit is \(u=1/4\). Strict concavity now proves the
claim and permits differentiation of (7).

**Lemma 1.** For \(0<v\le1/2\), with a left derivative at the
upper endpoint,
\[
                         M_4'(v)>\log4.
 \tag{11}
\]

*Proof.* Write \(V=\pi v\). First let \(V<\pi/2\), set
\(s=\sin V\), and choose the comparison angle
\[
                    E_0=V-\arcsin(s^3).
 \tag{12}
\]
It lies strictly between zero and \(V\). At \(e=E_0/\pi\),
let \(U=\pi u\) maximize the inner variable. By (9),
\[
 2\sin E_0\sin(E_0-U)
 =2\sin E_0\frac{\sin^3U}{\cos^2U}
 <\frac{2\sin^4E_0}{\cos^2E_0}.
 \tag{13}
\]
We used that \(\sin^3 U/\cos^2 U\) is strictly increasing
on \((0,\pi/2)\) and \(U<E_0\).

The elementary comparison from the type-three proof applies unchanged:
\[
 \sin E_0
 =s\sqrt{1-s^2}\bigl(\sqrt{1+s^2+s^4}-s^2\bigr)
 <s\sqrt{1-s^2},
 \tag{14}
\]
and consequently
\[
 \frac{2\sin^4E_0}{\cos^2E_0}
 <\frac{2s^4(1-s^2)^2}{1-s^2+s^4}<s^3.
 \tag{15}
\]
The last inequality follows from
\(2s(1-s^2)\le4/(3\sqrt3)<1\).
Since \(\sin(V-E_0)=s^3\), (10), (13) and (15) show
that the optimized derivative in \(e\) is positive at \(E_0/\pi\).
Strict concavity forces \(\pi e_*>E_0\). Thus
\(\sin\pi(v-e_*)<\sin^3\pi v\).

Differentiating at the stationary pair gives
\[
 M_4'(v)=\log\frac{4\sin^3\pi v}
                         {\sin\pi(v-e_*)}>\log4.
 \tag{16}
\]
At \(v=1/2\), interiority gives the same inequality directly,
since \(\sin\pi(v-e_*)<1\). This proves the lemma.
\(\square\)

Also \(M_4(v)\to0\) as \(v\downarrow0\), by continuity
of (6) on its shrinking domain. No concavity of \(M_4\) itself
has been assumed.

## 3. The entire upper triangle is bounded by its half-period face

The function (4) is absolutely continuous, including across its
integrable logarithmic singularities. Almost everywhere,
\[
 Q_a'(t)\le\log(1+e^{.24\pi})<\log(63/20).
 \tag{17}
\]
The final scalar bound is the same one used in the type-three
half-period proof. Combining (11) and (17), integrating on compact
subintervals, and passing to the endpoints gives the following result.

**Theorem 2.** For every external parameter admitted above and every
point of the real support with \(t\ge1/2\),
\[
 R_1(a;t,e,u)\le M_4(1/2)+Q_a(1/2)
                   -\log(80/63)(t-1/2).
 \tag{18}
\]
This bounds each absolute summand, so it remains valid for arbitrary
restrictions of this physical region.

The half-period maximum is independent of the external parameter.
Its unique maximizing pair \((e_\circ,u_\circ)\) satisfies
\[
 \sin\pi(e_\circ-u_\circ)
       =\frac{\sin^3\pi u_\circ}{\cos^2\pi u_\circ},
 \qquad
 \cot\pi e_\circ=2\sin\pi(e_\circ-u_\circ).
 \tag{19}
\]
It lies strictly in
\[
           .27<e_\circ<.40,\qquad .20<u_\circ<.25.
 \tag{20}
\]
Here is an elementary enclosure, to make the relation to the regular
source domain explicit. Put
\(f(U)=\sin^3U/\cos^2U\),
\(E(U)=U+\arcsin f(U)\). On \(0<U<\pi/4\), the
function \(\cot E(U)-2f(U)\) strictly decreases from positive
values to negative values. Its zero describes (19). At \(U=\pi/5\),
the exact trigonometric values give
\[
 7/12<\sin U<59/100,\qquad
 4/5<\cos U<81/100<13/16,
 \qquad 3/10<f(U)<13/40.
 \tag{21}
\]
For example the sine and cosine inequalities follow from
\(223/100<\sqrt5<56/25\), and the bounds for \(f\) follow
by substitution. Since \(\sqrt{1-f^2}>47/50\),
\[
\begin{split}
 \cos E&>(4/5)(47/50)-(59/100)(13/40)=2241/4000,\\
 2f\sin E&<(13/20)\{59/100+(81/100)(13/40)\}
                                      =44369/80000.
\end{split}
 \tag{22}
\]
The first number is larger: their difference is \(451/80000\).
Therefore \(u_\circ>1/5\), and \(u_\circ<1/4\) follows
from the interval on which the zero was located. Now
\(e_\circ>1/5+(3/10)/\pi>.27\), whereas (19) gives
\(\cot\pi e_\circ>3/5>\cot(2\pi/5)\), so
\(e_\circ<2/5\). This proves (20).

In particular the maximizing pair lies in the broad regular box of
the joint source note. At \(t=1/2\) the whole such box has
\(a+t\) and \(e+t\) in their regular strips. Its original
phase \(\mathcal F_1\) therefore agrees in real part with (5):
\[
 M_4(1/2)+Q_a(1/2)
  =\Re\mathcal F_1(a;e_\circ,1/2,u_\circ).
 \tag{23}
\]
No phase is continued through an external product zero in obtaining
the full triangular estimate (18).

## 4. What remains to prove for the finite sum

Let \(a_*=A+iH\) be an actual type-four terminal reference,
and let \(P_1\) be its original calibrated action. Define the bare
supporting plane, with \(\kappa_*=1/2500000\), by
\[
 B_{1,0}(a_*;y)=\Re P_1(a_*)+
     \Re P_1'(a_*)(y-A)-\kappa_*(y-A)^2.
 \tag{24}
\]
A sufficient additional comparison is a uniform \(\delta>0\)
such that
\[
 \Re\mathcal F_1(y+iH;e_\circ,1/2,u_\circ)
                       \le B_{1,0}(a_*;y)-\delta.
 \tag{25}
\]
No such gap is asserted here. One may equivalently bound the whole
raw half-period face in the broad regular box, because (20) contains
its global maximizing pair. There is no Fourier penalty in (25).

If (25) holds, (18) and the uniform product estimates bound the
positive majorant of every term in (3) with \(i/N\ge1/2\) by
\(\exp N(B_{1,0}-\delta')\), for any fixed
\(0<\delta'<\delta\) and all sufficiently large \(N\).
The at most \(N^3\) terms and endpoint factorial factors cost
only polynomial prefactors. The zero-safe whole-color Newton bound
preserves the gap on a sufficiently small fixed disk about \(w=-2\).
Cauchy's formula applied to each polynomial before taking absolute
values gives the same rate for every fixed ordinary-color derivative.
Both level parities and all numerator zeros are retained.

For an incoming type-four coordinate, its actual height is negative.
Multiplication by the original unselected Fourier halfweight, and
horizontal convexity of \(\Re g\), then gives the corresponding
allocated supporting plane just as in the type-three proof. No
division by that Fourier polynomial is required.

The theorem proved here is (18), with its exact source and explicit
maximizer enclosure. It does not establish the calibrated comparison
(25), the remaining lower-index regions, or noncancellation of the
whole type-four polynomial.
