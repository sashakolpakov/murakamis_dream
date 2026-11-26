# A weighted bound on the exact edge contours

Research proof, 2 November 2026. This note verifies the weighted edge
estimate used in
[the terminal large-power argument](research_terminal_large_fixed_powers.md),
equation (9). The frozen manuscripts are unchanged.

The issue is not a real-axis product bound. When the first boundary
angle is complex, the edge sum has to be estimated on its deformed
wire contours. The second, real boundary angle must decrease the rate
on every part of those contours, including the lattice corrections
and the finite endpoint currents. The canonical factorial bounds
provide precisely that decrease.

## 1. Statement

Let $I=[1/5,3/10]$, and let

\[
 K_{N,I}(t,u)=\sum_{k/N\in I}e_k(-2\cos t)e_k(-2\cos u)
\]

be the exact retained kernel from the circle-tree source. Let $b(x,t)$
be its canonical interpolating phase, and let

\[
 A_t(x)=b(x,t)+b(x,0),\qquad
 x_*(t)=x(t,0),\qquad \psi(t,0)=A_t(x_*(t)).
\]

The critical point and branches are the ones continued from
$x_*(0)=1/4$ in
[the exact edge proof](../papers/circle-tree-volume/edge-packet.tex).

**Lemma.** There is a constant $C$, independent of $N,t,u$, such that

\[
 \boxed{\displaystyle
 |K_{N,I}(t,u)|\leq C N^{-3/2}
   \exp N\left\{\operatorname{Re}\psi(t,0)
                         -\frac1{20}(1-\cos u)\right\},}
                                                               \tag{1}
\]

for $N\geq3$, $|t|\leq1/4$ and real $|u|\leq\pi$.
A weaker polynomial prefactor therefore gives equation (9) of the
large-power note. No local expansion in the real angle $u$ is assumed.

## 2. The exact interpolation remains holomorphic

Write $\mathcal B_N(x,u)$ for the canonical Newton interpolation
used in the edge proof:

\[
 \mathcal B_N(x,u)=
 \frac{N}{
 G_N(N(1/2-x+u/(2\pi))-1/2)
 G_N(N(1/2-x-u/(2\pi))-1/2)G_N(Nx)^2}.                     \tag{2}
\]

The numerator is exactly $N$ by the canonical factorial reflection
identity. At $x=k/N$, this is $e_k(-2\cos u)$.

All contours below lie in the fixed wire rectangle

\[
 \mathcal R=\left\{x=\xi+ih:
       \frac{19}{100}\leq\xi\leq\frac{31}{100},
                       \quad |h|\leq\frac1{100}\right\}.  \tag{3}
\]

For real $|u|\leq\pi$, the real parts of the two midpoint
arguments $w_\pm=1/2-x\pm u/(2\pi)$ range between $-0.31$
and $0.81$. Their imaginary parts remain bounded. These are within
the domain of the uniform reciprocal-factorial estimate in
[the factorial and boundary-decay note](research_uniform_factorial_and_boundary_decay.md),
equations (4)–(5).

Crossing $\operatorname{Re}w_\pm=0$ creates no pole in (2). On its
negative side the exact expression is

\[
 \frac1{G_N(Nw-1/2)}
       =\frac{2\cos(\pi Nw)}N G_N(-Nw-1/2).                \tag{4}
\]

The reflected factorial is holomorphic there and the cosine factor
may vanish; neither introduces a pole. This agrees with the original
reciprocal factorial on the overlap around $w=0$. Thus (2), as a
function of the wire variable $x$, is holomorphic throughout a
neighborhood of every contour used here, also for $u=\pm\pi$.
The factor $G_N(Nx)$ remains in an ordinary nonzero bulk strip.

For $|t|\leq1/4$, the midpoint arguments involving $t$ remain in
positive bulk strips throughout $\mathcal R$. The standard bulk
estimate and the uniform reciprocal estimate therefore give

