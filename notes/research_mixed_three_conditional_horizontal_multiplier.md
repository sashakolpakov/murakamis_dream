# The type-three incoming multiplier and its domain dependence

Research deduction, 8 November 2026. The original type-three
conditional critical branch has an incoming multiplier of modulus
less than one on the displaced far-half rectangle. Its proof does
not require the multiplier itself to remain in the upper half-plane:
that stronger assertion is false, as an exact example below shows.
This algebraic result is kept separate from a complete finite-source
asymptotic on that new rectangle.

There is also an actual finite-source obstruction to any
domain-independent horizontal contraction rule. On the original
central source domain, the complete type-three conditional
polynomial grows horizontally near \(a=y=1/4\). Its growth follows
from the existing complete canonical asymptotic, with both level
parities and all boundary rows retained. No numerical evaluation
or change to a frozen source is used.

## 1. Original finite function and critical equation

Keep
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 C_{0,N}(X,Y)=\sum_{j=0}^{N-1}
                   \frac{X^{-j}p_j(X)p_j(Y)}{P_j^2},\\
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\\
 Q_0(t;a,y)=g(a+t)+g(y+t)-2g(t)-g(a)-g(y)+2\pi iat.
 \end{gathered}
 \tag{1}
\]
The phase includes the original incoming carrier. With
\(v=e^{2\pi it}\), its exponential critical equation is
\[
              (v-X)(v-Y)=X(v-1)^2,
 \tag{2}
\]
or
\[
          (1-X)v^2+(X-Y)v+X(Y-1)=0.
 \tag{3}
\]
At an original zero-lift critical point, define
\[
 \Theta_0(a,y)=Q_0(t_*;a,y),\qquad
                   w=\frac{v-X}{1-X}.
 \tag{4}
\]
Stationarity then gives the exact derivative
\[
 (\Theta_0)_a=g'(a+t_*)-g'(a)+2\pi it_*,
                       \qquad e^{(\Theta_0)_a}=w .
 \tag{5}
\]
The missing third denominator factorial distinguishes (2) from
the cubic of type four.

## 2. A selected branch on the displaced rectangle

For this section use
\[
 \mathcal D_0=\left\{
 \frac12\le\Re a\le\frac7{10},\
 -\frac9{125}\le\Im a\le0;\quad
 \frac{11}{50}\le\Re y\le\frac9{20},\
 0\le\Im y\le\frac1{100}\right\}.
 \tag{6}
\]
Its exponential coordinates satisfy
\[
 \Re X<0,\quad \Im X\ge0,\quad0<|X|\le1,\qquad
 \Im Y<0,\quad\Re Y<1,\quad |Y|\ge1.
 \tag{7}
\]
The strict \(\Re Y<1\) follows, for example, from
\(|Y|<8/7\) and \(\cos(11\pi/25)<1/5\), as in the original
selected-parameter guards.

**Lemma 1.** On (6), the quadratic (3) has exactly one
upper-half-plane root. It is simple, holomorphic on a fixed
neighborhood of this compact parameter set, and satisfies
\[
     0<\arg v<\arg X,\qquad
     0<\Re t_*<1-\Re a,\qquad
                 t_*=\frac{\Log v}{2\pi i}.
 \tag{8}
\]
It solves the original equation \(Q_{0,t}=0\), not a nonzero
logarithmic lift.

*Proof.* The values \(v=0,1,X\) are excluded by (2) and (7).
For a putative real root, solve for the outgoing coordinate:
\[
                     Y=v-\frac{X(v-1)^2}{v-X}.
 \tag{9}
\]
When \(\Im X>0\),
\[
             \Im Y=-\frac{v(v-1)^2\Im X}{|v-X|^2}.
 \tag{10}
\]
Thus \(v<0\) is impossible. For \(v>1\),
\(\Re[X/(v-X)]<0\), so (9) gives \(\Re Y>v>1\).
For \(0<v<1\), put \(A=\Re X<0\) and \(R=|X|^2\). Direct
expansion gives
\[
 |Y|^2-1=
 \frac{v(v-1)}{|v-X|^2}
 \left[v(v+1)-2A(v^2+1)+R(v^2-v+2)\right]<0,
 \tag{11}
\]
also impossible. When \(X\) is negative real, (9) is real
at a real \(v\), contradicting \(\Im Y<0\).
No root therefore crosses the real axis.

