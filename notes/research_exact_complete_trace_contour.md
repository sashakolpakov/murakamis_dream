# An exact contour for the complete-meridian trace

Research note, 2 November 2026. Frozen manuscripts are unchanged.

The finite trace at the complete meridian contains first derivatives
at double roots. Those derivatives make a direct Fourier expansion
slightly different from an ordinary sampling formula: the coefficient
of the positive Fourier mode of charge $\ell$ is proportional to
$\ell$. Summing these modes gives a rational kernel with double poles.
This note derives that kernel directly from the original finite trace,
including the vertical endpoint term. It also gives a version after
removing outer grid points, and a criterion under which all charges
higher than one are controlled on a single contour.

The contour identity is exact for every signed integer crossing power.
The existence of a contour with the required global phase bound for
all fixed small powers is a separate analytic problem.

## 1. The original finite trace at the complete meridian

Let $N\geq3$, $d=N-1$, $q=e^{\pi i/N}$, and
$\eta=(-1)^d$. For an even trigonometric polynomial
$f(t)=f^\sharp(-2\cos t)$, write

\[
 \mathcal D_{n,N}[f]=\phi(R^n f^\sharp),\qquad
 C_{N,n}=q^{nd^2/4},\qquad
 \tau_j=\frac{2\pi}{N}\left(\frac d2-j\right),
 \quad 0\leq j<N.                                        \tag{1}
\]

The polynomial $f^\sharp$ may have arbitrary degree. The functional
$\phi$ means the full closing functional in
$\mathbb C[z]/(P_N)$, where $P_N(z)=2T_N(z/2)+2$ and $T_N$ is the
ordinary Chebyshev polynomial, including its first normal derivatives.
Define the odd entire function

\[
 g(t)=\sin t\,f(t)\exp\left(\frac{inN}{4\pi}t^2\right).      \tag{2}
\]

**Proposition 1.** The exact complete-meridian trace is

\[
 \boxed{\displaystyle
 \mathcal D_{n,N}[f]=\eta C_{N,n}\sum_{j=0}^{N-1}g'(\tau_j).} \tag{3}
\]

In particular, (3) is a derivative sampling formula, not a sum of
function values at the distinct roots of the pair algebra.

*Proof.* The original moving-meridian trace, keeping $f^\sharp$
fixed, is

\[
 \mathcal D_{n,\sigma,N}[f]
 =\frac{\eta N C_{N,n}(\sigma)}{\sin(2\pi\sigma)}
   \sum_{j=0}^{N-1}
       g\left(\tau_j+\frac{2\pi\sigma}{N}\right),
 \qquad
 C_{N,n}(\sigma)=q^{n(d^2/4-\sigma^2/2)}.                   \tag{4}
\]

This is the finite identity in
[the Fourier trace calculation](../papers/circle-tree-volume/fourier-trace.tex).
The grid in (1) is symmetric and $g$ is odd, so the numerator sum
vanishes at $\sigma=0$. Its first derivative is
$(2\pi/N)\sum_jg'(\tau_j)$. Since
$\sin(2\pi\sigma)=2\pi\sigma+O(\sigma^3)$, the removable value
of (4) is (3). The derivative of $C_{N,n}(\sigma)$ gives no extra
term. The removable value of the original finite trace is exactly
its Hermite trace; no roots or normal directions have been dropped.
$\square$

For later estimates, the summand is explicitly

\[
 g'(t)=\left\{\cos t\,f(t)+\sin t\,f'(t)
       +\frac{inN}{2\pi}t\sin t\,f(t)\right\}
        \exp\left(\frac{inN}{4\pi}t^2\right).               \tag{5}
\]

When $N$ is odd, the single grid point $\tau=0$ contributes
$g'(0)=f(0)$, with its original crossing scalar. The two points
$\tau$ and $-\tau$ associated with a double root give its full
value-and-derivative contribution.

## 2. Summing every positive Fourier charge

For a positive real number $y$, define

\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
                                                               \tag{6}
\]

Its poles lie on the real physical grid. In the lower half-plane,

\[
 W_N(t)=\sum_{\ell=1}^{\infty}
                 \ell\eta^{\ell-1}e^{-i\ell Nt}.            \tag{7}
\]

This series is absolutely and locally uniformly convergent there.

**Proposition 2.** For every $y>0$, the complete trace is

\[
 \boxed{\begin{aligned}
 \mathcal D_{n,N}[f]
 ={}&-\frac{N^2C_{N,n}}{\pi i}
       \int_{-\pi-iy}^{\pi-iy}g(t)W_N(t)\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
       \int_{-y}^{y}
         \frac{g(\pi+iv)}{4\cosh^2(Nv/2)}\,dv .
 \end{aligned}}                                             \tag{8}
\]

