# The intrinsic ADO cut and its meridian centralizer torsor

Research note, 26 October 2026. This proves a basis-independent formula
for the actual modified ADO cut, using the original nilpotent modules
and pivotal contraction. It then assembles the local meridian source
maps into an atlas for every even-strand knot braid. The transition
group is a product of general linear groups. Its conjugations disappear
on the trace quotient, but transitions inside a braid word remain.

The proof uses explicit Casimir moments and fusion matrix units, rather
than an assumed modified-trace theorem. This overlaps existing modified
dimension/trace theory; it is not a new invariant. The geometric
quantum-A component, integral source comparison with an ideal
triangulation, and selected regulator norm remain unproved.

## 1. Actual data and the claim

Fix N>=2, q=exp(pi*i/N), Q=q^2, rho=q-q^(-1). The original nilpotent
color V_x has basis v_a, 0<=a<N, with

    K v_a=x Q^(-a) v_a, F v_a=v_(a+1),
    E v_a=e_a(x) v_(a-1),
    e_a(x)=[a](x q^(1-a)-x^(-1)q^(a-1))/rho.

F v_(N-1)=0. Use exactly

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^(-1) tensor F,
    g_x=K^(1-N), theta_x=x^(1-N).                    (1.1)

In highest-root coordinates the full ADO dimension is

    d_x=-q^(N(1-N)/2) (q x-q^(-1)x^(-1))/(x^N-x^(-N)). (1.2)

For the actual meridian M=-q x this is

    d_N(M)=eta_N (M-M^(-1))/(M^N-M^(-N)),
    eta_N=(-1)^(N+1)q^(N(1-N)/2)=i^(N+3).           (1.3)

The quotient at M=1 is its whole regular value eta_N/N. The constant
in (1.2) is retained even though it cancels in the fusion ratios below.
All intertwining and centralizer conditions in this note refer to
the three actual total matrices E,F,K.

Work first over the generic color field: every successive product of
the chosen highest roots has 2N-th power different from one. These
conditions define a nonempty open chart. All ensuing identities are
rational identities on that chart.

For W=V_(x_1) tensor ... tensor V_(x_b), let t_W(A) be the scalar
right pivotal closure of all factors except the first. Thus the actual
cut row in the original basis is

    t_W(A)=Tr((P_0 tensor g_(x_2) tensor ... tensor g_(x_b)) A),
    P_0 v_a=delta_(a,0) v_0.                        (1.4)

For an intertwiner A this partial closure is t_W(A) times identity
on V_(x_1). Define the full weighted cut mathfrak_t_W=d_(x_1)t_W.

Write the actual module decomposition as

    W=direct_sum_z V_z tensor H_z,
    A=direct_sum_z I_(V_z) tensor A_z.

The result is the exact formula

    mathfrak_t_W(A)=sum_z d_z Tr_(H_z)(A_z).          (1.5)

In particular this full cut is cyclic, is independent of the fusion
basis, and is preserved by every U_q-module isomorphism. The zero
framing factor theta_x^(-writhe) is still applied to the braid operator;
it is not absorbed into (1.5).

## 2. A uniform two-color Casimir moment calculation

On V_x tensor V_y put

    Omega=rho^2 F_tot E_tot+q K_tot+q^(-1)K_tot^(-1),
    z_j=xy Q^(-j), c_j=q z_j+q^(-1)z_j^(-1), 0<=j<N.

The highest vector of degree j is h_j=sum_a b_a v_a tensor v_(j-a),
b_0=1, with

    b_(a+1)/b_a=-e_(j-a)(y)/(e_(a+1)(x)y Q^(-(j-a-1))). (2.1)

It is annihilated by E_tot. Its N F-descendants form V_(z_j).
Indeed all e_r(z_j), 0<r<N, are nonzero on this chart, so the
commutation relation precludes a shorter descendant string. The
primitive-root binomial identity gives F_tot^N=E_tot^N=0. Distinct
Casimir eigenvalues make these N summands a direct sum of dimension
N^2. This proves the stated two-color decomposition.

Put k_x=x^N, k_y=y^N and let T_N be normalized by
T_0=2,T_1=z,T_(r+1)=z T_r-T_(r-1). The Casimir polynomial is

    P_(x,y)(z)=product_j(z-c_j)=T_N(z)+k_x k_y+(k_x k_y)^(-1). (2.2)

