# The untruncated Verma period and its exact Alexander factor

Research note, 26 October 2026. This constructs a single graded Verma
cut series and proves its exact rational specialization at every root
q_N=exp(pi*i/N), including even and composite levels. Its root period
is the actual reduced ADO state divided by the full Alexander factor
Delta_K(M^(2N)). This root normalization already occurs in Willetts;
Section 9 records the statement coverage. The proof here is an
independent crossing, filtration and polynomial-trace calculation.
It does not assume a completion theorem or identify the generic
graded series with a completed literature invariant.

The root state has exactly the original all-level quantum A-ideal
and the original Kashaev specialization. The construction also turns
the [reducible period anchors](closed_braid_period_line.md) into
explicit polar data. It does not yet identify this period with the
marked Bloch regulator or prove the volume conjecture.

## 1. A graded cut series with no root-dependent truncation

Put Q=q^2 and x=q^alpha. On the infinite highest-weight Verma basis
v_a, a>=0, use

    K v_a=xQ^(-a)v_a,
    E v_a=[a]_q[alpha-a+1]_q v_(a-1), F v_a=v_(a+1).

For a fixed input vector the universal crossing sum is finite.
After removing its common Cartan factor, cancel the divided-factorial
denominators before specializing. In terms of the polynomial
Gaussian coefficient {a choose n}_Q the positive checked entry is

    R^+_(b+n,a-n; a,b)
       =x^(-a-b+n)Q^((a-n)b){a choose n}_Q
                      (x^(-2)Q^(a-n);Q)_n, 0<=n<=a.           (1.1)

The negative checked entry is

    R^-_(b-n,a+n; a,b)
       =x^(a+b-n)Q^(-ab){b choose n}_Q
                      (x^2 Q^(1-b);Q)_n, 0<=n<=b.            (1.2)

To derive (1.1), write the product of the n E coefficients as
[a]_q!/[a-n]_q! times the color product, use
{a choose n}_q=q^(-n(a-n)){a choose n}_Q, and combine the Cartan
exponent. For (1.2) apply the inverse Cartan first and reverse the
color-product factors; the signs and quadratic powers cancel.
Thus every displayed coefficient is Laurent polynomial in q,x.
There is no [N]_q denominator left to interpret.

At generic q these are the mutually inverse checked Verma crossings.
Their identities follow from the formal R coefficient recurrence
already derived in the [local braiding note](regular_holonomy_braiding.md).
Each homogeneous total-index sector is finite, and its entries are
Laurent polynomials. Those identities therefore specialize at roots
by polynomial identity. Terms with n>=N are included; they need
not vanish after the cancellation in (1.1)--(1.2).

Let beta be a b-strand braid of writhe w whose closure is K, and
put c=b-1-w. Let B_beta be the product of these checked crossings
and inverses. Define the auxiliary graded series

    V_beta(q,x;tau)=x^c sum_(a_2,...,a_b>=0)
        tau^(a_2+...+a_b)Q^(-a_2-...-a_b)
        <0,a_2,...,a_b|B_beta|0,a_2,...,a_b>.       (1.3)

The factor x^c combines the ordinary pivot K on the closed strands
and the residual twist x. Every coefficient of tau is a finite
sum: crossings preserve total index, so all intermediate indices
are bounded by that coefficient's total degree. Consequently
(1.3) is defined in Z[q^(+/-1),x^(+/-1)][[tau]]. This assertion
does not require convergence or a value at tau=1 for generic q.
The graded auxiliary series is not asserted to be a knot invariant.

## 2. Exact Frobenius block decomposition

Now q=q_N, Q of order N, and k=x^N. Write

    a=NA+r, b=NB+s, n=NC+t, 0<=r,s,t<N.

The root Gaussian identity is

    {NA+r choose NC+t}_Q={A choose C}{r choose t}_Q.             (2.1)

For an elementary proof, expand product_(j=0)^(a-1)(1+Q^j z)
by Gaussian coefficients and factor each full N-cycle as
1-(-z)^N. Comparing coefficients proves (2.1), with the cycle
signs canceled by the Gaussian prefactor. No primality assumption
on N enters. Also

    (hQ^j;Q)_(NC+t)=(1-h^N)^C(hQ^j;Q)_t.        (2.2)

