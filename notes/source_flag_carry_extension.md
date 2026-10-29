# The source flag extends through the full carry lattice

Research note, 26 October 2026. This extends the preceding
[source-flag construction](source_flag_transport.md) through its
marked normal chart at source infinity. The individual endpoint frames
can have fractional zeros or poles. In the complete tree evaluation,
conservation of the total residue converts all these exponents into
the integer carry. The same carry lattice, actual source sublattice
and dual linking form therefore work for finite source flags and at
the marked source infinity. Other root branches have an explicit
source-line twist, with uniformly bounded order; its reciprocal is
retained on the dual.

The result concerns the existing pointed recoupling presentation of
the actual cut state. It does not assign that full colored network to
an arbitrary geometric triangulation, identify a geometric quantum-A
factor, or prove the regulator norm. In particular the internal normal
parameter below is not assumed to be the marked meridian parameter.

## 1. The normal configuration and the specified source frames

Fix N>=2 and Q primitive of order N. Choose distinct normal flags

    delta_0,...,delta_b, b>=2.

Let R=k[[epsilon]], and temporarily adjoin u with u^N=epsilon.
For a finite source flag s avoiding the delta_i choose

    C_i(s)^N=delta_i-s,
    A_i=u C_i(s), p_i=p_*+epsilon delta_i,
    source point=p_*+epsilon s.                       (1.1)

Use the existing endpoint module on an oriented interval i<j,

    E_ij=k((u))[X]/(X^N-1),
    Y_ij=(A_i-A_j X)sigma_Q^(-1),
    Y_ij^N=epsilon(delta_i-delta_j).                   (1.2)

The normalized coordinate X here is the one used for the carry
presentation. The original color, Cartan factors and meridian M
remain in the actual crossing and cut operators. No unrecorded
replacement of the peripheral K-root by one is made.

Let H_(r,a)=Q^(ra), and put

    d_ij(n)=product_(h=1)^n (C_i-C_j Q^h),
    A_ij(u)=H^(-1)diag(u^n d_ij(n)).                  (1.3)

All d_ij(n), 0<=n<N, are nonzero: a zero would imply
C_i^N=C_j^N, contrary to distinct delta_i. The matrix (1.3)
is the existing endpoint factorial frame. It sends the standard
residue basis, with clock Q^n and F-wrap
epsilon(delta_i-delta_j), to the raw polynomial endpoint
module (1.2). Its scalar and zeroth column have been fixed.

For an ordered binary tree T on the b consecutive intervals,
let I_T^raw be the actual iterated pointed fusion. The basis of
its source is ordered as total polynomial exponent, then one
relative exponent for each internal node in preorder. Each
relative exponent ranges from zero to N-1.

The raw relative operator X_1+Y_1Y_2^(-1) is independent of u,
since its two Y factors contain the same u. Its iterates and
their pointed fusion columns are therefore independent of u.
Set

    Ical_T(u,s)=(tensor_leaves A_(j,j+1)(u))^(-1)
                  I_T^raw(s)(A_(0,b)(u) tensor I_rel). (1.4)

The total factor of (1.4) uses its standard source basis as
well. This total frame is essential to the cancellation below.

## 2. Fractional weights give exactly the integer carry

Write a leaf state as i=(i_1,...,i_b), and put

    r(i)=sum_j i_j mod N,
    kappa(i)=floor(sum_j i_j/N),
    J_epsilon=diag(epsilon^(-kappa(i))).              (2.1)

The total X-intertwining equation implies that, in evaluation
coordinates on the leaf factors and the total factor,
I_T^raw has support only where its input total residue is r(i).
Every leaf frame contributes u^(-i_j); the total frame contributes
u^r. Hence every nonzero entry of (1.4) has net factor

    u^(r-sum i_j)=u^(-N kappa(i))
                         =epsilon^(-kappa(i)).       (2.2)

Consequently exactly

    Ical_T(u,s)=J_epsilon M_T(s),
    M_T(s) in GL_(N^b)(k_s),                         (2.3)

where k_s contains the specified C_i(s) and Q. The matrix M_T
has no u or epsilon dependence. It is invertible because the
pointed fusion and all frames in (1.4) are invertible generically.

This proves the same full image lattice at every finite source:

    Ical_T R^(N^b)
       =C_carry=direct_sum_i epsilon^(-kappa(i)) R e_i.
                                                        (2.4)

It proves equality of lattices, not only equality of determinant
valuations. The statement holds for every tree and every N,
without parity division or a new determinant normalization.

