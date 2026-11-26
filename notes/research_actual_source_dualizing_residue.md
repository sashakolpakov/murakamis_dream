# The original finite source as a residue in a dualizing module

Research note, 2 November 2026.

The original closing functional is a residue, including at the repeated
Casimir roots. This note proves that its pairing remains perfect under
scalar smoothing, that all finite Conway operations admit an exact
residue formulation, and that a nonzero source has nonzero weights on
every branch of the generic spectral smoothing. The last conclusion is
an algebraic nonvanishing statement about the finite source. Identifying
these spectral branches with the critical branches governing large-level
asymptotics remains a separate problem.

The residue formula itself is already in
[the Newton calculus](../papers/newton-calculus/finite.tex), equations
labelled eq:hermite-trace and eq:leading-trace, and in
[the root-star calculation](actual_conway_root_star_full_jet_localization.md),
Section 1. The construction below organizes that formula into a family
of perfect pairings and follows it through
[the arbitrary-power source compiler](research_arbitrary_power_source_compilation.md).
It also states exactly what it supplies to the older
[irreducible critical-source theorem](irreducible_critical_source_and_whole_norm.md).
No new knot-volume conclusion is claimed here.

## 1. A perfect pairing for a monic relation

Let \(R\) be a commutative ring, let \(P(z)\in R[z]\) be monic of degree
\(N\), and put \(A=R[z]/(P)\). Every element has a unique representative
of degree below \(N\). Define
\[
 \lambda_P(f)=[z^{N-1}]\operatorname{rem}_P f.                 \tag{1}
\]
The \(A\)-module structure on \(A^\vee=\operatorname{Hom}_R(A,R)\) is
\((a\ell)(b)=\ell(ab)\).

**Proposition 1.** The map
\[
 A\longrightarrow A^\vee,\qquad
 a\longmapsto\bigl(b\longmapsto\lambda_P(ab)\bigr)              \tag{2}
\]
is an isomorphism. It commutes with every extension of the coefficient
ring \(R\).

**Proof.** In the power basis \(1,z,\ldots,z^{N-1}\), the pairing matrix
has entry \(\lambda_P(z^{i+j})\). It is zero when \(i+j<N-1\) and
one when \(i+j=N-1\). Reversing its columns makes it triangular with
diagonal entries one. Its determinant is therefore
\((-1)^{N(N-1)/2}\), a unit over any \(R\). Polynomial division by a
monic polynomial commutes with coefficient extension, proving the last
assertion. \(\square\)

Thus the relative dualizing module \(A^\vee\) is free of rank one as an
\(A\)-module, with generator \(\lambda_P\). This is the finite flat
Gorenstein property in the present explicit setting. The words identify
the structure; Proposition 1 proves it without appealing to a duality
theorem.

Over \(\mathbb C\), with finite roots counted by their actual
multiplicities, the same functional is
\[
 \lambda_P(f)=\sum_{P(c)=0}
       \operatorname{Res}_{z=c}\frac{f(z)\,dz}{P(z)}.          \tag{3}
\]
Indeed replacing \(f\) by its remainder changes the differential by a
polynomial differential. The coefficient of \(z^{-1}\) in the expansion
of that remainder divided by \(P\) at infinity is exactly (1). The
residue theorem proves (3). Here each distinct root contributes one
local residue; a multiple root is not counted several times as a simple
root.

If \(P=(z-c)^m Q\), with \(Q(c)\ne0\), its contribution is
\[
 \frac{1}{(m-1)!}
 \left(\frac{d}{dz}\right)^{m-1}\left(\frac{f(z)}{Q(z)}\right)_{z=c}.
                                                               \tag{4}
\]
Consequently this functional retains the nilpotent directions.

## 2. The physical normalization and its smoothing

