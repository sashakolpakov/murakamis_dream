# A projective monic certificate for repeated-turn principal rows

Private written proof, 16 November 2026.

For the full repeated-turn tensor presentation, the possible interior
physical colors over shift infinity lie in an explicit finite union
of resonant cosine grids. Away from this set, a monic polynomial
belongs to the maximal-minor ideal of the full principal matrix.
Its row certificate lifts to an exact quantum block equation with
an \(O(1/N)\) remainder of fixed, possibly higher, shift order.

This controls the leading coefficient needed by the buffered
slow/fast estimate. It does not give a regular companion for every
formal quantum solution, propagate the source across the exceptional
colors, or compare the resulting envelope with a geometric action.
The exceptions below are physical colors, not filling assignments.

## 1. Source, presentation and exceptional colors

Retain the actual column and ordered rows of the full-step interface:
\[
 Y_N=U_\tau\operatorname{can}
       \left(Q_{\rm base}\prod_{i=1}^bV_{n_i}Q_i\right),\qquad
 Q_i=\operatorname{can}\prod_{\ell=1}^{r_i}
       K_N(2\cosh(\alpha_{i\ell}/N),C).
 \tag{1}
\]
All retained \(n_i\ne0\), \(r_i\ge1\), and all counts are fixed.
The outer power is \(\tau\in\{1,-1\}\).
The desired scalar is a component of the full actual column
\(\mathcal Y_N=U_\tau Z_N\). No component, shared parameter or
first-normal source condition is removed.

Put \(h=1/N\), \(q=e^{\pi ih}\), \(v+v^{-1}=C\), and
\(E f(v)=f(q^2v)\). After the specified polynomial coefficient
clearings, the exact finite matrix of physical full-step rows is
\[
                       \mathcal R_h(v,E)\mathcal Y_N=0.
 \tag{2}
\]
Let \(\mathcal R_0(v,t)\) be its commuting specialization.
Use the natural clearings in the pinned input constructions:
products of the displayed coefficient denominators, shift extremes
and their reflected factors. Multiplying by additional arbitrary
factors is unnecessary here. Scalar removable powers of \(h\)
are treated as in the regular-arc note.

For a nonempty subset \(S\subset\{1,\ldots,b\}\), define
\[
       \gamma_S=\sum_{i\in S}\frac1{n_i},\qquad
       L_S=\operatorname{lcm}_{i\in S}|n_i|.
 \tag{3}
\]
The finite set of possible interior exceptional colors is
\[
 \mathcal E_\tau=
 \bigcup_{\substack{S\ne\varnothing\\\gamma_S=-\tau}}
       \left\{\,2\cos(2\pi k/L_S):
                         k\in\mathbb Z,\ 0<k<L_S/2\,\right\}.
 \tag{4}
\]
Empty sets in this union contribute nothing; in particular
\(L_S\le2\) contributes no interior color.

Here the sign is the actual point-transport sign. Operator
conjugation substitutes \(\mathcal A_\tau\) in old equations,
so the new characteristic point is \(\mathcal A_{-\tau}\)
of the old point. This is the convention of the pinned
projective-resonance theorem.

## 2. Full principal support, including the extra channels

**Lemma 1.** Away from finite old-color clearing divisors,
the reduced support of the full principal row presentation
is contained in the union of the active terminal products:
each transformed factor contributes either its signed terminal
component \(x_{n_i}=2\) or the source shift \(1\), and the
unturned base contributes only shift \(1\).
All nilpotent multiplicities remain in the presentation.
The natural limiting clearing divisors have old color
\(C=2\) or \(C=-2\); allowing additional finite old-color
divisors would not affect the conclusion below.

**Proof.**
For factor \(i\), use \(k_i=33r_i\), \(m_i=|n_i|\) and
the actual raw companion column from the interface. Its
principal gauged equation and forced recovery are
\[
     (x_{n_i}-2)^{k_i}(y-2)W_i=0,\qquad
     (x_{n_i}-2)^{r_i}Y_i=(W_i)_* .
 \tag{5}
\]
Thus its full companion determinant has only the roots
\(x_{n_i}=2\) and \(y=2\), with their original powers.
Equivalently its characteristic polynomial is, up to its
nonzero extreme scalar and a Laurent monomial,
\[
       \big[(x_{n_i}-2)^{k_i}(y-2)\big]^{6^{r_i}}
                           (x_{n_i}-2)^{r_i}.
 \tag{6}
\]
This follows from the block triangular gauged/recovery
equations, not from a reduction of their Jordan blocks.
The principal rational forward and backward matrices are inverses
on this generic chart: they solve the two extremes of the
same finite system, with the same recovery row.

