# Newton row curvature on the wider right hyperbola

Private written profile deduction, 9 November 2026. The original
complete diagonal Newton profile has height curvature less than
\(4/(3\pi)\) on an explicit polygon in its cosine variables.
Every height below the right hyperbola lies in that polygon.
This supplies a quadratic outgoing-height cost with its real-angle
loss retained. An attached finite-current comparison is separate.

No mathematical numerical evaluation, saved-value arithmetic, import,
compilation, test, or frozen-source edit is used.

## 1. Original profile and statement

Retain the complete lower-half row profile of the
[original low-horizontal theorem, (5)--(17)](research_mixed_symmetric_closing_low_horizontal_norm.md):
\[
 J(y)=\int_0^y\log(2\sin\pi x)\,dx,\qquad
 V_{\beta-ih}(y)=
 \int_0^y\log|2\cos(2\pi x)+2\cos(\beta-ih)|\,dx-2J(y),
\]
\[
 m(\beta,h)=\max_{0\le y\le1/2}V_{\beta-ih}(y),\qquad
 p=\cos\beta,\quad q=\cosh h .
 \tag{1}
\]
The literal finite Newton rows obey the zero-safe upper bound
\[
 |e_j(-2\cos(\beta-ih))|
 \le CN^A e^{NV_{\beta-ih}(j/N)},\qquad
 0\le j\le\lfloor N/2\rfloor-1,
 \tag{2}
\]
on fixed bounded angle-height sets, at both parities. The maximum
in (1) is over the entire lower half, including the rows after
a possible real numerator zero.

**Theorem.** On the closed polygon
\[
 -\frac12\le p\le0,\qquad
                 1\le q\le\frac{13}{10}+\frac p4,
 \tag{3}
\]
the unique maximizing row is regular and interior, and
\[
                         m_{hh}(\beta,h)<\frac4{3\pi}.
 \tag{4}
\]
For every fixed \(0<K_0\le7/10\), the whole set
\[
 \frac\pi2\le\beta\le\frac{2\pi}3,\qquad
              0\le h\le K(\beta):=\frac{\pi K_0}{2\beta}
 \tag{5}
\]
lies in (3). Consequently
\[
 m(\beta,K(\beta))
 \le m(\beta,0)+\frac{2K(\beta)^2}{3\pi}
 \le b_2-\frac{1-\cos\beta}{2\pi}
                         +\frac{2K(\beta)^2}{3\pi}.
 \tag{6}
\]
The actual \(K_0=K_g\) is eligible by the adopted geometric
height theorem. Neither a finite inner packet nor a closing
current bound is asserted by (4)--(6).

## 2. Regularity and an elementary two-variable reduction

Put
\[
 r=-p,\qquad s=q-r,\qquad v=(q+r)/2,\qquad A=1-v^2 .
 \tag{7}
\]
On (3), \(0\le r\le1/2\), \(q\ge1\), and
\[
 1+pq=1-rq\ge7/20>0,\qquad s\ge1/2,\qquad
                         v\le67/80<1.
 \tag{8}
\]
Thus the original maximizing-row formula and original mirror
return in (10),(13)--(17) of the cited theorem apply. In
particular, no logarithm is continued through a numerator zero
at the maximizing row, and \(m_h(\beta,0)=0\). Their exact
curvature is
\[
 \pi m_{hh}
 =\frac{(1+pq)/(q+p)+(q-p)/2}{2\sqrt{1-(q-p)^2/4}},
\]
or equivalently
\[
 2\pi m_{hh}
        =\frac{\sqrt A}{s}+\frac{s/4+v}{\sqrt A}.
 \tag{9}
\]
All roots and denominators in (9) are positive.

The map \((r,q)\mapsto(v,s)\) is linear and invertible.
At each fixed \(v\), the right side of (9) is strictly
convex in \(s>0\): its second derivative is
\(2\sqrt A/s^3>0\). Its maximum on each line segment of
the polygon is therefore attained at an endpoint of that
segment. It suffices to prove (4) on the four boundary
edges
\[
             q=1,\quad r=0,\quad r=1/2,\quad
                         q=13/10-r/4.
 \tag{10}
\]
This is convexity in one coordinate on a fixed polygon,
not an assertion of joint convexity.

## 3. Three boundary edges

If \(q=1\), then \(v=(1+r)/2\in[1/2,3/4]\) and
\(s=2(1-v)\). Equation (9) reduces exactly to
\[
 \pi m_{hh}=\frac12\sqrt{\frac{1+v}{1-v}}
                 \le\frac{\sqrt7}{2}<\frac43,
 \tag{11}
\]
where the last squared comparison is \(63<64\).

If \(r=0\), then \(1\le q\le13/10\) and
\[
 \pi m_{hh}=\frac{2+q^2}{2q\sqrt{4-q^2}}.
 \tag{12}
\]
Squaring positive quantities, (4) is equivalent to
\[
                   220q^2-73q^4-36>0.
 \tag{13}
\]
This polynomial is concave in \(q^2\). Its values at the
two endpoints are \(111\) and \(1273047/10000\), respectively.
Both are positive, proving (13) on the whole edge.