Substitution in (1.1) gives its residue entry at (r,s,t) times

    {A choose C}k^(-A-B+C)(1-k^(-2))^C.           (2.3)

Substitution in (1.2) gives its residue entry times

    {B choose C}k^(A+B-C)(1-k^2)^C.               (2.4)

The positive output block indices are (B+C,A-C), apart from a
possible carry when s+t>=N. The negative ones are (B-C,A+C),
apart from a carry when r+t>=N. A carry lowers the sum of the
residue indices by exactly N. Nonzero entries have t<=r in the
positive case and t<=s in the negative case. Thus neither sign
can increase total residue degree.

Identify the block indices (A_1,...,A_b) with monomials in
Z_1,...,Z_b. The carry-free block actions (2.3)--(2.4) are the
symmetric-power actions of the mutually inverse matrices

    L_+(k)=[[1-k^(-2),k^(-1)],[k^(-1),0]],
    L_-(k)=[[0,k],[k,1-k^2]].                      (2.5)

On the associated graded for total residue degree, the entire
Verma crossing therefore factors as

    actual finite checked R_N^sign tensor Sym L_sign(k).
                                                            (2.6)

The finite residue part is exactly the actual truncated ADO crossing:
a carry is precisely the term removed by its nilpotent F endpoint.
This proves the comparison rather than replacing the finite R by
an unverified cyclic one.

Every closed diagonal term in (1.3) returns to its initial residue
degree. Since all carries strictly lower that degree, none can
occur on a contributing path. Hence (2.6) computes the full graded
cut trace exactly, not only its leading term.

## 3. Polynomial blocks give a rational period

Let L_beta(k) be the product of (2.5) embedded in b dimensions,
in the same operator order as B_beta. Delete its first row and
column and call the resulting matrix A_beta(k). Define

    D_beta(k;z)=det(I-z A_beta(k)).

The first block index is cut at zero. Projecting the first output
block to zero amounts to setting Z_1=0. The remaining polynomial
trace is therefore the trace on Sym of A_beta, and

    sum_(d>=0) z^d Tr(Sym^d A_beta)=1/D_beta(k;z).               (3.1)

For a proof, verify the identity on diagonal matrices by multiplying
geometric series. For each coefficient both sides are polynomials
in the matrix entries; diagonalizable matrices are Zariski dense.
The coefficient identities follow for all matrices, including
nondiagonalizable ones. The identities have integer coefficients,
so they also support the exact finite-field diagnostics.

Let P_(N,beta)(x;tau) be the finite residue cut polynomial: sum
over 0<=r_2,...,r_b<N with the same factors x^c Q^(-sum r_i)
and tau^(sum r_i) as in (1.3). Combining (2.6) and (3.1) proves

    V_beta(q_N,x;tau)
       =P_(N,beta)(x;tau)/D_beta(x^N;tau^N).       (3.2)

This is an identity of formal tau series and hence an explicit
rational continuation in tau. The denominator, including its
polar divisor, is retained. Equation (3.2) also specifies its
actual relative algebraic equation D_beta V_beta=P_(N,beta).
Its shift/grade variable is internal; this is not yet the desired
affine meridian q-difference source equation.

## 4. The entire normalized denominator is Alexander

The classical matrices (2.5) have a common right and left fixed vector

    v(k)=(1,k^(-1),...,k^(1-b))^t.

Conjugating by diag(1,k,...,k^(b-1)) gives the usual Hurwitz/Fox
blocks [[1-k^(-2),k^(-2)],[1,0]] and their inverses. The deleted
minor of I-L_beta thus presents the ordinary Alexander module,
by the infinite-cyclic-cover argument in the
[closed-braid note](closed_braid_period_line.md). It is an Alexander
polynomial up to a Laurent unit. The exact unit is fixed here.
Put D_beta(k)=D_beta(k;1). Then

    Delta_K(k^2)=k^(-c)D_beta(k), c=b-1-w.          (4.1)

Here Delta_K is the symmetric normalization with Delta_K(1)=1.
The following direct checks fix all units in (4.1).

