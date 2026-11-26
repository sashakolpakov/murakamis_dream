# Selected type-four heights: physical rows and the remaining complex strip

Research deduction, 5 November 2026. This note retains the actual selected
Fourier halfweight. It proves that physical transform rows with
\(i/N\ge3/20\) need no additional exponential allowance when an actual
negative type-four input height is replaced by a selected height.
For complex transform currents it isolates a remaining strip
\(3/20\le\Re t<21/100\). It does not claim a complete selected-terminal
bound or discard the original incoming imaginary tangent.

## 1. Allocated rates

Let
\[
 y\in[.22,.45],\quad -.108\le c\le-.001,\quad
 0\le h\le H=7/500,\quad a_k=y+ik.
 \tag{1}
\]
Use the original \(g\), with \(J(y)=\Re g(y)\). Define
\[
\begin{split}
 R(t;k)&=\int_0^t\log|1-e^{-2\pi i(a_k+s)}|\,ds-2\pi kt,\\
 G(k)&=\Re g(y+ik),\qquad q_0(c)=-G(c)/2,\\
 q_1(h)&=\max\{-G(h)/2-\pi h,\ 0\}.
\end{split}
 \tag{2}
\]
The last line is the true selected halfweight:
\(\tfrac12\max(-G(h),2\pi h)-\pi h\), including the forced Fourier
alternative. For \(k\le0\), \(G(k)<0\). For example, with
\(r=e^{2\pi k}\), its radial derivative is
\(-\arg(1-re^{-2\pi iy})/(2\pi r)<0\), and its value at \(r=0\)
is zero.

Put \(A(y,k)=\arg(1-e^{2\pi k-2\pi iy})\) on the original lift.
The [exact Poisson identities](research_mixed_four_first_vertical_source_transport.md)
give
\[
 \partial_kR(t;k)=
 \begin{cases}
 -\pi t-\pi\int_y^{y+t}P_{e^{2\pi k}}(s)\,ds,&k<0,\\
 -\pi t+\pi\int_y^{y+t}P_{e^{-2\pi k}}(s)\,ds,&k>0,
 \end{cases}
 \quad
 P_r(s)=\frac{1-r^2}{1+r^2-2r\cos2\pi s}.
 \tag{3}
\]
Each integral is between zero and one for \(0\le t\le1\), with
all wrapped rows retained. Also
\[
 0<A(y,k)\le\pi(1/2-y)\ (k\le0),\qquad
 0<A(y,k)<\pi(1-2y)\ (k\ge0).
 \tag{4}
\]
The exact reflection identities are
\[
 R(t;h)=R(t;-h)-2\pi ht,\qquad
 G(h)=G(-h)-2\pi h(1/2-y).
 \tag{5}
\]

## 2. A short Poisson-arc bound

For \(0\le k\le H\), \(r=e^{-2\pi k}>10/11\).
Indeed \(2\pi H<11/125<2/21<\log(11/10)\).
For \(r\in[10/11,1)\), the following uniform bounds hold:
\[
 \begin{array}{c|c}
 s\text{ interval}&P_r(s)\text{ upper bound}\\ \hline
 [.22,.8]&3/20\\
 [.8,.9]&1/2\\
 [.9,.95]&2.
 \end{array}
 \tag{6}
\]
To verify them, use respectively
\(\cos2\pi s<1/3,\ 81/100,\ 191/200\).
The last two follow from the upper cosine Taylor polynomial
\(1-x^2/2+x^4/24\), with \(\pi>157/50\), at \(x=\pi/5,\pi/10\).
The first follows from \(\cos(2\pi/5)<1/3\) and monotonicity.
For each displayed cosine ceiling \(q\), the function
\((1-r^2)/(1+r^2-2rq)\) decreases for \(r\ge10/11\):
its derivative has the sign of \(q(1+r^2)-2r<0\).
Substitution of \(r=10/11\) gives each strict rational bound in (6).

