# Explicit critical-point guards at positive conditional height

Research deduction, 7 November 2026. On the full displaced incoming
rectangle, a conditional critical point of nonnegative height lies
strictly below real index \(3/10\), and at least \(3/40\) before
the incoming numerator wall. Both assertions follow from the original
force, including its incoming carrier, and the proved horizontal
concavity. No critical root or action is numerically evaluated.

These are bounds on the original critical branch. They do not assert
the still unresolved wall-action comparison or a complete finite-source
asymptotic on every positive-height parameter.

## 1. Original branch and force

Use the parameter set
\[
\begin{gathered}
a=x+ih_a,\qquad \frac12\le x\le\frac7{10},\qquad
                    -\frac9{125}\le h_a\le0,\\
y=z+iH,\qquad \frac{11}{50}\le z\le\frac9{20},\qquad
                    0\le H\le\frac1{100},\\
X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy}.
\end{gathered}                                                    \tag{1}
\]
The phase and its exact exponentiated derivative are
\[
\begin{split}
Q(s;a,y)&=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,\\
e^{Q_s}&=X^{-1}
       \frac{(1-Xe^{-2\pi is})(1-Ye^{-2\pi is})}
            {(1-e^{-2\pi is})^3}.
\end{split}                                                       \tag{2}
\]
The original primitive satisfies
\(g'(q)=\Log(1-e^{-2\pi iq})\) on \(0<\Re q<1\).
No logarithmic lift or additive constant is changed.

The
[negative-height branch theorem](research_mixed_conditional_negative_height_branch.md)
provides the simple selected point
\[
s_*=u_*+ih_*,\qquad Q_s(s_*;a,y)=0,\qquad
                      \frac1{16}<u_*<1-x.                       \tag{3}
\]
It also proves, at every fixed index height,
\[
\Re Q_{ss}(t+i\sigma;a,y)<0
       \quad\left(\frac3{50}\le t<1-x\right).                  \tag{4}
\]
We use (4) only on the original regular interval.

For an arbitrary index height \(\sigma\ge0\), put
\[
U=e^{2\pi\sigma}\ge1,\qquad
T=e^{-2\pi h_a},\qquad R_y=e^{2\pi H}.
\]
The
[full-depth lower-current proof, equations (7)--(9)](research_mixed_conditional_negative_height_lower_currents.md)
gives
\[
                  1\le T<\frac85,\qquad
                  1\le R_y<\frac{175}{164}.                    \tag{5}
\]
In particular the exact squared force at a real index \(t\) is
\[
|e^{Q_s(t+i\sigma;a,y)}|^2
=\frac{|T-Ue^{-2\pi i(x+t)}|^2
       |1-R_yUe^{-2\pi i(z+t)}|^2}
      {|1-Ue^{-2\pi it}|^6}.                                   \tag{6}
\]
The first numerator in (6) absorbs \(|X|^{-1}\) exactly.
It is not the unweighted incoming numerator.

## 2. A uniform upper index bound

**Lemma 1.** If \(h_*\ge0\), then
\[
                              u_*<\frac3{10}.                  \tag{7}
\]

*Proof.* For \(x<7/10\), the trial index \(t_0=3/10\)
is strictly inside the regular interval. At every
\(\sigma\ge0\),
\[
\cos(2\pi(x+t_0))\ge\cos(2\pi/5)>\frac3{10},
\qquad \cos(2\pi t_0)<-\frac3{10}.                             \tag{8}
\]
Indeed \(x+t_0\in[4/5,1)\), and
\(\cos(2\pi/5)=(\sqrt5-1)/4>3/10\).
Let
\[
                         D=1+U^2+\frac35U.
\]
The own squared modulus in (6) is greater than \(D\).
The incoming squared modulus is less than or equal to \(D\):
using (5),
\[
\begin{split}
D-\{T^2+U^2-(3/5)TU\}
   &=(1+T)\{1-T+(3/5)U\}>0.
\end{split}                                                       \tag{9}
\]
The outgoing modulus is also less than \(D\), since
\[
|1-R_yUe^{-2\pi i(z+t_0)}|
 \le1+R_yU<1+U^2+(3/5)U=D.                                    \tag{10}
\]
For the last step, \(U+3/5\ge8/5>175/164\).
Equations (6), (9), and (10) imply
\(|e^{Q_s(t_0+i\sigma)}|<1\), or
\(\Re Q_s(t_0+i\sigma)<0\).

At \(\sigma=h_*\), the real derivative is zero at \(u_*\)
and strictly decreases with the real index by (4).
Thus \(u_*<t_0\). If \(x=7/10\), (7) follows directly
from the already strict prewall bound \(u_*<1-x\) in (3);
no derivative is evaluated at a numerator zero. \(\square\)

## 3. A uniform distance from the incoming wall

**Lemma 2.** If \(h_*\ge0\), then
\[
             u_*<\frac{37}{40}-x,\qquad
                         1-x-u_*>\frac3{40}.                   \tag{11}
\]

*Proof.* Use the trial index
\[
b=\frac{37}{40}-x\in[9/40,17/40].
\]
It is always strictly inside the original chart, at real distance
\(3/40\) below the incoming wall. The angular guards are
\[
\cos(2\pi(x+b))=\cos(3\pi/20)>\frac78,\qquad
                    \cos(2\pi b)\le\sin(\pi/20)<\frac4{25}.
                                                                    \tag{12}
\]
For the first use \(3\pi/20<1/2\) and
\(\cos q\ge1-q^2/2\). The second follows from
\(\pi<22/7<16/5\) and \(\sin q<q\).

Put
\[
D=1+U^2-\frac8{25}U,\qquad
                   A=|T-Ue^{-2\pi i(x+b)}|^2.
\]
The own squared modulus in (6) is strictly greater than
\(D\). Also
\[
                         A\le D-\frac{23}{25}U.                \tag{13}
\]
To check (13), bound \(A\) by
\(T^2+U^2-(7/4)TU\), which is convex in \(T\).
At the two endpoints \(T=1,8/5\), the differences from \(D\)
are respectively
\[
\frac{143}{100}U,\qquad
                  \frac{62}{25}U-\frac{39}{25}
                                      \ge\frac{23}{25}U.
\]
Both dominate \(23U/25\), since \(U\ge1\). Convexity
proves the same bound throughout (5).

For the outgoing factor,
\[
|1-R_yUe^{-2\pi i(z+b)}|
    \le1+R_yU\le(1+R_y)U<\frac{21}{10}U,                        \tag{14}
\]
using \(1+175/164=339/164<21/10\).
Write \(d=D/U=U+U^{-1}-8/25\ge42/25\).
Equations (6), (13), and (14) give
\[
|e^{Q_s(b+i\sigma;a,y)}|^2
 <\frac{441}{100}\frac{d-23/25}{d^3}
 \le\frac{441}{100}
            \frac{19/25}{(42/25)^3}
 =\frac{475}{672}<1.                                            \tag{15}
\]
The scalar function \((d-23/25)/d^3\) decreases for
\(d\ge42/25\), because its derivative has numerator
\(-2d+69/25<0\). Thus (15) is a uniform negative real-force
bound at the trial index, for every nonnegative index height.
Apply it at \(\sigma=h_*\), and use (4) as in Lemma 1.
The critical real index lies strictly to the left of \(b\),
proving (11). \(\square\)

## 4. Scope of the guards

Combining the two lemmas gives, on the closed subset of (1)
where \(h_*\ge0\),
\[
\boxed{\qquad
u_*<\min\{3/10, 37/40-x\},\qquad
                         1-x-u_*>3/40.
\qquad}                                                         \tag{16}
\]
The proof uses only the actual selected branch, its original
zero lift, the exact incoming carrier, and established horizontal
concavity. It is independent of level parity and makes no
assertion about a selected subset of physical indices.

The
[wall-gap completion theorem](research_mixed_conditional_wall_gap_completion.md)
already proves the whole conditional asymptotic on compact sets
where the actual wall gap is positive, including every parameter
with nonpositive critical height. The explicit distance (16)
can be used when estimating the horizontal loss in its remaining
positive-height comparison. That comparison still requires
control of the competing vertical change in the original phase.
Neither a uniform wall-action sign nor a complete asymptotic on
all of (1) follows from (16) alone.
