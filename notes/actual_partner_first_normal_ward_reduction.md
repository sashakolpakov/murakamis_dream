# A general two-current reduction of the first Racah normal

**Later result, 29 October 2026:** the
[full all-partner first-normal theorem](actual_all_partner_first_normal_bound.md)
now bounds the remaining actual currents, using a positive presentation
of the complete generic source on face-supported branches. The
reductions and sharp rank obstructions below remain valid for the
particular Ward/Fourier relations studied here. Their undetermined
components are not counterexamples to the later source theorem.
General higher normals and completed physical transport remain open.

29 October 2026. The exact physical cluster Ward identity first reduces
the first normal of all sixty-four reflected Racah branches to at most
THREE potentially live-tail currents. Combining it with the independently
proved Fourier partner involution reduces this to at most TWO, uniformly
for every supported folded sextuple. The remaining entries have the
proved positive-core normal bounds. In particular, when at least two
opposite edge pairs have equal folded labels, every partner first
normal has a uniform polynomial bound, including branches with a
nonempty second-zero tail. This is a first-normal statement, not an
all-order or physical Hermitian transport theorem.

## 1. The actual scalar and its opposite-pair Ward equation

Use the integer-spin supported folded sextuple and actual generic
normalization of [the partner reflection theorem](actual_racah_partner_reflection_identity.md):

    D=N-1, 0<=j_i<=D/2,
    K_B(zeta)=[N]^2 S_B(zeta)^2 product_faces Delta_B^2,
    k(B)=D_log(zeta) K_B(q), q=exp(pi i/N).

Here B is a choice of six partner bits, and the generic seven-factorial
sum, all face normalizations and every [2N] current remain present.
All root values are the same strictly positive number W_N^2. In the
label order (a,b,c,d,e,f), the opposite edge pairs are

    (a,c), (b,d), (e,f).                              (1)

For either internal pair e,e*=D-e and f,f*=D-f, the proved generic
source-projector identity gives

    sum_(i,j=0,1) d_(e_i)d_(f_j) K_(i,j)
                 =[N]^2 tr(E_e E_f)=O(t^2),
    d_j=[2j+1], t=log(zeta/q).                        (2)

If both pairs are nontrivial, d_e*(q)=-d_e(q) and likewise for f.
When differentiating (2), the part differentiating the dimensions
is exactly W_N^2 times the derivative of

    (d_e+d_e*)(d_f+d_f*),

which vanishes at t=0 because both factors vanish there. The remaining
coefficient in (2), divided by the two nonzero root dimensions, is

    k(0,0)-k(0,1)-k(1,0)+k(1,1)=0.                 (3)

If one partner is simple, its two bit choices label the same generic
function, so (3) is tautological. Tetrahedral edge relabeling proves
(3) for each of the three pairs in (1), for EVERY choice of the
other four partner bits. This is the actual generic first normal;
it is not a differentiated equality of root values.

Thus k belongs to the tensor product of three three-dimensional
spaces of functions on a square satisfying its additive equation.
Equivalently its multilinear Boolean expansion has no coefficient
containing both members of any opposite pair. Its dimension is at
most 27; simple/duplicate branches may reduce that dimension.

## 2. An explicit interpolation with at most three unbounded inputs

For each folded edge put delta_i=D/2-j_i>=0. Within each opposite
pair order the edges so that delta_big>=delta_small, and write

    s_r=delta_big+delta_small,
    d_r=delta_big-delta_small>=0,  r=1,2,3.          (4)

A partner bit zero means a low label D/2-delta, and one means
D/2+delta. On the r-th pair retain these three bit states:

    0=(0,0),  -=(0,1),  +=(1,0).

Their deviations of the pair's label sum from D are respectively

    u_r(0)=-s_r, u_r(-)=-d_r, u_r(+) = d_r.       (5)

The omitted state (1,1) is reconstructed, by (3), as

    k(...,11,...) = k(...,-,...) + k(...,+,...)
                                      - k(...,0,...). (6)

Apply (6) independently to the three pairs. Every one of the 64
first normals is an explicit signed sum of at most 27 entries in
the grid {0,-,+}^3. Its coefficient absolute sum is at most 27;
no division by a small color difference or by a quantum dimension
occurs in this interpolation.

