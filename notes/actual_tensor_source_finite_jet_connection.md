# A flat finite-jet connection for the actual tensor source

30 October 2026. Independently reviewed. The specified generic
white tensors, cups and categorical duals have exact moving-period
head transport. After imposing their ORIGINAL integral affine head
constraints, this gives explicit commuting differential/rational
operators on every finite order of genuine quantum jets. The root
parity character is retained. Divisors, the finite support and the
original exposed-head trace normalization are retained as well.

This is a statement about the actual continued tensor summand. It
does not identify its finite sum with a periodic sum, move its residue
cycle across a divisor, or prove that a geometric saddle contributes.

## 1. The local source factors and their exact shifts

Fix N>=3, d=N-1, zeta=exp(pi i/N+epsilon),

    P=pi i/Log zeta, Q=zeta^2,
    eta=exp(2pi i P), Delta=N-P.                         (1)

All highest weights and finite polynomial degrees remain FIXED
integers as epsilon varies. Use the actual large-channel white
continuation from the [generic source theorem](actual_generic_boundary_gauge_and_source.md):

    W_a(i,j;r)=(-1)^m zeta^[-dr+di-m(m-1)]
                     H_m^(Q^(-N))(Q^i,Q^j)/F_m,
    m=d-a, i+j=m+r, F_m=(Q;Q)_m.                        (2)

It is the original generic W_a:V_(2a)->V_d tensor V_d, including
both physical degree halves. The channel is m=d-a, not its
root-colliding small partner a. For ANY integers p,q, (2) gives

    W_a(i+Pp,j+Pq;r+P(p+q))=(-1)^(d q) W_a(i,j;r).      (3)

Indeed Q^P=1 leaves the finite polynomial arguments unchanged,
and the remaining exponent is -dPq. In particular shifting i by
P at fixed i+j multiplies W by (-1)^d. The two physical legs
are ordered; the asymmetric form of (3) is intentional.

Use the specific moving-period factorial of the
[factorial theorem](actual_moving_period_factorial_normals.md), with

    Fhat_P(z+P)=[1-exp(2pi i z)]Fhat_P(z).

For an actual fixed highest weight L<N, its continued ordered cup is

    p_L(x,L-x)=exp(pi i x) zeta^[x(L-x-1)]
                       Fhat_P(x)Fhat_P(L-x)/F_L.          (4)

The physical cup has the additional, head-independent factor
N zeta^(-d^2). Put Y=exp(2pi i x). Direct substitution, retaining
both the quadratic monomial and exp(pi i x), gives

    p_L(x+nP,L-x-nP)=mu_(L,n)(P,x) p_L(x,L-x),
    mu_(L,n)=(-1)^(Ln) (1-Y)/(eta^(-n)-Y), n in Z.       (5)

For n=1 the two factorials contribute
(1-Y)/(1-eta^(-1)/Y); the monomials contribute
(-1)^(L-1)/Y. This is (5). Repetition telescopes, and reversing
the shift proves the formula for negative n. These are meromorphic
identities, also where a displayed ratio must be cleared first.

The cap is the ACTUAL matrix inverse, so

    ell_L(x,L-x)=1/p_L(L-x,x).                            (6)

Its multiplier is 1/mu_(L,-n)(P,L-x), not the inverse of
mu_(L,n)(P,x). This distinction keeps the cyclic and pivotal
normalizations. Physical cup and cap scalars remain in the tensor.
The generic Chevalley monomial zeta^[-(L+1)x] has multiplier
(-1)^((L+1)n), and the original pivotal clock
(-1)^L zeta^(L-2x) has multiplier one. Integer affine characters
exp[2pi i ell(heads)] have multiplier eta^(ell(n)).

Categorical white duals are expanded in their original ordered
W, cup, cap and reversal factors. Thus (3)--(6) apply to their
actual finite source, without replacing a dual by an adjoint or
dividing by its root norm. Scalar channel weights, fixed generic
normalizers and the original half-twist eigenvalues do not depend
on magnetic heads and are unchanged by these shifts.

## 2. The actual affine head lattice

Take a fixed typed tensor network built from these factors, its
original physical turns, and recorded integer affine characters.
Fix an admissible assignment of the finite channel labels. Impose
every literal head equation, including

    i+j=m+r at a white vertex, x+y=L at a cup or cap,

