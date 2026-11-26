# The joint retained-kernel bound with cap radius (1/25)

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This enlarges the input-distance cap in the proved joint height bound
from \(.01\) to \(.04\), keeping both quadratic coefficients unchanged.
The original L40 source and the already certified critical-height
branch are unchanged. Only the global exclusion argument is strengthened.

## 1. Statement

Use the exact retained vertex \(\widetilde V_N^{(40)}\), including
its original cardinal factors, and set
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 c=2\mathcal J(5/6),\qquad
 d_{04}(z)=\min\{\operatorname{dist}(z,\mathbb Z),1/25\}.
 \tag{1}
\]
The distance is on the real Fourier circle of circumference one.

**Theorem 1.** For every real \(z,\eta\), \(|v|\le1/200\),
and both level parities,
\[
 \sum_{\mathrm{retained}}|\mathrm{original\ summand}|
 \le CN^b\exp N\left\{
 2c+13v^2-\frac32d_{04}(z)^2\right\},
 \quad x=x_h+z,\quad y=\eta+i(\Im x_h+v).
 \tag{2}
\]
The constants are uniform in the Fourier variables and level. The
same upper bound holds for every subset of the real retained indices
and for each fixed wire derivative at polynomial cost. This asserts
no lower coefficient and no new complex source-packet domain.

## 2. Global exclusion with the larger weight

Use exactly the original envelope \(E(s,t,\xi;v)\) in equation (2)
of [the joint height theorem](research_three_vertex_weighted_height_bound.md),
with \(r=\tfrac12e^{-2\pi v}\), \(\xi=1/6+z\), and maximize
\[
 P_{04}(s,t,\xi;v)=E(s,t,\xi;v)
       +\frac32d_{04}(\xi-1/6)^2.
 \tag{3}
\]
The exact retained index domain is contained in
\(s,t\ge0\), \(s+t\le1\), \(\max(s,t)\ge1/40\).
The maximum weight in (3) is \(3/1250\).
At the homogeneous indices and input phase, the value is at least
\(2c\) for all the stated heights: its height derivative vanishes
at zero and its fixed-index second derivative is positive, as
proved in the joint height theorem.

First improve the small-index-sum estimate. Write \(p=s+t\).
For \(1/40\le p\le1/3\), the original denominator inequality gives
\[
 E(s,t,\xi;v)\le
 \log2+\mathcal J(p)-\tfrac12\log(2r)
                           +t\log\frac r{1-r}.
 \tag{4}
\]
The only interior critical point of \(\mathcal J\) on this interval
is its minimum at \(1/6\). Its two endpoint values are at most
\[
 T=\frac{\log(\pi/20)-1}{40}.
 \tag{5}
\]
For the first endpoint use \(2\sin(\pi u)\le2\pi u\) under
the defining integral. For the other use
\(\mathcal J(1/3)=-c/3<-323/3000<T\), with the previously proved
\(2c>323/500\). These are strict rational scalar comparisons.

If \(12/25\le r\le1/2\), the radius correction in (4) is at
most \(-\tfrac12\log(24/25)\). If \(1/2\le r\le13/25\),
it is at most
\[
 g(r)=-\tfrac12\log(2r)+\tfrac13\log\frac r{1-r},\qquad
 g(1/2)=0,\quad
 g'(r)=\frac{3r-1}{6r(1-r)}<\frac25.
 \tag{6}
\]
Thus \(g(r)<1/125< -\tfrac12\log(24/25)\).
The full weighted estimate is consequently
\[
 P_{04}\le
 \log2+T-\tfrac12\log(24/25)+\frac3{1250}
                       <\frac{129}{200}<2c.
 \tag{7}
\]
The first expression is less than \(.644684\). In particular,
the former coarse \(.645\) bound has not been reused before
adding the larger weight.

