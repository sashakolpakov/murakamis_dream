# The actual braided residual-framing current

30 October 2026. Independently reviewed. After a legitimate
coherent functional fixes the first cut, the actual Hopf adjoint gives
an exact current in the second cut. Its coefficients are two routed
OFF-DIAGONAL bands of the original tensor. They are not reconstructed
from the diagonal two-cut array. The identity holds at arbitrary
width, with actual finite endpoints and every genuine quantum jet.

This is a finite-source integration-by-parts identity. Its closed
flux is zero; no nonzero relative framing residue or selected global
cycle coefficient is inferred from that fact.

## 1. The source, coherent first cut, and actual generic generators

Use the [braided source adapter](actual_braided_two_cut_source_adapter.md).
Fix d=N-1 and zeta=q0 exp(epsilon). At the two actual Morse cuts let
V=V_d^tensor b, W=V_d^tensor c, with b,c>=1, and let A:W->V and
B:V->W be the original covariant maps. Original cups, caps and all
scalar/peripheral factors remain in A,B. The partial closure P_V uses
the actual generic pivot g=(-1)^d K on the closed heads.

Let U be the recorded braid carrying the chosen W head to its first
position. Thus in the parallel convention U=R_1...R_j, with R_j
acting first. Define the WHOLE band operator

    C_(p,q)=P_V[A U^-1(E_pq tensor I)U B],
    J_(a,l)=(C_(l,l))_(a,a).                              (1)

Indices outside 0,...,d are zero ACTUAL matrix entries. No Fourier
wrap or continued endpoint is substituted for that zero. By actual
integer degree conservation C_(l,l) is diagonal, although the nearby
band operators in (1) need not be. Closing the identity cut gives
sum_l C_(l,l)=z(epsilon)I.

For t distinct from 0,1 put

    beta_a(t)=binom(d,a)t^a(1-t)^(d-a),
    e_t=beta(t) 1^T,              Tr e_t=sum_a beta_a=1.  (2)

This is the existing coherent boundary functional with w=1 and
z_coh=t/(1-t). It is source-preserving on the WHOLE exposed scalar:
Tr(e_t zI)=z, exactly, including the fixed d=N-1. It is not an
additional normalized state on the second identity edge. All formulas
below also hold for any specified quantum-independent vector beta of
sum one; (2) is the legitimate coherent localization used here.

Write the actual generic generator entries as

    k_a=zeta^(d-2a),
    f_a=1-Q^(a+1),                   0<=a<d,
    e_a=zeta^(-N)(1-Q^(N-a)),        1<=a<=d,
    Q=zeta^2.                                            (3)

Their missing endpoint arrows are ZERO. In particular f_d=e_0=0
as matrices, even though the untruncated expressions in (3) need not
vanish there at generic zeta. The Hopf adjoints are

    ad_K C=K C K^-1,
    ad_E C=[E,C]K^-1,
    ad_F C=[F,C]+K^-1[K,C]F.

The residual combination is

    D_c=ad_F-ad_E-2(ad_K-I).                              (4)

Its proved principal framing field is partial_r in the actual
F(r,s) chart, with the first cut clock A_cut=(1+s)^-1 fixed; see
[the actual Ward fields](actual_borel_ward_cut_contraction.md).
Multiplication by s gives s partial_r. We do not identify a finite
translation with this infinitesimal field merely from its symbol.

## 2. A source-defined flux using the two neighboring bands

For 0<=a<d define

    L_a=f_a beta_a+(e_(a+1)/k_(a+1)) beta_(a+1),
    L_-1=L_d=0.                                          (5)

Define the actual band pairing and its second-head flux by

    T_t(p,q)=Tr(e_t C_(p,q)),
    M_l=f_l T_t(l+1,l)
                  +(e_(l+1)/k_(l+1)) T_t(l,l+1), 0<=l<d,
    M_-1=M_d=0.                                          (6)

Every C_(p,q) contains the full U and U^-1 and all original
contractions. In particular (6) is not a choice of interpolation
for J. The source identity is

    M_l-M_(l-1)
       =sum_(a=0)^d (L_a-L_(a-1)) J_(a,l)
       =sum_(a=0)^(d-1) L_a[J_(a,l)-J_(a+1,l)],
                         0<=l<=d.                        (7)

Here is a direct proof. Generic pivotal partial closure is an exact
Hopf-adjoint map, and A,B,U intertwine the actual coproduct. Therefore
applying D_c to C_(l,l) is the same as replacing its inserted E_ll
by the corresponding adjoint in W. Since E_ll commutes with K,
the spectator terms cancel, and the inserted matrix is exactly

    f_l E_(l+1,l)+(e_(l+1)/k_(l+1))E_(l,l+1)
       -f_(l-1)E_(l,l-1)-(e_l/k_l)E_(l-1,l),             (8)

