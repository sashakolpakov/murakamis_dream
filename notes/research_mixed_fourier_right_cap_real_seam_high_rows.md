# Payment of the high retained rows at the real outgoing endpoint

Research deduction, 7 November 2026. At the physical outgoing point
\(q=0\), every high retained row is bounded below the original
supporting plane. Consequently the complete conditional kernel may
replace its low-index truncation at this one endpoint, with an
exponentially small error after retaining the original cardinal
coefficient and incoming allocation.

This does not bound the central coherent seam or its complex
vertical deformation. No numerical evaluation is used.

## 1. The exact physical endpoint and its row rate

Retain the actual correlated references and targets from the
[completed bare inner-source theorem](research_mixed_fourier_right_cap_bare_inner_completion.md):
\[
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 a=x+i h,\quad x\in[11/50,9/20],\quad h=\Im a_*,
 \quad y=x_0,\quad Y=e^{2\pi iy}.
 \tag{1}
\]
The incoming height obeys \(-.108\le h\le.068\); when \(\eta=1\),
it is the original negative, unselected height. Keep the actual
plane \(B_\eta(x)\) and \(\kappa=1/2500000\) from that theorem.
No independent-height extension is made.

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(X=e^{-2\pi ia}\), the literal
outgoing coefficient at \(q=0\) is
\[
 f_0(y)=\frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}.
 \tag{2}
\]
Since \(p_j(1)=P_j\),
\[
 C_{1,N}(X,1)=\sum_{j=0}^{N-1}\frac{X^{-j}p_j(X)}{P_j^2}.
 \tag{3}
\]
Put \(M_N=\lceil N/2\rceil-1\) and let \(C_N^<(X,1)\)
be the same sum restricted to \(j\le M_N\).
There are no added or deleted outgoing rows in (2)--(3).

Use the continuous original product integral
\[
 I_a(s)=\int_0^s\log|1-Xe^{-2\pi iu}|\,du,\qquad J(s)=\Re g(s),
 \tag{4}
\]
and define the real-seam row rate
\[
 E_\eta^0(s;a)=
 I_a(s)-2J(s)-2\pi hs+\pi\Im y-\frac{\eta}{2}\Re g(a),
                               \qquad 0\le s\le1.
 \tag{5}
\]
The logarithmic zeros are integrable. The uniform finite-product
bounds used in the
[coherent retained-rate theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md)
give, for every \(\tau>0\),
\[
 \begin{split}
 &|d_N(X)|^{\eta/2}|f_0(y)|
       \sum_{j\ge\lceil N/2\rceil}^{N-1}
                  \left|\frac{X^{-j}p_j(X)}{P_j^2}\right|\\
 &\hspace{12mm}\le C_\tau N^{b_\tau}
    \exp N\left\{\sup_{1/2\le s\le1}E_\eta^0(s;a)+\tau\right\}.
 \end{split}
 \tag{6}
\]
Here (2) has rate \(\pi\Im y\), and the finite incoming
halfweight has its established rate \(-\eta\Re g(a)/2\).
All polynomial factors and zeros are retained. In particular (6)
is a bound on the sum of absolute row values, rather than an
inference from a coherently canceled high-index sum.

## 2. The maximum occurs at the two ends of the high interval

**Lemma 1.**
\[
 E_\eta^0(s;a)\le
          \max\{E_\eta^0(1/2;a),E_\eta^0(1;a)\},
                                    \qquad 1/2\le s\le1.
 \tag{7}
\]

*Proof.* Away from an incoming polynomial zero, differentiation
of (5) gives
\[
 (E_\eta^0)'(s)=
   \log\frac{|X^{-1}-e^{-2\pi is}|}{|1-e^{-2\pi is}|^2}.
 \tag{8}
\]
It holds almost everywhere, and the rate is absolutely continuous
across the integrable zeros.
The inherited height bounds give \(|X^{-1}|<2\): indeed
\(\log2>56/81>.216(22/7)>.216\pi\).

On \(1/2\le s\le2/3\), the numerator in (8) is strictly below
three and the denominator is at least three. On
\(2/3\le s\le3/4\), put \(t=1-s\).
The angle of \(X^{-1}\) is in \([.44\pi,.9\pi]\), and
that of \(e^{-2\pi is}=e^{2\pi it}\) is in
\([\pi/2,2\pi/3]\). Their difference has absolute value at
most \(2\pi/5\). Convexity of squared distance in
\(|X^{-1}|\in[0,2]\) gives
\[
 |X^{-1}-e^{2\pi it}|^2\le6-\sqrt5<4,\qquad
                       |1-e^{2\pi it}|^2\ge2.
 \tag{9}
\]
Thus (8) is strictly negative throughout \([1/2,3/4]\),
with a negative logarithmic divergence allowed at a zero.

