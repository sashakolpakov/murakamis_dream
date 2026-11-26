# The conditional action across the incoming unit circle

Private written proof, 10 November 2026. The simple geometric branch of
the type-four conditional cubic persists when the incoming exponential
coordinate moves slightly outside the unit disk. Its action still
decreases as the incoming logarithmic coordinate moves right or up.
This includes the positive height used by the selected first Fourier
term of an initial four/four word.

The assertion is about the original critical action. Estimates for the
complete finite conditional polynomial, the cap multiplying it, and
their contour corrections remain separate.

## 1. A larger algebraic domain

For \(X=c+iB\), write \(R=|X|^2\), and define
\[
 \mathcal D=\{X:\ c<0,\ B\ge0,\ R+c\le1,\
                         R(3-2c)\ge1\}.
 \tag{1}
\]
Keep the outgoing domain
\[
             \mathcal Y=\{Y:\Im Y<0,\ \Re Y<1\}.
 \tag{2}
\]
The incoming domain of
[the earlier algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
is contained in (1). No restriction \(R\le1\) is imposed here.

The domain \(\mathcal D\) is connected. On a fixed upper-left ray
write \(X=\rho e^{i\phi}\), \(\cos\phi<0\). The function
\(\rho^2(3-2\rho\cos\phi)\) increases strictly with \(\rho>0\).
If \(\rho\le1\), increasing the radius to one preserves its lower
bound in (1), and \(\rho^2+\rho\cos\phi<1\) all along that path.
If \(\rho\ge1\), decreasing to one preserves the lower bound because
its value at one exceeds three. It preserves the other inequality
because \(\rho^2+\rho\cos\phi\) increases with \(\rho\ge1\).
The upper-left unit arc lies in \(\mathcal D\) and connects every
such path to \(-1\).

Use the logarithmic coordinates
\[
 a=1-\frac{\Log X}{2\pi i},\qquad
 y=-\frac{\Log Y}{2\pi i},\qquad
 0<\Arg X\le\pi,\quad -\pi<\Arg Y<0 .
 \tag{3}
\]
Thus \(1/2\le\Re a<3/4\), \(0<\Re y<1/2\); the incoming
height may now have either sign. Keep the original primitive
\[
 g(z)=J(z)+\frac{i\pi}{2}(z-z^2),\qquad
 J'(z)=\Log(2\sin\pi z),\quad J(0)=0,
\]
continued from the positive real sine interval, and the phase
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat.
 \tag{4}
\]
In its regular strip \(g'(z)=\Log(1-e^{-2\pi iz})\).
The finite function whose conditional phase is (4) is
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^3},
 \qquad q_N=e^{-2\pi i/N}.
 \tag{5}
\]
Its summation range, chirp, and normalization have not changed.

## 2. The simple upper root and its logarithmic lift

**Theorem 1.** For \(X\in\mathcal D\), \(Y\in\mathcal Y\), the cubic
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0
 \tag{6}
\]
has exactly one root in the upper half-plane, counting multiplicity.
That root is simple and satisfies
\[
 0<\arg v<\arg X,\qquad
 t=\frac{\Log v}{2\pi i},\qquad
 0<\Re t<1-\Re a,\qquad Q_t(t;a,y)=0.
 \tag{7}
\]
It has a holomorphic continuation near every parameter pair in the
stated domain.

*Proof.* Equation (6) is equivalent to
\[
                 v(v-X)(v-Y)=X(v-1)^3.
 \tag{8}
\]
It excludes \(v=0,1,X\). A real root would imply
\[
 Y=v-\frac{X(v-1)^3}{v(v-X)},\qquad
 \Im Y=-\frac{(v-1)^3B}{|v-X|^2}.
 \tag{9}
\]
For \(B>0\), the sign rules out \(v<1\). If \(v>1\), then
\[
 \Re\frac{X}{v-X}=\frac{vc-R}{|v-X|^2}<0,
\]
so (9) gives \(\Re Y>v>1\), also impossible. For negative real
\(X\), (9) is real for real \(v\), which contradicts \(\Im Y<0\).

