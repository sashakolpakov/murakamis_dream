# Adequacy excludes a fixed algebraic meridian period

Research note, 26 October 2026. There is a uniform consequence of
alternatingness relevant to the torsor problem: the actual color
periods cannot be the traces of a fixed algebraic function of q and
M. This does not exclude an algebraic period torsor with transcendental
horizontal sections, or level-dependent algebraic root sections.
It excludes a proposed finite algebraic section before one attempts
to identify its norm with volume.

The C_j(q) and meridian convention M=-q^j are those independently
fixed in [the ADO pointing note](kashaev_ado_pointing.md). No Jones
asymptotic is used. The result concerns exact degree spans.

## 1. An elementary bound for any fixed algebraic trace

Suppose, for all sufficiently large positive integers j, C_j(q)
satisfies a fixed nonzero relation

    F(q,-q^j,C_j(q))=0,
    F(q,M,Y)=sum_i f_i(q,M)Y^i,
    f_i in C[q^(+/-1),M^(+/-1)].                    (1.1)

Collect coefficients first and discard zero f_i. For large j every
remaining f_i(q,-q^j) is nonzero: a collision of its q-exponents
a+bj requires j=(a'-a)/(b-b'), leaving only finitely many exceptional
positive j. All its q-exponents have absolute value at most A+Bj,
for fixed A,B depending only on F.

Let d_j be the largest q-exponent of the nonzero Laurent polynomial
C_j. In (1.1), the largest exponent among

    deg_q f_i(q,-q^j)+i*d_j

must occur at least twice. Otherwise its nonzero leading coefficient
cannot cancel. Thus for two distinct indices i,k,

    d_j=(deg_q f_k(q,-q^j)-deg_q f_i(q,-q^j))/(i-k).

It follows that |d_j|<=2(A+Bj). Applying the same argument to the
least exponents bounds the smallest exponent as well. Hence

    span_q C_j=O(j).                                (1.2)

This applies even if a different algebraic branch is selected for
each j: the fixed polynomial relation is all that was used. A
single overall framing monomial, even one with exponent quadratic
in j, does not change the span and cannot evade the conclusion.

The rational-function case is simpler. If C_j=p(q,-q^j)/r(q,-q^j)
is Laurent polynomial, span(C_j)=span(p_j)-span(r_j)<=span(p_j)=O(j).
Finite algebraic covers require the valuation argument above.

## 2. Exact extreme degrees for an adequate diagram

We give the diagram proof rather than importing a degree theorem.
Use the Kauffman bracket with empty value one, loop value

    delta=-A^2-A^(-2),

and crossing expansion A times its A-smoothing plus A^(-1) times
its B-smoothing. Let D be a connected knot diagram with c crossings.
Let v_A,v_B be the circle counts in its all-A and all-B states.
D is A-adequate if changing one crossing of the all-A state merges
two distinct state circles; define B-adequacy analogously.

For an A-adequate diagram, the all-A summand has top degree

    c+2v_A,

with coefficient (-1)^v_A. Every other state has degree at least
four lower: if k>=1 crossings are changed, the first change loses
one circle and each later change adds at most one. Its circle
count is at most v_A+k-2, so its top degree is at most
c-2k+2(v_A+k-2)=c+2v_A-4. Thus the top coefficient cannot cancel.
The all-B argument similarly gives bottom degree -c-2v_B.

Let D^(n) be the n-parallel blackboard cable. Its crossing count
is c*n^2, and its all-A and all-B circle counts are n*v_A,n*v_B.
To see this directly, follow the arcs through the n by n crossing
tile after uniform smoothing: it becomes n parallel copies of
the original smoothing and creates no internal circle. A single
changed cable crossing joins parallel copies belonging to distinct
original state circles. Thus cabling preserves each adequacy
condition. Consequently

    maxdeg_A <D^(n)>=c*n^2+2n*v_A,
    mindeg_A <D^(n)>=-c*n^2-2n*v_B.                  (2.1)

## 3. Passing from parallel strands to the actual color

The j-dimensional color, n=j-1, is the Chebyshev threading

    S_0(X)=1, S_1(X)=X,
    S_(n+1)(X)=X*S_n(X)-S_(n-1)(X).                 (3.1)

Thus S_n(D)=D^(n) plus a linear combination of cables D^(n-2r),
r>=1. Both extreme degrees in (2.1) strictly move outward with n.
The lower cables cannot cancel either extreme of the leading cable.

For completeness, the color convention in (3.1) agrees, up to an
overall color sign and framing monomial, with the fixed highest-weight
periods. At generic q and n>=1 the tensor product of
the fundamental module V_1 with V_n decomposes as

    V_1 tensor V_n = V_(n+1) direct-sum V_(n-1).

With Delta(E)=E tensor K+1 tensor E, highest vectors are
v_+ tensor w_0 and [n]_q*v_- tensor w_0-q^n*v_+ tensor w_1.
Successive F-actions give dimensions n+2 and n; the usual
E F^r highest-vector formula shows that these submodules are
disjoint and exhaust the tensor product. Naturality of the finite
R-matrix and additivity of the pivotal trace then give (3.1).
This is the representation-ring calculation behind threading,
not an additional asymptotic comparison theorem.

