# Entire adjacent source projectors and their lattice groupoid

Research note, 26 October 2026. On three strands, the two adjacent
actual meridian projectors have a joint two-channel polar form.
Its overlap is an explicit original pivotal cut moment. The
remaining projector terms are regular at completeness. This
determines their full local meridian germs, beyond the residue.

There is also a uniform obstruction: these two projectors cannot
both preserve one finite meridian lattice. A comparison must
retain their changes of lattice. This concerns the original ADO
source operators, not a replacement quantum invariant. The
selected geometric period and volume conjecture remain unproved.

## 1. Adjacent cups and caps give opposite source matrix units

Keep N>=2, q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), and

    x=-M/q, u=Log M, R=C[[u]],
    delta=rho(M^2-M^(-2)), nu=(-1)^N rho^2.

At M=1 use the actual cup C=vec(D^(-t)) and cap L=vec(gD)^t,
where D_(N-1-a,a)=q^(a^2) and g=K^(1-N). Their two snakes
are identities and LC=0. This follows directly by multiplying
the two antidiagonal matrices: gD D^(-t)=I and D^(-t)gD=I.
The remaining scalar uses x(1)^(1-N)q^((N-1)^2)=1.

On W_0=V^(tensor 3) put

    i_1=C tensor I, i_2=I tensor C,
    c_1=L tensor I, c_2=I tensor L.

The snakes and zero loop give

    c_1 i_2=c_2 i_1=I, c_1 i_1=c_2 i_2=0.        (1.1)

Consequently (i_1,i_2) and (c_2,c_1)^t split two copies of V,
and the two nilpotents Pi_i=i_i c_i are opposite matrix units.
In particular

    Pi_i^2=0, Pi_1 Pi_2 Pi_1=Pi_1,
    Pi_2 Pi_1 Pi_2=Pi_2,
    Tr(Pi_1 Pi_2)=N.                             (1.2)

Tensoring the other strands gives the same identities and trace
N^(b-2). This is the loop-zero Temperley--Lieb relation derived
from the actual cups and caps.

## 2. Integral numerators and the charged simple block

Let E_1,E_2 be the actual last Casimir projectors on positions
12 and 23 at generic M, and set T_i=delta E_i. They are
rational matrices regular at M=1. To see this without evaluating
a projector there, let Omega_i be the pair Casimir and let P_i
be the integral projector onto the colliding c_0,c_last cluster.
That unordered cluster is separated from the other roots at M=1;
polynomial Bezout interpolation therefore gives regular P_i.
Then

    T_i=(Omega_i-c_0)P_i,
    T_i^2=delta T_i,
    T_i(1)=nu Pi_i.                              (2.1)

All these identities use the exact branch difference delta,
not just its linear coefficient 4rho*u.

Use the charged color P=V_z, z=-M^3/q, required by
[the meridian charge calculation](sewn_source_and_meridian_charge.md).
Let S be the total-Casimir projector of W=V_x^(tensor 3) onto
its z block. Its complete Casimir is -2 and its derivative in
the central polynomial is (-1)^(N+1)N^2. Thus S is integral.
This block is P with multiplicity N. Each E_i S has rank one
on that multiplicity space: the pair image V_(M^2) tensored
with V_x contains P once in the explicit highest-vector fusion.

The remaining operators

    F_i=E_i(1-S)                                  (2.2)

are integral idempotents. Indeed T_i(1)(1-S(1))=0 since Pi_i
factors through the complete color V with Casimir -2. Their
integral numerators T_i(1-S) are therefore divisible by delta
in R. Their ordinary rank is N(N-1). This already isolates
all poles in the charged block, uniformly in N.

## 3. The exact overlap is an actual cut moment

Normalize the highest vector of the last two-color branch by

    h=sum_(a=0)^(N-1) h_a v_a tensor v_(N-1-a), h_0=1,
    h_(a+1)/h_a=-e_(N-1-a)(x)Q^(N-a-2)/[e_(a+1)(x)x].

Its coefficients are units near the complete color where needed.
The covector vanishing on the F-descendants of all other branches
has unnormalized coefficients

    lambda_a=(-1)^a x^(-a)Q^(a(a-1)/2).