A common change C_i -> zeta C_i with zeta^N=1 changes the
frame ratio by zeta^(r-sum i_j)=1. Thus its common-root
ambiguity cancels exactly. Other relative root choices remain
marked data.

## 3. An explicit full kernel, including the total source frame

For a node v, let its interval have endpoints a,z and split k,
so its right subinterval has endpoints k,z. At a leaf state i,
write r_I and r_R for the residues on those intervals. For its
relative exponent d_v define

    K_v(i,d_v)=(C_a/C_k)^d_v
          (Q(C_z/C_a)Q^r_I;Q)_(d_v)/
          (Q(C_z/C_k)Q^r_R;Q)_(d_v).                (3.1)

All denominators are nonzero on the stated source chart. The
complete matrix in (2.3) is

    M_T(s)_(i; r,{d_v})
       =delta_(r,r(i))
          d_(0,b)(r)/product_j d_(j-1,j)(i_j)
                    *product_v K_v(i,d_v).          (3.2)

The root factors in (3.1) and the total numerator in (3.2)
cannot be omitted.

For a direct proof, normalize a matched endpoint pair by
X_tilde=(C_k/C_a)X_1 and
x_tilde=(C_z/C_k)X_2. Applying the previously proved
pointed factorial kernel and undoing its relative basis
rescaling gives

    C_raw(U^a V^d)
      =w^a(C_a/C_k)^d
                    (Q(C_z/C_a)w;Q)_d/
                    (Q(C_z/C_k)z;Q)_d.              (3.3)

Iterating (3.3) gives the product in (3.1). Multiplication by
the inverse total evaluation matrix converts w^a into the
residue delta in (3.2). The factorial part of the total
frame and the inverse leaf frames supply the remaining ratio.

This also shows directly why replacing the total source by
a new polynomial unit would change the matrix and its period.

## 4. The marked source infinity is regular in these frames

Put t=1/s, and on the marked branch at infinity choose

    C_i(s)=h alpha_i(t),
    h^N=-1/t, alpha_i(t)^N=1-t delta_i,
    alpha_i(0)=1.                                   (4.1)

This is the coherent root branch selected by the normal source
in the earlier carry calculation. Other lifts at infinity are
not silently identified with this one; their cyclic cuts and
root transports remain part of the data.

The total/leaf factorial ratio contributes
h^(r-sum i_j)=(-t)^kappa(i).
The node root factors tend to one. The normalized consecutive
roots have expansions

    alpha_j/alpha_(j-1)
       =1-t(delta_j-delta_(j-1))/N+O(t^2).           (4.2)

The common-carry proof applies to these analytic roots as well
as to exactly linear roots. Here is the needed extension of
that proof: every factorial has the same zero threshold as
before, and its sole possible zero has first coefficient equal
to the corresponding consecutive sum. Those sums are
(delta_z-delta_a)/N and are nonzero. The row carry bound and
the determinant valuation are therefore unchanged. The
row-scaled matrix is integral with unit determinant.

Let L_T(t) denote that normalized evaluation kernel, still
with polynomial total input. Thus

    L_T(t)=diag(t^(-kappa)) U_T(t), U_T in GL(k[[t]]).

Inserting the remaining unit endpoint factors into (3.2)
proves

    M_T(s) extends to GL_(N^b)(k[[t]]) at t=0.         (4.3)

There is a useful exact expression for its value. Let
D(n)=(Q;Q)_n and let U_T(0) be the row-scaled leading matrix
of the preceding carry theorem with directions

    a_j=(delta_j-delta_(j-1))/N.

Then

    M_T(infinity)
      =diag_i[(-1)^kappa(i) D(r(i))/product_j D(i_j)]
                  U_T(0)(H^(-1) tensor I_rel).       (4.4)

Every displayed factor is a unit. In particular the sign
(-1)^kappa is required. It records h^N=-1/t; it is not an
arbitrary phase correction.

Equations (2.3)--(2.4) now hold at the marked infinity as well.
The proof never separately evaluates a vanishing edge frame
or a polar endpoint cap.

### Every relative-root branch has a computed source line

The other root cuts are accessible without setting their factors
to one. Write

    C_i=h Q^m_i alpha_i(t), 0<=m_i<N,
    a_j=(m_j-m_(j-1)) mod N in {0,...,N-1},
    a_total=(m_b-m_0) mod N,
    w=(sum_j a_j-a_total)/N in {0,...,b-1}.           (4.5)

Then the exact branch extension is

    M_T(t)=t^(-w) Mbar_T(t), Mbar_T in GL(k[[t]]).    (4.6)

