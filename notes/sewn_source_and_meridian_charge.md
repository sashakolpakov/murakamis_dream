# Sewing the actual source residue with its conserved meridian charge

Research note, 26 October 2026. The actual meridian source residue
can be sewn through an arbitrary integral knot operator. With one
helper strand it belongs to an explicit two-copy projective corner.
Its lift through the meridian wall requires a cubic meridian color;
keeping the remaining colors unchanged is obstructed at first order.
The charged corner has a regular rational construction anchored to
the original cup, cap, crossing and full modified cut.

This identifies the sewn residue and a regular lift of its corner.
It does not identify the entire polar source projector away from
the wall, the global affine extension, or the selected Bloch period.
The original volume conjecture remains unproved.

## 1. An adjacent crossing splits the actual cup/cap channel

Fix N>=2, q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), and the complete
actual color V=V_(x_0), x_0=-q^(-1)=q^(N-1). Its pivot and
zero-framing twist are the existing actual matrices and scalar

    g=K^(1-N), theta=x_0^(1-N).

Use the original self-duality matrix and right cup/cap from
[the actual meridian source](meridian_casimir_source.md):

    D_(N-1-a,a)=q^(a^2),
    cup=vec(D^(-t)), cap=vec(gD)^t,
    Pi=cup cap, cap cup=0.                        (1.1)

These are E,F,K intertwiners; the cup and cap factor through
the unit object and Pi has rank one. For b>=3 put

    W_0=V^(tensor b), P_0=V^(tensor(b-2)),
    i=cup tensor I_(P_0), c=cap tensor I_(P_0).

Let B_23 be the original checked positive crossing on the
second and third strands. Then

    c B_23 i=theta I_(P_0),
    c B_23^(-1) i=theta^(-1) I_(P_0).             (1.2)

Here is a direct scalar check. On the three active strands
the compositions are intertwiners of the simple color V,
so they are scalar. Evaluate the positive composition on
v_(N-1). The actual R has only its zero-th summand when its
second input is v_(N-1). The cap then forces the cup component
v_0 tensor v_(N-1). The cup and cap coefficients cancel D
and leave g_0=theta; the crossing coefficient on
v_(N-1) tensor v_(N-1) is one, since x_0=q^(N-1).
For the inverse composition evaluate on v_0. After the
permutation its first input is v_0, so again only the zero-th
summand remains; the cap forces v_(N-1) tensor v_0 and leaves
g_(N-1)=theta^(-1). Tensoring the other strands proves (1.2).

Define entirely specified maps

    beta=theta^(-1) B_23 i,
    alpha=theta^(-1)c B_23,
    Omega=alpha beta,
    alpha_prime=alpha-Omega c.

Equations (1.1)--(1.2) imply

    alpha_prime i=I, alpha_prime beta=0,
    c i=0, c beta=I.

Thus U=(i,beta):P_0^2->W_0 and R=(alpha_prime,c)^t give

    R U=I_(P_0^2), Pi_12 tensor I=U E_12 R.      (1.3)

The four maps U E_ij R are actual matrix units. Their corner
is End_H(P_0^2), with the calibrated full trace inherited from
W_0. This is an explicit splitting, including its twist unit.

## 2. The actual residue can be sewn through the whole knot operator

Let u=Log M, R_0=C[[u]], x(M)=-M/q, W_b(M)=V_(x(M))^(tensor b).
For any integral E,F,K intertwiner A(M) of W_b(M), use exactly
the full modified cut mathfrak_t_W=d_N(M)t_W. This includes an
actual knot braid with its original zero-framing scalar.

The [integral projective cut theorem](integral_projective_cut_duality.md)
identifies these traces with one calibrated symmetric PBW form.
Its rectangular-matrix cyclicity gives, for projective P_0,W_0,

    mathfrak_t_W0(A(0)i c)
                  =mathfrak_t_P0(c A(0)i).         (2.1)

This equality uses the same PBW scalar on both sides, so no
dimension or phase is chosen during sewing. It also follows by
embedding the two projectives in finite free modules and applying
the termwise identity sum mu((XY)_ii)=sum mu((YX)_jj).

Let E_last(M) be the actual last Casimir projector on the first
two factors, tensored with the remaining identities. The existing
source calculation gives

    [u E_last]_(M=1)=(-1)^N rho (Pi_12 tensor I)/4.

Combining this with (2.1) proves the all-operator residue formula

    Res_(u=0) mathfrak_t_W(A(M)E_last(M)) du
       =(-1)^N rho/4 *mathfrak_t_P0(c A(0)i).      (2.2)

