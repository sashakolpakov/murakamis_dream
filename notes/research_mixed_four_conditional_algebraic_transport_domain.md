# An algebraic domain for the type-four conditional action

Research deduction, 8 November 2026. The type-four conditional
action has a simple branch on a larger parameter domain than the
rectangle used in the finite-source theorem. Its incoming
logarithmic derivative has negative real part and positive imaginary
part. Moving the incoming coordinate rightward or upward therefore
decreases the real action. Negative outgoing heights are allowed.

The hypotheses are inequalities in the exponential coordinates.
No numerical evaluation is used. This extends the algebraic and
action statements; it does not extend the asymptotic estimate for
the complete finite polynomial to the whole new domain.

## 1. Parameters and the original phase

Put
\[
\begin{split}
\mathcal X=\{X:\ &\Re X<0,\quad \Im X\ge0,\quad |X|\le1,\\
               & |X|^2(3-2\Re X)\ge1\},\\
\mathcal Y&=\{Y:\Im Y<0,\quad \Re Y<1\}.
\end{split}
\tag{1}
\]
Use
\[
 a=1-\frac{\Log X}{2\pi i},\qquad
 y=-\frac{\Log Y}{2\pi i},
\tag{2}
\]
where \(0<\Arg X\le\pi\) and \(-\pi<\Arg Y<0\). Thus
\[
 \frac12\le\Re a<\frac34,\qquad \Im a\le0,\qquad
                       0<\Re y<\frac12.
\tag{3}
\]
There is no sign restriction on \(\Im y\).

Keep \(g'(z)=\Log(1-e^{-2\pi iz})\) on \(0<\Re z<1\), with
the original primitive constant, and
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat.
\tag{4}
\]
For \(v=e^{2\pi it}\), its exponential critical equation is
\[
 v(v-X)(v-Y)=X(v-1)^3,
\tag{5}
\]
or
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0.
\tag{6}
\]
These are the phase and carrier of the original finite polynomial
\[
 C_{1,N}(X,Y)
 =\sum_{j=0}^{N-1}\frac{X^{-j}(rX;r)_j(rY;r)_j}{(r;r)_j^3},
 \qquad r=e^{-2\pi i/N}.
\tag{7}
\]

The domain \(\mathcal X\) is connected. Radial enlargement to the
unit circle preserves its last inequality: for
\(X=\rho e^{i\phi}\), \(\cos\phi<0\), the function
\(\rho^2(3-2\rho\cos\phi)\) is strictly increasing. On the unit
upper-left arc the inequality is automatic, and that arc connects
every radial path to \(X=-1\). The domain \(\mathcal Y\) is convex.

## 2. A unique upper root and the original logarithmic equation

**Theorem 1.** For every \((X,Y)\in\mathcal X\times\mathcal Y\),
(6) has exactly one upper-half-plane root, counting multiplicity.
It is simple, depends holomorphically locally, and satisfies
\[
 0<\arg v<\arg X,\qquad
 t=\frac{\Log v}{2\pi i},\qquad 0<\Re t<1-\Re a.
\tag{8}
\]
At this root the original logarithmic equation is \(Q_t=0\).

*Proof.* Equation (5) excludes \(v=0,1,X\). A real root would
give
\[
 Y=v-\frac{X(v-1)^3}{v(v-X)}.
\tag{9}
\]
When \(\Im X>0\),
\[
 \Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
\tag{10}
\]
Thus \(v<1\) is impossible. If \(v>1\), then
\[
 \Re\frac{X}{v-X}
       =\frac{v\Re X-|X|^2}{|v-X|^2}<0,
\]
so (9) gives \(\Re Y>v>1\), also impossible. For negative real
\(X\), the right side of (9) is real for every allowed real \(v\).
No root therefore crosses the real axis.

