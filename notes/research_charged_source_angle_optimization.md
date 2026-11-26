# Angle optimization for the complete charged bridge source

Private written deduction, 14 November 2026. The object throughout is
the original closed, marked braid scalar. No numerical calculation,
test, or change to a frozen manuscript is used.

The exact bridge formula has a useful consequence before any saddle is
chosen. Including its clock prefactors turns the absolute weight of
every term into reciprocal sine factorials on a transportation polytope.
Its limiting exponent is a concave sum of ideal-tetrahedron volumes.
The phase-sensitive block estimate then gives a finite-dimensional
variational upper bound for the original scalar, with every clock and
closing factor retained. This upper bound is not yet identified with
the volume of the knot complement, and it supplies no lower bound for
the coherent clock sum.

## 1. The original events and their endpoint charges

Use the complete signed braid and the exact conventions of
[the charged bridge formula](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_global_charged_bridge_flow.md).
There are \(B\) overbridge events and \(b\) closing events. Put
\(k=B+b\), the number of anchor segments, and \(d=N-1\). Every
event has total polynomial degree \(d\), and the original coefficient
requires degree \(d\) at every anchor. Distinct incidences at the same
anchor remain distinct.

An overbridge with \(m\ge1\) encounters has \(m+1\) ordered binary
blocks, with lengths
\[
 L_0=d-h_1,\qquad L_j=h_j-h_{j+1}\ (1\le j<m),\qquad
 L_m=h_m.                                                   \tag{1}
\]
Their sum is \(d\). A closing event has one block of length \(d\).
Let a block \(e:u\to v\) give exponent \(n_{e,0}\) to its tail
anchor and exponent \(n_{e,1}\) to its head anchor. Thus
\[
 n_{e,0},n_{e,1}\ge0,\qquad L_e=n_{e,0}+n_{e,1}.
                                                               \tag{2}
\]
The two incidences are kept separately even when \(u=v\).

Define \(\mathcal P\) by nonnegative real incidence coordinates
\(x_{e,\epsilon}\) satisfying
\[
 \sum_{e\text{ in event }v}\sum_{\epsilon=0}^1x_{e,\epsilon}=1,
 \qquad
 \sum_{(e,\epsilon)\text{ assigned to anchor }a}
                    x_{e,\epsilon}=1.                        \tag{3}
\]
This is a compact bipartite transportation polytope, with event
vertices on one side and anchor vertices on the other. Its underlying
incidence graph is fixed by the original word and the chosen exact
overbridge grouping.

**Proposition 1.** The original clock assignments together with one
chosen monomial from each block, whose product has the prescribed
anchor degrees, are in bijection with
\(d\mathcal P\cap\mathbb Z^{\mathrm{incidences}}\).

Indeed (2) recovers every block length. For an overbridge the inverse
of (1) is
\[
                    h_j=\sum_{\ell=j}^{m}L_\ell .           \tag{4}
\]
Nonnegative lengths summing to \(d\) give precisely the original
monotone clocks. The second equations in (3) are the original anchor
coefficient conditions. Conversely a chosen block monomial gives these
incidences and clocks uniquely. The exact block coefficients have
already summed their internal choices; there is no missing binomial
multiplicity in this bijection.

## 2. The exact magnitude, including the clock factors

Put
\[
 S_j=\prod_{r=1}^{j}2\sin(\pi r/N),\qquad S_0=1.
\]
All \(S_j\), \(0\le j\le d\), are positive, and
\[
                      S_jS_{d-j}=N.                         \tag{5}
\]
The magnitude of a block coefficient is
\(S_{L_e}/(S_{n_{e,0}}S_{n_{e,1}})\). The original overbridge
factor, with its phase still retained, has magnitude
\[
 |\Gamma_v|=\frac{S_{h_1}}{S_{h_m}\prod_{j<m}S_{h_j-h_{j+1}}}
            =\frac{N}{\prod_{e\text{ in }v}S_{L_e}}.
                                                               \tag{6}
\]
This is the root-reflection calculation in
[the original length-frame source](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_length_gauge_clock_source.md),
Section 3. Consequently each overbridge contributes exactly
\[
                 \frac{N}{\prod_{e\text{ in }v}
                             S_{n_{e,0}}S_{n_{e,1}}}.        \tag{7}
\]
A closing block has the same expression with its single pair of
incidences; by (5) that expression is exactly one. Its pivotal phase
has not been removed.

