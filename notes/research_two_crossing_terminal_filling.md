# A two-crossing terminal filling with a free boundary

Research proof, 2 November 2026. This note concerns the complete meridian
parameter and the original finite crossing algebra used in the circle-tree
papers. It establishes an open-boundary estimate for a terminal vertex
whose signed crossing power is $2$ or $-2$. The frozen manuscripts
are unchanged. Arbitrary fixed short powers and adjacent short-filled
vertices require additional arguments.

## 1. The finite algebra and the statement

Fix an integer $N\ge3$, and put

\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad
 \kappa=q^{d^2/2},\qquad
 S_k=\prod_{j=1}^k2\sin(\pi j/N),\qquad S_0=1.
\]

All powers of $q$ use the indicated exponential, including fractional
powers. Write $T_N$ for the monic Chebyshev polynomial characterized
by $T_N(t+t^{-1})=t^N+t^{-N}$. The pair algebra is

\[
 \mathcal A_N=\mathbb C[z]/(T_N(z)+2).
\]

Its Newton basis and closing functional are

\[
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}(c_j-z),\qquad
 c_j=2\cos((2j+1)\pi/N),\qquad 0\le k\le d,
\]

\[
 \phi(f)=(-1)^dN^2[z^d]\operatorname{rem}_{T_N+2}f,
 \qquad \phi(e_i e_j)=\mathbf1_{i+j=d}.
\]

The finite crossing formulas, including their first derivatives at
double roots, are proved in the [Newton calculus](../papers/newton-calculus/finite.tex)
and [finite-source paper](../papers/circle-tree-volume/finite-bounds.tex).
In these conventions the positive physical crossing is

\[
 R=\kappa\sum_{k=0}^d(-q)^k e_k.
\]

At the complete meridian, the physical quarter-turn reverses the
coefficients in this basis. If a terminal vertex has crossing power
$n$, summing its only incident edge gives the exact polynomial

\[
 \mathcal H_{n,N}(z)
       =\sum_{k=0}^d\phi(R^n e_k)e_k(z).
\]

This equality is made before any other boundary is closed. Put
$H_{n,N}(u)=\mathcal H_{n,N}(-2\cos u)$, so that $u$ is the
remaining boundary angle.

Let $G=\sum_{j\ge0}(-1)^j/(2j+1)^2$ be Catalan's constant, and
let $v_{\rm oct}=4G$ be the volume of a regular ideal octahedron.
Define the even holomorphic function $V$, initially near zero, by

\[
 V(0)=M:=\frac{2G}{\pi},\qquad
 V'(u)=-\frac1{2\pi}\operatorname{artanh}(\sin(u/2)).
\]

Thus $V(u)=\psi(u,0)/2$ in the notation of the circle-tree papers.

**Theorem.** The two-crossing terminal message has the exact formula

\[
 \mathcal H_{2,N}(z)=N\sum_{k=0}^{N-1}
            \frac{i^kq^{k(k-1)/2}}{S_k}e_k(z).                 \tag{1}
\]

There is a disk $|u|\le\rho$ on which, uniformly as $N\to\infty$
through all integer levels,

\[
 H_{2,N}(u)=\frac{e^{-i\pi/4}}{2\sqrt{\cos(u/2)}}
       \exp\!\left[N\left(V(u)+\frac{i\pi}{8}
                              -\frac{iu^2}{8\pi}\right)\right]
       \bigl(1+O(N^{-1})\bigr).                             \tag{2}
\]

The square root is one at $u=0$. The normalized error is holomorphic;
each of its fixed derivatives is $O(N^{-1})$ on smaller disks.
There are positive constants $c_*,C_*,b_*,C,A$, independent of $N$,
such that

\[
 |H_{2,N}(a+ib)|\le CN^A
       \exp\!\left[N\{M-c_*(1-\cos a)+C_*b^2\}\right],
 \qquad |a|\le\pi,\quad |b|\le b_*.                       \tag{3}
\]

The negative-power message is obtained by conjugating the coefficients
of (1). Its holomorphic asymptotic is obtained from (2) by replacing
$i$ by $-i$, and it satisfies the same bound (3).

