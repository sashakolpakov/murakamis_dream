# Full inner dominance above the golden-ratio radius

Research deduction, 7 November 2026. A direct modulus comparison
extends the symmetric inner maximum of the actual merged-pair
phase down to total real part \(1/2\). It applies on the whole
difference interval of length one, including the portions whose
physical rows vanish. The criterion is the external radius exceeding
the golden ratio, rather than a numerical test at the critical point.

This is a phase theorem. The finite-source continuation and the
outer sampling contours still retain their own domain and remainder
requirements. No numerical evaluation is used.

## 1. Statement in the original phase

Let
\[
 \frac{\pi}{3}<\theta<\frac{\pi}{2},\qquad
 S>\frac{1+\sqrt5}{2},\qquad
 x=\frac{\theta}{2\pi}+\frac{i\log S}{2\pi}.
\tag{1}
\]
Thus \(X=e^{-2\pi ix}=S e^{-i\theta}\). Let
\[
 c=\gamma+iH,\qquad
          \frac12\le\gamma<1,\quad H\ge0,\quad r=e^{\pi H}\ge1.
\tag{2}
\]
For \(-1/2\le t\le1/2\), set \(a=c/2+t\), \(s=c/2-t\), and use
the exact merged phase
\[
\begin{split}
 F_c(a;x)={}&g_+(c)+g_+(a+x)+g_+(c-a+x)\\
 &-2g_+(a)-2g_+(c-a)-2g_+(x)+2\pi ia(c-a).
\end{split}
\tag{3}
\]
Here \(g_+\) is the original upper continuation, with its
absolute constant:
\[
 g_+(z)=\pi iz(1-z)
       +\frac{i}{2\pi}
              \{\operatorname{Li}_2(e^{2\pi iz})-\pi^2/6\}.
\tag{4}
\]
At zero height in an own argument, (3) means its continuous
upper boundary value. Its real part is continuous even at an
integer; logarithmic derivatives there are taken one-sided.
No symbol estimate at such a point is implied.

**Theorem 1.** The real function
\[
                  t\longmapsto\Re F_c(c/2+t;x)
\tag{5}
\]
is strictly decreasing for \(0<t<1/2\), and strictly increasing
for \(-1/2<t<0\). Consequently its unique global maximum on
the entire closed interval is \(t=0\).
Its actual complex derivative at zero is zero, and
\[
 \Re\left[
       2\pi\{\cot\pi(c/2+x)-2\cot(\pi c/2)-i\}
    \right]<0.
\tag{6}
\]
On compact parameter families satisfying (1)--(2), this gives
a uniform nondegenerate central maximum and a uniform phase gap
outside any fixed central neighborhood.

The conclusion concerns the full interval, not only the
original physical support at a real total.

## 2. Exact squared-modulus comparison

Put \(C=\pi\gamma\), \(D=2\pi t\). The real derivative of (3) is
\[
 \frac{d}{dt}\Re F_c(c/2+t;x)
   =\frac12\log\frac{P_+}{P_-}
                    -\log\frac{Q_+}{Q_-},
\tag{7}
\]
where
\[
\begin{split}
 P_\pm&=|1-Sr e^{-i(C+\theta\pm D)}|^2,\\
 Q_\pm&=|1-r e^{-i(C\pm D)}|^2.
\end{split}
\tag{8}
\]
The chirp derivative is \(-4\pi it\), whose real part is zero.
The numerator factors in (8) never vanish, since \(Sr>1\).

If \(C+\theta\ge\pi\), then for \(0<D<\pi\),
\[
 P_+-P_-=4Sr\sin(C+\theta)\sin D\le0,\qquad
 Q_+-Q_-=4r\sin C\sin D>0.
\tag{9}
\]
This already proves strict negativity in (7), wherever it
is finite. It remains to treat
\[
                    \pi/2\le C\le\pi-\theta .
\tag{10}
\]

Write
\[
\begin{gathered}
 p=-\cos C\ge0,\qquad b=\sin C>0,\qquad p^2+b^2=1,\\
 u=\cos\theta>0,\qquad v=\sin\theta>u,\qquad
 f=bu-pv=\sin(C+\theta)\ge0,\\
 g=pu+bv=-\cos(C+\theta)>0,\qquad z=\cos D.
\end{gathered}
\tag{11}
\]
In this range \(0\le p\le u<1/2\). With
\[
 q_0=1+r^2+2rpz,\qquad
 p_0=1+S^2r^2+2Sr g z,
\tag{12}
\]
the quantities in (8) are
\[
 Q_\pm=q_0\pm2rb\sin D,\qquad
 P_\pm=p_0\pm2Sr f\sin D .
\tag{13}
\]
To prove (7) negative, it suffices to prove
\[
                         P_+Q_-^2-P_-Q_+^2<0.
\tag{14}
\]
Direct expansion factors the left side as
\[
 4r\sin D\,E(z),\qquad
 E(z)=Sf\{q_0^2+4r^2b^2(1-z^2)\}-2b p_0q_0 .
\tag{15}
\]
No approximation of the factors is used in this identity.

