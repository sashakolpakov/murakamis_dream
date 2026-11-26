# A global capped Gaussian bound for the retained three-crossing vertex

Research proof, 4 November 2026. Frozen manuscripts and completed source
artifacts are unchanged.

This makes the global retained-vertex maximum quantitative on the entire
real wire torus. The bound applies to the absolute sum of the original
retained summands, so it also applies to every subset of those summands.
Both wire heights are fixed at the homogeneous height. No estimate with
varying heights or for an arbitrary cap is inferred here.

## 1. The original exponent and the statement

Use the literal finite double sum in
[the global wire bound](research_three_vertex_global_wire_bound.md),
equations (2)--(7), with the L40 deletion
\[
 L=\lfloor N/40\rfloor,\qquad
 \widetilde V_N^{(40)}(x,y)=h(x)^T(JM^3-E_{40})h(y).
 \tag{1}
\]
Set
\[
 Y_h=\frac{\log2}{2\pi},\quad x_h=\frac16+iY_h,
 \quad c=2\mathcal J(5/6)=-3\mathcal J(1/3),
 \quad \mathcal J(s)=\int_0^s\log(2\sin\pi u)\,du.
 \tag{2}
\]
For real phases modulo one, write
\[
 \begin{split}
 f(v)&=\log|1-\tfrac12e^{2\pi iv}|,\qquad
 I(s,\xi)=\int_0^s f(\xi-u)\,du,\qquad
 \ell(s)=\int_{-s/2}^{s/2}f(v)\,dv,\\
 E(s,t;\xi,\eta)&=\mathcal J(s+t)-(s+t)\log2
                  -I(s,\xi)-I(t,\eta)+\log2,\\
 E_0(s,t)&=\mathcal J(s+t)-(s+t)\log2
                  -\ell(s)-\ell(t)+\log2.
 \end{split}
 \tag{3}
\]
The last term includes both original cardinal factors. The continuous
retained domain is
\[
 \mathcal D_{40}=\{s,t\ge0:s+t\le1,\ \max(s,t)\ge1/40\}.
 \tag{4}
\]
Every retained lattice point belongs to this domain: the exact condition
\(\max(i,j)>\lfloor N/40\rfloor\) implies
\(\max(i/N,j/N)>1/40\), without a rounding loss.

Let \(d_{\mathbb T}\) denote distance on \(\mathbb R/\mathbb Z\),
and put
\[
 q(\xi)=\min\{d_{\mathbb T}(\xi,1/6),1/100\}^2.
 \tag{5}
\]

**Theorem 1.** For every point of
\(\mathcal D_{40}\times(\mathbb R/\mathbb Z)^2\),
\[
 \boxed{\quad E(s,t;\xi,\eta)
       \le 2c-\frac85\{q(\xi)+q(\eta)\}.\quad}
 \tag{6}
\]
Consequently the absolute sum of the literal L40 summands, including
their cardinal factors, is bounded at both parities by
\[
 C N^A\exp N\left[2c-\frac85\{q(\xi)+q(\eta)\}\right],
 \qquad x=\xi+iY_h,\quad y=\eta+iY_h.
 \tag{7}
\]
The same exponent bounds the modulus of the retained kernel, every
real-index subset, and every fixed Fourier-wire derivative, with a
possibly larger polynomial factor.

## 2. A quantitative gap outside a central index square

The exact interval-minimum argument gives \(I(s,\xi)\ge\ell(s)\),
so \(E\le E_0\). Let
\[
 B=[3/10,19/50],\qquad W=[3/20,19/100].
 \tag{8}
\]
The global normalization and critical equations proved in the cited
global-wire note give
\(E_0(1/3,1/3)=2c\) and \(\nabla E_0(1/3,1/3)=0\).

**Lemma 2.** On \(\mathcal D_{40}\setminus B^2\),
\[
                         E_0\le2c-1/1125.
 \tag{9}
\]

*Proof.* For \(p=s+t>1/2\), direct differentiation gives
\[
 -E_0''=\operatorname{diag}(d(s),d(t))+k(p)
                    \begin{pmatrix}1&1\\1&1\end{pmatrix},
 \quad d(s)=\frac{(\pi/2)\sin\pi s}{5/4-\cos\pi s},
 \quad k(p)=-\pi\cot\pi p>0.
 \tag{10}
\]
On \(B\), \(d\) decreases: its derivative has the sign of
\((5/4)\cos\pi s-1<0\). At its right endpoint,
\[
 \begin{gathered}
 \sin(19\pi/50)>23/25,\qquad \cos(19\pi/50)>9/25,
 \qquad \pi>25/8,\\
 2d(19/50)
   >\frac{(25/8)(23/25)}{5/4-9/25}
   =\frac{575}{178}>\frac{16}{5}.
 \end{gathered}
 \tag{11}
\]
Thus \(-E_0''\succ(8/5)I\) on \(B^2\).

Join \((1/3,1/3)\) to a point outside \(B^2\) with \(p\ge1/2\)
by its straight segment. The portion until its first exit from
\(B^2\) has distance at least \(1/30\). Equation (10) makes
\(E_0\) nonincreasing on the rest of the segment, since its initial
directional derivative is zero and its directional second derivative
is negative throughout \(p>1/2\). Hence its endpoint value is at most
\[
 2c-\frac45(1/30)^2=2c-1/1125.
 \tag{12}
\]
Limits include \(p=1/2\), the axes, and \(p=1\); no derivative at
a factorial endpoint is required.