and equality of each pair of contracted indices. Write the resulting
integer affine system as B h=b. Choose one integer solution h0
and a Z-basis A of ker_Z B, and set

    h=h0+A x, x in C^k.                                 (7)

This is a primitive free lattice parametrization. Indeed ker_Z B
is saturated: Z^n/ker_Z B is isomorphic to the free subgroup
im_Z B of Z^rows. The chosen basis also spans the complex kernel.
An inconsistent channel assignment has no original summands and
is discarded. The original finite admissibility inequalities are
kept separately; (7) does not remove or wrap them.

Let S(epsilon,x) be the MEROMORPHIC summand obtained from the
specified continuations (2),(4),(6), retaining all scalars, ordering
and characters. It agrees with the actual generic summand at every
admissible integer head assignment. Any exposed boundary heads are
held fixed, or their explicitly chosen factors and their constraints
are included in (7); an arbitrary boundary environment is not
silently assigned a continuation.

Use an admissible generic stratum of these head equations. A factor
whose head argument is constant on this chart is left as its original
constant source factor. In particular an admissible physical integer
cup is evaluated by its finite factorials. A forbidden constant polar
stratum is not made into a source by substituting into a 0/0 ratio:
keep its originally zero summand as zero, or use a separately proved
generic cancellation. No transport is asserted for an undefined
constant polar interpolation.

For b in Z^k, every local head changes by an integer multiple of P
under x->x+Pb. Multiplying the LITERAL local identities gives

    S(epsilon,x+Pb)=C_b(P,x) S(epsilon,x).                 (8)

The multiplier C_b is explicit: multiply the signs (3), the cup
factors (5), the inverse factors at the reversed cap arguments (6),
and the stated clock/character factors. In particular it belongs
to the rational field generated by eta and

    Y_l=exp(2pi i z_l(x)),

where each z_l is the corresponding integer affine head argument.
There are no omitted Fourier or peripheral characters. Since N is
an integer, each multiplier is N-periodic in every free coordinate.
Its root value, on a chart avoiding Y_l=1, is the explicit sign

    C_b(N,x)=chi(b) in {1,-1}.                            (9)

The sign is a lattice character. It includes the white-leg signs
and the parity of each actual highest weight; it is not reset to
one when N changes parity. Any additional boundary character must
be explicitly transported before extending this source class.

The construction also works termwise for the finite channel sum.
For the usual matching source the homogeneous head system is the
same for all channel assignments, each channel weight 2a is even,
and h0 is integral. Require also that the integer LINEAR coefficients
of every separately recorded head character be unchanged across the
assignments. Thus, whenever a common primitive basis is used and
this character-coefficient condition holds,
the same C_b applies to that sum: exp(2pi i h0)=1 and the local
parities are unchanged. This concerns only the chosen algebraic
extensions of the summands on their admissible strata. Their
support-dependent cycles remain separate; it does not create a
single unconstrained periodic sum. If a different source has label-dependent
parity, character coefficients or different homogeneous constraints,
retain the corresponding
finite vector of summands and its diagonal transport instead of
asserting a common multiplier.

There is an explicit rational trivialization, obtained from the actual
cup rather than an existence theorem. Put

    g(z)=exp(2pi i z)/[1-exp(2pi i z)].

Then g(z+nP)/g(z)=(1-Y)/(eta^(-n)-Y), so p_L/g has the
constant P-shift character (-1)^(Ln). For each factor of the
network put one g at the cup's first argument, and an inverse g
at the literal cup argument used by an inverse cap. Multiply these
factors and all separately retained exp(2pi i ell(heads)) characters:

    G(x)=product_cup_factors g(z_l(x))^(e_l)
                   *exp[2pi i ell(h0+A x)], e_l=+1 or -1. (9a)

The product in (9a) includes ONLY cup/cap arguments which are
NONCONSTANT on the chosen free chart. A constant argument has shift
number zero and multiplier identically one, so requires no g factor;
in particular we never insert the undefined g of a fixed integer.
Simplify mu_(L,0)=1 before evaluating any such constant argument.
The cap argument in (9a) is L-x when its first matrix index is x.
White, Chevalley and clock factors require no additional rational
gauge. Thus G is a SPECIFIED rational function of the marked head
exponentials, independent of P, and

    C_b(P,x)=chi(b) G(x+Pb)/G(x).                         (9b)

Equivalently S/G is P-quasiperiodic with exactly chi. This is an
algebraic identity on the meromorphic source; the zeros and poles
of G are part of the identity. In particular G can be singular on
the original physical lattice. It is not an allowable reason to
delete a factor from a period integral.

