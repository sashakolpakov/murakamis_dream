# A certified central phase estimate for three terminal crossings

Research proof, 2 November 2026. This note proves inequalities for the
limiting phase of the original two-variable terminal source. It includes
the connecting surfaces and the exponential penalties that arise from
the lower side of a finite Abel–Plana contour. The proof combines a local
negative Hessian with a finite covering by rational rectangles and
rigorous interval bounds.

The result is an analytic ingredient for the three-crossing terminal
asymptotic. A finite-sum contour identity, and uniform estimates comparing
its exact integrand with this limiting phase, are separate statements.
No volume limit is inferred from the phase inequalities alone.

## 1. The phase and its branches

Write $i^2=-1$. For real $0<w<1$, let

\[
 J(w)=\int_0^w\log(2\sin(\pi v))\,dv.
\]

Let $J_+$ and $J_-$ denote its continuations above and below zero,
respectively. For upper-half-plane arguments, the explicit formula is

\[
 J_+(w)=-\frac{i\pi}{2}(w^2-w)
       +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iw})
       -\frac{i\pi}{12}.
 \tag{1}
\]

The lower continuation is evaluated as

\[
 J_-(w)=-J_+(-w)-i\pi w.                           \tag{2}
\]

These formulas specify the continuation when a denominator factorial
passes its first zero. In particular, a negative real argument is
approached from its specified side. The two values need not be equal.
The exact factorial identities supporting these choices are proved in
[the continuation note](research_terminal_reflected_factorials.md).

Put $p=1/2+t/(2\pi)$ and $m=1/2-t/(2\pi)$. On every surface considered
below, $\Im t\le0$. The imaginary parts of $p-x$ and $m-x$ have
nonpositive and nonnegative signs, respectively. If
$\varepsilon\in\{+1,-1\}$ is the sign of the imaginary part of $x$,
define

\[
 \begin{aligned}
 b(x,t)&=J_-(p)+J_+(m)-J_-(p-x)-J_+(m-x)
                                      -2J_\varepsilon(x),\\
 b(x,0)&=2J(1/2)-2J_{-\varepsilon}(1/2-x)
                                      -2J_\varepsilon(x).
 \end{aligned}                                                   \tag{3}
\]

At a real argument the one-sided values prescribed by the surface
are used. On the initial region where the cosine factors are positive,
(3) is precisely

\[
 b(x,t)=\int_0^x
          \log(2\cos(2\pi v)+2\cos t)\,dv-2J(x).
\]

The phase for three positive crossings and Fourier charge one is

\[
 \Phi(x,t)=b(x,t)+b(x,0)+\frac{3it^2}{4\pi}-it.
 \tag{4}
\]

All inequalities in this note concern its real part with the branches
in (3). Formula (3) is necessary on the negative-angle and lower-wire
surfaces; silently substituting the other continuation would change
the quantity being bounded.

## 2. The selected saddle

Set

\[
 k=\frac{\sqrt7+i}{4},\qquad
 x_*=\frac{\arctan k}{\pi},\qquad t_*=2\arccos k,
 \qquad M=\Re\Phi(x_*,t_*).
 \tag{5}
\]

The branches have $0<\Re x_*<1/2$, $0<\Re t_*<\pi$,
$\Im x_*>0$, and $\Im t_*<0$. The stationary equations and their
chosen logarithms are proved in
[the terminal-power note](research_terminal_powers_three_and_above.md).
Thus stationarity in this proof is an exact mathematical fact, not a
claim based on a small numerical derivative.

Define the positive heights

\[
 h_x=\Im x_*=\frac{\log2}{4\pi},\qquad
 h_t=-\Im t_*
     =2\operatorname{arsinh}\sqrt{\frac{\sqrt2-1}{4}}.
 \tag{6}
\]

They satisfy $h_t/(2\pi)>h_x$. This verifies the denominator branch
signs stated after (2), including when the wire height is reduced
independently of the angular height. Approximately,

\[
 \begin{aligned}
 x_*&=0.19248663596+0.05515890004i,\\
 t_*&=1.77941301710-0.63297431920i,\\
 M&=0.84885122850.
 \end{aligned}
\]

The displayed decimals are explanatory. All comparisons below use
rigorous enclosures of the exact expressions (5)–(6).

