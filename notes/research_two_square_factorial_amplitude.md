# The original factorial amplitude through a two-square fold

Private written proof, 16 November 2026.

At every two-square edge classified by the radial primitive theorem,
both original same-index halfwire factorials are holomorphic units on
one neighborhood independent of the level. They have a uniform
all-order expansion with the retained original phase \(b_0\) and a
nonzero leading amplitude. This includes the square-root fold \(q=0\).
The proof fixes the phase constant and logarithmic marking, rather
than inferring an asymptotic expansion from finite-level holomorphy.

This result concerns the factors at the classified two-square edges.
It does not assert a single-phase expansion for unrelated incidences,
replace a free cardinal boundary by a factorial, or determine the
coefficient of the local Morse disk in the original relative cycle.

## 1. A centered factorial expansion with a fixed constant

Write
\[
 \Omega=\mathbb C\setminus\bigl((-\infty,0]\cup[1,\infty)\bigr).
 \tag{1}
\]
This domain is simply connected: \(u\mapsto u/(1-u)\) identifies
it with the plane cut along the nonpositive real axis. Let
\[
 J'(u)=\Log(2\sin\pi u),\qquad J(1/2)=0,
 \tag{2}
\]
where the logarithm is real on \(0<u<1\). This is the original
sine primitive, since \(\int_0^{1/2}\log(2\sin\pi u)\,du=0\).
Its reflection identities are
\[
 J(1-u)=-J(u),\qquad J^{(2r)}(1/2)=0\quad(r\ge1).
 \tag{3}
\]
In particular its restrictions to the upper and lower half-planes
are the marked branches of the archived half-plane expansions.

