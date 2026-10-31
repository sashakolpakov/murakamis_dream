# Complete six-port confluence in blocks of at most eight channels

29 October 2026. The saturated original six-port source decomposes by
regular joint idempotents of the three disjoint pair Casimirs. Each
block has rank at most eight. Relative to primitive generic eigenline
columns, its Smith exponents are between0 and3. Thus only three normal
saturation steps are needed. An explicit physical-projector construction
of those columns requires Taylor order at most TEN, independently of N.

This avoids arbitrary maximal-minor denominators. It is a valuation and
finite-jet theorem, NOT an estimate on a frame's Hermitian condition
number. All actual Casimir derivatives, original turns and marked rows
are retained. Disjoint pairs alone do not give bounded-size blocks at
eight or more heads; section7 states the precise limitation.

## 1. The actual lattice and the three commuting pair operators

Fix N>=2, d=N-1, q=exp(pi i/N), and t=zeta-q. Work over

    O=C{t}, K=Frac O,
    M=V_d(zeta)^tensor6,
    Lambda=Inv_K(M tensor K) intersect M.                 (1)

All modules and matrices use the regular balanced generic original
color. The [deformable source theorem](actual_six_port_deformable_source_and_recoupling.md)
proves saturation, injective root specialization and

    rank Lambda=(N^3+N)/2.

The [normal Ward theorem](actual_six_port_divided_power_source_kernel.md)
also identifies its root image with the explicit divided-current
kernel. Neither statement semisimplifies the original root color.

Let A_1,A_2,A_3 be the actual pair Casimirs on physical pairs12,34,56.
They commute and have the generic polynomial

    P(z;zeta)=product_(a=0)^d(z-c_a(zeta)),
    c_a(zeta)=zeta^(2a+1)+zeta^(-2a-1).                  (2)

The original generic highest-vector calculation proves P(A_i)=0;
at the root it is the complete polynomial T_N(z)+2, including its
double nodes. Their coefficients and all A_i are regular over O.

## 2. Regular cluster idempotents split the SATURATED source

Partition indices a by their root value c_a(q). Each cluster is

    C={a,d-a},

with a singleton when N is odd and a=d/2. Put
g_C(z)=product_(a in C)(z-c_a(zeta)). Distinct g_C have resultant a
UNIT of O: their roots have distinct values at t=0. The elementary
Chinese-remainder/Bezout construction therefore gives polynomials
e_C(z) with coefficients in O such that, modulo P,

    e_C=1 mod g_C, e_C=0 mod g_D (D!=C),
    sum_C e_C=1, e_C e_D=delta_(CD)e_C.                  (3)

One may construct e_C=H_C B_C, where H_C=P/g_C and B_C is its inverse
modulo g_C. Only a scalar/unit resultant is inverted; no vanishing
eigenvalue gap within C is divided at this step.

Each e_C(A_i) preserves M and the generic invariant space, hence Lambda.
The triple products

    E_C=e_(C1)(A_1)e_(C2)(A_2)e_(C3)(A_3)               (4)

are regular orthogonal ALGEBRAIC idempotents summing to identity. Thus

    Lambda=direct_sum_C Lambda_C, Lambda_C=E_C Lambda.    (5)

This is an actual decomposition of the free saturated lattice and
therefore also of its root source. It is not just a list of generic
eigenvalues that might miss the normal directions at specialization.

Over K the ordinary triangular channels are triples(a,b,c) satisfying
|a-b|<=c<=a+b. Each contributes ONE invariant line. Consequently

    rank Lambda_C=#admissible triples in C1 x C2 x C3<=8. (6)

The bound applies on the invariant lattice. The corresponding physical
joint pair eigenspace before imposing invariance is much larger.
Admissible subsets of a cube need not be the whole cube, and Lambda_C
need not be a free rank-one module over three dual-number variables.

## 3. Three is a uniform saturation bound

For a double cluster C={a,a*}, a*=d-a, the individual generic branch
projector is

    p_a(A)=e_C(A)(A-c_(a*))/[c_a-c_(a*)].                 (7)

For a singleton it is e_C(A). The denominator in(7) has a SIMPLE zero:

    D_log(zeta)(c_a-c_(a*))(q)
       =2N[q^(2a+1)-q^(-2a-1)] !=0.                    (8)

The excluded zero in(8) is precisely the singleton case. Thus p_a has
pole order at most one. A triple branch projector

    p_alpha=p_a(A_1)p_b(A_2)p_c(A_3)                     (9)

