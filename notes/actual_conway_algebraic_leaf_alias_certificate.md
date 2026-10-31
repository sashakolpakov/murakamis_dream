# The exact alias-tangent threshold and a rational port certificate

31 October 2026. **analytic and original-source certificate.**
The exact algebraic port condition below gives a uniform mixed-source gap;
it is a sufficient condition on the actual complete optimizer, not an
automatic property of every two-leaf expression.
This enlarges the sufficient leaf interval in the existing whole
mixed-source Conway argument. It does not assert that every expression
using h^2 has the required strict geometry, finite lattice packet, or
passing leaf labels. Those source and geometric hypotheses are supplied separately by the
[two-leaf source interface](actual_conway_two_leaf_seed_source.md) and
[actual geometric interface](actual_conway_two_leaf_seed_geometry.md).

The actual functions are those of the
[full original mixed-source theorem](actual_odd_conway_uniform_mixed_source_gap.md):

\[
\begin{gathered}
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\\
 g(a)=J(2a)-4J(a),\quad 0\le a\le\tfrac12,\qquad
 k(u)=-2J(u/2),\quad 0\le u\le1.
\end{gathered}
\]

The coefficient bounds for the full original core and alias, including
Hermite/normal data and both parities, are retained from that source
theorem. Nothing below replaces them by a semisimple or nodal estimate.

## 1. Exact minimization of the leaf tangent deficit

For 1/4<=a<1/2, put s(a)=g'(a)=2log cot(pi a) and

\[
I(a)=\min_{0\le u\le1}\left[g(a)+s(a)(u-a)-k(u)\right].\tag{1}
\]

The exact derivatives are

\[
\begin{gathered}
 g''(a)=-\frac{4\pi}{\sin(2\pi a)}<0,\qquad
 k'(u)=-\log(2\sin(\pi u/2)),\\
 k''(u)=-\frac\pi2\cot(\pi u/2)<0\quad(0<u<1).
\end{gathered}\tag{2}
\]

Let a0=atan(sqrt(2))/pi. For a in [1/4,a0], the unique maximizer
of k(u)-s(a)u is

\[
u(a)=\frac2\pi\arcsin\frac{\tan^2(\pi a)}2.\tag{3}
\]

with u in [1/3,1]. At a=a0 it is the endpoint 1. On the strict
interior the envelope derivative is

\[
I'(a)=g''(a)(u(a)-a)<0.
\]

The continuous extension has the same monotonicity at both endpoints.
The already proved exact lower bound is

\[
I(a)\ge I(a_0)\ge c_0,\qquad
 c_0=\frac{2\operatorname{Catalan}}\pi-\frac34\log2
          >\frac{161}{3960}>0.\tag{4}
\]

For a>=a0, s(a)<=-log2. Since k' decreases to -log2, the function
s(a)u-k(u) is decreasing on [0,1], strictly except possibly at its
right endpoint. Thus its minimum is EXACTLY at u=1. Since k(1)=0,

\[
I(a)=H(a):=g(a)+(1-a)g'(a),\qquad a_0\le a<\tfrac12.\tag{5}
\]

In particular H'(a)=(1-a)g''(a)<0. No sampling of the alias range or
unknown optimizer is involved in (5).

## 2. The exact threshold exists and lies below one third

Introduce the real inverse-tangent integral

\[
\operatorname{Ti}_2(x)=\int_0^x\frac{\arctan t}{t}\,dt,\qquad x\ge0.
\]

If x=cot(pi a), integration from g(1/2)=0 gives

\[
\begin{aligned}
 g(a)&=-\frac2\pi\int_0^x\frac{\log t}{1+t^2}\,dt\\
 &=\frac2\pi\left[\operatorname{Ti}_2(x)-\arctan(x)\log x\right].
\end{aligned}
\]

Since 1-a=1/2+atan(x)/pi, this yields the exact simplification

\[
H(a)=\frac2\pi\operatorname{Ti}_2(x)+\log x,\qquad x=\cot(\pi a).\tag{6}
\]

At a0, H is strictly positive by (4). At a=1/3, x=1/sqrt(3),
and atan(t)<t gives Ti2(x)<x. Using pi>3 and log3>1,

\[
H(\tfrac13)<\frac{2}{3\sqrt3}-\frac12<0.\tag{7}
\]

For the elementary log inequality, exp(1)<3 follows directly by
bounding its factorial series. The last inequality in (7) follows
from 16<27. Strict decrease and continuity therefore prove a UNIQUE