At \(X=Y=-1\), the roots are \(v=\pm i\). Moving \(Y\)
from \(-1\) into the lower unit semicircle and then to \(-i\)
keeps one upper root: the preceding real-root exclusion applies
as soon as \(\Im Y<0\), and the initial roots are simple.
One may then move through the connected rectangle (6).
The leading coefficient \(1-X\) stays nonzero and the
coefficients stay bounded on these compact paths, so no root
escapes to infinity. The upper root count remains one.
Counting multiplicities gives simplicity and hence the claimed
holomorphic dependence.

It remains to exclude the incoming numerator ray. If \(v=sX\)
with \(s>0\), \(s\ne1\), equation (9) becomes
\[
              Y=\frac{-s^2X^2+s(s+1)X-1}{s-1}.
 \tag{12}
\]
For \(s>1\) and \(\Im X>0\),
\[
       \Im Y=\frac{s\Im X\,\{s(1-2\Re X)+1\}}{s-1}>0.
 \tag{13}
\]
For \(0<s<1\), use \(\Re X^2\ge-|X|^2\ge-1\) to get
\[
 \Re Y-1
   =\frac{s[-s\Re X^2+(s+1)\Re X-1]}{s-1}>0.
 \tag{14}
\]
Both conclusions contradict (7). At negative real \(X\), the
ray is already outside the upper half-plane. Thus continuation
from that boundary gives the first inequality in (8).

All real parts of \(a,y,t_*,a+t_*,y+t_*\) now lie strictly
between zero and one; in particular \(\Re t_*<1/2\) and
\(\Re y<1/2\). The original logarithmic derivative is therefore
defined on its original regular strips. Its exponential is one,
so its lift is constant under this continuation. At
\[
                  a=y=1/2,\qquad t_*=1/4,
 \tag{15}
\]
the original sine-log formula gives
\[
 2g'(3/4)-2g'(1/4)+\pi i=0.
 \tag{16}
\]
This is the anchor used above, so the lift is zero everywhere
in (6). \(\square\)

## 3. The unit disk, without a global upper-half-plane premise

**Lemma 2.** For the branch in Lemma 1,
\[
                         0<|w|<1
                               \quad\text{on }\mathcal D_0.
 \tag{17}
\]

*Proof.* First show that any possible unit-circle value of
\(w\) would have positive imaginary part. Write
\[
 X=A+iB,\quad A<0,\ B\ge0,\quad
 w=c+is,\quad c^2+s^2=1,\quad
                       v=X+(1-X)w.
 \tag{18}
\]
The value \(w=1\) is excluded by \(v\ne1\). At \(w=-1\),
\(\Im(v\overline X)=B\ge0\), contradicting (8) when \(B>0\);
when \(B=0\), \(v\) is real. Suppose \(s<0\). The prewall
inequality \(\Im(v\overline X)<0\) reads
\[
                (A-|X|^2)s-Bc<0.
 \tag{19}
\]
Its first term is positive. Therefore \(B>0\) and \(c>0\).
But then \(-s=\sqrt{1-c^2}>1-c\), while \(1-A>B\), so
\[
 \Im v=B(1-c)+(1-A)s
        <(B-(1-A))(1-c)<0,
 \tag{20}
\]
contradicting the selected upper root. Hence \(s>0\).

Put \(d=2(1-c)>0\). On the unit circle,
\((w-1)^2/w=-d\). Equation (9) consequently simplifies to
\[
                          Y=v+dX(1-X).
 \tag{21}
\]
Since
\[
       \Im X(1-X)=B(1-2A)\ge0,\qquad \Im v>0,
 \tag{22}
\]
equation (21) gives \(\Im Y>0\), a contradiction.
Thus the multiplier never meets the unit circle.
At the anchor (15), \(w=(1+i)/2\) has modulus less than one;
connected continuation proves (17). \(\square\)

