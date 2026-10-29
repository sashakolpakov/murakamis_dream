# A regular holonomy-braiding line through the actual ADO color

Research note, 26 October 2026. This supplies local quantum data for the
[triangulation comparison](triangulation_regulator_bridge.md), continuing
the [marked braid calculation](marked_braid_holonomy.md). It constructs
the unrestricted quantum holonomy automorphism, a regular splitting
module through the actual Kashaev color, and an explicitly anchored
intertwiner line. Its restriction to the nilpotent meridian section
gives the original zero-framed knot evaluation with its full peripheral
factor. It does not construct the global relative source extension or
identify its selected period with the Bloch regulator.

Holonomy braidings have existing literature coverage; Section 8 records
it. The algebra calculations below reconstruct the needed local facts
without using a published holonomy-braiding proof.

The subsequent [semicyclic carry-braiding theorem](semicyclic_carry_braiding.md)
now gives a global explicit formula on E^N=0: its uncheck
finite Euler sum retains the wrap phi_2/K_1^N. Four elementary
conjugations, the Casimirs and the center powers prove all six
generator equations. A common highest-weight flag fixes strict
braid coherence without a determinant ambiguity on that locus.
The transported center maps are the Frobenius block matrices;
their common fixed line gives genuine braid actions on all
integral recoupling charts and the original entire scalar cut
operator. This is a special reducible-character source, not
an extension of that highest-weight argument to E^N!=0 or
an identification with the geometric regulator.

## 1. Rational conjugation survives when a universal matrix does not

Put q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), N>=2. Use the unrestricted
algebra with

    KE=QE K, KF=Q^(-1)FK, [E,F]=(K-K^(-1))/rho,
    Delta E=E_1 K_2+E_2, Delta F=F_1+K_1^(-1)F_2.

There is no unrolled H on a general cyclic module. To derive rational
formulas, first use a generic parameter and the formal series

    R=D Theta, D=q^(H_1 H_2/2),
    Theta=sum_(n>=0) c_n (E_1 F_2)^n,
    c_n=q^(n(n-1)/2)rho^n/[n]_q! .                (1.1)

Writing P_Q(t)=(t;Q)_infinity as a formal series, elementary coefficient
comparison gives

    Theta=P_Q(q rho^2 E_1 F_2),
    P_Q(Qt)=P_Q(t)/(1-t).

Thus conjugation on generators has rational expressions even though
the series (1.1) cannot itself be specialized on general cyclic modules.
Set, with the displayed multiplication order,

    u=q rho^2 E_1 K_1^(-1) K_2 F_2,
    H=(1-u)^(-1), G=(1-Q^(-1)u)^(-1).

The automorphism r is

    K'_1=K_1(1-Q^(-1)u),       K'_2=K_2 H,
    E'_1=E_1 K_2,             F'_2=K_1^(-1)F_2,
    E'_2=K_1 E_2+E_1-E_1 K_2^2 H,
    F'_1=F_2+F_1 K_2^(-1)-G K_1^(-2)F_2.          (1.2)

For K, commute K through P_Q and use its functional equation. E_1 and
F_2 commute with Theta, so their images follow from D. For the other
two images use r(Delta a)=Delta^op a. This last identity is independently
checked from

    c_(n+1)[n+1]_q=q^n rho c_n,
    [E,F^n]=[n]_q F^(n-1)
              (q^(1-n)K-q^(n-1)K^(-1))/rho.

Substitution cancels adjacent series coefficients; the F equation is
the same calculation with E,F and K,K^(-1) interchanged. No root-level
infinite series is used in (1.2).