Nor is this rational gauge automatically subexponential on scaled
complex charts. For z=N(x+iy) with fixed y>0,
|g(z)|=exp(-2pi N y)(1+o(1)). Thus G can contribute to the
leading action as well as to divisor residues. Conjugating the
transport does not normalize away that contribution or the volume;
any asymptotic source calculation must retain it.

## 3. A genuine commuting finite-jet representation

Take Taylor jets of the actual source after its proved generic
cancellations, on a head chart where it is regular in epsilon.
If an intermediate decomposition has a known scalar pole of order M,
first multiply it by epsilon^M; recovering its original Laurent
coefficients then requires the corresponding higher Taylor order.
No principal part is discarded by the transport construction.

Let D_b be the constant directional derivative in direction b and
M_f denote multiplication by f. Since x+Nb=(x+Delta b)+Pb,
(8) gives the exact local identity

    S(epsilon,x+Nb)=T_b S(epsilon,x),
    T_b=exp(Delta D_b) M_(C_b).                           (10)

In this formula the derivative acts on BOTH C_b and S. Modulo
epsilon^(J+1) it is the explicit finite differential operator

    T_b^(J)=sum_(r=0)^J Delta^r D_b^r M_(C_b)/r!
                                        mod epsilon^(J+1). (11)

Only the order-J Taylor coefficients of the rational multiplier
are needed. Its coefficients are rational in the marked Y_l and
retain their divisors; no infinite Taylor series is required for
a finite quantum jet.

These operators commute and represent the free head lattice, not
merely when applied to the particular source. The rational gauge
makes the statement especially explicit. Since G(x+Nb)=G(x),
(9b),(10) give the exact operator identity

    T_b=chi(b) M_G exp(Delta D_b) M_(G^(-1)).              (11a)

Thus all the operators are simultaneous conjugates of ordinary
translations. This proves their group law directly. Equivalently,
the local multipliers obey the exact P-shift cocycle

    C_(b+c)(P,x)=C_b(P,x+Pc) C_c(P,x).                    (12)

This follows either directly from (3),(5), or by composing the
literal meromorphic identities. Their N-periodicity gives
C_b(x-Delta c)=C_b(x+Pc). Hence, as operators on local meromorphic
functions,

    T_b T_c
       =exp[Delta D_(b+c)] M_(C_b(x-Delta c)C_c(x))
       =T_(b+c)=T_c T_b.                                (13)

The same holds after finite-jet truncation. Normalize by the retained
root character, U_b=chi(b)^(-1)T_b^(J). Since Delta is in
(epsilon) and C_b/chi(b)=1 mod epsilon,

    (U_b-I) raises the epsilon filtration,
    product_(r=1)^(J+1)(U_(b_r)-I)=0.                    (14)

Thus the normalized transport is a commuting unipotent representation
on finite jets of the ACTUAL tensor summand. Its inverses are finite
geometric series, or simply U_(-b). The number of vertices need not
be small; J is the chosen finite derivative order. This is a local
statement in the meromorphic coefficient field, not a bound near its
poles or a nilpotence theorem for global source periods.

Its logarithmic connection is explicit as well:

    U_b=exp[Delta nabla_b] mod epsilon^(J+1),
    nabla_b=D_b-D_b Log G=M_G D_b M_(G^(-1)).             (14a)

These commuting derivatives have the recorded simple logarithmic
poles along the integral-head divisors of (9a). No unspecified
gauge or discarded boundary character enters their construction.

