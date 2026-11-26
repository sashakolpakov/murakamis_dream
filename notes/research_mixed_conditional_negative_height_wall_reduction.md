# Exact reduction of the displaced conditional wall rows

Research deduction, 7 November 2026. On the full negative incoming
rectangle, the original physical conditional rate decreases strictly
from its incoming numerator wall to one half. The whole remaining
wall-row group therefore reduces to the single wall rate, with a
geometric row-distance factor. The difference between the actual
critical action and this wall rate decreases as the incoming height
moves downward.

Neither assertion pays the wall. In particular the common critical
action floor cannot replace the correlated wall-action comparison.
No numerical evaluation or replay is used.

## 1. Literal source and wall rate

Keep the exact source and domains of
[the upper-half theorem](research_mixed_conditional_negative_height_upper_half.md):
\[
 \begin{gathered}
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 a=x-i\eta,\quad \frac12\le x\le\frac7{10},\quad
                         0\le\eta\le\frac9{125},\\
 y=z+iH,\quad \frac{11}{50}\le z\le\frac9{20},\quad
                                  0\le H\le\frac1{100},\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 T=e^{2\pi\eta},\quad \rho=T^{-1},\quad R=e^{2\pi H},
 \quad v_0=1-x .
 \end{gathered}                                                    \tag{1}
\]
The original phase and selected critical action are
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\qquad
                         \Theta(a,y)=Q(t_*(a,y);a,y).
 \tag{2}
\]
The original logarithmic lift and prewall branch on (1) are proved in
[the negative-height branch theorem](research_mixed_conditional_negative_height_branch.md).

The zero-safe physical rate, including \(X^{-j}\), is
\[
 \mathcal R(t;a,y)=
  \int_0^t\log|T-e^{-2\pi i(x+s)}|\,ds
  +\int_0^t\log|1-Re^{-2\pi i(z+s)}|\,ds-3J(t).
 \tag{3}
\]
It agrees with the rate used in the complete upper-half and
[lower-current theorems](research_mixed_conditional_negative_height_lower_currents.md).
The incoming carrier has been absorbed exactly into the first
integrand, not discarded.

Define the wall value
\[
 \begin{split}
 \mathcal W(x,\eta,y)&=\mathcal R(v_0;x-i\eta,y)\\
 &=G_\rho(v_0)+
       \int_0^{v_0}\log|1-Re^{-2\pi i(z+s)}|\,ds
                   -3J(v_0)+2\pi\eta v_0,\\
 G_\rho(v)&=\int_0^v\log|1-\rho e^{-2\pi is}|\,ds .
 \end{split}                                                     \tag{4}
\]
The second equality follows from reflection of the incoming
complementary arc. All zero values use the continuous integrated
logarithm. This is the original wall rate, with no new scalar
normalization.

## 2. Every wall-to-half row decreases from the wall

**Theorem 1.** Uniformly on (1), the continuous rate obeys
\[
 \mathcal R(t;a,y)\le
  \mathcal W(x,\eta,y)-\log(8/7)(t-v_0),
                         \qquad v_0\le t\le1/2.
 \tag{5}
\]
Where its derivative is finite,
\[
                      e^{\partial_t\mathcal R}
                              <\frac{875}{1024}<\frac78.
 \tag{6}
\]

*Proof.* The lower-current theorem proves \(1\le T<8/5\) on
the full incoming-height range. For \(v_0\le t\le1/2\),
\[
 1\le x+t\le6/5,\qquad
 \cos(2\pi(x+t))\ge\cos(2\pi/5)>\frac3{10}.
 \tag{7}
\]
The last bound is the exact pentagon value and
\(\sqrt5>11/5\). Since \(T^2+1-2Tc\) increases in \(T\ge1\)
for \(c\le1\), it follows that
\[
 |T-e^{-2\pi i(x+t)}|^2
     <\frac{64}{25}+1-\frac{24}{25}
                   =\frac{13}{5}<\frac{25}{9}.
 \tag{8}
\]
The outgoing numerator satisfies the original elementary bound
\[
 |1-Re^{-2\pi i(z+t)}|\le1+R
                     <\frac{339}{164}<\frac{21}{10}.
 \tag{9}
\]
Also \(3/10\le v_0\le t\le1/2\), so
\[
                 2\sin\pi t\ge2\sin(3\pi/10)
                              =\frac{1+\sqrt5}{2}>\frac85.
 \tag{10}
\]
Differentiating (3) therefore gives
\[
 e^{\partial_t\mathcal R}
  =\frac{|T-e^{-2\pi i(x+t)}|\,
                |1-Re^{-2\pi i(z+t)}|}
                           {(2\sin\pi t)^3}
 <\frac{(5/3)(21/10)}{(8/5)^3}
                        =\frac{875}{1024}<\frac78.
 \tag{11}
\]
At \(\eta=0,t=v_0\), the incoming numerator may vanish.
Its logarithm is integrable and the rate is continuous there.
Integrating (11) from that endpoint proves (5); alternatively
take the limit from \(\eta>0\). When \(x=1/2\), the interval
has one point and (5) is its equality statement. \(\square\)

