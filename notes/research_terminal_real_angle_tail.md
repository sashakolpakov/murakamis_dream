# A uniform bound away from the central boundary angles

Research proof, 2 November 2026. This note supplies one global estimate
needed in the study of fixed short terminal fillings. It does not prove
their complete asymptotic. The finite kernel, the real phase, and the
region being estimated are specified below. Frozen manuscripts are
unchanged.

## 1. The kernel and the real exponential rate

Use the Newton polynomials from
[the finite-source paper](../papers/circle-tree-volume/finite-bounds.tex):

\[
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}
       \bigl(2\cos((2j+1)\pi/N)-z\bigr),\qquad
 S_k=\prod_{j=1}^k2\sin(\pi j/N),\quad 0\le k<N.
\]

The complete edge kernel with its second boundary left complete is

\[
 K_N(t,0)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2).
\]

For real arguments define

\[
 J(x)=\int_0^x\log|2\sin(\pi v)|\,dv.
\]

The integral is understood across its integrable logarithmic
singularities. This real function is odd and has period one. In
particular, $J(0)=J(1/2)=0$. For $0\le x\le1/2$ put

\[
 g(x)=J(2x)-4J(x).
\]

For $0\le t\le\pi$ write $r=(\pi-t)/(2\pi)$. The logarithm of the
absolute value of the low-index summand, divided by $N$, is bounded
above by the continuous rate

\[
 A(x,r)=J(r+x)-J(r-x)+J(2x)-6J(x),\qquad x=k/N,       \tag{1}
\]

up to $O(\log N/N)$, uniformly in $k$ and $t$. To obtain (1), factor
the cosine numerator as

\[
 2\cos(2\pi v)+2\cos t
   =4\sin(\pi(r+v))\sin(\pi(r-v)).
\]

Integrating its logarithmic absolute value gives
$J(r+x)-J(r-x)-2J(x)$ for the first Newton polynomial; the other
polynomial contributes $g(x)$. A product that vanishes satisfies the
upper bound automatically. Otherwise the usual sum--integral estimate
removes the at most two mesh intervals next to a moving zero and bounds
the remaining variation by $O(\log N)$. The removed intervals give the
same upper error, uniformly in the zero's position. This is the
moving-zero estimate used in Section 7 of
[the two-crossing proof](research_two_crossing_terminal_filling.md).

## 2. An inequality on the whole outer angular region

For real $0\le t<\pi$, let $\psi(t,0)$ be the real edge action. It is
the maximum of (1) in the interval $0\le x\le r$ where neither sine
factor changes sign. Its critical point is

\[
 x(t)=\frac1\pi\arctan(\cos(t/2)),\qquad
 \psi_t(t,0)=-\frac1\pi\operatorname{arsinh}(\tan(t/2))<0
 \quad(t>0).                                          \tag{2}
\]

These statements also follow directly by differentiating (1) on this
interval; the second derivative in $x$ is negative, and the first
derivative changes from positive infinity to negative infinity.

**Proposition.** If $\pi/2\le T\le2\pi/3$, then

\[
 A\left(x,\frac{\pi-t}{2\pi}\right)\le\psi(T,0),
 \qquad T\le t\le\pi,\quad 0\le x\le1/2.              \tag{3}
\]

**Proof.** Put $r_0=(\pi-T)/(2\pi)$, so $1/6\le r_0\le1/4$.
If $x\le r$, equation (2) gives
$A(x,r)\le\psi(t,0)\le\psi(T,0)$.

Suppose instead that $x\ge r$. Oddness of $J$ rewrites the rate as

\[
 A(x,r)=J(x+r)+J(x-r)+J(2x)-6J(x).
\]

For fixed $x\le1/2$, this expression is increasing in $r$ on $0<r<x$:

\[
 \partial_r A=\log\frac{\sin(\pi(x+r))}{\sin(\pi(x-r))}\ge0.
\]

Indeed the difference of the two sines is
$2\cos(\pi x)\sin(\pi r)\ge0$.

If $x\le r_0$, we may therefore replace $r$ by $x$. The resulting
function is

\[
 H(x)=2J(2x)-6J(x),\qquad
 H'(x)=2\log\frac{2\cos^2(\pi x)}{\sin(\pi x)}>0
 \quad(0<x\le1/4).
\]

Thus $A(x,r)\le H(r_0)$ in this case.

If $x\ge r_0$, replace $r$ by $r_0$ instead. Set
$c=\cos T\in[-1/2,0]$ and $y=\cos(2\pi x)$. In the interior of this
interval $y+c<0$, and differentiation gives

\[
 \partial_x A(x,r_0)
   =\log\frac{-(y+c)(y+1)}{(1-y)^2}<0.                \tag{4}
\]

For the strict inequality, the difference between denominator and
numerator is

