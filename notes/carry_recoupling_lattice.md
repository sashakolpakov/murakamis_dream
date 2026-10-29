# A common carry lattice for every recoupling tree

Research note, 26 October 2026. This gives an explicit integral model
for an arbitrary finite recoupling tree at simultaneous nilpotent
degeneration. Its pole orders are integer carries, independent of the
tree. The local moves, the actual meridian family and its original cut
trace can be transported on that common lattice at every N, including
even and composite levels.

This extends the two-factor Smith calculation in
[the cyclic lattice note](cyclic_steinberg_lattice.md). It uses the
existing pointed Borel recouplings and the literature ADO crossing.
It does not assign their full colored network to an arbitrary geometric
ideal triangulation or prove the selected Bloch-regulator norm.

## 1. Statement and hypotheses

Let N>=2 and Q be primitive of order N. Work over

    R=k[[epsilon]], K=k((epsilon)), char k=0,

enlarging constants to contain Q as needed. Fix b>=2 and directions
a_1,...,a_b such that every nonempty consecutive sum A_I is nonzero.
Put

    alpha_j=1-epsilon a_j, t_j=alpha_j^N,
    t_I=product_(j in I) t_j, w_I=product_(j in I) x_j.

The modules E_t=R[x]/(x^N-t) have their standard monomial lattices.
The leaf tensor lattice Lambda_leaf has the integral evaluation basis
e_i at x_j=alpha_j Q^(i_j), 0<=i_j<N. The evaluation changes are
units over R: their Vandermonde determinants are nonzero modulo epsilon.

For any ordered binary tree T with these leaves, factor each internal
interval I=L union R using the pointed Clebsch map

    C_(t_L,t_R): E_(t_I) tensor E_(tau_I)
                           -> E_(t_L) tensor E_(t_R),
    tau_I=(1-t_I)/(1-t_R).

Its iterated evaluation I_T maps the basic source lattice B_T, with
one total factor and b-1 relative factors, into Lambda_leaf tensor K.
The parameters extend as

    tau_I(0)=A_I/A_R, 1-tau_I(0)=-A_L/A_R.          (1.1)

Thus every relative cyclic algebra stays algebraically nondegenerate
on this exceptional divisor. No geometric positivity is inferred.

For a leaf residue tuple i define

    kappa(i)=floor((i_1+...+i_b)/N),
    J_kappa=diag(epsilon^(-kappa(i))).

**Common-lattice theorem.** For every tree T,

    I_T=J_kappa M_T, M_T in GL_(N^b)(R),
    I_T B_T=Lambda_carry
           =direct_sum_i epsilon^(-kappa(i)) R e_i.  (1.2)

The last lattice is the same for every tree. The Smith poles are
exactly -kappa(i). Their multiplicities are

    m_k=sum_(d=kN)^((k+1)N-1)
                    coefficient_d (1+z+...+z^(N-1))^b.         (1.3)

In particular poles can have order greater than one for larger
tensors. The two-factor result is m_1=N(N-1)/2 and
m_0=N(N+1)/2.

The actual integral source lattice is

    B_T^actual=I_T^(-1) Lambda_leaf
             =M_T^(-1) diag(epsilon^kappa) Lambda_leaf.        (1.4)

It has the corresponding nonnegative Smith exponents. Its distinguished
unit is retained, since I_T(1)=1 belongs to Lambda_leaf.

## 2. The kernel for a whole tree

Order the internal nodes in any fixed compatible order. In the
source monomial basis, with total exponent a and relative exponents
d_v in {0,...,N-1}, the exact evaluation is

    I_T(u^a product_v v_v^d_v)
      =w_all^a product_(v: I=L union R)
                 (Qw_I;Q)_d_v/(Qw_R;Q)_d_v.         (2.1)