First, c is even for a knot. The sign change k->-k conjugates
every block by diag(1,-1,1,...), so k^(-c)D_beta is Laurent in
k^2. At k=1 the matrix L_beta is the one-cycle strand permutation;
its deleted I-L cofactor is one. At k=-1 it is diagonally
conjugate to the same permutation, with the same cofactor.

For reciprocity introduce the upper triangular matrix H(k) with
diagonal one and

    H_ij=(1-k^2)k^(i-j) for i<j.

Multiplication of a single 2-by-2 block proves

    L_i(k^(-1))^t H(k)L_i(k)=H(k).

It follows for every word. Over C(k), I-L_beta has rank b-1,
because its deleted cofactor is nonzero at k=1. Thus its adjugate
is D_beta(k)v(k)v(k)^t. Use

    H(k)v(k)=k^(-2(b-1))v(k^(-1)),
    v(k^(-1))^t H(k)=v(k)^t,
    det L_beta=(-1)^w k^(-2w).

The adjugate of I-L_beta^(-1), together with knot parity
w=b-1 modulo two, gives

    D_beta(k^(-1))=k^(-2c)D_beta(k).

Consequently the right side of (4.1) is reciprocal and takes
value one at k=1. These properties uniquely fix the usual
symmetric Alexander normalization.

The same formula can be checked under braid moves without losing
units. Conjugation preserves D_beta, since the common left/right
vector v is fixed. A last-strand positive stabilization preserves
D_beta; a negative one multiplies it by k^2, by a last-coordinate
Schur complement. The corresponding c changes by zero and two.
Thus (4.1) is unchanged in both cases.

## 5. Exact comparison with the prescribed ADO state

At the root the ordinary pivot K and the actual ADO pivot satisfy

    g_ADO=K^(1-N)=k^(-1)K.

The residual actual twist is x^(1-N)=x/k. For b strands and
writhe w these give exactly

    P_(N,beta)(x;1)=k^c F_N(M), M=-q_N x.         (5.1)

Combining (3.2), (4.1) and (5.1) proves the root-period identity

    V_beta(q_N,x;1)=F_N(M)/Delta_K(M^(2N)).        (5.2)

The evaluation at tau=1 means the rational continuation (3.2).
It is defined over C(x); particular Alexander roots may be poles.
This is a direct all-knot, all-level comparison. The exponent c,
the sign of q_N^N and the full function Delta_K are accounted for.
At M=1, k=(-1)^(N-1), c is even, and Delta_K(1)=1. Therefore

    V_beta(q_N,q_N^(N-1);1)=F_N(1)=<K>_N          (5.3)

as a regular whole germ, including even levels. No asymptotic
normalization is involved. Although the graded series (1.3) is
diagram dependent, its rational root specialization (5.2) is a
knot invariant with the prescribed meridian and framing.

For the full ADO normalization multiply both sides by the entire
known function

    d_N(M)=i^(N+3)M^(N-1)/(1+M^2+...+M^(2N-2)).

The factor Delta_K(M^(2N)) does not replace this function. Both
divisors and their whole specializations are retained.

## 6. The same actual quantum A-ideal and pointed fiber

Let sigma(M)=q_N M. Since U=M^(2N) is fixed by sigma,
Delta_K(U) is a central scalar for the root meridian difference
action. Multiplication by this nonzero rational function therefore
gives, for every specified meridian operator P,

    P F_N=0 iff P(F_N/Delta_K(U))=0.               (6.1)

Thus the two root families have exactly the same all-level
annihilator ideal as defined for the actual ADO state. The
assertion holds in the reduced normalization and, with d_N
retained, in the full one. It does not assert equality with a
colored-Jones recursion ideal or a classical A-curve.

There is also exact compatibility with the marked ramified fiber.
Reciprocity makes Delta_K(U) even in z=(U-1)/(U+1), and its
constant term is one. Hence 1/Delta_K(U)=1+O(z^2). Multiplying
by it leaves both coordinates (a_0,b_0) of the
[ramified Weyl fiber](ramified_weyl_fibre.md) unchanged. In
particular it preserves the normal Kashaev functional, not merely
an unpointed root solution line. Away from U=1 its entire factor
still matters.

This supplies an explicit untruncated root-period realization of
the same quantum-A problem. The existence of the formal series
(1.3) and its root rational continuation does not yet identify
a generic completion, a geometric classical factor of the
minimal operator, or the regulator norm.

