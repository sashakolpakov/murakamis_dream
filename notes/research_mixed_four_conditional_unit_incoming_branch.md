# The original type-four branch on the whole upper incoming unit semicircle

Private written deduction, 10 November 2026. The original type-four
conditional cubic has exactly one simple upper root throughout the
upper incoming unit semicircle, excluding \(X=1\), when the outgoing
coordinate is below the real axis and to the left of one. The root
stays strictly before the incoming numerator wall, on the original
zero logarithmic lift.

This extends an algebraic branch domain. It does not estimate a
finite conditional sum, prove an action derivative sign, or pay a
remaining outer contour.

## 1. Literal source, phase and parameter set

Retain the finite polynomial in
[the original torus source, equation (1)](research_mixed_conditional_torus_composition.md),
\[
 C_{1,N}(X,Y)=
 \sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^3},
 \qquad q_N=e^{-2\pi i/N}.
 \tag{1}
\]
The incoming carrier \(X^{-j}\) and all indices remain unchanged.
The phase and exponential critical equation are those of
[the algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md):
\[
 \begin{split}
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 g'(z)&=\operatorname{Log}(1-e^{-2\pi iz}),\qquad 0<\Re z<1,\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad v=e^{2\pi it},\\
 e^{Q_t}&=\frac{v(v-X)(v-Y)}{X(v-1)^3}.
 \end{split}
 \tag{2}
\]
The primitive constants and logarithms are the original ones.

The new parameter set is
\[
 \mathcal U=\{X:|X|=1,\ \Im X>0\}\cup\{-1\},\qquad
 \mathcal Y=\{Y:\Im Y<0,\ \Re Y<1\}.
 \tag{3}
\]
Use the continuous arguments \(0<\Arg X\le\pi\) and
\(-\pi<\Arg Y<0\), and set
\[
 a=1-\frac{\operatorname{Log}X}{2\pi i},\qquad
 y=-\frac{\operatorname{Log}Y}{2\pi i}.
 \tag{4}
\]
Thus \(a\) is real, \(1/2\le a<1\), and \(0<\Re y<1/2\).
There is no restriction on \(|Y|\) beyond (3).

**Theorem 1.** For every parameter pair in (3), the original cubic
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0
 \tag{5}
\]
has exactly one upper-half-plane root, counted with multiplicity.
It is simple and satisfies
\[
 0<\arg v<\Arg X,\qquad
 t=\frac{\operatorname{Log}v}{2\pi i},\qquad
 0<\Re t<1-a,\qquad Q_t(t;a,y)=0 .
 \tag{6}
\]
The root and the original critical phase are holomorphic locally in
the parameters. On each compact subset of (3), the simplicity and
strict strip margins persist on a fixed neighborhood.

No uniform strip margin is asserted as \(X\) approaches the excluded
endpoint \(1\).

## 2. The upper root count

Equation (5) is equivalent to
\[
 v(v-X)(v-Y)=X(v-1)^3.
 \tag{7}
\]
It excludes \(v=0,1,X\). Solving for the outgoing parameter gives
\[
                  Y=v-\frac{X(v-1)^3}{v(v-X)}.
 \tag{8}
\]
For a real \(v\), with \(\Im X>0\), the exact identity from the
[original negative-height branch proof](research_mixed_conditional_negative_height_branch.md)
is
\[
              \Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
 \tag{9}
\]
If \(v<1\), this contradicts \(\Im Y<0\). If \(v>1\), write
\(c=\Re X\), \(\delta=1-c>0\), and use \(|X|=1\). Directly
from (8),
\[
 \begin{split}
 \Re Y-1
 &=\frac{v-1}{v|v-X|^2}
       \left\{v|v-X|^2-(v-1)^2(vc-1)\right\}\\
 &=\frac{v-1}{v|v-X|^2}
       \left\{(v-1)^2+\delta v(v^2+1)\right\}>0 .
 \end{split}
 \tag{10}
\]
This contradicts \(\Re Y<1\). At \(X=-1\), (8) is real
for every permitted real \(v\), also impossible. Thus no root
crosses the real axis anywhere on (3).

The set (3) is connected. At \(X=-1,\ Y=-i\), the same original
anchor factorization is
\[
 (v-i)\{2v^2+(-2+3i)v-i\}.
 \tag{11}
\]
The two quadratic roots have negative imaginary part. Indeed, if
\(\sqrt{-5-4i}=A-iB\) with \(A,B>0\), then
\(B^2=(\sqrt{41}+5)/2<9\), and those imaginary parts are
\((-3+B)/4\) and \((-3-B)/4\).
The sole upper root is therefore \(v=i\).

Along any compact parameter path in (3), the coefficients remain
bounded and \(1-X\) stays away from zero. No root escapes to infinity.
Together with (9)--(10), this preserves upper root count one.
A multiple upper root would count at least twice, so the upper
root is simple.