This follows from lambda_(a+1)+x^(-1)Q^a lambda_a=0, the
two entries of the actual total F at degree N-2. Its normalization
is Z=sum_a lambda_a h_a. On the total highest vectors
h tensor v_0 and v_0 tensor h, the cross-projection coefficients
of E_1 and E_2 are both lambda_(N-1)/Z. Only the component of
pair degree N-1 can contribute; the others have zero last-branch
projection. Thus the equality of these two coefficients is exact.

The finite calculation in the appendix gives, with r=x^(-2),

    Z=(1+r^N)(1-rQ^(-1))/(1-r^2 Q^(-3)).

Using r=Q/M^2 and lambda_(N-1)=(-1)^N q M^(1-N) yields

    delta*lambda_(N-1)/Z=A_N(M),
    A_N=(-1)^N rho (M+M^(-1))
                 *(qM^2-q^(-1)M^(-2))/(M^N+M^(-N)). (3.1)

The complete value is A_N(1)=nu. In particular A_N is a unit
of R. Its full M^N+M^(-N)=M^(-N)(1+U) factor is retained.
Comparison with the independently proved original pair moment
in Section 7 of [the cut-density note](geometric_rigidity_and_cyclic_source.md)
shows

    A_N(M)=Phi_pair(T_1),
    A_N/delta=Phi_pair(E_last).                   (3.2)

where Phi_pair is the original scalar pivotal partial trace,
before multiplication by the full modified dimension. Hence the
overlap is fixed by the actual cut, with its phase and peripheral
function, rather than selected by a model normalization.

## 4. A joint regular frame for the full polar source

Let theta=x(1)^(1-N). Define two P inclusions by highest vectors
theta*h tensor v_0 and theta*v_0 tensor h and then the original
total F descendants. Call them U_0,U_1. They are regular rational
intertwiners and at completeness become i_1,i_2. The common
theta is necessary to keep the original complete cup frame.

On their images, (3.1) gives the integral matrices

    t_1=[delta A_N;0 0], t_2=[0 0;A_N delta].     (4.1)

Here and below scalar matrices act on the two-copy multiplicity
factor, with identity on P. There are regular rational rows
r_1,r_2 with T_1 S=U_0 r_1 and T_2 S=U_1 r_2. For example,
extract them with any coordinate left inverse of the primitive
U_i; the factorization makes them H-linear. Their values on
U=(U_0,U_1) form

    C=[delta A_N;A_N delta].

Its determinant delta^2-A_N^2 has value -nu^2 at M=1, hence
is a unit. Set R=C^(-1)(r_1,r_2)^t. Then

    RU=I, T_i S=U t_i R,
    R(1)=(c_2,c_1)^t.                            (4.2)

This proves an exact joint normal form, retaining every meridian
coefficient of the actual projectors:

    E_1=U [1 A_N/delta;0 0]R+F_1,
    E_2=U [0 0;A_N/delta 1]R+F_2.               (4.3)

The regular F_i annihilate S and the common source corner e=UR.
Both E_i vanish on the remaining N-2 multiplicity directions of
S. Thus no additional polar channel has been discarded. Tensoring
the construction with the remaining colors proves it for b>=3,
with P replaced by the charged P_b of the preceding note.

There is an intrinsic version of the source corner. On S put

    G=A_N^2-delta^2,
    e=[T_1T_2+T_2T_1-delta(T_1+T_2)]/G.          (4.4)

This is the same regular projector onto two copies of P. Its
matrix units follow from

    (t_1t_2-delta t_1)/G=E_11,
    (t_2t_1-delta t_2)/G=E_22,
    (t_1-delta E_11)/A_N=E_12,
    (t_2-delta E_22)/A_N=E_21.                   (4.5)

Thus the integral numerators generate Mat_2(R) on the source
multiplicity space. Their joint comparison torsor, with the
charged P fixed, is R^times: End_H(P)=R and a simultaneous
intertwiner of the full matrix algebra is scalar. This specifies
the local torsor and its trace calibration on three strands.
After tensoring, the unrestricted comparison group is instead
End_H(P_b)^times unless the spectator action is also fixed.
Identifying such a
torsor with a triangulation realization still requires its actual
source operators and overlap to be matched.