For the unturned six-channel factor, the ordinary half-step
state is
\((f,\mathcal Df,\mathcal Sf,\mathcal S\mathcal Df,P_N,1)\).
The explicit module formulas have finite limits off \(C=2\).
At \(q=1\), their half-step matrix is the involution
\[
                (f,d,a,b,p,1)\longmapsto(a,b,f,d,4-p,1).
 \tag{7}
\]
Indeed \(U_1,U_2\to0\), while the removable parameter
ratios and the divided-difference matrix stay finite.
The \(s(v-v^{-1})\mathcal D/2\) part of a half step tends
to zero. Squaring the half step therefore gives the
identity. Tensoring base factors changes no principal
full-step eigenvalue. This checks the ordinary \(P_N\)
alias before reduction; it is not obtained by setting that
source channel to zero prematurely.

At a generic old color, the full-step tensor spectrum
consists of products of the individual eigenvalues.
This statement is valid for arbitrary Jordan multiplicities:
triangularize each finite matrix over an algebraic closure,
then tensor the triangular matrices. The equation \(y=2\)
has reduced physical shift \(1\). Hence the possible
reduced products are precisely of the indicated active-subset
form, with any coincidences retained.

The even/odd descent is an invertible change of fields on
the generic angular chart. Its mean and divided-difference
equations recover both full steps. In the principal variables
their equivalent forward rows are
\[
 t(F+WG)=M_+(F+WG),\qquad
 t(F-WG)=(\iota M_-)(F-WG),
 \tag{7a}
\]
with the backward rows obtained by inversion. Here
\(W=v-v^{-1}\ne0\), and \(\iota\) acts on coefficient \(v\).
The reflected column
uses \(v\mapsto v^{-1}\) and the reciprocal step, which
describe the same spectral correspondence. Thus this
descent adds no new generic reduced support.

Finally the coefficient denominators of the ordinary module
have limit powers of \(C-2\). The transformed companion
extremes in the pinned product proof have nonzero generic
limits; their coefficient poles and zeros come from the
physical \(A,B\) factors and the finite shifted endpoint
factors. Their limits lie at \(C=\pm2\).
The additional descent factors \(W_+W_-\) tend to \(C^2-4\),
and the polynomial conversion contributes \(C-2\).
All these factors are independent of the microscopic
parameters. Clearing them can enlarge the principal support
on these finite old-color divisors, which are retained here.
\(\square\)

Consider the maximal-minor ideal of the full principal matrix
on the new angular chart. Its zero set is the rank-drop support
of that presentation. It may contain additional solutions at
the clearing divisors; it is not declared to be a minimal
source ideal.

**Lemma 2.** The closure of this support in the new shift
projective line has no point with \(t=0\) or \(t=\infty\)
over
\[
                         C_{\rm new}\in(-2,2)\setminus\mathcal E_\tau.
 \tag{8}
\]
The same exclusion holds in a sufficiently small complex
neighborhood of any compact interval in (8).

**Proof.**
For fixed interior new color, the physical symbols of
\(D_\tau\) have nonzero coefficients at both extreme
shifts. More explicitly, with \(v+v^{-1}=C_{\rm new}\),
\[
 D_\tau=b(C_{\rm new})
       -g(C_{\rm new})(v^{-\tau}t+v^\tau t^{-1}),\qquad
 g(C)=\frac{C-2}{C+2},\quad b(C)=\frac8{C+2}.
 \tag{9}
\]
Thus \(t\to0\) or \(t\to\infty\), while the new color
stays in a compact interior set, forces
\[
                          C_{\rm old}=D_\tau\longrightarrow\infty.
 \tag{10}
\]
A component supported at a finite old clearing color
therefore cannot give such a point.
The additional coefficient clearing in the new physical
operator chart has limiting zeros only at \(C_{\rm new}=\pm2\),
which are already outside the interval in (8).

On all other components Lemma 1 applies. An algebraic
branch tending to the projective boundary consequently
belongs to one of its active terminal products. For an
empty active set the old product shift is \(1\), with
reciprocal exponent zero, so it cannot have finite new
color under a unit turn. For a nonempty set \(S\), the
pinned Puiseux theorem gives a finite new color only if
\(\gamma_S=-\tau\), and then that color is
\(2\cos(2\pi k/L_S)\). Its interior values are exactly
the members contributed to (4). This proves (8).

The argument concerns support, so nilpotents do not alter
the exclusion. It applies to the relative closure of the
whole principal presentation, not merely to a generic gcd
specialization. Lemma 1 also holds with the microscopic
parameters retained: the companion roots in (6), the base
identity and the limiting clearing colors are independent
of those parameters. Thus parameter specialization cannot
create a different boundary color in this argument.
The finite boundary set (4), together with \(C=\pm2\),
can be avoided by a complex neighborhood of a compact
interval in (8). \(\square\)