## 3. Two monotonic polynomial reductions

The coefficient of \(z^2\) in \(E\) and its coefficient of \(z\)
are respectively
\[
 \begin{split}
 -4Sr^2(bu+pv),\qquad
 -4r\{S(1+r^2)v+b(1+S^2r^2)p\}.
 \end{split}
\tag{16}
\]
For example the quadratic coefficient uses
\[
 f(p^2-b^2)-2bgp=-(bu+pv),
\]
and the linear coefficient uses \(pf-bg=-v\).

Moreover
\[
 bu+pv=\sin(C-\theta)\le\sin(2\theta)<\sin\theta=v .
\tag{17}
\]
Indeed \(C-\theta\) lies between \(\pi/2-\theta\) and
\(\pi-2\theta\), both in \((0,\pi/2)\); and
\(\sin(2\theta)=2uv<v\), since \(u<1/2\).
Using \(1+r^2\ge2r\), (16)--(17) imply \(E'(z)<0\)
on the full interval \([-1,1]\). Hence \(E(z)\le E(-1)\).

At \(z=-1\), let \(q_-=1+r^2-2rp>0\). Since the term
containing \(1-z^2\) vanishes, (15) becomes
\[
                         E(-1)=q_-\,b\,G(p),
\tag{18}
\]
where
\[
\begin{split}
 G(p)={}&S\left(u-\frac pbv\right)(1+r^2)
          -2(1+S^2r^2)\\
       &+2Sr\left\{pu+\frac{2-p^2}{b}v\right\},
       \qquad b=\sqrt{1-p^2}.
\end{split}
\tag{19}
\]
Its exact derivative is
\[
 G'(p)=\frac{S}{b^3}
       \{-v(1+r^2)+2r(ub^3+vp^3)\}<0.
\tag{20}
\]
To see the strict sign, \(u<v\) and
\(b^3+p^3\le b^2+p^2=1\) give
\(ub^3+vp^3<v\); then use \(1+r^2\ge2r\).
Consequently \(G(p)\le G(0)\).

The remaining quadratic is
\[
 G(0)=(Su-2S^2)r^2+4Svr+Su-2 .
\tag{21}
\]
It strictly decreases for \(r\ge1\). Its leading coefficient
is negative, and its derivative at \(r=1\) is negative because
\[
                 u+2v\le\sqrt5<2S .
\tag{22}
\]
Finally
\[
 G(0)\big|_{r=1}
       =2\{S(u+2v)-1-S^2\}
       \le2\{\sqrt5S-1-S^2\}<0.
\tag{23}
\]
The last inequality is exactly the larger-root condition
\(S>(1+\sqrt5)/2\) in (1). Equations (18)--(23) show
\(E(-1)<0\), hence \(E(z)<0\), proving (14).

If \(r=1\) and \(Q_-=0\) at an interior \(t\), the left side
of (14) is still strictly negative. In (7) the derivative
tends to \(-\infty\) at that point. Its logarithmic
singularity is integrable, and the continuous real phase
strictly decreases through it. Thus no zero-height own
endpoint has been omitted.

## 4. Nondegeneracy, actual domain, and remaining source requirements

Symmetry of (3) makes its complex derivative at \(t=0\) exactly
zero, with its original logarithms. In the case (10), the strict
inequality \(E(1)<0\) shows that the coefficient of \(t\) in
(7) is strictly negative. Explicitly it is
\[
 \frac{4\pi r\,E(1)}
 {(1+S^2r^2+2Sr g)(1+r^2+2rp)^2}<0.
\tag{24}
\]
It equals the real part in (6). In the case \(C+\theta\ge\pi\),
that same sign follows directly from the cotangent formula:
the shifted real cotangent is nonpositive and the own real
cotangent is positive. This proves nondegeneracy in every case.
Continuity and the strict global comparison prove the compact
uniform conclusions of Theorem 1.

For the actual output \(x_0=\xi+i\upsilon\), the existing bounds
give \(1/6<\xi<1/4\) and \(S>163/100>(1+\sqrt5)/2\).
The latter follows, for example, from
\((163/100)^2-163/100-1=269/10000>0\).
Thus Theorem 1 applies for every total real part
\(1/2\le\Re c<1\) and nonnegative total height.

For a fixed positive total height, all own arguments in (3)
are in the upper half-plane, even if their real parts are
negative. The original upper factorial continuation supplies
their specified phases and symbols. All shifted numerator
arguments have height \(\Im c/2+\Im x>0\), including when
their real parts cross zero or one. The reciprocal arguments
have real part less than one. These facts explain the
admissible phase branches, but a whole finite-source theorem
must still prove its uniform bounds at zero-height own walls.

In particular, extending \(\Re c\) down to \(1/2\) can put a
shifted numerator at negative real part. A lower total-index
deformation can then meet its negative-grid poles when
\(\Im c=-2\Im x\). This theorem does not cross those poles
or remove their residues. The complete outer contour,
its parity sampling, complementary totals, and the original
closing functional remain separate.