The [subsequent spectral-source calculation](actual_braid_group_and_spectral_source.md#6-a-cover-can-split-the-spectral-algebra-instead-of-killing-it)
places these formulas in a universal rank-four algebra.
For two numerators with t_i^2=delta t_i, the expression
z=t_1t_2+t_2t_1-delta(t_1+t_2) is central. On the cover
A^2=z+delta^2, with A,z units, (4.5) are its explicit matrix
units. The actual root is exactly (3.1). This is a spectral
splitting and scalar-torsor reduction, not nilpotence of the
full source group. Genuine pure braid powers have a connected
SL_2 quotient; their invariant plane is not generally this
particular two-cup corner.

## 5. Whole sewn cuts now have an exact source decomposition

For any integral whole knot operator B(M), let B_ij=R_i B U_j.
The original calibrated rectangular trace identity gives

    mathfrak_t_W(B E_1)
      =mathfrak_t_P(B_00)+(A_N/delta)mathfrak_t_P(B_10)
                                      +mathfrak_t_W(B F_1),
    mathfrak_t_W(B E_2)
      =mathfrak_t_P(B_11)+(A_N/delta)mathfrak_t_P(B_01)
                                      +mathfrak_t_W(B F_2). (5.1)

These are identities of full meridian germs, not only residues.
The P trace uses the original d_N(M^3), including the exact
dimension ratio already recorded in the charged-source note.
The full affine source coefficient 1+U^(-1) multiplies these
entire identities and is retained before specialization.

The regular terms can cancel the source diagonal term. For
example, on three strands the full cut of E_i itself is zero,
while mathfrak_t_P(I)=d_N(M^3). Consequently

    mathfrak_t_W(F_i)=-d_N(M^3).                 (5.2)

No positivity or noncancellation assertion follows from the
nonzero source corner or its perfect bilinear trace.

There is a useful exact simplification only after retaining the
whole affine coefficient. For c=1+U^(-1), equation (3.1) gives

    c A_N/delta
       =(-1)^N M^(1-N)(qM^2-q^(-1)M^(-2))/(M^2-1). (5.3)

Indeed c/(M^N+M^(-N))=M^(-N). Thus the 1+U factor cancels
in the full off-diagonal source, with its phase and monomial
left explicit. Its pole is precisely Y-1, the meridian divisor
in [the actual normal-period construction](peripheral_normal_period.md).
This is a rational identity before specialization, not a reset
of a numerical factor at M=1. It does not identify the full
global normal module or its selected knot period.

## 6. No one finite lattice can regularize adjacent projectors

From (4.3), on the source corner

    Tr(E_1E_2)=N A_N^2/delta^2.

The remaining trace is regular, since it comes from F_1F_2.
As delta=4rho*u+O(u^2) and A_N(1)=(-1)^N rho^2,

    Tr_(W_b)(E_1E_2)
        =N^(b-2)rho^2/(16u^2)+O(u^(-1)).         (6.1)

The leading coefficient is nonzero in characteristic zero.
If a full finite R-lattice were stable under both projectors,
their product would be an integral endomorphism and its ordinary
trace would belong to R. Equation (6.1), invariant under every
meromorphic change of basis, contradicts this. This proof does
not require H-linearity of the hypothetical lattice.

In fact the traces of (E_1E_2)^m have pole order 2m, so the
algebra of both unscaled projectors is not contained in a
finite integral endomorphism order. Multiplying either projector
by a meridian unit, including a peripheral factor with nonzero
complete value, does not remove this obstruction.

Each projector separately has an elementary stable lattice.
For the source pair, replacing P direct_sum P by
delta^(-1)P direct_sum P gives the matrices

    E_1 -> [1 A_N;0 0],
    E_2 -> [0 0;A_N/delta^2 1].                 (6.2)

Thus one elementary change shifts the pole into the adjacent
operator with order two. The appropriate retained data form
a groupoid of lattices and their source maps. The integral
numerators T_i and their polar quotients must stay distinguished.
This does not disprove a relative triangulation comparison with
different lattices on its charts. It rules out a common finite
regularization of these actual source arrows.

## 7. What remains and exact verification

The entire local adjacent polar source is now explicit, with
its charged object, overlap, trace, regular terms and lattice
obstruction. This removes the restriction of the earlier sewn
calculation to a residue. Its common comparison group is scalar
only after the ordered integral numerators have been matched.

These R-unit inversions are fixed-level meridian statements.
The value A_N(1)=(-1)^N rho^2 tends to zero as N grows, so they
are not automatically unit inversions in the joint quantum--meridian
completion S=C[[u,h]] used for the point-source model. A comparison
of those two realizations must retain this additional lattice
information. No cross-level norm bound is inferred from the frame.

The subsequent [uniform Frobenius source base](uniform_frobenius_source_base.md)
now resolves this coefficient degeneration on a specified meridian
chart. It retains w=M^N and the root phases, records the exceptional
rho line, and extends the normalized two-channel algebra. Its marked
Frobenius period also evaluates the full original cap normalization.
This concerns the coefficient algebra; the full color object and
selected knot period have not thereby been extended across levels.

The full meridian atlas still contains its specified transitions,
and their whole-germ cancellation must be compared with the
relative triangulation source. The actual selected section has
not been identified with the marked geometric period. Neither
the formal normal-block comparison nor (5.1) proves the regulator
norm across levels. The volume conjecture remains unproved.

The finite sum in the appendix has existing coverage as the
[first q-Chu--Vandermonde identity, DLMF 17.6.2](https://dlmf.nist.gov/17.6.E2).
The formula and scope were checked after deriving our independent
certificate. No published proof technique is imported. The cup/cap
relations and matrix-algebra facts are existing elementary theory;
no novelty is claimed for them. The calculation here fixes the
actual overlap, charge and pole data in the original conventions.

[The audit](../experiments/audit_adjacent_polar_source.py) checks
the generic telescoping certificate and the universal two-by-two
relations symbolically. Six complete original tensor cases verify
the opposite cup/cap units and vanishing of the regular-remainder
numerators. Twelve generic pairs of actual full projectors verify
the charged inclusions, retractions, overlap, regular idempotents
and their ranks and full modified cuts. Forty-eight full tensor-cut
decompositions for the identity and figure-eight words check (5.1),
with original framing and normalization. Even and odd composite
levels are included.
[Results](../experiments/adjacent_polar_source_results.json).

Reproduce with:

    python3 experiments/audit_adjacent_polar_source.py

## Appendix. An independent finite-sum certificate

From the actual highest-vector recurrence, at the primitive root Q,

    Z=sum_(k=0)^(N-1) [(r^(-1)Q^2;Q)_k/(r;Q)_k]
                                      *(r^2 Q^(-3))^k.

For a generic base Q define

    f_(n,k)={n choose k}_Q (a;Q)_k(c Q^k;Q)_(n-k)
                                    *(-c/a)^k Q^(k(k-1)/2).

Let t=Q^n, z=Q^k. The ratio f_(n+1,k+1)/f_(n+1,k) is

    R(z)=-(c/a)(z-Q t)(1-a z)/[(1-Qz)(1-cz)].

Set

    H(z)=-Q t(1-z)(1-cz/Q)/[z(1-Q t)(1-c t)].

Direct rational simplification gives

    R(z)H(Qz)-H(z)
      =1-(1-(c/a)t)(1-Q t/z)/[(1-Q t)(1-c t)].

Multiplication by f_(n+1,k), followed by summation, telescopes;
the two boundary terms vanish. Hence F_n=sum_k f_(n,k) satisfies
F_(n+1)=(1-cQ^n/a)F_n and F_0=1. This proves

    sum_(k=0)^n [(Q^(-n);Q)_k(a;Q)_k/
                     ((Q;Q)_k(c;Q)_k)](cQ^n/a)^k
       =(c/a;Q)_n/(c;Q)_n.

Specialize n=N-1, a=r^(-1)Q^2, c=r after proving this rational
identity. The factors (Q;Q)_k are nonzero for k<N, and
Q^(-n)=Q cancels the matching numerator and denominator. Thus

    Z=(r^2 Q^(-2);Q)_(N-1)/(r;Q)_(N-1)
      =(1+r^N)(1-rQ^(-1))/(1-r^2 Q^(-3)).

All cancellations are whole rational identities. At the complete
color the displayed final denominator is nonzero and Z has its
required simple zero. No infinite product or root asymptotic is used.
