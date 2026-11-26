# The outgoing Wall saddle throughout the high physical-index range

Research deduction, 7 November 2026. The original outgoing quadratic
has a single regular stationary branch throughout the whole high
physical-index interval. Its logarithmic lift and triangular support
chamber agree with the branch selected at the endpoint by the actual
finite Wall solution. This is an analytic continuation result, without
a numerical root calculation.

The final section identifies one explicit polynomial separation
condition that would extend the proved initialized finite asymptotic
to the whole half-degree range. That condition is not asserted here.
The original full-cap supporting-plane comparison also remains separate.

## 1. A unit-circle exclusion for the outgoing quadratic

Use the fixed original \(Y=e^{2\pi ix_0}\). The inherited analytic
bounds, proved in the
[allocation-curvature theorem](research_mixed_fourier_allocation_curvature.md),
are
\[
 \frac{121}{200}<\rho=|Y|<\frac{123}{200},\qquad
 \frac25<\cos\phi<\frac{21}{50},\qquad
 \frac9{10}<\sin\phi<\frac{921}{1000},\qquad \phi=\arg Y.
 \tag{1}
\]
Put
\[
 c_0=Y^{-1}-1=a-ib,\qquad L=|c_0|^2-1.
\]
Direct use of (1) gives
\[
 -\frac7{20}<a<0,\qquad
 \frac{60}{41}<b<\frac{921}{605},\qquad
                         \frac54<L<\frac{10}{7}.
 \tag{2}
\]
For the last bounds, use
\[
 L=\frac{1-2\rho\cos\phi}{\rho^2},\qquad
 \frac{19336}{15129}<L<\frac{20640}{14641},
\]
and compare these fractions with \(5/4\) and \(10/7\).
For the first bound on \(a\), one has
\(-43/123<a<-37/121\). All these comparisons use strict
inherited bounds; no value is evaluated anew.

For \(0<\theta\le\pi\), set \(S=e^{i\theta}\). The original
outgoing equation is
\[
                 Q^2-(2+c_0-S)Q+c_0=0.
 \tag{3}
\]
Write \(w=2+c_0-S\). A root on \(|Q|=1\) would satisfy
\(w=Q+c_0\overline Q\), and hence
\[
            |w-c_0\overline w|^2-L^2=0.
 \tag{4}
\]
We prove that the left side is positive throughout this semicircle.

For \(0<\theta<\pi\), put \(T=\tan(\theta/2)>0\). Direct
expansion gives
\[
 |w-c_0\overline w|^2-L^2
       =\frac{4T}{(1+T^2)^2}\,P(T),
 \tag{5}
\]
where
\[
 P(T)=[2+a(L-2)]T^3-b(4-L)T^2
                       +[2+a(L+2)]T+bL.
 \tag{6}
\]
For example (5) follows by writing \(S=x+iy\):
\[
 w-c_0\overline w
    =-L+(1-S)-c_0(1-\overline S),
\]
and then substituting
\(x=(1-T^2)/(1+T^2)\), \(y=2T/(1+T^2)\).
The bounds (2) imply
\[
 P(T)>2T^3-\frac{21}{5}T^2+\frac45T+\frac95.
 \tag{7}
\]
Indeed the cubic coefficient exceeds 2,
\(b(4-L)<(921/605)(11/4)<21/5\), the linear coefficient exceeds
\(2-(7/20)(24/7)=4/5\), and \(bL>75/41>9/5\).

The lower cubic is positive for every \(T\ge0\). To see this
without solving for its extrema, put \(v=T-5/4\), so \(v\ge-5/4\).
Then
\[
 \begin{split}
 10T^3-21T^2+4T+9
   &=10v^3+\frac{33}{2}v^2-\frac{13}{8}v+\frac{23}{32}\\
   &\ge4v^2-\frac{13}{8}v+\frac{23}{32}>0.
 \end{split}
 \tag{8}
\]
The first inequality uses \(10v+33/2\ge4\); the final quadratic
has discriminant \(-567/64<0\). At \(\theta=\pi\), the left
side of (5) is its limiting value
\(4[2+a(L-2)]>0\). This proves the claimed exclusion.

**Lemma 1.** Equation (3) has exactly one root in the unit disk
for every \(0<\theta\le\pi\). That root is nonzero and simple.