tensored with the spectator identity and conjugated by U. Its pairing
is the left side of (7), with all four bands and their actual order.

On the first cut the dual rows are, literally,

    e_(t,K)=K^-1 e_t K-e_t,
    e_(t,E)=K^-1 e_t E-E K^-1 e_t,
    e_(t,F)=e_t F-K F e_t K^-1.

The K row has zero diagonal. Direct multiplication gives

    (e_(t,F)-e_(t,E)-2e_(t,K))_(a,a)
      =f_a beta_a-f_(a-1) beta_(a-1)
        -(e_a/k_a) beta_a+(e_(a+1)/k_(a+1)) beta_(a+1)
      =L_a-L_(a-1).                                     (9)

Only these diagonals pair with C_(l,l). This proves the first
equality in (7); finite summation by parts gives the second.
The proof applies to rectangular A,B and arbitrary fixed width.
It uses the actual routed bands, not a scalar Ward operator assigned
to an unrelated residual index.

For clarity, the generic interior coefficient in (5) is

    e_(a+1)/k_(a+1)=zeta[Q^(a+1-N)-1].

At the root (5) becomes L_a=(1-Q^(a+1))[beta_a-q0 beta_(a+1)].
This shorter root formula must NOT be differentiated as the generic
current: the omitted term is
zeta Q^(a+1)(Q^-N-1) beta_(a+1), whose first derivative at zero is
-2N q0 Q^(a+1) beta_(a+1). Equation (5) retains it and all higher
genuine derivatives.

## 3. Finite-head integration by parts, with the interval ends

Let R_l denote either expression on the right of (7), and let h_l
be any specified finite-head weight. On EVERY actual subinterval
0<=L<=R<=d,

    sum_(l=L)^R h_l R_l
      =h_R M_R-h_L M_(L-1)
         +sum_(l=L)^(R-1)(h_l-h_(l+1)) M_l.              (10)

In particular a window's two current ends are retained. On the
whole head interval the actual endpoint arrows make M_-1=M_d=0.
For h=1 this says sum_l R_l=0. It also follows from
sum_l J_(a,l)=z and sum_a(L_a-L_(a-1))=0. Neither proof says that
the current has zero period on an arbitrarily selected relative
subchain, or that one of its two ends contributes nontrivially.

The identity is generic before any specialization. It may be
differentiated to any fixed quantum order, with the derivatives of
the actual U, inverse route, generator entries, pivots, coupons and
any moving h retained. The same holds for a specified finite sum of
channel assignments with its original coefficients. The original
closed normalization remains F=D_N z and z(0)=F'(0)/nu_N, with
D_N=(-1)^d[N]_zeta. No extra derivative per band or per vertex is
introduced by (7).

### The complete Fourier endpoint of the same actual channel

At completeness let S be the cyclic physical-head shift and
X_j its original Fourier projectors,

    (X_j)_(r,s)=Q^[j(s-r)]/N, eta_j=Q^j, j mod N.

For the ROUTED first-slot channel C(X)=P_V[A U^-1(X tensor I)U B],
the [complete Fourier source theorem](universal_resonant_fourier_source_completion.md)
applies: A U^-1 and U B are still actual covariant maps. Thus
C(X_j)=z X_j. Its proof uses the actual root adjoint equations and
C(I)=zI and also applies to the rectangular maps above. Since
1^T X_j=delta_(j,0)1^T, the legitimate first coherent functional
still gives Tr(e_t C(X_j))=z delta_(j,0), exactly for every t.

The actual cyclic generator formulas give

    D_c X_j=(eta_j-q0 eta_j^-1+2)X_j
          +(q0^-1 eta_j^-1-2)X_(j+1)-Q^-1 eta_j X_(j-1).
                                                               (10a)

Consequently this SAME sourced residual current has the exact
three-node Fourier endpoint distribution

    Tr[e_t C(D_c X_j)]
       =z[(3-q0)delta_(j,0)+(q0-2)delta_(j,N-1)
                                     -delta_(j,1)].      (10b)

Overlapping labels are added when N=2. The total of (10b) is zero.
It is a statement about the original complete root source, not its
generic normal, and no off-root cyclic endpoint is added. It locates
the current at the complete resonance rather than at regular-node
principal samples. Its coefficient remains the UNKNOWN whole scalar
z; homogeneous Ward equations alone cannot determine it or show that
the selected geometric component survives there.

## 4. The specified moving-period realization and its boundary chain

