# One extra quantum region degree, with an exact original crossing port

28 October 2026. The third classical certificate changes the region
flag in the literal middle configuration. Its two projective
coordinates do not form a quantum torus on the original two heads.
This note constructs a genuine quantum-torus extension with one
extra region degree whose **typed matrix elements** are exactly
those physical coordinates. The extension has a fixed vacuum source.

It also proves an exact vacuum-port formula for the other original
crossing factor. A complete marked full-Phi pentagon can be applied
BEFORE the auxiliary contraction; summing every intermediate index
still gives that original factor and hence the original R. No knot
value defines the auxiliary source.

The complete developed geometric face-order table for the third
certificate is not inferred from these two facts. In particular,
different matrix elements are not multiplied as though compression
were an algebra homomorphism.

The subsequent [physical THIRD theorem](literal_third_full_phi_certificate.md)
now supplies that literal face/source certificate by a different
construction on the original two heads: inverse actual flag transport
and opposite-root FIRST, with its full reflected input adapter. It
also explains the forced degenerate clock in this auxiliary vacuum
port. The auxiliary identities below remain valid; they are not used
as the missing regular geometric face table.

## 1. The actual third-region coordinates

Use complete original heads and marks

    Q=exp(2pi*i/N), x=-q^(-1), k=x^N=(-1)^(N-1),
    Z=Z_1, Z_2, X=xS_2S_1^(-1),
    S_1^N=mu, S_2^N=k mu,
    XZ=QZX, XZ_2=Q^(-1)Z_2X, X^N=Z^N=Z_2^N=1.

The actual total lowering current gives the normalized last
region flag in the middle configuration's homogeneous frame as

    R=1-n_R, n_R=(1-Z_2)X=x f_2 S_1^(-1).        (1)

The root binomial product gives n_R^N=0, so R is a unit.
Normalizing this new region to one changes the two projective
coordinates to

    X'=Z_2X R^(-1), Z'=1-R(1-Z).                (2)

Their failure to satisfy X'Z'=QZ'X' cannot be repaired by
renaming them as a new quantum-torus pair. We instead retain
the missing face degree explicitly.

## 2. An honest extended quantum torus

Add an auxiliary head with

    W|j>=Q^j|j>, S|j>=|j+1>, S|d>=k|0>,
    WS=QSW, W^N=1, S^N=k.

It commutes with the physical heads. Put a=Z_2X and

    A=a tensor S^(-1),
    B=1 tensor W-Q^(-1)1 tensor WS+Z tensor S.   (3)

Then exactly

    AB=QBA, A^N=B^N=1.                          (4)

For the commutator, A has quantum degree one against each
of the three displayed summands of B. For the central
powers, a^N=k and S^N=k give A^N=1. In the displayed
order the three summands of B pairwise Q-commute. Their
root binomial powers give 1-S^N+Z^NS^N=1. These
calculations include even and composite levels.

The face normalization has a periodic quantum lift. Define

    U_j=P(Q^j n_R)^(-1)P(n_R)
        =product_(r=0)^(j-1)(1-Q^r n_R),
    U=sum_(j=0)^d U_j tensor |j><j|,              (5)

where P is the original finite Euler polynomial. Every
factor is invertible since n_R is nilpotent. Moreover

    U_0=1, U_1=R, U_N=1.                        (6)

Thus there is no omitted auxiliary wrap or independently
chosen norm root. Let Atilde=UAU^(-1), Btilde=UBU^(-1).
Its typed matrix elements are

    <0|Atilde|1>=Z_2X R^(-1)=X',
    (<0|+<1|)Btilde|0>=1-R+RZ=Z'.              (7)

The Q^(-1) coefficient in (3) is essential: WS sends
|0> to Q|1>, so its off-diagonal contribution in (7)
is exactly -R.

For every physical operator O,

    <0|U(O tensor 1)U^(-1)|0>=O.                 (8)

Hence this controlled face extension can be inserted with
its fixed vacuum without changing an original physical
operator or any of its external source conventions.

The ports in (7) have different incoming/outgoing types.
When words are composed one must sum every intermediate
auxiliary index. Equation (4) applies before that sum.
It does not assert that multiplying the two entries in
(7) preserves the same commutator after compression.

## 3. An explicit quantum triangle source

The simple B in (3) is not an unspecified similarity.
Set

    L=(1-Q ZW^(-1))S, C_B=P(L).                  (9)

Then

    L^N=0, B=C_B W C_B^(-1), [A,C_B]=0,
    <0|C_B|0>=1.                                (10)

Indeed L W=Q^(-1)WL and the finite Euler shift gives
P(L)W P(L)^(-1)=W(1-Q^(-1)L)=B. The product around
its clock orbit is proportional to 1-Z^N=0. Direct
commutation gives [A,L]=0. The last identity follows
because fewer than N raises from input zero cannot
return to zero. Thus this source has fixed augmentation
one, not a normalization chosen from a knot invariant.

