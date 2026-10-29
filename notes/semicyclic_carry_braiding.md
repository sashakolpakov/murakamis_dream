# Genuine holonomy braiding on the common carry lattice

Research note, 26 October 2026. This replaces the frozen auxiliary
crossing of [the carry-lattice construction](carry_recoupling_lattice.md)
by an explicit genuine semicyclic holonomy braiding. A retained central
factor corrects the wrap, the transported centers obey a linear braid
map, and a common fixed center line gives a braid action on every
recoupled integral source and its special fiber. The entire original
ADO cut operator, not just its trace, is recovered with its meridian,
pivot, twist and modified dimension unchanged.

These are statements on the E^N=0 semicyclic locus. This locus represents
reducible knot characters. No identification with the complete
irreducible geometric character or its selected regulator norm follows.

## 1. The source modules and their fixed highest-weight flag

Put q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), N>=2, and k=x^N.
On V(x,phi), with basis v_0,...,v_(N-1), use

    K v_a=x Q^(-a)v_a,
    E v_a=e_a v_(a-1), E v_0=0,
    e_a=[a]_q (x q^(1-a)-x^(-1)q^(a-1))/rho,
    F_phi v_a=v_(a+1), a<N-1,
    F_phi v_(N-1)=phi v_0.                          (1.1)

These are the regular modules already constructed on the semicyclic
section of [the holonomy splitting chart](regular_holonomy_braiding.md):

    E^N=0, F^N=phi, K^N=k,
    Omega=rho^2 FE+qK+q^(-1)K^(-1)=qx+q^(-1)x^(-1).           (1.2)

The wrap of F never enters FE because E has no output v_(N-1).
This directly checks that the Casimir and commutator are unchanged.
For generic x the e_a, a>0, are units, and K projectors together
with the nonwrap E,F arrows generate every matrix unit, for every phi.
The vector v_0 is a fixed highest-weight flag throughout this locus.

The rational holonomy automorphism r and its center map are the
independently proved formulas in that linked note. Here its central
divisor is identically one because E_1^N=0. In raw F-power coordinates
the uncheck center transport is

    phi'_1=phi_1/k+(1-k^(-2))phi_2,
    phi'_2=phi_2/k.                                 (1.3)

The K roots and the individual Casimirs stay fixed.

## 2. An explicit global intertwiner, with the correct wrap factor

Let D be diagonal on the pair:

    D v_(a,b)=x^(-a-b)Q^(ab) v_(a,b),
    c_n=q^(n(n-1)/2)rho^n/[n]_q!.

Define

    R_(phi_1,phi_2)
      =D sum_(n=0)^(N-1)c_n E_1^n F_(2,phi_2/k)^n.           (2.1)

It maps V(x,phi'_1) tensor V(x,phi'_2) to
V(x,phi_1) tensor V(x,phi_2), intertwining the target
generators with r applied in the source. In particular the
wrap is phi_2/k, not phi_2. At the Kashaev color,

    x_0=q^(N-1), k_0=(-1)^(N-1),

so the missing factor is -1 at even levels. Before specialization
it is the whole function x^(-N).

All denominators [n]_q!, n<N, are nonzero. The series is a
polynomial in a nilpotent operator, with constant term one;
its inverse is the corresponding finite inverse Euler series.
Thus (2.1) is invertible for every phi and x!=0. It fixes v_00.

Here is a proof of every intertwining equation without assuming
a published semicyclic R formula. Write Theta for the finite
sum in (2.1), and U=q rho^2 E_1 F_(2,phi_2/k). The Euler
coefficient identity gives

    Theta(QU)=Theta(U)/(1-U), U^N=0.                (2.2)

Consequently its K conjugations are exact finite identities.
The Cartan factor satisfies

    D E_1 D^(-1)=E_1 K_2,
    D F_(2,phi_2/k) D^(-1)=K_1^(-1)F_(2,phi_2).    (2.3)

In the second equation a nonwrap has ratio x^(-1)Q^a;
the wrap has ratio x^(N-1)Q^a and its factor phi_2/k
restores exactly the same coefficient. This is the origin
of the central correction.

E_1 and F_(2,phi_2/k) commute with Theta. Combining (2.2)--(2.3)
therefore intertwines E_1,F_2,K_1,K_2 with precisely their
four rational holonomy images. No derivative or omitted
Nth Euler coefficient is used.

The remaining two generators are forced. On phi_2!=0, F_2 is
invertible, so its Casimir and K determine E_2 uniquely. For
the first factor, put the already matched K_1,E_1 in their
standard weight-string basis. Its Casimir determines every
nonwrap F_1 arrow. The weight relation allows only the remaining
arrow v_(N-1)->v_0, with an arbitrary matrix on the spectator.
F_1^N=phi'_1 fixes that matrix to phi'_1 times the identity.
Both representations have the same Casimirs and (1.3) is
the proved central map, so F_1 also agrees. This proves all
six equations on a dense open set. The intertwiner and its
inverse have only monomial x and fixed root denominators;
the holonomy denominators are finite nilpotent inverses.
Clearing them extends the identities to all phi and all
defined colors, including the original nilpotent section.