\[
 2y^2+(c-1)y+c+1>0.
\]

Its discriminant is $c^2-10c-7\le-7/4<0$ on $[-1/2,0]$, and its
leading coefficient is positive. Endpoint values follow by continuity.
This proves $A(x,r)\le A(r_0,r_0)=H(r_0)$ also in the second case.

Finally, $H(r_0)$ is the boundary value of the strictly concave
prezero phase at $t=T$, whose interior maximum is $\psi(T,0)$.
Consequently $H(r_0)<\psi(T,0)$, proving (3). $\square$

## 3. Consequences for the exact finite kernel

Uniformly for $T\le|t|\le\pi$, the proposition and the product estimate
give

\[
 |K_N(t,0)|\le C N^A\exp\{N\psi(T,0)\}.              \tag{5}
\]

Here $C,A$ do not depend on $N$ or $t$. Low indices use (1)--(3).
For $k>\lfloor(N-1)/2\rfloor$, both Newton factors have polynomial
interval norm by the high-index Hermite bound in the finite-source
paper. There are only $N$ summands, and $\psi(T,0)>0$, so these terms
are included in (5).

This estimate also controls the first normal derivatives needed in
the physical trace. Regard $K_N(t,0)$ as a polynomial in
$z=-2\cos t$, of degree at most $N-1$. Equation (5) holds on the
entire interval $[-2\cos T,2]$. Markov's polynomial inequality on
that interval bounds its $z$ derivative by $2(N-1)^2/(2+2\cos T)$
times the same supremum. The cost is polynomial in $N$. The original
fixed crossing power has polynomial Hermite norm as well. Thus the
part of its finite Hermite trace supported on these outer nodes has
the same upper exponential rate. This statement does not discard
the normal term at a repeated spectral root.

No approximation to an oscillatory integral was used in (5).
The estimate can be applied before constructing the contour for the
remaining central angles.

## 4. A strict gap for every selected saddle with $|n|\ge3$

For $n=3$, put

\[
 k=\frac{\sqrt7+i}{4},\qquad t_3=2\arccos k,
 \qquad x_3=\frac{\arctan k}{\pi}.
\]

The branches are the ones in
[the stationary-geometry proof](research_terminal_powers_three_and_above.md).
Write

\[
 M_3=\Re\left\{b(x_3,t_3)+b(x_3,0)
                       +\frac{3it_3^2}{4\pi}-it_3\right\}.
\]

At $T=2\pi/3$, the real maximizing wire coordinate is
$x_T=\arctan(1/2)/\pi$. The accompanying script evaluates these two
explicit constants with rigorous complex ball arithmetic and verifies

\[
 \psi(2\pi/3,0)<\frac45<\frac56<M_3.                 \tag{6}
\]

For this computation the continued primitive on $0<\Re z<1$ is

\[
 J(z)=-\frac{i\pi}{2}(z^2-z)
       +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz})
       -\frac{i\pi}{12},
\]

and

\[
 b(x,t)=J(1/2+t/(2\pi))+J(1/2-t/(2\pi))
        -J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x).
\]

Differentiation and the value at $z=0$ fix this primitive. Every
argument used in (6) lies strictly within the indicated strip; the
script checks this as well. The numerical midpoints are about
$0.777496$ and $0.848851$, respectively, but the certificate uses
the strict rational inequalities (6), not rounded decimal output.

Run

```sh
python3 experiments/audit_terminal_real_angle_tail.py
```

This requires `python-flint`, whose Arb/Acb arithmetic encloses the
values in rigorous real or complex balls. See the
[FLINT documentation](https://flintlib.org/doc/arb.html) and the
[Python complex-ball interface](https://python-flint.readthedocs.io/en/latest/acb.html).

The same gap works for every larger terminal power. Allow the crossing
coefficient $n$ to vary continuously over $[3,\infty)$. The selected
solution from Section 1 of the stationary-geometry note remains unique
and nondegenerate. At parent angle zero write it as $t_n=2a_n-2ib_n$,
where $a_n,b_n>0$. Stationarity gives

\[
 \frac{dM_n}{dn}
 =\Re\frac{it_n^2}{4\pi}
 =\frac{2a_nb_n}{\pi}>0.                              \tag{7}
\]

Consequently $M_n\ge M_3>5/6$ for every $n\ge3$. Negative powers
have the conjugate action and the same real part. Combining (5)--(7)
shows that the entire real outer-angle region $|t|\ge2\pi/3$ has a
strict rate gap of more than $1/30$ below every selected action with
$|n|\ge3$. This is a statement about the exact finite trace restricted
to these real nodes, before deforming the remaining central part.

This leaves the
central contour, its connecting faces, and the wire-lattice corrections
to be controlled. Inequality (6) alone does not establish that the
selected saddle contributes to the original finite sum.
