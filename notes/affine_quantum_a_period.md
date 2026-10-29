# The inhomogeneous quantum-A period is an affine difference torsor

Research note, 26 October 2026. A homogeneous norm line alone does
not record how a knot period is sourced. A literature-defined
inhomogeneous A-equation gives a more structured object: an affine
extension of its geometric difference module by a trivial line.
Its class survives finite algebraic covers unless it was already
split. At a root, a finite cyclic resolvent reconstructs its period.
These statements do not prove that every knot has the required
inhomogeneous factor or identify its extension class with the
classical regulator.

Inhomogeneous noncommutative A-polynomials are existing definitions;
see Section 1.5, equation (2), of
[Garoufalidis--Sun, 0802.4074v2](https://arxiv.org/html/0802.4074v2#S1.SS5).
No creative-telescoping proof or knot operator from that paper is
being assumed. The homogeneous operator and actual state remain
those of [the all-level formulation](all_level_a_period.md).
No minimal-order claim is made for a pair extracted from a given
homogeneous operator. Its source is fixed by the actual finite
color pointing, rather than selected to change the period.

## 1. The affine extension class

Over F=C(q,M), sigma(M)=qM, take a specified pair

    A y=b, A=sum_(i=0)^d a_i(q,M)T^i, b in F,
    T y=sigma(y), a_0*a_d!=0.                       (1.1)

Its column companion equation is

    sigma(v)=C v+c,
    c=e_d*b/a_d,
    sigma((v,1)^t)=U*(v,1)^t,
    U=[C c; 0 1].                                  (1.2)

C here is the forward solution companion (superdiagonal one and
last row -a_i/a_d). This is the transpose-dual convention to the
cyclic-module matrix used in the intrinsic norm-torsor note.

Translation v -> v+t changes the source by

    c -> c+sigma(t)-C t.

Thus the source defines the additive class

    [c] in F^d/(sigma-C)F^d.                        (1.3)

It is zero exactly when (1.2) has a rational particular solution.
The inhomogeneous solution set, when nonempty, is an affine torsor
under the vector space of homogeneous solutions. This linear and
affine structure is proved by subtraction of equations, not by a
nonlinear test on scalar sections.

More precisely, (1.3) measures a horizontal point of a trivial affine
bundle with semilinear transport. The underlying affine space has
ordinary F-points; nonsplitting concerns the horizontal equation.
This qualification is essential when comparing the difference
extension to the ordinary algebraic norm torsor at a fixed root.

The class is intrinsic under changes v -> Gv+t with G invertible:
the augmented matrices change by the usual difference gauge
U -> G_aug(qM) U G_aug(M)^(-1). One must transport the period
functional and its actual meridian lattice along with that gauge.

## 2. Finite algebraic covers do not kill a nonzero affine class

Let L/F be finite in characteristic zero, with sigma extending to
an automorphism of L. If t in L^d solves sigma(t)-C t=c, then

    t_0=Tr_(L/F)(t)/[L:F]

belongs to F^d and solves the same equation. Indeed trace is
semilinearly natural, Tr(sigma(t))=sigma(Tr(t)), and C,c are over F.
Consequently pullback on the classes (1.3) is injective.

This is the relevant finite-cover descent statement. It differs
from multiplicative Hilbert 90 on a fixed finite cyclic extension.
A nonsplit generic source cannot be made into a rational particular
solution merely by replacing F with a finite sigma-stable algebraic
cover. The qualification sigma-stable is necessary.

The subsequent [common period-space note, Section 6](common_frobenius_regulator_period_space.md#6-rational-frobenius-base-change-preserves-source-classes)
proves an additional injectivity statement for the rational
Frobenius enlargement. If sigma(w)=-w, extraction of the Laurent
w^0 coefficient commutes with sigma-C and retracts the enlarged
source quotient onto the original one. Thus a nonsplit source
defined over F remains nonsplit over F(w), also after finite
stable algebraic covers. This does not concern unrestricted
formal or analytic period extensions. Its Section 7 also bounds
the presentation degrees needed by exact separate root splittings.

### Formal splitting is a different operation

Put q=exp(h), delta=M*d/dM, and assume C,c are formal meromorphic
in h with coefficients in C(M), with C regular in h. If
det(I-C_0)!=0 in C(M), the source has a unique formal particular
solution in C(M)((h)). At order h^k, its coefficient is determined by

    (I-C_0)v_k=c_k-sum_(ell>=1)
                   [(delta^ell/ell!)-C_ell]v_(k-ell). (2.1)

Only previously computed coefficients occur on the right. The
sum is finite at each order, starting at the lowest h-order of c.
This proves the assertion by recursion. In scalar companion form,
the condition is A_0(M,1)!=0 generically; it does not require
nonvanishing at a special boundary point.

Thus an extension can be generically nonsplit, remain nonsplit
on every finite stable algebraic cover, and nevertheless split
after formal completion. That completion is not a finite cover.
Its formal splitting is not automatically an actual selected
period or a convergent section. For the nonsplit example in
Section 6, its coefficients begin

    v_0=1/(1-M), v_1=-M/(1-M)^3,
    v_2=M*(1+4M+M^2)/(2*(1-M)^5).

They have boundary poles at M=1, while the exact root period there
is the regular finite expression (6.3). Evaluating the coefficients
separately at that point would lose the period. This locates the
algebraization and boundary comparison that remains after formal
branch lifting; it does not identify it with the Bloch regulator.

## 3. Exact affine descent at a root of unity

Now let q have order n, E=C(M), K=C(u), u=M^n. Put
C_j=C(q^j M), c_j=c(q^j M), and form the forward monodromy

    H=C_(n-1)...C_0,
    s=sum_(j=0)^(n-1) C_(n-1)...C_(j+1)c_j.

Empty matrix products are identity. The augmented monodromy is

    U_(n-1)...U_0=[H s; 0 1].                       (3.1)

A rational solution necessarily obeys

    (I-H)v=s.                                      (3.2)

Conversely consistency of this ordinary E-linear equation suffices.
Define the affine semilinear map

    Phi(v)=sigma^(-1)(C v+c).

Its n-th iterate is H v+s. On the nonempty affine solution space
W of (3.2), Phi^n is identity and Phi preserves W. For any v_0
in W the affine average

    v=(1/n)sum_(j=0)^(n-1) Phi^j(v_0)               (3.3)

is fixed by Phi and hence solves (1.2). Affine averaging is valid
because its coefficients sum to one. This is an explicit additive
cyclic descent argument for any level, including even and composite.

In the nonresonant case det(I-H)!=0, there is a unique rational
particular solution and no average is needed:

    v_N=(I-H)^(-1)s.                               (3.4)

Each component is a Cramer quotient. Apparent zeros of its
denominator must be canceled in the whole meridian germ. The
solution transfer monodromy H is the transpose of the corresponding
cyclic-module monodromy, so this uses the same central spectrum
as the norm-torsor formulation, with the source retained.

If (3.2) is inconsistent there is no rational period. If it is
consistent and resonant, (3.3) supplies one; the others form an
affine torsor under the homogeneous rational solutions. One must
keep their actual lattice and pointing.

There is no conflict between a nonsplit generic extension and
rational splittings at individual roots. Specialization changes
the order of sigma and its constant field. The finite inverses
(3.4) can exist at every level without forming a fixed algebraic
section in (q,M); the adequacy theorem excludes just such a section
for the actual traces. This is information forgotten by performing
Hilbert 90 separately at unrelated levels.

The subsequent [actual threaded-character calculation](ado_threaded_shadow.md)
gives another exact selection criterion. A null-homologous 2N-threaded
loop acts on the actual period and its polar subtraction by two.
If an actual extension carries a compatible observable
X=[G d_gamma;0 2] with 2-G invertible, its unique source-one
eigenvector is ((2-G)^(-1)d_gamma,1); commutation with difference
transport makes this vector horizontal. A complete hyperbolic
commutator supplies a classical scalar gap g_gamma!=2. The actual
relative extension, observable and off-diagonal coefficient are
still unconstructed. For a nonsplit generic source no such fixed
generic separating endomorphism can exist, since it would split
the class; level-dependent degree-2N observables are different data.

## 4. A simple algebraic criterion for nonresonance

There is no need to compute a growing monodromy determinant when
the operator has a unique extremal coefficient. Suppose, as
Laurent functions of M, exactly one a_i has the strictly smallest
order at M=0. The same criterion works with the strictly largest
degree at infinity. Generic uniqueness persists at q_N for all
but finitely many levels.

For a nonzero rational homogeneous solution y with order k at zero,
each sigma^i(y) has the same order k. The terms a_i sigma^i(y)
would have a unique least order and could not sum to zero. Thus
there is no rational homogeneous solution at these levels.

This implies det(I-H)!=0. Here is a direct descent justification:
if ker(I-H) were nonzero, the homogeneous semilinear Phi above
has Phi^n=1 on that kernel. For nonzero w in it, some average
sum_j Phi^j(fw) with f in E is nonzero. Otherwise the distinct
field automorphisms sigma^(-j), applied to all f, would satisfy
a nontrivial E-linear relation. Their independence follows by
taking a relation with fewest terms and subtracting its value
at af from one coefficient times its value at f. A choice of a
distinguishing two automorphisms shortens the relation, a
contradiction. The nonzero average would give a homogeneous
rational companion solution, contradicting the valuation argument.

This criterion is uniform in n and concerns the actual quantum
coefficients. A classical extremal pattern alone does not prove
it: coefficients vanishing at q=1 can change the M-extremum at
every nonzero quantum parameter.

## 5. Returning to the actual all-level period

Suppose a specified actual all-level reduced annihilator factors as

    P=(T-sigma(b)/b)A, b!=0,                        (5.1)

and its generic color traces satisfy A C=b. More generally, after
such a factorization, A C_j/b(q,-q^j) is independent of j. Its
value kappa(q) is computed from finitely many fixed colors. If
kappa!=0, replace b by the exact source kappa(q)b; the first factor
is unchanged. No root-dependent source normalization is chosen.

At a root, (5.1) implies

    A F_N=c_N(u)b, c_N in C(u).                     (5.2)

Choose a fixed integer color J where b and the coefficients are
regular and b(q,-q^J) is not identically zero; a sufficiently large
fixed J avoids the finitely many exceptional trace identities.
For all large N, the quotient-color identity and A C=b give
c_N(1)=1. Its germ is regular there, since b is nonzero at that
reference color and A F_N is regular there.

If the geometric block A is nonresonant, (3.4) is the unique
inhomogeneous root solution h_N. Equation (5.2) gives

    F_N=c_N(u)h_N, <K>_N=[h_N(M)]_(M=1).            (5.3)

The reference pointing has fixed the central unit exactly on this
fiber. Its unit property also proves that h_N has a regular whole
germ there. Formula (3.4), or its Cramer quotients, is therefore
an exact source-normalized A-period formula. A rational homogeneous
left factor and the nonresonance criterion are extra properties to
prove for the chosen literature operator, not new definitions of
a favorable quantization.

The full ADO factor remains
eta_N*(M-M^-1)*M^N/(u-1), with its residue and first jet as in
[the meridian note](bounded_meridian_jets.md#5-the-full-ado-normalization-keeps-its-residue-and-first-jet).
It is not erased from (5.3) or replaced by its numerical value
before the whole-germ comparison.

## 6. Adequacy forces this extension to be nonsplit

Under the actual-source hypotheses of Section 5, suppose A is
nonresonant at infinitely many levels (the extremal criterion is
a sufficient condition). If [c]=0 generically, a fixed rational
particular solution h(q,M) exists. At every nonresonant level
uniqueness gives h_N=h(q_N,M), so for every sufficiently large
fixed j,

    C_j(q_N)=h(q_N,-q_N^j)

at infinitely many distinct q_N. Polynomial rigidity makes the
identity hold rationally in q. But for any nontrivial adequate
knot the [degree-span theorem](adequacy_and_algebraic_periods.md)
excludes even a fixed algebraic meridian trace, and in particular
a rational one. Therefore

    [c]!=0.                                        (6.1)

By Section 2 it remains nonzero under every finite sigma-stable
algebraic cover. This supplies a broad knot-class constraint on
the extension, including all the hyperbolic alternating knots
in the user's proposed class, whenever the explicit source and
nonresonance properties have been established. It is not a proof
that all those knot operators possess those properties.

### A formal test that does not require cyclotomic nonresonance

There is a second, often simpler route to (6.1). Put q=exp(h),
M=-exp(Xh), with X an independent color variable, and expand
the trace operator over C(X)((h)):

    a_i(exp(h),-exp(Xh))=h^nu*(alpha_i(X)+O(h)),      (6.2)

where nu is the least h-order among the coefficients; some
alpha_i may be zero. Let R be their maximum degree at X=infinity.
If the sum of their degree-R leading coefficients is nonzero,
the leading trace operator

    A_*=sum_i alpha_i(X)T^i, T r(X)=r(X+1),

has no nonzero rational solution. Indeed, for r(X)=a X^k(1+O(1/X)),
the coefficient of X^(R+k) in A_*r is a times that nonzero sum.

Suppose a rational splitting g(q,M) of the source exists. Its
trace expansion is in C(X)((h)); the lower h-order is finite,
and all its coefficients are rational in X. Subtract it from
the actual color period's formal expansion. By the independently
proved [color polynomiality](adequacy_and_algebraic_periods.md#5-the-perturbative-coefficients-are-polynomial-in-the-color),
this difference is also in C(X)((h)) and is annihilated by A.
Its first nonzero h-coefficient would be a nonzero rational
solution of A_*, a contradiction. Thus the difference is zero
formally. For every sufficiently large fixed integer j the two
trace functions are rational in q; all their Laurent coefficients
at q=1 agree, so they agree identically. This contradicts the
adequacy degree span. Therefore (6.1) follows from this formal
test without any hypothesis on root-level kernel dimensions.

Only finitely many fixed j must be excluded when expanding a
rational trace: the first nonzero denominator coefficient is a
fixed nonzero polynomial in X, and subsequent coefficients only
introduce powers of it. If the coefficients are regular at
(q,M)=(1,-1) and A_0(-1,1)!=0, the test reduces to that one
nonvanishing value. When they share an apparent peripheral zero,
(6.2) keeps the actual leading polynomial in X instead of
substituting into a zero-over-zero expression.

### Nonsplitting is not itself a positive volume theorem

The equation sigma(y)-M*y=1 is a simple nonsplit generic example.
A rational particular solution cannot have a pole in C^*: a
finite q-orbit chain of poles would leave an unmatched endpoint.
It must therefore be Laurent polynomial. Its order at zero must
be nonnegative, whereas comparing degrees at infinity forces
its degree to be at most -1, a contradiction. The argument uses
generic q, so its nonzero powers have infinite orbits.

At a root of even order n its exact particular solution is

    y_n(M)=[sum_(r=0)^(n-1) q^(-r(r+1)/2) M^r]
                         /(1+M^n).                 (6.3)

The cyclic norm of M is -M^n and (6.3) follows directly from
(3.4), or by translating the finite sum. At M=1 the denominator
is exactly two, and |y_n(1)|<=n/2. Thus this nonsplit source
has no positive exponential growth. It is not a knot model.
It demonstrates why the regulator identification, rather than
nonsplitting alone, is the missing norm theorem.

## 7. Why the classical A-equation alone cannot select volume

The source class is essential. Given any ordered operator A with
nonzero b=A(1), form P=(T-sigma(b)/b)A. The coherent period y=1
solves A y=b and P y=0 at every level. Its affine extension is
split, with the constant companion vector as a splitting. If the
classical b is nonzero, the classical symbol of P is

    (L-1)A_0(M,L).

Thus one may use the geometric factor of a hyperbolic knot in
A_0 and still obtain a split model with zero exponential growth.
This is not the knot's literature quantization or state. It shows
why the source extension, actual quantum operator, and finite
pointing cannot be inferred solely from the classical A-polynomial.

There is a corresponding classical warning about matrix norms.
For the figure-eight geometric curve

    L^2-t(M)L+1=0,
    t(M)=M^4-M^2-2-M^-2+M^-4,

the log spectral radius on M=exp(i theta), 0<=theta<=pi, is
positive on two reflected intervals (0,pi/3) and (2pi/3,pi).
It has equal integrals on them. Hence choosing the largest modulus
at each point counts two equal contributions, whereas a relative
period from a zero-volume real place to one complete place uses
one contribution. Numerical integration gives the full integral
2.0298832128193, twice the required action Vol/2 in the recorded
square-holonomy convention. The diagnostics label this a numerical
classical check; it is not a quantum volume proof.

The normalized curve matters for the zero-volume reference. Under
the conjugation/Weyl involution (M,L)->(1/conj(M),1/conj(L)), a
conjugation-odd volume primitive vanishes at a fixed normalized
place. A smooth torus point fixed in these coordinates has one
place and therefore value zero. At a node, the two normalized
places can be exchanged, as at the complete figure-eight point;
its coordinate values on the torus do not force volume zero.
This is an intrinsic algebraic way to locate a possible classical
reference, subject to the actual marked regulator's conjugation
compatibility. It does not yet transport the quantum source to it.

## 8. Status and checks

The affine class (1.3), finite-cover trace descent, cyclic averaging,
resolvent, extremal-coefficient criterion, and formal nonsplitting
test are proved above.
The standard inhomogeneous-operator coverage was checked to avoid
presenting a new definition. The independent
[diagnostics](../experiments/audit_affine_quantum_a_period.py) check
nonresonant and resonant affine descent, an inconsistent source,
the scalar source factorization, a whole-germ rank drop, the
formal trace criterion, and the nonsplit Gaussian-source example.
[Results](../experiments/affine_quantum_a_period_results.json) are
supplementary exact checks, not proofs of a broad knot operator class.

The necessary next comparison is between the actual nonsplit source
class and the marked regulator extension, with their peripheral
pointing and norms. It is not supplied by Hilbert 90 at one level,
by nonzero extension alone, or by maximizing classical eigenvalues.
The volume conjecture remains unproved.

The subsequent [regular-period theorem](regularized_kashaev_period.md)
supplies a canonical rootwise affine source for any specified actual
all-level operator, without Section 5's rational left-factor hypothesis.
Its construction subtracts the full state's proper polar function,
fixed by every ordinary-color value. Positive trace bounds make all
those data polynomial in N. After a fixed gauge and denominator
clearing, the source lies in a fixed Laurent space with polynomially
bounded coefficients. The selected complete regular value is exactly
a weighted cyclic field trace. Under a separate rational rank-one
hypothesis, regularity at the nonzero pole anchor and at completeness
fixes this affine value uniquely. A single generic rational source,
its nonsplit class, geometric coupling, and the regulator norm do not
follow from this rootwise construction.
