# Independent audit of the one-index actual source and fixed-phase operator

Proof audit, 27 October 2026, of
[the actual source/Ward reduction](actual_one_index_fourier_source_and_ward_reduction.md)
and Section 8 of
[the partial support theorem](partial_geometric_support_theorem.md).
The normalization, whole Ward defect, polynomial bound and root-only
phase specialization pass. The final selected Fourier-label sum remains
unproved geometrically.

## 1. The actual fixed-input source

Root K,F intertwining makes the reclosed C diagonal, then equates
successive entries through nonzero arrows 1-Q_N^k. Thus C=P_N(M)I,
with the SAME original peripheral line on both sides. This uses no
E edge, reducibility assumption or inversion of a vanishing norm.

The full original first-cut row gives lambda_a(C)=sum_c C_(c,a).
Partial trace on the second wire proves sum_j Jtilde_(a,j)=lambda_a(C)
for the WHOLE invertible Vandermonde change. On the root scalar
closure this is P_N(M) for every a. Hence the one-index source has
NO outside 1/N; its raw Jtilde still has the Fourier inverse 1/N
inside. The output c remains summed. Setting c=a first would
remove the momentum bands and is not this source change.

## 2. The whole current guard and its bound

For D_K=Ad K-I and D_F(C)=FC-K^-1CKF, direct entries give

    (D_K C)_ij=(Q^(j-i)-1)C_ij,
    (D_F C)_(k,k-1)=(1-Q^k)(C_(k-1,k-1)-C_(k,k)).

There is no off-diagonal pollution in the latter row. Dividing
these head units and centering the diagonal chain therefore gives
h delta C=C-I Tr(C)/N as a WHOLE matrix identity. Neither
1-Q^N nor a color-normal edge is inverted. With
Gamma_a=(e_a-1/N)1^t, where 1 is the all-ones column,

    lambda_a-Phi=Tr(Gamma_a h delta).

This proves the stated cochain source identity. It sets delta C=0
only on the actual root Hopf closure. Every whole derivative of
h, delta and C remains in its printed Taylor convolution. For
scalar C_0 the operator derivatives satisfy delta_j(C_0)=0,
since delta_t(I)=0 for all t; the stated first-order simplification
is consequently valid without off-root scalarity.

The root balanced-flat norm estimate also passes. Anchor at the
middle vertex. Left and reflected right edge inputs and anchored
outputs are disjoint; the inverse-arrow factors are bounded by
N/[4 min(k,N-k)]. Each block is dominated by N/4 times the
Hardy-tail kernel 1/k for i<=k. With weights i^-1/2 its row and
column bounds are respectively three and two, so its norm is
at most sqrt(6). Mean subtraction is orthogonal projection.
The K inverse is at most N/4 and has orthogonal output to the
diagonal primitive. For the direct-sum Hilbert--Schmidt input
norm this proves ||h||<=3N/4. Since
||Gamma_a||_HS=sqrt(N-1), the source primitive is bounded by
(3N/4)sqrt(N-1). This is not a whole-word or geometric-period
bound and does not assert a uniform root neighborhood.

## 3. Fixed phase and whole power marks

The finite bad-fiber argument is valid after clearing the finitely
many rational shape/Jacobian denominators. A whole excluded A fiber
requires all coefficient polynomials in the other coordinate to
vanish. If a unit is algebraic on a retained finite cover, its
field norm gives the same sufficient test. The operator's nonzero
leading symbol similarly excludes finitely many half-phase fibers.
Infinite root-of-unity half-phases provide a good fixed k/d.

For a_N=floor(kN/d) and r=kN modulo d, the root formulas are

    A_N=exp(2pi*i*k/d) q_N^(-2r/d),
    Ahat_N=exp(pi*i*k/d) q_N^(-r/d).

Before normal differentiation their actual power graph is
A_N=(Q^N)^(k/d)Q^(-r/d) and
Ahat_N=(q^N)^(k/d)q^(-r/d), with logarithmic marks N Log Q
and N Log q. Thus D_Q Log A_N=a_N; freezing its root phase first
would give only -r/d. The notes preserve this distinction.

The root operator substitution Ahat=alpha_* q^(-r/d) is an Ore
homomorphism because the meridian shift fixes these characters.
The good-phase choice keeps its first classical symbol nonzero;
its preexisting polynomial divisibility by A_geo specializes
unchanged. On q=z^d the leading order gains only the nonzero
scalar d^s. The nondegenerate geometric block persists on this
marked meridian/phase germ with its same frame-independent action.

A common LEFT multiple may combine the finite residue-class
operators; an arbitrary ordered product would not justify that
claim. None of this identifies the root partial lift with whole
Vandermonde normal jets or proves geometric survival after sum_j.