At \(X=-1,Y=-i\), the cubic is
\[
 (v-i)\{2v^2+(-2+3i)v-i\}.
\tag{11}
\]
Both quadratic roots have negative imaginary part. Indeed, write
\(\sqrt{-5-4i}=A-iB\), \(A,B>0\). Then
\(B^2=(\sqrt{41}+5)/2<9\), and their imaginary parts are
\((-3+B)/4\) and \((-3-B)/4\). The sole upper root is \(v=i\).
Along compact parameter paths the coefficients remain bounded
and \(1-X\) stays away from zero, so no root escapes to infinity.
Connectedness preserves the upper root count one. This proves
simplicity and local holomorphic dependence.

For the incoming numerator ray, set \(v=sX\), \(s>0\), \(s\ne1\),
and write \(c=\Re X<0\), \(R=|X|^2\). Direct substitution in (9)
gives the same identities as in
[the negative-height branch proof, equation (12)](research_mixed_conditional_negative_height_branch.md):
\[
\begin{split}
 \Im Y&=\Im X\,
 \frac{s^3(1-2c)+2s^2-R^{-1}}{s(s-1)},\\
 \Re Y-1&=
 \frac{s^3(R+c-2c^2)+(2c-1)s^2-2s+c/R}{s(s-1)}.
\end{split}
\tag{12}
\]
For \(s>1\), the first numerator is strictly greater than
\(3-2c-R^{-1}\ge0\). If \(\Im X>0\), this contradicts
\(\Im Y<0\). For \(0<s<1\), the second numerator is less than
\(s^3-s^2-2s<0\), since \(R\le1,c<0\). Its denominator is
negative, contradicting \(\Re Y<1\). For negative real \(X\),
the ray is outside the upper half-plane. Continuation from
\(X=-1\) proves (8).

Now \(t,a,y,a+t,y+t\) all have real parts in \((0,1)\):
\(\Re t<1/2\), \(\Re(a+t)<1\), and \(\Re(y+t)<1\).
The original logarithms in (4) are consequently defined.
Equation (5) says \(Q_t\in2\pi i\mathbb Z\). At the anchor
\(a=1/2,y=t=1/4\), direct evaluation gives
\[
 g'(3/4)+g'(1/2)-3g'(1/4)+\pi i=0.
\]
Continuity fixes the lift to zero throughout (1). \(\square\)

Uniqueness patches these local roots. Every compact subset of
(1) has a neighborhood on which simplicity and the strict strip
margins persist. No uniform neighborhood is asserted for the
whole noncompact outgoing domain.

## 3. The multiplier lies in the upper half of the unit disk

Define
\[
 \Theta(a,y)=Q(t(a,y);a,y),\qquad w=\frac{v-X}{1-X}.
\tag{13}
\]
Stationarity gives
\[
 \Theta_a=g'(a+t)-g'(a)+2\pi it,\qquad e^{\Theta_a}=w.
\tag{14}
\]

**Theorem 2.** Throughout (1),
\[
 \Im w>0,\qquad 0<|w|<1,\qquad \Theta_a=\Log w,
 \quad 0<\Im\Log w<\pi.
\tag{15}
\]

*Proof.* We give the exclusions to check that the outgoing radius
restrictions from the earlier rectangle are unnecessary.

At negative real \(X\), the upper-root property gives \(\Im w>0\).
Suppose \(w\) becomes real with \(\Im X>0\). The values zero
and one are excluded. The identity \(v=w+(1-w)X\) gives \(w<1\).
For \(w<0\), it also gives
\(\Im(v/X)=w\Im(X^{-1})>0\), contrary to (8). Thus \(0<w<1\).
Set \(A=\Re v\), \(r=|v|^2\), and \(d=1-A\). Using
\(\Re X<0\) and \(|X|\le1\) in this identity yields
\[
 A<w,\qquad r\le1-2wd.
\tag{16}
\]
Elimination of \(X\) in (9) gives
\[
 Y=2-\frac1v+\frac{(v-1)^2}{w},\qquad
 \frac{\Im Y}{\Im v}=\frac1r-\frac{2d}{w}.
\tag{17}
\]
Hence \(w<2rd\), and (16) implies
\[
 w<\frac{2d}{1+4d^2}\le\frac12,\qquad A<\frac12.
\tag{18}
\]
But
\[
 wr(\Re Y-1)=w(r-A)+r(2A^2-2A+1-r)=:M>0.
\tag{19}
\]
For completeness, if \(A\le0\), the first term is positive and
the second nonnegative. If \(A>0\), (16) and \(w>A\) imply
\(r<2A^2-2A+1\), so positivity holds when \(r\ge A\).
When \(r<A\), multiplication of \(w<2rd\) by the negative
number \(r-A\) gives instead
\[
 M>r(1-2A)(r+1-2A)>0.
\]
Thus (19) contradicts \(\Re Y<1\), and \(\Im w>0\) follows.