The horizontal integral is directed from left to right. The second
line is the exact contribution from the vertical sides of the
original rectangle. It is not an error term until it has been
estimated for the particular source.

*Proof.* The grid kernel

\[
 K_N(t)=\frac{iNe^{iNt}}{e^{iNt}-\eta}
\]

has residue one at every point of the grid. The positively oriented
rectangle with corners $\pm\pi\pm iy$ encloses exactly the $N$
points in (1). Applying the residue theorem to $K_Ng'$ and
integrating by parts on the closed contour gives

\[
 \mathcal D_{n,N}[f]
    =-\frac{\eta C_{N,n}}{2\pi i}\oint K_N'(t)g(t)\,dt,
 \qquad
 K_N'(t)=\frac{N^2\eta e^{iNt}}{(e^{iNt}-\eta)^2}.           \tag{9}
\]

The derivative $K_N'$ is even, and $g$ is odd. Reflecting the upper
horizontal side by $t\mapsto-t$, with its boundary orientation,
therefore makes it equal to the lower horizontal contribution.
On the lower side,

\[
 K_N'(t)=N^2\eta W_N(t),
\]

which gives the first line of (8).

On either vertical side $t=\pm\pi+iv$, one has
$e^{iNt}=-\eta e^{-Nv}$ and hence

\[
 K_N'(\pm\pi+iv)=-\frac{N^2}{4\cosh^2(Nv/2)}.              \tag{10}
\]

The right side is directed upward and the left side downward.
Oddness gives $g(-\pi+iv)=-g(\pi-iv)$. Combining both sides,
and then replacing $v$ by $-v$ in one term, gives the second line
of (8), with the sign shown there. $\square$

The factor $\ell$ in (7) is essential: it is the Fourier expression
of the first normal derivatives. Using a simple-pole kernel in its
place would give a different finite functional.

## 3. Removing outer grid points before contour deformation

It is often easier to estimate the outer part of the original finite
sum directly. This can be done without changing the contour identity
for its remaining part.

Choose an integer $m$ with $0\leq m<N/2$, and set

\[
 a_N=\pi-\frac{2\pi m}{N}>0.
\]

Then $e^{iNa_N}=-\eta$, and $\pm a_N$ lie halfway between
consecutive physical grid points. Define the retained trace

\[
 \mathcal D_{n,N}^{\,a_N}[f]
       =\eta C_{N,n}\sum_{|\tau_j|<a_N}g'(\tau_j).          \tag{11}
\]

The removed contribution is literally the sum of (5) over the
complementary grid points. In particular, normal derivatives are
retained on both sides of this decomposition.

**Corollary 3.** For every $y>0$,

