# The transformed saddle height and the true right endpoint gap

Research deduction, 7 November 2026. For physical real incoming
arguments in the actual type-three interval, the transformed
critical height lies strictly between zero and the output height.
The literal last summation row has rate at least \(1/20\) below
the selected left action. The proof uses the original upper
reciprocal-factorial branch and retains its finite periodic factor.
No numerical evaluation is used.

These are the endpoint inputs to the complete contour analysis.
They do not alone estimate an entire vertical current or prove
a whole finite-sum asymptotic.

## 1. The transformed saddle lies below the output height

Fix
\[
 a=x\in[267/1000,433/1000],\qquad
 y=x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\quad .07871<\upsilon<.07873 .
 \tag{1}
\]
Retain the original cotangents and both conditional roots:
\[
 P=p=\cot\pi a,\quad Q=q-ib=\cot\pi y,\quad
 S_1=u-iv,\quad S_2=-P-Q-S_1.
 \tag{2}
\]
The proved elementary bounds in
[the real-input action gap](research_mixed_three_real_input_action_gap.md)
are
\[
 \frac9{50}<p<\frac9{10},\quad
 \frac{127}{100}<q<\frac{13}{10},\quad
 \frac{17}{25}<b<\frac{73}{100},\quad
 u>0,\quad0<v<\frac25 .
 \tag{3}
\]
In fact \(u<9/20\). Otherwise the real root equation would give
\[
\begin{split}
 0&=u^2-v^2+(p+q)u+b(1-v)-1\\
 &>\frac{81}{400}-\frac4{25}
        +\frac{29}{20}\frac9{20}
        +\frac{17}{25}\frac35-1
   =\frac{103}{1000}>0 ,
\end{split}
 \tag{4}
\]
a contradiction.

Let \(s_2\) be the original inverse cotangent of \(S_2\), and
\(z_2=s_2-1\). The accepted
[second-period packet](research_mixed_three_fourier_conditional_second_period_packet.md)
already proves
\[
 \Im s_2<0,\quad
 1<\Re(s_2+a),\Re(s_2+y)<3/2,\quad
 t_*=-z_2,\quad0<\Re t_*<\min(a,\xi).
 \tag{5}
\]
The exact root equation also gives the cotangent addition identity
\[
 \cot\pi(s_2+y)=
            i\,\frac{S_1+2Q-i}{S_1+i}.
 \tag{6}
\]
Its imaginary numerator, over the positive denominator
\(|S_1+i|^2\), is
\[
                  u^2+v^2+2qu+2bv-1-2b.
 \]
For \(v<1\) this expression decreases with \(b\).
Using (3)--(4), it is strictly smaller than
\[
 \frac{81}{400}+\frac4{25}
       +2\frac{13}{10}\frac9{20}
       +2\frac{17}{25}\frac25-1-\frac{34}{25}
                         =-\frac{567}{2000}<0 .
 \tag{7}
\]
Thus \(\Im(s_2+y)>0\), by the original cotangent formula.
Together with (5), this proves the strict compact height bound
\[
                    \boxed{\,0<h_*:=\Im t_*<\upsilon.\,}
 \tag{8}
\]
All inequalities persist on a sufficiently small fixed neighborhood
of this real incoming family. No independent incoming-height
enlargement is asserted.

## 2. The literal last-row rate

