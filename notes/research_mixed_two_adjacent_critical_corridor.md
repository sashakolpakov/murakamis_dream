# The original critical point of the merged power-two pair

Research deduction, 7 November 2026. The complete adjacent pair
has an exact one-index contraction against the physical \(C_0\)
rows. Its regular two-index phase has a unique original critical
point on an explicit complex strip at equal Fourier endpoints
\(x=y=x_0\). The point and its zero logarithmic lift follow from
elementary rational inequalities. The real Hessian is strictly
negative on the whole strip, with independent internal heights.

This proves the Gaussian of the specified central zero-mode
rectangle. It does not compare all remaining currents in a
residue decomposition of the finite pair. No numerical evaluation
or new certificate is used.

## 1. The exact reversed source

Put \(D=N-1\), \(r=e^{-2\pi i/N}\),
\[
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\quad
 X=e^{-2\pi ix},\quad W=e^{-2\pi iy}.
 \tag{1}
\]
[The merged-source calculation](research_mixed_two_adjacent_merged_source.md)
gives the complete identity
\[
\begin{split}
 V_{22,N}(x,y)&:=h(x)^TA_2^2h(y)\\
 &=e^{\pi iD(x+y)}
   \sum_{\substack{j,k\ge0\\j+k<N}}
     \frac{r^{-jk}P_{j+k}p_j(X)p_k(W)}{P_j^2P_k^2}\\
 &=e^{\pi iD(x+y)}
      \sum_{j=0}^{D}\frac{p_j(X)}{P_j}C_{0,N}(r^j,W).
\end{split}
 \tag{2}
\]
The final equality uses the actual support
\[
 p_k(r^j)=P_{j+k}/P_j\quad(j+k<N),\qquad
 p_k(r^j)=0\quad(j+k\ge N).
 \tag{3}
\]
All channels remain in (2), including the incoming indices outside
the proved physical \(C_0\) packet interval.

For normalized indices \(a=j/N,s=k/N\), the original regular
row interpolant is
\[
 \mathcal T_N(a,s;x,y)
 =e^{2\pi iNas}
 \frac{\Pi_N(a+s)\Pi_N(a+x)\Pi_N(s+y)}
 {\Pi_N(x)\Pi_N(y)\Pi_N(a)^2\Pi_N(s)^2}.
 \tag{4}
\]
At physical indices in the triangle it equals the summand in (2).
No support condition is imposed off grid. On regular compact
charts its original phase and packet are
\[
\begin{split}
 F(a,s;x,y)={}&g(a+s)+g(a+x)+g(s+y)\\
             &-2g(a)-2g(s)-g(x)-g(y)+2\pi ias,\\
 \mathcal T_N&=N^{-3/2}b(a,s;x,y)e^{NF(a,s;x,y)}
                                      (1+O(N^{-1})),\\
 b&=
 \frac{\mathfrak a(a+s)\mathfrak a(a+x)\mathfrak a(s+y)}
 {\mathfrak a(x)\mathfrak a(y)\mathfrak a(a)^2\mathfrak a(s)^2}.
\end{split}
 \tag{5}
\]
There are three numerator and six denominator square-root powers
of \(N\). The chirp \(r^{-jk}\) is exactly \(e^{2\pi iNas}\),
without an extra lower-order factor.

## 2. A rigorous symmetric root

Write
\[
 Q=\cot(\pi x_0)=q-i\beta,\qquad
 \frac{127}{100}<q<\frac{13}{10},\qquad
             \frac{17}{25}<\beta<\frac{73}{100}.
 \tag{6}
\]
These are the original output bounds in
[the right-critical-sheet theorem](research_mixed_three_fourier_conditional_right_critical_sheet.md),
equations (2), (6)--(7); also \(1/6<\Re x_0<1/4\).

For \(x=y=x_0\), put \(U=e^{-2\pi ia},V=e^{-2\pi is}\).
The exponentiated derivatives of (5) are
\[
 (1-UV)(1-XU)=V(1-U)^2,\qquad
 (1-UV)(1-XV)=U(1-V)^2 .
 \tag{7}
\]
Subtracting gives \((1-X)(U-V)(1-UV)=0\). On the regular
strip below the first and last factors are nonzero, so \(U=V\)
and \(a=s\). The remaining equation is
\[
 (1-X)U^2-XU+1=0,\qquad
       2T^2+(Q-i)T+iQ-1=0,\quad T=\cot(\pi a).
 \tag{8}
\]

**Lemma 1.** The quadratic in (8) has a root \(T=u-iv\) with
\[
 \frac15<v<\frac14,\qquad \frac13<u<\frac37.
 \tag{9}
\]
Its original inverse cotangent \(a_*\), chosen with
\(0<\Re a_*<1/2\), satisfies
\[
 \frac13<\Re a_*<\frac5{12},\qquad
 \frac1{20}<\Im a_*<\frac{\operatorname{atanh}(1/4)}{\pi}.
 \tag{10}
\]