The uncheck determinant is independent of phi. Every wrap lowers
integer residue degree, and every nonzero transfer lowers the
first index before checking. Thus only the diagonal D contributes:

    det R=x^(-N^2(N-1)) Q^((N(N-1)/2)^2).           (2.4)

This is the original nilpotent determinant. Its anchored scalar
normalization is therefore exactly the one in the existing
holonomy note, with no new phi-dependent scalar.

## 3. Checked maps transport their centers

Let P be the literal flip. As a map from the input pair with
centers (u,v) to its transported output, the positive crossing is

    B^+(u,v)=P D sum_(n<N)c_n E_1^n F_(2,v)^n,
    (u,v) -> L_-(k)(u,v),
    L_-(k)=[[0,k],[k,1-k^2]].                       (3.1)

This follows by applying (2.1) at the swapped output centers.
Its source correction phi_2/k then equals the input v exactly.
Thus the old wrapped positive matrix can be used with the
proper center transport; holding arbitrary centers fixed
would use a different composition rule.

The inverse crossing at input (u,v) is

    B^-(u,v)=Theta_(u/k)^(-1) D^(-1)P,
    (u,v) -> L_+(k)(u,v),
    L_+(k)=[[1-k^(-2),k^(-1)],[k^(-1),0]].          (3.2)

The matrices L_- and L_+ are inverse. These are precisely
the classical polynomial-block matrices of
[the Frobenius Verma calculation](frobenius_verma_period.md).
The quantum holonomy and Frobenius center transports now have
the same explicit convention, rather than an unmarked identification.

## 4. Strict braid coherence on the semicyclic locus

The rational holonomy automorphisms satisfy the three-factor
identity by the earlier direct algebra proof. With (3.1)--(3.2)
transporting the centers, the two braid composites intertwine
the same split full matrix algebra with the same target centers.
They differ by one scalar on the generic regular chart.

Every crossing (2.1), checked crossing, and inverse fixes the
tensor highest-weight vector v_00. Therefore the two composites
both fix v_000, forcing that scalar to equal one. This proves
the braid relation exactly, without an unspecified determinant
phase. It holds over the entire semicyclic affine center chart
by the same polynomial continuation as in Section 2, including
even and composite N. Positive and negative maps are literal
inverses when the intermediate centers are updated.

The fixed highest-weight flag is essential to this argument.
On the full cyclic locus with E^N!=0 that flag is absent;
the general phase cover has not been removed by this special
coherence theorem.

## 5. A common fixed line and the even-level endpoint mark

For b strands the line

    phi_j=z k^(1-j), j=1,...,b,                     (5.1)

is fixed by every embedded L_+ and L_-. Substitution in each
two-by-two matrix proves this directly. Hence on this line
the matrices are endomorphisms of one ordered tensor module
and obey the ordinary braid relations.

Retain the unit endpoint change

    c_j=x^(j-1), S_j v_a=c_j^a v_a,
    F_j^new=c_j F_j, E_j^new=c_j^(-1)E_j.           (5.2)

In the new leaf frame the F central parameters are all

    (F_j^new)^N=c_j^N phi_j=z.

At M=1 these are exactly c_j=(-q)^(1-j), the previously
derived actual coproduct endpoint marks. For even N their
Nth powers remove the alternating raw center signs. This
is an explicit root/meridian function, not a numerical
choice made after evaluating M=1.

Choose z=1-(1-epsilon)^N. After (5.2), all leaves have the
same Borel parameter t_j=1-z=(1-epsilon)^N. The common carry
theorem applies with every direction a_j=1. Every relative
parameter specializes to

    tau_I(0)=|I|/|R| !=0,1.                         (5.3)

The endpoint change is diagonal and a unit and thus commutes
with the carry weights. Every genuine crossing and inverse
preserves both leaf and carry lattices: a wrap still lowers
residue degree by N and has one factor z. Therefore its
conjugation to each basic recoupled source is integral.

The braid identities hold over R before specialization, so
they hold on every basic recoupled carry fiber as well as
on its actual source sublattice. This upgrades the auxiliary
trace construction to a genuine braid action in each integral
recoupling chart.
The arbitrary frozen-direction lift in the preceding note is
not asserted to have this property; (5.1)--(5.2) supply it.

The recoupling statement is a transport of linear modules and
operators with the given endpoint frames. A complete assignment
of colored tensor-face data to a positive geometric knot
triangulation is still required.

## 6. The entire selected cut operator remains the actual ADO one

The finite crossing matrices in (3.1)--(3.2) have no degree-
increasing term. A wrap lowers the integer residue sum by N.
This holds for any transported semicyclic parameters, not
only the common fixed line. Close b-1 strands with the original
diagonal pivot and keep the original open N-dimensional strand.