The fundamental checked R-matrix has eigenvalues q^(1/2) and
-q^(-3/2). Writing it as A*I+A^(-1)*e with A=q^(1/2)
gives e^2=(-A^2-A^(-2))*e. This is the local bracket relation.
An overall mirror convention changes exponent signs, and the
zero-framing correction is a monomial; neither changes the span.

The unreduced colored bracket therefore has A-span

    2c*n^2+2n*(v_A+v_B).

The unknot color S_n(delta) has A-span 4n. Dividing by this quantum
dimension gives the reduced period C_j. Spans add under products
of nonzero Laurent polynomials. Since q=A^2, we obtain

    span_q C_j=c*(j-1)^2+(v_A+v_B-2)*(j-1).         (3.2)

In particular every nontrivial adequate diagram gives genuinely
quadratic growth, independently of its framing.

For a connected reduced alternating diagram, its two state graphs
are the checkerboard plane graph and its dual. A loop in either
would be a nugatory crossing, so both adequacy conditions hold.
Euler's formula gives v_A+v_B=c+2. Hence

    span_q C_j=c*j*(j-1).                           (3.3)

Here c is the crossing count of that diagram; no crossing-minimality
theorem is required for the argument.

## 4. Consequence for the period torsor

Equations (1.2) and (3.2) contradict each other for every nontrivial
adequate knot. Therefore there is no fixed finite algebraic meridian
section whose traces at M=-q^j equal all the actual C_j(q), even
allowing arbitrary algebraic branches in those specializations.
This applies in particular to the entire class of hyperbolic
alternating knots considered by the user. A large degree span supplies
no lower bound at a particular root of unity; it does not exclude
cancellation in the volume evaluation.

This conclusion is compatible with a period of an algebraic
connection or difference module. The underlying equations or
torsor can be algebraic while its selected horizontal section is
transcendental. It is also compatible with rational sections at
each individual root level: their degrees or algebraic complexity
can grow with that level. It is the fixed finite algebraic
presentation in (1.1) that fails.

The [affine extension construction](affine_quantum_a_period.md)
uses this to rule out a split source extension whenever its
geometric block has either stated nonresonance property. It does
not yet identify that nonsplit class with the Bloch regulator or
establish its archimedean norm growth.

## 5. The perturbative coefficients are polynomial in the color

A second elementary fact is useful for the extension test. For
every knot, with q=exp(h),

    C_j(exp(h))=sum_(k>=0) p_k(j)h^k, p_k in C[j].   (5.1)

Only polynomiality is asserted; no diagonal summation, Alexander
identity, convergence uniform in j, or large-color limit is used.

Here is a direct proof from the cut braid. Write each checked
crossing as its permutation times R or R^(-1). At each fixed
h-order the unpermuted factors have finite expansions in tensor
products of words in E,F,H: the r-th nilpotent R-term has factor
(q-q^(-1))^r/[r]_q! of order h^r, the Cartan factor is exp(h H
tensor H/2), and the pivotal factors are exp(h H). Negative
crossings are formal inverses with the same finiteness property.
Move the permutations to one end. Each coefficient is then a
finite sum of a single permutation times such tensor words.

The braid closure has one component, so that permutation is a
single cycle. Its cut partial trace is the ordered product of the
tensor words around this cycle; it creates no separate trace
loop or color-dependent dimension factor. This identity follows
by identifying the intermediate matrix indices along the cycle.

At fixed h-order, reorder each product into PBW form F^a H^b E^c.
The relation
[E,F]=(exp(hH)-exp(-hH))/(exp(h)-exp(-h)) has polynomial
coefficients in H at each h-order, so the reordering is finite.
On the highest vector of color j, E kills it and F lowers its
weight. Its highest component consequently evaluates the a=c=0
terms at H=j-1. It is polynomial in j. The zero-framing correction
is the exponential of h times a polynomial in j and preserves
this property. This proves (5.1) for the actual reduced cut period.

This is the elementary polynomiality part of existing perturbative
color theory; see the scope of
[Rozansky, q-alg/9604005](https://arxiv.org/abs/q-alg/9604005).
The stronger Melvin--Morton assertions are not premises here.

## 6. Coverage and independent checks

Adequate colored-degree growth is existing coverage, including
[Le, math/0407521](https://arxiv.org/abs/math/0407521) and
[Kalfagianni, 1601.03307](https://arxiv.org/abs/1601.03307).
Their stated scope is used for comparison; the extreme-state,
cabling, threading, and valuation arguments above supply the
proof here. No AJ or slope-conjecture theorem is imported.

The [exact diagnostic script](../experiments/audit_adequacy_algebraic_periods.py)
computes brackets by Temperley--Lieb multiplication and closure,
forms the Chebyshev combination, divides by the actual unknot
color, and checks the spans. It separately checks the circle
counts and single-crossing adequacy of the cables. Examples are
diagnostics of the uniform proof, not the scope of its statement.
The [results](../experiments/adequacy_algebraic_periods_results.json)
also check the fundamental local braid/bracket identity.