If \(r=1/2\), then \(1/2\le s\le27/40\), and
\[
 \pi m_{hh}
     =\frac{3+2s^2}{4s\sqrt{3-2s-s^2}} .
 \tag{14}
\]
Again all quantities are positive. The squared comparison
with \(4/3\) is precisely
\[
 P_1(s)=-292s^4-512s^3+660s^2-81>0 .
 \tag{15}
\]
Here
\[
 P_1''(s)=1320-3072s-3504s^2\le-1092<0.
 \tag{16}
\]
Its minimum on this interval is consequently at an
endpoint. The exact endpoint identities are
\[
 P_1(1/2)=7/4,\qquad
                     40^4P_1(27/40)=4175388>0 .
 \tag{17}
\]
For example the latter numerator is
\[
 -292\cdot531441-512\cdot19683\cdot40
          +660\cdot729\cdot1600-81\cdot2560000
 =4175388 .
\]
This proves the third edge without an interior extremum calculation.

## 4. The sloped boundary, with its written polynomial certificate

On \(q=13/10-r/4\), \(0\le r\le1/2\), write
\[
 s=\frac{26-25r}{20},\qquad
 v=\frac{26+15r}{40},\qquad
 a(r)=924-780r-225r^2,\quad
 n(r)=2952-2600r-350r^2 .
 \tag{18}
\]
Then \(A=a/1600\), and
\[
 A+s(s/4+v)=n/1600,\qquad
                   \pi m_{hh}=\frac{n}{4(26-25r)\sqrt a}.
 \tag{19}
\]
The quantities \(a,n,26-25r\) are positive by (8)--(9).
Thus (4) is equivalent to the strict polynomial inequality
\[
 \begin{split}
 P_2(r)&=256(26-25r)^2a(r)-9n(r)^2\\
 &=81475008-304337280r+326244000r^2
                         -66300000r^3-37102500r^4>0 .
 \end{split}
 \tag{20}
\]
Its derivative signs and endpoint value have the following
fully rational witnesses on \(0\le r\le1/2\):
\[
 \begin{split}
 P_2''(r)
 &=652488000-397800000r-445230000r^2\\
 &\ge652488000-198900000-111307500
                       =342280500>0,\\
 P_2'(1/2)&=-46369530<0,\\
 P_2(1/2)&=1043847/4>0 .
 \end{split}
 \tag{21}
\]
Hence \(P_2'\) is increasing but still negative at its right
endpoint. The polynomial decreases throughout the edge and
its minimum is the positive last value in (21).
This proves (20).

All four edges are now strict. The fixed-\(v\) convexity
argument proves (4) on the entire polygon, with a uniform
strict margin by compactness.

## 5. The whole hyperbolic height segment lies in the polygon

Let \(x=2\beta/\pi\in[1,4/3]\). The positive hyperbolic-cosine
series, and the original bound \(\cosh(7/10)<13/10\), give
\[
 \cosh h-1\le
  \left(\frac{h}{7/10}\right)^2
                       \{\cosh(7/10)-1\}
 \le\frac3{10x^2}
               \qquad(0\le h\le K_0/x,\quad K_0\le7/10).
 \tag{22}
\]
This includes \(h=0\); no strict inequality there is needed.
For \(x>1\),
\[
 \frac{1-x^{-2}}{x-1}=\frac{x+1}{x^2}
        \ge\frac{21}{16}>\frac{5\pi}{12}.
 \tag{23}
\]
The function on the left after cancellation decreases in \(x\).
The last comparison follows from
\(5\pi/12<55/42<21/16\), where \(880<882\).
Also
\[
 \cos\beta=-\sin\!\left(\frac\pi2(x-1)\right)
                          \ge-\frac\pi2(x-1).
 \tag{24}
\]
Equations (23)--(24), with equality handled directly at
\(x=1\), imply
\[
                  x^{-2}\le1+\frac56\cos\beta.
 \tag{25}
\]
Combining (22),(25) gives exactly
\[
                 q=\cosh h\le\frac{13}{10}+\frac p4.
 \tag{26}
\]
The other conditions of (3) follow from the angle interval.

Integrate (4) twice along this entire height segment, using
the original \(m_h(\beta,0)=0\). This proves the first bound
in (6). The second is the original real Newton inequality
\[
 m(\beta,0)\le b_2-\frac{1-\cos\beta}{2\pi},
                       \qquad0\le\beta\le\pi,
 \tag{27}
\]
whose full-angle scope is Lemma 3 of the
[real-period theorem](research_three_crossing_real_period_newton_bound.md).
Thus (6) retains the actual angular loss; it does not replace
it by a constant maximum.

The zero-safe estimate (2) permits (6) to be inserted in the
exact finite row Cauchy--Schwarz inequality, with its original
cutoff and both parities. The remaining first-edge rate, crossing,
sampling denominator, contour orientation, and full-trace
restoration are not estimated in this note. In particular no
whole inner or outer closing conclusion follows from (6) alone.

## Frozen source bindings

- Original full row profile, its unique maximizing row, mirror
  curvature, branch, zero-safe products, and both parity cutoffs:
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Original real-angle loss on the entire real period:
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Actual geometric height \(0<K_g<7/10\), used only to insert
  that value of \(K_0\) into (5):
  6bf4646f6ec7b48dcbdbacfaacbe14ecb864c9d049114d3bd7c1b95fb66cc6f0.
