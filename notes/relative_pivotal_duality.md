# Oriented turns and duality of the actual relative source

Research note, 26 October 2026. This supplies explicit oriented duality
for the actual semicyclic modules, including its double-dual pivot,
and dualizes the retained affine source and carry lattices. Caps
necessarily meet a degenerate fusion character. The correct dual
lattice and a perfect finite linking form retain the state directions
that a generic cyclic fusion chart would lose there.

This is a construction within the prescribed quantum-group/ADO
definitions, not another knot invariant. It gives turns and source
pairings on an already specified actual tensor network. It does not
assign all geometric tetrahedron face modules, identify the global
relative gluing period, or prove its Bloch-regulator norm.

## 1. The exact semicyclic dual

Use [the genuine source module](semicyclic_carry_braiding.md)
V(x,phi), N>=2, q=exp(pi*i/N), Q=q^2:

    K v_a=x Q^(-a)v_a,
    E v_a=e_a(x)v_(a-1), E v_0=0,
    e_a(x)=[a]_q (x q^(1-a)-x^(-1)q^(a-1))/(q-q^(-1)),
    F v_a=v_(a+1), F v_(N-1)=phi v_0.

The actual coproducts and antipodes are

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F,
    S(E)=-E K^(-1), S(F)=-K F, S(K)=K^(-1).

On the ordinary linear dual the generator matrices are rho(S(h))^t.
Put k=x^N and define

    x_dual=x^(-1)Q^(-1), phi_dual=-k phi,
    c_a(x)=(-x)^a Q^(a(a+1)/2),
    J_x v_a=c_a(x) v_(N-1-a)^*.                  (1.1)

Then J_x is an isomorphism

    V(x_dual,phi_dual) -> V(x,phi)^*.              (1.2)

Here is a direct verification. The reversed K-inverse weights
are x^(-1)Q^(N-1-a)=x_dual Q^(-a). For a<N-1 the dual F
arrow is -x Q^(a+1)c_a/c_(a+1)=1. Its wrap is
-x phi c_(N-1)=-x^N phi, since c_(N-1)=x^(N-1).
The dual E coefficient is e_(N-a)(x)=e_a(x_dual), obtained by
q^N=-1 and [N-a]_q=[a]_q. The top dual vector is killed by E.
These verify all generators, without a generic simplicity argument.
In particular the central factor -k is retained at both parities.

When phi=0 the actual unrolled weight is also retained. If the
source highest weight is alpha, its dual highest weight is

    alpha_dual=2(N-1)-alpha.                       (1.3)

This has the K-root in (1.1), but the chosen H-lift in (1.3)
must be used for the full Cartan and twist factors. For phi!=0
the statement concerns the root quantum group with E,F,K;
no unrolled H-action on a wrapping weight string is asserted.

At the Kashaev color x=q^(N-1), x_dual=x and
c_a=q^(a^2). This is the self-duality already used in the
[ADO comparison](kashaev_ado_pointing.md), now with a fixed
normalization throughout the semicyclic family.

## 2. Double duality fixes the actual pivot exactly

Dualizing the parameters in (1.1) twice returns (x,phi). The
composition from the twice-dual standard frame to V** is

    J_x^(-t) J_(x_dual)=K^(1-N)=:g.               (2.1)

There is no scalar in (2.1). In the ordinary V**=V vector-space
identification its a-th diagonal entry is

    c_a(x_dual)/c_(N-1-a)(x)
       =x^(1-N)Q^(a(N-1)),

which is exactly g on v_a. The signs cancel using
Q^(N(N-1)/2)=(-1)^(N-1). This proves (2.1) uniformly at even
and composite levels.

Also S^2=Ad K=Ad g at the root, since K^N is central.
Thus the ordinary matrix double dual in these specific frames
has precisely the literature pivot used by the actual cut state.
It is not an independently selected determinant normalization.

In standard dual coordinates the left cap and cup are

    ev(v_a_dual tensor v_b)=c_a delta_(a+b,N-1),
    coev(1)=sum_a c_a^(-1) v_(N-1-a) tensor v_a_dual.
                                                        (2.2)
