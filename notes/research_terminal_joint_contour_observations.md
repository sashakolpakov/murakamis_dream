# Candidate contours for a fixed short terminal filling

Exploratory record, 2 November 2026. The numerical observations below
are not used as premises of a theorem. They locate failures of simple
contour choices and suggest what a successful estimate must address.
The [real-angle tail inequality](research_terminal_real_angle_tail.md)
is proved separately.

At complete parent angle the original two-variable phase is

\[
 F_n(x,t)=b(x,t)+b(x,0)+\frac{in}{4\pi}t^2-it.
\]

Its selected stationary point $(x_n,t_n)$ and negative-definite real
Hessian are established in
[the stationary-geometry note](research_terminal_powers_three_and_above.md).
For $n=3$,

\[
 x_3\approx0.192486636+0.055158900i,\qquad
 t_3\approx1.779413017-0.632974319i,
 \qquad \Re F_3(x_3,t_3)\approx0.848851229.
\]

## 1. A constant translation over the whole period is too large

Translate $x$ and $t$ by the imaginary parts of their selected saddle,
and let their real parts range over $[0,1/2]\times[0,\pi]$.
For $n=3$, numerical optimization finds a real action near $1.03358$
at the boundary $\Re t=\pi$. This exceeds the selected action.
For $n=4$, the corresponding boundary value is about $1.07474$,
again larger than its selected action, about $0.97692$.

Global concavity on this translated domain also fails in a direct
Hessian calculation. For example, near
$\Re x=0.005$, $\Re t=2.48814$, with the three-crossing imaginary
translation, the determinant of the real Hessian is approximately
$-1.27869$. These computations rule out using an unsupported global
concavity assertion based on the Hessian at the saddle.

The phase outside the original positive factorial strip must use its
continued branches. In the computations, if $\Re z<0$, the primitive
is continued according to

\[
 J(z)=-J(-z)+\operatorname{sgn}(\Im z)i\pi z.
\]

An exact factorial continuation, including its second exponential
term, is still required when converting such phase calculations into
estimates on the finite sum.

## 2. First remove the real outer angles

The proved tail inequality permits discarding the original real
nodes with $|t|\ge T=2\pi/3$ at a rate below every selected action
with $|n|\ge3$. This is done before deforming the central part.
Numerical optimization on the smaller translated rectangle
$0\le\Re t\le T$ instead places the largest value at the selected
three-crossing saddle.

The connecting face at $\Re t=T$ cannot be treated by first shifting
$x$ to its final height and then moving $t$ vertically. That order
can raise the real action above the saddle near the start of the
vertical motion. A possible alternative moves both heights together:

\[
 x=r+i s\Im x_n,\qquad
 t=T+i s\Im t_n,
 \qquad 0\le s\le1.
\]

For $n=3$, the sampled maximum on this coupled face lies below the
selected action. This is encouraging but is not a global bound.
The face must be included as part of an actual deformation of the
two-dimensional integration chain. The wire-lattice correction terms,
the other faces, and the negative real angles also remain to be
estimated. A maximum of the limiting phase alone would not settle
these issues.

The diagnostic script is

```sh
python3 experiments/explore_terminal_joint_contour.py
```

It reports approximate maxima for powers $3,4,5,8$, with a fixed
optimization seed. Its results are reproducible numerical evidence,
not certified bounds. In contrast, the companion real-angle script
uses interval arithmetic only to certify the two constants in its
already proved analytic inequality.