has pole order at most THREE as an endomorphism of the physical lattice.
It preserves the generic invariant space; on Lambda tensor K an
admissible branch has rank one, and an inadmissible branch is zero.

Let L_alpha=Lambda intersect that generic invariant line, and choose
a primitive column v_alpha generating this rank-one lattice. In a
cluster put L0=direct_sum_alpha L_alpha. For v in Lambda_C,

    t^3 p_alpha v belongs to L_alpha,
    v=sum_alpha p_alpha v.

Therefore the EXACT lattice inclusions are

    t^3 Lambda_C subset L0 subset Lambda_C.              (10)

All elementary divisors of L0 in Lambda_C are consequently t^s with
0<=s<=3. This bound is independent of the size of the ambient physical
tensor and does not follow merely from a determinant valuation.

There is a constructive saturation algorithm. For any current basis
matrix B(t), use only a constant invertible column change to separate
independent residue columns from combinations that vanish modulo t.
Divide the latter columns by t. This replaces its lattice L by

    t^(-1)L intersect M.

Indeed the residue relation kernel forces exactly those coefficients
to cancel at order zero. After at most THREE repetitions it equals
Lambda_C by(10). No block contains more than eight columns. Their root
values require only Taylor coefficients through order3 of the chosen
primitive v_alpha. In particular all confluence is retained when only
some of the eight generic branches are admissible.

## 4. An explicit primitive column construction: no unspecified minor

The preceding statement used primitive generic invariant columns. They
can be constructed directly from known physical projectors with a
uniform derivative bound, without choosing an arbitrary nonzero minor
of a large Clebsch matrix.

Let Omega_tot be the actual SIX-head total Casimir. Generically its
irreducible highest weights are 2a, 0<=a<=3d, with eigenvalues c_a(zeta).
The polynomial

    I_inv=product_(a=1)^(3d)
                   (Omega_tot-c_a)/(c_0-c_a)             (11)

is precisely the projector onto the spin-zero isotypic component,
namely the generic invariant space. Nonzero generic eigenvalues are
distinct Laurent functions, even when they collide at the selected root.
There is no extra highest-weight component in its generic IMAGE;
every positive highest-weight component is killed.

Its pole order is at most FOUR. To see the exact count, use

    c_0-c_a=-zeta Q^(-a-1)(1-Q^a)(1-Q^(a+1)).            (12)

Apart from a unit monomial, its denominator is

    F_(3d) F_(3d+1)/(1-Q), F_m=(Q;Q)_m.                 (13)

For N>=3 the four root-zero factors are a=N-1,N,2N-1,2N. For N=2
there are three. Each is simple. For the denominator gap c_0-c_a,
its logarithmic derivative at a=kN is -2kN(q-q^-1); at a=kN-1 it is
+2kN(q-q^-1). Thus (11) is
not being assigned a four-pole bound merely from a root count with
unverified multiplicities. Formula(13) is an explicit fixed-factorial
normalizer, not an unknown condition number.

For each admissible alpha form

    T_alpha=I_inv p_alpha.                               (14)

All factors commute: a pair Casimir is a Hopf intertwiner and commutes
with the total generators. Generically T_alpha is an idempotent of
rank ONE onto the actual invariant line. Its pole order is at most
4+3=7, so Q_alpha=t^7 T_alpha is regular. Since

    Tr Q_alpha=t^7,

the smallest entry valuation nu_alpha is between0 and7. Choose a
physical column u_j in which that smallest valuation occurs and set

    v_alpha=t^(-nu_alpha) Q_alpha u_j.                  (15)

This is a regular primitive invariant column. A component is a unit,
so every regular vector in its generic line is an O multiple of it.
It therefore generates the FULL L_alpha used in(10), not a sublattice
with an unmeasured extra zero.

To know its Taylor coefficients through order3, it suffices to know
Q_alpha through order nu_alpha+3<=TEN. Together with the three-step
algorithm this constructs complete saturated root frames with a
uniform derivative order, even when a naive generic Clebsch column
vanishes or diverges at the root. Replacing t by the source coordinate
zeta=q exp(h/N) changes it by a unit with leading factor q/N; it does
not change these derivative-order bounds. Its explicit fixed powers
of N are polynomial.

The seed construction may be computationally large. It is an exact
all-N construction and pole bound, not a claim of a fast algorithm.
Its norm may still be exponential. This distinction is essential.

## 5. Recoupling on the root by only fixed-size inverses

