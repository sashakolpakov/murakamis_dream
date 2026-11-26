# A joint bound for a real input and a complex output

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The real Fourier variable at the input and the imaginary displacement
at the output must be estimated together. Separate bounds for these
two changes do not add. This note proves a bound on the original
absolute summand envelope that retains both changes.

## 1. Statement

Use the retained vertex with corner cutoff \(L=\lfloor N/40\rfloor\),
and the normalization of
[the global modulus calculation](research_three_vertex_global_wire_bound.md).
Write
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 x=x_h+z,\quad y=\eta+i\left(\frac{\log2}{2\pi}+v\right),
 \quad z,\eta,v\in\mathbb R,
\]
and put
\[
 d(z)=\min\left\{\operatorname{dist}(z,\mathbb Z),\frac1{100}\right\}.
\]
The distance here is the distance on the real Fourier circle, with
circumference one. Let \(c=2\mathcal J(5/6)\), where
\(\mathcal J(s)=\int_0^s\log(2\sin\pi u)\,du\).

**Theorem 1.** For \(|v|\le1/200\), all real \(z,\eta\), and
both level parities,
\[
 \sum_{\text{retained indices}}|\text{original summand}|
 \le C N^b
 \exp N\left\{2c+13v^2-\frac32d(z)^2\right\}.
 \tag{1}
\]
The constants are independent of the Fourier variables and the level.
The same bound applies to every subset of the real summation indices.
It is an upper bound, not an assertion that the sum has a nonzero
leading coefficient.

## 2. A global maximization with a bounded quadratic weight

Set \(r=\tfrac12e^{-2\pi v}\), and define
\[
 f(u)=\log|1-\tfrac12e^{2\pi iu}|,\quad
 I(s,\xi)=\int_0^s f(\xi-u)\,du,\quad
 \ell_r(t)=\int_{-t/2}^{t/2}\log|1-r e^{2\pi iu}|\,du.
\]
For the input phase \(\xi=1/6+z\), minimizing the output
denominator over its real phase gives the upper envelope
\[
 E(s,t,\xi;v)=
 -\frac12\log(r/2)+\mathcal J(s+t)
 +s\log(1/2)+t\log r-I(s,\xi)-\ell_r(t).
 \tag{2}
\]
The index domain is
\(s,t\ge0\), \(s+t\le1\), \(\max(s,t)\ge1/40\).
The original cardinal factors supply the first term in (2).

We maximize
\[
 P(s,t,\xi;v)=E(s,t,\xi;v)
       +\frac32\min\{\operatorname{dist}(\xi-1/6,\mathbb Z),1/100\}^2.
 \tag{3}
\]
At the fixed homogeneous indices and input phase, (3) has value
\(2c\) at zero height, zero first height derivative, and a positive
second height derivative. Its value is therefore at least \(2c\)
throughout the height interval. This supplies a comparison point
for every exterior exclusion below.
We first locate its maximum globally. The unweighted envelope,
maximized also over \(\xi\), is the function already bounded in
[the symmetric-height theorem](research_three_vertex_symmetric_height_bound.md):
its maximum is at most \(2c+15v^2\), at a unique index pair.
That pair lies in \([.30,.37]^2\).

A small refinement locates it in \([.317,.35]^2\). Indeed its
negative index Hessian is
\(A=\operatorname{diag}(d_1,d_2)+k\mathbf1\mathbf1^T\),
with the proved bounds
\(d_i>8/5\), \(k>1\), and height coupling \(q<34/5\).
Every entry of \(A^{-1}\) has absolute value below \(65/144\).
Differentiating the critical equations therefore bounds each index
derivative by \(221/72\). Integration from \(v=0\) gives
\[
 \left|s_*(v)-\frac13\right|,
 \left|t_*(v)-\frac13\right|<\frac{221}{14400},
 \tag{4}
\]
which implies the stated smaller square.

On the larger square \([.28,.39]^2\), the unweighted negative
index Hessian is at least \((3/2)I\). To check this it is enough
to bound
\[
 \frac{\pi r\sin(\pi s)}{1+r^2-2r\cos(\pi s)}>\frac32
 \quad(.28\le s\le.39,\ .48\le r\le.52).
\]
The fraction increases in \(r\) and decreases in \(s\) on
this rectangle; its lower endpoint suffices. The additional
rank-one term is positive since \(s+t>1/2\).
At a boundary of this square the distance from the maximizing
pair is greater than \(.037\), so the unweighted value loses at
least \(3(.037)^2/4\).
Strict concavity on \(s+t>1/2\) extends this bound beyond that
boundary. The earlier smaller-index argument moves every point
with \(1/3\le s+t\le1/2\) to \(s+t=1/2\) with increased
unweighted envelope. For \(s+t\le1/3\), the earlier bound is
\(.645\). These comparisons cover the full index domain.
Since
\[
 15(1/200)^2+\frac32(1/100)^2
       <\frac34(.037)^2,
 \tag{5}
\]
no maximum of (3) is outside \([.28,.39]^2\).