The exact transformed row from
[the left-contour theorem](research_mixed_three_left_cycle_left_contour.md)
has, at the true last index \(t=a=b/N\), the value
\[
 N e^{\pi iNa-\pi iNa^2-\pi ia}
                          E_N(a)^2E_N(y-a).
 \tag{9}
\]
Since \(\Re(y-a)<0\), its last factor is not evaluated by the
regular-strip expansion at a negative real argument. Instead use
the undivided original recurrence
\[
 E_N(y-a)=(1-e^{-2\pi iN(y-a)})E_N(1+y-a)
                         =(1-W^N)E_N(1+y-a),
 \quad W=e^{-2\pi iy}.
 \tag{10}
\]
The last equality uses the actual physical \(a=b/N\).
The shifted argument has real part strictly between zero and one.
On (1), \(|W|>1\), so the finite factor in (10) has its
ordinary exponentially accurate leading term \(-W^N\).
The upper branch is precisely
\[
                   g_+(y-a)=g(1+y-a)+2\pi i(y-a).
 \tag{11}
\]
Consequently the exponential rate of (9) is
\[
                     \mathcal E_R(a,y)
                         =-2J(a)-\Re g_+(y-a),
 \qquad J(x)=\Re g(x)\quad(0<x<1).
 \tag{12}
\]
No periodic zero is divided out in defining the finite source.

**Theorem 1.** Uniformly on (1),
\[
                   \boxed{\quad
       \Re\Phi_1(a,y)-\mathcal E_R(a,y)>\frac1{20}.
                   \quad}
 \tag{13}
\]
Here \(\Phi_1\) is the original, absolutely calibrated left action.

## 3. Reduce the comparison to two explicit real endpoints

Set \(s_0=3/8\), \(d=a-\xi>0\), and
\[
                   C(\xi)=J(3/8+\xi)-2J(3/8)-J(\xi).
 \tag{14}
\]
The fixed trial-index proof in
[the action-gap theorem](research_mixed_three_real_input_action_gap.md),
equations (8) and (14), gives
\[
 \Re\Phi_1>
     \Re\mathscr F(3/8;a,y)
          -d\,\operatorname{arctanh}(2/5).
 \tag{15}
\]
We keep that actual critical-action lower bound and compare it
directly with (12).

For \(0\le H\le\upsilon\), the original argument bounds imply
\[
\begin{split}
 \Im g'(3/8+\xi+iH)&<0,\\
 \Im g'(\xi+iH)&\ge\pi(1/2-\xi),\\
 \Im g'_+(-d+iH)&\le3\pi/2+\pi d .
\end{split}
 \tag{16}
\]
The second inequality follows by increasing the circle radius
from one at a real part below \(1/2\). For the last one, use
\(g'_+(-d+iH)=g'(1-d+iH)+2\pi i\); the regular argument at
real part \(1-d>1/2\) decreases with the radius.
Its real-height value is \(-\pi/2+\pi d\).
Thus
\[
 \frac d{dH}
 \{\Re g(3/8+\xi+iH)+\Re g_+(-d+iH)-\Re g(\xi+iH)\}
                                  >-\pi(1+a).
 \tag{17}
\]
The boundary value at \(H=0\) is taken on the original upper
branch; its real part satisfies \(J(1-d)=-J(d)\).
Combining (12), (15), and (17) gives
\[
 \Re\Phi_1-\mathcal E_R>
 \mathcal B(a,\xi)-\pi(1+a)\upsilon
                       -(a-\xi)\operatorname{arctanh}(2/5),
 \tag{18}
\]
where
\[
          \mathcal B(a,\xi)
          =-J(5/8-a)+J(a)-J(a-\xi)+C(\xi).
 \tag{19}
\]

For fixed \(\xi\), the right side of (18) is strictly concave
as a function of \(a\). Indeed the two losses are affine, and
\[
 \mathcal B_{aa}
   =\pi\{\cot\pi(3/8+a)+\cot\pi a-\cot\pi(a-\xi)\}<0.
 \tag{20}
\]
The first cotangent is negative, and \(0<a-\xi<a<1/2\)
makes the difference of the other two negative.
It is therefore enough to bound (18) at
\(a=267/1000\) and \(a=433/1000\).

## 4. Exact rational lower bounds at both endpoints