For the remaining interval define
\[
 G(t)=E_\eta^0(1-t;a),\qquad
 D_a(t)=|1-X^{-1}e^{-2\pi it}|,\qquad 0\le t\le1/4.
 \tag{10}
\]
Then
\[
 G'(t)=2\log(2\sin\pi t)-\log D_a(t).
 \tag{11}
\]
For \(0<t<\min(x,1/4)\), the angle
\(2\pi(x-t)\) is in \((0,.9\pi)\), so \(D_a'(t)\le0\).
It follows that
\[
                  G''(t)=2\pi\cot\pi t-(\log D_a)'(t)>0.
 \tag{12}
\]
If \(x<t\le1/4\), then \(x\ge.22\) and
\(|2\pi(x-t)|\le.06\pi\). The exact elementary bounds in the
[Wall-rate convexity theorem](research_mixed_fourier_right_cap_wall_rate_convexity.md)
give
\[
 D_a(t)^2\le\max\{1,5-4\cos(.06\pi)\}<(6/5)^2,\qquad
 4\sin^2\pi t>4\sin^2(\pi/5)>4/3 .
 \tag{13}
\]
Consequently \(G'(t)>\log(10/9)>0\) there.
If \(x\ge1/4\), convexity alone puts the maximum of \(G\)
at an endpoint. If \(x<1/4\), convexity on \([0,x]\)
and increase on \([x,1/4]\) give the same conclusion.
When \(h=0,t=x\), the derivative has a positive integrable
divergence; continuity gives the same conclusion at the crossing.
Thus the maximum on \(3/4\le s\le1\) is attained at
\(s=3/4\) or \(s=1\). The strict decrease already proved on
\([1/2,3/4]\) establishes (7). \(\square\)

## 3. Both endpoint rates are already paid

The completed original Wall action is
\[
 \Phi(s;y)=g(s)-\pi iy+I_{\rm W}(1-s,Y),\qquad
 \Re I_{\rm W}(1/2,Y)=\int_0^{1/2}\log|R(t,0,Y)|\,dt>0.
 \tag{14}
\]
The last sign follows from the proved exterior degree root,
not from a positivity assumption about the finite quantum sum.
Since \(J(1/2)=0\), the original coherent retained rate satisfies
\[
       E_\eta^0(1/2;a)
       =\mathcal E_\eta(1/2;a)-\Re I_{\rm W}(1/2,Y)
       <B_\eta(x)-1/35000.
 \tag{15}
\]
The last inequality is the
[proved coherent half-index comparison](research_mixed_fourier_right_cap_coherent_high_tail_payment.md),
equation (18). Its normalization matches (5) exactly.
Only that established action inequality is used; it is not
converted into a termwise estimate for arbitrary outgoing rows.

At the other end, the elementary circle mean gives
\(I_a(1)=\log_+|X|\), while \(J(1)=0\). Therefore
\[
 E_\eta^0(1;a)=
 2\pi(-h)_++\pi\Im y-\frac{\eta}{2}\Re g(a)
       <B_\eta(x)-387/70000.
 \tag{16}
\]
This is precisely the original rate in the
[endpoint-payment theorem](research_mixed_fourier_right_cap_endpoint_payment.md).
No physical-to-critical-height substitution occurs.

Combining (7), (15), and (16) proves
\[
                   E_\eta^0(s;a)<B_\eta(x)-1/35000,
                                        \qquad 1/2\le s\le1.
 \tag{17}
\]
Insert this in (6), choose a fixed tolerance smaller than
\(1/70000\), and absorb the uniform polynomial factor.
For all sufficiently large \(N\), both parities, uniformly on (1),
\[
 \boxed{
 \begin{split}
 &|d_N(X)|^{\eta/2}|f_0(y)|
    \sum_{j\ge\lceil N/2\rceil}^{N-1}
                   \left|\frac{X^{-j}p_j(X)}{P_j^2}\right|
       \le e^{N(B_\eta(x)-1/70000)},\\
 &|d_N(X)|^{\eta/2}|f_0(y)|
       |C_{1,N}(X,1)-C_N^<(X,1)|
       \le e^{N(B_\eta(x)-1/70000)} .
 \end{split}}
 \tag{18}
\]
The second line follows from the exact difference of (3) and its
truncation. The cardinal coefficient and incoming weight have not
been divided out, so their zeros and exact finite normalizations
are preserved.

This is a physical \(q=0\) theorem. It does not replace a half-grid
vertical function by its endpoint value, bound the remaining
central \(C_{1,N}(X,1)\), or control the compact outgoing
boundary current. It supplies a paid correction for any future
argument that genuinely controls that same coherent endpoint.
