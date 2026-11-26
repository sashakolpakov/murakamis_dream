# The open boundary left by three terminal crossings

Research proof, 2 November 2026. This note derives the asymptotic of the
original terminal polynomial with crossing power three. It treats the
whole finite source, including the first derivatives at repeated
spectral roots and both parities of the level. The boundary variable
remains free in a fixed complex neighborhood of the complete value.
The final estimate also controls a whole real period and a thin
complex strip.

The proof uses three ingredients established separately: an exact
trace formula with a rational kernel, a finite contour formula for the
wire sum, and a rigorous certificate for the limiting phase on the
required surfaces. The exact factorial bounds connect that certificate
to the finite integrands, including their moving zeros.

## 1. The finite polynomial and the statement

Fix an integer $N\ge3$, and put

\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad \eta=(-1)^d,\qquad
 S_k=\prod_{j=1}^k2\sin(\pi j/N).
\]

An empty product equals one. Let

\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}(c_j-z),
 \qquad 0\le k<N.
\]

The algebra is $\mathbb C[z]/(T_N(z)+2)$, where the monic Chebyshev
polynomial is defined by $T_N(w+w^{-1})=w^N+w^{-N}$. The original
positive crossing and the closing functional are

\[
 R=q^{d^2/2}\sum_{k=0}^d(-q)^ke_k,\qquad
 \phi(f)=(-1)^dN^2[z^d]\operatorname{rem}_{T_N+2}f.
\]

In particular, $\phi(e_i e_j)=1$ when $i+j=d$ and is zero otherwise.
This functional acts on the full quotient algebra; it includes the
first derivatives at double roots.

The terminal polynomial and its boundary-angle form are

\[
 \mathcal H_{3,N}(z)=\sum_{k=0}^d\phi(R^3e_k)e_k(z),
 \qquad H_{3,N}(u)=\mathcal H_{3,N}(-2\cos u).
 \tag{1}
\]

Thus $H_{3,N}$ is even, entire, and $2\pi$-periodic. The exact scalar
that will remain outside the asymptotic is

\[
 C_{N,3}=q^{3d^2/4}
        =\exp\left(\frac{3\pi i d^2}{4N}\right).
 \tag{2}
\]

No expansion or change of this scalar is made.

For real $0<x<1/2$ and initially small boundary angles, define

\[
 J(x)=\int_0^x\log(2\sin(\pi v))\,dv,\qquad
 b(x,t)=\int_0^x
       \log(2\cos(2\pi v)+2\cos t)\,dv-2J(x).
\]

Continue the functions from this region with the factorial branches
specified below. Put

\[
 \Phi(x,t;u)=b(x,t)+b(x,u)+\frac{3it^2}{4\pi}-it.
 \tag{3}
\]

At $u=0$, the selected critical point is

\[
 k_*=\frac{\sqrt7+i}{4},\qquad
 x_*=\frac{\arctan k_*}{\pi},\qquad
 t_*=2\arccos k_*.
 \tag{4}
\]

Its branches satisfy $\Im x_*>0$, $\Im t_*<0$,
$0<\Re x_*<1/2$, and $0<\Re t_*<\pi$. Its Hessian is invertible.
Let $(x(u),t(u))$ be the holomorphic critical point continuing (4),
and set

\[
 S_3(u)=\Phi(x(u),t(u);u),\qquad
 H(u)=D^2_{x,t}\Phi(x(u),t(u);u).
 \tag{5}
\]

The square root below is the Gaussian branch: at zero it is the
branch obtained by integrating the quadratic form on the real
horizontal tangent plane, where $\Re(-H(0))$ is positive definite.
It is then continued holomorphically.

**Theorem.** There is a disk $|u|<\rho$ on which

\[
 \boxed{\quad
 H_{3,N}(u)
   =C_{N,3}A_3(u)e^{NS_3(u)}\bigl(1+O(N^{-1})\bigr),\qquad
 A_3(u)=
 \frac{i\sin t(u)}
 {2\sin^2(\pi x(u))\sqrt{\det(-H(u))}} .
 \quad}                                                   \tag{6}
\]

