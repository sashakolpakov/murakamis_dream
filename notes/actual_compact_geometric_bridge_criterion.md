# When the compact physical star locus can contain hyperbolic geometry

28 October 2026. The compact Gram intersection is not automatically a
real-form locus of zero-volume representations. It CAN contain a
discrete-faithful representation: an explicit algebraic figure-eight
example is given below. There is also an all-width feasibility criterion,
including a necessary common-circle condition on the chosen bridge
eigenflags. Thus real compact accessibility depends on the actual bridge
marking; it cannot be assumed for a broad knot class.

The original cap has an exact nonzero coefficient on every matched
product packet, with no asymptotic normalization ambiguity. That
computes the cap half of a weighted geometric overlap. It leaves the
original braid transition amplitude, and possible cancellation in the
full overlap, unproved.

## 1. The compact cap locus is an explicit bridge-generator real form

Use the original complete source and the bounded physical meridians
of [the cup/cap Gram theorem](actual_plat_cup_cap_gram_support.md).
A compact head character has

    |k|=1, e=-conjugate(f), k+k^(-1)+ef=-2,
    G=[[k,e],[fk,k^(-1)+fe]].                       (1)

An ordinary adjacent cap relation is H_2 H_1=I. By the triangular
factorization, it says L_(-,2)L_(-,1)=L_(+,2)L_(+,1). One is lower
triangular with top-left one; the other is upper triangular with
bottom-right one. Consequently BOTH are I. All earlier paired L_-
prefixes therefore reset after each cap. The chosen top bridge
generators are precisely G_1,G_3,..., with their partners inverse.

Conversely for ANY G with data (1), the partner

    k_2=k^(-1), e_2=-k^(-1)e, f_2=-k f             (2)

also satisfies the compact star conditions, and its two L products
are I. Thus the compact top-cap locus is exactly the product of these
explicit bridge-generator sets, with based partners inverse. This
also includes G=-I, but a discrete-faithful meridian is noncentral.

Let a representation of a fixed k-bridge plat be given, and let mu_r
be its CHOSEN oriented top bridge meridians, with trace two. It lies,
up to simultaneous conjugation, in the compact physical intersection
IF AND ONLY IF there exists one g in PGL2(C) such that, for EVERY r,

    G_r=-g mu_r g^(-1)=[[a_r,b_r],[c_r,-2-a_r]],
    |a_r|=1, c_r=-a_r conjugate(b_r).              (3)

Necessity is (1) and the prefix reset. For sufficiency put k=a_r,
e=b_r,f=c_r/a_r, construct all partners by (2), and use the given
plat representation relations. They are exactly the bottom Nielsen
cap constraints. The same common conjugation, not independently
chosen frames at the bridges, is essential. Formula (3) is a finite
real-algebraic feasibility test at ANY width.

## 2. Equivalent common Hermitian-matrix criterion

There is a useful coordinate-free version of (3). It is equivalent to
the existence of Hermitian matrices B,J such that

    B>0, signature(J)=(1,1), J B^(-1) J=B,
    mu_r^* J mu_r-J
          =-(1/2)(mu_r-I)^* B(mu_r-I), every r.     (4)

These are actual matrix conditions on the specified meridians. They
do not require an arbitrary choice of a geometric action normalization.

Proof in the compact frame. Put J_0=diag(1,-1), B=I. If G is (1),
write N=G+I. A noncentral N has null image/kernel line (1,t), |t|=1,
and takes the form

    N=a [[1,-t^(-1)],[t,-1]],
    a=1+k, |a-1|=1.                              (5)

Direct multiplication gives N^*J_0 N=0 and
N^*J_0+J_0N=N^*N/2. Hence

    G^*J_0G-J_0=-N^*N/2,

which is (4), since mu=-G. Conversely for a noncentral trace-minus-two
G satisfying that equation, apply it to a nonzero v in ker(G+I).
It forces v^*J_0v=0. Thus v=(1,t), |t|=1. In (5), the same equation
forces |a|^2=2 Re a, equivalent to |a-1|=1. This recovers (1).
The central case is G=-I and is included directly.

Under a common conjugation g set B=g^*g and J=g^*J_0g. These satisfy
(4). Conversely J B^(-1)J=B makes B^(-1/2)J B^(-1/2) a Hermitian
involution of signature (1,1). A unitary diagonalization therefore
produces g with precisely those B,J, reducing back to the compact
frame. This proves equivalence.

## 3. A genuine all-width obstruction: bridge flags must be concyclic