For an allowed incidence assignment \(n\), let
\[
 \Omega_N(n)=\frac{W_{h(n)}}{|W_{h(n)}|}
               \prod_e\alpha_e(h(n))^{L_e}
                          w_e(h(n))^{n_{e,1}}.              \tag{8}
\]
Here \(W_h,\alpha_e,w_e\) are exactly the original factors in
the charged bridge formula, including its closing pivots and propagated
frames. Every factor in (8) has modulus one. In particular no phase is
chosen from an optimizer or from the value of the knot invariant.
The original scalar is exactly
\[
 \boxed{\displaystyle
 K_N=\chi_N N^{k-1}
       \sum_{n\in d\mathcal P\cap\mathbb Z^{\mathrm{incidences}}}
       \Omega_N(n)\prod_{e,\epsilon}S_{n_{e,\epsilon}}^{-1}.}
                                                               \tag{9}
\]
This follows from (7) for all events and the original factor
\(\chi_N/N\). Closure incidences can instead be eliminated using
(5), giving the equivalent factor \(\chi_N N^{B-1}\). Equation
(9) keeps them to make both sets of conservation equations explicit.
The exact bridge theorem has already proved that the anchor sampling
introduces no cyclic aliases. None is discarded in (9).

## 3. Concavity of the actual absolute exponent

Define
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 \mathcal V(x)=-\sum_{e,\epsilon}J(x_{e,\epsilon}).          \tag{10}
\]
The continuous values at zero and one are included. A closing row has
two entries summing to one, so its contribution to (10) is zero.

For nonnegative \(y_1,\ldots,y_s\) with sum one, set
\(A_j=\sum_{i\le j}y_i\). Reflection \(J(1-t)=-J(t)\) gives
the exact identity
\[
 -\sum_{i=1}^sJ(y_i)
   =\sum_{j=2}^{s-1}
       \{-J(A_{j-1})-J(y_j)-J(1-A_j)\}.                    \tag{11}
\]
Each summand is the volume divided by \(\pi\) of an ideal
tetrahedron with angles
\(\pi A_{j-1},\pi y_j,\pi(1-A_j)\). The sum telescopes, so
there is no added volume constant. This identity extends to the
closed simplex by continuity.

The tetrahedral angle-volume function is strictly concave on its
open angle simplex. For the normalized tetrahedral volume
\(-J(a)-J(b)-J(c)\), the negative Hessian in the first two
normalized angles is \(\pi\) times
\[
 \begin{pmatrix}
 \cot(\pi a)+\cot(\pi c)&\cot(\pi c)\\
 \cot(\pi c)&\cot(\pi b)+\cot(\pi c)
 \end{pmatrix},\qquad a+b+c=1.                             \tag{12}
\]
The diagonal entries of the displayed cotangent matrix are positive
by the sine addition formula, and that matrix has determinant one.
The fan maps in (11) jointly detect every
nonzero tangent variation of a row with \(s\ge3\). Thus its row
entropy is strictly concave in the open simplex. A two-entry row has
identically zero entropy. Summing proves concavity of \(\mathcal V\)
on \(\mathcal P\), with strict concavity wherever every nonzero
allowed variation changes a positive row with at least three entries.
Forced zero faces and directions supported only on two-entry rows
must be retained; no general interior-maximizer assertion is needed.

Define the positive sum without its external scalar by
\[
 Z_N^+=\sum_{n\in d\mathcal P\cap\mathbb Z^{\mathrm{incidences}}}
                         \prod_{e,\epsilon}S_{n_{e,\epsilon}}^{-1}.
\]
Then
\[
                  \lim_{N\to\infty}\frac1N\log Z_N^+
                           =\max_{x\in\mathcal P}\mathcal V(x).
                                                               \tag{13}
\]
If the polytope is empty the sum is zero; otherwise the following
proof also establishes that its required integer points exist.
Uniformly for \(0\le j<N\),
\(\log S_j=NJ(j/N)+O(\log(N+1))\). This follows by subtracting
the two endpoint logarithms from \(\log(2\sin\pi t)\) and
applying elementary integral comparison to the remaining smooth
function and to each endpoint logarithm. There are polynomially many
incidence assignments. This proves the upper bound in (13).

To prove the lower bound, round \(dx\) for a maximizing real flow
while retaining its row and column sums. Confine each coordinate to
its floor/ceiling interval. A nonintegral supported subgraph has no
vertex of degree one, since all required sums are integral. It
therefore has an even cycle. Alternately increase and decrease its
entries until one becomes integral, keeping every sum and every
floor/ceiling interval. Repeat. The resulting integer flow differs
coordinatewise from \(dx\) by at most one. Continuity of (10), or
its endpoint modulus \(O(\delta|\log\delta|)\), proves the matching
exponential lower bound for this positive sum. This is a lower bound
for \(Z_N^+\), not for the coherent scalar (9).

## 4. Fixed-clock capacity equals constrained angle optimization