No assertion is made that every color in (4) occurs in
every principal row presentation, or on a source with a
nonzero coefficient. The set is a sufficient exception set
for the full presentation.

## 3. A monic polynomial inside the full maximal-minor ideal

The algebraic construction is useful because it uses the
whole ideal, rather than dividing a generic gcd by factors
which vanish at special colors.

Let \(I\) be the maximal-minor ideal of \(\mathcal R_0\).
Coefficients are rational in the color variable and
holomorphic in a local microscopic-parameter chart.
Laurent shifts are allowed. To discuss \(t=\infty\),
multiply an individual member by a power of \(t\) to
make it a polynomial and homogenize in \(t\). This does
not change its leading coefficient or its value at infinity.
Use the homogenizations of all members of \(I\), equivalently
the relative projective closure ideal.

At a base point with no point of this closure over infinity,
the leading coefficients of the members of \(I\) generate
the unit ideal in the local coefficient ring. Here is the
direct reason. At the projective point \([t:1]=[1:0]\),
the homogenization of a polynomial evaluates to its
leading coefficient. If every such coefficient vanished
at the base point, all the homogenizations would vanish
there, producing precisely the excluded point. Thus a
finite combination has unit leading coefficient locally.
This argument uses the family ideal, not the ideal of one
specialized fiber.

For clarity, the following also gives a single certificate
over a compact arc. Fix a parameter value and a compact
angular arc above an interval in (8). Choose finitely many
members \(p_i(v,t)\in I\) whose leading coefficients
\(a_i(v)\) have no common zero on the arc. Clear their
coefficient denominators, keeping them nonzero at the
points where they were chosen. Shrink to one common
parameter neighborhood. With its center denoted by
\(\alpha^0\), set
\[
 a_i^\sharp(v)=
       \overline{a_i(1/\bar v,\alpha^0)},\qquad
 L(v,\alpha)=\sum_i a_i^\sharp(v)a_i(v,\alpha).
 \tag{11}
\]
On the unit arc at \(\alpha=\alpha^0\), this is
\(\sum_i|a_i(v,\alpha^0)|^2>0\).
It remains a holomorphic unit on a smaller complex arc
neighborhood and parameter neighborhood.

Let \(D\) be at least all the shift degrees \(d_i\).
Then
\[
              P(v,t)=\sum_i a_i^\sharp(v)t^{D-d_i}p_i(v,t)
                              \in I,\qquad
              p(v,t)=P(v,t)/L(v,\alpha)
 \tag{12}
\]
is monic of degree \(D\) on this chart. Membership of
\(P\) in the full ideal retains all nilpotent multiplicities
needed by that presentation; no radical quotient was used.
The division by \(L\) is only a coefficient-chart division
by a unit. Globally the equation keeps the factor \(L\).

Every \(p_i\) has a finite maximal-minor expression
\[
                     p_i=\sum_\nu b_{i\nu}(v,t)\det M_\nu(v,t).
 \tag{13}
\]
Together with the ordinary adjugates of the square row
minors \(M_\nu\), this is an explicit row certificate for
\(pI_d\), where \(d\) is the number of source columns.
This is a finite algebraic procedure: a projective ideal
or elimination computation can produce the \(p_i\);
no source solution is used to choose them.

The statement of membership is stronger than vanishing
on the reduced support. A polynomial chosen only from
the radical would need a proved power in \(I\) before
this row certificate could be used.

## 4. Exact quantum lift and the resulting local bound

Lift (12)--(13) with all coefficients on the left and
multiply the actual row equations (2). The regular-arc
adjugate argument gives exactly, on the coefficient chart,
\[
                        \{p(v,E)I_d+hK_h(v,E)\}\mathcal Y_N=0.
 \tag{14}
\]
The remainder is holomorphic at \(h=0\), has fixed finite
shift order, and retains every original channel.
After multiplying all coefficient denominators back,
(14) is a global quotient identity. Its ordinary residual
and first physical derivative vanish at the grid. Exterior
parameter derivatives are retained as well.

The monicity in (12) concerns the highest surviving
classical order. It does not assert that the higher shift
coefficients of \(hK_h\) vanish. In particular it does not
construct a uniformly bounded forward companion for all
formal solutions of (14).

Apply a fixed left shift to remove negative quantum powers,
and, as in the pinned regular-arc theorem, include the
explicit factor \(E-1\). This adds only possible zero roots and a
unit root to the classical envelope. The highest classical
coefficient remains a unit on the entire chosen chart.
Let \(\rho_p(u)\ge1\) be the maximal modulus of the resulting
finite roots at \(v=e^{2\pi iu}\).
Write
\[
        y_N(u)=\mathcal Y_N(2\cos(2\pi u+\pi/N))
\]
for the actual angular source column.