\[
 \begin{aligned}
 \mathcal D_{n,N}^{\,a_N}[f]
 ={}&-\frac{N^2C_{N,n}}{\pi i}
       \int_{-a_N-iy}^{a_N-iy}g(t)W_N(t)\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
       \int_{-y}^{y}
          \frac{g(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
 \end{aligned}                                               \tag{12}
\]

*Proof.* Repeat the proof of Proposition 2 with vertical sides
$\pm a_N$. The enclosed residues are exactly the terms in (11),
and (10) still holds because $e^{iNa_N}=-\eta$. $\square$

Given a desired limiting cutoff $0<a<\pi$, one can choose these
midpoint boundaries with $a_N=a+O(N^{-1})$. There is no moving
parameter or infinite family of endpoint connectors in (12).

For example, suppose the removed grid terms satisfy

\[
 |f(\tau_j)|+|f'(\tau_j)|
       \leq CN^A e^{N(M-\delta)}
       \qquad (|\tau_j|\geq a_N)
                                                               \tag{13}
\]

for a fixed $\delta>0$. Equation (5) then bounds their total
contribution by $C(1+|n|)N^{A+2}e^{N(M-\delta)}$.
A bound on values alone is not substituted for (13).

## 4. A freely deformable lower contour

Let $\Gamma_N$ be any piecewise smooth path from $-a_N-iy$ to
$a_N-iy$ that stays in the open lower half-plane and is homotopic
to the straight segment there. The integrand $gW_N$ is holomorphic
throughout that half-plane. Therefore the horizontal integral in
(12) can be replaced exactly by the integral over $\Gamma_N$.
The vertical endpoint current remains unchanged.

This permits a useful separation of choices. The endpoint height
$y$ can be small enough to preserve an already proved endpoint gap.
Only the interior of $\Gamma_N$ needs to descend to the critical
point. All the deformations concern one holomorphic rational
integrand, rather than an infinite list of Fourier modes.

If $-\operatorname{Im}t\geq h>0$, then

\[
 W_N(t)=e^{-iNt}\bigl(1+E_N(t)\bigr),\qquad
 |E_N(t)|\leq
 \frac{2e^{-Nh}+e^{-2Nh}}{(1-e^{-Nh})^2}.                   \tag{14}
\]

For all sufficiently large $N$, the right side is at most
$10e^{-Nh}$. Thus, if $\Gamma_N$ has length at most $CN^A$ and

\[
 |g(t)e^{-iNt}|\leq CN^A e^{NM}\qquad(t\in\Gamma_N),        \tag{15}
\]

then the contribution from every charge $\ell\geq2$, already
summed together, is bounded by

\[
 CN^{A'}e^{N(M-h)}.                                         \tag{16}
\]

The estimate is conditional on the bound along the entire contour.
The existence of a local saddle expansion alone does not imply (15).

## 5. The actual endpoint current

The endpoint term in (12) has its own finite estimate. Suppose that
for $|v|\leq y$,

\[
 |f(a_N+iv)|\leq CN^A\exp N(E+Bv^2),                        \tag{17}
\]

where $E,B$ are independent of $N$. Since

\[
 \left|\exp\frac{inN}{4\pi}(a_N+iv)^2\right|
        =\exp\left(-\frac{nNa_N}{2\pi}v\right),\qquad
 \frac1{4\cosh^2(Nv/2)}\leq e^{-N|v|},
\]

the absolute value of the endpoint term is at most

\[
 CN^{A+2}(1+y)
 \exp N\left\{E+By^2+
     \left(\frac{|n|a_N}{2\pi}-1\right)_+y\right\}.          \tag{18}
\]

Here $x_+=\max\{x,0\}$. The factor $\sin(a_N+iv)$ is uniformly
bounded when $y$ stays in a fixed compact interval. If $E<M$,
then a sufficiently small fixed $y>0$ makes the exponent in (18)
strictly less than $M$, for every fixed $n$. The interior contour
may subsequently be moved farther into the lower half-plane.

One can replace the quadratic term in (17) by any established local
modulus of continuity. The quadratic form is convenient, but the
endpoint argument needs only that its cost tends to zero with $y$.

## 6. What is sufficient for a fixed small-power asymptotic

The exact identity reduces the analytic problem to ordinary
steepest descent with two explicitly retained errors. To state this
precisely, suppose a fixed crossing power $n$ and a family $f_N$
satisfy the following conditions.

1. The outer grid terms obey (13).
2. The endpoint current has a strict gap as in (18).
3. There is a family of lower contours $\Gamma_N$, of bounded length
   and a fixed positive distance from the real axis, on which
   (15) holds and has a strict gap outside a neighborhood of one
   critical point $t_*$. In that neighborhood,
   
   \[
   f_N(t)=N^\alpha a(t)e^{N\Psi(t)}(1+O(N^{-1})),
   \]
   
   with a uniform holomorphic error, $a(t_*)\ne0$, and
   
   \[
   \Phi(t)=\Psi(t)+\frac{in}{4\pi}t^2-it,
   \qquad \Phi'(t_*)=0,\quad\Phi''(t_*)\ne0,
   \quad \operatorname{Re}\Phi(t_*)=M.
   \]
4. The local contour crosses the saddle along a direction of strict
   quadratic decrease, and $\sin t_*\ne0$.

Then ordinary one-variable saddle integration applied to (12) gives

\[
 \mathcal D_{n,N}[f_N]
       =C_{N,n}N^{\alpha+3/2}A_*
           e^{N\Phi(t_*)}(1+O(N^{-1})),\qquad A_*\ne0.      \tag{19}
\]

The contour orientation and the continued square root of the Hessian
fix $A_*$. The rational correction in (14), the endpoint current,
and the removed finite grid terms are exponentially smaller.
For the one-edge source with $\alpha=-3/2$, the resulting terminal
polynomial has a nonzero leading amplitude of order $N^0$.

The role of the rational kernel is precise. Once a contour with
(15) exists, there is no additional infinite-charge theorem to prove.
Constructing and estimating that contour uniformly in the free
boundary variable remains necessary. This note does not infer it
from the finite trace identity.

## 7. Finite numerical check of signs and normal terms

Run the finite verification with

```sh
python3 experiments/audit_complete_trace_rational_contour.py
```

The script requires `mpmath`. The identities (8) and (12) were compared
directly with their derivative sums in 120 cases at 60 decimal digits for $N\in\{3,4,5,8\}$,
$n\in\{-3,0,1,2,3\}$, and
$f(t)\in\{1,\cos(2t),\cos((N+2)t)\}$, using $y=0.17$, both for the full grid and after removing its
outermost pair. The largest relative discrepancy, measured with denominator
$1+|\mathcal D|$, was $5.4\times10^{-47}$. The high-frequency
examples test the absence of a degree restriction. The case $n=0$
also checks the cancellation between the horizontal and vertical
parts when the exact trace vanishes.

These are numerical sign checks. The proof of the identity is the
residue and integration-by-parts calculation in Section 2.