There is a source-preserving residue realization of the coefficients
in (6), not a new interpolation of those finite values. Expand their
ORIGINAL generic tensors, including the routed crossings, in the
specified finite white/cup/cap presentation. For U and U^-1 this is
the FULL generic spectral expansion of each original crossing, with
both small and large partner channels and their actual spectral
denominators. It is not the restricted regular complete-circle
sector sum. Use the actual large
white polynomials and moving-period factorial with P=pi i/Log zeta.
Keep every fixed generic spectral scalar and every integral character;
clear a known intermediate scalar pole before taking the required
higher jet. This is the source class of the
[actual tensor connection](actual_tensor_source_finite_jet_connection.md).

For each admissible assignment and each off-diagonal band retain its
own primitive affine head lattice and ORIGINAL finite support. The
band source has a fixed integral charge offset. At every allowed
integer point its moving-period coefficient is the actual generic
matrix entry. Its small product-cotangent torus therefore gives
that same entry. Summing those tori reproduces T_t(p,q), and the
displayed combinations reproduce M_l and (7), with no omitted
normal. An original constant forbidden stratum remains zero rather
than being assigned a 0/0 continuation.

The first head may be left as the exact finite coherent sum (2).
There is no need to invent a meromorphic interpolation of beta_a.
For the remaining free coordinates x of an individual band let
S(epsilon,x) be its specified meromorphic summand, Gamma its actual
ordered residue cycle, and c(x)=product_j pi cot(pi x_j). For an
integral translation v and an analytic retained weight w, change of
variables gives the EXACT chain identity

    integral_Gamma c w (S_v-I)S
       =integral_Gamma c (S_-v w-w)S
          +integral_(Gamma+v-Gamma) c (S_-v w)S.         (11)

All periods use (2pi i)^(-n_free). The only fact used about c is
its integer periodicity. When the last cycle difference is filled
by an allowed annular chain, its value is the sum of the actual
crossed source residues, with their orientations. All other crossed
divisors, and any remaining relative ends, stay in that formula.
At a coincident source/cotangent pole one must use the full finite
part and complement derivative, as in the
[actual degree-wall theorem](actual_matching_edge_degree_cycle_boundary.md).
It is not enough to multiply a cup's simple residue by an assigned
geometric scalar.

Equation (7) is proved AFTER the original finite internal period
contraction. It has not here been lifted to an off-grid meromorphic
Ward identity on a common free-head lattice: the separate band
charges and support cycles must still be compared to do that.
Equation (10) keeps the exact finite-head ends of this contracted
current. Equation (11) is a universal change-of-cycle rule for EACH
specified band summand, not a proof of that missing off-grid Ward
comparison. These formulas do not replace
Gamma+v by Gamma merely because the source has a moving-P
quasiperiod. The latter has its nontrivial rational gauge, characters
and divisors even at finite normal order.

## 5. The remaining equation at the framing diagonal

The new ingredient relative to the old formal Ward ideal is the
source-defined M_l in (6), including the off-diagonal routed bands
and its finite endpoint chain. Its principal D_c field is the
residual centralizer direction. A stationary pushforward would
have to send THIS current and THIS chain, with the coherent first
head and original complement, to the residual framing current.

In particular neither the finite values J_(a,l) nor the nonzero
local stationary density determine the residue at the framing
diagonal. No continuous second-head current has been defined by
interpolating (7). To obtain the desired framing coefficient one
must identify the pushforward of the prescribed band periods (6)
and the endpoint/divisor chain (10),(11) with that diagonal current,
and compute its actual relative coefficient. A global cycle or
nonzero endpoint intersection is not proved here.

The [focused audit](../experiments/audit_actual_braided_residual_framing_current.py)
and [results](../experiments/actual_braided_residual_framing_current_results.json)
check 19 actual braid/complete-circle sources, including rectangular
one-to-three-head birth/death cuts: 326 original routed band value/first
jet coefficients, 134 flux coefficients, 334 weighted interval/jet
identities, and 48 nonzero retained generic-normal corrections. Separate
original-matrix checks verify 1177 full Fourier-projector channel entries
and 67 three-node complete current values. Symbolic checks verify the
universal integer-shift chain rule and its
resonant cotangent finite part. They do not audit an off-grid Ward
identity or a stationary framing pushforward.

Independent validation: the primary and coherent-source readers fully
checked the actual generic adjoint, four routed bands, coherent dual
row, endpoint arrows, rectangular maps, and finite interval identity;
both freshly replayed the full focused audit, including the added
complete Fourier corollary. The geometry reader independently checked
the principal residual field, complete-source normalization, cotangent
change-of-chain rule and all three resonant coefficients. These reviews
retain the explicit distinction between finite contracted currents,
off-grid Ward assembly and an original geometric-period coefficient.
