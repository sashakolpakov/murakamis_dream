# An intrinsic norm torsor from the quantum A-module

Research note, 25 October 2026. The target is Kashaev's original invariant.
The noncommutative A-polynomial defined through recursions is a literature
object: see Garoufalidis, [math/0306230](https://arxiv.org/abs/math/0306230).
The construction below starts with a specified operator, without choosing
a new ordering of a classical polynomial. It applies to any finite-order
q-difference module and uses no triangulation or FAMED condition.

This is algebraic structure and an independently proved comparison
criterion, not a proof of the volume conjecture. A prescribed Kashaev
solution or period pairing is additional data.

The current [A-polynomial torsor formulation](a_polynomial_torsor_status.md)
puts these algebraic results alongside the regulator period, including
its explicit rank-three algebraic connection, and distinguishes the
norm-one torus from the scalar intertwiner torsor. It records the
unproved classical-curve and selected-period comparison.

For the actual knot state, the subsequent
[squared-meridian descent](even_meridian_norm_descent.md) applies this
construction with Y=M^2 and cyclic degree N at q=exp(pi*i/N), retaining
the full state's even-level sign. The
[regular-period theorem](regularized_kashaev_period.md) then supplies
the exact complete scalar Tr(Y F_N)/N at Y^N=1 and a positive trace
norm. The ordinary-color contribution is polynomially bounded, so
these give equivalent volume targets for hyperbolic knots. Their
norm comparison with the marked regulator remains unproved.

The later [peripheral normal-period theorem](peripheral_normal_period.md)
also identifies an integral datum invisible in this localization.
Positive volume growth requires every polynomial annihilator to
annihilate the complete-color delta module R/R*(Y-1). That module
vanishes over C(q,Y), while its selected normal extension records
the full ADO value. The theorem gives an exact derivative and
inverse-matrix presentation under its explicit rank or Weyl-sector
hypotheses. No general hyperbolic-knot rank or norm theorem is inferred.

When its stated quantum reciprocity holds, central reflection supplies
a further quadratic Hilbert-90 frame: g=(1+gamma(U))/2 for
gamma(U)gamma(U^(-1))=1 and gamma(1)=1. The frame preserves the
marked normal period. The ambient signed dihedral relation retains
kappa^N=(-1)^(N-1); it does not assert T-stability of the scalar
solution line or establish the regulator norm.

The [actual Weyl-descent theorem](actual_weyl_descent.md) now proves
the reflection of the literature knot state and forces a unitary
monomial reciprocity for its primitive minimal normal operator.
Thus its equivariant structure is not inferred from the classical
A-curve. Primitive generator units preserve the selected normal
metric period. The relevant root-fiber injectivity and regulator
norm remain to establish.

## 1. The central curve of an actual root-of-unity module

Let q=zeta be a primitive n-th root of unity. Let E=C(x),
sigma(x)=zeta*x, F=E^sigma=C(u), u=x^n. Assume that specializing the
specified operator is defined and its leading and trailing coefficients
are nonzero in E:

    Ahat=sum_(j=0)^r a_j(x) T^j,       T f=sigma(f) T.

Its cyclic module has E-basis e,T e,...,T^(r-1)e. The relation
Ahat e=0 specifies an invertible companion matrix C(x), with

    T=C sigma,       H=T^n=C sigma(C)...sigma^(n-1)(C).

The state is a solution pairing with this module; it is not identified
with an arbitrary choice of its column basis.

**Central-curve lemma.**

    D_n(u,v)=det(v I-H(x)) belongs to F[v].

Indeed sigma(H)=C^(-1) H C, so all characteristic coefficients are
sigma-invariant. This proof works at composite as well as prime n.
It retains all coefficients before any specialization u=1.

D_n is determined by the root-of-unity module. Equality of its relevant
component with a component of the classical A-polynomial is an extra
compatibility statement. Neither a classical symbol at q=1 nor the
existence of a quantization establishes that equality.

## 2. A simple component carries a canonical cyclic norm equation

Take a component of D_n=0 on which v is a simple eigenvalue, and let k
be its function field. The algebra

    S=k[x]/(x^n-u)

is a degree-n finite etale k-algebra. It may be a product of fields;
the argument does not assume that this Kummer algebra is connected.
Sigma acts on it, and S^sigma=k.

The eigenmodule

    L=ker(H-v I) in S^r

has rank one over S. T preserves it because T commutes with T^n.
Choose a basis e_L and write

    T e_L=a e_L,       a in S^*.

Iteration gives the exact equation

    N_(S/k)(a)=product_(j=0)^(n-1) sigma^j(a)=v.       (2.1)

Changing the basis to f e_L changes a to a sigma(f)/f. Thus the
generic scalar problem is a cyclic norm torsor on the central curve
of the actual operator, rather than on a chosen shape chart.

As a k-vector space L has dimension n. Multiplication by x and the
semilinear operator T give

    T x=zeta x T,       x^n=u,       T^n=v.

This is a splitting module of the corresponding central quantum torus.
Its endomorphisms commuting with x are S-linear scalars; commuting
also with T restricts them to k. Simplicity follows after a separable
base change: x has n distinct eigenlines and T cyclically permutes
them, so there is no proper nonzero invariant subspace.

## 3. Hilbert 90 gives the comparison torsor explicitly

Two scalar realizations a,b with the same norm v have ratio r=a/b
of norm one. Define

    r_0=1, r_j=product_(i=0)^(j-1) sigma^i(r),
    f(c)=sum_(j=0)^(n-1) r_j sigma^j(c).

The norm-one equation implies r sigma(f(c))=f(c). Some c makes f(c)
invertible. One elementary justification works also for an etale
product: after a separable closure sigma cyclically permutes n
coordinates; each coordinate of f(c) is a nonzero linear form.
Their product is a nonzero polynomial. Since k is infinite, there
is a k-rational c outside its zero set.

Hence r=f/sigma(f). A scalar intertwiner between the two modules exists,
and any two nonzero intertwiners differ by k^*. This identifies the
generic intertwiner torsor as G_m. Globally, local intertwiners give
a line bundle on the common regular locus; generic Hilbert 90 does
not automatically trivialize that line bundle.

Alternatively adjoin lambda with lambda^n=v. Then lambda^(-1)T has
n-th power one, and the same calculation descends its invariant
rank-one line. This is the peripheral-root realization of the torsor.

Consequently, once two specified constructions have the same simple
central component, their unpointed module comparison reduces to a
scalar period line. Identifying their distinguished vectors, cycles
and level-dependent scalar remains necessary.

The [root-orbit pointing theorem](root_orbit_pointing.md) now gives
an exact way to fix that central scalar on the relevant fiber.
The actual reduced state has value one at M=-q, in the same root
orbit as M=1. A comparison within the same rational solution line
that preserves this anchor has central factor one at M^(2N)=1.
For the full state one uses the specified nonzero central residue.
The theorem also reconstructs the fiber period by maximal minors
of the root operator matrix when its rational kernel has rank one.
This does not establish the required kernel rank or the geometric
period comparison for the full knot class.

The subsequent [all-level period theorem](all_level_a_period.md)
uses polynomial coherence of the actual integer-color traces to
give an exact period formula without that rank condition. It needs
only a fixed initial color window and bounded-order q-jets, whose
initial values stay bounded near q=1. Its
[meridian counterpart](bounded_meridian_jets.md) bounds the integral
kernel's Smith exponents by the fixed leading M-span. This supplies
finite pointing, not the remaining geometric norm comparison.

The [affine source extension](affine_quantum_a_period.md) retains
additional information when the actual homogeneous operator has
the stated inhomogeneous source factor. Its root period is a
cyclic affine fixed point; in the nonresonant case it is an exact
resolvent. The generic source class is not killed by finite stable
algebraic covers, by normalized trace. The
[adequacy proof](adequacy_and_algebraic_periods.md) excludes a
fixed algebraic meridian trace for all nontrivial adequate knots.
Under either stated source nonresonance test this forces the
affine class to be nonsplit. Its identification with the marked
regulator and its norm remains separate from multiplicative
Hilbert 90 at any single root level.

The [formal classical-curve construction](formal_a_curve_period_torsor.md)
gives a different, complementary branch construction directly at q=1.
Its Hensel lift and formal connection do not assume that D_n equals
the classical A-polynomial. They still require the geometric component
to occur in the actual operator's classical symbol and do not select
the actual knot period from its formal branch alone.

### 3.1 Extending through coalescing eigenvalues and apparent poles

Normalize the chosen central curve. Work where u and v are units, so
the x-root cover Y remains finite etale. The generic rank-one eigenline
can be extended as a fractional line lattice Lambda_0 on Y. Define

    Lambda_cyc=sum_(j=0)^(n-1) T^j Lambda_0.           (3.1)

**Extension lemma.** Lambda_cyc is an invertible fractional line sheaf,
T Lambda_cyc=Lambda_cyc, and it is the smallest T-stable lattice
containing Lambda_0.

Proof: the sum is coherent and torsion-free of rank one; on a smooth
curve this is invertible. The identity T^n=v and the fact that v is
a unit give T Lambda_cyc=Lambda_cyc. Minimality follows by applying
each T^j to the inclusion of Lambda_0. No regularity of the original
companion matrix at the point is needed on this generic eigenline.
After adjoining lambda^n=v, the invariant lattice for lambda^(-1)T
descends to a line bundle on the peripheral-root base.

This handles apparent poles or eigenvalue coalescence in the matrix
presentation. It does not equate the limiting eigenline with the
entire kernel of the specialized matrix, which can be larger. It
also does not assign a value to a meromorphic period without its
pointing. Different initial lattices can retain different divisor data.

A useful exact model is

    T e=((x-1)/(zeta*x-1)) e,       T^n=1.

Its coefficient has a zero and pole above u=1. Put

    P_n(x)=(x^n-1)/(x-1)=1+x+...+x^(n-1).

Starting from O_Y e, (3.1) gives O_Y e/P_n(x): at each root of unity
other than x=1 some summand has a simple pole, while at x=1 the
summand j=0 remains a unit. In the extended frame e'=e/P_n,

    T e'=e',        e' at x=1 equals e/n.             (3.2)

Thus the pole is removed by an actual lattice change, and the exact
specialization retains a factor n. Its exponential rate is zero.
This is a uniform algebraic example of why peripheral multipliers
and the integral period lattice must be tracked together.

### 3.2 Retain the full spectral algebra at a multiple root

Extending one generic eigenline does not recover the whole generalized
eigenspace or the operators acting on it. The
[Casimir/recoupling calculation](casimir_braiding_and_recoupling_lattice.md)
now gives an explicit instance relevant to the actual Kashaev crossing:
its cyclic spectral algebra is C[z]/(T_N(z)+2), with double roots.
The crossing and pivotal trace both use first derivatives at those
roots. Its vacuum lies in the socle of a double point and does not
by itself fix a module frame there.

When a generalized spectral module is rank one over its finite
spectral algebra A, its frame comparison is an A^*-torsor. Section 7
of that note extends Hilbert 90 to characteristic-zero Artin bases
by a finite nilpotent logarithm and an explicit additive telescoping
formula. This retains the jets. The rank-one-over-A hypothesis is
proved there by cyclicity of the relative Casimir; it is not assumed
for every specialized quantum A-module. The simple-component argument
above remains valid on its stated locus.

## 4. A uniform exact check on the central-curve condition

For the companion family

    C(x)=[[0,-1],[1,c-x]],

put s_0(c)=2, s_1(c)=c, s_(j+1)=c s_j-s_(j-1). Then at every
primitive level n,

    D_n(u,v)=v^2-(s_n(c)-u)v+1.                       (4.1)

Here is a direct proof. The determinant of H is one. Its trace is
sigma-invariant and is a polynomial in x of degree at most n, so
only the constant and x^n terms survive. The constant is
tr(C(0)^n)=s_n(c). The top coefficient is
(-1)^n zeta^(n(n-1)/2)=-1. This proves (4.1) uniformly.

For c=1, s_n(c)=2 cos(n*pi/3). Thus constants can retain a periodic
level dependence even when the input coefficients are integral.
This is an abstract module calculation, not a counterexample about
a knot invariant. It shows what must actually be checked in any
claimed quantum-Frobenius compatibility.

The exact audit in `experiments/audit_intrinsic_norm_torsor.py` checks
the central curve, eigenline norm, and Hilbert-90 formula at composite
levels as well as prime levels. It does not assume equality with a
classical knot A-polynomial.

## 5. Which normalization factors affect the volume rate

Let c(q) be a fixed nonzero meromorphic germ at q=1. Along
q_n=exp(2*pi*i/n),

    log|c(q_n)|=O(log n),

provided the specialized factor is defined and nonzero. This follows by
writing c(q)=(q-1)^j g(q), g(1)!=0. The same conclusion holds for a
fixed algebraic Puiseux germ, with rational j. Multiplication by such a
factor preserves the exponential volume rate. A regular nonzero factor
1+x^n=1+u at u=1 is harmless for that rate, although its exact value remains
part of the state comparison.

Finite-level Hilbert 90 by itself gives no uniform-in-n bound on its
remaining k^* scalar. For instance, (u/2)^n is a central algebraic unit
at each level, equals one at u=2, and equals 2^(-n) at u=1. This
preserves an unpointed module while changing a chosen scalar period's
exponential size. It demonstrates insufficient reconstruction data,
not freedom to renormalize the already defined Kashaev invariant.

Thus one needs level-compatible pointing and regulator normalization
of this intrinsic period line. The all-level theorem linked above now
specifies the quantum period by finite pointing once an actual operator
is given; its regulator comparison remains missing. A fixed algebraic
generic-q comparison could be sufficient for the rate; arbitrary
unrelated finite-level gauges are not.

The subsequent [central normalization theorem](algebraic_central_normalization.md)
allows a fixed finite algebraic comparison depending also on the
central variable z=M^(kN), evaluated as a whole germ. Its value is
between fixed powers of N. This covers the exact ADO normalization
and retains factors such as 1+M^N. The levelwise unit (u/2)^n above
has no such fixed finite algebraic presentation across levels.

The subsequent [local normalization tower](cyclotomic_normalization_tower.md)
proves distribution between arbitrary levels and its regulator estimate
directly from finite products and an exact convergent series. The
[regular cyclic/Steinberg family](cyclic_steinberg_lattice.md) extends
the selected local vacuum and gives explicit recoupling lattices at
degeneration. These supply local comparison data; neither establishes
the global period identification required in Section 7.

## 6. The classical A-curve and finite-cover descent

Fix the peripheral monomials m,l in the unhalved conventions of the
Bloch-period note. Put

    omega=-(1/2)(log|m| dArg(l)-log|l| dArg(m)).

The previously proved identity delta(beta)=-(1/2)m wedge l gives
dD(beta)=omega on an augmented character chart. This is the general
exactness property of the A-curve, with its peripheral conventions
retained. Exact polynomials and their volume functions are existing
literature definitions; see Guilloux--Marche,
[1804.01395](https://arxiv.org/abs/1804.01395). No novelty is claimed
for exactness or for conjugation normalization.

Here is a useful direct descent argument. Suppose p:Y->C is a connected
finite cover of smooth curves, and a single-valued real function V on Y
satisfies dV=p^*omega. Remove the finitely many branch values and set

    V_C(c)=(1/degree(p)) sum_(y over c) V(y).

Then dV_C=omega. The function V-p^*V_C is locally constant on the
connected punctured curve Y, so constant; its fiber average is zero,
so it is zero. Thus V descends exactly. Continuous extensions at
removed points agree wherever they exist. In particular, a finite
peripheral cover does not prevent descent of the real regulator norm.

If C is preserved by complex conjugation iota, then iota^*omega=-omega.
Any primitive V_0 gives a unique conjugation-odd primitive

    V_odd=(V_0-V_0 composed with iota)/2.

Uniqueness follows since two primitives differ by a constant, which
cannot be odd. When the chosen representation component and its volume
are conjugation-compatible, this fixes the real normalization. That
compatibility is not assumed for every component; the marked Bloch lift
retains the normalization in the general case.

The subsequent [Regge/cover calculation](regge_period_covers_and_a_curves.md)
distinguishes this parameter-cover descent from a manifold cover.
The latter changes peripheral variables by an integer monomial
map, sends the geometric A-factor by elimination and multiplies
the marked regulator by the topological cover degree. Its quantum
boundary inclusion changes the commutation parameter by the
boundary degree. For the unordered ideal-shape parameter space,
the finite Regge action also needs its orientation local system:
an untwisted norm over its six orderings cancels the Bloch volume.
That is a failure to descend the same differential form, rather
than an exception to the descent argument above.

## 7. The general target after the geometric audit

The audited geometric existence input supplies a positive fundamental-
class representative for every hyperbolic knot. On the classical side
the existing Bloch-period notes give the marked regulator line and

    log||P_hyp||=2 Vol(M)/pi.

For the original Kashaev invariant, the required comparison is

    (4/n) log|<K>_n| - log||P_hyp|| -> 0.             (7.1)

The sign and scale differ from the later AK state comparison. Equation
(7.1) is still unproved. Sections 1--3 identify the intrinsic algebraic
comparison torsor. The subsequent
[Kashaev/ADO pointing calculation](kashaev_ado_pointing.md) supplies the
actual normalization line and its specialization at the Kashaev point.
It also proves that rational root-level states lie in a central v=1
sector. That sector need not be the geometric component of the
classical q->1 A-curve. The required comparison must retain the original
quantum family and its selected period, rather than assume these two
curves coincide. Compatibility with the marked geometric regulator
and the norm statement (7.1) remain unproved.

The subsequent [ramified Weyl-fibre theorem](ramified_weyl_fibre.md)
specifies the branch-point lattice for the actual normal ADO state.
Its invariant lattice retains the first negative-sector coefficient
as an ordinary fibre coordinate, and its full complete period is
the exact functional (eta_N/2)e_0^*b_0. Under generic rank one the
saturated kernel gives a pointed line even at a special rank jump.
An equivariant change of frame may fix the ordinary root fibre
and still change this coordinate, so a comparison must transport
the marked ramified fibre and functional. No equality of central
spectra or regulator norms is deduced from that construction.

The subsequent [actual threaded-character theorem](ado_threaded_shadow.md)
proves an additional distinction: the selected ADO evaluation has
abelian even-threaded interior data, whereas a null-homologous loop
separates the fixed complete hyperbolic character. Hilbert-90
frame descent cannot identify eigenlines with those different
scalar data. A source extension can instead select a horizontal
source-one eigenvector of a separating observable. Its actual
relative realization and norm comparison remain unproved.