This is a scalar line twist, not permission to drop its value.
Here is a uniform entry and determinant proof. Put

    z_j=floor((i_j+a_j)/N), i_tilde_j=i_j+a_j-N z_j,
    z_total=floor((r+a_total)/N).

The factorial prefactor in (3.2), including h^(r-sum i),
has t-order kappa+z_total-sum z_j. The effective normalized
leaf residues are i_tilde_j, with carry

    kappa_tilde=kappa+w-sum z_j+z_total.

The raw kernel has entry pole order at most kappa_tilde,
by the same threshold argument. Hence t^w M_T is integral.
For its determinant, an endpoint frame with root increment a
has t-order a-(N-1)/2. The raw tree fusion has order
-(b-1)(N-1)N^(b-1)/2. Their total/leaf ratio therefore gives

    ord_t det M_T=N^(b-1)(a_total-sum a_j)=-N^b w.

Thus det(t^w M_T) is a unit, proving (4.6). Every remaining
unit and root phase is still determined by (3.2).

Over the two-parameter local ring the basic source line for
this branch is t^w k[[t,epsilon]]. Its actual sublattice is

    t^w Mbar_T^(-1) diag(epsilon^kappa)L_leaf.        (4.7)

Using that line as part of the domain of Ical gives exactly
the same carry image. The dual line is t^(-w), so the paired
period and linking form retain their full cancellation.
The bound w<=b-1 is independent of N. The coherent branch
in (4.1) has w=0. Forgetting the source line at another
branch would create artificial source-infinity torsion.

Equivalently the source connection has

    M_T^(-1)dM_T=-w(dt/t)I+Mbar_T^(-1)dMbar_T.

Its polar residue at infinity is central and is exactly
the computed source line. The projectivized connection is
regular there; the dual has the reciprocal central residue.
This regularity concerns the auxiliary source coordinate,
not the still-unidentified geometric quantum-A norm.

## 5. The whole source, dual and linking form extend

For any two tree/source charts define

    F_((T',s'),(T,s))=M_(T')(s')^(-1)M_T(s).          (5.1)

On the chosen normalized forward edge, the product in the
preceding source-flag proof is h_n=d'_ij(n)/d_ij(n).
Hence its actual edge adapter is A'_ij A_ij^(-1).
The reverse adapter is forced by the actual cap. Equation
(5.1) is therefore precisely their induced tree comparison,
with the same scalar normalization, rather than a newly
chosen frame at infinity.

It is an integral isomorphism, extends to the marked source
infinity and satisfies the strict composition law. Its
lattice statement includes the actual source

    B_(T,s)=Ical_(T,s)^(-1)L_leaf
       =M_T(s)^(-1)diag(epsilon^kappa)L_leaf.         (5.2)

Indeed substitution gives F B_(T,s)=B_(T',s'). Its dual
is F^(-t), so it also transports the full actual dual source.
As in the previous relative-duality proof,

    Ical_dual=J_epsilon^(-1) M_T(s)^(-t),
    B_(T,s)^sharp=Ical_(T,s)^t L_leaf^sharp.          (5.3)

Thus the linking pairing of C_carry/L_leaf with
L_leaf^sharp/C_carry^sharp is unchanged, including the
lost Tor fiber and all retained normal coefficients.

