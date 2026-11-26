# An upper bound on the right part of the internal Fourier circle

Research proof, 3 November 2026.

This note bounds the original mixed source on the segment
\(3/10\le\Re x\le1/2\) of the circle through its geometric wire
coordinate. The outer Newton index stays in its real finite sum.
Only the complete-meridian trace is moved. Thus this estimate has
no outer-wire contour corrections.

Use the exact source \(W_{3,N}(x,u)\), the root \(x_*\), and the
phase \(F_x(y,t;u)\) from the
[local mixed-source theorem](research_internal_pair_three_mixed_packet.md).
Put
\[
 Y=\Im x_*,\qquad M=\Re S(x_*,0),\qquad
 I=[1/32,15/32],\qquad T=39/20,\qquad h=4/5.
 \tag{1}
\]
All constants and branches refer to that same source.

**Theorem 1.** There are \(C,p,r>0\) such that, at every integer level,
\[
 |W_{3,N}(a+iY,u)|
 \le CN^p\exp\{N(M-1/4000)\},
 \qquad 3/10\le a\le1/2,\quad |u|\le r.
 \tag{2}
\]
The parameter \(u\) is complex. The source remains its original
polynomial in \(-2\cos u\); no boundary reduction is made.

## 1. An endpoint comparison for positive trace angles

Let \(x=a+iY\), \(t=\tau-id\), with \(0\le d\le4/5\).
The real part of the continued Newton phase has derivative
\[
 \partial_a\Re b(x,t)
  =\log\left|\frac{\cos(2\pi x)+\cos t}
                         {1-\cos(2\pi x)}\right|.
 \tag{3}
\]
This equality uses the prescribed factorial side. A different
logarithmic determination changes this derivative by a purely
imaginary integer multiple of \(2\pi i\), so (3) also gives
its real derivative across the negative-real cuts used below.
The real phase is continuous there.

The sign of (3) is the sign of
\[
 D=|\cos t|^2-1+
             2\Re\{\cos(2\pi x)(1+\overline{\cos t})\}.
 \tag{4}
\]
For \(3/10\le a\le1/2\), put
\(A=-\cos(2\pi a)\cosh(2\pi Y)>3/10\).
If \(0\le\tau\le 2\pi(311/1000)\), then
\(\sin\tau\ge0\), and \(c=\cos\tau>-2/5\). Consequently
\[
 D\le c^2+\sinh^2d-1-2A(1+c\cosh d).
 \tag{5}
\]
The omitted term is
\(-2\sin(2\pi a)\sinh(2\pi Y)\sin\tau\sinh d\le0\).
The right side is convex in \(c\); its endpoint values are
\[
 \begin{array}{ll}
 c=1:&(1+\cosh d)(\cosh d-1-2A)<0,\\[2mm]
 c=-2/5:&
 \sinh^2d-21/25-2A(1-2\cosh d/5)<0.
 \end{array}
 \tag{6}
\]
Here \(\cosh(4/5)<7/5\) and \(\sinh^2(4/5)<21/25\);
the verifier encloses both inequalities outwards. Thus the
phase decreases in \(a\) on this segment for nonnegative
trace angles, at every depth up to \(4/5\). Its maximum
there is at \(a=3/10\). Negative trace angles are bounded
directly; no corresponding monotonicity is assumed.

## 2. The four phase estimates

For a real outer-wire coordinate \(y\in I\), define
\[
 F(a,y,t)=b(a+iY,t)+b(y,t)+b(y,0)
                       +3it^2/(4\pi)-it.
 \tag{7}
\]
The certificate proves the following bounds for \(\Re F\),
each strictly below \(M-1/1000\).

| Surface | Domain |
|---|---|
| Positive bottom trace | \(a=3/10,\ y\in I,\ t=2\pi q-4i/5,\ 0\le q\le311/1000\) |
| Negative bottom trace | \(3/10\le a\le1/2,\ y\in I,\ t=2\pi q-4i/5,\ -311/1000\le q\le0\) |
| Positive angular endpoint | \(a=3/10,\ y\in I,\ t=T-4is/5,\ 0\le s\le1\) |
| Negative angular endpoint | \(3/10\le a\le1/2,\ y\in I,\ t=-T-4is/5,\ 0\le s\le1\) |

Section 1 extends the first and third bounds to every \(a\)
in the segment. The enlarged bottom interval contains all
sufficiently large midpoint cutoffs \(T_N=T+O(N^{-1})\).

