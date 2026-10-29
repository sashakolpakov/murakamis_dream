# A nonzero all-level annihilator from the actual finite cut state

Research note, 26 October 2026. This gives an independent existence
proof of a nonzero all-level meridian annihilator for the reduced
literature ADO state of every knot. The proof keeps the finite-sum
boundaries, handles an elimination operator vanishing under summation,
and removes a central factor before root specialization. It does not
identify the operator's classical symbol with the geometric A-curve
or prove a volume estimate.

Existence of level-independent ADO recursions is existing coverage:
[Brown--Dimofte--Garoufalidis--Geer, 2005.08176](https://arxiv.org/abs/2005.08176).
Proper q-hypergeometric sums and q-holonomicity are standard, with
scope surveyed in [Garoufalidis--Le, 1601.07487](https://arxiv.org/abs/1601.07487).
Their closure, Hamiltonian-reduction, and holonomicity proofs are not
premises here. The proof below is a filtered dimension count with
explicit boundary strata and finite exponential moments.

## 1. An auxiliary off-root lift, with the root state unchanged

Choose a braid presentation of a zero-framed knot. At a fixed
positive integer N, keep q generic and use the N by N matrices

    E v_a=[a]_q*(x*q^(1-a)-x^(-1)*q^(a-1))/(q-q^(-1)) v_(a-1),
    F v_a=v_(a+1), K v_a=x*q^(-2a)v_a, 0<=a<N,

with the endpoint vectors zero. These need not be a quantum-group
representation away from the root. Only their finite matrix entries
will be used off-root.

On a crossing put D_(a,b)=x^(-a-b)q^(2ab), and

    Theta=sum_(k=0)^(N-1) c_k (E tensor F)^k,
    c_k=q^(k(k-1)/2)*(q-q^(-1))^k/[k]_q!,
    R_tilde=D*Theta.                                 (1.1)

This is the actual unrolled R with its common q^(alpha^2/2)
factor removed, x=q^alpha. The inverse is

    R_tilde^(-1)=Theta_inv*D^(-1),
    Theta_inv=sum_(k=0)^(N-1)
       (-1)^k*q^(-k(k-1)/2)*(q-q^(-1))^k/[k]_q!
                                      *(E tensor F)^k. (1.2)

For a proof, set Q=q^2 and rewrite the two coefficient series as
the q-exponential and its inverse. Their coefficient convolution
is the finite q-binomial identity

    product_(j=0)^(m-1)(1+Q^j*t)
      =sum_(r=0)^m Q^(r(r-1)/2) {m choose r}_Q t^r.

Inserting the last factor and collecting coefficients proves this
identity inductively. At t=-1 its right side is zero for m>0,
which is exactly the inverse-series convolution after the factorial
rewrite. Finally (E tensor F)^N=0 truncates it. Thus (1.2) holds
for generic q, without a root-of-unity relation.

Use the checked crossings obtained by permutation, pivotal K^(1-N),
and the residual framing factor x^(w(N-1)), with w the braid writhe.
Take the (0,0) entry of the cut partial trace and call it L_N(q,x).
No scalarity or topological invariance is asserted for this off-root
lift. At q_N=exp(pi*i/N), it is exactly the actual reduced period

    L_N(q_N,x)=F_N(x).                              (1.3)

The cancellation of the removed factors against the twist, and the
root normalization, are those already independently checked in
[the ADO pointing note](kashaev_ado_pointing.md). All denominators
[k]_q!, k<N, and q-q^(-1), are nonzero at q_N. Consequently L_N
is regular there as a rational function of generic x.

## 2. The precise finite-sum class

The lift is a finite sum over crossing powers and strand labels.
All matching constraints are integral linear equations. Their
integer solution lattice has a fixed integral basis; use its
coordinates k=(k_1,...,k_s). All actual labels and crossing powers
are fixed integral linear functions of k. Their bounds 0,...,N-1
define a finite support P_N by finitely many inequalities

    ell_nu(N,k)>=0.                                (2.1)

Every nonzero summand on this support is a product of:

* a monomial q^Q(N,k) x^L(N,k), with Q integer-valued quadratic
  and L integral linear;
* finitely many q-factorials (q^v;q^v)_ell(N,k) and their inverses,
  with nonnegative integral linear lengths;
* finitely many (x^u*q^ell(N,k);q^v)_m(N,k) and their inverses,
  with u!=0 and nonnegative integral linear lengths;
* finitely many fixed nonzero Q(q)-scalars raised to integral
  linear exponents, including signs.

Here v!=0 is fixed. Include all factorial and Pochhammer length
conditions among (2.1). A term is defined as zero outside P_N.
Its value is nonzero as a rational function of generic (q,x) on
P_N. This is the only regularity of a summand used below.

The x-dependent Pochhammer parameters also satisfy the proper
alignment condition: v divides each coefficient of k_i in ell.
This ensures that an internal unit shift moves an argument by
an integral number of its q^v steps. For the actual R-weights
both v and those coefficients are even, with v=+/-2. The proof
does not assert this shift bound for unaligned Pochhammer products.

To check this class for (1.1), use

    E^k v_a=([a]_q!/[a-k]_q!)
          *product_(r=0)^(k-1)[alpha-a+r+1]_q v_(a-k).

The second product is an x-dependent Pochhammer of length k.
Explicitly, writing rho=q-q^(-1), it is

    (-x^(-1))^k q^(k(a-1)-k(k-1)/2) rho^(-k)
                         *(x^2*q^(2-2a);q^2)_k.

Also [r]_q!=q^(-r(r-1)/2)*(q^2;q^2)_r/(1-q^2)^r.
These formulas verify both the alignment and the allowed linear
exponents of scalar factors, with no appeal to a closure theorem.
The other coefficients in (1.1)--(1.2) are q-factorials and
quadratic q-monomials. Pivotal and framing entries contribute
x-powers linear in (N,k) and q-powers quadratic in (N,k).
Thus their shift ratios belong to the class just described.

Choose a fixed positive integer B so that shifting x by q^B
shifts every x-dependent Pochhammer argument by an integral
number of its q^v steps. B=1 works for these R-weights: u=+/-2,
v=+/-2. Write T for this x-shift and S_i for k_i -> k_i+1.
Set z=q^N and t_i=q^k_i. The variable z will be retained until
the last specialization.

## 3. A global shift-span bound, including the boundaries

Let I_N(q,x;k) be one summand, extended by zero. For R>=1 consider
the actions

    x^a z^c T^b S_1^beta_1...S_s^beta_s I,
    0<=a,c,b,beta_i<=R.                             (3.1)

These are functions of (N,k,x), over the coefficient field Q(q).
Their joint span has dimension O(R^(s+2)). The constant depends
on the fixed summand data and support, not N or R.

### Interior rational-shift estimate

Where a collection of shifted terms is supported, choose one
supported shift beta_0 as reference. Ratios of the shifted products
to I(k+beta_0) are rational in x,z,t_1,...,t_s. They have a common
Laurent-polynomial denominator of degree O(R), and after clearing
it all exponents are bounded in absolute value by C R.

Indeed a shift changes every factorial length and Pochhammer
endpoint by O(R). All possible endpoint factors belong to finitely
many types 1-q^r x^u z^v t^a, with r in intervals of length O(R).
Include their required denominator factors once, with the bounded
multiplicities of the original products. Quadratic q-monomials
change by linear functions of (N,k), hence by Laurent monomials
of degree O(R) in z,t; x-shifts of x^L contribute the same kind
of monomial. Powers q^O(R^2), and the shifted scalar factors,
are scalars in Q(q).

Without boundaries this proves the O(R^(s+2)) estimate immediately.
Ignoring the zero extension at a boundary would be incorrect.

### Boundary stratification and its codimension

Choose C so |ell_nu(0,beta)-ell_nu(0,0)|<=C R for all shifts
in (3.1). Partition the integer pairs (N,k) by declaring each
support form either greater than C R, less than -C R, or equal
to one particular integer in [-C R,C R]. A stratum with a form
less than -C R contributes zero to every shifted term.

On any remaining stratum the supported shifts are a fixed subset:
large forms remain positive, while near-boundary forms have fixed
integer values. An empty subset contributes zero. Otherwise choose
beta_0 from that subset. All q-factorial
ratios between it and another supported shift have nonnegative
endpoint indices. Their intervening factorial factors have strictly
positive indices. A common denominator can therefore be chosen
nonzero on the stratum. The x-dependent factors are nonzero for
generic x. Thus the interior estimate still applies there.

Suppose the fixed near-boundary forms have rank r as affine
constraints on (N,k). Their consistent integer labels have only
O(R^r) possibilities: choose r independent forms, after which
all dependent labels are determined. There are finitely many
choices of forms and large/small patterns.

On each such stratum, the multiplicative variables z,t satisfy
r independent binomial constraints

    z^b product_i t_i^a_i=q^d.                      (3.2)

The Laurent monomials of degree O(R) in x,z,t modulo these
constraints span a space of dimension O(R^(s+2-r)). To see this
integrally, use Smith normal form of the fixed constraint lattice.
The r constrained exponents can be reduced modulo fixed integers;
the other s+2-r exponents range through O(R) integers. This also
keeps the finitely many components if the lattice is not saturated.
The varying right sides q^d are coefficient-field scalars.

Restrict the family (3.1) to all these strata. A function is
determined by its restrictions, and multiplication by the nonzero
reference summand or common denominator does not increase dimension.
Consequently its dimension is at most

    sum_(r=0)^(s+1) O(R^r)*O(R^(s+2-r))
        =O(R^(s+2)).                               (3.3)

This proves the global bound. It also treats small N, intersecting
boundary faces, and redundant support inequalities. In particular
it does not assume that the index polytope is a box.

The same estimate holds for a finite sum on the same lattice by applying
it to the direct sum of their spaces. One can retain separate term
components in the elimination below, so cancellation between terms
is not an assumption.

## 4. Elimination without internal multiplication variables

The PBW monomials of the operators in (3.1) are linearly independent
in the formal Ore algebra. There are (R+1)^(s+3) of them. For large
R this exceeds the bound (3.3). Finite linear algebra yields a
nonzero formal operator

    P(x,z,T,S_1,...,S_s) I=0                        (4.1)

with coefficients in Q(q), and no multiplication t_i in P.
Identity (4.1) is global on the zero-extended integer array,
not merely an equality of ratios at interior indices.

The construction is effective in principle. List the boundary
strata, clear the proper denominators, reduce their monomials
by the binomial constraints, and solve the resulting finite
linear system over Q(q). No efficiency or minimal-order claim
is made.

## 5. Finite moments repair vanishing under summation

For each N introduce independent formal units w_i and the finite
Laurent polynomial

    F_N(q,x,w)=sum_(k in Z^s) w^k I_N(q,x;k).

Since the support is finite, translation of the sum is exact:

    sum_k w^k S_i I(k)=w_i^(-1) F_N(q,x,w).

Thus (4.1) becomes

    P(x,q^N,T,w_1^(-1),...,w_s^(-1)) F_N(q,x,w)=0.  (5.1)

Expand the nonzero polynomial P in its commuting internal shifts
around S_i=1:

    P=sum_alpha A_alpha(x,z,T)(S-1)^alpha.

Choose a nonzero A_alpha at least total degree h. Set w_i=exp(v_i)
in (5.1). Its coefficient of v^alpha at that least degree is

    (-1)^h A_alpha(x,q^N,T) F_N(q,x,1)=0.            (5.2)

Every term in which a positive-degree moment of F_N occurs has
a lower-degree coefficient of P, and therefore vanishes. Hence
A_alpha is a genuine nonzero meridian operator for the summed
state, even if P(x,z,T,1,...,1)=0. This is a formal finite-moment
argument, with no convergence, contour shift, or boundary omission.

## 6. Specializing q^N=-1 without losing the operator

Apply (5.2) to the actual off-root lift L_N. Clear denominators
and write its nonzero operator as

    A(x,z,T)=(z+1)^h A_0(x,z,T),

where at least one coefficient of A_0 has nonzero value at z=-1.
The factor is central. For every fixed positive N, q^N+1 is a
nonzero rational function of generic q, so the identity for L_N
also implies

    A_0(x,q^N,T)L_N(q,x)=0

before specialization. At q=q_N the lift is regular, as proved
in Section 1. Therefore

    P_K(q,x,T)=A_0(x,-1,T),
    P_K(q_N,x,T)F_N(x)=0                            (6.1)

for all but finitely many N. The excluded levels are poles of
the fixed rational q-coefficients. P_K is nonzero by construction.

This cancels a common operator factor before specialization of
an auxiliary lift. It changes neither the state nor any peripheral
factor in a state comparison. In particular the actual full ADO
factor d_N is still the whole rational germ of the pointing note.

At the trivial quotient color the actual reduced state has value
one. Thus an order-zero multiplication operator cannot annihilate
it at all large levels. After removing a common shift, (6.1) has
positive order and nonzero leading and trailing coefficients in
Q(q,x). Its existence proves that the actual localized all-level
annihilator ideal is nonzero for every knot.

The exact change x=-q^(-1)M and the fixed full/reduced shift gauge
transport this operator to the meridian M and to the full literature
ADO normalization. In the localized skew polynomial ring over
Q(q,M), left Euclidean division gives the unique monic element
of least order in the actual nonzero ideal. This is the literature
minimal-operator convention; the construction above need not
compute that minimal element efficiently.

## 7. What this settles and what the triangulation must still supply

The [all-level exact period theorem](all_level_a_period.md) can
now be applied to a nonzero actual annihilator for every knot,
with its finite fixed-color pointing and bounded q-jets. Existence
of such an operator is no longer an unaudited premise in that
application. No proof of an equality with a Jones recursion ideal
is needed for this implication.

This proof does not show that the minimal operator has the geometric
A-component in its classical symbol, that it has a rational
inhomogeneous source factor, or that its period has the geometric
regulator norm. A positive ideal triangulation supplies the geometric
Bloch class and gluing branch. The exact comparison between its
quantum gluing period and the actual cut-state module remains
necessary, as detailed in [the triangulation bridge](triangulation_regulator_bridge.md).

The subsequent [relative octahedral presentation](relative_octahedral_period.md)
now rewrites these very cut-state coefficients into five tetrahedral
atoms, proves their local ideal-octahedron geometry, and derives
the finite factorial's source and exact cyclic boundary transition.
This gives explicit local input for the remaining comparison;
it does not identify this eliminated meridian operator's global
geometric block or its selected regulator period.

The [diagnostics](../experiments/audit_finite_sum_annihilator.py)
check the generic off-root crossing lift and its inverse against
the actual root matrices, explicit global boundary certificates,
and the finite-moment and central-specialization repairs. Their
[results](../experiments/finite_sum_annihilator_results.json) are
checks of these ingredients, not a volume theorem or an efficient
all-knot computation of minimal operators.