The right cap and cup are

    ev_right(v_b tensor v_a_dual)=c_a g_b delta_(a+b,N-1),
    coev_right(1)=sum_a c_a^(-1)g_(N-1-a)^(-1)
                              v_a_dual tensor v_(N-1-a).
                                                        (2.3)
The antipode identities make these actual Hopf module maps.
The four snake identities follow by contracting the single
matched index; c_a and its inverse cancel, as do the right
g factors. Closing an endomorphism A with (2.2)--(2.3) gives
exactly Tr(g A), with the original pivotal convention.

For a map A:V->W its turned map in these coordinates is

    A_dual=J_V^(-1) A^t J_W.                       (2.4)

This is contravariant under composition. For tensor products
the dual factors reverse order; the corresponding literal flip
is included. Thus turning a specified matrix identity, including
an allowed tetrahedral rewrite inside the actual network,
preserves it with its full scalar. One must use the turned map
(2.4), rather than insert a same-color formula on a dual color.

These statements give oriented turns on the actual colored
network. They do not identify an independently assigned geometric
tetrahedron face module with one of these duals, or establish
unrestricted S_4 symmetries of an unassigned face tensor.

## 3. A cap forces a fusion wall

The need for the relative source is already visible in the
central character. On V_dual tensor V the q-binomial identity
for the actual coproduct gives

    (Delta K)^N=k^(-1)k=1,
    (Delta F)^N=phi_dual+k phi=0.                  (3.1)

The reversed order V tensor V_dual gives the same zero, since
phi+k^(-1)phi_dual=0. Consequently the composite is on the
degenerate Borel fusion character even when phi!=0. A cyclic
factorization requiring a nonzero total F^N cannot be evaluated
at this cap by forgetting the wall. The explicit maps (2.2)
and (2.3) remain defined there and provide its canonical duality.

There is a second exact check:

    Tr g=x^(1-N) sum_(a=0)^(N-1) Q^(-a)=0.         (3.2)

Thus closing the distinguished scalar cut F_N(M)I with an
ordinary pivotal cap gives zero. The selected reduced cut and
the actual modified trace must be retained. In particular the
full factor remains the already specified

    d_N(M)=eta_N M^(N-1)/S_N(M^2),
    S_N(Y)=(1-Y^N)/(1-Y), eta_N=i^(N+3),           (3.3)

with its whole boundary germ. At M=1 it is eta_N/N. It is not
obtained by multiplying the identically zero ordinary closure
by a finite rational factor. Modified dimensions in this setting
are existing literature definitions; no replacement is proposed.

The later [actual meridian source](meridian_casimir_source.md)
identifies a further operator built from these very cups and caps.
At the Kashaev color their rank-one composition Pi has Pi^2=0
and actual pivotal partial trace identity. It is the nilpotent
part of the complete two-color Casimir projector with the fixed
factor (-1)^N(q-q^(-1))^2. The actual meridian source residue and
the nontrivial pure-braid action are explicit multiples of Pi.
This uses the full pivot above; an ordinary scalar closure or
the reduced eigenline alone would lose that source test.

## 4. Dualizing the affine quantum-A source retains a co-source

This duality has a direct form for the
[inhomogeneous quantum-A system](affine_quantum_a_period.md).
On a common difference base write

    sigma(w)=U w, U=[C c;0 1], w=(v,1)^t.

The dual column has transport U_dual=U^(-t), explicitly

    U_dual=[ C^(-t)           0 ],
           [ -c^t C^(-t)     1 ].                 (4.1)

Indeed U_dual^t U=I, so the pairing of a dual horizontal
column with w is sigma-invariant. Equation (4.1) reverses
the extension: the source quotient becomes a trivial submodule,
with the displayed nonzero lower off-diagonal term. This term
is called the co-source here only to indicate that reversal.
Deleting it is not dualizing the specified extension.

For a source line with multiplier d instead of 1 the lower
row is [-d^(-1)c^t C^(-t),d^(-1)]. Thus a nontrivial source
line is dualized too, rather than first replaced by a trivial
quotient. This applies to the full two-direction factorial
extension and to its tensor sources.