## 3. The central rectangle

Put

\[
 \alpha=\frac3{32},\qquad \beta=\frac{13}{32},
 \qquad T=\frac{2\pi}{3}.
\]

On the rectangle

\[
 x=\xi+ih_x,\quad t=\tau-ih_t,\qquad
 \alpha\le\xi\le\beta,\quad 0\le\tau\le T,             \tag{7}
\]

the real phase has its unique maximum $M$ at $(x_*,t_*)$.
More precisely, let $r=\tau/(2\pi)$ and

\[
 Q=[9/50,1/5]\times[27/100,29/100]
\]

in the $(\xi,r)$ plane. Outside $Q$, the certificate proves

\[
 \Re\Phi(\xi+ih_x,2\pi r-ih_t)
               <M-\frac1{100000}.                  \tag{8}
\]

Inside $Q$, the real Hessian is negative definite everywhere.
The exact saddle lies in the interior of $Q$. Strict concavity on
this convex rectangle, together with exact stationarity, proves
that equality with $M$ occurs only at the saddle.

This argument does not assert concavity on the whole rectangle (7).
Such an assertion is false, as shown by the
[translated-Hessian counterexample](research_terminal_reflected_factorials.md#3-the-translated-phase-is-not-concave-on-its-whole-central-domain).

On the negative-angle rectangle with the same upper wire height,
one has the separate bound

\[
 \Re\Phi(\xi+ih_x,\tau-ih_t)<M-\frac1{10},
 \qquad \alpha\le\xi\le\beta,\quad -T\le\tau\le0.
 \tag{9}
\]

For the entire lower-wire rectangle, the bound includes its lattice
penalty:

\[
 \Re\Phi(\xi-ih_x,\tau-ih_t)-2\pi h_x
                   <M-\frac1{20},
 \qquad \alpha\le\xi\le\beta,\quad |\tau|\le T.
 \tag{10}
\]

## 4. Connecting surfaces

The following notation describes all the surfaces in the certificate.
Let $\xi$ range over $[\alpha,\beta]$, let $e$ be either endpoint
$\alpha$ or $\beta$, let $\tau$ range over $[-T,T]$, and let
$s,v\in[0,1]$. The signs $\epsilon,\sigma$ are independently chosen
from $\{+1,-1\}$. A penalty is subtracted from $\Re\Phi$.
Write $c_\epsilon=0$ for $\epsilon=+1$ and
$c_\epsilon=2\pi h_x$ for $\epsilon=-1$.

| Surface | $x$ | $t$ | Subtracted penalty |
|---|---|---|---|
| Angular cutoff | $\xi+\epsilon ih_xs$ | $\sigma T-ih_ts$ | $c_\epsilon s$ |
| Wire endpoint with coupled heights | $e+\epsilon ih_xs$ | $\tau-ih_ts$ | $c_\epsilon s$ |
| Wire endpoint at the bottom angular contour | $e+\epsilon ih_xv$ | $\tau-ih_t$ | $c_\epsilon v$ |
| Wire endpoint inside an angular connector | $e+\epsilon ih_xvs$ | $\sigma T-ih_ts$ | $c_\epsilon vs$ |

On every surface in this table, including its boundary,

\[
 \Re\Phi(x,t)-\text{penalty}<M-\frac1{1000}.          \tag{11}
\]

The last row is needed when the wire contour is evaluated inside
an already deformed angular connector. It is a two-parameter curved
surface, not an affine rectangle in $(x,t)$. Its mixed second
derivative therefore includes the term
$\Phi_x\,\partial_s\partial_v x$; the calculation retains this term.
For $\epsilon=-1$ it also retains the mixed derivative of
$2\pi h_xvs$.

The penalties in (10)–(11) are part of the statements. No estimate
without the indicated penalty is claimed for a lower-wire surface.

The certificate also verifies the useful constant comparison

\[
 M-2g(\alpha)>\frac{19}{1000},\qquad
 g(x)=J(2x)-4J(x).
 \tag{12}
\]

Here $2g(\alpha)$ is about $0.82973861647$. Applying (12) to discard
parts of the original finite wire sum requires the corresponding
finite-source bound; (12) by itself is only an explicit comparison
of two constants.

## 5. How the finite certificate proves the inequalities

All parameters are represented by exact rational numbers. All
transcendental values and their errors are enclosed by Arb/Acb
arithmetic at 120-bit precision.

The local rectangle $Q$ is divided into a $32$ by $32$ grid.
On each of its 1024 closed rectangles, interval evaluation proves

\[
 \Re\Phi_{xx}<0,\qquad
 (\Re\Phi_{xx})(\Re\Phi_{tt})-(\Re\Phi_{xt})^2>0.
 \tag{13}
\]

The use of $r=t/(2\pi)$ changes the Hessian by a positive diagonal
congruence and therefore preserves negative definiteness.
The derivative formulas used in (13) are

\[
 \begin{aligned}
 \Phi_{xx}
  &=-\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+\cos t}
    -4\pi\cot(\pi x)
    -\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+1},\\
 \Phi_{xt}
  &=-\frac{\sin t}{\cos(2\pi x)+\cos t},\\
 \Phi_{tt}
  &=-\frac{\tan(\pi x+t/2)+\tan(\pi x-t/2)}{4\pi}
                                             +\frac{3i}{2\pi}.
 \end{aligned}                                                   \tag{14}