\[
 |\mathcal B_N(x,t)|\leq\frac CN e^{N\operatorname{Re}b(x,t)},
 \qquad
 |\mathcal B_N(x,u)|\leq\frac CN e^{N\mathfrak b(x,u)}.     \tag{5}
\]

The same canonical branches occur in both expressions. In particular,
$\mathfrak b(x,0)=\operatorname{Re}b(x,0)$ on $\mathcal R$.

Lemma 2 of the boundary-decay note states

\[
 \mathfrak b(x,u)-\mathfrak b(x,0)
 \leq-\frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h)}
                                      (1-\cos u).          \tag{6}
\]

On (3), $\sin(2\pi\xi)>9/10$ and
$\cosh^2(\pi h)<101/100$. The coefficient in (6) is larger
than $1/20$. Consequently the complete interpolated product obeys

\[
 |\mathcal B_N(x,t)\mathcal B_N(x,u)|
 \leq\frac C{N^2}
     e^{N\{\operatorname{Re}A_t(x)-(1-\cos u)/20\}}
                          \qquad(x\in\mathcal R).          \tag{7}
\]

This is the only replacement estimate needed. The loss is uniform
on the contour itself, not just at its lattice points.

## 3. The complete list of wire contours

Let $k_-$ and $k_+$ be the smallest and largest integers with
$k/N\in I$, and take the half-grid boundaries

\[
 \alpha_N=(k_--1/2)/N,\qquad
 \beta_N=(k_++1/2)/N.
\]

For all large $N$, the exact finite sum is the residue integral on
the rectangle with these vertical sides and horizontal heights
$\pm h_0$, where $h_0=1/500$. The kernel is $\pi N\cot(\pi Nx)$.
The edge proof then uses the following pieces:

1. The two initial horizontal lines, with the nonconstant cotangent
   remainders retained on those lines.
2. The two half-grid vertical sides, including the exact currents
   of the original cotangent kernel.
3. The vertical connectors that move the constant horizontal terms
   to the real interval $[\alpha_N,\beta_N]$.
4. The interval at height $\operatorname{Im}x_*(t)$ through the
   stationary point, together with its endpoint connectors.

For the second boundary fixed at zero, the critical equation is
$\cos(2\pi x_*)=(1-\cos t)/(3+\cos t)$. Since
$|\cos t-1|<0.032$, the right side has modulus less than $0.009$.
The branch
$x_*=1/4-(2\pi)^{-1}\arcsin((1-\cos t)/(3+\cos t))$
therefore satisfies the conservative bound

\[
 |x_*(t)-1/4|<0.003\qquad(|t|\leq1/4).                     \tag{8}
\]

Thus every listed contour has $|\operatorname{Im}x|\leq0.003$.
Its real part is between $\alpha_N$ and $\beta_N$, hence in a
fixed compact subinterval of $(0,1/2)$. All the contours lie inside
(3) for sufficiently large $N$.

The half-grid sides can extend $O(N^{-1})$ beyond $I$. One should not
apply a bound stated only on the closed interval $I$ without addressing
that extension. The following conservative Hessian bounds hold on the
larger rectangle (3):

\[
 |A_t''(x)|<46,\qquad \operatorname{Re}A_t''(x)<-11.
                                                               \tag{9}
\]

Here is a direct check. In

\[
 A_t''(x)=\sum_{v\in\{t,0\}}
 \left[-\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+\cos v}
                                      -2\pi\cot(\pi x)\right],
\]

one has $|\cos v-1|<0.032$. The bounds on (3) give

\[
 \begin{gathered}
 \operatorname{Re}\sin(2\pi x)>0.92,\quad
 |\operatorname{Im}\sin(2\pi x)|<0.024,\\
 \operatorname{Re}(\cos(2\pi x)+\cos v)>0.586,\quad
 |\operatorname{Im}(\cos(2\pi x)+\cos v)|<0.095,\quad
 |\cos(2\pi x)+\cos v|<1.42.
 \end{gathered}
\]