For an entry from cut index a to a', closing the other strands
makes the total degree change equal a'-a. On the other hand
it is -N times the number of wraps. Since 0<=a,a'<N, the
only possibility is a'=a and no wraps. Thus the whole cut
operator has exactly its original nilpotent entries:

    C_(beta,N)(x;phi)=F_N(M) I_N, M=-qx.             (6.1)

All pivot and zero-framing twist factors are the original ones.
At a closed center fixed point this is a literal semicyclic
holonomy cut evaluation. The same finite matrix identity also
holds before imposing center closure; that extra assertion
does not define a new geometric-character invariant.

Any vector/covector pair with value one can evaluate the scalar
operator (6.1). This includes the original highest-weight cut
and its already proved factorial/Whittaker frame. After a
recoupling the corresponding insertion is transported as the
full matrix; it is not reset independently in the new chart.

The determinant normalization from (2.4) uses the original
same-color scalar s=x^(N-1)q^(-(N-1)^2/2). Its compensating
twist is s*x^(1-N)=q^(-(N-1)^2/2), exactly as on the nilpotent section.
The zero-framed evaluation and its full factor remain exactly

    F_N(M), d_N(M)F_N(M),
    d_N(M)=i^(N+3)M^(N-1)/(1+M^2+...+M^(2N-2)).     (6.2)

All meridian germs, the Kashaev value, and the actual all-level
meridian annihilator ideal are consequently retained. The
raw k=x^N, its even-level sign, and the separately known full
ADO shift sign have not been discarded or identified by fiat.

## 7. What this closes and what remains

There is now an explicit genuine holonomy braiding through the
actual semicyclic source, a common fixed center line with the
correct endpoint marks, and an integral braid action compatible
with every recoupling tree and the full actual cut operator.
The scalar is fixed by a highest-weight flag and the wrap by
its central character. These comparisons use actual operators
and evaluations, not only matching algebra dimensions.

The E^N=0 locus is preserved by the center maps. Its meridian
holonomies are triangular after the existing prefix change,
so its closed knot representations are reducible. The common
fixed line does not represent complete irreducible hyperbolic
holonomy. The previously constructed Alexander attachment
points and mixed E/F deformation problem remain relevant.
No Hilbert-90 change can remove that central-character distinction.

Transport to the equivariant colored positive triangulation,
identification of the meridian source with its marked Bloch
period, and the selected regulator norm across N remain to
be proved. The volume conjecture is not established here.

The subsequent [four cyclic-atom theorem](four_cyclic_atoms.md)
now writes the explicit crossing (2.1) as four literature cyclic
dilogarithm matrices in changing central frames. Their norm
roots and determinant normalizations, the Cartan map and one
external root are all retained. A formal source anchor fixes
the remaining finite scalar. This is an actual root-level
operator factorization, not separate specialization of compact
infinite products. It supplies local tetrahedron data while
leaving the geometric global source and selected norm open.

## 8. Coverage and exact diagnostics

This lies in the existing Kashaev--Reshetikhin holonomy-braiding
and semicyclic quantum-group framework, whose statement coverage
is recorded in [the regular holonomy note](regular_holonomy_braiding.md).
The abstracts of [Kashaev--Reshetikhin, math/0202212](https://arxiv.org/abs/math/0202212)
and [McPhail-Snyder--Reshetikhin, 2509.02354v2](https://arxiv.org/abs/2509.02354v2)
were checked for this coverage, including the latter's four-dilogarithm
and holonomy Yang--Baxter scope. Their proofs are not used here.
The root module is the literature quantum-group module (1.1),
and the actual knot invariant is unchanged. No new general
semicyclic invariant or novelty claim is made. The four-generator,
Casimir, center and highest-weight arguments above give the proof
without importing a published R-matrix or coherence proof.

[The exact audit](../experiments/audit_semicyclic_carry_braiding.py)
checks all six generator intertwinings in 18 cases at nine
levels through 12, retaining the wrap factor k^(-1). It
checks ten dynamically transported braid/inverse cases and
compares freezing the wrong centers. On the common fixed
line it checks the genuine braid in both three-leaf carry
frames and 60 original recoupled cut periods. It separately
checks 30 entire scalar cut matrices with arbitrary transported
centers, at generic and Kashaev colors. All passed.
Results: [semicyclic_carry_braiding_results.json](../experiments/semicyclic_carry_braiding_results.json).

    python3 experiments/audit_semicyclic_carry_braiding.py

The subsequent [braided source atlas](braided_source_groupoid.md)
also handles varying centers through every tree/source chart,
including the line data at source infinity. For that construction
the explicit inverse endpoint factors c_j=x^(-j), j starting at
zero, make the normalized total Y exactly the original coproduct
of F. The normalized wraps are k^(-j)a_j and their center maps
depend on U=k^2=M^(2N), preserving their total. This is a different
coordinate choice from (5.2), whose purpose was to make the fixed
line have equal wraps. All inverse/source factors remain explicit.
The full arrows act on the relative factors and preserve the
selected original cut. The actual meridian-source equation and
nontrivial pure-braid jet are derived in the companion note;
the complete geometric gluing and regulator norm remain unproved.