At \(X=-1,Y=-i\), the factorization is
\[
       (v-i)\{2v^2+(-2+3i)v-i\}.
 \tag{10}
\]
The two quadratic roots have negative imaginary parts. Indeed, if
\(\sqrt{-5-4i}=A-iD\) with \(A,D>0\), then
\(D^2=(\sqrt{41}+5)/2<9\), and their imaginary parts are
\((-3+D)/4\) and \((-3-D)/4\). The unique upper root is \(i\).
No root crosses the real axis by (9). Along compact parameter
paths no root escapes to infinity, since the coefficients stay
bounded and \(1-X\) stays away from zero. Connectedness of
\(\mathcal D\times\mathcal Y\) proves the count one. This also
proves simplicity.

To locate the upper root relative to the incoming ray, substitute
\(v=sX\), \(s>0\), \(s\ne1\), in (9). Direct simplification gives
\[
\begin{split}
 \Im Y&=B\,\frac{s^3(1-2c)+2s^2-R^{-1}}{s(s-1)},\\
 \Re Y-1&=
 \frac{s^3(R+c-2c^2)+(2c-1)s^2-2s+c/R}{s(s-1)} .
\end{split}
 \tag{11}
\]
For \(s>1\), the first numerator is strictly greater than
\(3-2c-R^{-1}\ge0\), contradicting \(\Im Y<0\) when \(B>0\).
For \(0<s<1\), the condition \(R+c\le1\) implies
\(R+c-2c^2<1\). The second numerator is strictly less than
\(s^3-s^2-2s<0\), whereas its denominator is negative.
Thus \(\Re Y>1\), again impossible. For negative real \(X\)
its ray does not meet the upper half-plane.
Continuation from (10) proves the strict argument inequality in (7).

Consequently \(t,a+t,y+t\) all lie in the original open real
strips of the primitive. Equation (8) gives
\(Q_t\in2\pi i\mathbb Z\). At the anchor
\(a=1/2,\ y=t=1/4\), the original logarithms give
\[
 g'(3/4)+g'(1/2)-3g'(1/4)+\pi i=0.
\]
The logarithmic lift therefore remains zero. The implicit function
theorem and uniqueness give the asserted local continuations,
including at the boundary of (1). \(\square\)

## 3. The incoming multiplier

Define
\[
 \Theta(a,y)=Q(t(a,y);a,y),\qquad
             \omega=\frac{v-X}{1-X}.
 \tag{12}
\]

**Theorem 2.** On the same domain,
\[
 \Im\omega>0,\qquad 0<|\omega|<1,\qquad
                     \Theta_a=\Log\omega .
 \tag{13}
\]
The logarithm has \(0<\Im\Log\omega<\pi\).

*Proof.* Stationarity and (4) give
\[
 \Theta_a=g'(a+t)-g'(a)+2\pi it,\qquad
                         e^{\Theta_a}=\omega .
 \tag{14}
\]
The main issue is to exclude a real multiplier without assuming
\(|X|\le1\).

For negative real \(X\), the upper-root property already implies
\(\Im\omega>0\). If \(B>0\) and \(\omega\) is real, the identity
\(v=\omega+(1-\omega)X\) forces \(\omega<1\). The values zero
and one are excluded by (8). A negative \(\omega\) would give
\(\Im(v/X)=\omega\Im(X^{-1})>0\), contrary to
\(0<\arg v<\arg X\). Thus only \(0<\omega<1\) could occur.

Write \(A=\Re v\), \(r=|v|^2\), and \(d=1-A\).
Then \(A<\omega<1\), and the following exact identity supplies
the needed replacement for the old unit-disk estimate:
\[
 2A^2-2A+1-r
   =(1-\omega)^2(1-2c+2c^2-R)>0.
 \tag{15}
\]
Its last factor is positive because \(R\le1-c\) gives
\(1-2c+2c^2-R\ge-c+2c^2>0\).
Eliminating \(X\) from (8) gives
\[
 Y=2-\frac1v+\frac{(v-1)^2}{\omega},\qquad
 \frac{\Im Y}{\Im v}=\frac1r-\frac{2d}{\omega}.
 \tag{16}
\]
In particular \(\omega<2rd\). Its real part yields
\[
 \omega r(\Re Y-1)
   =\omega(r-A)+r(2A^2-2A+1-r)=:M.
 \tag{17}
\]
If \(r\ge A\), (15) makes \(M>0\). If \(r<A\), then \(A>0\).
In this case \(A\ge1/2\) would imply
\[
 \omega<2r(1-A)<2A(1-A)\le A<\omega,
\]
a contradiction. Thus \(A<1/2\). Multiplying
\(\omega<2r(1-A)\) by \(r-A<0\) in (17) now gives
\[
                 M>r(1-2A)(r+1-2A)>0.
 \tag{18}
\]
Both cases contradict \(\Re Y<1\). Hence the multiplier cannot
cross the real axis, and continuation proves \(\Im\omega>0\).