Use the original normalized gamma-product factorial \(G_N\), \(N\ge2\).
Its exact logarithmic derivative and divisor are
\[
 \frac{G_N'(w)}{G_N(w)}
  =\frac{\pi}{N^2}\sum_{k=0}^{N-1}(w-k)
          \cot\frac{\pi(w-k)}N,\qquad
 \operatorname{ord}_{w=k}G_N(w)=\lfloor k/N\rfloor .
 \tag{4}
\]
There are no other divisors. Terms with \(w=k\), \(0\le k<N\),
are removable. Put
\[
                       H_N(u)=G_N(Nu-1/2).
 \tag{5}
\]
Every divisor of (5) lies on one of the two removed real rays.
Thus \(H_N\) has a holomorphic logarithm on \(\Omega\).

Its exact normalization is
\[
                         H_N(1/2)=\sqrt N>0.
 \tag{6}
\]
Indeed (4) gives \(G_N'(N-1-w)/G_N(N-1-w)=G_N'(w)/G_N(w)\);
hence \(G_N(w)G_N(N-1-w)\) is constant. At \(w=0\) it is
\(\prod_{j=1}^{N-1}2\sin(\pi j/N)=N\). Positivity of the
defining gamma product on \(-1<w<N\) fixes the sign in (6).
Choose \(\log H_N(1/2)=\tfrac12\log N\).

**Lemma 1.** For every compact \(K\Subset\Omega\) and integer
\(R\ge0\),
\[
 \log H_N(u)=\tfrac12\log N+NJ(u)
  +\sum_{r=1}^{R}
    \frac{B_{2r}(1/2)}{(2r)!\,N^{2r-1}}J^{(2r)}(u)
  +O_{K,R}(N^{-2R-1}).
 \tag{7}
\]
The remainder is holomorphic and has the same order under every
fixed derivative on smaller compact sets. Here \(B_m(z)\) are
the Bernoulli polynomials and an empty sum is zero.

**Proof.** Equation (4) gives the literal midpoint sum
\[
 \frac d{du}\log H_N(u)
     =\sum_{k=0}^{N-1}F_u((k+1/2)/N),
 \qquad F_u(s)=\pi(u-s)\cot\pi(u-s).
 \tag{8}
\]
For \(u\) in a compact subset of \(\Omega\), \(0\le s\le1\),
this function and all its fixed derivatives are uniformly bounded.
The apparent singularity at \(u=s\) is removable; every other
possible pole would place \(u\) on a removed ray.

The leading integral is
\[
                       \int_0^1F_u(s)\,ds=J'(u).
 \tag{9}
\]
Its derivative is \(F_u(0)-F_u(1)=\pi\cot\pi u=J''(u)\).
At \(u=1/2\), integration by parts gives
\[
 \int_{-1/2}^{1/2}\pi v\cot\pi v\,dv
  =-2\int_0^{1/2}\log(\sin\pi v)\,dv=\log2,
\]
which fixes (9). The elementary log-sine integral here follows
from reflection and the sine double-angle formula.

Midpoint Euler--Maclaurin, with enough remainder terms, gives
\[
 \frac d{du}\log H_N(u)
  =NJ'(u)+\sum_{r=1}^{R}
    \frac{B_{2r}(1/2)}{(2r)!\,N^{2r-1}}J^{(2r+1)}(u)
    +O_{K,R}(N^{-2R-1}).
 \tag{10}
\]
The endpoint derivative difference used here is
\[
 \partial_s^{2r-1}F_u(1)-\partial_s^{2r-1}F_u(0)
                       =J^{(2r+1)}(u).
 \tag{11}
\]
The odd Bernoulli polynomials at \(1/2\) vanish. Formula (10)
can, for example, be obtained by retaining one further even term
and absorbing it and its uniformly bounded remainder at the stated
order.

Join \(K\) to \(1/2\) by paths of uniformly bounded length in a
larger compact subset of \(\Omega\). Such paths exist by a finite
cover and connectedness of the domain. Integrating (10), then
using (3) and (6), proves (7), including its constant. Cauchy
estimates on a slightly larger compact set give the derivative
assertion. No asymptotic error was continued from another domain.
\(\square\)

The usual uncentered version follows by replacing \(u\) in (7)
by \(u+1/(2N)\). Bernoulli translation gives
\[
 \log G_N(Nu)=\tfrac12\log N+NJ(u)+\tfrac12J'(u)
   +\sum_{r=1}^{R}
       \frac{B_{2r}}{(2r)!\,N^{2r-1}}J^{(2r)}(u)
   +O_{K,R}(N^{-2R-1}),
 \tag{12}
\]
where \(B_{2r}=B_{2r}(0)\). To justify the indicated remainder,
first retain sufficiently many terms in (7) and in its Taylor
expansion. The identities \(B_m(1)=B_m(0)\) for \(m\ne1\)
and \(B_m(0)=0\) for odd \(m>1\) cancel the intervening even
inverse powers. The logarithm in (12) is the one induced by (5);
on the original real interval it is the actual real logarithm.

## 2. A common exact unit neighborhood

At a classified two-square edge write
\[
 t=-iH,\quad u=-iK,\quad
 A=\tanh(H/2),\quad B=\tanh(K/2),\quad
 q=iQ,\quad Q^2=A^2+B^2-1\ge0,
 \quad |Q|<\min(A,B)<1.
 \tag{13}
\]
These are the actual limiting data of the pinned radial theorem;
in particular \(H,K>0\). The retained stationary wire is
\[
                   x_*=\frac12-\frac{i}{\pi}\operatorname{artanh}Q.
 \tag{14}
\]
Use \(D=N-1\) and the literal source factor
\[
 B_N(x,t)=
 \frac{N}{G_N(Nz_+-1/2)G_N(Nz_--1/2)G_N(Nx)^2},
 \qquad z_\pm=\frac12-x\pm\frac{t}{2\pi}.
 \tag{15}
\]
At (13)--(14),
\[
 z_+=\frac{i}{\pi}\{\operatorname{artanh}Q-H/2\},
 \qquad
 z_-=\frac{i}{\pi}\{\operatorname{artanh}Q+H/2\}.
 \tag{16}
\]
The first lies strictly below the real axis and the second strictly
above it. The same assertion holds with \(H\) replaced by \(K\).

**Theorem 2.** A neighborhood \(\mathcal U\) of
\((x_*,t,u)\), independent of \(N\ge2\), exists on which
\(B_N(x,t)\) and \(B_N(x,u)\) are holomorphic and nonzero.
It can be chosen so that all their normalized arguments
\(x,z_+,z_-\) lie in fixed compact subsets of \(\Omega\).
The assertions hold simultaneously for every edge of a finite
classified two-square matching, including every \(Q=0\).

**Proof.** Shrink a relatively compact neighborhood so that
\(1/4<\Re x<3/4\) and the two signs in (16) are separated from
zero, for each endpoint. Then the shifted arguments in (15)
are nonreal at every level and have no divisor by (4).
Also \(-1<\Re(Nx)<N\), so \(G_N(Nx)\) is a unit.
The strict inequalities are independent of \(N\).
They also give the compact subsets of \(\Omega\).
Intersect the finitely many neighborhoods for the matching.
\(\square\)

For precision, the corresponding reversed factor
\(B_N(D/N-x,t)\) is an exact unit on a possibly smaller common
neighborhood as well. Its shifted arguments are
\(N(x-1/2\pm t/(2\pi))+1/2\), still strictly nonreal;
its unshifted argument is \(N(1-x)-1\), whose real part lies
strictly between \(-1\) and \(N\) for all \(N\ge2\).
This does not identify its different asymptotic phase with \(b_0\).

## 3. Agreement with the retained geometric logarithms

The domain membership at the target alone does not determine a
previously continued logarithmic marking. Here the actual positive
approach and its allowed tangent contraction fix it.

**Lemma 3.** At each edge in Theorem 2, the primitive obtained by
using (2) in
\[
 b_{\rm can}(x,t)=-J(z_+)-J(z_-)-2J(x)
 \tag{17}
\]
is exactly the retained original \(b_0(x,t)\) germ, including
its additive constant and its logarithmic derivatives.

**Proof.** Let \((a_j,b_j)\) be its positive approach, tending to
\((-iA,-iB)\). The pinned positive-wire theorem proves that
\[
              (\lambda a_j,\lambda b_j),\qquad 0\le\lambda\le1,
 \tag{18}
\]
stays positive. Its original stationary branch has
\(\Re q_j(\lambda)>0\), \(x_j(0)=1/4\). Thus continuation along
(18) gives precisely the original marked phase, from completeness.

Put \(\lambda_0=(A^2+B^2)^{-1/2}\le1\). The limiting root is
nonnegative real on \([0,\lambda_0]\), with
\[
 q_\lambda^2=1-\lambda^2(A^2+B^2),
 \tag{19}
\]
and for \(\lambda>\lambda_0\) is the imaginary root whose sign
is that of \(Q\). If \(Q=0\), this latter interval is empty.
The principal square roots along (18) converge uniformly to
this continuous path. For \(Q\ne0\), the sign of their imaginary
parts is eventually the sign of \(Q\); at the single zero of
(19), continuity of the square root gives the same conclusion.
The inverse cotangent has no singularity on this compact path,
which avoids \(q=\pm i\), so the wires converge uniformly too.

The limiting endpoint angle is
\[
                     t_\lambda=-2i\operatorname{artanh}(\lambda A).
 \tag{20}
\]
Before \(\lambda_0\), \(x_\lambda\) is real in \([1/4,1/2]\).
For \(0<\lambda\le\lambda_0\), the two arguments \(z_\pm\)
therefore have opposite nonzero imaginary parts, with nonnegative
real parts. At \(\lambda=0\) all three arguments equal \(1/4\).
After \(\lambda_0\), write \(q_\lambda=iQ_\lambda\).
Then
\[
 Q_\lambda^2=\lambda^2(A^2+B^2)-1,\qquad
 |Q_\lambda|<\lambda A,\quad |Q_\lambda|<\lambda B,
 \tag{21}
\]
because \(\lambda A,\lambda B<1\). Formula (16), with these
contracted values, again places \(z_+\) strictly below and
\(z_-\) strictly above the axis. The wire has real part \(1/2\).

Consequently each entire limiting argument path is a compact
subset of \(\Omega\). Uniform convergence implies that the late
actual positive paths (18) stay in this same domain. Along them
the logarithm (2) is the original one, since it agrees at their
common complete starting point. Its primitive constants agree
there as well. Passing to the limit proves (17), and continuation
to the small independent-variable neighborhood proves equality
of the full germs. This argument does not assume that the radial
charge path is connected, or deform fixed primitive equations
along (18). \(\square\)

## 4. The actual local amplitude

**Theorem 4.** Uniformly on compact subsets of the neighborhood
in Theorem 2, with all fixed holomorphic derivatives after the
displayed phase and prefactor are extracted,
\[
 \boxed{\quad
 B_N(x,t)=\frac{e^{Nb_0(x,t)}}{2N\sin\pi x}
   \exp\left\{\sum_{r=1}^{R}\frac{C_r(x,t)}{N^{2r-1}}
                     +O(N^{-2R-1})\right\},\quad}
 \tag{22}
\]
for every \(R\ge0\), where
\[
 C_r(x,t)=-
 \frac{B_{2r}(1/2)\{J^{(2r)}(z_+)+J^{(2r)}(z_-)\}
                  +2B_{2r}J^{(2r)}(x)}{(2r)!}.
 \tag{23}
\]
In particular \(2N\sin(\pi x)e^{-Nb_0}B_N\to1\) holomorphically,
and the leading amplitude is a unit through the fold.

**Proof.** Apply (7) to the two shifted factors in (15), and
(12) to its two unshifted factors. The four half-logarithms give
\(2\log N\); subtracting them from the numerator \(\log N\)
leaves \(-\log N\). The two unshifted half-logarithms of the
sine give \(-J'(x)=-\Log(2\sin\pi x)\). The action and all
remaining terms are exactly (17), (23). Lemma 3 identifies the
action with the retained \(b_0\). The uniform remainder and
derivative statements follow from Lemma 1. \(\square\)

For the two endpoints of one affected edge this gives
\[
 B_N(x,t)B_N(x,u)
   =\frac{e^{N\{b_0(x,t)+b_0(x,u)\}}{4N^2\sin^2\pi x}
                   (1+O_{\rm hol}(N^{-1})).
 \tag{24}
\]
At its stationary limit the leading coefficient is explicitly
\[
               \frac1{4\sin^2\pi x_*}=\frac{1-Q^2}{4}>0.
 \tag{25}
\]
It equals \(1/4\) at a fold. For a finite matching the products
of (22)--(25) hold simultaneously, with their original shared
angular variables. Compact families of the stated regular data
have uniform constants after taking a finite cover; no height or
regularity margin is claimed outside such compact families.

There is thus no Stokes or logarithmic wall obstruction to this
specific local factorial amplitude. The proof does not delete
exponentially small terms of the exact factorial as a source
identity: (22) is an asymptotic expansion of that exact function.
The full unsummed Hessian theorem supplies nonzero coordinate
Jacobians through a fold, so these affected factors introduce no
additional zero under its local Morse change of variables.

The other factors of the original source remain in place:
unrelated halfwires, the full-Hermite angular kernels, both charged
cosine terms, all constants and spectators, and any genuine free
cardinal ends. A nonzero local factorial density does not establish
the coefficient of the geometric exponential sector in their
prescribed integral. In particular neither a global contour
coefficient nor a metric completion at a two-square limit follows.

## Direct sources and coverage

* [Exact canonical factorial](research_exact_cyclotomic_factorial.md),
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b:
  the original gamma product, normalization and exact finite logarithmic
  derivative. The complete written text was reread.
* [Exact factorial divisors](research_factorial_rectangle_divisor_criterion.md),
  SHA256 462b8c22c73f73b12152bca96cf6636708dcf153c2cbc2751458454827b3ddf8:
  all-level divisor orders and the distinction between a unit and a
  pole-free interpolation. The complete text was reread.
* [Positive wire product domain](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  actual tangent contraction, inverse-cotangent marking and exact
  halfwire conventions. The complete text was reread.
* [Radial two-square primitive lift](research_radial_two_square_primitive_lift.md),
  SHA256 21d9af750653621cc82bd73373a99a138210fc4cdb10407faabcb209505df9ad:
  the supplied radial-limit hypotheses and classification (13).
  The unchanged complete author and peer-source readbacks are retained.
* [Full unsummed fold phase](research_unsummed_two_square_morse_lift.md),
  SHA256 82ad7a75e6ab2857bbebb2f003f7e182ab1f26da1cf425f579106cdad11d15dd:
  the retained \(b_0\) marking, full Hessian result and exact-source
  limitations. The complete text was reread.

The archived [uniform half-plane expansion](research_factorial_uniform_halfplane_continuation.md)
and [lower-half continuation](research_lower_half_factorial_continuation.md)
already establish factorial asymptotics away from real walls. Both
complete texts were read for coverage. The proof here uses (4) directly
to fix all centered constants on one slit domain; its source-specific
addition is the contraction proof of the retained phase and the actual
unit/amplitude at every classified two-square edge.

Only written mathematics, source-text reads and hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Frozen notes, manuscripts and public documents were unchanged.