For those indices we can also restrict \(\xi\) to
\([.12,.21]\), interpreted in the real circle. The integral
\(I(s,\xi)\) is minimized at \(\xi=s/2\), and increases
strictly with circular distance from that point up to distance
\(1/2\). Along the interval from \(s/2\) to \(.21\),
\[
 I_{\xi\xi}=f'(\xi)+f'(s-\xi)>6.
\]
Both arguments lie in \([.07,.21]\), where \(f'>3\).
Thus the loss at that boundary is at least
\(3(.21-.39/2)^2=.000675\).
Along the interval from \(.12\) to \(s/2\), the two
derivatives exceed three and two, respectively; the loss is
at least \(5(.28/2-.12)^2/2=.001\).
Both losses exceed the left side of (5). Monotonicity covers
the rest of the circle. The derivative bounds follow from
\[
 f'(u)=\frac{\pi\sin(2\pi u)}{5/4-\cos(2\pi u)}:
\]
this function first increases and then decreases on \((0,1/2)\),
so the endpoint bounds on each stated interval suffice.

## 3. The unique weighted maximum

In the rectangle just obtained put
\[
 k=-\pi\cot(\pi(s+t)),\quad D=-f'(\xi-s),\quad C=f'(\xi),
 \quad d=\frac{\pi r\sin(\pi t)}{1+r^2-2r\cos(\pi t)}.
\]
All four quantities are positive, and \(C>3\).
Where the weight in (3) is quadratic, its negative Hessian is
the positive quadratic form
\[
 k(ds+dt)^2+D(ds-d\xi)^2+d\,dt^2+(C-3)d\xi^2.
 \tag{6}
\]
Where the weight is constant its last coefficient is \(C\).
At the two transitions its first derivative jumps down. Consequently
(3) is strictly concave on the entire rectangle, including those
transitions.

There is one critical point for every \(|v|\le.005\), and it
lies in the region \(|\xi-1/6|<.01\). Its equations are
\[
 \begin{split}
 0&=\log(2\sin\pi(s+t))+\log(1/2)-f(\xi-s),\\
 0&=\log(2\sin\pi(s+t))+\log r
               -\log|1-r e^{\pi it}|,\\
 0&=f(\xi-s)-f(\xi)+3(\xi-1/6).
 \end{split}
 \tag{7}
\]
The certificate described below proves existence on an exact cover
of the full height interval by uniform real Newton boxes. Equation
(6) proves uniqueness and makes these local solutions one smooth
branch. All inequalities are strict, so it continues to a
neighborhood of the closed interval. At zero height the solution
is exactly \((s,t,\xi)=(1/3,1/3,1/6)\).

Write \(P_*(v)\) for its value. It is the global maximum:
the earlier exclusions put every competing point in the strictly
concave rectangle. In matrix notation let
\[
 H=\begin{pmatrix}
 k+D&k&-D\\ k&k+d&0\\-D&0&D+C-3
 \end{pmatrix},\qquad
 q=\frac{2\pi(1-r\cos\pi t)}{1+r^2-2r\cos\pi t}.
\]
Differentiation of (2) and the critical equations gives the exact
Schur formula
\[
 P_*''(v)=4d+q^2(H^{-1})_{22}.
 \tag{8}
\]
Here the matrix indices start at one. The certificate proves
\[
 P_*''(v)<\frac{251}{10}+450\max(v,0).
 \tag{9}
\]
It checks the whole Newton box on each height interval, not only
the proposed center of the critical point.

The homogeneous calibration gives \(P_*(0)=2c\).
The first height derivative is zero: at the homogeneous point
\(\partial_v\ell_r(1/3)=\pi/3\), which cancels
\(\pi-2\pi/3\) from the other terms. Integrating (9) twice,
with the integration direction reversed for negative height, gives
\[
 P_*(v)\le
 \begin{cases}
 (2c)+(251/20)v^2,&v\le0,\\
 (2c)+(251/20)v^2+75v^3,&v\ge0.
 \end{cases}
 \le 2c+\frac{517}{40}v^2\le2c+13v^2.
 \tag{10}
\]
Equations (2)--(3) now give the exponent in (1).
Uniform Riemann-sum bounds for the nonzero denominator products
and the endpoint sine-factorial bound contribute only a polynomial
in \(N\). Summing at most \(N^2\) retained summands proves
Theorem 1. \(\square\)

## 4. Reproduction

The checker `experiments/certify_three_vertex_weighted_height_bound.py`
records exact rational height intervals, Newton centers and
preconditioners, strict self-map inequalities, and the bound (9).
The numerical solver only proposes rational centers. Acceptance
uses outward interval arithmetic on every parameter interval and
every complete Newton box. The endpoint comparisons used in the
global exclusions are recorded separately in the same artifact.

The new estimate concerns the original retained finite sum, but
does not establish the next source attachment by itself. That
step also needs a bound on the incoming function on its full real
period and control of the integral through its critical point.
