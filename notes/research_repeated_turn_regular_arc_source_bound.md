# An exact regular-arc bound for the repeated-turn tensor source

Private written proof, 16 November 2026.

The full-step tensor interface admits a constructive block recurrence
whose highest surviving classical coefficient is a scalar unit on
regular arcs. Its higher-order quantum terms remain in the equation.
The existing slow-forward/fast-backward estimate then bounds the actual
source using an initial packet and its actual exponential ceiling on a
right buffer. No leading quantum coefficient is inverted.

The finite-root envelope below belongs to an explicit classical
presentation. It need not be the geometric envelope. Exceptional
colors, the initial packet at a positive color fraction, and global
gluing across those colors remain separate.

## 1. Exact input and the coefficient chart

Use the full-step interface at its pinned version. Its source is
\[
 Y_N=U_\tau\operatorname{can}
       \left(Q_{\rm base}\prod_i V_{n_i}Q_i\right),\qquad
 Q_i=\operatorname{can}\prod_{\ell=1}^{r_i}
             K_N(2\cosh(\alpha_{i\ell}/N),C).
 \tag{1}
\]
The number of factors, their powers and their endpoint counts are fixed.
Empty transformed factors have already been removed. Keep the entire
actual descended column \(\mathcal Y_N=U_\tau Z_N\) of that interface,
not just its component (1). All shared parameters and first normals
remain in this column.

Put \(h=1/N\), \(q=e^{\pi ih}\), and write
\[
 v_N(u)=e^{2\pi i(u+h/2)},\qquad
 C_N(u)=v_N(u)+v_N(u)^{-1},\qquad
 E f(u)=f(u+h).
 \tag{2}
\]
Write \(y_N(u)=\mathcal Y_N(C_N(u))\) for its angular evaluation;
operator equations below use this angular lift of the column.
The exact ordered equations (25)--(26) of the interface, expanded
in this physical full step, give a fixed finite matrix of Laurent
operators
\[
                         \mathcal R_h(v,E)\mathcal Y_N=0.
 \tag{3}
\]
Every row of (3) is an exact quotient equation. Its ordinary residual
is a \(P_N(C)\) multiple, so its value and first \(u\)-derivative
vanish at \(u=j/N\).

Here and below coefficient denominators are cleared before claiming
a global quotient equation. We use rational formulas only on their
specified coefficient charts. A coefficient which is a nonunit in
the finite physical quotient is never canceled there.

After removing removable scalar powers of \(h\), the coefficients
on a chart are holomorphic at \(h=0\), rational in \(v\), and
holomorphic in the endpoint parameters. This follows directly from
the finite input formulas: \(w=2\cosh(\alpha h)\), \(q=e^{\pi ih}\),
and \(P_N(w)=4\cosh^2(\alpha/2)\); the divided scalar factors have
their indicated removable Taylor limits. One may treat the two
level parities separately if a source convention retains a parity
constant. A common denominator, with nonzero specialization on
the chart, makes the rows polynomial in \(v,v^{-1}\).

The chart and the parameters must be retained in the construction.
A minor or a later elimination denominator may vanish at a special
parameter. Uniform statements below concern compact parameter sets
in a chart where the stated coefficient bounds and unit conditions
hold. They do not assert one choice for every bounded complex
parameter set.

## 2. A classical adjugate gives an exact quantum block equation

Let \(d\) be the length of \(\mathcal Y_N\), and let
\(\mathcal R_0(v,t)\) be the commuting specialization of (3).
It has generic full column rank.

To see this before the outer turn, use the first equation (24) of
the interface. On the generic coefficient field it is
\[
             \left\{\frac{t+t^{-1}}2 I-\mathcal S_0(C)\right\}Z=0,
 \tag{4}
\]
after division by its nonzero scalar clearing polynomial.
Its determinant has a nonzero highest power of \(t\). The polynomial
conversion (10) is invertible on the generic original chart, so
the stacked principal rows (25) have full column rank there.
The classical turn is an automorphism of the original cubic and
its physical chart is dominant. Pullback by that automorphism
preserves generic full rank. Further coefficient clearing cannot
destroy it. These are rank assertions over the function field;
they make no cancellation at an endpoint source.

