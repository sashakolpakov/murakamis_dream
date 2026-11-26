# A common terminal theorem for crossing powers four through thirty-one

Research proof, 2 November 2026. The contour argument for three
crossings extends to every integer power from four through thirty-one.
The wire interval, angular cutoff, exact residue identities, and
families of connecting surfaces are unchanged. A single program
certifies the algebraic saddle and the required inequalities for the
entire finite range.

The program supplies two finite proofs: a Rouché inequality isolating
the selected algebraic root, and a covering by rectangles on which
the phase bounds hold. The remaining source argument is the common
analytic proof given below. Approximate critical points or numerical
maximization are not used as premises.

## 1. The theorem

Use the original Newton basis, crossing $R$, and closing functional
$\phi$ defined in
[the three-crossing theorem](research_three_crossing_terminal_filling.md).
For a fixed signed integer $n$, define

\[
 \mathcal H_{n,N}(z)=\sum_{j=0}^{N-1}\phi(R^ne_j)e_j(z),
 \qquad H_{n,N}(u)=\mathcal H_{n,N}(-2\cos u),
 \qquad C_{N,n}=q^{nd^2/4}.
 \tag{1}
\]

The integer $n$ in this formula is the original crossing power.
All first normal derivatives in the finite algebra are retained.
For $n>0$, put

\[
 \Phi_n(x,t;u)
    =b(x,t)+b(x,u)+\frac{int^2}{4\pi}-it,
 \tag{2}
\]

