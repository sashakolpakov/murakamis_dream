# Absolute end-strip bounds for the actual merged pair

Research deduction, 7 November 2026. The complete Fourier-ended
power-two pair admits fixed physical-index end strips with a strict
exponential loss at its own critical action. The proof retains both
complex boundary products and the exact triangular support. It uses
no numerical evaluation and does not assert a bound on the remaining
compact interior or on the diagonal support boundary.

## 1. The literal rows and their continuous absolute rate

Use the exact source in
[the merged-pair theorem](research_mixed_two_adjacent_merged_source.md),
equation (14):
\[
 V_{22,N}(x,y)=e^{\pi i(N-1)(x+y)}
 \sum_{j+k<N}
 \frac{r^{-jk}P_{j+k}p_j(X)p_k(W)}{P_j^2P_k^2},
 \quad X=e^{-2\pi ix},\ W=e^{-2\pi iy}.
 \tag{1}
\]
Here \(P_j=(r;r)_j\), \(p_j(X)=(rX;r)_j\), and
\(r=e^{-2\pi i/N}\). The summands with \(j+k\ge N\)
in the original full-square extension vanish exactly. They will not
be replaced by a continuation of a positive rate.

Initially set \(x=y=x_0=\xi+i\upsilon\), where
\[
 .18299<\xi<.18301,\qquad .07871<\upsilon<.07873.
 \tag{2}
\]
These are the unchanged original output bounds in
[the real-input action comparison](research_mixed_three_real_input_action_gap.md),
equation (1). Put
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du\quad(0\le t\le1),
 \qquad
 L_z(t)=\int_0^t\log|1-e^{-2\pi iz}e^{-2\pi iu}|\,du.
 \tag{3}
\]
For \(\Im z>0\), the latter integrand is smooth, including at
\(t=0,1\). The original uniform factorial estimate gives
\(\log|P_j|=NJ(j/N)+O(\log N)\), uniformly for
\(0\le j<N\); see
[the full physical-tail estimate](research_adjacent_two_crossing_global_tails.md),
Section 2. An ordinary bounded-derivative Riemann-sum estimate gives
\[
 \log|p_j(e^{-2\pi iz})|=NL_z(j/N)+O(1)
 \tag{4}
\]
uniformly in the same complete range and in compact positive-height
parameter families. Thus every supported row of (1), including its
outside factor, has absolute value at most a fixed power of \(N\)
times \(e^{N\mathcal E_{x,y}(a,s)}\), where
\[
\begin{split}
 \mathcal E_{x,y}(a,s)={}&J(a+s)-2J(a)-2J(s)\\
 &+L_x(a)+L_y(s)-\pi\Im(x+y),\qquad
 a,s\ge0,\quad a+s\le1.
\end{split}
 \tag{5}
\]
This is continuous on the closed triangle, jointly with the
parameters under consideration. No sign is assigned to the original
complex rows.

## 2. A lower bound for the pair's own critical action

Write \(a_*=s_*\) for the critical point proved in
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md),
and let
\[
 M_{22}=\Re\{F(a_*,a_*;x_0,x_0)+2\pi ix_0\},
 \quad
 \frac13<\Re a_*<\frac5{12},\quad
 0<h_*:=\Im a_*<\frac{\operatorname{atanh}(1/4)}\pi.
 \tag{6}
\]
All phase constants are those of the literal source (1).

**Lemma 1.** The original critical action satisfies
\[
       M_{22}>\frac{187049}{504000}>\frac9{25}.
 \tag{7}
\]

*Proof.* Set \(t=3/8\). The strict horizontal concavity of the
whole corridor implies
\[
 \Re F(a_*,a_*;x_0,x_0)
       \ge\Re F(t+ih_*,t+ih_*;x_0,x_0).
 \tag{8}
\]
The same Hessian theorem makes
\(H\mapsto\Re F(t+iH,t+iH;x_0,x_0)\) convex. At \(H=0\),
the original logarithmic arguments give
\[
 \Im F_a(t,t;x_0,x_0)
  =\frac\pi4+\Im g'(t+x_0)
  <\pi(t-\xi).
 \tag{9}
\]
Indeed \(1/2<t+\xi<1\), and the argument of
\(1-Re^{-2\pi i(t+\xi)}\) decreases for \(R\ge1\).
The two equal internal derivatives therefore give the tangent bound
\[
 \Re F(t+ih_*,t+ih_*;x_0,x_0)
 >\Re F(t,t;x_0,x_0)-2(t-\xi)\operatorname{atanh}(1/4).
 \tag{10}
\]