*Proof.* No root crosses the unit circle, by (4)--(8). The number
inside is therefore constant on this connected interval. At
\(S=-1\), the existing
[half-plane branch theorem](research_mixed_fourier_endpoint_halfplane_branch.md),
Proposition 1, gives exactly one. The constant term is nonzero,
and the other root is \(c_0/Q\), of modulus greater than one
because \(|c_0|>1\). In particular the roots are distinct.
\(\square\)

## 2. The original triangular chamber and logarithmic lift

Set \(t=\theta/(2\pi)\), \(z=e^{-2\pi it}\), and take the
root \(Q(t)\) from Lemma 1. At \(t=0\) it continues as \(Q(0)=1\):
the other root there is \(c_0\), outside the unit disk. The
[initialized endpoint-strip proof](research_mixed_fourier_right_cap_wall_endpoint_strip.md)
fixes the local logarithm
\[
 q(t)=-\frac{\log Q(t)}{2\pi i},\qquad
 q(t)=\frac{Y}{2Y-1}\,t+O(t^2),
 \tag{9}
\]
and gives \(0<\Re q(t)<t\), \(\Im q(t)<0\) for small positive
\(t\). We now continue those inequalities to \(t=1/2\).

First, \(Q(t)\) cannot cross either real ray inside the unit disk.
The inverse relation is
\[
                         S=2+c_0-Q-c_0/Q.
 \tag{10}
\]
If \(0<Q=k<1\), its real part is
\(2-k+a(1-1/k)>1\), incompatible with \(S=e^{2\pi it}\).
If \(Q=-k\), \(0<k<1\), its imaginary part is
\(-b(1+1/k)<0\), also incompatible. Thus \(Q(t)\) stays in
the lower half-disk, its argument is in \((-\pi,0)\), and
\[
                      0<\Re q(t)<1/2,
                          \qquad \Im q(t)<0.
 \tag{11}
\]

It remains to exclude the moving upper wall \(\Re q=t\).
At such a point \(Q=kz\), \(0<k<1\). The original equation
\(Y(1-SQ)=(1-Q)(1-YQ)\) would give
\[
                   Y^{-1}=kz+\frac{1-k}{1-kz}.
 \tag{12}
\]
For \(z=e^{-i\theta}\), \(0\le\theta\le\pi\), its right side
has imaginary magnitude
\[
 k\sin\theta+
    \frac{(1-k)k\sin\theta}{1+k^2-2k\cos\theta}<\frac75.
 \tag{13}
\]
Here is a uniform elementary proof. The circle identity
\[
 \left|\frac1{1-kz}-\frac1{1-k^2}\right|
                            =\frac{k}{1-k^2}
\]
bounds the second term in (13) by \(k/(1+k)<1/2\).
If \(\sin\theta\le9/10\), this proves (13) immediately.
Otherwise \(\cos\theta<9/20\), and the denominator is greater
than
\[
       1+k^2-\frac9{10}k
         =\left(k-\frac9{20}\right)^2+\frac{319}{400}.
\]
The second term is then at most \(100/319\), since
\(k(1-k)\le1/4\). The whole expression is less than
\(419/319<7/5\). But (2) gives
\(|\Im Y^{-1}|=b>60/41>7/5\), contradicting (12).

Starting with the strict local inequality in (9), continuity and
this wall exclusion prove the full statement:
\[
 \boxed{\quad
        0<\Re q(t)<t,\qquad \Im q(t)<0,
                          \qquad 0<t\le1/2.
 \quad}
 \tag{14}
\]
All original factorial arguments \(q\) and \(1-t+q\) therefore
stay in their regular strips. Also \(|YQ|<1\), so the original
cardinal branch stays regular. The outgoing logarithmic residual
vanishes initially by the endpoint-strip proof; its exponential is
one everywhere. Continuous continuation on this regular chamber
keeps its value zero. Thus this is the original stationary branch,
not only a root of its exponentiated equation.

The stationary point is nondegenerate. The two roots of (3) are
distinct; the derivative of its numerator with respect to \(Q\)
is therefore nonzero. The denominators \((1-Q)(1-YQ)\) and
\(dQ/dq=-2\pi iQ\) are nonzero. Differentiating the original
logarithmic equation consequently gives
\(\partial_q^2[g(1-t+q)-g(q)+\ell_q(y)]\ne0\).

## 3. What would extend the actual finite asymptotic