Choose \(d\) rows whose square principal matrix \(M_0(v,t)\) has
nonzero determinant
\[
                             p(v,t)=\det M_0(v,t).
 \tag{5}
\]
Let \(M_h(v,E)\) be the same exact rows. Lift the commuting
adjugate \(\operatorname{adj}M_0(v,t)\) to a left full-step
operator by putting every coefficient before its power of \(E\).
Then
\[
 \widehat{\operatorname{adj}M_0}\,M_h
                          =p(v,E)I+hK_h(v,E).
 \tag{6}
\]
The matrix \(K_h\) has fixed finite shift order and holomorphic
coefficients on a slightly smaller chart.

Indeed the left side has specialization
\(\operatorname{adj}M_0 M_0=pI\). Commuting a step past a
coefficient replaces \(a(v)\) by \(a(q^{2k}v)\); its difference
from \(a(v)\) is divisible by \(h\) holomorphically. There are
only finitely many such operations. This proves (6) as an exact
operator identity with a holomorphic remainder, not an asymptotic
source equation.

After clearing any coefficient denominators introduced in this
calculation, (6) applied to the actual column is still a quotient
identity. Full shifts and multiplication preserve the original
double-root ideal. Thus no component of \(\mathcal Y_N\), no
normal and no source datum is discarded by this construction.

For fixed parameters, the coefficients of the nonzero Laurent
polynomial (5) are rational in \(v\). Its highest and lowest
nonzero coefficients have only finitely many zeros or poles on
the physical circle, unless a parameter specialization changes
the polynomial. Rechoose the minor at such a parameter, or
exclude it from the current chart. Consequently (6) supplies
regular compact physical arcs outside a finite algebraic set
for each fixed valid parameter choice.

### An optional generic Fitting reduction

There is a finite improvement which also preserves the source.
Form all maximal minors \(p_\nu(v,t)\) of \(\mathcal R_0\).
Over the field of meromorphic parameter germs and rational
functions of \(v\), the Laurent polynomial ring in \(t\) is a
principal ideal domain. Its Euclidean algorithm gives
\[
                     g=\sum_\nu b_\nu(v,t)p_\nu(v,t),
 \tag{7}
\]
where \(g\) is their gcd, up to a Laurent unit.
Lift each adjugate row construction and then (7), always multiplying
on the left. This gives exactly
\[
                             \{g(v,E)I+h\widetilde K_h\}
                                     \mathcal Y_N=0
 \tag{8}
\]
on the coefficient chart. Multiplying by a scalar common denominator
\(D(v)\) gives a global quotient equation with principal polynomial
\(D(v)g(v,t)\). We retain this factor in that equation and absorb it
into the notation \(p\) below. All new coefficient denominators are
explicit exceptional factors; they are not canceled at their physical
zeros. The same convention applies to coefficient clearing in (6).

Generically the nonzero roots of \(g\) are exactly the rank-drop
support of this displayed cleared principal presentation. This is
its zeroth Fitting support. It is not automatically the support
of a minimal source module: over-clearing and the retained source
or recovery branches can add factors. Exceptional specialization
of the Euclidean calculation is also excluded from its chart.

Either (6) or (8) will be used below. Denote its scalar principal
Laurent polynomial by \(p\).

## 3. Normalization and the actual normal block

Multiply the exact equation by a fixed left power of \(E\) so
that every quantum shift index is nonnegative. This changes
the commuting principal polynomial only by a monomial; the
shift of its coefficients changes the remainder by \(O(h)\).
If useful, multiply also by \(E-1\). We henceforth make that
last choice, so the finite-root spectral radius is at least one.
This is an explicit harmless enlargement of the upper envelope.

Write the resulting exact equation as
\[
       \left\{p(v_N(u),E)I+hK_h(v_N(u),E)\right\}\mathcal Y_N=0,
 \qquad p(v,t)=\sum_{i=0}^m a_i(v)t^i,\quad m\ge1.
 \tag{9}
\]
The quantum order may exceed \(m\). On a regular compact arc,
assume
\[
                         |a_m(e^{2\pi iu})|\ge c>0.
 \tag{10}
\]
Its neighborhood and parameter compact are chosen so the same
unit condition holds uniformly. Set
\[
             \rho(u)=\max\{|t|:p(e^{2\pi iu},t)=0\}.
 \tag{11}
\]
The optional factor above ensures \(\rho(u)\ge1\).

