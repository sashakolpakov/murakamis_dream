# Geometric integrality and constants of the all-circle source field

1 November 2026. Private proof.

This note proves the algebraic constants step in the proposed rigidity
argument. It does not assume that the geometric longitude has already
been identified with the source longitude. Boundary isotropy and
regularity of that geometric ratio are separate inputs.

## 1. The exact quadratic equations

Let \(T\) be a finite tree, with one independent variable \(Q_v\) at
each vertex and one variable \(E_e\) at each edge. The distinguished
main variable is \(M\). Work first over
\[
 k_0=\mathbb C(M),\qquad
 t=(M+M^{-1})^2,\qquad D=t-2.
 \tag{1}
\]
For an edge \(e=vw\), put
\[
 b_v=Q_v+Q_v^{-1},\quad
 S_e=b_v+b_w+t.
 \tag{2}
\]
The source edge equation is exactly
\[
 S_eE_e^2+(b_vb_w-2D)E_e+S_e=0.
 \tag{3}
\]
Indeed this is the Laurent source equation after dividing by \(E_e^2\)
and collecting \(E_e+E_e^{-1}\). At the complete germ
\(M=Q_v=1\), one has \(S_e=8\) and \(E_e=i\), so
inverting every \(S_e\) retains that germ.

The discriminant of (3) factors as
\[
 \begin{aligned}
 (b_vb_w-2D)^2-4S_e^2
 &=(b_v+2)(b_w+2)
       (b_vb_w-2b_v-2b_w-4D-4)\\
 &=\left(\frac{(Q_v+1)(Q_w+1)}{Q_vQ_w}\right)^2H_e,
 \end{aligned}
 \tag{4}
\]
where
\[
 H_e=(Q_v-1)^2(Q_w-1)^2-4tQ_vQ_w.
 \tag{5}
\]
Thus the full generic source field is the multiquadratic extension
\[
 L=k_0(Q_v:v\in V(T))(\sqrt{H_e}:e\in E(T)).
 \tag{6}
\]
The choice \(E_e=i\) selects a local analytic branch of this field.
It does not introduce an additional algebraic component.

## 2. Each edge discriminant is an irreducible prime

Let \(k\) be an algebraic closure of \(k_0\). Consider
\[
 H(X,Y)=(X-1)^2(Y-1)^2-4tXY
\]
as a quadratic in \(Y\) over \(k(X)\). Its discriminant is
\[
 16tX\bigl[X^2+(t-2)X+1\bigr].
 \tag{7}
\]
Its valuation at \(X=0\) is one: \(t\ne0\) and the bracket has
constant term one. A square rational function has even valuation at
every prime. Therefore (7) is not a square in \(k(X)\), and the
quadratic \(H(X,Y)\) is irreducible over \(k(X)\).

Its coefficients in \(k[X]\) are primitive. Any common divisor would
divide \((X-1)^2\), whereas the coefficient of \(Y\) takes the nonzero
value \(-4t\) at \(X=1\). Gauss's lemma now gives irreducibility in
\(k[X,Y]\). Adding independent variables preserves this prime, since
the quotient remains a polynomial ring over the domain
\(k[X,Y]/(H)\). Localizing all vertex variables also preserves it:
\(H\) does not divide a monomial.

Distinct edges of the tree have distinct unordered endpoint sets.
Their polynomials \(H_e\) are not associates. In the polynomial ring,
an associate differs by a scalar; \(H_e\) depends nontrivially on
exactly its two endpoint variables. After Laurent localization they
still cannot become associates, because neither irreducible polynomial
divides a monomial.

This argument in fact applies to every finite simple graph. The tree
hypothesis is required by the geometric source construction, not by
this squareclass calculation.

## 3. Independence of all squareclasses

For a subset \(J\) of the edges, the product
\(\prod_{e\in J}H_e\) has valuation one at the prime \(H_f\)
for each \(f\in J\). Hence no nonempty such product is a square in
\(k(Q_v:v\in V(T))\). The classes of the \(H_e\) are linearly
independent in the squareclass group.

For completeness, independent squareclasses imply the expected
multiquadratic degree. Suppose the preceding radicals give degree
\(2^r\). The sign changes of those radicals act independently, and
their simultaneous eigenspaces in the field are the one-dimensional
base-field spans of the radical monomials. If an element \(a\) of the
base field becomes a square, say \(z^2=a\), every sign change sends
\(z\) to \(z\) or \(-z\). Thus \(z\) lies in one of those
eigenspaces and \(a\) is a base-field square times a product of
the preceding radicands. Independence excludes this for the next
radicand. Induction proves
\[
 [k(Q_v)(\sqrt{H_e}:e\in E(T)):k(Q_v)]
                  =2^{|E(T)|}.
 \tag{8}
\]

