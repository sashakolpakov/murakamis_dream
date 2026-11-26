# Stationary geometry for terminal powers of magnitude at least three

Research note, 2 November 2026. This establishes the selected stationary
point, the original factorial bulk conditions, and a positive real
quadratic form at that point for every fixed terminal crossing power
$|n|\ge3$. It does not prove the full finite-source asymptotic for those
powers. In particular, global contour and Fourier remainder estimates
are still required. Frozen manuscripts are unchanged.

## 1. The phase and its selected leaf solution

Use the edge phase from the circle-tree papers:

\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                  (\tan(t/2)\cos(u/2)),\qquad
 \psi(0,0)=\frac{v_{\rm oct}}\pi.
\]

The original unit-charge leaf phase, before filling its parent, is

\[
 S_n(t,u)=\psi(t,u)+\frac{in}{4\pi}t^2-it.
\]

We first take a positive integer $n$ and set the parent angle $u=0$.
Write $t=2a-2ib$, with $0<a<\pi/2$ and $b>0$. On this strip,

\[
 \operatorname{arsinh}(\tan(t/2))
 =\operatorname{artanh}\frac{\sin a}{\cosh b}
       -i\arctan\frac{\sinh b}{\cos a}.
\]

Indeed $R=\sec(t/2)+\tan(t/2)$ satisfies

\[
 R=\frac{\cos a-i\sinh b}{\cosh b-\sin a},
\]

so its real part is positive and its logarithm is on one fixed branch.
The saddle equation is therefore equivalent to

\[
 \sin a=\cosh b\tanh(nb),\qquad
 na+\arctan\frac{\sinh b}{\cos a}=\pi.                 \tag{1}
\]

For fixed $n\ge1$, the function $\cosh b\tanh(nb)$ is strictly
increasing from zero to infinity. The first equation defines an
increasing function $b=b_n(a)$. The left side of the second equation
is strictly increasing from zero to $(n+1)\pi/2$ as $a$ increases
from zero to $\pi/2$. For every $n\ge2$ there is consequently one
interior solution of (1). It satisfies $a<\pi/n$.

The stationary point is nondegenerate:

\[
 S_{n,tt}(t,0)=\frac{-\sec(t/2)+in}{2\pi},\qquad
 \Re S_{n,tt}(t,0)<0.                                  \tag{2}
\]

The inequality holds throughout the right lower strip, since the
real part of $\cos(t/2)$ and of its reciprocal are positive. Thus
the solution extends holomorphically to a small complex parent disk.
For negative powers the selected solution at real parent angle is
$t_{-n}=-\overline{t_n}$, with the corresponding continued branches.

Exponentiating the stationary equation with $w=e^{it/2}$ gives

\[
 w^{n+1}-iw^n-iw+1=0.                                  \tag{3}
\]

Equation (1), rather than (3) alone, selects the original logarithmic
branch. Exponentiation by itself would also admit unwanted roots.

## 2. The original wire saddle stays in the factorial bulk for $n\ge3$

Set

\[
 k=\cos(t_n/2)=\cos(a-ib),\qquad
 x_n=\frac1\pi\arctan k.
\]

The arctangent is continued from the positive real axis. These are
the critical wire coordinates of the original two-variable edge sum.
The nontrivial real-part condition for its factorial arguments is

\[
 \Re x_n+\frac{a}{\pi}<\frac12.                        \tag{4}
\]

The first equation in (1) gives, for $n\ge2$,

\[
 \sin a=\cosh b\tanh(nb)
 \ge\cosh b\tanh(2b)>\sinh b.
\]

Hence

\[
 1-|k|^2=\sin^2a-\sinh^2b>0.
\]

Also $\Re k>0$ and $\Im k>0$. In the formula
$e^{2\pi ix_n}=(1+ik)/(1-ik)$, its argument is the argument of
$(1-|k|^2)+2i\Re k$, which lies between zero and $\pi/2$.
Therefore

\[
 0<\Re(\pi x_n)<\pi/4.
\]

For $n\ge4$, combine this with $a<\pi/n\le\pi/4$ to obtain (4).
For all $n\ge5$ it even gives the uniform margin
$\Re x_n+a/\pi<9/20$.

The remaining value $n=3$ can be handled exactly. Divide (3) by
$w^2$ and write $w+w^{-1}=2k$. One obtains

\[
 2k^2-ik-1=0,\qquad k=\frac{\sqrt7+i}{4}.
\]

Consequently

\[
 \Re(\pi x_3)=\frac12\arctan\sqrt7<\frac\pi5,
 \qquad
 \cos^2a=\frac{3-\sqrt2}{4},\qquad a<\frac{3\pi}{10}.
\]

For the first inequality use
$\tan^2(2\pi/5)=5+2\sqrt5>7$; for the second compare
$(3-\sqrt2)/4$ with $\cos^2(3\pi/10)=(5-\sqrt5)/8$.
Their sum proves (4) for $n=3$ as well.

Thus the original canonical factorial interpolation is regular at
every selected saddle with $|n|\ge3$. The argument needs no change
to the factorial function and no unproved continuation across its
bulk boundary. For each fixed $n$, the same is true in a complex
neighborhood of the saddle and of the parent origin.