## 7. The reducible anchor is actual polar data

On a local meridian cover choose U=M^(2N) near an Alexander root
alpha and a branch M(U) through M_*. Equation (5.2) is an exact
meromorphic period identity. If alpha is a simple root,

    Res_(U=alpha) V_beta dU
                    =F_N(M_*)/Delta_K'(alpha).    (7.1)

The [upper triangular comparison](closed_braid_period_line.md)
independently computes F_N(M_*) as the selected cut period of
the exact nonabelian reducible family. Thus (7.1) matches that
period with a specified residue of the untruncated trace. For
a multiple root the same whole ratio gives all principal-part
coefficients from the corresponding meridian jets. If the
numerator vanishes the pole order can decrease; no nonvanishing
claim is assumed.

The Alexander divisor is therefore not only a classical necessary
attachment locus: it is the actual pole divisor of this global
root trace, with selected polar data fixed by the ADO state.
An occurrence can cancel when the numerator vanishes. This
construction retains such cancellations and does not evaluate
the numerator and denominator separately at the divisor.

## 8. What this adds to the triangulation comparison

The local relative factorial source and the classical Alexander
deformation matrix now have a common global trace interpretation.
Untruncated Verma crossings give the explicit period (1.3); the
Frobenius polynomial blocks produce its full Alexander denominator,
and (5.2) identifies its selected root value with the prescribed
quantum-A period. This supplies actual global period data rather
than choosing a scalar on a torsor to impose the desired answer.

The remaining geometric theorem must transport this selected
relative period to the ideal-triangulation gluing realization,
including its poles, source and boundary pointing, and establish
its marked Bloch-regulator norm. The geometric fundamental class
and its classical action are already identified in the linked
[triangulation bridge](triangulation_regulator_bridge.md).
Neither the algebraic polynomial trace (3.1) nor cancellation
of the Alexander factor at U=1 controls that quantum norm.
The target remains

    (4/N)log|F_N(1)| -> log||P_hyp||=2Vol(M)/pi.

No such estimate, noncancellation theorem or selected-period
identification with the Bloch regulator is proved here.

The subsequent [pointed tetrahedral transport](verma_tetrahedral_transport.md)
does establish a local part of the transport: exact four-factor
Verma crossings, a scalar-one formal tetrahedral pentagon, and
preservation of the rational root period under finite formal
operator rewrites with the same external pointing. Complete
compression to the original lattice is performed before root
specialization. Individual compact products can be singular;
their norm characters and poles remain in the relative data.
Application to an arbitrary positive geometric triangulation and
the regulator norm are additional work.

## 9. Coverage and independent verification

[Willetts, 2003.09854v2, Introduction Result 2](https://arxiv.org/html/2003.09854v2)
already states a completed invariant with root evaluation ADO divided
by Delta_K(A^(2r)). That is the prior coverage of the normalization
in (5.2). Its completion, comparison and recursion proofs are not
premises here. We prove the root trace formula by the displayed
Gaussian cancellation, residue filtration, symmetric-power trace
and explicitly normalized Fox cofactor. Equality of the generic
graded auxiliary series with Willetts's completed element is not
claimed. The literature ADO definition remains the fixed state.

[The audit](../experiments/audit_frobenius_verma_period.py) compares
the full untruncated coefficients with the block factorization,
tests both signs and full homogeneous-sector inverse matrices,
and checks the finite crossing against the actual ADO matrices.
Independent symbolic checks verify the Fox minor, duality,
reciprocity, conjugation and stabilization units. Full graded
Verma traces are computed by unbounded-index sparse propagation
to a stated degree and compared with the rational formula using
independently constructed finite ADO matrices. Polar samples are
retained. See [the results](../experiments/frobenius_verma_period_results.json).
These checks support the uniform proof and establish no volume
asymptotic.

The saved audit includes 26,454 local block coefficient comparisons
at nine levels through 12, both full homogeneous-sector inverse
crossings and exact finite ADO restrictions, 16 symbolic Alexander/
duality normalization cases, and 506 graded coefficients in 34
complete trace cases on two, three and four strands. The cases
include even/composite levels, both signs, exact Kashaev points,
and a polar Alexander sample with nonzero finite numerator.