The opposite sums in the actual seven-factorial range are exactly

    Q_1=2D+u_1+u_2,
    Q_2=2D+u_1+u_3,
    Q_3=2D+u_2+u_3.                               (7)

The existing tail-free theorem applies whenever min Q_r<=2D.
A grid point failing that condition has all three pairwise sums
u_i+u_j strictly positive. It must therefore have at least two
positive u's, hence at least two '+' states. The only possibilities
are:

* (+,+,+), if all pairwise sums d_i+d_j are positive;
* '+' on two pairs and '-' on pair r, only if
  d_r<min(d_i,d_j);
* '+' on two pairs and '0' on pair r, only if
  s_r<min(d_i,d_j).

In each of the last two cases r must be the UNIQUE strict minimum
of the three d's, since s_r>=d_r. Consequently there are at most
THREE such grid points. This is an exact all-label assertion, with
strict inequalities at the boundary handled as written.

Let E be this explicit exceptional set. By the proved tail-free
bound there are absolute C,c such that, for every partner B,

    |k(B)| <= 27 C N^c W_N^2 + sum_(v in E)|k(v)|. (8)

The coefficient of any retained grid entry in the expanded formula
is 0,+1 or -1, explaining the unit coefficient on the exceptional
sum. No claim that its terms are individually polynomial is needed
to prove (8).

## 3. A complete first-normal theorem with genuine live tails

If at least two of the three opposite pairs have equal folded
labels, at least two d_r vanish. Every point of the interpolation
grid has a nonpositive pairwise sum, so E is empty. Equation (8)
then proves, uniformly on this supported class and all its partner
branches,

    |D_log(zeta) K_B(q)| <= C' N^c W_N^2.          (9)

This includes every supported disphenoid label pattern
(a,b,a,b,e,e), and permits one of those opposite equalities to be
removed. It controls a first normal even if B itself has min Q_B>2D.
For example N=3m+1 and folded labels all m have all-high partners
all 2m, whose range z=6m,...,8m has a nonempty [2N] tail for every
m>=1. All those first normals satisfy (9).

The same conclusion bounds the coherent tail VALUE T(q)/C(q)
polynomially for this class. Indeed the exact scalar has

    K_B=U_B G_B^2, G_B=C_B+[2N]T_B,
    U_B=[N]^4 product_faces Delta_B^2,

where U_B is a nonzero analytic unit after the four face zeros are
canceled. Its logarithmic derivative and C_B'(q)/C_B(q) have the
proved polynomial unit-factorial bounds. Divide the derivative
of K_B by its root value U_B(q) C_B(q)^2 and use (9). This bounds
G_B'(q)/C_B(q), hence T_B(q)/C_B(q), because

    D_log(zeta)[2N](q)=4N/(q-q^-1)

is nonzero with a polynomially bounded inverse. The independent
[finite Fourier residue theorem](actual_coherent_racah_tail_fourier_residues.md)
now proves the sharper all-high cotangent formula and controls every
branch with a repeated maximal face. Those are additional identities;
they are not obtained by differentiating the Ward interpolation.
Neither argument supplies a bound for derivatives of T_B.

## 4. Why the first-order identity does not determine higher normals

The right side of (2) is only O(t^2), and its second coefficient
contains the actual finite cluster overlap tr(E_e(q)E_f(q)).
Second differentiation also produces first derivatives of quantum
dimensions multiplying k(B). Thus the homogeneous equation (3)
cannot be imposed on second or higher normals. No positive physical
metric, small condition number, or complete marked-source bound is
inferred from the first-normal interpolation.

Even at first order the remaining exceptional currents cannot in
general be recovered from tail-free values and (3) alone. In fact
THREE is sharp for this method. Choose delta=(5,19,3,9,4,16) in the
original edge order and D=80, hence folded labels
(35,21,37,31,36,24). All faces satisfy the support inequalities.
Exact linear algebra on the 27-dimensional space shows that its
48 tail-free vertices impose rank 24, leaving THREE unconstrained
directions. The audit constructs this rank over the rationals.
This is an obstruction to that interpolation method, not a
counterexample to a bound for the actual source function.

The proof consists of the actual projector identity (2), its
careful first derivative, and the finite interpolation and support
inequalities above. The [audit](../experiments/audit_actual_partner_first_normal_ward_reduction.py)
also checks the full generic normal coefficients in finite root
fields; it does not replace the proof by sampled values.