For \(1/3\le p\le1/2\), increase a smaller index, switching
indices if needed, until \(p=1/2\). During this path the smaller
index \(s\) is at most \(1/4\), and
\[
 \exp(\partial_s E_0)
  =\frac{\sin\pi p}{\sqrt{5/4-\cos\pi s}}>1,
 \quad \sin^2\pi p\ge3/4>5/4-\sqrt2/2.
 \tag{13}
\]
The path remains in the retained domain and increases \(E_0\).
Its endpoint has already been bounded by (12).

Finally, if \(p\le1/3\), then \(p\ge1/40\), and
\(\ell(s)\ge-s\log2\) implies \(E_0\le\log2+\mathcal J(p)\).
The maximum of \(\mathcal J\) on \([1/40,1/3]\) is at an
endpoint, because \(\mathcal J'\) changes from negative to positive
at \(1/6\). The elementary bounds
\[
 \begin{gathered}
 c>323/1000,\quad \log2<347/500,\qquad
 \mathcal J(1/3)=-c/3<-7/100,\\
 \mathcal J(1/40)
  \le\frac{\log(\pi/20)-1}{40}<-7/100
 \end{gathered}
 \tag{14}
\]
give \(E_0<78/125<2c-1/1125\). The first two bounds are also
recorded in the global-wire checker; all scalar comparisons needed
here are independently reproduced below. This proves (9).
\(\square\)

## 3. Joint curvature and the full wire torus

For indices in \(B^2\) and wire phases in \(W^2\), use the
exact unsummed Hessian from
[the joint-concavity proof](research_three_vertex_joint_concavity.md),
equation (4). With both indices real and both wire heights \(Y_h\),
\[
 -d^2E=a(ds+dt)^2+d_x(ds-d\xi)^2+d_y(dt-d\eta)^2
                            +c_\xi d\xi^2+c_\eta d\eta^2,
 \quad c_\xi=\frac{\pi\sin2\pi\xi}{5/4-\cos2\pi\xi}.
 \tag{15}
\]
Here \(s+t\in[3/5,19/25]\) and
\(s-\xi,t-\eta\in[11/100,23/100]\), so
\(a,d_x,d_y>0\). The function \(c_\xi\) decreases on \(W\),
because \(\cos2\pi\xi<4/5\). By (11),
\[
                     c_\xi,c_\eta>16/5.
 \tag{16}
\]
The straight segment from the homogeneous point stays in this convex
box. Every first real derivative vanishes at that point, including
the two wire derivatives by the centered-interval property. Integrate
(15) along the segment and discard its first three nonnegative terms:
\[
 E(s,t;\xi,\eta)
  \le2c-\frac85\{(\xi-1/6)^2+(\eta-1/6)^2\},
 \qquad (s,t,\xi,\eta)\in B^2\times W^2.
 \tag{17}
\]

It remains to justify a uniform bound when a wire phase is outside
\(W\). This is a global monotonicity step, not an extrapolation of
the Hessian. For \(0<s<1\), the function
\(I(s,s/2+d)\) is even in \(d\), periodic, and strictly increasing
with \(d\in(0,1/2)\):
\[
 \frac{d}{dd}I(s,s/2+d)=f(d+s/2)-f(d-s/2)>0,
 \tag{18}
\]
since the difference of the squared moduli inside these two logarithms
is \(2\sin(2\pi d)\sin(\pi s)>0\). If \(s\in B\), its center
\(s/2\) lies in \(W\). On the complementary arc to \(W\), the
minimum of \(I\) therefore occurs at one of the two endpoints of
\(W\). Replace each outside wire phase by such an endpoint, leaving
the inside phases fixed. This can only increase \(E\), and produces
a point of \(B^2\times W^2\) with at least one wire on the boundary.
The nearer boundary of \(W\) to \(1/6\) has distance \(1/60\).
Equation (17) thus gives
\[
 E\le2c-\frac85(1/60)^2=2c-1/2250
 \quad\hbox{if }(s,t)\in B^2,\ (\xi,\eta)\notin W^2.
 \tag{19}
\]

The largest possible loss required by (6) is
\[
 \frac85\{q(\xi)+q(\eta)\}\le
 2\frac85(1/100)^2=1/3125<1/2250<1/1125.
 \tag{20}
\]
Equations (9), (17), and (19) exhaust all indices and wire phases and
prove (6).

## 4. Original finite products and reproduction

The finite sine-factorial bound used in (7) of the global-wire note is
uniform through \(i+j=0,N-1\), with a logarithmic error \(O(\log N)\).
At both fixed wire radii \(1/2\), all denominator factors have modulus
at least \(1/2\), so their Riemann-sum errors are \(O(1)\), uniformly
over every real phase. The cardinal product contributes exactly the
rate \(\log2\) already in (3). Thus each original summand is bounded
by \(CN^A e^{NE}\), without any phase cancellation. Sum at most
\(N^2\) terms to obtain (7). For fixed wire derivatives, logarithmic
derivatives of the nonvanishing denominator products and cardinal
factors cost powers of \(N\); the numerator is independent of the
wire phases. This proves the derivative assertion directly on the
same circles and preserves the original parity and normal data.

The theorem is a global source upper bound. It supplies neither a
cap lower coefficient nor a conclusion about closing an arbitrary
chain; those require their respective source and contour arguments.

Run

```sh
python3 experiments/check_three_vertex_capped_gaussian_bound.py --precision 192
```

The [checker](../experiments/check_three_vertex_capped_gaussian_bound.py)
and [record](../repro/results/research-three-vertex-capped-gaussian-bound.json)
verify the exact differential identities, all rational margins, and
the few outward scalar enclosures used above. The global covering is
the analytic three-case argument (9), (17), (19), not a sampled grid.