The amplitude is holomorphic and nonzero after reducing $\rho$ if
necessary. The error is uniform on a fixed smaller closed disk.
Every fixed derivative of the normalized error has the same order
on a still smaller disk. Formula (6) holds for every sufficiently
large integer $N$, without restricting its parity.

Write $M=\Re S_3(0)$. There are positive constants $c,C,B,\rho_1$
and a fixed exponent $A$ such that

\[
 |H_{3,N}(a+ib)|
 \le CN^A
   \exp\left[N\{M-c(1-\cos a)+Bb^2\}\right],
 \qquad |a|\le\pi,\quad |b|\le\rho_1.
 \tag{7}
\]

The opposite crossing power satisfies the conjugate statements:
$H_{-3,N}(u)=\overline{H_{3,N}(\bar u)}$.

For orientation, the exact constants in (4)–(6) have approximate
values

\[
 \begin{aligned}
 x_*&=0.19248663596+0.05515890004i,\\
 t_*&=1.77941301710-0.63297431920i,\\
 M&=0.84885122850,\\
 A_3(0)&=-0.18858767319+0.31315381281i.
 \end{aligned}
\]

These numbers are not premises of the proof. The estimates use
exact expressions and rigorous enclosures.

## 2. The exact source and the wire cutoff

Define

\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u).
\]

Then (1) is exactly $\mathcal D_{3,N}[K_N(\,\cdot\,,u)]$, where
$\mathcal D_{3,N}[f]=\phi(R^3f^\sharp)$ for
$f(t)=f^\sharp(-2\cos t)$.

We first remove wire indices whose complete norms are too small
to contribute at rate $M$. Put

\[
 \alpha=3/32,\qquad \beta=13/32,\qquad
 g(x)=J(2x)-4J(x).
\]

Choose half-grid endpoints
$a_N=\alpha+O(N^{-1})$ and $b_N=\beta+O(N^{-1})$, so
$Na_N,Nb_N\in\mathbb Z+1/2$. Retain the indices

\[
 I_N=\{k: a_N<k/N<b_N\},
 \qquad
 K_{I,N}(t,u)=\sum_{k\in I_N}e_k(-2\cos t)e_k(-2\cos u).
 \tag{8}
\]