The phase in (2) differs from the actual marked primitive leaf-filling
action by exactly $i\pi/2$. Thus the extra exponential is the unit
phase $i^N$, rather than an unidentified change of volume.

## 2. The exact two-crossing identity

Multiplication by $R$ in the Newton basis has entries

\[
 R_{ij}=\kappa(-1)^i q^{i(j+1)}
            \frac{S_i}{S_jS_{i-j}},\qquad i\ge j.
\]

Consequently, with $Q=q^2$,

\[
 [e_i]R^2=\kappa^2(-1)^i q^i
       \sum_{j=0}^i(-1)^j q^{j(i+1)}\frac{S_i}{S_jS_{i-j}}.
\]

The relation
$S_i/(S_jS_{i-j})=q^{-j(i-j)}{i\brack j}_Q$ turns this sum into

\[
 \sum_{j=0}^i(-1)^jQ^{j(j+1)/2}{i\brack j}_Q
        =\prod_{j=1}^i(1-Q^j)=(Q;Q)_i.
\]

This is the finite binomial expansion of the displayed product; it
also follows by induction in $i$. No denominator vanishes, since
every factorial index is smaller than $N$. Hence

\[
 [e_i]R^2=\kappa^2 i^i q^{i(i+3)/2}S_i.
\]

The closing relation reverses the coefficient index. Set $i=d-k$
and use

\[
 S_{d-k}S_k=N,\qquad
 \kappa^2i^d q^{d(d+3)/2}=1.
\]

This gives (1), with every scalar retained. Since the basis is real
and $R^{-1}$ has conjugate coefficients, it also gives the stated
negative-power formula. These are identities in the actual
nonsemisimple algebra, not identities only at its distinct roots.

## 3. Interpolation and the selected critical point

On $0<x<1$, put

\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt.
\]

In complex formulas use its analytic continuation from this interval.
For $0<\Re x<1/2$ and small $u$, define

\[
 b(x,u)=\int_0^x\log(2\cos(2\pi t)+2\cos u)\,dt-2J(x),
 \qquad
 F(x,u)=b(x,u)-J(x)+\frac{i\pi}{2}(x^2+x).              \tag{4}
\]

The branches start on $0<x<1/2,u=0$. In particular
$b(x,0)=J(2x)-4J(x)$.

The canonical factorial $G_N$ from the
[factorial interpolation proof](../papers/circle-tree-volume/edge-packet.tex)
is holomorphic and zero-free in the bulk strip, agrees with $S_k$
at integers, and has its uniform Stirling expansion there. Its exact
interpolation of $e_k(-2\cos u)$ is

\[
 B_N(x,u)=\frac{G_N(d/2+Nu/(2\pi))G_N(d/2-Nu/(2\pi))}
 {G_N(d/2-Nx+Nu/(2\pi))G_N(d/2-Nx-Nu/(2\pi))G_N(Nx)^2}.
\]

On every fixed rectangle $0<\alpha\le\Re x\le\beta<1/2$, with
bounded imaginary part, uniformly for sufficiently small $u$, the
exact summand interpolation is

\[
 \begin{aligned}
 f_N(x,u)&=\frac{N e^{i\pi Nx/2}e^{i\pi(Nx^2-x)/2}B_N(x,u)}{G_N(Nx)}\\
 &=N^{-1/2}\frac{e^{-i\pi x/2}}{(2\sin\pi x)^{3/2}}
                  e^{NF(x,u)}(1+O(N^{-1})).                 \tag{5}
 \end{aligned}
\]

All factorial arguments stay in compact bulk strips. In particular,
the midpoint shifts in $d/2$ cancel the numerator and denominator
square-root factors, leaving exactly the amplitude in (5).

Put $z=e^{2\pi ix}$. Exponentiating the critical equation gives

\[
 e^{F_x(x,u)}=\frac{z(z^2+2\cos u\,z+1)}{(z-1)^3}.
\]

The selected root, with the unexponentiated logarithms continued from
the saddle at $u=0$, is

\[
 z_*(u)=\frac1{1-2i\cos(u/2)},\qquad
 x_*(u)=\frac{\log z_*(u)}{2\pi i}.                       \tag{6}
\]

At zero,