For clarity, write S=S0+epsilon S1+O(epsilon^2), and
C_b=chi(b)[1+epsilon c_b1+O(epsilon^2)]. Since
P'(0)=iN^2/pi, (10) is

    S0(x+Nb)=chi(b) S0(x),
    S1(x+Nb)=chi(b)[S1-P'(0)D_b S0+c_b1 S0].             (15)

For a cup factor with argument z_l and shift number n_l,
its contribution to c_b1 is

    2pi i P'(0) n_l/[1-exp(2pi i z_l)].                  (16)

For an inverse cup use its literal argument and the negative of
this contribution. An eta^k character contributes 2pi i P'(0)k.
White and clock signs have zero derivative. Thus (15) is explicit
even before a particular network is chosen. The simple poles in
(16) are essential genuine normal terms.

## 4. A concrete exceptional-operator connection

The [literal generic exceptional lift](actual_matching_edge_generic_deficient_operator_lift.md)
is an example with three free coordinates (t,u,v). Put

    r=a-v+u, ell=t-v, Y_r=exp(2pi i r),
    Y_v=exp(2pi i v), Y_ell=exp(2pi i ell), s=d-2a,
    A(Y)=(1-Y)/(eta^(-1)-Y),
    B(Y)=(1-Y)/(eta-Y).

Applying the two actual large whites, the Chevalley scalar and the
three ordered cups of that lift gives

    C_u=(-1)^s A(Y_r),
    C_v=(-1)^s B(Y_r)/[A(Y_v)B(Y_ell)],
    C_t=1/A(Y_ell).                                     (17)

These are identities for the full generic polynomial kernel and for
its completed version: the moving face scalar is independent of
t,u,v. They preserve the retained exp(-2pi i v) root character;
that character is one under an integer N-shift but not under a
moving P-shift. It must not be erased before forming (17).

Equation (17), including its cocycles, is a short source-specific
certificate for the abstract-looking operators (10). Its poles
include the actual channel-row divisors of the continued kernel.
The formulas do not replace that kernel by its phase-canceled
root value before differentiation.

Here the rational gauge (9a) is particularly short:

    G_K=g(r)/[g(v)g(ell)]
       =exp[2pi i(u-v-t)]
                    (1-Y_v)(1-Y_ell)/(1-Y_r).            (17a)

Substitution in (9b) reproduces all three multipliers (17), with
chi_u=chi_v=(-1)^s and chi_t=1. Formula (17a) includes its
integer exponential and its actual channel-row pole.

## 5. Ordinary closure, the exposed mark, and remaining scope

For the original marked invariant use the SAME exposed physical
head and its actual generic ordinary pivotal closure. If
F(epsilon) is that finite closed source, its normalization is

    D_N(epsilon)=(-1)^d[N]_(q0 exp(epsilon)),
    nu_N=D_N'(0)=2N(-1)^N/(q0-q0^(-1)),
    Z=F'(0)/nu_N.                                       (18)

The transport above applies to its actual continued ordinary
summand and its retained first jet before carrying out this
normalization. It does not create a generic continuation of the
bare dense root mark. If an off-root marked row is specified, it
must be transported covariantly with its original cup; otherwise
the ordinary closure and (18) are the available source theorem.
Likewise a regular Hopf lift of a complete-circle coupon and the
literal moving-q exceptional polynomial are distinct generic germs.
Use whichever has actually been specified; (10) never identifies
them merely because their root values agree.

At the original lattice, Y_l=1. The normalized rational operators
can therefore have poles even where the complete source has a
removable cancellation. Equalities (8),(10) hold meromorphically,
and may be cleared of denominators before specialization. They
are not permission to discard a residue or apply an individual
singular factor to a root value without its full generic germ.

Finally, a shift of the summand does not preserve its finite
admissibility polytope. A residue-cycle representation also has its
own cotangent factors and boundary. To pass from (10) to a global
period identity one must carry that original cycle, its crossed
divisors and all affine mark/peripheral characters. No such cycle
deformation or nonzero selected contribution is proved here.

## 6. Focused source checks

The [focused audit](../experiments/audit_actual_tensor_source_finite_jet_connection.py)
and [saved results](../experiments/actual_tensor_source_finite_jet_connection_results.json)
verify the rational trivialization and all three literal exceptional
kernel multipliers, their cocycles and first-normal connections, and
a shared integral head chart. Independent evaluations of the original
large white polynomial, moving-factorial cups and the full generic
completed kernel check 24, 6 and 6 moving-period shifts respectively.
Three genuine fixed-N transports include first and second normals.
The largest relative identity error at 85 digits was below 1.2e-82.
These checks do not replace the arbitrary-network multiplication and
operator proofs, and make no assertion about a transported period.

Independent full analytical reviews by the primary and cluster-source
agents passed the literal source shifts, cap ordering, primitive head
chart, rational gauge, operator group law and finite-jet conclusion.
The reviews retain the constant-head omission, common-character
condition for color sums, possible exponential action of G, and
ordinary-closure/bare-mark distinction. The cluster-source agent
also checked the root-regular or cleared-Laurent jet scope and freshly
replayed the entire focused audit with the reported counts and error.
No global cycle or volume-equality conclusion is included in this
review.