If \(|w|=1\), write
\[
 X=A+iB,\quad w=c+is,\quad s>0,\quad d=2(1-c)>0.
\]
Then
\[
 P:=|v|^2=1+(|X|^2-A)d+2Bs>1.
\tag{20}
\]
Since \((w-1)^2/w=-d\), (5) becomes
\[
 Y=v+dX(1-X)(1-v^{-1}).
\tag{21}
\]
Put \(X(1-X)=C+iD\); then
\[
 D=B(1-2A)\ge0,\qquad P+dC=1+2Bs+2B^2d>0.
\]
Writing \(v=r+it\), \(t>0\), gives
\[
 \Im Y=\frac{t}{P}(P+dC)+\frac{dD}{P}(P-r)>0,
\tag{22}
\]
because \(r\le\sqrt P<P\). This is impossible.
At the anchor (11), \(w=(1+i)/2\) has modulus less than one;
connectedness proves the modulus assertion.

Direct evaluation at that anchor also gives
\(\Theta_a=-\frac12\log2+i\pi/4=\Log w\).
Both logarithmic lifts persist by continuity, proving (15).
\(\square\)

These are the same multiplier exclusions as
[height-action monotonicity](research_mixed_conditional_height_action_monotonicity.md)
and [horizontal contraction](research_mixed_conditional_horizontal_contraction.md),
now with their hypotheses stated on (1). In particular no step
uses a lower bound for \(|Y|\).

## 4. Directed action transport

On each compact subset of (1), there exist
\(\kappa_x,\kappa_h>0\) such that
\[
 \partial_x\Re\Theta=\log|w|\le-\kappa_x,\qquad
 \partial_h\Re\Theta=-\Arg w\le-\kappa_h,\qquad a=x+ih.
\tag{23}
\]
A piecewise smooth path with fixed \(y\), staying in that compact
set and satisfying \(x'\ge0,h'\ge0\), therefore obeys
\[
 \Re\Theta(a_1,y)-\Re\Theta(a_0,y)
 \le-\kappa_x(x_1-x_0)-\kappa_h(h_1-h_0).
\tag{24}
\]
This is the chain rule applied to (15).

The old incoming rectangle belongs to (1), because it has
\(|X|^2>1/3,\Re X<0\). For those same incoming parameters,
every outgoing coordinate
\[
                  0<\Re y<1/2,\qquad \Im y\le0
\tag{25}
\]
also belongs to (1): its exponential has negative imaginary part
and modulus at most one, hence real part less than one.
This includes the actual negative outgoing heights of an attached
ordinary block. Positive outgoing heights are allowed whenever
the explicit inequality \(\Re Y<1\) is preserved.

The incoming inequality itself is sharper than \(|X|^2>1/3\).
For \(X=-\rho\), it becomes \(\rho^2(3+2\rho)\ge1\), or
\(\rho\ge1/2\). This describes an enlarged action domain;
it does not give a finite-source estimate at its extra boundary.

## 5. The analytic step remains separate

The [complete displaced-rectangle theorem](research_mixed_conditional_nonnegative_height_complete_source.md)
already proves a nonzero asymptotic for (7) on its smaller
specified domain. There (23) gives contraction of the finite
polynomial, as in the existing horizontal theorem.

On a new domain one must still estimate every physical row,
Fourier remainder and connecting segment of (7). The action
inequalities cannot substitute for these bounds. In particular
this note supplies the branch and action transport needed at
negative outgoing heights, but neither a whole-source bound
there nor a new knot-family theorem. The type-three quadratic
has different boundary behavior; the conclusions are not
transferred to that equation.