## 5. The Fourier partner involution reduces three currents to two

The [finite Fourier theorem, section 6](actual_coherent_racah_tail_fourier_residues.md#6-the-residual-is-an-exact-partner-involution)
now proves an additional ACTUAL first-normal relation. For a live
branch with a unique largest face, let B* flip the three complementary
edges while retaining that face. Then

    |k(B)-k(B*)| <= C N^2(1+log N) W_N^2.          (10)

This includes all face normalizations. It follows from the exact
coherent tail difference, equality of the two positive cores, and
their separately bounded generic core and face-factor derivatives.

Together, (3) and (10) reduce EVERY supported sextuple to at most TWO
uncontrolled partner first normals. Here is a uniform proof, including
the only case not already settled by section 2.

If its exceptional set E has at most two elements, there is nothing
to do. If E has three elements, relabel the opposite pairs so that

    s_1 < min(d_2,d_3).                           (11)

On the FULL 64-vertex cube, the live-tail condition is now exactly
that the larger-deficit edge of pair 2 and the larger-deficit edge
of pair 3 both have their high bit set. Indeed a high dominant bit
in pair i gives u_i>=d_i, while a low one gives u_i<=-d_i. Also
|u_1|<=s_1. Thus both dominant bits high make every pairwise sum
positive, while either dominant bit low makes its sum with u_1
negative. The live set is a 16-vertex cylinder, independent of the
other four bits.

Call those two dominant edges p and q. They belong to a unique
tetrahedral face together with one edge r of pair 1; call its opposite
edge r*. That face is the UNIQUE largest face everywhere in the
live cylinder. To check this without an incidence guess, the four
faces are

    (p,q,r), (p,q*,r*), (p*,q,r*), (p*,q*,r).

Writing each label as D/2 plus its signed deficit, the first face
exceeds the second by at least d_3-s_1>0, the third by at least
d_2-s_1>0, and the fourth by at least d_2+d_3>0. Thus (10) applies
everywhere in this cylinder, and its move flips precisely r*,p*,q*.

Changing the bit p* with p high changes k by a controlled quantity:
the Ward equation (3) says that this difference equals the same
difference with p LOW, and both of those entries are tail-free by
the cylinder description. The identical assertion holds for q*.
Consequently their two flips in (10) can be removed at polynomial
cost. What remains is a polynomial bound for changing r* alone
within the cylinder.

In the 27-point interpolation grid the three exceptional entries
are exactly the three pair-1 states 0,-,+, with pairs 2 and 3 in
state '+'. The last relation identifies, up to polynomial cost,
the state 0 with either '-' or '+', according as r* is the smaller-
or larger-deficit edge of pair 1. Eliminate state 0. At most two
actual partner values remain. Explicitly there is a set R of at
most two partner branches such that

    max_B |k(B)| <= C N^c W_N^2 + 2 sum_(v in R)|k(v)|. (12)

All constants are uniform in N and the supported labels. No small
matrix determinant is inverted: the proof uses the signed Ward
interpolation, at most two tail-free bit differences, and one
controlled Fourier partner difference. This is a reduction of the
remaining problem, not a bound for the two residual currents.

TWO is sharp for these relations. For the D=80 example in section 4,
the live cylinder is exactly b=f=1. Its unique largest face is
(b,c,f), and its Fourier partner move flips (a,d,e). In Boolean
notation both functions

    h_1(B)=b f,  h_2(B)=b c f

vanish on all tail-free vertices, obey every opposite-pair Ward
equation, and are unchanged by every applicable Fourier partner move.
They are linearly independent. There is no live repeated-maximal-face
vertex in this example. Equivalently the exact combined constraint
matrix has rank 25 in the 27-dimensional Ward space. Hence these
relations alone leave two free components, even after every known
bounded vertex and every applicable involution is used. They do not
prove the general first-normal estimate or higher-order transport.

The focused audit freshly passes 33 actual source families, all 64
first-normal reconstructions for each family, 3,000 deficit-pattern
classifications (including the cylinder and unique-face implications),
and exact rational ranks 24 and 25 for the separate and combined
constraints. These checks supplement the uniform argument above.