Every noncentral compact G has its unique eigenflag (1,t) in (5),
with |t|=1. Consequently ALL chosen bridge eigenflags of a compact
representation must lie on ONE generalized round circle before
conjugation. For four distinct flags every cross-ratio must therefore
be real. Equivalently they must be null for one indefinite Hermitian
form J. This is a necessary condition at arbitrary bridge number;
it is not claimed sufficient without the amplitude conditions (4).

Thus a discrete-faithful representation whose chosen bridge flags
have a nonreal four-point cross-ratio is absent from that particular
compact physical star intersection. It could still contribute to the
original scalar through a complex analytic saddle. Ordinary real Gram
moment support would miss that exponential mechanism.

The criterion concerns the ACTUAL chosen bridge generators. A change
of bridge presentation can change the set of flags. It is not a
claim that a given knot has no other compactly accessible presentation.

## 4. Complete two-bridge criterion: an explicit cardioid

For two noncommuting noncentral trace-two parabolics put

    tau=Tr(mu_1 mu_2)-2 !=0, phi=Arg tau in (-pi,pi].

Then (3) holds IF AND ONLY IF

    phi!=pi, 0<|tau|<=16 cos^2(phi/2).             (6)

In particular a nonzero negative real tau is excluded. To prove this,
write the two compact matrices using (5), with a_j=1+k_j and unit
flags t_j. Their trace invariant is exactly

    tau=a_1 a_2(2-t_1/t_2-t_2/t_1)
         =4 a_1 a_2 sin^2(delta/2),
    a_j=2cos(alpha_j)exp(i alpha_j),
    -pi/2<alpha_j<pi/2, alpha_1+alpha_2=phi.

Since cos(alpha_1)cos(alpha_2)<=cos^2(phi/2), this proves necessity.
Conversely choose k_1=k_2=exp(i phi), a_1=a_2=1+exp(i phi), and
t_1=1,t_2=exp(i delta), where

    sin^2(delta/2)=|tau|/[16cos^2(phi/2)].

These give the prescribed invariant. Two irreducible trace-two
parabolics are determined up to simultaneous conjugation by tau:
use their distinct fixed eigenvectors as a basis, obtaining
[[1,s],[0,1]] and [[1,0],[t,1]], then diagonally normalize s=1;
the remaining parameter is st=tau. This proves sufficiency for the
original pair, not only for some abstract representation.

## 5. Exact discrete-faithful prototype inside the compact intersection

Use the independently checked figure-eight Riley pair

    A=[[1,1],[0,1]], B=[[1,0],[u,1]], u^2-u+1=0,
    u=exp(i*pi/3),

from [the marked holonomy proof](marked_braid_holonomy.md). Set

    a=1+u, z=(5+i sqrt(11))/6, z+z^(-1)=5/3,
    G_1=[[u,-a],[a,-2-u]],
    G_2=[[u,-a/z],[a z,-2-u]].                      (7)

Both matrices satisfy (1), and Tr(G_1G_2)-2=u. There is an explicit
conjugation, not just matching dimensions:

    F=[[a(z-1),1],[a(z-1),z]],
    F A F^(-1)=-G_1, F B F^(-1)=-G_2.             (8)

Its determinant is nonzero. The identity for B uses
a^2=3u and 3(z-1)^2+z=0. Thus this is the SAME discrete-faithful
representation, at the recorded geometric embedding.
All algebraic identities hold at BOTH Riley embeddings. Conjugating
u,z and every displayed matrix gives the conjugate discrete-faithful
place, including the positive-volume convention used in the earlier
regulator calibration. Compact accessibility is therefore not confined
to the opposite volume orientation.

With top meridians (G_1,G_1^(-1),G_2,G_2^(-1)), the actual Nielsen
word for the four-plat [2,-1,2,2] satisfies BOTH bottom inverse-pair
relations exactly. Symbolically their common Riley factor is
u^2-u+1. After the top pair substitutions the remaining free-group
relator is a cyclic permutation of the usual figure-eight relation
a b^(-1) a^(-1) b a=b a b^(-1) a^(-1) b, so this is the same
two-bridge presentation. Consequently the complete compact star intersection can
contain a discrete-faithful point. It is not uniformly a trivial,
unitary-group or zero-volume representation locus.

This is a prototype diagnostic of the GENERAL criterion, not a new
figure-eight asymptotic proof or a broad accessibility claim.

### The same prototype has NO wholly real compact source-to-source transport

There is an exact limitation even in this accessible case. The top
compact point above does NOT imply that the actual incoming cup
point pulled through W is also compact. In fact no simultaneous
frame makes both endpoints compact for this discrete-faithful plat.

The other bottom bridge generator of [2,-1,2,2], in the canonical
A,B frame, is

    C=A^(-1) B A^(-1) B^(-1) A
       =[[2,u],[u-1,0]].