Fix \(N\ge2\), write \(D=N-1\) and \(\eta=(-1)^D\), and use the
original relation and closure
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N=\eta N^2\lambda_{P_N}.                              \tag{5}
\]
Here \(T_N\) is the usual Chebyshev polynomial. The pair coordinate,
the marked cut and the scalar in (5) are the original physical choices.
The dualizing module is intrinsic to the finite algebra, whereas this
particular generator includes those choices.

For a double root \(c\), the Chebyshev equation gives
\[
 Q_c(c)=\frac{N^2}{4-c^2},\qquad
 \frac{Q_c'(c)}{Q_c(c)}=\frac{c}{4-c^2},
 \qquad Q_c=P_N/(z-c)^2.
\]
Equations (4)--(5) therefore recover the original contribution
\(\eta((4-c^2)f'(c)-cf(c))\). At odd \(N\), the simple root \(-2\)
has \(P_N'(-2)=N^2\) and contributes \(f(-2)\).

Introduce an independent parameter \(s\):
\[
 A_s=\mathbb C[s,z]/(P_N(z)-s),\qquad
 \phi_s=\eta N^2[z^D]\operatorname{rem}_{P_N-s}.             \tag{6}
\]
This is finite free over \(\mathbb C[s]\), with a perfect pairing for
every \(s\), including \(s=0\). If the roots \(r_j(s)\) are simple, then
\[
 \phi_s(f_s)=\eta N^2\sum_{j=1}^N
                \frac{f_s(r_j(s))}{P_N'(r_j(s))}.           \tag{7}
\]
The sum is regular at every collision whenever \(f_s\) is a regular
section. This is proved by the coefficient extraction (6), not by
bounding the individual terms in (7).

For example, take \(N=2\), when \(P_2=z^2\) and \(\eta N^2=-4\).
For \(s\ne0\),
\[
 \lambda_s(1)=\frac1{2\sqrt s}-\frac1{2\sqrt s}=0,\qquad
 \lambda_s(z)=\frac12+\frac12=1.                            \tag{8}
\]
Both equalities extend to \(s=0\); the latter becomes the residue of
\(z\,dz/z^2\). A regular total residue can require cancellation of
singular individual weights.

The physical meridian relations
\(2T_N(z/2)+2\cos(2\pi\sigma)\) are the base change
\(s=2-2\cos(2\pi\sigma)\) of (6). Their actual crossing polynomials and
turn factors must also be retained under that base change. An arbitrary
lift of a crossing to (6) need not be the physical meridian deformation.

## 3. Newton duality and the original turn survive scalar smoothing

Keep the original polynomials
\[
 e_i(z)=S_i^{-2}\prod_{k<i}(c_k-z),\quad
 c_k=2\cos((2k+1)\pi/N),\quad
 S_i=\prod_{k=1}^i2\sin(\pi k/N).
\]
They form a basis of \(A_s\), because they have nonzero leading
coefficients and distinct degrees. At \(s=0\), the original source
calculation proves
\(\phi_0(e_i e_j)=\delta_{i+j,D}\).

**Proposition 2.** For every \(s\),
\[
 \phi_s(e_i e_j)=\delta_{i+j,D}.                            \tag{9}
\]
Consequently the same two kernels implement identity and turn:
\[
 K_I(z,w)=\sum_{i=0}^D e_i(z)e_{D-i}(w),\qquad
 K_T(z,w)=\sum_{i=0}^D e_i(z)e_i(w).                        \tag{10}
\]
In particular
\(\phi_{s,w}(K_I(z,w)f(w))=f(z)\) and
\(\phi_{s,w}(K_T(z,w)f(w))=Tf(z)\), where \(Te_i=e_{D-i}\).

**Proof.** For a polynomial \(h\) of degree at most \(2N-2\), write
\(h=qP_N+r\), with \(\deg q\le N-2\) and \(\deg r<N\). Then
\[
 h=q(P_N-s)+(r+sq),
\]
and \(r+sq\) still has degree below \(N\). Its coefficient of \(z^D\)
is unchanged. Apply this to \(h=e_i e_j\); (10) follows by expanding
\(f\) in the basis. \(\square\)

The turn is linear, involutive and self-adjoint for this pairing.
It is not an algebra homomorphism. This distinction has an immediate
consequence for the proposed torsor of generating dualizing sections:
\[
             \phi_0\circ T=e_D\,\phi_0,\qquad e_D^2=0,
             \qquad \phi_0(e_D)=1.                        \tag{11}
\]
The functional equality follows by testing \(e_i\), using (9).
For the square, the multiset of zeros of
\(\prod_{k<D}(c_k-z)^2\) contains every zero of \(P_N\) with its
required multiplicity. Thus \(P_N\) divides that square.

Therefore the actual invertible linear turn sends the generator
\(\phi_0\) of \(A_0^\vee\) to a nongenerating section of that same
\(A_0\)-module. The full dualizing module accommodates the operations;
its subset of generators is not preserved by them. This does not
contradict (9), which concerns the bilinear pairing.

The degeneration is explicit. Since \(S_D=N\) and \(c_D=c_0\),
\[
 (z-c_0)e_D=\frac{\eta s}{N^2}\quad\hbox{in }A_s.           \tag{11a}
\]
Thus \(e_D\) is a unit away from \(s=0\), and its inverse is
\(\eta N^2(z-c_0)/s\). The functional identity
\(\phi_s\circ T=e_D\phi_s\) holds throughout the family. The generator
torsor is therefore adequate on this punctured smoothing for the
particular functional in (11), but its extension through zero requires
the whole dualizing module. Equation (11a) records the pole rather than
discarding it.

## 4. Arbitrary finite compositions and negative crossing powers

Let \(R_N(z)\), of degree below \(N\), be the original crossing in
\(A_0\). It is a unit there, because the physical crossing is invertible.
Use this polynomial as one possible lift to \(A_s\), and put
\[
 \Delta_N(s)=\det(m_{R_N}:A_s\longrightarrow A_s).
\]
This polynomial has \(\Delta_N(0)\ne0\). Over
\(\mathbb C[s,\Delta_N(s)^{-1}]\), its inverse is given by the adjugate
matrix, so all signed powers \(R_N^n\), \(n\in\mathbb Z\), exist and
are regular at zero. This proves regularity without choosing a branch
of a logarithm. More generally the same argument applies to any
specified regular lift of any unit coupon.

Start with these lifted coupons and the original basis elements.
Use quotient multiplication, the turn of Proposition 2, and the
closing functional (6) a finite number of times. Every resulting
coefficient is regular at zero, and specialization at zero gives the
original finite source exactly. All multiplication coefficients are
the regular functions
\[
       \mu_{ijr}(s)=\phi_s(e_i e_j e_{D-r}).                \tag{12}
\]
They need not be independent of \(s\). The identity and turn kernels
(10), in contrast, are independent of \(s\).

More explicitly, any such finite tensor contraction can be written,
with one variable for each contracted algebra copy, as
\[
 Z_{\boldsymbol s}=(\eta N^2)^m
   \operatorname{Res}
   \frac{F_{\boldsymbol s}(z_1,\ldots,z_m)\,
                     dz_1\cdots dz_m}
        {\prod_{v=1}^m(P_N(z_v)-s_v)}.                    \tag{13}
\]
The residue means the sum over all common finite zeros, or equivalently
successive applications of (1). The numerator contains the original
coupons and the identity or turn kernels. Free boundary polynomials
remain coefficients and are not reduced. Formula (13) follows by
induction on the finite expression, inserting (10) wherever a linear
operation is contracted. Conversely, expanding (10) recovers the exact
Newton-index contraction. Iterated residues commute because, after
reducing in each independent variable, they extract one specified
coefficient of the same polynomial.

This argument works with different scalar parameters at different
vertices: (9) holds in each copy, so the same basis kernels pair those
copies. For a more general finite collection of linear operations,
their basis matrices give kernels by the same perfect-pairing argument.

The family (13) is an exact algebraic deformation of the recorded
expression. It does not assert that all isotopies of the specialized
physical source remain identities for arbitrary independent smoothing
parameters. Nor does it replace the physical crossing, framing or
marked-cut choices by newly chosen ones.

## 5. Generic spectral branches have nonzero residue weights

There is a useful irreducibility fact special to the full scalar
smoothing. The total ring
\[
 \mathbb C[s,z]/(P_N(z)-s)\simeq\mathbb C[z]
\]
is an integral domain. Its generic fiber over \(\mathbb C(s)\) is a
finite-dimensional domain and therefore a field, of degree \(N\).
It is separable, since the characteristic is zero.

The same statement holds for independent parameters at \(m\) vertices:
\[
 B=\mathbb C[\boldsymbol s,\boldsymbol z]/
       (P_N(z_v)-s_v:1\le v\le m)\simeq
       \mathbb C[z_1,\ldots,z_m].                         \tag{14}
\]
Its generic fiber \(K\) over \(F=\mathbb C(s_1,\ldots,s_m)\) is a
field of degree \(N^m\). Inverting the unit-coupon determinants does
not change this conclusion.

Free boundary coordinates can be retained as independent coefficient
variables throughout. For the field statement, replace \(\mathbb C\)
by their rational function field. All the domain and finite-free
arguments remain unchanged. Specializing those free coordinates can,
of course, make a previously nonzero numerator vanish.

Let \(f\in K\) be the class of the compiled numerator and set
\(J=\prod_v P_N'(z_v)\). Since the generic fiber is separable, \(J\)
is nonzero and hence a unit. After passing to a splitting field,
the individual weights in (13) are
\[
       w_\sigma=(\eta N^2)^m\,\sigma(f/J).                \tag{15}
\]
If \(f\ne0\), every weight is nonzero, and
\[
 \prod_\sigma w_\sigma
   =(\eta N^2)^{mN^m}
                  \frac{\operatorname{Norm}_{K/F}(f)}
                       {\operatorname{Norm}_{K/F}(J)}
   \ne0.                                                  \tag{16}
\]
This follows because every field embedding is injective.
It is an actual residue-and-norm nonvanishing theorem for the finite
source smoothing. If the specialized numerator is a nonzero element
of the full algebra, its generic class is necessarily nonzero: the
family is free over its parameter ring.

For the usual compiler using only multiplication, turn, nonzero
crossing powers and nonzero colour coupons, the numerator in a fully
expanded kernel presentation is a product of nonzero factors, so this
nonzero hypothesis can be checked before evaluating the closed source.
Under (14), each crossing is the nonzero rational function \(R_N(z_v)\)
or its inverse, and each colour coupon is a nonzero polynomial.
Each kernel (10) is a nonzero polynomial in its incident variables.
If both ends belong to the same variable, it remains nonzero:
\(K_I(z,z)\) has leading coefficient \(\eta/N\) and degree \(D\),
whereas \(K_T(z,z)\) has degree \(2D\) and leading coefficient \(N^{-4}\).
For an edge ending at a fixed free boundary value, the basis expansion
contains a coefficient \(e_0=1\), so that kernel also cannot vanish
identically in its contracted variable. The ambient rational function
field is a domain, and their product is nonzero. This assertion excludes
extra linear combinations of complete networks that cancel, and any
explicit zero scalar coupon; it does not exclude cancellation in the
final residue sum.

A nonzero total pairing is sufficient to establish a nonzero numerator,
but not necessary. For example \(f=1\) in (8) has nonzero individual
generic weights and identically zero total pairing. Thus (16) is not
a lower bound on the absolute value of their sum. It also does not
justify specializing individual weights through a collision.

## 6. What changes for a geometric critical algebra

Let \(C/F\) be the finite algebra of isolated, nondegenerate solutions
of a specified critical system \(g_1=\cdots=g_r=0\), and let
\(J_g=\det(\partial g_i/\partial x_j)\). On its simple locus the
critical residue functional is
\[
 \rho(a)=\sum_p\frac{a(p)}{J_g(p)}
        =\operatorname{Tr}_{C/F}(a/J_g).                  \tag{17}
\]
For completeness, near a simple solution use \(g_1,\ldots,g_r\)
as local coordinates. The differential changes by \(1/J_g\);
the small product-circle residue is \(a(p)/J_g(p)\).
Summing gives (17); descent follows since the expression is invariant
under permutation of the solutions.

If \(C\) is a field and \(a\ne0\), (17) has nonzero individual weights
on every embedding. If \(C\) is a product of fields, the correct
condition is that \(a\) be nonzero on every factor under discussion.
For arbitrary \(C\), a unit \(a\) is sufficient. These are precisely
the trace-density conclusions of the older irreducible-source theorem,
with the explicit density \(a/J_g\).

This gives a concrete sufficient target for a geometric comparison:
construct a residue-compatible map from the original source period,
including its closing functional, to a marked critical dualizing line;
prove that the resulting density is nonzero on the geometric field;
and prove that its local residue decomposition is the actual
action-normalized asymptotic decomposition. Under these hypotheses
the selected algebraic coefficient cannot vanish. If the density and
Jacobian also have a fixed whole algebraic presentation along the
cyclotomic arc, the earlier norm argument supplies subexponential
upper and lower bounds. A presentation whose degree grows with \(N\)
does not automatically satisfy that hypothesis.

The present compiler supplies (13), not this comparison. Its zeros
are the finite spectral nodes \(P_N(z_v)=s_v\). The geometric critical
equations arise from the large-\(N\) phase of the numerator and kernel;
they are a different system. An enclosing spectral residue cycle does
not by itself become the sum of all small critical residue cycles.
The map must retain the original cycle or co-source, the half-twist
and peripheral marking, and the normalization of the exponential
actions. Neither critical-scheme irreducibility nor a perfect
spectral residue pairing establishes that map.

There is also an elementary reason to retain the quantum differential
relations during such a construction. For a convergent period
\(I_N(a)=\int_\Gamma a e^{NS}\,d^r x\), integration by parts, when its
boundary term vanishes, gives
\[
 I_N(b\,\partial_j S)=-N^{-1}I_N(\partial_j b).             \tag{18}
\]
Thus \(I_N\) does not generally factor through the ordinary Jacobian
algebra obtained by setting every \(\partial_jS\) to zero. For the
Gaussian \(S=-x^2/2\) on the real line, \(I_N(x^2)=I_N(1)/N\ne0\),
although \(x^2\) vanishes in that Jacobian algebra. A critical-algebra
description of leading coefficients must be constructed from the
quantum period relations with the corresponding cycle; simply taking
the classical quotient loses (18).

The established result is therefore a regular, exact residue family
for the original finite source, together with nonvanishing on every
generic spectral branch. The first remaining implication is a
residue-compatible passage from that family to the marked geometric
critical period, with control of its specialization and its selected
asymptotic coefficient.

## 7. Terminology and prior coverage

The use of \(\operatorname{Hom}_R(A,R)\) as the dualizing module for a
finite flat algebra, and its invertibility as the Gorenstein condition,
are standard; see the
[Stacks Project, Section 49.16](https://stacks.math.columbia.edu/tag/0C14).
Those words are used only to locate the construction. The pairing,
base change, smoothing, network contraction and generic norm claims
needed here have been proved explicitly above.

The finite physical residue and the Newton duality are prior results
in this repository. The additions are their simultaneous use in the
scalar smoothing, the generic-field statement (14)--(16), and the
precise distinction between its spectral branch weights and the
geometric coefficient required by the volume argument.