Differentiating the ordinary residual of (9) once in \(u\)
and then evaluating at the physical grid gives the exact
equation for the original first normal. The principal block
on \((\mathcal Y_N,\partial_u\mathcal Y_N)\) is
\[
             \begin{pmatrix}pI&0\\(\partial_u p)I&pI\end{pmatrix}.
 \tag{12}
\]
Its highest coefficient is invertible by (10), and its
characteristic determinant is a power of \(p^2\).
Consequently its finite-root radius is still (11).
All coefficient derivatives and product-rule normals are present.
At compact interior colors, conversion between \(u\)-normal and
spectral normal has a bounded nonzero factor. The odd simple
endpoint is not part of this interior assertion.

The same triangular argument includes any fixed exterior-parameter
derivatives on a slightly larger parameter chart. It does not
differentiate the spectral residual twice: only its original
value and first physical normal are guaranteed to vanish.

## 4. The actual exponential ceiling and the buffered estimate

The actual column in (3), with its first normals, has a global
bound
\[
                           \|\mathcal Y_N\|_{\mathbb R}
                                      \le e^{C N}.
 \tag{13}
\]
Here and below a polynomial factor is absorbed into the constant
in this coarse ceiling. The pre-turn bound is the proved budget
of the interface. For completeness the remaining turn costs at
most an exponential, uniformly in the original real color.

Indeed \(S_j=\prod_{k\le j}2\sin(k\pi/N)\) and
 \(2\sin(k\pi/N)\ge4\min(k,N-k)/N\) imply
\(\max_j S_j^{-1}\le e^{CN}\) by the elementary factorial
bound. Hence \(\max_{j,Z\in[-2,2]}|e_j(Z)|\le e^{CN}\),
and the real kernel norm has the same type of bound.
The exact identity
\[
                           Tf(Z)=\phi_N(K_N(Z,\cdot)f)
 \tag{14}
\]
and the polynomial full-jet trace bound give
\(\|Tf\|_{\mathbb R}\le e^{CN}\|f\|_{\mathbb R}\).
The original \(R^{\pm1}\) has polynomially bounded physical
values and first normals; canonical Hermite reconstruction
therefore gives a polynomial multiplication cost.
This proves (13) for \(U_\tau=\kappa^\tau TR^{-\tau}T\).
Markov bounds give its first physical normals with the same
ceiling. The argument also holds uniformly on the fixed
complex endpoint-parameter sets used in the interface.

Fix \(a<t<b\) in one regular compact interior arc, with all
fixed shift buffers still inside that arc. Let \(\mathcal P_N(a)\)
be the actual initial packet of \(m\) consecutive values of
the block (12), starting at \(j/N\to a\). Put
\[
       A_a=\limsup_N N^{-1}\log(1+\|\mathcal P_N(a)\|).
 \tag{15}
\]
It is finite by (13). No independently known smaller value
of this macroscopic initial budget is presumed.