*Proof.* The exact real equations are
\[
 (4v+\beta+1)u=q(1-v),\qquad
 2u^2+qu=2v^2+(\beta+1)v+1-\beta.
 \tag{11}
\]
Set
\[
 u(v)=\frac{q(1-v)}{4v+\beta+1},\quad
 E(v)=2u(v)^2+qu(v)-2v^2-(\beta+1)v-1+\beta .
 \tag{12}
\]
On \(0\le v\le1\),
\[
 u'(v)=-\frac{q(\beta+5)}{(4v+\beta+1)^2}<0,\qquad
 E'(v)=(4u+q)u'(v)-4v-\beta-1<0.
 \tag{13}
\]
Also \(E(0)>0\), since \(u(0)>1/2,q>1,\beta>1/2\),
while \(E(1)=-4\).

At \(v=1/5\), (6) gives
\[
 u>\frac{508}{1265}>\frac25,\quad
 2u^2+qu>\frac{207}{250}>\frac{92}{125}
                       >2v^2+(\beta+1)v+1-\beta .
 \tag{14}
\]
At \(v=1/4\) it gives
\[
 u<\frac{195}{536}<\frac38,\quad
 2u^2+qu<\frac{123}{160}<\frac{331}{400}
                       <2v^2+(\beta+1)v+1-\beta .
 \tag{15}
\]
Thus the unique zero of \(E\) lies in \((1/5,1/4)\).
Equation (11) then gives
\[
                  \frac{127}{364}<u<\frac{13}{31},
 \tag{16}
\]
which implies the two stated bounds on \(u\).

Put
\[
 B=\arctan\frac{u}{1-v}+\arctan\frac{u}{1+v}.
\]
The original inverse cotangent has
\[
 \Re a_*=\frac12-\frac{B}{2\pi},\qquad
 \Im a_*=\frac1{4\pi}
        \log\frac{u^2+(1+v)^2}{u^2+(1-v)^2}.
 \tag{17}
\]
Now \(B<2u/(1-v^2)<32/35<\pi/3\).
Since \(u^2+v^2<1\), \(0<B<\pi/2\), and
\[
        \tan B=\frac{2u}{1-v^2-u^2}
              >\frac{2u}{1-u^2}>\frac34>\frac1{\sqrt3}.
 \tag{18}
\]
Therefore \(\pi/6<B<\pi/3\), proving the real bounds.
The logarithm in (17) is positive. Adding \(u^2>0\)
decreases its ratio, so the imaginary part is less than
\(\operatorname{atanh}(v)/\pi\). For the lower bound, rewrite it as
\[
 \Im a_*=\frac1{2\pi}
       \operatorname{atanh}\frac{2v}{1+u^2+v^2}
   >\frac1{2\pi}\frac{1568}{4885}
   >\frac{10976}{214940}>\frac1{20}.
 \tag{18a}
\]
Here the denominator is less than
\(1+9/49+1/16=977/784\), and \(\pi<22/7\).
This proves (10).
\(\square\)

The other quadratic root is exactly
\[
                  -q/2-u+i\{(\beta+1)/2+v\}.
 \tag{19}
\]
Its real part is negative, so it cannot be the cotangent of
a point with real part in \((1/3,5/12)\).

## 3. Original logarithmic lift and whole-strip Hessian

Let
\[
 \mathcal C=\{(a,s)\in\mathbb C^2:
                      1/3<\Re a,\Re s<5/12\},
 \qquad 1/6<\Re x,\Re y<1/4.
 \tag{20}
\]
All arguments in (5) are on their original regular strips.
Specifically
\[
 2/3<\Re(a+s)<5/6,\qquad
          1/2<\Re(a+x),\Re(s+y)<2/3.
 \tag{21}
\]
This holds for independent arbitrary imaginary parts.

At \(a=s=a_*\), \(x=y=x_0\), all three arguments
\(a_*,2a_*,a_*+x_0\) have positive height. The original
strip logarithms therefore satisfy
\[
\begin{split}
 -\pi&<\Im g'(2a_*),\Im g'(a_*+x_0)<0,\\
 0&<\Im g'(a_*)<\pi/3,\qquad
       2\pi/3<2\pi\Re a_*<5\pi/6 .
\end{split}
 \tag{22}
\]
The actual derivative is
\[
 F_a=g'(2a_*)+g'(a_*+x_0)-2g'(a_*)+2\pi ia_*.
 \tag{23}
\]
Hence \(-2\pi<\Im F_a<5\pi/6\). Equation (7) says
\(e^{F_a}=1\), so its only possible original lift is zero.
The same argument applies to \(F_s\). This proves stationarity
for the original phase, not only for its multiplier equations.

The real Hessian throughout (20) is
\[
\begin{split}
 \Re F''={}&\pi\Re\cot\pi(a+s)
                     \begin{pmatrix}1&1\\1&1\end{pmatrix}\\
 &+\pi\operatorname{diag}\left(
  \Re\{\cot\pi(a+x)-2\cot\pi a\},
  \Re\{\cot\pi(s+y)-2\cot\pi s\}\right).
\end{split}
 \tag{24}
\]
The additional off-diagonal chirp is purely imaginary.
Using
\[
 \Re\cot\pi z=
 \frac{\sin(2\pi\Re z)}
      {\cosh(2\pi\Im z)-\cos(2\pi\Re z)}
 \tag{25}
\]
shows that the rank-one coefficient in (24) is negative,
and both diagonal entries are strictly negative. Thus
\[
                       -\Re F''\succ0
                          \quad\hbox{throughout }\mathcal C.
 \tag{26}
\]
There is a uniform positive floor on every bounded height
family. No such floor is asserted at infinite height.