\[
 x_*:=x_*(0)=\frac{\log((1+2i)/5)}{2\pi i},\qquad
 F_{xx}(x_*,0)=\pi(-4+3i).                               \tag{7}
\]

There is no hidden multiple of $2\pi i$ in $F_x$: direct
substitution in the logs gives zero. Equivalently, the imaginary part
of the substituted expression lies strictly between $-2\pi$ and
$2\pi$, and exponentiation gives one. The root is nondegenerate
and extends holomorphically in $u$.

### The critical action and its constant

For real $0\le u<\pi$, let $c=\cos(u/2)$ and $s=\sin(u/2)$.
At the selected root, $\tan(\pi x_*)=c/(1-ic)$. Therefore

\[
 \frac d{du}F(x_*(u),u)
 =-\frac1\pi\operatorname{artanh}\frac{s}{1-ic}
 =-\frac1{2\pi}\operatorname{artanh}s-\frac{iu}{4\pi}.   \tag{8}
\]

For the last equality, exponentiate twice the artanh and use
$(1+s-ic)/(1-s-ic)=((1+s)/c)e^{iu/2}$. Its argument is continued
from zero, so there is no additional logarithmic period.

The constant in (8) is fixed at $u\to\pi^-$. Put $\delta=\pi-u$.
Then $x_*=a+ih=O(\delta)$, $h\sim\delta^2/(4\pi)$, and
$\delta/2-\pi a=O(\delta^3)>0$. Along $t=\lambda x_*$,
$0\le\lambda\le1$, the numerator of the logarithm in $b$ factors
as $4\sin(\delta/2+\pi t)\sin(\delta/2-\pi t)$. Its modulus is
between fixed positive multiples of $\delta^3$ and $\delta^2$
for all sufficiently small $\delta$. The continued logarithm is
therefore $O(|\log\delta|)$; its integral and $J(x_*)$ tend to
zero. Thus $F(x_*(u),u)\to0$.

Also $V(\pi)=0$: the integral of
$\operatorname{artanh}(\sin(u/2))$ over $[0,\pi]$ is (4G).
Integrating (8) now gives the exact identity

\[
 F(x_*(u),u)=V(u)+\frac{i\pi}{8}-\frac{iu^2}{8\pi}.     \tag{9}
\]

In particular its central real part is $M=2G/\pi>0$.

## 4. The finite contour estimate