Let \(\lambda_e=x_{e,0}+x_{e,1}\), and let \(\mathcal L\) be
the projection of \(\mathcal P\) onto these block lengths. Each
overbridge row has length sum one; every closing length is one.
For fixed \(\lambda\in\mathcal L\), put
\[
 v_\lambda(t)=J(\lambda)-J(t)-J(\lambda-t),\qquad
 0\le t\le\lambda.
\]
The original anchor constraints are
\[
 \sum_{e:v\to a}t_e-\sum_{e:a\to v}t_e
                     =1-\sum_{e:a\to v}\lambda_e.          \tag{14}
\]
The endpoint cases \(\lambda=0,1\) remain included.

For positive radius ratios \(r\), define
\[
 I_{\lambda,r}(\theta)=\frac1{2\pi}
       \int_{-\pi\lambda}^{\pi\lambda}
                   \log|1+r e^{i(\theta+s)}|\,ds.
                                                               \tag{15}
\]
The block theorem proves
\[
 I_{\lambda,e^y}(0)
           =\max_{0\le t\le\lambda}\{v_\lambda(t)+yt\}.
                                                               \tag{16}
\]
Write \(s_a=\log r_a\) for anchor log-radii. The exact dual
identity for the closed feasible polytope is
\[
 \begin{split}
 \max_{x\in\mathcal P,\,x_{e,0}+x_{e,1}=\lambda_e}\mathcal V(x)
 ={}&-\sum_eJ(\lambda_e)\\
 &+\inf_s\left\{\sum_{e:u\to v}
       [\lambda_es_u+I_{\lambda_e,e^{s_v-s_u}}(0)]
                                      -\sum_a s_a\right\}.
 \end{split}                                                  \tag{17}
\]
Closing lengths contribute \(J(1)=0\). In particular the
prefactor in the first line of (17) is exactly the limiting magnitude
of the original clock factors; it is not omitted.

The inequality from left to right follows immediately from (16) and
(14). Equality holds also on tight faces, without claiming a finite
minimizing radius there. To see it, let \(D t\) be the incidence
imbalance in (14), and let \(F(t)=\sum_ev_{\lambda_e}(t_e)\).
The set
\(\{(Dt,z):0\le t\le\lambda,\ z\le F(t)\}\) is closed and
convex. Separate it from \((b,z_0)\), where \(b\) is the feasible
target in (14) and \(z_0>\max_{Dt=b}F(t)\). The coefficient of
\(z\) in a strict separating functional must be positive: it
cannot be negative because the set extends downward, and cannot be
zero because it contains a point with first coordinate \(b\).
Normalize that coefficient to one. The remaining coefficients give
an affine multiplier whose unconstrained maximum is less than
\(z_0\). Letting \(z_0\) decrease to the constrained maximum
proves the reverse inequality. Formula (16) evaluates that maximum
as the radial expression in (17). This argument handles loops,
forced endpoints, and degenerate lengths.

Thus the positive radial capacity, including the original clock
prefactor, has precisely the same limiting variational problem as
the incidence angles. These are two representations of the same
positive comparison, not independent optimizations whose values may
be combined arbitrarily.

## 5. A phase-sensitive upper bound for the complete original scalar

The original block gains have limits
\(w_e(\lambda)=\exp(i\omega_e(\lambda))\) as the normalized
clocks approach \(\lambda\). These follow from the explicit
integer-linear exponents in the charged bridge formula, including
the signs from \(x=-q^{-1}\). One may use their circle values;
no globally selected argument is required. Finite pivot shifts and
the \(-1\) in \(d=N-1\) remain in (9). Their limiting shifts
are obtained from those exact formulas, not reset independently.

For any fixed positive anchor radii define
\[
 \begin{split}
 \mathcal A(\lambda,r)={}&-\sum_eJ(\lambda_e)
       +\sum_{e:u\to v}\lambda_e\log r_u-\sum_a\log r_a\\
 &+\max_{\vartheta\in\mathbb T^k}
       \sum_{e:u\to v}I_{\lambda_e,r_v/r_u}
              (\omega_e(\lambda)+\vartheta_v-\vartheta_u).
 \end{split}                                                  \tag{18}
\]
The expression is invariant under a common scaling of all radii.
If \(c_\chi=\limsup_NN^{-1}\log|\chi_N|\) is finite, then
\[
 \boxed{\displaystyle
 \limsup_N\frac1N\log|K_N|
        \le c_\chi+\sup_{\lambda\in\mathcal L}
                                  \inf_{r_a>0}\mathcal A(\lambda,r).}
                                                               \tag{19}
\]
In the original framing conventions the external factor is retained
explicitly; its known subexponential size makes \(c_\chi=0\).