For the outgoing height, the arguments at \(\xi+iH\) and
\(t+\xi+iH\) respectively increase and decrease as \(H\)
increases from zero. Their difference at zero is \(\pi t\).
Consequently
\[
 \frac d{dH}\{2\Re g(t+\xi+iH)-2\Re g(\xi+iH)\}
      \ge2\pi t=\frac{3\pi}4.
 \tag{11}
\]
Combining (8)--(11), and retaining the outside rate
\(-2\pi\upsilon\), yields
\[
 M_{22}>B-\frac{5\pi}4\upsilon
                   -2(t-\xi)\operatorname{atanh}(1/4),
 \quad
 B=J(3/4)-4J(3/8)+2J(3/8+\xi)-2J(\xi).
 \tag{12}
\]

Here are elementary lower bounds for all four real terms. Let
\(f(u)=\log(2\sin\pi u)\). Its second derivative is negative
on \((0,1)\), so its integral is at least the trapezoid formed
by any two endpoint values. The familiar positive-series witnesses
give \(69/100<\log2<7/10\). Also
\[
 f(3/8)>3/5,\qquad f(1/5)>3/20,\qquad
 f(u)>2/3\quad(1/2\le u\le3/8+\xi).
 \tag{13}
\]
For completeness, \(2\sin(3\pi/8)=\sqrt{2+\sqrt2}>11/6\),
whereas
\(e^{3/5}\le1+3/5+(3/5)^2/[2(1-(3/5)/3)]
=73/40<11/6\).
The pentagon identity gives \(2\sin(\pi/5)>7/6\), since
\(\sqrt5<41/18\); and \(\log(7/6)>2/13>3/20\).
For the last bound, \(0\le u-1/2<3/50\), so
\(2\cos\pi(u-1/2)>2-(19/100)^2>49/25\).
The same exponential-series majorant gives
\(e^{2/3}\le41/21<49/25\). These prove (13).

Using \(J(1-u)=-J(u)\), \(J(1/2)=0\), and
\(1/6<\xi<1/5\), the trapezoid bounds now give
\[
\begin{split}
 J(3/4)&>207/1600,\\
 -4J(3/8)&>129/400,\\
 2J(3/8+\xi)&>19/250,\\
 -2J(\xi)&>63/250.
\end{split}
 \tag{14}
\]
For the third inequality use \(\xi>182/1000\); for the last
retain just the positive integral from \(1/5\) to \(1/2\).
Thus \(B>6239/8000\). Finally,
\[
 \frac{5\pi}4\upsilon<\frac{869}{2800},\qquad
 2(t-\xi)<\frac{77}{200},\qquad
 \operatorname{atanh}(1/4)
 <\frac14+\frac{(1/4)^3}{3(1-(1/4)^2)}=\frac{23}{90}.
 \tag{15}
\]
The middle inequality uses \(\xi>73/400\).
Substitution in (12) gives
\[
 \frac{6239}{8000}-\frac{869}{2800}-\frac{1771}{18000}
       =\frac{187049}{504000}
       =\frac9{25}+\frac{5609}{504000},
\]
as claimed. \(\square\)

## 3. The two physical end faces

Let \(c=-J(1/6)<1/6\); the last strict inequality follows by
\(\sin\pi u>3u\) on \((0,1/6)\), as in the same
[physical-tail source](research_adjacent_two_crossing_global_tails.md),
Section 3. Extend \(J\) periodically for the following single
real-product identity only.