## 3. Excluding the whole incoming numerator ray

For \(\Im X>0\), a point on that ray has \(v=sX\), \(s>0\);
\(s=1\) has already been excluded. Specializing the exact identities
in the negative-height branch proof, equation (12), to \(|X|=1\)
and writing \(\delta=1-\Re X>0\), gives
\[
 \Im Y=\Im X\,\frac{\mathcal N}{s(s-1)},\qquad
 \Re Y-1=\frac{\mathcal S}{s(s-1)},
 \tag{12}
\]
where
\[
 \begin{split}
 \mathcal N&=s^3(-1+2\delta)+2s^2-1,\\
 \mathcal S&=(s-1)^2+
       \delta(3s^3-2s^2-1)-2s^3\delta^2.
 \end{split}
 \tag{13}
\]
These formulas retain the signs of both the real and imaginary
outgoing conditions. No radius assumption on \(Y\) is used.

First let \(0<s<1\). The condition \(\Im Y<0\) forces
\(\mathcal N>0\), hence
\[
 \delta>\delta_0:=
       \frac{(1-s)(1+s-s^2)}{2s^3}>0.
 \tag{14}
\]
For fixed \(s\) in this range, \(\mathcal S\) decreases strictly
with \(\delta\ge0\), because
\[
 \partial_\delta\mathcal S
 =(s-1)(3s^2+s+1)-4s^3\delta<0.
 \tag{15}
\]
Using \(2s^3\delta_0=(1-s)(1+s-s^2)\) gives
\[
 \mathcal S(\delta_0)
 =(1-s)\{(1-s)-2\delta_0(1+s+s^2)\}<0.
 \tag{16}
\]
For the last inequality,
\((1+s-s^2)(1+s+s^2)>1>s^3\).
Thus \(\mathcal S<0\). Its denominator in (12) is negative,
so \(\Re Y>1\), a contradiction.

Next let \(s>1\). Now \(\Im Y<0\) forces \(\mathcal N<0\).
Writing \(\mathcal A=s^3-2s^2+1\), this means
\[
                        2s^3\delta<\mathcal A,\qquad
                        \mathcal A>0.
 \tag{17}
\]
Consequently
\[
 \begin{split}
 \mathcal S
 &>(s-1)^2+
       \delta\{3s^3-2s^2-1-\mathcal A\}\\
 &=(s-1)^2+2\delta(s^3-1)>0 .
 \end{split}
 \tag{18}
\]
Its denominator in (12) is positive, again giving \(\Re Y>1\).
Both possible ray ranges are excluded.

At \(X=-1\), the incoming ray is the negative real axis and
cannot contain the upper root. There the root has
\(\arg v<\pi=\Arg X\). Continuity, the upper root count, and
the ray exclusions now preserve \(0<\arg v<\Arg X\) everywhere
on (3).

## 4. Original logarithmic lift and exact scope

The strip conclusion in (6) puts
\[
              t,\ a,\ y,\ a+t,\ y+t
                 \quad\hbox{in }0<\Re z<1.
 \tag{19}
\]
For the last argument, use \(\Re y<1/2\) and
\(\Re t<1-a\le1/2\).
Every logarithm in (2) is therefore its original strip branch.
Equation (7) says \(Q_t\in2\pi i\mathbb Z\).
At the anchor \(a=1/2,\ y=t=1/4\), the exact identity
\[
                 g'(3/4)+g'(1/2)-3g'(1/4)+\pi i=0
 \tag{20}
\]
fixes this lift to zero. Connected continuation proves \(Q_t=0\).

Simplicity gives local holomorphic continuation of the same root,
and (19) gives the original holomorphic critical action
\(\Theta(a,y)=Q(t(a,y);a,y)\), without an additive phase change.
On compact parameter sets all strict margins have positive minima.
This proves Theorem 1.

The original stationary derivative identity still gives
\[
             e^{\Theta_a}=\frac{v-X}{1-X}.
 \tag{21}
\]
No half-plane or modulus assertion for this multiplier is made on
the newly added arc. In particular (21) is not an extension of the
previous action monotonicity theorem.

The finite polynomial (1) is unchanged at both parities. This
algebraic deduction removes no physical row, Fourier current,
endpoint or connector, and bounds none of them. Its application to
the remaining real first-coordinate interval requires a separate
complete finite-source comparison.

## Frozen source bindings

| Direct source | SHA-256 |
|---|---|
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |
| research_mixed_four_conditional_algebraic_transport_domain.md | 4788b140b0ab435bb5951db75aadad03376ddaf3bfb6378b8f17242253b7ace0 |
| research_mixed_conditional_negative_height_branch.md | 2bb12f853dec6cf3a0ab56acfee21b8ce21f47f176e9a9d999237ab0d12e6a46 |