To exclude \(|\omega|=1\), put
\(\omega=u+is\), \(s>0\), and \(d_0=2(1-u)>0\).
The identity \(v=\omega+(1-\omega)X\) gives
\[
 P:=|v|^2=1+(R-c)d_0+2Bs>1.
 \tag{19}
\]
Since \((\omega-1)^2/\omega=-d_0\), equation (8) becomes
\[
                 Y=v+d_0X(1-X)(1-v^{-1}).
 \tag{20}
\]
Write \(X(1-X)=C+iD\). Then
\[
 D=B(1-2c)\ge0,\qquad
 P+d_0C=1+2Bs+2B^2d_0>0.
\]
If \(v=\alpha+i\beta\), \(\beta>0\), taking the imaginary part
of (20) gives
\[
 \Im Y=\frac{\beta}{P}(P+d_0C)
                  +\frac{d_0D}{P}(P-\alpha)>0,
 \tag{21}
\]
because \(\alpha\le\sqrt P<P\). This contradicts (2).
At the anchor \(\omega=(1+i)/2\), so connectedness proves
\(|\omega|<1\) everywhere.

Finally, direct substitution at the anchor gives
\(\Theta_a=-\frac12\log2+i\pi/4=\Log\omega\).
Both sides of (14) continue with the same lift, proving (13).
\(\square\)

## 4. Consequences for the selected positive-height path

On every compact parameter subset the strict inequalities above give
positive constants \(\kappa_x,\kappa_h\) such that
\[
 \partial_x\Re\Theta=\log|\omega|\le-\kappa_x,\qquad
 \partial_h\Re\Theta=-\Arg\omega\le-\kappa_h,
 \qquad a=x+ih .
 \tag{22}
\]
They apply along any rightward or upward path that stays in this
subset with \(y\) fixed.

In particular the entire rectangle
\[
 \frac12\le x\le\frac7{10},\qquad
 -\frac{39}{500}\le h\le\frac1{100}
 \tag{23}
\]
is contained in the incoming domain (1).
For \(h\le0\), put \(\rho=e^{2\pi h}\). The inequalities
\(2\pi|h|\le39\pi/250<1/2\) and
\[
 e^{1/2}<1+\frac12+\frac{1/8}{1-1/6}
                    =\frac{33}{20}<\frac53
\]
give \(\rho>3/5\). Thus \(R(3-2c)>27/25>1\), and
\(R+c<1\).

For \(0\le h\le1/100\), the elementary positive-series bound
\(e^u\le(1-u)^{-1}\) for \(0\le u<1\), together with
\(\pi<22/7\), gives
\[
 1\le\rho<\frac{175}{164}<\frac{43}{40},\qquad R<\frac65.
\]
Here \(\Arg X\in[3\pi/5,\pi]\), and
\[
 \cos(3\pi/5)=-\frac{\sqrt5-1}{4}<-\frac4{13}.
\]
The latter follows from \(5>841/169\). Hence \(c<-4/13\) and
\[
                         R+c<\frac65-\frac4{13}
                                  =\frac{58}{65}<1.
 \tag{24}
\]
The remaining inequality \(R(3-2c)>1\) is immediate from \(R\ge1\).
For \(y=z+id\), \(0<z<1/2\) and \(d\le0\), its exponential
belongs to (2). This includes the actual outgoing interval and
negative heights in the initial four/four estimates.

Thus the original critical action at the selected height \(1/100\)
is bounded above by its value at any lower height in (23), at the
same \(x,y\). This is a comparison of the original action functions
with their primitive constants retained. It introduces no new saddle,
factor, or normalization.

The finite source (5) still needs physical-row and contour estimates
on this enlarged domain. Neither (22) nor (24) bounds its full sum
by its critical exponential. In a product with a cap and a selected
Fourier weight, those additional factors must also be estimated.

## Direct source version

| Source | SHA-256 |
|---|---|
| research_mixed_four_conditional_algebraic_transport_domain.md | 4788b140b0ab435bb5951db75aadad03376ddaf3bfb6378b8f17242253b7ace0 |

The proof uses written algebra and inequalities only. No mathematical
numerical evaluation, saved-value arithmetic, test, import, compilation,
or edit to a frozen source or manuscript was performed.