\[
a_{\mathrm{crit}}\in(a_0,\tfrac13),\qquad H(a_{\mathrm{crit}})=0.\tag{8}
\]

For the whole interval 1/4<=a<1/2, the exact supporting-plane
condition I(a)>0 holds if and only if a<a_crit. At equality it has
zero margin; above it, the genuine alias endpoint u=1 lies above
the tangent. That is a failure of this sufficient tangent method,
not a lower bound for an actual mixed source or a volume obstruction.
No decimal approximation defines or proves (8).

## 3. A sharper reusable algebraic certificate: cot(pi a)>=2/3

Set

\[
a_* =\frac1\pi\arctan\frac32.
\]

It lies strictly above a0 because 3/2>sqrt(2). At x=2/3 the alternating
series for Ti2 is valid, with decreasing terms. Four terms give

\[
\operatorname{Ti}_2(\tfrac23)
  >\frac23-\frac{(2/3)^3}{9}+\frac{(2/3)^5}{25}-\frac{(2/3)^7}{49}
  =\frac{1708762}{2679075}.\tag{9}
\]

The positive series log((1+y)/(1-y))=2sum_(n>=0)y^(2n+1)/(2n+1)
at y=1/5, bounding all remaining denominators by 7, gives

\[
\begin{aligned}
 \log\frac32
 &\le2\left[\frac15+\frac{1}{3\cdot5^3}+\frac{1}{5\cdot5^5}
              +\frac{1}{7\cdot5^7(1-1/25)}\right]\\
 &=\frac{177391}{437500}.
\end{aligned}\tag{10}
\]

Since pi<22/7, equations (6),(9),(10) imply the exact rational margin

\[
H(a_*)>\frac7{11}\frac{1708762}{2679075}-\frac{177391}{437500}
 =\frac{57269}{136687500}>\frac1{2500}.\tag{11}
\]

Every inequality here is analytic or rational arithmetic; no
asymptotic computation or numerical sign test is used. Combining
(4), strict decrease in (5), and (11) proves

\[
\begin{gathered}
 k(u)\le g(a)+g'(a)(u-a)-\frac1{2500},\\
 0\le u\le1,\qquad \frac14\le a\le a_*.
\end{gathered}\tag{12}
\]

It also sharpens the exact bracket to

\[
\frac1\pi\arctan\frac32<a_{\mathrm{crit}}<\frac13.
\]

The certificate (12) is algebraic in the positive actual port variable:

\[
X=\cot(\pi a)\ge\frac23
   \quad\Longleftrightarrow\quad 9X^2\ge4.\tag{13}
\]

The positivity of X and the retained a>=1/4 hypothesis matter in the
equivalence and source application. No claim is made that the true
transcendental threshold itself is an algebraic port condition.

For comparison, the simpler bound X>=7/10 also follows
without the Ti2 series. For a0<=a<=atan(10/7)/pi, concavity gives
g(a)>=g(a0)+g'(a)(a-a0). Hence

