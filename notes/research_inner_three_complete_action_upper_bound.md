# A rational upper bound for the original complete three-crossing action

Private written source estimate, 8 November 2026. The original complete
inner action satisfies
\[
                  \mathfrak M_3=\Re S_3(0,0)<\frac{121}{63}.
 \tag{1}
\]
This is an upper bound for the calibrated action of the full original
inner source. It is not a bound for that source on a new complex
contour. No numerical evaluation, saved-value arithmetic, or frozen
source edit is used.

## 1. Original phase and the actual height

Keep the original edge phase and complete inner action from
[the horizontal phase theorem, equations (2)--(5)](research_mixed_next_inner_three_horizontal_concavity.md):
\[
\begin{split}
 \psi_t(t,0)&=-\pi^{-1}\operatorname{arsinh}\tan(t/2),\\
 \psi(0,0)&=-8J(1/4)=2b_2,\\
 \Phi(t,0)&=2\psi(t,0)+\frac{3it^2}{4\pi}-it,\\
 S_3(0,0)&=\Phi(t_3,0),\qquad t_3=a_3-iH_3 .
\end{split}
 \tag{2}
\]
The phase is holomorphic on a neighborhood of
\(0\le\Re t\le\pi/2,\ -1\le\Im t\le0\), on the original
principal-return branch. This is the closed primitive with the
original additive constant established in
[the endpoint theorem, Lemma 1](research_mixed_next_shortened_edge_endpoint_gap.md).
In particular (2) makes no change of logarithmic charge.