To prove (19), apply the original Cauchy coefficient integral at any
fixed radii in each clock sector. The uniform midpoint estimate in
[the block phase-loss theorem](research_charged_block_holonomy_rate_loss.md)
gives
\(\log|B_{L,N}(r e^{i\theta})|\le
 NI_{L/N,r}(\theta)+O(\log(N+1))\), including every zero.
The factorial estimate and (6) supply the first term of (18).
There are only polynomially many clocks for the fixed word. Along a
subsequence giving the largest nonzero sector rate, its feasible
normalized lengths have a convergent subsequence
\(\lambda_N\to\lambda\in\mathcal L\). For every fixed choice
of radii, the arc integrals are jointly continuous in their length
and center, uniformly on the center circle. This also holds at a
logarithmic zero, by integrability and translation continuity of the
logarithmic kernel. The sector rate is consequently at most
\(\mathcal A(\lambda,r)\) for every fixed \(r\). Taking the
infimum now proves (19). Neither a radius chosen uniformly for all
clock sectors nor an interchange of supremum and infimum is used.
If all sectors vanish the bound is immediate.

The maximum in (18) equals the centered positive arc sum minus the
exact graph arc-loss energy. Consequently the infimum of (18) over
radii is bounded by the positive capacity rate in (17), and can be
strictly smaller. The quantitative
cycle estimate in the block theorem gives an explicit loss when
the actual gains have incompatible phases on a regular cycle.
Boundary lengths and diverging optimal radii are included in (19);
they do not automatically give a uniform positive loss.

## 6. Which geometric equations have been obtained

There is a direct local volume interpretation on a smaller real
chamber. Order one overbridge row by its original blocks, taking
the tail incidence and then the head incidence of each block. If
every angle in that row satisfies \(0<x_i<1/2\), put equatorial
vertices on the unit circle with
successive arguments differing by \(2\pi x_i\), and use apices
\(0,\infty\) in the upper-half-space boundary. The convex ideal
bipyramid is subdivided by its axial edge into tetrahedra of shapes
\(e^{2\pi i x_i}\). Its volume is
\[
          \sum_i D(e^{2\pi i x_i})
                 =-2\pi\sum_iJ(x_i).                       \tag{20}
\]
The gaps less than \(\pi\) put the origin inside the equatorial
polygon, so these tetrahedra have disjoint interiors and positive
orientations. The row equation gives angle \(2\pi\) around the
internal axial edge. The outer equatorial edge in position \(i\)
has dihedral angle \(2\pi x_i\); the polar edge at the intervening
equatorial vertex has dihedral angle
\[
                         \pi(1-x_{i-1}-x_i).                \tag{21}
\]
This follows by adding the two neighboring tetrahedral angles
\(\pi/2-\pi x_{i-1}\) and \(\pi/2-\pi x_i\).

The anchor equations in (3) are therefore the correct numerical
equatorial angle sums if those incidences are realized by face
pairings. The charged coefficient metadata alone do not specify or
verify all such face pairings for the original knot exterior. In
particular a class \(C\) of glued polar edges must satisfy
\[
                 \sum_{(v,i)\in C}(1-x_{v,i-1}-x_{v,i})=2,
                                                               \tag{22}
\]
and the remaining shape and peripheral equations must be retained.
No assertion that (22) follows from (3) is made here. At a block's
internal pair of incidences the angle (21) depends only on its
length. Between blocks it depends on their separate endpoint
charges. Consequently the full clock-dependent phase (8), not only
fixed-clock graph holonomy, must enter a proposed gluing comparison.

Outside the chamber of (20), the algebraic entropy identity (11)
and all variational results remain valid. The axial subdivision
need no longer be a positive geometric subdivision. None of these
positive comparisons changes the phase or declares the original
cycle to pass through the absolute optimizer. The two-crossing
positive-chart obstruction is avoided in the exact bridge identity,
but is not resolved by assigning independent positive shapes to
the original crossings. A geometric identification of (18), and a
nonzero contribution to (9), remain separate tasks.

## Direct source versions

The direct source formulas used in this proof were read in these versions:

| Source | SHA-256 |
| --- | --- |
| actual_global_charged_bridge_flow.md | b444e487eab3ec0a56c40b22584837cefcbe374a137b0beeaa185116c2a81d8c |
| actual_length_gauge_clock_source.md | ccc3139960cf113f97e0454a902a11dfabca15ceb0b1e12f8175dc56a2be5315 |
| research_charged_block_holonomy_rate_loss.md | dfd2cae48cd534a12602670145ee09c3c959cf663e304e62896d4b47e1184b6e |