Consequently, for \(0<t\le1/2\),
\[
                    \int_y^{y+t}P_r(s)\,ds<t.
 \tag{7}
\]
For \(t\le.3\) the arc stays in \([.22,.75]\), and the first
bound in (6) suffices. For \(.3\le t\le.5\), it lies in
\([.22,.95]\), whose integral is less than
\(.58(3/20)+.1(1/2)+.05(2)=237/1000<.3\).
If \(1/2\le t\le1-y\), symmetry gives the further bound
\[
 \int_y^{y+t}P_r\le\int_y^1P_r
       =\frac12+\int_y^{1/2}P_r
       \le\frac12+\frac3{20}(1/2-y)\le\frac{271}{500}.
 \tag{8}
\]

## 3. Every physical row at or above the left cut

**Proposition 1.** On (1), for every \(3/20\le t\le1\),
\[
                  R(t;h)+q_1(h)\le R(t;c)+q_0(c).
 \tag{9}
\]

*Proof.* On the negative path,
\[
 \partial_k(R-G/2)\le\pi(1/4-y/2-t)\le-\pi/100<0.
 \tag{10}
\]
For the selected factorial branch at positive height, (3)--(4) give
\[
 \partial_k(R-G/2-\pi k)
       \le\pi\left\{\int_y^{y+t}P_r-t-\frac12-y\right\}.
 \tag{11}
\]
This is negative by (7) when \(t\le1/2\), and by the full-period
integral bound when \(t\ge1/2\). Thus the factorial alternative in
(9) is proved.

For the forced alternative the halfweight rate is zero. If \(t\le1/2\),
(7) and negative bare monotonicity give \(R(t;h)\le R(t;c)\).
For \(1/2\le t\le1-y\), (8) gives
\[
 R(t;h)-R(t;0)\le\frac{21\pi H}{500}<.002.
 \tag{12}
\]
The unselected rate at \(c\) is at least its value at zero by (10).
Its zero-height Fourier credit satisfies
\[
 -J(y)/2\ge-J(.45)/2>
 \frac1{40}\log(19/10)>\frac{2}{125}=.016.
 \tag{13}
\]
Here \(2\sin(.45\pi)>19/10\), and
\(\log(19/10)>2(9/29+(9/29)^3/3)>16/25\).
This pays (12).

It remains to consider \(t\ge1-y\). If \(c\le-h\), (5) and
negative bare monotonicity immediately give \(R(t;h)\le R(t;c)\).
If \(-h<c\), integrate (3) between \(-h\) and \(c\), using the
full-period mass one, to obtain
\[
 R(t;h)-R(t;c)\le\pi\{h(1-t)+c(1+t)\}.
 \tag{14}
\]
Furthermore
\(q_0(c)\ge-J(y)/2+\pi c(1/2-y)/2\).
Since the resulting right side decreases with \(t\), its maximum
on \(t\ge1-y\), \(c\le-.001\), \(h\le.014\) satisfies
\[
 R(t;h)-R(t;c)-q_0(c)
 \le\frac{191\pi}{40000}+\frac{J(.45)}2
 <\frac{191}{40000}\frac{22}{7}-\frac{2}{125}<0.
 \tag{15}
\]
This proves both alternatives. \(\square\)

For the exact external factor \(F_{i,N}(k)=X_k^{-i}p_i(X_k)\),
the zero-safe product estimate cited in
[the complete real-row proof](research_mixed_outer_cap_real_tails.md),
Section 1, gives the following uniform finite consequence. For every
\(\tau>0\), all sufficiently large levels of either parity satisfy
\[
 |F_{i,N}(h)|e^{Nq_1(h)}
       \le C_\tau N^{A_\tau}e^{N\tau}
                         |F_{i,N}(c)|e^{Nq_0(c)}
       \qquad(3N/20\le i<N).
 \tag{16}
\]
The lower comparison at \(c\) is harmless: \(c\le-.001\) keeps every
reference numerator factor uniformly away from zero, so its Riemann
estimate is two-sided. At \(h=0\), any new numerator zero only improves
the upper bound. The reference chirp and all wrapped factors remain.
The original Fourier theorem bounds the physical selected halfweight
by \(e^{N(q_1+\tau)}\) up to polynomial factors, so the total tolerance
can be chosen once.