The three distinct fixed flags of A,B,C are 0,infinity,u-1 in the
column-ratio coordinate. Their unique generalized circle has,
up to a nonzero real scalar, Hermitian form

    J_0=[[0,2-u],[1+u,0]], det J_0=-3.

Direct exact multiplication gives

    A^*J_0A-J_0=diag(0,3),
    B^*J_0B-J_0=diag(3,0),
    C^*J_0C-J_0=0.                               (8a)

Any common compact frame for A,B,C would, by Section 3, have this
same null circle. But (4) forces a NONZERO negative rank-one defect
for every noncentral bridge meridian and every B>0. The last identity
in (8a) contradicts it for C, regardless of the scale/sign of J_0.

Thus the bottom Nielsen cap equations in the weak Gram intersection
are weaker than demanding that its transported input variables obey
the same physical star real form. This is allowed because the
original W is nonunitary: Ad_W does not preserve adjoints. The
geometric source-to-source transition here must be treated by complex
analytic propagation, not by a positive real canonical map between
the two compact cup loci in this fixed physical polarization. New
frame adapters could change that question, but would have to retain
their source and exponential normalization. This explicitly locates a mechanism by
which weak Gram support can fail to see the exponential geometry,
even when its necessary intersection contains that representation.

## 6. The original cap packet weight is nonzero EXACTLY

The cap half of an admissible real compact overlap can also be
computed without a formal Gaussian approximation. The ORIGINAL
normalized cup has coefficients

    phat_(i,j)=x^(-j)delta_(i+j,d)/sqrt(N).

For ANY unit vector v in C^N define its actual reflected dual by

    (J_x bar v)_j=x^(-j) conjugate(v_(d-j)).

It is a unit vector and direct summation gives

    <v tensor J_x bar v, phat>=N^(-1/2).           (9)

For k cups choose arbitrary unit v_r and put

    z_0=tensor_r(v_r tensor J_x bar v_r),
    z=G_top^* z_0, phihat=G_top^* uhat.

With ALL original pivot phases retained,

    <z,phihat>=N^(-k/2).                          (10)

In particular cup-compatible localized product packets have a known
nonzero cap coefficient, uniformly in their centers and N. This is
the actual positive cap state fixed in the source theorem; it is not
a new favorable cap or a division by the knot period.

There is an exact whole-source decomposition. Choose ANY orthonormal
basis {v_(r,a)} on the first head of each pair and form the matched
packets z_a above. They are orthonormal and

    phihat=N^(-k/2) sum_a z_a,
    P_N=chi_N N^(k/2-1) sum_a <z_a,W uhat>.        (11)

Thus every cap coefficient in this complete decomposition is the
same positive polynomial factor. A single chosen packet may be
included by extending its v_r to an orthonormal basis. The individual
projector-weighted term is exactly chi_N N^(k/2-1)<z,W uhat>.

For (7) this includes localized packets at the geometric compact
point. On each odd head take a Gaussian of width sqrt(N), center
N/3-1/2, and phase exp(-i Arg(t_r)j), with t_1=1,t_2=z; normalize
on j=0,...,d and use the exact reflected dual above on its partner.
The K,e,f mean-square errors relative to (7) and (2) are O(1/N):
the clock varies by O(N^(-1/2)) across the packet, the shift error
is O(N^(-1/2)), and the endpoint tails are exponentially small.
Applying the specified G_top^* changes the shift phase only by Q,
so the same leading geometric point is retained. Its cap coefficient
is STILL exactly (10), rather than merely a formal Gaussian unit.
At the conjugate Riley place the same construction has center
2N/3-1/2 and the conjugated t_r; the source root and pivots remain
the original ones.

Equation (11) does NOT say that its braid transition amplitudes have
the same phase or that the geometric one is nonzero. Those amplitudes
still contain the original whole W and can cancel in their sum. The
bounded Nielsen constraints control their classical support, not their
action-normalized coefficients. No exponential overlap estimate has
been proved here. In particular one may not infer that a geometric
point satisfying (3) has positive mass in the actual ket Gram limit.

The exact criterion (3)-(6) and cap amplitude (9)-(11) locate the next
missing quantity: the original braid transition to a geometric matched
packet, with its actual analytic cycle, and its cancellation against
the other transitions. Weak real Gram support alone cannot supply it;
when (3) fails it cannot see that geometric point at all.

[Audit](../experiments/audit_actual_compact_geometric_bridge_criterion.py):
exact algebraic compact figure-eight data and literal four-plat
Nielsen equations, common Hermitian identity, the two-bridge cardioid
construction, and exact original cup/pivot packet coefficients.