Repeat the construction for the other pairing/tree. Let B_beta be its
root frame in the beta-cluster, with at most eight independent columns,
and E_beta its regular joint cluster projector. On the actual source,
the coefficients of an input frame column v in that output cluster are

    (B_beta^dagger B_beta)^(-1) B_beta^dagger E_beta v.     (16)

The Gram in(16) is positive definite because those columns are
independent. One can use the literal physical tensor metric, or first
apply the fixed original W_2 extraction and use its specified physical
metric. All original source/cap normalizations are then transported
literally. Formula(16) is exact coordinate extraction; no orthogonality
of distinct algebraic cluster projectors is assumed.

The only inverses in(16) have order at most8. This replaces a large
arbitrary maximal-minor inverse with regular spectral separation,
bounded normal saturation, and explicit small-block Gram inverses.
There is NO uniform lower bound for those Gram eigenvalues asserted.
Thus (16) does not turn bounded jet order into polynomial recoupling
norm or into a sharp geometric energy estimate.

For an original regular physical tangle operator G, use E_beta G v
in(16). Its actual root matrix already contains the complete Casimir
Hermite derivatives. Constructing both complete root frames by(15)
and the three-step saturation does not require discarding a derivative
row or a marked source term.

## 6. What this settles for the six-port analytic problem

The following pieces are now PROVED: regular joint decomposition of
the saturated source, rank<=8 per collision block, Smith exponents<=3,
an explicit derivative-order<=10 seed construction, and source-exact
recoupling with only fixed-size block inverses. No arbitrary generic
Clebsch maximal-minor denominator remains as an unmeasured q-pole.

To estimate an actual fixed-factor factorial/Clebsch sum, bounded
normal jets can be compared with its original factorial envelope.
The independently checked
[uniform normal-factorial bound](bounded_normal_quantum_factorial_envelope.md)
proves this when each entry is an explicit fixed-factor factorial sum,
including indices exceeding N with their root zeros removed. It does
not apply automatically to an unestimated small-block Gram inverse.
But the norm of a saturated frame, the inverse Gram in(16), and the
coherent source/cap contraction still require their own quantitative
estimate. The present theorem supplies neither a positive geometric
measure nor the missing non-tree source packet by itself.
The germ variable here is the normal q deformation. It is not an
automatic holomorphic continuation of the physical auxiliary colors
on a fixed complex corridor, which remains a separate analytic input.

## 7. The precise fixed-width limitation

The rank<=8 statement uses the fact that THREE ordinary pair channels
have invariant multiplicity at most one. It is FALSE for disjoint
pairs alone at eight or more physical heads. For example, fix all four
pair spins to a=d in eight heads. The invariant space of W_d^tensor4
has generic dimension2d+1, since the intermediate W_j occurs once
for every j=0,...,2d. A single joint four-pair collision block therefore
already contains at least2N-1 independent generic invariants.

At a larger fixed width one must refine the commuting family by a
COMPLETE laminar fusion tree, not just disjoint pair Casimirs. Its
generic branches again have multiplicity one. Each internal highest
weight is at most a fixed multiple of N; its root collision class
has bounded size depending only on that width. A gap between two
different branches has order at most2: order1 except at a root
Casimir value+/-2, where the distinct positive exponents have
different squares and split at order2. Products of the finitely
many branch projectors therefore have a pole bound depending only
on the fixed tree. The argument(10)--(15) then gives a fixed-width
finite-jet bound too, with larger constants. It does NOT give
bounded-size blocks for an incompletely resolving family.

The six-port bounds3,7,10 above are explicit and require no such
additional tree. No high-width norm or volume bound follows from
this fixed-jet observation.

## 8. Exact checks and analytical scope

[The focused exact audit](../experiments/audit_actual_six_port_bounded_confluent_blocks.py)
passes nineteen physical spectral-gap families N=2,...,20 using
cyclotomic polynomial divisibility, not numerical root proximity. It
checks the actual total-projector zero indices and every simple pair
gap. It also tests all nine admissibility patterns appearing there in
the tensor-Jordan lattice model; their Smith exponents are<=3. The
full eight-branch example has exponents0,1,1,1,2,2,2,3, so the algebraic
pole argument cannot in general promise fewer than three saturation
steps. These lattice stress tests are explicitly NOT a bound or an
identification of an unknown physical Gram matrix.

Section 4 uses the corrected signs in the derivative of c_0-c_a. The nonzero multiplicities and bounds are unchanged.