Any coefficient independent of the incoming variable may multiply
(16), including a whole coherent Newton sum, a Newton contour
current with physical \(i\), or an ordinary-color derivative.
This does not replace an absolute sum by the modulus of a cancelling
sum over \(i\). It applies to parts of a proved decomposition for which
the physical outer rows were already bounded individually.

## 4. Complex transform currents: where a fee remains

For either terminal own type, its bare joint phase has incoming
marginal
\[
 \mathcal T_a=\log_{\mathrm R}(\cot\pi t+\cot\pi a)
                 -\log_{\mathrm R}(\cot\pi t-i).
 \tag{17}
\]
Keep \(t=v+i\eta\) in \([.15,.5]+i[-.12,.12]\) and all other
indices on their admitted fixed contours. For \(a=y+ik\) as in
(1), including \(c\le k\le h\), the
[fixed-index cotangent argument](research_mixed_terminal_three_height_transport.md)
applies with
\(\Re\cot\pi a<5/4\), \(\Im\cot\pi a>-.11\), and
\((\Im\cot\pi t-1)/\Re\cot\pi t<7/16\) when the numerator is
positive. Thus \(0<\Im\mathcal T_a<\pi\), with the continuous
original lift at \(v=.5\). In particular the bare phase decreases
as the incoming height increases.

For the slightly wider real interval here, the two incoming bounds
follow directly: \(\tan(.22\pi)>x+x^3/3>4/5\) at
\(x=1727/2500<.22\pi\). At positive height,
\(\sinh(2\pi k)<89/1000\) and
\(\cosh(2\pi k)-\cos(2\pi y)>142/175\), using
\(2\pi k<11/125\) and \(\cos(.44\pi)=\sin(.06\pi)<33/175\).
Their ratio is less than \(11/100\); negative heights are favorable.
Thus the ratio's imaginary numerator is positive because
\(1-.11>(5/4)(7/16)\), precisely as in the cited argument.

The allocated negative-height derivative is exactly
\[
 \partial_k\Re(\mathcal T-g(a)/2)
 =\frac32 A(y,k)-A(y+v,k+\eta)-2\pi v.
 \tag{18}
\]
If \(y+v<.5\), the middle argument is positive, so this is at most
\(\pi(3/4-3y/2-2v)\). If \(y+v\ge.5\), use
\(A(y+v,k+\eta)\ge-\pi(2y+2v-1)\); (18) is then at most
\(\pi(y/2-1/4)<0\).
The two selected branches both decrease on \(k\ge0\):
the factorial derivative is
\(-\Im\mathcal T_a+A(y,k)/2-\pi<0\), and the forced branch
is the bare phase. At zero the factorial branch dominates.

It follows, pointwise on every admitted fixed current, that
\[
 \Re\mathcal T(a_h;t,\ldots)+q_1(h)
 \le\Re\mathcal T(a_c;t,\ldots)+q_0(c)
       +\gamma_c(y,v),
 \quad
 \gamma_c(y,v)=\pi(-c)[3/4-3y/2-2v]_+.
 \tag{19}
\]
Alias penalties are unchanged. In particular \(\gamma_c=0\) whenever
\(v\ge21/100\); only the leftmost complex strip can incur this fee.
No assertion that its available source margin pays the fee is made.

Finally, if the horizontal baseline rate is bounded by an allocated
supporting plane \(B(y)\) and \(p\) is its original incoming complex
marginal, the full complex affine plane at height \(h\) is
\(B(y)-\Im p\,(h-c)\). Relative to that plane, (19) retains the fee
\[
                   \gamma_c(y,v)+\Im p\,(h-c).
 \tag{20}
\]
Equation (16) similarly retains the latter tangent fee even when its
additional transport cost is zero. These terms cannot be omitted
before the adjacent factor supplies its matching tangent or loss.
The low physical end sector and the leftmost complex strip remain
separate obligations for a complete selected-terminal source theorem.