The branch conclusion (14) is unconditional. The following condition
on the *degree* roots is an additional, explicit premise; their
moduli are not determined merely by \(|Q|<1\).

For \(z=e^{-2\pi it}\), \(0\le t\le1/2\), put
\[
 A=z(1-Yz),\qquad C=Yz(1-z),\qquad D=A+C-Y,
 \qquad P(R)=AR^2-DR+C.
 \tag{15}
\]
The fixed separation condition is
\[
      |A\overline D-D\overline C|^2
                -( |A|^2-|C|^2)^2>0
                   \qquad(0\le t\le1/2).
 \tag{16}
\]
It is a real polynomial test on the lower unit semicircle and
the original \(Y\). In particular, if
\(Y=p+iv\), \(k=|Y|^2\), \(u=k-p\),
\(z=c-is\), \(c^2+s^2=1\), \(s\ge0\), its left side is exactly
\[
 (uc+vs)[2(1-k)+5uc-3vs]
                 +[vc+(p+k)s-4kcs]^2.
 \tag{17}
\]
To check this identity, write
\[
 \begin{split}
 h&=|A|^2-|C|^2=1-k+2uc-2vs,\\
 B&=A\overline D-D\overline C
       =h-\overline Yz+k\overline z+k(z^2-\overline z^2),\\
 \Re B&=1-k+3uc-vs,\qquad
 \Im B=vc+(p+k)s-4kcs.
 \end{split}
 \tag{18}
\]

**Proposition 2, conditional on (16).** The actual finite solution
and amplitude theorem of the initialized endpoint-strip note extend
uniformly to \(0\le n/N\le1/2\), with the same formulas (17)--(19)
there and the same exact normalization. Its action remains the
original critical action of (14). No additional connection-coefficient
premise is required.

*Proof.* First (16) puts exactly one degree root inside and one
outside the unit circle. Here is a direct Schur--Cohn argument.
Let \(P^*(R)=\overline C R^2-\overline D R+\overline A\).
Then
\[
 \overline A P-C P^*=R(hR-\overline B).
 \tag{19}
\]
If \(h>0\), Rouché's theorem on the unit circle identifies the
zero count of the left side with that of \(P\). The right side
has one zero inside, because \(|B|>|h|\). If \(h<0\), compare
instead with \(-CP^*\); it again has one inside zero, so \(P\)
has one as well. If \(h=0\), (16) excludes unit roots and a small
coefficient perturbation reduces to either preceding case. The
constant \(C\) may vanish at \(t=0\); then \(h>0\), and (19)
still applies. Also \(A\ne0\) since \(|Y|<1\).

The outside root \(R_+\) is simple, nonzero and analytic along
the interval, and its ratio-map derivative is
\[
                 \frac{C}{AR_+^2}=\frac{R_-}{R_+}.
 \tag{20}
\]
Its modulus has a uniform upper bound strictly below one by
compactness. These conclusions persist on a common small complex
neighborhood of the interval and of \(Y\), and for sufficiently
small \(\varepsilon=1/N\) in the exact finite coefficients (8)
of the endpoint-strip note. A uniform small disk about the root
therefore satisfies that note's contraction bound (12).

At zero, the outside root is precisely \((1-2Y)/(1-Y)\),
and the original initial ratio is still (14) of that note.
The same initialized induction, first-order correction and
endpoint-corrected Riemann sum now prove its actual finite
asymptotic throughout this larger compact interval. All constants
are uniform; no independent initial solution is inserted.

For \(t>0\), the transformation
\[
                         R=\frac{z-1}{z-Q}
 \tag{21}
\]
maps the two outgoing roots to the two degree roots. At small
positive \(t\), (14)'s branch maps to the initialized outside
root. Neither pair collides, and \(|Q|<1\) keeps \(z-Q\ne0\).
Continuation therefore identifies it with \(R_+\) everywhere.
The original log lift from Section 2 continues the action identity
(27) of the endpoint-strip note. This proves the proposition.
\(\square\)

No proof of (16) is supplied by (5)--(8): those calculations concern
the different outgoing quadratic. Likewise, even a proof of (16)
and the resulting asymptotic would still leave the final retained-index
sum and its comparison with the full right-cap supporting plane.
The exact physical wedge is retained inside the contraction; it is
not removed from the original source or paid by a positive norm.
