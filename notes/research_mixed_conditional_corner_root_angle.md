# The lower real-coordinate guard for the corner conditional root

Private research proof, 8 November 2026. On the full closed
parameter rectangle of
[the corner root annulus](research_mixed_conditional_corner_root_annulus.md),
the original selected critical point satisfies
\(\Re t_*>2/25\). The proof keeps both the force and the original
logarithmic equation. It uses no phase evaluation and no extension
of the former argument that assumed \(\Re y\ge11/50\).

## 1. The original force and logarithmic lift

Write
\[
\begin{gathered}
a=x-i\eta,\quad \frac12\le x\le\frac7{10},\quad
0\le\eta\le\frac9{125},\\
y=q-i\xi,\quad 0\le q\le\frac{11}{50},\quad
\frac1{1000}\le\xi\le\frac{51}{500},\\
Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat.
\end{gathered}                                                   \tag{1}
\]
The cited annulus theorem proves that the unique selected root
has the original zero lift and lies strictly prewall:
\[
Q_t(t_*;a,y)=0,\qquad 0<\Re t_*<1-x,
\qquad \frac12<|e^{2\pi it_*}|<2.                            \tag{2}
\]
This includes \(q=0\); the original primitive is regular there
at the strictly negative outgoing height.

Suppose, seeking a contradiction, that
\[
u:=\Re t_*\le\frac2{25},\qquad \theta=2\pi u,
\quad U=e^{2\pi\Im t_*},\quad T=e^{2\pi\eta},
\quad R=e^{-2\pi\xi}.
\]
Then
\[
0<\theta\le\frac{4\pi}{25},\quad
\frac12<U<2,\quad 1\le T<\frac85,\quad \frac12<R<1.
                                                               \tag{3}
\]
Set \(\phi=2\pi(x+u)\) and \(\psi=2\pi(q+u)\).
The exact chirp-folded squared force is
\[
|e^{Q_t}|^2=
\frac{|T-Ue^{-i\phi}|^2\,|1-RUe^{-i\psi}|^2}
     {|1-Ue^{-i\theta}|^6}.                                  \tag{4}
\]
In these ranges
\[
\pi<\phi\le\frac{39\pi}{25},\qquad
\theta\le\psi\le\frac{3\pi}{5},\qquad
\cos\phi<\frac15,
\quad \cos\theta>\frac67,
\quad \sin\theta<\frac12.                                   \tag{5}
\]
For the cosine at \(\theta\), use
\(4\pi/25<8/15\) and
\(1-(8/15)^2/2=193/225>6/7\).
The incoming cosine is at most
\(\cos(39\pi/25)=\sin(3\pi/50)<1/5\).

## 2. The case \(U\le1\)

Put \(D=|1-Ue^{-i\theta}|^2\). Convexity in
\(U\in[1/2,1]\), together with (5), gives
\[
D<1+U^2-\frac{12U}{7}
\le\max\left\{\frac{11}{28},\frac27\right\}
=\frac{11}{28}.                                             \tag{6}
\]
The outgoing angle is in \([\theta,\pi]\), so
\[
|1-RUe^{-i\psi}|\ge|1-RUe^{-i\theta}|
                         \ge R|1-Ue^{-i\theta}|.             \tag{7}
\]
Indeed the difference of the squares in the second inequality is
\((1-R)(1+R-2RU\cos\theta)\ge(1-R)^2\).
The incoming factor satisfies
\[
|T-Ue^{-i\phi}|^2
>1+U^2-\frac{2U}{5}>1.                                      \tag{8}
\]
Here decreasing \(T\) to one decreases the squared modulus,
since \(T-U\cos\phi>0\). Consequently (4) gives
\[
|e^{Q_t}|^2>\frac1{4D^2}>
\frac1{4(11/28)^2}=\frac{196}{121}>1,                        \tag{9}
\]
contrary to (2).

## 3. The case \(U>1\): an argument bound before the force bound

Use the original strip arguments
\[
B=\Arg(1-Ue^{-i\theta}),\quad
A=\Arg(T-Ue^{-i\phi}),\quad
O=\Arg(1-RUe^{-i\psi}).                                    \tag{10}
\]
They satisfy \(B,O>0\), \(A<0\), and the zero lift in (2)
is exactly
\[
                         A+O-3B+2\pi x=0.                   \tag{11}
\]
For a fixed angle in \((0,\pi)\), the argument
\(\Arg(1-se^{-i\alpha})\) increases with \(s\).
For radius \(U\ge1\), it decreases with \(\alpha\), because
its angular derivative is
\((U\cos\alpha-U^2)/|1-Ue^{-i\alpha}|^2<0\).
Since \(RU\le U\) and \(\psi\ge\theta\), this proves
\(O\le B\). Hence
\[
                         2B\le A+2\pi x.                    \tag{12}
\]