The [complete basis estimates](research_terminal_powers_qbinomial.md#4-a-uniform-bound-near-the-other-endpoint)
give, with polynomial factors uniform in the index,

\[
 |\phi(R^3e_k)|+
       \sup_{u\in[-\pi,\pi]}|e_k(-2\cos u)|
 \le CN^A
 \begin{cases}
 e^{Ng(k/N)},&k\le\lfloor d/2\rfloor,\\
 1,&k>\lfloor d/2\rfloor.
 \end{cases}                                             \tag{9}
\]

The coefficients in (9) retain the first normal derivatives;
the estimate is not based on distinct spectral values alone.
Since $g'(x)=2\log\cot(\pi x)$ and $g(1/2-x)=g(x)$,
the omitted low indices have $g(k/N)\le g(\alpha)+O(N^{-1})$.
The certificate proves

\[
 2g(\alpha)<M-\frac{19}{1000}.                    \tag{10}
\]

Thus the total omitted part of (1) is bounded by a polynomial in
$N$ times $e^{2Ng(\alpha)+O(1)}$, uniformly for real $u$.
For small complex $u$, the polynomial Bernstein inequality on
$[-2,2]$ costs at most $e^{N|\Im u|}$, so a sufficiently small
fixed disk preserves this strict gap.

Notice the order of this reduction. The wire terms are removed
from the original finite polynomial, before applying a contour
formula. No estimate for a complete sum is assigned to an
uncontrolled partial sum.

## 3. The angular cutoff, including the normal terms

For an even polynomial function $f(t)$, put

\[
 G_f(t)=\sin t\,f(t)e^{3iNt^2/(4\pi)},\qquad
 \tau_j=\frac{2\pi}{N}\left(\frac d2-j\right).
\]

The [exact complete trace](research_exact_complete_trace_contour.md)
is

\[
 \mathcal D_{3,N}[f]
          =\eta C_{N,3}\sum_{j=0}^{N-1}G_f'(\tau_j).
 \tag{11}
\]

Both $G_f$ and its derivative here are the original finite
functions. In particular, the derivative sampling includes the
double-root normal terms and the odd-level simple node.

Let $T=2\pi/3$, and choose an angular half-grid cutoff
$T_N\ge T$, $T_N=T+O(N^{-1})$, with $e^{iNT_N}=-\eta$.
For real $u$, the
[outer-angle proof](research_terminal_real_angle_tail.md)
applies to the absolute sum defining (8):

\[
 \sup_{T_N\le |t|\le\pi}|K_{I,N}(t,u)|
          \le CN^A e^{N\psi(T,0)},\qquad
 \psi(T,0)<4/5<M.                                  \tag{12}
\]

To justify the asserted uniformity in $u$, (9) bounds each parent
factor by a polynomial times $e^{Ng(k/N)}$. The proof of the
outer-angle inequality bounds the absolute rate of each remaining
summand by the same function used at the complete parent. Restricting
the wire indices can only decrease this absolute upper sum.
Small complex $u$ again adds at most $N|\Im u|$ to its exponent.

As a function of $z=-2\cos t$, the truncated kernel has degree at
most $N-1$. Applying Markov's inequality on the interval
$[-2\cos T_N,2]$ bounds its $z$ derivative with polynomial cost.
Its $t$ derivative has the same property. Since

\[
 G_f'(t)=
 \left(\cos t\,f(t)+\sin t\,f'(t)
       +\frac{3iN}{2\pi}t\sin t\,f(t)\right)e^{3iNt^2/(4\pi)},
\]

all removed terms of (11), including their derivatives, have a
strict rate gap. This completes the finite angular truncation.

## 4. The exact nested contour decomposition

For the retained angular nodes the rational trace formula is

\[
 \begin{aligned}
 \eta C_{N,3}\sum_{|\tau_j|<T_N}G_f'(\tau_j)
 ={}&-\frac{N^2C_{N,3}}{\pi i}
       \int_{-T_N-ih_t}^{T_N-ih_t}G_f(t)W_N(t)\,dt\\
 &+\frac{\eta N^2C_{N,3}}{\pi}
       \int_{-h_t}^{h_t}
       \frac{G_f(T_N+iv)}{4\cosh^2(Nv/2)}\,dv,
 \end{aligned}                                             \tag{13}
\]

where

\[
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 h_x=\Im x_*,\qquad h_t=-\Im t_*.
\]

Here $f(t)=K_{I,N}(t,u)$. Formula (13) is exact at each $N$.
The rational kernel has already summed every positive Fourier
charge, with the coefficient required by the normal derivative.
On its horizontal contour,

\[
 W_N(t)=e^{-iNt}\bigl(1+O(e^{-Nh_t})\bigr)
 \tag{14}
\]

uniformly. It will only be replaced by its leading term after
the full integrand has been bounded.

For the wire variable, let

\[
 B_N(x,t)=
 \frac{G_N(d/2+Nt/(2\pi))G_N(d/2-Nt/(2\pi))}
 {G_N(d/2-Nx+Nt/(2\pi))G_N(d/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{15}
\]

The symbol $G_N$ in (15) is the canonical factorial, not the odd
trace function $G_f$. At each retained wire node,
$B_N(k/N,t)=e_k(-2\cos t)$ exactly. The reciprocal factorial
continuations show that (15) is holomorphic on all wire rectangles
used below, including where a denominator argument crosses zero.

Apply the [one-sided wire formula](research_terminal_one_sided_wire_formula.md)
to $F(x)=B_N(x,t)B_N(x,u)$. For height $h>0$ the wire sum is

\[
 \begin{aligned}
 \sum_{k\in I_N}F(k/N)
 ={}&N\int_{a_N}^{b_N}F(\xi+ih)\,d\xi\\
 &+N\int_{a_N}^{b_N}F(\xi+ih)
          \frac{E_+}{1-E_+}\,d\xi\\
 &+N\int_{a_N}^{b_N}F(\xi-ih)
          \frac{E_-}{1-E_-}\,d\xi\\
 &-iN\int_{-h}^{h}
       \frac{F(b_N+iy)-F(a_N+iy)}
            {1+e^{-2\pi Ny}}\,dy,
 \end{aligned}                                             \tag{16}
\]

with $E_+=e^{2\pi iN(\xi+ih)}$ and
$E_-=e^{-2\pi iN(\xi-ih)}$.
The first integral has coefficient $N$. The upper and lower
corrections each have an exponential weight at most a constant
times $e^{-2\pi Nh}$. The endpoint weight is at most one for
$y\ge0$ and at most $e^{-2\pi N|y|}$ for $y\le0$.

On the horizontal angular contour in (13), choose $h=h_x$ in
(16). This gives the upper main rectangle, two horizontal wire
corrections, and the two full endpoint currents at fixed angular
depth.

For the vertical angular current, oddness gives
$G_f(T_N+iv)=-G_f(-T_N-iv)$ for $v\ge0$. Thus both halves can
be estimated on lower contours

\[
 t=\pm T_N-ih_ts,\qquad 0\le s\le1.
 \tag{17}
\]

Their exact angular weight is bounded by $e^{-Nh_ts}$, the
modulus of the unit-charge factor $e^{-iNt}$. For
$s\ge N^{-1}$, apply (16) with $h=h_xs$. The horizontal correction
denominators obey
$1-e^{-2\pi Nh_xs}\ge1-e^{-2\pi h_x}>0$.
The wire endpoint currents include every point

\[
 x=a_N\pm ih_xvs\ \text{or}\ b_N\pm ih_xvs,\qquad
 t=\pm T_N-ih_ts,\qquad 0\le v\le1.                \tag{18}
\]

These nested surfaces, rather than only their diagonal corners,
are the ones used in the phase certificate.

## 5. The small part of the angular connector

For $0\le s\le N^{-1}$, do not separate the four wire terms in
(16). Keep the original truncated polynomial $K_{I,N}(t,u)$.
The uniform real interval bound (12) is already available for
that polynomial.

The Bernstein–Walsh inequality on $[-2\cos T_N,2]$ extends (12)
to $t=\pm T_N-ih_ts$, $s\le N^{-1}$. The displacement in the
polynomial variable is $O(N^{-1})$. At an interval endpoint its
ellipse coordinate has logarithm $O(N^{-1/2})$. Consequently

\[
 |K_{I,N}(\pm T_N-ih_ts,u)|
     \le CN^A
       \exp\{N\psi(T,0)+C\sqrt N\}.                  \tag{19}
\]

This holds uniformly for real $u$; a small fixed complex disk
costs the additional factor already described after (12).
The crossing chirp has modulus $e^{O(1)}$ on this interval,
the sine factor is bounded, and the exact angular weight is at
most one. The length and the prefactors in (13) cost only
powers of $N$. Therefore this whole initial part has a strict
gap below $M$.

There is also a less sharp bound that avoids using the
summandwise refinement. Subtract the discarded wire polynomial
from the full kernel. Its real interval norm is at most a
polynomial times $e^{2Ng(\alpha)+O(1)}$, by (9). Applying the
same Bernstein–Walsh estimate separately to these two
polynomials gives (19) with
$E=\max\{\psi(T,0),2g(\alpha)\}$ in place of $\psi(T,0)$.
This still has a strict gap by (10). Under this alternative,
the available collar gap is limited by $M-2g(\alpha)$,
approximately $0.0191$.

This step is needed because separately bounding the rational
wire corrections by $1/s$ at zero would create a spurious
singularity. No such bound is used.

## 6. From the phase certificate to bounds on every contour term

The [uniform factorial estimate](research_uniform_factorial_and_boundary_decay.md)
proves

\[
 |B_N(x,t)|\le \frac CN
                      e^{N\mathfrak b(x,t)}.        \tag{20}
\]

The real exponent uses the branch approached by each denominator
argument. It agrees with $\Re b(x,t)$ on the holomorphic pieces
of the contour. The proof includes zero and the negative real
factorial arguments, with both terms in their exact reflection
formula retained.

At parent $u=0$, the
[central phase certificate](research_terminal_three_central_phase.md)
proves the following bounds. Its endpoints are $\alpha,\beta$
and $\pm T$; the actual half-grid endpoints differ by $O(N^{-1})$.

* On the upper wire rectangle with $0\le\Re t\le T$, the unique
  maximum is the selected saddle, with value $M$. Outside a fixed
  small rectangle about the saddle there is a strict gap.
* The upper wire rectangle with $-T\le\Re t\le0$ has a gap at
  least $1/10$.
* The lower wire rectangle, after subtracting its penalty
  $2\pi h_x$, has a gap at least $1/20$.
* The fixed-depth wire endpoint currents, the two angular cutoff
  connectors, their lower-wire corrections, and every nested
  endpoint surface (18) have gap at least $1/1000$ after the
  indicated lower-wire penalty.

The upper horizontal wire correction has the same phase as the
upper main rectangle and the additional fixed penalty $2\pi h_x$.
On an angular connector its main phase already has a strict gap,
so its extra nonnegative penalty is unnecessary.

These are bounds for compact, explicitly specified surfaces.
The real primitives remain continuous at their moving zeros.
Uniform continuity therefore preserves smaller strict gaps when
the endpoints move by $O(N^{-1})$. Small extensions of the main
rectangle are also harmless: its boundary has a strict gap and
the saddle remains a fixed distance from that boundary.

Now (20) bounds the exact integrands on those surfaces by their
certified exponents, with polynomial prefactors. Equation (16)
supplies exactly the penalties used in the certificate. Equation
(13) supplies the unit-charge angular factor on the connectors.
Hence every term except the upper main rectangle near the saddle
is exponentially smaller. On the main horizontal contour,
(14) shows that replacing the full trace kernel by its first
charge also leaves an exponentially smaller term. This controls
all higher charges together, rather than assuming a separate
asymptotic for each one.

For $u$ in a small complex disk, the parent factorial arguments
in (15) have positive real parts on all these wire surfaces.
The parent phase is holomorphic there, and its perturbation tends
uniformly to zero with $u$. All strict gaps consequently persist
on a fixed smaller disk. The finite truncation estimates and
(19) persist there as well.

## 7. The main integral and its coefficient

Near the selected saddle, every factorial argument is in the
ordinary bulk. The exact interpolation has the uniform expansion

\[
 B_N(x,t)B_N(x,u)
 =\frac{e^{N(b(x,t)+b(x,u))}}
        {4N^2\sin^2(\pi x)}\bigl(1+O(N^{-1})\bigr).
 \tag{21}
\]

Its remainder is holomorphic, with uniform fixed derivatives on
smaller neighborhoods. Insert (21) into the first term of (16),
and then into the first term of (13), using the first charge
from (14). The coefficient of the double integral is exactly

\[
 -\frac{N^2C_{N,3}}{\pi i}\cdot N\cdot\frac1{4N^2}
          =-\frac{NC_{N,3}}{4\pi i}.
\]

Thus the surviving local integral is

\[
 -\frac{NC_{N,3}}{4\pi i}
 \iint
       \frac{\sin t}{\sin^2(\pi x)}
           e^{N\Phi(x,t;u)}\bigl(1+O(N^{-1})\bigr)
       \,dx\,dt.                                      \tag{22}
\]

Both real coordinates increase in this integral. The upper wire
formula has already accounted for its contour orientation.

At zero, the real Hessian is negative definite on a neighborhood
of the critical point. For small complex $u$, the implicit
function theorem gives (5). A local contour translation reaches
that critical point; its connecting boundary stays in the strict
gap region. Holomorphy justifies this translation. The real part
of the translated quadratic form remains negative definite after
shrinking the disk.

The two-dimensional Gaussian factor is

\[
 \frac{2\pi}{N\sqrt{\det(-H(u))}}.
\]

Multiplying it into (22) gives precisely (6). The saddle is
nondegenerate and the sine factors are nonzero, so the amplitude
does not vanish. Every omitted term has either a uniform
$O(N^{-1})$ relative expansion or an exponential gap. This
proves the uniform holomorphic assertion. Cauchy's estimate
gives the stated bounds on derivatives of the normalized error.

Parity occurs only in the exact scalar and the rational trace
kernel. The leading charge of that kernel has coefficient one
for both values of $\eta$. This explains why no parity
subsequence is needed.

## 8. The real boundary estimate

On every wire surface above, the uniform factorial lemma also
proves

\[
 \mathfrak b(x,u)-\mathfrak b(x,0)
 \le-\frac{\sin(2\pi\Re x)}
           {4\pi\cosh^2(\pi\Im x)}(1-\cos u),
 \qquad -\pi\le u\le\pi.                         \tag{23}
\]

The coefficient in (23) has a positive lower bound on all the
retained wire surfaces. Thus every contour term considered in
Section 6 acquires the same type of loss in the real boundary
angle. This includes every intermediate height of an endpoint
current.

The removed wire terms, the removed angular terms, and the
initial connector pieces only need their already proved uniform
real bounds at some rate $E<M$. Choose $c>0$ small enough that
$E<M-2c$, and also smaller than the lower bound in (23).
Since $1-\cos u\le2$, these remaining terms fit the same estimate.
Summing the finite decomposition proves

\[
 |H_{3,N}(u)|\le CN^A
              e^{N\{M-c(1-\cos u)\}},
 \qquad -\pi\le u\le\pi.                         \tag{24}
\]

No moving saddle theorem for each real $u$ has been used. The
same contours and the exact free-boundary inequality suffice.

## 9. Extension to a thin complex strip

Evenness implies $S_3'(0)=0$. At $u=0$ the critical point has
zero first derivative in $u$, and direct differentiation of
the parent integral gives

\[
 S_3''(0)=b_{uu}(x_*,0)
       =-\frac{\tan(\pi x_*)}{2\pi}
       =-\frac{k_*}{2\pi}.
 \tag{25}
\]

Its real part is negative. The holomorphic expansion (6) and
(25) therefore give constants $c_0,B_0>0$ with

\[
 |H_{3,N}(a+ib)|\le C
         e^{N(M-c_0a^2+B_0b^2)}
\]

on a fixed small disk. A mixed $ab$ term is absorbed by
$|ab|\le\epsilon a^2+b^2/(4\epsilon)$.

Away from that disk, (24) has a fixed gap on a slightly larger
real boundary interval. Apply the polynomial Bernstein–Walsh
inequality to $\mathcal H_{3,N}$ on its corresponding interval
in $z=-2\cos u$. The degree is at most $N-1$. The complex
ellipse coordinate costs $O(|b|)$ uniformly there. At the
endpoint $u=\pi$, the displacement in $z$ is $O(b^2)$, so the
square-root endpoint coordinate still costs $O(|b|)$.
A sufficiently thin fixed strip preserves half the strict gap.
Reducing $c$ if necessary combines this bound with the local
quadratic estimate and proves (7).

Since the Newton basis and the closing functional have real
coefficients, conjugating the original crossing replaces it by
its inverse. Conjugating (1) proves the assertion for power
$-3$, with no additional normalization.

## 10. What this result supplies

Formula (6) is an asymptotic for the original polynomial with an
unclosed boundary. Its phase is the stationary value of the
original wire action and the original crossing chirp in (3).
Its scalar and Gaussian coefficient have both been retained.
Estimate (7) is the complementary bound needed when this
terminal polynomial is subsequently glued to another tangle.

The phase comparisons are reproducible with

    python3 experiments/certify_terminal_three_central_phase.py \
      --output repro/results/research-terminal-three-central-phase.json

The [saved certificate](../repro/results/research-terminal-three-central-phase.json)
records the rational rectangles and their rigorous upper bounds.
The exact finite trace identity and its independent numerical
sign checks are recorded in
[the trace note](research_exact_complete_trace_contour.md).
The computation certifies the inequalities used in Section 6;
the source identity and theorem assembly are the written
arguments above.

This theorem does not cover arbitrary adjacent blocks of short
fillings or arbitrary fixed terminal powers. Their finite
polynomials remain defined by (1) with $R^3$ replaced by the
desired power, but the global contour estimates must be proved
for those sources as well.