Here is the pivotal moment identity, before using any fusion weight:

    ptr_(g_y)(Omega^m)=0,                   0<=m<N-1,
    ptr_(g_y)(Omega^(N-1))=s_x I,
    s_x=-N (k_x-k_x^(-1))/(q x-q^(-1)x^(-1)).         (2.3)

First, the closure is an intertwiner of V_x. For Z=E or Z=KF,
Delta Z=Z tensor K+1 tensor Z. Multiply its intertwining identity
by 1 tensor K^(-1)g_y before closing. The first terms give the
commutator with Z on the open leg. The remaining terms cancel
by cyclicity on the closed leg, since K^(-1)g_y=K^(-N) is central.
The Delta K identity gives commutation with K as well, hence with F.
V_x is simple, so it suffices to compute its (0,0) entry.

For the input v_0 tensor v_d, write t=Q^(-d) and use the first
index a along its fixed total-degree block. The diagonal entry
(Omega^m)_(0,d;0,d) is a polynomial H_m(t) of degree at most m.
To check this explicitly, the three entries of Omega along this
block are

    diagonal at a:
      x^(-1)Q^a(qy+q^(-1)y^(-1))
       +y Q^a((q x+q^(-1)x^(-1))-(q+q^(-1))x^(-1)Q^a)t,
    a -> a+1: rho^2 e_(d-a)(y),
    a -> a-1: rho^2 e_a(x)x^(-1)y Q^(2a-1)t.

The upward coefficient is Laurent of degrees -1,0,1 in t; the
downward coefficient has degree 1. A closed path has as many
upward as downward steps, so its lowest exponent is nonnegative
and its highest is at most its length. Invalid paths at d-a=0
vanish because e_0=0. No truncation at a=N affects these moments.

Since g_y v_d=y^(1-N)Q^(-d)v_d, closing multiplies H_m(Q^(-d))
by y^(1-N)Q^(-d) and sums d=0,...,N-1. Root orthogonality proves
the vanishing in (2.3). For m=N-1 only the leading coefficient of
H_(N-1) survives.

After removing y, the leading tridiagonal matrix L has entries

    L_(a,a)=Q^a((q x+q^(-1)x^(-1))-(q+q^(-1))x^(-1)Q^a),
    L_(a+1,a)=-q Q^a,
    L_(a-1,a)=rho^2 e_a(x)x^(-1)Q^(2a-1).

For 0<=a<=m<N its first column satisfies the explicit identity

    (L^m)_(a,0)=(-1)^a q^m Q^(a(a-1)/2)
                  {m choose a}_Q product_(r=a)^(m-1)(x-Q^r x^(-1)). (2.4)

This is proved by induction in the displayed three-term recurrence.
The coefficient of x uses
{m+1 choose a}_Q={m choose a-1}_Q+Q^a{m choose a}_Q.
For the coefficient of x^(-1), use in addition
(1-Q^(a+1)){m choose a+1}_Q=(1-Q^(m-a)){m choose a}_Q;
the remaining adjacent-coefficient identity is the same relation
with a replaced by a-1. Thus (2.4) follows without an unproved
orthogonal-polynomial or integration formula.

At m=N-1,a=0, the product in (2.4) becomes

    q^(N-1) product_(r=0)^(N-2)(x-Q^r x^(-1))
       =-(k_x-k_x^(-1))/(q x-q^(-1)x^(-1)).

Root orthogonality supplies the further factor N. This proves (2.3).

Every polynomial f now obeys

    ptr_(g_y)(f(Omega))
      =s_x [z^(N-1)](f mod P_(x,y)) I.              (2.5)

For the spectral projector P_j, Lagrange interpolation gives top
coefficient 1/P_(x,y)'(c_j). Differentiate
T_N(t+t^(-1))=t^N+t^(-N) at t=q z_j to obtain

    P_(x,y)'(c_j)=-N(k_x k_y-(k_x k_y)^(-1))
                         /(q z_j-q^(-1)z_j^(-1)).

Consequently

    ptr_(g_y)(P_j)=(d_(z_j)/d_x) I.                 (2.6)