There is also no negative real value of \(w\). Indeed
\(v=w+(1-w)X\) would be real when \(B=0\); when \(B>0\)
and \(w<0\), it gives
\(\Im(v\overline X)=-wB>0\), contradicting (8).
Thus the principal \(\Log w\) is defined throughout (6).
Its value agrees with (5) at (15), and hence throughout:
\[
          (\Theta_0)_a=\Log w,\qquad
                     \Re(\Theta_0)_a=\log|w|<0.
 \tag{23}
\]
Compactness gives a uniform strict negative bound for this real
derivative. This is an algebraic action statement; a complete
finite-source consequence requires an actual asymptotic for
\(C_{0,N}\) on the same parameter set.

## 4. The upper-half-plane assertion really fails for type three

Unlike the type-four multiplier, \(w\) need not have positive
imaginary part in (6). The following exact values exhibit the
difference:
\[
 \begin{gathered}
 X=-\frac{21}{100}+\frac{31}{50}i,\qquad
 w=\frac3{10},\qquad
 v=\frac{153}{1000}+\frac{217}{500}i,\\
 Y=-\frac{17947}{300000}-\frac{75299}{75000}i.
 \end{gathered}
 \tag{24}
\]
They satisfy \(v=X+(1-X)w\). When \(w\ne0,1\), eliminating
\(X\) in (9) gives the exact identity
\[
                         Y=1+\frac{v(v-1)}{w}.
 \tag{25}
\]
For (24), its real and imaginary numerators before division by
\(w\) are \(-317947/10^6\) and \(-301196/10^6\), respectively.
Thus (25), and hence the original critical equation, holds exactly.
The root \(v\) is in the first quadrant whereas \(X\) is in the
second; it is therefore the upper prewall root of Lemma 1.

Here is a purely analytic check of the actual containing domains.
One has
\[
 |X|^2=\frac{857}{2000}>\left(\frac{13}{20}\right)^2,
 \qquad
 \Re a=\frac12+\frac1{2\pi}\arctan\frac{62}{21}
                                      \in(1/2,7/10).
 \tag{26}
\]
For the last inequality, \(62/21<3<\tan(2\pi/5)\), since
\(\tan^2(2\pi/5)=5+2\sqrt5>9\).
Also
\[
 \log(20/13)<9/20<18\pi/125,
 \tag{27}
\]
where \(e^{9/20}>1+9/20+(9/20)^2/2=1241/800>20/13\)
and \(\pi>25/8\). Equations (26)--(27) put
\(-9/125<\Im a=\log|X|/(2\pi)<0\).

The imaginary part of \(Y\) has magnitude greater than one, while
\[
 |\Re Y|<3/50,\qquad |\Im Y|<201/200,\qquad
 |Y|^2<\frac{40545}{40000}
                           <\left(\frac{101}{100}\right)^2.
 \tag{28}
\]
Thus \(0<\Im y=\log|Y|/(2\pi)<1/100\).
Since \(Y\) is in the lower left quadrant,
\[
 \Re y=\frac14+
  \frac1{2\pi}\arctan\frac{|\Re Y|}{|\Im Y|}
                          \in(1/4,13/50),
 \tag{29}
\]
using \(\arctan t<t\) and \(\pi>3\).
This lies strictly inside the selected interval in (6).
Every containing-domain inequality is strict.

Small perturbations \(w=3/10-i\varepsilon\), with the same \(X\),
and with \(v=X+(1-X)w\) and \(Y\) defined by (9), remain in
these strict domains for sufficiently small \(\varepsilon>0\).
The resulting upper root remains the selected one. Hence
\(\Im w<0\) occurs in (6), not just a zero boundary value.
By (23), the sign of the incoming-height derivative then differs
from the type-four sign. This does not contradict the horizontal
decrease in (23).

The example is in the stated containing rectangle. It is not
asserted to lie in a particular canonical following-reference image,
and it is not a counterexample to a finite-source asymptotic.

## 5. An actual complete-source horizontal-growth example