**Theorem 3.** Fix a compact physical interval
\(J\Subset(-2,2)\setminus\mathcal E_\tau\), and use its
corresponding angular interval inside \(0<u<1/2\).
Near any fixed microscopic parameter value, the construction
above gives a fixed finite exact block equation (14) with
unit highest classical coefficient throughout that interval.
For \(a<t<b\) in its angular interior, the actual source and
first normal satisfy
\[
 \limsup_N\frac1N\log\big(\|y_N(t_N)\|+\|y_N'(t_N)\|\big)
       \le A_a+\int_a^t\log\rho_p(u)\,du ,
 \tag{15}
\]
where \(A_a\) is the actual macroscopic initial-packet budget
of the pinned regular-arc theorem. Parameters may range
over a compact subset of the resulting parameter chart.

**Proof.**
Lemmas 1--2 and the monic ideal construction provide (14)
with the stated coefficient unit. The regular-arc theorem
applies without another exceptional color inside this chart.
It retains the exact first-normal triangular block, all
higher-order small terms, and all terminal defect data.
The actual \(\exp(CN)\) ceiling suppresses those data
superexponentially across the fixed right buffer \(b-t\).
Its conclusion is (15). \(\square\)

The constructed polynomial can have additional finite roots
beyond the principal support. Its degree and envelope are
explicit once a row certificate is fixed. Monicity alone
does not make that envelope the geometric one.

## 5. Exceptional colors and the original physical grid

The colors in (4) cannot be dismissed as points that never
meet the finite grid. Write an interior phase in lowest terms
as \(a/b\), with \(0<a<b/2\), \(\gcd(a,b)=1\). Its color is
\(2\cos(2\pi a/b)\). The original distinct physical colors are
\[
                  c_j=2\cos((2j+1)\pi/N).
 \tag{16}
\]
Equality of these interior colors is equivalent to
\[
                         (2j+1)b=2aN.
 \tag{17}
\]
If \(b\) is even, then \(a\) is odd, and equality occurs at
every level
\[
             N=(b/2)(2\ell+1),\qquad
             j=(a(2\ell+1)-1)/2
 \tag{18}
\]
for sufficiently large \(\ell\). These are valid physical
indices. If \(b\) is odd, the left side of (17) is odd and
the right side even, so equality never occurs. Nonetheless
the nearest physical angle is within \(\pi/N\). Moreover
the integer numerator in its angular difference has modulus
at least one, giving the lower bound \(\pi/(bN)\).
For this fixed interior color, angular and spectral distances
are comparable. Thus in the odd-denominator case the closest
physical colors remain at distance of order \(1/N\), not at
a fixed distance.

Here the denominator is the reduced phase denominator \(b\),
not necessarily the larger \(L_S\).

Neither case supplies a permissible deletion or a free contour
bypass. The current result leaves propagation through these
colors, endpoint initialization, and the relation of the
finite-root envelope to the retained geometric action open.
It also gives no lower source coefficient or finite list of
exceptional filling assignments.

## 6. Direct sources and coverage

The generic adjugate and buffered comparison are already in
the regular-arc note. The new statements are the full support
audit, its explicit physical exception set, and a monic
certificate in the full maximal-minor ideal on its complement.

Direct source pins and complete readbacks are recorded below:

* [Full-step repeated-turn interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  exact source columns, clearings, even/odd descent and turn convention.
* [Divided-difference endpoint-product module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  six-channel half-step matrices and their explicit coefficient divisors.
* [Turned-product characteristic upper bound](research_turned_endpoint_product_characteristic_upper_bound.md),
  SHA256 5e594fa40c1ab70b72a0c1b85748182e33850675a45ed6ea42f2c20349831b2a:
  exact companion extremes, gauged/recovery blocks and source-normal scope.
* [Terminal-product projective resonance](research_terminal_product_projective_resonance.md),
  SHA256 a648b644c5506e539d14fa715d61a3f680d7d53e48eec8efc1358b6ca047bf08:
  all signed active products, finite infinity limits and original nilpotents.
* [Repeated-turn regular-arc source bound](research_repeated_turn_regular_arc_source_bound.md),
  SHA256 20484b56147b684e400a107034c8ff14b9309948a85e0e317307189df85dd945:
  exact adjugate lift, actual exponential ceiling and buffered normal estimate.

Only written mathematics and source-text/hash reads are used;
no mathematical program, test, numerical experiment or compilation
is used. Adopted notes and public manuscripts are unchanged.