If a comparison is w'=A_aug w, the corresponding dual comparison
is A_aug^(-t). Their paired period is unchanged exactly. The
same construction works in every commuting shift direction;
inverse transpose carries each flatness equation to its dual.

For the [factorial source](factorial_source_torsor.md) the
internal matrix [a b;0 1] therefore has dual

    [ a^(-1)      0 ],
    [ -b/a        1 ].                             (4.2)

The meridian source norm V=(1-UC)/(1-U) becomes V^(-1) on
the dual. Interior dual pairings cancel these full functions
and their specified comparison roots before any specialization.
The raw non-scalar cut loop is also paired with its full
inverse transpose; its off-diagonal source is not omitted.
Unpaired boundary factors, including (3.3), remain in the
selected period. This is an algebraic explanation for internal
normalization cancellation when the actual duality data match;
it is not a repair of an unrelated positive factorial model.

At a zero of a, (4.2) can have a pole. Its extension on a
lattice is handled by dualizing the retained lattice, not by
evaluating that displayed fraction separately.

## 5. The dual carry source and its perfect linking pairing

Let R=k[[epsilon]], F=k((epsilon)), and use the two lattices
proved in [the carry construction](carry_recoupling_lattice.md):

    L=Lambda_leaf=direct_sum_i R e_i,
    C=Lambda_carry=direct_sum_i epsilon^(-kappa_i) R e_i,
    kappa_i=floor((i_1+...+i_b)/N).

For any lattice A let A_sharp={ell in V* : ell(A) subset R}.
Then duality reverses the inclusion:

    C_sharp=direct_sum_i epsilon^(kappa_i) R e_i^*
       subset L_sharp=direct_sum_i R e_i^*.        (5.1)

Put Q=C/L and Q_dual=L_sharp/C_sharp. There is a canonical
perfect R-balanced linking pairing

    Q times Q_dual -> F/R,
    (c mod L,ell mod C_sharp) -> ell(c) mod R.      (5.2)

It is well defined: adding a member of L or C_sharp changes
the value by an element of R. In the displayed diagonal
bases each positive kappa contributes

    R/(epsilon^kappa) times R/(epsilon^kappa) -> F/R,
    (f,g) -> epsilon^(-kappa) f g mod R.           (5.3)

This is nondegenerate on both sides, as can be checked on the
lowest nonzero coefficient of either input. It proves perfectness.
Equivalently Q_dual=Ext_R^1(Q,R), by dualizing 0->L->C->Q->0;
both lattice modules are free and Hom_R(Q,R)=0.

For the fixed normal coordinate epsilon, the residue of (5.2)
against d epsilon is the finite k-valued pairing

    (f,g) -> [epsilon^(kappa-1)] f g.              (5.4)

In bases 1,epsilon,...,epsilon^(kappa-1) its matrix is the
anti-diagonal identity. Only jets of order at most
floor(b(N-1)/N)-1<=b-2 occur, independently of N for fixed b.
The F/R pairing is intrinsic; the scalar residue convention
uses the marked normal coordinate, which is retained.

In particular there is a perfect pairing

    Tor_1^R(Q,k) times (Q_dual/epsilon Q_dual) -> k. (5.5)

On each summand, the Tor class is the socle epsilon^(kappa-1)
and the dual residual class is represented by 1, so (5.4)
equals one. The connecting map identifies this Tor class with
the actual leaf direction killed by L/epsilon->C/epsilon.
Thus (5.5) gives a canonical cap for those lost directions,
rather than treating their ordinary image as the whole state.
Its dimension is N^b-binomial(N+b-1,b).

## 6. Integral recoupling and turned contractions

For every tree the actual evaluation has I_T=J_kappa M_T,
M_T in GL_(N^b)(R), J_kappa=diag(epsilon^(-kappa_i)).
Its dual evaluation is forced by preservation of the pairing:

    I_T_dual=(I_T^(-1))^t=J_kappa^(-1) M_T^(-t).   (6.1)

It has image C_sharp. The actual source in the tree chart is
B_T=I_T^(-1)L, and its full dual source is

    B_T_sharp=I_T^t L_sharp.                      (6.2)