At a negative real factorial argument, the two prescribed
continuations have the common expression for their real parts
\[
 \Re J_{\mathrm{side}}(z)
       =-\Re J(-z)-\pi|\Im z| \qquad(\Re z<0).
 \tag{8}
\]
The argument \(-z\) is in the positive real strip.
The checker uses (8) on the angular endpoints, including
the depth where an imaginary part changes sign. On the
bottom trace it uses the fixed upper or lower half-plane.
Reciprocal-factorial zeros are therefore retained.

Each accepted rational box has an outward upper bound for
the whole phase. The saved boxes cover the four domains
in the table; no sample-point bound is used as a proof.

## 3. Passage to the original finite source

First remove outer-wire indices outside \(I\) in the original
finite sum. Their complete Hermite norm has rate at most
\(2g(1/32)\), where \(g(y)=J(2y)-4J(y)\).
For \(0<a\le1/2\), the real-angle Newton rate is greatest
at \(t=0\). Equations (3)--(6) put its maximum over the
present segment at \(a=3/10\). Its values and first normals
therefore give the discarded-source rate
\[
 E_{\mathrm{wire}}
   =\Re b(3/10+iY,0)+2g(1/32)<M-1/1000.
 \tag{9}
\]
At \(a=1/2\), the real-angle rate is constant, which causes
no exception. The normal bounds also follow from the exact
physical sine products: \(Y>0\) keeps their cotangents
bounded and adds only powers of \(N\).

Next remove real trace nodes with \(|t|\ge T_N\).
The [real outer-angle estimate](research_terminal_real_angle_tail.md)
bounds every retained wire subset, with its first normal,
by a polynomial times \(e^{N\psi(T,0)}\).
The Newton rate decreases with \(|t|\) when \(a<1/2\).
Its largest value at \(t=T\) is again at \(a=3/10\), so
the resulting rate is
\[
 E_{\mathrm{angle}}
     =\Re b(3/10+iY,T)+\psi(T,0)<M-1/1000.
 \tag{10}
\]
Both scalar inequalities are included in the certificate.
They bound original finite rows and all first normals.

Apply the exact midpoint trace rectangle to the retained
even function
\[
 B_N(x,t)\sum_{j/N\in I}B_N(j/N,t)B_N(j/N,u).
 \tag{11}
\]
Use depth \(4/5\), and leave \(j\) as a real finite index.
On the bottom trace, the full double-pole kernel is bounded
by \(C e^{-4N/5}\). At a folded endpoint of depth \(4s/5\),
it is bounded by \(C e^{-4Ns/5}\), including \(s=0\).
These are precisely the real contributions of \(-it\) in
(7). The crossing Gaussian and all other trace factors
keep their original coefficients. Summing the \(O(N)\)
remaining wire terms costs only a polynomial factor.

The reciprocal-factorial bounds hold throughout these
rectangles. Every moving real part stays strictly between
\(-1\) and \(1\), and \(G_N(Nx)\) is nonzero on the
compact set \(3/10\le\Re x\le1/2,\ \Im x=Y>0\).
The two shifted fixed-wire factorials have opposite
imaginary signs on the bottom trace. Their negative-real
cuts on the endpoints are handled by (8). The exact
interpolation is holomorphic where its reciprocal
factorials vanish, so no residue is introduced there.

The four strict inequalities bound the retained trace.
Uniform continuity preserves smaller gaps under the
\(O(N^{-1})\) endpoint changes, also at factorial zeros.
Restoring (9)--(10) gives a gap \(1/2000\) at \(u=0\).
For small complex \(u\), the retained factor \(B_N(j/N,u)\)
has its uniform factorial bounds on \(j/N\in I\).
The original omitted terms have coefficientwise interval
bounds and polynomial continuation at cost
\(e^{N O(|\Im u|)}\). Shrinking a disk about zero
preserves the gap \(1/4000\), proving (2).
Fixed derivatives obey the same kind of bound on smaller
disks by Cauchy's formula.

This theorem is an upper bound on one segment of the period;
it does not assert that segment has its own geometric asymptotic.

## 4. Reproduction

Run the standalone checker:

~~~sh
python3 experiments/certify_internal_pair_three_right_period.py
~~~

The [saved certificate](../repro/results/research-internal-pair-three-right-period.json)
records the root enclosure, monotonicity inequalities, both
original tail rates, and all accepted boxes. The imported
local mixed-source checker and interval engine are unchanged,
with their hashes recorded.