For the remaining indices, let \(\widehat E_r\) be the unweighted
envelope after minimizing both denominator intervals. The proved
height theorem gives its unique maximum at an index pair in
\([.317,.35]^2\), and
\(\max\widehat E_r\le2c+15v^2\).
Consider the larger square
\[
                         Q_*=[1/4,21/50]^2.
 \tag{8}
\]
There the unweighted negative index Hessian is
\(\operatorname{diag}(d_1,d_2)+k\mathbf1\mathbf1^T\),
with \(k\ge0\) and
\[
 d_i=\frac{\pi r_i\sin(\pi s_i)}
                {1+r_i^2-2r_i\cos(\pi s_i)}>\frac75,
 \qquad r_i\in[12/25,13/25].
 \tag{9}
\]
The fraction increases with \(r_i\) and decreases with \(s_i\)
on the stated box, so its minimum is at
\((r_i,s_i)=(12/25,21/50)\); its value exceeds \(1.4728\).
The critical pair is at distance greater than \(.067\) from every
face of (8). Hence the loss at each exit from (8) is greater than
\((7/10)(.067)^2\), whereas
\[
 15(1/200)^2+\frac3{1250}
       =.002775<.0031423=\frac7{10}(.067)^2.
 \tag{10}
\]
Strict concavity of \(\widehat E_r\) on \(p>1/2\) extends this
loss beyond the square. The previously proved smaller-index variation
raises every unweighted value with \(1/3\le p\le1/2\) to the
boundary \(p=1/2\), where the same exit bound applies. This step
uses the unweighted majorant plus the maximum weight; it does not
assert monotonicity of (3) while holding \(\xi\) fixed. Together
with (7), it proves that every global maximum of (3) lies in (8).

Now restrict the input phase to
\[
                              W=[3/25,21/100].
 \tag{11}
\]
For \(s\in[1/4,21/50]\), the minimizing center \(s/2\) lies
in \([1/8,21/100]\subset W\). The interval integral
\(I(s,\xi)\) is strictly increasing with circular distance from
\(s/2\) up to distance \(1/2\). A phase outside \(W\) can
therefore be moved toward that center to the first endpoint of
\(W\), increasing \(E\). The quadratic weight is unchanged:
the full interval \([1/6-1/25,1/6+1/25]\) lies strictly inside
\(W\), so both endpoints of \(W\) and the whole complementary arc
have weight \(3/1250\). Thus every maximum occurs in
\(Q_*\times W\).

## 3. The same critical branch and the finite source

On \(Q_*\times W\), define \(k,D,C,d\) as in the joint
height theorem. Then
\[
 k\ge0,\qquad D,d>0,\qquad C=f'(\xi)>3.
 \tag{12}
\]
Indeed \(s-\xi\in[.04,.30]\subset(0,1/2)\). The last
inequality follows from the endpoint bounds for \(f'\) on
\([.12,.21]\), which has at most one interior maximum.
In the quadratic part of the weight, the negative Hessian is
exactly
\[
 k(ds+dt)^2+D(ds-d\xi)^2+d\,dt^2+(C-3)d\xi^2.
 \tag{13}
\]
In the constant part its last coefficient is \(C\). At both
clipping transitions the first derivative jumps down. This proves
strict concavity on the entire rectangular domain, including
\(s+t=1/2\) and the clipping faces.

The already certified critical-height branch has
\(s,t\in(.28,.39)\) and \(|\xi-1/6|<.01\). It lies strictly
inside this domain and inside the quadratic parts of both the old
\(.01\) cap and the new \(.04\) cap. Its stationary equations
and its value are therefore exactly the same for both problems.
Strict concavity and the global exclusions identify it as the unique
global maximum of (3), with no new critical branch or numerical
continuation assumption. In particular the existing full-interval
certificate and its integration give
\[
 \max P_{04}=P_*(v)\le2c+13v^2.
 \tag{14}
\]

Subtracting the weight proves the exponent in (2). The unchanged
original finite-product and endpoint-factorial estimates cost only
powers of \(N\), uniformly over every real index and Fourier phase.
The actual retained indices satisfy \(\max(i/N,j/N)>1/40\),
so no endpoint strip has been omitted. Every denominator has modulus
bounded away from zero because both wire radii stay below one.
Its fixed derivatives, and those of the original cardinal factors,
cost only powers of \(N\) term by term. Summing the finite terms
proves Theorem 1, including subsets, derivatives and both parities.
\(\square\)

## 4. Reproduction and scope

The [focused checker](../experiments/check_three_vertex_large_cap_height_bound.py)
and [record](../repro/results/research-three-vertex-large-cap-height-bound.json)
verify the sharper low-index bound, the enlarged-square coercivity,
all clipping and projection margins, and the exact 2,048-cell cover
and branch enclosures in the existing critical-height artifact.
They retain the hashes of that artifact and its independent replay.
The Newton certificate is reused unchanged; no new sampled
maximization is used.

```sh
python3 experiments/check_three_vertex_large_cap_height_bound.py --precision 192
```

This is an upper bound for the actual retained kernel. It strengthens
the far-input estimate in a source attachment, but does not itself
provide an entrance source packet, its incoming tail bound, or a
nonzero closing coefficient.