This distinguishes the two-crossing case: there
$k=(1+i)/2$, and the analogous original joint saddle violates (4).
Its successful proof used the separate exact one-index reduction in
[the two-crossing terminal note](research_two_crossing_terminal_filling.md).

## 3. The original joint saddle has a negative-definite real Hessian

Let $J$ and $b$ have the same normalization as in the two-crossing
note, and consider the original joint phase

\[
 \mathcal F_n(x,t)=b(x,t)+b(x,0)+\frac{in}{4\pi}t^2-it.
\]

At its selected saddle put $k=\cos(t_n/2)$ and $s=\sin(t_n/2)$.
Direct differentiation gives

\[
 \begin{aligned}
 H_{xx}&=-\frac{2\pi(1+k^2)^2}{k^3},\\
 H_{xt}&=-\frac{s(1+k^2)}{k^3},\\
 H_{tt}&=\frac{-k^{-3}+in}{2\pi}.                       \tag{5}
 \end{aligned}
\]

The complex Schur complement of $H_{xx}$ is exactly (2). More is
true: the real part of the entire two-variable Hessian is negative
definite for every $n\ge3$.

Write

\[
 X=\sin^2a,\quad Y=\sinh^2b,\quad D=1-X+Y=|k|^2,
 \quad p=\Re k=\sqrt{(1-X)(1+Y)}.
\]

For $n=3$ the exact values above give

\[
 X=(1+\sqrt2)/4<5/8,\qquad Y=(\sqrt2-1)/4<1/8.
\]

For $n\ge4$, one has $X<1/2$. Furthermore,
$\cosh b\tanh(nb)\ge\cosh b\tanh(3b)$, and in terms of
$B=\sinh b$ the latter is $B(3+4B^2)/(1+4B^2)$. At
$B=1/(2\sqrt2)$ this equals $7/(6\sqrt2)>1/\sqrt2$.
Since $\sin a<1/\sqrt2$, equation (1) forces $Y<1/8$.
Thus every $n\ge3$ lies in the rectangle

\[
 0\le X<5/8,\qquad 0\le Y<1/8.                        \tag{6}
\]

Taking real parts of (5) yields

\[
 \Re H_{tt}=-\frac{p(D-4XY)}{2\pi D^3}<0,
\]

because $D-4XY\ge3/16$ on (6). A direct expansion gives

\[
 \det(\Re H)=\frac{(1-X)Q(X,Y)}{D^4},
\]

\[
 \begin{aligned}
 Q(X,Y)={}&(1-X)(2-X)^2
       +(11X^2-22X+8)Y\\
       &+(4X^2-19X+5)Y^2+(1-4X)Y^3.
 \end{aligned}
\]

Each coefficient has an elementary lower bound on (6), giving

\[
 Q(X,Y)\ge\frac{363}{512}-\frac{93}{512}
                  -\frac{85}{1024}-\frac3{1024}
          =\frac{113}{256}>0.
\]

Therefore $\Re H$ is negative definite. This supplies a legitimate
local horizontal Gaussian contour in the original two variables,
with a nonzero Gaussian determinant. It also persists for small
complex parent parameters. It does not establish that this local
contour represents the whole original finite trace.

## 4. The other interior Fourier saddles

Replace the unit charge by a positive real charge $\ell$:

\[
 S_{n,\ell}(t,0)=\psi(t,0)+\frac{in}{4\pi}t^2-i\ell t.
\]

The same increasing function in (1) now has value $\pi\ell$.
An interior saddle in the right lower strip exists exactly when
$0<\ell<(n+1)/2$. Along this branch, stationarity gives

\[
 \frac d{d\ell}\Re S_{n,\ell}(t_{n,\ell},0)
           =\Im t_{n,\ell}<0.
\]

Thus every interior positive integer charge greater than one has
strictly smaller stationary real action than the unit charge.
Charges reaching the boundary or lying beyond it require separate
endpoint and contour estimates. This monotonicity is a statement
about the selected actions, not a proof that all terms of the exact
Fourier expansion have been controlled.

## 5. The remaining analytic step

The missing theorem is still a whole-source statement. One must:

1. Construct a contour for the exact finite wire sum and the exact
   leaf trace that reaches the joint saddle without dropping the
   moving-grid correction terms or crossing unaccounted poles.
2. Bound every vertical connector, lattice mode, and endpoint term
   below the unit-charge action. Local bulk regularity and a
   negative-definite Hessian do not imply these global inequalities.
3. Sum the nonminimal Fourier charges, including those with no
   interior saddle, with an error below the surviving contribution.
4. Preserve a uniform open-boundary estimate after this calculation,
   strong enough for further gluing and remaining long fillings.

The current small common chart in the frozen paper is insufficient
for these short powers. The facts above show that $n\ge3$ does not
have the factorial-boundary obstruction of $n=2$, and that the
original joint local saddle is well behaved. They identify a viable
local starting point for the next global argument; they do not close
the finite-exception goal.