The left closure uses g_x^(-1), and gives d_(z_j)/d_y. One can
check this by transposition and duality: S(Omega)=Omega,
V_x^*=V_(x^(-1)Q^(-1)), and s_(x^(-1)Q^(-1))=s_x.
The same calculation (2.5) therefore proves the left formula.
No vanishing ordinary quantum dimension has been divided out.

## 3. All multiplicity spaces, including off-diagonal matrix units

Iterate (2.1) along a left-associated fusion tree. A path p has
successive simple roots z_1=x_1,z_2,...,z_b, with
z_r=z_(r-1)x_r Q^(-j_r). A normalized inclusion i_p and projection
p_p give matrix units i_p p_(p') between paths with the same final
simple root. These span the entire centralizer.

Close the last leaf of such a matrix unit. It becomes an intertwiner
between the preceding simple roots. If those roots differ, it is
zero. If they agree, their last fusion labels agree, and (2.6)
gives the factor d_(z_b)/d_(z_(b-1)). Repeat.

For a diagonal path all ratios telescope to d_(z_b)/d_(x_1).
For distinct paths with the same final root, there is a last stage
where their preceding simple roots differ; the partial closure at
that stage is zero. Thus

    d_(x_1)t_W(i_p p_(p'))=delta_(p,p') d_(z_b).

This proves (1.5) on every matrix unit, hence on every intertwiner.
It also proves the claim for arbitrary fusion frames: ordinary
multiplicity traces are invariant under their basis changes.

For b>=2 there are N final roots z_j=(product_i x_i)Q^(-j), and
each has multiplicity r=N^(b-2). In particular

    C_W=End_(U_q)(W)=product_(j=0)^(N-1) Mat_r(F),
    C_W^times=product_j GL_r(F).                    (3.1)

The original cut functional, including its full dimension, is
therefore intrinsic to W and its actual pivotal structure.

### The full cut is an algebraic residue

Let k=(product_i x_i)^N and P_W(z)=T_N(z)+k+k^(-1). The center
of (3.1) is F[z]/P_W, represented by the total Casimir. If a(z)
is the unique degree<N polynomial whose value at c_j is Tr(A_j),
then (2.2) and (1.2) give

    d_(z_j) P_W'(c_j)=c_N, c_N=N q^(N(1-N)/2),
    mathfrak_t_W(A)=c_N sum_j a(c_j)/P_W'(c_j)
                  =c_N [z^(N-1)]a(z).              (3.2)

Here a is the ordinary matrix trace on every central block, hence
the reduced trace of the centralizer over its center. The last
functional is the algebraic residue of a/P_W. It remains defined
by the displayed coefficient when roots collide. This expression
retains c_N, including its phase and factor N.

### The complete two-factor centralizer has a perfect integral pairing

Set M=exp(u), R=C[[u]], x=-M/q, and use the actual equal-color
two-factor matrices over R. The coefficient in (2.3) is the Laurent
polynomial

    s_x=(-1)^(N+1)N M^(1-N) sum_(j=0)^(N-1)M^(2j),
    s_x|_(M=1)=(-1)^(N+1)N^2.                      (3.3)

It is a unit in R. On the finite free algebra

    A_R=R[z]/(T_N(z)+U+U^(-1)), U=M^(2N),

the actual pivotal cut is s_x times the top-coefficient functional.
In the basis 1,z,...,z^(N-1), its pairing (a,b)->ptr_g(ab) has
Gram determinant

    (-1)^(N(N-1)/2) s_x^N in R^times.              (3.4)

To see this, entries with i+j<N-1 vanish and those with
i+j=N-1 equal s_x. Reversing columns makes the Gram matrix
triangular with diagonal s_x. This proves (3.4), regardless of
the lower coefficients of P. Thus A_R identifies with its full
R-dual by the original cut, including the nonreduced complete
fiber. Multiplying by the full ADO factor gives exactly the
constant c_N in (3.2), since d_N(M)s_x=c_N.

This also identifies the entire deformable centralizer order:

    End_(U_q,R)(V_x tensor V_x)=A_R.                (3.5)

Indeed its fraction-field algebra is A_R tensor Frac(R), by the
generic multiplicity-one decomposition. Any integral intertwiner
therefore belongs to this fraction algebra. Its pairing with A_R
is integral, because the actual matrices and pivotal closure are
integral. Self-duality (3.4) places it back in A_R. Conversely
every polynomial in the Casimir is an integral intertwiner.

The subsequent [integral projective cut theorem](integral_projective_cut_duality.md)
now proves base change and perfect cut duality for every tensor
power: all complete-color intertwiners lift through R. No
matrix-algebra description over the confluent center is asserted
for higher tensor powers. The argument uses explicit projective
summands and a symmetric PBW form calibrated to the same ADO cut.

## 4. The comparison torsor and its canonical trace quotient

For two isomorphic generic modules W,W', their intertwiners form
a right torsor under C_W^times. If G:W->W' is such an intertwiner,

    mathfrak_t_(W')(G A G^(-1))=mathfrak_t_W(A).     (4.1)

Changing G to G D conjugates the pulled operator by D in C_W.
These inner changes act trivially on the additive quotient

    C_W/[C_W,C_W] = direct_sum_(j=0)^(N-1) F.       (4.2)

The bracket here denotes the span of commutators, not a group
quotient. On each matrix block the quotient is its ordinary trace.
Indeed every traceless matrix is a sum of elementary commutators;
and D A D^(-1)-A=[D,A D^(-1)]. This proves both assertions directly.
Thus the intertwiner torsor induces a canonical map on (4.2),
and (1.5) is its specified weighted period functional.

This resolves a scalar-normalization issue generically: a choice
of intertwiner does not change the transported full cut. It does
not say that one scalar cut determines all N quotient coordinates,
or that a matrix identification preserves the integral source lattice.

## 5. Meridian atlas for an entire even-strand braid

Let b=2h and W_M=V_x^(tensor b), x=-M/q. Then W_M and W_(qM)
are generically isomorphic: their final highest-root sets differ
by q^b=Q^h, which permutes the labels. The actual two-factor
meridian map from [the Casimir-source note](meridian_casimir_source.md)
therefore gives an explicit base comparison

    G_A(M)=G_12(M) tensor G_34(M) tensor ... tensor G_(b-1,b)(M). (5.1)

All total E,F,K are intertwined. The 2N-step product is identity,
because each local G=H(qM)P H(M)^(-1) telescopes and P^(2N)=1.
The N-step color/parity identification is still the specified one
in the Casimir-source note, rather than an omitted sign.

Let B_i(M) be the actual positive crossing at positions i,i+1,
with i=1,...,b-1. Put Y=M^2, U=M^(2N), a=-Y^(-1), c=1+U^(-1).
Let P_i be its actual last Casimir projector. The local formula is

    L_i^+=a B_i+c P_i,
    L_i^-=a^(-1)B_i^(-1)(I-P_i)+P_i.               (5.2)

They are exact inverses: on P_i, B_i has eigenvalue Y/U and
a(Y/U)+c=1; on its complement L_i^+=a B_i. The full factor c
and the projector pole at U=1 have not been replaced separately
by a numerical value.

Put delta=B_1 ... B_(b-1), delta_s=delta(qM). The braid relation
gives delta^(i-1)B_1 delta^(-(i-1))=B_i. The same holds for P_i,
since the generic projector is a polynomial in B_i. Define

    G_i=delta_s^(i-1) G_A delta^(-(i-1)),
    D_i=G_A^(-1)G_i in C_(W_M)^times.              (5.3)

The genuine local meridian source formula at the first pair gives

    G_i^(-1)B_i(qM)G_i=L_i^+,
    G_A^(-1)B_i(qM)G_A=D_i L_i^+ D_i^(-1).         (5.4)

These are compatible meridian charts for every generator. Their
transitions G_i^(-1)G_j=D_i^(-1)D_j lie in the actual centralizer
and satisfy the strict cocycle identity. They need not be scalar.

For any braid word beta=product_k B_(i_k)^(s_k), the whole identity is

    G_A^(-1)B_beta(qM)G_A
       =product_k D_(i_k)L_(i_k)^(s_k)D_(i_k)^(-1), (5.5)

where L^(-1) means the displayed L^- and all intermediate
D_(i_k)^(-1)D_(i_(k+1)) remain. Cyclicity removes a common outer
conjugation, not the interior transitions of this product.

The full period N_N(M)=d_N(M)F_N(M), with the original zero-framing
normalization and writhe w, therefore has the exact expression

    N_N(qM)=theta_(qx)^(-w) mathfrak_t_(W_M)
                 (product_k D_(i_k)L_(i_k)^(s_k)D_(i_k)^(-1)). (5.6)

Its peripheral gauge is exactly

    d_N(qM)/d_N(M)=-(qM-q^(-1)M^(-1))/(M-M^(-1)).  (5.7)

Thus the actual cut is now transported through this entire generic
meridian atlas. This constructs a global matrix expression with the
local source factors; it does not yet identify an all-level quantum-A
source extension with the geometric gluing source.

## 6. Stabilization and singular fibers

Every knot admits an even-strand braid presentation: if necessary
make one ordinary stabilization. Direct right closing of the actual
last crossing gives theta_x^(+/-1)I. Its new writhe factor cancels
it exactly. This is a local matrix identity of the fixed enhanced
crossing, so the selected zero-framed period is unchanged, including
at the Kashaev color. No growing number of stabilizations is needed.

Equations (1.5) and (5.6) are equalities of rational functions of M.
They therefore remain equalities of whole meromorphic germs at
M=1. The original d_N(M) is regular there. At shifted colors such
as qM, d_N(qM) can have a pole; its full principal part is retained.
For the reduced period the inverse of (5.7) can have a zero that
cancels a pole in the pulled cut. These factors must be combined
before evaluation. Wherever the prescribed period is regular, its
whole-germ value is preserved.

Individual fusion frames, meridian G_i and transition D_i generally
have poles at the complete color. The meromorphic identity does
not prove G_i Lambda_K=Lambda_T for the retained integral source
lattices, or identify their nonreduced normal fibers. Those are
additional parts of the triangulation/source comparison.

### The first meridian wall is an elementary integral modification

There is a more precise local integral statement. Retain R=C[[u]],
M=exp(u), A=A_R from Section 3, and put E=E_(N-1). Let c_last(M)
be the last Casimir branch. Only c_0 collides with it at M=1,
and their difference has a simple zero. Hence

    A^+=A[E]=A+R E,
    A^+/A=R/(u).                                   (6.1)

Indeed, write P=(z-c_last)P_rest. The resultant
P_rest(c_last) has valuation one. The elementary polynomial
Chinese-remainder sequence identifies A with the congruent pairs
inside R times R[z]/P_rest, with cokernel R/(P_rest(c_last)).
Adjoining E=(1,0) gives this full product. This is the partial
normalization of the colliding c_0,c_last pair; it leaves every
other local factor unchanged. Since E f=f(c_last)E, it is also
exactly the displayed rank-one lattice enlargement.

This enlargement is forced by the actual shifted crossing. On
W_(qM)=V_(-M) tensor V_(-M), let iota_s send z to its actual
total Casimir Omega_s. The local meridian equation is

    B_s=a r(Y,Omega_s)+c iota_s(E),
    a=-M^(-2), c=1+U^(-1).                         (6.2)

The source polynomial r(Y,z) is regular at M=1 by its confluent
interpolation proof. Both a and c are units in R, with c(1)=2.
Since B_s and Omega_s have integral matrices, (6.2) proves that
iota_s(E) is integral as well. In particular the actual order
generated by the shifted crossing and Casimir is exactly

    R[Omega_s,B_s]=iota_s(A^+).                    (6.3)

This is a statement about the algebra generated by these actual
operators; it does not assert it is the entire shifted centralizer.
The regular complete-color projector is explicitly

    E_s(0)=(B_s(0)+r_N(Omega_s(0)))/2,             (6.4)

where r_N is the already proved complete source crossing polynomial.
It is an idempotent of rank N: idempotence and its constant ordinary
trace N hold generically, hence extend on its integral matrix lattice.

The exact source pole and its cut are

    [u E]_(u=0)=J_N/(4rho),
    [u Phi_M(E)]_(u=0)=(-1)^N rho/4.                (6.5)

Here Phi_M is the original scalar pivotal cut and J_N is the
nonzero rank-one source Casimir nilpotent from the
[meridian source proof](meridian_casimir_source.md). These coefficients
include the actual cup/cap normalization. Because E_s is regular,
(6.5) also proves J_N(Omega_s(0))=0. The nilpotent source is
nonzero on the Kashaev module and vanishes on the shifted module;
the generic comparison cannot extend as an invertible integral
matrix at this wall.

The dual lattice is equally explicit. Using the perfect source
pairing of Section 3,

    (A^+)^vee={a in A:Phi_M(a E) in R}
             ={a in A:a(c_last) in uR}
             =(u,z-c_last)A.                      (6.6)

Its quotient in A has length one. The equivalence follows from
aE=a(c_last)E and the nonzero simple pole (6.5). Thus both sides
of the source/cut modification are fixed; there is no choice of
an arbitrary dual scalar.

This same ideal is the conductor {a in A:a A^+ subset A}:
it is exactly the condition that a(c_last)E return to A. Thus
the dual cut lattice is the conductor of this partial normalization.
This supplies a concrete normalization-and-residue description
of the meridian source wall.

Finally the actual dimension gauge gives on this same algebra

    Phi_(qM) o iota_s=-f(M)/f(qM) Phi_M,
    f(M)=M-M^(-1).

Since this ratio is -2u/rho+O(u^2), (6.5) yields the finite value

    Phi_(qM)(E_s)|_(M=1)=(-1)^(N+1)/2.             (6.7)

This evaluates the whole regular shifted projector, rather than
replacing c by 2 in a polar source expression. Equations
(6.1)--(6.7) supply an actual meridian-induced integral source
enlargement and its dual cut. Their global counterpart on an
ideal triangulation is still to be constructed.

## 7. Consequence for the geometric triangulation program

The [ideal triangulation input](ge_geometric_triangulation_audit.md)
provides beta_T and its marked regulator. The
[classical crossing comparison](crossing_fundamental_cycle.md)
already identifies the complete rational Bloch class. This note
adds an intrinsic selected quantum cut and an explicit meridian
centralizer atlas; fusion-basis changes create no additional
unfixed scalar in that cut.

The remaining geometric comparison must construct the relevant
relative tensor presentation and its source lattice, identify its
selected section, and control the period norm across levels.
The rank-N quotient (4.2) is a trace quotient of an actual tensor
centralizer; its dimension alone does not identify it with the
rank-N geometric quantum boundary module or match central curves.
The [threaded-observable obstruction](ado_threaded_shadow.md) to
a literal fixed-hyperbolic-root-character identification still applies.
No general hyperbolic or alternating volume conjecture follows here.

## 8. Coverage and exact diagnostics

The coverage check is the abstract of
[Geer--Patureau-Mirand--Turaev, 0711.4229](https://arxiv.org/abs/0711.4229):
modified dimensions and renormalized nilpotent sl2 link invariants,
including Kashaev invariants, are established literature subjects.
No result or proof of that paper is a premise of the moment and
fusion-matrix-unit arguments above. This note independently fixes
the relevant formula in the exact conventions and source comparison
used here; it makes no novelty claim for modified traces.

[The exact audit](../experiments/audit_intrinsic_cut_transport.py)
checks 16 two-color cases at N=2,3,4,5,6,9,12,15, including all
lower Casimir moments, their full top constant, every projector
weight, and the inverse pivot in the left closure. Twenty tensor
cases, with identical and heterogeneous colors and up to six
strands, test all 8,700 centralizer matrix units against the actual
cut density, including every off-diagonal unit.

At the same eight levels, direct complete-color Casimir moments
also give the nonzero Gram determinant (3.4) and the exact
full-state residue constant c_N, without diagonalizing a colliding
spectral frame or dividing a zero quantum dimension.

Eight further shifted-color cases check (6.4)--(6.7): the regular
projector is an actual E,F,K intertwiner of rank N, its cut is
the full signed half, its source pole coefficient is as printed,
and the rank-one source nilpotent becomes zero on the shifted
module. Both signs of the actual stabilization closure are checked
at the complete color as well.

On four strands at N=2,3,4 the paired map (5.1) alone fails the
middle-generator affine formula: the exact defects have full
matrix ranks 16,81,256 respectively. The conjugated charts (5.3)
satisfy the local formulas, intertwine all total E,F,K, and their
transitions commute with these operators. Nine stabilized whole
knot words verify (5.5)--(5.7) with the original cut, dimension and
zero-framing factors; nine direct ideal-color evaluations verify
stabilization without singular fusion frames. The diagnostics
support the uniform proofs and do not substitute for them.
[Results](../experiments/intrinsic_cut_transport_results.json).

Reproduce with:

    python3 experiments/audit_intrinsic_cut_transport.py