For \(h>0\), put
\[
 L_h(s)=\int_0^s\log|1-e^{2\pi h}e^{-2\pi i(\xi+u)}|\,du.
\]
Its height derivative is nonnegative and its integral over the full
period is exactly \(2\pi\): explicitly its integrand is
\[
 \partial_h\log|1-Re^{-2\pi i(\xi+u)}|
       =\pi\left(1+\frac{R^2-1}{|1-Re^{-2\pi i(\xi+u)}|^2}\right),
 \quad R=e^{2\pi h}>1.
 \tag{16}
\]
The second term is the Poisson kernel of the exterior circle.
Therefore \(0\le\partial_hL_h(s)\le2\pi\) for
\(0\le s\le1\). Taking the integrable logarithmic limit at
\(h=0\) gives
\[
 L_{x_0}(s)\le J(s+\xi)-J(\xi)+2\pi\upsilon.
 \tag{17}
\]
This step covers the moving sine zero at \(s+\xi=1\);
it does not use a regular-strip symbol at that zero.

At \(a=0\), (5) and (17) imply
\[
 \mathcal E_{x_0,x_0}(0,s)
       \le J(s+\xi)-J(s)-J(\xi).
 \tag{18}
\]
On \(0\le s\le1-\xi\), the right side has its unique
maximum at \(s=(1-\xi)/2\), since its derivative is the
logarithm of \(\sin\pi(s+\xi)/\sin\pi s\). The maximum is
\[
 -2J((1-\xi)/2)-J(\xi)
       \le\xi\log2+c.
 \tag{19}
\]
On \(1-\xi\le s\le1\), the periodic term
\(J(s+\xi)\le0\), whereas \(J(s)\ge0\), so the same upper
bound holds. By (2),
\[
 \sup_{0\le s\le1}\mathcal E_{x_0,x_0}(0,s)
       <\frac{23}{125}\frac7{10}+\frac16
       =\frac{1108}{3750}<\frac3{10}.
 \tag{20}
\]
At the other outer endpoint, the supported triangle contains only
\((a,s)=(1,0)\). Jensen's circle identity gives
\(L_{x_0}(1)=\log|X|=2\pi\upsilon\); hence
\[
                         \mathcal E_{x_0,x_0}(1,0)=0.
 \tag{21}
\]
Both conclusions also hold with \(a,s\) interchanged.

## 4. A complete finite-source tail bound

**Theorem 2.** There is a fixed \(\epsilon\in(0,1/12)\)
such that the sum of the absolute values of all original rows in
(1) with
\[
 j/N\notin[\epsilon,1-\epsilon]
 \tag{22}
\]
is at most
\[
               C N^A e^{N(M_{22}-1/25)}.
 \tag{23}
\]
The same assertion holds for the union of (22) with its second-index
counterpart. It holds along both parities and includes every endpoint
row. The statement is stable on a sufficiently small fixed complex
neighborhood of \((x_0,x_0)\), with the corresponding continued
critical action, after decreasing the gap to \(1/50\).

*Proof.* The closed supported triangle is compact. Its continuous
rate (5), together with (20)--(21), permits choosing a positive
\(\epsilon<1/12\) for which the rate on either end strip, in
either index, is less than \(8/25\). Lemma 1 gives
\(8/25<M_{22}-1/25\). Apply the uniform finite bounds
(4)--(5) and sum at most \(N^2\) rows. All supported factorial
denominators are nonzero. Rows outside the triangle remain their
exact original zeros; overlapping strips are counted once.
The parameters and the continued critical action are continuous,
and the product estimates are uniform in a small positive-height
parameter neighborhood. A smaller neighborhood therefore retains
gap \(1/50\). \(\square\)

Equivalently, the outer-index tail of the exact coherent sum
\(\sum_j[p_j(X)/P_j]C_{0,N}(r^j,W)\) is controlled by (23),
because its physical support and all its internal rows are exactly
those already bounded above. No positivity of its weights is used.
This does not place \(\epsilon\) at either endpoint of
\([.267,.433]\), extend the one-block packet to the complex pair
saddle, or pay the remaining diagonal support boundary. It removes
only fixed physical end strips before any subsequent contour
deformation. All retained currents and the prescribed closing
observation still require their own estimates.