\]

For each other surface, the algorithm starts with its complete
closed parameter rectangle. A rectangle is accepted only after a
rigorous upper bound is smaller than the stated target. Otherwise,
it is bisected into two closed rectangles. The process finishes
with a finite covering of the initial domain.

Two bounds are available. The first directly evaluates (1)–(4) on
the parameter rectangle. The second uses Taylor's theorem. For a
real function $f$ on a parameter rectangle with center $c$ and
half-widths $a,b$, interval enclosures of its derivatives give

\[
 f\le f(c)+|f_1(c)|a+|f_2(c)|b
       +\frac12\left(C_{11}a^2+2C_{12}ab+C_{22}b^2\right),
 \tag{15}
\]

where $C_{jk}$ bounds $|f_{jk}|$ throughout the rectangle. The chain
rule in (15) is applied to the parameterized surface, including its
second derivatives and the derivatives of any subtracted penalty.
An indeterminate interval cannot pass an acceptance test; it leads
to further subdivision or to the direct bound below.

There is one continuous branch point to handle explicitly. When a
rectangle meets $w=0$, a direct dilogarithm enclosure may be
indeterminate. For $|w|\le\rho<1/(2\pi)$, the convergent expansion

\[
 J(w)=w(\log(2\pi w)-1)
       -\sum_{m\ge1}
          \frac{\zeta(2m)w^{2m+1}}{m(2m+1)}
\]

gives the conservative bound

\[
 |J(w)|\le
 \rho\bigl(1-\log(2\pi\rho)+2\pi\bigr)
       +\frac{\pi^2\rho^3}{18(1-\rho^2)}.           \tag{16}
\]

The branch arguments used here have absolute value less than
$2\pi$; in the prescribed half-planes the sharper bound $\pi$
would suffice. The estimate uses
$\zeta(2m)\le\pi^2/6$ and
$m(2m+1)\ge3$. Also
$r(1-\log(2\pi r))$ is increasing for $0<r<1/(2\pi)$.
Formula (16) supplies a valid enclosure of the limiting value at
zero. It avoids any assumption of differentiability there.

The selected action is enclosed by an interval of radius less than
$5\cdot10^{-34}$. The comparisons in (8)–(12) use strict interval
inequalities against rational gaps. They do not compare rounded
decimal approximations.

## 6. Reproduction and scope

The complete calculation is in
[the certificate script](../experiments/certify_terminal_three_central_phase.py).
Run it from the repository root:

    python3 experiments/certify_terminal_three_central_phase.py \
      --output repro/results/research-terminal-three-central-phase.json

It requires the Python package python-flint. The
[saved certificate](../repro/results/research-terminal-three-central-phase.json)
contains every accepted rational rectangle, its method of
acceptance, and its certified upper bound. The local Hessian grid
is specified separately. The code never uses a floating-point
optimizer to accept a rectangle.

Together, (7)–(11) establish a unique maximum and strict boundary
gaps for these particular limiting-phase surfaces. To obtain the
asymptotic of the original finite source, one still needs the exact
residue decomposition, the factorial upper bounds on its moving
boundaries, and its local leading coefficient. Those statements
are not replaced by the interval calculation.