At other root branches, (5.1) is an integral isomorphism of
the source lines in (4.7). Its coordinate matrix includes
the retained power t^(w'-w); it is not asserted to be an
untwisted unit matrix when those line orders differ.

This is also a flat two-parameter statement near source
infinity. Over k[[t,epsilon]] the quotient is explicitly

    direct_sum_(kappa(i)>0)
                      k[[t,epsilon]]/(epsilon^kappa(i)).     (5.4)

It is free of finite rank over k[[t]], with no additional
source-infinity torsion. Its normal thickness is at most
floor(b(N-1)/N)<=b-1, independent of N for fixed b. The
dual residue pairing is the same perfect coefficient pairing
[epsilon^(kappa-1)]fg, now with coefficients in k[[t]].

For a branch with nonzero w, the same statement holds with
its source line t^w and dual line t^(-w). Their quotient
is again the carry quotient in (5.4) after the specified
line identification, not after discarding the scalar.

The original cut row, pivot and duality tensors must move by
these complete maps. In particular a polar row on a basic
tree frame is a legitimate element of the full dual source;
it is not replaced by a regular coordinate vacuum. This is
how the endpoint pole times its missing normal coefficient
continues to give the actual nonzero cap.

## 6. The selected actual cut is unchanged through infinity

Use the specified crossing lift and actual color from
[the carry-period proof](carry_recoupling_lattice.md).
In the standard residue bases its leaf wraps may be taken as

    F_j v_(N-1)=epsilon Delta_j v_0,
    Delta_j=delta_(j-1)-delta_j.

The nilpotent E, actual Cartan factor, pivot, twist and cut
projector are the original ones. A crossing preserves the
integer residue degree or lowers it by N on a wrap. Thus
both L_leaf and C_carry are preserved. The retained carry
operator is

    Bcal_(T,s)=M_T(s)^(-1)
                    (J_epsilon^(-1) B_beta J_epsilon)M_T(s).
                                                        (6.1)

The cut insertion is transported by the same conjugation.
It remains generally a full matrix in the relative coordinates.

For the entire open cut operator, closing the other strands
sets their input and output indices equal. A term containing
a wrap would lower the total residue degree by a positive
multiple of N. Its remaining change would have to equal
the difference of the two open-core indices, whose absolute
value is less than N. This is impossible. Hence no wrap
contributes to any entry of that cut operator. It is exactly
the original nilpotent scalar cut F_N(M) I.

Consequently, retaining the original normalization,

    theta^(-w) Tr(D_cut B_beta)=F_N(M)                (6.2)

in every tree/source chart, including the algebraic carry
fiber and the marked source infinity. Multiplication by
the full original ADO dimension retains the same meridian
family and its whole boundary germ. The all-level quantum-A
annihilator ideal is unchanged because (6.2) is the same
actual rational function, not a new state.

For the general root branch (4.6), the scalar t^(-w)
cancels exactly in both operator and cut conjugation. A
source vector and its dual row still carry their reciprocal
line factors. This does not discard any unpaired boundary
factor or the original ADO dimension.

For arbitrary frozen normal directions this uses the already
specified auxiliary crossing lift; no generic braid relation
for that lift is asserted. On the coherent semicyclic source
family the genuine holonomy braid construction remains the
one proved separately. Neither claim identifies a fixed
hyperbolic root-central character with the actual rational
state.

The carry source is essential even in the simplest check:
the figure-eight cut at N=2 is 3+2=5, with the second
contribution in the retained Tor directions. The finite and
infinite source frames preserve all five, not just the
ordinary specialization image.

The subsequent [braided source groupoid](braided_source_groupoid.md)
now transports these full charts under genuine moving-center
braids. Its inverse endpoint factors retain the actual total
F and give relative-space arrows with strict mixed transport
relations. The separate [actual meridian source](meridian_casimir_source.md)
constructs a local color-shift connection with a specified
projector source and meridian-normal cup/cap residue. These
spectral meridian jets are not identified with the internal
carry epsilon by a change of notation.

## 7. Exact audit and the remaining geometric comparison

[The audit](../experiments/audit_source_flag_carry_extension.py)
checks 42 tree configurations at N=2,3,4,5,6,9, with up to
six leaves. It compares the full finite-source formula (3.2)
to independently constructed pointed fusion trees and actual
endpoint frames at two nonzero ramified parameters and two
source flags: 168 full matrix comparisons.

The marked infinity matrix is constructed from exact
valuations and leading coefficients, retaining the sign in
(4.4). In the two-leaf cases, independent carry generators
verify its full total and relative algebra intertwinings,
including the wrap coefficients. Source-image naturality
keeps the Tor dimensions. Thirty actual generic/Kashaev
braid cuts agree in all three source charts, and their
whole open cut operators are the original scalar. The
figure-eight split 3+2=5 is retained. The audit also includes
256 relative-root branches at infinity, 114
with a nonzero retained line order and largest tested order
three. Every two-leaf branch is checked against the full
independent total and relative carry generators; no new
determinant-one normalization is imposed.
[Results](../experiments/source_flag_carry_extension_results.json).

    python3 experiments/audit_source_flag_carry_extension.py

The proof supplies a common integral local presentation of
the selected actual period through the source degeneration.
It permits the geometric normal flags to be used in these
ordered recoupling charts without discarding the source or
rechoosing its cut. It does not yet construct the complete
equivariant colored tensor presentation on the positive
ideal triangulation. In particular the earlier bare
vertex-order counterexample and the distinct actual threaded
central character are not removed by this lattice theorem.

The operator's relevant geometric component and the selected
marked Bloch-regulator norm across levels remain unproved.
The internal epsilon and auxiliary source parameter t are
not identified with the actual meridian normal coordinate
by a change of notation. The original volume conjecture
remains the active goal.