These statements follow directly by evaluating the pairing.
They distinguish the dual of the basic carry lattice from
the larger dual of the actual source. The row ell I_T can
have poles in a basic tree frame while still belonging to
B_T_sharp and evaluating integrally on B_T. Replacing it by
an arbitrary regular vacuum row can lose (5.5).

A tree change I_(T')^(-1)I_T transports its dual by inverse
transpose. All compositions, loops and paired interior maps
cancel exactly. The same holds for a genuine braid map
preserving both lattices and its appropriately typed dual.
Because J_x in (1.1) has unit entries whenever x is a unit,
its orientation change preserves the original leaf lattice
at the nilpotent boundary. Equations (6.1)--(6.2), rather
than a new unit pointing, specify its recoupled dual source.

For an already specified finite actual network these maps
therefore give consistent cups, caps, oriented turns and
dual affine sources, with the entire cut evaluation retained.
This resolves this part of the exterior data needed to use
the [root tetrahedral pentagon](cyclic_tetrahedron_pentagon.md).
It does not supply every face identification on the positive
geometric triangulation, a comparison of its projected source
with the actual one, or the selected Bloch-regulator norm.
The carry normal coordinate is not thereby identified with
the meridian normal coordinate or a regulator realization.

### 6.1 Reversing a triangle fixes its relative algebra

The ordered relative operators for two quantum affine modules are

    D=X_1+Y_1 Y_2^(-1), Z=-Y_1 Y_2^(-1)X_2,
    DZ=QZD.

Reverse the tensor factors and replace each by its Hopf dual.
Construct D_rev,Z_rev by the same ordered formula in that
reversed product. After the literal flip identifying its
underlying dual vector space with the dual of the old product,
the exact operator identities are

    D_rev^t=-Z^(-1)D, Z_rev^t=Q Z^(-1).            (6.3)

For example put S(Y_i)=-X_i^(-1)Y_i. Transposing the reversed
formula gives

    D_rev^t=X_2^(-1)+S(Y_1)^(-1)S(Y_2)
           =X_2^(-1)(1+Y_1^(-1)X_1Y_2)=-Z^(-1)D.

The second calculation gives
-X_1^(-1)Y_1^(-1)X_1X_2^(-1)Y_2=QZ^(-1).
This proves the phase and ordering without an unrecorded
face-orientation convention.

If D^N=lambda_R and Z^N=mu_R, (6.3) gives

    (lambda_R,mu_R) -> (-lambda_R/mu_R,1/mu_R).    (6.4)

On a normalized Steinberg face lambda_R+mu_R=1 this is an
ordinary cross-ratio shape change. Its operator lift includes
the transpose and Q in (6.3); central shapes alone do not
determine the turned vector or covector.

### 6.2 The triangle face pairing is induced, with its scalar fixed

Let g,h have matched endpoints c->d and a->c. Assume their
three affine characters are nondegenerate. Use the existing
pointed factorization maps

    C_gh:E_gh tensor R_gh -> E_g tensor E_h,
    C_rev:E_(gh)^(-1) tensor R_rev -> E_(h^(-1)) tensor E_(g^(-1)).

Their columns are the already proved finite expressions
X_total^i D^j(1 tensor 1); no new quantum kernel is chosen.
Let J_g,J_h,J_total be the endpoint caps with the actual
source normalization of Section 7. Their edge root markings
are retained. A product total mark is one local source
choice; globally the total cap is the already assigned cap
of that edge, including its prescribed dual mark. With P
the literal flip, form

    B=C_gh^t (J_g tensor J_h) P C_rev.             (6.5)

There is a unique invertible face pairing M_gh such that

    B=J_total tensor M_gh.                        (6.6)

To prove this, (6.5) intertwines the total algebra with its
Hopf dual, since each endpoint pairing and both C maps do.
After removing J_total on that factor, it commutes with
the full matrix algebra of E_(gh)^(-1). Its commutant is
I tensor End(R), so it equals I tensor M_gh. Every matrix
in (6.5) is invertible, proving invertibility of M_gh.
In particular its entire scalar is determined. An explicit
finite formula is

    M_gh=(1/N)Tr_total[(J_total^(-1) tensor I)B].  (6.7)

Equation (6.3) proves that M_gh intertwines the reversed
relative module with the indicated transposed relative
operators. Thus the face algebra as well as its pairing
has been specified. Its reversed unit becomes M_gh e_0,
which can be a nonconstant covector in the old monomial
dual frame. This vector is retained in selected periods.

These pairings are coherent on every specified recoupling
diagram. For a tree T write

    B_T=I_T^t B_leaf I_(T,reverse).

If F=I_(T')^(-1)I_T and F_rev is the corresponding reverse
tree change, then exactly

    B_T=F^t B_(T') F_rev.                          (6.8)

Substitution proves (6.8) with scalar one. Consequently the
face pairings transported by these C maps respect the
recoupling pentagon, without an independent face scalar
or a reset of its unit vector. At a wall, whole identities
are interpreted on the actual paired lattices of (6.1)--(6.2)
and their retained source quotients. No separate invertible
specialization of every generic matrix is assumed.

This constructs dual face data for the matched-endpoint
recoupling network. It does not identify every independently
assigned geometric tetrahedron face with that network,
establish all uncolored tetrahedron ordering moves, or
identify its selected positive geometric source. Those are
the remaining global comparison questions.

The subsequent [oriented source calculation](oriented_tetrahedron_source.md)
now treats shared edge marks, exact full reversal and cyclic
face orderings with these caps. The raw cyclic rotation has
a non-scalar inverse-pivot defect; an explicit Weyl and
central correction with its cubic phase gives coherent face
orderings preserving M. A separate full tetrahedron vertex
test still fails for the bare tensor, with an exact N=2
counterexample. Thus these face constructions do not yet
justify a direct uncolored geometric tetrahedron assignment.

## 7. A cyclic endpoint cap matches the actual source frame

There is also a direct comparison with the matched endpoint
modules used by the pointed tetrahedral recoupling. Use the
quantum affine Hopf algebra

    XY=QYX, Delta X=X tensor X,
    Delta Y=X tensor Y+Y tensor 1,
    S(X)=X^(-1), S(Y)=-X^(-1)Y.

For g=(lambda,mu), with nonzero lambda,mu, take the existing
endpoint module

    E_(g;a,b)=k[z]/(z^N-lambda),
    X f=z f, Y f=(b-a z)f(Q^(-1)z),
    b^N=lambda a^N+mu.                            (7.1)

Its inverse affine character is g^(-1)=(lambda^(-1),-mu/lambda),
with reversed endpoints b->a. Write tau for the normalized
field-algebra trace, tau(f)=(1/N)Tr(multiplication by f).
The explicit duality map J_B is the pairing

    <f,h>_B=tau_z( f(z^(-1))h(z)/(a-b/z) ),
    f in E_(g^(-1);b,a), h in E_(g;a,b).           (7.2)

The denominator is a unit when mu!=0, so this is a perfect
pairing. X-duality follows by multiplication by z^(-1).
For Y-duality change z to Qz in the trace. The weight
w(z)=1/(a-b/z) obeys

    w(z)(a-b/z)=w(Qz)(a-b/(Qz))=1,

which proves the antipode pairing equation. Thus the pointed
unit on the inverse endpoint module is transported to a
specified weighted trace functional, rather than reset to
an arbitrary unit covector.

The unnormalized endpoint double dual is

    J_B^(-t) J_(B,inverse)=-X^(-1).               (7.3)

For a proof, the weight for the inverse endpoint pairing,
expressed back in z, is 1/(b-a z)=-z^(-1)w(z).
This gives (7.3) directly. The sign is therefore part of the
endpoint normalization; it cannot be silently identified
with a different pivotal frame.

Now make the actual quantum-group comparison. Set

    lambda=x^(-N), mu=phi,
    r_i=x^(-1)Q^i,
    d_i=product_(s=1)^i(b-a x^(-1)Q^s).

The evaluation matrix H_(ij)=r_i^j identifies polynomials
with functions at the N roots. In that basis Y has entry
b-a r_i from i-1 to i. Consequently the exact frame

    A_g=H^(-1)diag(d_0,...,d_(N-1))               (7.4)

takes the actual K^(-1),F_phi matrices to X,Y. Its dual
counterpart A_inverse uses x_dual=x^(-1)Q^(-1) and the
reversed endpoints. Both frames are invertible when mu!=0.
The actual vector v_0 maps to the idempotent supported at r_0.
The endpoint unit has actual coordinates sum_i d_i^(-1)v_i.
These are the specified vector transports to use in a period;
module duality alone does not identify the two selected lines.
The transported endpoint unit solves
(F_phi+a K^(-1)-b)sum_i d_i^(-1)v_i=0 exactly.
The paired cap in the actual bases is exactly

    A_g^t J_B A_inverse=c(x;a,b) J_x,

    c(x;a,b)=-1/(N xQ)
                product_(s=1)^(N-2)(b-a x^(-1)Q^s).   (7.5)

To prove (7.5), both matrices intertwine the same K,F
algebra, which is the full matrix algebra when phi!=0.
Their ratio is scalar. The entry pairing the dual zeroth
vector with the original (N-1)st vector is

    d_(N-1)/(N(a-bxQ)).

Cancel its last factor b-a x^(-1)Q^(-1) to get (7.5).
This determines the full scalar from the actual source
frame, with no determinant-root choice.

The finite product also gives

    c(x_dual;b,a)=-x^N c(x;a,b).                  (7.6)

For example, reverse the exponents s=1,...,N-2 and use
Q^(N(N-1)/2)=(-1)^(N-1). Thus the source-normalized endpoint
pairing J_B/c has double dual

    (J_B/c)^(-t) (J_(B,inverse)/c_inverse)
       =lambda X^(-1)=X^(N-1).                   (7.7)

Under the actual Hopf identification X=K^(-1), this is
precisely K^(1-N). Equations (7.5)--(7.7) prove that the
cyclic endpoint cap, with its finite-factorial source frame,
has the actual pivotal normalization at every parity. The
normalization is a full function on the marked endpoint
cover before any peripheral evaluation.

The nilpotent boundary shows concretely why the source must
be retained. Choose a=x and let b tend algebraically to 1,
so phi=b^N-1. On the original side d_i=(Q;Q)_i at b=1,
all nonzero for i<N. The inverse endpoint frame instead has
diagonal factors

    d'_j=x^j product_(s=1)^j(1-bQ^(s+1)).

At b=1 its last factor d'_(N-1) vanishes simply; the other
diagonal factors are nonzero. At the same time (7.2) has a
simple pole in its root component z=x^(-1). The complete
product (7.5), after cancellation, has the regular value

    [A_g^t J_B A_inverse]_(b=1)
         =J_x/[x(1-Q)].                           (7.8)

Indeed product_(s=1)^(N-1)(1-Q^s)=N gives
c(x;x,1)=1/[x(1-Q)]. Thus the whole cap is nondegenerate
even though its separate inverse endpoint frame has rank
N-1 after ordinary specialization.

The missing last column in (7.8) comes from multiplying
the simple pole by the first normal coefficient of
d'_(N-1). Deleting that coefficient gives a zero last
column and cannot yield the actual cap. This is an explicit
instance of the linking pairing (5.2)--(5.5), with a single
normal source direction. No analytic limiting argument or
replacement of the actual invariant is involved.

There is also uniform normalization control on this actual
boundary. At the Kashaev color |x|=1, (7.8) gives exactly

    |c(x;x,1)|=1/(2 sin(pi/N)),
    N/(2pi)<=|c(x;x,1)|<=N/4.                     (7.9)

The elementary bounds 2/N<=sin(pi/N)<=pi/N prove the
inequalities. The nonzero entries of J_x and of the actual
pivot all have modulus one there; a cap or cup has operator
norm sqrt(N). The scalar endpoint comparisons and their
inverses have polynomial size. A fixed finite composition
of these turn maps has an operator norm bounded by a fixed
power of N. Such an upper bound gives no lower bound for
the value of a cap on a specified tensor. Nonvanishing and
cancellation in the selected global contraction, and the
norm of an arbitrary moving endpoint frame, remain separate.

The selected endpoint units also have a literal relative
period interpretation. Equation (7.2) gives

    <1,1>_B=-a^(N-1)lambda/mu,
    <1,1>_(B/c)=-a^(N-1)lambda/(mu c).            (7.10)

To prove it, use
tau((b-a z)^(-1))=b^(N-1)/(b^N-a^N lambda) and
z/(az-b)=(1/a)(1-b/(b-az)). These are finite algebraic
trace identities. For a=x, mu=b^N-1 the exact normal
coefficient is therefore

    [mu <1,1>_(B/c)]_(mu=0)=-(1-Q).              (7.11)

This is nonzero at every N>=2. It is an evaluation of the
regularized algebraic period, equivalently the residue of
<1,1>_(B/c) d mu. In the normal coordinate b-1 its leading
polar coefficient has the additional factor 1/N; the two
normal coordinates are not conflated. This identifies a
specific local source as a marked cyclic period residue,
with its normalization fixed by the actual pivot. The
internal cap coordinate mu has not thereby been identified
with a peripheral meridian coordinate or with a global
Bloch-regulator realization.

This closes a marked local duality comparison between the
cyclic endpoint module used in recoupling and the actual
quantum-group source. Its tensor products, duals and
already specified exterior contractions transport with
their full factors. It does not yet identify all geometric
tetrahedron face data or the selected global source on a
positive ideal triangulation.

## 8. Coverage and independent checks

Duality, pivotal traces and torsion linking pairings are standard
structures; no novelty is claimed. The actual pivot and state
definitions are those already fixed from
[Brown--Dimofte--Garoufalidis--Geer, 2005.08176](https://arxiv.org/abs/2005.08176).
The abstract of
[Geer--Patureau-Mirand--Turaev, 0711.4229](https://arxiv.org/abs/0711.4229)
already covers nonzero modified dimensions when ordinary
dimensions vanish, including the nilpotent quantum-sl(2)
invariants containing Kashaev's invariant. The independent
calculations here concern the exact source frame, pivot,
duality maps and lattice pairing in the current conventions;
no published modified-trace proof is a premise.

[The exact audit](../experiments/audit_relative_pivotal_duality.py)
checks 36 duality cases at generic/Kashaev colors and nilpotent/
nonzero wraps for N=2,3,4,5,6,8,9,10,12. It verifies all generator
intertwinings, all four snake identities, Hopf caps/cups, the
exact double-dual pivot, the forced central degeneration and
the zero ordinary bubble. Explicit turns recover the entire
scalar cut in 30 actual braid cases, with the original pivot
and framing. Nine two-direction factorial extensions have flat
dual sources, reciprocal full meridian norms and the paired
non-scalar cut loops. Eighteen cyclic endpoint caps match
the actual dual frame with their explicit finite-factorial
scalar and exact pivot; their complete nilpotent cap remains
nondegenerate with the lost first normal coefficient retained.
Ten carry quotients have perfect balanced
residue forms and perfect lost-fiber pairings. All pass.
Nine reversed triangle algebras verify (6.3)--(6.4), including
the exact Q and transpose. Nine induced face pairings verify
(6.5)--(6.7), their invertibility, scalar and both relative
generator intertwinings. Their unit transport also exhibits
the required nonconstant covector. These checks all pass.
[Results](../experiments/relative_pivotal_duality_results.json).

    python3 experiments/audit_relative_pivotal_duality.py

The subsequent [source flag carry extension](source_flag_carry_extension.md)
now extends ordered source/tree frames through the marked
source infinity on the common carry lattice. Its maps
preserve the actual sublattice and transport the full dual
by inverse transpose, so the linking form and lost normal
directions remain paired there. The original whole cut and
all peripheral factors are retained. It does not separately
specialize a polar endpoint cap or identify the global
geometric source and regulator norm.

The uniform proofs above, rather than the finite samples,
establish the stated dualities. The global marked geometric
period comparison and the volume conjecture remain unproved.
