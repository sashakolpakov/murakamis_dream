# Exact boundary messages and a complex-strip estimate

The aim is to estimate a subtree after its own crossing-circle traces
have been taken. Its value at zero can then be factored out exactly.
This differs from bounding every subtree by its complete, unfilled
action. The argument below proves two elementary parts of that
program: the degree of the exact boundary message, and the passage
from a real envelope and a local complex estimate to a strip bound.
It does not prove the nonvanishing or real envelope required by an
induction.

## 1. The exact finite message has degree at most N-1

Fix an original ordered tree with a crossing circle at every vertex.
Use the complete Newton basis e_k, 0<=k<N, even when the main meridian
varies. The full covariant edge kernel is
\[
 K_{e,N}(t,u;s)=\sum_{k=0}^{N-1}
 e_k(-2\cos t)e_k(-2\cos u)\,
       \gamma_{e,N}(s)\frac{H_N(s)}{W_k(s)}.                 \tag{1}
\]
This includes all low and high indices. The recorded orientation
factor is assigned to that edge exactly once.

Root the actual tree and let p be the parent of v. Define
\[
 M_{v\to p,N}(u;s)=
 \mathcal D_{n_v,\sigma_v,N}^{(t)}
 \left[K_{vp,N}(t,u;s)
       \prod_{w\text{ child of }v}M_{w\to v,N}(t;s)\right].
                                                               \tag{2}
\]
The functional is the original polynomial crossing-power trace,
including its normal limit at repeated roots. Its argument can have
degree larger than N-1 in t; that is allowed because the trace takes
the remainder in its prescribed moving or constant quotient.
The explicit reference and final framing factors can be kept outside
(2). None depends on u.

Equation (2) is a finite tensor contraction, so changing the order of
these linear evaluations is exact. It makes no tangle isotopy or
commutativity assertion. Only the kernel in (1) depends on u.
Consequently
\[
 M_{v\to p,N}(u;s)=\sum_{k=0}^{N-1}a_{v,k,N}(s)e_k(-2\cos u).
                                                               \tag{3}
\]
The coefficients may be complicated and can have cancellations.
Nevertheless the boundary function is an even trigonometric
polynomial of degree at most N-1, independently of subtree size,
degree, or depth. This conclusion does not require nonvanishing.

At the root the remaining crossing trace is applied to the product
of its child messages. Multiplying by the one original main closing
factor and all retained reference/framing scalars recovers the
unchanged finite invariant.

## 2. A global real envelope has a precise complex continuation

Let f be a trigonometric polynomial of degree at most m. Suppose
\[
 |f(t)|\le B\exp\{N[A-c(1-\cos t)]\},
 \qquad t\in\mathbb R,\qquad c>0,\quad B>0.                 \tag{4}
\]
No reality or positivity of f is assumed. For every real t,y,
\[
 |f(t+iy)|\le B\exp\{
 N[A-c(1-e^{-|y|}\cos t)]+m|y|\}.                         \tag{5}
\]
Indeed write f(t)=F(e^{it}), where F is a Laurent polynomial
supported in [-m,m]. For y>=0 the function z^m F(z) is a polynomial
on the unit disk. On its boundary the logarithm of its modulus is
bounded by
\[
 \log B+NA-Nc+Nc\operatorname{Re}z.
\]
The right side is harmonic, so the subharmonic maximum principle
gives the same bound throughout the disk. Divide by |z|^m and set
z=e^{-y+it}. Zeros cause no difficulty for the subharmonic inequality.
For y<=0 apply the same argument to z^m F(z^{-1}); the cosine
boundary majorant is unchanged by t->-t. This proves (5).

If m<=kappa N, then 1-e^{-|y|}<=|y| gives the useful coarser form
\[
 |f(t+iy)|\le B\exp N[
 A-c(1-\cos t)+(\kappa+c)|y|].                            \tag{6}
\]
This is a linear imaginary-growth bound. A real envelope alone does
not justify replacing its last term by a quadratic term.

## 3. Patching the far region to a local quadratic estimate

Assume also, for |t|<=rho and |y|<=y_*, that
\[
 |f(t+iy)|\le B_*\exp N[A-a t^2+C y^2],
 \qquad 0<\rho<\pi,\quad a>0,\quad C\ge0.                            \tag{7}
\]
Set
\[
 c_*=\min\{c/2,2a\},\qquad
 0<y_0\le\min\left\{y_*,
             \frac{c(1-\cos\rho)}{2(\kappa+c)}\right\}.    \tag{8}
\]
Then on the full periodic real interval and this fixed strip,
\[
 |f(t+iy)|\le\max\{B,B_*\}\exp N[
       A-c_*(1-\cos t)+C y^2],
 \qquad |t|\le\pi,\ |y|\le y_0.                          \tag{9}
\]
For |t|>=rho, (6) and (8) bound the imaginary cost by
c(1-cos t)/2. For |t|<=rho, use t^2>=2(1-cos t) in (7).
These two regions cover the required strip.

Since 1-cos t>=2t^2/pi^2 on [-pi,pi], (9) also gives
\[
 |f(t+iy)|\le\max\{B,B_*\}\exp N[
       A-\frac{2c_*}{\pi^2}t^2+C y^2].                  \tag{10}
\]
The constants do not depend on the trigonometric degree beyond
m/N<=kappa. For the exact message (3), kappa=1 is sufficient.

The factors B,B_* can be polynomial in N and depend on the fixed
subtree, the fixed crossing powers, and a fixed meridian disk.
The proof is unchanged for complex coefficients or auxiliary
parameters, provided the two hypotheses hold uniformly in those
parameters.

## 4. Use in the volume theorem

If M_v(0;s) is nonzero, apply the lemma to
f=M_v(u;s)/M_v(0;s), with A=0. The [local volume proof](actual_all_circle_local_message_volume.md) establishes

* a real envelope (4), with a depth-independent positive c;
* a zero-free angular disk and the local estimate (7);
* the corresponding analytic phase and nonzero amplitude;
* enough uniform derivative control to apply the actual finite
  crossing trace at the next vertex.

The full kernel has one-edge real decay, and its angular argument
enters a limiting subtree action only through that boundary edge.
The linked proof uses these facts to establish the hypotheses. In particular a child's exponentially
small errors must not be expanded and then compared with the
complete action of all of its ancestors. The proof keeps its exact local logarithm to avoid that accumulation.

The metric completion of a positive critical branch is now separate:
the vertexwise geometric criterion constructs such a branch without
the global summed bound. The linked theorem closes the induction and proves its nonzero
final trace under its explicit local degree-and-twist condition.