with the continued factorial branches used in
[the central-phase proof](research_terminal_three_central_phase.md#1-the-phase-and-its-branches).
The function $b$ is the primitive of the logarithm of the original
cosine product, with its two sine-factorial contributions subtracted.

Let $(x_n(u),t_n(u))$ be the selected holomorphic critical point
of (2), and write

\[
 S_n(u)=\Phi_n(x_n(u),t_n(u);u),\qquad
 Q_n(u)=D^2_{x,t}\Phi_n(x_n(u),t_n(u);u).
 \tag{3}
\]

Section 2 specifies this critical point without a numerical branch
choice. Its Gaussian square root is fixed by the horizontal tangent
plane, on which $\Re(-Q_n(0))$ is positive definite.

**Theorem.** For every integer $4\le n\le31$,

\[
 \boxed{\quad
 H_{n,N}(u)
  =C_{N,n}
    \frac{i\sin t_n(u)}
      {2\sin^2(\pi x_n(u))\sqrt{\det(-Q_n(u))}}
       e^{NS_n(u)}\bigl(1+O(N^{-1})\bigr).
 \quad}                                                   \tag{4}
\]

The expansion is uniform on a fixed complex disk about $u=0$,
the displayed amplitude is nonzero, and every fixed derivative
of the normalized error has order $N^{-1}$ on a smaller disk.
It holds for both parities of $N$. The scalar $C_{N,n}$ is kept
exactly.

With $M_n=\Re S_n(0)$, there are positive constants
$c,C,B,\rho$ and an exponent $A$ such that

\[
 |H_{n,N}(a+ib)|
 \le CN^A
       e^{N\{M_n-c(1-\cos a)+Bb^2\}},
 \qquad |a|\le\pi,\quad |b|\le\rho.                 \tag{5}
\]

Because the power range is finite, the disk and constants can
be chosen simultaneously for all $4\le n\le31$.
The negative powers satisfy the conjugate statements, since
$H_{-n,N}(u)=\overline{H_{n,N}(\bar u)}$.

## 2. An algebraic root with its logarithm fixed

Let $U_j$ denote the Chebyshev polynomial of the second kind,
defined by

\[
 U_0(X)=1,\quad U_1(X)=2X,\quad
 U_{j+1}(X)=2XU_j(X)-U_{j-1}(X).
\]

For each positive $n$ in the theorem, define

\[
 P_n(X)=XU_{n-1}(X)-i.
 \tag{6}
\]

The certificate isolates a zero $k_n$ of (6). It also proves that
the principal inverse cosine has the form

\[
 z_n=\arccos k_n=a_n-ib_n,\qquad
 0<a_n<\frac{\pi}{n},\quad b_n>0.
 \tag{7}
\]

Set

\[
 t_n(0)=2z_n,\qquad x_n(0)=\frac{\arctan k_n}{\pi}.
 \tag{8}
\]

The polynomial equation alone is not yet the original logarithmic
stationary equation. Here is the branch verification.
Since $\sin z_n\ne0$, the identity
$U_{n-1}(\cos z)=\sin(nz)/\sin z$ gives

\[
 \sin(nz_n)=i\tan z_n.
 \tag{9}
\]

Taking imaginary parts in (9) yields

\[
 -\cos(na_n)\sinh(nb_n)
     =\frac{\sin(2a_n)}
            {\cos(2a_n)+\cosh(2b_n)}>0.
\]

Together with (7), this implies $\pi/2<na_n<\pi$.
Equation (9) also gives $\cos^2(nz_n)=\sec^2z_n$.
The real part of $\cos(nz_n)$ is negative, whereas that of
$\sec z_n$ is positive. Therefore

\[
 \cos(nz_n)=-\sec z_n,\qquad
 -e^{inz_n}=\sec z_n+\tan z_n.
\]

The number on the right equals
$\tan(\pi/4+z_n/2)$ and lies in the fourth quadrant.
Its argument is $na_n-\pi\in(-\pi/2,0)$. Consequently its
specified logarithm satisfies the exact identity

\[
 \log(\sec z_n+\tan z_n)=inz_n-i\pi.                \tag{10}
\]

This is the original unit-charge leaf equation, without an
undetermined multiple of $2\pi i$. The
[principal-saddle theorem](research_terminal_powers_three_and_above.md)
proves uniqueness on this branch and proves that the corresponding
wire point (8) is in the original factorial bulk.
The same result proves the invertibility of the joint Hessian.
Thus (8) is the critical point required in (3).

## 3. How the zero of the polynomial is certified

The root finder only proposes a center $c_n$ for a disk. The center
is then replaced by an exact complex dyadic rational, and the radius
is fixed as $r=2^{-100}$. Expand the exact polynomial as

\[
 P_n(c_n+w)=\sum_{j=0}^n a_jw^j.
\]

Interval arithmetic verifies

\[
 |a_0|+\sum_{j=2}^n|a_j|r^j<|a_1|r.               \tag{11}
\]

On $|w|=r$, the linear term $a_1w$ therefore dominates the sum
of all other terms. Rouché's theorem proves that the disk contains
exactly one zero, counted with multiplicity. This also proves
that the zero is simple. No accuracy claim from the initial root
proposal is needed after (11).

The disk is enclosed in a complex rectangle, and interval
evaluation of its inverse cosine verifies (7). The subsequent
inverse tangent and all action values are evaluated on this
enclosure, not just at its midpoint. The certificate also checks

\[
 \alpha<\Re x_n(0)<\beta,\qquad
 \frac{h_{t,n}}{2\pi}>h_{x,n}>0,
 \quad
 h_{x,n}=\Im x_n(0),\quad h_{t,n}=-\Im t_n(0),
 \tag{12}
\]

where $\alpha=3/32$ and $\beta=13/32$.
The last inequality fixes the upper and lower branch sides of
the denominator factorials on every nested surface.

The real coefficients of $XU_{n-1}(X)$ are generated by exact
integer polynomial arithmetic. The only nonreal coefficient of
$P_n$ is its constant term $-i$.

## 4. One set of contour domains for the entire range

Use the same angular cutoff $T=2\pi/3$ as for three crossings.
For each $n$, the main rectangle is

\[
 x=\xi+ih_{x,n},\quad t=\tau-ih_{t,n},\qquad
 \alpha\le\xi\le\beta,\quad 0\le\tau\le T.
\]

The certificate selects a rational rectangle $Q_n$ around
$(\Re x_n(0),\Re t_n(0)/(2\pi))$ and verifies that it contains
that point in its interior. A $16$ by $16$ subdivision of $Q_n$
proves negative definiteness of the real Hessian throughout it.
The chosen rectangle is recorded explicitly for each power.

The remaining bounds are as follows.

| Part of the contour | Proved gap below $M_n$ |
|---|---:|
| Upper main rectangle outside $Q_n$ | $10^{-7}$ |
| Negative angular rectangle at the same upper wire height | $1/(100n^2)$ |
| Full lower wire rectangle after subtracting $2\pi h_{x,n}$ | $1/(100n^3)$ |
| Every angular connector and endpoint surface, with its prescribed lower-wire penalty | $1/1000$ |

The connector family is exactly the family in
[Section 4 of the three-crossing phase proof](research_terminal_three_central_phase.md#4-connecting-surfaces).
It includes both angular cutoffs, both wire endpoints, both wire
signs, the independent wire-height parameter on the bottom contour,
and every nested surface

\[
 x=e\pm ih_{x,n}vs,\qquad
 t=\pm T-ih_{t,n}s,\qquad 0\le v,s\le1,
 \quad e\in\{\alpha,\beta\}.
\]

On a lower nested surface the penalty is $2\pi h_{x,n}vs$.
All mixed derivatives of this parameterization and its penalty
are retained in the Taylor bound. The program checks 23 surface
cases for each power.

Together with the exact stationarity proved in Section 2, the
negative Hessian on $Q_n$ and the strict bound outside it prove
that the main rectangle has a unique maximum, equal to $M_n$.
The calculation does not claim negative definiteness on the
whole main rectangle.

The same run also verifies

\[
 M_n-2g(\alpha)>\frac{19}{1000}.
 \tag{13}
\]

All powers use the original sine-factorial rate
$g(x)=J(2x)-4J(x)$. The real outer-angle estimate remains
$\psi(T,0)<4/5$, whereas $M_n>2g(\alpha)+19/1000>4/5$.
Thus both finite truncations have a strict gap.

## 5. From the certificate to the finite polynomial

Here the proof is common to all powers in the range. It is the
argument in
[the full three-crossing theorem](research_three_crossing_terminal_filling.md),
with the integer $3$ in the original chirp replaced by $n$.
The following points explain why no new interface assumption is
being made.

The original finite Hermite trace has polynomial cost at each
fixed power. Therefore (13) removes the original wire indices
outside $[\alpha,\beta]$ before any contour deformation.
The real outer-angle bound removes the angular grid nodes
outside a half-grid cutoff $T_N\ge T$, including their first
normal derivatives.

The exact rational trace identity is valid for every integer
power. Its leading positive charge has coefficient one for
both parities of $N$. The full rational denominator controls
all higher charges on the fixed lower angular contour.
The one-sided wire identity is independent of $n$.
It produces exactly the main rectangle, lower penalties, and
nested endpoint surfaces certified in Section 4.

The first portion $0\le s\le N^{-1}$ of an angular connector
is kept as the original finite wire polynomial. The real
interval bound and Bernstein–Walsh inequality give a
subexponential continuation cost there. If the conservative
full-kernel-minus-wire-tail estimate is used, its real rate is
$\max\{\psi(T,0),2g(\alpha)\}<M_n$.

Away from that small portion, the exact factorial bound across
moving zeros compares the finite integrand with the certified
real phase. Its reciprocal reflection retains both exponential
terms. The phase gaps therefore control every contour
correction. Half-grid movements of size $O(N^{-1})$ preserve
smaller gaps by uniform continuity, including at the cuts.

Only the neighborhood of the selected joint saddle survives.
The exact bulk prefactor of the two Newton factors is
$1/(4N^2\sin^2(\pi x))$. The trace and wire densities together
give $-NC_{N,n}/(4\pi i)$ before the two-dimensional Gaussian
integration. The Gaussian supplies
$2\pi/(N\sqrt{\det(-Q_n)})$. Their product is the coefficient
in (4).

Holomorphic perturbation of the free boundary preserves all
strict gaps and the local nondegeneracy. The exact parent
factorial estimate supplies a uniform loss proportional to
$1-\cos u$ on a real period. Finally the local quadratic
action and Bernstein–Walsh continuation away from the complete
point give (5). These arguments prove the full source
expansion and its boundary bound, rather than merely the
location of a stationary point.

## 6. Reproduction

Run the single program

    python3 experiments/certify_terminal_powers_four_through_thirty_one.py \
      --output repro/results/research-terminal-powers-four-through-thirty-one.json

The [program](../experiments/certify_terminal_powers_four_through_thirty_one.py)
uses exact integer coefficients, exact rational cutoffs, and
180-bit Arb/Acb arithmetic. The
[saved certificate](../repro/results/research-terminal-powers-four-through-thirty-one.json)
contains the exact dyadic root centers, the Rouché bounds,
the root enclosures, the local Hessian rectangles, and every
accepted rectangle in the surface covering.

The shared interval engine is the
[three-crossing certificate](../experiments/certify_terminal_three_central_phase.py).
It uses direct primitive bounds or Taylor bounds with interval
Hessians. A special convergent-series bound handles the continuous
primitive at a moving zero. A rectangle is never accepted on
the basis of a numerical sample.

This theorem covers the indicated terminal powers with an
unclosed boundary. It does not assert an asymptotic for an
arbitrary connected group of adjacent short fillings. Such a
group has a different global source and requires its own
assembly argument.