Write \(F(t)=-J(t)\) for \(0<t<1/2\).
The elementary sine-logarithm witnesses in Section 3 of
[the action-gap theorem](research_mixed_three_real_input_action_gap.md)
give
\[
\begin{gathered}
 C(\xi)>\frac3{80}+\frac4{25}+\frac{247}{1600}
                         =\frac{563}{1600},\\
 F(179/500)>\frac{1787}{20000},\qquad
 F(1/4)>\frac9{64},\qquad
 \log(2\sin\pi t)>\frac1{10}\quad(3/16\le t\le1/4).
\end{gathered}
 \tag{21}
\]
For the \(F(1/4)\) bound, the same two trapezoids on
\([1/4,3/8]\) and \([3/8,1/2]\), with endpoint logarithms
larger than \(17/50,61/100,69/100\), sum to \(9/64\).
We also use
\[
        \log2<\frac7{10},\quad \pi\upsilon<\frac14,\quad
                 \operatorname{arctanh}(2/5)<\frac37.
 \tag{22}
\]
The last two are already proved there. For the first,
\(1+7/10+(7/10)^2/2+(7/10)^3/6=12013/6000>2\)
is an explicit positive exponential-series witness.

At \(a=267/1000\), (1) gives \(83/1000<d<17/200\).
Since \(\sin\pi t<\pi t\),
\[
                     F(d)>d\{1-\log(2\pi d)\}.
 \]
The function on the right increases on this interval.
Moreover \(2\pi(83/1000)<53/100\), using \(\pi<22/7\), and
\[
              -\log(53/100)>
                    \frac{2(1-53/100)}{1+53/100}
                         =\frac{94}{153}>\frac35.
 \]
Consequently \(F(d)>664/5000\).
Also \(F(267/1000)<(233/1000)\log2<1631/10000\).
Equations (19)--(22) now give
\[
 \mathcal B(267/1000,\xi)>
   \frac{1787}{20000}-\frac{1631}{10000}
             +\frac{664}{5000}+\frac{563}{1600}
                         =\frac{16437}{40000}.
 \tag{23}
\]
The two losses in (18) are smaller than
\(1267/4000\) and \(51/1400\), respectively. Their subtraction
leaves
\[
 \frac{16437}{40000}-\frac{1267}{4000}-\frac{51}{1400}
                 =\frac1{20}+\frac{2169}{280000}.
 \tag{24}
\]

At \(a=433/1000\), one has \(249/1000<d<251/1000\).
The same bounds give
\[
\begin{split}
 F(24/125)&>\frac9{64}+\frac{29}{5000},\\
 F(d)&>\frac9{64}-\frac7{10000},\\
 F(433/1000)&<\frac{469}{10000}.
\end{split}
 \tag{25}
\]
The first inequality integrates the \(1/10\) bound in (21)
from \(24/125\) to \(1/4\); the second loses at most
\((1/1000)\log2\) beyond \(1/4\).
Thus
\[
 \mathcal B(433/1000,\xi)>
 \frac{563}{1600}+\frac9{32}
               +\frac{29}{5000}-\frac{476}{10000}
                         =\frac{23653}{40000}.
 \tag{26}
\]
The losses in (18) are smaller than \(1433/4000\) and
\(753/7000\). Their subtraction is
\[
 \frac{23653}{40000}-\frac{1433}{4000}-\frac{753}{7000}
                =\frac1{20}+\frac{21141}{280000}.
 \tag{27}
\]
Concavity (20), with (24) and (27), proves (13).

The strict compact reserve also survives on a smaller complex
neighborhood for the two holomorphic actions
\(\Phi_1\) and
\(\Theta_R=-2g(a)-g_+(y-a)+\pi i(a-a^2)\);
on real \(a\), \(\Re\Theta_R=\mathcal E_R\).
The first equality in (10) is the off-grid recurrence.
Its simplification to \(1-W^N\) remains restricted to
physical \(a=b/N\).
The purpose of (8) and (13) is to control the actual right
joining path and its complete endpoint current once their
profile comparisons have been proved.