For one node this is the independently proved pointed kernel
C(u^a v^d)=w^a(Qw;Q)_d/(Qz;Q)_d. For the induction, a total
coordinate function acts after subtree evaluation by multiplication
by its product w_I. Subtree relative operators commute with that
total coordinate. Thus every numerator and denominator pulls back
to the displayed multiplication function, proving (2.1). Denominators
are units in the generic K-algebra; the integral behavior is proved next.

All parity signs in the pointed Clebsch map and its literal permutations
remain as in the all-level construction. No determinant normalization
or independent scalar root is introduced in (2.1).

## 3. Carries bound every matrix-entry pole

For a node interval I let

    s_I=sum_(j in I) i_j, r_I=s_I mod N,
    c_v=(r_L+r_R-r_I)/N in {0,1}.

At the chosen leaf evaluation point,

    w_I=Q^r_I product_(j in I)(1-epsilon a_j).

For d<N, the product (Qw_I;Q)_d has a simple zero precisely
when d>=N-r_I and r_I!=0. Every other factor is a unit. The
zero is simple because its first coefficient is A_I!=0.
Use the threshold N when r_I=0. Therefore the node ratio in
(2.1) has valuation

    1_(d>=threshold(r_I))-1_(d>=threshold(r_R)).     (3.1)

If c_v=0 then r_I>=r_R, so this difference is nonnegative.
If c_v=1 it is at least -1. Hence its valuation is at least
-c_v in both cases.

The carries telescope:

    floor(s_I/N)=floor(s_L/N)+floor(s_R/N)+c_v,
    sum_(internal v)c_v=kappa(i).                   (3.2)

Multiplication of row i by epsilon^kappa(i) therefore makes
every entry of I_T integral, for every tree. This proves
M_T=J_kappa^(-1)I_T has entries in R.

## 4. The determinant proves the common image exactly

At every node the pointed two-factor determinant is

    det C=sign_N [t_R(1-t_I)/(1-t_R)^2]^(N(N-1)/2),
    sign_N=(-1)^(N(N-1)^2/2).

Its valuation is -N(N-1)/2: both 1-t_I and 1-t_R have a
simple zero. Extending by the other b-2 tensor factors raises
this determinant to N^(b-2). There are b-1 nodes. Thus

    val(det I_T)=-(b-1)(N-1)N^(b-1)/2.              (4.1)

The sum of the row carries is exactly the opposite:

    sum_i kappa(i)=(b-1)(N-1)N^(b-1)/2.             (4.2)

For a direct count, sum s_all over all N^b tuples. The residue
r_all is uniform on {0,...,N-1}, each appearing N^(b-1) times.
Subtract the sum of these residues from the sum of s_all and
divide by N. This gives (4.2) without a parity assumption.

Consequently det M_T is a unit. An integral square matrix with
unit determinant is invertible over R. Equation (1.2), including
the equality of image lattices rather than only their index,
now follows. Formula (1.3) counts tuples with each carry value.

This proof uses only finite products, valuations and the exact
two-factor determinant. It does not infer an integral lattice
from numerical invertibility at a nearby complex point.

### The relative source is an explicit bounded normal jet

The two lattices give a specified relative source module in this
marked degeneration:

    0 -> Lambda_leaf -> Lambda_carry -> Q_carry -> 0,
    Q_carry=direct_sum_(kappa(i)>0) R/(epsilon^kappa(i)).       (4.3)

Its nilpotence order is at most floor(b(N-1)/N)<=b-1,
independent of N for a fixed tensor size. It is a module supported
on a bounded nonreduced normal neighborhood, with all its exponents
determined by the two lattices.

Specialization is not injective on these two lattices. Its exact
sequence is

    0 -> Tor_1^R(Q_carry,k) -> Lambda_leaf/epsilon
      -> Lambda_carry/epsilon -> Q_carry/epsilon -> 0.        (4.4)

The middle comparison has image rank

    m_0=binomial(N+b-1,b),