\[
\begin{aligned}
 H(a)&\ge c_0+(1-a_0)[g'(a)+\log2]\\
 &>\frac{161}{3960}-\log\frac{50}{49}
 >\frac{161}{3960}-\frac1{49}=\frac{3929}{194040}>0.
\end{aligned}
\]

The cutoff (13) admits the larger interval and will suffice below.

## 4. Exact conditional mixed-source transfer

Consider a FIXED actual Conway source made from the original leaves
T(R^epsilon L_j), actual Newton products and literal turns, with the
original final cylindrical closure. Suppose its complete pure source
has a unique strict optimizer, every unforced gate is strict, and every
actual complete leaf label satisfies

\[
\frac14<a_\ell<a_{\mathrm{crit}}.\tag{14}
\]

Retain all finite source, strict lattice, nonzero complete packet and
geometric assumptions required by the existing assembly. The present
statement supplies the mixed-source inequality; it does not reprove
those other assumptions for a new grammar.

For a finite set of leaves define c=min_l I(a_l)>0. The original
all-color core has uniform upper rate

\[
\widetilde g(u)=g(\max(u,\tfrac14)),\qquad 0\le u\le\tfrac12.
\]

This function is concave: it is constant up to 1/4, its right derivative
there is zero, and it is strictly concave thereafter. Thus, for every
leaf in (14),

\[
\widetilde g(u)\le g(a_\ell)+g'(a_\ell)(u-a_\ell).\tag{15}
\]

with equality only at u=a_l. Its pure-core counterpart obeys the same
upper bound. For an alias, (1) gives on its ENTIRE physical range

\[
k(u)\le g(a_\ell)+g'(a_\ell)(u-a_\ell)-I(a_\ell),
       \qquad0\le u\le1.\tag{16}
\]

The exact original multiplication action remains concave on
max(x,y)<=z<=x+y<=1. Add its supporting planes at the SAME complete
state to (15),(16). All linear terms cancel under the original affine
turn and closure equations by complete-source stationarity. For any
nonempty alias subset S the resulting rate is at most

\[
F_0-\sum_{\ell\in S}I(a_\ell)\le F_0-c.\tag{17}
\]

This argument uses neither a vanishing product of aliases after turns
nor covariance of a projected coupon. It keeps the full original
Hermite/normal terms in the known source bounds. At finite level the
actual wire affine right sides are 1-1/N. Fixed tangent slopes therefore
cost only O(1) in the exponent, while endpoint-uniform factorial and
transport errors are o(N). The fixed circuit has polynomially many
wire states and finitely many alias subsets. Reducing c if necessary
gives the whole mixed-source radical gap uniformly over all physical
auxiliary colors, both parities and composite levels.

The physical-color complement argument also transfers. The concave
all-core majorant is bounded above by the sum of the same supporting
planes. Equality forces every leaf to equal its original a_l by (15)
and every retained strict gate to equal its original state. It therefore
has the same unique maximum. Compactness gives a gap outside a fixed
complete-state neighborhood. Inside that neighborhood, choose beta<1/2
larger than every leaf label; the existing uniform far-color core loss
applies with unchanged terminal source and recurrence branches.
Combining it with (17) gives the existing complete-color corridor gap.

If every leaf obeys the algebraic condition (13), one can take the
uniform tangent margin 1/2500 in this argument. Under merely (14) the
positive margin depends on the fixed actual optimizer, as permitted by
the original fixed-expression quantifiers.

This is a CLOSED-source argument. It does not assert an open,
coefficientwise error comparison for an h^2 seed at every prescribed
output, and does not fill a missing finite top coefficient by changing
the exact source lattice.

## 5. Interface with h^2 and other actual seeds

The existing complete port formulas for A_s=h^s are

\[
X=\cot(\pi a),\qquad B_s=\frac{T_s(X)}{U_{s-1}(X)},\qquad
 Y_s=\frac1{U_{s-1}(X)}.
\]

Whenever the independently checked closed strict geometry gives the
proper-seed inequalities, s>=3 already forces X>1/sqrt(2)>2/3. Thus
all old admissible seeds retain the new certificate automatically.
For a proper h^2 seed the known port relation is Y_2=1/(2X). The new
test becomes X>=2/3, equivalently Y_2<=3/4, in addition to the actual
strict source/geometric hypotheses. The weaker proper h^2 inequality
X>1/2 by itself does NOT imply (13) or (14).

Thus a fixed mixed grammar with h^2 seeds can inherit the old
mixed-source proof by checking the algebraic inequality (13) at its
actual selected complete gluing branch, provided its other source,
packet and geometric interfaces have been proved independently. This
does not cover all h^2 expressions.

When those separately proved packet and actual marked-geometry hypotheses
hold, the [original-source long-filling transfer](general_original_source_long_filling_transfer.md)
applies with all its original scalar, Cartan, phase and peripheral
normalizations. Fix the expression and its retained half-twist signs,
then fix independently sufficiently long signed integral full-twist
fillings. The threshold may depend on this fixed datum. If the chosen
main-component parity gives a knot and ALL auxiliary circles are filled,
the conclusion is the actual **knot complement volume**:

\[
\lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
   =\operatorname{Vol}(S^3\setminus K).
\]

The limit retains both parities and composite levels. With some auxiliary
circles unfilled, the corresponding conclusion concerns the actual
remaining cusped link complement. This conditional transfer does not
assert that every two-leaf expression passes (13) or (14), and does not
replace the original signed knot by a different diagonal or pure partner.

## Dependencies

- [Whole original mixed-source gap](actual_odd_conway_uniform_mixed_source_gap.md)
- [Full Newton transport and normal terms](actual_odd_conway_newton_transport.md)
- [Uniform all-color core envelope](actual_pretzel_global_core_spectral_gap.md)
- [Actual seed port formulas](actual_conway_arbitrary_width_seeds.md)

No numerical asymptotic audit is used as proof. Native MathML and
AST dependency checks validate the document rather than its conclusions.