For h<N its complete input column is

    <h|C_B|0>=p_h(Z;Q^(-1))_h,
    p_h=(-1)^hQ^(h(h-1)/2)/F_h.                 (11)

All factors and endpoint zeros in this column remain
part of the source.

## 4. The other original R factor is an exact coherent vacuum port

The original crossing has

    R_0=D P(n_-)P(n),
    n=(Q-Z^(-1))X=e_1S_2,
    n_-=-(Q-Z^(-1))a=-e_1Z_2S_2.

Set

    a_eff=Q a Z^(-1),
    e_aux=(Q-W^(-1))S^(-1), n_0=a_eff e_aux.    (12)

The auxiliary e_aux is a unit scalar times the literal
complete nilpotent raising/lowering matrix. Then exactly

    P(n_-)=<0|P(n_0)C_B|0>.                     (13)

Here the whole intermediate auxiliary sum has been
performed, not suppressed. For a finite proof, the
original Euler coefficient cancels the h-fold lowering
matrix coefficient to give

    <0|P(n_0)|h>=a_eff^h.

Together with (11), the right side of (13) is
sum_h p_h a_eff^h(Z;Q^(-1))_h. The actual physical
relations aZ=QZa imply

    n_-^h=a_eff^h(Z;Q^(-1))_h,

which proves (13) term by term. This is an exact
all-level finite q-binomial bridge from a genuine
auxiliary source to the original crossing factor.
The polarization factor a_eff=QaZ^(-1) is forced
by this calculation and is retained explicitly.

Equation (13) can be conjugated by the U of (5) on
the full extended space without changing its vacuum
port, since U_0=1. Thus the same source extension
contains both the actual third-region coordinate
ports (7) and an original-R operator port.

## 5. A full marked pentagon before the complete auxiliary contraction

Use the marked full-Phi clock on the auxiliary head,
with its fixed scalar and top lift:

    F_W=phi_N diag_j[1/F_j],
    phi_N=sqrt(N)exp{i pi[1/4-(N+N^(-1))/12]}.

Let P_0=P(n_0), H_0=P_0^(-1)WP_0, and
F_H0=P_0^(-1)F_WP_0. Exactly as in the literal middle
identity, since n_0W=QWn_0 and its missing arrow is
the actual input zero,

    P_0 F_H0^(-1)
       =F_H0^(-1)P_0 P(-n_0H_0).                (14)

Inserting (14) into (13), while retaining its interface
and source, gives the exact full physical factor

    P(n_-)=<0| U [F_H0^(-1)P_0P(-n_0H_0)
                              F_H0 C_B] U^(-1)|0>. (15)

Every intermediate auxiliary index in this product is
summed. The source F_H0 C_B|0> is not replaced by a
scalar vacuum. Its full-Phi scalar, both radial pieces
and every finite boundary current are retained.

Consequently substituting (15) for P(n_-) in the
displayed R_0 gives the ORIGINAL crossing as a matrix
identity, before choosing a cut entry or a closing
tangle. Its common Cartan/framing/peripheral line and
the original cups and caps therefore remain unchanged.
The factors phi_N in F_H0 and its inverse cancel
because those exact interfaces occur on opposite
sides in (15), not because a phase has been dropped.

Each nilpotent Euler factor can be represented by its
exact full-Psi circle/radial moment. The controlled
operator (5) is likewise a ratio of two such finite
Euler factors in n_RQ^(J_aux), with its inverse and
vacuum edge fixed. Factorial conjugations reduce
n_R to xS_1^(-1) tensor J_+ with unit coefficients;
the joint physical/auxiliary clock similarly gives
the single missing edge of L. Thus these are finite
relative full-Phi kernels with their original
coefficient sources, not bare functional substitutions.

## 6. What this proves and what still needs its face table

The extra region degree resolves the actual failure
of projective coordinate renaming: (7) comes from
an honest extended quantum torus, with an explicit
periodic source-preserving controlled transport.
The same construction has a fixed coherent vacuum
port for the actual second crossing factor, and its
complete marked pentagon still gives that original
factor after ALL auxiliary sums. This is stronger
than a coordinate compression or an equality of
unmarked generic kernels.

The precise developed geometric face-order table
linking the pentagon in (14) to all five third-
certificate flags still must be checked. In
particular A in (3) and the forced a_eff in (12)
are different typed polarization coordinates; one
cannot erase their QZ^(-1) relation. Nor can one
replace products by products of the compressed
entries (7). These are the remaining explicit face
data, not a claim that the original operator or
source comparison in (15) is conditional.

No global selected cycle, geometric intersection
degree or volume lower bound is asserted.

## 7. Exact audit

Run

    python3 experiments/audit_third_region_quantum_face_extension.py

The audit checks ten complete/wrap families through
N=6 over exact prime fields. It verifies the extended
torus and its centers, both coordinate ports, C_B's
source augmentation and clock intertwiner, the
complete physical port (13), the marked pentagon
BEFORE auxiliary contraction, and the entire original
R after (15), using the independent original E/Cartan
crossing evaluator. It never multiplies compressed
coordinates in place of the full auxiliary word.