There is an explicit rational inverse. From the primed generators set
u=q rho^2 E'_1 F'_2, with H,G as above. Then

    K_1=K'_1 G, K_2=K'_2(1-u),
    E_1=E'_1 K_2^(-1), F_2=K_1 F'_2,
    E_2=K_1^(-1)(E'_2-E_1+E_1 K_2^2 H),
    F_1=(F'_1-F_2+G K_1^(-2)F_2)K_2.              (1.3)

These equations also specify the necessary localizations.

Here is a direct coherence proof. If AB=QBA, expansion of (A+B)^n
gives the ordered Gaussian coefficients and hence

    Theta(A+B)=Theta(A)Theta(B).

After commuting the Cartan factors, the two instances needed are
(A,B)=(E_1 K_2 F_3,E_2 F_3) and
(E_1 K_2^(-1)F_3,E_1 F_2). They give

    (Delta tensor id)R=R_13 R_23,
    (id tensor Delta)R=R_13 R_12.

Applying the intertwining identity to the first equation proves
R_12 R_13 R_23=R_23 R_13 R_12. Consequently the rational conjugations
(1.2) satisfy the corresponding three-factor identity. The identities
involve only rational functions of the generators and q after
conjugation. Clear their denominators and specialize: they hold at
each root where the indicated denominators are invertible. This proves
coherence of the automorphisms rather than assuming an infinite
universal matrix exists at that root.

## 2. Exact root center and its peripheral marking

Write k_i=K_i^N, e_i=E_i^N, f_i=F_i^N and

    Omega=rho^2 FE+qK+q^(-1)K^(-1),
    C_0=2, C_1=z, C_(n+1)=z C_n-C_(n-1).

Multiplying the N shifted FE factors proves

    C_N(Omega)=rho^(2N)ef-k-k^(-1).                (2.1)

For example the polynomial identity behind this calculation is
product_(j=0)^(N-1)(z-qKQ^j-q^(-1)K^(-1)Q^(-j))
=C_N(z)+K^N+K^(-N), using q^N=-1. Both individual Casimirs are
fixed by r.

Ordered multiplication gives u^N=-rho^(2N)e_1 f_2 k_2/k_1. Retain
the entire central divisor

    D_c=1-u^N=1+rho^(2N)e_1 f_2 k_2/k_1.           (2.2)

All factors 1-Q^j u become invertible after D_c is inverted: their
product is D_c. No parity-dependent scalar is discarded. The center
map of (1.2) is

    k'_1=k_1 D_c,                k'_2=k_2/D_c,
    e'_1=e_1 k_2,                f'_2=f_2/k_1,
    e'_2=k_1 e_2+e_1-e_1 k_2^2/D_c,
    f'_1=f_2+f_1/k_2-f_2/(k_1^2 D_c).             (2.3)

For the last two formulas, take the N-th powers of the coproduct
intertwining equations. The mixed Gaussian-binomial coefficients
vanish because Q has order N, including composite N.

Use balanced center coordinates

    epsilon=rho^N E^N, varphi=-rho^N F^N.

Then k+k^(-1)+epsilon*varphi=-C_N(Omega) and
D_c=1-epsilon_1 varphi_2 k_2/k_1. Equations (2.3) have the same
form in these balanced variables. For the checked algebra map
Ad_(PR)=tau composed with r, its point map applies (2.3) to swapped
inputs, by contravariance. For inputs (k,e,f),(l,g,h), with
c=1-k g f/l, that point map is

    ((l c, k g, f+h/k-f/(l^2 c)),
     (k/c, l e+g-k^2 g/c, f/l)).                  (2.4)

This is exactly the inverse holonomy map (4.7) in the
[marked braid note](marked_braid_holonomy.md). The inverse is required
by pullback; replacing it by the positive critical map changes the
convention. The previously derived Borel-factorization/prefix change
therefore identifies (2.4) with inverse Hurwitz transport.

In those coordinates put

    G(k,e,f)=[[k,e],[kf,k^(-1)+ef]].

At the actual ideal color a=N-1, x_0=q^a,
k_0=x_0^N=delta=(-1)^(N-1), Omega_0=-2, e=f=0.
The marked meridian is mu=delta G. It is the identity at this
augmentation. On the actual nilpotent color section x=x_0 M it
has eigenvalues M^N,M^(-N); its squared eigenvalue coordinate is
U=M^(2N), as in the [actual threading calculation](ado_threaded_shadow.md).
This fixes the sign rather than silently changing the root character.

## 3. A regular three-parameter splitting module

Work near (x,epsilon_0,phi_0)=(x_0,0,0), where epsilon_0 and phi_0
now denote the raw central powers E^N,F^N, not the balanced variables
of Section 2. Choose the unique algebraic Hensel branch omega near -2
satisfying

    C_N(omega)=rho^(2N)epsilon_0 phi_0-x^N-x^(-N).

It exists because C_N'(-2)=delta N^2 is a unit in characteristic
zero. Thus the full center is smooth on this cover at the actual
color; fixing omega=-2 first would instead produce a singular
quadratic cone at the augmentation.

For 1<=j<N define

    a_j=(omega-qxQ^(-j)-q^(-1)x^(-1)Q^j)/rho^2,
    P=product_(j=1)^(N-1)a_j.

Every a_j specializes to [j]_q^2, a unit. On a basis v_0,...,v_(N-1)
set

    K v_j=xQ^(-j)v_j,
    F v_j=v_(j+1) (j<N-1), F v_(N-1)=phi_0 v_0,
    E v_j=a_j v_(j-1) (j>0), E v_0=(epsilon_0/P)v_(N-1).
                                                            (3.1)

The product identity (2.1) gives the missing FE diagonal at j=0.
The differences of the other diagonals give [E,F], and K gives
the remaining relations. Thus (3.1) has the specified Casimir and
central powers. At epsilon_0=phi_0=0 the chosen omega is
qx+q^(-1)x^(-1), so these are exactly the actual nilpotent ADO
E,F,K matrices. At x=x_0 they give the Kashaev color. General
cyclic members have no H satisfying the unrolled weight rule;
none is asserted.

This is a splitting module, including at the nilpotent point.
Indeed the distinct K eigenvalues give spectral projectors p_j.
For adjacent nonwrapping indices, F and a_j^(-1)E give inverse
matrix units. Their products give all matrix units. Conversely
reduce any returning path using FE, EF and the specified full
E and F cycles. Its p_0 corner is a scalar. Hence the central
quotient on this chart is End of the free module (3.1). This
proves the needed splitting directly, including the special fiber.

## 4. A concrete Hom line and its anchor

For a pair of source modules use (2.3) for the target center and choose

    x'_1=x_1 D_c^(1/N), x'_2=x_2 D_c^(-1/N),

with D_c^(1/N)=1 at the ideal pair. Keep the individual Casimirs.
The target modules are again (3.1). Source matrices transformed by
(1.2), and these target matrices, are two splitting representations
with the same center. Their intertwiners form a rank-one Hom module.

There is an explicit generator. For each transformed K'_i form

    P_i=(1/N)sum_(j=0)^(N-1)(K'_i/x'_i)^j.

Let lambda_0=q^((N-1)^2/2), using the already specified square root
of q, and v=P_1 P_2(lambda_0 v_0 tensor v_0). Define the columns of I by

    I(v_r tensor v_s)=(F'_1)^r(F'_2)^s v.           (4.1)

The matrix-unit description proves all six intertwining equations.
At the ideal pair the transformed algebra is conjugated by the actual
full R, and R(v_0 tensor v_0)=lambda_0(v_0 tensor v_0).
Consequently (4.1) equals that actual R at this point. In particular
I is invertible on the formal neighborhood. This constructs the
Hom frame using the K cover and ordinary units; no roots of E^N or
F^N are required.

At the base det I=1. Set

    I_bar=(det I)^(-1/N^2) I,                     (4.2)

using the root with value one there. This is a specified finite
algebraic cover and a pointed line, not a free scalar choice.

For a triple, the rational Yang--Baxter identity identifies the two
target splitting modules. The two products of the framed
intertwiners differ by a scalar. Each pair map has determinant one,
so its embedding on a triple also has determinant one. Thus the
scalar has N^3-th power one. It equals one at the ideal triple,
where the actual finite R satisfies Yang--Baxter (the generic
highest-weight identity specializes without denominators [N]_q).
In the formal neighborhood a root of unity with this value is one.
This proves strict local holonomy coherence on the specified cover.
Global continuation must retain its root cover and phases; this
argument alone gives no globally normalized tangle invariant.

## 5. Exact restriction to the original knot period

For the same nilpotent color on both strands, write R^0 for the actual
uncheck R with its common Cartan factor q^(alpha^2/2) removed.
The formula (4.1) restricts to I=lambda_0 R^0. Its diagonal entries
before the common factor are x^(-r-s)q^(2rs), whence

    det R^0=x^(-N^2 a)q^(N^2 a^2/2), a=N-1.

Writing x=x_0 M, the root of det I selected above is M^(-a).
Therefore

    I_bar=x^a q^(-a^2/2) R^0.                     (5.1)

At M=1 this is the actual full R. For the residual normalization
R^0 the actual same-color twist is theta_0=x^(-a). For (5.1)
take theta_bar=q^(-a^2/2). Their ratio is exactly the crossing
scalar x^a q^(-a^2/2). On a knot braid of writhe w, multiplying
crossings contributes this scalar to the power w; the zero-framing
twist correction contributes its inverse. The pivot and cut pairing
are unchanged. Thus the reduced and full zero-framed knot periods
are exactly the original ones throughout this nilpotent meridian
germ. In particular F_N(1)=<K>_N still holds.

This statement concerns the same-color cut evaluation. It does not
assert that the constant theta_bar is a ribbon twist on every mixed
cyclic object. Nor does it change the full ADO factor

    d_N(M)=i^(N+3) M^(N-1)/(1+M^2+...+M^(2N-2)).

The [rank-one meridian wall](marked_braid_holonomy.md) and its whole
ratio at M=1 must still be retained in a global source construction.

## 6. What this contributes to the ideal-triangulation route

The audited ideal-triangulation theorem supplies a complete positive
geometric representative beta_T and its marked Bloch regulator. The
[crossing fundamental-cycle calculation](crossing_fundamental_cycle.md)
already identifies the complete classical crossing class with beta_T.
The construction here supplies actual local quantum holonomy data
and a Hom line regular through the color used by the original invariant.
It therefore provides a local object to transport when comparing a
diagram decomposition and an ideal triangulation.

It supplies neither the relative gluing source nor its chosen global
contraction. In particular the actual root augmentation mu=I and the
complete hyperbolic meridians are different central data. The
[threaded separator](ado_threaded_shadow.md) rules out simply equating
their homogeneous eigenlines while preserving the interior observables.
A regular local family of crossing modules does not prove that the
corresponding closed knot representations lie on one component, or
identify their evaluations.

The required comparison is of pointed relative source extensions,
including their cut/cap data, full meridian wall, peripheral factors,
and selected evaluation. It must also specify the trajectory between
fixed semiclassical shapes and root-central coordinates. Positivity
and local Yang--Baxter coherence alone do not prove nonzero geometric
contribution, exclude cancellation, or bound the norm of the unknown
comparison period. The volume identity

    (4/N)log|F_N(1)| -> log||P_hyp||=2Vol(M)/pi

remains unproved.

The subsequent [closed-braid note](closed_braid_period_line.md)
constructs the admissible global braid Hom line and a literal
scalar cut functional from these local data. A grading calculation
identifies its entire upper triangular reducible period with the
actual ADO meridian value. It also proves that the formal central
augmentation neighborhood is abelian and identifies the Alexander
attachment divisor. This advances the global braid construction;
the relative triangulation source, opposite-weight geometric
coupling and regulator norm remain unproved.

## 7. Independent exact diagnostics

[The audit](../experiments/audit_regular_holonomy_braiding.py) checks
14 generic cyclic automorphism cases, including every commutator,
the rational inverse, coproduct transport, Casimirs and central powers.
Six three-factor tests check the quantum Yang--Baxter maps. Six tests
construct the matrix-unit intertwiner and check all six generators.
Fourteen actual nilpotent/ideal cases check exact conjugation, the
anchored frame and determinant root; thirty knot cut evaluations
check the compensating twist. Nine third-order deformation tests,
through level 15, check the Hensel module and both central powers.
The balanced-center sign and inverse holonomy convention are also
checked symbolically. Even and composite levels are included.
See [the results](../experiments/regular_holonomy_braiding_results.json).
These diagnostics support the algebraic proofs, not a global period
identification or volume estimate.

## 8. Literature coverage, not proof premises

[Kashaev--Reshetikhin, math/0202212](https://arxiv.org/abs/math/0202212)
already constructs root-of-unity holonomy R-matrices. The abstract of
[McPhail-Snyder--Reshetikhin, 2509.02354v2](https://arxiv.org/abs/2509.02354v2)
announces an explicit four-dilogarithm factorization and holonomy
Yang--Baxter equation. The abstract of
[McPhail-Snyder, 2509.02365v3](https://arxiv.org/abs/2509.02365v3)
announces invariants with flat-connection input and a phase-free
geometric twist of Kashaev's invariant. These establish prior coverage
of the general framework, not the selected original-state period
comparison needed here. Their proofs, factorization and global
normalization claims are not premises of Sections 1--6.

The fixed-Casimir polynomial in the
[older recoupling note](casimir_braiding_and_recoupling_lattice.md)
is a specialization/lattice lift; that note does not assert a generic
braiding for it. Equations (1.2)--(2.3) use a different construction:
the individual unrestricted central characters change by the holonomy
map. The coherence proof here gives no generic Yang--Baxter identity
for that fixed polynomial extension.