A universal horizontal-contraction rule for \(C_{0,N}\), without
a domain restriction, fails even where its whole source is proved.
Use the original canonical theorem on
\([1/5,9/20]^2\) in
[the type-three finite-source proof](research_mixed_three_canonical_conditional.md).
Its exact relation to (1) is
\[
 \mathcal L_{0,N}(a,y)
                    =\Pi_N(a)\Pi_N(y)C_{0,N}(X,Y).
 \tag{30}
\]
The two denominator factors are nonzero on a fixed neighborhood
of that square. Dividing the original complete expansion by
their original marked-factorial symbols gives
\[
 C_{0,N}(X,Y)
   =N^{-1/2}\mathcal B_0(a,y)e^{N\Theta_0(a,y)}
                 (1+O_{\rm hol}(N^{-1})),
                   \qquad \mathcal B_0\ne0.
 \tag{31}
\]
The action is precisely the bare phase in (1), with both
\(-g(a)\) and \(-g(y)\) retained. The power is
\(\sqrt N/(\sqrt N\,\sqrt N)=N^{-1/2}\).
The original theorem proves (31) for the single complete finite
sum, including all revived rows, both physical endpoints, both
weighted alias signs, and both unweighted joins. Both parities
and fixed normalized derivatives are included.

At the interior source point
\[
                    a=y=\frac14,\qquad t_*=\frac38,
 \tag{32}
\]
the original logarithmic derivative is zero. The two shifted
sines at \(5/8\) equal the own sine at \(3/8\), and their
original arguments cancel the incoming carrier. Thus (32)
is the selected root of the canonical theorem.
Here
\[
 X=-i,\quad v=\frac{-1+i}{\sqrt2},\qquad
 w=\frac12+\frac{1+\sqrt2}{2}i,\qquad
                         |w|^2=1+\frac1{\sqrt2}>1.
 \tag{33}
\]
It follows from the original derivative (5) that
\[
            \Re(\Theta_0)_a(1/4,1/4)
                 =\frac12\log\left(1+\frac1{\sqrt2}\right)>0.
 \tag{34}
\]
Differentiating the complete nonzero expansion (31) gives
\[
 \partial_a\log C_{0,N}
                   =N(\Theta_0)_a+O(1).
 \tag{35}
\]
Consequently there are fixed \(c,\delta>0\) and a level
threshold such that, for all higher levels of either parity,
fixed \(y=1/4\), and
\(1/4-\delta\le x_1\le x_2\le1/4+\delta\),
\[
 \boxed{\quad
 |C_{0,N}(e^{-2\pi ix_2},-i)|
   \ge e^{cN(x_2-x_1)}
                         |C_{0,N}(e^{-2\pi ix_1},-i)|.
 \quad}
 \tag{36}
\]
Choose the interval inside the original square so that (34)
has a fixed positive lower bound, then integrate the real
logarithmic derivative in (35). Uniform nonvanishing from (31)
licenses this integration. This is horizontal growth of the
actual finite source with its boundary retained, not merely
growth of one formal saddle.

## 6. What transfers to other short kernels

For any specified source whose already proved complete expansion
has a nonzero symbol and holomorphic relative error, an exact
incoming identity \(e^{\Theta_a}=w\) with \(|w|\le e^{-\kappa}<1\)
on a compact parameter set gives finite horizontal contraction
by the logarithmic-derivative argument in (35). The algebraic
test and the complete-source premise have separate roles.

For type three, Sections 2--3 prove the algebraic test on the
displaced rectangle (6), but the canonical theorem used in
Section 5 supplies its whole expansion near the central square,
not that entire displaced rectangle. The type-four displaced
source theorem cannot supply the missing type-three row and
current estimates: its denominator has a different power.
No full \(C_{0,N}\) contraction on (6) is claimed here.

Conversely, (36) rules out importing horizontal contraction
indiscriminately into the existing central source domains or
into every short-tangle kernel. It does not rule out a contraction
for a specified composite with its own allocation and actual
correlated parameters. Those must retain their original finite
source and exact boundary factors.
