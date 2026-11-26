# Orthogonal boundary packets under Conway composition

20 November 2026. Research note; the public manuscripts remain frozen.

The full Newton packet already makes a genuine quarter-turn unitary.
Multiplication of neighboring tangles requires a further metric. At
\(N\ge3\), different output rows overlap, so row-by-row normalization
does not give a coisometry. This note constructs that metric for every
finite expression made from Conway multiplication and quarter-turns.
It keeps the entire boundary algebra and both original closing rows.

The result is an exact finite-dimensional compatibility theorem. It
identifies two quantitative losses that remain to be estimated: the
projection of the actual leaf data onto the surviving boundary packet,
and its angle with the prescribed closing row. Neither loss is given a
positive lower bound here. In particular, this note proves no new
hyperbolic-volume identity or finite-exception theorem.

## 1. The actual boundary algebra

Fix an integer level \(N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 s_0=1,\qquad s_r=\prod_{u=1}^r2\sin(\pi u/N)
 \quad(1\le r\le d).
\]
The boundary space is the actual pair-Casimir algebra
\[
 H_N=\mathbb C[z]/\bigl(2T_N(z/2)+2\bigr).
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. The
normalized Newton basis is
\[
 b_r(z)=\frac{\prod_{j=0}^{r-1}(c_j-z)}{s_r^2},
 \qquad 0\le r\le d.                                      \tag{1}
\]
The empty product gives \(b_0=1\). Coefficient vectors in this basis
are columns in \(\mathbb C^N\), equipped initially with the usual
Hermitian inner product. A superscript \(*\) means its conjugate
transpose. The algebra retains the value and first derivative at every
double Casimir root and the simple value at \(-2\) when \(N\) is odd.
It is not the algebra of functions on the distinct roots alone.

We use the actual source identities proved in
[the Newton turn note](actual_newton_turn_positive_gram.md) and
[the multiplication note](actual_positive_newton_multiplication.md).
The genuine quarter-turn has coefficient matrix
\[
 J e_r=e_{d-r},\qquad J=J^*=J^{-1}.                       \tag{2}
\]
Multiplication is the linear map
\[
 M:H_N\otimes H_N\longrightarrow H_N,
 \qquad M(e_i\otimes e_j)=\sum_r\mu_{ijr}e_r.             \tag{3}
\]
If \(i+j\le d\), its nonzero coefficients are
\[
 \mu_{ijr}
 =\frac{s_{i+j}s_r}
 {s_i s_j s_{r-i}s_{r-j}s_{i+j-r}},
 \qquad \max(i,j)\le r\le i+j.                          \tag{4}
\]
All other coefficients are zero, including every product with
\(i+j\ge N\). Equations (2)--(4) hold in the full repeated-root
algebra. In particular
\[
 M(e_0\otimes f)=f,\qquad
 \mu_{ij0}=\delta_{i0}\delta_{j0},\qquad
 \mu_{ij,d}=\delta_{i+j,d}.                              \tag{5}
\]
The first equality makes \(M\) surjective.

There are two original scalar closures. For
\(f=\sum_r f_rb_r\), the original cup followed by the marked cap
evaluates \(f(c_0)=f_0\). The cylindrical closure, with one ordinary
pivotal trace and the prescribed mark, is \(\phi(f)=f_d\). We retain
both rows:
\[
 \lambda_0=e_0^{\mathsf T},\qquad
 \lambda_d=e_d^{\mathsf T}.                              \tag{6}
\]
In particular the ordinary pivotal trace in the cylindrical closure
has not been substituted for the marked cap. The exact Frobenius
identity is
\[
 \phi(fg)=f^{\mathsf T}Jg.                               \tag{7}
\]
The positive fixed Newton metric is
\(\langle f,g\rangle=\phi(\overline f\,Jg)=f^*g\), where
coefficient conjugation is well-defined because (1) has real
coefficients. Both rows (6) have dual norm one in that fixed metric.

The literal ribbon operations and normalizations are also recorded
in [the complete-circle Conway note](actual_positive_complete_circle_conway_trees.md).
Any external framing or normalization factor remains attached to the
original diagram; the constructions below introduce no new such factor.

## 2. Keep every leaf variable before inserting its filling

Let \(E\) be a finite expression obtained from leaves by products
\(EF\) and quarter-turns \(\mathscr R E\). A leaf stands for an
arbitrary boundary packet in \(H_N\). It does not stand for a
one-dimensional space spanned by the already computed tangle value.
Every occurrence of a leaf receives its own copy of \(H_N\).

If \(n(E)\) is the number of leaf occurrences, define
\[
 B_E:H_N^{\otimes n(E)}\longrightarrow H_N                \tag{8}
\]
by the following actual coefficient operations:
\[
 B_{\mathrm{leaf}}=I,\qquad
 B_{\mathscr R E}=JB_E,\qquad
 B_{EF}=M(B_E\otimes B_F).                              \tag{9}
\]
Ordered leaf tensor factors are inherited from the planar expression.
Thus no permutation convention is left implicit.

If the actual leaf packets are \(f_1,\ldots,f_{n(E)}\), then
\[
 v=f_1\otimes\cdots\otimes f_{n(E)},\qquad y=B_Ev          \tag{10}
\]
is the full actual boundary packet of the composed tangle. This follows
by induction from the full operator identities (2)--(4). It includes
the Hermite directions even when a component has zero value at every
distinct root.

An actual signed crossing power can be inserted as a leaf packet. Its
Newton coefficients include its original common Cartan scalar and all
first derivatives. No crossing is replaced by its nodal phases. Fixed
short tangles can likewise be inserted as their full packets. With this
convention, \(B_E\) depends on the unfilled expression and \(N\), but
not on the numerical twist assignments or an unknown closed invariant.

**Lemma 1.** Every \(B_E\) is surjective.

**Proof.** This is true at a leaf. A turn preserves surjectivity because
\(J\) is invertible. If \(B_E\) and \(B_F\) are surjective, their
tensor product is surjective, and (5) says that \(M\) is surjective.
Their composite in (9) is therefore surjective. Induction proves the
claim. \(\square\)

## 3. The boundary quotient metric and the expanded Gram

Define the real symmetric positive-definite matrices
\[
 C_E=B_EB_E^*,\qquad G_E=C_E^{-1}.                        \tag{11}
\]
Positive definiteness follows from Lemma 1. Reality follows because
the universal matrices \(I,J,M\) are real; the actual leaf vectors
in (10) can still be complex. The recursion is explicit:
\[
 C_{\mathrm{leaf}}=I,\qquad
 C_{\mathscr R E}=JC_EJ,\qquad
 C_{EF}=M(C_E\otimes C_F)M^*.                            \tag{12}
\]
Consequently \(G_{\mathscr R E}=JG_EJ\). In the remainder,
\(\|y\|_{G_E}^2=y^*G_Ey\).

Two different Grams must be distinguished. The matrix
\(B_E^*B_E\) acts on the expanded leaf tensor space and is generally
singular. It gives the fixed Newton boundary norm
\(\|B_Ev\|^2=v^*B_E^*B_Ev\). The matrix \(G_E\) acts on the
\(N\)-dimensional boundary and is nonsingular. It gives the quotient
norm inherited from the entire expanded leaf space.

**Theorem 2.** The least-norm expanded lift of \(y\in H_N\) is
\[
 S_Ey=B_E^*C_E^{-1}y.                                   \tag{13}
\]
Its squared norm is \(y^*G_Ey\). The matrix
\[
 P_E=B_E^*C_E^{-1}B_E                                   \tag{14}
\]
is the orthogonal projection onto \((\ker B_E)^\perp\), and
\[
 \|B_Ev\|_{G_E}^2=\|P_Ev\|^2,\qquad
 \|v\|^2=\|P_Ev\|^2+\|(I-P_E)v\|^2.                    \tag{15}
\]

**Proof.** Equation (11) gives \(B_ES_E=I\). The range of
\(S_E\) lies in \(\operatorname{ran}B_E^*=(\ker B_E)^\perp\).
Every other lift of \(y\) is \(S_Ey+k\), with \(k\in\ker B_E\),
and the summands are orthogonal. This proves minimality and uniqueness.
Direct multiplication gives
\[
 S_E^*S_E=C_E^{-1}B_EB_E^*C_E^{-1}=C_E^{-1}.
\]
Likewise \(P_E^*=P_E\), \(P_E^2=P_E\), and its kernel is
\(\ker B_E\). These identities prove the projection claim and
both equalities in (15). \(\square\)

In particular this is the canonical quotient metric once the full leaf
Newton inner products have been fixed:
\[
 y^*C_E^{-1}y=\min_{B_Ec=y}\|c\|^2.
\]
Equivalently, \(C_E^{-1/2}B_E\) is a coisometry: its product with
its adjoint is the rank-\(N\) identity on the boundary. This is an exact
orthogonal packet for the actual synthesis, with no deleted boundary
channel.

## 4. Compatibility at every multiplication and turn

Consider neighboring subexpressions \(E,F\). Set \(C=C_{EF}\), and
define the normalized multiplication map
\[
 A_{E,F}=C^{-1/2}M(C_E^{1/2}\otimes C_F^{1/2}).             \tag{16}
\]
Equation (12) gives
\[
 A_{E,F}A_{E,F}^*=I.                                    \tag{17}
\]
Thus the original multiplication is a coisometry from the product of
the two child quotient metrics to the parent quotient metric. The
metric is transported at the gluing; it is not held fixed while an
unproved isometry is imposed on \(M\).

For arbitrary actual child packets \(f,g\), put
\[
 x=(C_E^{-1/2}f)\otimes(C_F^{-1/2}g),\qquad
 P_{E,F}=A_{E,F}^*A_{E,F}.
\]
Then \(P_{E,F}\) is an orthogonal projection, and the exact loss is
\[
 \boxed{\quad
 \|f\|_{G_E}^2\|g\|_{G_F}^2-\|fg\|_{G_{EF}}^2
       =\|(I-P_{E,F})x\|^2.\quad}                       \tag{18}
\]
Indeed the two terms on the left are \(\|x\|^2\) and
\(\|A_{E,F}x\|^2=\|P_{E,F}x\|^2\), respectively. Orthogonal
decomposition proves (18). For a turn the corresponding equality is
\[
 \|Jf\|_{G_{\mathscr R E}}=\|f\|_{G_E}.                  \tag{19}
\]
This proves exact compatibility through arbitrarily many finite
neighboring Conway gluings and turns. At a product, the loss can be
nonzero; (18) computes it rather than asserting that it is small.

There is also a parenthesization check. For expressions involving
products alone, the two maps associated with \((EF)H\) and
\(E(FH)\) coincide, after the usual tensor associator, because they
are multiplication in the same actual algebra. Their \(B,C,G,P\)
therefore coincide. A genuine turn is not an algebra homomorphism,
so no analogous unproved interchange of turns and products is used.

The nullspace removed here is safe in any exterior: if \(B_Ev=0\),
the full actual boundary operator is zero. Every further linear or
multilinear tangle context therefore gives zero. This statement
concerns redundant expanded descriptions of a boundary operator.
It does not remove a nonzero vector from the boundary space \(H_N\).
In particular it does not quotient by the kernel of one closing row.
That row kernel can be exposed by a different exterior.

This distinction agrees with the contextual source-quotient criterion
in [the two-sided quotient note](actual_source_two_sided_quotients.md),
Section 1. The stronger observability results in
[the adjacent-observable note](actual_adjacent_observable_source_filtration.md),
Sections 2--3, concern quotients of the true boundary representation;
they do not forbid removal of redundant expanded descriptions.

## 5. Both original closing costs and the remaining angle

For a nonzero boundary row \(\lambda\), its squared dual norm is
\[
 a_\lambda(E)=\lambda G_E^{-1}\lambda^*
             =\lambda C_E\lambda^*.                    \tag{20}
\]
It is strictly positive. In particular the two original rows (6) cost
\[
 a_0(E)=(C_E)_{00},\qquad a_d(E)=(C_E)_{dd}.               \tag{21}
\]
Equivalently \(a_\lambda(E)=\|\lambda B_E\|^2\): it is an
explicit contraction of the expression with its adjoint. This does not
identify it with a hyperbolic volume or a regulator.
A turn exchanges these two costs. A product has the explicit updates
\[
 a_0(EF)=a_0(E)a_0(F),                                  \tag{22}
\]
\[
 a_d(EF)=\sum_{i,k=0}^d(C_E)_{ik}(C_F)_{d-i,d-k}
        =\operatorname{tr}(C_EJC_FJ).                   \tag{23}
\]
For (22), only the input \((0,0)\) contributes to row zero of
\(M\). For (23), row \(d\) is the antidiagonal selector in (5).
The displayed trace uses the real symmetry established after (11).
For a general complex Hermitian covariance the sum is still valid,
but its trace form is \(\operatorname{tr}(C_EJC_F^{\mathsf T}J)\).

Equations (20)--(23) compute the original source cost before the
numerical filling packets are inserted. Cauchy gives
\[
 |\lambda B_Ev|^2\le a_\lambda(E)\,\|P_Ev\|^2.           \tag{24}
\]
It is useful to retain the exact difference between this upper bound
and the desired scalar. Suppose first that \(v\ne0\), and put
\[
 t=C_E^{-1/2}B_Ev,\qquad
 r=\frac{C_E^{1/2}\lambda^*}{\sqrt{a_\lambda(E)}},
 \qquad \|r\|=1.
\]
Define
\[
 \eta_E(v)=\frac{\|P_Ev\|^2}{\|v\|^2},\qquad
 \gamma_{E,\lambda}(v)=
 \begin{cases}|r^*t|^2/\|t\|^2,&t\ne0,\\0,&t=0.
 \end{cases}                                           \tag{25}
\]
Both numbers lie in \([0,1]\). Since
\(\lambda B_Ev=\sqrt{a_\lambda(E)}\,r^*t\), there is an exact identity
\[
 \boxed{\quad
 |\lambda B_Ev|^2
 =a_\lambda(E)\,\|v\|^2\,\eta_E(v)\,
                         \gamma_{E,\lambda}(v).\quad}   \tag{26}
\]
For \(v=0\), define both factors in (25) to be zero; (26) remains
valid. For the actual tensor input (10),
\(\|v\|^2=\prod_j\|f_j\|^2\).

The first factor in (25) measures how much expanded leaf data survives
as a boundary operator. The second is the squared angle with the
prescribed closing vector. A nonzero boundary packet can still be
orthogonal to that closing vector. An orthogonal change of coordinates
does not prevent either factor from being zero or exponentially small.
No lower estimate for these factors is asserted.
Consistent unitary coordinate changes on the expanded and boundary
spaces leave these norms, projections, and angles unchanged; changing
an orthonormal basis alone cannot improve \(\eta_E\gamma_{E,\lambda}\).

## 6. A single gluing already has exponential metric cost

The metric update cannot in general be replaced by a harmless scalar
normalization. For two variable leaves,
\[
 C=MM^*,\qquad C_{00}=1,\qquad C_{dd}=N.                  \tag{27}
\]
The last two claims follow from the two distinct row descriptions in
(5). Hence \(C\) is not a scalar matrix at any \(N\ge2\).
In particular the actual multiplication is not a coisometry, even
after one common scalar rescaling, in the fixed Newton metric.
For \(N\ge3\), its covariance is not even diagonal: the input
\((1,d-1)\) contributes positively to both output rows \(d-1\) and
\(d\), by (4)--(5). Hence \(C_{d-1,d}>0\), and diagonal row
rescaling alone cannot make these rows orthogonal. At \(N=2\)
the rows have disjoint supports; (27) still excludes a common scalar
normalization, while separate row normalization does work at that level.

There is a stronger quantitative separation. Take
\(a=\lfloor N/3\rfloor\). For every \(N\ge3\),
\(1\le a\) and \(2a\le d\), so (4) applies exactly and gives
\[
 \mu_{a,a,a}=\frac{s_{2a}}{s_a^2}.                       \tag{28}
\]
Let \(\kappa_2(C)\) be the ratio of the largest to the smallest
eigenvalue. Its smallest eigenvalue is at most \(C_{00}=1\),
whereas its largest is at least
\(C_{aa}\ge\mu_{a,a,a}^2\). Thus
\[
 \kappa_2(C)\ge\mu_{a,a,a}^2.                            \tag{29}
\]

We use the Lobachevsky convention
\[
 \Lambda(\theta)=-\int_0^\theta\log|2\sin u|\,du.
\]
For fixed \(0<x<1\), the integrable Riemann-sum limit is
\[
 \frac1N\log s_{\lfloor Nx\rfloor}
       \longrightarrow-\frac{\Lambda(\pi x)}\pi.        \tag{30}
\]
For completeness, subtract \(\log t\) from
\(\log(2\sin\pi t)\) near zero; the difference extends continuously.
The continuous part has ordinary Riemann sums, and the monotone
integral bounds for \(\log t\) give its integrable Riemann sum.
This proves (30) and also applies when the index differs by a bounded
integer from \(Nx\), as needed for \(2a\).

Since \(\Lambda(2\pi/3)=-\Lambda(\pi/3)\), equations (28)--(30) give
\[
 \frac1N\log\mu_{a,a,a}\longrightarrow
             \frac{3\Lambda(\pi/3)}\pi>0,
\]
\[
 \liminf_{N\to\infty}\frac1N\log\kappa_2(MM^*)
       \ge\frac{6\Lambda(\pi/3)}\pi.                    \tag{31}
\]
The positivity follows from
\(\Lambda(\pi/2)=0\) and
\(\Lambda(\pi/3)=\int_{\pi/3}^{\pi/2}\log(2\sin u)\,du>0\).
These are lower bounds on conditioning, not an assertion of its
optimal exponent. The inverse metric \(G=C^{-1}\) has the same
condition number.

## 7. What changes relative to the existing packet results

The fixed Newton metric, the unitary actual turn, and the two closing
rows were already known. The
[ordinary-cap tree theorem](actual_cap_tree_angle_energy.md),
Sections 3--4, also gives an exact coisometry after its known diagonal
row normalization. That diagonal normalization works because different
root rows of that particular cap kernel have disjoint supports. The
same note explicitly leaves arbitrary adjoining interior operations
outside that conclusion.

Here the neighboring actual Conway multiplication is included. Its
overlapping rows are handled by the full covariance (12), rather than
by a diagonal weight or an unspecified positive global metric. The
recursive metric depends on all unfilled child expressions, remains
full dimensional, and has exact multiplication and turn interfaces.
The price can be exponential, as (31) already shows for one gate.

This gives a precise version of choosing the orthogonality adapted to
the synthesis: redundant expanded directions are orthogonally removed
without changing any exterior. It does not make the remaining closing
coefficient positive. To use (26) in a volume theorem, one must still
estimate the combined exponential rate of its explicit source cost,
leaf norms, projection factor, and closing angle. Their separate upper
bounds do not supply the missing lower bound. In particular no assertion
about generic or finitely many exceptional fillings follows here.

## 8. Long powers do not change an exact span by themselves

There is a simple limitation on using a smaller exact leaf space for
long fillings. Let \(T\) be an invertible operator on a finite-dimensional
space and let \(U\) be any prescribed subspace. For every integer
\(p\ge0\),
\[
 \operatorname{span}\{T^nu:n\ge p,\ u\in U\}
 =\operatorname{span}\{T^nu:n\ge0,\ u\in U\}.             \tag{32}
\]
Indeed the space on the right, call it \(W\), is \(T\)-invariant.
The restriction \(T|_W\) is injective and \(W\) is finite dimensional,
so \(T(W)=W\). The left side is \(T^pW=W\), proving (32).

This applies to multiplication by the actual crossing or full twist,
with its complete Hermite inverse and original Cartan factor. Thus
replacing a nonnegative filling half-line by a sufficiently long
half-line does not by itself reduce the exact space of allowed leaf
packets or the family of linear tests that annihilate it. The advantage
of long filling must enter a quantitative estimate. This assertion
uses no diagonalization and remains valid for Jordan blocks.

## Direct sources read for this note

The first two sources supply the algebraic identities used in the proof.
The remaining sources establish the physical-operation conventions and
the precise scope of the earlier orthogonality and quotient statements.

| Source | SHA-256 |
|---|---|
| [Newton turn and metric](actual_newton_turn_positive_gram.md) | `d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3` |
| [Actual Newton multiplication](actual_positive_newton_multiplication.md) | `543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb` |
| [Literal complete-circle Conway operations](actual_positive_complete_circle_conway_trees.md) | `f7e5bfbb1c556c1ea357a6880619851308cd73afc4402e8b42680963410edd58` |
| [Ordinary-cap trees](actual_cap_tree_angle_energy.md) | `ecaf7177962dfa5a944a532fed37d505b97e81361926039f69cbf7f9b674a2da` |
| [Contextual source quotients](actual_source_two_sided_quotients.md) | `7ec8b1482c6c312c3f103d148322219b31d318a79f6bf87dd5609071d0d184c0` |
| [Adjacent-observable source filtration](actual_adjacent_observable_source_filtration.md) | `c115426182ba06c5db16fc1c3292dabfdec187182c4666aacd53b91e13073f44` |

No mathematical program, numerical test, build, or public-document edit
was used to establish the assertions of this note.