**Theorem 2.** At \(x=y=x_0\), the original phase has exactly
one critical point in \(\mathcal C\), namely \((a_*,a_*)\).
It is nondegenerate and continues holomorphically, with zero
lifts and the original absolute action, for \((x,y)\) in a
fixed complex neighborhood of \((x_0,x_0)\).

*Proof.* Lemma 1 and (22)--(23) prove existence. At equal
endpoints (7) forces symmetry, since \(1-UV\ne0\) by (21);
the strip width excludes an integer difference between \(a,s\).
The other root is excluded by (19). Nondegeneracy follows
from (26), and the holomorphic implicit function theorem
gives the continuation. In fact for any fixed endpoints in
(20), a critical point in \(\mathcal C\), if it exists, is
unique: integrate the positive Hermitian real part of
\(-F''\) along the complex straight segment between two
points, and take its quadratic form on their difference.
Their gradients cannot agree. This uses the convex complex
strip, not just a real slice. \(\square\)

## 4. Exact symmetric Hessian and the central current

At the symmetric root set \(T=\cot\pi a_*\) and
\(U=(T-i)/(T+i)\). The quadratic gives
\[
                  \cot\pi(a_*+x_0)
                         =2T+3i-\frac4{T-i}.
 \tag{27}
\]
The antisymmetric and symmetric Hessian eigenvalues are
\[
\begin{split}
 \lambda_-&=2\pi i\,U^{-1},\\
 \lambda_+&=\pi U^{-1}\frac{T^2+2iT+1}{T}
       =\frac{\pi(T+i)^2(4T+Q-i)}{2T(T-i)} .
\end{split}
 \tag{28}
\]
In particular
\[
        \det F''=2\pi^2i\,U^{-2}
                           \frac{T^2+2iT+1}{T}\ne0.
 \tag{29}
\]
To verify these identities, use
\(\cot(2\pi a_*)=(T^2-1)/(2T)\) in (24)'s full complex
Hessian and substitute (27). The last expression in (28)
uses \(Q(T+i)=1-2T^2+iT\); its derivative factor \(4T+Q-i\)
is nonzero because the two quadratic roots are distinct.
The sign proof (26) independently fixes the Gaussian branch.

Write the continued critical point as
\((a_*(x,y),s_*(x,y))\), and define
\[
 \mathcal S_{22}(x,y)=
        F(a_*(x,y),s_*(x,y);x,y)+\pi i(x+y).
 \tag{30}
\]
Consider the zero-mode integral of the exact row (4), with
lattice density \(N^2\), on
\[
 \mathcal R_{x,y}
 =([1/3,5/12]+i\Im a_*(x,y))
        \times([1/3,5/12]+i\Im s_*(x,y)).
 \tag{31}
\]
At nearby complex endpoint pairs, (26) makes its horizontal
real phase strictly concave, with its unique interior maximum
at the actual critical point. Its boundary has a uniform
gap on compact endpoint subfamilies. Therefore this entire
central current has the nonzero Gaussian
\[
\begin{split}
 &e^{\pi iD(x+y)}N^2
          \iint_{\mathcal R_{x,y}}\mathcal T_N(a,s;x,y)\,da\,ds\\
 &\quad=
 N^{-1/2}
 \frac{2\pi e^{-\pi i(x+y)}b(a_*,s_*;x,y)}
      {\sqrt{\det[-F''(a_*,s_*;x,y)]}}\,
       e^{N\mathcal S_{22}(x,y)}(1+O(N^{-1})).
\end{split}
 \tag{32}
\]
The square root is the accretive Gaussian branch. The factors
\(N^{-3/2},N^2,N^{-1}\) from the row, the two lattice
densities and the two-dimensional Gaussian give precisely
\(N^{-1/2}\). On a symmetric local box the odd first
corrections cancel; uniform quartic and symbol bounds give
the stated relative error. One can instead translate a fixed
center rectangle through the moved saddle, retaining its
product-boundary connectors. They remain in the same strict
boundary gap.

Equation (32) concerns the specified central current. A full
packet for the literal pair (2) additionally requires control
of all remaining physical indices, endpoint currents and
Fourier corrections, with their original period factors.
In particular the physical \(C_0\) packet in (2) does not
cover every index. Its chosen fixed-cutoff holomorphic
representative cannot replace \(C_0\) off grid without
retaining the new aliases and joins. The earlier adjacent-pair
theorem with an already closed ordinary endpoint is a
different observation and does not prove the two-Fourier-end
assertion.

In particular (18a) separates the actual pair saddle from the
real incoming centers by more than \(1/20\) in height. The
fixed-cutoff packet has a positive but not quantitatively
specified complex radius; it has not been proved to reach
this saddle. The direct two-index regular chart (4) does
contain it, with all arguments on their original strips.