The classical Abel--Plana formula is reviewed in
[DLMF, Section 2.10(i)](https://dlmf.nist.gov/2.10#i). We derive the
finite half-grid estimate needed here, including its vertical weights.

We give the complete argument at $u=0$, followed by its real-parameter
extension. Write $L(x)=J(2x)-5J(x)$ on $[0,1/2]$. It is continuous
and vanishes at both endpoints. Choose $\alpha>0$ small and
$eta<1/2$ close to (1/2), so that

\[
 \alpha<\Re x_*<\beta,
 \qquad L<M/4\quad\hbox{on }[0,\alpha]\cup[\beta,1/2].
\]

The uniform sine-product estimate proved in Section 6 bounds the
discarded low-index terms by a polynomial times
$e^{N(L(k/N)+|\Im u|)}$. The higher indices also have a gap:
the complete Newton norm of $e_k$ is polynomial for $k>d/2$,
including its first derivatives at double roots, and
$S_k^{-1}=S_{d-k}/N$ is polynomially bounded there. The
[finite-source norm argument](../papers/circle-tree-volume/finite-bounds.tex)
makes these bounds polynomial interval bounds. For complex $u$,
the degree bound costs at most $e^{N|\Im u|}$. Thus all discarded
indices are exponentially smaller than $e^{NM}$ for small $u$.

Move (alpha,eta) by $O(N^{-1})$ to half-grid points
$\alpha_N,eta_N$, and set $h=\Im x_*>0$. For a holomorphic
function $f$ on the rectangle between these sides and heights
$-h,h$, the residue formula gives

\[
 \sum_{\alpha_N<k/N<\beta_N}f(k/N)
       =N\int_{\alpha_N}^{\beta_N}f(x)\,dx+R_N,
\]

\[
 \begin{aligned}
 |R_N|\le {}&N\sum_{\xi=\alpha_N,\beta_N}
       \int_{-h}^h\frac{|f(\xi+iy)|}{1+e^{2\pi N|y|}}\,dy\\
 &+\frac{N}{e^{2\pi Nh}-1}
       \int_{\alpha_N}^{\beta_N}
            (|f(x+ih)|+|f(x-ih)|)\,dx.                    \tag{10}
 \end{aligned}
\]

To derive (10), integrate $\pi N\cot(\pi Nx)f(x)$, subtracting
the constant $-i$ from the upper cotangent and $i$ from the lower.
The constants give the real integral. On a vertical half-grid side,
$\cot(\pi N(x+iy))=-i\tanh(\pi Ny)$, so the remaining factor has
modulus $2/(1+e^{2\pi N|y|})$. On either horizontal side it is
at most $2/(e^{2\pi Nh}-1)$. This proves the estimate with its
essential exponentially weighted vertical terms.

At $u=0$,

\[
 F_{xx}(x,0)=-\pi(3\cot\pi x+2\tan\pi x)+i\pi.
\]

Its real part is negative throughout $0<\Re x<1/2$. Hence
$\Re F(x+ih,0)$ is strictly concave in real $x$, with its unique
maximum $M$ at $x=\Re x_*$. In addition,

\[
 \Re F(x-iy,0)=\Re F(x+iy,0)+\pi y(2x+1).              \tag{11}
\]

After the weight in (10), the lower horizontal exponent is at most
$M-\pi h(1-2\beta)+O(N^{-1})$; the upper one is at most
$M-2\pi h$. On a vertical side the real part is convex in $y$,
because its second $y$-derivative is $-\Re F_{xx}>0$.
Subtracting the linear weight separately on the upper and lower
halves preserves convexity. Its value at height zero is below
$M/4$, and its values at the other endpoints have the preceding
strict gaps. The whole correction $R_N$ is therefore exponentially
smaller than $e^{NM}$.

Shift the main real integral to height $h$. The unweighted vertical
connectors also have convex exponents; both their endpoints lie
strictly below $M$. The remaining horizontal integral has one
nondegenerate saddle and a strictly concave real part. Substituting
$x-x_*=N^{-1/2}w$, Taylor expanding, and bounding the remainder by
the Gaussian proves

\[
 H_{2,N}(u)=A(u)e^{NF(x_*(u),u)}(1+O(N^{-1})),
\]

\[
 A(u)=\frac{e^{-i\pi x_*(u)/2}}{(2\sin\pi x_*(u))^{3/2}}
          \sqrt{\frac{2\pi}{-F_{xx}(x_*(u),u)}}.          \tag{12}
\]

All discarded terms have a fixed exponential gap. These strict gaps
persist on compact contours for sufficiently small complex $u$;
the contour moves slightly through the continued saddle. This proves
uniformity and a holomorphic normalized error. Cauchy's estimates
give the derivative statement on smaller disks.

For completeness, at $c=\cos(u/2)$ the critical quadratic gives
$F_{xx}=-8\pi c z_*/(z_*-1)^3$. Squaring (12) gives
$A(u)^2=-i/(4c)$. The Gaussian branch with positive real part at
$u=0$, together with the continued sine power, gives
$A(0)=e^{-i\pi/4}/2$. This proves the precise amplitude in (2).

## 5. A real-parent interval extending beyond the local chart

Let $0\le u<\pi$, $r=(\pi-u)/(2\pi)$, and work first in
$0<\Re x<r$, before the first real zero of the numerator product.
The real exponent is

\[
 L_u(x)=J(r+x)-J(r-x)-3J(x).
\]

On this strip,

\[
 F_{xx}=-\pi\{\tan(\pi x+u/2)+\tan(\pi x-u/2)
                    +3\cot(\pi x)\}+i\pi,
\]

and its real part is negative for every imaginary height. Here is a
direct check. Set $C=\cosh(2\pi\Im x)$, $v=\cos u$, and
$c=\cos(2\pi\Re x)$. After extracting positive denominators and
$\sin(2\pi\Re x)$, the needed numerator is

\[
 Q(C)=(3+2v)C^2+2c(1+2v)C+c^2+3v^2-3.
\]

Since $c+v>0$,
$Q(1)=(c+v)(c+3v+2)>0$. For $v\ge-1/2$, $Q'(C)\ge4$;
for $v<-1/2$, $Q'(C)\ge8(1+v)>0$. Thus $Q(C)>0$ for $C\ge1$.
The reflection formula (11) remains valid.

The endpoint rate $J(2r)-3J(r)$ is strictly below $V(u)$.
Their difference tends to zero as $r\to0$, and its derivative
with respect to $r$ is

\[
 \log\frac{1+\cos(\pi r)}{2\cos^2(\pi r)}>0.
\]

Endpoints sufficiently close to zero and to $r$ consequently have
strict gaps. The same finite contour proof applies.

For indices after the first zero but still below $N/2$, the
absolute-product rate is

\[
 L_{\rm abs}(x,u)=J(r+x)+J(x-r)-3J(x),\qquad r\le x\le1/2.
\]

Its derivative is

\[
 \log\frac{\sin^2(\pi x)-\sin^2(\pi r)}{2\sin^3(\pi x)}.
\]

The fraction is at most $1/(3\sqrt3\sin(\pi r))$: maximize
$(y^2-a^2)/(2y^3)$ over $y\ge a$, with $a=\sin(\pi r)$.
Since $\sin(\pi/16)>1/(3\sqrt3)$, this rate is nonincreasing
when $r\ge1/16$. Every such term is therefore bounded by the
strictly smaller endpoint rate. Higher indices remain polynomial
by the complete norm argument above. Compactness of
$0\le u\le7\pi/8$ now makes the contour and tail bounds uniform
on this real interval.

By (9), its dominant real part is $V(u)$. Since
$\operatorname{artanh}(\sin(u/2))\ge\sin u/2$, integration gives

\[
 V(u)\le M-\frac{1-\cos u}{4\pi},\qquad 0\le u<\pi.  \tag{13}
\]

## 6. Uniform control near the opposite endpoint

For this real-variable argument extend
$f(t)=\log|2\sin\pi t|$ periodically, and let
$J(t)=\int_0^t f(s)\,ds$. This real $J$ is odd and periodic.

The needed uniform product estimate is

\[
 \sum_{j=0}^{k-1}f\left(r+\frac{j+1/2}{N}\right)
 \le N\{J(r+k/N)-J(r)\}+C\log N,
\]

for every real shift $r$, every $0\le k<N$, and one absolute
constant $C$. Also $\log S_k=NJ(k/N)+O(\log N)$ uniformly.
To prove this, partition the integral into mesh cells. Only a bounded
number of cells are within $2/N$ of an integer. On these cells,
$f(t)=\log\operatorname{dist}(t,\mathbb Z)+O(1)$: its integral
average is at least $-\log N-C$, whereas a sampled value is at
most $-\log N+C$. A sampled zero gives an automatic upper bound.
On the other cells, sum the variation bound from
$f'(t)=\pi\cot\pi t$; it is $O(\log N)$. For the factorial
use right endpoints and estimate its first cell directly. No sampled
factorial endpoint is a sine zero because $k<N$.

For $7\pi/8\le u\le\pi$, put $r=(\pi-u)/(2\pi)\le1/16$.
Factoring the cosine numerator into the two shifted sine products
shows that every summand of (1) is bounded by a polynomial in $N$
times $e^{NL_r(x)}$, where

\[
 L_r(x)=J(x+r)+J(x-r)-3J(x),\qquad x=k/N.
\]

This includes every index and every possible numerator zero. For
$0<r\le1/16$,

\[
 |J(x+r)-J(x)|\le r\{1-\log(2r)\}.                    \tag{14}
\]

Indeed $f\le\log2$, while
$(-f(t))_+\le(-\log(4\operatorname{dist}(t,\mathbb Z)))_+$,
using $\sin(\pi t)\ge2t$ on $[0,1/2]$. The integral of this
last function over an interval of length $r$ is largest for an
interval centered at an integer; it equals $r(1-\log(2r))$.
This also exceeds $r\log2$, proving (14).

The minimum of $J$ occurs at $1/6$ modulo integers. Concavity
of sine gives $\sin(\pi t)\ge3t$ on $[0,1/6]$, and hence
$-\min J\le1/6$. Therefore

\[
 L_r(x)\le\frac16+2r\{1-\log(2r)\}
 \le\frac16+\frac{1+\log8}{8}<\frac{133}{240}.          \tag{15}
\]

On the other hand $G>8/9$ and $\pi<22/7$ give
$M>56/99>133/240$. Thus the whole opposite-endpoint region has
a fixed exponential gap from the central rate. Summing its $N$
terms changes only the polynomial factor. Evenness handles negative
$u$, and conjugation handles the negative crossing power.

Combining (13) and (15) proves, for some $c>0$,

\[
 |H_{2,N}(a)|\le CN^A e^{N\{M-c(1-\cos a)\}},
                         \qquad -\pi\le a\le\pi.        \tag{16}
\]

## 7. A thin complex boundary strip

Near zero, (2) and (9) give

\[
 F(x_*(u),u)=F(x_*,0)-\frac{1+i}{8\pi}u^2+O(u^4).
\]

For $u=a+ib$ in a sufficiently small disk, Taylor's theorem and
Young's inequality therefore give a bound $M-c_0a^2+C_0b^2$.

Away from zero, take a small fixed $\delta>0$. On the larger real
spectral interval $I=[-2\cos(\delta/2),2]$, (16) supplies a fixed
gap $g>0$. A polynomial $p$ of degree at most (N-1) satisfies

\[
 |p(z)|\le\|p\|_I e^{(N-1)g_I(z)},
\]

where $g_I(z)=\log|\zeta+\sqrt{\zeta^2-1}|$,
$\zeta=(2z-a_I-b_I)/(b_I-a_I)$, with the branch of modulus at
least one. This follows by applying the maximum principle to the
polynomial divided by that branch to its degree. The explicit
formula gives $g_I(z)\le C_\delta\sqrt{\operatorname{dist}(z,I)}$
uniformly near $I$. If $|a|\ge\delta$, the point
$z=-2\cos(a+ib)$ is within $C|b|$ of $I$. Choose $b_*>0$
so small that this cost is at most $g/2$. The exterior strip then
has exponent at most $M-g/2$.

Choose $c_*\le g/4$ and $c_*\le2c_0$. Since $1-\cos a\le2$
and $a^2\ge2(1-\cos a)$, the local and exterior estimates combine
to give (3). Cauchy's estimate on small nested strips supplies fixed
derivative bounds when needed.

## 8. The original marked geometric action

The circle-tree geometry paper defines

\[
 \psi_t(t,u)=-\pi^{-1}\operatorname{arsinh}
                 (\tan(t/2)\cos(u/2)),\qquad
 \psi(0,0)=4G/\pi.
\]

For a leaf with physical power $2$, the primitive unit-charge
equation is the stationarity equation of

\[
 S(t,u)=\psi(t,u)+\frac{i}{2\pi}t^2-it.
\]

For real $0\le u<\pi$, put $c=\cos(u/2)>0$ and choose

\[
 \cos(t(u)/2)=\frac{1+i}{2}\sqrt c,
 \qquad 0<\Re t(u)<\pi,\quad\Im t(u)<0.                \tag{17}
\]

This is the branch through the complete-parent filled-leaf solution.
Squaring (17) gives $\cos^2(t/2)=ic/2$, and substitution shows

\[
 \operatorname{arsinh}(c\tan(t/2))=it-i\pi.
\]

The branch is determined without exponentiation ambiguity: its
argument has positive real part and negative imaginary part, and
the logarithm continues from the positive primitive cone path.
Thus $t(u)$ satisfies the original primitive filling equation.

Let $S_{\rm geom,2}(u)=S(t(u),u)$. Stationarity eliminates $t'(u)$,
and, with $s=\sin(u/2)$,

\[
 \begin{aligned}
 S_{\rm geom,2}'(u)
 &=-\pi^{-1}\operatorname{arsinh}\frac{(1+i)s}{2\sqrt c}\\
 &=-\frac1{2\pi}\operatorname{artanh}s-\frac{iu}{4\pi}.
 \end{aligned}
\]

For the second equality take the hyperbolic sine of
$\tfrac12\operatorname{artanh}s+iu/4$; its real and imaginary
parts are both $s/(2\sqrt c)$. Its imaginary part lies in
$[0,\pi/4)$, fixing the inverse-hyperbolic branch.

It remains to fix the additive constant. As $u\to\pi^-$,
$c\to0$ and $t(u)\to\pi$. On the straight segment from zero
to $t(u)$,

\[
 |c\tan(v/2)|=O(\sqrt c).
\]

Indeed the endpoint's distance from the tangent pole is comparable
to $\sqrt c$, and the whole segment stays in the right lower
strip. The derivative formula gives

\[
 \psi(t(u),u)=\psi(0,u)-\frac1\pi
       \int_0^{t(u)}\operatorname{arsinh}(c\tan(v/2))\,dv
       \longrightarrow0.
\]

Here $\psi(0,u)\to0$, and the integral is $O(\sqrt c)$.
Consequently $S_{\rm geom,2}(u)\to-i\pi/2$, whereas the source
action in (9) tends to zero. Their derivatives agree, so

\[
 \boxed{\quad F(x_*(u),u)=S_{\rm geom,2}(u)+i\pi/2.\quad}        \tag{18}
\]

This is an identity of holomorphic germs at the parent origin. For
power $-2$, conjugating the real-parent identities gives the
constant $-i\pi/2$.

The geometric branch is an actual positive partial filling. At parent
angle zero write $t=2a-2ib$. Along the cone parameter $0\le\lambda\le1$,
the equations are

\[
 \sin a=\cosh b\tanh(2b),\qquad
 2a+\arctan\frac{\sinh b}{\cos a}=\pi\lambda.
\]

The first equation determines an increasing function $b(a)$; the
second has a strictly increasing left side, running from zero to
$3\pi/2$ as $a\to\pi/2$. Hence its solution for
$0<\lambda\le1$ has $0<a<\pi/2$, $b>0$.
Set $w=e^{it/2}$ and $R_0=\sec(t/2)+\tan(t/2)$.
The eight oriented tetrahedron shapes in the original two-octahedron
block simplify exactly to

\[
 (iR_0,iw,i/R_0,i/w),\qquad(i/R_0,iw,iR_0,i/w).
\]

They all have positive imaginary part: $w=e^{b+ia}$ and
$\Re R_0>0$. The exact rational face pairings and primitive peripheral
logarithms therefore continue throughout this positive path. The
leaf's primitive cone angle is $2\pi\lambda$, its core length is
$-2\Im t>0$, and the filling is smooth at $\lambda=1$.
All unfilled parent periods remain complete because $\psi_u(t,0)=0$.
For negative power use $t_{-2}=-\overline{t_2}$ at real parent angle.
Then $w$ becomes $\overline w$ and $R_0$ becomes
$1/\overline{R_0}$; the displayed ordered shapes still have positive
imaginary part. The real action constant in (18) is therefore the
absolute marked hyperbolic volume constant fixed by the complete
octahedra, not a choice of a formal stationary branch.

## 9. What this result supplies

Equations (1)--(3) provide an exact terminal replacement, a nonzero
uniform holomorphic leading term, and control of the full real and
nearby complex boundary. Equation (18) identifies its selected action
with the original primitive geometric filling, including the unit
phase. The result is restricted to a terminal two-crossing filling
at complete meridian parameter; it is not an all-orders meridian
statement or a theorem about every short tangle.

Applying several such replacements and proving the remaining filling
asymptotics is a separate assembly. Adjacent short-filled vertices
and arbitrary fixed short powers remain open in this research step.

## 10. Reproduction checks

The script [audit_short_terminal_filling.py](../experiments/audit_short_terminal_filling.py)
and its [saved results](../repro/results/research-short-terminal-filling.json)
check the finite formulas independently of the asymptotic derivation.
At 120-digit precision, 414 comparisons of crossing values and
double-root first derivatives at levels 3 through 20 had maximum
relative residual $1.25338\times10^{-117}$. Forty complete-sum
samples, using even and odd levels from 20/21 through 320/321 and
four real or complex parent values, check the leading amplitude and
phase in (2). These computations detect normalization and transcription
errors; the finite identities and contour estimates above are the proof.