Invert the \(Q_v\), the \(S_e\), and any further nonzero denominators
needed for the selected chart. The ring defined by (3) is finite free
of rank \(2^{|E(T)|}\) over the resulting vertex-variable ring,
with basis \(\prod_eE_e^{\epsilon_e}\), \(\epsilon_e\in\{0,1\}\).
Its localization at the base fraction field is the field in (8).
Consequently the original ring injects into that field and is a
domain. The same proof holds after extending \(k_0\) to \(k\).
The selected source chart is therefore geometrically integral over
\(k_0\).

This is a statement about the chart containing the complete branch,
with \(S_e\ne0\). Clearing denominators and then retaining every
component on the excluded locus would be a different assertion.

## 4. The relative constants field

Geometric integrality implies that \(k_0\) is algebraically closed
inside \(L\). An elementary verification is useful here. If
\(a\in L\) were algebraic of degree greater than one over \(k_0\),
its minimal polynomial would be separable in characteristic zero.
After extending to \(k\), the algebra \(k_0(a)\otimes_{k_0}k\)
would split as a product of at least two copies of \(k\). Its
injection into \(L\otimes_{k_0}k\) would give zero divisors,
contrary to geometric integrality.

Extend the usual derivations \(\partial/\partial Q_v\) uniquely
from \(k_0(Q_v)\) to \(L\); uniqueness and existence follow from
the finite separable extension. If \(R\in L\) satisfies
\[
       \frac{\partial R}{\partial Q_v}=0
                 \quad\text{for every }v,
 \tag{9}
\]
then \(dR=0\) in \(\Omega_{L/k_0}\). The differentials \(dQ_v\)
are a basis because \(L/k_0(Q_v)\) is finite separable.
In characteristic zero an element with zero relative differential is
algebraic over the base field: otherwise extend that element to a
transcendence basis, over which separability would make its
differential nonzero. The preceding paragraph therefore gives
\[
                         R\in\mathbb C(M).
 \tag{10}
\]
For nonzero \(R\), the hypotheses
\(\partial_{Q_v}\log R=0\) are equivalent to (9).

The conclusion also holds if (9) was first proved on the selected
analytic germ. A rational function vanishing there vanishes in \(L\):
the germ is a nonempty analytic open subset of the irreducible
algebraic chart, and hence is Zariski dense.

## 5. What the rigidity application still needs

Suppose a squared geometric/source longitude ratio is an element
\[
 R=\frac{L_{\mathrm{geom}}^2}
           {\prod_e f_e^2}\in L^\times,\qquad
 f_e=\frac{M^2-E_e}{1-M^2E_e}.
 \tag{11}
\]
If the actual marked boundary isotropy calculation supplies (9),
then (10) follows without a separate longitude-word factorization.
This note proves precisely that implication. The membership in
\(L\), the marked isotropy identity, and the choice of the main
eigenflag in (11) are not consequences of squareclass independence.

If, in addition, both \(R\) and \(R^{-1}\) have no pole at any
\(M_0\in\mathbb C^\times\), a rational-function divisor argument
gives
\[
                         R=cM^k,\qquad
              c\in\mathbb C^\times,\ k\in\mathbb Z.
 \tag{12}
\]
No poles for \(R\) alone would not suffice: its zeros must also
be excluded. Complete normalization \(R(1)=1\) fixes \(c=1\).
With the agreed longitude orientation, the already proved preferred
cusp identity then fixes \(k\). For example, if
\[
 \left.\frac{d\log L_{\mathrm{geom}}}{d\log M}\right|_{M=1}
   =a+2i\sum_e\cot(\pi x_e),
 \qquad E_e=e^{2\pi ix_e},
 \]
then \(\left.d\log f_e/d\log M\right|_{M=1}
=2i\cot(\pi x_e)\), including moving \(E_e\), since
\(f_e(1,E_e)=1\). Thus (11) gives \(k=2a\).
The negative complete lift would then choose
\(L_{\mathrm{geom}}=-M^a\prod_ef_e\) as a local germ.

## 6. Exceptional specialized fibers

The irreducibility proof works after specializing \(M=M_0\) whenever
\(t(M_0)\ne0\), including \(M_0=\pm1\). At \(M_0=\pm i\),
however, \(t=0\) and
\[
                   H_e=(Q_v-1)^2(Q_w-1)^2
 \tag{13}
\]
is a square. Those specialized fibers split. This does not affect the
generic constants theorem, but it prevents using generic-fiber
irreducibility to assert regularity at these two values.

A separate regularity argument may work on a component through a
generic \(Q\)-point there. It must exhibit a point where the actual
geometric ratio and its inverse are regular and nonzero. The present
proof neither supplies nor rules out that point.