since kappa=0 counts b-tuples with sum<N. Its lost source and
cokernel each have dimension N^b-m_0. Keeping the ordinary
image alone therefore loses genuine state directions.

There is also a uniform finite-jet evaluation rule. If A preserves
both lattices, its carry-frame specialization has entry

    (J_kappa^(-1) A J_kappa)_(ij)|_0
                   =coefficient_(kappa(j)-kappa(i)) A_(ij),  (4.5)

with a negative coefficient interpreted as zero. Thus M_T(0)
and at most b-1 normal jets of A suffice to compute its recoupled
specialization. The local crossing below needs only its zeroth
and first wrap coefficients. No analytic limiting process is
needed for this specialization theorem.

The subsequent [relative duality calculation](relative_pivotal_duality.md)
now constructs the dual inclusion Lambda_carry_sharp subset
Lambda_leaf_sharp. Its relative quotient pairs perfectly with
Q_carry in k((epsilon))/k[[epsilon]]. The residue pairing
is [epsilon^(kappa-1)]fg on each torsion summand, and it
pairs the lost Tor fiber perfectly with the dual residual
fiber. Thus turned source evaluations have a specified
finite normal pairing. Their actual tree rows are transported
by I_T^t, not replaced by arbitrary regular vacuum rows.
An explicit cyclic endpoint cap exhibits the single-wall
case: the retained first normal coefficient recovers a
missing cap column and yields the actual pivotal pairing.

## 5. Local moves preserve both integral lattices