**Theorem 1.** For the actual repeated-turn source column,
\[
 \limsup_N\frac1N\log
   \big(\|y_N(t_N)\|+\|y_N'(t_N)\|\big)
       \le A_a+\int_a^t\log\rho(u)\,du ,
 \tag{16}
\]
where \(t_N\) is a grid coordinate tending to \(t\).
The estimate is uniform on compact parameter
charts satisfying (10), with the corresponding uniform
initial budget in (15).

**Proof.**
Apply the exact slow-forward/fast-backward reduction in the
pinned fast-elimination note to the finite block (12).
Its proof works with block norms: the classical highest
coefficient is invertible, whereas every coefficient above
the classical order is \(O(h)\). Solving the order-\(m\)
row defines its exact defect \(z_j\); finitely many forward
substitutions give
\[
       Y_{j+1}=A_{N,j}Y_j+B_{N,j}z_j,\qquad
       z_j=h C_{N,j}Y_j+
                  h\sum_{\ell=1}^{r}D_{N,j,\ell}z_{j+\ell},
 \tag{17}
\]
with uniformly bounded matrices. A possible \(O(h)\)
coefficient of \(z_j\) is absorbed using its inverse near
the identity. There is no division by the highest quantum
coefficient. If there are no higher terms, only the forward
system is needed.

The limiting slow companion includes (12), and has spectral
radius \(\rho(u)\). The continuous positive-metric argument
in the pinned spectral-bound note applies to fixed-size
matrices, including nonnormal blocks and repeated roots.
For any fixed \(\varepsilon>0\), normalize by step weights
\(\rho(j/N)+2\varepsilon\). The exact inequalities from (17)
then have the form
\[
 U_{j+1}\le U_j+C Z_j,\qquad
 Z_j\le hC U_j+hC\sum_{\ell=1}^{r}Z_{j+\ell}.
 \tag{18}
\]
Uniform \(o(1)\) metric variation is absorbed in
\(\varepsilon\), as in that proof.

Retain all \(r\) terminal defect values at \(j/N\to b\).
Equation (13) bounds them, also after weight normalization,
by \(e^{C_1N}\). The explicit positive supersolution of the
fast-elimination note bounds their contribution at \(t_N\) by
\[
        e^{C_2N}N^{-(b-t+o(1))N/(2r)}.
 \tag{19}
\]
This is superexponentially small. The slow part costs only
\(\exp[O(1)]\) beyond the initial packet and the step weights.
The finite positive comparison argument in that note uses
only inequalities, so it is unchanged for the block norms
in (18). Finally take logarithms, use the Riemann sum, and
send \(\varepsilon\downarrow0\). Since \(\rho\ge1\), there
is no zero-radius integrability issue. This proves (16).
Exterior parameter derivatives use the triangular version
of (12) or Cauchy on a larger regular parameter chart.
\(\square\)

The notation in (16) does not assert a bound for the canonical
polynomial on a fixed complex color strip. It concerns its
actual physical values and first normals.

## 5. What this removes, and what remains

The construction is source preserving: it takes left combinations
of the original quotient equations and bounds their actual
solutions using both boundaries. Fast terminal data are bounded
in (19), never set to zero. Thus small higher-order quantum
coefficients need not by themselves prevent a regular-arc
upper bound.

For each fixed valid parameter, one obtains an explicit finite
exceptional algebraic set from the chosen principal polynomial
and its coefficient chart. The generic gcd construction can
reduce extraneous roots of an individual row minor, but does
not cancel a nonunit or identify the actual source quotient.

The projective resonance theorem concerns the reduced composed
terminal correspondence. Its exclusion of old-infinity points
does not alone show that every exceptional factor in the present
cleared presentation is an endpoint factor. Nor does it supply
the macroscopic initial budget (15), a right buffer across a
singular color, or a global comparison of the integral in (16)
with the filled geometric action. Those assertions are not
made here. There is also no lower bound or selected-branch
coefficient assertion.

## 6. Coverage and direct sources

The slow/fast comparison and the positive spectral metric already
exist in the archive. The new step is the exact adjugate (or
maximal-minor Bezout) lift from the repeated-turn full-normal
interface, followed by their application to that actual block.
It requires no new generic-annihilator theorem.

Complete direct sources were read at their recorded versions:

* [Full-step repeated-turn tensor interface](research_full_step_repeated_turn_tensor_interface.md):
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398;
  exact rows, quotient-safe operations, original source column,
  source initialization and full-normal conventions.
* [Regular-arc fast-color elimination](actual_regular_fast_color_elimination.md):
  SHA256 68e32bc72a875d081eeb91ef10ace5c5b8d5273e71b15265afcf0e9fd8dd4b49;
  exact defect equation and the two-boundary positive barrier.
* [Macroscopic spectral upper bound](actual_macroscopic_a_spectral_upper_bound.md):
  SHA256 4d2ab2dbcd9afd5fca5f9628dbeb36636d741f0087fbc92540b649848711f0ac;
  continuous positive metric for the finite-root envelope.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or compilation
was run. Adopted notes and public manuscripts are unchanged.