For every sufficiently small fixed \(\tau>0\), the uniform
zero-safe finite-product bound consequently gives
\[
 \begin{split}
 &\sum_{\substack{0\le j<N\\v_0\le j/N<1/2}}
       \left|X^{-j}p_j(X)p_j(Y)/P_j^3\right|\\
 &\qquad\le C_\tau N^{B_\tau}
          e^{N\{\mathcal W(x,\eta,y)+\tau\}}
          \sum_{j\ge\lceil Nv_0\rceil}
                  e^{-\log(8/7)(j-Nv_0)}
 \le8C_\tau N^{B_\tau}e^{N\{\mathcal W+\tau\}} .
 \end{split}                                                     \tag{12}
\]
The last infinite geometric sum only enlarges the finite positive
sum and has ratio \(7/8\). Both level parities, the integer
alignment of the wall, and every numerator zero are included.
Equation (12) also bounds any subset of the displayed rows.

Thus no interior real optimizer remains in this physical row group.
Equation (12) is not an estimate relative to the actual critical
action until \(\mathcal W\) has been compared with that action.

## 3. The correlated wall gap decreases toward the deepest face

Put
\[
 V=e^{2\pi it_*(a,y)},\qquad
 w_*=\frac{V-X}{1-X},\qquad
 \mathcal G(x,\eta,y)=\Re\Theta(x-i\eta,y)-\mathcal W(x,\eta,y).
 \tag{13}
\]
The height-action theorem proves the exact original derivative
\[
          \partial_\eta\Re\Theta(x-i\eta,y)=\Arg w_*,
                   \qquad 0<\Arg w_*<\pi.
 \tag{14}
\]
The prewall branch satisfies
\[
                  0<\arg V<\arg X=2\pi(1-x)\le\pi .
 \tag{15}
\]

For fixed \(x,y\) and \(\eta>0\), differentiating the integrated
wall rate (4), or the original phase at its real wall approached
from the left, gives
\[
 \partial_\eta\mathcal W
  =2\pi v_0-\Arg(1-X)
                     =\Arg\frac{X}{1-X}.
 \tag{16}
\]
For \(x>1/2\), the last argument is in \((0,\pi)\);
for \(x=1/2\), it is the value \(\pi\). This is the original
continuous argument: \(X\) lies in the upper left quadrant,
and \(1-X\) in the lower right quadrant. In particular no
integer logarithmic shift is released.

The quotient of the two derivative multipliers is
\[
                \frac{w_*}{X/(1-X)}=\frac VX-1.
 \tag{17}
\]
Its imaginary part is strictly negative by (15). The difference
of the two arguments in (14), (16) lies in \((-\pi,\pi)\)
(and in \((-\pi,0)\) when \(x=1/2\)). Equation (17) therefore
forces that difference to be negative. Hence
\[
 \boxed{\qquad
                \partial_\eta\mathcal G(x,\eta,y)<0
                               \quad(\eta>0).
 \qquad}                                                        \tag{18}
\]
The integrated rates and the selected phase are continuous at
\(\eta=0\). Integrating (18) proves that \(\mathcal G\)
strictly decreases on the entire allowed height interval.

In particular the worst wall gap, with the other parameters
held fixed, occurs at the prescribed deepest face
\(\eta=9/125\). This is a dimensional reduction of the remaining
comparison. Its sign on that face is not established here.
It also explains why the increase of the critical action alone
does not transport the old real-wall gap: the wall rate increases
strictly faster.

## 4. Exact remaining obligation and finite-source scope

The complete upper-half theorem already pays every row
\(j/N\ge1/2\) at the full incoming depth. Theorem 1 reduces the
remaining wrapped group \(1-x\le j/N<1/2\) to its exact wall
value. It neither discards the rows nor identifies them with
an incoming contour arc.

A uniform positive bound for the actual \(\mathcal G\) would,
by zero-safe continuity, also pay a fixed small regular collar
before the wall. Together with the already proved branch margins,
that would permit choosing a retained upper cut whose physical
complement and real endpoint have the same own-action gap.
The lower-current theorem then supplies the corresponding
upper vertical aliases and, by convexity, the upper unweighted
main join. The positive comparison for \(\mathcal G\) remains
unproved; no complete conditional packet follows from this note.

For fixed row subsets at a base parameter, the same finite
holomorphic sums and the continuous rates give the corresponding
ordinary mixed incoming/outgoing derivative upper bounds with an
arbitrarily small extra rate allowance. Hold the row sets and
integration paths fixed before using Cauchy's formula; do not
differentiate the moving wall cutoff. The original outer factor
\(N\) costs only a polynomial factor. There is no ordinary-color
variable or additional observation scalar in this conditional
source.