It holds for the entire sewn knot operator, not only an isolated
crossing. In the original source coordinate U=M^(2N), keeping
the full coefficient 1+U^(-1) gives

    [(U-1)(1+U^(-1))mathfrak_t_W(A E_last)]_(M=1)
       =(-1)^N N rho *mathfrak_t_P0(c A(0)i).      (2.3)

Indeed U-1=2Nu+O(u^2), while the full source coefficient has
value two only after the polar product is combined. Its factor
has not been dropped in (2.3).

The sewn functional is nonzero as a functional on the complete
centralizer. To see this uniformly, choose T in End_H(P_0) with
mathfrak_t_P0(T)!=0, using its perfect trace pairing, and set
A=U E_21(T)R. Then c A i=T. In particular its zero set is a
proper linear hyperplane. This does not say that every specified
knot operator avoids that hyperplane. As a concrete actual braid
check, the positive stabilized unknot on b strands has

    mathfrak_t_P0(c A_unknot i)=d_N(1)theta^(-1)!=0

after its original zero-framing correction.
Here B_12 i=i, the adjacent crossing contributes theta by
(1.2), and the remaining positive Markov chain contributes
theta^(b-3)d_N(1). The original correction is theta^(-(b-1)),
giving precisely the displayed value.

The helper strand is essential. At b=2 the remaining object is
the nonprojective unit: mathfrak_t_(V tensor V)(Pi)=d_N(1)!=0,
although cap cup=0. Extending (2.1) to that unit would be false.
Every knot can be represented after actual Markov stabilization
with b>=3, retaining the same reduced zero-framed invariant.

## 3. An unchanged lower-strand color cannot lift this source

Write epsilon_N=x_0^N=(-1)^(N+1). The central K^N character of
the original meridian family is

    k_W=epsilon_N^b M^(bN).

The unmodified lower tensor power V_(x(M))^(tensor(b-2)) has
character epsilon_N^(b-2)M^((b-2)N). These agree at M=1 but
differ at first order. If an intertwiner lifting i existed,
centrality would force

    (k_W-k_lower)i(M)=0.

Its u coefficient is 2N epsilon_N^b i(0), which is nonzero.
Hence no such lift exists, even over C[u]/(u^2). This is an
obstruction from the actual central character, despite agreement
of the complete modules and their point-source signs.

The charge-preserving lower object is instead

    P_b(M)=V_(-M^3/q) tensor V_(-M/q)^(tensor(b-3)). (3.1)

Its K^N character is exactly k_W, including the parity sign.
The first surviving strand carries the charges of the two
removed strands as well as its own. If all other surviving
colors remain fixed and the replacement is x(M^c), equality
of central characters forces c=3.

Both P_b(M) and W_b(M) are projective over the same finite
nilpotent algebra H_(k_W): each color is a Steinberg deformation
at M=1, and tensoring preserves projectivity. Thus the complete
split corner in (1.3) admits a regular lift. The next construction
makes that lift rational and anchors it without an unspecified
choice of scalar.

## 4. A regular rational construction of the charged corner

It is enough to construct the maps on three strands and tensor
the remaining factors. Put z=-M^3/q, k=z^N, c_z=qz+q^(-1)z^(-1).
On W_3(M) use the actual total K,E,F and scaled Casimir Omega.
Let

    P_k(t)=T_N(t)+k+k^(-1),
    e_z=[P_k(Omega)/(Omega-c_z)]/P_k'(c_z),
    pi_z=(1/N)sum_(r=0)^(N-1)(K/z)^r,
    e=e_z pi_z.                                  (4.1)

The quotient is polynomial division before evaluation. At M=1,
c_z=-2 and P_k'(c_z)=(-1)^(N+1)N^2. It is therefore a unit
in the meridian germ. The selected block is Mat_N(R_0), and
its interior E,F chain coefficients e_a(z), 0<a<N, are units.
These are the explicit block and matrix-unit calculations from
the integral projectivity proof, applied to this actual branch.
In particular e projects to the highest vectors of V_z.

Let U_0^0=i, U_1^0=beta and R_0^0=alpha_prime, R_1^0=c on
the complete three-strand module. With the fixed basis v_a of
V_z, define

    h_j(M)=e(M)U_j^0 v_0,
    U_j(M)v_a=F^a h_j(M),
    R_j^pre(M)(w)_a
       =(v_0^t R_j^0)e(M)E^a w/
                       product_(r=1)^a e_r(z).   (4.2)

The empty product is one. These are rational functions of M,
regular at M=1. The block matrix units F^a e E^b divided by
the same chain products prove all E,F,K intertwinings. At M=1
they recover exactly U_j^0,R_j^0, including the original phase.

