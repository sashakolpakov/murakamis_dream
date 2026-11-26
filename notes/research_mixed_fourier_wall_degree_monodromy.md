# The initialized Wall degree roots exchange over a full period

Research deduction, 7 November 2026. The two roots of the actual Wall
degree equation are distinct throughout the full real degree period.
Nevertheless their analytic continuations exchange after that period.
The initialized dominant root must therefore have equal modulus with
the other root somewhere beyond the completed half-degree interval.

This rules out extending the existing single-dominant-root argument
through the whole period. It does not assert a failure of the finite
Wall solution, of local semiclassical transport, or of a two-branch
connection analysis. No function value or new root is evaluated.

## 1. The original degree equation and its two discriminant zeros

Keep the original \(Y=e^{2\pi ix_0}\) and limiting degree equation
from the
[completed half-degree theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md):
\[
 A(w)R^2-D(w)R+C(w)=0,\qquad w=e^{-2\pi it},
 \quad 0\le t\le1,
 \tag{1}
\]
where
\[
 A=w(1-Yw),\qquad C=Yw(1-w),\qquad D=A+C-Y.
 \tag{2}
\]
In particular this is the \(\varepsilon=0\) equation of the
original finite recurrence, with its original parameter and marks.
Let
\[
 c=Y^{-1}-1=a-ib,\qquad
 -\frac7{20}<a<-\frac{37}{121}<-\frac3{10},\qquad
 \frac{60}{41}<b<\frac{61}{40}.
 \tag{3}
\]
These are the inherited analytic bounds from the
[original branch theorem](research_mixed_fourier_right_cap_wall_high_index_branch.md).
Choose the square root \(\sqrt c=u-iv\) with \(u,v>0\), and put
\[
                         S_\pm=2+c\pm2\sqrt c.
 \tag{4}
\]

**Lemma 1.** One has
\[
 \frac34<u<\frac45,\qquad \frac9{10}<v<1,
 \tag{5}
\]
and consequently
\[
 \frac1{20}<\Re S_-<\frac15,\qquad
 \frac{11}{40}<\Im S_-<\frac{11}{20},\qquad
 |S_-|^2<\frac{137}{400}<1,\qquad
 \Re S_+>\frac{63}{20}>1.
 \tag{6}
\]

*Proof.* The inherited bounds imply \(b>29/20\) and \(b^2<7/3\).
Since \(2u^2=|c|+a\), compare positive quantities by squaring:
\[
 \begin{split}
 |c|^2-(9/8-a)^2
 &=b^2-\frac{81}{64}+\frac94a\\
 &>\frac{841}{400}-\frac{81}{64}-\frac{63}{80}
   =\frac{79}{1600}>0,\\
 (32/25-a)^2-|c|^2
 &=\frac{1024}{625}-\frac{64}{25}a-b^2\\
 &>\frac{1504}{625}-\frac73>0 .
 \end{split}
 \tag{7}
\]
These give the two bounds on \(u\).
Also \(2uv=b\), so \(v>29/32>9/10\).
For the upper bound, \(2v^2=|c|-a\), and
\[
                 (2+a)^2-|c|^2=4+4a-b^2
                          >\frac{13}{5}-\frac73>0.
 \tag{8}
\]
Since \(2+a>0\), this proves \(v<1\).

Now \(S_-=2+a-2u+i(2v-b)\). Its real part lies between
\(2-7/20-8/5=1/20\) and \(2-3/10-3/2=1/5\).
Its imaginary part lies between
\(9/5-61/40=11/40\) and \(2-29/20=11/20\).
This proves its squared-modulus bound in (6). Finally
\(\Re S_+=2+a+2u>2-7/20+3/2=63/20\).
\(\square\)

Direct algebra in the original coefficients gives
\[
 \begin{split}
 \Delta(w):=D(w)^2-4A(w)C(w)
  &=(1-2Y+5Y^2)w^2-2Y(1+Y)w+Y^2\\
  &=Y^2(1-S_+w)(1-S_-w).
 \end{split}
 \tag{9}
\]
Thus \(\Delta\) has exactly one zero in \(|w|<1\), at
\(w=S_+^{-1}\), and one zero outside, at \(w=S_-^{-1}\).
Both are nonzero and distinct; neither lies on the unit circle.

## 2. Exchange of the initialized roots

**Proposition 2.** Let \(R_1(t),R_2(t)\) be the continuous analytic
branches of (1) along \(0\le t\le1\), initialized by
\[
                  R_1(0)=\frac{1-2Y}{1-Y},\qquad R_2(0)=0.
 \tag{10}
\]
Then
\[
                         R_1(1)=0,\qquad
                         R_2(1)=\frac{1-2Y}{1-Y}.
 \tag{11}
\]
Moreover there is \(t_c\in(1/2,1)\) such that
\[
                         |R_1(t_c)|=|R_2(t_c)|>0.
 \tag{12}
\]

*Proof.* On the unit circle, \(A=w(1-Yw)\ne0\), because
\(|Y|<1\), and \(\Delta\ne0\) by Lemma 1. Both degree roots
therefore continue without a collision along this parameter path.
As \(w=e^{-2\pi it}\) goes once clockwise around the unit circle,
(9) has winding number \(-1\) about zero: exactly one of its
zeros is inside. A continuous square root of \(\Delta\) changes
sign after this loop. Since \(A\) and \(D\) return to their original
values, the two expressions
\((D+\sqrt\Delta)/(2A)\) and \((D-\sqrt\Delta)/(2A)\)
are exchanged. This proves (11).

The original initialization (10) is precisely the exterior root
used in the completed half-degree theorem. Its modulus exceeds
one, while the other initialized root is zero. Throughout
\(0\le t\le1/2\), that theorem proves one root outside and one
inside the unit circle, on the same continued branches.
Thus \(|R_1|>|R_2|\) on that entire interval. At \(t=1\),
(11) reverses this strict inequality. Continuity gives (12) at
some \(t_c\in(1/2,1)\). On the open interval \(0<t<1\),
\(C=Yw(1-w)\ne0\), so neither root vanishes there.
\(\square\)

The equality in (12) occurs without an algebraic double root.
Consequently a nonvanishing discriminant on the full degree path
does not provide the modulus contraction required by the initialized
single-root proof. Relabeling whichever root has larger modulus
at each point does not supply a holomorphic continued branch or
the missing connection coefficient of the actual finite recurrence.

The finite solution remains its original normalized polynomial.
This note supplies no assertion about its zeros or leading
connection coefficients beyond the already completed interval.
The coherent contour approach and a two-branch recurrence analysis
remain distinct possible routes.