The adopted
[cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
gives \(0<a_3<\pi/2\), \(0<H_3<1\), and
\[
 v_3=2\cos(t_3/2)=x+ib,\qquad
 x>\frac32,\qquad \frac13<b<\frac23,\qquad
 v_3^3-2iv_3^2-3v_3+2i-2=0.
 \tag{3}
\]
These are proved inequalities at the original selected root;
no saved root enclosure is evaluated here.

The imaginary part of the last equation is
\[
 F_x(b):=(3b-2)x^2-b^3+2b^2-3b+2=0.
 \tag{3a}
\]
For fixed \(x>3/2\), this function increases on
\([1/3,2/3]\): its derivative is
\(3x^2-3b^2+4b-3>0\). But
\(F_x(1/2)=-x^2/2+7/8<-1/4\).
Thus the actual root has \(b>1/2\).

These facts imply the additional height bound
\[
                            \frac23<H_3<1.
 \tag{4}
\]
Indeed
\[
 b=2\sin(a_3/2)\sinh(H_3/2)<\sqrt2\,\sinh(H_3/2).
 \tag{5}
\]
If \(H_3\le2/3\), the positive series for the hyperbolic sine
and its successive term ratios give
\[
 \sinh(1/3)
   <\frac{1/3}{1-1/54}=\frac{18}{53},\qquad
 \sqrt2<\frac{10}{7}.
 \tag{6}
\]
The ratios are at most \(1/54\), with a strict decrease after
the first. Thus (5) would imply
\[
             b<\frac{180}{371}<\frac12,
 \tag{7}
\]
contrary to \(b>1/2\). This proves (4).

## 2. A uniform bound on the original horizontal action

We first record a bound valid on the entire rectangle in
Section 1. On the original branch,
\[
                \psi_{tt}(t,0)=-\frac1{2\pi\cos(t/2)}.
 \tag{8}
\]
It follows by differentiating (2). The square root in that
derivative is \(\sec(t/2)\), continued from \(t=0\);
the real part of \(\cos(t/2)\) is positive on the rectangle.

For \(t=a-iH\), \(0\le a\le\pi/2\), \(0\le H\le1\), one has
\[
                  \Re\sec(t/2)>\frac78 .
 \tag{9}
\]
Here is an elementary uniform witness. The positive series gives
\[
 \cosh(1/2)
   <1+\frac{1/8}{1-1/48}
   =\frac{53}{47}<\frac87.
 \tag{10}
\]
Put \(c=\cos(a/2)\), \(s=\sinh(H/2)\), and
\(C=\cosh(H/2)\). Then \(c^2\ge1/2\) and
\(s^2<15/49<1/2\), by (10), while
\[
                \Re\sec(t/2)=\frac{cC}{c^2+s^2}.
 \tag{11}
\]
For fixed \(H\) this expression decreases as \(c\) increases,
since its derivative has the sign of \(s^2-c^2<0\).
Its minimum for the allowed \(c\) is therefore \(1/C>7/8\),
proving (9).

On the imaginary axis the same original branch satisfies
\[
 \operatorname{arsinh}(-i\tanh(H/2))
                    =-i\arcsin(\tanh(H/2)).
 \tag{12}
\]
Moreover
\[
 \arcsin(\tanh s)=\arctan(\sinh s)\le s
                  \qquad(s\ge0),
 \tag{13}
\]
because the last function has derivative \(\operatorname{sech}s\le1\)
and vanishes at zero. Equations (2),(12)--(13) consequently give
\[
 2\Re\psi(-iH,0)
  =4b_2+\frac2\pi\int_0^H
                       \arcsin(\tanh(s/2))\,ds
  \le4b_2+\frac{H^2}{2\pi}.
 \tag{14}
\]

At \(a=0\), \(\Re\psi_t(-iH,0)=0\). Integrating the real
second-derivative bound (8)--(9) horizontally twice gives
\[
 2\Re\psi(a-iH,0)
       \le4b_2+\frac{H^2}{2\pi}-\frac{7a^2}{16\pi}.
 \tag{15}
\]
The two other terms in the exact phase (2) have real part
\(3aH/(2\pi)-H\). Completing the square therefore gives
\[
\begin{split}
 \Re\Phi(a-iH,0)
 &\le4b_2-H+\frac{H^2}{2\pi}
                    -\frac{7a^2}{16\pi}+\frac{3aH}{2\pi}\\
 &\le4b_2-H+\frac{25H^2}{14\pi}.
\end{split}
 \tag{16}
\]
The last maximization allows all real \(a\), so it remains valid
on the stated rectangle.

## 3. Evaluation at the selected source point

The original elementary bound
\[
                              b_2<\frac7{12}
 \tag{17}
\]
is recorded, with a stronger written rational witness, in
[the low-index kernel margin](research_mixed_next_low_index_kernel_margin.md).
Using (17) and the elementary rational bound \(\pi>25/8\)
in (16) gives, at the actual point from (4),
\[
 \mathfrak M_3<
                    \frac73-H_3+\frac47 H_3^2.
 \tag{18}
\]
The quadratic is convex. Its maximum on \([2/3,1]\) occurs
at an endpoint, where its values are respectively
\[
              \frac{121}{63},\qquad
              \frac{40}{21}=\frac{120}{63}.
 \tag{19}
\]
This proves (1) with its original action normalization.

The full degree-two source theorem
[Theorem 1](research_all_nonzero_degree_two_fillings.md)
identifies this same action with the complete kernel
\[
 Q_N^{\rm full}(-2\cos u)
   =P_{3,N}(0,u)
   =C_{N,3}N^{-3/2}A_3(0,u)e^{NS_3(0,u)}
                              (1+O(N^{-1}))
 \tag{20}
\]
on a fixed complex neighborhood of \(u=0\), with a holomorphic
normalized remainder and nonzero amplitude. Thus (1) concerns
the complete original source, including both parities and its
normal data, rather than a formal isolated stationary action.

The neighborhood in (20) has not been enlarged here. In
particular no bound for the full kernel at \(|\Im u|=1\),
no transport of the central-layer boundary response, and no
exponential estimate for the remaining coherent outer layer
follows from (1). The new conclusion is the quantitative upper
budget for that contour problem.