We bound the right side with its full incoming argument retained.
At fixed \(x,u\), \(A\) increases with \(T\) and decreases
with \(U\): the corresponding derivatives have signs
\(-U\sin\phi>0\) and \(T\sin\phi<0\).
Also
\[
\partial_x(A+2\pi x)
=2\pi\frac{T^2-TU\cos\phi}{|T-Ue^{-i\phi}|^2}>0,          \tag{13}
\]
using \(T\ge1,U<2,\cos\phi<1/5\).
Thus its maximum is bounded by the endpoint values
\(x=7/10,T=8/5,U=1\), with \(u\) fixed.

At these endpoint values
\(7\pi/5<\phi\le39\pi/25\). On this interval
\[
|\sin\phi|>\frac9{10},\qquad
\frac85-\cos\phi<2.                                       \tag{14}
\]
For the first inequality, the two endpoint lower bounds are
\(\sin(2\pi/5)>9/10\) and
\(\cos(3\pi/50)>49/50\). The former follows from
\(\sin^2(2\pi/5)=(5+\sqrt5)/8>7/8>81/100\).
For the second, the minimum cosine is
\(-\cos(2\pi/5)>-2/5\), using \(\sqrt5<9/4\).
The real part of \(8/5-e^{-i\phi}\) is positive, so
\[
-\tan A>\frac9{20}>\frac37>\sqrt2-1=\tan\frac\pi8.
\]
It follows that \(A<-\pi/8\) at the endpoint, and (12)
therefore yields
\[
                      B<\frac12\left(\frac{7\pi}{5}
                                     -\frac\pi8\right)
                        =\frac{51\pi}{80}.                 \tag{15}
\]

Since \(U>1\), radial monotonicity at the own angle also gives
\(B>(\pi-\theta)/2\). Thus
\[
\frac\pi2<B+\theta
 <\left(\frac{51}{80}+\frac4{25}\right)\pi
 =\frac{319\pi}{400}<\frac{4\pi}{5},
\qquad \sin(B+\theta)>\sin\frac\pi5>\frac7{12}.             \tag{16}
\]
The final sine bound follows from
\(\sin^2(\pi/5)=(5-\sqrt5)/8>11/32>49/144\).

If \(m=|1-Ue^{-i\theta}|\), the imaginary part of
\(e^{i\theta}(1-Ue^{-i\theta})\) gives the exact relation
\[
               m\sin(B+\theta)=\sin\theta,
\qquad D=m^2=\frac{\sin^2\theta}{\sin^2(B+\theta)}.         \tag{17}
\]
For every nonnegative radius and \(\psi\in[\theta,3\pi/5]\),
radial minimization gives
\[
                         |1-RUe^{-i\psi}|^2\ge\sin^2\theta.
                                                               \tag{18}
\]
When \(\psi\le\pi/2\), its unrestricted radial minimum is
\(\sin^2\psi\ge\sin^2\theta\); for
\(\psi\ge\pi/2\), the modulus is at least one.
The incoming factor in (8) is now strictly greater than
\(8/5\), since \(U>1\). Substitution of (16)--(18) into
(4), and then \(\sin\theta<1/2\), proves
\[
|e^{Q_t}|^2>
\frac85\frac{(7/12)^6}{\sin^4\theta}
>\frac{128}{5}\left(\frac7{12}\right)^6
=\frac{117649}{116640}>1.                                  \tag{19}
\]
This is the remaining contradiction to (2).

## 4. Established scope

Both cases prove the strict guard
\[
\boxed{\qquad \frac2{25}<\Re t_*<1-x,
\qquad |\Im t_*|<\frac{\log2}{2\pi}.\qquad}                 \tag{20}
\]
The parameter set (1) is compact and the original selected root
is continuous and simple, so the separations in (20) are uniform.
In particular the selected critical point lies inside the strip
of [the corner prewall curvature lemma](research_mixed_next_lower_left_corner_prewall_curvature.md).

These are genuine guards for the original critical point, including
the seam \(q=0\), rather than hypotheses imposed on a possible
branch. They concern the phase and its regular local chart only.
The retained canonical finite integral still requires its complete
unweighted contour deformation, including the postwall part and
both connecting segments. No finite-source estimate or new
transfer asymptotic is concluded from (20) alone.