For any two trees,

    F_(T,T')=I_(T')^(-1)I_T=M_(T')^(-1) M_T

is an integral isomorphism of their basic sources and also
of the actual sublattices (1.4). All loops are exactly the
identity. This proves path independence through the entire
degeneration, not merely on the punctured generic fiber.

The local arrow is the existing pointed recoupling, with its
spectators and permutations retained. For a rotation
((A,B),C)->(A,(B,C)), set A_X=sum_(j in X)a_j. On the
exceptional divisor its two affected relative factors are
related by

    C_(c,d), c=A_ABC/A_BC, d=A_BC/A_C.               (5.1)

These parameters and their required complements are nonzero.
All unaffected relative factors and the total factor are
spectators. Formula (5.1) follows either by specializing the
ordered relative-operator identities or by substituting (1.1)
in the exact three-factor pointed recoupling. Thus the pentagon
is the same algebraic two-to-three coherence with its full
factorial lattice; no scalar has been suppressed at the pole.

This theorem concerns recoupling networks. Arbitrary face turns,
an equivariant knot-character gluing and a presentation on an
arbitrary positive ideal triangulation are further constructions.

## 6. A regular crossing lift with its wrap source retained

Use the prescribed ADO color at q=q_N, Q=q^2, x=q^alpha,
M=-qx. The leaf evaluation basis can be changed by the units

    v_a=(Qalpha_j;Q)_a e_a, 0<=a<N.

They specialize to the original factorial basis, and the Borel
operator (1-X_j)sigma^(-1) in this frame is exactly

    F_j v_a=v_(a+1), a<N-1;
    F_j v_(N-1)=(1-t_j)v_0.                         (6.1)

The nonwrap coefficient is the cancellation of adjacent products;
the wrap coefficient is (1-alpha_j)(Qalpha_j;Q)_(N-1)=1-t_j.

Choose the actual nilpotent E(x) and the actual diagonal Cartan
factor D, both independent of epsilon in this regular frame. In
the finite universal crossing series replace only F_j by (6.1).
This is a specified auxiliary crossing lift. Since E^N=0 its
nilpotent series and inverse terminate at N-1 and are regular.
At epsilon=0 it is exactly the original positive/inverse ADO
crossing in its original basis. No generic braid relation for
this auxiliary lift is assumed.

Every nonzero transfer has k<=a<N on the E side. On the F side
it can wrap at most once. A nonwrap preserves the total integer
residue degree; a wrap lowers it by N and has coefficient
1-t_j=N a_j epsilon+O(epsilon^2). The checked permutation
preserves that degree. The inverse crossing has the same property.

It follows that every crossing and inverse preserve both
Lambda_leaf and Lambda_carry. In the carry frame a wrap has
the compensating factor epsilon^(-1), so its first coefficient
N a_j survives. Dropping that coefficient would discard a
real source term. Arbitrary products retain all repeated wall
and corner contributions.

The specialized carry operator is lower triangular with respect
to kappa. Its diagonal blocks are the actual truncated crossing
blocks; its off-diagonal blocks are the retained wrap sources.
In particular those blocks need not be zero even though their
closed diagonal traces vanish.

## 7. The selected cut trace is exactly the original meridian family

For a b-strand knot braid beta, use the original pivot
g=K^(1-N), residual twist theta=x^(1-N), and writhe w.
Let P_0 be the original rank-one cut projector onto v_0.
Put

    D_cut=P_0 tensor g tensor ... tensor g,
    Z_beta=theta^(-w) Tr(D_cut B_beta).               (7.1)

On the actual nilpotent module this is the original cut entry,
so Z_beta=F_N(M). It does not close the core with its vanishing
quantum dimension. The rank-one cut projector is retained.

The auxiliary lift has no degree-increasing transition. Any
closed diagonal path in (7.1) therefore contains no wrap.
Its weight is the actual nilpotent weight. Consequently

    Z_beta(epsilon,x)=F_N(M)                         (7.2)

as an exact identity in K(x), before specialization. The pivot
and cut projector are diagonal and preserve both lattices.

Transport all operators and the functional through I_T. Writing
I_T=J_kappa M_T, the recoupled operator on the basic source is

    B_T=M_T^(-1)(J_kappa^(-1) B_beta J_kappa)M_T.    (7.3)

It is integral, as is the transported cut insertion. At epsilon=0
its trace is still (7.2), now in the algebraically nondegenerate
relative factors (1.1) and the remaining total factor. The
cut insertion is generally a full matrix in these coordinates;
it must not be reset to a new coordinate projector or vacuum.
The local moves of Section 5 transport this same functional.

This gives an exact recoupled presentation of the actual ADO
meridian family for every knot and every N. All constants and
M-dependent factors remain fixed. Multiplying by the entire
original d_N(M) preserves the full ADO family and its whole
meridian germs. At M=1 the original Kashaev value is obtained.
The resulting sequence has exactly the same all-level meridian
annihilator ideal because it is the same sequence of rational
functions F_N(M), not a newly chosen state.

The argument does not claim that every specialized auxiliary
matrix defines a braid representation on the basic carry fiber.
The actual nilpotent representation is recovered on the actual
lattice (1.4); (7.2) supplies the selected period on the larger
recoupling presentation without that extra assertion.

The subsequent [semicyclic holonomy-braiding theorem](semicyclic_carry_braiding.md)
now supplies that extra assertion on a specified coherent
source family. Its corrected uncheck wrap and transported
centers give genuine holonomy braid maps. Their common fixed
line, with the actual endpoint rescalings, has equal carry
directions and yields a braid action on every basic recoupled
fiber as well as its actual sublattice. It also proves the
whole cut operator is the original scalar, rather than only
the trace identity above. Arbitrary frozen directions are
not substituted for that coherent family.

### An exact check that the retained source matters

For the figure-eight braid (sigma_1 sigma_2^(-1))^2 at N=2,
q=x=i, the selected cut trace splits by carry as

    carry zero: 3,  carry one: 2,  F_2(1)=5.         (7.4)

These are exact Q(i) matrix calculations, not numerical estimates.
For example E=[[0,1],[0,0]], F=E^t, D=diag(1,-i,-i,1),
R_plus=P D(1+2i E tensor F),
R_minus=(1-2i E tensor F)D^(-1)P, and g=diag(-i,i)
give (7.4) by the literal rank-one cut trace. The braid has
writhe zero. The carry-one directions are in the kernel term
of (4.4). Retaining only the specialization image would yield
3 instead of 5. Thus that source term cannot be omitted even
when the final scalar period is the only quantity of interest.

## 8. Relation to the source torsor and the remaining geometric step

Each factor in (2.1) is one of the actual factorial primitives
of [the source-torsor theorem](factorial_source_torsor.md).
The carry theorem controls their complete tree contraction,
including all simultaneous poles, rather than specializing
them separately. It extends the local two-step lattice to
arbitrary tensor size and proves that its recoupling paths
preserve the actual cut period, all root parities included.

The direction labels are a configuration of distinct cumulative
points A_0=0,A_1,...,A_b. Their relative cyclic factors and local
recouplers are nondegenerate, but they have not been identified
with the complete flat knot representation or its positive
geometric triangulation. The actual interior threading character
and the fixed hyperbolic character remain distinguished as in
[the threading theorem](ado_threaded_shadow.md).

The next comparison must construct the colored/polarized global
gluing and transport this full period functional, source lattice,
peripheral lifts and root factors. It must also prove the selected
Bloch-regulator norm across N. The uniform recoupling and exact
period identities above do not themselves supply that norm or
prove the volume conjecture.

The degeneration source Q_carry is not yet identified with the
source of an inhomogeneous meridian A-equation. Its bounded
normal thickness makes finite nilpotent descent available once
the relevant operator and central data match; that match remains
a comparison to prove.

## 9. Coverage and exact diagnostics

Cyclic Borel recoupling and its pentagon already have the
Kashaev 6j origin recorded in
[the pointed recoupling note](pointed_steinberg_recoupling.md).
The comparison with the literature cyclic dilogarithm and its
singular factorial frame is in the source-torsor note. No
external integral-lattice or global state-comparison theorem
is assumed in Sections 2--7; their proof is the finite-product
carry count, determinant and literal cut trace above.

[The exact audit](../experiments/audit_carry_recoupling_lattice.py)
constructs the row-scaled leading matrices from their valuations
and leading coefficients. It verifies unit determinants for 83
tree presentations, including every ordered tree on up to six
leaves at N=2. It checks 120 local rotations against the
independently constructed pointed Clebsch matrix, with exact
spectators. Thus its local-move checks are not only products
of a matrix and its computed inverse.

At N=2,3,4,5,6 it retains genuine wrap terms, verifies inverse
crossings, and compares 30 actual generic/Kashaev cut periods
in both three-leaf trees. All pivot and writhe factors are
included. Higher even and composite levels through 12 enter
the lattice and local-move checks. These are finite diagnostics
for the uniform proof, not a geometric or asymptotic theorem.
The audit also verifies (7.4) symbolically over Q(i), and records
the carry-sector contributions in all 30 finite-field periods.
Results: [carry_recoupling_lattice_results.json](../experiments/carry_recoupling_lattice_results.json).

    python3 experiments/audit_carry_recoupling_lattice.py

## 10. Source flags and the actual total frame

The subsequent [source flag carry extension](source_flag_carry_extension.md)
now realizes the normal directions as distinct cumulative flags
delta_i with an auxiliary source point. In the moving-source
chart every endpoint root has a common epsilon^(1/N) factor.
Including the actual total source frame leaves exactly the
row power epsilon^(-kappa); this gives the same carry lattice
for every finite source flag. The matrix extends as an
invertible one at the marked source infinity by this note's
valuation argument, which also applies to roots with the
same nonzero first coefficients and arbitrary higher terms.

The actual sublattice, dual linking form and original whole
cut operator extend together. In particular this transports
the complete period and its Tor contribution, rather than
only the ordinary image. The full geometric colored gluing,
marked meridian identification and regulator norm remain
the outstanding global comparison.