These imply
$\operatorname{Re}(\sin(2\pi x)/(\cos(2\pi x)+\cos v))>0.26$.
Also $\operatorname{Re}\cot(\pi x)>0.66$. Their sum proves
the negative real-part estimate in (9). For the modulus use
$|\sin(2\pi x)|<1.003$,
$|\cot(\pi x)|<1.001/0.53$, and the denominator bound $0.586$.
Then
$|A_t''|<4\pi(1.003/0.586+1.001/0.53)<46$.
All these elementary inequalities have slack; in particular they
apply on the half-grid sides as well as on $I$ itself.

## 4. Every correction retains the boundary loss

Write $x-x_*=X+iY$. Taylor's theorem using (9) gives

\[
 \operatorname{Re}(A_t(x)-\psi(t,0))
       \leq-\frac{11}{2}X^2+46|XY|+23Y^2.                 \tag{10}
\]

On a vertical side or an endpoint connector, for sufficiently large
$N$, one has $|X|\geq0.046$ and $|Y|\leq0.005$. The right side
of (10) is then less than $-1/3000$. Indeed it is maximized at the
smallest allowed $|X|$ and largest allowed $|Y|$, where it equals
$-0.000483$.

The half-grid cotangent has modulus at most one. Thus (7) bounds its
entire vertical current by a polynomial times

\[
 e^{N\{\operatorname{Re}\psi(t,0)
                    -(1-\cos u)/20-1/3000\}}.              \tag{11}
\]

The same estimate applies to each constant-mode endpoint connector.

On the original horizontal lines, $|Y|\leq0.005$. Maximizing
(10) in $X$ gives an excess less than $3/1000$. The nonconstant
cotangent remainder has the exact bound

\[
 O\left(Ne^{-2\pi Nh_0}\right),\qquad
 2\pi h_0=\pi/250>0.012.
\]

It therefore has a fixed exponential gap, in addition to the same
boundary loss in (7). There is no cancellation between different
cotangent corrections or between them and the vertical currents in
this estimate; each piece is bounded separately.

## 5. The translated main integral

The two constant horizontal terms give $N$ times the real integral,
with the already estimated endpoint connectors. The integrand
$\mathcal B_N(x,t)\mathcal B_N(x,u)$ is holomorphic by Section 2.
It can therefore be translated to the horizontal segment through
$x_*(t)$ without encountering a moving pole. Its new endpoint
connectors satisfy (11).

On this translated segment, (9) gives

\[
 \operatorname{Re}A_t(x)
       \leq\operatorname{Re}\psi(t,0)
                    -\frac{11}{2}(\operatorname{Re}x-
                                         \operatorname{Re}x_*)^2.
\]

Apply (7) there and integrate the real Gaussian upper bound. The
factor $N$ from the cotangent constant term, the factor $N^{-2}$
from (7), and the Gaussian width $N^{-1/2}$ give

\[
 CN^{-3/2}e^{N\{\operatorname{Re}\psi(t,0)-(1-\cos u)/20\}}.
\]

Every correction in Section 4 has an extra fixed exponential loss
and a polynomial prefactor, so it is absorbed into this bound.
Increasing $C$ handles the finitely many small levels, including
any level with no retained integer. This proves (1).

The shift of the main integral is essential: it preserves the
cancellation encoded by the complex wire saddle before taking an
absolute value. The real-boundary factor is replaced only through
(7), after this exact holomorphic deformation has been justified.
Its moving reciprocal-factorial zeros never create additional residues.

## 6. Scope of the conclusion

Equation (1) is uniform for the entire real parent period while the
other boundary remains in $|t|\leq1/4$. It therefore supplies the
weighted bound on the lower horizontal segment and the endpoint
currents in the terminal large-power trace argument. The omitted
wire indices and the outer angular grid terms still require their
separate estimates; this lemma does not silently replace them by the
retained kernel. It also makes no statement about a different, deeper
wire deformation outside (3).