Every composition R_i^pre U_j is a scalar multiple D_ij(M) of
identity on V_z. The two-by-two matrix D has D(1)=I. Define

    R_i(M)=sum_j (D(M)^(-1))_ij R_j^pre(M).

Then the full two-copy retraction identity holds exactly,

    R_i(M)U_j(M)=delta_ij I.                      (4.3)

All denominators are units in the complete meridian germ.
Tensoring these maps with the remaining V_(x(M)) factors
constructs the claimed charged corner for every b>=3.

The calibrated full cut is preserved on this corner:

    mathfrak_t_W(U A R)=mathfrak_t_(P_b^2)(A).     (4.4)

This follows from the same rectangular PBW trace identity as
(2.1), or from the generic actual fusion weights followed by
whole-germ continuation. Thus the corner and its trace pairing
extend through the wall together. The nilpotent U E_12 R is
a regular lift of Pi_12 tensor I. It is not the full generic
projector E_last, whose rank and generic minimal polynomial
are different. Equations (2.2)--(2.3) identify its residue, not
every higher meridian coefficient of that projector.

## 5. The complete peripheral factor and source step must stay charged

The first source color in (3.1) has full modified dimension
d_N(M^3). Its exact ratio to the original cut normalization is

    d_N(M^3)/d_N(M)
       =(M^2+1+M^(-2))/(M^(2N)+1+M^(-2N))
       =(Y+1+Y^(-1))/(U+1+U^(-1)).               (5.1)

The phase eta_N cancels in this ratio; it remains present in
each dimension separately. The whole complete value is 3/3=1.
Discarding the central denominator would instead introduce an
incorrect factor three. Its other central zeros also matter
away from the complete germ.

The source step is charged as well: under M->qM its first
meridian becomes M^3->q^3M^3. A source period in that color
is pulled back by the third meridian step, with all its
intermediate factors retained. Identifying it with a single
uncharged step would change its period connection.

This charge is not visible in the complete longitude sign:
for L_c=+/-1, L_c^3=L_c. Consequently a point-source module
and its complete shift character alone cannot establish the
required global comparison. The actual source network must
retain the meridian cocharacter on its surviving strands.
For positive odd charges c_1,c_2,c_3 the same central-character
argument replaces them by the surviving charge c_1+c_2+c_3;
the total charge and strand parity are conserved.

## 6. Scope, coverage and independent checks

The residue can now be sewn through any original knot operator,
and its projective corner has an explicit integral rational lift
with conserved meridian charge and calibrated full trace. This
adds actual quantum data to the normalized local comparison in
[the equivariant source note](equivariant_cut_source_transport.md).

The original knot's value of the sewn functional can still vanish.
Its geometric component and selected period have not been
identified. Higher source jets, coherent transport through a
positive triangulation, and the central pole lattice still need
comparison. The residue formulas require integral surrounding
operators; polar meridian-atlas transitions must first be combined
in their whole germs and are not covered term by term by (2.3).
Perfection of the bilinear trace does not provide
a positive norm or a noncancellation bound. No volume limit is
deduced here.

Projective trace ideals and ribbon calculus have existing coverage,
including [the modified-trace abstract](https://arxiv.org/abs/1801.00321)
already checked for scope. No proof from it is assumed. The curl
calibration, charge obstruction, explicit rational corner and full
source factors above are independently derived in our conventions.
No novelty claim is made for projective splitting or trace cyclicity.

[The audit](../experiments/audit_sewn_source_corner.py) checks eight
actual complete source corners, including all E,F,K intertwinings
and inherited full trace pairings. Twenty-eight original braid-word
cases compare the literal Casimir source residue, with the full
coefficient in (2.3), against the lower-strand cup/cap evaluation.
The cases include both crossing signs and both root parities.

Five independent linear solves verify the first-order charged
intertwiner and the obstruction for charge one. Fifteen separate
exact rational corner constructions check (4.1)--(4.4) at complete
and generic colors, including their actual modified dimensions.
The tests include even and odd composite levels; they validate
the uniform algebraic arguments, not the unproved geometric
selection or norm claim.
[Results](../experiments/sewn_source_corner_results.json).

Reproduce with:

    python3 experiments/audit_sewn_source_corner.py

The subsequent [adjacent-source normal form](adjacent_source_normal_form.md)
now determines the full adjacent local projectors beyond these
residues. Their charged two-channel overlap equals the actual
pivotal cut moment, and the remaining projector terms are regular.
The ordered integral numerators generate the local matrix algebra.
A trace pole proves that the unscaled adjacent projectors cannot
share one finite stable lattice. The full source comparison must
retain those changes of lattice and its selected section; its
global geometric period and norm remain unproved.
